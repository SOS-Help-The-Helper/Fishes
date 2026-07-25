import soundfile as sf, numpy as np, sys
from scipy.signal import butter, sosfilt, sosfiltfilt
SR=48000; REG_A=130.268
DUCK=float(sys.argv[1]); DIP=float(sys.argv[2]); VT=float(sys.argv[3])
mix,_=sf.read('mix_v23.wav'); vox48,_=sf.read('ovl48.wav')
st=int(round(REG_A*SR)); L=len(mix)-st
def db(x): return 20*np.log10(np.sqrt(np.mean(x**2))+1e-12)
def active(x,h=1024,pct=60):
    m=x.mean(1) if x.ndim>1 else x; n=len(m)//h
    fr=np.sqrt(np.mean(m[:n*h].reshape(n,h)**2,axis=1))
    return 20*np.log10(fr[fr>np.percentile(fr,pct)].mean()+1e-12)
reg=mix[st:st+L].copy(); v_old=vox48[:L]
bed=np.stack([reg[:,c]-float(np.dot(reg[:,c],v_old[:,c])/np.dot(v_old[:,c],v_old[:,c]))*v_old[:,c] for c in range(2)],1)
S0=214.5; SPEECH_END=234.87; KEEP=0.80
gaps=[(214.98,215.43),(218.01,218.60),(223.40,223.61),(223.64,223.76),(223.77,224.01),
      (225.64,226.20),(227.62,228.40),(229.27,229.55),(230.54,231.30),(233.08,233.52)]
pieces=[];cur=0.0
for a,b in gaps:
    ga,gb=a-S0,b-S0
    pieces.append(vox48[int(cur*SR):int(ga*SR)]); pieces.append(np.zeros((int((gb-ga)*KEEP*SR),2))); cur=gb
pieces.append(vox48[int(cur*SR):int((SPEECH_END-S0)*SR)])
voice=sosfilt(butter(2,85,'hp',fs=SR,output='sos'),np.concatenate(pieces),axis=0)
h=256; m=voice.mean(1); n=len(m)//h
lvl=20*np.log10(np.sqrt(np.mean(m[:n*h].reshape(n,h)**2,axis=1))+1e-9)
gr=np.where(lvl>-28.0,(-28.0-lvl)*0.75,0.0)
sm=np.zeros_like(gr); aA,aR=np.exp(-1/(0.005*SR/h)),np.exp(-1/(0.12*SR/h)); p=0.0
for i,g in enumerate(gr):
    a=aA if g<p else aR; p=a*p+(1-a)*g; sm[i]=p
gl=np.repeat(10**(sm/20),h); gl=np.concatenate([gl,np.full(len(voice)-len(gl),gl[-1])])
voice*=gl[:,None]
voice=voice+0.20*sosfilt(butter(2,[1800,4500],'bp',fs=SR,output='sos'),voice,axis=0)
voice*=10**((VT-active(voice))/20)
vfull=np.zeros_like(bed); vl=min(len(voice),L); vfull[:vl]=voice[:vl]
f=int(0.12*SR); vfull[vl-f:vl]*=np.linspace(1,0,f)[:,None]
ve=np.abs(vfull.mean(1)); n=len(ve)//h
env=20*np.log10(np.sqrt(np.mean((ve[:n*h]**2).reshape(n,h),axis=1))+1e-9)
d=np.clip((env-(-45.0))/18.0,0,1)
sd=np.zeros_like(d); aA,aR=np.exp(-1/(0.025*SR/h)),np.exp(-1/(0.22*SR/h)); p=0.0
for i,g in enumerate(d):
    a=aA if g>p else aR; p=a*p+(1-a)*g; sd[i]=p
def stretch(x):
    y=np.repeat(x,h); return np.concatenate([y,np.full(L-len(y),y[-1])])[:L]
duck=stretch(10**(-DUCK*sd/20)); dip=stretch(10**(-DIP*sd/20)); spk=stretch(sd)
sb=butter(2,[1200,4500],'bp',fs=SR,output='sos')
band=sosfiltfilt(sb,bed,axis=0)
bed_d=(bed-band)*duck[:,None]+band*(duck*dip)[:,None]
out=vfull+bed_d
CEIL=0.95
pkv=np.max(np.abs(out),axis=1); nb=int(np.ceil(len(pkv)/64))
pk=np.array([pkv[i*64:(i+1)*64].max() for i in range(nb)])
need=np.minimum(1.0,CEIL/(pk+1e-9)); g=np.ones_like(need); cur=1.0
aA,aR=np.exp(-1/(0.0015*SR/64)),np.exp(-1/(0.10*SR/64))
for i,v in enumerate(need):
    a=aA if v<cur else aR; cur=a*cur+(1-a)*v; g[i]=min(cur,v)
gg=np.repeat(g,64)[:len(out)]
out=np.clip(out*gg[:,None],-CEIL,CEIL)
sp=spk>0.5
gapmask=spk<0.15
bv=sosfiltfilt(sb,vfull,axis=0); bb=sosfiltfilt(sb,bed_d,axis=0)
print(f'DUCK{DUCK} DIP{DIP} VT{VT}')
print('  music at full recovery:',round(db(bed_d[gapmask]),1) if gapmask.sum()>2000 else 'n/a','   unducked bed:',round(db(bed),1))
print('  voice / bed (broad) :',round(db(vfull[sp]),1),'/',round(db(bed_d[sp]),1),'=>',round(db(vfull[sp])-db(bed_d[sp]),1),'dB clear')
print('  voice / bed (1-4kHz):',round(db(bv[sp]),1),'/',round(db(bb[sp]),1),'=>',round(db(bv[sp])-db(bb[sp]),1),'dB clear')
print('  section rms',round(db(out),1),' peak',round(20*np.log10(np.abs(out).max()),2))
new=mix.copy(); new[st:st+L]=out
xf=int(0.02*SR); w=np.linspace(0,1,xf)[:,None]
new[st:st+xf]=mix[st:st+xf]*(1-w)+out[:xf]*w
sf.write('mix_v24.wav',new,SR)

import soundfile as sf, numpy as np
from scipy.signal import butter, sosfilt, sosfiltfilt, resample_poly

SR=48000
SRC_A, SRC_END = 212.52, 234.87      # full "for what is our mission in life but to love and serve" -> "...force when you're together"
VOX_END_TL     = 149.752             # where his last word lands in the timeline
OLD_VOX_TL     = 130.268             # where the previous (buried) officiant track sat
DUCK, DIP, VT  = 10.0, 4.0, -12.0
KEEP           = 0.80

mix,_=sf.read('mix_v23.wav')          # v23 = last version before the voice was touched
vox_old,_=sf.read('ovl48.wav')
def db(x): return 20*np.log10(np.sqrt(np.mean(x**2))+1e-12)
def active(x,h=1024,pct=60):
    m=x.mean(1) if x.ndim>1 else x; n=len(m)//h
    fr=np.sqrt(np.mean(m[:n*h].reshape(n,h)**2,axis=1))
    return 20*np.log10(fr[fr>np.percentile(fr,pct)].mean()+1e-12)

# ---------- 1. dry officiant, straight from the isolated vocal stem ----------
stem,ssr=sf.read('stems/htdemucs/audio_full/vocals.wav')
dry=stem[int(SRC_A*ssr):int(SRC_END*ssr)]
dry=resample_poly(dry,SR,ssr,axis=0)

# tighten his pauses so the whole line fits without rushing his delivery
gaps=[(214.98,215.43),(218.01,218.60),(223.40,223.61),(223.64,223.76),(223.77,224.01),
      (225.64,226.20),(227.62,228.40),(229.27,229.55),(230.54,231.30),(233.08,233.52)]
pieces=[];cur=0.0
for a,b in gaps:
    ga,gb=a-SRC_A,b-SRC_A
    pieces.append(dry[int(cur*SR):int(ga*SR)])
    pieces.append(np.zeros((int((gb-ga)*KEEP*SR),2)))
    cur=gb
pieces.append(dry[int(cur*SR):])
voice=np.concatenate(pieces)
print('retimed voice', round(len(voice)/SR,3),'s')

# ---------- 2. voice chain ----------
voice=sosfilt(butter(2,85,'hp',fs=SR,output='sos'),voice,axis=0)
h=256; m=voice.mean(1); n=len(m)//h
lvl=20*np.log10(np.sqrt(np.mean(m[:n*h].reshape(n,h)**2,axis=1))+1e-9)
gr=np.where(lvl>-28.0,(-28.0-lvl)*0.75,0.0)
sm=np.zeros_like(gr); aA,aR=np.exp(-1/(0.005*SR/h)),np.exp(-1/(0.12*SR/h)); p=0.0
for i,g in enumerate(gr):
    a=aA if g<p else aR; p=a*p+(1-a)*g; sm[i]=p
gl=np.repeat(10**(sm/20),h); gl=np.concatenate([gl,np.full(len(voice)-len(gl),gl[-1])])
voice*=gl[:,None]
voice=voice+0.20*sosfilt(butter(2,[1800,4500],'bp',fs=SR,output='sos'),voice,axis=0)

# light room so he sits in the space rather than on top of it
rng=np.random.default_rng(7)
ir_len=int(0.38*SR); t=np.arange(ir_len)/SR
ir=rng.normal(0,1,(ir_len,2))*np.exp(-t/0.11)[:,None]
ir[:int(0.012*SR)]=0
ir=sosfilt(butter(2,[250,6000],'bp',fs=SR,output='sos'),ir,axis=0)
ir/=np.sqrt((ir**2).sum(0))[None,:]
N=len(voice)+ir_len
wet=np.stack([np.convolve(voice[:,c],ir[:,c])[:N] for c in range(2)],1)
wet=np.pad(wet,((0,N-len(wet)),(0,0)))
voice=np.pad(voice,((0,ir_len),(0,0)))[:N]+0.16*wet
voice*=10**((VT-active(voice))/20)

# ---------- 3. place it, extending the rebuild region back over the pre-lap ----------
VOX_START_TL = VOX_END_TL - len(voice)/SR
REG_A = min(OLD_VOX_TL, VOX_START_TL) - 0.5
st=int(round(REG_A*SR)); L=len(mix)-st
print('voice starts at timeline', round(VOX_START_TL,3),'  (was 130.268) -> pre-lap of',
      round(OLD_VOX_TL-VOX_START_TL,2),'s over the dissolve')

# bed: mix as-is, minus the old buried voice wherever it used to sit
bed=mix[st:st+L].copy()
o=int(round((OLD_VOX_TL-REG_A)*SR)); ov=vox_old[:L-o]
for c in range(2):
    g=float(np.dot(bed[o:o+len(ov),c],ov[:,c])/np.dot(ov[:,c],ov[:,c]))
    bed[o:o+len(ov),c]-=g*ov[:,c]
print('bed recovered at', round(db(bed),1),'dB')

vfull=np.zeros_like(bed)
vs=int(round((VOX_START_TL-REG_A)*SR))
vl=min(len(voice),L-vs); vfull[vs:vs+vl]=voice[:vl]
f=int(0.12*SR); vfull[vs+vl-f:vs+vl]*=np.linspace(1,0,f)[:,None]

# ---------- 4. duck the bed under him ----------
ve=np.abs(vfull.mean(1)); n=len(ve)//h
env=20*np.log10(np.sqrt(np.mean((ve[:n*h]**2).reshape(n,h),axis=1))+1e-9)
d=np.clip((env-(-45.0))/18.0,0,1)
sd=np.zeros_like(d); aA,aR=np.exp(-1/(0.025*SR/h)),np.exp(-1/(0.22*SR/h)); p=0.0
for i,g in enumerate(d):
    a=aA if g>p else aR; p=a*p+(1-a)*g; sd[i]=p
def stretch(x):
    y=np.repeat(x,h); return np.concatenate([y,np.full(max(0,L-len(y)),y[-1])])[:L]
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

sp=spk>0.5; gapm=spk<0.15
bv=sosfiltfilt(sb,vfull,axis=0); bb=sosfiltfilt(sb,bed_d,axis=0)
print('  music at full recovery:',round(db(bed_d[gapm]),1),' unducked',round(db(bed),1))
print('  voice/bed broad :',round(db(vfull[sp])-db(bed_d[sp]),1),'dB clear')
print('  voice/bed 1-4kHz:',round(db(bv[sp])-db(bb[sp]),1),'dB clear')

new=mix.copy(); new[st:st+L]=out
xf=int(0.02*SR); w=np.linspace(0,1,xf)[:,None]
new[st:st+xf]=mix[st:st+xf]*(1-w)+out[:xf]*w
sf.write('mix_v25.wav',new,SR)
print('  party 110-125:',round(db(new[110*SR:125*SR]),1),' officiant 133-146:',round(db(new[133*SR:146*SR]),1))
print('  peak',round(20*np.log10(np.abs(new).max()),2),'dBFS  duration',round(len(new)/SR,3))

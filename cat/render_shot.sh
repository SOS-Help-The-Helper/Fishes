#!/bin/bash
# Usage: shot.sh <name> <src_start> <src_dur> <out_dur> <z0> <z1> <px> <py>
set -e
SRC=/root/.claude/uploads/9ebe7e9d-9915-529f-bba8-f8491735ee3b/a33c1b9a-80664450236__F323C62298054892A4B2182B9D313133.mov
N=$1; SS=$2; SD=$3; OD=$4; Z0=$5; Z1=$6; PX=$7; PY=$8
FR=$(python3 -c "print(int(round($OD*30)))")
SPEED=$(python3 -c "print(round($OD/$SD,4))")

# zoompan: input 2160x3840 -> output 1080x1920.  z=0.5 is full frame.
Z="0.5*($Z0+($Z1-$Z0)*on/$FR)"
X="$PX*(iw*zoom)-(ow/2)"
Y="$PY*(ih*zoom)-(oh/2)"

ffmpeg -v error -ss $SS -t $SD -i "$SRC" -an -vf "\
zscale=t=linear:npl=88,format=gbrpf32le,zscale=p=bt709,tonemap=mobius:param=0.3:desat=0,zscale=t=bt709:m=bt709:r=tv,format=yuv420p,\
hqdn3d=2:3:5:7,\
minterpolate=fps=120:mi_mode=mci:mc_mode=aobmc:me_mode=bidir:vsbmc=1,\
setpts=${SPEED}*PTS,fps=30,\
scale=2160:3840:flags=lanczos,\
unsharp=5:5:1.0:5:5:0.3,cas=0.5,\
eq=contrast=1.16:brightness=0.0:saturation=1.18:gamma=1.02,\
colorbalance=rs=-0.02:bs=0.05:bm=0.01:rh=0.04:bh=-0.02,\
curves=all='0/0.02 0.25/0.21 0.75/0.78 1/0.96',\
split[a][b];[b]curves=all='0/0 0.62/0 1/1',gblur=sigma=30[bl];[a][bl]blend=all_mode=screen:all_opacity=0.22,\
zoompan=z='${Z}':x='${X}':y='${Y}':d=1:s=1080x1920:fps=30,\
vignette=PI/5,\
noise=alls=5:allf=t+u,\
trim=end_frame=${FR},setpts=PTS-STARTPTS,format=yuv420p" \
 -c:v libx264 -crf 13 -preset medium -r 30 "shot_${N}.mp4" -y
echo "DONE $N $(ffprobe -v error -show_entries stream=nb_frames,duration -of csv=p=0 shot_${N}.mp4)"

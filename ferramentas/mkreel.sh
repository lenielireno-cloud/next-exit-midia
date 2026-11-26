#!/bin/bash
# mkreel.sh nome  -> Reel_nome.mp4
k=$1; W=/home/claude/work; M=/home/claude/musica
python3 $W/render.py $W/reel_$k.html /tmp/rv_$k.mp4 || exit 1
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 /tmp/rv_$k.mp4)
if [[ $k == frase_* ]]; then
  EV="pop@0.4,pop@2.2,tick@6.8,tick@8.6,tick@10.4,ding@14.6,whoosh@19.9"; TR=$M/quiz_trilha.wav
else
  N=12; EV="pop@1.4,whoosh@3.5"; for i in $(seq 0 11); do EV="$EV,pop@$(python3 -c "print(round(3.6+$i*1.9,2))"),ding@$(python3 -c "print(round(3.6+$i*1.9+0.9,2))")"; done; EV="$EV,whoosh@$(python3 -c "print(round(3.6+12*1.9+3.4,2))")"
  TR=$M/feliz$(( (RANDOM % 3) + 1 )).wav
fi
python3 $W/sfx.py /tmp/rv_$k.mp4 /tmp/rs_$k.mp4 $D "$EV" && ffmpeg -loglevel error -y -i /tmp/rs_$k.mp4 -stream_loop -1 -i $TR -filter_complex "[1:a]volume=0.28,afade=t=out:st=$(python3 -c "print($D-1.5)"):d=1.5,aformat=channel_layouts=stereo,aresample=44100[m];[0:a][m]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 160k -t $D $W/Reel_$k.mp4 && echo "ok $k $D"

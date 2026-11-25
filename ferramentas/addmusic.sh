#!/bin/bash
# addmusic.sh in.mp4 out.mp4 track.wav  (música baixinha por baixo do áudio existente)
D=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$1")
ffmpeg -loglevel error -y -i "$1" -stream_loop -1 -i "$3" -filter_complex "[1:a]volume=0.22,afade=t=out:st=$(python3 -c "print(max(0,$D-1.5))"):d=1.5,aformat=channel_layouts=stereo,aresample=44100[m];[0:a][m]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 160k -t $D "$2"

import sys,json,subprocess,wave,os
# voice.py in.mp4 out.mp4 lines.json   lines: [[start,voice,text,maxdur],...]
V={'leo':'pt_BR-cadu-medium','m':'en_US-ryan-high','f':'en_US-amy-medium','m2':'en_US-joe-medium'}
D=os.path.dirname(os.path.abspath(__file__))
vin,vout,lines=sys.argv[1],sys.argv[2],json.load(open(sys.argv[3]))
tmp='/tmp/vo';os.makedirs(tmp,exist_ok=True)
args=['ffmpeg','-y','-loglevel','error','-i',vin];fc=['[0:a]volume=0.55[s]'];labs=['[s]']
for i,(st,v,txt,mx) in enumerate(lines):
    f=f'{tmp}/{i}.wav'
    subprocess.run(['python3','-m','piper','-m',f'{D}/{V[v]}.onnx','-f',f],input=txt.encode(),stderr=subprocess.DEVNULL,check=True)
    with wave.open(f) as w: d=w.getnframes()/w.getframerate()
    tempo=max(1.0,min(1.3,d/mx)) if mx else 1.0
    if mx and d/tempo>mx+0.05: print(f'WARN line {i} {d:.2f}s > {mx}s')
    args+=['-i',f];ms=int(st*1000)
    fc.append(f'[{i+1}]atempo={tempo:.3f},aresample=44100,aformat=channel_layouts=stereo,volume=1.6,adelay={ms}|{ms}[v{i}]');labs.append(f'[v{i}]')
fc.append(''.join(labs)+f'amix=inputs={len(labs)}:normalize=0,alimiter=limit=0.95[a]')
args+=['-filter_complex',';'.join(fc),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','160k',vout]
subprocess.run(args,check=True);print('ok',vout)

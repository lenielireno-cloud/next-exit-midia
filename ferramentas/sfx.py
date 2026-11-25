import sys,subprocess
# usage: sfx.py video.mp4 out.mp4 dur "kind@t,kind@t"
v,out,dur,ev=sys.argv[1],sys.argv[2],float(sys.argv[3]),sys.argv[4]
src={'tick':'sine=f=1400:d=0.05','ding':'sine=f=880:d=0.6','whoosh':'anoisesrc=d=0.5:c=pink:a=0.4','pop':'sine=f=620:d=0.08','type':'anoisesrc=d=0.03:c=white:a=0.25'}
flt={'tick':'volume=0.5','ding':'afade=t=out:st=0.1:d=0.5,volume=0.6','whoosh':'afade=t=in:d=0.25,afade=t=out:st=0.25:d=0.25,highpass=f=800','pop':'volume=0.35','type':'highpass=f=2000,volume=0.5'}
evs=[(e.split('@')[0],float(e.split('@')[1])) for e in ev.split(',') if e]
args=['ffmpeg','-y','-loglevel','error','-i',v];fc=[];labs=[]
for i,(k,t) in enumerate(evs):
    args+=['-f','lavfi','-i',src[k]];ms=int(t*1000)
    fc.append(f'[{i+1}]{flt[k]},aformat=sample_rates=44100:channel_layouts=stereo,adelay={ms}|{ms}[e{i}]');labs.append(f'[e{i}]')
fc.append(''.join(labs)+f'amix=inputs={len(labs)}:normalize=0,apad[a]')
args+=['-filter_complex',';'.join(fc),'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-t',str(dur),out]
subprocess.run(args,check=True)

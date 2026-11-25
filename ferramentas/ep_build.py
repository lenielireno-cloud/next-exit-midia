import json,subprocess,wave,sys,os
# Builds timeline + narration audio for a "Léo mostra o app" episode. Usage: ep_build.py ep.json outprefix
V={'leo':'pt_BR-cadu-medium','m':'en_US-ryan-high','f':'en_US-amy-medium','m2':'en_US-joe-medium'}
VD='/home/claude/voz'
cfg=json.load(open(sys.argv[1])); out=sys.argv[2]; tmp=out+'_vo'; os.makedirs(tmp,exist_ok=True)
def tts(txt,v,i,ls=None):
    f=f'{tmp}/{i}.wav'; a=['python3','-m','piper','-m',f'{VD}/{V[v]}.onnx','-f',f]
    if ls: a+=['--length-scale',str(ls)]
    subprocess.run(a,input=txt.encode(),stderr=subprocess.DEVNULL,check=True)
    with wave.open(f) as w: return f,w.getnframes()/w.getframerate()
t=0.4; clips=[]; TL={'lesson':cfg['lesson'],'lines':cfg['lines'],'ev':[]}; n=0
def say(txt,v='leo',gap=0.25):
    global t,n
    f,d=tts(txt,v,n,0.88 if v=='leo' else None); n+=1; clips.append((t,f)); s=t; t+=d+gap; return s,d
for step in cfg['steps']:
    k=step['k']
    if k=='intro':   # Léo talking, with captions
        s,d=say(step['say']); TL['ev'].append({'k':'intro','s':s,'e':t,'cap':step.get('cap','')})
    elif k=='zoom':
        TL['ev'].append({'k':'zoom','s':t,'e':t+0.9}); t+=0.9
    elif k=='type':  # type line i, optional narration over it
        i=step['i']; L=cfg['lines'][i]['en']; s=t; dt=len(L)/14+0.4
        if step.get('say'): _,d=say(step['say'],gap=0); t=s
        else: d=0
        dur=max(dt,d+0.3); TL['ev'].append({'k':'type','i':i,'s':s,'e':s+dur,'typo':step.get('typo'),'sub':step.get('say','')}); t=s+dur+0.2
        if step.get('listen',True):
            TL['ev'].append({'k':'tap','i':i,'s':t,'e':t+0.6}); t+=0.5
            s2,d2=say(cfg['lines'][i]['en'],cfg['lines'][i].get('v','m'),gap=0.4); TL['ev'].append({'k':'listen','i':i,'s':s2,'e':s2+d2})
    elif k=='done':
        s,d=say(step['say']); TL['ev'].append({'k':'done','s':s,'e':t,'sub':step['say']})
    elif k=='outro':
        s,d=say(step['say']); TL['ev'].append({'k':'outro','s':s,'e':t,'cap':step.get('cap','')})
    elif k=='end':
        s,d=say(step['say'],gap=1.2); TL['ev'].append({'k':'end','s':s,'e':t})
TL['dur']=round(t,2)
open(out+'_tl.js','w').write('window.TL='+json.dumps(TL,ensure_ascii=False)+';')
# narration track
a=['ffmpeg','-y','-loglevel','error'];fc=[];lab=''
for j,(s,f) in enumerate(clips):
    a+=['-i',f];ms=int(s*1000);fc.append(f'[{j}]aresample=44100,aformat=channel_layouts=stereo,adelay={ms}|{ms}[c{j}]');lab+=f'[c{j}]'
fc.append(lab+f'amix=inputs={len(clips)}:normalize=0,volume=1.5,apad=whole_dur={t}[a]')
a+=['-filter_complex',';'.join(fc),'-map','[a]','-t',str(t),out+'_voz.wav'];subprocess.run(a,check=True)
print('dur',TL['dur'])

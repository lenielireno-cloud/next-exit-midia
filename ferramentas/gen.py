import numpy as np, wave, sys
import os
SR=44100; BPM=int(os.environ.get('BPM',112)); TR=int(os.environ.get('TR',0)); np.random.seed(int(os.environ.get('SEED',1))); beat=60/BPM; dur=float(sys.argv[2]) if len(sys.argv)>2 else 32
N=int(SR*dur); out=np.zeros(N)
def note(f,t,l,amp,kind='mar'):
    n=int(l*SR); tt=np.arange(n)/SR
    if kind=='mar': w=(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*f*4*tt)*np.exp(-tt*30))*np.exp(-tt*6)
    elif kind=='bass': w=np.sin(2*np.pi*f*tt)*np.exp(-tt*3)*np.minimum(1,tt*80)
    elif kind=='pad': w=(np.sin(2*np.pi*f*tt)+0.5*np.sin(2*np.pi*f*2.005*tt))*np.minimum(1,tt*4)*np.exp(-tt*0.8)
    elif kind=='hat': w=np.random.randn(n)*np.exp(-tt*60)
    elif kind=='kick': w=np.sin(2*np.pi*(50+90*np.exp(-tt*25))*tt)*np.exp(-tt*9)
    s=int(t*SR); e=min(N,s+n); 
    if s<N: out[s:e]+=amp*w[:e-s]
hz=lambda m:440*2**((m+TR-69)/12)
P={'a':[[60,64,67],[55,59,62],[57,60,64],[53,57,60]],'b':[[60,64,67],[57,60,64],[53,57,60],[55,59,62]],'c':[[53,57,60],[55,59,62],[60,64,67],[60,64,67]]}
prog=P[os.environ.get('PROG','a')]
mel=[76,74,72,74,76,76,76,None, 74,74,74,None,76,79,79,None, 76,74,72,74,76,76,76,76, 74,74,76,74,72,None,None,None]
bar=4*beat; t=0; i=0
while t<dur:
    ch=prog[i%4]
    note(hz(ch[0]-24),t,bar,0.35,'bass'); note(hz(ch[0]-24),t+2*beat,bar/2,0.3,'bass')
    for k in range(8): note(hz(ch[k%3]+12),t+k*beat/2,0.5,0.12,'mar')
    for c in ch: note(hz(c),t,bar,0.04,'pad')
    for k in range(4): note(0,t+k*beat,0.1,0.35,'kick') if k%2==0 else None; note(0,t+k*beat+beat/2,0.05,0.05,'hat')
    if (i//4)%2==1:
        for k in range(8):
            m=mel[(i%4)*8+k]
            if m: note(hz(m),t+k*beat/2,0.6,0.16,'mar')
    t+=bar; i+=1
fade=int(1.5*SR); out[-fade:]*=np.linspace(1,0,fade); out[:int(0.3*SR)]*=np.linspace(0,1,int(0.3*SR))
out=out/np.max(np.abs(out))*0.8
with wave.open(sys.argv[1],'w') as w: w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes())

import numpy as np, wave, sys
# trilha de quiz: suspense na contagem (6.8–12.4), rufar (12.4–14.6), alegre depois da resposta
SR=44100; D=float(sys.argv[2]); N=int(SR*D); out=np.zeros(N)
def add(s,w,a):
    i=int(s*SR); e=min(N,i+len(w)); out[i:e]+=a*w[:e-i]
t=lambda l:np.arange(int(l*SR))/SR
hz=lambda m:440*2**((m-69)/12)
# drone grave + pulso tipo coração, 0–12.4
tt=t(12.4); add(0,np.sin(2*np.pi*hz(38)*tt)*np.minimum(1,tt/2)*(0.6+0.4*np.sin(2*np.pi*0.5*tt)),0.35)
add(0,(np.sin(2*np.pi*hz(50)*tt)+np.sin(2*np.pi*hz(51)*tt))*np.minimum(1,tt/4),0.06)
for k in np.arange(0,12.4,60/90):
    p=t(0.18); add(k,np.sin(2*np.pi*55*p)*np.exp(-p*25),0.5); add(k+0.18,np.sin(2*np.pi*50*p)*np.exp(-p*30),0.3)
# ostinato tenso subindo (cromático) na contagem
for j,k in enumerate(np.arange(5.4,12.4,0.25)):
    p=t(0.2); f=hz(62+(j//4)); add(k,np.sin(2*np.pi*f*p)*np.exp(-p*12),0.12)
# rufar 12.4–14.6 crescendo
for k in np.arange(12.4,14.6,0.04):
    p=t(0.05); add(k,np.random.randn(len(p))*np.exp(-p*60),0.05+0.15*(k-12.4)/2.2)
# acorde de resolução 14.6
p=t(2.5)
for m in (60,64,67,72): add(14.6,(np.sin(2*np.pi*hz(m)*p)+0.3*np.sin(2*np.pi*hz(m)*3*p)*np.exp(-p*8))*np.exp(-p*1.5),0.12)
out=out/np.max(np.abs(out))*0.8
with wave.open(sys.argv[1],'w') as w: w.setnchannels(1);w.setsampwidth(2);w.setframerate(SR);w.writeframes((out*32767).astype(np.int16).tobytes())

// Generic lesson reel. Needs window.L config.
function diner(t){
  return `<div style="position:absolute;left:0;right:0;top:640px;height:900px;background:linear-gradient(#fbe3c4,#f5d0a0)"></div>
  <div style="position:absolute;left:0;right:0;top:640px;height:60px;background:repeating-linear-gradient(90deg,${R} 0 60px,#fff 60px 120px)"></div>
  <div style="position:absolute;left:60px;top:760px;width:300px;height:200px;background:#cfe8f5;border:10px solid #8a5a3a;border-radius:10px"></div>
  <div style="position:absolute;left:400px;top:770px;font:900 60px Overpass;color:${R};text-shadow:0 0 18px #ff9">DINER</div>`;
}
function table(t,items=''){return `<div style="position:absolute;left:140px;top:1290px;width:800px;height:40px;background:#c94a3a;border:5px solid ${INK};border-radius:10px"></div>
  <div style="position:absolute;left:500px;top:1330px;width:60px;height:220px;background:#999;border:5px solid ${INK}"></div>${items}`}
function render(t){
  const S=L.s; let h=brand(L.tag);
  if(t<S.q){ h+=L.hook(t) }
  else if(t<S.type){
    if(L.kind==='A'){
      h+=cap(t,S.q,'Saberia falar isso em inglês? 🤔',260,66);
      h+=`<div class="card" style="top:560px;text-align:center;opacity:${io(t,S.q+0.6)};transform:scale(${pop(io(t,S.q+0.6))})"><div style="font:800 40px Brico;color:#5E6E67">🇧🇷 Em português</div><div style="font:800 70px/1.2 Brico;margin-top:14px">${L.pt}</div></div>`;
      const r=io(t,S.rev,0.4);
      h+=`<div class="card" style="top:960px;text-align:center;opacity:${r};transform:scale(${pop(r)});border:6px solid ${G}"><div style="font:800 40px Brico;color:${G}">🇺🇸 Em inglês</div><div style="font:700 62px/1.25 Mono;margin-top:14px;color:${G}">${L.en}</div></div>`;
    } else {
      h+=cap(t,S.q,L.qcap,240,60);
      h+=`<div class="card" style="top:460px;text-align:center;opacity:${io(t,S.q+0.3)}"><div style="font:700 62px/1.25 Mono">“${L.ask}”</div><div style="font:700 44px Atk;color:${B};margin-top:14px">${L.askpt}</div></div>`;
      h+=cap(t,S.q+1,'Saberia responder? ⏳',820,64,R);
      const r=io(t,S.rev,0.4);
      h+=`<div class="card" style="top:980px;opacity:${r};transform:scale(${pop(r)});border:6px solid ${G}">${L.answers.map(a=>`<div style="display:flex;justify-content:space-between;gap:20px;padding:10px 0;border-bottom:2px solid #eee"><span style="font:700 44px Mono;color:${G}">${a[0]}</span><span style="font:700 38px Atk;color:${B};text-align:right">${a[1]}</span></div>`).join('')}</div>`;
    }
  } else if(t<S.tip){
    h+=cap(t,S.type,'Agora pratica no app 👇',210,60);
    const lines=L.lines, ci=L.typeLine, n=lines[ci].en.length, prog=C(0,n,(t-S.type-1)*13);
    const doneA=t>S.tip-1.8?io(t,S.tip-1.8,0.4):0;
    h+=phone(t,150,320,1.5,L.title,lines,prog>=n&&doneA?ci+1:ci,prog,{typo:{i:ci,at:6,len:3},done:doneA});
  } else if(t<S.end){
    h+=cap(t,S.tip,L.tipTitle,300,72);
    h+=`<div class="card" style="top:560px;opacity:${io(t,S.tip+0.5)}"><div style="font:700 50px/1.4 Atk">${L.tip}</div></div>`;
    h+=cap(t,S.tip+2.2,'O que acha de praticar no tempo ocioso?<br><span style="color:#0B6B47">5 minutos fazem diferença no seu dia!</span>',1180,54);
  } else h=endcard(t,S.end);
  document.getElementById('root').innerHTML=h;
}

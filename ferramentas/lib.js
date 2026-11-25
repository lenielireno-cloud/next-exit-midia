// Shared helpers for Next Exit videos (1080x1920)
const C=(a,b,x)=>Math.max(a,Math.min(b,x));
const io=(t,s,d=0.4)=>C(0,1,(t-s)/d);
const ease=x=>1-Math.pow(1-x,3);
const pop=x=>{x=C(0,1,x);return x<1?(1+0.25*Math.sin(x*Math.PI))*ease(x):1};
const G='#0B6B47',Y='#FFC21A',B='#2C4A9A',R='#E5482F',INK='#13201B';
const brand=(tag)=>`<div class="sign"><small>NEXT EXIT</small>English ↗</div>${tag?`<div class="tag">${tag}</div>`:''}`;

// Flat character. o:{skin,hair,hairStyle:'short'|'curly'|'bald',shirt,pants,cap,apron,band,talk,wave,glasses}
function person(o,t,x,y,h=640,flip=false){
  const k=o.skin||'#F1C9A5', bob=Math.sin(t*3+(o.ph||0))*3;
  const mouthOpen=o.talk?Math.abs(Math.sin(t*14)):0;
  const blink=((t+(o.ph||0))%3.2)<0.12;
  const arm=o.wave?(-60+25*Math.sin(t*8)):10;
  let hair='';
  if(o.hairStyle==='curly') hair=`<g fill="${o.hair}">${[[60,62,34],[100,48,38],[140,62,34],[50,100,28],[150,100,28],[78,46,26],[122,46,26]].map(c=>`<circle cx="${c[0]}" cy="${c[1]}" r="${c[2]}"/>`).join('')}</g>`;
  else if(o.hairStyle==='bald') hair=`<path d="M58 92 q-4 -20 10 -26 M142 92 q4 -20 -10 -26" stroke="#bbb" stroke-width="10" fill="none"/>`;
  else hair=`<path d="M56 96 q-2 -52 44 -54 q46 2 44 54 q-10 -26 -44 -28 q-34 2 -44 28z" fill="${o.hair||'#222'}"/>`;
  const cap=o.cap?`<path d="M54 82 q0 -46 46 -46 q46 0 46 46z" fill="#1F3A7A" stroke="${INK}" stroke-width="4"/><circle cx="84" cy="62" r="4" fill="#fff"/><circle cx="100" cy="54" r="4" fill="#fff"/><circle cx="116" cy="62" r="4" fill="#fff"/><path d="M96 82 h70 q6 0 2 8 h-72z" fill="${R}" stroke="${INK}" stroke-width="4"/>`:'';
  const band=o.band?`<path d="M58 70 q42 -22 84 0" stroke="${R}" stroke-width="10" fill="none"/>`:'';
  const glasses=o.glasses?`<g fill="none" stroke="${INK}" stroke-width="4"><circle cx="84" cy="104" r="12"/><circle cx="116" cy="104" r="12"/><path d="M96 104h8"/></g>`:'';
  const apron=o.apron?`<path d="M70 200 h60 l8 150 h-76z" fill="#fff" stroke="${INK}" stroke-width="4"/>`:'';
  const strap=o.strap?`<path d="M66 190 L132 300" stroke="${Y}" stroke-width="12"/>`:'';
  const item=o.item||'';
  return `<svg viewBox="0 0 200 460" style="position:absolute;left:${x}px;top:${y+bob}px;height:${h}px;overflow:visible;transform:${flip?'scaleX(-1)':''}" >
  <g stroke="${INK}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round">
   <rect x="68" y="330" width="28" height="110" rx="10" fill="${o.pants||'#3B5BA5'}"/><rect x="104" y="330" width="28" height="110" rx="10" fill="${o.pants||'#3B5BA5'}"/>
   <ellipse cx="80" cy="444" rx="22" ry="10" fill="#333"/><ellipse cx="120" cy="444" rx="22" ry="10" fill="#333"/>
   <path d="M56 186 q44 -24 88 0 l6 156 h-100z" fill="${o.shirt||G}"/>
   <g transform="rotate(${-arm} 142 196)"><rect x="138" y="190" width="24" height="110" rx="12" fill="${o.shirt||G}"/><circle cx="150" cy="306" r="14" fill="${k}"/></g>
   <rect x="38" y="190" width="24" height="110" rx="12" fill="${o.shirt||G}"/><circle cx="50" cy="306" r="14" fill="${k}"/>
   <rect x="88" y="150" width="24" height="30" fill="${k}"/>
   <ellipse cx="100" cy="102" rx="46" ry="54" fill="${k}"/>
  </g>
  ${apron}${strap}${hair}${band}${cap}${glasses}
  ${o.mustache?`<path d="M86 128 q14 -8 28 0" stroke="#999" stroke-width="7" fill="none"/>`:''}
  <g fill="${INK}">${blink?`<rect x="78" y="102" width="12" height="3"/><rect x="110" y="102" width="12" height="3"/>`:`<circle cx="84" cy="104" r="6"/><circle cx="116" cy="104" r="6"/>`}</g>
  <ellipse cx="100" cy="134" rx="${10}" ry="${2+mouthOpen*9}" fill="#7a2a20" stroke="${INK}" stroke-width="3"/>
  ${item}
  </svg>`;
}
const LEO={skin:'#F6D2B4',hair:'#6b4a2b',cap:1,shirt:G,strap:1,pants:'#3B5BA5'};
const YURI={skin:'#B97A50',hair:'#1c1c1c',shirt:G,pants:'#3B5BA5',ph:1};
const JHENE={skin:'#7A4A2E',hair:'#2a1a12',hairStyle:'curly',band:1,shirt:Y,pants:'#2C4A9A',ph:2};
const CAIO={skin:'#B97A50',hair:'#111',shirt:G,apron:1,pants:'#333',ph:0.5};
const MAYA={skin:'#E8B48A',hair:'#5a3315',hairStyle:'curly',shirt:Y,apron:1,pants:'#333',ph:1.7};

// Speech balloon with EN + PT
function balloon(t,s,x,y,w,name,en,pt,tail='left'){
  const a=io(t,s,0.3);
  return `<div style="position:absolute;left:${x}px;top:${y}px;width:${w}px;transform:scale(${pop(a)});transform-origin:${tail==='left'?'10% 100%':'90% 100%'};opacity:${a};
   background:#fff;border:5px solid ${INK};border-radius:30px;padding:26px 30px 24px">
   <span style="position:absolute;top:-24px;left:24px;background:${G};color:#fff;font:800 28px Brico;padding:4px 16px;border-radius:10px">${name}</span>
   <div style="font:800 44px/1.2 Brico;color:${INK}">${en}</div>${pt?`<div style="font:700 36px/1.25 Atk;color:${B};margin-top:8px">${pt}</div>`:''}
   <div style="position:absolute;bottom:-28px;${tail}:60px;width:0;height:0;border-left:22px solid transparent;border-right:22px solid transparent;border-top:28px solid ${INK}"></div></div>`;
}
const cap=(t,s,txt,top=260,size=64,col=INK)=>{const a=io(t,s);return `<div class="abs big" style="top:${top}px;font-size:${size}px;color:${col};opacity:${a};transform:translateY(${(1-ease(a))*30}px)">${txt}</div>`};

// Phone with the app's lesson screen. lines:[{who,en,pt}], cur: index typing, prog: chars typed; typo: {i,at,len}
function phone(t,x,y,sc,title,lines,cur,prog,opts={}){
  const rows=lines.map((l,i)=>{
    let en;
    if(i<cur) en=`<span style="color:#137A3E">${l.en}</span>`;
    else if(i===cur){
      const n=Math.floor(prog); let typed=l.en.slice(0,n);
      if(opts.typo&&opts.typo.i===i&&n>=opts.typo.at&&n<opts.typo.at+opts.typo.len){typed=l.en.slice(0,opts.typo.at)+`<span style="color:#C2352B;background:#f6d6d3">${l.en[opts.typo.at]==='x'?'z':'x'}</span>`}
      else typed=`<span style="color:#137A3E">${typed}</span>`;
      en=typed+`<span style="color:#13201B;opacity:${Math.floor(t*2.5)%2}">|</span><span style="color:#9AA8A2">${n<l.en.length?l.en.slice(n):''}</span>`;
    } else en=`<span style="color:#9AA8A2">${l.en}</span>`;
    const ptShow=i<cur||(i===cur&&prog>=l.en.length*0.35);
    const ptv=i===cur?l.pt.slice(0,Math.floor(l.pt.length*C(0,1,(prog/l.en.length-0.35)/0.65))):l.pt;
    return `<div style="padding:18px 22px;border-bottom:1px solid #D7DFDB;background:${i===cur?'#fff':'transparent'}">
      <span style="font:700 19px Mono;letter-spacing:.06em;text-transform:uppercase;color:${l.who==='Você'?G:'#5E6E67'}">${l.who}</span>
      <div style="font:700 33px/1.35 Mono;margin-top:6px">${en}</div>
      <div style="font:700 27px Atk;color:${B};min-height:34px;margin-top:4px">${ptShow?(i===cur?ptv:l.pt):''}</div></div>`}).join('');
  const done=opts.done?`<div style="position:absolute;left:30px;right:30px;top:300px;background:${G};border:6px solid #fff;outline:3px solid ${G};border-radius:20px;color:#fff;text-align:center;padding:30px;transform:scale(${pop(opts.done)})">
     <div style="font:900 44px Overpass">Lição concluída ✓</div><div style="font:700 26px Atk;margin-top:8px">+10 ★</div></div>`:'';
  return `<div style="position:absolute;left:${x}px;top:${y}px;width:520px;height:1040px;transform:scale(${sc});transform-origin:0 0;background:#1a1a1a;border-radius:64px;padding:22px">
   <div style="width:100%;height:100%;background:#F3F5F4;border-radius:46px;overflow:hidden;position:relative">
    <div style="height:40px"></div>
    <div style="display:flex;align-items:center;gap:10px;padding:10px 20px;border-bottom:1px solid #D7DFDB">
      <span style="font:800 30px Brico">←</span><span style="font:800 26px/1.15 Brico;flex:1">${title}</span><span style="font:700 20px Atk;background:#fff;border:1px solid #D7DFDB;border-radius:99px;padding:4px 12px">⏱ 1:24</span></div>
    ${rows}${done}
    ${opts.tap?`<div style="position:absolute;right:20px;top:${opts.tapY||200}px;font-size:52px;transform:scale(${1-0.15*Math.sin(C(0,1,opts.tap)*Math.PI)})">🔊👆</div>`:''}
   </div></div>`;
}
function endcard(t,s,line2='Quer praticar grátis?<br>Comenta EU QUERO'){
  const a=io(t,s,0.5);
  return `<div style="position:absolute;inset:0;background:${G}"></div>
  <div style="position:absolute;left:150px;right:150px;top:520px;border:12px solid #fff;border-radius:40px;text-align:center;padding:50px 20px;color:#fff;transform:scale(${pop(a)})">
   <div style="font:700 52px Overpass;letter-spacing:6px">NEXT EXIT</div><div style="font:900 130px/1 Overpass">English ↗</div></div>
  <div class="abs big" style="top:1010px;color:#fff;font-size:68px;opacity:${io(t,s+0.7)}">Curte para mais! 💚</div>
  <div class="abs big" style="top:1130px;color:${Y};font-size:56px;opacity:${io(t,s+1.3)}">${line2}</div>`;
}

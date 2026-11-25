import os
from playwright.sync_api import sync_playwright
W=os.path.dirname(os.path.abspath(__file__)); OUT=W+'/imagens'; os.makedirs(OUT,exist_ok=True)
CSS=open(W+'/base.css').read().replace('height:1920px','height:1350px')
CAR={
 'casa':('🏠 Partes da casa',[('🛏️','bed','cama'),('🛋️','couch','sofá'),('🪟','window','janela'),('🚪','door','porta'),('🪞','mirror','espelho'),('💡','lamp','abajur'),('🧺','closet','armário'),('🪜','stairs','escada'),('🧸','pillow','travesseiro'),('🛌','blanket','cobertor'),('🎞️','curtains','cortinas'),('🟫','rug','tapete')]),
 'ferramentas':('🔧 Ferramentas',[('🔨','hammer','martelo'),('🪛','screwdriver','chave de fenda'),('🔧','wrench','chave inglesa'),('🪚','saw','serrote'),('📏','tape measure','fita métrica'),('🔩','screw','parafuso'),('📌','nail','prego'),('🪜','ladder','escada'),('🧰','toolbox','caixa de ferramentas'),('🗜️','pliers','alicate'),('🔌','drill','furadeira'),('🧴','glue','cola')]),
 'escritorio':('💼 No escritório',[('🖥️','computer','computador'),('🪑','chair','cadeira'),('🗄️','desk','mesa'),('🖨️','printer','impressora'),('📎','paper clip','clipe'),('📁','folder','pasta'),('🖊️','pen','caneta'),('📓','notebook','caderno'),('📅','schedule','escala / agenda'),('🤝','meeting','reunião'),('👥','coworker','colega de trabalho'),('☕','break','intervalo')]),
 'clima':('🌦️ O clima',[('☀️','sunny','ensolarado'),('☁️','cloudy','nublado'),('🌧️','rainy','chuvoso'),('❄️','snowy','com neve'),('💨','windy','ventando'),('🌫️','foggy','com neblina'),('🔥','hot','quente'),('🥶','cold','frio'),('⛈️','storm','tempestade'),('⚡','thunder','trovão'),('☂️','umbrella','guarda-chuva'),('📺','forecast','previsão do tempo')]),
 'emocoes':('😊 Emoções',[('😄','happy','feliz'),('😢','sad','triste'),('😠','angry','bravo'),('😴','tired','cansado'),('😨','scared','com medo'),('🤩','excited','animado'),('😬','nervous','nervoso'),('🥱','bored','entediado'),('😌','proud','orgulhoso'),('😲','surprised','surpreso'),('😕','confused','confuso'),('🥺','homesick','com saudade de casa')]),
 'profissoes':('👷 Profissões',[('👨‍🍳','cook','cozinheiro'),('🧾','cashier','caixa'),('🚚','driver','motorista'),('👩‍⚕️','nurse','enfermeira'),('🧹','cleaner','faxineiro'),('🍽️','server','garçom'),('🔧','mechanic','mecânico'),('👩‍🏫','teacher','professor'),('👶','babysitter','babá'),('🛏️','housekeeper','camareira'),('🛟','lifeguard','salva-vidas'),('🧽','dishwasher','lavador de pratos')]),
}
US_UK=[('🏢','apartment','flat','apartamento'),('🛗','elevator','lift','elevador'),('🍪','cookie','biscuit','biscoito'),('🍟','fries','chips','batata frita'),('🚛','truck','lorry','caminhão'),('🏖️','vacation','holiday','férias'),('🚶','sidewalk','pavement','calçada'),('⛽','gas','petrol','gasolina'),('🗑️','trash','rubbish','lixo'),('🧍','line','queue','fila'),('👖','pants','trousers','calça'),('⚽','soccer','football','futebol')]
FRASES=[('running_late','⏰',"I'm running late!",'Estou atrasado!','Pra avisar o chefe ou um amigo quando não vai chegar na hora.'),
 ('no_worries','🙌','No worries!','Sem problemas! / Imagina!','Resposta simpática quando alguém pede desculpa ou agradece.'),
 ('check','🧾','Can I get the check?','Pode trazer a conta?','No restaurante nos EUA, a conta só vem quando você pede.'),
 ('living','💼','What do you do for a living?','Você trabalha com quê?','Uma das primeiras perguntas que americanos fazem.')]
def head(): return '<div class="sign" style="top:40px"><small>NEXT EXIT</small>English ↗</div>'
def foot(n=''): return f'<div style="position:absolute;left:0;right:0;bottom:0;height:90px;background:#0B6B47;color:#fff;display:flex;align-items:center;justify-content:center;font:800 38px Brico">Salva pra praticar 📌{n}</div>'
def cover(title,sub):
    return f'''<div style="position:absolute;inset:0;background:#0B6B47"></div>{head()}
    <div style="position:absolute;left:90px;right:90px;top:330px;border:12px solid #fff;border-radius:40px;padding:60px 40px;text-align:center;color:#fff">
     <div style="font:800 46px Brico;color:#FFC21A">Vocabulário nos EUA</div><div style="font:900 104px/1.05 Overpass;margin-top:20px">{title}</div></div>
    <div style="position:absolute;left:0;right:0;top:900px;text-align:center;color:#fff;font:800 48px/1.3 Brico">{sub}</div>
    <div style="position:absolute;left:0;right:0;bottom:70px;text-align:center;color:#FFC21A;font:800 44px Brico">Arrasta pro lado 👉</div>'''
def grid(title,items,pg):
    cells=''.join(f'''<div style="background:#fff;border-radius:24px;padding:22px 10px;height:320px;text-align:center;box-shadow:0 6px 0 #D7DFDB">
      <div style="font-size:120px;line-height:1.15">{e}</div><div style="font:700 46px Mono;color:#0B6B47;margin-top:8px">{en}</div><div style="font:700 34px Atk;color:#2C4A9A">{pt}</div></div>''' for e,en,pt in items)
    return f'''{head()}<div style="position:absolute;right:40px;top:56px;font:800 34px Brico;color:#13201B">{title} · {pg}</div>
    <div style="position:absolute;left:50px;right:50px;top:180px;display:grid;grid-template-columns:repeat(2,1fr);gap:28px">{cells}</div>{foot()}'''
def usuk(items,pg):
    rows=''.join(f'''<div style="display:grid;grid-template-columns:80px 1fr 1fr;align-items:center;background:#fff;border-radius:20px;padding:22px 24px;margin-bottom:22px">
      <span style="font-size:60px">{e}</span><div><div style="font:700 40px Mono;color:#0B6B47">{us}</div><div style="font:700 26px Atk;color:#2C4A9A">{pt}</div></div><div style="font:700 40px Mono;color:#E5482F;text-align:right">{uk}</div></div>''' for e,us,uk,pt in items)
    return f'''{head()}<div style="position:absolute;left:50px;right:50px;top:170px;display:flex;justify-content:space-between;font:800 40px Brico;padding:0 20px 16px"><span style="margin-left:90px">🇺🇸 EUA</span><span>🇬🇧 Reino Unido</span></div>
    <div style="position:absolute;left:50px;right:50px;top:240px">{rows}</div>{foot(f' · {pg}')}'''
def cta():
    return f'''<div style="position:absolute;inset:0;background:#0B6B47"></div>{head()}
    <div style="position:absolute;left:0;right:0;top:400px;text-align:center;color:#fff;font:800 72px/1.25 Brico;padding:0 80px">Quer praticar essas palavras digitando no celular?</div>
    <div style="position:absolute;left:0;right:0;top:820px;text-align:center;color:#FFC21A;font:800 64px Brico">Comenta EU QUERO 💚</div>
    <div style="position:absolute;left:0;right:0;top:960px;text-align:center;color:#fff;font:700 44px Atk">É grátis · 5 min por dia ✍️</div>'''
def frase(e,en,pt,ctx):
    return f'''{head()}<div style="position:absolute;right:40px;top:56px;background:#FFC21A;font:800 34px Brico;padding:8px 20px;border-radius:12px">FRASE DO DIA</div>
    <div style="position:absolute;left:0;right:0;top:230px;text-align:center;font-size:160px">{e}</div>
    <div class="card" style="top:480px;text-align:center"><div style="font:700 76px/1.2 Mono;color:#0B6B47">{en}</div><div style="font:700 54px Atk;color:#2C4A9A;margin-top:20px">{pt}</div></div>
    <div style="position:absolute;left:100px;right:100px;top:900px;text-align:center;font:700 40px/1.35 Atk;color:#5E6E67">{ctx}</div>{foot()}'''
pages={}
for k,(t,items) in CAR.items():
    pages[f'{k}_1']=cover(t.split(' ',1)[1],'12 palavras que você vai usar<br>no dia a dia nos EUA')
    pages[f'{k}_2']=grid(t,items[:6],'1/2'); pages[f'{k}_3']=grid(t,items[6:],'2/2'); pages[f'{k}_4']=cta()
pages['usuk_1']=cover('EUA × Reino Unido','Mesma coisa, palavras diferentes!<br>Qual você usaria? 🤔')
pages['usuk_2']=usuk(US_UK[:6],'1/2'); pages['usuk_3']=usuk(US_UK[6:],'2/2'); pages['usuk_4']=cta()
for k,e,en,pt,ctx in FRASES: pages[f'frase_{k}']=frase(e,en,pt,ctx)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=b.new_page(viewport={'width':1080,'height':1350})
    for name,body in pages.items():
        f=f'{W}/_tmp.html';open(f,'w').write(f'<html><head><meta charset="utf-8"><style>{CSS}</style></head><body>{body}</body></html>');pg.goto('file://'+f)
        pg.evaluate('document.fonts.ready'); pg.wait_for_timeout(150)
        pg.screenshot(path=f'{OUT}/{name}.png')
    b.close()
print(len(pages))

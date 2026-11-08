#!/usr/bin/env python3
"""Einheitlicher Kopf, Fuß und Über-uns-Box für ALLE Seiten (eine Quelle). Aufruf: python3 tools/layout.py
Ersetzt <header class="site">…</header>, <footer class="site">…</footer> und den Block <!--ABOUT-->…<!--/ABOUT--> (vor </main>)
in jeder index.html und setzt die Cache-Version. Neue Seiten: einfach Kopf/Fuß aus einer bestehenden Seite kopieren oder Platzhalter
<header class="site"></header> / <footer class="site"></footer> setzen und dieses Skript ausführen."""
import re,pathlib,json,subprocess,urllib.parse,html
R=pathlib.Path(__file__).resolve().parent.parent
VER=5
LOGO='https://bride-light.de/medien/70/480-weisses-herz-logo-mit-make-up-puder-pinsel-und-text-bride-un.webp?v=1'
FOTO='https://bride-light.de/medien/44/1600-waehrend-der-trauung.webp?v=1'
UTM=lambda m,c:f'?utm_source=tools&amp;utm_medium={m}&amp;utm_campaign={c}'
NAV=[('budgetrechner','Budget'),('gaesteliste','Gästeliste'),('sitzplan','Sitzplan'),('getraenkerechner','Getränke'),('checkliste','Checkliste'),('ratgeber','Ratgeber')]
def header(p,active):
    n=''.join(f'<a href="{p}{d}/"{" aria-current=\"page\"" if d==active else ""}>{t}</a>' for d,t in NAV)
    return f'''<header class="site"><div class="wrap"><a class="brand" href="{p or './'}"><img src="{LOGO}" alt="Bride &amp; Light" width="56" height="56"><span><b>Hochzeits-Tools</b><small>von Bride &amp; Light</small></span></a>
<nav>{n}<a class="nav-cta" href="https://bride-light.de/{UTM('nav','header')}">Zu Bride &amp; Light</a></nav></div></header>'''
def about(p):
    return f'''<!--ABOUT--><section class="about noprint"><div class="about-in wrap">
<div class="about-foto"><img src="{FOTO}" alt="Brautpaar im Strandkorb vor dem Meer – Hochzeitsfoto von Bride &amp; Light" loading="lazy" width="520" height="640"></div>
<div class="about-txt"><p class="eyebrow">Über uns</p><h2>Hinter den Tools: <em>Bride &amp; Light</em></h2>
<p>Wir begleiten Brautpaare mit Hochzeitsfotografie und Brautstyling – auf Rügen, in Stralsund und in ganz Mecklenburg-Vorpommern. Diese Tools sind unser Geschenk an euch, damit ihr eure Planung mit Ruhe angeht.</p>
<p>Und wenn ihr jemanden für schöne Bilder und ein entspanntes Styling sucht: Wir freuen uns auf eure Geschichte.</p>
<p class="about-btns"><a class="btn" href="https://bride-light.de/{UTM('about','ueber-uns')}">Bride &amp; Light kennenlernen</a></p></div>
</div></section><!--/ABOUT-->'''
def footer(p):
    tl=''.join(f'<a href="{p}{d}/">{t}</a>' for d,t in NAV[:5])
    return f'''<footer class="site"><div class="wrap foot-grid">
<div class="foot-brand"><img src="{LOGO}" alt="Bride &amp; Light" width="96" height="96" loading="lazy"><p>Hochzeitsfotografie und Brautstyling<br>auf Rügen, in Stralsund und ganz MV.</p></div>
<div><h3>Planungs-Tools</h3>{tl}<a href="{p}download/hochzeitsplaner.pdf" download>Planer als PDF</a></div>
<div><h3>Bride &amp; Light</h3><a href="https://bride-light.de/{UTM('footer','footer')}">Startseite</a><a href="https://bride-light.de/hochzeitsfotograf-ruegen{UTM('footer','footer')}">Hochzeitsfotograf Rügen</a><a href="https://bride-light.de/{UTM('footer','footer')}#unserepakete">Pakete</a><a href="https://bride-light.de/{UTM('footer','footer')}#kontakt">Kontakt</a><a href="https://instagram.com/_bride_light_">Instagram</a></div>
<div><h3>Rechtliches</h3><a href="https://bride-light.de/impressum">Impressum</a><a href="https://bride-light.de/datenschutzerklarung">Datenschutz</a><a href="https://bride-light.de/agb">AGB</a></div>
</div><div class="wrap foot-copy">© Bride &amp; Light · Alle Eingaben bleiben in eurem Browser gespeichert.</div></footer>'''
def pinbox(p,rel):
    """Pinterest-Merken-Box: nutzt das Pin-Bild (Variante 0) der Seite aus marketing/pins.json. Reiner Link, kein Skript, kein Tracking."""
    pins=json.loads((R/'marketing'/'pins.json').read_text(encoding='utf-8'))
    c=[x for x in pins if x['link'].strip('/')==rel.strip('/')]
    if not c: return ''
    x=sorted(c,key=lambda q:q['variant'])[0]; B='https://tools.bride-light.de/'
    th=R/'assets'/'img'/f"pin-{x['slug']}.webp"
    if not th.exists(): subprocess.run(['convert',str(R/'marketing'/'pins'/f"{x['slug']}.png"),'-resize','300x','-quality','80',str(th)],check=True)
    desc=re.sub(r'\s*#\w+','',x['desc']).strip()
    url='https://www.pinterest.com/pin/create/button/?'+urllib.parse.urlencode({'url':B+x['link'],'media':B+f"marketing/pins/{x['slug']}.png",'description':x['title']+' – '+desc},quote_via=urllib.parse.quote)
    t=html.escape(x['title'],quote=True)
    return f'''<!--PIN--><aside class="pinbox noprint"><img src="{p}assets/img/pin-{x['slug']}.webp" alt="{t}" width="200" height="300" loading="lazy">
<div><h2>Auf Pinterest merken</h2><p>Speichert euch diese Seite als Pin, dann findet ihr sie beim Planen schnell wieder.</p><a class="btn" href="{html.escape(url,quote=True)}" target="_blank" rel="noopener">Auf Pinterest merken</a></div></aside><!--/PIN-->'''
def pages():
    return [f for f in R.rglob('index.html') if not any(x in f.parts for x in ('marketing','node_modules','.git'))]
def run():
    for f in pages():
        rel=f.relative_to(R).parent.parts; p='../'*len(rel); active=rel[0] if rel else ''
        s=f.read_text(encoding='utf-8')
        s=re.sub(r'<header class="site">.*?</header>',lambda m:header(p,active),s,flags=re.S)
        s=re.sub(r'<footer class="site">.*?</footer>',lambda m:footer(p),s,flags=re.S)
        s=re.sub(r'\n?<!--PIN-->.*?<!--/PIN-->','',s,flags=re.S)
        s=re.sub(r'<!--ABOUT-->.*?<!--/ABOUT-->\s*','',s,flags=re.S)
        pb=pinbox(p,'/'.join(rel)) if rel else ''
        if pb: s=s.replace('</main>',pb+'\n</main>',1)
        s=s.replace('</main>',about(p)+'\n</main>',1) if False else s.replace('</main>','</main>\n'+about(p),1)
        s=re.sub(r'(style\.css|site\.js)\?v=\d+',lambda m:f'{m.group(1)}?v={VER}',s)
        f.write_text(s,encoding='utf-8')
        print('ok',f.relative_to(R))
if __name__=='__main__': run()

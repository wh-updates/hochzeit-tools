#!/usr/bin/env python3
"""Einheitlicher Kopf, Fuß und Über-uns-Box für ALLE Seiten (eine Quelle). Aufruf: python3 tools/layout.py
Ersetzt <header class="site">…</header>, <footer class="site">…</footer> und den Block <!--ABOUT-->…<!--/ABOUT--> (vor </main>)
in jeder index.html und setzt die Cache-Version. Neue Seiten: einfach Kopf/Fuß aus einer bestehenden Seite kopieren oder Platzhalter
<header class="site"></header> / <footer class="site"></footer> setzen und dieses Skript ausführen."""
import re,pathlib,json,subprocess,urllib.parse,html
R=pathlib.Path(__file__).resolve().parent.parent
VER=7
LOGO='https://bride-light.de/medien/70/480-weisses-herz-logo-mit-make-up-puder-pinsel-und-text-bride-un.webp?v=1'
FOTO='https://bride-light.de/medien/44/1600-waehrend-der-trauung.webp?v=1'
UTM=lambda m,c:f'?utm_source=tools&amp;utm_medium={m}&amp;utm_campaign={c}'
NAV=[('budgetrechner','Budget'),('gaesteliste','Gästeliste'),('sitzplan','Sitzplan'),('getraenkerechner','Getränke'),('checkliste','Checkliste'),('ratgeber','Ratgeber')]
# Weitere Tools (Auswahlmenü im Kopf) in Planungs-Reihenfolge: Ablauf → Fotos → Licht → Torte → Tischkarten → Test
MORE=[('hochzeitsdatum-finder','Hochzeitsdatum-Finder'),('hochzeitstyp','Hochzeitstyp-Test'),('ablaufplan','Ablaufplan'),('einladungs-rechner','Einladungs-Rechner'),('brautstrauss-konfigurator','Brautstrauß'),('tischkarten','Tischkarten'),('gastgeschenke-rechner','Gastgeschenke'),('hochzeitstorte-rechner','Hochzeitstorte'),('fotostunden-rechner','Fotostunden-Rechner'),('goldene-stunde','Goldene Stunde'),('foto-wunschliste','Foto-Wunschliste'),('fotograf-test','Fotografen-Test'),('packliste-hochzeit','Packliste'),('hochzeitstag-rechner','Hochzeitstage')]
def header(p,active):
    def a(d,t): return f'<a href="{p}{d}/"{" aria-current=\"page\"" if d==active else ""}>{t}</a>'
    mact=any(d==active for d,_ in MORE)
    more=f'<details class="navmore"{" open" if False else ""}><summary{" aria-current=\"true\"" if mact else ""}>Weitere Tools</summary><div class="navmore-in">'+''.join(a(d,t) for d,t in MORE)+'</div></details>'
    n=''.join(a(d,t) for d,t in NAV[:5])+more+a(*NAV[5])
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
    tl=''.join(f'<a href="{p}{d}/">{t}</a>' for d,t in NAV[:5]+MORE)
    return f'''<footer class="site"><div class="wrap foot-grid">
<div class="foot-brand"><img src="{LOGO}" alt="Bride &amp; Light" width="96" height="96" loading="lazy"><p>Hochzeitsfotografie und Brautstyling<br>auf Rügen, in Stralsund und ganz MV.</p></div>
<div><h3>Planungs-Tools</h3>{tl}<a href="{p}download/hochzeitsplaner.pdf" download>Planer als PDF</a></div>
<div><h3>Bride &amp; Light</h3><a href="{p}hochzeitsfotograf/">Hochzeitsfotograf in MV</a><a href="https://bride-light.de/{UTM('footer','footer')}">Startseite</a><a href="https://bride-light.de/hochzeitsfotograf-ruegen{UTM('footer','footer')}">Hochzeitsfotograf Rügen</a><a href="https://bride-light.de/{UTM('footer','footer')}#unserepakete">Pakete</a><a href="https://bride-light.de/{UTM('footer','footer')}#kontakt">Kontakt</a><a href="https://instagram.com/_bride_light_">Instagram</a><a href="{ETSY}{UTM('footer','footer')}">Website-Vorlagen für Fotograf:innen</a></div>
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
# E-Mail-Liste: Formular-Adresse des E-Mail-Anbieters (z. B. Double-Opt-in-Formular). Leer = Block wird nicht angezeigt.
NEWSLETTER_ACTION=''
def newsletter():
    if not NEWSLETTER_ACTION: return ''
    return f'''<!--NEWSLETTER--><section class="card noprint" aria-label="Erinnerungen per E-Mail"><h2>Erinnerungen per E-Mail</h2><p>Wir schicken euch die Aufgaben der Checkliste zur richtigen Zeit. Abmeldung jederzeit möglich.</p>
<form action="{NEWSLETTER_ACTION}" method="post" target="_blank"><label for="nl-mail">E-Mail-Adresse</label><input id="nl-mail" type="email" name="email" required autocomplete="email">
<label style="display:flex;gap:.5rem;align-items:flex-start;margin:.7rem 0"><input type="checkbox" required style="width:auto;margin-top:.25rem"><span>Ich möchte E-Mails mit Planungs-Erinnerungen erhalten. Hinweise zur Verarbeitung stehen in der <a href="https://bride-light.de/datenschutzerklarung">Datenschutzerklärung</a>.</span></label>
<button type="submit">Anmelden</button></form></section><!--/NEWSLETTER-->'''
ETSY='https://www.etsy.com/shop/BrideLightShop'
KUNDEN='https://kunden.bride-light.de/'
# Eigenwerbung: pro Seitenbereich eine Karte (eine Quelle). Reiner Link, kein Skript, kein Tracking.
PROMO={
 'budgetrechner':('kunden','Budget steht? Plant jetzt eure Fotos mit ein.','Hochzeitsfotografie und Brautstyling von Bride &amp; Light – auf Rügen, in Stralsund und ganz MV.','Fotos anfragen'),
 'ratgeber':('kunden','Hochzeit auf Rügen oder an der Ostsee?','Fotos und Brautstyling aus einer Hand – persönlich, entspannt und mit Blick für Details.','Jetzt anfragen'),
 'gaesteliste':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'sitzplan':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'getraenkerechner':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'checkliste':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'ablaufplan':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'hochzeitstorte-rechner':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'einladungs-rechner':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'brautstrauss-konfigurator':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'gastgeschenke-rechner':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'packliste-hochzeit':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'hochzeitstag-rechner':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'hochzeitsdatum-finder':('kunden','Hochzeit auf Rügen oder an der Ostsee?','Habt ihr euer Datum? Wir halten gerne einen Termin für Fotos und Brautstyling frei, unverbindlich anfragen.','Termin anfragen'),
 'foto-wunschliste':('kunden','Eure Wunschliste, unsere Bilder','Schickt uns Datum und Wünsche. Wir melden uns persönlich bei euch.','Jetzt anfragen'),
 'fotograf-test':('kunden','Passt unser Stil zu euch?','Lernt uns unverbindlich kennen: Fotos und Brautstyling auf Rügen und in ganz MV.','Kennenlernen anfragen'),
 'tischkarten':('etsy','Mehr Vorlagen für eure Hochzeitsplanung','Planer, Checklisten und Vorlagen zum Sofort-Download in unserem Etsy-Shop.','Zum Etsy-Shop'),
 'fotostunden-rechner':('kunden','Wie viele Stunden braucht ihr wirklich?','Wir beraten euch zu Ablauf und Fotozeit – persönlich und unverbindlich.','Fotos anfragen'),
 'goldene-stunde':('kunden','Das schönste Licht für eure Fotos','Wir planen Trauung und Paarshooting mit euch rund um das beste Licht.','Fotos anfragen'),
 'hochzeitstyp':('kunden','Euer Stil, eure Bilder','Fotos und Brautstyling, die zu euch passen – persönlich und entspannt.','Jetzt anfragen'),
 'hochzeitsfotograf':('kunden','Euer Termin ist noch frei?','Schreibt uns Datum und Ort – wir melden uns persönlich bei euch.','Termin anfragen'),
}
def promo(rel):
    """Eigenwerbung-Karte (Label „Eigenwerbung“). Nur für Tool- und Ratgeberseiten, nicht für Start und Shop."""
    x=PROMO.get(rel[0]) if rel else None
    if not x: return ''
    kind,h,t,b=x
    url=(KUNDEN if kind=='kunden' else ETSY+'/')+UTM('promo',rel[0])
    if kind=='etsy': url=ETSY+UTM('promo',rel[0])
    return f'''<!--PROMO--><aside class="promo noprint" aria-label="Eigenwerbung"><p class="promo-label">Eigenwerbung</p>
<div class="promo-in"><div><h2>{h}</h2><p>{t}</p></div><a class="btn" href="{url}" target="_blank" rel="noopener">{b}</a></div></aside><!--/PROMO-->'''
def related_block(p,rel):
    import sys
    sys.path.insert(0,str(R/'tools'))
    from content.clusters import related,TITLES
    key='/'.join(rel); keys=related(key)
    if not keys: return ''
    li=''.join(f'<li><a href="{p}{k}/">{html.escape(TITLES[k],quote=False)}</a></li>' for k in keys)
    return f'<!--RELATED--><section class="card related noprint" aria-label="Mehr zum Thema"><h2>Mehr zum Thema</h2><ul>{li}</ul></section><!--/RELATED-->'
def pages():
    return [f for f in R.rglob('index.html') if not any(x in f.parts for x in ('marketing','node_modules','.git','whitelabel'))]
def run():
    for f in pages():
        rel=f.relative_to(R).parent.parts; p='../'*len(rel); active=rel[0] if rel else ''
        s=f.read_text(encoding='utf-8')
        s=re.sub(r'<header class="site">.*?</header>',lambda m:header(p,active),s,flags=re.S)
        s=re.sub(r'<footer class="site">.*?</footer>',lambda m:footer(p),s,flags=re.S)
        s=re.sub(r'\n?<!--PIN-->.*?<!--/PIN-->','',s,flags=re.S)
        s=re.sub(r'\n?<!--PROMO-->.*?<!--/PROMO-->','',s,flags=re.S)
        s=re.sub(r'<!--ABOUT-->.*?<!--/ABOUT-->\s*','',s,flags=re.S)
        s=re.sub(r'\n?<!--NEWSLETTER-->.*?<!--/NEWSLETTER-->','',s,flags=re.S)
        if rel==('checkliste',) and newsletter(): s=s.replace('<!--ICS-->','<!--ICS-->\n'+newsletter(),1)
        s=re.sub(r'\n?<!--RELATED-->.*?<!--/RELATED-->','',s,flags=re.S)
        rb=related_block(p,rel) if rel and rel[0] not in ('shop',) else ''
        if rb: s=s.replace('</main>',rb+'\n</main>',1)
        pb=pinbox(p,'/'.join(rel)) if rel else ''
        pm=promo(rel) if rel and rel[0]!='shop' else ''
        if pm or pb: s=s.replace('</main>',pm+('\n' if pm and pb else '')+pb+'\n</main>',1)
        s=s.replace('</main>',about(p)+'\n</main>',1) if False else s.replace('</main>','</main>\n'+about(p),1)
        s=re.sub(r'(style\.css|site\.js)\?v=\d+',lambda m:f'{m.group(1)}?v={VER}',s)
        f.write_text(s,encoding='utf-8')
        print('ok',f.relative_to(R))
if __name__=='__main__': run()

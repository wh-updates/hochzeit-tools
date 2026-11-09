#!/usr/bin/env python3
"""White-Label-Paket: baut aus den Tool-Seiten dieses Repos eine eigenständige, neutrale Version (Logo, Name, Farbe, Kontakt, Impressum, Datenschutz des Kunden).
Ohne Bride-&-Light-Bezug, ohne Ratgeber, ohne MV-Banner, ohne Eigenwerbung. Reine statische Dateien (Upload per FTP/Hosting, keine Server-Technik).
Aufruf: python3 whitelabel/build.py whitelabel/kunde.beispiel.json   → whitelabel/out/<slug>/ und whitelabel/out/<slug>.zip"""
import sys,re,json,html,shutil,pathlib,zipfile
W=pathlib.Path(__file__).resolve().parent; R=W.parent
TOOLS=['budgetrechner','gaesteliste','sitzplan','getraenkerechner','checkliste','ablaufplan','fotostunden-rechner','goldene-stunde','hochzeitstorte-rechner','tischkarten','hochzeitstyp']
NAV5=['budgetrechner','gaesteliste','sitzplan','getraenkerechner','checkliste']
CITIES=[['Hamburg',53.5511,9.9937],['Berlin',52.52,13.405],['Bremen',53.0793,8.8017],['Hannover',52.3759,9.732],['Düsseldorf',51.2277,6.7735],['Köln',50.9375,6.9603],['Frankfurt am Main',50.1109,8.6821],['Leipzig',51.3397,12.3731],['Dresden',51.0504,13.7373],['Nürnberg',49.4521,11.0767],['Stuttgart',48.7758,9.1829],['München',48.1351,11.582]]
E_=lambda s:html.escape(s,quote=True)
def cfg_load(p):
    c=json.load(open(p,encoding='utf-8'))
    for k in ('slug','name','domain','site_url','contact_url','imprint_url','privacy_url'):
        if not c.get(k): sys.exit(f'Konfiguration: Feld "{k}" fehlt')
    for k in ('tagline','logo_url','instagram_url','about_title','about_text','about_image_url','contact_text'): c.setdefault(k,'')
    c.setdefault('color','#8a4a50'); c.setdefault('color_dark','#6f3a40'); c.setdefault('orte',[]); c.setdefault('credit',False)
    c['domain']=c['domain'].rstrip('/'); c['contact_text']=c['contact_text'] or 'Jetzt anfragen'
    for k in ('color','color_dark'):
        if not re.fullmatch(r'#[0-9a-fA-F]{6}',c[k]): sys.exit(f'Konfiguration: {k} muss wie #8a4a50 aussehen')
    return c
def titles():
    s=(R/'index.html').read_text(encoding='utf-8'); out={}
    for m in re.finditer(r'<a class="tile" href="([a-z\-]+)/"><img class="ico" src="assets/img/([a-z]+)\.webp"[^>]*><h2>(.*?)</h2><p>(.*?)</p></a>',s):
        if m.group(1) in TOOLS: out[m.group(1)]=(m.group(2),m.group(3),m.group(4))
    return out
def header(c,p,active,t):
    a=lambda d,txt:f'<a href="{p}{d}/"{" aria-current=\"page\"" if d==active else ""}>{txt}</a>'
    short={d:re.sub(r'&amp;','&',t[d][1]) for d in t}
    nav5={'budgetrechner':'Budget','gaesteliste':'Gästeliste','sitzplan':'Sitzplan','getraenkerechner':'Getränke','checkliste':'Checkliste'}
    more=[d for d in TOOLS if d not in NAV5]; mact=active in more
    mn=f'<details class="navmore"><summary{" aria-current=\"true\"" if mact else ""}>Weitere Tools</summary><div class="navmore-in">'+''.join(a(d,short[d]) for d in more)+'</div></details>'
    logo=f'<img src="{E_(c["logo_url"])}" alt="{E_(c["name"])}" width="56" height="56">' if c['logo_url'] else ''
    return f'<header class="site"><div class="wrap"><a class="brand" href="{p or "./"}">{logo}<span><b>{E_(c["name"])}</b>'+(f'<small>{E_(c["tagline"])}</small>' if c['tagline'] else '')+f'</span></a>\n<nav>'+''.join(a(d,nav5[d]) for d in NAV5)+mn+f'<a class="nav-cta" href="{E_(c["contact_url"])}">{E_(c["contact_text"])}</a></nav></div></header>'
def footer(c,p,t):
    tl=''.join(f'<a href="{p}{d}/">{t[d][1]}</a>' for d in TOOLS)
    ig=f'<a href="{E_(c["instagram_url"])}">Instagram</a>' if c['instagram_url'] else ''
    cr='<p class="muted"><small>Technik: Hochzeits-Tools</small></p>' if c['credit'] else ''
    return f'''<footer class="site"><div class="wrap foot-grid">
<div class="foot-brand"><p><b>{E_(c["name"])}</b><br>{E_(c["tagline"])}</p></div>
<div><h3>Planungs-Tools</h3>{tl}</div>
<div><h3>{E_(c["name"])}</h3><a href="{E_(c["site_url"])}">Zur Webseite</a><a href="{E_(c["contact_url"])}">{E_(c["contact_text"])}</a>{ig}</div>
<div><h3>Rechtliches</h3><a href="{E_(c["imprint_url"])}">Impressum</a><a href="{E_(c["privacy_url"])}">Datenschutz</a></div>
</div><div class="wrap foot-copy">© {E_(c["name"])} · Alle Eingaben bleiben im Browser gespeichert.{cr}</div></footer>'''
def about(c):
    if not c['about_text']: return ''
    img=f'<div class="about-foto"><img src="{E_(c["about_image_url"])}" alt="" loading="lazy" width="520" height="640"></div>' if c['about_image_url'] else ''
    return f'<section class="about noprint"><div class="about-in wrap" style="{"" if img else "grid-template-columns:1fr"}">{img}<div class="about-txt"><h2>{E_(c["about_title"] or c["name"])}</h2><p>{E_(c["about_text"])}</p><p class="about-btns"><a class="btn" href="{E_(c["contact_url"])}">{E_(c["contact_text"])}</a></p></div></div></section>\n'
def clean(s,c,slug,t):
    host=c['domain'].split('://',1)[1]
    for b in ('SEO','PROMO','PIN','ABOUT'): s=re.sub(r'\n?<!--%s-->.*?<!--/%s-->'%(b,b),'',s,flags=re.S)
    s=re.sub(r'<link rel="canonical"[^>]*>\n?','',s)
    title=re.search(r'<title>(.*?)</title>',s,re.S).group(1); desc=re.search(r'<meta name="description" content="(.*?)">',s).group(1)
    desc=re.sub(r'Rechner für Rügen, Usedom, Stralsund und ganz Deutschland','Rechner für ganz Deutschland',desc)
    s=re.sub(r'<meta name="description" content=".*?">',lambda m:f'<meta name="description" content="{desc}">',s,count=1)
    canon=f'{c["domain"]}/{slug}/'
    s=s.replace('</head>',f'<link rel="canonical" href="{canon}">\n<meta name="robots" content="index,follow,max-image-preview:large">\n<meta name="theme-color" content="{c["color"]}">\n<meta property="og:type" content="website"><meta property="og:site_name" content="{E_(c["name"])}"><meta property="og:title" content="{title}"><meta property="og:description" content="{desc}"><meta property="og:url" content="{canon}">\n</head>',1)
    s=re.sub(r'<header class="site">.*?</header>',lambda m:header(c,'../',slug,t),s,flags=re.S)
    s=re.sub(r'<footer class="site">.*?</footer>',lambda m:footer(c,'../',t),s,flags=re.S)
    s=s.replace('</main>','</main>\n'+about(c),1) if about(c) else s
    s=s.replace('href="https://tools.bride-light.de/">Start','href="../">Start')
    # Verweise auf Ratgeber / Ortsseiten entfernen
    def weiter(m):
        items=[x for x in m.group(1).split(' · ') if 'ratgeber/' not in x and 'hochzeitsfotograf/' not in x]
        return '<p>Weiter planen: '+' · '.join(items)+'</p>' if items else ''
    s=re.sub(r'<p>Weiter planen: (.*?)</p>',weiter,s)
    s=s.replace('placeholder="z. B. 12. Juni 2027 · Stralsund"','placeholder="z. B. 12. Juni 2027 · Ort"')
    s=s.replace('PRODID:-//Bride & Light//Hochzeit-Tools//DE',f'PRODID:-//{c["name"]}//Hochzeit-Tools//DE').replace('@tools.bride-light.de','@'+host).replace('https://tools.bride-light.de/checkliste/',f'{c["domain"]}/checkliste/')
    s=s.replace('https://kunden.bride-light.de/?utm_source=tools&amp;utm_medium=quiz&amp;utm_campaign=hochzeitstyp',E_(c['contact_url']))
    s=s.replace('>Unverbindlich anfragen<',f'>{E_(c["contact_text"])}<')
    s=re.sub(r'(site\.js|style\.css)\?v=\d+',r'\1?v=wl1',s)
    return s
GENERIC_ORTE={'klassisch':'Gutshaus, Schloss, Hotel oder Kirche: Orte mit Platz für Gäste und einem festlichen Rahmen.','boho':'Wiese, Waldrand, Strand, Scheune oder Gartenfest: Orte mit viel Natur.','modern':'Moderne Hotels, Lofts und Design-Locations mit klarer Architektur.','maritim':'Strand, Seebrücke, Hafen oder Leuchtturm: Orte am Wasser.','vintage':'Alte Gutshäuser, Gärten, Dorfkirchen und Scheunen mit Charme.'}
def tool_specific(s,slug,c):
    if slug=='goldene-stunde':
        places=c['orte'] or CITIES
        s=re.sub(r'var PLACES = \[.*?\];\n','var PLACES = '+json.dumps(places,ensure_ascii=False)+';\n',s,count=1,flags=re.S)
    if slug=='hochzeitstyp':
        for k,v in GENERIC_ORTE.items(): s=re.sub(r"(%s: \{.*?orte: )'.*?'"%k,lambda m:m.group(1)+json.dumps(v,ensure_ascii=False),s,count=1,flags=re.S)
        s=re.sub(r"links: \[\[.*?\]\] \}",'links: [] }',s,flags=re.S)
        s=s.replace('<h3>Orte an der Ostsee</h3>','<h3>Orte</h3>').replace("$('links').innerHTML = 'Weiter lesen: '","$('links').innerHTML = ''; if (false) $('links').innerHTML = 'Weiter lesen: '")
        s=s.replace('Findet heraus, welcher Stil zu eurer Hochzeit passt, und bekommt Ideen für Deko, Fotos und Orte an der Ostsee.','Findet heraus, welcher Stil zu eurer Hochzeit passt, und bekommt Ideen für Deko, Fotos und Orte.')
        s=s.replace("Hochzeitsstil an der Ostsee","Hochzeitsstil")
    return s
def build(cfgp):
    c=cfg_load(cfgp); t=titles(); out=W/'out'/c['slug']
    if out.exists(): shutil.rmtree(out)
    (out/'assets'/'img').mkdir(parents=True)
    css=(R/'assets'/'style.css').read_text(encoding='utf-8')
    css+=f'\n/* White-Label-Farben */\n:root{{--accent:{c["color"]};--accent-d:{c["color_dark"]}}}\n'
    (out/'assets'/'style.css').write_text(css,encoding='utf-8')
    js=(R/'assets'/'site.js').read_text(encoding='utf-8'); js=js[:js.index('// Regionsfrage')]
    (out/'assets'/'site.js').write_text(js,encoding='utf-8')
    for d in TOOLS:
        src=(R/d/'index.html').read_text(encoding='utf-8'); s=tool_specific(clean(src,c,d,t),d,c)
        (out/d).mkdir(); (out/d/'index.html').write_text(s,encoding='utf-8'); shutil.copy(R/'assets'/'img'/f'{t[d][0]}.webp',out/'assets'/'img'/f'{t[d][0]}.webp')
    tiles='\n'.join(f'<a class="tile" href="{d}/"><img class="ico" src="assets/img/{t[d][0]}.webp" alt="" loading="lazy"><h2>{t[d][1]}</h2><p>{t[d][2]}</p></a>' for d in TOOLS)
    title=f'Kostenlose Hochzeits-Tools von {c["name"]}'; desc=f'Hochzeitsbudget, Gästeliste, Sitzplan, Checkliste, Ablaufplan und mehr: kostenlose Planungs-Tools von {c["name"]}. Ohne Anmeldung.'
    home=f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E_(title)}</title>
<meta name="description" content="{E_(desc)}">
<link rel="canonical" href="{c["domain"]}/">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="{c["color"]}">
<link rel="stylesheet" href="assets/style.css?v=wl1">
</head>
<body>
{header(c,"","",t)}
<main class="wrap">
<h1>Eure Hochzeits-Planungstools</h1>
<p class="lead">Kostenlos, ohne Anmeldung und ohne Datenweitergabe: Eure Eingaben bleiben in eurem eigenen Browser.</p>
<div class="grid">
{tiles}
</div>
</main>
{about(c)}{footer(c,"",t)}
</body>
</html>
'''
    (out/'index.html').write_text(home,encoding='utf-8')
    (out/'robots.txt').write_text(f'User-agent: *\nAllow: /\nSitemap: {c["domain"]}/sitemap.xml\n',encoding='utf-8')
    (out/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join(f'<url><loc>{c["domain"]}/{u}</loc></url>\n' for u in ['']+[d+'/' for d in TOOLS])+'</urlset>\n',encoding='utf-8')
    (out/'ANLEITUNG.txt').write_text(f'''Hochzeits-Tools für {c["name"]}
================================
Inhalt: reine statische Dateien (HTML, CSS, JS). Keine Datenbank, kein PHP, keine Cookies, kein Tracking.

Einrichtung
1. Subdomain anlegen, z. B. {c["domain"].split("://",1)[1]} (beim Hosting-Anbieter).
2. Gesamten Inhalt dieses Ordners in das Hauptverzeichnis der Subdomain hochladen (index.html muss direkt im Hauptverzeichnis liegen).
3. Aufrufen und kurz alle Seiten prüfen. Fertig.

Hinweise
- Impressum und Datenschutz verlinken auf eure Webseite. Dort sollte ein Hinweis stehen, dass die Tools Eingaben nur lokal im Browser speichern (localStorage).
- Logo, Farbe, Texte und Kontakt-Link kommen aus der Konfiguration. Änderungen: Konfiguration anpassen, Paket neu erzeugen, neu hochladen.
- Optional: Subdomain in der Google Search Console anmelden und {c["domain"]}/sitemap.xml einreichen.
''',encoding='utf-8')
    # Leck-Prüfung
    bad=[]
    for f in out.rglob('*'):
        if f.is_file() and f.suffix in ('.html','.js','.css','.xml','.txt'):
            s=f.read_text(encoding='utf-8')
            for pat in ('bride-light','Bride &','Bride &amp;','Rügen','Stralsund','kunden.bride','ratgeber/','hochzeitsfotograf/','Mecklenburg','Etsy','etsy'):
                if pat in s and not (pat=='Rügen' and False): bad.append((str(f.relative_to(out)),pat))
    if bad: sys.exit('Leck-Prüfung fehlgeschlagen: '+str(bad[:12]))
    z=W/'out'/f'{c["slug"]}.zip'
    with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(out.rglob('*')):
            if f.is_file(): zf.write(f,f.relative_to(out))
    print('fertig',out,z)
if __name__=='__main__': build(sys.argv[1] if len(sys.argv)>1 else W/'kunde.beispiel.json')

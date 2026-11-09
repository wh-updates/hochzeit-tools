#!/usr/bin/env python3
"""Baut alle Ratgeber-Seiten aus tools/content/*.py:
Seite (ratgeber/<slug>/index.html), Kachel-Icon (assets/img/<motiv>.webp), 6 Pins (pins.json + PNG), Ratgeber-Index (nach Themen gruppiert),
danach layout.py (Kopf/Fuß/Promo/Pinbox) und seo_apply.py (SEO, Sitemap, llms.txt) und build_feed.py.
Aufruf: python3 tools/build_pages.py [slug ...]   (ohne Argument: alle; vorhandene Pin-PNGs werden nur mit --force neu gezeichnet)"""
import sys,re,json,html,pathlib,subprocess
T=pathlib.Path(__file__).resolve().parent; R=T.parent
sys.path.insert(0,str(T))
import content, make_pin, make_icons
E=lambda s:html.escape(s,quote=False)
GROUPS=[('ort','Ort, Location und Unterkunft an der Ostsee'),('planung','Planung, Zeitplan und Papierkram'),('foto','Fotos und Styling'),('winter','Winterhochzeit')]
def card(h,c):
    if isinstance(c,list): body='<ul>\n'+'\n'.join(f'<li>{E(x)}</li>' for x in c)+'\n</ul>'
    else: body=''.join(f'<p>{E(x)}</p>' for x in c.split('\n\n'))
    return f'<div class="card">\n<h2>{E(h)}</h2>\n{body}\n</div>'
def page_html(pg):
    d='ratgeber/'+pg['slug']
    faq=''.join(f'<h3>{E(q)}</h3>\n<p>{E(a)}</p>\n' for q,a in pg['faq'])
    weiter=' · '.join(f'<a href="../../{l}/">{E(t)}</a>' if not l.startswith('http') else f'<a href="{l}">{E(t)}</a>' for l,t in pg['weiter'])
    season=pg.get('hinweis','Termine, Gebühren und Regeln ändern sich – bitte immer direkt bei den genannten Stellen bestätigen lassen.')
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(pg['title'])}</title>
<meta name="description" content="{html.escape(pg['desc'])}">
<link rel="canonical" href="https://tools.bride-light.de/{d}/">
<link rel="stylesheet" href="../../assets/style.css?v=7">
</head>
<body>
<header class="site"></header>
<main class="wrap">

<h1>{E(pg['h1'])}</h1>
<p class="lead">{E(pg['lead'])}</p>
{chr(10).join(card(h,c) for h,c in pg['cards'])}
<section class="card faq">
<h2>Häufige Fragen</h2>
{faq}</section>
<p>Weiter planen: {weiter}</p>
<p class="muted"><small>Stand: November 2026. {E(season)}</small></p>
</main>
<footer class="site"></footer>
<script src="../../assets/site.js?v=7"></script>
</body>
</html>
'''
def register_pins(pg,force=False):
    pj=R/'marketing'/'pins.json'; d=json.loads(pj.read_text(encoding='utf-8')); link=f"ratgeber/{pg['slug']}/"
    keep=[x for x in d if x['link']!=link]; old={x['slug']:x for x in d if x['link']==link}
    new=[]
    for i,(board,t1,t2,sub,title,desc) in enumerate(pg['pins']):
        slug=f"{pg['motif']}-{i+1}"
        assert len(t1)<=17 and len(t2)<=22,(slug,t1,t2)
        x=dict(slug=slug,board=board,title=title,desc=desc,link=link,live=old.get(slug,{}).get('live',False),date=old.get(slug,{}).get('date','2026-11-09T12:00:00+00:00'),t1=t1,t2=t2,sub=sub,variant=i%3)
        if pg.get('season'): x['from'],x['until']=pg['season']
        new.append(x)
    pj.write_text(json.dumps(keep+new,ensure_ascii=False,indent=1),encoding='utf-8')
    for x in new:
        png=R/'marketing'/'pins'/f"{x['slug']}.png"
        if force or not png.exists(): make_pin.make(x['slug'],x['t1'],x['t2'],x['sub'],x['board'],x['variant'])
def tiles(pages,prefix):
    out=[]
    for pg in pages:
        out.append(f'<a class="tile" href="{prefix}{pg["slug"]}/"><img class="ico" src="{prefix and "../"}assets/img/{pg["motif"]}.webp" alt="" loading="lazy"><h2>{E(pg["short"])}</h2><p>{E(pg["tile"])}</p></a>')
    return '\n'.join(out)
def index_ratgeber():
    allp=content.PAGES; f=R/'ratgeber'/'index.html'; s=f.read_text(encoding='utf-8')
    body=''
    for g,t in GROUPS:
        ps=[p for p in allp if p['group']==g]
        if ps: body+=f'<h2 class="sec-h">{E(t)}</h2>\n<div class="grid">\n'+tiles(ps,'').replace('src="assets','src="../assets')+'\n</div>\n'
    s=re.sub(r'(<p class="lead">.*?</p>\n).*?(<div class="card"><h2>Kostenloser Hochzeitsplaner)',lambda m:m.group(1)+body+m.group(2),s,count=1,flags=re.S)
    f.write_text(s,encoding='utf-8')
def main(args):
    force='--force' in args; sel=[a for a in args if not a.startswith('--')]
    for pg in content.PAGES:
        if pg.get('static'): continue
        if sel and pg['slug'] not in sel: continue
        d=R/'ratgeber'/pg['slug']; d.mkdir(parents=True,exist_ok=True)
        (d/'index.html').write_text(page_html(pg),encoding='utf-8')
        if not (R/'assets'/'img'/f"{pg['motif']}.webp").exists() or force: make_icons.icon(pg['motif'])
        register_pins(pg,force)
        print('gebaut',pg['slug'])
    index_ratgeber()
    for cmd in (['layout.py'],['seo_apply.py'],['build_feed.py']): subprocess.run(['python3',str(T/cmd[0])],cwd=R,check=True,stdout=subprocess.DEVNULL)
if __name__=='__main__': main(sys.argv[1:])

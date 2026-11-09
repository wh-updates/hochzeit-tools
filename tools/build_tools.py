#!/usr/bin/env python3
"""Baut die Tool-Seiten (Quelle: tools/content/extra.py + tools/toolsrc/<slug>.html/.js) und die lokalen Fotografen-Seiten (hochzeitsfotograf/).
Aufruf: python3 tools/build_tools.py [--force]   (danach layout.py, seo_apply.py, build_feed.py)"""
import re,sys,json,html,pathlib,subprocess
T=pathlib.Path(__file__).resolve().parent; R=T.parent
sys.path.insert(0,str(T))
import make_pin, make_icons
from content.extra import TOOLPAGES,LOCAL,LOCAL_INDEX
from build_pages import card,E
from content.tooltexte import render as text_render
KUNDEN='https://kunden.bride-light.de/'
def head(title,desc,canon,up):
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="https://tools.bride-light.de/{canon}">
<link rel="stylesheet" href="{up}assets/style.css?v=7">
</head>
<body>
<header class="site"></header>
<main class="wrap">

'''
def faq_html(faq,h='Häufige Fragen'):
    return f'<section class="card faq">\n<h2>{h}</h2>\n'+''.join(f'<h3>{E(q)}</h3>\n<p>{E(a)}</p>\n' for q,a in faq)+'</section>\n'
def weiter_html(w,up):
    return '<p>Weiter planen: '+' · '.join(f'<a href="{up}{l}/">{E(t)}</a>' for l,t in w)+'</p>\n'
def tool_html(pg):
    body=(T/'toolsrc'/f"{pg['slug']}.html").read_text(encoding='utf-8'); js=(T/'toolsrc'/f"{pg['slug']}.js").read_text(encoding='utf-8')
    extra=(T/'toolsrc'/f"{pg['slug']}.css").read_text(encoding='utf-8') if (T/'toolsrc'/f"{pg['slug']}.css").exists() else ''
    st=f'<style>{extra}</style>\n' if extra else ''
    return head(pg['title'],pg['desc'],pg['slug']+'/','../')+f'''<h1>{E(pg['h1'])}</h1>
<p class="lead">{E(pg['lead'])}</p>
{st}{body}
{text_render(pg['slug'],'../')}{faq_html(pg['faq'])}{weiter_html(pg['weiter'],'../')}<p class="muted"><small>Stand: November 2026. Alle Eingaben bleiben in eurem Browser gespeichert, es wird nichts übertragen. Die Ergebnisse sind Richtwerte zur Orientierung.</small></p>
</main>
<footer class="site"></footer>
<script src="../assets/site.js?v=13"></script>
<script>
{js}</script>
</body>
</html>
'''
def cta(ort):
    return f'<div class="card"><h2>Hochzeitsfotos in {E(ort)} anfragen</h2><p>Schreibt uns Datum, Ort und eure Wünsche. Wir melden uns persönlich bei euch, unverbindlich.</p><p><a class="btn" href="{KUNDEN}?utm_source=tools&amp;utm_medium=ortsseite&amp;utm_campaign=hochzeitsfotograf-{E(ort.lower())}" target="_blank" rel="noopener">Unverbindlich anfragen</a></p></div>\n'
def local_html(pg):
    return head(pg['title'],pg['desc'],f"hochzeitsfotograf/{pg['slug']}/",'../../')+f'''<h1>{E(pg['h1'])}</h1>
<p class="lead">{E(pg['lead'])}</p>
{chr(10).join(card(h,c) for h,c in pg['cards'])}
{cta(pg['h1'].replace('Hochzeitsfotograf ',''))}{faq_html(pg['faq'])}{weiter_html(pg['weiter'],'../../')}<p class="muted"><small>Stand: November 2026. Orte, Regeln und Genehmigungen ändern sich – bitte vor dem Termin bei der jeweiligen Stelle bestätigen lassen.</small></p>
</main>
<footer class="site"></footer>
<script src="../../assets/site.js?v=13"></script>
</body>
</html>
'''
def local_index():
    tiles='\n'.join(f'<a class="tile" href="{p["slug"]}/"><img class="ico" src="../assets/img/{p["motif"]}.webp" alt="" loading="lazy"><h2>{E(p["short"])}</h2><p>{E(p["tile"])}</p></a>' for p in LOCAL)
    I=LOCAL_INDEX
    return head(I['title'],I['desc'],'hochzeitsfotograf/','../')+f'''<h1>{E(I['h1'])}</h1>
<p class="lead">{E(I['lead'])}</p>
{chr(10).join(card(h,c) for h,c in I['intro'])}
<div class="grid">
{tiles}
</div>
{cta('Mecklenburg-Vorpommern')}<p>Weiter planen: <a href="../goldene-stunde/">Goldene Stunde berechnen</a> · <a href="../fotostunden-rechner/">Fotostunden-Rechner</a> · <a href="../ratgeber/hochzeitsfotograf-finden/">Hochzeitsfotograf finden</a></p>
</main>
<footer class="site"></footer>
<script src="../assets/site.js?v=13"></script>
</body>
</html>
'''
def register_pins(pg,force=False):
    pj=R/'marketing'/'pins.json'; d=json.loads(pj.read_text(encoding='utf-8')); link=f"{pg['slug']}/"
    keep=[x for x in d if x['link']!=link]; old={x['slug']:x for x in d if x['link']==link}; new=[]
    for i,(board,t1,t2,sub,title,desc) in enumerate(pg['pins']):
        slug=f"{pg['motif']}-{i+1}"; assert len(t1)<=17 and len(t2)<=22,(slug,t1,t2)
        x=dict(slug=slug,board=board,title=title,desc=desc,link=link,live=old.get(slug,{}).get('live',False),date=old.get(slug,{}).get('date','2026-11-09T12:00:00+00:00'),t1=t1,t2=t2,sub=sub,variant=i%3)
        if pg.get('season'): x['from'],x['until']=pg['season']
        new.append(x)
    pj.write_text(json.dumps(keep+new,ensure_ascii=False,indent=1),encoding='utf-8')
    for x in new:
        png=R/'marketing'/'pins'/f"{x['slug']}.png"
        if force or not png.exists(): make_pin.make(x['slug'],x['t1'],x['t2'],x['sub'],x['board'],x['variant'])
def inject_old():
    from content.tooltexte import T,render
    for slug in ('budgetrechner','gaesteliste','sitzplan','getraenkerechner','checkliste'):
        f=R/slug/'index.html'
        h=f.read_text()
        h=re.sub(r'\n?<!--TEXT-->.*?<!--/TEXT-->','',h,flags=re.S)
        blk=render(slug,'../')
        assert '<section class="faq"' in h,slug
        h=h.replace('<section class="faq"',blk+'\n<section class="faq"',1)
        f.write_text(h)

def main(args):
    force='--force' in args
    for pg in TOOLPAGES:
        d=R/pg['slug']; d.mkdir(exist_ok=True); (d/'index.html').write_text(tool_html(pg),encoding='utf-8')
        if force or not (R/'assets'/'img'/f"{pg['motif']}.webp").exists(): make_icons.icon(pg['motif'])
        register_pins(pg,force); print('Tool',pg['slug'])
    inject_old()
    h=R/'hochzeitsfotograf'; h.mkdir(exist_ok=True); (h/'index.html').write_text(local_index(),encoding='utf-8')
    for p in LOCAL:
        (h/p['slug']).mkdir(exist_ok=True); (h/p['slug']/'index.html').write_text(local_html(p),encoding='utf-8')
        if not (R/'assets'/'img'/f"{p['motif']}.webp").exists(): make_icons.icon(p['motif'])
        print('Ort',p['slug'])
    for c in ('layout.py','seo_apply.py','build_feed.py'): subprocess.run(['python3',str(T/c)],cwd=R,check=True,stdout=subprocess.DEVNULL)
if __name__=='__main__': main(sys.argv[1:])

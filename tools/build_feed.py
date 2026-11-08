#!/usr/bin/env python3
"""Baut feed.xml (Board "Hochzeitsplanung Tipps") und feed-ostsee.xml (Board "Heiraten an der Ostsee") und feed-winter.xml (Board "Winterhochzeit")
aus marketing/pins.json. Nur Einträge mit "live": true kommen in den Feed.
Neue Pins: Eintrag mit live=false ans Ende von pins.json; pro Lauf wird der nächste auf live=true gesetzt
(release_next), danach build_feed.py ausführen."""
import json,pathlib,datetime,email.utils,html,sys
R=pathlib.Path(__file__).resolve().parent.parent; B='https://tools.bride-light.de/'
FEEDS={'planung':('feed.xml','Hochzeitsplanung Tipps – Hochzeit-Tools von Bride & Light'),'ostsee':('feed-ostsee.xml','Heiraten an der Ostsee – Bride & Light'),'winter':('feed-winter.xml','Winterhochzeit – Bride & Light')}
def load(): return json.loads((R/'marketing'/'pins.json').read_text(encoding='utf-8'))
def save(d): (R/'marketing'/'pins.json').write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding='utf-8')
def release_next(n=1,boards=None):
    """Gibt je Board die nächsten n wartenden Pins frei. Reihenfolge: Pins verschiedener Seiten abwechselnd (nicht dieselbe Seite hintereinander)."""
    d=load(); done=[]
    for board in (boards or FEEDS):
        for k in range(n):
            wait=[p for p in d if not p['live'] and p['board']==board]
            last=[p['link'] for p in d if p['live'] and p['board']==board]; last=last[-1] if last else None
            wait.sort(key=lambda p:(p['link']==last, p['variant']))   # erst andere Seite, dann niedrigere Variante
            if not wait: done.append(f'(Warteschlange {board} leer)'); break
            p=wait[0]; p['live']=True
            p['date']=(datetime.datetime.now(datetime.timezone.utc)-datetime.timedelta(minutes=k)).strftime('%Y-%m-%dT%H:%M:%S+00:00'); done.append(p['slug'])
    save(d); return ', '.join(done)
def build():
    d=load()
    for board,(fn,title) in FEEDS.items():
        items=[p for p in d if p['live'] and p['board']==board]; items.sort(key=lambda p:p['date'],reverse=True); x=[]
        for p in items:
            img=R/'marketing'/'pins'/f"{p['slug']}.png"; url=B+f"marketing/pins/{p['slug']}.png"; dt=datetime.datetime.fromisoformat(p['date'])
            x.append(f'''<item><title>{html.escape(p['title'])}</title><link>{html.escape(B+p['link'])}</link><guid isPermaLink="false">pin-{p['slug']}</guid>
<pubDate>{email.utils.format_datetime(dt)}</pubDate><description><![CDATA[<img src="{url}" alt="{html.escape(p['title'])}"/><p>{p['desc']}</p>]]></description>
<enclosure url="{url}" length="{img.stat().st_size}" type="image/png"/><media:content url="{url}" medium="image" type="image/png" width="1000" height="1500"/></item>''')
        (R/fn).write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/"><channel><title>{html.escape(title)}</title><link>{B}</link>
<description>Kostenlose Hochzeitsplaner-Tools und Ratgeber von Bride &amp; Light</description><language>de-de</language>
{chr(10).join(x)}
</channel></rss>
''',encoding='utf-8')
def build_flipboard(d=None):
    """feed-flipboard.xml: alle freigegebenen Pins beider Boards in einem Feed für Flipboard (Titel, Bild, Text ohne Hashtags, Link zur Seite)."""
    import re
    d=d if d is not None else load(); items=[p for p in d if p['live']]; items.sort(key=lambda p:p['date'],reverse=True); x=[]
    for p in items[:50]:
        img=R/'marketing'/'pins'/f"{p['slug']}.png"; url=B+f"marketing/pins/{p['slug']}.png"; dt=datetime.datetime.fromisoformat(p['date'])
        txt=html.escape(re.sub(r'\s*#\w+','',p['desc']).strip()); t=html.escape(p['title']); l=html.escape(B+p['link'])
        x.append(f'''<item><title>{t}</title><link>{l}</link><guid isPermaLink="false">flip-{p['slug']}</guid><pubDate>{email.utils.format_datetime(dt)}</pubDate>
<description>{txt}</description><content:encoded><![CDATA[<img src="{url}" alt="{t}"/><p>{re.sub(r'\s*#\w+','',p['desc']).strip()}</p><p><a href="{B+p['link']}">Zum kostenlosen Tool</a></p>]]></content:encoded>
<enclosure url="{url}" length="{img.stat().st_size if img.exists() else 0}" type="image/png"/><media:content url="{url}" medium="image" type="image/png"/></item>''')
    (R/'feed-flipboard.xml').write_text(f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:media="http://search.yahoo.com/mrss/" xmlns:content="http://purl.org/rss/1.0/modules/content/"><channel><title>Hochzeit-Tools &amp; Ratgeber – Bride &amp; Light</title><link>{B}</link>
<description>Kostenlose Hochzeitsplaner-Tools und Ratgeber für Heiraten an der Ostsee – von Bride &amp; Light</description><language>de-de</language>
{chr(10).join(x)}
</channel></rss>
''',encoding='utf-8')
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='release': print('freigegeben:',release_next(int(sys.argv[2]) if len(sys.argv)>2 else 1))
    build(); build_flipboard()

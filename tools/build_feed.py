#!/usr/bin/env python3
"""Baut feed.xml (Board "Hochzeitsplanung Tipps") und feed-ostsee.xml (Board "Heiraten an der Ostsee")
aus marketing/pins.json. Nur Einträge mit "live": true kommen in den Feed.
Neue Pins: Eintrag mit live=false ans Ende von pins.json; pro Lauf wird der nächste auf live=true gesetzt
(release_next), danach build_feed.py ausführen."""
import json,pathlib,datetime,email.utils,html,sys
R=pathlib.Path(__file__).resolve().parent.parent; B='https://tools.bride-light.de/'
FEEDS={'planung':('feed.xml','Hochzeitsplanung Tipps – Hochzeit-Tools von Bride & Light'),'ostsee':('feed-ostsee.xml','Heiraten an der Ostsee – Bride & Light')}
def load(): return json.loads((R/'marketing'/'pins.json').read_text(encoding='utf-8'))
def save(d): (R/'marketing'/'pins.json').write_text(json.dumps(d,ensure_ascii=False,indent=1),encoding='utf-8')
def release_next():
    d=load()
    for p in d:
        if not p['live']:
            p['live']=True; p['date']=datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%S+00:00'); save(d); return p['slug']
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
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='release': print('freigegeben:',release_next())
    build()

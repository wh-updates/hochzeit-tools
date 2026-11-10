"""Inhalte aller Ratgeber-Seiten (eine Quelle). Jede Seite ist ein dict, siehe tools/build_pages.py.
Ratgeber werden mit `python3 tools/build_pages.py` erzeugt (Seite, Kachel, Pins, Zeichnung, Sitemap)."""
import importlib
MODULES=['ratgeber_alt','ratgeber_winter','ratgeber_winter2','ratgeber_ostsee','ratgeber_planung','ratgeber_orte']
PAGES=[]
for m in MODULES:
    try: PAGES+=importlib.import_module('content.'+m).PAGES
    except ModuleNotFoundError as e:
        if m not in str(e): raise
ARTICLE_TITLES={f"ratgeber/{p['slug']}":p['short'] for p in PAGES if not p.get('static')}

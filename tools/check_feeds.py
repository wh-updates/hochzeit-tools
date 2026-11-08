#!/usr/bin/env python3
"""Prüft Kandidaten-Feeds (Gültigkeit, Aktualität, Bilder, Vorschaulänge) und schreibt marketing/feed-bericht.md + marketing/feeds-geprueft.json.
Nur Python-Standardbibliothek. Läuft in GitHub Actions (offenes Netz)."""
import json, re, sys, time, urllib.request, xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime

CAND = [
 ("Hochzeitswahn (DE)", "https://www.hochzeitswahn.de/feed/"),
 ("Hochzeitsguide (DE)", "https://www.hochzeitsguide.com/feed/"),
 ("Green Wedding Shoes", "https://www.greenweddingshoes.com/feed/"),
 ("100 Layer Cake", "https://www.100layercake.com/blog/feed/"),
 ("Rock n Roll Bride", "https://www.rocknrollbride.com/feed/"),
 ("Style Me Pretty", "https://www.stylemepretty.com/feed/"),
 ("Reddit r/weddingplanning", "https://www.reddit.com/r/weddingplanning/.rss"),
]
UA = "Mozilla/5.0 (compatible; HochzeitToolsFeedCheck/1.0; +https://tools.bride-light.de)"
NS = {"content": "http://purl.org/rss/1.0/modules/content/", "media": "http://search.yahoo.com/mrss/", "a": "http://www.w3.org/2005/Atom"}

def parse_date(s):
    try: return parsedate_to_datetime(s)
    except Exception:
        try: return datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception: return None

def check(name, url):
    r = {"name": name, "url": url, "ok": False}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml, application/atom+xml, text/xml, */*"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            raw = resp.read(3_000_000); r["http"] = resp.status
        root = ET.fromstring(raw)
    except Exception as e:
        r["fehler"] = str(e)[:150]; return r
    items = root.findall(".//item") or root.findall(".//a:entry", NS)
    r["items"] = len(items)
    if not items: r["fehler"] = "keine Einträge"; return r
    with_img = full = 0; newest = None
    for it in items:
        txt = " ".join((x.text or "") for x in it.iter() if x.tag.endswith("encoded") or x.tag.endswith("description") or x.tag.endswith("content") or x.tag.endswith("summary"))
        if re.search(r"<img\b", txt) or it.find("media:content", NS) is not None or it.find("media:thumbnail", NS) is not None or it.find("enclosure") is not None: with_img += 1
        if len(re.sub(r"<[^>]+>", "", txt)) > 1500: full += 1
        d = it.findtext("pubDate") or it.findtext("a:updated", namespaces=NS) or it.findtext("a:published", namespaces=NS)
        d = parse_date(d) if d else None
        if d:
            d = d if d.tzinfo else d.replace(tzinfo=timezone.utc)
            newest = max(newest, d) if newest else d
    r.update(mit_bild=with_img, volltext=full)
    if newest: r["neuester"] = newest.date().isoformat(); r["alter_tage"] = (datetime.now(timezone.utc) - newest).days
    r["ok"] = bool(with_img) and r.get("alter_tage", 9999) <= 60
    if not r["ok"]: r["fehler"] = "keine Bilder" if not with_img else "veraltet (>60 Tage)"
    return r

res = []
for n, u in CAND:
    res.append(check(n, u)); time.sleep(2)
json.dump([r for r in res if r["ok"]], open("marketing/feeds-geprueft.json", "w"), ensure_ascii=False, indent=1)
L = ["# Feed-Prüfung", "", "Stand: " + datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"), "",
     "Nutzung: nur Titel, Vorschaubild und Link zur Originalseite anzeigen – Bilder nicht kopieren oder neu veröffentlichen.", "",
     "| Quelle | OK | Einträge | mit Bild | Volltext | neuester | Hinweis |", "|---|---|---|---|---|---|---|"]
for r in res:
    L.append(f"| [{r['name']}]({r['url']}) | {'✅' if r['ok'] else '❌'} | {r.get('items','–')} | {r.get('mit_bild','–')} | {r.get('volltext','–')} | {r.get('neuester','–')} | {r.get('fehler','')} |")
open("marketing/feed-bericht.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L))

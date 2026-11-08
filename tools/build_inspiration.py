#!/usr/bin/env python3
"""Baut inspiration/index.html aus den geprüften Feeds (marketing/feeds-geprueft.json).
Zeigt je Eintrag nur Titel, Quelle, Datum, Vorschaubild (verlinkt, nicht kopiert) und Link zur Originalseite."""
import json, re, html, urllib.request, xml.etree.ElementTree as ET, pathlib, sys
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
R = pathlib.Path(__file__).resolve().parent.parent
UA = "Mozilla/5.0 (compatible; HochzeitToolsFeedCheck/1.0; +https://tools.bride-light.de)"
NS = {"media": "http://search.yahoo.com/mrss/", "a": "http://www.w3.org/2005/Atom"}
def dt(s):
    try: d = parsedate_to_datetime(s)
    except Exception:
        try: d = datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception: return None
    return d if d.tzinfo else d.replace(tzinfo=timezone.utc)
def items(src):
    try:
        raw = urllib.request.urlopen(urllib.request.Request(src["url"], headers={"User-Agent": UA}), timeout=30).read(3_000_000)
        root = ET.fromstring(raw)
    except Exception as e:
        print("Fehler", src["name"], e, file=sys.stderr); return []
    out = []
    for it in (root.findall(".//item") or root.findall(".//a:entry", NS))[:12]:
        title = (it.findtext("title") or "").strip()
        link = it.findtext("link") or (it.find("a:link", NS).get("href") if it.find("a:link", NS) is not None else "")
        blob = " ".join((x.text or "") for x in it.iter())
        m = it.find("media:content", NS) if it.find("media:content", NS) is not None else it.find("media:thumbnail", NS)
        img = m.get("url") if m is not None else ((re.search(r'<img[^>]+src=["\']([^"\']+)', html.unescape(blob)) or [None, ""])[1])
        d = dt(it.findtext("pubDate") or it.findtext("a:updated", namespaces=NS) or it.findtext("a:published", namespaces=NS) or "")
        if title and link.startswith("http") and img.startswith("http"): out.append((d or datetime(2000, 1, 1, tzinfo=timezone.utc), title, link, img, src["name"]))
    return out
srcs = [s for s in json.load(open(R / "marketing" / "feeds-geprueft.json", encoding="utf-8")) if "reddit" not in s["url"]]
allit = sorted([i for s in srcs for i in items(s)], key=lambda x: x[0], reverse=True)[:36]
if not allit: print("Keine Einträge – Seite bleibt unverändert."); sys.exit(0)
E = html.escape
cards = "\n".join(f'<a class="tile" href="{E(l)}" target="_blank" rel="noopener nofollow"><img src="{E(i)}" alt="" loading="lazy" referrerpolicy="no-referrer" style="width:100%;height:180px;object-fit:cover;border-radius:12px"><h2>{E(t)}</h2><p>{E(n)} · {d.strftime("%d.%m.%Y")}</p></a>' for d, t, l, i, n in allit)
page = (R / "ratgeber" / "index.html").read_text(encoding="utf-8")
head = page[:page.index('<main class="wrap">')].replace("Hochzeits-Ratgeber für Mecklenburg-Vorpommern", "Hochzeits-Inspiration – aktuelle Ideen").replace("https://tools.bride-light.de/ratgeber/", "https://tools.bride-light.de/inspiration/").replace(' aria-current="page"', "")
head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="Aktuelle Hochzeits-Inspiration aus ausgewählten Blogs – mit Link zur Originalseite.">', head)
head = head.replace('<a href="../ratgeber/">Ratgeber</a>', '<a href="../ratgeber/">Ratgeber</a><a href="../inspiration/" aria-current="page">Inspiration</a>')
body = f'<main class="wrap">\n<h1>Hochzeits-Inspiration</h1>\n<p class="lead">Aktuelle Ideen aus ausgewählten Hochzeitsblogs. Ein Klick führt zur Originalseite – dort findet ihr alle Bilder und Details.</p>\n<div class="grid">\n{cards}\n</div>\n<p class="small">Stand: {datetime.now(timezone.utc).strftime("%d.%m.%Y")} · Titel, Vorschaubilder und Inhalte gehören den jeweiligen Blogs.</p>\n</main>\n'
tail = page[page.index("</main>") + len("</main>"):]
(R / "inspiration").mkdir(exist_ok=True); (R / "inspiration" / "index.html").write_text(head + body + tail.lstrip("\n"), encoding="utf-8")
print(len(allit), "Einträge")

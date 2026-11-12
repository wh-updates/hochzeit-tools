#!/usr/bin/env python3
"""SEO/GEO-Baustein: schreibt in jede Seite einen Block <!--SEO-->…<!--/SEO--> (Meta, Open Graph, JSON-LD) und sichtbare Brotkrumen,
und erzeugt sitemap.xml (mit lastmod), robots.txt, llms.txt. Idempotent – kann beliebig oft laufen."""
import re, json, html, subprocess, pathlib, datetime
R = pathlib.Path(__file__).resolve().parent.parent; B = "https://tools.bride-light.de/"; MAIN = "https://bride-light.de/"
LOGO = "https://bride-light.de/medien/70/480-weisses-herz-logo-mit-make-up-puder-pinsel-und-text-bride-un.webp?v=1"
OGIMG = "https://bride-light.de/medien/44/1600-waehrend-der-trauung.webp?v=1"
E = html.escape
TOOLS = {"budgetrechner": "Hochzeitsbudget-Rechner", "gaesteliste": "Gästelisten-Planer", "sitzplan": "Sitzplan-Planer", "getraenkerechner": "Getränkerechner für die Hochzeit", "checkliste": "Hochzeits-Checkliste mit Countdown"}
ARTICLES = {"ratgeber/heiraten-auf-ruegen": "Heiraten auf Rügen", "ratgeber/strandhochzeit-mv": "Strandhochzeit in Mecklenburg-Vorpommern",
            "ratgeber/hochzeitslocations-ruegen-ostsee": "Hochzeitslocations auf Rügen und an der Ostsee", "ratgeber/kosten-hochzeit-mv": "Kosten einer Hochzeit in Mecklenburg-Vorpommern",
            "ratgeber/hochzeitsfotograf-finden": "Hochzeitsfotograf finden – 10 Fragen", "ratgeber/heiraten-im-winter-ostsee": "Heiraten im Winter an der Ostsee"}
import sys
sys.path.insert(0, str(R / "tools"))
from content import ARTICLE_TITLES
import geo
ARTICLES.update(ARTICLE_TITLES)
try:
    from content.extra import TOOL_TITLES, LOCAL_TITLES
except Exception:
    TOOL_TITLES, LOCAL_TITLES = {}, {}
TOOLS.update(TOOL_TITLES)
LOCAL = dict(LOCAL_TITLES)
def git(*a): return subprocess.run(["git", "-C", str(R), *a], capture_output=True, text=True).stdout.strip()
def dates(rel):
    l = git("log", "--format=%cs", "--", rel).splitlines()
    today = datetime.date.today().isoformat()
    changed = bool(git("status", "--porcelain", "--", rel))   # ungespeicherte Änderung = heute geändert
    return (l[-1] if l else today), (today if (changed or not l) else l[0])
def pages():
    return ["index.html"] + [f"{k}/index.html" for k in TOOLS] + ["ratgeber/index.html"] + [f"{k}/index.html" for k in ARTICLES] + [f"{k}/index.html" for k in LOCAL]
def faq(src):
    m = re.search(r"<section[^>]*class=\"[^\"]*faq[^\"]*\"[^>]*>(.*?)</section>", src, re.S)
    if not m: return []
    out = []
    for q, a in re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", m.group(1), re.S):
        out.append((html.unescape(re.sub(r"<[^>]+>", "", q)).strip(), html.unescape(re.sub(r"<[^>]+>", "", a)).strip()))
    return out
SAMEAS = ["https://www.instagram.com/_bride_light_/", "https://www.hochzeiten-in-mv.de/portfolio/bride-light/", "https://bridebook.com/de/wedding-photographers/bride-light-i-hochzeitsfotografie-und-brautstyling-parchtitz-mecklenburg-vorpommern-deZgjKJ3mY",
          "https://web2.cylex.de/firma-home/bride-_-light---hochzeitsfotografie-_-brautstyling-17043807.html", "https://hochzeit.click/hochzeitsfotografen/bride-light/", "https://www.gelbeseiten.de/gsbiz/5cd74846-5113-4315-beab-943c00ec9efe",
          "https://www.provenexpert.com/de-de/bride-light-i-hochzeitsfotografie-und-brautstyling/", "https://www.hochzeitsportal24.de/branchenbuch/hochzeitsfotos/bride-und-light-parchtitz/",
          "https://www.unternehmensverzeichnis.org/bride--light-i-hochzeitsfotografie-und-brautstyling-auf-ruegen-parchtitz-2503230475511", "https://www.listando.com/de-de/auftragnehmer/bride-light?serviceId=rEY5oL2IiD",
          "https://www.11880.com/branchenbuch/parchtitz/150996671B113399729/bride-light-i-hochzeitsfotografie-und-brautstyling.html", "https://www.yellowmap.de/Details/I3XTGbC92eiSEKokUH5IcA==.aspx",
          "https://www.allefotografen.de/sebastian-krueger", "https://maps.app.goo.gl/ogEHwYqu63yqEZDPA"]
ORG = {"@type": ["Organization", "ProfessionalService"], "@id": MAIN + "#organization", "name": "Bride & Light", "url": MAIN, "logo": {"@type": "ImageObject", "url": LOGO},
       "description": "Hochzeitsfotografie und Brautstyling auf Rügen, in Stralsund und in ganz Mecklenburg-Vorpommern.",
       "areaServed": [{"@type": "AdministrativeArea", "name": "Mecklenburg-Vorpommern"}, {"@type": "Place", "name": "Rügen"}, {"@type": "City", "name": "Stralsund"}],
       "telephone": "+49 152 26726728", "email": "info@bride-light.de", "priceRange": "ab 690 €", "knowsLanguage": ["Deutsch", "Englisch"],
       "openingHoursSpecification": [{"@type": "OpeningHoursSpecification", "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"], "opens": "09:00", "closes": "18:00"}],
       "aggregateRating": {"@type": "AggregateRating", "ratingValue": 5, "reviewCount": 18, "bestRating": 5, "worstRating": 1},
       "employee": [{"@type": "Person", "name": "Sebastian Krüger", "jobTitle": "Hochzeitsfotograf"}, {"@type": "Person", "name": "Christine", "jobTitle": "Friseurmeisterin, Brautstyling"}],
       "sameAs": SAMEAS}
PERSON = {"@type": "Person", "@id": MAIN + "#sebastian-krueger", "name": "Sebastian Krüger", "jobTitle": "Hochzeitsfotograf", "worksFor": {"@id": MAIN + "#organization"},
          "knowsAbout": ["Hochzeitsfotografie", "Hochzeit auf Rügen", "Hochzeit in Mecklenburg-Vorpommern"], "sameAs": ["https://www.allefotografen.de/sebastian-krueger"]}
AUTHOR = {"@id": PERSON["@id"]}
SITE = {"@type": "WebSite", "@id": B + "#website", "url": B, "name": "Hochzeits-Tools von Bride & Light", "inLanguage": "de-DE", "publisher": {"@id": MAIN + "#organization"}}
def block(rel, src):
    url = B + ("" if rel == "index.html" else rel[:-len("index.html")])
    t = html.unescape(re.search(r"<title>(.*?)</title>", src, re.S).group(1)); d = html.unescape(re.search(r'<meta name="description" content="(.*?)">', src, re.S).group(1))
    key = rel[:-len("/index.html")] if rel != "index.html" else ""
    first, last = dates(rel)
    crumbs = [("Start", B)]
    if key in TOOLS: crumbs.append((TOOLS[key], url))
    elif key == "ratgeber": crumbs.append(("Ratgeber", url))
    elif key in ARTICLES: crumbs += [("Ratgeber", B + "ratgeber/"), (ARTICLES[key], url)]
    elif key == "hochzeitsfotograf": crumbs.append((LOCAL[key], url))
    elif key in LOCAL: crumbs += [(LOCAL["hochzeitsfotograf"], B + "hochzeitsfotograf/"), (LOCAL[key], url)]
    g = [ORG, PERSON, SITE]
    page = {"@type": "CollectionPage" if key in ("", "ratgeber") else "WebPage", "@id": url + "#webpage", "url": url, "name": t, "description": d, "inLanguage": "de-DE", "isPartOf": {"@id": B + "#website"},
            "primaryImageOfPage": {"@type": "ImageObject", "url": OGIMG}, "dateModified": last}
    if key not in ("", "ratgeber"): page["author"] = AUTHOR; page["publisher"] = {"@id": MAIN + "#organization"}
    if len(crumbs) > 1: page["breadcrumb"] = {"@id": url + "#breadcrumb"}
    cit = geo.sources_for(rel)
    if cit: page["citation"] = [{"@type": "CreativeWork", "name": n, "url": u} for n, u, _ in cit]
    g.append(page)
    if len(crumbs) > 1:
        g.append({"@type": "BreadcrumbList", "@id": url + "#breadcrumb", "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(crumbs)]})
    if key in TOOLS:
        g.append({"@type": "WebApplication", "@id": url + "#app", "name": TOOLS[key], "url": url, "description": d, "applicationCategory": "LifestyleApplication", "operatingSystem": "Alle (Browser)", "browserRequirements": "Benötigt JavaScript",
                  "inLanguage": "de-DE", "isAccessibleForFree": True, "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"}, "author": AUTHOR, "publisher": {"@id": MAIN + "#organization"}, "mainEntityOfPage": {"@id": url + "#webpage"}})
    if key in ARTICLES:
        h1 = html.unescape(re.sub(r"<[^>]+>", "", re.search(r"<h1>(.*?)</h1>", src, re.S).group(1)))
        g.append({"@type": "Article", "@id": url + "#article", "headline": h1, "description": d, "inLanguage": "de-DE", "image": OGIMG, "datePublished": first, "dateModified": last,
                  "author": AUTHOR, "publisher": {"@id": MAIN + "#organization"}, "mainEntityOfPage": {"@id": url + "#webpage"}})
    fq = faq(src)
    if fq: g.append({"@type": "FAQPage", "@id": url + "#faq", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in fq]})
    ld = json.dumps({"@context": "https://schema.org", "@graph": g}, ensure_ascii=False, separators=(",", ":"))
    og = "article" if key in ARTICLES else "website"
    head = f'''<!--SEO-->
<meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1">
<meta name="theme-color" content="#f4e6e3">
<link rel="icon" href="{LOGO}" type="image/webp">
<link rel="apple-touch-icon" href="{LOGO}">
<link rel="alternate" hreflang="de" href="{url}"><link rel="alternate" hreflang="x-default" href="{url}">
<link rel="alternate" type="application/rss+xml" title="Hochzeit-Tools &amp; Ratgeber" href="{B}feed-flipboard.xml">
<meta property="og:type" content="{og}"><meta property="og:site_name" content="Hochzeits-Tools von Bride &amp; Light"><meta property="og:locale" content="de_DE">
<meta property="og:title" content="{E(t)}"><meta property="og:description" content="{E(d)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{OGIMG}"><meta property="og:image:alt" content="Brautpaar im Strandkorb vor dem Meer – Hochzeitsfoto von Bride &amp; Light">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{E(t)}"><meta name="twitter:description" content="{E(d)}"><meta name="twitter:image" content="{OGIMG}">
<script type="application/ld+json">{ld}</script>
<!--/SEO-->'''
    return head, crumbs, url, last
for rel in pages():   # Vorlauf: GEO-Blöcke einfügen (Datum folgt in der Hauptschleife, damit dates() die Änderung sieht)
    p = R / rel; s0 = p.read_text(encoding="utf-8"); s1 = geo.apply(rel, s0, "@@STANDISO@@", geo.STAND)
    if s1 != s0: p.write_text(s1, encoding="utf-8")
sitemap = []
for rel in pages():
    p = R / rel; s = p.read_text(encoding="utf-8")
    s = re.sub(r"\n?<!--SEO-->.*?<!--/SEO-->", "", s, flags=re.S)
    s = re.sub(r'\n?<link rel="alternate" type="application/rss\+xml"[^>]*>', "", s)   # alter Einzeleintrag (jetzt im Block)
    head, crumbs, url, last = block(rel, s)
    s = s.replace("@@STANDISO@@", last).replace(geo.STAND, datetime.date.fromisoformat(last).strftime("%d.%m.%Y"))
    s = s.replace("</head>", head + "\n</head>", 1)
    s = re.sub(r'<nav class="crumbs".*?</nav>\n?', "", s, flags=re.S)
    if len(crumbs) > 1:
        nav = '<nav class="crumbs" aria-label="Brotkrumen">' + " › ".join(f'<a href="{u}">{E(n)}</a>' if i < len(crumbs) - 1 else f'<span aria-current="page">{E(n)}</span>' for i, (n, u) in enumerate(crumbs)) + "</nav>\n"
        s = s.replace('<main class="wrap">\n', '<main class="wrap">\n' + nav, 1) if '<main class="wrap">\n' in s else s.replace('<main class="wrap">', '<main class="wrap">\n' + nav, 1)
    s = s.replace("style.css?v=3", "style.css?v=4")
    p.write_text(s, encoding="utf-8")
    sitemap.append((url, last, "1.0" if rel == "index.html" else ("0.9" if rel.split("/")[0] in TOOLS or rel.startswith("ratgeber/") else "0.8")))
(R / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(f"<url><loc>{u}</loc><lastmod>{d}</lastmod></url>" for u, d, _ in sitemap) + "\n</urlset>\n", encoding="utf-8")
bots = ["GPTBot", "OAI-SearchBot", "ChatGPT-User", "ClaudeBot", "Claude-User", "Claude-SearchBot", "PerplexityBot", "Google-Extended", "Applebot-Extended", "CCBot", "Bingbot", "Googlebot"]
(R / "robots.txt").write_text("User-agent: *\nAllow: /\n\n" + "".join(f"User-agent: {b}\nAllow: /\n\n" for b in bots) + f"Sitemap: {B}sitemap.xml\n", encoding="utf-8")
tool_lines = "\n".join(f"- [{n}]({B}{k}/): {html.unescape(re.search(r'<meta name=\"description\" content=\"(.*?)\">', (R / k / 'index.html').read_text(encoding='utf-8'), re.S).group(1))}" for k, n in TOOLS.items())
loc_lines = "\n".join(f"- [{n}]({B}{k}/): {html.unescape(re.search(r'<meta name=\"description\" content=\"(.*?)\">', (R / k / 'index.html').read_text(encoding='utf-8'), re.S).group(1))}" for k, n in LOCAL.items())
art_lines = "\n".join(f"- [{n}]({B}{k}/): {html.unescape(re.search(r'<meta name=\"description\" content=\"(.*?)\">', (R / k / 'index.html').read_text(encoding='utf-8'), re.S).group(1))}" for k, n in ARTICLES.items())
(R / "llms.txt").write_text(f"""# Hochzeits-Tools von Bride & Light

> Kostenlose Online-Tools und Ratgeber für die Hochzeitsplanung, besonders für Hochzeiten an der Ostsee, auf Rügen und in Mecklenburg-Vorpommern. Alle Tools laufen ohne Anmeldung im Browser; Eingaben bleiben im eigenen Browser gespeichert (localStorage). Herausgeber ist Bride & Light, Hochzeitsfotografie und Brautstyling auf Rügen, in Stralsund und in ganz Mecklenburg-Vorpommern ({MAIN}).

## Herausgeber
- Bride & Light, Hochzeitsfotografie und Brautstyling, https://bride-light.de/
- Einsatzgebiet: Rügen, Stralsund, Mecklenburg-Vorpommern. Sprachen: Deutsch, Englisch
- Kontakt: info@bride-light.de, +49 152 26726728 (Mo-Fr 9-18 Uhr)
- Hochzeitsfotografie ab 690 €

## Planungs-Tools (kostenlos)
{tool_lines}

## Ratgeber Mecklenburg-Vorpommern
{art_lines}
- [Alle Ratgeber]({B}ratgeber/)

## Hochzeitsfotografie in Mecklenburg-Vorpommern
{loc_lines}

## Über den Anbieter
- [Bride & Light – Hochzeitsfotografie und Brautstyling]({MAIN}): Startseite des Studios
- [Hochzeitsfotograf Rügen]({MAIN}hochzeitsfotograf-ruegen)

## Hinweise
- Sprache: Deutsch. Preise: alle Tools kostenlos. Es werden keine personenbezogenen Daten an einen Server gesendet.
- Methodik: Rechner-Seiten erklären unter „So rechnet das Tool“ die verwendeten Formeln und Standardwerte; Rechtsthemen nennen Quellen (Gesetze im Internet).
- Zitieren erwünscht, bitte mit Link auf die jeweilige Seite von {B}.
""", encoding="utf-8")
print("Seiten:", len(sitemap))

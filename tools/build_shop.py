"""Erzeugt die Verkaufsseiten unter /shop/ (Digistore24-Produkte).
Kauf-Links werden NUR in shop/links.js eingetragen. Solange ein Link leer ist,
zeigt der Button "Bald erhältlich". Seiten stehen auf noindex, bis die Produkte freigegeben sind.
Aufruf: python3 tools/build_shop.py
"""
import os, html, glob
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC_IMG = '/home/claude/out/digistore'
LOGO = 'https://bride-light.de/medien/70/480-weisses-herz-logo-mit-make-up-puder-pinsel-und-text-bride-un.webp?v=1'
INDEX = False  # nach Freigabe durch Digistore24 auf True setzen + in sitemap.xml aufnehmen

P = [
 dict(slug='hochzeit-planen-12-monate', folder='01', title='Hochzeit planen in 12 Monaten', price='14,90', kind='E-Book · PDF · 9 Seiten',
      lead='Der stressfreie Fahrplan vom Antrag bis zum Ja-Wort – mit Checklisten für jede Phase.',
      who=['Ihr seid frisch verlobt und wisst nicht, wo ihr anfangen sollt.', 'Ihr wollt den Überblick behalten, statt in 40 Browser-Tabs zu planen.', 'Ihr habt 6–18 Monate Zeit bis zur Hochzeit.'],
      inside=['Die vier Grundsatzentscheidungen vor der ersten Buchung', 'Budget realistisch planen – mit Richtwerten zur Verteilung', 'Monat 12–10: die großen Buchungen',
              'Monat 9–7: Dienstleister & Outfits', 'Monat 6–4: Standesamt, Einladungen, Details', 'Monat 3–1: Feinschliff & Ablaufplan', 'Die letzte Woche', 'Der Hochzeitstag', 'Nach der Hochzeit']),
 dict(slug='brautstyling-guide', folder='02', title='Der Brautstyling-Guide', price='12,90', kind='E-Book · PDF · 7 Seiten',
      lead='Haare & Make-up perfekt am Hochzeitstag – geschrieben von Brautstylisten.',
      who=['Du willst deinen Brautlook finden, der wirklich zu dir passt.', 'Du willst den Probetermin optimal nutzen.', 'Du willst am Hochzeitsmorgen entspannt bleiben.'],
      inside=['Den eigenen Stil finden – Frisur passend zum Kleid', 'Haare vorbereiten: Zeitplan bis zum Tag', 'Hautvorbereitung ohne Experimente', 'Make-up, das bis zum letzten Tanz hält',
              'Der Probetermin: Checkliste', 'Zeitplan für den Hochzeitsmorgen', 'Notfalltasche & Tipps für den ganzen Tag']),
 dict(slug='traumhafte-hochzeitsfotos', folder='03', title='Traumhafte Hochzeitsfotos', price='12,90', kind='E-Book · PDF · 7 Seiten',
      lead='Der Guide für Brautpaare – von Hochzeitsfotografen, die jedes Jahr viele Hochzeiten begleiten.',
      who=['Ihr sucht eine Fotografin und wollt wissen, worauf es ankommt.', 'Ihr findet euch „unfotogen“.', 'Ihr wollt euren Tag so planen, dass schöne Bilder möglich sind.'],
      inside=['Die richtige Fotografin finden', 'Wie viele Stunden Begleitung ihr braucht', 'Licht verstehen – und den Zeitplan danach ausrichten', 'Entspannt vor der Kamera',
              'Zeitplan mit Puffer', 'Gruppenfotos ohne Chaos', 'Unplugged Wedding', 'Bilder sichern & genießen']),
 dict(slug='hochzeit-kleines-budget', folder='04', title='Schöne Hochzeit, kleines Budget', price='9,90', kind='E-Book · PDF · 7 Seiten',
      lead='60 Spartipps zum Abhaken – und ehrlich gesagt, wo Sparen sich rächt.',
      who=['Euer Budget ist begrenzt, euer Anspruch nicht.', 'Ihr wollt wissen, wo die großen Hebel liegen.', 'Ihr wollt Prioritäten setzen statt überall ein bisschen zu sparen.'],
      inside=['Die 3-Säulen-Methode für eure Prioritäten', 'Die größten Spar-Hebel', '60 konkrete Spartipps nach Bereichen', 'Wo ihr nicht sparen solltet', 'Zwei Beispielbudgets (40 und 70 Gäste)']),
 dict(slug='heiraten-an-der-ostsee', folder='05', title='Heiraten an der Ostsee', price='12,90', kind='E-Book · PDF · 7 Seiten',
      lead='Der Hochzeitsguide für Mecklenburg-Vorpommern – von einem Team aus der Region.',
      who=['Ihr träumt von einer Hochzeit am Meer, auf Rügen, Usedom oder an der Seenplatte.', 'Ihr kommt von außerhalb und kennt die Region noch nicht.', 'Ihr plant eine Strandhochzeit.'],
      inside=['Warum Mecklenburg-Vorpommern', 'Standesamt an besonderen Orten', 'Strandhochzeit: Genehmigung, Wind, Plan B', 'Die beste Jahreszeit', 'Unterkünfte & Anreise', 'Regionale Ideen', 'Checkliste Küstenhochzeit']),
 dict(slug='winterhochzeit-guide', folder='06', title='Winterhochzeit', price='9,90', kind='E-Book · PDF · 6 Seiten',
      lead='Gemütlich heiraten von November bis März – mit Licht-Planung, Outfit-Tipps und Plan B.',
      who=['Ihr heiratet in der kalten Jahreszeit.', 'Ihr wollt wissen, wie ihr trotz kurzer Tage schöne Fotos bekommt.', 'Ihr wollt euch gegen Wetter absichern.'],
      inside=['Warum im Winter heiraten', 'Das Licht im Winter', 'Outfit & Styling – schön und warm', 'Location & Deko', 'Wetter & Plan B', 'Beispiel-Zeitplan', 'Checkliste']),
 dict(slug='hochzeitsrede', folder='07', title='Die perfekte Hochzeitsrede', price='9,90', kind='E-Book · PDF · 7 Seiten',
      lead='Leitfaden & Vorlagen für Trauzeugen, Eltern, Brautpaar und Freunde.',
      who=['Du sollst eine Rede halten und weißt nicht, wie anfangen.', 'Du hast Lampenfieber.', 'Du willst persönlich statt Zitate aus dem Internet.'],
      inside=['Die Grundregeln guter Reden', 'Die 5-Teile-Struktur', 'Fragen, die Geschichten hervorbringen', 'Vorlage Trauzeuge/Trauzeugin', 'Vorlage Brautpaar', 'Vorlage Eltern', 'Vortragen ohne Lampenfieber', '10 Trinksprüche']),
 dict(slug='jga-planer', folder='08', title='Der JGA-Planer', price='9,90', kind='E-Book · PDF · 6 Seiten',
      lead='Den Junggesellinnenabschied organisieren – mit Programmen, Spielen und Kostenplan.',
      who=['Du bist Trauzeugin oder beste Freundin und organisierst den JGA.', 'Du willst etwas, das zur Braut passt.', 'Du willst Geld und Organisation sauber regeln.'],
      inside=['Planung: wer, wann, wie viel', 'Ideen nach Brauttyp', 'Drei fertige Programme', 'Spiele & Partner-Quiz', 'Organisation & Kostenplan', 'Checkliste']),
 dict(slug='trauzeugen-handbuch', folder='09', title='Das Trauzeugen-Handbuch', price='9,90', kind='E-Book · PDF · 6 Seiten',
      lead='Alles für die rechte Hand des Brautpaars – Aufgaben, Zeitplan, Notfälle.',
      who=['Du wurdest gefragt, Trauzeugin oder Trauzeuge zu sein.', 'Du willst dem Paar den Tag so leicht wie möglich machen.', 'Du willst auf Notfälle vorbereitet sein.'],
      inside=['Die Rolle heute', 'Aufgaben vor der Hochzeit', 'Der Hochzeitsmorgen & die Notfalltasche', 'Während der Feier', 'Typische Probleme & Lösungen', 'Nach der Feier']),
 dict(slug='hochzeits-bundle', folder='10', title='Das große Hochzeits-Bundle', price='39,00', kind='ZIP · 10 Vorlagen + 2 E-Books',
      lead='Alles, was ihr für die Planung braucht – zum Bundle-Preis statt über 85 € einzeln.',
      who=['Ihr wollt alle Planungsvorlagen auf einmal.', 'Ihr wollt Excel-Tabellen, die automatisch rechnen.', 'Ihr wollt Vorlagen zum Bearbeiten und Ausdrucken.'],
      inside=['Premium-Hochzeitsplaner (29 Seiten, PDF)', 'Budgetplaner (Excel / Google Sheets)', 'Gästeliste mit Zusagen & Tischplanung (Excel)', 'Sitzplan-Planer (PDF)',
              'Platzkarten & Tischnummern (Word)', 'Menü- & Getränkekarte (Word)', 'Ablaufplan Hochzeitstag (Word)', 'Hochzeitsspiele-Set (PDF)', 'Foto-Shotlist & Fotografen-Briefing (PDF)',
              'Brautstyling-Planer (PDF)', 'E-Book „Hochzeit planen in 12 Monaten“', 'E-Book „Traumhafte Hochzeitsfotos“']),
]

E = lambda s: html.escape(s, quote=True)
ROBOTS = 'index,follow' if INDEX else 'noindex,follow'


def head(title, desc, url, img, pre):
    return f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="{pre}assets/style.css?v=5">
<link rel="stylesheet" href="{pre}shop/shop.css?v=1">
<meta name="robots" content="{ROBOTS}">
<meta name="theme-color" content="#f4e6e3">
<link rel="icon" href="{LOGO}" type="image/webp">
<meta property="og:type" content="product"><meta property="og:site_name" content="Bride &amp; Light"><meta property="og:locale" content="de_DE">
<meta property="og:title" content="{E(title)}"><meta property="og:description" content="{E(desc)}"><meta property="og:url" content="{url}"><meta property="og:image" content="https://tools.bride-light.de/{img}">
</head>
<body>
<header class="site"><div class="wrap"><a class="brand" href="{pre}"><img src="{LOGO}" alt="Bride &amp; Light" width="56" height="56"><span><b>Hochzeits-Tools</b><small>von Bride &amp; Light</small></span></a>
<nav><a href="{pre}budgetrechner/">Budget</a><a href="{pre}gaesteliste/">Gästeliste</a><a href="{pre}sitzplan/">Sitzplan</a><a href="{pre}getraenkerechner/">Getränke</a><a href="{pre}checkliste/">Checkliste</a><a href="{pre}ratgeber/">Ratgeber</a><a href="{pre}shop/" aria-current="page">Shop</a><a class="nav-cta" href="https://bride-light.de/?utm_source=tools&amp;utm_medium=nav&amp;utm_campaign=header">Zu Bride &amp; Light</a></nav></div></header>
'''


def foot(pre):
    return f'''<footer class="site"><div class="wrap foot-grid">
<div class="foot-brand"><img src="{LOGO}" alt="Bride &amp; Light" width="96" height="96" loading="lazy"><p>Hochzeitsfotografie und Brautstyling<br>auf Rügen, in Stralsund und ganz MV.</p></div>
<div><h3>Shop</h3><a href="{pre}shop/">Alle Produkte</a><a href="{pre}shop/hochzeits-bundle/">Hochzeits-Bundle</a></div>
<div><h3>Bride &amp; Light</h3><a href="https://bride-light.de/?utm_source=tools&amp;utm_medium=footer&amp;utm_campaign=shop">Startseite</a><a href="https://bride-light.de/?utm_source=tools&amp;utm_medium=footer&amp;utm_campaign=shop#kontakt">Kontakt</a><a href="https://instagram.com/_bride_light_">Instagram</a></div>
<div><h3>Rechtliches</h3><a href="https://bride-light.de/impressum">Impressum</a><a href="https://bride-light.de/datenschutzerklarung">Datenschutz</a><a href="https://bride-light.de/agb">AGB</a></div>
</div><div class="wrap foot-copy">© Bride &amp; Light · Der Verkauf erfolgt über Digistore24 als Wiederverkäufer.</div></footer>
<script src="{pre}shop/links.js?v=1"></script>
<script src="{pre}shop/shop.js?v=1"></script>
</body>
</html>
'''


def buybox(p):
    return f'''<div class="buybox" id="kaufen"><p class="price">{p["price"]} €</p><p class="kind">{E(p["kind"])}</p>
<a class="btn buy" data-product="{p["slug"]}" href="#kaufen" aria-disabled="true">Bald erhältlich</a>
<p class="fine">Sofort-Download nach dem Kauf · Sichere Zahlung über Digistore24 (PayPal, Karte, Überweisung u. a.) · inkl. MwSt.</p></div>'''


FAQ = [('Wie bekomme ich das Produkt?', 'Direkt nach dem Kauf erhaltet ihr per E-Mail einen Download-Link. Es wird nichts verschickt.'),
       ('Welche Programme brauche ich?', 'PDFs öffnet jeder PDF-Reader. Excel-Vorlagen funktionieren mit Excel, Google Sheets und Numbers; Word-Vorlagen mit Word, LibreOffice oder Google Docs.'),
       ('Kann ich das Produkt zurückgeben?', 'Bei digitalen Inhalten erlischt das Widerrufsrecht, sobald ihr dem sofortigen Download ausdrücklich zustimmt. Die genauen Bedingungen seht ihr im Bestellprozess von Digistore24.'),
       ('Wer steckt dahinter?', 'Wir sind Bride &amp; Light – Hochzeitsfotografie und Brautstyling in Mecklenburg-Vorpommern. Unsere Produkte basieren auf unserer Arbeit mit vielen Brautpaaren.')]


def page(p):
    pre = '../../'; url = f'https://tools.bride-light.de/shop/{p["slug"]}/'; img = f'assets/img/shop/{p["slug"]}.webp'
    out = head(f'{p["title"]} – {p["kind"].split(" · ")[0]} von Bride & Light', p['lead'], url, img, pre)
    out += f'''<main class="wrap shop">
<nav class="crumbs" aria-label="Brotkrumen"><a href="{pre}">Start</a> › <a href="../">Shop</a> › <span aria-current="page">{E(p["title"])}</span></nav>
<section class="phero"><div><p class="eyebrow">{E(p["kind"])}</p><h1>{E(p["title"])}</h1><p class="lead">{E(p["lead"])}</p>{buybox(p)}</div>
<div><img class="pimg" src="{pre}{img}" alt="Vorschau: {E(p["title"])}" width="1200" height="960"></div></section>
<section class="card"><h2>Für euch, wenn …</h2><ul class="ticks">{"".join(f"<li>{E(w)}</li>" for w in p["who"])}</ul></section>
<section class="card"><h2>Das steckt drin</h2><ol class="inside">{"".join(f"<li>{E(i)}</li>" for i in p["inside"])}</ol></section>
<section class="card trust"><h2>Aus der Praxis, nicht aus dem Lehrbuch</h2><p>Wir begleiten als Hochzeitsfotografen und Brautstylisten Paare an ihrem großen Tag. In unsere Produkte fließt, was wir dort jedes Mal sehen: was funktioniert, was Stress macht und was am Ende wirklich zählt.</p>
<p class="fine">Bei der Erstellung wurden KI-Werkzeuge unterstützend eingesetzt; alle Inhalte wurden von uns geprüft.</p></section>
<section class="card"><h2>Häufige Fragen</h2>{"".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q, a in FAQ)}</section>
<section class="card center"><h2>{E(p["title"])}</h2>{buybox(p).replace('id="kaufen"', '')}</section>
</main>
'''
    return out + foot(pre)


def index():
    pre = '../'
    out = head('Shop – Hochzeitsplaner, Vorlagen & E-Books von Bride & Light', 'Hochzeitsplaner, Excel-Vorlagen und E-Books von Hochzeitsfotografen und Brautstylisten – als Sofort-Download.',
               'https://tools.bride-light.de/shop/', 'assets/img/shop/hochzeits-bundle.webp', pre)
    tiles = ''.join(f'<a class="tile" href="{p["slug"]}/"><img class="ico" src="{pre}assets/img/shop/{p["slug"]}.webp" alt="" loading="lazy"><h2>{E(p["title"])}</h2><p>{E(p["lead"])}</p><p class="tprice">{p["price"]} €</p></a>' for p in P)
    out += f'''<main class="wrap shop">
<nav class="crumbs" aria-label="Brotkrumen"><a href="{pre}">Start</a> › <span aria-current="page">Shop</span></nav>
<h1>Shop</h1><p class="lead">Planer, Vorlagen und E-Books – aus unserer Arbeit als Hochzeitsfotografen und Brautstylisten. Sofort-Download.</p>
<div class="grid">{tiles}</div>
<div class="card"><h2>Lieber kostenlos?</h2><p>Unsere Online-Tools und der Basis-Planer als PDF bleiben selbstverständlich gratis.</p><a class="btn ghost" href="{pre}">Zu den kostenlosen Tools</a></div>
</main>
'''
    return out + foot(pre)


CSS = '''.shop .phero{display:grid;gap:2rem;grid-template-columns:1.1fr 1fr;align-items:center;margin:1rem 0 2rem}
@media(max-width:800px){.shop .phero{grid-template-columns:1fr}.shop .phero>div:last-child{order:-1}}
.shop .pimg{width:100%;height:auto;border-radius:18px;box-shadow:0 10px 30px -18px rgba(138,74,80,.5)}
.shop .eyebrow{color:var(--gold);text-transform:uppercase;letter-spacing:.12em;font-size:.8rem;margin:0}
.buybox{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:1.2rem 1.4rem;margin-top:1.2rem}
.buybox .price{font-family:var(--serif);font-size:2.2rem;color:var(--accent-d);margin:0}
.buybox .kind{color:var(--muted);margin:.1rem 0 .8rem}
.buybox .btn{font-size:1.05rem;padding:.85rem 2rem}
.buybox .btn[aria-disabled="true"]{background:var(--muted);cursor:default;pointer-events:none}
.fine{font-size:.8rem;color:var(--muted);margin:.7rem 0 0}
.ticks{list-style:none;padding:0}.ticks li{padding-left:1.6rem;position:relative;margin:.45rem 0}
.ticks li:before{content:"\\2665";position:absolute;left:0;color:var(--gold)}
.inside{columns:2;column-gap:2rem}@media(max-width:700px){.inside{columns:1}}.inside li{margin:.35rem 0;break-inside:avoid}
.shop details{border-top:1px solid var(--line);padding:.7rem 0}.shop summary{cursor:pointer;font-weight:600}
.shop .center{text-align:center}.shop .center .buybox{max-width:420px;margin:1rem auto 0}
.tile .tprice{color:var(--accent-d);font-weight:700;margin-top:.5rem}
'''

LINKS = '''// Digistore24-Kauflinks. Nach Freigabe eines Produkts hier den Bestell-Link eintragen,
// z. B. "https://www.digistore24.com/product/123456". Leer = Button zeigt "Bald erhältlich".
window.SHOP_LINKS = {
''' + ''.join(f'  "{p["slug"]}": "",\n' for p in P) + '};\n'

JS = '''(function () {
  var L = window.SHOP_LINKS || {};
  document.querySelectorAll('a.buy').forEach(function (a) {
    var url = L[a.getAttribute('data-product')];
    if (url) { a.href = url; a.textContent = 'Jetzt kaufen'; a.removeAttribute('aria-disabled'); a.rel = 'nofollow'; }
  });
})();
'''


def main():
    os.makedirs(f'{ROOT}/assets/img/shop', exist_ok=True)
    for p in P:
        src = glob.glob(f'{SRC_IMG}/{p["folder"]}_*/Produktbild.jpg')
        dst = f'{ROOT}/assets/img/shop/{p["slug"]}.webp'
        if src: Image.open(src[0]).convert('RGB').resize((1200, 960), Image.LANCZOS).save(dst, 'WEBP', quality=82)
        assert os.path.exists(dst), dst
        os.makedirs(f'{ROOT}/shop/{p["slug"]}', exist_ok=True)
        open(f'{ROOT}/shop/{p["slug"]}/index.html', 'w').write(page(p))
    open(f'{ROOT}/shop/index.html', 'w').write(index())
    open(f'{ROOT}/shop/shop.css', 'w').write(CSS)
    open(f'{ROOT}/shop/shop.js', 'w').write(JS)
    lp = f'{ROOT}/shop/links.js'
    if not os.path.exists(lp): open(lp, 'w').write(LINKS)  # eingetragene Links nie überschreiben
    print('ok', len(P))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""GEO-Baustein (sichtbar): Herausgeber + Stand unter der Einleitung, „So rechnet das Tool“ (Methodik), „Quellen“.
Wird von seo_apply.py je Seite aufgerufen (idempotent, Marker <!--GEO-->…<!--/GEO-->, im White-Label-Build entfernt).
Alle Zahlen in METHODE stammen aus dem Code der jeweiligen Tools (tools/toolsrc/*.js bzw. Inline-Skript der Seite) – bei Änderung dort hier nachziehen."""
import re, html

E = html.escape
STAND = "@@STAND@@"   # wird von seo_apply.py durch das Datum (TT.MM.JJJJ) ersetzt

# Methodik je Tool: Liste (Überschrift, [Sätze]) – nur Fakten aus dem Tool-Code
METHODE = {
    "budgetrechner": ["Die Standardverteilung ist ein Richtwert: Essen & Getränke 28 %, Location & Miete 20 %, Fotografie & Video 10 %, Brautkleid & Accessoires 7 %, Deko & Blumen 7 %, Musik 6 %, Puffer 6 %, Ringe 5 %, dazu kleinere Posten (zusammen 100 %).",
                      "Geplant = Gesamtbudget × Anteil. Tatsächliche Kosten tragt ihr selbst ein; der Rechner markiert Posten, die über Plan liegen. Alle Anteile sind frei änderbar, die Summe sollte 100 % ergeben."],
    "getraenkerechner": ["Berechnet wird je Getränk ein Liter-Wert plus 10 % Reserve: Sekt = Erwachsene × Gläser × 0,1 l; Wein = Erwachsene × Weintrinker-Anteil × (0,2 l in der ersten Stunde + 0,15 l je weiterer Stunde); Bier = Erwachsene × Biertrinker-Anteil × (0,5 l + 0,33 l je weiterer Stunde).",
                         "Wasser: 0,3 l je Erwachsenem und 0,35 l je Kind pro Stunde; Softdrinks: 0,2 l je Erwachsenem und 0,4 l je Kind pro Stunde. Bei „Sommer / heiß“ steigen Wasser und Softdrinks um den Faktor 1,25. Kaffee: 1,5 Tassen je Erwachsenem. Flaschen und Kisten werden aufgerundet.",
                         "Das sind Erfahrungswerte, keine Garantie – Trinkgewohnheiten eurer Gäste und die Jahreszeit verschieben die Menge."],
    "hochzeitstorte-rechner": ["Benötigte Portionen = Gäste × Anteil der Tortenesser. Die Fläche je Portion hängt von der Stückgröße ab (Klein 20 cm², Normal 28 cm², Groß 38 cm²).",
                               "Die Etagen sind rund, jede Etage ist 6 cm breiter als die darüber und 10 cm hoch. Der Rechner erhöht den Durchmesser der obersten Etage in 2-cm-Schritten, bis die Gesamtfläche für alle Portionen reicht; das Gewicht ergibt sich aus Volumen × 0,85 g/cm³ als Näherung."],
    "fotostunden-rechner": ["Gerechnet wird die Summe der angehakten Programmpunkte vor der Trauung, der Trauungsdauer und der angehakten Punkte danach (jeweils mit der eingetragenen Dauer in Minuten).",
                            "Dazu kommen 10 % Puffer, aufgerundet auf volle 5 Minuten. Das Ergebnis wird auf halbe Stunden aufgerundet. Der Beginn ergibt sich rückwärts aus der Trauungszeit."],
    "einladungs-rechner": ["Einladungen = Haushalte × (1 + Reserve in %), aufgerundet. Mit Save-the-Date verdoppelt sich die Kartenzahl.",
                           "Kosten = Karten × Preis je Karte inkl. Umschlag, Porto = Haushalte × Porto je Brief (ohne Reserve; bei Save-the-Date doppelt). Die Preisvorgaben (Karte, Porto) sind Platzhalter und lassen sich ändern – prüft das aktuelle Porto der Post."],
    "gastgeschenke-rechner": ["Stückzahl = Gäste × (1 + Reserve in %), aufgerundet. Im Modus „Gesamtbudget“ ist der Preis je Stück = Budget ÷ Stückzahl, im Modus „Preis pro Stück“ ist die Summe = Preis × Stückzahl.",
                              "Die Ideen sind nach vier Preisstufen sortiert (bis 1,50 €, bis 3 €, bis 6 €, darüber)."],
    "goldene-stunde": ["Sonnenauf- und -untergang folgen der Näherung der US-Wetterbehörde NOAA (Sonnendeklination und Zeitgleichung, vier Iterationen) für den gewählten Ort und das Datum; Zeiten in Mitteleuropäischer Zeit bzw. Sommerzeit (Europe/Berlin).",
                       "Sonnenauf- und -untergang gelten bei −0,833° Sonnenhöhe, die Goldene Stunde ab +6° Sonnenhöhe, die Blaue Stunde zwischen Sonnenuntergang und −6°. Wolken, Horizont (Wald, Hügel, Gebäude) und Wetter sind nicht berücksichtigt. Abweichung zu amtlichen Tabellen: wenige Minuten."],
    "hochzeitsdatum-finder": ["Feiertage werden im Browser berechnet: Ostern nach der Gaußschen Osterformel, bewegliche Feiertage daraus abgeleitet; welche zusätzlichen Landesfeiertage gelten, ist je Bundesland hinterlegt (z. B. Mecklenburg-Vorpommern: Reformationstag und Internationaler Frauentag).",
                              "Schulferien und die Öffnungszeiten der Standesämter sind nicht enthalten – bitte direkt bei den zuständigen Stellen prüfen."],
}

# Quellen je Seite: Liste (Titel, URL, Hinweis) – nur geprüfte Links
Q_PSTG = ("§ 12 Personenstandsgesetz – Anmeldung der Eheschließung", "https://www.gesetze-im-internet.de/pstg/__12.html", "Rechtsgrundlage der Anmeldung beim Standesamt")
Q_BGB = ("§ 1310 BGB – Zuständigkeit des Standesbeamten", "https://www.gesetze-im-internet.de/bgb/__1310.html", "Rechtsgrundlage: Die Ehe wird vor dem Standesbeamten geschlossen")
Q_NOAA = ("NOAA – Solar Calculation Details", "https://gml.noaa.gov/grad/solcalc/calcdetails.html", "Formeln für Sonnenstand, Auf- und Untergang")
QUELLEN = {
    "ratgeber/standesamt-unterlagen": [Q_PSTG, Q_BGB],
    "ratgeber/standesaemter-ruegen": [Q_PSTG, Q_BGB],
    "ratgeber/freie-trauung-mv": [Q_BGB, Q_PSTG],
    "ratgeber/strandhochzeit-mv": [Q_PSTG, Q_BGB],
    "goldene-stunde": [Q_NOAA],
    "hochzeitsdatum-finder": [("Feiertage Mecklenburg-Vorpommern – schulferien.org", "https://www.schulferien.org/deutschland/feiertage/mecklenburg-vorpommern/", "Gesetzliche Feiertage in MV je Jahr (u. a. Internationaler Frauentag, Reformationstag)")],
}
HINWEIS_RECHT = "Welche Unterlagen und Fristen konkret gelten, entscheidet das zuständige Standesamt – bitte dort rechtzeitig nachfragen. Dieser Beitrag ersetzt keine Rechtsberatung."


def _byline(rel):
    kind = "Rechner" if rel.split("/")[0] in METHODE else ("Beitrag" if rel.startswith("ratgeber/") or rel.startswith("hochzeitsfotograf") else "Tool")
    kostenlos = " · kostenlos, ohne Anmeldung" if kind != "Beitrag" else ""
    return (f'<p class="geo-meta noprint">Autor: Sebastian Krüger, Hochzeitsfotograf · Herausgeber: <a href="https://bride-light.de/">Bride &amp; Light</a>, Hochzeitsfotografie und Brautstyling auf Rügen · '
            f'Stand: <time datetime="@@STANDISO@@">{STAND}</time>{kostenlos}</p>')


def top(rel):
    if rel in ("index.html", "ratgeber/index.html"):
        return ""
    return f'<!--GEO-->{_byline(rel)}<!--/GEO-->'


def bottom(rel):
    key = rel[:-len("/index.html")] if rel != "index.html" else ""
    parts = []
    if key in METHODE:
        ps = "".join(f"<p>{E(t, quote=False)}</p>" for t in METHODE[key])
        parts.append(f'<section class="card geo-how" aria-label="So rechnet das Tool"><h2>So rechnet das Tool</h2>{ps}</section>')
    if key in QUELLEN:
        li = "".join(f'<li><a href="{u}" rel="noopener" target="_blank">{E(t, quote=False)}</a> – {E(n, quote=False)}</li>' for t, u, n in QUELLEN[key])
        extra = f'<p class="muted">{E(HINWEIS_RECHT, quote=False)}</p>' if "Personenstandsgesetz" in QUELLEN[key][0][0] or "BGB" in QUELLEN[key][0][0] else ""
        parts.append(f'<section class="card geo-src" aria-label="Quellen"><h2>Quellen</h2><ul>{li}</ul>{extra}</section>')
    return f'<!--GEO2-->{"".join(parts)}<!--/GEO2-->' if parts else ""


def apply(rel, s, date_iso, date_de):
    """Fügt die Blöcke ein (zuvor entfernen). Rückgabe: neuer HTML-Text."""
    s = re.sub(r"\n?<!--GEO-->.*?<!--/GEO-->", "", s, flags=re.S)
    s = re.sub(r"\n?<!--GEO2-->.*?<!--/GEO2-->", "", s, flags=re.S)
    t = top(rel)
    if t:
        t = t.replace("@@STANDISO@@", date_iso).replace(STAND, date_de)
        m = re.search(r'<p class="lead">.*?</p>', s, re.S) or re.search(r"<h1>.*?</h1>", s, re.S)
        if m: s = s[:m.end()] + "\n" + t + s[m.end():]
    b = bottom(rel)
    if b:
        # vor „Mehr zum Thema“ bzw. Eigenwerbung/Pin, sonst direkt vor </main>
        m = re.search(r"<!--RELATED-->|<!--PROMO-->|<!--PIN-->", s)
        pos = m.start() if m else s.find("</main>")
        if pos > 0: s = s[:pos] + b + "\n" + s[pos:]
    return s


def sources_for(rel):
    key = rel[:-len("/index.html")] if rel != "index.html" else ""
    return QUELLEN.get(key, [])

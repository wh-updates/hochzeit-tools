# Pin- und Seiten-Plan bis Silvester 2026

Ziel: **1 Pin pro Feed und Tag** (planung, ostsee, winter) vom 10.11. bis 31.12.2026 = 52 Tage × 3 Feeds = **156 Pins**.
Vorhanden (Stand 9.11.): 29 wartende Pins (planung 19, ostsee 7, winter 3). Der Rest entsteht aus den Seiten unten.

## Regeln für Abwechslung
- **Das Bild zeigt genau das Thema des Pins, nie ein allgemeines Bild.** Ringe → Ringe; Brautstyling/Make-up → Pinsel, Puderdose, Lippenstift, Schere, Föhn, Spiegel; Torte → Torte; Foto-Thema → Kamera; Checkliste → Klemmbrett mit Haken usw. Die Zeichnung bildet die Kernobjekte des Titels ab (keine Schneeflocke für „Make-up im Winter“). Jahreszeit nur als kleines Beiwerk (Schneeflocken, Sonne).
- **Jede Seite bekommt ein eigenes Bleistift-Motiv.** Nie dasselbe Motiv für mehrere Seiten (die bisherigen 8 Winter-Pins zeigen alle dieselbe Schneeflocke – das ist zu ähnlich).
- **Pro Seite zwei Boards:** je 3 Varianten für das Haupt-Board **und** 3 Varianten für das zweite Board, mit anderem Titel, anderen Zeilen und anderem Untertitel (nicht nur andere Farbe).
- Titel verschiedener Pins beginnen nicht mit demselben Wort (nicht dreimal „Winterhochzeit …“). Mal Frage, mal Liste, mal Nutzen („So…“, „5 Tipps…“, „Was kostet…“, „Wann…“).
- `tools/build_feed.py release` wählt automatisch: nicht dieselbe Seite wie in den letzten 8 Pins des Boards, nicht dieselbe Seite am selben Tag in zwei Boards, Seiten mit wenigen Pins zuerst.
- Saisonale Seiten bekommen in `pins.json` die Felder `"from"` und `"until"` (Datum), damit sie nur im passenden Zeitraum erscheinen.

## Reihenfolge der Seiten (je Lauf der Bau-Aufgabe: die nächste mit Status „offen“)
Läufe: Montag, Dienstag, Donnerstag, Freitag (ca. 28 bis Silvester). Zuerst Winter (die Winter-Warteschlange ist ab ca. 13.11. leer), dann Ostsee, dann Planung.

| # | Slug der Seite | Typ | Haupt-Board | Zweites Board | Motiv-Idee | Saison (from–until) | Status |
|---|---|---|---|---|---|---|---|
| 1 | ratgeber/winterhochzeit-outfit | Ratgeber | winter | planung | Mantel, Stola, warme Schuhe | – | gebaut (2026-11-09) |
| 2 | ratgeber/silvester-hochzeit | Ratgeber | winter | planung | Sektgläser und Feuerwerk | 2026-11-25 – 2026-12-28 | gebaut (2026-11-09) |
| 3 | ratgeber/winterhochzeit-deko-licht | Ratgeber | winter | ostsee | Kerzen und Lichterkette | – | gebaut (2026-11-09) |
| 4 | ratgeber/heiraten-weihnachten | Ratgeber | winter | ostsee | Tannenzweig mit Kerze | 2026-11-30 – 2026-12-27 | gebaut (2026-11-09) |
| 5 | ratgeber/winter-fotospots-ruegen | Ratgeber | winter | ostsee | Kreidefelsen im Schnee | – | gebaut (2026-11-09) |
| 6 | ratgeber/verlobung-planen | Ratgeber | planung | winter | Ringschachtel | 2026-11-20 – 2026-12-31 | gebaut (2026-11-09) |
| 7 | ratgeber/unterkuenfte-hochzeitsgaeste-ruegen | Ratgeber | ostsee | planung | Bett, Haus, Koffer | – | gebaut (2026-11-09) |
| 8 | ratgeber/heiraten-usedom | Ratgeber | ostsee | planung | Seebrücke | – | gebaut (2026-11-09) |
| 9 | ratgeber/heiraten-darss | Ratgeber | ostsee | planung | Darßer Wald und Strand | – | gebaut (2026-11-09) |
| 10 | ratgeber/heiraten-stralsund | Ratgeber | ostsee | planung | Backsteingiebel Hafen | – | gebaut (2026-11-09) |
| 11 | ratgeber/freie-trauung-mv | Ratgeber | ostsee | planung | Bogen mit Stühlen | – | gebaut (2026-11-09) |
| 12 | ratgeber/hochzeit-2027-zeitplan | Ratgeber | planung | winter | Kalender | – | gebaut (2026-11-09) |
| 13 | ablaufplan | Tool | planung | ostsee | Uhr mit Zeitstrahl | – | gebaut (2026-11-09) |
| 14 | hochzeitstorte-rechner | Tool | planung | ostsee | Torte | – | gebaut (2026-11-09) |
| 15 | ratgeber/save-the-date-einladung | Ratgeber | planung | winter | Briefumschlag | – | gebaut (2026-11-09) |
| 16 | ratgeber/trauzeugen-aufgaben | Ratgeber | planung | ostsee | zwei Gläser, Liste | – | gebaut (2026-11-09) |
| 17 | ratgeber/hochzeitsrede-tipps | Ratgeber | planung | ostsee | Mikrofon und Karten | – | gebaut (2026-11-09) |
| 18 | ratgeber/standesamt-unterlagen | Ratgeber | planung | ostsee | Mappe mit Stempel | – | gebaut (2026-11-09) |
| 19 | ratgeber/brautstyling-probe | Ratgeber | planung | ostsee | Spiegel und Bürste | – | gebaut (2026-11-09) |
| 20 | ratgeber/hochzeitsfotos-tipps-paare | Ratgeber | planung | ostsee | Kamera mit Herz | – | gebaut (2026-11-09) |
| 21 | ratgeber/sitzordnung-tipps | Ratgeber | planung | ostsee | Tisch mit Namenskärtchen | – | gebaut (2026-11-09) |
| 22 | ratgeber/hochzeitsgeschenke-wunschliste | Ratgeber | planung | winter | Geschenkpaket | – | gebaut (2026-11-09) |
| 23 | ratgeber/flitterwochen-budget | Ratgeber | planung | winter | Koffer und Flugzeug | – | gebaut (2026-11-09) |
| 24 | ratgeber/hochzeitsnacht-hotel-ruegen | Ratgeber | ostsee | planung | Hotelbett mit Meerblick | – | gebaut (2026-11-09) |

Rechnung: 24 Seiten × 6 Pins = 144 neue Pins + 29 vorhandene = 173 ≥ 156 Slots.
Alle 24 Seiten sind gebaut (2026-11-09). Zusätzlich: 3 Winter-Ratgeber (winterhochzeit-brautstrauss, -menue-getraenke, -zeitplan) und 6 Tool-/Ortsseiten (fotostunden-rechner, goldene-stunde, tischkarten, hochzeitstyp, hochzeitsfotograf/ + 6 Orte). Weitere Seiten: Generatoren `tools/build_pages.py` (Ratgeber), `tools/build_tools.py` (Tools, Ortsseiten).

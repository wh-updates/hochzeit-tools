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
| 1 | ratgeber/winterhochzeit-outfit | Ratgeber | winter | planung | Mantel, Stola, warme Schuhe | – | offen |
| 2 | ratgeber/silvester-hochzeit | Ratgeber | winter | planung | Sektgläser und Feuerwerk | 2026-11-25 – 2026-12-28 | offen |
| 3 | ratgeber/winterhochzeit-deko-licht | Ratgeber | winter | ostsee | Kerzen und Lichterkette | – | offen |
| 4 | ratgeber/heiraten-weihnachten | Ratgeber | winter | ostsee | Tannenzweig mit Kerze | 2026-11-30 – 2026-12-27 | offen |
| 5 | ratgeber/winter-fotospots-ruegen | Ratgeber | winter | ostsee | Kreidefelsen im Schnee | – | offen |
| 6 | ratgeber/verlobung-planen | Ratgeber | planung | winter | Ringschachtel | 2026-11-20 – 2026-12-31 | offen |
| 7 | ratgeber/unterkuenfte-hochzeitsgaeste-ruegen | Ratgeber | ostsee | planung | Bett, Haus, Koffer | – | offen |
| 8 | ratgeber/heiraten-usedom | Ratgeber | ostsee | planung | Seebrücke | – | offen |
| 9 | ratgeber/heiraten-darss | Ratgeber | ostsee | planung | Darßer Wald und Strand | – | offen |
| 10 | ratgeber/heiraten-stralsund | Ratgeber | ostsee | planung | Backsteingiebel Hafen | – | offen |
| 11 | ratgeber/freie-trauung-mv | Ratgeber | ostsee | planung | Bogen mit Stühlen | – | offen |
| 12 | ratgeber/hochzeit-2027-zeitplan | Ratgeber | planung | winter | Kalender | – | offen |
| 13 | ablaufplan | Tool | planung | ostsee | Uhr mit Zeitstrahl | – | offen |
| 14 | hochzeitstorte-rechner | Tool | planung | ostsee | Torte | – | offen |
| 15 | ratgeber/save-the-date-einladung | Ratgeber | planung | winter | Briefumschlag | – | offen |
| 16 | ratgeber/trauzeugen-aufgaben | Ratgeber | planung | ostsee | zwei Gläser, Liste | – | offen |
| 17 | ratgeber/hochzeitsrede-tipps | Ratgeber | planung | ostsee | Mikrofon und Karten | – | offen |
| 18 | ratgeber/standesamt-unterlagen | Ratgeber | planung | ostsee | Mappe mit Stempel | – | offen |
| 19 | ratgeber/brautstyling-probe | Ratgeber | planung | ostsee | Spiegel und Bürste | – | offen |
| 20 | ratgeber/hochzeitsfotos-tipps-paare | Ratgeber | planung | ostsee | Kamera mit Herz | – | offen |
| 21 | ratgeber/sitzordnung-tipps | Ratgeber | planung | ostsee | Tisch mit Namenskärtchen | – | offen |
| 22 | ratgeber/hochzeitsgeschenke-wunschliste | Ratgeber | planung | winter | Geschenkpaket | – | offen |
| 23 | ratgeber/flitterwochen-budget | Ratgeber | planung | winter | Koffer und Flugzeug | – | offen |
| 24 | ratgeber/hochzeitsnacht-hotel-ruegen | Ratgeber | ostsee | planung | Hotelbett mit Meerblick | – | offen |

Rechnung: 24 Seiten × 6 Pins = 144 neue Pins + 29 vorhandene = 173 ≥ 156 Slots.
Der Status wird von der Bau-Aufgabe auf „gebaut (Datum)“ gesetzt.

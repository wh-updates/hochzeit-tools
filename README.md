# Hochzeit-Tools

Kostenlose Hochzeitsplaner-Tools unter https://tools.bride-light.de (GitHub Pages, statisch, ohne Server).
Alle Eingaben bleiben im Browser der Nutzer (localStorage).

## Tools
- `budgetrechner/` – Hochzeitsbudget-Rechner
- `gaesteliste/` – Gästelisten-Planer mit CSV-Export
- `sitzplan/` – Sitzplan-Planer (Import aus Gästeliste)
- `getraenkerechner/` – Getränkemengen-Rechner
- `checkliste/` – Countdown & Checkliste
- `ratgeber/` – Heiraten auf Rügen, Strandhochzeit MV
- `download/hochzeitsplaner.pdf` – PDF-Planer (7 Seiten)
- `marketing/` – Pinterest-Pins + Link-Baustein (nicht indexiert)

## Logbuch
- 2026-11-08: Gerüst + 3 Tools, CNAME, Sitemap.
- 2026-11-08: Regionsfrage „Wo heiratet ihr?“ + MV-Banner (in assets/site.js, gilt automatisch für alle Seiten).
- 2026-11-08: Sitzplan, Getränkerechner, 2 Ratgeber (MV), PDF-Planer, Pins. Nav: Budget · Gästeliste · Sitzplan · Getränke · Checkliste · Ratgeber.
- 2026-11-08: Pinterest-RSS: `feed.xml` (Board Hochzeitsplanung Tipps) + `feed-ostsee.xml`, Warteschlange `marketing/pins.json` (live=true erscheint im Feed). Skripte `tools/make_pin.py`, `tools/build_feed.py` (`release` gibt den nächsten Pin frei). pinterest-bulk.csv entfernt.

- 2026-11-08: Pins im Bleistift-Stil (tools/pencil.py: je Thema ein Motiv, make_pin.py legt es mit Wackel-Filter auf die Hintergrundfarbe). Neue Seite = neues Motiv in pencil.py (Funktion + Eintrag in MOTIVE, Schlüssel = erstes Wort des Pin-Slugs).

- 2026-11-08: Marken-Look (Rosé & Champagner wie bride-light.de): Kopf mit Logo, Fuß mit Verweisen auf die Hauptseite, Über-uns-Box auf jeder Seite, Willkommens-Hero auf der Startseite, Bleistift-Icons auf den Kacheln. Kopf/Fuß/Über-uns kommen aus EINER Quelle: `python3 tools/layout.py` (setzt auch ?v= für CSS/JS). Logo und Foto werden direkt von bride-light.de geladen. Neue Seite: Kopf/Fuß-Platzhalter `<header class="site"></header>` und `<footer class="site"></footer>` setzen, `tools/layout.py` ausführen, Icon in tools/make_icons.py erzeugen.

- 2026-11-09: Eigenwerbung-Karten („Eigenwerbung“, `tools/layout.py` → `promo()`, Zuordnung im Dict `PROMO`): Budgetrechner + Ratgeber → kunden.bride-light.de (Fotoanfrage), Gästeliste/Sitzplan/Getränke/Checkliste → Etsy-Shop BrideLightShop; Fußbereich: Link „Website-Vorlagen für Fotograf:innen“. Nicht auf Start und Shop. Kein Skript, kein Tracking, UTM `utm_medium=promo`.
- 2026-11-09: Pins: 1 pro Feed und Tag (`release 1`). `release` wählt abwechslungsreich (nicht dieselbe Seite in den letzten 8 Pins eines Boards, nicht am selben Tag in zwei Boards); optionale Saisonfelder `from`/`until` in pins.json. Plan bis Silvester mit 24 neuen Seiten: `marketing/PINPLAN.md`.

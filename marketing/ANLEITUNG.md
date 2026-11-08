# Marketing-Material

## 1. Link von bride-light.de auf die Tools

Diesen Baustein im WedHero-Website-Editor als HTML-Block einfügen, zum Beispiel auf der Startseite unten oder auf der Kontakt-/Info-Seite:

```html
<section style="max-width:760px;margin:2rem auto;padding:1.5rem;border:1px solid #e8e0d8;border-radius:14px;text-align:center">
  <h2 style="margin-top:0">Kostenlose Planungshelfer für eure Hochzeit</h2>
  <p>Budgetrechner, Gästeliste, Sitzplan, Getränkerechner und Checkliste – ohne Anmeldung, eure Daten bleiben bei euch.</p>
  <p><a href="https://tools.bride-light.de/" style="display:inline-block;background:#b0806a;color:#fff;padding:.7rem 1.2rem;border-radius:8px;text-decoration:none">Zu den Hochzeits-Tools</a></p>
</section>
```

Zusätzlich im Footer oder Menü ein einfacher Textlink: `<a href="https://tools.bride-light.de/">Hochzeitsplaner-Tools</a>`

## 2. Pinterest-Pins (Ordner `pins/`, 1000 × 1500 px)

Pro Woche 1–2 Pins hochladen. Board-Vorschlag: „Hochzeitsplanung Tipps“ und „Heiraten an der Ostsee“.

| Datei | Titel | Beschreibung | Link |
|---|---|---|---|
| budgetrechner.png | Hochzeitsbudget berechnen – kostenloser Rechner | Gesamtbudget eingeben und automatisch auf Location, Essen, Fotograf, Kleid & Co. verteilen. Ohne Anmeldung. #hochzeitsplanung #hochzeitsbudget | https://tools.bride-light.de/budgetrechner/ |
| gaesteliste.png | Gästeliste Hochzeit – kostenloser Planer | Zusagen, Kinder und Essenswünsche erfassen, Kosten pro Kopf automatisch berechnen. #gästeliste #hochzeit2027 | https://tools.bride-light.de/gaesteliste/ |
| sitzplan.png | Sitzplan Hochzeit einfach erstellen | Tische anlegen, Gäste zuordnen, ausdrucken – kostenlos online. #sitzplan #hochzeitsplanung | https://tools.bride-light.de/sitzplan/ |
| getraenkerechner.png | Wie viel Wein & Bier für die Hochzeit? | Getränkemengen-Rechner mit Flaschen- und Kistenzahl für Sekt, Wein, Bier und Wasser. #hochzeitsplanung #hochzeitsfeier | https://tools.bride-light.de/getraenkerechner/ |
| checkliste.png | Hochzeits-Checkliste mit Countdown | Was ihr 12, 6, 3 und 1 Monat vorher erledigen müsst – zum Abhaken. #hochzeitscheckliste #verlobt | https://tools.bride-light.de/checkliste/ |
| ruegen.png | Heiraten auf Rügen – Trauorte & Tipps | Kap Arkona, Binz, Schlösser: so plant ihr eure Inselhochzeit. #rügen #ostseehochzeit | https://tools.bride-light.de/ratgeber/heiraten-auf-ruegen/ |
| strand.png | Strandhochzeit an der Ostsee | Was in Mecklenburg-Vorpommern standesamtlich und frei am Strand möglich ist. #strandhochzeit #ostsee | https://tools.bride-light.de/ratgeber/strandhochzeit-mv/ |
| pdf.png | Hochzeitsplaner zum Ausdrucken (PDF) | Kostenlos: Budget, Gästeliste, Checkliste, Tagesablauf und Kontakte. #hochzeitsplaner #printable | https://tools.bride-light.de/download/hochzeitsplaner.pdf |

## 3. Pinterest automatisch befüllen (RSS-Feed)

Pinterest erzeugt Pins selbst aus einem Feed (Funktion „Auto-publish“, nur mit bestätigter Website). Einmal einrichten:

1. Pinterest am Computer (Desktop-Ansicht) → Einstellungen → **Link zu Pinterest** („Beanspruchte Konten“) → Bereich **Auto-publish**.
2. Feed 1 eintragen: `https://tools.bride-light.de/feed.xml` → Board **Hochzeitsplanung Tipps** → Speichern.
3. Feed 2 eintragen: `https://tools.bride-light.de/feed-ostsee.xml` → Board **Heiraten an der Ostsee** → Speichern.

Neue Pins erscheinen laut Pinterest innerhalb von etwa 24 Stunden. Ab dann braucht es keinen Handgriff mehr: Pro Lauf der geplanten Aufgabe wird der nächste Pin freigegeben und für neue Tools ein neuer Pin vorbereitet (`marketing/pins.json`, `tools/build_feed.py`, `tools/make_pin.py`).
Falls „Auto-publish“ bei deinem Konto nicht erscheint, bietet Pinterest die Funktion nur schrittweise an – dann bleibt der manuelle Weg mit `pins-zum-kopieren.txt`.


## 4. Pinterest-Turbo (Stand 08.11.2026)

- **Pins:** 39 Pins (je Seite 3–4 Varianten mit unterschiedlichen Suchbegriffen in Titel und Beschreibung). Die tägliche Aufgabe gibt je Board 2 Pins frei (`python3 tools/build_feed.py release 2`), abwechselnd von verschiedenen Seiten, damit nie dieselbe Seite mehrfach hintereinander erscheint.
- **Neue Seiten:** Die Aufgabe „neues Tool bauen“ legt pro Seite 3 Pin-Varianten an (Slug beginnt mit dem Motivnamen aus `tools/pencil.py`). Titel: Suchbegriff zuerst, max. 100 Zeichen; Beschreibung mit 2 Hashtags, max. 500 Zeichen.
- **Merken-Box:** `python3 tools/layout.py` setzt auf jeder Seite mit Pin eine Box „Auf Pinterest merken“ (reiner Link, kein Skript). Danach `python3 tools/seo_apply.py`.
- **Einmalig durch dich (Pinterest-Konto):** Website bestätigen („Beanspruchte Konten“), Auto-publish-Feeds eintragen (siehe Punkt 3), Konto als Unternehmenskonto führen.

- **Drittes Board „Winterhochzeit“:** Feed `https://tools.bride-light.de/feed-winter.xml` in Pinterest unter Auto-publish eintragen und dem Board „Winterhochzeit“ zuordnen (8 Pins, 3 davon freigegeben). Die tägliche Freigabe bedient alle drei Boards.

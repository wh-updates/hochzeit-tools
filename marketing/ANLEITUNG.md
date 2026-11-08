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

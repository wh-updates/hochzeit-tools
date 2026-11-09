"""Themen-Cluster für die interne Verlinkung ("Mehr zum Thema" auf jeder Seite). Reihenfolge = Priorität (Pillar zuerst)."""
from content import ARTICLE_TITLES
from content.extra import TOOL_TITLES, LOCAL_TITLES
BASE={'budgetrechner':'Hochzeitsbudget-Rechner','gaesteliste':'Gästelisten-Planer','sitzplan':'Sitzplan-Planer','getraenkerechner':'Getränkerechner','checkliste':'Hochzeits-Checkliste',
 'ratgeber/heiraten-auf-ruegen':'Heiraten auf Rügen','ratgeber/strandhochzeit-mv':'Strandhochzeit in MV','ratgeber/hochzeitslocations-ruegen-ostsee':'Hochzeitslocations auf Rügen',
 'ratgeber/kosten-hochzeit-mv':'Kosten einer Hochzeit in MV','ratgeber/hochzeitsfotograf-finden':'Hochzeitsfotograf finden','ratgeber/heiraten-im-winter-ostsee':'Winterhochzeit an der Ostsee'}
TITLES={**BASE,**TOOL_TITLES,**{'ratgeber/'+k.split('/')[-1]:v for k,v in ARTICLE_TITLES.items()},**{k:v for k,v in LOCAL_TITLES.items()}}
TITLES.update({k:v for k,v in ARTICLE_TITLES.items()}); TITLES['hochzeitsfotograf']='Hochzeitsfotograf in MV'
R='ratgeber/'
CLUSTERS={
 'ruegen':[R+'heiraten-auf-ruegen','hochzeitsfotograf/ruegen',R+'hochzeitslocations-ruegen-ostsee',R+'kosten-hochzeit-mv',R+'unterkuenfte-hochzeitsgaeste-ruegen',R+'hochzeitsnacht-hotel-ruegen',R+'strandhochzeit-mv',R+'freie-trauung-mv',R+'winter-fotospots-ruegen','hochzeitsdatum-finder','goldene-stunde',R+'heiraten-usedom',R+'heiraten-darss'],
 'foto':[R+'hochzeitsfotograf-finden','hochzeitsfotograf/ruegen','fotostunden-rechner','foto-wunschliste','fotograf-test',R+'hochzeitsfotos-tipps-paare','goldene-stunde',R+'brautstyling-probe','hochzeitsfotograf'],
 'planung':['checkliste','budgetrechner',R+'hochzeit-2027-zeitplan','hochzeitsdatum-finder','ablaufplan','gaesteliste','einladungs-rechner',R+'save-the-date-einladung',R+'standesamt-unterlagen',R+'trauzeugen-aufgaben','sitzplan'],
 'deko':['hochzeitstyp','brautstrauss-konfigurator','tischkarten','gastgeschenke-rechner','hochzeitstorte-rechner','getraenkerechner',R+'sitzordnung-tipps',R+'winterhochzeit-deko-licht'],
 'winter':[R+'heiraten-im-winter-ostsee',R+'winterhochzeit-outfit',R+'winterhochzeit-deko-licht',R+'winterhochzeit-brautstrauss',R+'winterhochzeit-menue-getraenke',R+'winterhochzeit-zeitplan',R+'winter-fotospots-ruegen',R+'silvester-hochzeit',R+'heiraten-weihnachten','goldene-stunde'],
 'danach':['hochzeitstag-rechner',R+'flitterwochen-budget',R+'hochzeitsgeschenke-wunschliste','packliste-hochzeit',R+'hochzeitsnacht-hotel-ruegen'],
 'orte':['hochzeitsfotograf/stralsund','hochzeitsfotograf/ruegen','hochzeitsfotograf/usedom','hochzeitsfotograf/darss-zingst','hochzeitsfotograf/greifswald','hochzeitsfotograf/rostock',R+'heiraten-stralsund',R+'heiraten-usedom',R+'heiraten-darss'],
}
def related(key,n=7):
    out=[]
    for members in CLUSTERS.values():
        if key in members:
            for m in members:
                if m!=key and m not in out and m in TITLES: out.append(m)
    # Pillar-Seite zu Rügen soll von jeder Seite mit Rügen-Bezug erreichbar sein
    return out[:n]

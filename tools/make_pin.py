#!/usr/bin/env python3
"""Pinterest-Pin (1000x1500 PNG) erzeugen.
Aufruf: python3 tools/make_pin.py <slug> "<Zeile 1>" "<Zeile 2>" "<Untertitel>" <planung|ostsee> [Variante 0-2 = Farbe]
Ergebnis: marketing/pins/<slug>.png  (braucht rsvg-convert + DejaVu-Schriften)"""
import sys,html,subprocess,pathlib
COL={'planung':['#b0806a','#8f6452','#9a7b5f'],'ostsee':['#5f7a86','#486573','#7a9aa8']}
def wrap(t,n=30):
    L=['']
    for x in t.split():
        if len(L[-1])+len(x)+1>n:L.append(x)
        else:L[-1]=(L[-1]+' '+x).strip()
    return L
def make(slug,t1,t2,sub,board,variant=0):
    col=COL[board][int(variant)%3]; root=pathlib.Path(__file__).resolve().parent.parent
    subl=''.join(f'<text x="500" y="{1010+i*52}" font-family="DejaVu Sans" font-size="38" fill="#5a4f47" text-anchor="middle">{html.escape(l)}</text>' for i,l in enumerate(wrap(sub)))
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="1500">
<rect width="1000" height="1500" fill="#faf7f4"/><rect width="1000" height="560" fill="{col}"/><circle cx="500" cy="560" r="150" fill="#faf7f4"/>
<g fill="none" stroke="{col}" stroke-width="10"><circle cx="465" cy="565" r="55"/><circle cx="535" cy="565" r="55"/></g>
<text x="500" y="220" font-family="DejaVu Sans" font-size="34" letter-spacing="8" fill="#fff" text-anchor="middle">KOSTENLOS · OHNE ANMELDUNG</text>
<text x="500" y="820" font-family="DejaVu Serif" font-size="86" fill="#2b2622" text-anchor="middle">{html.escape(t1)}</text>
<text x="500" y="915" font-family="DejaVu Serif" font-size="62" font-style="italic" fill="{col}" text-anchor="middle">{html.escape(t2)}</text>
{subl}
<rect x="250" y="1230" width="500" height="90" rx="45" fill="{col}"/>
<text x="500" y="1288" font-family="DejaVu Sans" font-size="36" fill="#fff" text-anchor="middle">tools.bride-light.de</text>
<text x="500" y="1420" font-family="DejaVu Sans" font-size="26" fill="#7a6f66" text-anchor="middle">Bride &amp; Light · Hochzeitsfotografie &amp; Brautstyling</text></svg>'''
    out=root/'marketing'/'pins'/f'{slug}.png'; out.parent.mkdir(parents=True,exist_ok=True)
    subprocess.run(['rsvg-convert','-o',str(out)],input=svg.encode(),check=True); return out
if __name__=='__main__':
    a=sys.argv[1:]; print(make(*a))

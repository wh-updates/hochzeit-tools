#!/usr/bin/env python3
"""Pinterest-Pin (1000x1500 PNG) erzeugen.
Aufruf: python3 tools/make_pin.py <slug> "<Zeile 1>" "<Zeile 2>" "<Untertitel>" <planung|ostsee> [Variante 0-2 = Farbe]
Ergebnis: marketing/pins/<slug>.png  (braucht rsvg-convert + DejaVu-Schriften)"""
import sys,html,subprocess,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from pencil import MOTIVE
# (Hintergrund, Akzent) je Board und Variante
COL={'planung':[('#e6cdbf','#8f6452'),('#dccaae','#7d6548'),('#e3d0d3','#8a5f6b')],
     'ostsee':[('#adc4cd','#3f6272'),('#bcd2c9','#41675a'),('#c5cfe2','#4d5d85')]}
DEFS='''<defs>
<filter id="pen1" filterUnits="userSpaceOnUse" x="0" y="0" width="1000" height="720">
<feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="3" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="8" xChannelSelector="R" yChannelSelector="G" result="d"/>
<feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed="8" result="g"/>
<feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.2 1.75" result="ga"/>
<feComposite in="d" in2="ga" operator="in"/></filter>
<filter id="pen2" filterUnits="userSpaceOnUse" x="0" y="0" width="1000" height="720">
<feTurbulence type="fractalNoise" baseFrequency="0.045" numOctaves="2" seed="11" result="n"/>
<feDisplacementMap in="SourceGraphic" in2="n" scale="6" xChannelSelector="G" yChannelSelector="R" result="d"/>
<feTurbulence type="fractalNoise" baseFrequency="1.1" numOctaves="2" seed="21" result="g"/>
<feColorMatrix in="g" type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 -2.4 1.6" result="ga"/>
<feComposite in="d" in2="ga" operator="in"/></filter>
<pattern id="h" width="13" height="13" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><line x1="0" y1="0" x2="0" y2="13" stroke="#4a4540" stroke-width="1.8"/></pattern>
<pattern id="h2" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(40)"><line x1="0" y1="0" x2="0" y2="8" stroke="#4a4540" stroke-width="1.6"/></pattern>
</defs>'''
RATGEBER={'ruegen','strand','locations','kosten','fotograf','winter'}
def wrap(t,n=30):
    L=['']
    for x in t.split():
        if len(L[-1])+len(x)+1>n:L.append(x)
        else:L[-1]=(L[-1]+' '+x).strip()
    return L
def make(slug,t1,t2,sub,board,variant=0):
    bg,acc=COL[board][int(variant)%3]; root=pathlib.Path(__file__).resolve().parent.parent
    label='RATGEBER · KOSTENLOS' if slug.split('-')[0] in RATGEBER else 'KOSTENLOS · OHNE ANMELDUNG'
    motif=MOTIVE.get(slug.split('-')[0],MOTIVE['ruegen'])()
    subl=''.join(f'<text x="500" y="{1050+i*52}" font-family="DejaVu Sans" font-size="38" fill="#5a4f47" text-anchor="middle">{html.escape(l)}</text>' for i,l in enumerate(wrap(sub)))
    ink='fill="none" stroke="#3d3935" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"'
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000" height="1500">{DEFS}
<rect width="1000" height="1500" fill="#faf7f4"/><rect width="1000" height="700" fill="{bg}"/>
<path d="M0 700 Q250 668 500 700 T1000 700 V716 H0Z" fill="#faf7f4"/>
<text x="500" y="92" font-family="DejaVu Sans" font-size="30" letter-spacing="8" fill="{acc}" text-anchor="middle">{label}</text>
<g id="m" {ink}>{motif}</g>
<use xlink:href="#m" filter="url(#pen1)"/><use xlink:href="#m" filter="url(#pen2)" opacity="0.55"/>
<text x="500" y="870" font-family="DejaVu Serif" font-size="86" fill="#2b2622" text-anchor="middle">{html.escape(t1)}</text>
<text x="500" y="965" font-family="DejaVu Serif" font-size="62" font-style="italic" fill="{acc}" text-anchor="middle">{html.escape(t2)}</text>
{subl}
<rect x="250" y="1250" width="500" height="90" rx="45" fill="{acc}"/>
<text x="500" y="1308" font-family="DejaVu Sans" font-size="36" fill="#fff" text-anchor="middle">tools.bride-light.de</text>
<text x="500" y="1430" font-family="DejaVu Sans" font-size="26" fill="#7a6f66" text-anchor="middle">Bride &amp; Light · Hochzeitsfotografie &amp; Brautstyling</text></svg>'''
    out=root/'marketing'/'pins'/f'{slug}.png'; out.parent.mkdir(parents=True,exist_ok=True)
    subprocess.run(['rsvg-convert','-o',str(out)],input=svg.encode(),check=True); return out
if __name__=='__main__':
    a=sys.argv[1:]; print(make(*a))

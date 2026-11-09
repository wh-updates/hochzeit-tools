"""Bleistift-Motive für die zweite Tool-Runde (Datum, Jahrestag, Einladungen, Blumen, Gastgeschenke, Packliste, Foto-Wunschliste, Fotografen-Test)."""
import math
from pencil import H,H2,flake_s,waves,cloud,gulls,grass
from pencil_neu import circ,flute
def heart(x,y,s=1):
    return f'<path d="M{x} {y+14*s} C{x-30*s} {y-8*s} {x-14*s} {y-28*s} {x} {y-10*s} C{x+14*s} {y-28*s} {x+30*s} {y-8*s} {x} {y+14*s}Z" stroke-width="3"/>'
def check(x,y,s=1):
    return f'<path d="M{x} {y} l{10*s} {11*s} l{22*s} {-26*s}" stroke-width="4"/>'
def datumfinder():
    g=''.join(f'<rect x="{352+c*46}" y="{352+r*52}" width="36" height="40" rx="3"/>' for r in range(4) for c in range(6) if (r,c)!=(2,3))
    return f'''
<rect x="330" y="230" width="340" height="360" rx="14"/><path d="M330 300 L670 300"/><rect x="332" y="232" width="336" height="66" rx="12" {H2}/>
<path d="M400 205 L400 250 M500 205 L500 250 M600 205 L600 250" stroke-width="7"/>
{g}
<ellipse cx="508" cy="476" rx="30" ry="29" stroke-width="5"/><ellipse cx="508" cy="476" rx="30" ry="29" {H}/>{heart(508,474,.7)}
<path d="M360 460 L376 480 M360 480 L376 460" stroke-width="3"/>
{heart(740,230,1.3)}{heart(770,285,.8)}
<path d="M200 650 Q500 630 800 650"/>'''
def jahrestag():
    return f'''{flute(430,290,18)}{flute(570,290,-18)}
<path d="M500 262 l-8 -16 M500 262 l8 -16 M500 262 l0 -22 M470 270 l-14 -10 M530 270 l14 -10" stroke-width="3"/>
<path d="M250 190 Q500 270 750 190" stroke-width="3"/><path d="M290 205 l16 52 l22 -42 M420 237 l16 56 l22 -44 M570 237 l16 56 l22 -44 M690 205 l16 52 l22 -42" stroke-width="3"/>
{heart(318,262,.9)}{heart(450,292,.9)}{heart(598,292,.9)}{heart(720,262,.9)}
<ellipse cx="500" cy="600" rx="62" ry="22"/><ellipse cx="500" cy="590" rx="30" ry="10" stroke-width="4"/><path d="M500 573 l-9 -14 l9 -9 l9 9z" stroke-width="3"/>
<path d="M200 650 Q500 635 800 650"/>'''
def einladungen():
    def env(x,y,rot,seal=False):
        return f'''<g transform="translate({x},{y}) rotate({rot})"><rect x="0" y="0" width="300" height="200" rx="8" fill="#fbf5f0"/><path d="M0 0 L150 110 L300 0 M0 200 L112 98 M300 200 L188 98"/>{'<path d="M135 105 l15 -17 l15 17 l-15 22z" stroke-width="3"/>' if seal else ''}</g>'''
    return f'''{env(250,380,-6)}{env(262,320,3)}{env(240,250,-2,True)}
<rect x="610" y="190" width="100" height="120" rx="3" fill="#fbf5f0"/><rect x="620" y="200" width="80" height="100" {H}/><path d="M628 232 Q660 200 692 232 L692 290 L628 290Z" stroke-width="3"/>{heart(660,265,.7)}
<circle cx="700" cy="350" r="38" stroke-width="3"/><path d="M670 350 q15 -12 30 0 t30 0 M670 362 q15 -12 30 0 t30 0" stroke-width="3"/>
<path d="M200 650 Q500 635 800 650"/>'''
def blumenwahl():
    tul=lambda x:f'<path d="M{x} 380 L{x} 560"/><path d="M{x-34} 300 Q{x-38} 372 {x} 384 Q{x+38} 372 {x+34} 300 L{x+16} 330 L{x} 290 L{x-16} 330Z"/><path d="M{x} 520 Q{x-50} 480 {x-62} 440 M{x} 540 Q{x+50} 500 {x+60} 460"/>'
    rose=lambda x:f'<path d="M{x} 400 L{x} 570"/><circle cx="{x}" cy="352" r="48"/><path d="M{x-20} 352 q20 -26 40 0 q-8 24 -36 14 q-8 -26 24 -30 q14 14 -6 24" stroke-width="3"/><path d="M{x} 500 Q{x+50} 470 {x+56} 430 M{x} 530 Q{x-48} 506 {x-50} 468"/>'
    dai=lambda x:f'<path d="M{x} 380 L{x} 560"/>'+circ(x,334,16)+''.join(f'<ellipse cx="{x+38*math.cos(a*math.pi/4):.0f}" cy="{334+38*math.sin(a*math.pi/4):.0f}" rx="18" ry="9" transform="rotate({a*45} {x+38*math.cos(a*math.pi/4):.0f} {334+38*math.sin(a*math.pi/4):.0f})"/>' for a in range(8))+f'<path d="M{x} 500 Q{x+44} 480 {x+50} 440"/>'
    tags=''.join(f'<rect x="{x-32}" y="596" width="64" height="40" rx="6"/>{check(x-16,618,.9)}' for x in (320,500,680))
    return f'{tul(320)}{rose(500)}{dai(680)}{tags}<path d="M220 570 L780 570" stroke-width="3"/>{H and ""}'
def gastgeschenk():
    return f'''<path d="M250 330 L232 600 L400 600 L382 330Z"/><path d="M250 330 L382 330" /><path d="M285 330 Q285 270 316 270 Q347 270 347 330" stroke-width="4"/><path d="M245 380 L387 380" stroke-width="3"/>{heart(316,470,1.6)}<path d="M250 330 L232 600 L262 600 L276 330Z" {H}/>
<rect x="450" y="410" width="130" height="190" rx="12"/><rect x="440" y="372" width="150" height="46" rx="8"/><path d="M450 480 L580 480 M450 540 L580 540" stroke-width="3"/><rect x="470" y="496" width="90" height="30" {H}/><path d="M440 395 Q515 440 590 395" stroke-width="3"/>
<rect x="620" y="480" width="130" height="120" rx="6"/><path d="M620 520 L750 520 M685 480 L685 600"/><path d="M685 480 Q650 430 640 470 Q650 490 685 480 Q720 490 730 470 Q720 430 685 480Z"/>
<path d="M232 600 Q316 612 400 600" stroke-width="3"/><path d="M360 335 q40 40 60 100" stroke-width="3"/><rect x="408" y="430" width="50" height="34" rx="3" transform="rotate(10 408 430)"/>
<path d="M200 650 Q500 635 800 650"/>'''
def packliste():
    lines=''.join(f'<path d="M300 {260+i*46} L520 {260+i*46}" stroke-width="3"/>{check(268,268+i*46,.7)}' for i in range(4))
    return f'''<path d="M280 210 L560 210 L580 460 L260 460Z"/><path d="M290 220 L552 220 L568 450 L272 450Z" {H}/>{lines}
<path d="M250 460 L620 460 L650 600 Q440 620 230 600Z"/><path d="M262 480 Q440 500 630 480" stroke-width="3"/><path d="M360 440 L360 400 Q440 380 520 400 L520 440" stroke-width="4"/>
<path d="M300 540 q10 -40 50 -30 q25 6 28 24 l-6 20 l-70 0z" stroke-width="3"/><rect x="420" y="525" width="48" height="40" rx="6" stroke-width="3"/><path d="M420 540 L468 540" stroke-width="3"/><path d="M500 545 q22 -26 44 0 q-22 20 -44 0z M508 570 L540 570" stroke-width="3"/>
<path d="M650 600 q40 -10 60 20 M650 600 l-4 -30" stroke-width="3"/>{heart(720,250,1.1)}
<path d="M200 650 Q500 640 800 650"/>'''
def wunschfotos():
    def pol(x,y,rot,kind):
        inner={'heart':heart(70,70,2.4),'ring':circ(54,78,24)+circ(86,78,24),'sea':waves(24,56,100,2),'glas':'<path d="M44 40 L52 96 Q60 108 68 96 L76 40Z M84 40 L92 96 Q100 108 108 96 L116 40Z" stroke-width="3"/>'}[kind]
        return f'<g transform="translate({x},{y}) rotate({rot})"><rect width="150" height="180" rx="4" fill="#fbf5f0"/><rect x="12" y="12" width="126" height="126" {H}/><rect x="12" y="12" width="126" height="126"/><g transform="translate(5 3)">{inner}</g></g>'
    return f'''{pol(230,200,-6,'heart')}{pol(430,190,4,'ring')}{pol(250,400,3,'sea')}{pol(450,395,-4,'glas')}
{check(640,250,1.3)}{check(640,330,1.3)}{check(640,410,1.3)}{check(640,490,1.3)}
<path d="M700 250 L770 250 M700 330 L770 330 M700 410 L770 410 M700 490 L770 490" stroke-width="3"/>
<path d="M690 560 L760 600 L735 626 L665 586Z"/><path d="M665 586 L660 610 L690 600" stroke-width="3"/>
<path d="M200 650 Q500 640 800 650"/>'''
def fotografentest():
    return f'''<rect x="250" y="290" width="360" height="230" rx="22"/><rect x="250" y="290" width="360" height="52" rx="22" {H2}/><path d="M330 290 L350 250 L440 250 L460 290"/>
<circle cx="430" cy="410" r="86"/><circle cx="430" cy="410" r="62"/><circle cx="430" cy="410" r="30" {H2}/><path d="M410 388 q10 -12 24 -6" stroke-width="3"/>
<circle cx="560" cy="318" r="10"/><path d="M280 316 L320 316" stroke-width="4"/>
<circle cx="660" cy="300" r="84" stroke-width="5"/><path d="M720 360 L780 430" stroke-width="9"/>{check(620,306,1.6)}
<path d="M300 560 L560 560 M300 590 L470 590" stroke-width="3"/>{check(232,570,.9)}{check(232,600,.9)}
<path d="M200 650 Q500 640 800 650"/>'''
MOTIVE_NEU2={'datumfinder':datumfinder,'jahrestag':jahrestag,'einladungen':einladungen,'blumenwahl':blumenwahl,'gastgeschenk':gastgeschenk,'packliste':packliste,'wunschfotos':wunschfotos,'fotografentest':fotografentest}

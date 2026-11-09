"""Neue Bleistift-Motive (je Ratgeber-Seite / Tool ein eigenes). Bereich ca. x 200-800, y 140-660. Wird am Ende von pencil.py eingebunden."""
import math
from pencil import H,H2,flake_s,waves,cloud,gulls,grass
G='<path d="M200 650 Q500 630 800 650"/>'
def circ(x,y,r): return f'<circle cx="{x}" cy="{y}" r="{r}"/>'
def flame(x,y,s=1):
    return f'<path d="M{x} {y} q{-14*s} {-22*s} 0 {-52*s} q{14*s} {30*s} 0 {52*s}z" stroke-width="3"/><path d="M{x} {y-6*s} q{-5*s} {-10*s} 0 {-22*s}" stroke-width="2"/>'
def burst(x,y,r=60,n=9,dots=True):
    o=''
    for k in range(n):
        a=k*2*math.pi/n; c,s=math.cos(a),math.sin(a)
        o+=f'<path d="M{x+r*.35*c:.0f} {y+r*.35*s:.0f} L{x+r*c:.0f} {y+r*s:.0f}" stroke-width="3"/>'
        if dots: o+=circ(round(x+r*1.22*c),round(y+r*1.22*s),3)
    return o
def flute(x,y,rot=0):
    return f'''<g transform="translate({x},{y}) rotate({rot})"><path d="M-26 0 L-19 125 Q-15 155 0 155 Q15 155 19 125 L26 0 Z"/>
<path d="M-23 45 L-19 125 Q-15 155 0 155 Q15 155 19 125 L23 45 Z" {H}/><path d="M-26 45 Q0 56 26 45" stroke-width="3"/>
<path d="M0 155 L0 235"/><path d="M-38 241 Q0 226 38 241 Q0 252 -38 241Z"/>{circ(-6,100,3)}{circ(5,80,3)}{circ(-2,125,3)}</g>'''

def outfit():
    fringe=''.join(f'<path d="M{592+i*21} {470-i*0} l-2 22" stroke-width="3"/>' for i in range(8))
    return f'''
<path d="M420 208 L420 192 Q420 166 446 166 Q472 166 472 192"/>
<path d="M420 208 L292 266 Q276 273 292 280 L548 280 Q564 273 548 266 Z"/>
<path d="M310 280 L296 566 L544 566 L530 280"/>
<path d="M310 280 L262 520 L302 536 L322 410" /><path d="M530 280 L578 520 L538 536 L518 410"/>
<path d="M378 280 L420 372 L462 280"/><path d="M420 372 L420 566"/>
<path d="M378 280 L420 372 L400 300Z" {H}/><path d="M462 280 L420 372 L440 300Z" {H}/>
<path d="M312 446 L528 446 L528 472 L312 472 Z" {H}/><rect x="404" y="444" width="32" height="30" rx="3"/>
{circ(434,500,9)}{circ(434,535,9)}{circ(406,500,9)}{circ(406,535,9)}
<path d="M296 566 L544 566 L544 548 L296 548Z" {H2}/>
<path d="M610 300 L770 322 L752 478 L592 456 Z"/><path d="M610 300 L770 322 L764 372 L604 350Z" {H}/>
<path d="M620 392 Q690 408 760 396 M616 424 Q686 440 756 428" stroke-width="3"/>{fringe}
<path d="M640 540 L640 618 L724 618 L724 540"/><path d="M634 540 L730 540 L730 566 L634 566Z" {H2}/>
<path d="M640 618 L640 636 L700 636 L700 650 L790 650 Q804 626 774 620 L724 612"/><path d="M640 590 L724 590" stroke-width="3"/><path d="M700 636 L700 650" />
{flake_s(250,220,24)}{flake_s(700,200,20)}{flake_s(210,420,16)}{flake_s(780,260,14)}'''

def silvester():
    return f'''
{flute(440,330,-16)}{flute(560,330,16)}
<path d="M497 318 l-8 -24 M505 316 l10 -26 M488 326 l-24 -14 M514 326 l24 -14 M500 300 l0 -34" stroke-width="3"/>
{burst(290,250,64,10)}{burst(710,230,56,9)}{burst(500,190,38,8,False)}
{''.join(circ(x,y,4) for x,y in [(240,420),(330,460),(690,430),(770,480),(250,520),(740,560)])}
<path d="M270 600 q20 -26 40 0 M720 610 q20 -26 40 0" stroke-width="3"/>
<path d="M200 650 Q500 630 800 650"/>'''

def lichter():
    bulbs=''
    for i in range(8):
        x=240+i*74; t=(x-200)/600; y=235*(1-t)**2+660*t*(1-t)+235*t*t
        bulbs+=f'<path d="M{x:.0f} {y:.0f} L{x:.0f} {y+14:.0f}"/><path d="M{x-9:.0f} {y+14:.0f} L{x+9:.0f} {y+14:.0f} L{x+11:.0f} {y+24:.0f} Q{x:.0f} {y+52:.0f} {x-11:.0f} {y+24:.0f}Z"/>'
    can=''
    for x,top,w in ((380,420,70),(500,360,82),(620,450,64)):
        can+=f'<path d="M{x-w/2} {top} L{x-w/2} 610 L{x+w/2} 610 L{x+w/2} {top}"/><path d="M{x-w/2} {top} Q{x} {top+16} {x+w/2} {top}"/><path d="M{x-w/2+8} {top+30} L{x-w/2+8} 600" {H}/>{flame(x,top-6,1.1)}<path d="M{x-w/2} {top+12} q8 30 14 6 M{x+w/2-10} {top+14} q6 34 10 8" stroke-width="3"/><path d="M{x} {top} L{x} {top-14}" stroke-width="3"/>'
    return f'''<path d="M200 235 Q500 330 800 235" stroke-width="3"/>
{bulbs}{can}
<path d="M310 614 L690 614" /><path d="M300 650 Q500 630 700 650"/>
{flake_s(230,420,18)}{flake_s(770,420,16)}'''

def tannenzweig():
    ne=''
    for i in range(17):
        x=236+i*32; y=478-48*math.sin((x-220)/560*math.pi)*0.5
        if 470<x<545: continue
        ne+=f'<path d="M{x} {y:.0f} q22 -14 46 -46"/><path d="M{x} {y:.0f} q22 14 46 46"/>'
    return f'''<path d="M220 478 Q500 440 780 478" stroke-width="6"/>
{ne}
<path d="M472 456 L472 336 L528 336 L528 456"/><path d="M462 456 L538 456 L528 474 L472 474Z"/><path d="M472 346 L472 450" {H}/>{flame(500,328,1.2)}
<path d="M330 520 L330 570" stroke-width="3"/>{circ(330,602,32)}<path d="M318 570 L342 570" stroke-width="3"/><path d="M310 592 q14 -20 36 -8" stroke-width="3"/>
<path d="M660 520 L660 550" stroke-width="3"/>{circ(660,582,32)}<path d="M648 550 L672 550" stroke-width="3"/><path d="M640 576 L680 590 M646 596 L674 566" stroke-width="3"/>
{flake_s(270,230,24)}{flake_s(560,210,16)}{flake_s(250,350,14)}'''

def kreidefelsen():
    trees=''.join(f'<path d="M{x} 330 L{x} {296-h}" stroke-width="4"/><path d="M{x-30} {300-h} q-10 -34 16 -34 q8 -26 30 -8 q26 2 14 42 q-30 14 -60 0z"/>' for x,h in ((250,10),(325,30),(395,6)))
    return f'''
<path d="M200 660 L200 340 L236 310 L262 352 L310 300 L338 346 L380 310 L410 360 L436 420 L452 520 L470 660Z"/>
<path d="M310 300 L338 346 L380 310 L410 360 L436 420 L452 520 L470 660 L400 660 L370 480Z" {H}/>
<path d="M240 420 L260 470 M290 520 L318 580 M232 580 L250 620" stroke-width="3"/>
{trees}
<path d="M560 660 L600 560 L626 585 L650 470 L690 520 L720 410 L760 470 L800 440 L800 660Z"/><path d="M650 470 L690 520 L720 410 L760 470 L800 440 L800 660 L720 660Z" {H}/>
<circle cx="640" cy="250" r="44"/><path d="M640 180 L640 168 M640 320 L640 332 M570 250 L558 250 M710 250 L722 250 M590 200 L581 191 M690 300 L699 309 M690 200 L699 191 M590 300 L581 309" stroke-width="3"/>
{waves(480,640,70,1)}{waves(500,612,50,1)}
{gulls(470,330,.9)}{gulls(540,380,.7)}
{''.join(circ(x,y,4) for x,y in [(220,260),(430,250),(500,300),(760,300),(540,470)])}'''

def ringbox():
    sp=''.join(f'<path d="M{500+dx*r:.0f} {330+dy*r:.0f} L{500+dx*(r+30):.0f} {330+dy*(r+30):.0f}" stroke-width="3"/>' for dx,dy,r in ((-1,-.2,100),(1,-.2,100),(-.6,-1,66),(.6,-1,66),(0,-1,64)))
    return f'''
<path d="M345 478 L388 345 L612 345 L655 478"/><path d="M360 478 L396 360 L604 360 L640 478" {H}/>
<path d="M320 478 L680 478 L680 600 Q500 626 320 600Z"/><path d="M320 478 Q500 508 680 478" /><path d="M320 600 Q500 626 680 600 L680 584 Q500 610 320 584Z" {H2}/>
<ellipse cx="500" cy="440" rx="56" ry="68"/><ellipse cx="500" cy="440" rx="40" ry="52"/><path d="M450 410 Q452 380 472 372" stroke-width="3"/>
<path d="M500 348 L466 372 L500 410 L534 372 Z"/><path d="M466 372 L534 372 M500 348 L486 372 L500 410 L514 372Z" stroke-width="3"/>
{sp}
<path d="M220 640 Q500 620 780 640"/>{flake_s(260,230,16)}'''

def unterkunft():
    return f'''
<path d="M230 470 L230 600 L560 600 L560 470"/><path d="M200 480 Q230 400 395 330 Q560 400 590 480 Q395 440 200 480Z"/><path d="M200 480 Q230 400 395 330 Q560 400 590 480 Q395 440 200 480Z" {H}/>
<path d="M470 360 L470 310 L510 310 L510 392"/><path d="M360 600 L360 520 Q395 490 430 520 L430 600"/><path d="M395 504 L395 600" stroke-width="3"/>
<rect x="262" y="506" width="62" height="50"/><path d="M293 506 L293 556 M262 531 L324 531" stroke-width="3"/><rect x="466" y="506" width="60" height="50"/><path d="M496 506 L496 556 M466 531 L526 531" stroke-width="3"/>
<path d="M610 600 L610 470 L760 470 L760 600Z"/><path d="M625 470 L625 600 M745 470 L745 600" stroke-width="3"/><path d="M660 470 L660 440 Q685 420 710 440 L710 470"/><path d="M610 520 L760 520 M610 550 L760 550" stroke-width="3"/>
<path d="M200 640 Q500 620 800 640"/>{grass(250,606,3,30)}{grass(570,606,3,30)}
<path d="M560 258 q20 -30 40 0 M610 230 q20 -30 40 0" stroke-width="3"/>{flake_s(240,260,22)}'''

def seebruecke():
    posts=''.join(f'<path d="M{x} 500 L{x} 600" /><path d="M{x} 460 L{x} 500" stroke-width="3"/>' for x in range(230,660,60))
    return f'''
<path d="M200 500 L690 500 M200 520 L690 520"/><path d="M200 460 L690 460" stroke-width="3"/>{posts}
<path d="M650 500 L650 360 L790 360 L790 500"/><path d="M630 360 L720 290 L810 360Z"/><path d="M630 360 L720 290 L810 360Z" {H}/><rect x="690" y="410" width="60" height="90"/><path d="M720 410 L720 500" stroke-width="3"/>
<path d="M200 610 Q300 596 400 610 T600 610 T800 610"/><path d="M230 640 Q330 626 430 640 T630 640 T800 640" />
<circle cx="360" cy="260" r="42"/><path d="M360 195 L360 180 M360 325 L360 340 M295 260 L280 260 M425 260 L440 260 M314 214 L303 203 M406 306 L417 317 M406 214 L417 203 M314 306 L303 317" stroke-width="3"/>
{gulls(500,300,1)}{gulls(560,350,.8)}{cloud(220,380,.8)}'''

def darss():
    def tree(x,h,lean):
        return f'<path d="M{x} 560 Q{x+lean*0.2} {560-h*0.5} {x+lean*0.6} {560-h}" stroke-width="5"/><path d="M{x+lean*0.6-20} {560-h+10} q{lean*0.8+10} -50 {lean*1.4+60} -8 q10 40 {-lean*0.5-30} 36 q-30 22 {-lean*0.6-30} -28z"/><path d="M{x+lean*0.6} {560-h+10} q{lean*0.5+30} -30 {lean*0.8+40} 0" {H2}/>'
    return f'''
{tree(300,200,110)}{tree(430,250,130)}{tree(560,180,100)}
<path d="M200 560 Q330 520 480 550 Q640 580 800 540 L800 665 L200 665Z"/><path d="M200 560 Q330 520 480 550 Q640 580 800 540 L800 665 L200 665Z" {H}/>
{grass(240,552,4,36)}{grass(690,556,4,40)}{grass(600,568,3,30)}
<circle cx="700" cy="250" r="38"/><path d="M700 190 L700 176 M700 310 L700 324 M640 250 L626 250 M760 250 L774 250" stroke-width="3"/>
{gulls(240,250,1)}{gulls(310,300,.8)}<path d="M250 660 L330 640" stroke-width="3"/>'''

def giebel():
    rows=''
    for r,(y,n) in enumerate(((330,3),(410,4),(490,5))):
        w=60+r*20; x0=420-(n-1)*w/2*0.0
        for i in range(n):
            cx=330+(i-(n-1)/2)*70+90; rows+=circ(round(cx),y,16) if r<2 else f'<path d="M{cx-18:.0f} {y+40} L{cx-18:.0f} {y} Q{cx:.0f} {y-26} {cx+18:.0f} {y} L{cx+18:.0f} {y+40}"/>'
    return f'''
<path d="M240 620 L240 500 L270 500 L270 440 L300 440 L300 380 L330 380 L330 320 L360 320 L360 260 L420 200 L480 260 L480 320 L510 320 L510 380 L540 380 L540 440 L570 440 L570 500 L600 500 L600 620"/>
<path d="M240 620 L240 500 L270 500 L270 440 L300 440 L300 380 L330 380 L330 320 L360 320 L360 260 L420 330 L420 620Z" {H2}/>
<path d="M420 200 L420 170 M408 182 L432 182" stroke-width="3"/>{rows}
<rect x="380" y="560" width="80" height="60"/><path d="M380 560 Q420 520 460 560" />
<path d="M660 620 L660 280 M660 320 L740 560 L660 560 M660 360 L610 560 L660 560" /><path d="M660 280 L660 240 M650 250 L670 250" stroke-width="3"/><path d="M660 320 L760 330 M660 400 L780 420" stroke-width="3"/>
<path d="M610 620 L790 620 L770 650 L630 650Z"/><path d="M200 650 Q500 640 800 650"/>{gulls(560,240,.9)}'''

def trauungsbogen():
    ch=''
    for row,(y,s) in enumerate(((520,1.0),(580,1.15))):
        for side in (-1,1):
            for i in range(2):
                x=500+side*(120+i*60*s+row*10)
                ch+=f'<path d="M{x-18} {y} L{x-18} {y-44} L{x+18} {y-44} L{x+18} {y}"/><path d="M{x-22} {y} L{x+22} {y} M{x-14} {y} L{x-14} {y+26} M{x+14} {y} L{x+14} {y+26}" stroke-width="3"/>'
    fl=''.join(circ(x,y,r)+f'<path d="M{x-r*.5:.0f} {y} q{r*.5:.0f} {-r*.6:.0f} {r:.0f} 0" stroke-width="2.5"/>' for x,y,r in ((330,330,22),(350,270,18),(392,226,20),(448,196,16),(552,196,16),(608,226,20),(650,270,18),(670,330,22),(325,390,16),(675,390,16)))
    return f'''
<path d="M340 560 L340 330 Q340 200 500 200 Q660 200 660 330 L660 560" stroke-width="6"/>
{fl}<path d="M350 330 Q352 220 500 214 Q648 220 650 330" {H}/>
{ch}
<path d="M470 560 L440 660 M530 560 L560 660" stroke-width="3"/><path d="M200 650 Q500 630 800 650"/>{gulls(250,250,.9)}{cloud(670,170,.7)}'''

def hotelbett():
    return f'''
<path d="M300 180 L700 180 L700 420 L300 420 Z" stroke-width="6"/><path d="M500 180 L500 420 M300 300 L700 300" stroke-width="4"/>
<path d="M300 360 Q400 340 500 360 T700 360 L700 420 L300 420Z" {H}/><circle cx="380" cy="250" r="30"/><path d="M380 206 L380 192 M380 294 L380 308 M336 250 L322 250 M424 250 L438 250" stroke-width="3"/>
<path d="M600 240 q20 -22 40 0 M560 270 q16 -18 32 0" stroke-width="3"/>
<path d="M250 640 L250 470 L750 470 L750 640"/><path d="M250 470 L250 440 Q500 420 750 440 L750 470"/>
<path d="M250 560 L750 560 L750 600 L250 600Z" {H2}/>
<path d="M280 520 Q360 490 440 520 L440 470 L280 470Z"/><path d="M560 520 Q640 490 720 520 L720 470 L560 470Z"/>
<path d="M250 560 Q500 540 750 560"/><path d="M250 640 L250 660 M750 640 L750 660"/>
<path d="M200 650 L800 650" stroke-width="3"/>'''

def kalender():
    cells=''
    for r in range(5):
        for c in range(7):
            x=300+c*57; y=330+r*50
            cells+=f'<path d="M{x} {y} l0 50 M{x} {y} l57 0" stroke-width="2.5"/>'
    return f'''
<path d="M290 230 L710 230 L710 590 L290 590Z"/><path d="M290 230 L710 230 L710 310 L290 310Z" {H}/>
{''.join(f'<path d="M{x} 206 L{x} 252"/>' for x in (350,420,490,560,630))}
<path d="M300 330 L700 330 L700 580 L300 580Z" stroke-width="3"/>{cells}
<path d="M300 580 L700 580 M700 330 L700 580" stroke-width="3"/>
<path d="M527 440 q-20 -22 -2 -32 q12 -6 17 8 q8 -14 20 -6 q16 10 -4 30 l-16 16z" stroke-width="4"/>
{circ(528,458,34)}
{''.join(f'<path d="M{x} {y} l12 12 M{x+12} {y} l-12 12" stroke-width="3"/>' for x,y in ((326,350),(383,350),(440,400)))}
<path d="M200 650 Q500 630 800 650"/>'''

def umschlag():
    return f'''
<path d="M330 290 L330 180 L670 180 L670 290"/><path d="M360 220 L640 220 M360 250 L560 250" stroke-width="3"/>
<path d="M270 290 L730 290 L730 590 L270 590Z"/><path d="M270 290 L500 470 L730 290"/><path d="M270 590 L440 430 M730 590 L560 430" stroke-width="3"/>
<path d="M270 290 L500 470 L730 290Z" {H}/>
<circle cx="500" cy="468" r="36"/><path d="M500 488 q-26 -20 -12 -34 q10 -8 12 6 q2 -14 12 -6 q14 14 -12 34z" stroke-width="3"/>
<path d="M240 190 l20 20 M760 190 l-20 20 M500 140 l0 28" stroke-width="3"/>{flake_s(250,560,0)}
<path d="M220 640 Q500 620 780 640"/>'''

def trauzeugen():
    rows=''.join(f'<rect x="548" y="{y}" width="26" height="26" rx="3" stroke-width="3"/><path d="M584 {y+13} L690 {y+13}" stroke-width="3"/>' for y in (250,310,370,430))
    return f'''
<g transform="translate(-60,60)">{flute(340,300,0)}</g><g transform="translate(40,60)">{flute(420,300,0)}</g>
<rect x="520" y="190" width="200" height="300" rx="12"/><rect x="590" y="172" width="60" height="34" rx="8"/>{rows}
<path d="M552 262 l8 9 l14 -20 M552 322 l8 9 l14 -20" stroke-width="5"/>
<path d="M230 640 Q500 620 770 640"/>'''

def rede():
    return f'''
<ellipse cx="420" cy="260" rx="62" ry="78"/><ellipse cx="420" cy="260" rx="62" ry="78" {H2}/>
<path d="M360 250 Q420 280 480 250 M362 280 Q420 306 478 280" stroke-width="3"/>
<path d="M385 330 L385 372 L455 372 L455 330"/><path d="M420 372 L420 580"/><path d="M360 600 Q420 570 480 600 Z"/>
<path d="M330 330 Q330 410 420 410 Q510 410 510 330" stroke-width="3"/>
<path d="M560 520 L690 480 L722 590 L592 630Z"/><path d="M586 540 L670 514 M594 570 L682 544 M600 600 L690 574" stroke-width="3"/>
<path d="M545 500 L675 462 L706 570 L576 608Z"/>
<path d="M300 150 q16 -22 40 -6 M520 160 q16 -22 40 -6" stroke-width="3"/>
<path d="M200 650 Q500 630 800 650"/>'''

def mappe():
    return f'''
<path d="M250 250 L250 590 L620 590 L620 270 L450 270 L420 240 L250 240Z"/><path d="M250 590 L250 330 L620 330 L620 590" stroke-width="3"/>
<path d="M300 300 L300 230 L560 230 L560 300"/><path d="M325 255 L535 255 M325 280 L480 280" stroke-width="3"/>
<path d="M300 380 L570 380 M300 420 L520 420 M300 460 L560 460" stroke-width="3"/>
<circle cx="520" cy="530" r="38"/><circle cx="520" cy="530" r="26" stroke-width="3"/><path d="M505 530 l10 12 l20 -24" stroke-width="5"/>
<path d="M700 330 L700 470 M670 470 L730 470 L730 500 L670 500Z M660 500 L740 500 L740 560 L660 560Z"/><path d="M660 560 L740 560 L740 580 L660 580Z" {H2}/>
<path d="M660 640 L740 640" stroke-width="3"/><rect x="680" y="600" width="60" height="36" rx="4" stroke-width="3"/>
<path d="M200 650 Q500 640 800 650"/>'''

def styling():
    br=''.join(circ(x,y,3) for x in (396,420,444) for y in (250,276,302))
    return f'''
<circle cx="360" cy="280" r="100"/><circle cx="360" cy="280" r="80" {H}/><path d="M360 380 L360 440 Q360 470 340 480 L340 620 L380 620 L380 480 Q360 470 360 440" stroke-width="4"/>
<path d="M300 220 q30 -30 70 -24" stroke-width="3"/>
<path d="M520 220 L520 480 Q520 520 560 520 Q600 520 600 480 L600 220 Q560 190 520 220Z"/><path d="M520 220 Q560 250 600 220" stroke-width="3"/>{br.replace('396','536').replace('420','560').replace('444','584')}
<path d="M560 520 L560 640" /><path d="M545 640 L575 640" />
<path d="M660 250 L760 450 M760 250 L660 450"/><circle cx="650" cy="480" r="26"/><circle cx="770" cy="480" r="26"/><circle cx="650" cy="480" r="12" stroke-width="3"/><circle cx="770" cy="480" r="12" stroke-width="3"/>
<path d="M220 560 L440 560 L440 600 L220 600Z"/><path d="M230 560 L230 600 M250 560 L250 600 M270 560 L270 600 M290 560 L290 600 M310 560 L310 600 M330 560 L330 600 M350 560 L350 600 M370 560 L370 600 M390 560 L390 600 M410 560 L410 600 M430 560 L430 600" stroke-width="2.5"/>
<path d="M650 560 L650 640 L690 640 L690 560Z"/><path d="M650 590 L690 590" stroke-width="3"/><path d="M652 560 Q670 520 688 560" />'''

def paarfotos():
    return f'''
<path d="M260 330 L340 330 L370 290 L630 290 L660 330 L740 330 Q770 330 770 360 L770 560 Q770 590 740 590 L260 590 Q230 590 230 560 L230 360 Q230 330 260 330Z"/>
<path d="M260 330 L340 330 L370 290 L630 290 L660 330 L740 330 Q770 330 770 360 L770 400 L230 400 L230 360 Q230 330 260 330Z" {H}/>
<circle cx="500" cy="480" r="86"/><circle cx="500" cy="480" r="58" {H2}/><circle cx="500" cy="480" r="58"/>
<path d="M500 510 q-34 -24 -16 -42 q14 -8 16 8 q2 -16 16 -8 q18 18 -16 42z" stroke-width="3"/>
<rect x="262" y="352" width="56" height="30" rx="6"/><circle cx="710" cy="365" r="12"/>
<path d="M500 250 q-50 -40 -22 -66 q22 -12 22 14 q0 -26 24 -14 q28 26 -24 66z"/>
<path d="M310 220 l-26 -22 M690 220 l26 -22 M240 280 l-26 -6 M760 280 l26 -6" stroke-width="3"/>
<path d="M230 640 Q500 620 770 640"/>'''

def tisch():
    ch=''
    for k in range(8):
        a=k*math.pi/4; x=500+150*math.cos(a); y=400+150*math.sin(a)
        ch+=f'<circle cx="{x:.0f}" cy="{y:.0f}" r="28" transform="rotate(0)"/>'
    plates=''.join(circ(round(500+100*math.cos(k*math.pi/4)),round(400+100*math.sin(k*math.pi/4)),20) for k in range(8))
    cards=''
    for k in range(8):
        a=k*math.pi/4+math.pi/8; x=500+62*math.cos(a); y=400+62*math.sin(a)
        cards+=f'<path d="M{x-16:.0f} {y+8:.0f} L{x-12:.0f} {y-8:.0f} L{x+12:.0f} {y-8:.0f} L{x+16:.0f} {y+8:.0f}Z" stroke-width="3"/>'
    return f'''
<circle cx="500" cy="400" r="122"/>{plates}
{ch}{cards}
<path d="M480 420 L480 390 Q480 376 500 376 Q520 376 520 390 L520 420Z"/><path d="M500 376 L500 350 M500 360 q-16 -14 -24 -4 M500 354 q16 -14 24 -4" stroke-width="3"/>
<path d="M200 650 Q500 640 800 650"/>'''

def geschenk():
    return f'''
<path d="M280 360 L720 360 L720 450 L280 450Z"/><path d="M300 450 L300 610 L700 610 L700 450"/>
<path d="M470 360 L470 610 M530 360 L530 610"/><path d="M470 360 L470 610 L530 610 L530 360Z" {H}/>
<path d="M500 360 Q430 270 380 300 Q340 340 440 360Z"/><path d="M500 360 Q570 270 620 300 Q660 340 560 360Z"/><path d="M440 360 Q480 330 500 360 Q520 330 560 360" stroke-width="3"/>
<path d="M500 360 L450 420 M500 360 L550 420" stroke-width="3"/>
<path d="M300 450 L300 610 L340 610 L340 450Z" {H2}/>
<path d="M280 230 l-18 -22 M720 230 l18 -22 M500 220 l0 -34" stroke-width="3"/>{flake_s(240,300,0)}
<path d="M220 640 Q500 625 780 640"/>'''

def flitter():
    return f'''
<path d="M300 330 L300 310 Q300 290 320 290 L480 290 Q500 290 500 310 L500 330" stroke-width="5"/>
<path d="M250 330 L550 330 L550 600 L250 600Z"/><path d="M280 330 L280 600 M520 330 L520 600" stroke-width="3"/><path d="M250 450 L550 450" stroke-width="3"/>
<path d="M250 330 L550 330 L550 380 L250 380Z" {H2}/><circle cx="400" cy="520" r="30"/><path d="M400 500 L400 540 M380 520 L420 520" stroke-width="3"/>
<path d="M270 600 L270 622 M530 600 L530 622" stroke-width="5"/>
<g transform="translate(610,210) rotate(-18)"><path d="M-110 0 Q-120 -20 -90 -22 L70 -22 Q130 -20 140 0 Q130 20 70 22 L-90 22 Q-120 20 -110 0Z"/><path d="M-10 -22 L-60 -90 L-30 -90 L40 -22 M-10 22 L-60 90 L-30 90 L40 22"/><path d="M-100 -20 L-130 -64 L-108 -64 L-70 -22"/><path d="M60 -8 L110 -8" stroke-width="3"/><circle cx="100" cy="0" r="4"/></g>
<path d="M640 340 q20 -10 40 0 M600 400 q20 -10 40 0" stroke-width="3"/>
<circle cx="700" cy="480" r="38"/><path d="M700 430 L700 418 M700 530 L700 542 M650 480 L638 480 M750 480 L762 480" stroke-width="3"/>
<path d="M200 650 Q500 630 800 650"/>'''

def strauss():
    fl=''
    for x,y,r in ((430,300,50),(540,280,56),(490,380,46),(380,390,40),(600,380,40)):
        fl+=circ(x,y,r)+circ(x,y,round(r*.55))+circ(x,y,round(r*.2))+''.join(f'<path d="M{x+r*.55*math.cos(k*1.2566):.0f} {y+r*.55*math.sin(k*1.2566):.0f} L{x+r*math.cos(k*1.2566):.0f} {y+r*math.sin(k*1.2566):.0f}" stroke-width="3"/>' for k in range(5))
    lv=''.join(f'<path d="M{x} {y} q{dx} {-40} {dx*2} {-10} q{-dx} {30} {-dx*2} {10}z" {H2}/>' for x,y,dx in ((330,330,-30),(660,330,30),(300,440,-30),(690,440,30)))
    bs=''.join(circ(x,y,7) for x,y in ((350,300),(640,290),(560,440),(420,450)))
    return f'''{lv}{fl}{bs}
<path d="M470 430 L450 600 M510 430 L530 600 M490 430 L490 610" stroke-width="5"/>
<path d="M440 540 L540 540 L550 580 L430 580Z" {H}/><path d="M430 580 L350 640 L400 600 M550 580 L630 640 L580 600" stroke-width="4"/>
{flake_s(250,230,22)}{flake_s(740,230,18)}{flake_s(250,560,0)}
<path d="M220 650 Q500 635 780 650"/>'''

def gluehwein():
    st=''.join(f'<path d="M{x} 300 q-24 -30 0 -60 q24 -30 0 -60" stroke-width="3"/>' for x in (400,470,540))
    return f'''{st}
<path d="M340 340 L360 560 Q364 600 410 600 L530 600 Q576 600 580 560 L600 340Z"/><path d="M345 380 L596 380" stroke-width="3"/>
<path d="M346 400 L362 556 Q366 592 410 592 L530 592 Q572 592 578 556 L594 400Z" {H}/>
<path d="M600 390 Q690 390 690 460 Q690 530 590 520" stroke-width="5"/><path d="M596 410 Q660 412 660 460 Q660 506 592 500" stroke-width="3"/>
<ellipse cx="470" cy="340" rx="130" ry="20"/>
<path d="M210 640 L330 580 M230 650 L350 590" stroke-width="5"/><path d="M210 640 L230 650" stroke-width="3"/>
<circle cx="700" cy="590" r="50"/><circle cx="700" cy="590" r="38" stroke-width="3"/><path d="M700 590 L700 552 M700 590 L733 571 M700 590 L733 609 M700 590 L700 628 M700 590 L667 609 M700 590 L667 571" stroke-width="3"/>
<path d="M600 640 L640 620 L650 640 L610 650Z" stroke-width="3"/><path d="M642 650 q16 -20 30 -4 q-4 18 -30 4z" stroke-width="3"/>
{flake_s(260,260,22)}{flake_s(740,250,18)}'''

def tageslicht():
    ray=''.join(f'<path d="M500 560 L{500+250*math.cos(a):.0f} {560-250*math.sin(a):.0f}" stroke-width="2.5"/>' for a in [i*math.pi/10 for i in range(11)])
    return f'''{ray}
<path d="M390 560 A110 110 0 0 1 610 560Z" {H}/><path d="M390 560 A110 110 0 0 1 610 560"/>
<path d="M200 560 L800 560"/><path d="M200 590 Q350 580 500 590 T800 590"/><path d="M230 625 Q380 615 530 625 T800 625"/>
<circle cx="700" cy="250" r="70"/><circle cx="700" cy="250" r="60" stroke-width="3"/>
<path d="M700 250 L700 205 M700 250 L732 270" stroke-width="5"/><path d="M700 186 L700 196 M700 304 L700 314 M636 250 L646 250 M754 250 L764 250" stroke-width="3"/>
{flake_s(260,260,22)}{flake_s(380,200,16)}'''

def ablauf():
    ticks=''.join(f'<path d="M{500+150*math.sin(k*math.pi/6):.0f} {330-150*math.cos(k*math.pi/6):.0f} L{500+128*math.sin(k*math.pi/6):.0f} {330-128*math.cos(k*math.pi/6):.0f}" stroke-width="3"/>' for k in range(12))
    tl=''.join(f'<circle cx="{x}" cy="570" r="12"/><path d="M{x} 582 L{x} 600" stroke-width="3"/><path d="M{x-30} 610 L{x+30} 610" stroke-width="3"/>' for x in (270,400,530,660,790)[:4])
    return f'''
<circle cx="500" cy="330" r="170"/><circle cx="500" cy="330" r="156" stroke-width="3"/>{ticks}
<path d="M500 330 L500 220 M500 330 L580 372" stroke-width="7"/><circle cx="500" cy="330" r="10"/>
<path d="M500 160 L500 140 M485 140 L515 140"/>
<path d="M250 570 L760 570" stroke-width="4"/>{tl}<path d="M760 570 l-18 -12 M760 570 l-18 12" stroke-width="4"/>
<path d="M280 250 q-10 -26 14 -34 M720 250 q10 -26 -14 -34" stroke-width="3"/>'''

def torte():
    def tier(cx,y,w,h):
        return f'<path d="M{cx-w/2} {y} L{cx-w/2} {y+h} Q{cx} {y+h+18} {cx+w/2} {y+h} L{cx+w/2} {y}"/><ellipse cx="{cx}" cy="{y}" rx="{w/2}" ry="16"/><path d="M{cx-w/2+10} {y+h*0.55} Q{cx} {y+h*0.55+22} {cx+w/2-10} {y+h*0.55}" stroke-width="3"/>'+''.join(circ(round(cx-w/2+22+i*(w-44)/5),round(y+h*0.55+9+ (6 if i%2 else 0)),5) for i in range(6))
    return f'''
{tier(500,470,420,100)}{tier(500,350,290,100)}{tier(500,240,170,90)}
<path d="M500 224 L500 190 M478 196 q22 -34 44 0" stroke-width="4"/><circle cx="500" cy="180" r="8"/>
<path d="M270 600 Q500 625 730 600" /><path d="M240 640 L760 640"/>
<path d="M250 300 l-20 -20 M750 300 l20 -20 M270 230 l-24 0 M730 230 l24 0" stroke-width="3"/>
<path d="M360 330 q10 -20 20 0 M610 450 q10 -20 20 0" stroke-width="3"/>'''

def fotostunden():
    return f'''
<circle cx="440" cy="400" r="190"/><circle cx="440" cy="400" r="170" stroke-width="3"/>
{''.join(f'<path d="M{440+170*math.sin(k*math.pi/6):.0f} {400-170*math.cos(k*math.pi/6):.0f} L{440+148*math.sin(k*math.pi/6):.0f} {400-148*math.cos(k*math.pi/6):.0f}" stroke-width="3"/>' for k in range(12))}
<path d="M440 400 L440 300 M440 400 L510 440" stroke-width="7"/>
<path d="M395 190 L395 160 L485 160 L485 190"/><path d="M380 160 L500 160"/>
<g transform="translate(560,380)"><path d="M0 40 L40 40 L55 20 L145 20 L160 40 L200 40 Q215 40 215 55 L215 150 Q215 165 200 165 L0 165 Q-15 165 -15 150 L-15 55 Q-15 40 0 40Z"/><circle cx="100" cy="100" r="42"/><circle cx="100" cy="100" r="26" {H2}/><circle cx="100" cy="100" r="26"/></g>
<path d="M200 650 Q500 635 800 650"/>'''

def goldenestunde():
    ray=''.join(f'<path d="M500 520 L{500+300*math.cos(a):.0f} {520-300*math.sin(a):.0f}" stroke-width="2.5"/>' for a in [0.1+i*0.3 for i in range(10)])
    return f'''{ray}
<path d="M360 520 A140 140 0 0 1 640 520Z" {H}/><path d="M360 520 A140 140 0 0 1 640 520"/>
<path d="M200 520 L800 520"/>{waves(240,560,150,2)}{waves(520,560,150,2)}
{gulls(630,260,1)}{gulls(700,300,.8)}{gulls(280,280,.9)}'''

def tischkarte():
    return f'''
<path d="M250 440 L420 440 L440 360 L270 360Z"/><path d="M250 440 L420 440 L420 500 L250 500Z"/><path d="M270 360 L440 360 L440 420 L420 440" stroke-width="3"/>
<path d="M285 470 L385 470" stroke-width="5"/><path d="M300 485 L370 485" stroke-width="3"/>
<path d="M500 220 L740 220 L740 580 L500 580Z"/><path d="M530 270 L710 270 M530 300 L690 300 M560 350 L680 350 M560 380 L670 380 M545 430 L700 430 M565 460 L670 460" stroke-width="3"/><path d="M590 245 q20 -22 40 0" stroke-width="3"/>
<path d="M500 540 L740 540" stroke-width="3"/>
<path d="M250 560 Q330 530 410 560" stroke-width="3"/><path d="M300 300 q18 -30 36 0 q18 -30 36 0 q-36 40 -72 0z" stroke-width="3"/>
<path d="M200 620 Q500 605 800 620"/>'''

def hochzeitstyp():
    def card(x,y,r):
        return f'<g transform="translate({x},{y}) rotate({r})"><rect x="-80" y="-100" width="160" height="200" rx="6"/><rect x="-64" y="-84" width="128" height="130" {H2}/><rect x="-64" y="-84" width="128" height="130" stroke-width="3"/></g>'
    flower=circ(500,360,16)+''.join(circ(round(500+34*math.cos(k*1.2566)),round(360+34*math.sin(k*1.2566)),16) for k in range(5))
    return f'''
{card(340,400,-10)}{card(500,380,0)}{card(660,400,10)}
<path d="M338 395 q-40 -30 -18 -52 q18 -10 20 12 q2 -22 22 -12 q22 22 -24 52z" stroke-width="4"/>
{flower}<path d="M500 396 L500 440" stroke-width="3"/>
<ellipse cx="668" cy="372" rx="26" ry="32"/><path d="M646 330 L668 306 L690 330 L668 352Z" stroke-width="3"/>
<path d="M320 540 L360 540 M480 540 L520 540 M640 540 L680 540" stroke-width="4"/>
<path d="M500 235 q-40 -34 -18 -56 q18 -10 18 12 q0 -22 20 -12 q22 22 -20 56z"/>
<path d="M200 640 Q500 625 800 640"/>'''

MOTIVE_NEU={'outfit':outfit,'silvester':silvester,'lichter':lichter,'tannenzweig':tannenzweig,'kreidefelsen':kreidefelsen,'ringbox':ringbox,'unterkunft':unterkunft,'seebruecke':seebruecke,'darss':darss,'giebel':giebel,'trauungsbogen':trauungsbogen,'hotelbett':hotelbett,'kalender':kalender,'umschlag':umschlag,'trauzeugen':trauzeugen,'rede':rede,'mappe':mappe,'styling':styling,'paarfotos':paarfotos,'tisch':tisch,'geschenk':geschenk,'flitter':flitter,'strauss':strauss,'gluehwein':gluehwein,'tageslicht':tageslicht,'ablauf':ablauf,'torte':torte,'fotostunden':fotostunden,'goldenestunde':goldenestunde,'tischkarte':tischkarte,'hochzeitstyp':hochzeitstyp}

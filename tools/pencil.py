"""Bleistift-Motive als SVG-Gruppen (Bereich ca. x 200-800, y 140-660). Jedes Motiv wird später doppelt mit Wackel-Filter gezeichnet."""
import math
H='fill="url(#h)" stroke="none"'      # lockere Schraffur
H2='fill="url(#h2)" stroke="none"'    # dichte Schraffur
def gulls(x,y,s=1):
    return f'<path d="M{x} {y} q{15*s} {-20*s} {30*s} 0 q{15*s} {-20*s} {30*s} 0"/>'
def cloud(x,y,s=1):
    return f'<path d="M{x} {y} q{-5*s} {-30*s} {30*s} {-28*s} q{15*s} {-35*s} {55*s} {-12*s} q{40*s} {-12*s} {45*s} {25*s} q{25*s} {5*s} {15*s} {15*s} z"/>'
def grass(x,y,n=5,h=40):
    return ''.join(f'<path d="M{x+i*12} {y} q{(-1)**i*8} {-h*0.6} {(-1)**i*14} {-h+(i%3)*8}"/>' for i in range(n))
def waves(x,y,w,n=3):
    return ''.join(f'<path d="M{x+i*18} {y+i*24} q{w/6} -14 {w/3} 0 t{w/3} 0 t{w/3} 0"/>' for i in range(n))

def ruegen():
    b=''
    for i,y in enumerate([300,360,420,480]):
        w0=70+(y-300)*0.2
        if i%2==0: b+=f'<path d="M{500-w0/2} {y} L{500+w0/2} {y} L{500+w0/2+6} {y+60} L{500-w0/2-6} {y+60} Z" {H2}/>'
    return f'''
<path d="M{500-35} 300 L{500-60} 545 L{500+60} 545 L{500+35} 300 Z"/>
<path d="M{500-70} 548 L{500+70} 548"/>
{b}
<path d="M{500-38} 300 L{500+38} 300 M{500-38} 300 L{500-46} 290 L{500+46} 290 L{500+38} 300"/>
<path d="M{500-46} 290 L{500+46} 290"/>
<rect x="472" y="248" width="56" height="42"/><path d="M472 269 L528 269 M500 248 L500 290"/>
<path d="M466 248 L500 212 L534 248 Z"/><path d="M500 212 L500 186 M492 190 L508 190"/>
<path d="M482 548 L482 515 Q500 495 518 515 L518 548"/><path d="M500 498 L500 548"/>
<rect x="490" y="395" width="20" height="26" /><rect x="490" y="455" width="20" height="26"/>
<path d="M468 268 L360 232 M468 276 L350 280 M532 268 L640 232 M532 276 L650 280" stroke-width="3"/>
<path d="M200 600 Q300 565 420 560 L580 560 Q700 565 800 600 L800 665 L200 665 Z"/>
<path d="M200 600 Q300 565 420 560 L580 560 Q700 565 800 600 L800 665 L200 665 Z" {H}/>
<path d="M250 640 L270 600 M330 650 L345 590 M650 650 L640 590 M730 640 L715 600" stroke-width="3"/>
{grass(255,590,4,34)}{grass(715,592,4,34)}{grass(380,566,3,26)}{grass(585,566,3,26)}
{cloud(230,215,1.1)}{cloud(630,190,0.9)}{cloud(690,330,0.7)}
{gulls(270,330)}{gulls(330,372,.8)}{gulls(610,420,.9)}
{waves(215,668,60,1)}'''

def strand():
    # Korb-Haube als Bogen mit Streifen
    x0,x1,yb=360,640,410
    def ya(x): t=(x-x0)/(x1-x0); return yb-4*(yb-215)*t*(1-t)
    stripes='';lines=''
    xs=[x0+i*(x1-x0)/10 for i in range(11)]
    for i in range(10):
        a,b=xs[i],xs[i+1]
        if i%2==0: stripes+=f'<path d="M{a} {yb} L{a} {ya(a)} L{b} {ya(b)} L{b} {yb} Z" {H2}/>'
    for x in xs: lines+=f'M{x} {yb} L{x} {ya(x)} '
    wick=''.join(f'<path d="M382 {y} q30 -8 60 0 t60 0 t60 0 t55 0" stroke-width="3"/>' for y in range(440,560,20))
    return f'''
<path d="M{x0} {yb} Q500 {yb-2*(yb-215)} {x1} {yb}"/>
<path d="{lines}" stroke-width="3"/>{stripes}
<path d="M{x0-8} {yb} L{x1+8} {yb} L{x1+8} {yb+14} L{x0-8} {yb+14} Z"/>
<path d="M378 424 L378 575 M622 424 L622 575"/>
<path d="M378 575 L622 575"/>{wick}
<path d="M378 480 Q500 505 622 480" stroke-width="3"/>
<path d="M362 575 L362 596 Q450 604 540 596 L638 596 L638 575"/>
<path d="M430 600 L560 600" stroke-width="3"/>
<circle cx="722" cy="235" r="38"/><path d="M722 170 L722 150 M722 300 L722 320 M657 235 L637 235 M787 235 L807 235 M676 189 L662 175 M768 281 L782 295 M768 189 L782 175 M676 281 L662 295" stroke-width="3"/>
<path d="M200 592 Q280 560 340 590 M660 592 Q740 560 800 592" />
<path d="M200 600 Q300 585 360 610 L360 665 L200 665Z M640 610 Q700 585 800 600 L800 665 L640 665Z"/>
<path d="M200 600 Q300 585 360 610 L360 665 L200 665Z M640 610 Q700 585 800 600 L800 665 L640 665Z" {H}/>
{grass(215,598,6,56)}{grass(690,600,6,60)}
{gulls(250,300)}{gulls(300,345,.8)}{gulls(560,178,.8)}
<path d="M250 640 q22 -22 44 0 q-22 8 -44 0 M262 636 l10 -14" stroke-width="3"/>
<path d="M200 330 L340 330 M660 330 L800 330" stroke-width="3"/>{waves(215,345,110,2)}'''

def budgetrechner():
    keys=''
    for r in range(4):
        for c in range(4):
            x=405+c*50; y=340+r*52
            keys+=f'<rect x="{x}" y="{y}" width="38" height="38" rx="8"/>'
    coins=''
    for i in range(5):
        y=610-i*20; coins+=f'<ellipse cx="715" cy="{y}" rx="55" ry="16"/><path d="M660 {y} L660 {y-18} M770 {y} L770 {y-18}"/>'
    coins+='<ellipse cx="715" cy="510" rx="55" ry="16"/><text x="715" y="516" font-family="DejaVu Serif" font-size="22" text-anchor="middle" stroke="none" fill="#3d3935">€</text>'
    return f'''
<rect x="375" y="190" width="250" height="400" rx="26"/><rect x="388" y="203" width="224" height="374" rx="18" stroke-width="3"/>
<rect x="405" y="222" width="190" height="80" rx="8"/><path d="M405 222 L595 222 L595 302 L405 302Z" {H}/>
<rect x="410" y="228" width="180" height="68" fill="#faf7f4" stroke="none"/><text x="582" y="278" font-family="DejaVu Serif" font-size="38" text-anchor="end" stroke="none" fill="#3d3935">12.500 €</text>
{keys}
<path d="M610 192 L625 210 L625 590 L610 575 Z" {H2}/>
{coins}
<path d="M650 614 L780 614"/>
<circle cx="285" cy="470" r="38"/><text x="285" y="484" font-family="DejaVu Serif" font-size="40" text-anchor="middle" stroke="none" fill="#3d3935">€</text>
<path d="M255 430 L240 410 M315 430 L330 410" stroke-width="3"/>{grass(215,598,3,30)}'''

def gaesteliste():
    rows=''
    for i in range(5):
        y=300+i*58
        rows+=f'<rect x="405" y="{y}" width="30" height="30" rx="4"/><path d="M{455} {y+20} q25 -22 50 -2 t55 0 t35 -4" stroke-width="3"/>'
        if i!=3: rows+=f'<path d="M409 {y+16} l9 10 l16 -26" stroke-width="6"/>'
    return f'''
<rect x="350" y="200" width="300" height="400" rx="14"/><rect x="362" y="214" width="276" height="372" rx="8" stroke-width="3"/>
<path d="M350 200 L650 200 L650 600 L350 600Z" {H}/>
<rect x="395" y="240" width="210" height="340" fill="#faf7f4" stroke="none"/>
<rect x="440" y="170" width="120" height="52" rx="10"/><circle cx="500" cy="196" r="9"/>
<path d="M410 262 q40 -14 80 0 t90 0 M410 272 q70 8 170 0" stroke-width="3"/>
{rows}
<path d="M670 590 L560 450 L580 434 L690 574 Z" fill="#faf7f4"/><path d="M570 440 L554 462 L548 478 L568 464Z" {H2}/><path d="M620 506 L636 494 M638 528 L654 516" stroke-width="3"/>
<path d="M270 330 q-40 -50 0 -80 q40 30 0 80 z M730 260 q-30 -40 0 -60 q30 20 0 60z"/><path d="M270 330 L270 420 M730 260 L730 350"/>'''

def sitzplan():
    ch=''
    for k in range(8):
        a=k*45
        ch+=f'<g transform="rotate({a} 500 420) translate(500 255)"><path d="M-28 -8 Q0 -26 28 -8 L24 24 Q0 34 -24 24 Z"/><path d="M-22 0 L22 0" stroke-width="3"/></g>'
    pl=''.join(f'<circle cx="{500+78*math.cos(math.radians(k*45-90)):.0f}" cy="{420+78*math.sin(math.radians(k*45-90)):.0f}" r="22" stroke-width="3"/>' for k in range(8))
    cards=''.join(f'<path d="M{x-16} {y+8} L{x} {y-14} L{x+16} {y+8} Z" stroke-width="3"/>' for x,y in [(500,360),(558,455),(442,455)])
    return f'''{ch}
<circle cx="500" cy="420" r="118"/><circle cx="500" cy="420" r="102" stroke-width="3"/>
<circle cx="500" cy="420" r="118" {H}/><circle cx="500" cy="420" r="96" fill="#e9dfd6" stroke="none"/>
{pl}
<circle cx="500" cy="420" r="30"/><path d="M500 390 q-26 10 0 30 q26 -20 0 -30 M470 420 q10 -26 30 0 q-20 26 -30 0 M530 420 q-10 26 -30 0 q20 -26 30 0" stroke-width="3"/>
{cards}
<path d="M260 600 q240 40 480 0" /><path d="M270 640 q230 30 460 0" stroke-width="3"/>
<path d="M240 560 l0 -90 M280 560 l0 -90 M240 470 q20 -22 40 0"/><circle cx="260" cy="440" r="14"/>
<path d="M770 560 l0 -90 M730 560 l0 -90 M730 470 q20 -22 40 0"/><circle cx="750" cy="440" r="14"/>'''

def getraenke():
    return f'''
<path d="M372 600 L372 345 Q372 322 392 306 L392 232 L408 232 L408 306 Q428 322 428 345 L428 600 Z"/>
<rect x="390" y="212" width="20" height="24" rx="4" {H2}/><path d="M388 212 L412 212"/>
<rect x="372" y="440" width="56" height="96"/><path d="M372 440 L428 440 L428 536 L372 536Z" fill="#faf7f4" stroke="none"/><rect x="372" y="440" width="56" height="96"/>
<path d="M384 470 q16 -10 32 0 M384 490 q16 -8 32 0 M392 512 l16 0" stroke-width="3"/>
<path d="M372 345 L372 600 L388 600 L388 345Z" {H2}/>
<path d="M480 300 L552 300 Q548 410 520 428 L520 560 M520 428 Q492 410 480 300 M520 560 Q500 562 490 590 L550 590 Q540 562 520 560"/>
<path d="M486 330 L546 330" stroke-width="3"/><circle cx="508" cy="380" r="5"/><circle cx="526" cy="350" r="4"/><circle cx="515" cy="410" r="4"/><circle cx="500" cy="352" r="3"/>
<path d="M486 330 L550 330 Q548 400 520 424 Q492 400 486 330Z" {H}/>
<path d="M590 340 Q580 440 650 450 Q720 440 710 340 Z"/><path d="M590 340 L710 340"/><path d="M650 450 L650 570 M610 592 Q650 575 690 592 Z"/>
<path d="M596 395 Q650 410 704 395 L706 340 L592 340Z" {H}/>
<path d="M200 600 L800 600" stroke-width="3"/>
<path d="M740 560 l32 -70 l22 12 l-10 60 z M752 540 l30 12" stroke-width="3"/>'''

def checkliste():
    g=''
    for r in range(4):
        for c in range(5):
            x=380+c*50; y=345+r*54
            g+=f'<rect x="{x}" y="{y}" width="44" height="46" stroke-width="2.5"/>'
    ticks=''.join(f'<path d="M{x+8} {y+24} l12 12 l18 -28" stroke-width="6"/>' for x,y in [(380,345),(430,345),(480,345),(380,399),(430,399),(530,399)])
    return f'''
<rect x="350" y="200" width="300" height="400" rx="14"/><path d="M350 200 L650 200 L650 290 L350 290Z" {H}/>
{''.join(f'<path d="M{385+i*46} 175 L{385+i*46} 222"/>' for i in range(6))}{''.join(f'<circle cx="{385+i*46}" cy="198" r="10"/>' for i in range(6))}
<rect x="410" y="232" width="180" height="42" rx="6" fill="#faf7f4"/><text x="500" y="264" font-family="DejaVu Serif" font-size="30" text-anchor="middle" stroke="none" fill="#2b2622" font-style="italic">12 Monate</text>
{g}{ticks}
<path d="M594 430 q-30 -40 0 -62 q30 22 0 62z" stroke-width="6"/><circle cx="602" cy="418" r="36" stroke-width="3"/>
<path d="M270 590 q-30 -80 20 -120 q36 50 -20 120 M270 590 L270 520"/><path d="M730 590 q30 -80 -20 -120 q-36 50 20 120"/>'''

def pdf():
    return f'''
<g transform="rotate(-6 500 400)"><rect x="370" y="230" width="260" height="350"/></g>
<g transform="rotate(4 500 400)"><rect x="370" y="230" width="260" height="350"/></g>
<rect x="372" y="220" width="256" height="360" fill="#faf7f4"/><rect x="372" y="220" width="256" height="360"/>
<g stroke-width="3"><path d="M400 275 l130 0 M400 295 l90 0"/></g><path d="M400 262 L540 262 L540 270 L400 270Z" {H2}/>
{''.join(f'<rect x="402" y="{330+i*48}" width="22" height="22" rx="3"/><path d="M440 {346+i*48} q40 -10 80 0 t60 0" stroke-width="3"/>' for i in range(4))}
<path d="M406 340 l8 8 l12 -18 M406 388 l8 8 l12 -18" stroke-width="5"/>
{''.join(f'<circle cx="372" cy="{250+i*52}" r="9"/>' for i in range(6))}
<path d="M700 600 L596 420 L614 408 L718 588 Z" fill="#faf7f4"/><path d="M596 420 L580 448 L588 456 L614 408Z" {H2}/><path d="M700 600 L718 588 L722 610Z" {H2}/><path d="M648 500 L666 489" stroke-width="3"/>
<path d="M270 590 q-14 -70 30 -90 q30 50 -30 90 M270 590 L286 500" /><path d="M255 520 q-30 -24 -10 -50 q34 10 10 50" stroke-width="3"/>
<circle cx="285" cy="400" r="28"/><circle cx="321" cy="400" r="28"/>'''

def locations():
    # Gutshaus mit Giebel, Fenstern, Bäumen
    win=''.join(f'<rect x="{x}" y="{y}" width="34" height="46"/><path d="M{x+17} {y} L{x+17} {y+46} M{x} {y+22} L{x+34} {y+22}" stroke-width="2.5"/>' for x in (350,420,546,616) for y in (400,490))
    return f'''
<path d="M300 380 L300 600 L700 600 L700 380 Z"/><path d="M300 380 L300 600 L700 600 L700 380 Z" {H}/>
<path d="M300 380 L500 230 L700 380 Z"/><path d="M270 392 L500 215 L730 392"/>
<path d="M440 380 L440 330 L560 330 L560 380 Z"/><circle cx="500" cy="300" r="26"/><path d="M500 280 L500 300 L514 306" stroke-width="3"/>
<rect x="300" y="380" width="400" height="14" fill="#faf7f4"/>
{win}
<path d="M460 600 L460 520 Q500 480 540 520 L540 600" fill="#faf7f4"/><path d="M500 492 L500 600 M460 556 L540 556" stroke-width="2.5"/>
<path d="M440 600 L440 612 L560 612 L560 600 M420 612 L420 624 L580 624 L580 612" stroke-width="3"/>
<path d="M230 600 L230 480 M230 480 q-60 -20 -40 -90 q40 -30 70 -10 q40 -40 70 20 q20 60 -40 80z"/><path d="M770 600 L770 490 M770 490 q60 -20 40 -90 q-40 -30 -70 -10 q-40 -40 -70 20 q-20 60 40 80z"/>
<path d="M200 640 Q500 610 800 640" />{grass(330,640,5,30)}{grass(640,640,5,30)}
{cloud(215,215,1)}{cloud(680,200,.9)}{gulls(560,170,.8)}'''

def kosten():
    # Münzstapel, Sparschwein-ähnlich vereinfacht: Münzen + Herz + Euro
    coins=''.join(f'<ellipse cx="500" cy="{590-i*34}" rx="120" ry="34"/><path d="M380 {590-i*34} L380 {620-i*34} Q500 {660-i*34} 620 {620-i*34} L620 {590-i*34}"/>' for i in range(4))
    return f'''
{coins}
<ellipse cx="500" cy="454" rx="120" ry="34" fill="#faf7f4"/><text x="500" y="468" font-family="DejaVu Serif" font-size="44" text-anchor="middle" stroke="none" fill="#2b2622">€</text>
<path d="M380 454 L380 590 M620 454 L620 590" stroke-width="3"/><path d="M386 530 L614 530 M386 560 L614 560" {H}/>
<circle cx="250" cy="330" r="62"/><text x="250" y="352" font-family="DejaVu Serif" font-size="64" text-anchor="middle" stroke="none" fill="#2b2622">€</text>
<circle cx="760" cy="280" r="48"/><text x="760" y="300" font-family="DejaVu Serif" font-size="50" text-anchor="middle" stroke="none" fill="#2b2622">€</text>
<path d="M500 330 q-70 -60 -70 -100 q0 -45 45 -45 q25 0 25 28 q0 -28 25 -28 q45 0 45 45 q0 40 -70 100z" transform="translate(0 -10)"/>
<path d="M200 640 L800 640" stroke-width="3"/>{grass(250,640,5,28)}{grass(700,640,5,28)}'''

def fotograf():
    return f'''
<path d="M290 330 L350 330 L375 290 L625 290 L650 330 L710 330 Q740 330 740 360 L740 560 Q740 590 710 590 L290 590 Q260 590 260 560 L260 360 Q260 330 290 330Z"/>
<path d="M290 330 L350 330 L375 290 L625 290 L650 330 L710 330 Q740 330 740 360 L740 400 L260 400 L260 360 Q260 330 290 330Z" {H}/>
<circle cx="500" cy="470" r="105"/><circle cx="500" cy="470" r="76"/><circle cx="500" cy="470" r="42"/><circle cx="500" cy="470" r="76" {H2}/>
<path d="M470 440 q14 -14 34 -10" stroke-width="3"/>
<rect x="296" y="352" width="56" height="30" rx="6"/><circle cx="690" cy="360" r="12"/><path d="M640 262 L690 262 L690 290 L640 290Z"/>
<path d="M300 590 q-10 40 -40 50 M700 590 q10 40 40 50" stroke-width="3"/>
<path d="M200 640 Q500 620 800 640"/>{gulls(240,250)}{gulls(700,200,.8)}'''

def winter():
    flake=''
    for k in range(6):
        flake+=f'<g transform="rotate({k*60} 500 330)"><path d="M500 330 L500 205 M500 240 L470 215 M500 240 L530 215 M500 275 L478 258 M500 275 L522 258"/></g>'
    return f'''
{flake}<circle cx="500" cy="330" r="14"/>
<path d="M200 560 Q350 500 500 540 Q650 580 800 520 L800 665 L200 665 Z"/><path d="M200 560 Q350 500 500 540 Q650 580 800 520 L800 665 L200 665 Z" {H}/>
<path d="M360 560 L360 480 Q420 430 480 480 L480 560" /><path d="M360 560 L480 560 M368 540 L472 540" stroke-width="3"/>
<path d="M356 482 Q420 420 484 482" {H2}/><path d="M350 482 q70 -70 140 0 l-10 -12 q-60 -50 -120 0z"/>
<path d="M600 600 q-20 -70 25 -120 q30 40 -25 120 M600 600 L625 480" /><path d="M600 560 q-30 -10 -28 -40 q30 4 28 40"/>
<path d="M610 480 q20 -22 40 0" stroke-width="3"/>
{''.join(f'<circle cx="{x}" cy="{y}" r="5" stroke-width="3"/>' for x,y in [(250,250),(300,400),(720,260),(780,380),(650,180),(340,170),(220,470),(760,470)])}
{waves(230,640,90,1)}'''

def flake_s(x,y,r=22):
    return ''.join(f'<path d="M{x} {y} l{r*__import__("math").cos(k*1.0472):.1f} {r*__import__("math").sin(k*1.0472):.1f}" stroke-width="3"/>' for k in range(6))

def winterfoto():
    sun=''.join(f'<path d="M{660+84*math.cos(k*0.5236):.0f} {250+84*math.sin(k*0.5236):.0f} L{660+118*math.cos(k*0.5236):.0f} {250+118*math.sin(k*0.5236):.0f}" stroke-width="3"/>' for k in range(12))
    return f'''
<circle cx="660" cy="250" r="60"/><circle cx="660" cy="250" r="60" {H}/>{sun}
<g transform="translate(40,120) scale(.9)">
<path d="M290 330 L350 330 L375 290 L625 290 L650 330 L710 330 Q740 330 740 360 L740 560 Q740 590 710 590 L290 590 Q260 590 260 560 L260 360 Q260 330 290 330Z"/>
<path d="M290 330 L350 330 L375 290 L625 290 L650 330 L710 330 Q740 330 740 360 L740 400 L260 400 L260 360 Q260 330 290 330Z" {H}/>
<circle cx="500" cy="470" r="105"/><circle cx="500" cy="470" r="76"/><circle cx="500" cy="470" r="42"/><circle cx="500" cy="470" r="76" {H2}/>
<path d="M470 440 q14 -14 34 -10" stroke-width="3"/><rect x="296" y="352" width="56" height="30" rx="6"/><circle cx="690" cy="360" r="12"/></g>
<path d="M200 650 Q350 625 500 645 Q650 665 800 635"/>
{flake_s(280,230,26)}{flake_s(400,180,18)}{flake_s(790,420,20)}{flake_s(230,380,16)}'''

def wintermakeup():
    return f'''
<path d="M240 560 Q240 610 400 610 Q560 610 560 560 L560 540 Q560 590 400 590 Q240 590 240 540Z"/>
<ellipse cx="400" cy="540" rx="160" ry="52"/><ellipse cx="400" cy="536" rx="122" ry="36" {H}/><ellipse cx="400" cy="536" rx="122" ry="36"/>
<path d="M250 530 L272 300 Q400 262 528 300 L550 530"/><path d="M272 300 Q400 340 528 300" stroke-width="3"/>
<ellipse cx="400" cy="400" rx="104" ry="92" stroke-width="3"/><path d="M340 360 q30 -30 70 -24 M345 392 q40 -26 88 -18" stroke-width="3"/>
<path d="M610 600 L610 470 L690 470 L690 600Z"/><path d="M610 600 L690 600 L690 580 L610 580Z" {H2}/>
<path d="M618 470 L618 410 L682 410 L682 470"/><path d="M618 410 Q618 330 660 300 L682 410Z"/><path d="M618 410 Q618 330 660 300 L682 410Z" {H}/>
<path d="M610 500 L690 500" stroke-width="3"/>
<path d="M722 650 L738 470 L752 470 L760 650Z" {H2}/><path d="M722 650 L738 470 L752 470 L760 650Z"/>
<rect x="732" y="440" width="28" height="36" rx="3"/><path d="M732 440 Q726 390 746 330 Q770 390 760 440Z"/><path d="M732 440 Q726 390 746 330 Q770 390 760 440Z" {H}/>
{flake_s(270,200,24)}{flake_s(470,170,18)}{flake_s(620,215,22)}{flake_s(790,250,16)}
<path d="M200 650 Q500 630 800 650"/>'''

def winterliste():
    rows=''
    for i in range(5):
        y=270+i*66
        rows+=f'<rect x="388" y="{y}" width="38" height="38" rx="4" stroke-width="3"/><path d="M{432+4*0} {y+20} L{432} {y+20}" stroke-width="1"/><path d="M{444} {y+19} L{600} {y+19}" stroke-width="3"/>'
        if i in (0,1,3): rows+=f'<path d="M{395} {y+20} l10 11 l18 -26" stroke-width="6"/>'
    return f'''
<rect x="350" y="200" width="300" height="420" rx="14"/><path d="M350 200 L650 200 L650 245 L350 245Z" {H}/>
<rect x="450" y="176" width="100" height="44" rx="10"/>
{rows}
{flake_s(300,330,28)}{flake_s(720,300,24)}{flake_s(700,470,18)}{flake_s(260,500,20)}
<path d="M200 650 Q500 630 800 650"/>'''

MOTIVE={'winterfoto':winterfoto,'wintermakeup':wintermakeup,'winterliste':winterliste,'locations':locations,'kosten':kosten,'fotograf':fotograf,'winter':winter,'ruegen':ruegen,'strand':strand,'budgetrechner':budgetrechner,'gaesteliste':gaesteliste,'sitzplan':sitzplan,'getraenkerechner':getraenke,'checkliste':checkliste,'pdf':pdf}

try:
    from pencil_neu import MOTIVE_NEU
    MOTIVE.update(MOTIVE_NEU)
except ImportError:
    pass

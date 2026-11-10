"""Zusätzliche Bleistift-Motive: Schloss, Badekarren, Kurhaus, Standesamt."""
from pencil import H,H2,gulls,cloud,grass,waves,MOTIVE
def schloss():
    win=''.join(f'<rect x="{x}" y="{y}" width="18" height="26"/>' for x in (300,350,400,560,610,660) for y in (420,490))
    return f'''
<path d="M260 600 L260 400 L740 400 L740 600"/><path d="M260 400 L260 600 L420 600 L420 400Z" {H}/>
<path d="M440 600 L440 340 L560 340 L560 600"/><path d="M425 340 L500 270 L575 340 Z"/><path d="M425 340 L500 270 L575 340 Z" {H2}/>
<path d="M500 270 L500 235 M492 242 L510 242"/>
<path d="M240 600 L240 330 L330 330 L330 600"/><path d="M228 330 L285 262 L342 330 Z" {H2}/><path d="M228 330 L285 262 L342 330 Z"/>
<path d="M670 600 L670 330 L760 330 L760 600"/><path d="M658 330 L715 262 L772 330 Z"/><path d="M658 330 L715 262 L772 330 Z" {H2}/>
<path d="M285 262 L285 235 M715 262 L715 235"/>
{win}
<path d="M470 600 L470 520 Q500 490 530 520 L530 600"/><path d="M500 498 L500 600"/>
<path d="M200 600 L800 600"/>
<path d="M300 600 Q500 625 700 600" stroke-width="3"/><path d="M360 640 Q500 652 640 640" stroke-width="3"/>
{grass(215,602,3,28)}{grass(745,602,3,28)}
{cloud(250,215,1)}{cloud(600,185,.9)}{gulls(430,210)}{gulls(700,230,.8)}'''
def badekarren():
    spokes=''.join(f'<path d="M{cx} {cy} L{cx+34*__import__("math").cos(a)} {cy+34*__import__("math").sin(a)}" stroke-width="3"/>' for cx,cy in((400,560),(600,560)) for a in (0,.8,1.6,2.4,3.2,4,4.8,5.6))
    return f'''
<path d="M330 330 L330 530 L670 530 L670 330"/><path d="M310 335 L500 240 L690 335 Z"/><path d="M310 335 L500 240 L690 335 Z" {H2}/>
<path d="M330 330 L330 530 L430 530 L430 330 Z" {H}/>
<path d="M470 400 L470 530 L540 530 L540 400 Z"/><rect x="580" y="375" width="60" height="55"/><path d="M610 375 L610 430 M580 402 L640 402"/>
<path d="M330 380 L670 380" stroke-width="3"/>
<circle cx="400" cy="560" r="36"/><circle cx="600" cy="560" r="36"/><circle cx="400" cy="560" r="6"/><circle cx="600" cy="560" r="6"/>{spokes}
<path d="M670 500 L760 540 M670 520 L760 560 M690 510 L690 535 M720 523 L720 548 M750 536 L750 560" stroke-width="3"/>
<path d="M200 596 Q300 585 420 598 T640 598 T800 592"/><path d="M200 596 L800 592 L800 660 L200 660Z" {H}/>
<circle cx="250" cy="250" r="34"/><path d="M250 190 L250 170 M250 310 L250 330 M190 250 L170 250 M310 250 L330 250 M208 208 L194 194 M292 292 L306 306 M292 208 L306 194 M208 292 L194 306"/>
{gulls(600,200)}{gulls(690,240,.8)}{cloud(440,185,.8)}{waves(560,610,100,1)}'''
def kurhaus():
    cols=''.join(f'<path d="M{x} 400 L{x} 580 M{x+14} 400 L{x+14} 580"/>' for x in range(330,670,52))
    return f'''
<path d="M230 600 L230 420 L770 420 L770 600"/><path d="M230 420 L230 600 L330 600 L330 420Z" {H}/>
<path d="M300 400 L500 330 L700 400 Z"/><path d="M300 400 L500 330 L700 400 Z" {H2}/><circle cx="500" cy="378" r="14"/>
<path d="M300 400 L700 400 M300 408 L700 408"/>{cols}
<path d="M300 580 L700 580 M290 600 L710 600 M280 618 L720 618" />
<path d="M455 600 L455 520 Q500 480 545 520 L545 600"/><path d="M500 495 L500 600"/>
<path d="M440 330 L440 270 L560 270 L560 330"/><path d="M430 270 L500 205 L570 270 Z"/><path d="M430 270 L500 205 L570 270 Z" {H2}/>
<path d="M500 205 L500 165 M500 170 L545 180 L500 192"/>
<rect x="250" y="450" width="24" height="34"/><rect x="725" y="450" width="24" height="34"/>
<path d="M200 640 L800 640"/><path d="M260 662 L740 662" stroke-width="3"/>
{cloud(215,215,1)}{cloud(640,200,.9)}{gulls(330,250)}{gulls(740,290,.8)}'''
def standesamt():
    return f'''
<path d="M300 600 L300 380 L700 380 L700 600"/><path d="M280 380 L500 280 L720 380 Z"/><path d="M280 380 L500 280 L720 380 Z" {H2}/>
<path d="M300 380 L300 600 L380 600 L380 380Z" {H}/>
<path d="M440 600 L440 480 Q500 430 560 480 L560 600"/><path d="M500 445 L500 600 M440 520 L560 520"/>
<rect x="330" y="440" width="50" height="70"/><rect x="620" y="440" width="50" height="70"/><path d="M355 440 L355 510 M330 475 L380 475 M645 440 L645 510 M620 475 L670 475"/>
<circle cx="500" cy="335" r="22"/><path d="M500 335 L500 320 M500 335 L512 340" stroke-width="3"/>
<path d="M500 280 L500 245 M500 250 L535 258 L500 268"/>
<circle cx="470" cy="190" r="26"/><circle cx="515" cy="190" r="26"/>
<path d="M280 600 L720 600 M260 620 L740 620 M240 640 L760 640"/>
{grass(230,600,3,34)}{grass(750,600,3,34)}
{cloud(215,215,1)}{cloud(610,205,.8)}{gulls(700,250)}{gulls(290,250,.8)}'''
MOTIVE.update({'schloss':schloss,'badekarren':badekarren,'kurhaus':kurhaus,'standesamt':standesamt})

def kaparkona():
    return f'''
<path d="M200 560 L200 640 L800 640 L800 560"/>
<path d="M230 600 L420 560 L520 560 L520 600"/>
<path d="M200 600 Q300 560 420 556 L760 556 L800 600 L800 665 L200 665 Z"/><path d="M200 600 Q300 560 420 556 L760 556 L800 600 L800 665 L200 665 Z" {H}/>
<path d="M300 556 L300 360 L420 360 L420 556"/><path d="M285 360 L435 360 L420 340 L300 340 Z"/><path d="M300 340 L300 322 M420 340 L420 322 M360 340 L360 322" stroke-width="3"/>
<rect x="335" y="420" width="50" height="60"/><path d="M360 420 L360 480" stroke-width="3"/><path d="M335 556 L335 520 Q360 500 385 520 L385 556"/>
<path d="M300 360 L300 556 L350 556 L350 360Z" {H2}/>
<path d="M590 556 L610 280 L670 280 L690 556 Z"/><path d="M600 340 L680 340 M596 420 L684 420 M592 490 L688 490" stroke-width="3"/>
<path d="M590 556 L610 280 L640 280 L640 556 Z" {H2}/>
<rect x="612" y="236" width="56" height="44"/><path d="M640 236 L640 280 M612 258 L668 258" stroke-width="3"/><path d="M606 236 L640 202 L674 236 Z"/><path d="M640 202 L640 175"/>
<path d="M600 268 L520 238 M680 268 L760 238" stroke-width="3"/>
{waves(560,590,100,1)}{cloud(250,215,1)}{gulls(470,200)}{gulls(760,310,.8)}{grass(230,560,3,30)}'''
def goehren():
    bal=''.join(f'<path d="M{x} {y} L{x+60} {y} M{x} {y-14} L{x+60} {y-14} M{x+10} {y} L{x+10} {y-14} M{x+30} {y} L{x+30} {y-14} M{x+50} {y} L{x+50} {y-14}" stroke-width="3"/>' for y in (420,500) for x in (270,360,450))
    return f'''
<path d="M250 600 L250 330 L560 330 L560 600"/><path d="M250 330 L405 280 L560 330"/><path d="M250 330 L250 600 L330 600 L330 330Z" {H}/>
{bal}<rect x="285" y="440" width="30" height="50"/><rect x="375" y="440" width="30" height="50"/><rect x="465" y="440" width="30" height="50"/><rect x="285" y="520" width="30" height="50"/><rect x="465" y="520" width="30" height="50"/>
<path d="M370 600 L370 545 Q405 520 440 545 L440 600"/>
<path d="M200 600 L800 600"/>
<path d="M610 600 L610 540 Q650 480 690 540 L690 600 M650 485 L650 600 M630 515 L670 515" stroke-width="3.5"/><path d="M610 540 Q650 480 690 540 Z" {H2}/>
<path d="M720 600 L720 560 Q745 530 770 560 L770 600 Z" {H2}/>
<path d="M200 640 Q300 625 400 640 T600 640 T800 636"/><path d="M230 662 Q330 650 430 662 T640 662" stroke-width="3"/>
<circle cx="700" cy="250" r="34"/><path d="M700 190 L700 170 M640 250 L620 250 M760 250 L780 250 M658 208 L644 194 M742 208 L756 194"/>
{cloud(230,215,1)}{gulls(600,350)}{gulls(740,380,.8)}'''
def sellin():
    posts=''.join(f'<path d="M{x} 520 L{x} 600"/>' for x in range(230,560,40))
    return f'''
<path d="M200 520 L560 520 M200 540 L560 540 M200 490 L560 490 M240 490 L240 520 M280 490 L280 520 M320 490 L320 520 M360 490 L360 520 M400 490 L400 520 M440 490 L440 520 M500 490 L500 520" stroke-width="3.5"/>
{posts}<path d="M520 540 L520 600 M560 540 L560 600"/>
<path d="M560 520 L560 380 L760 380 L760 520 Z"/><path d="M540 380 L660 305 L780 380 Z"/><path d="M540 380 L660 305 L780 380 Z" {H2}/>
<path d="M630 305 L630 270 L690 270 L690 305"/><path d="M620 270 L660 235 L700 270 Z"/><path d="M660 235 L660 210"/>
<rect x="590" y="410" width="36" height="46"/><rect x="694" y="410" width="36" height="46"/><path d="M640 520 L640 440 Q660 420 680 440 L680 520"/>
<path d="M560 380 L560 520 L610 520 L610 380Z" {H}/>
<path d="M560 520 L760 520"/>
<path d="M200 600 Q330 585 460 600 T800 600"/><path d="M200 625 Q330 610 460 625 T800 625" stroke-width="3"/><path d="M220 650 Q350 638 480 650 T780 650" stroke-width="3"/>
<circle cx="300" cy="260" r="34"/><path d="M300 200 L300 180 M240 260 L220 260 M360 260 L380 260 M258 218 L244 204 M342 218 L356 204"/>
{cloud(420,235,.9)}{gulls(480,330)}{gulls(260,360,.8)}'''
def hansehafen():
    sails=''.join(f'<path d="M{x-34} {y} L{x+34} {y} L{x+30} {y+62} L{x-30} {y+62} Z"/>' for x in (440,540,640) for y in (300,380))
    return f'''
<path d="M300 560 L340 620 L740 620 L780 560 Z"/><path d="M300 560 L340 620 L740 620 L780 560 Z" {H}/>
<path d="M300 560 L780 560 M330 590 L750 590" stroke-width="3"/>
<path d="M440 560 L440 250 M540 560 L540 230 M640 560 L640 260"/>{sails}
<path d="M440 250 L440 235 M540 230 L540 212 M640 260 L640 245" stroke-width="3"/>
<path d="M250 440 L250 560 M300 440 L300 560 M250 440 L275 405 L300 440 Z"/>
<path d="M200 640 L800 640"/><path d="M200 660 Q330 648 460 660 T800 660" stroke-width="3"/>
<path d="M200 560 L300 560" /><path d="M770 560 L860 530" stroke-width="3"/>
{cloud(215,215,1)}{gulls(700,200)}{gulls(330,300,.8)}{waves(220,610,60,1)}'''
def granitz():
    return f'''
<path d="M300 600 L300 400 L700 400 L700 600"/><path d="M300 400 L300 600 L400 600 L400 400Z" {H}/>
<path d="M280 400 L280 330 L330 330 L330 400 M670 400 L670 330 L720 330 L720 400"/><path d="M270 330 L305 285 L340 330 Z"/><path d="M660 330 L695 285 L730 330 Z"/>
<path d="M280 600 L280 500 L330 500 L330 600 M670 600 L670 500 L720 500 L720 600"/>
<path d="M440 400 L440 230 L560 230 L560 400"/><path d="M425 230 L575 230"/><path d="M435 230 L435 210 L565 210 L565 230 M460 210 L500 165 L540 210 Z"/><path d="M500 165 L500 135"/>
<path d="M440 230 L440 400 L480 400 L480 230Z" {H2}/><path d="M440 280 L560 270 M440 330 L560 320 M440 380 L560 370" stroke-width="3"/>
<rect x="345" y="440" width="25" height="40"/><rect x="630" y="440" width="25" height="40"/><path d="M470 600 L470 520 Q500 490 530 520 L530 600"/>
<path d="M200 600 L800 600"/>
<path d="M200 660 Q250 600 300 600 M800 660 Q750 600 700 600" stroke-width="3"/>
<path d="M240 560 q-30 -50 0 -100 q40 20 20 100 M780 560 q30 -50 0 -100 q-40 20 -20 100"/>
{cloud(215,190,.9)}{cloud(640,170,.8)}{gulls(380,260)}{gulls(640,260,.8)}'''
def putbus():
    return f'''
<path d="M500 590 L500 250"/><path d="M485 590 L515 590 L508 250 L492 250 Z" {H2}/><path d="M492 250 L500 215 L508 250 Z"/><path d="M470 590 L530 590 L530 605 L470 605 Z"/>
<path d="M240 600 L240 400 L400 400 L400 600 M600 600 L600 400 L760 400 L760 600"/>
<path d="M240 400 L320 360 L400 400 M600 400 L680 360 L760 400"/>
<path d="M240 400 L240 600 L290 600 L290 400Z" {H}/><path d="M710 400 L710 600 L760 600 L760 400Z" {H}/>
<path d="M265 440 L265 500 M320 440 L320 500 M375 440 L375 500 M625 440 L625 500 M680 440 L680 500 M735 440 L735 500" stroke-width="5"/>
<path d="M265 530 L265 600 M320 530 L320 600 M375 530 L375 600 M625 530 L625 600 M680 530 L680 600 M735 530 L735 600" stroke-width="3"/>
<path d="M200 605 L800 605"/><path d="M280 640 Q500 620 720 640" stroke-width="3"/>
<path d="M420 600 q-20 -60 0 -110 q40 10 30 110 M580 600 q20 -60 0 -110 q-40 10 -30 110"/>
{cloud(215,215,1)}{cloud(650,200,.9)}{gulls(420,300)}{gulls(600,320,.8)}'''
def ranzow():
    return f'''
<path d="M280 600 L280 400 L720 400 L720 600"/><path d="M270 400 L400 330 L600 330 L730 400"/><path d="M270 400 L400 330 L600 330 L730 400" {H2}/>
<path d="M280 400 L280 600 L360 600 L360 400Z" {H}/>
<path d="M440 400 L440 300 L560 300 L560 400"/><path d="M430 300 L500 235 L570 300 Z"/><circle cx="500" cy="340" r="16"/><path d="M500 340 L500 328 M500 340 L510 345" stroke-width="3"/>
<rect x="310" y="440" width="26" height="40"/><rect x="390" y="440" width="26" height="40"/><rect x="584" y="440" width="26" height="40"/><rect x="664" y="440" width="26" height="40"/>
<path d="M470 600 L470 520 Q500 490 530 520 L530 600"/><path d="M200 600 L800 600"/>
<path d="M200 660 Q330 625 500 640 T800 660" stroke-width="3"/>
<path d="M210 600 L210 470 M210 470 q-60 -30 -30 -80 q40 -30 65 10 q35 -45 70 10 q10 55 -45 60" /><path d="M790 600 L790 480 M790 480 q50 -20 30 -70 q-40 -25 -65 10"/>
{cloud(400,210,.8)}{gulls(620,230)}{gulls(330,260,.8)}'''
def koenigsstuhl():
    return f'''
<path d="M200 330 Q260 320 320 340 L360 330 Q420 280 480 330 L520 350 Q560 340 600 380 L640 430 L660 560 L640 665 L200 665 Z"/>
<path d="M200 330 Q260 320 320 340 L360 330 Q420 280 480 330 L520 350 Q560 340 600 380 L640 430 L660 560 L640 665 L200 665 Z" {H}/>
<path d="M330 345 L350 600 M420 330 L440 640 M520 350 L540 580 M590 385 L600 520" stroke-width="3"/>
<path d="M240 330 L240 270 M240 270 q-30 -20 -10 -50 q30 -20 45 10 q25 -15 35 20 q-10 40 -50 20 M450 320 L450 260 M450 260 q-30 -15 -10 -45 q35 -20 55 10 q25 5 10 35 q-30 20 -55 0"/>
<path d="M660 520 Q720 530 800 520 M660 600 Q720 615 800 600 M650 640 Q720 655 800 645" stroke-width="3"/>
<path d="M690 560 L690 470 L740 560 Z"/><path d="M670 560 L760 560 L745 580 L685 580 Z"/>
<circle cx="720" cy="230" r="34"/><path d="M720 170 L720 150 M660 230 L640 230 M780 230 L800 230 M678 188 L664 174 M762 188 L776 174"/>
{cloud(560,200,.9)}{gulls(560,280)}{gulls(700,330,.8)}'''
def hiddensee():
    return f'''
<path d="M300 600 L300 460 L500 460 L500 600"/><path d="M280 470 L400 370 L520 470 Z"/><path d="M280 470 L400 370 L520 470 Z" {H2}/>
<path d="M300 480 L500 480 M290 495 L510 495" stroke-width="3"/>
<rect x="330" y="510" width="40" height="40"/><path d="M350 510 L350 550 M330 530 L370 530" stroke-width="3"/><path d="M420 600 L420 535 L470 535 L470 600"/>
<path d="M300 460 L300 600 L350 600 L350 460Z" {H}/>
<path d="M200 600 Q300 580 400 600 T800 600"/><path d="M200 600 L800 600 L800 665 L200 665Z" {H}/>
<path d="M600 600 L600 470 M600 470 q-70 -10 -90 -50 M600 480 q-60 10 -80 40 M600 460 q50 -30 100 -10 M600 500 q40 -20 80 10" />
{grass(220,605,4,40)}{grass(730,605,4,40)}
<path d="M650 560 L710 560 L690 590 L670 590 Z" stroke-width="3"/>
{cloud(240,215,1)}{gulls(560,260)}{gulls(700,300,.8)}{waves(560,625,100,1)}'''
def prora():
    arch=''.join(f'<path d="M{x} 450 L{x} 430 Q{x+12} 415 {x+24} 430 L{x+24} 450 M{x} 520 L{x} 500 Q{x+12} 485 {x+24} 500 L{x+24} 520" stroke-width="3"/>' for x in range(250,720,48))
    return f'''
<path d="M220 600 L220 400 L780 400 L780 600"/><path d="M220 400 L220 600 L300 600 L300 400Z" {H}/>
<path d="M220 400 L780 400 M220 560 L780 560 M220 475 L780 475" stroke-width="3"/>
{arch}
<path d="M200 600 L800 600"/><path d="M200 625 Q330 610 500 625 T800 625"/>
<path d="M200 660 Q330 645 500 660 T800 660" stroke-width="3"/>
<circle cx="680" cy="250" r="34"/><path d="M680 190 L680 170 M620 250 L600 250 M740 250 L760 250 M638 208 L624 194 M722 208 L736 194"/>
{cloud(240,230,1)}{gulls(440,270)}{gulls(540,320,.8)}{grass(235,602,3,26)}'''
MOTIVE.update({'kaparkona':kaparkona,'goehren':goehren,'sellin':sellin,'hansehafen':hansehafen,'granitz':granitz,'putbus':putbus,'ranzow':ranzow,'koenigsstuhl':koenigsstuhl,'hiddensee':hiddensee,'prora':prora})

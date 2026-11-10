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

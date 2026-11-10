"""Zusatzmotive: Schloss Ralswiek (Park, See, Portal) und Kurhaus Binz (Promenade, Portikus, Strand)."""
from pencil import H,H2,gulls,cloud,grass,waves,MOTIVE
import pencil_orte
def tree(x,y,s=1):
    return f'<path d="M{x} {y} L{x} {y-90*s}"/><path d="M{x} {y-80*s} q{-70*s} {-10*s} {-60*s} {-70*s} q{10*s} {-60*s} {70*s} {-50*s} q{70*s} {-30*s} {90*s} {30*s} q{20*s} {60*s} {-100*s} {90*s}"/><path d="M{x-40*s} {y-120*s} q{20*s} {20*s} {40*s} 0 M{x+10*s} {y-150*s} q{20*s} {20*s} {40*s} 0" stroke-width="3"/>'
def lamp(x,y):
    return f'<path d="M{x} {y} L{x} {y-130}"/><path d="M{x-14} {y-130} L{x+14} {y-130} L{x+10} {y-160} L{x-10} {y-160} Z"/><path d="M{x-8} {y} L{x+8} {y}"/>'
def ralswiek_park():
    return f'''
<path d="M380 470 L380 380 L620 380 L620 470"/><path d="M380 380 L380 470 L430 470 L430 380Z" {H}/>
<path d="M450 380 L450 340 L550 340 L550 380"/><path d="M440 340 L500 295 L560 340 Z" {H2}/>
<path d="M360 380 L360 335 L395 335 L395 380 M605 380 L605 335 L640 335 L640 380"/><path d="M352 335 L378 300 L404 335 Z"/><path d="M596 335 L622 300 L648 335 Z"/>
<rect x="405" y="410" width="12" height="18"/><rect x="583" y="410" width="12" height="18"/><rect x="470" y="425" width="60" height="45"/>
<path d="M360 470 L640 470"/>
<path d="M470 470 L330 660 M530 470 L670 660"/><path d="M500 470 L500 660" stroke-width="3" stroke-dasharray="2 14"/>
<path d="M330 660 L670 660"/>{tree(250,640,1.1)}{tree(760,630,1.2)}{tree(330,500,.5)}{tree(690,500,.5)}
{grass(210,660,4,30)}{grass(790,660,4,30)}
{cloud(215,215,1)}{cloud(610,190,.9)}{gulls(450,230)}{gulls(700,260,.8)}'''
def ralswiek_see():
    return f'''
<path d="M300 480 L300 380 L640 380 L640 480"/><path d="M300 380 L300 480 L370 480 L370 380Z" {H}/>
<path d="M290 380 L470 320 L650 380 Z"/><path d="M290 380 L470 320 L650 380 Z" {H2}/>
<path d="M410 380 L410 330 L530 330 L530 380"/><path d="M400 330 L470 280 L540 330 Z"/>
<path d="M330 410 L330 440 M400 410 L400 440 M470 410 L470 440 M540 410 L540 440 M600 410 L600 440" stroke-width="5"/>
<path d="M200 485 L800 485"/><path d="M200 485 L800 485 L800 665 L200 665Z" {H}/>
<path d="M300 500 L300 520 M300 520 L330 540 M340 500 L340 560 M470 500 L470 540 M600 500 L600 520" stroke-width="3" stroke-opacity=".5"/>
<path d="M560 590 L700 590 L680 620 L580 620 Z"/><path d="M630 590 L630 480 L700 570 Z"/><path d="M630 590 L630 505 L590 580 Z" {H2}/>
<path d="M240 665 L240 600 M260 665 L255 590 M280 665 L285 610 M690 665 L690 620 M710 665 L715 630" stroke-width="3"/>
{waves(250,630,100,1)}{cloud(215,215,1)}{cloud(610,190,.9)}{gulls(420,230)}{gulls(700,270,.8)}'''
def ralswiek_portal():
    return f'''
<path d="M280 640 L280 330 L720 330 L720 640"/><path d="M280 330 L280 640 L340 640 L340 330Z" {H}/>
<path d="M260 330 L500 230 L740 330 Z"/><path d="M260 330 L500 230 L740 330 Z" {H2}/><circle cx="500" cy="290" r="20"/>
<path d="M410 640 L410 440 Q500 380 590 440 L590 640"/><path d="M500 410 L500 640 M410 520 L590 520 M420 560 L580 560" stroke-width="3"/><path d="M445 440 Q500 415 555 440" stroke-width="3"/>
<path d="M370 640 L370 460 M630 640 L630 460"/><path d="M360 460 L380 460 M620 460 L640 460"/>
<path d="M340 660 L660 660 M320 680 L680 680" /><path d="M360 640 L640 640"/>
<path d="M300 560 L300 640 M300 560 q-25 -20 0 -45 q25 20 0 45 M700 560 L700 640 M700 560 q-25 -20 0 -45 q25 20 0 45" />
<rect x="330" y="400" width="26" height="46"/><rect x="644" y="400" width="26" height="46"/>
<path d="M380 400 L380 380 M620 400 L620 380 M372 380 L388 380 M612 380 L628 380" stroke-width="3"/>
{cloud(215,215,1)}{gulls(700,220)}{gulls(330,260,.8)}'''
def kurhaus_promenade():
    return f'''
<path d="M200 470 L200 400 L560 400 L560 470"/><path d="M200 400 L200 470 L260 470 L260 400Z" {H}/>
<path d="M190 400 L380 340 L570 400 Z" {H2}/><path d="M190 400 L380 340 L570 400 Z"/><path d="M340 340 L340 290 L420 290 L420 340"/><path d="M332 290 L380 245 L428 290 Z"/>
<path d="M240 420 L240 470 M300 420 L300 470 M360 420 L360 470 M420 420 L420 470 M480 420 L480 470" stroke-width="5"/>
<path d="M200 470 L800 470"/><path d="M200 480 L800 480" stroke-width="3"/>
<path d="M200 665 L800 665 M200 540 L800 540"/><path d="M200 540 L800 540 L800 665 L200 665Z" {H}/>
{lamp(300,540)}{lamp(520,540)}{lamp(720,540)}
<path d="M600 540 L680 540 M610 540 L610 575 M670 540 L670 575 M600 515 L680 515 L680 540 L600 540" stroke-width="3"/>
<path d="M200 600 L800 600" stroke-width="3" stroke-dasharray="3 16"/>
<path d="M600 470 Q700 450 800 470" stroke-width="3"/><path d="M640 450 L640 420 M660 448 L660 425" stroke-width="3"/>
{cloud(215,215,1)}{cloud(610,190,.9)}{gulls(470,230)}{gulls(700,280,.8)}'''
def kurhaus_portikus():
    cols=''.join(f'<path d="M{x} 380 L{x} 600 M{x+22} 380 L{x+22} 600"/><path d="M{x-8} 380 L{x+30} 380 M{x-8} 600 L{x+30} 600"/>' for x in (300,400,500,600))
    return f'''
<path d="M240 640 L240 380 L760 380 L760 640"/><path d="M240 380 L240 640 L290 640 L290 380Z" {H}/>
<path d="M270 370 L500 270 L730 370 Z"/><path d="M270 370 L500 270 L730 370 Z" {H2}/><circle cx="500" cy="330" r="18"/>
<path d="M280 380 L720 380 M280 395 L720 395"/>{cols}
<path d="M290 600 L710 600"/><path d="M270 620 L730 620"/><path d="M250 640 L750 640"/><path d="M230 660 L770 660"/>
<path d="M470 600 L470 500 Q500 470 530 500 L530 600" stroke-width="3"/>
<path d="M500 270 L500 225 M500 230 L545 240 L500 252"/>
{cloud(215,215,1)}{cloud(630,190,.9)}{gulls(330,240)}{gulls(700,260,.8)}'''
def kurhaus_strand():
    return f'''
<path d="M300 470 L300 400 L700 400 L700 470"/><path d="M300 400 L300 470 L370 470 L370 400Z" {H}/>
<path d="M290 400 L500 330 L710 400 Z"/><path d="M290 400 L500 330 L710 400 Z" {H2}/><path d="M460 330 L460 285 L540 285 L540 330"/><path d="M450 285 L500 245 L550 285 Z"/>
<path d="M340 420 L340 470 M400 420 L400 470 M460 420 L460 470 M520 420 L520 470 M580 420 L580 470 M640 420 L640 470" stroke-width="5"/>
<path d="M200 470 L800 470"/><path d="M200 470 Q400 490 800 470 L800 560 Q500 580 200 560Z" {H}/>
<path d="M260 650 L260 590 Q260 560 310 560 Q360 560 360 590 L360 650 Z"/><path d="M260 600 L360 600 M310 560 L310 650" stroke-width="3"/><path d="M250 650 L370 650"/>
<path d="M620 650 L620 590 Q620 560 670 560 Q720 560 720 590 L720 650 Z"/><path d="M620 600 L720 600 M670 560 L670 650" stroke-width="3"/><path d="M610 650 L730 650"/>
<path d="M200 665 Q330 650 500 665 T800 665" stroke-width="3"/>{grass(440,665,4,40)}
{cloud(215,215,1)}{cloud(630,190,.9)}{gulls(470,230)}{gulls(700,270,.8)}{waves(480,620,60,1)}'''
MOTIVE.update({'ralswiek_park':ralswiek_park,'ralswiek_see':ralswiek_see,'ralswiek_portal':ralswiek_portal,'kurhaus_promenade':kurhaus_promenade,'kurhaus_portikus':kurhaus_portikus,'kurhaus_strand':kurhaus_strand})

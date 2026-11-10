#!/usr/bin/env python3
"""Rendert die Bleistift-Motive (tools/pencil.py) als transparente Icons nach assets/img/<motiv>.webp (für Kacheln auf der Seite)."""
import sys,subprocess,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from pencil import MOTIVE
import pencil_orte
from make_pin import DEFS
R=pathlib.Path(__file__).resolve().parent.parent
ink='fill="none" stroke="#3b2a2a" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"'
def icon(name):
    m=MOTIVE[name]().replace('#faf7f4','#fbf5f0').replace('#e9dfd6','#f1e4dc')
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="480" height="416" viewBox="200 140 600 520">{DEFS}
<g id="m" {ink}>{m}</g><use xlink:href="#m" filter="url(#pen1)"/><use xlink:href="#m" filter="url(#pen2)" opacity="0.55"/></svg>'''
    png=R/'assets'/'img'/f'{name}.png'; out=png.with_suffix('.webp'); subprocess.run(['rsvg-convert','-o',str(png)],input=svg.encode(),check=True)
    subprocess.run(['convert',str(png),'-resize','380x','-quality','82','-define','webp:alpha-quality=90',str(out)],check=True); png.unlink(); return out
if __name__=='__main__':
    for n in (sys.argv[1:] or MOTIVE): print(icon(n))

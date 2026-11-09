#!/usr/bin/env python3
"""Titelbilder (16:9, Bleistift-Zeichnung auf Papierfarbe) für Blogartikel: python3 tools/make_blog_img.py <ausgabeordner> <motiv:dateiname> ..."""
import sys,subprocess,pathlib,tempfile
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from pencil import MOTIVE
from make_pin import DEFS
ink='fill="none" stroke="#3b2a2a" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"'
def render(motif,out):
    m=MOTIVE[motif]().replace('#faf7f4','#fbf5f0').replace('#e9dfd6','#f1e4dc')
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1600" height="900" viewBox="-100 100 1200 675">{DEFS}
<rect x="-100" y="100" width="1200" height="675" fill="#f6e9e3"/><rect x="-70" y="130" width="1140" height="615" fill="none" stroke="#e3cfc6" stroke-width="2"/>
<g id="m" {ink}>{m}</g><use xlink:href="#m" filter="url(#pen1)"/><use xlink:href="#m" filter="url(#pen2)" opacity="0.55"/></svg>'''
    with tempfile.TemporaryDirectory() as d:
        png=pathlib.Path(d)/'a.png'; subprocess.run(['rsvg-convert','-o',str(png)],input=svg.encode(),check=True)
        subprocess.run(['convert',str(png),'-quality','80',str(out)],check=True)
if __name__=='__main__':
    o=pathlib.Path(sys.argv[1]); o.mkdir(parents=True,exist_ok=True)
    for a in sys.argv[2:]:
        mo,fn=a.split(':'); render(mo,o/(fn+'.webp')); print(fn)

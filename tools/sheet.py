#!/usr/bin/env python3
"""Kontaktbogen: rendert Motive (Namen als Argumente) in eine Bilddatei /tmp/sheet.png zur Sichtprüfung."""
import sys,subprocess,pathlib
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parent))
from pencil import MOTIVE
from make_pin import DEFS
names=sys.argv[1:]; ink='fill="none" stroke="#3b2a2a" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"'
fs=[]
for n in names:
    svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="600" height="520" viewBox="200 140 600 520">{DEFS}<rect x="200" y="140" width="600" height="520" fill="#fbf5f0"/>
<g id="m" {ink}>{MOTIVE[n]()}</g><use xlink:href="#m" filter="url(#pen1)"/><use xlink:href="#m" filter="url(#pen2)" opacity="0.55"/></svg>'''
    f=f'/tmp/sh_{n}.png'; subprocess.run(['rsvg-convert','-w','500','-o',f],input=svg.encode(),check=True); fs.append(f)
subprocess.run(['montage',*fs,'-tile','3x','-geometry','500x433+6+6','-label','%f','/tmp/sheet.png'],check=True); print('/tmp/sheet.png')

#!/usr/bin/env python3
"""JS para buscar candidatos de fotos en Commons (API con origin=*) desde el navegador.

Uso: python3 commons_js.py <slug>            → JS de búsqueda (lee <slug>/commons_queries.json: {n: [q1, q2]})
     python3 commons_js.py <slug> verify     → JS de verificación (lee <slug>/photo_sel.json)
Salida del JS de búsqueda: {n: [{q,t,a,l,w,h,d}]}  (t=título File:, a=autor, l=licencia, d=descripción corta)
"""
import json
import os
import sys
from pathlib import Path

SCRATCH = Path(os.environ.get("A27_SCRATCH", Path(__file__).resolve().parent.parent))
SEARCH = ("const Q=%s;const clean=s=>(s||'').replace(/<[^>]+>/g,'').replace(/\\s+/g,' ').trim();const out={};"
          "for(const [n,qs] of Object.entries(Q)){out[n]=[];const seen=new Set();for(const q of qs){"
          "const u='https://commons.wikimedia.org/w/api.php?action=query&format=json&origin=*&generator=search&gsrsearch='+encodeURIComponent(q+' filetype:bitmap')+'&gsrnamespace=6&gsrlimit=%d&prop=imageinfo&iiprop=url|extmetadata|size';"
          "try{const j=await (await fetch(u)).json();const pages=Object.values((j.query||{}).pages||{}).sort((a,b)=>a.index-b.index);"
          "for(const p of pages){if(seen.has(p.title))continue;seen.add(p.title);const ii=(p.imageinfo||[{}])[0];const m=ii.extmetadata||{};"
          "if(!/\\.(jpe?g|webp)$/i.test(p.title))continue;if((ii.width||0)<900)continue;"
          "out[n].push({q,t:p.title.replace(/^File:/,''),a:clean((m.Artist||{}).value).slice(0,40),l:clean((m.LicenseShortName||{}).value),w:ii.width,h:ii.height,d:clean((m.ImageDescription||{}).value).slice(0,70)})}}"
          "catch(e){out[n].push({q,err:String(e)})}}}JSON.stringify(out)")
VERIFY = ("const T=%s;const clean=s=>(s||'').replace(/<[^>]+>/g,'').replace(/\\s+/g,' ').trim();const out=[];"
          "for(let i=0;i<T.length;i+=20){const u='https://commons.wikimedia.org/w/api.php?action=query&format=json&origin=*&prop=imageinfo&iiprop=url|extmetadata|size&titles='+encodeURIComponent(T.slice(i,i+20).join('|'));"
          "const j=await (await fetch(u)).json();for(const p of Object.values(j.query.pages)){const ii=(p.imageinfo||[{}])[0];const m=ii.extmetadata||{};"
          "out.push({t:p.title,missing:'missing' in p,a:clean((m.Artist||{}).value).slice(0,50),l:clean((m.LicenseShortName||{}).value),w:ii.width,h:ii.height})}}JSON.stringify(out)")


def main(slug, mode):
    d = SCRATCH / slug
    if mode == "verify":
        sel = json.loads((d / "photo_sel.json").read_text())
        titles = ["File:" + f for v in sel.values() for f, _ in v]
        print(VERIFY % json.dumps(titles, ensure_ascii=False))
    else:
        q = json.loads((d / "commons_queries.json").read_text())
        limit = int(mode) if mode.isdigit() else 6
        print(SEARCH % (json.dumps(q, ensure_ascii=False), limit))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "6")

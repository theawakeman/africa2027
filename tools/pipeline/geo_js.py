#!/usr/bin/env python3
"""Genera el JavaScript que consulta Google Maps (endpoint /search?tbm=map) para todos los
puntos de un país desde una pestaña de google.com, con consultas de reserva por punto.

Uso: python3 geo_js.py <slug> [pais_en]  → imprime el JS (pegar en javascript_tool)
Resultado del JS: {clave: {q: consulta que funcionó, res: [{name, lat, lon, addr, cat}...]}}
"""
import json
import os
import re
import sys
from pathlib import Path

SCRATCH = Path(os.environ.get("A27_SCRATCH", Path(__file__).resolve().parent.parent))
STRIP = re.compile(r"\b(entrance|entrée|entree|bureau d'accueil|bureau|office|parking|gate|main gate|headquarters|"
                   r"reception|taquilla|puerta|acceso|border crossing|border post|poste frontière|frontière|border)\b",
                   re.I)


def variants(key, q, name, country):
    v = [q]
    s = STRIP.sub("", q).replace("  ", " ").strip(" ,")
    if s and s != q:
        v.append(s)
    base = name.split("·")[0].split("(")[0].strip()
    if base and base not in v:
        v.append(base + ", " + country)
    return v


def main(slug, country):
    d = SCRATCH / slug
    pdis = json.loads((d / "pdis.json").read_text())
    op = json.loads((d / "operativo.json").read_text())
    items = []
    for x in pdis["pois"]:
        items.append([f"poi-{x['n']}", variants(x["n"], x["gmaps_query"], x["name"], country)])
    for i, l in enumerate(op["logistics"]):
        q = l.get("gmaps_query") or l["name"]
        items.append([f"log-{i}", variants(i, q, l["name"], country)])
    (d / "gm_queries.json").write_text(json.dumps(items, ensure_ascii=False, indent=1))
    js = ("const Q=" + json.dumps(items, ensure_ascii=False) + ";const out={};"
          "async function g(q){const r=await fetch('/search?tbm=map&hl=es&q='+encodeURIComponent(q));const t=await r.text();"
          "const j=JSON.parse(t.replace(/^\\)\\]\\}'\\n?/,''));return (j[0][1]||[]).slice(0,3).map(w=>{const p=w[14];"
          "if(!Array.isArray(p)||p.length<12)return null;const pt=p[9];return pt&&pt.length>3?{name:p[11],lat:pt[2],lon:pt[3],"
          "addr:p.length>39?p[39]:null,cat:(p[13]||[])[0]}:null}).filter(Boolean)}"
          "for(const [k,qs] of Q){out[k]={q:null,res:[]};for(const q of qs){try{const res=await g(q);if(res.length){out[k]={q,res};break}}"
          "catch(e){out[k].err=String(e)}}}JSON.stringify(out)")
    print(js)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2] if len(sys.argv) > 2 else "")

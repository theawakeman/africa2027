#!/usr/bin/env python3
"""Prepara las consultas de Google Maps de un país (PDIs + logística).

Uso: python3 geo_batches.py <slug> [n_lote]  → imprime el lote n (JSON de acciones para browser_batch)
     python3 geo_batches.py <slug> list      → lista todas las consultas con su clave
Guarda scratchpad/<slug>/gm_queries.json con [clave, consulta].
"""
import json
import os
import sys
import urllib.parse
from pathlib import Path

SCRATCH = Path(os.environ.get("A27_SCRATCH", Path(__file__).resolve().parent.parent))
JS = ("(async()=>{const P=/!3d(-?\\d+\\.\\d+)!4d(-?\\d+\\.\\d+)/;for(let i=0;i<16;i++){const h=location.href;"
      "const m=h.match(P);if(h.includes('/maps/place/')&&m)return {mode:'place',title:document.title,lat:m[1],lon:m[2]};"
      "const as=[...document.querySelectorAll('a[href*=\"/maps/place/\"]')];if(as.length)return {mode:'list',title:document.title,"
      "res:as.slice(0,6).map(a=>{const m=a.href.match(P);return {name:a.getAttribute('aria-label'),lat:m&&m[1],lon:m&&m[2]}})};"
      "await new Promise(r=>setTimeout(r,500))}return {mode:'none',title:document.title,url:location.href}})()")
PER_BATCH = 8


def queries(slug):
    d = SCRATCH / slug
    pdis = json.loads((d / "pdis.json").read_text())
    op = json.loads((d / "operativo.json").read_text())
    qs = [(f"poi-{x['n']}", x["gmaps_query"]) for x in pdis["pois"]]
    for i, l in enumerate(op["logistics"]):
        qs.append((f"log-{i}", l.get("gmaps_query") or l["name"]))
    (d / "gm_queries.json").write_text(json.dumps(qs, ensure_ascii=False, indent=1))
    return qs


def actions(qs):
    out = []
    for _k, q in qs:
        url = "https://www.google.com/maps/search/" + urllib.parse.quote_plus(q) + "?hl=es"
        out += [{"name": "navigate", "input": {"url": url}},
                {"name": "computer", "input": {"action": "wait", "duration": 2}},
                {"name": "javascript_tool", "input": {"action": "javascript_exec", "text": JS}}]
    return out


if __name__ == "__main__":
    slug = sys.argv[1]
    qs = queries(slug)
    arg = sys.argv[2] if len(sys.argv) > 2 else "list"
    if arg == "list":
        for i, (k, q) in enumerate(qs):
            print(i, k, q)
        print("lotes:", (len(qs) + PER_BATCH - 1) // PER_BATCH)
    else:
        n = int(arg)
        print(json.dumps(actions(qs[n * PER_BATCH:(n + 1) * PER_BATCH]), ensure_ascii=False))

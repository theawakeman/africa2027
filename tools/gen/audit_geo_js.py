# -*- coding: utf-8 -*-
"""Genera el JavaScript que consulta Photon (OSM) y Wikidata para un país.

Se ejecuta en el navegador (pestaña abierta en photon.komoot.io) y devuelve,
por cada punto de la app, los candidatos más cercanos de las dos fuentes con
su distancia en km al punto actual. El resultado se guarda en
audit/geo/<slug>_ref.json y lo evalúa audit_geo_eval.py.

Uso:  python3 audit_geo_js.py <slug> [inicio] [fin]   (imprime el JS)
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]

JS = r"""
const ITEMS = %(items)s;
const BBOX = %(bbox)s;
const WD_LANGS = ["es","fr","en","pt"];
function km(a,b,c,d){const r=Math.PI/180;const x=(c-a)*r,y=(d-b)*r;const h=Math.sin(x/2)**2+Math.cos(a*r)*Math.cos(c*r)*Math.sin(y/2)**2;return 6371*2*Math.asin(Math.sqrt(h));}
function inBox(lat,lon){return !BBOX||(lon>=BBOX[0]&&lat>=BBOX[1]&&lon<=BBOX[2]&&lat<=BBOX[3]);}
const sleep=ms=>new Promise(r=>setTimeout(r,ms));
async function photon(q,lat,lon){
  const u=`https://photon.komoot.io/api/?q=${encodeURIComponent(q)}&limit=6&lat=${lat}&lon=${lon}`+(BBOX?`&bbox=${BBOX.join(',')}`:'');
  try{const j=await (await fetch(u)).json();
    return (j.features||[]).map(f=>({n:f.properties.name||'',k:f.properties.osm_key,v:f.properties.osm_value,lat:+f.geometry.coordinates[1].toFixed(5),lon:+f.geometry.coordinates[0].toFixed(5)}))
      .filter(f=>inBox(f.lat,f.lon)).map(f=>({...f,d:+km(lat,lon,f.lat,f.lon).toFixed(1)}));}
  catch(e){return [{err:String(e)}];}
}
async function wikidata(q,lat,lon){
  let ids=[];
  for(const L of WD_LANGS){
    try{const s=await (await fetch(`https://www.wikidata.org/w/api.php?action=wbsearchentities&search=${encodeURIComponent(q)}&language=${L}&format=json&limit=4&origin=*`)).json();
      ids=ids.concat((s.search||[]).map(x=>x.id));}catch(e){}
    if(ids.length>=4) break;
  }
  ids=[...new Set(ids)].slice(0,6); if(!ids.length) return [];
  try{const e=await (await fetch(`https://www.wikidata.org/w/api.php?action=wbgetentities&ids=${ids.join('|')}&props=claims|labels|descriptions&languages=es|en|fr&format=json&origin=*`)).json();
    return Object.values(e.entities||{}).map(en=>{const c=(en.claims.P625||[]).map(x=>x.mainsnak.datavalue&&x.mainsnak.datavalue.value).filter(Boolean)[0];
      return c?{id:en.id,l:(en.labels.es||en.labels.en||en.labels.fr||{}).value,t:(en.descriptions.es||en.descriptions.en||en.descriptions.fr||{}).value,lat:+c.latitude.toFixed(5),lon:+c.longitude.toFixed(5)}:null;})
      .filter(x=>x&&inBox(x.lat,x.lon)).map(x=>({...x,d:+km(lat,lon,x.lat,x.lon).toFixed(1)}));}
  catch(e){return [{err:String(e)}];}
}
// Se ejecuta en segundo plano (la herramienta corta a los 45 s): el resultado
// se recoge después con  JSON.stringify({done:window.__geoDone,n:window.__geoOut.length,out:window.__geoOut})
window.__geoOut=[]; window.__geoDone=false; window.__geoErr=null;
(async()=>{try{
for(const it of ITEMS){
  let ph=[]; for(const q of it.q){ph=await photon(q,it.lat,it.lon); if(ph.length&&!ph[0].err) break; await sleep(60);}
  let wd=[]; for(const q of it.q.slice(0,2)){wd=await wikidata(q,it.lat,it.lon); if(wd.length&&!wd[0].err) break;}
  window.__geoOut.push({id:it.id,ph:ph.slice(0,3),wd:wd.slice(0,2)});
  await sleep(60);
}
}catch(e){window.__geoErr=String(e);} window.__geoDone=true;})();
"started "+ITEMS.length
"""

POLL = "JSON.stringify({done:window.__geoDone,err:window.__geoErr,n:(window.__geoOut||[]).length,out:window.__geoDone?window.__geoOut:null})"



def main(slug, ini=0, fin=None, compact=False):
    data = json.loads((ROOT / "audit" / "geo" / f"{slug}_queries.json").read_text(encoding="utf-8"))
    items = [{"id": it["id"], "q": it["q"], "lat": it["lat"], "lon": it["lon"]} for it in data["items"]][ini:fin]
    bbox = [round(x, 2) for x in data["bbox"]] if data["bbox"] else None
    if compact:
        # las funciones ya están definidas en la pestaña como window.__geoRun(ITEMS, BBOX)
        print(f"window.__geoRun({json.dumps(items, ensure_ascii=False)}, {json.dumps(bbox)})")
    else:
        print(JS % {"items": json.dumps(items, ensure_ascii=False), "bbox": json.dumps(bbox)})


if __name__ == "__main__":
    a = [x for x in sys.argv if x != "--compact"]
    main(a[1], int(a[2]) if len(a) > 2 else 0, int(a[3]) if len(a) > 3 else None, compact="--compact" in sys.argv)

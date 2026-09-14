# -*- coding: utf-8 -*-
"""Consulta Photon y Wikidata para una auditoría GPS preparada.

Es la versión reproducible por línea de comandos del flujo histórico de
``audit_geo_js.py``. Conserva el mismo esquema de salida para que
``audit_geo_eval.py`` pueda evaluar los resultados sin cambios.

Uso: python3 tools/gen/audit_geo_fetch.py <slug> [<slug> ...]
"""
import json
import math
import subprocess
import sys
import time
import urllib.parse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
GEO = ROOT / "audit" / "geo"
UA = "Africa2027-coordinate-audit/1.0 (travel research; contact via project owner)"
WD_LANGS = ("es", "fr", "en", "pt")


def km(a, b, c, d):
    r = math.pi / 180
    x, y = (c - a) * r, (d - b) * r
    h = math.sin(x / 2) ** 2 + math.cos(a * r) * math.cos(c * r) * math.sin(y / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def get_json(url, attempts=3):
    last = None
    for attempt in range(attempts):
        try:
            raw = subprocess.check_output(
                ["curl", "-sS", "-L", "--max-time", "20", "-A", UA, url],
                text=True,
                timeout=25,
            )
            return json.loads(raw)
        except Exception as exc:
            last = exc
            time.sleep(0.5 * (attempt + 1))
    raise last


def in_box(lat, lon, bbox):
    return not bbox or bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]


def photon(query, item, bbox):
    params = {"q": query, "limit": 6, "lat": item["lat"], "lon": item["lon"]}
    if bbox:
        params["bbox"] = ",".join(str(round(x, 2)) for x in bbox)
    url = "https://photon.komoot.io/api/?" + urllib.parse.urlencode(params)
    data = get_json(url)
    out = []
    for feature in data.get("features", []):
        lat = round(float(feature["geometry"]["coordinates"][1]), 5)
        lon = round(float(feature["geometry"]["coordinates"][0]), 5)
        if not in_box(lat, lon, bbox):
            continue
        props = feature.get("properties", {})
        out.append({
            "n": props.get("name", ""),
            "k": props.get("osm_key"),
            "v": props.get("osm_value"),
            "lat": lat,
            "lon": lon,
            "d": round(km(item["lat"], item["lon"], lat, lon), 1),
        })
    return out


def wikidata(query, item, bbox):
    ids = []
    for language in WD_LANGS:
        params = {
            "action": "wbsearchentities", "search": query, "language": language,
            "format": "json", "limit": 4, "origin": "*",
        }
        data = get_json("https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode(params))
        ids.extend(row["id"] for row in data.get("search", []))
        ids = list(dict.fromkeys(ids))
        if len(ids) >= 4:
            break
    ids = ids[:6]
    if not ids:
        return []
    params = {
        "action": "wbgetentities", "ids": "|".join(ids),
        "props": "claims|labels|descriptions", "languages": "es|en|fr",
        "format": "json", "origin": "*",
    }
    data = get_json("https://www.wikidata.org/w/api.php?" + urllib.parse.urlencode(params))
    out = []
    for entity in data.get("entities", {}).values():
        claims = entity.get("claims", {}).get("P625", [])
        if not claims:
            continue
        value = claims[0].get("mainsnak", {}).get("datavalue", {}).get("value")
        if not value:
            continue
        lat, lon = round(float(value["latitude"]), 5), round(float(value["longitude"]), 5)
        if not in_box(lat, lon, bbox):
            continue
        labels, descriptions = entity.get("labels", {}), entity.get("descriptions", {})
        label = next((labels.get(lang, {}).get("value") for lang in ("es", "en", "fr") if labels.get(lang)), entity["id"])
        desc = next((descriptions.get(lang, {}).get("value") for lang in ("es", "en", "fr") if descriptions.get(lang)), "")
        out.append({
            "id": entity["id"], "l": label, "t": desc,
            "lat": lat, "lon": lon,
            "d": round(km(item["lat"], item["lon"], lat, lon), 1),
        })
    return out


def fetch_slug(slug):
    prepared = json.loads((GEO / f"{slug}_queries.json").read_text(encoding="utf-8"))
    bbox = prepared.get("bbox")
    output = []
    for number, item in enumerate(prepared["items"], 1):
        ph, wd = [], []
        for query in item["q"]:
            try:
                ph = photon(query, item, bbox)
            except Exception as exc:
                ph = [{"err": str(exc)}]
            if ph and "err" not in ph[0]:
                break
        for query in item["q"][:2]:
            try:
                wd = wikidata(query, item, bbox)
            except Exception as exc:
                wd = [{"err": str(exc)}]
            if wd and "err" not in wd[0]:
                break
        output.append({"id": item["id"], "ph": ph[:3], "wd": wd[:2]})
        print(f"{slug} {number}/{len(prepared['items'])} {item['id']}", flush=True)
        time.sleep(0.15)
    path = GEO / f"{slug}_ref.json"
    path.write_text(json.dumps(output, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{slug}: {len(output)} referencias -> {path}")


if __name__ == "__main__":
    for requested_slug in sys.argv[1:]:
        fetch_slug(requested_slug)

#!/usr/bin/env python3
"""Consulta Photon y Wikidata y guarda las referencias de una auditoría GPS.

Uso: python3 tools/gen/audit_geo_fetch.py <slug>
"""
from __future__ import annotations

import json
import math
import ssl
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

import certifi


ROOT = Path(__file__).resolve().parents[2]
GEO = ROOT / "audit" / "geo"
CONTEXT = ssl.create_default_context(cafile=certifi.where())
AGENT = "Africa2027-geo-audit/1.0 (route planning data verification)"


def request(url: str) -> dict:
    req = urllib.request.Request(url, headers={"User-Agent": AGENT})
    with urllib.request.urlopen(req, timeout=30, context=CONTEXT) as response:
        return json.load(response)


def km(a: float, b: float, c: float, d: float) -> float:
    rad = math.pi / 180
    x, y = (c - a) * rad, (d - b) * rad
    h = math.sin(x / 2) ** 2 + math.cos(a * rad) * math.cos(c * rad) * math.sin(y / 2) ** 2
    return 6371 * 2 * math.asin(math.sqrt(h))


def photon(query: str, item: dict, bbox: list[float]) -> list[dict]:
    params = urllib.parse.urlencode({
        "q": query,
        "limit": 6,
        "lat": item["lat"],
        "lon": item["lon"],
        "bbox": ",".join(str(x) for x in bbox),
    })
    data = request("https://photon.komoot.io/api/?" + params)
    out = []
    for feature in data.get("features", []):
        lon, lat = feature["geometry"]["coordinates"]
        if not (bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]):
            continue
        props = feature.get("properties", {})
        out.append({
            "n": props.get("name", ""),
            "k": props.get("osm_key"),
            "v": props.get("osm_value"),
            "lat": round(lat, 5),
            "lon": round(lon, 5),
            "d": round(km(item["lat"], item["lon"], lat, lon), 1),
        })
    return out[:3]


def wikidata(query: str, item: dict, bbox: list[float]) -> list[dict]:
    ids = []
    for language in ("es", "fr", "en", "pt"):
        params = urllib.parse.urlencode({
            "action": "wbsearchentities", "search": query, "language": language,
            "format": "json", "limit": 4, "origin": "*",
        })
        data = request("https://www.wikidata.org/w/api.php?" + params)
        ids.extend(row["id"] for row in data.get("search", []))
        if len(ids) >= 4:
            break
    ids = list(dict.fromkeys(ids))[:6]
    if not ids:
        return []
    params = urllib.parse.urlencode({
        "action": "wbgetentities", "ids": "|".join(ids),
        "props": "claims|labels|descriptions", "languages": "es|en|fr",
        "format": "json", "origin": "*",
    })
    data = request("https://www.wikidata.org/w/api.php?" + params)
    out = []
    for entity in data.get("entities", {}).values():
        claims = entity.get("claims", {}).get("P625", [])
        coords = [row.get("mainsnak", {}).get("datavalue", {}).get("value") for row in claims]
        coords = [row for row in coords if row]
        if not coords:
            continue
        lat, lon = coords[0]["latitude"], coords[0]["longitude"]
        if not (bbox[0] <= lon <= bbox[2] and bbox[1] <= lat <= bbox[3]):
            continue
        labels = entity.get("labels", {})
        descriptions = entity.get("descriptions", {})
        label = next((labels.get(lang, {}).get("value") for lang in ("es", "en", "fr") if labels.get(lang)), entity["id"])
        desc = next((descriptions.get(lang, {}).get("value") for lang in ("es", "en", "fr") if descriptions.get(lang)), "")
        out.append({
            "id": entity["id"], "l": label, "t": desc,
            "lat": round(lat, 5), "lon": round(lon, 5),
            "d": round(km(item["lat"], item["lon"], lat, lon), 1),
        })
    return out[:2]


def main(slug: str) -> None:
    data = json.loads((GEO / f"{slug}_queries.json").read_text(encoding="utf-8"))
    rows = []
    for item in data["items"]:
        row = {"id": item["id"], "ph": [], "wd": []}
        for query in item["q"]:
            try:
                row["ph"] = photon(query, item, data["bbox"])
            except Exception as error:
                row["ph"] = [{"err": f"{type(error).__name__}: {error}"}]
            if row["ph"] and "err" not in row["ph"][0]:
                break
        for query in item["q"][:2]:
            try:
                row["wd"] = wikidata(query, item, data["bbox"])
            except Exception as error:
                row["wd"] = [{"err": f"{type(error).__name__}: {error}"}]
            if row["wd"] and "err" not in row["wd"][0]:
                break
        rows.append(row)
        time.sleep(0.1)
    target = GEO / f"{slug}_ref.json"
    target.write_text(json.dumps(rows, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{slug}: {len(rows)} referencias -> {target}")


if __name__ == "__main__":
    main(sys.argv[1])

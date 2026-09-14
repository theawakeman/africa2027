#!/usr/bin/env python3
"""Busca candidatos de fotografía en Commons sin modificar contenido.

Uso: python3 tools/audit_commons.py "Mount Cameroon" "Lobe Falls Cameroon"
     python3 tools/audit_commons.py --compact "Mount Cameroon" "Lobe Falls Cameroon"
     python3 tools/audit_commons.py --check-json content/pois/angola.json
La salida conserva título, descripción, autor, licencia y GPS para que la
selección sea humana; una coincidencia de buscador no se considera verificación.
"""
import html
import json
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

import certifi

API = "https://commons.wikimedia.org/w/api.php"


def clean(value):
    value = html.unescape(re.sub(r"<[^>]+>", " ", value or ""))
    return re.sub(r"\s+", " ", value).strip()


def request_json(params):
    request = urllib.request.Request(
        API + "?" + urllib.parse.urlencode(params),
        headers={"User-Agent": "Africa2027-photo-audit/1.0"},
    )
    context = ssl.create_default_context(cafile=certifi.where())
    for attempt in range(6):
        try:
            with urllib.request.urlopen(request, timeout=30, context=context) as response:
                payload = json.load(response)
            break
        except urllib.error.HTTPError as error:
            if error.code != 429 or attempt == 5:
                raise
            retry_after = error.headers.get("Retry-After")
            delay = int(retry_after) if retry_after and retry_after.isdigit() else 8 * (attempt + 1)
            time.sleep(delay)
    return payload


def search(query, limit=6):
    params = {
        "action": "query",
        "format": "json",
        "generator": "search",
        "gsrsearch": query,
        "gsrnamespace": 6,
        "gsrlimit": limit,
        "prop": "imageinfo",
        "iiprop": "url|extmetadata",
        "iiurlwidth": 1200,
    }
    payload = request_json(params)
    pages = sorted(payload.get("query", {}).get("pages", {}).values(), key=lambda x: x.get("index", 999))
    out = []
    for page in pages:
        info = (page.get("imageinfo") or [{}])[0]
        meta = info.get("extmetadata") or {}
        value = lambda key: clean((meta.get(key) or {}).get("value", ""))
        out.append({
            "title": page.get("title", ""),
            "description": value("ImageDescription"),
            "artist": value("Artist"),
            "license": value("LicenseShortName"),
            "latitude": value("GPSLatitude"),
            "longitude": value("GPSLongitude"),
            "thumb": info.get("thumburl", ""),
            "source": info.get("descriptionurl", ""),
        })
    return out


def check_json(path):
    with open(path, encoding="utf-8") as handle:
        pois = json.load(handle)
    expected = []
    for poi in pois:
        for photo in poi.get("photos", []):
            source = photo.get("source", "")
            marker = "/wiki/File:"
            if marker not in source:
                continue
            title = "File:" + urllib.parse.unquote(source.split(marker, 1)[1]).replace("_", " ")
            expected.append((poi.get("n"), poi.get("name"), title, photo.get("credit", "")))
    results = []
    for start in range(0, len(expected), 20):
        chunk = expected[start:start + 20]
        params = {
            "action": "query",
            "format": "json",
            "titles": "|".join(title for _, _, title, _ in chunk),
            "prop": "imageinfo",
            "iiprop": "extmetadata",
        }
        payload = request_json(params)
        normalized = {x["from"]: x["to"] for x in payload.get("query", {}).get("normalized", [])}
        pages = {page.get("title"): page for page in payload.get("query", {}).get("pages", {}).values()}
        for number, name, requested, declared_credit in chunk:
            title = normalized.get(requested, requested)
            page = pages.get(title, {})
            info = (page.get("imageinfo") or [{}])[0]
            meta = info.get("extmetadata") or {}
            value = lambda key: clean((meta.get(key) or {}).get("value", ""))
            results.append({
                "n": number,
                "name": name,
                "requested": requested,
                "resolved": page.get("title", ""),
                "exists": bool(info),
                "description": value("ImageDescription"),
                "artist": value("Artist"),
                "license": value("LicenseShortName"),
                "declared_credit": declared_credit,
                "latitude": value("GPSLatitude"),
                "longitude": value("GPSLongitude"),
            })
        time.sleep(2)
    return results


def main():
    if len(sys.argv) < 2:
        raise SystemExit("Indica al menos una consulta")
    if sys.argv[1] == "--check-json":
        if len(sys.argv) != 3:
            raise SystemExit("Uso: --check-json RUTA")
        print(json.dumps(check_json(sys.argv[2]), ensure_ascii=False, indent=2))
        return
    compact = sys.argv[1] == "--compact"
    queries = sys.argv[2:] if compact else sys.argv[1:]
    if not queries:
        raise SystemExit("Indica al menos una consulta")
    for query in queries:
        candidates = search(query)
        if compact:
            candidates = [
                {
                    "title": item["title"],
                    "description": item["description"][:240],
                    "artist": item["artist"],
                    "license": item["license"],
                    "latitude": item["latitude"],
                    "longitude": item["longitude"],
                    "source": item["source"],
                }
                for item in candidates
            ]
        print(json.dumps({"query": query, "candidates": candidates}, ensure_ascii=False))
        time.sleep(2)


if __name__ == "__main__":
    main()

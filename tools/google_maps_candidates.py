#!/usr/bin/env python3
"""Consulta candidatos de Google Maps sin seleccionar uno a ciegas.

La salida conserva nombre, categoría, dirección, coordenadas, identificador y
URL de los primeros resultados. La elección editorial sigue siendo manual.
"""
from __future__ import annotations

import argparse
import json
import ssl
import urllib.parse
import urllib.request

import certifi


ENDPOINT = "https://www.google.com/search"


def photo_urls(value: object, limit: int = 6) -> list[str]:
    """Extrae solo las fotos servidas por la ficha, sin otros enlaces del payload."""
    found: list[str] = []

    def walk(item: object) -> None:
        if len(found) >= limit:
            return
        if isinstance(item, str):
            if item.startswith("https://lh3.googleusercontent.com/") and item not in found:
                found.append(item)
            return
        if isinstance(item, list):
            for child in item:
                walk(child)
        elif isinstance(item, dict):
            for child in item.values():
                walk(child)

    walk(value)
    return found


def fetch(query: str, limit: int) -> list[dict]:
    params = urllib.parse.urlencode({"tbm": "map", "hl": "es", "q": query})
    request = urllib.request.Request(
        f"{ENDPOINT}?{params}",
        headers={"User-Agent": "Africa2027-geodata-audit/1.0"},
    )
    context = ssl.create_default_context(cafile=certifi.where())
    with urllib.request.urlopen(request, timeout=30, context=context) as response:
        raw = response.read().decode("utf-8")
    payload = json.loads(raw.removeprefix(")]}'\n"))
    result = []
    for wrapper in (payload[0][1] or [])[:limit]:
        place = wrapper[14] if len(wrapper) > 14 else None
        if not isinstance(place, list) or len(place) < 12:
            continue
        point = place[9] if isinstance(place[9], list) else []
        if len(point) < 4 or not isinstance(point[2], (int, float)):
            continue
        result.append(
            {
                "name": place[11],
                "lat": point[2],
                "lon": point[3],
                "address": place[39] if len(place) > 39 else None,
                "categories": place[13],
                "feature_id": place[10],
                "url": place[42] if len(place) > 42 else None,
                "photos": photo_urls(place),
            }
        )
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", nargs="+")
    parser.add_argument("--limit", type=int, default=3)
    args = parser.parse_args()
    for query in args.query:
        print(
            json.dumps(
                {"query": query, "candidates": fetch(query, args.limit)},
                ensure_ascii=False,
            )
        )


if __name__ == "__main__":
    main()

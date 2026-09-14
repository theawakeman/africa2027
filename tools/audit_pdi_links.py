#!/usr/bin/env python3
"""Comprueba los enlaces informativos e imágenes externas de uno o más JSON PDI."""
from __future__ import annotations

import json
import ssl
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import certifi


CONTEXT = ssl.create_default_context(cafile=certifi.where())


def probe(item: tuple[str, str, str]) -> tuple[str, str, str, int, str]:
    country, label, url = item
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 Africa2027-link-audit/1.0",
            "Range": "bytes=0-2047",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30, context=CONTEXT) as response:
            response.read(2048)
            return country, label, url, response.status, response.geturl()
    except urllib.error.HTTPError as error:
        return country, label, url, error.code, error.geturl()
    except Exception as error:  # La salida conserva la causa exacta para revisarla.
        return country, label, url, 0, f"{type(error).__name__}: {error}"


def collect(path: Path) -> list[tuple[str, str, str]]:
    country = path.stem
    pois = json.loads(path.read_text(encoding="utf-8"))
    items = []
    for poi in pois:
        for link in poi.get("links", []):
            if isinstance(link, dict) and str(link.get("url", "")).startswith("http"):
                items.append((country, f'{poi["n"]} enlace', link["url"]))
        for photo in poi.get("photos", []):
            if not isinstance(photo, dict):
                continue
            image = str(photo.get("img", ""))
            if image.startswith("http") and "commons.wikimedia.org" not in image:
                items.append((country, f'{poi["n"]} imagen', image))
    return items


def main() -> None:
    if len(sys.argv) < 2:
        raise SystemExit("Uso: audit_pdi_links.py content/pois/pais.json [...]")
    items = []
    for argument in sys.argv[1:]:
        items.extend(collect(Path(argument)))
    with ThreadPoolExecutor(max_workers=6) as pool:
        results = list(pool.map(probe, items))
    failures = 0
    for country, label, url, status, final in results:
        blocked = status in {401, 403, 429}
        semantic_404 = "/404" in final.lower()
        ok = 200 <= status < 400 and not semantic_404
        failures += not ok
        state = "BLOCKED" if blocked else ("OK" if ok else "FAIL")
        if blocked:
            failures -= 1  # Un WAF no demuestra que el enlace público esté roto.
        print(f'{state} {status:>3} {country} {label} {url}')
        if final != url:
            print(f"  -> {final}")
    print(f"TOTAL {len(results)} | FALLOS {failures}")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()

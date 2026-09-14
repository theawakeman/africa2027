#!/usr/bin/env python3
"""Valida que fuente, tarjeta, mapa de país y mapa general comparten cada PDI."""

from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
POIS_DIR = ROOT / "content" / "pois"
GLOBAL_POINTS = ROOT / "assets" / "js" / "points.json"
VISIT_KEYS = {"why", "see", "access", "when", "skip"}


def embedded_config(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    match = re.search(r"var A27_FICHA = (\{.*?\});</script>", text, re.DOTALL)
    if not match:
        raise ValueError(f"no se encuentra A27_FICHA en {path}")
    return json.loads(match.group(1))


def source_photos(poi: dict) -> list[dict]:
    photos = [photo for photo in poi.get("photos", []) if isinstance(photo, dict) and photo.get("img")]
    if photos:
        return photos
    if poi.get("img"):
        return [{
            "img": poi["img"],
            "credit": poi.get("credit", ""),
            "source": poi.get("source", ""),
            # Coincide con la normalización de build.py para el formato antiguo.
            # El modal usa el nombre del PDI como pie solo en el navegador.
            "caption": "",
        }]
    return []


def card_fragment(page: str, number: object) -> str:
    pattern = rf'<article class="poi-card" id="poi-{re.escape(str(number))}".*?</article>'
    match = re.search(pattern, page, re.DOTALL)
    return match.group(0) if match else ""


def visible_text(fragment: str) -> str:
    """Texto visible aproximado de un fragmento generado.

    El postprocesador enlaza nombres de fuentes dentro de las descripciones;
    retirar las etiquetas permite comprobar el contenido, no su marcado.
    """
    return html.unescape(re.sub(r"<[^>]+>", "", fragment))


def compare_point(label: str, actual: dict, source: dict, photos: list[dict], errors: list[str]) -> None:
    direct = ("name", "cat", "prio", "time", "desc", "dog", "dog_note", "visit", "links")
    for key in direct:
        expected = source.get(key, {} if key == "visit" else [] if key == "links" else "")
        if actual.get(key, {} if key == "visit" else [] if key == "links" else "") != expected:
            errors.append(f"{label}: difiere {key}")
    if actual.get("lat") != round(float(source["lat"]), 5):
        errors.append(f"{label}: difiere lat")
    if actual.get("lon") != round(float(source["lon"]), 5):
        errors.append(f"{label}: difiere lon")
    if actual.get("photos") != photos:
        errors.append(f"{label}: difiere la galería")
    cover = photos[0]["img"] if photos else ""
    if actual.get("img", "") != cover:
        errors.append(f"{label}: la portada no es la primera foto")


def validate_country(
    slug: str,
    global_by_ref: dict[str, dict],
    *,
    require_detail: bool = True,
) -> tuple[int, list[str]]:
    errors: list[str] = []
    source_path = POIS_DIR / f"{slug}.json"
    page_path = ROOT / "paises" / slug / "index.html"
    pois = json.loads(source_path.read_text(encoding="utf-8"))
    page = page_path.read_text(encoding="utf-8")
    cfg = embedded_config(page_path)
    country_by_ref = {point.get("ficha"): point for point in cfg.get("points", []) if point.get("type") == "poi"}

    for poi in pois:
        number = poi.get("n")
        label = f"{slug} PDI {number} ({poi.get('name', '')})"
        local_ref = f"#poi-{number}"
        global_ref = f"paises/{slug}/#poi-{number}"
        photos = source_photos(poi)
        links = [link for link in poi.get("links", []) if isinstance(link, dict) and str(link.get("url", "")).startswith("http")]
        visit = poi.get("visit") if isinstance(poi.get("visit"), dict) else {}

        if not photos:
            errors.append(f"{label}: sin fotografía")
        if require_detail:
            if not links:
                errors.append(f"{label}: sin enlace útil")
            if not VISIT_KEYS.issubset(visit):
                errors.append(f"{label}: faltan campos de decisión {sorted(VISIT_KEYS - set(visit))}")

        local = country_by_ref.get(local_ref)
        global_point = global_by_ref.get(global_ref)
        if local is None:
            errors.append(f"{label}: ausente del mapa de país")
        else:
            compare_point(f"{label} / mapa de país", local, poi, photos, errors)
        if global_point is None:
            errors.append(f"{label}: ausente del mapa general")
        else:
            compare_point(f"{label} / mapa general", global_point, poi, photos, errors)

        card = card_fragment(page, number)
        if not card:
            errors.append(f"{label}: tarjeta ausente")
            continue
        desc_match = re.search(r'<p class="poi-desc">(.*?)</p>', card, re.DOTALL)
        cover = photos[0]["img"] if photos else ""
        if not desc_match or visible_text(desc_match.group(1)) != str(poi.get("desc", "")):
            errors.append(f"{label}: el resumen de la tarjeta difiere")
        if cover:
            image_match = re.search(r'<img[^>]+src="([^"]+)"', card)
            card_cover = html.unescape(image_match.group(1)) if image_match else ""
            if card_cover.removeprefix("../../") != cover:
                errors.append(f"{label}: la portada de la tarjeta difiere")

    expected_refs = {f"#poi-{poi['n']}" for poi in pois}
    if set(country_by_ref) != expected_refs:
        errors.append(f"{slug}: conjunto de PDIs del mapa de país distinto de la fuente")
    return len(pois), errors


def main() -> None:
    args = sys.argv[1:]
    sync_only = "--sync-only" in args
    slugs = [arg for arg in args if arg != "--sync-only"]
    if not slugs:
        slugs = sorted(path.stem for path in POIS_DIR.glob("*.json"))
    global_points = json.loads(GLOBAL_POINTS.read_text(encoding="utf-8"))
    global_by_ref: dict[str, dict] = {}
    duplicate_refs: set[str] = set()
    for point in global_points:
        ref = point.get("ficha")
        if point.get("type") != "poi" or not ref:
            continue
        if ref in global_by_ref:
            duplicate_refs.add(ref)
        global_by_ref[ref] = point

    total = 0
    all_errors: list[str] = []
    for slug in slugs:
        count, errors = validate_country(slug, global_by_ref, require_detail=not sync_only)
        total += count
        all_errors.extend(errors)
        print(f"{slug}: {count} PDIs · {'OK' if not errors else f'{len(errors)} errores'}")

    selected_prefixes = tuple(f"paises/{slug}/#poi-" for slug in slugs)
    selected_duplicates = sorted(ref for ref in duplicate_refs if ref.startswith(selected_prefixes))
    if selected_duplicates:
        all_errors.append(f"referencias duplicadas en mapa general: {selected_duplicates}")
    if all_errors:
        print("\n".join(f"ERROR {error}" for error in all_errors))
        raise SystemExit(1)
    print(f"TOTAL {total} PDIs · fuente, tarjeta, mapa de país y mapa general sincronizados")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Valida la estructura de la auditoría de agua de servicio por país."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FICHA = ROOT / "content" / "ficha"


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


slugs = sys.argv[1:]
if not slugs:
    fail("indica al menos un slug de país")

total = 0
all_coords: dict[tuple[float, float], str] = {}
for slug in slugs:
    path = FICHA / f"{slug}.json"
    if not path.exists():
        fail(f"{slug}: no existe {path}")
    data = json.loads(path.read_text(encoding="utf-8"))

    sections = [s for s in data.get("custom_sections", []) if s[0] == "agua-combustible"]
    if len(sections) != 1:
        fail(f"{slug}: se esperaba una sección agua-combustible")
    html = sections[0][2]
    for required in ("Agua de servicio", "Agua de servicio no significa agua potable", "Combustible"):
        if required not in html:
            fail(f"{slug}: falta el criterio {required!r}")

    points = [p for p in data.get("logistics", []) if "agua" in str(p.get("cat", "")).lower()]
    if not points:
        fail(f"{slug}: no tiene puntos de agua auditados")
    for point in points:
        if point.get("cat") != "Agua de servicio":
            fail(f"{slug}: categoría antigua en {point.get('name')}")
        if not str(point.get("info", "")).startswith("["):
            fail(f"{slug}: falta estado operativo en {point.get('name')}")
        if not str(point.get("source", "")).startswith("http"):
            fail(f"{slug}: falta fuente directa en {point.get('name')}")
        coords = (float(point["lat"]), float(point["lon"]))
        if coords in all_coords:
            fail(f"{slug}: coordenadas repetidas con {all_coords[coords]}: {coords}")
        all_coords[coords] = f"{slug}/{point['name']}"
    total += len(points)
    print(f"{slug}: {len(points)} puntos · OK")

print(f"TOTAL {total} puntos de agua de servicio auditados")

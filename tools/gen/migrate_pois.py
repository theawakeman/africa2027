# -*- coding: utf-8 -*-
"""Migración única: vuelca los POIs calculados de cada país (tal y como los
produce hoy build.py, incluyendo cualquier ficha de foto ya corregida) a
content/pois/<slug>.json, para que el panel de edición (/admin/) los use como
fuente editable. No toca las fichas de país en Python: build.py seguirá
importándolas para todo lo demás (historia, chips, secciones, logística...).

Ejecutar una sola vez; volver a ejecutarlo sobreescribiría cualquier edición
hecha desde el panel con el estado actual de los data_<pais>.py, así que no
forma parte del build normal.
"""
import json
from pathlib import Path

from site_common import SITE
import data_senegal
import data_mauritania

FULL = {"senegal": data_senegal.get_data(), "mauritania": data_mauritania.get_data()}
import importlib
for _slug in ["marruecos", "sahara-occidental", "guinea", "sierra-leona", "liberia", "costa-de-marfil",
              "ghana", "togo", "benin", "nigeria", "camerun", "gabon", "congo", "rd-congo", "angola",
              "namibia", "sudafrica", "mozambique", "malaui", "tanzania", "kenia", "etiopia", "sudan", "egipto",
              "gambia", "lesoto", "esuatini", "zimbabue", "botsuana", "zambia", "uganda", "ruanda", "yibuti"]:
    try:
        _m = importlib.import_module("data_" + _slug.replace("-", "_"))
        FULL[_slug] = _m.get_data()
    except ModuleNotFoundError:
        pass

POIS_DIR = SITE / "content" / "pois"
POIS_DIR.mkdir(parents=True, exist_ok=True)

n_written = 0
for slug, d in FULL.items():
    out = POIS_DIR / f"{slug}.json"
    if out.exists():
        print(f"SKIP {slug}: ya existe {out}, no se sobreescribe")
        continue
    out.write_text(json.dumps(d["pois"], ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n_written += 1
    print(f"OK {slug}: {len(d['pois'])} POIs -> {out}")

print(f"\n{n_written} archivos escritos en {POIS_DIR}")

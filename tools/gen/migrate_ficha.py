# -*- coding: utf-8 -*-
"""Migración única: vuelca el resto de la ficha de cada país (hero, chips,
historia, logística, fuentes, secciones personalizadas...) tal y como la
produce hoy data_<pais>.py, a content/ficha/<slug>.json, para que el panel de
edición (/admin/) los use como fuente editable (Fase 2 del CMS).

No toca los POIs (eso ya lo hace migrate_pois.py / content/pois/<slug>.json).

Ejecutar una sola vez; volver a ejecutarlo sobreescribiría cualquier edición
hecha desde el panel con el estado actual de los data_<pais>.py, así que no
forma parte del build normal.
"""
import json

from site_common import SITE, FICHA_FIELDS
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

FICHA_DIR = SITE / "content" / "ficha"
FICHA_DIR.mkdir(parents=True, exist_ok=True)

n_written = 0
for slug, d in FULL.items():
    out = FICHA_DIR / f"{slug}.json"
    if out.exists():
        print(f"SKIP {slug}: ya existe {out}, no se sobreescribe")
        continue
    data = {k: d[k] for k in FICHA_FIELDS if k in d}
    out.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    n_written += 1
    print(f"OK {slug}: {len(data)} campos -> {out}")

print(f"\n{n_written} archivos escritos en {FICHA_DIR}")

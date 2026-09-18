# -*- coding: utf-8 -*-
"""Vuelca a content/ los PDIs y la ficha de UN país a partir de su data_<slug>.py.

Uso: python3 tools/gen/exporta_contenido.py <slug> [--force]

Sirve para dar de alta un país nuevo en el CMS (/admin/) o para sincronizar
un país cuya fuente sigue siendo el módulo Python. No sobreescribe un JSON
existente salvo con --force, porque los JSON son la fuente editable y pueden
contener correcciones hechas desde el panel.
"""
import importlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from site_common import SITE, FICHA_FIELDS  # noqa: E402


def main(slug, force=False):
    mod = importlib.import_module("data_" + slug.replace("-", "_"))
    d = mod.get_data()
    pois = SITE / "content" / "pois" / f"{slug}.json"
    ficha = SITE / "content" / "ficha" / f"{slug}.json"
    for path, payload in ((pois, d["pois"]), (ficha, {k: d[k] for k in FICHA_FIELDS if k in d})):
        if path.exists() and not force:
            print(f"SKIP {path}: ya existe (usa --force para sobreescribir)")
            continue
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"OK {path}")


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        raise SystemExit(__doc__)
    main(args[0], force="--force" in sys.argv)

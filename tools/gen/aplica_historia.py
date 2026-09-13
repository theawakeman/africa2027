# -*- coding: utf-8 -*-
"""Vuelca las historias ampliadas de audit/historia/<slug>.json a content/ficha/<slug>.json.

Sustituye historia_resumen, historia_secciones e historia_fuentes conservando el
resto de la ficha. Las notas del redactor se guardan en audit/historia/NOTAS.md.

Uso:  python3 aplica_historia.py <slug> [<slug> ...]
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]


def main(slugs):
    notas = []
    for slug in slugs:
        h = json.loads((ROOT / "audit" / "historia" / f"{slug}.json").read_text(encoding="utf-8"))
        fp = ROOT / "content" / "ficha" / f"{slug}.json"
        d = json.loads(fp.read_text(encoding="utf-8"))
        antes = len(json.dumps(d.get("historia_secciones", []), ensure_ascii=False))
        d["historia_resumen"] = h["historia_resumen"]
        d["historia_secciones"] = [list(x) for x in h["historia_secciones"]]
        d["historia_fuentes"] = [list(x) for x in h["historia_fuentes"]]
        fp.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        despues = len(json.dumps(d["historia_secciones"], ensure_ascii=False))
        print(f"{slug}: {len(d['historia_secciones'])} secciones, {len(d['historia_fuentes'])} fuentes ({antes} → {despues} car.)")
        if h.get("notas"):
            notas.append(f"## {slug}\n\n" + "\n".join(f"- {n}" for n in h["notas"]))
    if notas:
        (ROOT / "audit" / "historia" / "NOTAS.md").write_text(
            "# Notas de los redactores de historia (dudas y datos no verificados)\n\n" + "\n\n".join(notas) + "\n",
            encoding="utf-8")


if __name__ == "__main__":
    main(sys.argv[1:])

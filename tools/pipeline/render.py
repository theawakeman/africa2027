#!/usr/bin/env python3
"""Rellena las tres plantillas de encargo con los parámetros de un país.

Uso: python3 render.py <slug>   →  escribe scratchpad/<slug>/prompt_{historia,pdis,operativo}.md
Los parámetros están en scratchpad/paises.json (clave = slug).
"""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRATCH = Path(os.environ.get("A27_SCRATCH", HERE.parent))
FECHA = "18 de septiembre de 2026"


def main(slug):
    params = json.loads((SCRATCH / "paises.json" if (SCRATCH / "paises.json").exists() else HERE / "paises.json").read_text())[slug]
    params.setdefault("SLUG", slug)
    params.setdefault("FECHA", FECHA)
    params.setdefault("FUENTES_EXTRA", "")
    params["PDI_LIST"] = "\n".join(f"{i} {p}" for i, p in enumerate(params["PDIS"], 1))
    out = SCRATCH / slug
    out.mkdir(exist_ok=True)
    for name in ("historia", "pdis", "operativo"):
        t = (HERE / f"{name}.md").read_text()
        for k, v in params.items():
            if isinstance(v, str):
                t = t.replace("{" + k + "}", v)
        missing = [m for m in ("{PAIS}", "{CONTEXTO}", "{SLUG}") if m in t]
        assert not missing, missing
        (out / f"prompt_{name}.md").write_text(t)
        print("ok", out / f"prompt_{name}.md")


if __name__ == "__main__":
    for s in sys.argv[1:]:
        main(s)

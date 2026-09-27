# -*- coding: utf-8 -*-
"""Títulos neutros para los recorridos y subtítulos de las fichas.

Las fichas se escribieron para una ruta fija (bajada por la costa oeste, bucle
en el sur y subida). Con el planificador el viaje puede ir en cualquier orden,
así que los títulos visibles no deben decir «bajada», «subida» ni
«alternativa»: cada corredor es un recorrido (A, B, …) y el papel que tiene en
el viaje lo pone la página según el plan activo en el Planificador.
"""
import re

from data_cabeceras import RUTAS

# Descripciones a mano cuando la etiqueta original solo decía el papel.
PROPIAS = {
    ("sahara-occidental", "corridor"): "Tránsito rápido por la costa",
    ("sahara-occidental", "corridor_alt"): "Con más tiempo: Cintra, Imlili, Asmaa y Smara",
    ("tanzania", "corridor"): "Por el interior (Zambia – Kenia)",
    ("tanzania", "corridor_alt"): "Por la costa (Kenia – Mozambique)",
    ("mauritania", "corridor"): "Guerguerat – Atar – Uadane",
    ("mauritania", "corridor_alt"): "Uadane – Nuakchot – Diama",
    ("angola", "corridor"): "Lufu – frontera de Zambia",
    ("angola", "corridor_alt"): "Santa Clara (Namibia) – Lufu",
    ("tunez", "corridor"): "Norte → sur (La Goulette → oasis de montaña)",
}

_ROL = re.compile(r"^(bajada|subida|ida|vuelta)\b\s*(\([^)]*\))?\s*(·|:|—|-)?\s*", re.I)


def _extremos(slug, key):
    par = RUTAS.get(slug)
    if not par:
        return ""
    txt = par[0 if key == "corridor" else 1]
    txt = re.sub(r"\s*\(.*?\)", "", txt.split(" · ")[0]).strip()
    if "→" not in txt or txt.lower().startswith(("no aplica", "opcional", "solo", "fuera", "excluido", "variante")):
        return ""
    return txt.replace(" → ", " – ")


def descripcion(slug, key, label):
    """Etiqueta sin papel de ruta: «Bajada · eje costero» → «Eje costero»."""
    if (slug, key) in PROPIAS:
        return PROPIAS[(slug, key)]
    label = (label or "").strip()
    resto = _ROL.sub("", label, count=1).strip() if _ROL.match(label) else label
    if not resto:
        resto = _extremos(slug, key)
    if resto.lower() in ("corredor", "corredor principal", "corredor alternativo"):
        resto = ""
    resto = re.sub(r"^alternativa secundaria\s*·\s*", "Secundario · ", resto, flags=re.I)
    return resto[:1].upper() + resto[1:] if resto else ""


def etiqueta(slug, key, label, letra):
    desc = descripcion(slug, key, label)
    return f"Recorrido {letra} · {desc}" if desc else f"Recorrido {letra}"


_SEG = re.compile(
    r"(fuera de (la )?ruta|excluid|protocolo|^alternativa|ficha informativa|ruta fija|corredor|bajada|subida|bucle"
    r"|tránsito|primer país|recta final|punto más|se cruza|vuelta de 2027|no está en la ruta|solo alcanzable"
    r"|ruta overland|travesía norte|^entrada |^salida |desvío|va unida|variante|revisión \d|opcional|vehículos"
    r"|viajeros|perro|documentación|logística|^seguridad$|seguridad determinante|→|en estudio|de paso|ida y vuelta)", re.I)


def subtitulo(sub):
    """Quita del subtítulo de la ficha los trozos que hablan del papel en la ruta."""
    partes = [p.strip() for p in re.split(r"\s+[—·|]\s+", sub or "") if p.strip()]
    txt = " · ".join(p for p in partes if not _SEG.search(p))
    return txt[:1].upper() + txt[1:]

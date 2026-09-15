#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 8.

Sustituye dos pines regionales por cinco instalaciones físicas y separa
ducha, fregado, toma publicada, llenado autorizado y potabilidad.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FICHA = ROOT / "content" / "ficha"

COMMON = (
    '<div class="callout warn"><div class="callout-title">Regla operativa</div>'
    '<p><strong>Agua de servicio no significa agua potable.</strong> Que un camping tenga '
    'ducha, fregadero o grifo no autoriza a cargar los depósitos. Antes de desviarse hay '
    'que confirmar fecha, litros, toma, precio, calidad, restricciones por sequía y acceso '
    'de los dos 4x4. Para beber y cocinar: agua sellada o tratamiento completo salvo '
    'confirmación sanitaria local vigente.</p></div>'
    '<div class="callout"><div class="callout-title">Criterio común del proyecto</div>'
    '<p>Estados, reservas, higiene del depósito y protocolo de potabilización: ver '
    '<a href="../../documentacion/#agua-combustible">Documentación general · agua y combustible</a>.</p></div>'
)


def a(url: str, label: str) -> str:
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


def gm(lat: float, lon: float) -> str:
    return a(f"https://www.google.com/maps?q={lat},{lon}", "GPS comprobado")


def table(rows: list[tuple[str, str, str]]) -> str:
    body = "".join(
        f"<tr><td>{place}</td><td>{status}</td><td>{action}</td></tr>"
        for place, status, action in rows
    )
    return (
        '<div class="tblwrap"><table><thead><tr><th>Punto exacto</th>'
        '<th>Qué está acreditado</th><th>Decisión operativa</th></tr></thead>'
        f'<tbody>{body}</tbody></table></div>'
    )


WATER = {
    "esuatini": {
        "intro": (
            "<h3>Agua de servicio: dos campamentos reales del corredor</h3>"
            "<p>Se retira el marcador regional Ezulwini–Mbabane–Manzini. Mlilwane publica "
            "puntos de agua en parte del camping; Ndlovu acredita ducha y fregado, pero "
            "su propia ficha dice que no hay tomas en las parcelas.</p>"
        ),
        "rows": [
            (
                "Mlilwane Rest Camp · -26.492764, 31.185226",
                "<strong>Veinte parcelas con punto de agua y electricidad y otras diez con "
                "agua cercana, además de un bloque grande de abluciones.</strong> La fuente "
                "no publica potabilidad ni permiso para llenar depósitos. "
                + a("https://biggameparks.org/img/cms/tabs/MLILWANE%20PRODUCT%20SHEET%20for%20Web.pdf", "ficha oficial")
                + " · " + gm(-26.4927635, 31.1852261),
                "Primera opción para concertar una carga en el eje central. Reservar y "
                "confirmar dos 4x4, volumen, manguera, coste, calidad y acceso sin perro.",
            ),
            (
                "Ndlovu Camp, Hlane · -26.259647, 31.874957",
                "<strong>Camping con abluciones amplias, agua caliente por caldera de leña, "
                "cocina comunitaria y zona de fregado; sin electricidad ni puntos de agua "
                "en las parcelas.</strong> "
                + a("https://biggameparks.org/properties/hlane-royal-national-park", "parque oficial")
                + " · " + gm(-26.2596472, 31.8749574),
                "Parada de ducha y lavado durante una estancia reservada, no de llenado. "
                "Entrar al lowveld con los depósitos cargados y sin contar con el perro.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Mlilwane es el único punto del '
            "país auditado cuya fuente publica tomas en el camping. Sigue siendo una "
            "recarga condicionada: obtener permiso y litros antes de llegar.</li><li>Ndlovu "
            "resuelve ducha y fregado, pero la ficha oficial niega expresamente grifos en las "
            "parcelas. No pedir una carga que comprometa el suministro del parque.</li><li>Los "
            "dos puntos están dentro de reservas con fauna. Planificar la estancia del perro "
            "por separado y no dejarlo en el vehículo para usar las duchas.</li><li>Malolotja, "
            "Maguga, Phophonyane y KaMsholo quedan sin pin de agua: sus fuentes no acreditan "
            "a la vez toma accesible, volumen y permiso de llenado.</li><li>No captar de ríos, "
            "pozas o embalses del lowveld; hay riesgo biológico y la captación puede no estar "
            "permitida.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Mlilwane Rest Camp",
                "cat": "Agua de servicio", "lat": -26.4927635, "lon": 31.1852261,
                "info": "[TOMA EN CAMPING; LLENADO CONDICIONADO] Parte de las parcelas tiene agua y el resto, una toma cercana. Acordar litros, manguera, coste y calidad; reserva con fauna, no contar con el perro.",
                "source": "https://biggameparks.org/img/cms/tabs/MLILWANE%20PRODUCT%20SHEET%20for%20Web.pdf",
            },
            {
                "name": "Agua de servicio · Ndlovu Camp (Hlane)",
                "cat": "Agua de servicio", "lat": -26.2596472, "lon": 31.8749574,
                "info": "[SOLO DUCHA Y FREGADO; SIN GRIFO EN PARCELA] Abluciones con agua caliente y cocina de campers. La ficha oficial niega tomas en el camping: no planificar llenado; reserva con fauna.",
                "source": "https://biggameparks.org/properties/hlane-royal-national-park",
            },
        ],
        "sources": [
            ["Mlilwane · ficha oficial de camping y agua", "https://biggameparks.org/img/cms/tabs/MLILWANE%20PRODUCT%20SHEET%20for%20Web.pdf"],
            ["Mlilwane · sitio oficial y acceso", "https://biggameparks.org/properties/mlilwane-wildlife-sanctuary"],
            ["Hlane · Ndlovu Camp y sus servicios", "https://biggameparks.org/properties/hlane-royal-national-park"],
        ],
    },
    "lesoto": {
        "intro": (
            "<h3>Agua de servicio: tres alojamientos físicos, ningún llenado automático</h3>"
            "<p>Se retira el pin regional Maseru–Butha-Buthe–Semonkong. Molengoane, Malealea "
            "y Semonkong admiten camping y publican duchas; solo Malealea declara además "
            "que su agua de grifo no debe beberse.</p>"
        ),
        "rows": [
            (
                "Molengoane Lodge, Nazareth · -29.404032, 27.783094",
                "<strong>Camping seguro con aseos, duchas y tomas eléctricas.</strong> La "
                "oficina de turismo también lo lista como pet-friendly. No publica toma para "
                "vehículo, volumen ni potabilidad. "
                + a("https://www.visitlesotho.org.ls/places-to-stay/molengoane-lodge", "turismo oficial")
                + " · " + gm(-29.4040318, 27.7830938),
                "Base de higiene cerca del eje de Maseru y candidata a carga concertada. "
                "Confirmar el perro, los dos vehículos, litros, conexión y tratamiento.",
            ),
            (
                "Malealea Lodge · -29.828006, 27.599906",
                "<strong>Camping con dos bloques compartidos; cada uno tiene dos duchas y "
                "dos aseos, más zona cubierta de fregado.</strong> La guía del huésped dice "
                "que no se beba del grifo y vende agua embotellada. "
                + a("https://www.malealealodge.com/pages/faqs-facilities-and-comfort/", "instalaciones oficiales")
                + " · " + a("https://www.malealealodge.com/pages/malealea-lodge-digital-guest-guide/", "calidad declarada")
                + " · " + gm(-29.8280062, 27.599906),
                "Buena parada de ducha y lavado. El agua de red solo sirve para usos no "
                "potables; pedir permiso antes de cualquier carga y tratar según destino.",
            ),
            (
                "Semonkong Lodge · -29.843003, 28.043450",
                "<strong>Camping para tiendas y campervans, con abluciones y duchas "
                "calientes; enchufes de 08:00 a 22:00.</strong> No publica grifo vehicular, "
                "llenado de depósitos ni potabilidad. "
                + a("https://www.semonkonglodge.com/accommodation-in-lesotho/", "camping oficial")
                + " · " + gm(-29.8430033, 28.0434498),
                "Parada de higiene en el interior. Reservar por su aforo reducido y confirmar "
                "vehículos, perro y recarga; no depender del río Maletsunyane.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Molengoane cubre el corredor de '
            "Maseru; Malealea, el suroeste; Semonkong, el interior. Los tres son alojamientos, "
            "no fuentes públicas.</li><li>Malealea es la advertencia más clara: el propio "
            "establecimiento prohíbe beber del grifo. La ducha o el fregado no convierten esa "
            "agua en potable.</li><li>Ninguna fuente autoriza una carga a granel. Contactar "
            "antes y llevar autonomía suficiente para completar y deshacer cada tramo si la "
            "respuesta es negativa o las tuberías están congeladas.</li><li>No extrapolar "
            "la calidad del agua que exporta el Lesotho Highlands Water Project a un arroyo "
            "superficial: hay ganado en las cuencas. Captar solo con permiso y aplicar "
            "filtración y desinfección completas.</li><li>En invierno, llenar por la tarde "
            "cuando funcione la instalación y proteger manguera, bomba y depósito frente a "
            "heladas nocturnas.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Molengoane Lodge (Nazareth)",
                "cat": "Agua de servicio", "lat": -29.4040318, "lon": 27.7830938,
                "info": "[SOLO DUCHA PUBLICADA; LLENADO CONDICIONADO] Camping seguro con duchas y electricidad; turismo oficial lo lista pet-friendly. Sin toma vehicular ni potabilidad publicadas.",
                "source": "https://www.visitlesotho.org.ls/places-to-stay/molengoane-lodge",
            },
            {
                "name": "Agua de servicio · Malealea Lodge",
                "cat": "Agua de servicio", "lat": -29.8280062, "lon": 27.599906,
                "info": "[DUCHA Y FREGADO; GRIFO NO POTABLE] Dos bloques de abluciones y zona de lavado. El lodge dice que no se beba del grifo; pactar cualquier carga y tratar el agua.",
                "source": "https://www.malealealodge.com/pages/malealea-lodge-digital-guest-guide/",
            },
            {
                "name": "Agua de servicio · Semonkong Lodge",
                "cat": "Agua de servicio", "lat": -29.8430033, "lon": 28.0434498,
                "info": "[SOLO DUCHA CALIENTE PUBLICADA] Camping para campervans con abluciones. No publica toma de llenado ni potabilidad; reservar y confirmar vehículos, perro y volumen.",
                "source": "https://www.semonkonglodge.com/accommodation-in-lesotho/",
            },
        ],
        "sources": [
            ["Visit Lesotho · Molengoane Lodge", "https://www.visitlesotho.org.ls/places-to-stay/molengoane-lodge"],
            ["Malealea Lodge · instalaciones del camping", "https://www.malealealodge.com/pages/faqs-facilities-and-comfort/"],
            ["Malealea Lodge · guía de agua para huéspedes", "https://www.malealealodge.com/pages/malealea-lodge-digital-guest-guide/"],
            ["Semonkong Lodge · camping y duchas", "https://www.semonkonglodge.com/accommodation-in-lesotho/"],
        ],
    },
}


TEXT_REPLACEMENTS = {
    "lesoto": {
        "Agua: los arroyos de altura son de las aguas más limpias del continente (es lo que el país vende a Sudáfrica), pero hay ganado por todas partes. Filtrar y potabilizar siempre.":
            "Agua: no extrapolar la calidad del agua del Lesotho Highlands Water Project a los arroyos superficiales. Hay ganado en las cuencas; captar solo con permiso y filtrar y potabilizar siempre.",
    },
}


def fuel_from(old: str) -> str:
    start = old.find("<h3>Combustible</h3>")
    if start < 0:
        raise ValueError("No se encontró el bloque de combustible")
    end = old.find('<div class="callout', start)
    return old[start:] if end < 0 else old[start:end]


def is_old_water(point: object) -> bool:
    if not isinstance(point, dict):
        return False
    return "agua" in str(point.get("cat", "")).lower() or "agua" in str(point.get("name", "")).lower()


def deep_replace(value, replacements: dict[str, str]):
    if isinstance(value, str):
        for old, new in replacements.items():
            value = value.replace(old, new)
        return value
    if isinstance(value, list):
        return [deep_replace(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: deep_replace(item, replacements) for key, item in value.items()}
    return value


def update(slug: str, cfg: dict) -> None:
    path = FICHA / f"{slug}.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    for section in data["custom_sections"]:
        if section[0] == "agua-combustible":
            section[2] = cfg["intro"] + table(cfg["rows"]) + cfg["plan"] + fuel_from(section[2]) + COMMON
            break
    else:
        raise ValueError(f"{slug}: falta la sección agua-combustible")

    data["logistics"] = [p for p in data.get("logistics", []) if not is_old_water(p)] + cfg["points"]
    data = deep_replace(data, TEXT_REPLACEMENTS.get(slug, {}))

    existing = {tuple(item) for item in data.get("sources", []) if isinstance(item, list) and len(item) == 2}
    for source in cfg["sources"]:
        if tuple(source) not in existing:
            data.setdefault("sources", []).append(source)
            existing.add(tuple(source))

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{slug}: {len(cfg['points'])} puntos de agua exactos")


for country, config in WATER.items():
    update(country, config)

#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 9: Namibia."""

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
    "namibia": {
        "intro": (
            "<h3>Agua de servicio: seis bases físicas para un país árido</h3>"
            "<p>Se retiran dos pines regionales que agrupaban ciudades, parques y todo el "
            "noroeste. Las nuevas paradas acreditan ducha, fregado o agua corriente; ninguna "
            "se presenta como llenado automático.</p>"
        ),
        "rows": [
            (
                "UrbanCamp, Windhoek · -22.554544, 17.093142",
                "<strong>Admite motorhomes, camiones y caravanas; publica duchas calientes "
                "con agua de calidad potable y acepta perros bien educados.</strong> No "
                "publica grifo vehicular ni permiso para cargar a granel. "
                + a("https://urbancamp.net/contents/de/d16_FAQ.html", "preguntas oficiales")
                + " · " + gm(-22.5545439, 17.0931424),
                "Base urbana de higiene y candidata a recarga concertada. Confirmar por "
                "escrito litros, toma/manguera, coste, perro y aviso de calidad vigente.",
            ),
            (
                "Alte Brücke Resort, Swakopmund · -22.686379, 14.525428",
                "<strong>Treinta y seis parcelas; cada una con baño privado, lavamanos y "
                "electricidad.</strong> La web no acredita potabilidad ni autorización para "
                "llenar depósitos. "
                + a("https://altebrucke.com/camp-caravan/", "camping oficial")
                + " · " + gm(-22.6863787, 14.5254276),
                "Parada fiable de ducha y lavado en la costa. Reservar y negociar aparte "
                "cualquier volumen para el vehículo y la admisión del perro.",
            ),
            (
                "Sossus Oasis Camp Site, Sesriem · -24.491027, 15.803219",
                "<strong>Cada parcela tiene aseo, ducha solar, fregadero de cocina y "
                "electricidad.</strong> No publica calidad sanitaria ni carga de grandes "
                "depósitos; está en pleno Namib. "
                + a("https://www.sossus-oasis.com/camping.html", "camping oficial")
                + " · " + gm(-24.491027, 15.803219),
                "Higiene antes o después de Sossusvlei. Solicitar litros con la reserva y "
                "entrar igualmente con autonomía desde una base confirmada.",
            ),
            (
                "Etosha Trading Post Campsite · -19.387927, 15.935381",
                "<strong>Agua corriente, ducha, lavamanos y zona de fregado en las parcelas "
                "individuales; los grupos también tienen suministro.</strong> No publica "
                "potabilidad ni permiso de llenado. "
                + a("https://www.etosha-tradingpost.com/downloads/EtoshaTradingPost_factsheet.pdf", "ficha oficial")
                + " · " + gm(-19.3879271, 15.9353813),
                "Primera candidata para pactar carga antes de Etosha, fuera de la puerta. "
                "Confirmar volumen, conexión, tratamiento, perro y restricciones del día.",
            ),
            (
                "Palmwag Campsite · -19.887162, 13.937520",
                "<strong>Parcela para un camper o dos 4x4, con lavamanos, electricidad y "
                "abluciones con agua caliente y fría.</strong> La ficha operativa dice que "
                "no admite mascotas; elefantes cruzan el camping abierto. "
                + a("https://gondwana-collection.com/accommodation/palmwag-campsite", "camping oficial")
                + " · " + gm(-19.8871616, 13.9375198),
                "Ducha y fregado durante una reserva. No usar como carga sin autorización; "
                "plan B obligatorio para el perro y máxima prudencia nocturna.",
            ),
            (
                "Opuwo Country Lodge · -18.044589, 13.833410",
                "<strong>Once parcelas valladas, cada una con ducha privada de agua caliente "
                "y fría, aseo, lavamanos, cocina con fregadero y electricidad.</strong> No "
                "publica potabilidad ni autorización de carga. "
                + a("https://www.opuwolodge.com/", "alojamiento oficial")
                + " · " + gm(-18.0445893, 13.8334102),
                "Principal candidata antes o después del Kaokoland. Reservar y pactar la "
                "carga completa de ambos coches; confirmar perro, calidad y posibles límites.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>UrbanCamp cubre Windhoek y '
            "Alte Brücke la costa; son las paradas urbanas para revisar, limpiar y rellenar "
            "solo si el alojamiento lo autoriza.</li><li>Sossus Oasis tiene agua para ducha "
            "y fregado en cada parcela, pero el Namib se planifica desde la recarga anterior: "
            "no llegar dependiendo de una respuesta en recepción.</li><li>Etosha Trading Post "
            "es el punto más claro antes de Andersson Gate porque publica agua corriente. "
            "Dentro de Etosha se usan las abluciones reservadas, sin convertir los camps de "
            "NWR en estaciones de carga.</li><li>Palmwag permite dos SUV por parcela y tiene "
            "agua caliente/fría, pero no admite mascotas y recibe elefantes. Opuwo es la "
            "base prioritaria para concertar la carga antes del Kaokoland.</li><li>Skeleton "
            "Coast, Messum, Van Zyl's Pass, Marienfluss y los campamentos del Cunene quedan "
            "sin pin de recarga. Entrar con agua para personas, perro, cocina, higiene, "
            "avería y retorno.</li><li>No captar del Cunene, pozas de Sesriem, waterholes ni "
            "ríos efímeros. Hay riesgo sanitario, fauna y restricciones de conservación; "
            "una emergencia exige autorización local y tratamiento completo.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · UrbanCamp (Windhoek)",
                "cat": "Agua de servicio", "lat": -22.5545439, "lon": 17.0931424,
                "info": "[DUCHA CALIENTE DE CALIDAD POTABLE; LLENADO CONDICIONADO] Admite camiones, motorhomes y perros educados. Sin grifo vehicular ni carga publicada: pactar litros, toma y coste.",
                "source": "https://urbancamp.net/contents/de/d16_FAQ.html",
            },
            {
                "name": "Agua de servicio · Alte Brücke (Swakopmund)",
                "cat": "Agua de servicio", "lat": -22.6863787, "lon": 14.5254276,
                "info": "[SOLO DUCHA Y LAVAMANOS PUBLICADOS] Cada parcela tiene baño privado y electricidad. Sin potabilidad ni llenado acreditados; confirmar volumen, toma, coste y perro.",
                "source": "https://altebrucke.com/camp-caravan/",
            },
            {
                "name": "Agua de servicio · Sossus Oasis (Sesriem)",
                "cat": "Agua de servicio", "lat": -24.491027, "lon": 15.803219,
                "info": "[DUCHA Y FREGADO EN PARCELA; LLENADO CONDICIONADO] Aseo, ducha solar y fregadero propios. Sin potabilidad ni volumen publicados; reservar y entrar con autonomía.",
                "source": "https://www.sossus-oasis.com/camping.html",
            },
            {
                "name": "Agua de servicio · Etosha Trading Post",
                "cat": "Agua de servicio", "lat": -19.3879271, "lon": 15.9353813,
                "info": "[AGUA CORRIENTE EN PARCELA; LLENADO CONDICIONADO] Ducha, lavamanos y fregado junto a Andersson Gate. Pactar litros, manguera, coste, tratamiento y perro.",
                "source": "https://www.etosha-tradingpost.com/downloads/EtoshaTradingPost_factsheet.pdf",
            },
            {
                "name": "Agua de servicio · Palmwag Campsite",
                "cat": "Agua de servicio", "lat": -19.8871616, "lon": 13.9375198,
                "info": "[DUCHA Y LAVAMANOS; NO MASCOTAS] Parcela para dos SUV con agua caliente/fría. Sin llenado publicado; elefantes cruzan el camping: no improvisar ni dejar comida fuera.",
                "source": "https://gondwana-collection.com/accommodation/palmwag-campsite",
            },
            {
                "name": "Agua de servicio · Opuwo Country Lodge",
                "cat": "Agua de servicio", "lat": -18.0445893, "lon": 13.8334102,
                "info": "[AGUA CALIENTE/FRÍA Y FREGADERO; LLENADO CONDICIONADO] Parcela vallada con baño y cocina. Mejor candidata antes de Kaokoland; pactar ambos coches, calidad, coste y perro.",
                "source": "https://www.opuwolodge.com/",
            },
        ],
        "sources": [
            ["UrbanCamp · vehículos, duchas y mascotas", "https://urbancamp.net/contents/de/d16_FAQ.html"],
            ["Alte Brücke · camping y baños privados", "https://altebrucke.com/camp-caravan/"],
            ["Sossus Oasis · servicios de cada parcela", "https://www.sossus-oasis.com/camping.html"],
            ["Etosha Trading Post · ficha de agua corriente", "https://www.etosha-tradingpost.com/downloads/EtoshaTradingPost_factsheet.pdf"],
            ["Palmwag · camping, agua y capacidad", "https://gondwana-collection.com/accommodation/palmwag-campsite"],
            ["Opuwo Country Lodge · instalaciones de camping", "https://www.opuwolodge.com/"],
        ],
    },
}


TEXT_REPLACEMENTS = {
    "namibia": {
        "No dar por auditada la potabilidad urbana ni el agua de campings. Para beber, usar una fuente confirmada o tratarla; para ducha y lavado, verificar acceso, conexión, coste y permiso antes de planificar la recarga.":
            "La auditoría acredita instalaciones concretas, no una potabilidad urbana general ni permiso automático para llenar. Para beber, exigir confirmación local vigente o tratar; para ducha y lavado, acordar acceso, conexión, coste y volumen.",
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

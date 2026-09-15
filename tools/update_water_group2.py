#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 2.

Elimina referencias urbanas genéricas y conserva solo instalaciones físicas con
coordenadas y alcance documentados. El bloque de combustible no se modifica.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FICHA = ROOT / "content" / "ficha"


COMMON = (
    '<div class="callout warn"><div class="callout-title">Regla operativa</div>'
    '<p><strong>Agua de servicio no significa agua potable.</strong> Para beber y cocinar, '
    'usar agua sellada o aplicar el tratamiento completo del vehículo. Una instalación '
    'con duchas no autoriza por sí sola a llenar el depósito: pedir permiso, confirmar '
    'caudal y precio el mismo día y llevar garrafa, manguera, adaptadores y bomba.</p></div>'
    '<div class="callout"><div class="callout-title">Criterio común del proyecto</div>'
    '<p>Estados, reservas, higiene del depósito y protocolo de potabilización: ver '
    '<a href="../../documentacion/#agua-combustible">Documentación general · agua y combustible</a>.</p></div>'
)


def a(url: str, label: str) -> str:
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


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
    "guinea": {
        "intro": (
            "<h3>Agua de servicio: tres puntos físicos, no ciudades enteras</h3>"
            "<p>Se retiran los pines representativos de Conakry y del Fouta Djallon y la promesa "
            "genérica de manguera en hoteles, misiones o gasolineras. Los apoyos aceptados son estos:</p>"
        ),
        "rows": [
            (
                "Woro Ladia, Conakry · 9.600400, -13.649970",
                "<strong>Solo ducha; llenado no acreditado.</strong> La ficha reciente confirma agua no potable, "
                "duchas calientes y espacio para dos 4x4, pero no para vehículos grandes. "
                + a("https://ioverlander.com/places/267424-woro-laida", "ficha y coordenadas"),
                "Reservar y usar como base de ducha. El depósito solo con autorización expresa; no bloquear el patio con los dos coches.",
            ),
            (
                "Tinka Eco Village, Dalaba · 10.691200, -12.251600",
                "<strong>Toma de agua reportada en abril de 2026.</strong> Un viajero pudo tomar agua y lavar ropa; "
                "también constan duchas, aparcamiento amplio y vaciado de negras, pero no de grises. "
                + a("https://park4night.com/de/place/672219", "ficha reciente")
                + " · "
                + a("https://tinkaecovillage.com/", "web del establecimiento"),
                "Anclaje del Fouta: consumir en el restaurante, pedir cantidad y punto de toma y tratar el agua de bebida. No admite mascotas según la ficha camper.",
            ),
            (
                "Grifo junto a la N5, Téguéréya · 10.611800, -12.191100",
                "<strong>Recarga de depósito publicada.</strong> Grifo gratuito junto a una gasolinera, descrito "
                "expresamente como no potable y apto para depósitos; todavía no tiene historial de reseñas. "
                + a("https://park4night.com/en/place/582309", "ficha y GPS"),
                "Verificar que sigue operativo, no obstaculizar la estación y usar solo para servicio. Tinka queda a unos kilómetros como respaldo.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Conakry aporta ducha, no una recarga garantizada; '
            "llegar a Dalaba con margen.</li><li>Tinka y Téguéréya forman el par operativo del Fouta: comprobar ambos "
            "antes de continuar a Sierra Leona.</li><li>Kankan, Nzérékoré y la pista de Tougué quedan sin pin: "
            "no se encontró una toma pública actual y exacta que justifique prometerla.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Woro Ladia (Conakry)",
                "cat": "Agua de servicio",
                "lat": 9.6004,
                "lon": -13.64997,
                "info": "[SOLO DUCHA] Agua no potable y duchas calientes verificadas; patio para dos 4x4, no grandes. El llenado del depósito no está acreditado: reservar y pedir permiso expreso.",
                "source": "https://ioverlander.com/places/267424-woro-laida",
            },
            {
                "name": "Agua de servicio · Tinka Eco Village (Dalaba)",
                "cat": "Agua de servicio",
                "lat": 10.6912,
                "lon": -12.2516,
                "info": "[TOMA REPORTADA EN 2026] Viajeros alojados pudieron tomar agua y lavar ropa; aparcamiento amplio. Pedir cantidad y punto de toma, tratar para consumo y recordar que la ficha indica que no admite mascotas.",
                "source": "https://park4night.com/de/place/672219",
            },
            {
                "name": "Agua de servicio · grifo N5 (Téguéréya)",
                "cat": "Agua de servicio",
                "lat": 10.6118,
                "lon": -12.1911,
                "info": "[RECARGA DE DEPÓSITO PUBLICADA] Grifo gratuito junto a gasolinera; agua expresamente no potable. Punto nuevo sin historial: comprobar funcionamiento y llenar sin obstaculizar.",
                "source": "https://park4night.com/en/place/582309",
            },
        ],
        "sources": [
            ["iOverlander · Woro Ladia, Conakry", "https://ioverlander.com/places/267424-woro-laida"],
            ["park4night · Tinka Eco Village, Dalaba", "https://park4night.com/de/place/672219"],
            ["Tinka Eco Village · web oficial", "https://tinkaecovillage.com/"],
            ["park4night · grifo N5 de Téguéréya", "https://park4night.com/en/place/582309"],
        ],
    },
    "sierra-leona": {
        "intro": (
            "<h3>Agua de servicio: cobertura escasa y sin falsas recargas</h3>"
            "<p>No se ha encontrado una recarga pública de depósito, actual y geolocalizada, que cubra el país. "
            "Se eliminan los dos pines genéricos y se conservan únicamente dos instalaciones útiles para higiene y agua de huéspedes.</p>"
        ),
        "rows": [
            (
                "Bureh Beach Surf Club · 8.207200, -13.155700",
                "<strong>Solo ducha básica.</strong> La ficha del camping registra aseos y una reseña que confirma ducha, "
                "pero no enumera toma de agua ni recarga de depósito. "
                + a("https://park4night.com/en/place/97969", "ficha y GPS")
                + " · "
                + a("https://tourismsierraleone.com/attractions/bureh-beach/", "lugar oficial"),
                "Útil para ducharse durante la parada costera. Llegar con agua propia y no pedir más alcance al punto del que acredita la fuente.",
            ),
            (
                "Campamento de Tiwai Island · 7.554150, -11.355367",
                "<strong>Agua y baños para huéspedes.</strong> La web oficial ofrece acceso a agua, baños y agua purificada "
                "gratuita para huéspedes; el acceso final es en barca y el vehículo queda fuera de la isla. "
                + a("https://www.tiwaiisland.org/visit/accommodation-and-food/", "servicios y contacto"),
                "Sirve para higiene y consumo durante la estancia, no para acercar el 4x4 ni llenar su depósito. Reservar y entrar al desvío con autonomía completa.",
            ),
            (
                "Red urbana de SALWACO · sin pin",
                "<strong>No equivale a acceso overlander.</strong> La empresa pública gestiona suministro entubado en ciudades "
                "como Bo, Kenema y Makeni, pero no publica tomas para vehículos. "
                + a("https://salwaco.gov.sl/about-salwaco/", "operador público"),
                "Concertar por escrito con un alojamiento vallado una cantidad concreta; no marcar el centro de una ciudad como si fuera un grifo.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Completar en Dalaba/Téguéréya antes de entrar y llevar '
            "autonomía suficiente para atravesar Sierra Leona si falla una cita privada.</li><li>Para Freetown, Bo, Kenema, "
            "Makeni o Kabala: reservar alojamiento 24–48 h antes y pedir por escrito acceso del coche, litros, recipiente/manguera "
            "y precio.</li><li>Outamba obtiene agua del río y no se acepta como recarga ordinaria; Tiwai tampoco repone el vehículo.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Bureh Beach Surf Club",
                "cat": "Agua de servicio",
                "lat": 8.2072,
                "lon": -13.1557,
                "info": "[SOLO DUCHA BÁSICA] Aseos y ducha documentados; la fuente no ofrece toma ni llenado de depósito. Llegar con reserva y usarlo únicamente para higiene durante la parada.",
                "source": "https://park4night.com/en/place/97969",
            },
            {
                "name": "Agua de servicio · campamento de Tiwai Island",
                "cat": "Agua de servicio",
                "lat": 7.55415,
                "lon": -11.3553667,
                "info": "[AGUA PARA HUÉSPEDES; NO PARA EL VEHÍCULO] Web oficial: acceso a agua, baños y agua purificada gratis. El 4x4 queda en tierra firme y el tramo final es en barca; no es una recarga del depósito.",
                "source": "https://www.tiwaiisland.org/visit/accommodation-and-food/",
            },
        ],
        "sources": [
            ["park4night · Bureh Beach Surf Club", "https://park4night.com/en/place/97969"],
            ["Ministerio de Turismo · Bureh Beach", "https://tourismsierraleone.com/attractions/bureh-beach/"],
            ["Tiwai Island · alojamiento, agua y contacto", "https://www.tiwaiisland.org/visit/accommodation-and-food/"],
            ["SALWACO · cobertura del operador público", "https://salwaco.gov.sl/about-salwaco/"],
        ],
    },
    "liberia": {
        "intro": (
            "<h3>Agua de servicio: dos instalaciones verificables</h3>"
            "<p>Se retiran los pines genéricos de Monrovia y Sapo. La lluvia abundante, un hotel o un río no son por sí solos "
            "una recarga segura; los únicos apoyos que superan el corte documental son estos:</p>"
        ),
        "rows": [
            (
                "Robertsport Surf Club Beach · 6.752200, -11.379900",
                "<strong>Duchas y pozo; llenado condicionado.</strong> El proyecto publica torre, pozo, baños y plataformas "
                "de camping; reseñas de 2026 confirman duchas limpias. No consta recarga de depósito. "
                + a("https://www.universaloutreachfoundation.org/surf-tourism", "instalaciones del proyecto")
                + " · "
                + a("https://park4night.com/en/place/473020", "estado y GPS"),
                "Pedir permiso y cantidad antes de sacar manguera. Acceso final de arena para 4x4; no apto para camiones según la ficha.",
            ),
            (
                "Kpatawee Waterfalls Ecolodge · 7.122365, -9.640770",
                "<strong>Duchas y agua para clientes; llenado condicionado.</strong> El operador ofrece camping, aparcamiento "
                "seguro y duchas en sus alojamientos. La web no promete una toma para vehículos. "
                + a("https://www.kpataweewaterfalls.com/", "web y reservas"),
                "Reservar y solicitar por escrito litros y método. Los campers estacionan alejados de la cascada; no captar de las pozas para el circuito.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Robertsport es una parada de ducha y una posible recarga '
            "previa autorización, no un grifo libre.</li><li>Monrovia, Ganta, Greenville, Zwedru y Harper quedan sin pin de agua: "
            "las fuentes localizadas prueban duchas o suministro del alojamiento, no llenado del coche ni una toma exacta estable.</li>"
            "<li>Para el sureste, concertar el llenado en un recinto seguro antes de salir y llevar reserva redundante. "
            "La captación de lluvia limpia y tratada es contingencia, no el plan principal.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Robertsport Surf Club Beach",
                "cat": "Agua de servicio",
                "lat": 6.7522,
                "lon": -11.3799,
                "info": "[DUCHAS; LLENADO CONDICIONAL] Torre, pozo, baños y camping publicados; reseñas de 2026 confirman duchas. Pedir permiso y litros: no consta una recarga libre. Acceso final de arena para 4x4.",
                "source": "https://www.universaloutreachfoundation.org/surf-tourism",
            },
            {
                "name": "Agua de servicio · Kpatawee Waterfalls Ecolodge",
                "cat": "Agua de servicio",
                "lat": 7.1223645,
                "lon": -9.6407703,
                "info": "[DUCHAS; LLENADO CONDICIONAL] Ecolodge activo con camping, aparcamiento seguro y duchas; reservar y acordar litros y método. No captar de la cascada para el depósito.",
                "source": "https://www.kpataweewaterfalls.com/",
            },
        ],
        "sources": [
            ["Universal Outreach · instalaciones de Robertsport Surf Club", "https://www.universaloutreachfoundation.org/surf-tourism"],
            ["park4night · Robertsport Surf Club Beach", "https://park4night.com/en/place/473020"],
            ["Liberia Tourism · Robertsport", "https://enjoyliberia.travel/pages/robertsport/"],
            ["Kpatawee Waterfalls Ecolodge · servicios y reservas", "https://www.kpataweewaterfalls.com/"],
        ],
    },
    "costa-de-marfil": {
        "intro": (
            "<h3>Agua de servicio: apoyos costeros de alcance limitado</h3>"
            "<p>Se elimina el pin genérico de Abiyán y la afirmación de que cadenas enteras de gasolineras y hoteles "
            "permiten llenar con manguera. Los puntos exactos localizados sirven sobre todo para ducha y garrafas:</p>"
        ),
        "rows": [
            (
                "Anunu Eco Surf Camp, Vodiéko · 4.918200, -6.144100",
                "<strong>Grifo y ducha; llenado condicionado.</strong> El camping publica un grifo, ducha artesanal, "
                "aseo, acceso 4x4 y apertura anual; no tiene reseñas que confirmen volumen o manguera. "
                + a("https://park4night.com/fr/place/473078", "ficha y GPS"),
                "Llamar antes y pedir litros. Aceptarlo como toma para garrafas; no como depósito completo hasta confirmación local.",
            ),
            (
                "Chez Raymond et Perico, Lateko · 4.906600, -6.164700",
                "<strong>Solo ducha de cubo.</strong> Dos reseñas, una de diciembre de 2025, mantienen activo el camping; "
                "la descripción especifica ducha y WC con cubo. "
                + a("https://park4night.com/fr/place/394571", "ficha y comentarios"),
                "Útil para higiene y una noche costera. El llenado del vehículo no está acreditado: llegar con reserva.",
            ),
            (
                "Green Land / 4x4 Garage CI, Yaou · 5.176300, -3.619100",
                "<strong>Solo agua transportada para ducha.</strong> La ficha declara expresamente que no hay agua corriente "
                "y que el vigilante lleva agua para ducha y baño. "
                + a("https://park4night.com/fr/place/474289", "ficha y GPS"),
                "No usarlo como recarga. Es un apoyo de higiene al este de Abiyán y debe contactarse a través del taller antes de ir.",
            ),
        ],
        "plan": (
            '<h3>Descartes y plan de tramo</h3><ul class="ticks"><li>Hotel Excellence de Danané no se incorpora: '
            "su ficha de 2019 no aporta una confirmación reciente de llenado.</li><li>Anunu es la única toma física publicada, "
            "pero el volumen sigue condicionado. Lateko y Green Land son solo ducha.</li><li>Para Abiyán, Yamoussoukro, Bouaké, "
            "Man o Korhogo: comprar agua sellada para beber y concertar una recarga privada antes de entrar en los bloques "
            "de Taï o Séguéla–Sipilou; ninguna ciudad se representa ya mediante un pin ficticio.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Anunu Eco Surf Camp",
                "cat": "Agua de servicio",
                "lat": 4.9182,
                "lon": -6.1441,
                "info": "[TOMA PARA GARRAFAS; DEPÓSITO CONDICIONAL] Camping con grifo y ducha artesanal publicados. No hay reseñas que acrediten volumen o manguera: llamar, pedir litros y tratar para consumo.",
                "source": "https://park4night.com/fr/place/473078",
            },
            {
                "name": "Agua de servicio · Chez Raymond et Perico (Lateko)",
                "cat": "Agua de servicio",
                "lat": 4.9066,
                "lon": -6.1647,
                "info": "[SOLO DUCHA DE CUBO] Camping activo con reseña de diciembre de 2025. Ducha y WC funcionan con cubo; no consta llenado del vehículo. Llegar con reserva.",
                "source": "https://park4night.com/fr/place/394571",
            },
            {
                "name": "Agua de servicio · Green Land / 4x4 Garage CI (Yaou)",
                "cat": "Agua de servicio",
                "lat": 5.1763,
                "lon": -3.6191,
                "info": "[SOLO DUCHA; SIN AGUA CORRIENTE] El vigilante transporta agua para ducha y baño. No es una recarga. Contactar previamente con 4x4 Garage CI en Abiyán.",
                "source": "https://park4night.com/fr/place/474289",
            },
        ],
        "sources": [
            ["park4night · Anunu Eco Surf Camp", "https://park4night.com/fr/place/473078"],
            ["park4night · Chez Raymond et Perico, Lateko", "https://park4night.com/fr/place/394571"],
            ["park4night · Green Land / 4x4 Garage CI", "https://park4night.com/fr/place/474289"],
            ["park4night · Hotel Excellence, Danané (descartado)", "https://park4night.com/fr/place/165257"],
        ],
    },
}


def fuel_from(old: str) -> str:
    start = old.find("<h3>Combustible</h3>")
    if start < 0:
        raise ValueError("No se encontró el bloque de combustible")
    end = old.find('<div class="callout', start)
    return old[start:] if end < 0 else old[start:end]


def is_old_water(point: dict) -> bool:
    return "agua" in str(point.get("cat", "")).lower() or "agua" in str(point.get("name", "")).lower()


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
    existing = {tuple(item) for item in data.get("sources", []) if isinstance(item, list) and len(item) == 2}
    for source in cfg["sources"]:
        if tuple(source) not in existing:
            data.setdefault("sources", []).append(source)
            existing.add(tuple(source))

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{slug}: {len(cfg['points'])} puntos de agua exactos")


for country, config in WATER.items():
    update(country, config)

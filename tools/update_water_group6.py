#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 6.

Sustituye zonas genéricas por instalaciones físicas, distingue ducha de
llenado y corrige afirmaciones sanitarias falsas sobre lagos de la región.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FICHA = ROOT / "content" / "ficha"

COMMON = (
    '<div class="callout warn"><div class="callout-title">Regla operativa</div>'
    '<p><strong>Agua de servicio no significa agua potable.</strong> Una ducha no equivale '
    'a una toma para el vehículo. Antes de '
    'desviarse hay que confirmar fecha, litros, toma, precio, calidad y acceso de los '
    'dos 4x4. El agua de lagos, ríos y manantiales no entra en el depósito como '
    'operación ordinaria. Para beber y cocinar: agua sellada o tratamiento completo.</p></div>'
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
    "uganda": {
        "intro": (
            "<h3>Agua de servicio: una toma en parcela y una ducha occidental</h3>"
            "<p>Se retiran Kampala, Entebbe, Jinja, Fort Portal, Bunyonyi y Buhoma como "
            "supuestos grifos colectivos. Adrift acredita agua en la propia bahía de camión; "
            "Kluges acredita camping y abluciones, pero no llenado.</p>"
        ),
        "rows": [
            (
                "Adrift Overland Camp, Jinja · 0.594448, 33.052454",
                "<strong>Agua corriente y electricidad en seis bahías para camiones y camper, "
                "más duchas calientes.</strong> Es la única instalación del grupo que publica "
                "agua en la propia plaza del vehículo. No publica potabilidad, caudal ni permiso "
                "para llenar dos depósitos. "
                + a("https://www.adrift.ug/accommodation/adrift-overland-camp/", "servicios oficiales")
                + " · " + gm(0.594448, 33.052454),
                "Primera opción para concertar la recarga ugandesa. Reservar bahía y obtener "
                "por escrito litros, conexión, coste y política del perro; tratar el agua.",
            ),
            (
                "Kluges Guest Farm, Fort Portal · 0.594478, 30.250206",
                "<strong>Camping para grandes vehículos, duchas solares y zona de lavado; sin "
                "llenado publicado.</strong> La web oficial mantiene el camping y Google Maps "
                "sitúa la instalación real en Kabahango. Maps indica que no admite mascotas. "
                + a("https://klugesguestfarm.com/", "establecimiento oficial")
                + " · " + gm(0.5944781, 30.2502064),
                "Apoyo de higiene del corredor occidental solo cuando el perro tenga plan B. "
                "No contar con litros para el coche salvo autorización previa.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Adrift es el punto prioritario porque '
            "el agua llega a la bahía del vehículo; aun así, se reserva y se pacta el volumen.</li>"
            "<li>Kidepo, Bwindi, Bunyonyi y los lagos de cráter quedan sin recarga exacta. Resolver "
            "el volumen antes del desvío y conservar margen de retorno.</li><li>No usar Bunyonyi "
            "como fuente ni zona de baño supuestamente segura: hay literatura que documenta "
            "transmisión a gran altitud y caracoles compatibles.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Adrift Overland Camp (Jinja)",
                "cat": "Agua de servicio", "lat": 0.594448, "lon": 33.052454,
                "info": "[AGUA EN BAHÍA Y DUCHA; LLENADO CONDICIONADO] Seis plazas para camión/camper con agua corriente y electricidad. Reservar y acordar litros, conexión, coste y perro; no consta potabilidad.",
                "source": "https://www.adrift.ug/accommodation/adrift-overland-camp/",
            },
            {
                "name": "Agua de servicio · Kluges Guest Farm (Fort Portal)",
                "cat": "Agua de servicio", "lat": 0.5944781, "lon": 30.2502064,
                "info": "[SOLO DUCHA; PERRO NO ADMITIDO EN MAPS] Camping para vehículos grandes con abluciones y zona de lavado. No publica llenado; confirmar antes de desviarse.",
                "source": "https://klugesguestfarm.com/",
            },
        ],
        "sources": [
            ["Adrift Overland Camp · servicios oficiales", "https://www.adrift.ug/accommodation/adrift-overland-camp/"],
            ["Kluges Guest Farm · sitio oficial", "https://klugesguestfarm.com/"],
            ["Estudio · esquistosomiasis a gran altitud en Uganda", "https://pmc.ncbi.nlm.nih.gov/articles/PMC5292801/"],
        ],
    },
    "ruanda": {
        "intro": (
            "<h3>Agua de servicio: dos duchas reales, ningún llenado acreditado</h3>"
            "<p>Se eliminan las ciudades y toda la orilla del Kivu como supuesto servicio de "
            "manguera. Red Rocks acredita ducha; Imuhira admite vehículos de camping y ofrece "
            "ducha sencilla. Ninguno publica una toma para depósitos.</p>"
        ),
        "rows": [
            (
                "Red Rocks Base Camp, Musanze · -1.560308, 29.636233",
                "<strong>Camping actual con baños compartidos y duchas calientes.</strong> La "
                "página oficial publica parcelas y más de veinte tiendas, pero no confirma "
                "espacio para dos 4x4 ni llenado. "
                + a("https://www.redrocksrwanda.com/accommodation/", "alojamiento oficial")
                + " · " + gm(-1.5603078, 29.6362333),
                "Ducha de la zona de Volcanes. Confirmar antes acceso de los coches y del perro; "
                "no atribuir al camping una manguera que no publica.",
            ),
            (
                "Imuhira Camp & CBT, Kagano · -2.353379, 29.080959",
                "<strong>Camping para vehículos y ducha fría, con cubo caliente a petición.</strong> "
                "La web actual lo orienta a overlanders y vehículos; no ofrece llenado y su "
                "sistema sencillo obliga a limitar el consumo. "
                + a("https://www.imuhirecotourism.rw/", "servicios oficiales")
                + " · " + gm(-2.3533786, 29.0809588),
                "Parada de higiene entre Karongi y Rusizi. Reservar y no pedir volumen para el "
                "coche sin acuerdo expreso; confirmar perro y acceso en lluvias.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Ruanda queda sin recarga vehicular '
            "publicada. Para llenar, concertar una toma privada en Kigali o Musanze antes de salir, "
            "con volumen y calidad confirmados.</li><li>Red Rocks e Imuhira resuelven ducha durante "
            "la estancia, no autonomía del depósito.</li><li>Se retira la afirmación de que el Kivu "
            "no tiene bilharzia: hay infecciones publicadas tras una sola exposición en su orilla "
            "ruandesa. No nadar ni captar agua cruda.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Red Rocks Base Camp (Musanze)",
                "cat": "Agua de servicio", "lat": -1.5603078, "lon": 29.6362333,
                "info": "[SOLO DUCHA; ACCESO 4X4 POR CONFIRMAR] Camping actual con duchas calientes. No publica llenado ni confirma espacio para dos vehículos; reservar.",
                "source": "https://www.redrocksrwanda.com/accommodation/",
            },
            {
                "name": "Agua de servicio · Imuhira Camp & CBT (Kagano)",
                "cat": "Agua de servicio", "lat": -2.3533786, "lon": 29.0809588,
                "info": "[SOLO DUCHA; VEHÍCULOS ADMITIDOS] Camping para overlanders con ducha fría y cubo caliente a petición. Sin llenado publicado; consumo contenido.",
                "source": "https://www.imuhirecotourism.rw/",
            },
        ],
        "sources": [
            ["Red Rocks Rwanda · alojamiento oficial", "https://www.redrocksrwanda.com/accommodation/"],
            ["Imuhira Camp & CBT · sitio oficial", "https://www.imuhirecotourism.rw/"],
            ["Frontiers 2024 · esquistosomiasis adquirida en el lago Kivu", "https://www.frontiersin.org/journals/tropical-diseases/articles/10.3389/fitd.2024.1354031/full"],
            ["CDC · salud del viajero en Ruanda", "https://wwwnc.cdc.gov/travel/destinations/traveler/none/rwanda"],
        ],
    },
    "malaui": {
        "intro": (
            "<h3>Agua de servicio: tres duchas del corredor, sin captar del lago</h3>"
            "<p>Se eliminan las tres ciudades y todos los campings lacustres como pines genéricos. "
            "Chitimba, Butterfly Space y Kuti son instalaciones reales para vehículos; ninguna "
            "autoriza de antemano llenar el depósito.</p>"
        ),
        "rows": [
            (
                "Chitimba Camp · -10.585098, 34.175657",
                "<strong>Camping para camiones overland y viajeros con vehículo; ducha caliente "
                "condicionada.</strong> El establecimiento avisa de que el agua caliente depende "
                "de electricidad y diésel. Maps indica mascotas, pero se confirma al reservar. "
                + a("https://camp018.wixsite.com/chitimbacamp", "camping oficial")
                + " · " + gm(-10.585098, 34.175657),
                "Primera ducha tras la frontera norte. Avisar con antelación; no esperar agua "
                "caliente ni llenado sin confirmación expresa.",
            ),
            (
                "Butterfly Space, Nkhata Bay · -11.612045, 34.305155",
                "<strong>Zona para overland trucks y tiendas de techo, duchas solares y agua "
                "filtrada para huéspedes.</strong> La gestión ecológica reutiliza el agua gris; "
                "no publica recarga de grandes depósitos. "
                + a("https://butterflyspacemalawi.com/the-lodge/", "servicios oficiales")
                + " · " + gm(-11.6120451, 34.3051549),
                "Buena base de higiene. Usar el agua filtrada solo como ofrece el alojamiento y "
                "pedir por separado cualquier litro para el vehículo; confirmar perro.",
            ),
            (
                "Kuti Camp, Salima · -13.706292, 34.428897",
                "<strong>Campsite con cocina y abluciones de agua caliente y fría.</strong> Malawi "
                "Tourism acredita camping y acceso self-drive dentro de una reserva. No publica "
                "llenado ni política de mascotas. "
                + a("https://www.malawitourism.com/regions/central-malawi/kuti-wildlife-reserve/kuti-camp/", "ficha turística oficial")
                + " · " + gm(-13.7062918, 34.4288973),
                "Ducha del corredor central. Confirmar dos 4x4 y perro antes de entrar en la "
                "reserva; no usarlo como grifo salvo permiso escrito.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Chitimba y Butterfly cubren el norte; '
            "Kuti, el centro. El sur y las mesetas siguen sin recarga exacta: concertarla en una "
            "base urbana antes de subir.</li><li>No captar del lago Malaui ni usarlo para lavar o "
            "ducharse: CDC documenta esquistosomiasis y recomienda evitar todo contacto con agua "
            "dulce no clorada.</li><li>La OMS registró un brote de cólera en 2025–2026. Toda agua "
            "no sellada se trata; una ducha del camping no acredita calidad de bebida.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Chitimba Camp",
                "cat": "Agua de servicio", "lat": -10.585098, "lon": 34.175657,
                "info": "[SOLO DUCHA; AGUA CALIENTE CONDICIONADA] Camping para overland trucks y vehículos propios. Reservar: el agua caliente depende de electricidad/diésel y no hay llenado publicado.",
                "source": "https://camp018.wixsite.com/chitimbacamp",
            },
            {
                "name": "Agua de servicio · Butterfly Space (Nkhata Bay)",
                "cat": "Agua de servicio", "lat": -11.6120451, "lon": 34.3051549,
                "info": "[DUCHA SOLAR; VEHÍCULOS OVERLAND] Zona para camiones y tiendas de techo, ducha caliente y agua filtrada de huéspedes. Sin recarga vehicular publicada; consumo ecológico.",
                "source": "https://butterflyspacemalawi.com/the-lodge/",
            },
            {
                "name": "Agua de servicio · Kuti Camp (Salima)",
                "cat": "Agua de servicio", "lat": -13.7062918, "lon": 34.4288973,
                "info": "[SOLO DUCHA; PERRO POR CONFIRMAR] Camping con abluciones de agua caliente/fría dentro de una reserva. No publica llenado; reservar acceso de los dos 4x4.",
                "source": "https://www.malawitourism.com/regions/central-malawi/kuti-wildlife-reserve/kuti-camp/",
            },
        ],
        "sources": [
            ["Chitimba Camp · sitio oficial", "https://camp018.wixsite.com/chitimbacamp"],
            ["Butterfly Space · alojamiento y camping", "https://butterflyspacemalawi.com/the-lodge/"],
            ["Malawi Tourism · Kuti Camp", "https://www.malawitourism.com/regions/central-malawi/kuti-wildlife-reserve/kuti-camp/"],
            ["CDC · salud del viajero en Malaui", "https://wwwnc.cdc.gov/travel/destinations/traveler/none/malawi"],
            ["OMS · brote de cólera de Malaui 2025–2026", "https://afro.who.int/photo-story/timely-vaccination-reinforces-malawis-cholera-outbreak-control"],
        ],
    },
}


TEXT_REPLACEMENTS = {
    "uganda": {
        "con baño en agua sin bilharzia. Uno de los mejores sitios del país para acampar.":
            "sin usar el agua del cráter para baño o depósito: hay transmisión documentada a cotas altas. Uno de los mejores sitios del país para acampar.",
        "sí es seguro en los lagos de cráter de Fort Portal y en Bunyonyi.":
            "tampoco debe considerarse segura el agua de los lagos de cráter ni de Bunyonyi sin una evaluación sanitaria local actual.",
        "Los lagos de cráter de Fort Portal y el Bunyonyi se consideran seguros, pero conviene confirmarlo en el momento.":
            "Hay transmisión documentada incluso a cotas altas y caracoles compatibles en Bunyonyi: evitar el contacto con agua dulce no tratada.",
    },
    "ruanda": {
        "La orilla del Kivu es una de las mejores zonas de todo el viaje para el animal: sin cocodrilos, sin hipopótamos y sin bilharzia documentada.":
            "La orilla del Kivu ofrece alojamientos, pero el riesgo documentado de esquistosomiasis obliga a impedir que el animal entre o beba del lago.",
        "sin cocodrilos, sin hipopótamos, sin bilharzia documentada y con campings junto al agua.":
            "con campings junto al agua, pero con riesgo de esquistosomiasis documentado: no se considera zona de baño segura.",
        "la pista del Kivu no atraviesa parque nacional, hay campings y hoteles junto al agua, y el Kivu no tiene cocodrilos ni hipopótamos ni bilharzia documentada, así que el perro puede bañarse.":
            "la pista del Kivu no atraviesa parque nacional y hay campings y hoteles, pero existe riesgo documentado de esquistosomiasis: el perro no debe bañarse.",
        "El lago Kivu es de los pocos grandes lagos africanos sin bilharzia documentada, sin cocodrilos y sin hipopótamos: se puede nadar.":
            "El lago Kivu tiene riesgo documentado de esquistosomiasis en su orilla ruandesa: no se considera seguro nadar ni usar agua cruda.",
        "la orilla del Kivu es una de las mejores zonas de todo el viaje para el animal: sin cocodrilos, sin hipopótamos y sin bilharzia documentada.":
            "la orilla del Kivu ofrece alojamientos, pero el riesgo documentado de esquistosomiasis obliga a impedir que el animal entre o beba del lago.",
        "campings y hoteles junto a la playa del Kivu, con posibilidad de bañarse.":
            "campings y hoteles junto al Kivu, pero sin considerar segura la inmersión por el riesgo documentado de esquistosomiasis.",
    },
    "malaui": {
        "BILHARZIA en todo el lago — dato crítico, todo el mundo se baña":
            "ESQUISTOSOMIASIS documentada en el lago — evitar todo contacto con agua dulce",
        "BILHARZIA (esquistosomiasis) EN TODO EL LAGO MALAUI, y este es el dato importante porque el lago es el motivo del viaje y todo el mundo se baña en él.":
            "BILHARZIA (esquistosomiasis) DOCUMENTADA EN EL LAGO MALAUI, un riesgo que condiciona la visita y obliga a evitar la exposición.",
        "Ver la sección de salud para el protocolo que sigue de hecho casi todo el mundo (bañarse y tratarse después con praziquantel) y decidirlo con Sanidad Exterior ANTES de salir.":
            "CDC recomienda evitar el contacto; tomar praziquantel después no es una medida preventiva fiable. Consultarlo con medicina del viajero ANTES de salir.",
        "Qué se hace en la práctica: la mayoría de viajeros de larga duración se baña y asume la exposición, y después se trata con praziquantel (dosis única según peso) pasadas unas semanas desde el último contacto con el agua, porque el tratamiento antes de que el parásito madure no es eficaz; alternativamente se hace serología unas semanas después. Esto NO es una recomendación médica: es el protocolo de hecho de los overlanders que pasan por el país. La decisión tiene que tomarse con Sanidad Exterior antes de salir de España, no improvisarse allí.":
            "Prevención: CDC recomienda evitar nadar, vadear, bañarse o lavar en agua dulce sin tratar. El praziquantel después de una exposición no se considera prevención fiable y no debe planificarse por cuenta propia; si ocurre contacto, consultar medicina del viajero para valoración y posible cribado.",
        "Qué se hace en la práctica: la mayoría de viajeros de larga duración se baña y asume la exposición, y después se trata con praziquantel (dosis única según peso) pasadas unas semanas desde el último contacto con el agua, porque el tratamiento antes de que el parásito madure no es eficaz; alternativamente se hace serología unas semanas después. Esto NO es una recomendación médica: es el protocolo que hay que consultar y cerrar con Sanidad Exterior o con un centro de medicina del viajero ANTES de salir de España, llevando el fármaco encima si así se decide.":
            "Prevención: CDC recomienda evitar nadar, vadear, bañarse o lavar en agua dulce sin tratar. El praziquantel después de una exposición no se considera prevención fiable y no debe planificarse por cuenta propia; si ocurre contacto, consultar medicina del viajero para valoración y posible cribado.",
        "Medidas que reducen el riesgo sin eliminarlo: evitar las orillas someras con juncos y con actividad humana, preferir agua profunda y alejada de la costa, salir y secarse enérgicamente con toalla, y no usar nunca agua del lago sin filtrar y tratar para beber o lavar los dientes.":
            "No existe una zona del lago que pueda darse por segura: profundidad, distancia a la costa y secarse con toalla no sustituyen evitar el contacto. No usar agua del lago para beber, lavarse, lavar dientes o llenar el vehículo.",
        "Cerrar con Sanidad Exterior o medicina del viajero el protocolo concreto (praziquantel preventivo tras exposición vs. serología posterior) y llevar la pauta por escrito antes de salir de España":
            "Evitar la exposición al agua dulce; si ocurre, consultar medicina del viajero sobre cribado y tratamiento. No planificar praziquantel preventivo por cuenta propia",
        "La actitud mayoritaria de los viajeros de larga duración es «báñate, disfruta y trátate después»: asumir la exposición y tomar praziquantel pasadas unas semanas, en lugar de renunciar al lago. No es consejo médico, pero explica por qué casi nadie se abstiene.":
            "El consejo sanitario vigente es evitar el contacto con agua dulce no clorada. Tomar praziquantel por cuenta propia después no sustituye la prevención ni una valoración médica si hubo exposición.",
        "Bilharzia:</strong> es el otro tema que sale en todos los relatos, porque todo el mundo se baña en el lago.":
            "Bilharzia:</strong> es un riesgo central del itinerario por el lago y debe explicarse sin normalizar la exposición.",
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

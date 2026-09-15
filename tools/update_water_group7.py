#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 7.

Sustituye ciudades y regiones genéricas por instalaciones físicas, separa
ducha de llenado y corrige generalizaciones sobre la red sudafricana.
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
    "zimbabue": {
        "intro": (
            "<h3>Agua de servicio: tres instalaciones reales del eje</h3>"
            "<p>Se retiran cinco ciudades, todos los campings de ZimParks y tres regiones "
            "remotas como si fueran grifos colectivos. Explorers Village y Big Cave "
            "acreditan higiene; Antelope Park publica tomas en el camping.</p>"
        ),
        "rows": [
            (
                "Shearwater Explorers Village, Victoria Falls · -17.924172, 25.841059",
                "<strong>Bahías diseñadas para camiones overland, duchas calientes y frías "
                "y zona de fregado.</strong> No publica toma para llenar un depósito ni "
                "potabilidad. "
                + a("https://explorersvillage.com/camping/", "camping oficial")
                + " · " + gm(-17.9241715, 25.8410587),
                "Parada de ducha al entrar o salir por Victoria Falls. Reservar bahía y "
                "preguntar por escrito por dos vehículos, perro y cualquier recarga.",
            ),
            (
                "Big Cave Camp, Matobo · -20.496369, 28.435008",
                "<strong>Aseos renovados, duchas privadas con agua caliente y fregadero de "
                "cocina.</strong> No aparece una toma para vehículos y Google Maps indica "
                "que no admite mascotas. "
                + a("https://www.bigcavematopos.com/campsite.html", "servicios oficiales")
                + " · " + gm(-20.4963688, 28.4350083),
                "Solo higiene durante una estancia y con plan B para el perro. No desviarse "
                "para llenar hasta obtener permiso y volumen confirmados.",
            ),
            (
                "Antelope Park, Gweru · -19.507381, 29.720279",
                "<strong>Tomas de agua en el camping, duchas calientes, fregado y lavandería; "
                "creado para overlanders.</strong> La toma existe, pero la web no autoriza "
                "grandes volúmenes ni acredita potabilidad. "
                + a("https://antelopepark.co.zw/guests/accommodation/camping-sites/", "camping oficial")
                + " · " + gm(-19.5073813, 29.7202794),
                "Primera opción de recarga concertada en el eje central. Reservar y pactar "
                "litros, conexión, coste, tratamiento y perro antes de llegar.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Antelope Park es el único punto '
            "del grupo que publica grifos en el camping; se usa como candidato, nunca como "
            "llenado automático.</li><li>Explorers Village cubre Victoria Falls y Big Cave, "
            "Matobo. Ambos resuelven ducha y lavado durante la estancia, no autonomía del "
            "vehículo.</li><li>ZimParks pide llevar agua de bebida al camping y diferencia "
            "campings con abluciones de bush camps sin ellas. Hwange, Mana Pools, Gonarezhou, "
            "Chizarira y Nyanga quedan sin pin de recarga: entrar cargados y confirmar cada "
            "campamento poco antes.</li><li>No captar de Zambeze, Kariba, Runde o Save por "
            "riesgo biológico y fauna; tampoco aproximarse a una orilla para llenar a mano.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Explorers Village (Victoria Falls)",
                "cat": "Agua de servicio", "lat": -17.9241715, "lon": 25.8410587,
                "info": "[SOLO DUCHA Y FREGADO; CAMIONES OVERLAND] Bahías para camiones y camper con duchas calientes/frías. No publica toma de llenado ni potabilidad; reservar y confirmar perro.",
                "source": "https://explorersvillage.com/camping/",
            },
            {
                "name": "Agua de servicio · Big Cave Camp (Matobo)",
                "cat": "Agua de servicio", "lat": -20.4963688, "lon": 28.4350083,
                "info": "[SOLO DUCHA; PERRO NO ADMITIDO EN MAPS] Aseos con agua caliente y fregadero. No publica toma para el vehículo; no usar como recarga sin autorización.",
                "source": "https://www.bigcavematopos.com/campsite.html",
            },
            {
                "name": "Agua de servicio · Antelope Park (Gweru)",
                "cat": "Agua de servicio", "lat": -19.5073813, "lon": 29.7202794,
                "info": "[TOMA EN CAMPING; LLENADO CONDICIONADO] Publica grifos, duchas calientes y zona de lavado para overlanders. Acordar litros, conexión, coste, tratamiento y perro.",
                "source": "https://antelopepark.co.zw/guests/accommodation/camping-sites/",
            },
        ],
        "sources": [
            ["Explorers Village · camping oficial", "https://explorersvillage.com/camping/"],
            ["Big Cave Camp · servicios del campsite", "https://www.bigcavematopos.com/campsite.html"],
            ["Antelope Park · instalaciones de camping", "https://antelopepark.co.zw/guests/accommodation/camping-sites/"],
            ["ZimParks · preguntas de reserva y servicios", "https://book.zimparks.org.zw/booking_faqs"],
        ],
    },
    "botsuana": {
        "intro": (
            "<h3>Agua de servicio: dos posibles tomas y una ducha restringida</h3>"
            "<p>Se eliminan Maun, Kasane y tres regiones remotas como marcadores genéricos. "
            "BOGA y El-Fari son campings físicos con agua corriente; Elephant Sands solo "
            "se conserva como ducha porque su agua llega desde un sondeo a 14 km.</p>"
        ),
        "rows": [
            (
                "BOGA Rest Camp, Maun · -19.941965, 23.507816",
                "<strong>Parcelas de camping con agua corriente y electricidad, duchas calientes "
                "y fregaderos.</strong> El servicio está publicado, pero no el llenado de "
                "depósitos, su caudal ni la potabilidad. "
                + a("https://bogarestcamp.co.bw/", "camping oficial")
                + " · " + gm(-19.941965, 23.5078156),
                "Base para concertar la carga antes de Moremi, CKGR o la variante oeste. "
                "Reservar y obtener volumen, toma, coste y perro por escrito.",
            ),
            (
                "El-Fari Camp, norte de Ghanzi · -21.358160, 22.135437",
                "<strong>Grifo en cada parcela y agua caliente y fría permanente en "
                "abluciones.</strong> Es la evidencia más fuerte del grupo para conectar una "
                "manguera; no se publica permiso de gran volumen ni potabilidad. "
                + a("https://elfari.co.za/", "camping oficial")
                + " · " + gm(-21.3581598, 22.1354372),
                "Punto prioritario antes o después del Kalahari Central. Concertar los litros "
                "de ambos coches y no llegar dependiendo de una autorización implícita.",
            ),
            (
                "Elephant Sands Lodge, eje Nata–Kasane · -19.749044, 26.071255",
                "<strong>Camping con duchas calientes, pero agua muy limitada.</strong> La "
                "propiedad la bombea a diario desde un sondeo situado a 14 km y corta el "
                "suministro de huéspedes a las 22:00 para priorizar a la fauna. "
                + a("https://elephantsandsbotswana.com/campsite", "camping oficial")
                + " · " + a("https://elephantsandsbotswana.com/conservation", "restricciones de agua")
                + " · " + gm(-19.7490438, 26.0712547),
                "Solo ducha contenida durante la estancia. No pedir llenado y no contar con "
                "ducha nocturna. Entorno sin valla: plan B obligatorio para el perro.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>BOGA sirve de base en Maun y '
            "El-Fari cubre Ghanzi; ambos se contactan antes de entrar en las reservas. "
            "El-Fari es la mejor toma publicada, pero sigue requiriendo permiso para el volumen.</li>"
            "<li>Elephant Sands no es una recarga: su limitación documentada convierte incluso "
            "la ducha en un consumo que debe moderarse.</li><li>No hay recarga de visitante "
            "auditada dentro de CKGR, Kubu, Baines' Baobabs o Gcwihaba. Salir con toda el agua "
            "desde Maun, El-Fari/Ghanzi, Rakops o Letlhakane según el acceso, más margen de "
            "retorno.</li><li>Ríos, canales y pans no se usan para depósito, lavado o ducha; "
            "pueden tener patógenos y fauna peligrosa.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · BOGA Rest Camp (Maun)",
                "cat": "Agua de servicio", "lat": -19.941965, "lon": 23.5078156,
                "info": "[AGUA CORRIENTE Y DUCHA; LLENADO CONDICIONADO] Parcela servida con agua, electricidad, ducha caliente y fregadero. Pactar litros, toma, coste, calidad y perro.",
                "source": "https://bogarestcamp.co.bw/",
            },
            {
                "name": "Agua de servicio · El-Fari Camp (Ghanzi)",
                "cat": "Agua de servicio", "lat": -21.3581598, "lon": 22.1354372,
                "info": "[GRIFO EN PARCELA; LLENADO CONDICIONADO] Cada campsite publica toma y las abluciones, agua caliente/fría. Confirmar grandes volúmenes, potabilidad, coste y perro.",
                "source": "https://elfari.co.za/",
            },
            {
                "name": "Agua de servicio · Elephant Sands (Nata–Kasane)",
                "cat": "Agua de servicio", "lat": -19.7490438, "lon": 26.0712547,
                "info": "[SOLO DUCHA; AGUA RESTRINGIDA] Ducha caliente, pero el agua se bombea desde 14 km y se corta a las 22:00. No pedir recarga; recinto sin valla y perro sin confirmar.",
                "source": "https://elephantsandsbotswana.com/conservation",
            },
        ],
        "sources": [
            ["BOGA Rest Camp · instalaciones oficiales", "https://bogarestcamp.co.bw/"],
            ["El-Fari Camp · agua y camping", "https://elfari.co.za/"],
            ["Elephant Sands · campsite", "https://elephantsandsbotswana.com/campsite"],
            ["Elephant Sands · abastecimiento y restricciones", "https://elephantsandsbotswana.com/conservation"],
        ],
    },
    "sudafrica": {
        "intro": (
            "<h3>Agua de servicio: cuatro bases, no una promesa nacional</h3>"
            "<p>Se elimina el marcador «todo el país» y la afirmación de que cualquier "
            "camping, taller o gasolinera permite llenar sin restricciones. La calidad de red "
            "se decide por sistema municipal y cada recarga requiere permiso.</p>"
        ),
        "rows": [
            (
                "Country Park, Muldersdrift/Johannesburgo · -26.057805, 27.881235",
                "<strong>Camping para overlanders con puntos centrales de agua, fregadero, "
                "lavado y duchas con calentamiento solar.</strong> No publica potabilidad ni "
                "llenado de grandes depósitos. "
                + a("https://www.countrypark.co.za/caravan-park.php", "camping oficial")
                + " · " + gm(-26.0578048, 27.8812349),
                "Base urbana para higiene y recarga concertada. Maps indica mascotas; "
                "confirmar dos 4x4, litros, conexión y calidad antes de desplazarse.",
            ),
            (
                "African Overlanders, Atlantis/Ciudad del Cabo · -33.590279, 18.537797",
                "<strong>Camping orientado a expediciones con duchas calientes, cocina, "
                "electricidad y taller.</strong> No publica grifo de parcela ni llenado. "
                + a("https://africanoverlanders.com/camping-sites-in-cape-town-western-cape/", "camping oficial")
                + " · " + gm(-33.590279, 18.5377969),
                "Buena base de llegada, salida o reparación; reservar. Usarlo como ducha y "
                "negociar aparte cualquier carga, incluidos calidad y volumen.",
            ),
            (
                "Springbok Caravan Park · -29.673335, 17.898991",
                "<strong>Parcelas niveladas con agua y electricidad, aseos y política "
                "pet-friendly bajo consulta.</strong> El grifo existe en la plaza, pero el "
                "sitio no publica potabilidad ni permiso de carga masiva. "
                + a("https://www.springbokkaravaanpark.co.za/", "camping oficial")
                + " · " + gm(-29.6733346, 17.8989912),
                "Toma prioritaria antes o después de Namaqualand/Richtersveld. Reservar y "
                "pactar litros para ambos coches, sequía, coste y tratamiento.",
            ),
            (
                "Twee Rivieren Rest Camp, Kgalagadi · -26.472559, 20.612178",
                "<strong>Camping con abluciones y agua de bebida muy mineralizada.</strong> "
                "SANParks exige llevar agua propia a los wilderness camps y recomienda 10 l "
                "de emergencia en el vehículo. La disponibilidad no autoriza llenar depósitos. "
                + a("https://www.sanparks.org/parks/kgalagadi/useful-information/visitor-tips", "aviso oficial")
                + " · " + gm(-26.4725589, 20.6121781),
                "Ducha y apoyo dentro del campamento reservado. Cargar la autonomía en "
                "Upington; no depender de esta agua para beber ni para grandes volúmenes.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Country Park cubre Gauteng; '
            "African Overlanders, Ciudad del Cabo; Springbok, el corredor norte. Son bases "
            "concretas, no una autorización nacional.</li><li>El informe Blue Drop oficial "
            "evalúa cada sistema: en 2023, 277 de 958 estaban en estado crítico. Antes de "
            "beber agua de red hay que consultar el aviso municipal y los datos vigentes, no "
            "suponer «calidad europea».</li><li>Kgalagadi: Twee Rivieren tiene abluciones y "
            "agua muy mineralizada; los wilderness camps exigen llevar la propia. La carga "
            "principal se hace en Upington.</li><li>Richtersveld no es homogéneo: De Hoop, "
            "Richtersberg y Potjiespram publican abluciones de agua fría; Kokerboomkloof tiene "
            "retrete seco y exige llevar toda el agua. Ninguna se convierte en pin de recarga. "
            "Confirmar el estado con SANParks antes de entrar.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Country Park (Johannesburgo)",
                "cat": "Agua de servicio", "lat": -26.0578048, "lon": 27.8812349,
                "info": "[PUNTOS DE AGUA; LLENADO CONDICIONADO] Camping para overlanders con agua central, fregadero y duchas solares. Maps indica mascotas; pactar litros, toma, coste y calidad.",
                "source": "https://www.countrypark.co.za/caravan-park.php",
            },
            {
                "name": "Agua de servicio · African Overlanders (Ciudad del Cabo)",
                "cat": "Agua de servicio", "lat": -33.590279, "lon": 18.5377969,
                "info": "[SOLO DUCHA PUBLICADA; BASE OVERLAND] Duchas calientes, cocina, electricidad y taller. Sin grifo de parcela ni llenado publicado; reservar y negociar cualquier carga.",
                "source": "https://africanoverlanders.com/camping-sites-in-cape-town-western-cape/",
            },
            {
                "name": "Agua de servicio · Springbok Caravan Park",
                "cat": "Agua de servicio", "lat": -29.6733346, "lon": 17.8989912,
                "info": "[AGUA EN PARCELA; LLENADO CONDICIONADO] Stands con agua/electricidad y abluciones; perro bajo consulta. Acordar volumen, conexión, sequía, coste y tratamiento.",
                "source": "https://www.springbokkaravaanpark.co.za/",
            },
            {
                "name": "Agua de servicio · Twee Rivieren (Kgalagadi)",
                "cat": "Agua de servicio", "lat": -26.4725589, "lon": 20.6121781,
                "info": "[DUCHA Y AGUA MUY MINERALIZADA; NO RECARGA PLANIFICADA] Camping con abluciones. Llevar agua de Upington y 10 l de emergencia; wilderness camps sin agua potable.",
                "source": "https://www.sanparks.org/parks/kgalagadi/useful-information/visitor-tips",
            },
        ],
        "sources": [
            ["Country Park · camping y puntos de agua", "https://www.countrypark.co.za/caravan-park.php"],
            ["African Overlanders · camping oficial", "https://africanoverlanders.com/camping-sites-in-cape-town-western-cape/"],
            ["Springbok Caravan Park · sitio oficial", "https://www.springbokkaravaanpark.co.za/"],
            ["SANParks · consejos de Kgalagadi", "https://www.sanparks.org/parks/kgalagadi/useful-information/visitor-tips"],
            ["SANParks · alojamiento de Richtersveld", "https://www.sanparks.org/parks/ai-ais-richtersveld/accommodation"],
            ["DWS · informe Blue Drop 2023", "https://ws.dws.gov.za/IRIS/releases/BDN_2023_Report.pdf"],
        ],
    },
}


TEXT_REPLACEMENTS = {
    "zimbabue": {
        "Agua: tratar siempre la de los campamentos de parques, que tienen agua corriente pero no potable sin tratar. Ha habido brotes de cólera en Zimbabue en los últimos años asociados a problemas de saneamiento urbano: no beber agua de grifo sin tratar en ninguna ciudad.":
            "Agua: ZimParks pide llevar agua de bebida y no garantiza una toma en todos sus tipos de campamento. En ciudad, comprobar el aviso de suministro vigente; si no hay confirmación reciente, usar agua sellada o aplicar tratamiento completo.",
    },
    "botsuana": {
        "Los campings del Kalahari Central no tienen agua;":
            "No hay recarga de visitante acreditada en los campings remotos del Kalahari Central;",
        "CKGR: Deception Valley, Kori y Leopard Pan por el DWNP; Piper Pan y Sunday Pan por Bigfoot Tours. Letrina de pozo, ducha de cubo y fogón. NINGUNO tiene agua.":
            "CKGR: Deception Valley, Kori y Leopard Pan por el DWNP; Piper Pan y Sunday Pan por Bigfoot Tours. Las instalaciones cambian por parcela: no planificar ninguna recarga de visitante y entrar con toda el agua.",
        "Khama Rhino Sanctuary: camping con agua, fogones y piscina; unos P133 por persona y noche para extranjeros.":
            "Khama Rhino Sanctuary: camping con grifos y abluciones según su ficha turística; confirmar antes el suministro y no asumir permiso para llenar. Verificar la tarifa vigente.",
        "Cada camping tiene letrina de pozo, ducha de cubo y fogón, y NINGUNO tiene agua.":
            "Las instalaciones varían entre parcelas; no planificar ninguna recarga de visitante y llevar toda el agua desde fuera de la reserva.",
        "Agua: 6 l por persona y día más 2 l de reserva para 5 días extra.":
            "Agua: calcular personas, perro, cocina, higiene y limpieza para todos los días previstos, más una reserva de avería y retorno.",
        "Agua en el Kalahari, regla que citan de Tracks4Africa: 6 litros por persona y día, MÁS otros 2 litros por persona y día para 5 días extra por si algo sale mal.":
            "Agua en el Kalahari: calcular el consumo completo de personas, perro, cocina, higiene y limpieza, y añadir margen suficiente para avería, retraso y retorno. No usar una cifra genérica como sustituto de ese cálculo.",
    },
    "sudafrica": {
        "Sin agua, sin combustible y sin cobertura dentro del parque. En verano se superan los 45 °C: la ventana razonable es de mayo a septiembre.":
            "Sin recarga de depósitos ni combustible garantizados y sin cobertura fiable dentro del parque. Algunos campamentos tienen abluciones de agua fría y otros no tienen agua; en verano se superan los 45 °C, por lo que la ventana razonable es de mayo a septiembre.",
        "Campamentos sin servicio alguno a orillas del Orange (Tatasberg, De Hoop, Richtersberg, Kokerboomkloof): hay que entrar con toda el agua, todo el combustible y comida de sobra.":
            "Campamentos muy básicos del Richtersveld: De Hoop, Richtersberg y Potjiespram publican abluciones de agua fría, mientras Kokerboomkloof tiene retrete seco y exige llevar agua. En todos se entra con autonomía, combustible y comida de sobra.",
        "En el lado botsuano y en los wilderness camps no hay agua ni combustible: autonomía completa.":
            "En el lado botsuano y en los wilderness camps no se garantiza agua potable, recarga de depósitos ni combustible: autonomía completa.",
        "Richtersveld (Tatasberg, De Hoop, Richtersberg, Kokerboomkloof): vivac puro junto al Orange o entre bolas de granito, sin agua, sin luz y sin cobertura. Entrar cargado de todo.":
            "Richtersveld: los servicios no son iguales. De Hoop, Richtersberg y Potjiespram publican abluciones de agua fría; Kokerboomkloof tiene retrete seco y exige llevar toda el agua. No hay electricidad ni cobertura fiable: confirmar cada campamento y entrar cargado.",
        "Los campamentos junto al Orange (Tatasberg, De Hoop) aparecen sistemáticamente como de los mejores vivacs de Sudáfrica, sin ningún servicio y con un silencio absoluto.":
            "De Hoop aparece como uno de los grandes vivacs junto al Orange y publica abluciones de agua fría; Tatasberg es un wilderness camp de cabañas, no un camping sin servicios.",
        "Agua del grifo potable en ciudades y en la mayoría de los pueblos, con calidad europea. Excepciones puntuales en municipios pequeños del Karoo y del Eastern Cape con avisos de calidad: preguntar localmente. Buen país para descansar del protocolo de potabilización, salvo en el Richtersveld y el Kgalagadi, donde se entra con el agua cargada.":
            "La calidad del agua de red se decide por sistema municipal, no por país. El Blue Drop oficial encontró 277 de 958 sistemas en estado crítico en 2023: consultar el aviso local vigente y tratar si no hay confirmación. En Richtersveld y Kgalagadi se entra con autonomía completa.",
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

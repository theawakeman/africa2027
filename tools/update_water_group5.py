#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 5.

Sustituye ciudades usadas como falsos grifos por instalaciones físicas y
separa agua del camping, ducha y autorización para llenar el vehículo.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FICHA = ROOT / "content" / "ficha"


COMMON = (
    '<div class="callout warn"><div class="callout-title">Regla operativa</div>'
    '<p><strong>Agua de servicio no significa agua potable.</strong> El icono de agua de un '
    'camping tampoco autoriza a llenar los depósitos. Antes de desviarse hay que confirmar '
    'fecha, litros, toma, precio y acceso de los dos 4x4. Para beber y cocinar: agua sellada '
    'o tratamiento completo. Llevar garrafas, manguera, adaptadores, bomba y prefiltro.</p></div>'
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
    "zambia": {
        "intro": (
            "<h3>Agua de servicio: una parcela con toma y una ducha actual</h3>"
            "<p>Se retiran Lusaka, Livingstone y el circuito de cascadas como supuestos puntos de "
            "manguera. Solo se conservan dos instalaciones identificables y con alcance limitado.</p>"
        ),
        "rows": [
            (
                "The Moorings Campsite, Monze · -16.194229, 27.543504",
                "<strong>Toma de agua en cada parcela.</strong> Zambia Tourism publica que cada "
                "emplazamiento dispone de su propio punto de agua y electricidad, además de "
                "duchas calientes. No publica caudal, rosca ni potabilidad. "
                + a("https://www.zambiatourism.com/listing/the-moorings-campsite/", "ficha oficial")
                + " · "
                + gm(-16.1942291, 27.543504),
                "Primera opción para una recarga planificada del corredor sur. Reservar parcela y "
                "acordar por escrito el volumen y si aceptan manguera o trasvase por garrafas.",
            ),
            (
                "Rapid 14 Logistical Base, Livingstone · -17.976536, 25.886568",
                "<strong>Ducha caliente y agua de camping; llenado no acreditado.</strong> "
                "iOverlander lo marca verificado en 2026, con agua, ducha caliente y acceso para "
                "vehículos grandes; la disponibilidad puede ser estacional. El pin se ha movido "
                "del punto colaborativo a la ficha real de Google Maps. "
                + a("https://ioverlander.com/places/54877-rapid-14-campsite-and-lodge", "ficha y verificación")
                + " · "
                + gm(-17.9765356, 25.8865676),
                "Llamar antes y usarlo para higiene durante la estancia. No contar con llenar el "
                "depósito hasta obtener permiso, litros y toma concretos.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>El oeste entre Caripande, Chavuma y Mongu '
            "y el circuito septentrional de cascadas quedan sin recarga exacta: entrar con autonomía "
            "y negociar una toma privada antes de abandonar una base grande.</li><li>Ngonye Falls "
            "Community Campsite tiene agua y ducha en una verificación reciente, pero prohíbe perros "
            "y su pin no coincide con el establecimiento que devuelve Google Maps; se documenta como "
            "descarte y no se publica un marcador dudoso.</li><li>No llenar desde el Zambeze, pozas o "
            "cascadas como operación ordinaria. El agua de parcela sigue requiriendo tratamiento si "
            "entra en el circuito de cocina.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · The Moorings Campsite (Monze)",
                "cat": "Agua de servicio",
                "lat": -16.1942291,
                "lon": 27.543504,
                "info": "[TOMA EN PARCELA; VOLUMEN CONDICIONADO] La ficha oficial publica un punto de agua en cada emplazamiento y duchas calientes. Reservar y acordar litros, manguera y precio; no presupone potabilidad.",
                "source": "https://www.zambiatourism.com/listing/the-moorings-campsite/",
            },
            {
                "name": "Agua de servicio · Rapid 14 Logistical Base",
                "cat": "Agua de servicio",
                "lat": -17.9765356,
                "lon": 25.8865676,
                "info": "[DUCHA CALIENTE Y AGUA; SIN LLENADO] Camping verificado en 2026 y apto para vehículos grandes. Confirmar apertura; el agua del camping no autoriza el depósito.",
                "source": "https://ioverlander.com/places/54877-rapid-14-campsite-and-lodge",
            },
        ],
        "sources": [
            ["Zambia Tourism · The Moorings Campsite", "https://www.zambiatourism.com/listing/the-moorings-campsite/"],
            ["iOverlander · Rapid 14 Campsite", "https://ioverlander.com/places/54877-rapid-14-campsite-and-lodge"],
            ["iOverlander · Ngonye Falls Community Campsite (descarte)", "https://ioverlander.com/places/7160-ngonye-falls-community-campsite"],
        ],
    },
    "tanzania": {
        "intro": (
            "<h3>Agua de servicio: dos campings concretos, sin promesas urbanas</h3>"
            "<p>Arusha, Dar es Salaam, Mbeya, los parques del norte y el lago Natron dejan de ser "
            "pines de agua. Kisolanza ofrece agua fresca en un camping de vehículos; Ndanindani "
            "resuelve ducha. En ambos, el depósito exige permiso.</p>"
        ),
        "rows": [
            (
                "The Old Farm House, Kisolanza · -8.146950, 35.412217",
                "<strong>Agua fresca y duchas calientes en camping para vehículos.</strong> La web "
                "oficial actual publica parcelas amplias para vehículo privado y camión overland, "
                "aseos, duchas calientes y fresh water. No ofrece conexión de manguera ni certifica "
                "potabilidad. "
                + a("https://www.kisolanza.com/", "camping oficial")
                + " · "
                + gm(-8.14695, 35.4122167),
                "Apoyo principal entre Mbeya e Iringa. Reservar y preguntar si el agua puede "
                "trasvasarse al vehículo, en qué volumen y con qué adaptador.",
            ),
            (
                "Ndanindani Lodge & Campsite, Naitolia · -3.565924, 36.109813",
                "<strong>Duchas calientes y parking seguro para overlanders.</strong> La web 2026 "
                "publica parcelas niveladas, abluciones compartidas, duchas calientes y vigilancia. "
                "El establecimiento trabaja con agua de lluvia y no anuncia llenado de depósitos. "
                + a("https://www.ndanindani.com/accommodation", "servicios oficiales")
                + " · "
                + gm(-3.5659236, 36.1098127),
                "Usarlo para higiene y pernocta reservada. Cualquier litro para el coche se consulta "
                "antes; no presionar un sistema de agua recogida en una zona seca.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Kisolanza es el único apoyo del grupo con '
            "agua actual publicada y acceso de vehículos; sigue siendo llenado condicionado, no grifo "
            "público.</li><li>Seronera y Simba no se usan como recarga: la evidencia localizada es "
            "antigua y describe suministro irregular. Entrar a Ngorongoro–Serengeti con reserva cerrada "
            "mediante una cita privada en Karatu o Arusha.</li><li>Para Natron y el bucle occidental, "
            "resolver el volumen antes del desvío y conservar margen de retorno. No captar de lagos, "
            "ríos o manantiales sin tratamiento completo.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · The Old Farm House (Kisolanza)",
                "cat": "Agua de servicio",
                "lat": -8.14695,
                "lon": 35.4122167,
                "info": "[AGUA EN CAMPING; LLENADO CONDICIONADO] Web oficial actual: acceso para vehículo/camión overland, agua fresca y duchas calientes. Acordar litros y toma; no consta potabilidad.",
                "source": "https://www.kisolanza.com/",
            },
            {
                "name": "Agua de servicio · Ndanindani Lodge & Campsite",
                "cat": "Agua de servicio",
                "lat": -3.5659236,
                "lon": 36.1098127,
                "info": "[SOLO DUCHA DE CAMPISTA] Camping 2026 orientado a overlanders, con duchas calientes y parking seguro. No publica llenado; confirmar cualquier volumen antes de ir.",
                "source": "https://www.ndanindani.com/accommodation",
            },
        ],
        "sources": [
            ["The Old Farm House Kisolanza · sitio oficial", "https://www.kisolanza.com/"],
            ["Ndanindani Lodge & Campsite · alojamiento oficial", "https://www.ndanindani.com/accommodation"],
            ["iOverlander · Seronera public campsite (evidencia antigua)", "https://ioverlander.com/places/7093-np-serenera-public-campsite"],
        ],
    },
    "kenia": {
        "intro": (
            "<h3>Agua de servicio: una ducha central y un apoyo condicionado en Turkana</h3>"
            "<p>Se elimina Nairobi como falso grifo y se corrige la afirmación de que el agua de "
            "Loiyangalani es potable. Ndege Mingi acredita ducha; Palm Shade tiene agua de manantial "
            "subterráneo, pero la recarga del vehículo y su calidad deben confirmarse.</p>"
        ),
        "rows": [
            (
                "Ndege Mingi Bush Camp, Nanyuki · 0.160158, 37.025161",
                "<strong>Duchas calientes y frías para overlanders; llenado no publicado.</strong> "
                "La web oficial actual acepta vehículos overland y tiendas y ofrece baños compartidos; "
                "el agua caliente se prepara a leña bajo petición. "
                + a("https://ndegemingi.com/faqs/", "preguntas frecuentes oficiales")
                + " · "
                + gm(0.1601575, 37.0251606),
                "Base de higiene antes del norte. Reservar, confirmar el perro y tratar el llenado "
                "del coche como una petición separada, no como parte de la parcela.",
            ),
            (
                "Palm Shade, Loiyangalani · 2.756328, 36.721233",
                "<strong>Camping con agua subterránea y duchas; depósito condicionado.</strong> "
                "Una guía actual identifica agua de manantial subterráneo y sanitarios; un relato "
                "de viaje documentó un llenado, pero no es reciente. La analítica histórica encontrada "
                "no permite declarar potable el suministro actual. "
                + a("https://www.petitfute.co.uk/v40332-loiyangalani/c1166-hebergement/c158-hotel/71187-palm-shade-camp.html", "servicios actuales")
                + " · "
                + gm(2.7563276, 36.7212331),
                "Llamar desde Marsabit y obtener confirmación de caudal y litros. Llevar suficiente "
                "reserva para llegar y regresar si la toma no funciona; tratar todo el volumen.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Nanyuki solo aporta ducha confirmada; no '
            "se atribuye una manguera a Nairobi, Isiolo o Marsabit sin establecimiento y permiso.</li>"
            "<li>Palm Shade es un apoyo remoto condicionado, no una garantía. Confirmarlo por teléfono "
            "antes de salir de Marsabit y mantener reserva para el retorno por Baragoi–Maralal.</li>"
            "<li>Se descarta como potable la fórmula anterior del «manantial mejorado por una ONG». "
            "Ni el lago Turkana ni el manantial superficial se incorporan al depósito como operación ordinaria.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Ndege Mingi Bush Camp (Nanyuki)",
                "cat": "Agua de servicio",
                "lat": 0.1601575,
                "lon": 37.0251606,
                "info": "[SOLO DUCHA DE CAMPISTA] Web oficial actual: overlanders, baños compartidos y ducha caliente a petición. No publica llenado; reservar y preguntar también por el perro.",
                "source": "https://ndegemingi.com/faqs/",
            },
            {
                "name": "Agua de servicio · Palm Shade (Loiyangalani)",
                "cat": "Agua de servicio",
                "lat": 2.7563276,
                "lon": 36.7212331,
                "info": "[AGUA Y DUCHA; LLENADO CONDICIONADO] Camping real con agua subterránea. El llenado documentado no es reciente: llamar desde Marsabit, confirmar litros y tratar todo el volumen.",
                "source": "https://www.petitfute.co.uk/v40332-loiyangalani/c1166-hebergement/c158-hotel/71187-palm-shade-camp.html",
            },
        ],
        "sources": [
            ["Ndege Mingi Bush Camp · FAQ oficial", "https://ndegemingi.com/faqs/"],
            ["Petit Futé · Palm Shade Camp", "https://www.petitfute.co.uk/v40332-loiyangalani/c1166-hebergement/c158-hotel/71187-palm-shade-camp.html"],
            ["Stuck in Low Gear · llenado histórico en Palm Shade", "https://stuckinlowgear.com/staging/1919/lake-turkana-road-to-sibiloi-national-park/"],
            ["AfDB · proyecto de agua de Loiyangalani 2024", "https://www.afdb.org/sites/default/files/esia_report_loiyangalani.pdf"],
        ],
    },
    "mozambique": {
        "intro": (
            "<h3>Agua de servicio: tres duchas reales, ninguna manguera genérica</h3>"
            "<p>Se eliminan las ciudades y toda la costa sur como supuestos puntos de llenado. "
            "Chitengo, Baobab Beach y Morrumbene son instalaciones concretas; resuelven higiene, "
            "pero ninguna publica conexión libre al depósito.</p>"
        ),
        "rows": [
            (
                "Gorongosa Campsite, Chitengo · -18.979006, 34.351308",
                "<strong>Duchas calientes y agua en camping; perro prohibido.</strong> iOverlander "
                "mantiene una verificación de 2026 y acceso para vehículos grandes. Su coordenada "
                "colaborativa quedaba casi 1 km desplazada; el pin se corrige a Gorongosa Campsite "
                "en Google Maps. "
                + a("https://www.ioverlander.com/places/38753-chitengo-camp-gorongosa-np", "ficha y verificación")
                + " · "
                + gm(-18.9790057, 34.3513083),
                "Solo sirve durante la estancia y sin el perro. Preguntar por litros si se desea "
                "trasvasar; no equiparar el icono de agua con una toma para dos coches.",
            ),
            (
                "Baobab Beach, Vilanculos · -22.009046, 35.322090",
                "<strong>Duchas calientes comunitarias para campistas.</strong> La página del "
                "establecimiento publica camping y duchas; Google Maps mantiene centenares de reseñas "
                "y fotografías recientes. No anuncia llenado vehicular. "
                + a("https://baobabbeachnew.wixsite.com/baobabbeach/baobab-facilities", "servicios del establecimiento")
                + " · "
                + gm(-22.0090462, 35.3220895),
                "Buena parada de higiene del eje EN1. Reservar espacio para los 4x4 y pedir por "
                "separado cualquier volumen para limpieza o ducha del coche.",
            ),
            (
                "Morrumbene Beach Resort · -23.621398, 35.422756",
                "<strong>Ducha caliente con agua no potable; no apto para vehículo grande.</strong> "
                "La ficha verificada en 2026 permite usar el baño de un chalet, pero marca el agua "
                "como no potable y los últimos 4 km como arena. El pin se normaliza a la ficha real "
                "de Google Maps, unos 160 m al sureste. "
                + a("https://www.ioverlander.com/places/232608-morrumbene-lodge", "ficha y verificación")
                + " · "
                + gm(-23.6213978, 35.4227555),
                "Contactar antes con dimensiones y peso de cada vehículo. Usarlo para ducha si "
                "aceptan el acceso; no llenar el depósito ni beber esa agua.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Entre Matchedje y Lichinga, y en el interior '
            "norte, no queda ninguna recarga acreditada. Entrar con reserva completa negociada en el "
            "lado tanzano.</li><li>Chitengo queda fuera del plan con perro y Morrumbene puede rechazar "
            "vehículos grandes: Baobab Beach es la ducha más sencilla del eje sur, no un grifo.</li>"
            "<li>La N222 entre Mapai y Machaila tiene un aviso específico de unos 200 km sin agua "
            "limpia. No usar ríos, pozos o grifos de lodge sin tratamiento completo, aunque el agua "
            "solo vaya a aseo y limpieza.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Gorongosa Campsite (Chitengo)",
                "cat": "Agua de servicio",
                "lat": -18.9790057,
                "lon": 34.3513083,
                "info": "[DUCHA Y AGUA DE CAMPING; PERRO PROHIBIDO] Verificado en 2026 y apto para vehículos grandes. Sin llenado publicado; el GPS se corrige casi 1 km a la ficha real de Maps.",
                "source": "https://www.ioverlander.com/places/38753-chitengo-camp-gorongosa-np",
            },
            {
                "name": "Agua de servicio · Baobab Beach (Vilanculos)",
                "cat": "Agua de servicio",
                "lat": -22.0090462,
                "lon": 35.3220895,
                "info": "[SOLO DUCHA DE CAMPISTA] El establecimiento publica camping y duchas calientes comunitarias. No consta toma para vehículos; reservar y negociar aparte cualquier litro.",
                "source": "https://baobabbeachnew.wixsite.com/baobabbeach/baobab-facilities",
            },
            {
                "name": "Agua de servicio · Morrumbene Beach Resort",
                "cat": "Agua de servicio",
                "lat": -23.6213978,
                "lon": 35.4227555,
                "info": "[SOLO DUCHA; AGUA NO POTABLE; SIN BIG RIG] Verificado en 2026, con 4 km finales de arena. Contactar con medidas de los 4x4; no llenar ni beber.",
                "source": "https://www.ioverlander.com/places/232608-morrumbene-lodge",
            },
        ],
        "sources": [
            ["iOverlander · Chitengo Camp", "https://www.ioverlander.com/places/38753-chitengo-camp-gorongosa-np"],
            ["Baobab Beach Vilanculos · instalaciones", "https://baobabbeachnew.wixsite.com/baobabbeach/baobab-facilities"],
            ["iOverlander · Morrumbene Lodge", "https://www.ioverlander.com/places/232608-morrumbene-lodge"],
            ["iOverlander · aviso de agua en la N222", "https://ioverlander.com/places/283249-road-condition-n222"],
        ],
    },
}


TEXT_REPLACEMENTS = {
    "kenia": {
        "Agua potable disponible en Loiyangalani gracias a un manantial mejorado por una ONG.":
            "Palm Shade tiene agua subterránea, pero el llenado debe confirmarse y todo el volumen tratarse; no hay potabilidad actual acreditada.",
        "Palm Shade Camp, el mejor sitio del pueblo, con sombra de palmeras y agua de manantial.":
            "Palm Shade Camp, establecimiento real con sombra, sanitarios y agua subterránea; confirmar antes ducha, litros y acceso de los vehículos.",
        "Una ONG mejoró el manantial del pueblo, así que hay agua potable abundante.":
            "El camping usa agua subterránea y existe un llenado histórico documentado, pero no hay análisis actual ni caudal garantizado: confirmar y tratar.",
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

    replacements = TEXT_REPLACEMENTS.get(slug, {})
    for sections_key in ("custom_sections", "custom_sections_post"):
        for section in data.get(sections_key, []):
            if len(section) < 3 or not isinstance(section[2], str):
                continue
            for old, new in replacements.items():
                section[2] = section[2].replace(old, new)

    existing = {tuple(item) for item in data.get("sources", []) if isinstance(item, list) and len(item) == 2}
    for source in cfg["sources"]:
        if tuple(source) not in existing:
            data.setdefault("sources", []).append(source)
            existing.add(tuple(source))

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{slug}: {len(cfg['points'])} puntos de agua exactos")


for country, config in WATER.items():
    update(country, config)

#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 4.

Elimina promesas urbanas sin toma identificada y separa recarga publicada,
recarga condicionada y ducha sin llenado del vehículo.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FICHA = ROOT / "content" / "ficha"


COMMON = (
    '<div class="callout warn"><div class="callout-title">Regla operativa</div>'
    '<p><strong>Agua de servicio no significa agua potable.</strong> Para beber y cocinar, '
    'usar agua sellada o aplicar el tratamiento completo del vehículo. Una habitación con '
    'ducha no autoriza a llenar el depósito: hay que pactar por escrito litros, toma, precio '
    'y acceso de los dos 4x4. Llevar garrafa, manguera, adaptadores, bomba y prefiltro.</p></div>'
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
    "camerun": {
        "intro": (
            "<h3>Agua de servicio: una ducha localizada, ninguna recarga acreditada</h3>"
            "<p>Se eliminan los pines urbanos de Duala/Yaundé y Kribi y la afirmación de que "
            "hoteles, campamentos y gasolineras permiten llenar con manguera. No se ha localizado "
            "una toma vehicular actual que sostenga esa promesa.</p>"
        ),
        "rows": [
            (
                "Méhéba Les Vagues Bleues, Kribi · 2.836019, 9.885499",
                "<strong>Ducha exterior sugerida; llenado no acreditado.</strong> La ficha de abril de "
                "2024 describe una ducha de jardín en el alojamiento, pero no tiene reseñas en la "
                "plataforma ni promete agua para el depósito. El establecimiento sí coincide con "
                "Google Maps. "
                + a("https://park4night.com/es/place/490765", "ficha original")
                + " · "
                + gm(2.8360192, 9.8854993),
                "Contactar antes y usarlo solo para higiene si el alojamiento lo autoriza. No llegar "
                "a Kribi contando con una manguera o un volumen determinado.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Resolver el depósito mediante una cita privada '
            "antes de abandonar Duala/Yaundé y conservar margen hasta Congo; ninguna ciudad es un punto de agua.</li>"
            "<li>La web oficial del Monte Camerún anuncia una ducha para quien acampa dentro del producto de trekking, "
            "pero también indica que el parque solo es accesible a pie y que los vehículos no pueden entrar. Por eso no "
            "se convierte su oficina de Buea en un falso punto camper.</li><li>No planificar captación rutinaria en ríos, "
            "pozos o lluvia del sureste. Si una emergencia obliga a usarla, sedimentar, filtrar y desinfectar.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Méhéba Les Vagues Bleues (Kribi)",
                "cat": "Agua de servicio",
                "lat": 2.8360192,
                "lon": 9.8854993,
                "info": "[DUCHA CONDICIONADA; SIN LLENADO] La ficha de 2024 sugiere una ducha exterior, pero no tiene reseñas ni acredita toma para el vehículo. Contactar antes y no depender de ella.",
                "source": "https://park4night.com/es/place/490765",
            }
        ],
        "sources": [
            ["park4night · Méhéba Les Vagues Bleues", "https://park4night.com/es/place/490765"],
            ["Mount Cameroon National Park · acceso y tarifas", "https://mtcameroonnationalpark.org/visit-the-park/"],
        ],
    },
    "gabon": {
        "intro": (
            "<h3>Agua de servicio: dos duchas de alojamiento, ninguna toma vehicular</h3>"
            "<p>Se retira el pin genérico de Libreville y la promesa de manguera en hoteles y estaciones. "
            "Los dos apoyos siguientes son lugares reales y actuales, pero solo resuelven higiene mediante estancia.</p>"
        ),
        "rows": [
            (
                "Hotel Hibiscus Blvd Triomphal, Libreville · 0.416364, 9.449545",
                "<strong>Ducha de habitación y aparcamiento privado; depósito no acreditado.</strong> "
                "La oferta vigente en 2026 publica baño o ducha y aparcamiento privado gratuito. Tiene "
                "centenares de reseñas, pero no ofrece servicio camper. "
                + a("https://www.booking.com/hotel/ga/hibiscus-blvd-triomphal.html", "servicios actuales")
                + " · "
                + gm(0.4163639, 9.4495445),
                "Opción urbana para ducha con habitación pagada. Consultar por separado si aceptan los dos coches "
                "y un llenado limitado; sin respuesta afirmativa, el depósito no se toca.",
            ),
            (
                "Lopé Hotel, parque de la Lopé · -0.099134, 11.595769",
                "<strong>Alojamiento operativo; solo higiene de huésped.</strong> La web oficial de 2026 anuncia "
                "apertura de temporada el 1 de junio y reservas directas. Google Maps sitúa el hotel real junto al "
                "Ogooué; no consta toma para vehículos. "
                + a("https://www.lopehotel.com/fr", "hotel oficial")
                + " · "
                + gm(-0.0991344, 11.5957689),
                "Reservar la estancia y preguntar por estacionamiento antes de desviarse. No asociar el río, la "
                "piscina ni el baño de la habitación con agua disponible para el depósito.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Libreville y Lopé solo resuelven ducha; entrar en Gabón '
            "con autonomía de agua de servicio y una cita concreta si se necesita llenar.</li><li>Lambaréné, Mouila, "
            "Makokou y Franceville quedan sin pin: se puede comprar agua sellada, pero no se ha verificado una toma "
            "accesible al vehículo.</li><li>No captar de los ríos Ogooué, Ivindo ni lagunas como operación ordinaria. "
            "Las expediciones a parques deben suministrar su propia agua o la del operador.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Hotel Hibiscus Blvd Triomphal",
                "cat": "Agua de servicio",
                "lat": 0.4163639,
                "lon": 9.4495445,
                "info": "[SOLO DUCHA DE HUÉSPED] Hotel activo con baño o ducha y aparcamiento privado publicados. No consta toma ni llenado del vehículo; cualquier volumen se acuerda aparte.",
                "source": "https://www.booking.com/hotel/ga/hibiscus-blvd-triomphal.html",
            },
            {
                "name": "Agua de servicio · Lopé Hotel",
                "cat": "Agua de servicio",
                "lat": -0.0991344,
                "lon": 11.5957689,
                "info": "[SOLO HIGIENE DE HUÉSPED] Hotel del parque con web y temporada 2026 activas. No consta toma para vehículos: reservar, confirmar aparcamiento y no pedir llenado como servicio incluido.",
                "source": "https://www.lopehotel.com/fr",
            },
        ],
        "sources": [
            ["Booking · Hotel Hibiscus Blvd Triomphal", "https://www.booking.com/hotel/ga/hibiscus-blvd-triomphal.html"],
            ["Lopé Hotel · sitio oficial", "https://www.lopehotel.com/fr"],
        ],
    },
    "congo": {
        "intro": (
            "<h3>Agua de servicio: una recarga publicada y dos duchas</h3>"
            "<p>La ruta principal obtiene por fin un punto físico antes de Massabi. Pointe-Noire, Ouesso y "
            "Brazzaville dejan de funcionar como promesas urbanas: solo cuentan las instalaciones siguientes.</p>"
        ),
        "rows": [
            (
                "Tres grifos al sur de Pointe-Noire · -4.913330, 11.941230",
                "<strong>Recarga de depósito publicada.</strong> iOverlander describe tres grifos, uso local del "
                "agua y una verificación de febrero de 2026. El testimonio no equivale a análisis de potabilidad. "
                + a("https://ioverlander.com/places/c1901a0b-e464-4bc4-86e8-9e42360a8429", "ficha y última verificación")
                + " · "
                + gm(-4.91333, 11.94123),
                "Punto principal de servicio antes de Massabi. Comprobar caudal, pedir permiso local, llenar por "
                "garrafas si no entra la manguera y tratar el agua si alcanza el circuito de cocina.",
            ),
            (
                "Hotel Palm Beach, Pointe-Noire · -4.802790, 11.839168",
                "<strong>Ducha de habitación y parking; llenado no acreditado.</strong> La oferta 2026 publica "
                "baño privado, parking gratuito y recepción 24 h. Es un respaldo de higiene, no un área camper. "
                + a("https://www.booking.com/hotel/cg/palm-beach.html", "servicios actuales")
                + " · "
                + gm(-4.8027895, 11.8391682),
                "Reservar y confirmar acceso de ambos 4x4. Solo negociar agua si fallan los grifos del sur; "
                "no asumir manguera por existir piscina o jardín.",
            ),
            (
                "Tennis Club, Brazzaville · -4.269197, 15.252222",
                "<strong>Agua y duchas en la alternativa secundaria.</strong> La ficha de 2025 admite vehículos "
                "grandes, marca agua y duchas y tiene reseña de abril de 2026. Prohíbe perros. "
                + a("https://park4night.com/en/place/609359", "ficha y reseña")
                + " · "
                + gm(-4.2691974, 15.2522223),
                "Solo para el ramal secundario Brazzaville–Kinshasa y únicamente si resuelven el perro. Acordar "
                "litros; el icono de agua no demuestra llenado libre.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Bajada: completar en los grifos al sur de Pointe-Noire '
            "antes de Massabi; Cabinda no ofrece después una recarga vehicular confirmada.</li><li>Subida: entrar desde "
            "Cabinda con margen y comprobar los mismos grifos antes de consumir la reserva. Palm Beach solo resuelve "
            "ducha.</li><li>Ouesso, Owando y el eje de Odzala siguen sin toma exacta. La expedición forestal requiere "
            "autonomía o un suministro pactado con el operador.</li><li>El Tennis Club no convierte Brazzaville en el "
            "corredor principal: queda documentado exclusivamente para el ramal secundario del ferry.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · tres grifos al sur de Pointe-Noire",
                "cat": "Agua de servicio",
                "lat": -4.91333,
                "lon": 11.94123,
                "info": "[RECARGA DE DEPÓSITO PUBLICADA] Tres grifos verificados en febrero de 2026. El consumo local no acredita potabilidad: pedir permiso, comprobar caudal y tratar si se usa para cocinar.",
                "source": "https://ioverlander.com/places/c1901a0b-e464-4bc4-86e8-9e42360a8429",
            },
            {
                "name": "Agua de servicio · Hotel Palm Beach (Pointe-Noire)",
                "cat": "Agua de servicio",
                "lat": -4.8027895,
                "lon": 11.8391682,
                "info": "[SOLO DUCHA DE HUÉSPED] Hotel activo con baño privado, parking y recepción 24 h. No consta toma para el vehículo; negociar cualquier volumen por separado.",
                "source": "https://www.booking.com/hotel/cg/palm-beach.html",
            },
            {
                "name": "Agua de servicio · Tennis Club (Brazzaville; alternativa)",
                "cat": "Agua de servicio",
                "lat": -4.2691974,
                "lon": 15.2522223,
                "info": "[ALTERNATIVA SECUNDARIA; AGUA Y DUCHA] Acepta vehículos grandes y tiene reseña de abril de 2026, pero prohíbe perros. Acordar litros; no implica llenado libre.",
                "source": "https://park4night.com/en/place/609359",
            },
        ],
        "sources": [
            ["iOverlander · tres grifos al sur de Pointe-Noire", "https://ioverlander.com/places/c1901a0b-e464-4bc4-86e8-9e42360a8429"],
            ["Booking · Hotel Palm Beach", "https://www.booking.com/hotel/cg/palm-beach.html"],
            ["park4night · Tennis Club de Brazzaville", "https://park4night.com/en/place/609359"],
        ],
    },
    "rd-congo": {
        "intro": (
            "<h3>Agua de servicio: dos apoyos concretos en Muanda</h3>"
            "<p>Se sustituyen los centros urbanos de Muanda, Boma y Matadi por dos establecimientos reales. "
            "Ambos resuelven ducha; ninguno publica llenado de depósito con manguera.</p>"
        ),
        "rows": [
            (
                "Résidence Walter, Muanda · -5.938573, 12.361338",
                "<strong>Agua garantizada, baño y parking seguro; depósito condicionado.</strong> La web oficial "
                "garantiza agua y electricidad y publica aparcamiento privado seguro. Google Maps mantiene reseñas "
                "recientes en el lugar exacto. "
                + a("https://www.residence-walter.ch/index.html", "web oficial")
                + " · "
                + gm(-5.9385726, 12.3613384),
                "Primera llamada para el cruce de Yema: reservar y pedir por escrito litros, toma y acceso de los "
                "dos 4x4. La garantía de agua del alojamiento no incluye el depósito.",
            ),
            (
                "Hotel Atlantic View, Muanda · -5.933194, 12.342148",
                "<strong>Ducha y parking privado; depósito no acreditado.</strong> La oferta vigente en 2026 "
                "publica baño con ducha y aparcamiento privado gratuito; Google Maps sitúa el hotel en Avenue de "
                "la Mission. "
                + a("https://www.booking.com/hotel/cd/atlantic-view-muanda.html", "servicios actuales")
                + " · "
                + gm(-5.9331942, 12.3421481),
                "Respaldo de Résidence Walter para higiene o estancia. Consultar llenado como petición separada; "
                "sin confirmación, salir hacia Yema con el agua ya resuelta.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Bajada: desde Yema, cerrar en Muanda la ducha y la '
            "posible recarga antes de continuar a Boma–Matadi–Lufu. Ninguno de los dos hoteles es un grifo público.</li>"
            "<li>Subida: Muanda es la última oportunidad negociada antes de Cabinda; obtener respuesta escrita y "
            "salir con dos días de reserva.</li><li>Boma y Matadi quedan sin pin de agua. Sus hoteles y talleres son "
            "opciones a contactar, no servicios confirmados.</li><li>No utilizar el Congo, estuarios o fuentes sin "
            "control como suministro ordinario. El riesgo microbiológico y el sedimento exigen tratamiento completo.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Résidence Walter (Muanda)",
                "cat": "Agua de servicio",
                "lat": -5.9385726,
                "lon": 12.3613384,
                "info": "[AGUA GARANTIZADA Y DUCHA; DEPÓSITO CONDICIONAL] Alojamiento con agua y parking seguro publicados. Reservar y acordar por escrito litros, toma y acceso de los dos 4x4.",
                "source": "https://www.residence-walter.ch/index.html",
            },
            {
                "name": "Agua de servicio · Hotel Atlantic View (Muanda)",
                "cat": "Agua de servicio",
                "lat": -5.9331942,
                "lon": 12.3421481,
                "info": "[SOLO DUCHA DE HUÉSPED] Hotel activo con ducha y parking privado en 2026. No consta toma para el vehículo; cualquier llenado requiere acuerdo separado.",
                "source": "https://www.booking.com/hotel/cd/atlantic-view-muanda.html",
            },
        ],
        "sources": [
            ["Résidence Walter · sitio oficial", "https://www.residence-walter.ch/index.html"],
            ["Booking · Hotel Atlantic View Muanda", "https://www.booking.com/hotel/cd/atlantic-view-muanda.html"],
        ],
    },
    "angola": {
        "intro": (
            "<h3>Agua de servicio: tres duchas concretas, ninguna recarga pública actual</h3>"
            "<p>Se elimina el pin genérico de Luanda y la promesa de manguera en hoteles y gasolineras. "
            "Cabinda, Luanda y Kalandula quedan ancladas a instalaciones reales con el alcance claramente limitado.</p>"
        ),
        "rows": [
            (
                "Executive Paraíso Hotel, Cabinda · -5.554228, 12.191838",
                "<strong>Habitación, parking gratuito y seguridad 24 h; llenado no acreditado.</strong> La web "
                "oficial mantiene activos alojamiento, piscina, lavandería, parking y seguridad; Google Maps tiene "
                "centenares de reseñas en este punto. "
                + a("https://www.ephotel.co.ao/", "hotel oficial")
                + " · "
                + gm(-5.5542279, 12.1918382),
                "Base concreta para ducha y noche vigilada entre Massabi y Yema. Solicitar por escrito cualquier "
                "llenado; la piscina y el agua del hotel no autorizan una manguera.",
            ),
            (
                "Luanda's Naval Club · -8.798900, 13.224900",
                "<strong>Duchas para overlanders; sin toma de depósito.</strong> Punto creado y reseñado en abril "
                "de 2026: admite hasta diez vehículos, aseos, duchas y wifi. La misma reseña exige ya pre-reserva. "
                + a("https://park4night.com/en/place/670798", "ficha y reseña")
                + " · "
                + gm(-8.7989, 13.2249),
                "Apoyo principal de higiene en Luanda. Reservar antes de entrar en la ciudad; no solicitar llenado "
                "como si formara parte del estacionamiento.",
            ),
            (
                "Pousada Calandula · -9.078257, 16.001842",
                "<strong>Camping de hotel con ducha; sin agua de depósito publicada.</strong> La ficha de julio "
                "de 2025 y una reseña de agosto confirman camping en césped, aseos y duchas. "
                + a("https://park4night.com/en/place/615872", "ficha y reseña")
                + " · "
                + gm(-9.0782573, 16.0018423),
                "Útil en el triángulo de Malanje para ducha y pernocta. Confirmar precio, acceso y cualquier litro "
                "extra; no captar de las cascadas o piscinas naturales.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Cabinda: entrar desde los grifos del sur de Pointe-Noire '
            "con el depósito lleno. Executive Paraíso es ducha y base vigilada, no recarga confirmada.</li><li>Luanda: "
            "el Naval Club resuelve higiene previa reserva. Una antigua ficha de GIRASSOL decía haber llenado 100 l, "
            "pero llevaba más de cuatro años sin verificar y su GPS no coincide con la estación GIRASSOL de Google "
            "Maps; se descarta.</li><li>En el resto de Angola no se asigna agua a ciudades enteras. Reservar por teléfono "
            "con hoteles o talleres y conservar autonomía reforzada para Iona, Moxico y Caripande.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Executive Paraíso Hotel (Cabinda)",
                "cat": "Agua de servicio",
                "lat": -5.5542279,
                "lon": 12.1918382,
                "info": "[SOLO DUCHA DE HUÉSPED] Hotel real con parking gratuito y seguridad 24 h. No consta toma vehicular: reservar y pactar aparte cualquier volumen.",
                "source": "https://www.ephotel.co.ao/",
            },
            {
                "name": "Agua de servicio · Luanda's Naval Club",
                "cat": "Agua de servicio",
                "lat": -8.7989,
                "lon": 13.2249,
                "info": "[SOLO DUCHA; PRE-RESERVA] Punto para overlanders creado y reseñado en abril de 2026. Aseos y duchas publicados; no consta llenado del depósito.",
                "source": "https://park4night.com/en/place/670798",
            },
            {
                "name": "Agua de servicio · Pousada Calandula",
                "cat": "Agua de servicio",
                "lat": -9.0782573,
                "lon": 16.0018423,
                "info": "[SOLO DUCHA DE CAMPISTA] Camping de hotel con reseña de agosto de 2025, aseos y duchas. No publica toma para el vehículo; acordar cualquier litro extra.",
                "source": "https://park4night.com/en/place/615872",
            },
        ],
        "sources": [
            ["Executive Paraíso Hotel Cabinda · sitio oficial", "https://www.ephotel.co.ao/"],
            ["park4night · Luanda's Naval Club", "https://park4night.com/en/place/670798"],
            ["park4night · Pousada Calandula", "https://park4night.com/en/place/615872"],
        ],
    },
}


CHIPS = {
    "congo": "Un punto de recarga publicado al sur de Pointe-Noire; el resto requiere cita",
    "rd-congo": "Muanda: dos apoyos exactos; llenado solo con permiso escrito",
    "angola": "Cabinda, Luanda y Kalandula: duchas exactas; ningún llenado público confirmado",
}


SERVICE_INFO = {
    "congo": {
        "Pointe-Noire · zona urbana de servicios": "Referencia urbana, no instalación. La recarga publicada está en el pin de tres grifos al sur de la ciudad; Palm Beach es solo apoyo de ducha. Resolver aquí taller, efectivo y víveres antes de Massabi.",
        "Ouesso · zona urbana de servicios": "Referencia urbana, no grifo. No se ha localizado una toma vehicular actual en Ouesso: entrar en el bloque forestal con autonomía o suministro pactado con el operador.",
        "Brazzaville · zona urbana de servicios": "Referencia del ramal secundario, no punto de agua. El Tennis Club tiene pin propio, agua y duchas publicadas, pero prohíbe perros y no convierte el ferry de Kinshasa en ruta principal.",
    },
    "rd-congo": {
        "Muanda · zona urbana de servicios": "Referencia urbana, no grifo. Résidence Walter y Atlantic View tienen pines propios: ambos resuelven ducha; solo Walter garantiza agua y cualquier llenado exige permiso escrito.",
        "Boma · zona urbana de servicios": "Referencia urbana e histórica. No se ha verificado una toma accesible al vehículo; usarla para combustible o alojamiento solo tras confirmar el establecimiento concreto.",
        "Matadi · zona urbana de servicios": "Referencia del eje junto al puente, no instalación de agua. Es la principal base de talleres, banco y hospital del tránsito por Kongo Central; el llenado requiere cita privada identificada.",
    },
    "angola": {
        "Cabinda ciudad · zona urbana de servicios": "Referencia urbana, no grifo. Executive Paraíso tiene pin propio para ducha, parking y seguridad; no publica llenado de depósito. Entrar desde Pointe-Noire con el agua resuelta.",
    },
}


TEXT_REPLACEMENTS = {
    "congo": {
        "Nada se presenta como grifo confirmado: recarga acordada en Pointe-Noire, Brazzaville u Ouesso.":
            "Recarga publicada en tres grifos al sur de Pointe-Noire; Brazzaville solo aporta una ducha secundaria y Ouesso no tiene toma exacta.",
        "Nombre de establecimiento, persona que autoriza y fecha; si falta, el punto sigue como no verificado.":
            "Comprobar los tres grifos al sur de Pointe-Noire; para cualquier alternativa, exigir nombre, persona que autoriza, litros y fecha.",
    },
    "angola": {
        "Recarga completa pactada en Cabinda ciudad; dos días de reserva.":
            "Entrar desde Pointe-Noire con el depósito lleno; Cabinda solo tiene ducha exacta y dos días de reserva.",
        "Alojamiento/taller concreto en Cabinda con permiso de manguera y fecha.":
            "Confirmar Executive Paraíso para ducha y noche; no contar con llenado salvo autorización escrita con litros y fecha.",
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

    by_name = SERVICE_INFO.get(slug, {})
    for point in data["logistics"]:
        if point.get("name") in by_name:
            point["info"] = by_name[point["name"]]

    if slug in CHIPS:
        for chip in data.get("chips", []):
            if chip[0] == "AGUA":
                chip[1] = CHIPS[slug]
                break

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

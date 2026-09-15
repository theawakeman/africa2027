#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 1.

Sustituye referencias geográficas genéricas por instalaciones/puntos concretos,
con coordenadas y condiciones de acceso documentadas. El combustible existente se
conserva sin cambios para mantener este bloque limitado a la auditoría de agua.
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
        f'<th>Qué está acreditado</th><th>Decisión operativa</th></tr></thead><tbody>{body}</tbody></table></div>'
    )


WATER = {
    "marruecos": {
        "intro": (
            "<h3>Agua de servicio: puntos concretos</h3>"
            "<p>El eje atlántico tiene varias opciones, pero no se da por cierta ninguna recarga genérica "
            "en hoteles, riads o gasolineras. Los anclajes del itinerario son estos:</p>"
        ),
        "rows": [
            (
                "Taddart, N7 · 31.455600, -7.980400",
                "<strong>Recarga confirmada recientemente.</strong> Fuente de carretera con informes de llenados de 200 l; el caudal puede ser débil. "
                + a("https://www.park4night.com/es/place/561107", "ficha y comentarios"),
                "Parar solo si no se bloquea el acceso local; usar bomba/garrafas si no hay presión. Tratarla antes de beber.",
            ),
            (
                "Camping Equinox, El Ouatia · 28.490910, -11.337891",
                "<strong>Recarga y duchas declaradas; estado variable.</strong> El directorio marca agua incluida, pero una reseña de 2026 avisa de instalaciones degradadas. "
                + a("https://www.campercontact.com/fr/maroc/guelmim-oued-noun/el-ouatia/30150/camping-equinox-tan-tan", "fuente"),
                "Llamar antes o inspeccionar el grifo; alternativa, Oued Ma Fatma. No asumir potabilidad.",
            ),
            (
                "Oued Ma Fatma · 28.205000, -11.782833",
                "<strong>Recarga de pago documentada.</strong> La guía de campings registra 100 l por 20 MAD. "
                + a("https://saharawander.com/campings_maroc.pdf", "guía y coordenadas"),
                "Usarlo como último respaldo medido antes de continuar al sur; reconfirmar precio y disponibilidad.",
            ),
            (
                "Esprit Nature, Essaouira · 31.554307, -9.628866",
                "<strong>Duchas y zona de lavado, no llenado acreditado.</strong> La web oficial publica duchas calientes y prohíbe lavar vehículos. "
                + a("https://espritnature-essaouira.com/", "web oficial")
                + " · "
                + a("https://www.espritnature-essaouira.com/_media/hiver-en-plaquette-verso-2025-2026.pdf", "servicios y normas"),
                "Válido para ducha; el depósito solo si lo autoriza expresamente el establecimiento.",
            ),
        ],
        "plan": (
            "<h3>Plan de tramo</h3><ul class=\"ticks\"><li>Salir de Tan-Tan/El Ouatia con los depósitos completos y "
            "mantener una reserva separada para beber.</li><li>Antes de Tarfaya, comprobar Equinox y conservar Oued Ma Fatma "
            "como respaldo; no existe ya en el mapa el antiguo pin representativo de Marrakech.</li></ul>"
        ),
        "points": [
            {"name": "Agua de servicio · fuente de Taddart (N7)", "cat": "Agua de servicio", "lat": 31.4556, "lon": -7.9804,
             "info": "[RECARGA CONFIRMADA] Fuente de carretera con llenados recientes de hasta 200 l; caudal a veces débil. No bloquear el uso local, llevar bomba/garrafas y tratar antes de beber. Verificar el mismo día en la fuente enlazada.", "source": "https://www.park4night.com/es/place/561107"},
            {"name": "Agua de servicio · Camping Equinox (El Ouatia)", "cat": "Agua de servicio", "lat": 28.49091, "lon": -11.337891,
             "info": "[CONDICIONAL] Directorio actual declara agua y duchas, pero hay informes recientes de deterioro. Confirmar funcionamiento, acceso con ambos 4x4 y calidad antes de conectar; no asumir potabilidad.", "source": "https://www.campercontact.com/fr/maroc/guelmim-oued-noun/el-ouatia/30150/camping-equinox-tan-tan"},
            {"name": "Agua de servicio · Oued Ma Fatma", "cat": "Agua de servicio", "lat": 28.205, "lon": -11.782833,
             "info": "[RECARGA DE PAGO DOCUMENTADA] Guía overlander registra 100 l por 20 MAD. Reconfirmar disponibilidad y precio; agua de servicio, no potable sin tratamiento.", "source": "https://saharawander.com/campings_maroc.pdf"},
        ],
        "sources": [
            ["park4night · fuente de Taddart N7", "https://www.park4night.com/es/place/561107"],
            ["Campercontact · Camping Equinox Tan-Tan", "https://www.campercontact.com/fr/maroc/guelmim-oued-noun/el-ouatia/30150/camping-equinox-tan-tan"],
            ["Sahara Wander · guía de campings y recargas de Marruecos", "https://saharawander.com/campings_maroc.pdf"],
            ["Camping Esprit Nature · servicios oficiales", "https://espritnature-essaouira.com/"],
        ],
    },
    "sahara-occidental": {
        "intro": (
            "<h3>Agua de servicio: dos anclajes, no una garantía urbana</h3>"
            "<p>Se elimina la afirmación de que El Aaiún y Dajla tienen suministro «garantizado» para vehículos. "
            "La desalación o una red urbana no implican acceso a una manguera.</p>"
        ),
        "rows": [
            (
                "Camping Sahara Line, Bojador · 26.132167, -14.495333",
                "<strong>Recarga de pago con reservas.</strong> Reseñas de 2026 describen 100 l y duchas; también agua algo salobre, baja presión y servicio irregular. "
                + a("https://park4night.com/fr/place/12064", "ficha reciente"),
                "Confirmar ese día; agua de servicio solamente. Llevar bomba y no llenar el circuito potable.",
            ),
            (
                "Camping Moussafir, Dajla · 23.764167, -15.907500",
                "<strong>Agua y vaciado publicados.</strong> El directorio del establecimiento enumera agua, vaciado, electricidad y acceso 4x4. "
                + a("https://www.morocco-guide.com/accommodation/campsites/camping-moussafir-dakhla/", "directorio y coordenadas"),
                "Reservar/llamar y pedir expresamente llenado de depósito; tratar antes de beber.",
            ),
        ],
        "plan": (
            "<h3>Plan de tramo</h3><ul class=\"ticks\"><li>Intentar Bojador y completar obligatoriamente en Dajla.</li>"
            "<li>Salir de Dajla con autonomía de varios días hasta Nuadibú: no hay punto de recarga confirmado en Guerguerat "
            "ni se deben usar como garantía las estaciones de la N1.</li></ul>"
        ),
        "points": [
            {"name": "Agua de servicio · Camping Sahara Line (Bojador)", "cat": "Agua de servicio", "lat": 26.132167, "lon": -14.495333,
             "info": "[CONDICIONAL] Se documentan recargas de pago y duchas, pero también agua salobre, poca presión y servicio irregular. Confirmar el mismo día; usar solo como agua de servicio.", "source": "https://park4night.com/fr/place/12064"},
            {"name": "Agua de servicio · Camping Moussafir (Dajla)", "cat": "Agua de servicio", "lat": 23.764167, "lon": -15.9075,
             "info": "[CONDICIONAL] El establecimiento publica agua y vaciado para 4x4/campers. Reservar y pedir autorización expresa para llenar ambos depósitos; no asumir potabilidad.", "source": "https://www.morocco-guide.com/accommodation/campsites/camping-moussafir-dakhla/"},
        ],
        "sources": [
            ["park4night · Camping Sahara Line, Bojador", "https://park4night.com/fr/place/12064"],
            ["Morocco Guide · Camping Moussafir, Dajla", "https://www.morocco-guide.com/accommodation/campsites/camping-moussafir-dakhla/"],
            ["Ministerio de Turismo de Marruecos · registro de alojamientos", "https://mtaess.gov.ma/fr/annuaires/annuaire-des-etablissements-dhebergements-touristique/"],
        ],
    },
    "mauritania": {
        "intro": (
            "<h3>Agua de servicio: un punto fuerte y dos apoyos condicionados</h3>"
            "<p>Nuadibú, Atar y Nuakchot ya no aparecen como si la mera presencia de comercios garantizara recarga. "
            "En Mauritania hay que concertar el acceso y conservar margen para que una negativa no inmovilice la ruta.</p>"
        ),
        "rows": [
            (
                "Camping Baie du Lévrier, Nuadibú · 20.915500, -17.050200",
                "<strong>Solo ducha; recarga descartada.</strong> La ficha reciente mantiene duchas, pero los informes indican que no llenan depósitos. "
                + a("https://park4night.com/en/place/70265", "fuente"),
                "No contar con agua para el vehículo. Llegar desde Dajla con reserva y concertar otra opción privada si se permanece en la ciudad.",
            ),
            (
                "Africa Escale, Nuakchot · 18.104900, -15.992200",
                "<strong>Agua y duchas, acceso condicionado.</strong> La ficha está activa, pero las reseñas recientes discrepan sobre caudal y limpieza. "
                + a("https://park4night.com/en/place/398533", "comentarios"),
                "Contactar antes, inspeccionar y pedir permiso para llenar; alternativa, comprar/transportar garrafas.",
            ),
            (
                "Bab Sahara, Atar · 20.519230, -13.061900",
                "<strong>Recarga confirmada por el establecimiento.</strong> Su web ofrece agua limpia: 100 l por 100 MRU, además de duchas. "
                + a("https://bab-sahara.com/", "web oficial"),
                "Anclaje principal del bucle del Adrar. Reconfirmar tarifa; tratar para consumo aunque el operador la describa como potable.",
            ),
        ],
        "plan": (
            "<h3>Plan de tramo</h3><ul class=\"ticks\"><li>Dajla → Nuadibú: entrar con reserva completa; Baie du Lévrier "
            "no cuenta como recarga.</li><li>Nuakchot es apoyo condicionado; Bab Sahara es el anclaje documentado antes de las "
            "pistas del Adrar.</li><li>No consumir agua de pozo sin filtración y desinfección redundante.</li></ul>"
        ),
        "points": [
            {"name": "Agua de servicio · Africa Escale (Nuakchot)", "cat": "Agua de servicio", "lat": 18.1049, "lon": -15.9922,
             "info": "[CONDICIONAL] El recinto publica agua y duchas, pero hay reseñas recientes contradictorias sobre disponibilidad y estado. Contactar antes y pedir autorización para llenar; inspeccionar el agua.", "source": "https://park4night.com/en/place/398533"},
            {"name": "Agua de servicio · Bab Sahara (Atar)", "cat": "Agua de servicio", "lat": 20.51923, "lon": -13.0619,
             "info": "[RECARGA CONFIRMADA POR EL OPERADOR] 100 l por 100 MRU según su web, con duchas. Anclaje para el Adrar; reconfirmar tarifa y tratar antes de beber.", "source": "https://bab-sahara.com/"},
        ],
        "sources": [
            ["Bab Sahara Atar · agua y coordenadas oficiales", "https://bab-sahara.com/"],
            ["park4night · Africa Escale, Nuakchot", "https://park4night.com/en/place/398533"],
            ["park4night · Camping Baie du Lévrier, Nuadibú", "https://park4night.com/en/place/70265"],
        ],
    },
    "senegal": {
        "intro": (
            "<h3>Agua de servicio: cobertura real del eje norte–este</h3>"
            "<p>Se eliminan las promesas genéricas de las redes de gasolineras. Estos son puntos físicos concretos; "
            "salvo la tubería de Hamdallai, el llenado del depósito debe acordarse con el establecimiento.</p>"
        ),
        "rows": [
            (
                "Zebrabar, Saint-Louis · 15.864900, -16.512000",
                "<strong>Duchas y camping confirmados; llenado condicionado.</strong> Web oficial y ficha reciente acreditan servicios de agua, no una manguera libre al depósito. "
                + a("https://en.zebrabar.net/", "web oficial")
                + " · "
                + a("https://park4night.com/en/place/50392", "ficha reciente"),
                "Reservar y pedir permiso para llenar ambos vehículos. Tratar antes de beber.",
            ),
            (
                "Café Romantique, Rufisque · 14.728500, -17.255600",
                "<strong>Agua corriente y duchas, acceso condicionado.</strong> Recinto pequeño, vallado, con altura máxima aproximada de 4 m. "
                + a("https://park4night.com/en/place/674597", "ficha 2026"),
                "Precontactar: confirmar altura de los coches, plaza y autorización de llenado.",
            ),
            (
                "Hamdallai Diapaldi, N7 · 13.445700, -13.431700",
                "<strong>Tres tuberías públicas con caudal reportado.</strong> Los comentarios describen uso comunitario para agua y lavado. "
                + a("https://park4night.com/en/place/568817", "ubicación y comentarios"),
                "Usar garrafas, esperar turno y no bloquear ni reducir el suministro de la población. Tratar para consumo.",
            ),
            (
                "Hôtel Oasis Oriental Club, Tambacounda · 13.775100, -13.692100",
                "<strong>Agua y duchas publicadas; llenado condicionado.</strong> Alojamiento activo con acceso camper. "
                + a("https://park4night.com/en/place/112064", "ficha reciente"),
                "Confirmar acceso y precio; apoyo antes/después del eje oriental, no garantía sin llamada.",
            ),
        ],
        "plan": (
            "<h3>Descartes que evitan una falsa seguridad</h3><ul class=\"ticks\"><li>El antiguo grifo de Rufisque "
            "(14.710600, -17.434300) figura sin agua: no se incorpora al mapa.</li><li>Wassadou tiene duchas, pero "
            "reseñas recientes niegan el llenado de depósito; tampoco es un anclaje.</li></ul>"
        ),
        "points": [
            {"name": "Agua de servicio · Zebrabar (Saint-Louis)", "cat": "Agua de servicio", "lat": 15.8649, "lon": -16.512,
             "info": "[CONDICIONAL] Duchas y camping verificados; pedir permiso explícito para llenar los depósitos. No asumir potabilidad.", "source": "https://en.zebrabar.net/"},
            {"name": "Agua de servicio · Café Romantique (Rufisque)", "cat": "Agua de servicio", "lat": 14.7285, "lon": -17.2556,
             "info": "[CONDICIONAL] Agua corriente y duchas en recinto pequeño; precontactar, confirmar altura aproximada de 4 m, plaza y permiso de llenado.", "source": "https://park4night.com/en/place/674597"},
            {"name": "Agua de servicio · tuberías de Hamdallai Diapaldi (N7)", "cat": "Agua de servicio", "lat": 13.4457, "lon": -13.4317,
             "info": "[PUNTO PÚBLICO REPORTADO] Tres tuberías con caudal, usadas por la comunidad. Prioridad absoluta a residentes: esperar turno, llenar con garrafas sin bloquear y tratar antes de beber.", "source": "https://park4night.com/en/place/568817"},
            {"name": "Agua de servicio · Oasis Oriental Club (Tambacounda)", "cat": "Agua de servicio", "lat": 13.7751, "lon": -13.6921,
             "info": "[CONDICIONAL] Alojamiento con agua, duchas y acceso camper publicados. Contactar para confirmar acceso de dos 4x4, precio y autorización de llenado.", "source": "https://park4night.com/en/place/112064"},
        ],
        "sources": [
            ["Zebrabar · servicios oficiales", "https://en.zebrabar.net/"],
            ["park4night · Zebrabar Saint-Louis", "https://park4night.com/en/place/50392"],
            ["park4night · Café Romantique Rufisque", "https://park4night.com/en/place/674597"],
            ["park4night · agua pública Hamdallai Diapaldi", "https://park4night.com/en/place/568817"],
            ["park4night · Oasis Oriental Club Tambacounda", "https://park4night.com/en/place/112064"],
        ],
    },
    "gambia": {
        "intro": (
            "<h3>Agua de servicio: costa y corredor oriental</h3>"
            "<p>Se retira la afirmación de que los hoteles de Kotu/Kololi permiten llenar con manguera. "
            "Hay agua en varias instalaciones, pero el acceso del vehículo se confirma caso por caso.</p>"
        ),
        "rows": [
            (
                "Camping Sukuta · 13.419300, -16.715400",
                "<strong>Duchas, depósitos de agua y zona de lavado.</strong> La información del alojamiento acredita esos servicios, no el llenado automático del coche. "
                + a("https://www.accessgambia.com/hotelweb/camping-sukuta.html", "servicios")
                + " · "
                + a("https://park4night.com/en/place/172124", "estado reciente"),
                "Contactar y pedir permiso de manguera/garrafas; usar como base de ducha en la costa.",
            ),
            (
                "Kachadulaa Beach · 13.341300, -16.811700",
                "<strong>Recarga de depósito publicada.</strong> La ficha de 2026 indica manguera de ducha y agua algo salada para llenar depósitos. "
                + a("https://park4night.com/en/place/661636", "ficha"),
                "Solo agua de servicio; no introducirla en el circuito potable. Acceso a la zona baja para 4x4.",
            ),
            (
                "Tendaba Camp · 13.439200, -15.809100",
                "<strong>Duchas y agua; llenado condicionado.</strong> Comentarios recientes confirman actividad, con estado/precios variables. "
                + a("https://park4night.com/en/place/557532", "ficha reciente"),
                "Llamar antes de salir de la costa y pedir cantidad concreta; llevar reserva hasta Soma.",
            ),
            (
                "Triple K Hotel · 13.290900, -14.206700",
                "<strong>Agua limpia y duchas publicadas; sin historial suficiente.</strong> Punto nuevo de 2026 con acceso asfaltado. "
                + a("https://park4night.com/de/place/663366", "ficha"),
                "Solo respaldo condicionado: confirmar que sigue abierto y que admite llenar depósitos.",
            ),
        ],
        "plan": (
            "<h3>Plan de tramo</h3><ul class=\"ticks\"><li>Kachadulaa es la única recarga de depósito explícitamente "
            "descrita, pero su agua es algo salada y solo sirve para uso general.</li><li>Sukuta, Tendaba y Triple K son "
            "instalaciones condicionadas: contactar antes y conservar una reserva que permita continuar si niegan el llenado.</li></ul>"
        ),
        "points": [
            {"name": "Agua de servicio · Camping Sukuta", "cat": "Agua de servicio", "lat": 13.4193, "lon": -16.7154,
             "info": "[CONDICIONAL] Duchas, depósitos y lavado publicados. Contactar y pedir autorización expresa para llenar los vehículos; no asumir potabilidad.", "source": "https://www.accessgambia.com/hotelweb/camping-sukuta.html"},
            {"name": "Agua de servicio · Kachadulaa Beach", "cat": "Agua de servicio", "lat": 13.3413, "lon": -16.8117,
             "info": "[RECARGA PUBLICADA] Agua algo salada para llenar depósitos y manguera de ducha. Solo uso general, nunca circuito potable; acceso inferior para 4x4.", "source": "https://park4night.com/en/place/661636"},
            {"name": "Agua de servicio · Tendaba Camp", "cat": "Agua de servicio", "lat": 13.4392, "lon": -15.8091,
             "info": "[CONDICIONAL] Duchas y agua disponibles, pero el llenado no está garantizado y las condiciones varían. Llamar antes y pedir cantidad/precio.", "source": "https://park4night.com/en/place/557532"},
            {"name": "Agua de servicio · Triple K Hotel", "cat": "Agua de servicio", "lat": 13.2909, "lon": -14.2067,
             "info": "[RESPALDO CONDICIONAL] Punto nuevo con agua, duchas y acceso asfaltado, todavía sin historial suficiente. Confirmar apertura y permiso de llenado.", "source": "https://park4night.com/de/place/663366"},
        ],
        "sources": [
            ["Access Gambia · servicios de Camping Sukuta", "https://www.accessgambia.com/hotelweb/camping-sukuta.html"],
            ["park4night · Camping Sukuta", "https://park4night.com/en/place/172124"],
            ["park4night · Kachadulaa Beach", "https://park4night.com/en/place/661636"],
            ["park4night · Tendaba Camp", "https://park4night.com/en/place/557532"],
            ["park4night · Triple K Hotel", "https://park4night.com/de/place/663366"],
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

    found = False
    for section in data["custom_sections"]:
        if section[0] == "agua-combustible":
            fuel = fuel_from(section[2])
            section[2] = cfg["intro"] + table(cfg["rows"]) + cfg["plan"] + fuel + COMMON
            found = True
            break
    if not found:
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

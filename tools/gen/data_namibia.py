# -*- coding: utf-8 -*-
"""Namibia — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Parque Nacional de Etosha", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 días",
         lat=-19.1667, lon=15.9167,
         desc="Una de las mejores reservas de fauna de África: la gran cuenca salina (pan) atrae elefantes, leones, rinocerontes y grandes manadas a los abrevaderos, muy visibles desde el propio vehículo. El perro no tiene acceso al parque bajo ninguna circunstancia.",
         credit="Olga Ernst · CC BY-SA 4.0", source=W + "Elephants%20at%20waterhole%2C%20Etosha%20National%20Park%2C%20Namibia.jpg?width=900"),
    dict(n=2, name="Swakopmund", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-22.6783, lon=14.5267,
         desc="Ciudad costera de arquitectura colonial alemana en plena puerta del Skeleton Coast; mejor oferta de talleres y recambios del tramo namibio tras Windhoek, y base para excursiones a las dunas y a la colonia de focas de Cape Cross.",
         credit="Daniel Kraft · CC BY-SA 3.0", source=W + "Swakopmund%20panorama%20from%20mole%2020190522.jpg?width=900"),
    dict(n=3, name="Sossusvlei y Dune 45", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–2 días",
         lat=-24.7333, lon=15.8000,
         desc="Las dunas de arena naranja más altas y fotografiadas del planeta, en el corazón del desierto del Namib; amanecer en Dune 45 y la arcilla blanca agrietada de Deadvlei como referencia visual del país.",
         credit="Giles Laurent · CC BY-SA 4.0", source=W + "006%20Dune%2045%20in%20Sossusvlei%20at%20sunrise%20Photo%20by%20Giles%20Laurent.jpg?width=900"),
    dict(n=4, name="Cañón del río Fish (Fish River Canyon)", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 día",
         lat=-27.5833, lon=17.6167,
         desc="El segundo cañón más grande del mundo tras el Gran Cañón; miradores accesibles en coche sobre el borde del desfiladero, último gran hito namibio antes de cruzar a Sudáfrica.",
         credit="Thomas Schoch · CC BY-SA 3.0", source=W + "Fish%20River%20Canyon%20Namibia.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Oshikango (desde Angola, Santa Clara)", "Frontera", -17.3833, 15.8833,
     "Paso ágil, operativo 24h; complejo con instalaciones para ambos países en la misma zona. Pagar el Cross-Border Charge (CBC) del vehículo en la oficina de la Road Fund Administration del puesto."),
    ("Frontera · Salida — Vioolsdrif/Noordoewer (hacia Sudáfrica)", "Frontera", -28.7167, 17.7333,
     "Paso principal hacia Sudáfrica, operativo 24h; desde el 1 de junio de 2026, Sudáfrica exige declarar el vehículo extranjero en el sistema SARS/TMS antes de cruzar (ver alerta)."),
    ("Embajada de España en Windhoek", "Consular", -22.5667, 17.0833,
     "58 Simeon Shixungileni Street, Windhoek. Tel. +264 (0)61 22 30 66 · Emergencia consular 24h: +264 85 128 0571 · emb.windhoek@maec.es."),
    ("Windhoek Central Hospital", "Hospital", -22.5750, 17.0833,
     "Principal hospital de referencia del país. Coordenada urbana aproximada."),
    ("Combustible · Windhoek / Swakopmund", "Combustible", -22.6783, 14.5267,
     "Mejor oferta y calidad del país (Engen, Puma, Total); repostar a fondo en ambas antes de los tramos largos del desierto."),
    ("Combustible · Solitaire (ruta a Sossusvlei) / Sesriem", "Combustible", -23.8667, 16.0000,
     "Único punto de repostaje formal en el eje hacia Sossusvlei — considerado un clásico de la ruta namibia; no depender de encontrar otra opción en el tramo."),
    ("Agua potable y de uso general · Windhoek y Swakopmund", "Agua potable", -22.6783, 14.5267,
     "Agua del grifo potable en las principales ciudades (raro en el continente); estaciones de servicio, campings y lodges de todo el país permiten llenar el depósito de uso general con manguera — la infraestructura turística namibia está pensada para vehículos propios."),
]

DRONE_CALLOUT = ("ok", "Registro y autorización simples, entre los más accesibles del continente",
                  "Namibia permite el registro de drones de uso turístico ante la Namibia Civil Aviation Authority (NCAA) con un procedimiento relativamente simple comparado con el resto del corredor. Aun así, no volar dentro de los parques nacionales (Etosha, Namib-Naukluft) sin autorización específica del Ministerio de Medio Ambiente, ni cerca de aeropuertos o zonas militares.")

STARLINK_CALLOUT = ("warn", "Licencia denegada — bloqueado por requisitos de propiedad local",
                     "La autoridad reguladora namibia denegó a Starlink la licencia de telecomunicaciones el 31 de marzo de 2026 por no cumplir los requisitos de propiedad local (ninguna acción en manos de ciudadanos namibios). El servicio NO está disponible legalmente en el país a mediados de 2026, y el uso de un kit registrado en otro país como «roaming» permanente incumple las condiciones de Starlink y puede ser suspendido. Mantener SIM local (MTC, TN Mobile) como base y valorar mensajería satelital (InReach) como respaldo independiente.")

DOG_MATRIX = [
    ("Parque Nacional de Etosha", "prohibido", "Dejar el perro en Windhoek o Swakopmund con cuidador, o planificar el parque con rotación entre los viajeros."),
    ("Sossusvlei, Fish River Canyon", "permitido con condiciones", "Correa y sombra; calor extremo del desierto durante el día, agua siempre disponible."),
    ("Swakopmund y ciudades", "permitido con condiciones", "Sin restricciones específicas conocidas; clima costero más suave."),
]

SOURCES = [
    ("WhirledAway · cruce de frontera Angola (Santa Clara) / Namibia (Oshikango)", "https://whirled-away.com/crossing-border-angola-namibia/"),
    ("Road Fund Administration Namibia · Cross-Border Charges (CBC)", "https://www.rfanam.com.na/cbc-cross-border-charges/"),
    ("VisaGo · requisitos de visado de Namibia para ciudadanos españoles", "https://visago.dev/visa/namibia/from-spain/"),
    ("Embajada de España en Windhoek · contacto", "https://www.embassypages.com/spain-embassy-windhoek-namibia"),
    ("Broadband Breakfast · denegación de licencia a Starlink en Namibia (2026)", "https://broadbandbreakfast.com/starlink-denied-license-in-namibia-over-local-ownership-requirements/"),
    ("Anywhere We Roam · guía de la Skeleton Coast", "https://anywhereweroam.com/driving-the-skeleton-coast/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(-17.3833, 15.8833), (-19.1667, 15.9167), (-22.6783, 14.5267), (-24.7333, 15.8000), (-27.5833, 17.6167), (-28.7167, 17.7333)]

HISTORIA_RESUMEN = ("Namibia fue escenario del primer genocidio del siglo XX, perpetrado por Alemania contra los pueblos herero y nama entre 1904 y 1908, y pasó después a ser administrada durante 75 años por Sudáfrica bajo un régimen que extendió allí su propio apartheid, "
                     "hasta lograr la independencia en 1990 como uno de los últimos países africanos en descolonizarse; hoy es uno de los países más estables, mejor gestionados y menos poblados del continente, con una economía basada en minería y en un turismo de naturaleza de primer nivel.")

HISTORIA_SECCIONES = [
    ("Pueblos san, herero y nama del suroeste africano",
     "El territorio, con algunos de los ecosistemas desérticos más antiguos del planeta (el Namib), fue hogar histórico de los pueblos san (bosquimanos), con una de las tradiciones culturales continuas más antiguas de la humanidad, junto con los herero y los nama, pastores organizados en confederaciones tribales en las tierras centrales y del sur."),
    ("El genocidio herero y nama (1904-1908)",
     "Alemania estableció la colonia del África del Suroeste Alemán en 1884; ante la rebelión de los pueblos herero y nama contra la expropiación de tierras y ganado, las tropas coloniales alemanas llevaron a cabo entre 1904 y 1908 una campaña de exterminio sistemático —incluyendo campos de concentración y la expulsión al desierto sin agua— que causó la muerte de decenas de miles de personas y es reconocido hoy como el primer genocidio del siglo XX, formalmente admitido por Alemania en 2021."),
    ("La administración sudafricana y el apartheid extendido",
     "Tras la derrota alemana en la Primera Guerra Mundial, el territorio pasó a ser administrado por Sudáfrica bajo mandato de la Sociedad de Naciones, que desde 1948 extendió allí su propio sistema de apartheid; la guerrilla independentista de la SWAPO libró una larga guerra de liberación contra la ocupación sudafricana desde 1966, en paralelo a la guerra civil angoleña vecina, hasta que las negociaciones internacionales condujeron a la independencia en 1990."),
    ("Situación actual: estabilidad, minería y conservación",
     "Namibia se independizó en 1990 bajo el liderazgo de Sam Nujoma y la SWAPO, que sigue gobernando el país en un marco democrático estable, con un notable modelo de conservación comunitaria de fauna salvaje que ha convertido a Namibia en referencia mundial de turismo de naturaleza sostenible (Etosha, Sossusvlei, la costa de los Esqueletos); la minería de diamantes y uranio, junto con la pesca y el turismo, sostienen una de las economías más estables de África, aunque con una de las desigualdades de renta más marcadas del planeta, herencia directa del reparto de tierra colonial."),
]

HISTORIA_FUENTES = [
    ("BBC News · Namibia country profile", "https://www.bbc.com/news/world-africa-13890726"),
    ("Deutsche Welle · reconocimiento alemán del genocidio herero-nama (2021)", "https://www.dw.com/en/germany-genocide-namibia/a-57813178"),
    ("Encyclopaedia Britannica · Namibia, History", "https://www.britannica.com/place/Namibia/History"),
]

SPEC = dict(
    slug="namibia", name="Namibia", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Oshikango (desde Angola)"),
        ("SALIDA", "Vioolsdrif/Noordoewer (hacia Sudáfrica)"),
        ("SEGURIDAD", "estable · precaución normal"),
        ("VEHÍCULO", "sin CPD obligatorio — Cross-Border Charge (CBC) en frontera"),
        ("STARLINK", "bloqueado por requisitos de propiedad local — no disponible"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[-23.0, 16.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Namibia es, con Sudáfrica, el país mejor preparado para el turismo en vehículo propio de todo el corredor: carreteras en buen estado, infraestructura de campings y estaciones de servicio pensada para overlanders, "
                   "y algunos de los paisajes más icónicos del planeta —Etosha, las dunas de Sossusvlei, la costa de los Esqueletos y el cañón del río Fish— antes de llegar a Sudáfrica, el punto de giro del viaje."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Angola y antes de Sudáfrica."),
        ("Entrada", "Oshikango desde Angola: paso ágil, operativo 24h."),
        ("Salida", "Vioolsdrif/Noordoewer hacia Sudáfrica: operativo 24h, con el nuevo trámite SARS/TMS desde junio de 2026."),
        ("Visado", "Visado a la llegada para pasaportes españoles desde abril de 2025 — confirmar vigencia y condiciones antes de viajar."),
        ("Vehículo", "CPD no obligatorio: permiso temporal (Cross-Border Charge, CBC) pagado en la propia frontera."),
        ("Seguridad", "Estable en todo el país, precaución normal; sin zonas excluidas."),
        ("Comunicaciones", "Starlink bloqueado por la reguladora namibia (marzo 2026); SIM local (MTC, TN Mobile) como base."),
    ],
    alerts=[
        "Etosha: perro prohibido en el parque sin excepción — planificar cuidado en Windhoek o Swakopmund antes de la visita.",
        "Starlink: licencia denegada por la reguladora namibia en marzo de 2026 por requisitos de propiedad local — no dar por hecho el servicio ni usar un kit «roaming» de otro país de forma permanente, contraviene las condiciones de Starlink.",
        "Distancias del desierto: repostar siempre en Solitaire antes de Sossusvlei y llevar reserva de agua y combustible en cualquier desvío fuera del eje principal.",
    ],
    ruta_intro="Descenso por el eje central y la costa del desierto del Namib hasta la frontera sudafricana.",
    route_rows=[
        ("Entrada y fauna", "Oshikango → Etosha", "Perro prohibido en el parque"),
        ("Costa del desierto", "Etosha → Swakopmund", "Skeleton Coast; mejor base de servicios tras Windhoek"),
        ("Dunas icónicas", "Swakopmund → Solitaire → Sossusvlei", "Repostar en Solitaire; amanecer en Dune 45"),
        ("Hacia Sudáfrica", "Sossusvlei → Fish River Canyon → Vioolsdrif", "Último gran hito namibio; nuevo trámite SARS/TMS antes de cruzar"),
    ],
    offroad=[
        "Pista de Sesriem a Sossusvlei: los últimos km hasta Deadvlei requieren arena suelta — tracción 4x4 recomendable, o transbordo en el shuttle del parque si se prefiere no arriesgar.",
        "Skeleton Coast: pistas de grava bien señalizadas pero con reflejo intenso y distancias largas entre servicios; planificar combustible con margen.",
    ],
    acampada=[
        "Etosha: campamentos del parque (Okaukuejo, Namutoni, Halali) con cercado perimetral y abrevadero iluminado de noche.",
        "Sossusvlei/Sesriem: camping oficial dentro del parque, con acceso más temprano a las dunas al amanecer.",
        "Red de campings y lodges en todo el país, la más desarrollada del corredor para vehículos propios.",
    ],
    visado=[
        "Visado a la llegada para ciudadanos españoles desde abril de 2025; confirmar vigencia y duración exacta 30-60 días antes de viajar.",
        "Certificado internacional de fiebre amarilla exigido si se llega desde un país con riesgo (confirmar aplicabilidad según el itinerario previo).",
    ],
    fronteras_rows=[
        ("Entrada", "Oshikango (Angola)", "Paso ágil operativo 24h; complejo conjunto para ambos países."),
        ("Salida", "Vioolsdrif/Noordoewer (Sudáfrica)", "Operativo 24h; desde junio de 2026 exige declaración previa del vehículo en el sistema SARS/TMS de Sudáfrica."),
    ],
    vehiculos=[
        "CPD no obligatorio: pagar el Cross-Border Charge (CBC) en la oficina de la Road Fund Administration de la propia frontera de entrada.",
        "Llevar el CPD igualmente si se dispone de él, útil para el resto de fronteras del corredor y como respaldo documental.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registrar el dron ante la NCAA namibia: procedimiento comparativamente simple respecto al resto del corredor.",
        "No volar dentro de Etosha ni del Namib-Naukluft (incluida la zona de Sossusvlei) sin autorización específica del Ministerio de Medio Ambiente.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio no disponible legalmente a mediados de 2026 tras la denegación de licencia de marzo; revisar si hay apelación resuelta 30-60 días antes de viajar.",
        "SIM local (MTC, TN Mobile) como conectividad principal; considerar mensajería satelital (InReach) como respaldo independiente dada la falta de Starlink.",
    ],
    perro_intro=[
        "Permiso de importación veterinario previo obligatorio — tramitarlo con antelación suficiente antes de la entrada.",
        "Certificado veterinario internacional reciente y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en el norte del país (incluida la zona de Etosha): profilaxis a valorar con Sanidad Exterior según la época del año.",
        "Agua del grifo potable en las principales ciudades, poco habitual en el resto del corredor — buena oportunidad para descansar del protocolo de potabilización.",
        "Windhoek Central Hospital como mejor referencia hospitalaria de todo el tramo hasta Sudáfrica; seguro con evacuación médica igualmente imprescindible en el desierto.",
    ],
    seguridad_intro="País estable con precaución normal en todo el itinerario previsto; el mejor tramo de infraestructura y seguridad vial del corredor hasta ahora.",
    seguridad=[
        "Sin zonas excluidas por seguridad en el tramo previsto.",
        "Extremar la gestión de agua y combustible en los desvíos del desierto (Sossusvlei, Skeleton Coast): el riesgo aquí es logístico, no de seguridad personal.",
        "Revisar el nuevo trámite SARS/TMS de Sudáfrica con suficiente antelación antes de llegar a Vioolsdrif.",
    ],
    agua=[
        "Windhoek y Swakopmund: agua del grifo potable, poco habitual en el resto del corredor.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): la red de campings y lodges de todo el país está pensada para vehículos propios y permite llenar el depósito sin problema; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje principal: Oshikango → Etosha (~120 km) → Swakopmund (~350 km) → Solitaire/Sossusvlei (~280 km) → Fish River Canyon (~470 km) → Vioolsdrif (~180 km).",
        "Solitaire es el único punto de repostaje formal en el eje hacia Sossusvlei: no depender de encontrar otra opción en ese tramo.",
        "Buena calidad y red de estaciones (Engen, Puma, Total) en todo el país, la mejor del corredor hasta ahora junto con Sudáfrica.",
    ],
    pendientes=[
        ("Starlink", "Revisar si la apelación ante la reguladora namibia se ha resuelto antes de la entrada"),
        ("SARS/TMS", "Prepararse para el nuevo trámite de declaración del vehículo antes de cruzar a Sudáfrica"),
        ("Etosha", "Planificar el cuidado del perro durante la visita al parque"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Windhoek, 24h): +264 85 128 0571 · Embajada: +264 (0)61 22 30 66.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Yibuti — ficha completa (9 sep 2026): puerto clave de la alternativa marítima al corredor de Sudán."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Yibuti ciudad y el puerto", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=11.5721, lon=43.1456,
         desc="Capital y único gran centro urbano del país, con el puerto de Doraleh y el histórico muelle colonial como referencia logística clave del proyecto: aquí se gestiona el envío marítimo del vehículo hacia Egipto o Europa dado el bloqueo del corredor de Sudán.",
         credit="Uvceto · CC BY-SA 4.0", source=W + "Jetty%20of%20the%20Port%20of%20Djibouti.jpg?width=900"),
    dict(n=2, name="Lac Assal", cat="Naturaleza", prio="Alta", dog="no recomendado", time="1 día (excursión)",
         lat=11.6600, lon=42.4100,
         desc="El punto más bajo de África (155 m bajo el nivel del mar) y uno de los lagos más salados del planeta, en pleno desierto volcánico de Afar; paisaje lunar de costras de sal blanca sobre aguas turquesa.",
         credit="Charles Fred (flickr) · CC BY-SA 3.0", source=W + "DjiboutiLacAssal.jpg?width=900"),
    dict(n=3, name="Lac Abbé", cat="Naturaleza", prio="Media", dog="no recomendado", time="1–2 noches",
         lat=11.1667, lon=41.8000,
         desc="Paisaje geotérmico de chimeneas de piedra caliza humeantes en la frontera con Etiopía, escenario de ciencia ficción y de la vida pastoral afar; acceso por pista, mejor con guía local.",
         credit="Rolf Cosar · CC BY 3.0", source=W + "Lac%20Abbe-01.JPG?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Galafi (desde Etiopía)", "Frontera", 11.4667, 41.9333,
     "Puesto principal del corredor comercial Adís Abeba-Yibuti; bien transitado y equipado, comparte trazado con el ferrocarril de mercancías."),
    ("Puerto de Doraleh / Puerto de Yibuti — envío marítimo del vehículo", "Frontera", 11.5928, 43.0794,
     "Punto de embarque del vehículo hacia Egipto (vía Arabia Saudí en tránsito) o directamente hacia Europa en RoRo/contenedor; gestionar con un agente de envíos con semanas de antelación — ver la decisión de ruta de la ficha de Sudán."),
    ("Embajada de España en Adís Abeba (competente para Yibuti)", "Consular", 9.0280, 38.7600,
     "Haile Melekot Street, Gullele Subcity, Addis Abeba (Etiopía). Tel. +251 111222542 · Emergencia consular 24h: +251 911 219 403. Yibuti no tiene embajada española propia; gestiones ordinarias por esta vía."),
    ("Hôpital Général Peltier, Yibuti ciudad", "Hospital", 11.5850, 43.1450,
     "Principal hospital de referencia del país; capacidad limitada — seguro con evacuación médica real imprescindible."),
    ("Combustible · Yibuti ciudad", "Combustible", 11.5721, 43.1456,
     "Única concentración fiable de estaciones formales del país; repostar a fondo aquí antes de cualquier excursión a Lac Assal o Lac Abbé, sin garantía de suministro en el resto del territorio."),
    ("Agua potable y de uso general · Yibuti ciudad", "Agua potable", 11.5721, 43.1456,
     "Agua embotellada sin problema en supermercados de la capital; hoteles permiten llenar el depósito de uso general con manguera. Fuera de la capital (Lac Assal, Lac Abbé), llevar reserva completa: no hay puntos fiables en el desierto de Afar."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria dado el contexto militar y portuario",
                  "Yibuti alberga varias bases militares extranjeras (Francia, EE. UU., China, Japón) y un puerto estratégico de primer orden, lo que hace muy sensible cualquier vuelo de dron cerca de estas instalaciones. Norma del proyecto: tramitar autorización previa ante la autoridad de aviación civil y no volar en ningún caso cerca del puerto, de la ciudad de Yibuti o de instalaciones militares.")

STARLINK_CALLOUT = ("warn", "Sin fecha prevista de licencia a mediados de 2026",
                     "Yibuti figura entre los países africanos sin fecha prevista de aprobación de licencia para Starlink a mediados de 2026. Tratar como no disponible y llevar SIM local (Djibouti Telecom) como conectividad principal.")

DOG_MATRIX = [
    ("Lac Assal y Lac Abbé", "no recomendado", "Calor extremo del desierto de Afar (uno de los lugares más calurosos del planeta) incompatible con llevar mascota en excursión; dejar en el vehículo con sombra en Yibuti ciudad o con cuidador."),
    ("Yibuti ciudad", "permitido con condiciones", "Correa y sombra; calor húmedo intenso todo el año, extremar precauciones al mediodía."),
]

SOURCES = [
    ("Overlanding Association · Shipping around Ethiopia (envío marítimo desde Yibuti)", "https://overlandingassociation.org/overland-wiki/shipping-around-ethiopia/"),
    ("Embajada de España en Adís Abeba · contacto (competente para Yibuti)", "https://www.exteriores.gob.es/Embajadas/addisabeba/es/Embajada/Paginas/Contacto.aspx"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("PetTravel.com · requisitos de importación de mascotas a Yibuti", "https://www.petholidayclub.com/pet-travel-guide/djibouti/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
]

CORRIDOR = [(11.4667, 41.9333), (11.5721, 43.1456), (11.5928, 43.0794), (11.6600, 42.4100), (11.1667, 41.8000)]

HISTORIA_RESUMEN = ("Yibuti debe su existencia a su posición en la boca del mar Rojo: puesto comercial afar y somalí convertido en colonia francesa en 1896 precisamente para controlar esa ruta marítima, "
                     "obtuvo la independencia en 1977 y hoy vive de esa misma posición estratégica —puerto, base logística internacional y, para este viaje, la salida marítima que sustituye al bloqueado corredor de Sudán.")

HISTORIA_SECCIONES = [
    ("Pueblos afar e issa en la boca del mar Rojo",
     "Antes de la colonización, la actual Yibuti era territorio de pastores nómadas afar (relacionados con los pueblos de las tierras altas etíopes) y de clanes somalíes issa, organizados en sultanatos y jefaturas tradicionales que controlaban las rutas de caravanas de sal y ganado entre el interior africano y el mar Rojo."),
    ("La Costa Francesa de los Somalíes",
     "Francia estableció un protectorado en 1862 sobre Obock y fundó la ciudad de Yibuti en 1888, atraída por su bahía natural profunda, justo enfrente de la colonia británica de Adén, en la orilla arábiga. "
     "En 1896 el territorio se formalizó como colonia de la Costa Francesa de los Somalíes, y en 1917 el ferrocarril Yibuti-Adís Abeba convirtió al puerto en la salida marítima natural de la Etiopía interior, sin costa propia — el mismo papel que cumple hoy para este proyecto."),
    ("Independencia en 1977",
     "Tras dos referendos (1958 y 1967) en los que la población optó por seguir vinculada a Francia, Yibuti alcanzó finalmente la independencia en 1977, bajo el liderazgo de Hassan Gouled Aptidon, en un delicado equilibrio político entre las comunidades afar e issa que marcó las décadas siguientes, incluida una guerra civil interna entre 1991 y 1994."),
    ("Situación actual: la geografía como destino",
     "Yibuti ha convertido su posición geográfica en su principal activo económico: alberga bases militares de Francia, Estados Unidos, China y Japón —una concentración única en el mundo— y su puerto, ampliado en las últimas décadas, "
     "es la salida marítima de facto de Etiopía y un nodo clave del comercio del mar Rojo. Para este proyecto, esa misma infraestructura portuaria es la que permite sortear el bloqueo del corredor de Sudán y enviar el vehículo hacia Egipto o Europa por mar."),
]

HISTORIA_FUENTES = [
    ("BBC News · Djibouti country profile", "https://www.bbc.com/news/world-africa-13232162"),
    ("Encyclopaedia Britannica · Djibouti, History", "https://www.britannica.com/place/Djibouti/History"),
    ("Overlanding Association · Shipping around Ethiopia", "https://overlandingassociation.org/overland-wiki/shipping-around-ethiopia/"),
]

SPEC = dict(
    slug="yibuti", name="Yibuti", revision="9 sep 2026",
    sub="Ruta overland · puerto clave de la alternativa a Sudán · documentación · logística",
    chips=[
        ("ENTRADA", "Galafi (desde Etiopía)"),
        ("SALIDA", "Puerto de Yibuti/Doraleh — envío marítimo del vehículo"),
        ("SEGURIDAD", "estable · precaución normal"),
        ("VEHÍCULO", "CPD recomendado; trámite clave: el envío marítimo, no el CPD"),
        ("COMUNICACIONES", "Starlink sin fecha prevista"),
        ("ROL EN LA RUTA", "puerto de salida hacia Egipto/Europa por el bloqueo de Sudán"),
    ],
    center=[11.5, 42.5], zoom=8,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y confirmar la reserva del envío marítimo con antelación suficiente.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("Yibuti es la pieza clave de la alternativa marítima que este proyecto adopta ante el bloqueo del corredor terrestre de Sudán (ver la ficha de Sudán): en lugar de continuar hacia el norte por tierra, "
              "el vehículo se embarca en el puerto de Yibuti (o en el vecino Doraleh) en un envío RoRo o en contenedor con destino a Egipto —en tránsito por Arabia Saudí— o directamente a Europa, mientras la tripulación vuela por separado. "
              "Esta decisión convierte a Yibuti, un país pequeño y a menudo solo de paso, en una etapa logística central del regreso: conviene reservar el envío marítimo con varias semanas de antelación a través de un agente de carga especializado en vehículos, "
              "y aprovechar la estancia para visitar el Lac Assal y el Lac Abbé, dos de los paisajes más singulares de todo el itinerario."),
    facts=[
        ("Ventana prevista", "Puerto de embarque del vehículo tras la decisión de excluir el corredor de Sudán."),
        ("Entrada", "Galafi desde Etiopía, por el corredor comercial Adís Abeba-Yibuti."),
        ("Salida", "Puerto de Yibuti/Doraleh, por mar, no por una frontera terrestre."),
        ("Seguridad", "País estable, con fuerte presencia militar internacional por su posición estratégica en el mar Rojo."),
        ("Vehículo", "CPD recomendado como respaldo documental, pero el trámite determinante es la reserva del envío marítimo con un agente de carga."),
        ("Comunicaciones", "Starlink sin fecha prevista de licencia; SIM local imprescindible."),
    ],
    alerts=[
        "Envío marítimo: reservarlo con varias semanas de antelación; los espacios en RoRo/contenedor hacia Egipto o Europa pueden agotarse o retrasarse.",
        "Lac Assal y Lac Abbé: temperaturas extremas del desierto de Afar — llevar agua de sobra, salir temprano y evitar el mediodía.",
        "Dron: no volar cerca del puerto, la ciudad de Yibuti o instalaciones militares sin autorización previa por escrito.",
    ],
    ruta_intro="Entrada por Galafi, base logística y de gestión del envío marítimo en la capital, y dos excursiones de paisaje volcánico (Lac Assal, Lac Abbé) antes de embarcar el vehículo hacia Egipto o Europa.",
    route_rows=[
        ("Entrada y logística", "Galafi → Yibuti ciudad", "Gestión del envío marítimo con agente de carga"),
        ("Paisaje volcánico", "Yibuti ciudad → Lac Assal", "Excursión de un día; punto más bajo de África"),
        ("Paisaje geotérmico", "Yibuti ciudad → Lac Abbé", "1-2 noches; chimeneas calizas junto a la frontera etíope"),
        ("Embarque", "Yibuti ciudad → Puerto de Doraleh", "Embarque del vehículo; tripulación vuela por separado"),
    ],
    offroad=[
        "Pistas de tierra y arena hacia Lac Assal y, especialmente, Lac Abbé (recomendable con guía local o 4x4 de apoyo); el resto del eje (Galafi-Yibuti ciudad) es carretera asfaltada.",
    ],
    acampada=[
        "Yibuti ciudad: hoteles con aparcamiento vigilado; base recomendada mientras se gestiona el envío marítimo.",
        "Lac Abbé: campamentos rústicos junto al lago, gestionados por comunidades afar; sin infraestructura moderna.",
    ],
    visado=[
        "e-Visa disponible para ciudadanos españoles, tramitar online con antelación.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica (aplica viniendo de Etiopía).",
    ],
    fronteras_rows=[
        ("Entrada", "Galafi (Etiopía)", "Corredor comercial principal Adís Abeba-Yibuti; puesto bien equipado."),
        ("Salida", "Puerto de Yibuti/Doraleh", "Embarque marítimo del vehículo, no cruce fronterizo terrestre."),
    ],
    vehiculos=[
        "CPD recomendado como respaldo documental durante la estancia en el país, aunque el trámite decisivo es la reserva del envío marítimo.",
        "Contratar el envío (RoRo o contenedor) con un agente de carga especializado en vehículos con varias semanas de antelación; confirmar puerto de destino (Alejandría) y tránsito por Arabia Saudí si aplica.",
        "Seguro de terceros local obligatorio durante la estancia en Yibuti.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Tramitar autorización previa ante la autoridad de aviación civil de Yibuti antes de volar.",
        "No volar en ningún caso cerca del puerto, la ciudad de Yibuti o instalaciones militares (varias bases extranjeras en el país).",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Sin fecha prevista de licencia a mediados de 2026: tratar como no disponible.",
        "SIM local (Djibouti Telecom) como conectividad principal, con cobertura limitada fuera de la capital.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente y vacuna antirrábica en vigor, exigibles en frontera.",
        "No recomendado en las excursiones a Lac Assal y Lac Abbé por el calor extremo; dejar en el vehículo con sombra en Yibuti ciudad o con cuidador.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Calor extremo todo el año, especialmente en el interior desértico (Lac Assal, Lac Abbé): hidratación reforzada y evitar esfuerzo físico al mediodía.",
        "Malaria presente en algunas zonas: profilaxis a valorar con Sanidad Exterior.",
        "Hôpital Général Peltier (Yibuti ciudad) como única referencia sanitaria seria del país; seguro con evacuación médica real imprescindible.",
    ],
    seguridad_intro="Yibuti es un país pequeño y estable, con fuerte presencia militar internacional que en la práctica refuerza la seguridad general del entorno urbano y portuario.",
    seguridad=[
        "Precaución normal de viaje en Yibuti ciudad; sin alertas de seguridad activas relevantes para este proyecto.",
        "Evitar fotografiar instalaciones militares o portuarias sin autorización explícita.",
        "En las excursiones a Lac Assal y Lac Abbé, salir siempre con depósito de combustible y agua completos y, si es posible, con guía o vehículo de apoyo.",
    ],
    agua=[
        "Yibuti ciudad: agua embotellada sin problema en supermercados.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): hoteles de Yibuti ciudad permiten llenar el depósito con manguera. Antes de Lac Assal o Lac Abbé, cargar el depósito a tope: no hay puntos fiables en el desierto de Afar.",
    ],
    combustible=[
        "Yibuti ciudad concentra la única oferta fiable de combustible del país; repostar a fondo aquí antes de cualquier excursión.",
        "Sin garantía de suministro entre Yibuti ciudad y Lac Assal (~120 km) o Lac Abbé (~150 km): llevar reserva en jerricán para el trayecto de ida y vuelta.",
    ],
    pendientes=[
        ("Envío marítimo", "Reservar el RoRo/contenedor con un agente de carga con varias semanas de antelación"),
        ("CPD", "Confirmar si se mantiene como respaldo documental durante la estancia"),
        ("Dron", "Tramitar autorización previa si se quiere volar fuera de zonas sensibles"),
        ("Excursiones", "Confirmar guía o vehículo de apoyo para Lac Abbé"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. La logística del envío marítimo debe cerrarse con antelación suficiente.",
    emergency="Emergencia consular española (vía Embajada en Adís Abeba, 24h): +251 911 219 403.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

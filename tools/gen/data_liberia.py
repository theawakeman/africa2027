# -*- coding: utf-8 -*-
"""Liberia — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Monrovia (Providence Island y West Point)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=6.3156, lon=-10.8074,
         desc="Capital y única gran base logística: puerto, aeropuerto (Roberts Intl., a ~1 h), bancos y talleres. Providence Island, cuna histórica del asentamiento, y el barrio densísimo de West Point como referencia urbana.",
         credit="Mark Fischer · CC BY-SA 2.0", source=W + "An%20aerial%20view%20of%20the%20West%20Point%20area%20of%20Monrovia.jpg?width=900"),
    dict(n=2, name="Robertsport", cat="Costa · surf", prio="Media", dog="permitido", time="1–2 días",
         lat=6.7500, lon=-11.3667,
         desc="Península de Cape Mount, meca del surf en África Occidental, playas extensas y poco masificadas, y el Centro Tubman de Cultura Africana. Buen punto de descanso cerca de la frontera con Sierra Leona.",
         credit="Bethel. Anthony Chisom · CC BY-SA 4.0", source=W + "Robertsport%20Beach%2C%20Cape%20Mount%20County.jpg?width=900"),
    dict(n=3, name="Parque Nacional de Sapo", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 días",
         lat=5.4000, lon=-8.8000,
         desc="Segunda mayor selva primaria continua de África Occidental tras Taï; hipopótamo pigmeo, elefante de bosque y chimpancés. Acceso por pista larga desde Greenville; solo con guía del parque y autorización previa. El perro no puede entrar en el área protegida.",
         credit="Raimond Spekking · CC BY-SA 4.0", source=W + "Zwergflusspferd%20-%20Pygmy%20Hippopotamus%20-%20Hexaprotodon%20liberiensis.jpg?width=900"),
    dict(n=4, name="Reserva Estricta del Monte Nimba (lado liberiano)", cat="Naturaleza · frontera", prio="Media", dog="requiere autorización escrita", time="½–1 día",
         lat=7.5500, lon=-8.5000,
         desc="Macizo montañoso compartido con Guinea y Costa de Marfil, reserva UNESCO de alta biodiversidad; el acceso turístico regulado es limitado y depende de la zona (núcleo vs. periferia). Confirmar con la Forestry Development Authority antes de desviarse de la carretera principal.",
         credit="Guy Debonnet · CC BY-SA 3.0 IGO", source=W + "Mount%20Nimba%20Strict%20Nature%20Reserve-108453.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "costa · surf": "turquesa", "naturaleza": "verde", "naturaleza · frontera": "verde"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Bo-Waterside/Jendema (desde Sierra Leona)", "Frontera", 6.8500, -11.2500,
     "Puesto operativo 08:00-18:00 con tráfico comercial denso (camiones y buses); control de inmigración liberiano. Reservar margen de tiempo por congestión."),
    ("Frontera · Salida — Loguatuo/Ganta (hacia Costa de Marfil, vía Danané)", "Frontera", 7.2833, -8.1667,
     "Paso principal hacia el oeste de Costa de Marfil desde Ganta; confirmar estado de la vía y horarios antes de salir."),
    ("Embajada de España en Abidjan (cobertura de Liberia)", "Consular", 5.3600, -3.9700,
     "Impasse Ablaha Pokou, Cocody Danga Nord, Abiyán. +225 22 44 48 50 · emb.abidjan@maec.es. Sin embajada española en Monrovia desde 1990."),
    ("John F. Kennedy Medical Center — Monrovia", "Hospital", 6.2900, -10.7600,
     "Principal hospital de referencia del país; capacidad limitada para politraumatismos graves. Coordenada urbana aproximada."),
    ("Combustible · Monrovia", "Combustible", 6.3156, -10.8074,
     "Mejor oferta y calidad del país (Total, ExxonMobil/Liberia Petroleum); repostar aquí antes de tramos hacia el interior."),
    ("Combustible · Ganta", "Combustible", 7.2333, -8.9833,
     "Última ciudad grande con estaciones formales antes de la frontera de Loguatuo hacia Costa de Marfil."),
    ("Agua potable · Monrovia (supermercados y garrafas)", "Agua potable", 6.3156, -10.8074,
     "Agua embotellada disponible en la capital; fuera de Monrovia, tratar o hervir el agua local, especialmente cerca de Sapo."),
]

DRONE_CALLOUT = ("warn", "Sin procedimiento turístico claro: tratar como restringido",
                  "No se ha localizado normativa pública específica para visitantes con dron en Liberia. Solicitar autorización previa por escrito a la Autoridad de Aviación Civil de Liberia (LCAA) o, en su defecto, no volarlo, especialmente cerca de Monrovia, el aeropuerto Roberts y zonas gubernamentales.")

STARLINK_CALLOUT = ("ok", "Starlink activo en el país (verificar cobertura exacta antes de entrar)",
                     "Liberia figura entre los mercados africanos con servicio Starlink activo a mediados de 2026. Puede usarse como respaldo, sin sustituir la SIM local (Orange, Lonestar/MTN) en zonas urbanas. Revisar el mapa oficial 30-60 días antes.")

DOG_MATRIX = [
    ("Parque Nacional de Sapo (zona núcleo)", "prohibido", "Dejar el perro en Monrovia/Robertsport con cuidador o rotación entre los viajeros durante la visita al parque."),
    ("Reserva del Monte Nimba (zona núcleo)", "requiere autorización escrita", "Confirmar con la Forestry Development Authority antes de desviarse de la carretera principal."),
    ("Monrovia, Robertsport, resto del país", "permitido con condiciones", "Correa y sombra; tráfico denso en Monrovia."),
]

SOURCES = [
    ("Digital Logistics Capacity Assessment · frontera de Bo-Waterside", "https://lca.logcluster.org/2315-liberia-border-crossing-bo-waterside-sierra-leone"),
    ("Wikipedia · Embajada de España en Liberia (cerrada desde 1990, cobertura desde Abidjan)", "https://es.wikipedia.org/wiki/Embajada_de_Espa%C3%B1a_en_Liberia"),
    ("Embajada de España en Abidjan · consulados y demarcación", "https://www.exteriores.gob.es/Embajadas/abidjan/es/Embajada/Paginas/Consulados.aspx"),
    ("Entrybrief · requisitos de mascotas en Liberia", "https://entrybrief.com/pets/liberia/"),
    ("tech.africa · disponibilidad de Starlink en África (2026)", "https://tech.africa/starlink-africa/"),
    ("UNESCO · Reserva Estricta del Monte Nimba", "https://whc.unesco.org/en/list/155/"),
    ("Wikivoyage · Liberia", "https://en.wikivoyage.org/wiki/Liberia"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(6.8500, -11.2500), (6.7500, -11.3667), (6.3156, -10.8074), (5.4000, -8.8000), (7.5500, -8.5000), (7.2833, -8.1667)]

HISTORIA_RESUMEN = ("Liberia es un caso único en África: nunca fue colonia europea, sino un estado fundado en 1847 por antiguos esclavos afroamericanos liberados, reasentados con apoyo de sociedades de colonización estadounidenses; esa élite américo-liberiana gobernó "
                     "durante más de un siglo sobre la mayoría indígena, un desequilibrio que desembocó en un golpe de Estado en 1980 y en dos guerras civiles devastadoras (1989-2003) de las que el país, aún entre los más pobres del mundo, sigue recuperándose.")

HISTORIA_SECCIONES = [
    ("Un proyecto de colonización afroamericana",
     "La Sociedad Americana de Colonización, con apoyo de figuras políticas estadounidenses, comenzó a reasentar en la costa liberiana desde 1822 a antiguos esclavos y afroamericanos libres, con la idea (controvertida incluso entonces) de que el regreso a África era la solución al problema racial en Estados Unidos; los colonos fundaron Monrovia, nombrada en honor al presidente estadounidense James Monroe."),
    ("Independencia en 1847 y el dominio américo-liberiano",
     "Liberia se declaró independiente en 1847, convirtiéndose en la primera república de África, pero el poder quedó concentrado en manos de la minoría américo-liberiana (descendientes de los colonos), que gobernó durante 133 años bajo un único partido, el True Whig Party, marginando política y económicamente a los pueblos indígenas mayoritarios del interior."),
    ("El golpe de Samuel Doe y las guerras civiles",
     "En 1980 el sargento Samuel Doe derrocó y ejecutó al presidente en un golpe sangriento que puso fin al dominio américo-liberiano, pero abrió una etapa de gobierno autoritario e inestabilidad étnica que degeneró en 1989 en la primera guerra civil liberiana, liderada por Charles Taylor, y después en una segunda guerra (1999-2003); el conflicto combinado dejó alrededor de 250.000 muertos y quedó marcado por el uso masivo de niños soldado."),
    ("Situación actual: reconstrucción y la primera presidenta electa de África",
     "Tras el fin de la guerra en 2003 y una misión de paz de la ONU, Liberia eligió en 2005 a Ellen Johnson Sirleaf, la primera mujer elegida jefa de Estado en África, que lideraría la reconstrucción hasta 2018 (Nobel de la Paz en 2011). El país afrontó después el brote de ébola de 2014-2016, uno de los más letales de su historia, y mantiene hoy una democracia frágil pero funcional, con Monrovia como centro logístico y comercial del eje costero."),
]

HISTORIA_FUENTES = [
    ("BBC News · Liberia country profile", "https://www.bbc.com/news/world-africa-13729504"),
    ("Encyclopaedia Britannica · Liberia, History", "https://www.britannica.com/place/Liberia/History"),
    ("Nobel Prize · Ellen Johnson Sirleaf", "https://www.nobelprize.org/prizes/peace/2011/johnson_sirleaf/facts/"),
]

SPEC = dict(
    slug="liberia", name="Liberia", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Bo-Waterside/Jendema (desde Sierra Leona)"),
        ("SALIDA", "Loguatuo/Ganta (hacia Costa de Marfil)"),
        ("SEGURIDAD", "estable · precaución normal"),
        ("FRONTERA TERRESTRE", "operativa en ambos extremos"),
        ("VISADO", "visado previo — verificar para españoles"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[6.4, -9.8], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Liberia se atraviesa entrando desde Sierra Leona por Bo-Waterside y saliendo hacia Costa de Marfil por Ganta-Loguatuo. "
                   "El interés combina Monrovia como base logística, Robertsport como parada de costa y surf, y dos áreas naturales de interés — "
                   "Sapo (selva primaria) y el macizo de Nimba (patrimonio UNESCO compartido) — con restricciones distintas para el perro."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Sierra Leona."),
        ("Entrada", "Bo-Waterside/Jendema desde Sierra Leona; puesto con tráfico comercial denso."),
        ("Salida", "Ganta → Loguatuo hacia Danané (Costa de Marfil)."),
        ("Visado", "Confirmar visado previo para pasaporte español; certificado de fiebre amarilla obligatorio."),
        ("Seguridad", "Estable, sin conflicto activo; precaución normal en carreteras rurales."),
        ("Comunicaciones", "Starlink activo en el país; SIM local (Orange, Lonestar/MTN) en ciudades."),
    ],
    alerts=[
        "Sin embajada de España en Monrovia desde 1990: la Embajada en Abidjan es la referencia consular para cualquier incidencia grave.",
        "Sapo NP: perro prohibido en la zona núcleo — planificar cuidado o rotación antes de la visita.",
        "Certificado de fiebre amarilla exigido en frontera, sin excepciones.",
    ],
    ruta_intro="Tramo de oeste a este; el desvío a Sapo exige tiempo y pista larga desde Greenville.",
    route_rows=[
        ("Entrada y costa", "Bo-Waterside → Robertsport", "Descanso de costa cerca de la frontera"),
        ("Monrovia", "Capital y servicios", "Provisiones, trámites, talleres antes del interior"),
        ("Selva de Sapo (opcional)", "Greenville → Sapo NP", "Bloque largo en pista; solo con guía y autorización"),
        ("Hacia Costa de Marfil", "Ganta → Loguatuo → Danané", "Confirmar estado de la vía antes de salir"),
    ],
    offroad=[
        "Pista de acceso a Sapo NP desde Greenville: tramos de tierra irregular, más exigente en temporada de lluvias (mayo-octubre).",
        "Entorno de Nimba: pistas secundarias hacia la periferia de la reserva, transitables en 4x4 en estación seca.",
    ],
    acampada=[
        "Robertsport: alojamientos sencillos orientados al surf con acceso para vehículo; opción más práctica que la acampada libre.",
        "Monrovia: aparcamiento vigilado recomendado por la densidad urbana.",
    ],
    visado=[
        "Confirmar 30-60 días antes si Liberia exige visado previo o eVisa para pasaporte español.",
        "Certificado internacional de fiebre amarilla obligatorio para la entrada.",
    ],
    fronteras_rows=[
        ("Entrada", "Bo-Waterside/Jendema (Sierra Leona)", "Tráfico comercial denso; reservar margen de tiempo."),
        ("Salida", "Ganta → Loguatuo (Costa de Marfil, vía Danané)", "Confirmar estado de la vía y horarios antes de salir."),
    ],
    vehiculos=[
        "CPD recomendado; laissez-passer temporal en frontera como alternativa.",
        "Carte Brune (CEDEAO) como seguro de responsabilidad civil regional.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa a la LCAA o no volar el dron en el país ante la falta de procedimiento turístico claro.",
        "Evitar sobrevolar Monrovia, el aeropuerto Roberts y edificios gubernamentales.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo confirmado a mediados de 2026: revisar el mapa oficial 30-60 días antes.",
        "SIM local (Orange, Lonestar/MTN) como respaldo en ciudades.",
    ],
    perro_intro=[
        "Sin normativa pública detallada localizada para Liberia: aplicar pasaporte UE de mascota, microchip y certificado antirrábico vigente, y confirmar por escrito antes de viajar.",
        "Sapo NP: perro prohibido en la zona núcleo. Nimba: requiere autorización escrita de la Forestry Development Authority.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado obligatorio para entrar.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "Seguro con evacuación médica: la capacidad hospitalaria fuera de Monrovia es muy limitada.",
    ],
    seguridad_intro="País estable desde el fin de la guerra civil, sin conflicto activo; precaución general y atención al estado de las carreteras rurales.",
    seguridad=[
        "Evitar desplazamientos nocturnos fuera de Monrovia.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
        "Revisar el aviso de Exteriores 72 h antes de entrar.",
    ],
    agua=[
        "Monrovia: agua embotellada en supermercados; fuera de la capital, tratar o hervir el agua local.",
        "Entorno de Sapo NP: sin fuente potable fiable en la pista de acceso, llevar reserva completa desde Greenville.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles de Monrovia y Robertsport permiten llenar el depósito; fuera de estas dos poblaciones no dar por hecho ningún punto fiable, salir con el depósito lleno.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km: Bo-Waterside → Monrovia (~180 km) → Ganta (~260 km) → Loguatuo cubren el tramo con estaciones formales en las ciudades principales.",
        "El desvío a Sapo NP (Greenville) añade un tramo largo en pista sin estaciones: repostar a fondo en Monrovia o Buchanan antes de bajar.",
        "Confirmar puntos recientes en iOverlander antes de tramos rurales.",
    ],
    pendientes=[
        ("Visado", "Confirmar requisito y modalidad (previo/eVisa) 30-60 días antes"),
        ("Sapo NP", "Reservar guía y autorización con antelación; planificar cuidado del perro"),
        ("Nimba", "Confirmar con la Forestry Development Authority el acceso permitido"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía 911 (variable según región, verificar localmente). Emergencia consular española (Abidjan): +225 22 44 48 50.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

# -*- coding: utf-8 -*-
"""Gabón — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Libreville (Boulevard de l'Indépendance)", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=0.4162, lon=9.4673,
         desc="Capital y única gran base logística del país: puerto, aeropuerto internacional, embajada de España, talleres y recambios. Ciudad extendida a lo largo del estuario del Gabón, con el bulevar de la Indépendance como referencia urbana.",
         credit="Delrick Trevor · CC BY-SA 4.0", source=W + "Boulevard%20de%20l'indépendance%20Libreville%20.jpg?width=900"),
    dict(n=2, name="Parque Nacional de Loango", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 días",
         lat=-1.9500, lon=9.5500,
         desc="El «último Edén de África»: selva, sabana y playa atlántica en el mismo paisaje, con elefantes de bosque, búfalos, hipopótamos y gorilas visibles desde la costa. Acceso limitado (avioneta o pista larga desde Port-Gentil/Gamba) y solo con operador autorizado; el perro no tiene acceso al parque.",
         credit="Kurt Dundy · CC BY 3.0", source=W + "Gabon%20Loango%20National%20Park%20Elephant%20with%20offspring.jpeg?width=900"),
    dict(n=3, name="Lambaréné (Hospital y Museo Albert Schweitzer)", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=-0.7000, lon=10.2333,
         desc="Ciudad sobre el río Ogooué donde Albert Schweitzer fundó su hospital en 1913; el museo conserva su vivienda y consultorio originales. Buen punto de descanso a mitad de camino entre Libreville y el sur del país.",
         credit="David Stanley · CC BY 2.0", source=W + "Albert%20Schweitzer%20Museum%20(46282656671).jpg?width=900"),
    dict(n=4, name="Mayumba (laguna de Banio)", cat="Naturaleza", prio="Media", dog="permitido", time="1 día",
         lat=-3.4167, lon=10.6500,
         desc="Ciudad costera en el extremo suroeste, junto al Parque Nacional de Mayumba, con la mayor concentración de puestas de tortuga laúd de África; la laguna de Banio separa la lengua de arena del continente. Último punto notable antes de cruzar a Congo-Brazzaville.",
         credit="Vincent.vaquin · CC BY-SA 3.0", source=W + "Mayumba%20remorqueur%20lagune.jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "cultura": "marron"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Ambam/Bitam (desde Camerún) o Kyé-Ossi (desde la zona de las tres fronteras)", "Frontera", 2.0833, 11.4833,
     "Zona de las tres fronteras Camerún-Gabón-Guinea Ecuatorial; carretera asfaltada desde Yaundé, fuera de las áreas de conflicto camerunesas."),
    ("Frontera · Salida — Doussala/Ndendé (hacia Congo-Brazzaville)", "Frontera", -2.8333, 10.9167,
     "Paso principal hacia Dolisie; carretera asfaltada en el lado gabonés, confirmar estado de la pista en el lado congoleño antes de salir."),
    ("Embajada de España en Libreville", "Consular", 0.3936, 9.4550,
     "Immeuble Diamant, 2º piso, Bd. de la Nation (cruce con Rue Dr. Cureau), B.P. 1157, Libreville. Tel. +241 (0)11 72 12 64 · Emergencia consular: +241 (0)66 44 47 47. También acreditada en Santo Tomé y Príncipe (no en Congo-Brazzaville)."),
    ("Centre Hospitalier Universitaire de Libreville", "Hospital", 0.4247, 9.4142,
     "Principal hospital universitario y de referencia del país. Coordenada urbana aproximada."),
    ("Combustible · Libreville", "Combustible", 0.4162, 9.4673,
     "Mejor oferta y calidad del país (Total, Petro Gabon); repostar a fondo antes del tramo largo hacia el sur."),
    ("Combustible · Lambaréné / Mayumba", "Combustible", -0.7000, 10.2333,
     "Estaciones formales en el eje sur; confirmar disponibilidad real en Mayumba, última plaza antes de Congo-Brazzaville."),
    ("Agua potable y de uso general · Libreville", "Agua potable", 0.4162, 9.4673,
     "Agua embotellada sin problema en supermercados; estaciones de servicio y hoteles de Libreville y Lambaréné permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria: tratar como restringido",
                  "Gabón no publica un procedimiento civil turístico simple y estable para drones; la Agence Nationale de l'Aviation Civile (ANAC-Gabon) exige autorización previa. Norma prudente del proyecto: no volar sin permiso escrito, y en ningún caso en el Parque Nacional de Loango ni cerca de instalaciones petroleras de la costa (Gamba, Port-Gentil).")

STARLINK_CALLOUT = ("warn", "Anunciado para 2026, aún no activo a mediados de año: tratar como no disponible",
                     "Gabón figura entre los mercados africanos con Starlink previsto («coming in 2026») pero sin confirmación de servicio activo a mediados de 2026. Tratarlo como no disponible hasta confirmación oficial y mantener SIM local (Airtel Gabon, Moov) como conectividad principal.")

DOG_MATRIX = [
    ("Parque Nacional de Loango", "prohibido", "Dejar el perro en Libreville con cuidador o rotación; el parque solo se visita con operador autorizado y sin mascotas."),
    ("Libreville, Lambaréné, Mayumba", "permitido con condiciones", "Correa y sombra; calor húmedo intenso en toda la costa."),
]

SOURCES = [
    ("Amazing Gabon · formalidades de entrada", "https://www.amazinggabon.com/en/advice-and-formalities/"),
    ("Take Your Backpack · guía del Parque Nacional de Loango (2026)", "https://www.takeyourbackpack.com/backpacking-in-gabon/visit-loango-national-park/"),
    ("Embajada de España en Libreville · contacto", "https://www.embassypages.com/spain-embassy-libreville-gabon"),
    ("BNCR · Carte Rose CEMAC, portal oficial", "https://bncr.cm/en/"),
    ("tech.africa · disponibilidad de Starlink en África (2026)", "https://tech.africa/starlink-africa/"),
    ("UNESCO · ecosistema y paisaje cultural de Lopé-Okanda (referencia regional)", "https://whc.unesco.org/en/list/1147/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(2.0833, 11.4833), (0.4162, 9.4673), (-0.7000, 10.2333), (-1.9500, 9.5500), (-3.4167, 10.6500), (-2.8333, 10.9167)]

HISTORIA_RESUMEN = ("Gabón es un país pequeño y muy boscoso (más del 85% de su territorio es selva) que la abundancia de petróleo convirtió en uno de los de mayor renta per cápita de África continental, gobernado sin embargo durante 56 años por una sola familia, los Bongo, "
                     "hasta que un golpe de Estado militar puso fin a esa dinastía en agosto de 2023, tras una disputada reelección del presidente Ali Bongo.")

HISTORIA_SECCIONES = [
    ("Pueblos bantúes y el mito de la reina Ngwe",
     "El territorio fue poblado por sucesivas migraciones de pueblos bantúes —fang, myene, punu, entre otros— organizados en pequeños reinos y jefaturas forestales, con tradiciones espirituales como el bwiti, un culto iniciático centrado en la raíz de iboga que sigue practicándose hoy y es objeto de interés espiritual internacional."),
    ("Libreville, colonia de esclavos liberados y colonia francesa",
     "Libreville («ciudad libre») fue fundada en 1849 por Francia como asentamiento de esclavos liberados de un barco negrero capturado, un origen paralelo al de Freetown en Sierra Leona; el territorio se convirtió después en colonia francesa de plena explotación maderera (okoumé) dentro del África Ecuatorial Francesa."),
    ("Independencia y la era Bongo",
     "Gabón se independizó en 1960. Tras un breve periodo bajo Léon M'ba, Omar Bongo asumió la presidencia en 1967 y gobernó hasta su muerte en 2009, instaurando un régimen de partido único (después multipartidista de fachada) sostenido por la riqueza petrolera y una relación muy estrecha con Francia; a su muerte, el poder pasó a su hijo Ali Bongo."),
    ("Situación actual: el golpe de 2023 y el fin de la dinastía Bongo",
     "En agosto de 2023, horas después de que Ali Bongo fuera proclamado vencedor de una reelección ampliamente cuestionada, un grupo de oficiales militares dio un golpe de Estado y puso fin a 56 años de gobierno de la familia Bongo, instaurando una transición militar que ha prometido, con escepticismo internacional, un retorno a elecciones civiles; Gabón sigue siendo, pese a la riqueza petrolera, un país con fuertes desigualdades y gran parte de su selva ecuatorial intacta, un activo creciente para el turismo de naturaleza."),
]

HISTORIA_FUENTES = [
    ("BBC News · Gabon country profile", "https://www.bbc.com/news/world-africa-13376333"),
    ("Encyclopaedia Britannica · Gabon, History", "https://www.britannica.com/place/Gabon/History"),
    ("Reuters · golpe de Estado en Gabón, agosto de 2023", "https://www.reuters.com/world/africa/"),
]

SPEC = dict(
    slug="gabon", name="Gabón", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Kyé-Ossi (zona tres fronteras, desde Camerún)"),
        ("SALIDA", "Doussala/Ndendé (hacia Congo-Brazzaville)"),
        ("SEGURIDAD", "estable · precaución normal"),
        ("SEGURO", "zona CEMAC · Carte Rose"),
        ("NATURALEZA", "Loango, el «último Edén de África»"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[-1.0, 10.3], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Gabón ofrece el primer gran respiro del proyecto tras el tramo de mayor exigencia de seguridad (Nigeria-Camerún): selva ecuatorial casi intacta, "
                   "el Parque Nacional de Loango con playas donde conviven elefantes e hipopótamos, el legado de Albert Schweitzer en Lambaréné y la laguna de Mayumba antes de cruzar a Congo-Brazzaville. "
                   "País estable, con Libreville como única gran base logística."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Camerún y antes de Congo-Brazzaville."),
        ("Entrada", "Zona de las tres fronteras (Camerún-Gabón-Guinea Ecuatorial), fuera de áreas de conflicto."),
        ("Salida", "Doussala/Ndendé hacia Congo-Brazzaville, hacia Dolisie."),
        ("Seguridad", "Estable en todo el país, precaución normal; sin zonas excluidas."),
        ("Seguro", "Zona CEMAC (misma que Camerún): Carte Rose válida en todo el tramo Gabón-Congo-Brazzaville."),
        ("Comunicaciones", "Starlink anunciado para 2026, no confirmado activo; SIM local (Airtel Gabon, Moov) como base."),
    ],
    alerts=[
        "Parque Nacional de Loango: acceso solo con operador autorizado (avioneta o pista larga); no intentar el acceso por cuenta propia sin confirmar el estado de la pista y la reserva con antelación.",
        "Dron: sin procedimiento civil turístico claro — tratar como restringido y no volar sin autorización previa por escrito, en ningún caso cerca de instalaciones petroleras costeras.",
    ],
    ruta_intro="Tramo forestal y costero entre la frontera camerunesa y la de Congo-Brazzaville, con Libreville como eje.",
    route_rows=[
        ("Entrada y capital", "Kyé-Ossi → Libreville", "Base logística única; embajada española"),
        ("Naturaleza emblemática", "Libreville → Loango NP", "Solo con operador autorizado; playa y selva con megafauna"),
        ("Legado histórico", "Libreville → Lambaréné", "Hospital y museo de Albert Schweitzer"),
        ("Hacia Congo-Brazzaville", "Lambaréné → Mayumba → Doussala", "Laguna de Banio y tortugas laúd antes de la frontera"),
    ],
    offroad=[
        "Acceso a Loango: pista de tierra desde Gamba o Port-Gentil, transitable solo en temporada seca y preferiblemente con guía local — confirmar con el operador del parque antes de intentarlo con vehículo propio.",
    ],
    acampada=[
        "Libreville: alojamientos con parking vigilado.",
        "Loango: solo campamentos del operador autorizado, sin acampada libre dentro del parque.",
        "Lambaréné y Mayumba: pequeños hoteles con aparcamiento.",
    ],
    visado=[
        "Visado electrónico (e-Visa) gabonés previo obligatorio para ciudadanos españoles; tramitar con antelación.",
        "Certificado internacional de fiebre amarilla exigido en frontera.",
    ],
    fronteras_rows=[
        ("Entrada", "Zona de las tres fronteras (Camerún)", "Carretera asfaltada desde Yaundé; fuera de zonas de conflicto."),
        ("Salida", "Doussala/Ndendé (Congo-Brazzaville)", "Hacia Dolisie; confirmar estado de la pista en el lado congoleño."),
    ],
    vehiculos=[
        "CPD con todos los pares de sellos en regla.",
        "Carte Rose CEMAC como seguro de responsabilidad civil regional, ya válida desde Camerún.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa por escrito a la ANAC-Gabon antes de intentar introducir el dron en el país.",
        "No volar en Loango ni cerca de instalaciones petroleras de la costa (Gamba, Port-Gentil).",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Estado no confirmado a mediados de 2026 pese al anuncio de llegada dentro del año: revisar el mapa oficial 30-60 días antes.",
        "SIM local (Airtel Gabon, Moov) como conectividad principal en Libreville y el eje sur.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio para la entrada.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "CHU de Libreville como referencia hospitalaria del tramo; seguro con evacuación médica imprescindible dada la escasa infraestructura sanitaria fuera de la capital.",
    ],
    seguridad_intro="País estable con precaución normal en todo el itinerario previsto; primer tramo sin exclusiones de seguridad desde Ghana.",
    seguridad=[
        "Sin zonas excluidas por seguridad en el tramo previsto.",
        "Extremar la organización logística del acceso a Loango: es la parte técnicamente más exigente del país, no por inseguridad sino por aislamiento y falta de infraestructura.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
    ],
    agua=[
        "Libreville y Lambaréné: agua embotellada en supermercados sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles de Libreville, Lambaréné y Mayumba permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje principal: Kyé-Ossi → Libreville (~250 km) → Lambaréné (~250 km) → Mayumba (~350 km) → Doussala (~50 km), con estaciones formales en cada núcleo urbano.",
        "Repostar a fondo en Libreville y de nuevo en Mayumba: la oferta se vuelve más escasa cuanto más al sur, y es la última plaza formal antes de Congo-Brazzaville.",
    ],
    pendientes=[
        ("Loango", "Confirmar operador, pista de acceso y reserva con semanas de antelación"),
        ("Visado", "Tramitar el e-Visa gabonés con margen suficiente"),
        ("Dron", "Contactar con la ANAC-Gabon o descartar el vuelo en el país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Libreville): +241 (0)66 44 47 47 · Embajada: +241 (0)11 72 12 64.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

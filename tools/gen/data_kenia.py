# -*- coding: utf-8 -*-
"""Kenia — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Nairobi", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-1.2864, lon=36.8172,
         desc="Capital y mayor base logística del proyecto en el corredor de regreso: talleres especializados en vehículos de expedición, recambios, embajada de España y el único Parque Nacional del mundo pegado al perfil de una gran ciudad.",
         credit="Timothy A. Gonsalves · CC BY-SA (verificar términos de uso no comercial del autor)", source=W + "Nairobi%20Skyline%20Savannah%20Kenya%20May19%20R1600687.jpg?width=900"),
    dict(n=2, name="Parque Nacional de Amboseli", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=-2.6527, lon=37.2606,
         desc="Célebre por sus manadas de elefantes con el Kilimanjaro como telón de fondo; primer gran parque tras cruzar desde Tanzania por Namanga, con alojamientos justo a la entrada del parque.",
         credit="Ninaras · CC BY 4.0", source=W + "Amboseli%20National%20Park%20and%20Mt.%20Kilimanjaro.jpg?width=900"),
    dict(n=3, name="Nanyuki y el monte Kenia", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=0.0167, lon=37.0667,
         desc="Localidad sobre el ecuador geográfico a los pies del monte Kenia (segundo pico más alto de África); base de servicios y descanso en el eje norte hacia Isiolo y Marsabit, con buena oferta de talleres.",
         credit="Martin Kithinji Mwirigi · CC BY-SA 4.0", source=W + "View%20of%20Mt.%20Kenya%20from%20the%20Nanyuki%20Town.jpg?width=900"),
    dict(n=4, name="Parque Nacional de Marsabit", cat="Naturaleza", prio="Media", dog="prohibido", time="1 noche",
         lat=2.3167, lon=37.9833,
         desc="Oasis forestal de altitud en pleno desierto del norte de Kenia, con cráteres-lago (Lake Paradise) y fauna adaptada al bosque de niebla; última gran referencia natural antes del corredor desértico hacia Moyale y Etiopía.",
         credit="Nagarjun · CC BY 2.0", source=W + "Buffalos%20at%20Marsabit%20National%20Park.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Namanga (desde Tanzania)", "Frontera", -2.5450, 36.7867,
     "Paso principal del corredor norte, junto al Parque de Amboseli; puesto de alto tránsito turístico bien equipado. Alternativa: Taveta, más al sureste."),
    ("Frontera · Salida — Moyale (hacia Etiopía)", "Frontera", 3.5228, 39.0556,
     "Extremo norte del corredor desértico; carretera asfaltada (A2) completada en los últimos años, aunque la zona requiere revalidación de seguridad 30-60 días antes por el contexto fronterizo con Etiopía y Somalia."),
    ("Embajada de España en Nairobi", "Consular", -1.2977, 36.8129,
     "CBA Building, 3ª planta, Mara & Ragati Roads, Upper Hill, P.O. Box 45503-00100 Nairobi. Tel. +254 20 272 02 22/3/4/5 · Emergencia consular: +254 733 63 11 44."),
    ("Aga Khan University Hospital / Nairobi Hospital", "Hospital", -1.2667, 36.8083,
     "Referencia sanitaria de mayor nivel del corredor de regreso completo; buen momento para revisiones médicas antes del tramo final hacia Etiopía."),
    ("Combustible · Nairobi / Nanyuki / Isiolo", "Combustible", -1.2864, 36.8172,
     "Estaciones formales (Shell, TotalEnergies, Rubis) en todo el eje sur-norte hasta Isiolo; a partir de Marsabit, repostar a fondo antes del tramo desértico hacia Moyale."),
    ("Agua potable y de uso general · Nairobi", "Agua potable", -1.2864, 36.8172,
     "Agua embotellada sin problema en supermercados de Nairobi; talleres y campings de Nanyuki e Isiolo permiten llenar el depósito de uso general con manguera. En Marsabit y el corredor hacia Moyale, cargar el depósito a tope antes de salir de Isiolo."),
]

DRONE_CALLOUT = ("warn", "Registro y autorización previa obligatorios ante la KCAA",
                  "Kenia exige registro del dron y autorización previa de la Kenya Civil Aviation Authority (KCAA) para cualquier uso, incluido el recreativo; el Kenya Wildlife Service (KWS) añade restricciones adicionales dentro de los parques nacionales (Amboseli, Marsabit), donde en la práctica rara vez se autoriza a particulares. Norma prudente del proyecto: tramitar el registro KCAA con antelación y no volar dentro de los parques sin autorización específica del KWS.")

STARLINK_CALLOUT = ("warn", "Activo pero con nuevas altas restringidas — verificar disponibilidad antes de contar con él",
                     "Starlink está operativo en Kenia, pero ha llegado a pausar temporalmente nuevas altas en determinadas zonas por sobrecarga de capacidad de red; no dar por hecho que se pueda contratar o activar un kit sobre la marcha en el país. Confirmar el estado de las altas 30-60 días antes del viaje y llevar SIM local (Safaricom, Airtel Kenya) como respaldo garantizado en todo el corredor.")

DOG_MATRIX = [
    ("Amboseli y Marsabit", "prohibido", "No se permite el acceso de mascotas a las zonas de fauna de los parques nacionales; dejar con cuidador en Nairobi o Nanyuki."),
    ("Nairobi, Nanyuki, Isiolo", "permitido con condiciones", "Correa y sombra; clima templado en Nairobi y Nanyuki, más caluroso hacia Isiolo."),
]

SOURCES = [
    ("Embajada de España en Nairobi · contacto", "https://www.exteriores.gob.es/Embajadas/nairobi/en/Embajada/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("trip.com · transición de Kenia al sistema eTA (2024) y requisitos para todos los cruces terrestres", "https://sg.trip.com/blog/kenyaevisa/"),
    ("connectingafrica.com · pausa de nuevas altas de Starlink en Kenia", "https://www.connectingafrica.com/connectivity/starlink-halts-new-sign-ups-in-kenya"),
    ("Business Radar Kenya · guía de Carnet de Passage en Kenia", "https://www.businessradar.co.ke/blog/2024/09/30/how-to-get-a-carnet-de-passage-in-kenya-a-complete-guide/"),
    ("Overlanding Association · Kenia, wiki overland", "https://overlandingassociation.org/overland-wiki/kenya/"),
    ("Kenya Embassy Washington D.C. · requisitos de importación de mascotas (perros/gatos)", "https://kenyaembassydc.org/petimport/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(-2.5450, 36.7867), (-2.6527, 37.2606), (-1.2864, 36.8172), (0.0167, 37.0667), (2.3167, 37.9833), (3.5228, 39.0556)]

HISTORIA_RESUMEN = ("Kenia fue cuna de algunos de los restos humanos más antiguos del planeta y, siglos después, centro de la civilización comercial swahili en su costa; la colonización británica trajo consigo el reparto de tierras de las Tierras Altas "
                     "y la violenta guerra de los Mau Mau por la independencia, lograda en 1963 bajo Jomo Kenyatta. Hoy es la locomotora económica y logística de África oriental, con Nairobi como gran centro regional y una franja fronteriza con Somalia que este viaje evita por completo.")

HISTORIA_SECCIONES = [
    ("Cuna de la humanidad y la costa swahili",
     "El valle del Rift keniano ha aportado algunos de los hallazgos fósiles más importantes sobre el origen de la humanidad, con yacimientos como Koobi Fora y el trabajo de la familia Leakey. "
     "Milenios después, su costa índica —Mombasa, Malindi, Lamu— se integró en el mundo comercial swahili, con ciudades-estado que comerciaban marfil, oro y esclavos con Arabia, Persia e India; Lamu conserva hoy uno de los cascos históricos swahilis mejor preservados de África, declarado Patrimonio de la Humanidad."),
    ("Colonización británica y el reparto de las Tierras Altas",
     "Gran Bretaña estableció el Protectorado de África Oriental en 1895 y, atraída por el clima templado de las Tierras Altas centrales, expropió extensas tierras de los kikuyu y otros pueblos para asentar a colonos blancos dedicados al café y al té. "
     "Este despojo de tierras, unido a un sistema de trabajo forzado y restricciones raciales, sembró un resentimiento que marcaría toda la segunda mitad del siglo XX colonial."),
    ("El levantamiento Mau Mau y la independencia",
     "Entre 1952 y 1960, el movimiento armado Mau Mau, formado mayoritariamente por kikuyus, libró una insurgencia contra el dominio colonial y los colonos de las Tierras Altas. "
     "La represión británica fue extremadamente dura, con decenas de miles de personas internadas en campos de detención — episodio que Reino Unido reconoció y por el que pidió disculpas e indemnizó a supervivientes décadas después. "
     "Kenia alcanzó la independencia en 1963 bajo el liderazgo de Jomo Kenyatta, antiguo preso político devenido primer presidente del país."),
    ("Situación actual: locomotora regional y la frontera con Somalia",
     "Kenia se ha consolidado como la economía y el centro logístico, tecnológico y diplomático más importante de África oriental, con Nairobi como sede de agencias de la ONU y hub de startups del continente. "
     "El principal punto de fricción de seguridad del país es la frontera con Somalia, donde el grupo yihadista Al-Shabaab mantiene una actividad terrorista transfronteriza intermitente desde hace más de una década; "
     "por eso el itinerario de este viaje discurre siempre por el eje central Nairobi-Nanyuki-Isiolo-Marsabit-Moyale, lejos de esa franja fronteriza — ver la decisión de ruta de esta ficha."),
]

HISTORIA_FUENTES = [
    ("BBC News · Kenya country profile", "https://www.bbc.com/news/world-africa-13681341"),
    ("Encyclopaedia Britannica · Kenya, History", "https://www.britannica.com/place/Kenya/History"),
    ("UNESCO · Ciudad vieja de Lamu, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/1055/"),
    ("National Archives (Reino Unido) · documentación sobre la represión de los Mau Mau", "https://www.nationalarchives.gov.uk/"),
]

SPEC = dict(
    slug="kenia", name="Kenia", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Namanga/Taveta (desde Tanzania)"),
        ("SALIDA", "Moyale (hacia Etiopía)"),
        ("SEGURIDAD", "precaución · evitar zonas fronterizas con Somalia"),
        ("VISADO", "eTA obligatoria — tramitar con antelación"),
        ("VEHÍCULO", "CPD exigido en la práctica — imprescindible"),
        ("COMUNICACIONES", "Starlink activo con altas restringidas — verificar antes"),
    ],
    center=[0.5, 37.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("Kenia excluye de la ruta las zonas fronterizas con Somalia (condado de Mandera, franja este de Wajir y Garissa) por riesgo de terrorismo transfronterizo de Al-Shabaab, sin relación con el corredor previsto. "
              "El itinerario del proyecto sigue en cambio el eje central Namanga-Nairobi-Nanyuki-Isiolo-Marsabit-Moyale, que discurre por el centro y norte del país sin acercarse a la frontera somalí; el tramo Isiolo-Marsabit-Moyale es desértico y menos poblado, "
              "por lo que conviene reconfirmar el estado de seguridad de esta franja norte (contexto fronterizo con Etiopía) 30-60 días antes del viaje, igual que el resto de zonas sensibles del corredor de regreso."),
    facts=[
        ("Ventana prevista", "Cuarto país del corredor de regreso, tras Tanzania; base logística grande en Nairobi."),
        ("Entrada", "Namanga desde Tanzania, junto al Parque de Amboseli (alternativa: Taveta)."),
        ("Salida", "Moyale hacia Etiopía, extremo norte del corredor desértico."),
        ("Seguridad", "Zonas fronterizas con Somalia EXCLUIDAS del itinerario; el eje central Nairobi-Isiolo-Marsabit-Moyale queda fuera de esa franja pero requiere revalidación 30-60 días antes."),
        ("Visado", "eTA (autorización electrónica) obligatoria para todos los cruces, incluidos los terrestres; tramitar 48-72h o con hasta 14 días de antelación."),
        ("Vehículo", "CPD exigido en la práctica — imprescindible, no opcional."),
    ],
    alerts=[
        "Zona fronteriza con Somalia (Mandera, franja este de Wajir/Garissa): EXCLUIDA por riesgo de terrorismo — no forma parte de ninguna variante de la ruta.",
        "eTA obligatoria para TODOS los cruces, incluidos los terrestres de Namanga y Moyale: tramitarla antes de salir de Tanzania, no en la propia frontera.",
        "Starlink: ha pausado nuevas altas en algunas zonas por sobrecarga de red — confirmar disponibilidad real 30-60 días antes, no dar el servicio por garantizado.",
        "Perro prohibido en Amboseli y Marsabit: prever cuidador en Nairobi o Nanyuki antes de cada parque.",
    ],
    ruta_intro="Entrada por Namanga junto a Amboseli, base logística mayor del corredor en Nairobi, y ascenso por el eje central Nanyuki-Isiolo-Marsabit hasta el corredor desértico de salida por Moyale, evitando por completo la franja fronteriza con Somalia.",
    route_rows=[
        ("Entrada y fauna", "Namanga → Amboseli → Nairobi", "Elefantes con el Kilimanjaro de fondo; 2 noches en la capital"),
        ("Ecuador y monte Kenia", "Nairobi → Nanyuki → Isiolo", "Base de servicios antes del corredor desértico"),
        ("Corredor desértico", "Isiolo → Marsabit", "Repostar y cargar agua a fondo antes de salir de Isiolo"),
        ("Salida", "Marsabit → Moyale", "Extremo norte; revalidar seguridad 30-60 días antes"),
    ],
    offroad=[
        "El eje Namanga-Nairobi-Nanyuki-Isiolo-Marsabit-Moyale es carretera asfaltada (incluida la A2 hasta Moyale); pistas de safari solo dentro de Amboseli y Marsabit, con guía cuando el parque lo exija.",
    ],
    acampada=[
        "Nairobi: campings orientados a overlanders en las afueras (zona de Karen/Langata), con aparcamiento vigilado.",
        "Nanyuki e Isiolo: campings y lodges de tránsito con buena reputación entre viajeros de expedición.",
        "Marsabit: campamento del parque o alojamiento en el pueblo; cargar agua y combustible a fondo antes de este tramo.",
    ],
    visado=[
        "eTA (Electronic Travel Authorisation) obligatoria desde 2024 para todos los visitantes, incluidos los cruces terrestres: pasaporte, foto, billete de continuación, prueba de alojamiento y certificado de fiebre amarilla si aplica.",
        "Tramitar con 14 días de antelación cuando sea posible; procesamiento estándar de 48-72 horas.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica (aplica viniendo de Tanzania).",
    ],
    fronteras_rows=[
        ("Entrada", "Namanga (Tanzania)", "Paso de alto tránsito turístico junto a Amboseli; alternativa Taveta al sureste."),
        ("Salida", "Moyale (Etiopía)", "Extremo norte del corredor desértico; carretera A2 asfaltada, revalidar seguridad antes."),
    ],
    vehiculos=[
        "CPD exigido en la práctica en frontera terrestre — imprescindible, con todos los pares de sellos en regla.",
        "Seguro de terceros (COMESA) obligatorio, comprado en la frontera de entrada.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registrar el dron y tramitar autorización ante la KCAA con antelación suficiente.",
        "No volar dentro de Amboseli o Marsabit sin autorización específica del Kenya Wildlife Service (KWS).",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo en el país, pero con altas nuevas pausadas en algunas zonas por sobrecarga de red — confirmar disponibilidad real 30-60 días antes.",
        "SIM local (Safaricom, Airtel Kenya) como respaldo garantizado en todo el corredor, incluido el tramo desértico hacia Moyale.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente, vacuna antirrábica en vigor y permiso de importación previo, exigibles en frontera.",
        "Perro prohibido en Amboseli y Marsabit; prever cuidador en Nairobi o Nanyuki antes de cada parque.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en gran parte del territorio, con menor riesgo en Nairobi por altitud: profilaxis a valorar con Sanidad Exterior según el itinerario exacto.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Aga Khan University Hospital y Nairobi Hospital como mejores referencias sanitarias del corredor de regreso completo; aprovechar Nairobi para revisiones antes del tramo final hacia Etiopía.",
    ],
    seguridad_intro="Kenia combina un tramo central y logístico muy manejable (Nairobi-Nanyuki-Isiolo) con un extremo norte desértico que exige revalidación específica antes de cada viaje, manteniendo siempre la franja fronteriza con Somalia fuera de cualquier variante de ruta.",
    seguridad=[
        "No aproximarse en ningún caso a la franja fronteriza con Somalia (Mandera, este de Wajir/Garissa); fuera de cualquier variante del itinerario.",
        "Tramo Isiolo-Marsabit-Moyale: revalidar el estado de seguridad 30-60 días antes del viaje, especialmente el contexto fronterizo con Etiopía.",
        "Aparcamiento vigilado en Nairobi por prudencia estándar frente a la delincuencia oportunista habitual de grandes ciudades.",
        "En safari, seguir siempre las indicaciones del guía/ranger de Amboseli o Marsabit respecto a distancia con la fauna.",
    ],
    agua=[
        "Nairobi: agua embotellada sin problema en supermercados.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): talleres y campings de Nanyuki e Isiolo permiten llenar el depósito con manguera; en Marsabit y el tramo hacia Moyale, cargar el depósito a tope antes de salir de Isiolo por la escasez de puntos fiables en el desierto.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km hasta Isiolo: Namanga → Nairobi (~165 km) → Nanyuki (~200 km) → Isiolo (~80 km), todos con estaciones formales.",
        "Tramo Isiolo → Marsabit → Moyale (~530 km): repostar a fondo en Isiolo, ya que la oferta en Marsabit es limitada y entre Marsabit y Moyale (~250 km) no hay estaciones formales garantizadas — llevar reserva en jerricán.",
    ],
    pendientes=[
        ("eTA", "Tramitar antes de salir de Tanzania, con margen de 14 días si es posible"),
        ("Seguridad norte", "Revalidar Isiolo-Marsabit-Moyale 30-60 días antes del viaje"),
        ("Starlink", "Confirmar si las altas nuevas siguen pausadas en la ruta prevista"),
        ("Perro", "Confirmar cuidador en Nairobi/Nanyuki para Amboseli y Marsabit"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Nairobi): +254 733 63 11 44 · Embajada de España en Nairobi: +254 20 272 02 22/3/4/5.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

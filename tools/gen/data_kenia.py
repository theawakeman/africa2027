# -*- coding: utf-8 -*-
"""Kenia — ficha completa (12 sep 2026): punto más oriental, corredor doble."""
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
    dict(n=3, name="Lago Naivasha y monte Longonot", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-0.9144, lon=36.4461,
         desc="Primer gran alto del Valle del Rift saliendo de Nairobi: lago de agua dulce con hipopótamos y águilas pescadoras, alojamientos y campings en la orilla, y enfrente el cono perfecto del volcán Longonot, que se sube a pie en unas 4-5 horas para rodear todo el cráter por el borde. Al lado está Hell's Gate, el único parque de Kenia que se recorre a pie y en bicicleta entre cebras y jirafas, porque no tiene grandes depredadores.",
         credit="Wikimedia Commons", source=W + "A%20view%20of%20Lake%20Naivasha%20from%20Mt%20Longonot.jpg?width=900"),
    dict(n=4, name="Lago Nakuru · flamencos y rinocerontes", cat="Naturaleza", prio="Alta", dog="prohibido", time="1–2 noches",
         lat=-0.3667, lon=36.0833,
         desc="Lago alcalino del Rift famoso por sus bandadas masivas de flamencos (que fluctúan mucho según el nivel del agua) y por ser uno de los santuarios de rinoceronte blanco y negro más importantes de Kenia, con el añadido de los leones trepadores y las jirafas de Rothschild. Parque de categoría premium en la nueva tarifa del KWS: 90 USD por adulto y día.",
         credit="Wikimedia Commons", source=W + "Flamingos%2C%20Lake%20Nakuru.jpg?width=900"),
    dict(n=5, name="Lago Bogoria · géiseres y aguas termales", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=0.2500, lon=36.0833,
         desc="Reserva gestionada por el condado (no por el KWS, así que es más barata y más flexible) con géiseres y fumarolas que brotan en la propia orilla del lago, además de una de las mayores concentraciones de flamenco enano de África cuando las algas acompañan. El contraste de los chorros de vapor contra el agua rosa es de los paisajes más raros de Kenia.",
         credit="Wikimedia Commons", source=W + "Lake%20bogoria%20view.jpg?width=900"),
    dict(n=6, name="Nanyuki y el monte Kenia", cat="Naturaleza", prio="Alta", dog="permitido con condiciones", time="1–4 noches",
         lat=0.0167, lon=37.0667,
         desc="Localidad justo sobre el ecuador geográfico a los pies del monte Kenia, segundo pico más alto de África (5.199 m) y una de las grandes caminatas del continente: el pico Lenana (4.985 m) es accesible sin escalada técnica en 3-5 días por las rutas Sirimon, Chogoria o Naro Moru. Buena oferta de talleres y servicios, y puerta de las reservas privadas de Laikipia.",
         credit="Martin Kithinji Mwirigi · CC BY-SA 4.0", source=W + "View%20of%20Mt.%20Kenya%20from%20the%20Nanyuki%20Town.jpg?width=900"),
    dict(n=7, name="Reserva Nacional de Samburu", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=0.6000, lon=37.5333,
         desc="Al norte del ecuador, sobre el río Ewaso Ng'iro, es el mejor sitio del país para ver las llamadas «cinco especiales del norte», que no existen en los parques del sur: la cebra de Grevy, la jirafa reticulada, el gerenuk (el antílope que se pone de pie para comer), el oryx beisa y el avestruz somalí. Paisaje árido de acacias y palmeras doum, gestionado por el condado.",
         credit="Wikimedia Commons", source=W + "Male%20Somali%20ostrich%20walking%20through%20Samburu%20National%20Reserve%20landscape%2C%20Kenya.jpg?width=900"),
    dict(n=8, name="El bucle del norte: Marsabit, Chalbi y el lago Turkana", cat="Naturaleza", prio="Alta", dog="prohibido en el parque de Marsabit", time="7–10 días",
         lat=2.3167, lon=37.9833,
         desc="LA GRAN EXPEDICIÓN 4x4 DE KENIA, y la razón de llevar dos vehículos. Marsabit es un oasis de bosque de niebla con cráteres-lago (Lake Paradise) en pleno desierto; al oeste se abre el DESIERTO DE CHALBI, una llanura de sal y arena que es el único desierto verdadero del país; y más allá aparece el LAGO TURKANA, el «mar de jade», el lago desértico más grande del mundo, con la mayor densidad de cocodrilos del planeta y los yacimientos de homínidos de Koobi Fora. Pista rocosa durísima («como conducir por la luna», en palabras de un overlander que la hizo), gasóleo solo de bidón en Loiyangalani, y vuelta por Baragoi y Maralal.",
         credit="Nagarjun · CC BY 2.0", source=W + "Buffalos%20at%20Marsabit%20National%20Park.jpg?width=900"),
    dict(n=9, name="Reserva Nacional Masái Mara", cat="Naturaleza", prio="Alta", dog="prohibido", time="3 noches",
         lat=-1.4061, lon=35.0083,
         desc="La continuación keniana del Serengeti y el escenario del cruce del río Mara durante la gran migración (aproximadamente de julio a octubre). No depende del KWS sino del condado de Narok, con tarifas propias: 100 USD por persona y día de enero a junio, y 200 USD a partir de julio. Las conservancies privadas del contorno (Naboisho, Olare Motorogi, Mara North) son más caras pero permiten conducción nocturna y fuera de pista, algo prohibido en la reserva.",
         credit="Wikimedia Commons", source=W + "Maasai%20Mara%20National%20Reserve%20Kenya.jpg?width=900"),
    dict(n=10, name="Parque Nacional de Tsavo Oeste", cat="Naturaleza", prio="Alta", dog="prohibido", time="2 noches",
         lat=-3.0500, lon=38.0500,
         desc="Junto con Tsavo Este forma uno de los mayores espacios protegidos del mundo. El Oeste es el más variado: los manantiales de Mzima, donde se ven hipopótamos y peces desde una cámara sumergida; las coladas de lava de Shetani; la colina de Chaimu; y los elefantes rojos, teñidos por el polvo de laterita. Categoría wilderness del KWS: 80 USD por adulto y día.",
         credit="Wikimedia Commons", source=W + "View%20of%20the%20Tsavo%20River%20in%20Tsavo%20West%20National%20Park%20(edited).jpg?width=900"),
    dict(n=11, name="Mombasa y el Fuerte Jesús", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=-4.0632, lon=39.6797,
         desc="La gran ciudad suajili de la costa, con casi mil años de historia como puerto del Índico. El Fuerte Jesús, construido por los portugueses en 1593 y disputado durante siglos con los omaníes, es Patrimonio de la Humanidad; alrededor, la ciudad vieja conserva callejones, balcones tallados y puertas suajilis. Gran plaza logística de la costa.",
         credit="Wikimedia Commons", source=W + "Fort%20jesus%20mombasa.JPG?width=900"),
    dict(n=12, name="Diani Beach · el punto más oriental del viaje", cat="Costa", prio="Alta", dog="permitido con condiciones", time="3–4 noches",
         lat=-4.2769, lon=39.5906,
         desc="Arena blanca, agua turquesa y colobos rojos en los árboles de la playa: una de las mejores playas de África oriental y el LUGAR MÁS AL ESTE DE TODO EL VIAJE, el punto donde la ruta da la vuelta. Ambiente relajado, muchos alojamientos admiten perro y hay veterinarios cerca. El sitio natural para parar varios días, revisar los vehículos y celebrar el hito antes de empezar el regreso.",
         credit="Wikimedia Commons", source=W + "Diani%20Beach%2C%20Kenya%20-%2051984265786.jpg?width=900"),
    dict(n=13, name="Lamu", cat="Cultura", prio="Media", dog="no recomendado", time="2–3 noches",
         lat=-2.2717, lon=40.9020,
         desc="El casco histórico suajili mejor conservado de África oriental y Patrimonio de la Humanidad: una ciudad sin coches, de callejones estrechos, burros, dhows y puertas de madera tallada que son su seña de identidad. El problema es el acceso: queda muy al norte de la costa, se llega en barco desde el continente y la carretera de aproximación pasa cerca de la franja sensible del condado de Lamu. Valorar con la información de seguridad del momento.",
         credit="Wikimedia Commons", source=W + "Lamu%20Kenya-door.jpg?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado", "costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Namanga (desde Tanzania)", "Frontera", -2.5450, 36.7867,
     "Paso principal del corredor norte, junto al Parque de Amboseli; puesto de alto tránsito turístico bien equipado. Alternativa: Taveta, más al sureste."),
    ("Frontera · Salida — Lunga Lunga/Horohoro (hacia Tanzania)", "Frontera", -4.5583, 39.1167,
     "Paso COSTERO al sur de Diani, distinto del de entrada: puesto de ventanilla única moderno y abierto 24 horas, que enlaza directamente con Tanga y el corredor costero tanzano. Es la salida del punto más oriental del viaje y el inicio del regreso."),
    ("Moyale · frontera con Etiopía (FUERA de la ruta)", "Frontera", 3.5228, 39.0556,
     "Se mantiene como referencia informativa: la ruta confirmada NO continúa hacia el Cuerno de África. Desde Kenia el viaje da la vuelta y regresa por Tanzania."),
    ("Embajada de España en Nairobi", "Consular", -1.2977, 36.8129,
     "CBA Building, 3ª planta, Mara & Ragati Roads, Upper Hill, P.O. Box 45503-00100 Nairobi. Tel. +254 20 272 02 22/3/4/5 · Emergencia consular: +254 733 63 11 44."),
    ("Aga Khan University Hospital / Nairobi Hospital", "Hospital", -1.2667, 36.8083,
     "La mejor referencia sanitaria de todo el bucle sur y este: buen momento para revisiones médicas y para reponer botiquín antes de emprender el regreso."),
    ("Combustible · Nairobi / Nanyuki / Isiolo", "Combustible", -1.2864, 36.8172,
     "Estaciones formales (Shell, TotalEnergies, Rubis) en todo el eje central hasta Isiolo; a partir de Marsabit hay que repostar a fondo antes del bucle desértico de Chalbi y Turkana, donde solo hay combustible de bidón."),
    ("Agua potable y de uso general · Nairobi", "Agua potable", -1.2864, 36.8172,
     "Agua embotellada sin problema en supermercados de Nairobi; talleres y campings de Nanyuki e Isiolo permiten llenar el depósito de uso general con manguera. Para el bucle del norte, cargar a tope en Isiolo y de nuevo en Marsabit."),
]

DRONE_CALLOUT = ("warn", "Registro y autorización previa obligatorios ante la KCAA",
                  "Kenia exige registro del dron y autorización previa de la Kenya Civil Aviation Authority (KCAA) para cualquier uso, incluido el recreativo; el Kenya Wildlife Service (KWS) añade restricciones adicionales dentro de los parques nacionales (Amboseli, Marsabit), donde en la práctica rara vez se autoriza a particulares. Norma prudente del proyecto: tramitar el registro KCAA con antelación y no volar dentro de los parques sin autorización específica del KWS.")

STARLINK_CALLOUT = ("warn", "Activo pero con nuevas altas restringidas — verificar disponibilidad antes de contar con él",
                     "Starlink está operativo en Kenia, pero ha llegado a pausar temporalmente nuevas altas en determinadas zonas por sobrecarga de capacidad de red; no dar por hecho que se pueda contratar o activar un kit sobre la marcha en el país. Confirmar el estado de las altas 30-60 días antes del viaje y llevar SIM local (Safaricom, Airtel Kenya) como respaldo garantizado en todo el corredor.")

DOG_MATRIX = [
    ("Diani Beach y la costa sur", "permitido con condiciones",
     "La mejor zona del país con el perro: muchos alojamientos de Diani lo admiten, hay veterinarios y es donde tiene sentido parar varios días. Ojo con el calor húmedo y con los colobos de los árboles."),
    ("Nairobi, Nanyuki, Naivasha, Bogoria, Mombasa", "permitido con condiciones",
     "Nairobi es la ciudad más pet-friendly de la región, con veterinarios y residencias caninas de buen nivel: es LA base para los días de parque. Bogoria, al ser reserva de condado y no parque nacional, es más flexible: confirmar en la puerta."),
    ("Todos los parques del KWS y el Masái Mara", "prohibido",
     "Amboseli, Nakuru, Tsavo, Aberdare, monte Kenia, Marsabit y el Mara no admiten mascotas. Plan B real: turnos entre los tres viajeros, con base en Nairobi, Nanyuki, Naivasha o Voi, y residencia canina en Nairobi para los bloques largos."),
    ("Conservancies privadas de Laikipia (Ol Pejeta, Lewa, Borana, Segera)", "por confirmar",
     "No dependen del KWS y cada una tiene su propio reglamento, así que son la vía más prometedora para ver fauna con el perro cerca: hay que escribir a cada una por separado. Está en los pendientes."),
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
    ("The Road Chose Me · relato de la ruta 4x4 a Loiyangalani y el lago Turkana", "http://theroadchoseme.com/loiyangalani-lake-turkana"),
    ("Trunk Trails Safaris · la nueva tarifa de cuatro tramos del KWS para 2026", "https://trunktrailssafaris.com/kenya-national-park-fees-2026/"),
    ("SafariFind · tarifas y disponibilidad de los parques de Kenia 2026", "https://safarifind.com/blog/kenya-national-park-fees-availability-2026"),
    ("4x4 Kenya · recomendaciones para hacer overland por Kenia", "https://www.4x4kenya.com/recommendations-for-overlanding-in-kenya/"),
    ("Trunk Trails Safaris · travesía del desierto de Chalbi en la ruta de Turkana", "https://trunktrailssafaris.com/chalbi-desert-safari-kenya/"),
    ("4x4community.co.za · hilo del foro sobre la ruta al lago Turkana", "https://www.4x4community.co.za/forum/showthread.php/360080-Lake-Turkana"),
    ("UNESCO · Parques Nacionales del Lago Turkana, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/801/"),
]

# Entrada por Namanga, Rift, centro y norte, hasta el punto más oriental (la costa)
CORRIDOR = [(-2.5450, 36.7867), (-2.6527, 37.2606), (-1.2864, 36.8172), (-0.9144, 36.4461),
            (-0.3667, 36.0833), (0.2500, 36.0833), (0.0167, 37.0667), (0.6000, 37.5333),
            (2.3167, 37.9833), (2.7500, 36.7167), (0.0167, 37.0667), (-1.2864, 36.8172),
            (-1.4061, 35.0083)]

# Salida por la costa: del Mara y Tsavo a la costa y al paso costero de Lunga Lunga
CORRIDOR_ALT = [(-1.4061, 35.0083), (-3.0500, 38.0500), (-2.7500, 38.7500), (-4.0632, 39.6797),
                (-2.2717, 40.9020), (-4.0632, 39.6797), (-4.2769, 39.5906), (-4.5583, 39.1167)]

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
     "por eso el itinerario de este viaje discurre siempre por el eje central y la costa sur, lejos de esa franja fronteriza, y da la vuelta en Kenia sin continuar hacia el Cuerno de África — ver la decisión de ruta de esta ficha."),
]

HISTORIA_FUENTES = [
    ("BBC News · Kenya country profile", "https://www.bbc.com/news/world-africa-13681341"),
    ("Encyclopaedia Britannica · Kenya, History", "https://www.britannica.com/place/Kenya/History"),
    ("UNESCO · Ciudad vieja de Lamu, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/1055/"),
    ("National Archives (Reino Unido) · documentación sobre la represión de los Mau Mau", "https://www.nationalarchives.gov.uk/"),
]

SPEC = dict(
    slug="kenia", name="Kenia", revision="12 sep 2026",
    sub="PUNTO MÁS ORIENTAL del viaje · corredor doble · entrada y salida por Tanzania",
    chips=[
        ("PUNTO MÁS AL ESTE", "Diani Beach — aquí el viaje da la vuelta"),
        ("ENTRADA", "Namanga (desde Tanzania), junto a Amboseli"),
        ("SALIDA", "Lunga Lunga/Horohoro (costera, hacia Tanzania) — paso distinto"),
        ("EXPEDICIÓN 4x4", "Bucle del norte: Marsabit, desierto de Chalbi y lago Turkana"),
        ("A PIE", "Monte Kenia (pico Lenana, 4.985 m) · Longonot · Hell's Gate"),
        ("PARQUES CAROS", "Nueva tarifa KWS 2026: 80–90 USD/persona/día; Mara hasta 200"),
        ("VISADO", "eTA obligatoria — tramitar con antelación"),
        ("PERRO", "Prohibido en parques; Diani y Nairobi son las bases buenas"),
    ],
    center=[0.0, 37.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Entrada, Rift y norte", corridor_alt_label="Salida por la costa",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("Kenia es el PUNTO MÁS ORIENTAL del viaje: aquí la ruta da la vuelta y empieza el regreso. Se entra desde Tanzania por Namanga y se sale de nuevo a Tanzania por el paso costero de Lunga Lunga, "
              "de modo que los dos corredores no se solapan. La ruta excluye por completo la franja fronteriza con Somalia (condado de Mandera, este de Wajir y Garissa) por el riesgo de Al-Shabaab, "
              "y también la salida por Moyale hacia Etiopía, que era el plan antiguo y ya no forma parte del viaje: el itinerario confirmado no pasa de Kenia hacia el Cuerno de África."),
    facts=[
        ("Rol en la ruta", "Punto más oriental del viaje y final del trayecto de ida: desde aquí se regresa hacia el sur y luego hacia el oeste."),
        ("Entrada", "Namanga desde Tanzania, junto al Parque de Amboseli."),
        ("Salida", "Lunga Lunga/Horohoro hacia Tanzania, paso costero al sur de Diani, abierto 24 h y distinto del de entrada."),
        ("Tarifas de parques", "Nueva tarifa KWS de cuatro tramos desde octubre de 2025: no residentes pagan 90 USD/día en Amboseli y Nakuru, 80 en Tsavo, Nairobi NP, Meru y Aberdare, y 50 en Hell's Gate. El Masái Mara va aparte (condado de Narok): 100 USD/día de enero a junio y 200 a partir de julio. Se paga por eCitizen y KWSPay."),
        ("Expedición 4x4", "El bucle del norte (Marsabit, desierto de Chalbi, lago Turkana y vuelta por Baragoi y Maralal) es el gran tramo 4x4 del país: 7-10 días, pista rocosa muy dura y combustible solo de bidón."),
        ("Seguridad", "Franja fronteriza con Somalia EXCLUIDA. El norte (Turkana, Baragoi, Marsabit) tiene conflicto intercomunitario intermitente por ganado: revalidar antes de entrar, no es una zona a improvisar."),
        ("Visado", "eTA (autorización electrónica) obligatoria para todos los cruces, incluidos los terrestres; tramitar 48-72 h o con hasta 14 días de antelación."),
        ("Vehículo", "CPD exigido en la práctica — imprescindible, no opcional."),
    ],
    alerts=[
        "Zona fronteriza con Somalia (Mandera, franja este de Wajir/Garissa): EXCLUIDA por riesgo de terrorismo — no forma parte de ninguna variante de la ruta. La carretera de acceso a Lamu roza esa franja sensible: valorar Lamu con la información de seguridad del momento.",
        "El coste de los parques es el mayor del viaje después de Tanzania: tres adultos un solo día en Amboseli o Nakuru son 270 USD, y tres días en el Mara en temporada alta, 1.800 USD solo en entradas. Hay que presupuestarlo y decidir a cuáles se entra de verdad.",
        "Bucle del norte (Turkana): conflicto intercomunitario intermitente por el ganado en la zona de Baragoi y el norte de Samburu. Informarse en Maralal y Marsabit antes de meterse, viajar de día y no improvisar rutas.",
        "eTA obligatoria para TODOS los cruces, incluidos los terrestres de Namanga y Lunga Lunga: tramitarla antes de salir de Tanzania, no en la propia frontera.",
        "Starlink: ha pausado nuevas altas en algunas zonas por sobrecarga de red — confirmar disponibilidad real 30-60 días antes, no dar el servicio por garantizado.",
        "Perro prohibido en todos los parques del KWS y en el Mara: la base para los turnos es Nairobi (residencias caninas de buen nivel), Nanyuki, Naivasha y Diani.",
    ],
    ruta_intro=("Entrada por Namanga junto a Amboseli, bajada del Valle del Rift y sus lagos, subida al monte Kenia y a Samburu, "
                "el gran bucle 4x4 del norte hasta el lago Turkana, el Masái Mara, y salida por Tsavo y la costa hasta el punto más "
                "oriental del viaje. Etapas sobre una media de 250 km/día."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Entrada y elefantes", "Namanga → Amboseli → Nairobi", "~400 km · 3-4 días"),
        ("2 · Capital y logística", "Nairobi: talleres, recambios, embajada, Parque Nacional de Nairobi", "2-3 días de parada"),
        ("3 · Lagos del Rift", "Nairobi → Naivasha y Longonot → Hell's Gate → Nakuru → Bogoria", "~350 km · 4-5 días"),
        ("4 · El ecuador y la montaña", "Bogoria → Nanyuki → monte Kenia (pico Lenana, 3-5 días a pie)", "~250 km · 5-6 días"),
        ("5 · Al norte del ecuador", "Nanyuki → Laikipia (conservancies) → Samburu", "~200 km · 3 días"),
        ("6 · Expedición al norte", "Samburu → Marsabit → desierto de Chalbi → lago Turkana (Loiyangalani)", "~700 km · 5-6 días de pista dura"),
        ("7 · Vuelta del norte", "Loiyangalani → Baragoi → Maralal → Nanyuki/Nairobi", "~600 km · 4 días"),
        ("8 · La gran migración", "Nairobi → Masái Mara → Nairobi", "~600 km ida y vuelta · 4-5 días"),
        ("9 · Bajada a Tsavo", "Nairobi → Tsavo Oeste (Mzima, Shetani) → Tsavo Este", "~500 km · 4 días"),
        ("10 · La costa suajili", "Tsavo → Mombasa y el Fuerte Jesús → (Lamu, opcional)", "~250 km · 2-3 días, más 4-5 si se hace Lamu"),
        ("11 · Punto más oriental", "Mombasa → Diani Beach", "~40 km · 3-4 días de parada y celebración"),
        ("12 · Salida y vuelta al sur", "Diani → Lunga Lunga/Horohoro (frontera de Tanzania)", "~50 km · 1 día"),
    ],
    offroad=[
        "EL BUCLE DEL NORTE (la gran expedición del país): Marsabit → desierto de Chalbi → lago Turkana (Loiyangalani) → Baragoi → Maralal. Pista rocosa constante, descrita por overlanders que la han hecho como «conducir por la luna»: piedra y más piedra, con neumáticos reforzados obligatorios. Gasóleo solo de bidón en Loiyangalani y no siempre; hay que salir de Marsabit con los depósitos y las garrafas llenos. Agua potable disponible en Loiyangalani gracias a un manantial mejorado por una ONG.",
        "Desierto de Chalbi: llanura de sal y arena, el único desierto verdadero de Kenia. Impracticable tras las lluvias, cuando se convierte en barrizal.",
        "Pistas de Tsavo Oeste: lava de Shetani, colina de Chaimu y las pistas de tierra roja del parque, con tramos de arena.",
        "Samburu y Laikipia: pistas de tierra y vados del Ewaso Ng'iro, fáciles pero lentas.",
        "Masái Mara: dentro de la reserva está prohibido salirse de la pista; solo las conservancies privadas del contorno permiten conducción fuera de pista y nocturna.",
    ],
    senderismo=[
        "Monte Kenia, pico Lenana (4.985 m): la gran caminata de Kenia y de las mejores de África. Sin escalada técnica, 3-5 días por las rutas Sirimon (la más seca y usada), Chogoria (la más bonita) o Naro Moru (la más rápida y dura). Aclimatación obligatoria; el pico Batian (5.199 m) sí exige escalada técnica y queda fuera.",
        "Monte Longonot (2.776 m): volcán de cono perfecto sobre Naivasha. Se sube al borde del cráter en poco más de una hora y se puede rodear entero por el filo en 4-5 horas, con vistas al Rift y al bosque interior del cráter.",
        "Hell's Gate: el único parque de Kenia que se recorre A PIE y EN BICICLETA entre cebras, jirafas y búfalos, porque no tiene grandes depredadores. Incluye el desfiladero de Ol Njorowa y los géiseres. A 50 USD por persona, el parque más barato del país y el más original.",
        "Montes Aberdare: bosque de altura, cascadas (Karuru, de las más altas del país) y páramo de brezo gigante; caminatas de día con ranger.",
        "Cráter de Menengai (Nakuru): caldera enorme que se recorre por el borde, gratis y fuera de parque.",
        "Ngong Hills (Nairobi): la cresta de colinas de «Memorias de África», caminata de media jornada a las afueras de la capital y perfecta para hacer con el perro.",
        "Shimba Hills (costa): bosque costero con elefantes y las cascadas de Sheldrick, caminata corta con ranger cerca de Diani.",
    ],
    acampada=[
        "Nairobi: campings orientados a overlanders en la zona de Karen/Langata, con aparcamiento vigilado. Base natural para los turnos con el perro.",
        "Naivasha: campings a orillas del lago con hipopótamos saliendo del agua de noche, muy usados por viajeros de expedición.",
        "Nanyuki: campings y lodges de tránsito, base del monte Kenia y de Laikipia.",
        "Loiyangalani (lago Turkana): Palm Shade Camp, el mejor sitio del pueblo, con sombra de palmeras y agua de manantial.",
        "Marsabit: campamento del parque o alojamiento en el pueblo; cargar agua y combustible a fondo antes de seguir.",
        "Diani: alojamientos y campings junto a la playa, muchos de ellos aptos para el perro.",
    ],
    visado=[
        "eTA (Electronic Travel Authorisation) obligatoria desde 2024 para todos los visitantes, incluidos los cruces terrestres: pasaporte, foto, billete de continuación, prueba de alojamiento y certificado de fiebre amarilla si aplica.",
        "Tramitar con 14 días de antelación cuando sea posible; procesamiento estándar de 48-72 horas.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica (aplica viniendo de Tanzania).",
    ],
    fronteras_rows=[
        ("Entrada", "Namanga (Tanzania)", "Paso de alto tránsito turístico junto a Amboseli; puesto bien equipado. Alternativa: Taveta, al sureste."),
        ("Salida", "Lunga Lunga/Horohoro (Tanzania)", "Paso costero al sur de Diani, ventanilla única abierta 24 h, que enlaza con Tanga. Distinto del de entrada, como marca la ruta."),
        ("Fuera de la ruta", "Moyale (Etiopía)", "Se conserva como referencia: el viaje ya NO continúa hacia el Cuerno de África."),
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
        "SIM local (Safaricom, Airtel Kenya) como respaldo garantizado en el eje central y la costa; en el bucle del norte (Chalbi, Turkana) la cobertura es intermitente o inexistente.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente, vacuna antirrábica en vigor y permiso de importación previo, exigibles en frontera.",
        "Perro prohibido en Amboseli y Marsabit; prever cuidador en Nairobi o Nanyuki antes de cada parque.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en gran parte del territorio, con menor riesgo en Nairobi por altitud: profilaxis a valorar con Sanidad Exterior según el itinerario exacto.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Aga Khan University Hospital y Nairobi Hospital son las mejores referencias sanitarias de todo el bucle: aprovechar Nairobi para revisiones y reposición de botiquín antes de emprender el regreso.",
    ],
    seguridad_intro="Kenia combina un eje central y costero muy manejable con un norte desértico que exige revalidación específica, manteniendo siempre la franja fronteriza con Somalia fuera de cualquier variante de ruta.",
    seguridad=[
        "No aproximarse en ningún caso a la franja fronteriza con Somalia (Mandera, este de Wajir/Garissa); fuera de cualquier variante del itinerario.",
        "Bucle del norte (Samburu norte, Baragoi, Turkana, Marsabit): hay conflicto intercomunitario intermitente por el robo de ganado, con episodios violentos entre comunidades. No es terrorismo ni va dirigido a viajeros, pero obliga a informarse sobre el terreno (en Maralal, Marsabit y Loiyangalani), a viajar de día y a no improvisar rutas alternativas.",
        "Carretera de acceso a Lamu: roza la franja sensible del condado de Lamu. Consultar la recomendación oficial del momento antes de decidir ese desvío.",
        "Aparcamiento vigilado en Nairobi y Mombasa por prudencia estándar frente a la delincuencia oportunista de grandes ciudades.",
        "En safari, seguir siempre las indicaciones del ranger respecto a distancia con la fauna; en Hell's Gate se camina y se pedalea entre herbívoros, pero hay búfalos.",
        "Lago Turkana: la mayor densidad de cocodrilos del mundo. No bañarse ni dejar que el perro se acerque a la orilla.",
    ],
    agua=[
        "Nairobi, Nakuru, Nanyuki, Mombasa y Diani: agua embotellada sin problema en supermercados.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): talleres y campings de Nairobi, Naivasha, Nanyuki e Isiolo permiten llenar con manguera.",
        "Bucle del norte: cargar los depósitos a tope en Isiolo y de nuevo en Marsabit. En Loiyangalani hay agua potable de un manantial mejorado por una ONG, dato confirmado por overlanders que han estado.",
    ],
    combustible=[
        "Eje central sin problemas: Namanga → Nairobi (~165 km) → Nanyuki (~200 km) → Isiolo (~80 km), todos con estaciones formales (Shell, TotalEnergies, Rubis).",
        "Bucle del norte, el tramo crítico del país: repostar a fondo en Isiolo y en Marsabit. Entre Marsabit, Chalbi y Loiyangalani no hay estaciones formales; en Loiyangalani se vende gasóleo y gasolina DE BIDÓN, con disponibilidad irregular. Salir con garrafas llenas y calcular el retorno por Baragoi y Maralal.",
        "Costa y Tsavo: oferta amplia y fiable en Voi, Mombasa y Diani.",
    ],
    experiencias_intro="Relatos y datos reales de otros overlanders y de fuentes especializadas, sobre todo del norte, que es el tramo menos documentado:",
    experiencias=[
        "Bucle del lago Turkana (relato de un overlander que lo hizo en un Jeep): la pista es «roca y más roca» y describe el paisaje como haber «conducido hasta la luna». Llevaba neumáticos reforzados BFG KO2, que aguantaron bien el terreno. Tuvo que trasvasar unos 50 litros del depósito auxiliar para llegar con el principal lleno: en Loiyangalani hay gasóleo y gasolina, pero DE BIDÓN y sin garantía.",
        "Loiyangalani (mismo relato): recomienda Palm Shade Camp como el mejor sitio para acampar, un oasis con sombra de palmeras. Una ONG mejoró el manantial del pueblo, así que hay agua potable abundante. Convive allí gente de tres etnias distintas y avisa de que el lago tiene la mayor densidad de cocodrilos del mundo, pese a lo cual los pescadores locales siguen faenando.",
        "Tarifas del KWS, cambio importante de 2025-2026: el sistema pasó a cuatro tramos según ciudadanía y residencia el 1 de octubre de 2025. Los no residentes pagan 90 USD por adulto y día en Amboseli y Nakuru, 80 en Tsavo Este y Oeste, Nairobi NP, Meru y Aberdare, y 50 en Hell's Gate, todo por periodos de 24 horas. El pago se tramita por eCitizen y KWSPay, no en efectivo en la puerta.",
        "El Masái Mara va por libre: lo gestiona el condado de Narok y no el KWS, con 100 USD por persona y día de enero a junio y 200 USD de julio en adelante, coincidiendo con la migración. Las conservancies privadas del contorno cuestan más pero permiten salir de la pista y conducir de noche, cosa prohibida dentro de la reserva.",
        "Hell's Gate es la rareza útil: al no haber grandes depredadores se recorre a pie y en bicicleta entre cebras y jirafas. Es el parque más barato del país (50 USD) y el único donde el paisaje se disfruta sin estar encerrado en el vehículo.",
        "Perro: Nairobi es la ciudad más pet-friendly de la región, con veterinarios y residencias caninas de buen nivel, y Diani tiene bastantes alojamientos que lo admiten. Las conservancies privadas de Laikipia (Ol Pejeta, Lewa, Borana, Segera) no dependen del KWS y cada una fija sus normas, así que son la vía más prometedora para ver fauna con el perro: hay que escribirles una por una.",
    ],
    pendientes=[
        ("eTA", "Tramitar antes de salir de Tanzania, con margen de 14 días si es posible"),
        ("Presupuesto de parques", "Decidir a qué parques se entra de verdad: con la tarifa de 2026, tres adultos un día en Amboseli o Nakuru son 270 USD y tres días en el Mara en temporada alta, 1.800 USD solo en entradas"),
        ("Bucle del norte", "Confirmar seguridad en Baragoi y el norte de Samburu poco antes de entrar, y decidir si se hace el bucle completo de Turkana (7-10 días) o solo Marsabit"),
        ("Perro en las conservancies de Laikipia", "Escribir a Ol Pejeta, Lewa, Borana y Segera para saber si alguna admite perro: es la mejor opción del país para ver fauna sin dejarlo atrás"),
        ("Residencia canina en Nairobi", "Reservar para los bloques de parques largos (Mara, Tsavo, monte Kenia)"),
        ("Lamu", "Decidir si entra, valorando la seguridad de la carretera de acceso y que la ciudad es sin coches (hay que dejar los vehículos en el continente)"),
        ("Monte Kenia", "Decidir ruta (Sirimon, Chogoria o Naro Moru), reservar guía y porteadores, y organizar quién se queda con el perro los 3-5 días"),
        ("Starlink", "Confirmar si las altas nuevas siguen pausadas en la ruta prevista"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Nairobi): +254 733 63 11 44 · Embajada de España en Nairobi: +254 20 272 02 22/3/4/5.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

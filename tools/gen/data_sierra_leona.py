# -*- coding: utf-8 -*-
"""Sierra Leona — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Freetown (península y Cotton Tree)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=8.4840, lon=-13.2299,
         desc="Capital y única gran base de servicios: puerto, aeropuerto (vía ferry/carretera a Lungi), bancos, talleres y el símbolo colonial del Cotton Tree en el centro. Punto de repostaje y provisiones antes o después de la península.",
         credit="Christian Trede · CC BY-SA 2.0 DE", source=W + "Cotton%20Tree%20(Sierra%20Leone).jpg?width=900"),
    dict(n=2, name="Tacugama Chimpanzee Sanctuary", cat="Naturaleza", prio="Media", dog="pendiente de confirmación oficial", time="½ día",
         lat=8.4667, lon=-13.1500,
         desc="Santuario de chimpancés en el bosque de la península de Freetown, referencia de conservación en el país; visitas guiadas y senderismo corto. Confirmar con el santuario si el perro puede acompañar en el aparcamiento o debe quedarse en el vehículo.",
         credit="BigMikeSndTech · CC BY 2.0", source=W + "West%20African%20Chimpanzee.jpg?width=900"),
    dict(n=3, name="River No. 2 Beach", cat="Costa", prio="Media", dog="permitido", time="1 día",
         lat=8.3230, lon=-13.1866,
         desc="La playa más conocida de la península de Freetown: arena blanca, aguas tranquilas y algunos chiringuitos; buena base para descansar tras la frontera de Guinea. Sombra natural de palmeras.",
         credit="Christian Trede · Attribution", source=W + "River%20No.%202%20Beach%20(Sierra%20Leone).jpg?width=900"),
    dict(n=4, name="Islas Banana", cat="Naturaleza · costa", prio="Media", dog="pendiente de confirmación oficial", time="1 día",
         lat=8.1000, lon=-13.2333,
         desc="Archipiélago frente a la península, antiguo punto de la trata de esclavos y hoy retiro tranquilo de pesca y buceo; acceso en lancha desde Kent o York. Confirmar con el operador si el perro puede embarcar.",
         credit="Christian Trede · Attribution", source=W + "Banana%20Islands%20(Sierra%20Leone).jpg?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "naturaleza": "verde", "costa": "turquesa", "naturaleza · costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Gbalamuya/Pamelap (desde Guinea)", "Frontera", 9.5100, -12.9500,
     "Paso principal desde Conakry (~6-8 h de trayecto total); control de inmigración y aduanas, certificado de fiebre amarilla exigido. Recomendable cruzar y circular en horas de luz."),
    ("Frontera · Salida — Jendema / Bo-Waterside (hacia Liberia)", "Frontera", 6.8500, -11.2500,
     "Ruta menos usada que la de Guinea; mismos requisitos documentales. Confirmar estado de la vía en temporada de lluvias antes de salir."),
    ("Cobertura consular española (referencia)", "Consular", 9.5300, -13.6800,
     "Sin embajada de España en Sierra Leona: la demarcación consular corresponde a la Embajada de España en Conakry (Guinea), +224 664 20 22 01, emergencia +224 664 33 54 93."),
    ("Connaught Hospital — Freetown", "Hospital", 8.4870, -13.2340,
     "Principal hospital público de referencia en la capital; capacidad limitada para politraumatismos graves. Coordenada urbana aproximada."),
    ("Combustible · Freetown", "Combustible", 8.4840, -13.2299,
     "Mejor oferta y calidad del país (Total, Petroleum SL, ORYX); repostar aquí siempre que sea posible."),
    ("Agua potable · Freetown (supermercados y garrafas)", "Agua potable", 8.4840, -13.2299,
     "Agua embotellada disponible en la capital; fuera de Freetown, tratar o hervir el agua local antes de consumirla."),
]

DRONE_CALLOUT = ("warn", "Sin procedimiento turístico claro: tratar como restringido",
                  "No se ha localizado normativa pública específica para visitantes con dron en Sierra Leona. Solicitar autorización previa por escrito a la autoridad de aviación civil (SLCAA) o, en su defecto, no volarlo, especialmente cerca de Freetown, el aeropuerto de Lungi y zonas gubernamentales.")

STARLINK_CALLOUT = ("ok", "Starlink activo en el país (verificar cobertura exacta antes de entrar)",
                     "Sierra Leona figura entre los mercados africanos con servicio Starlink activo a mediados de 2026. Puede usarse como respaldo de comunicaciones, sin sustituir la SIM local (Orange, Africell) en zonas urbanas. Revisar el mapa oficial 30–60 días antes por si cambia la cobertura o el marco regulatorio de itinerancia.")

DOG_MATRIX = [
    ("Tacugama, Islas Banana (operadores/lanchas)", "pendiente de confirmación oficial", "Confirmar con el santuario/operador antes de la visita."),
    ("Freetown urbano, playas de la península", "permitido con condiciones", "Correa y sombra; tráfico denso en el centro de Freetown."),
]

SOURCES = [
    ("VisitSierraLeone · cruces fronterizos terrestres", "https://www.visitsierraleone.org/getting-to-sierra-leone-by-land/"),
    ("Wikipedia · Misiones diplomáticas en Sierra Leona (sin embajada española)", "https://en.wikipedia.org/wiki/List_of_diplomatic_missions_in_Sierra_Leone"),
    ("Embajada de España en Guinea · contacto (cobertura de Sierra Leona)", "https://www.exteriores.gob.es/Embajadas/conakry/es/Embajada/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("PetTravel · requisitos de mascotas en la región (referencia)", "https://www.pettravel.com/information/pet-passports/"),
    ("tech.africa · disponibilidad de Starlink en África (2026)", "https://tech.africa/starlink-africa/"),
    ("Comisión Europea · animales de compañía", "https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_es.htm"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(9.5100, -12.9500), (8.4840, -13.2299), (8.4667, -13.1500), (8.3230, -13.1866), (8.1000, -13.2333), (6.8500, -11.2500)]

HISTORIA_RESUMEN = ("Sierra Leona nació como proyecto humanitario británico para reasentar a antiguos esclavos liberados en Freetown («ciudad libre»), y décadas después se convirtió en escenario de una de las guerras civiles más brutales de África (1991-2002), "
                     "alimentada por los llamados «diamantes de sangre»; el país se ha recuperado desde entonces con elecciones democráticas sucesivas, aunque sigue entre los más pobres del mundo y fue duramente golpeado por el brote de ébola de 2014-2016.")

HISTORIA_SECCIONES = [
    ("Freetown, colonia de esclavos liberados",
     "Freetown fue fundada en 1787 por abolicionistas británicos como asentamiento para antiguos esclavos liberados procedentes de Gran Bretaña, Nueva Escocia y barcos negreros interceptados por la Marina Real tras la abolición del comercio de esclavos en 1807; esta población, los krios, desarrolló una cultura angloafricana propia que dominó la vida política y comercial de la colonia."),
    ("Colonia y protectorado británico",
     "Gran Bretaña extendió su control sobre el interior como protectorado en 1896, gobernando por separado la colonia costera (con los krios) y el protectorado del interior (con las etnias mende y temne, mayoritarias), una división administrativa y de privilegios que generaría tensiones tras la independencia."),
    ("La guerra civil y los diamantes de sangre (1991-2002)",
     "Sierra Leona se independizó en 1961, pero cayó en 1991 en una guerra civil de once años, protagonizada por el Frente Revolucionario Unido (RUF), tristemente célebre por el reclutamiento de niños soldado y la amputación de manos a civiles, financiada en gran medida por el contrabando de diamantes («diamantes de sangre» o «diamantes de conflicto»), hasta la intervención de fuerzas británicas y de la ONU que puso fin al conflicto en 2002."),
    ("Situación actual: reconstrucción, ébola y recursos naturales",
     "Desde el fin de la guerra, Sierra Leona ha celebrado varias elecciones con alternancia pacífica de poder, un logro notable tras el conflicto. El país fue uno de los más afectados por el brote de ébola de África Occidental en 2014-2016, con miles de muertos, y sigue dependiendo en gran medida de la minería de diamantes, hierro y rutilo, con altos niveles de pobreza pese a su riqueza mineral."),
]

HISTORIA_FUENTES = [
    ("BBC News · Sierra Leone country profile", "https://www.bbc.com/news/world-africa-14094194"),
    ("Encyclopaedia Britannica · Sierra Leone, History", "https://www.britannica.com/place/Sierra-Leone/History"),
    ("United Nations · UNAMSIL, misión de paz en Sierra Leona", "https://peacekeeping.un.org/en/mission/past/unamsil/"),
]

SPEC = dict(
    slug="sierra-leona", name="Sierra Leona", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Gbalamuya/Pamelap (desde Guinea)"),
        ("SALIDA", "Jendema/Bo-Waterside (hacia Liberia)"),
        ("SEGURIDAD", "estable · precaución normal"),
        ("FRONTERA TERRESTRE", "operativa en ambos extremos"),
        ("VISADO", "visado/eVisa previo — verificar"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[8.6, -12.5], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Sierra Leona se recorre casi íntegramente por la península de Freetown: playas, el santuario de Tacugama y las islas Banana, con la capital como única gran base de servicios. "
                   "Tramo relativamente corto entre la frontera guineana de Gbalamuya y la salida hacia Liberia por Jendema/Bo-Waterside."),
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Guinea."),
        ("Entrada", "Gbalamuya/Pamelap desde Conakry, 6-8 h de trayecto."),
        ("Salida", "Jendema/Bo-Waterside hacia Liberia."),
        ("Visado", "Confirmar eVisa o visado previo para pasaporte español; certificado de fiebre amarilla obligatorio."),
        ("Seguridad", "Estable, precaución normal; carreteras rurales en mal estado en temporada de lluvias."),
        ("Comunicaciones", "Starlink activo en el país; SIM local (Orange, Africell) como base en ciudades."),
    ],
    alerts=[
        "Certificado de fiebre amarilla exigido en frontera, sin excepciones.",
        "Carreteras rurales deficientes en época de lluvias (mayo-octubre): evitar en esa ventana si es posible.",
        "Sin representación consular española en el país: la Embajada en Conakry es la referencia operativa para cualquier incidencia grave.",
    ],
    ruta_intro="Tramo corto centrado en la península de Freetown.",
    route_rows=[
        ("Entrada y Freetown", "Gbalamuya → Freetown", "Provisiones, combustible y trámites de llegada"),
        ("Península", "Tacugama, River No. 2, Islas Banana", "Ritmo tranquilo; base para playas y naturaleza"),
        ("Hacia Liberia", "Freetown → Jendema/Bo-Waterside", "Confirmar estado de carretera antes de salir"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto en este tramo; el foco es la red principal pavimentada de la península.",
    ],
    acampada=[
        "Zona de River No. 2 y playas cercanas: alojamientos y explanadas informales frecuentadas por viajeros; confirmar seguridad antes de pernoctar fuera de un alojamiento.",
    ],
    visado=[
        "Confirmar 30-60 días antes si Sierra Leona exige eVisa previa o admite visado a la llegada para pasaporte español (la información pública cambia con frecuencia).",
        "Certificado internacional de fiebre amarilla obligatorio para la entrada.",
    ],
    fronteras_rows=[
        ("Entrada", "Gbalamuya/Pamelap (Guinea)", "Control de inmigración y aduanas; cruzar en horas de luz."),
        ("Salida", "Jendema/Bo-Waterside (Liberia)", "Ruta menos transitada; confirmar estado de la vía antes de salir."),
    ],
    vehiculos=[
        "CPD no imprescindible: permiso temporal en frontera suele bastar para turismo.",
        "Carte Brune (CEDEAO) recomendable como seguro de responsabilidad civil regional.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa a la SLCAA (Sierra Leone Civil Aviation Authority) o no volar el dron en el país ante la falta de procedimiento turístico claro.",
        "Evitar sobrevolar Freetown, el aeropuerto de Lungi y edificios gubernamentales.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo confirmado a mediados de 2026: revisar el mapa oficial 30-60 días antes por posibles cambios normativos de itinerancia.",
        "SIM local (Orange, Africell) como respaldo en ciudades y para gestiones cotidianas.",
    ],
    perro_intro=[
        "Sin normativa pública detallada localizada para Sierra Leona: aplicar como base pasaporte UE de mascota, microchip y certificado antirrábico vigente, y confirmar por escrito antes de viajar.",
        "Llevar certificado sanitario reciente para el control fronterizo de Gbalamuya.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado obligatorio para entrar.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior.",
        "Seguro con evacuación médica: la capacidad hospitalaria fuera de Freetown es limitada.",
    ],
    seguridad_intro="País estable con precaución general; el mayor riesgo práctico es el estado de las carreteras rurales, no la seguridad personal.",
    seguridad=[
        "Evitar desplazamientos nocturnos fuera de Freetown por el estado del firme y la señalización.",
        "Llevar siempre el certificado de fiebre amarilla y copias de la documentación del vehículo.",
        "Revisar el aviso de Exteriores 72 h antes de entrar.",
    ],
    agua=[
        "Freetown: agua embotellada en supermercados; fuera de la capital, tratar o hervir el agua local.",
        "Playas de la península (River No. 2, Islas Banana): sin fuente potable propia, llevar reserva desde Freetown.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio y hoteles/lodges de Freetown y de la península (Tokeh, River No. 2) permiten llenar el depósito con manguera; en las Islas Banana llevar el depósito lleno desde el continente.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km: Gbalamuya → Freetown (~230 km) → Jendema/Bo-Waterside (~300 km) cubren el tramo con estaciones formales en las ciudades principales.",
        "Repostar en Freetown antes de la península y antes de la salida hacia Liberia.",
        "Confirmar puntos recientes en iOverlander antes de tramos rurales; la red formal es más escasa fuera de la capital.",
    ],
    pendientes=[
        ("Visado", "Confirmar eVisa/visado a la llegada 30-60 días antes"),
        ("Perro en Tacugama e islas Banana", "Confirmar por escrito con el santuario y el operador de lanchas"),
        ("Estado de la vía Freetown-Jendema", "Verificar 7-15 días antes, especialmente si coincide con lluvias"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía 019 · Bomberos/Ambulancia 999 (verificar localmente, numeración poco estandarizada). Emergencia consular española (Conakry): +224 664 33 54 93.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

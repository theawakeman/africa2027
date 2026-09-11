# -*- coding: utf-8 -*-
"""Mozambique — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Maputo", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=-25.9692, lon=32.5732,
         desc="Capital y mayor base de servicios del país, con la Avenida Samora Machel y la Casa de Fierro de Eiffel como referencias urbanas; sede de la embajada de España y punto de entrada natural desde Sudáfrica o Esuatini.",
         credit="F Mira from Lisbon, Portugal · CC BY-SA 2.0", source=W + "Avenida%20Samora%20Machel%20towards%20Maputo%20City%20Hall.jpg?width=900"),
    dict(n=2, name="Arquipélago de Bazaruto (Vilanculos)", cat="Naturaleza", prio="Alta", dog="no recomendado", time="2 noches",
         lat=-21.9686, lon=35.3172,
         desc="Parque nacional marino con dunas de arena blanca, dugongos y arrecifes de coral; Vilanculos es la base logística en tierra para visitar el archipiélago en barco, punto de referencia de toda la costa índica del sur del país.",
         credit="Copernicus Sentinel-2 (Unión Europea) · Attribution", source=W + "Bazaruto%20Archipelago%20National%20Park%2C%20Mozambique.jpg?width=900"),
    dict(n=3, name="Beira", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=-19.8437, lon=34.8389,
         desc="Segunda ciudad del país y puerto clave del corredor hacia Zimbabue y Malaui; la Catedral (Sé da Beira) resume el legado colonial portugués. Base de repostaje y descanso antes de virar hacia el interior por Tete.",
         credit="Rosino · CC BY-SA 2.0", source=W + "Sé%20da%20Beira.jpg?width=900"),
    dict(n=4, name="Parque Nacional de Gorongosa", cat="Naturaleza", prio="Media", dog="prohibido", time="1–2 noches",
         lat=-18.9686, lon=34.3536,
         desc="Uno de los grandes proyectos de restauración de fauna de África tras la guerra civil (elefantes, leones, licaones); acceso por la puerta de Chitengo. Perro prohibido dentro del parque; opción de dejarlo en el campamento de la entrada con cuidador.",
         credit="Brian Dell · dominio público", source=W + "Gorongosa%20Park%20Gate.JPG?width=900"),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Lebombo/Ressano Garcia (desde Sudáfrica)", "Frontera", -25.4358, 31.9814,
     "Cruce principal y más usado del corredor Maputo-Johannesburgo; a partir del 1 de junio de 2026, declaración vehicular obligatoria en el sistema SARS/TMS sudafricano ANTES de salir de Sudáfrica — ver ficha de Sudáfrica."),
    ("Frontera · Salida — Zóbuè/Mwanza (hacia Malaui)", "Frontera", -16.1167, 33.0500,
     "Cruce del corredor de Tete hacia Malaui; carretera asfaltada, tráfico de camiones pesado en el corredor de Tete."),
    ("Embajada de España en Maputo", "Consular", -25.9700, 32.5850,
     "Rua Damião de Góis, 347, Caixa Postal 1331, Maputo. Tel. (+258) 21 49 20 25/27/30 · Emergencia consular 24h: (+258) 84 32 82 900."),
    ("Hospital Central de Maputo", "Hospital", -25.9575, 32.5789,
     "Principal hospital de referencia del país; mejor opción sanitaria del itinerario junto con clínicas privadas de Maputo (Clínica Cruz Azul)."),
    ("Combustible · Maputo / Beira", "Combustible", -19.8437, 34.8389,
     "Mejor oferta y calidad del país (Petromoc, Total, Puma) en las dos grandes ciudades; repostar a fondo en ambas antes del tramo hacia Tete."),
    ("Combustible · Corredor de Tete", "Combustible", -16.1564, 33.5867,
     "Estaciones formales en Tete antes del cruce a Malaui por Zóbuè; sin gap relevante de 500 km en el eje Beira-Tete-frontera."),
    ("Agua potable y de uso general · Maputo y Beira", "Agua potable", -25.9692, 32.5732,
     "Agua embotellada sin problema en supermercados de ambas ciudades; estaciones de servicio, campings y hoteles permiten llenar el depósito de uso general con manguera."),
]

DRONE_CALLOUT = ("warn", "Autorización previa recomendada, especialmente cerca de zonas militares y del norte",
                  "Mozambique no prohíbe los drones de forma generalizada, pero exige registro/autorización de la Aviación Civil (IACM) para uso recreativo con cámara, y la práctica varía por provincia. Norma prudente del proyecto: solicitar autorización antes de volar, evitar totalmente Cabo Delgado y el norte del país, y no volar cerca de instalaciones militares o portuarias en Maputo/Beira.")

STARLINK_CALLOUT = ("ok", "Disponible y operativo en 2026",
                     "Starlink está activo comercialmente en Mozambique desde 2025-2026, con cobertura en las principales ciudades y zonas rurales del corredor sur; kit y suscripción configurables antes de entrar al país o vía distribución local.")

DOG_MATRIX = [
    ("Parque Nacional de Gorongosa", "prohibido", "No se permite el acceso de mascotas a las zonas de fauna del parque; dejar con cuidador en la entrada de Chitengo."),
    ("Arquipélago de Bazaruto", "no recomendado", "Acceso solo en barco a las islas; sin infraestructura para mascotas y calor intenso — dejar en Vilanculos."),
    ("Maputo, Beira, corredor de Tete", "permitido con condiciones", "Correa y sombra; calor húmedo en la costa."),
]

SOURCES = [
    ("FCDO / travelwarningcheck.com · alerta de seguridad Mozambique 2026 (Cabo Delgado)", "https://www.travelwarningcheck.com/travel-advisory/mozambique"),
    ("Embajada de España en Maputo · contacto", "https://www.exteriores.gob.es/Embajadas/maputo/en/Paginas/index.aspx"),
    ("Carnetdepassage.org · Mozambique, requisitos de importación temporal de vehículos", "https://carnetdepassage.org/country/mozambique/"),
    ("PetTravel.com · requisitos de importación de mascotas a Mozambique", "https://www.pettravel.com/information/pet-passports/mozambique-pet-import-requirements/"),
    ("tech.africa · Starlink en África, estado por país 2026", "https://tech.africa/starlink-africa/"),
    ("SARS · Traveller Management System (TMS), declaración vehicular obligatoria desde el 1 de junio de 2026", "https://www.sars.gov.za/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [(-25.4358, 31.9814), (-25.9692, 32.5732), (-21.9686, 35.3172), (-19.8437, 34.8389), (-18.9686, 34.3536), (-16.1564, 33.5867), (-16.1167, 33.0500)]

HISTORIA_RESUMEN = ("Mozambique fue durante siglos un cruce de rutas swahilis del Índico antes de convertirse en la colonia portuguesa más longeva de África (casi 500 años); su independencia en 1975 dio paso casi de inmediato a una guerra civil devastadora, "
                     "y hoy el país reconstruido convive con una insurgencia yihadista activa en el extremo norte, lejos del corredor de este viaje.")

HISTORIA_SECCIONES = [
    ("Antes de la colonización: rutas del Índico",
     "Mucho antes de la llegada europea, la costa mozambiqueña formaba parte del mundo swahili: puertos comerciales donde pueblos bantúes del interior intercambiaban oro, marfil y esclavos con mercaderes árabes, persas e indios que llegaban con los monzones. "
     "Ilha de Moçambique, en el norte, y Sofala, cerca de la actual Beira, fueron los grandes puertos de esta red, conectados por tierra con el imperio de Gran Zimbabue y sus sucesores, que controlaban las minas de oro del interior."),
    ("Colonización portuguesa: casi 500 años",
     "Vasco da Gama tocó la costa mozambiqueña en 1498 de camino a la India, y Portugal fue construyendo aquí, de forma lenta y desigual, la colonia europea más duradera de África: formalmente hasta 1975. "
     "El dominio efectivo del interior no llegó hasta bien entrado el siglo XX, y se sostuvo en gran medida sobre el trabajo forzado (chibalo) y una economía de exportación de mano de obra hacia las minas y plantaciones de Sudáfrica y Rodesia, "
     "más que sobre un desarrollo interno del país."),
    ("Independencia y guerra civil (1975-1992)",
     "El FRELIMO (Frente de Liberación de Mozambique) libró una guerra de independencia desde 1964 y tomó el poder en 1975, tras la Revolución de los Claveles en Portugal. "
     "Casi de inmediato, el nuevo Estado de orientación marxista se vio enfrentado a la RENAMO, un movimiento insurgente armado y financiado primero por la Rodesia blanca y después por el apartheid sudafricano como forma de desestabilizar a un vecino hostil. "
     "La guerra civil resultante (1977-1992) causó alrededor de un millón de muertos y desplazó a varios millones de personas, dejando el país entre los más pobres del mundo al firmarse la paz de Roma en 1992."),
    ("Situación actual: reconstrucción y la insurgencia de Cabo Delgado",
     "Desde los años 90 Mozambique vivió una recuperación económica notable, apoyada después por el descubrimiento de enormes reservas de gas natural frente a las costas de Cabo Delgado, en el extremo norte del país. "
     "Precisamente esa provincia, una de las más pobres y marginadas históricamente, es desde 2017 escenario de una insurgencia yihadista vinculada a ISIS-Mozambique, con centenares de miles de desplazados y ataques periódicos a poblaciones y proyectos de gas. "
     "Esta zona de conflicto está a más de 1.000 km del corredor sur (Maputo-Vilanculos-Beira-Tete) que sigue este viaje, y queda completamente excluida de cualquier variante de la ruta — ver la decisión de ruta de esta ficha."),
]

HISTORIA_FUENTES = [
    ("BBC News · Mozambique country profile", "https://www.bbc.com/news/world-africa-13890416"),
    ("Encyclopaedia Britannica · Mozambique, History", "https://www.britannica.com/place/Mozambique/History"),
    ("Human Rights Watch · Cabo Delgado, informes sobre el conflicto", "https://www.hrw.org/africa/mozambique"),
    ("UNESCO · Ilha de Moçambique, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/599/"),
]

SPEC = dict(
    slug="mozambique", name="Mozambique", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Lebombo/Ressano Garcia (desde Sudáfrica) — declaración SARS/TMS previa"),
        ("SALIDA", "Zóbuè/Mwanza (hacia Malaui)"),
        ("SEGURIDAD", "Cabo Delgado y norte EXCLUIDOS — insurgencia activa"),
        ("VEHÍCULO", "CPD no obligatorio: permiso temporal en frontera"),
        ("COMUNICACIONES", "Starlink activo (ok)"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[-21.5, 34.2], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision=("Cabo Delgado (extremo norte) sufre desde 2017 una insurgencia yihadista activa vinculada a ISIS-Mozambique: más de 946.000 personas desplazadas y ataques recientes en Mocímboa da Praia, Palma, Macomia y Muidumbe. "
              "El FCDO británico desaconseja todo viaje al norte del río Rovuma al menos hasta marzo de 2026. Esta zona está completamente fuera de cualquier versión de la ruta del proyecto, que se limita al corredor sur "
              "Maputo-Vilanculos-Beira-Tete, a más de 1.000 km de la zona de conflicto. Aun así, Maputo registró un repunte del 23% en delitos violentos a comienzos de 2026 (2.341 incidentes): extremar precauciones urbanas "
              "normales (atracos, robo de vehículo) en la propia capital, y evitar circular de noche en la EN1 entre Xai-Xai y Maputo por actividad delictiva ocasional."),
    facts=[
        ("Ventana prevista", "Primer país del corredor de regreso, tras el giro en Sudáfrica."),
        ("Entrada", "Lebombo/Ressano Garcia desde Sudáfrica: declaración vehicular SARS/TMS obligatoria ANTES de salir de Sudáfrica (ver ficha de Sudáfrica)."),
        ("Salida", "Zóbuè/Mwanza hacia Malaui, por el corredor de Tete."),
        ("Seguridad", "Cabo Delgado y todo el norte: EXCLUIDOS por insurgencia activa — ver decisión de ruta."),
        ("Vehículo", "CPD no obligatorio: permiso de importación temporal expedido en la propia frontera; llevar CPD igualmente recomendado como respaldo."),
        ("Comunicaciones", "Starlink activo y operativo (ok) en el corredor sur."),
    ],
    alerts=[
        "Cabo Delgado y el norte del país: insurgencia yihadista activa — excluidos por completo del itinerario, sin excepción.",
        "EN1 Xai-Xai–Maputo: actividad delictiva ocasional (atracos a vehículos); evitar circular de noche.",
        "Maputo: repunte de criminalidad violenta en 2026 — precauciones urbanas normales reforzadas (aparcamiento vigilado, no exhibir objetos de valor).",
        "Declaración SARS/TMS: gestionarla en Sudáfrica antes de cruzar hacia Mozambique, no en el propio puesto fronterizo.",
    ],
    ruta_intro="Entrada por el corredor de Maputo, desvío a la costa índica (Vilanculos/Bazaruto) y ascenso por Beira hasta el corredor de Tete, evitando el norte del país por completo.",
    route_rows=[
        ("Entrada y capital", "Lebombo/Ressano Garcia → Maputo", "Declaración SARS/TMS ya tramitada en Sudáfrica; embajada española"),
        ("Costa índica", "Maputo → Vilanculos/Bazaruto", "Desvío recomendado de 2 noches; acceso al archipiélago en barco"),
        ("Corredor central", "Vilanculos → Beira", "Repostaje a fondo antes de virar al interior"),
        ("Hacia Malaui", "Beira → Tete → Zóbuè/Mwanza", "Corredor de Tete, tráfico pesado; salida del país"),
    ],
    offroad=[
        "Sin pistas 4x4 destacadas de interés específico para el proyecto: el eje Maputo-Vilanculos-Beira-Tete es carretera asfaltada, con baches importantes en algunos tramos del corredor de Tete tras la temporada de lluvias.",
    ],
    acampada=[
        "Vilanculos: campings y lodges con aparcamiento vigilado orientados a overlanders, buena oferta para el desvío a Bazaruto.",
        "Beira y Tete: hoteles y campings urbanos; evitar acampada libre en el corredor de Tete por tráfico pesado y menor vigilancia.",
    ],
    visado=[
        "Exención de visado corta para turismo — verificar la duración exacta y condiciones 30-60 días antes, ya que Mozambique ha ajustado su política en los últimos años.",
        "Certificado internacional de fiebre amarilla exigido si se procede de zona endémica.",
    ],
    fronteras_rows=[
        ("Entrada", "Lebombo/Ressano Garcia (Sudáfrica)", "Declaración SARS/TMS obligatoria antes de salir de Sudáfrica desde el 1 de junio de 2026."),
        ("Salida", "Zóbuè/Mwanza (Malaui)", "Corredor de Tete; carretera asfaltada con tráfico pesado de camiones."),
    ],
    vehiculos=[
        "CPD no obligatorio: permiso de importación temporal (TIP) expedido en la propia frontera de entrada.",
        "Llevar el CPD igualmente como respaldo, ya que simplifica el resto de fronteras del corredor de regreso.",
        "Seguro de terceros (COMESA / local) obligatorio, comprado en la frontera de entrada.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Registro/autorización previa ante el Instituto de Aviação Civil de Moçambique (IACM) recomendado antes de volar.",
        "No volar en ningún caso en Cabo Delgado ni cerca de instalaciones militares o portuarias en Maputo/Beira.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio activo y operativo en 2026 en el corredor sur (Maputo-Beira-Tete); kit configurable antes de entrar o vía distribuidor local.",
        "SIM local (Vodacom, Movitel, Tmcel) como respaldo en zonas sin cobertura satelital directa.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente y vacuna antirrábica en vigor, exigibles en frontera.",
        "Perro prohibido en el Parque Nacional de Gorongosa; no recomendado en el archipiélago de Bazaruto (solo acceso en barco).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Malaria presente en todo el territorio, incluida la costa: profilaxis a valorar con Sanidad Exterior.",
        "Fiebre amarilla: certificado exigido si se procede de zona endémica.",
        "Hospital Central de Maputo y Clínica Cruz Azul como mejores referencias sanitarias del tramo; seguro con evacuación médica real imprescindible fuera de Maputo.",
    ],
    seguridad_intro="Fuera de Cabo Delgado (excluido por completo), el corredor sur de Mozambique es manejable con precaución urbana normal, reforzada en Maputo por el repunte de criminalidad de 2026.",
    seguridad=[
        "No circular de noche por la EN1 entre Xai-Xai y Maputo.",
        "Aparcamiento vigilado en Maputo y Beira; no dejar objetos a la vista dentro del vehículo.",
        "Mantenerse informado sobre la evolución de Cabo Delgado aunque quede fuera de ruta, por si afecta a corredores de suministro compartidos con el resto del país.",
    ],
    agua=[
        "Maputo y Beira: agua embotellada sin problema en supermercados.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio, campings y hoteles de Maputo, Vilanculos, Beira y Tete permiten llenar el depósito con manguera; confirmar en recepción.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km en el eje previsto: Maputo → Vilanculos (~700 km, con paradas intermedias en Xai-Xai e Inhambane) → Beira (~470 km) → Tete (~370 km) → Zóbuè (~90 km), todos con estaciones formales.",
        "Maputo y Beira concentran la mejor oferta y calidad del país (Petromoc, Total, Puma); repostar a fondo en ambas antes de tramos más largos.",
    ],
    pendientes=[
        ("Declaración SARS/TMS", "Completar en Sudáfrica antes de cruzar Lebombo/Ressano Garcia"),
        ("Visado", "Reconfirmar exención/condiciones 30-60 días antes"),
        ("Cabo Delgado", "Monitorizar evolución del conflicto aunque quede fuera de ruta"),
        ("Perro", "Confirmar cuidador en Gorongosa (Chitengo) y logística de Bazaruto"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Emergencia consular española (Maputo, 24h): (+258) 84 32 82 900 · Embajada de España en Maputo: (+258) 21 49 20 25/27/30.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

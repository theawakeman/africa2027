# -*- coding: utf-8 -*-
"""Guinea (Conakry) — ficha completa (9 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Conakry", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=9.5092, lon=-13.7122,
         desc="Capital y única gran base logística del país: puerto, aeropuerto internacional, bancos, talleres y la embajada de España. Punto obligado para provisiones, trámites y descanso antes o después del Fouta Djallon.",
         credit="Alpha hmd · CC BY-SA 4.0", source=W + "Un%20aper%C3%A7u%20de%20la%20ville%20de%20conakry.jpg?width=900"),
    dict(n=2, name="Îles de Los", cat="Naturaleza · costa", prio="Media", dog="pendiente de confirmación oficial", time="1 día",
         lat=9.4500, lon=-13.8300,
         desc="Archipiélago frente a Conakry (Kassa, Room), playas tranquilas y antiguo enclave colonial; se llega en piragua o lancha desde el puerto de Conakry. Confirmar si se admite el perro en el trayecto marítimo antes de organizar la excursión.",
         credit="Cnes - Spot Image · CC BY-SA 3.0", source=W + "Los%20island%20SPOT%201386.jpg?width=900"),
    dict(n=3, name="Fouta Djallon — Labé y Dalaba", cat="Naturaleza · montaña", prio="Alta", dog="permitido", time="2–3 días",
         lat=11.3167, lon=-12.2833,
         desc="Altiplano de sabana y bosque de galería, clima fresco, base para trekking y cascadas; Labé es la capital regional con servicios básicos (talleres, mercado, alojamiento). Carreteras principales asfaltadas con baches crecientes; pistas secundarias solo transitables en estación seca (noviembre-marzo).",
         credit="Maarten van der Bent · CC BY-SA 2.0", source=W + "Fouta%20Djallon%20(14604722652).jpg?width=900"),
    dict(n=4, name="Chutes de Kinkon (Pita)", cat="Naturaleza", prio="Alta", dog="permitido", time="½ día",
         lat=10.9833, lon=-12.4000,
         desc="Cascada y presa hidroeléctrica cerca de Pita, en el corazón del Fouta Djallon; acceso por pista corta desde la carretera principal. Combinar con las cercanas cascadas de Kambadaga (a ~1 h en pista/mototaxi desde Pita).",
         credit="Sayd224 · CC BY 4.0", source=W + "Chute%20de%20Kinkon.jpg?width=900"),
    dict(n=5, name="Boké — fuerte y museo colonial", cat="Patrimonio", prio="Media", dog="permitido", time="½ día",
         lat=10.9333, lon=-14.3000,
         desc="Antiguo puesto colonial francés con fuerte y museo regional; ciudad de paso en la región minera (bauxita) camino de la frontera con Guinea-Bissau, que el protocolo del proyecto evita expresamente.",
         credit="Aboubacarkhoraa · CC BY-SA 4.0", source=W + "Mus%C3%A9e%20de%20Bok%C3%A9.jpg?width=900"),
]

_CAT_COLOR = {
    "ciudad · servicios": "azul", "naturaleza · costa": "turquesa",
    "naturaleza · montaña": "verde", "naturaleza": "verde", "patrimonio": "marron",
}
for _p in POIS:
    _url = _p.pop("source")
    _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower()
    _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Sambaïlo / Diaobé (desde Kédougou, Senegal)", "Frontera", 12.5500, -13.3500,
     "Paso terrestre principal desde Senegal, evitando expresamente Guinea-Bissau. ~20 km de tierra de nadie entre puestos; ferry antiguo sobre el río Bantala que puede estar averiado — prever demoras. Horario habitual 08:00–18:30. Documentos del vehículo (carta verde, laissez-passer/CPD) deben estar en regla antes de llegar."),
    ("Embajada de España en Conakry", "Consular", 9.5300, -13.6800,
     "Place Almamy Samory Touré, Bâtiment R2000, 6º piso, Moussoudougou, Coléah. Cancillería +224 664 20 22 01. Sección consular +224 613 33 90 90. Emergencia consular grave +224 664 33 54 93. Coordenada urbana aproximada."),
    ("Hôpital National Donka — Conakry", "Hospital", 9.5350, -13.6950,
     "Principal hospital de referencia del país; capacidad limitada para politraumatismos — el seguro de evacuación es imprescindible en todo el país. Coordenada urbana aproximada."),
    ("Centre médical — Labé", "Hospital", 11.3167, -12.2833,
     "Recurso sanitario regional del Fouta Djallon; para casos graves, evacuación a Conakry o a Dakar. Coordenada urbana aproximada."),
    ("Combustible · Labé", "Combustible", 11.3167, -12.2833,
     "Estaciones formales (Total, Petroguinée) en el centro regional del Fouta Djallon; confirmar existencias antes de tramos secundarios."),
    ("Combustible · Conakry", "Combustible", 9.5092, -13.7122,
     "Mejor oferta y calidad del país; repostar aquí siempre que sea posible antes de tramos interiores."),
    ("Agua potable · Conakry y Labé (garrafas/supermercados)", "Agua potable", 9.5092, -13.7122,
     "Agua embotellada disponible en Conakry y Labé; fuera de estas ciudades, tratar o hervir el agua local antes de consumirla."),
]

DRONE_CALLOUT = ("warn", "Sin normativa civil turística clara: tratar como restringido",
                  "No se ha localizado un procedimiento público de autorización de drones para visitantes en Guinea. Ante la falta de información oficial verificable, el criterio del proyecto es no volarlo sin autorización previa y por escrito de la autoridad de aviación civil guineana (ANAC-Guinée) o del Ministerio de Transportes, especialmente cerca de Conakry (aeropuerto, puerto, edificios oficiales).")

STARLINK_CALLOUT = ("danger", "Sin confirmación de disponibilidad activa a fecha de esta revisión",
                     "Revisar el mapa oficial de Starlink 30–60 días antes de entrar. Guinea no ha aparecido de forma consistente como mercado activo en las fuentes consultadas: no planificarlo como comunicación primaria. La cobertura móvil (Orange, MTN/Areeba) es aceptable en Conakry y Labé, y se degrada en pistas secundarias del Fouta Djallon.")

DOG_MATRIX = [
    ("Trayecto marítimo a Îles de Los", "pendiente de confirmación oficial", "Confirmar con el operador de la lancha/piragua antes de reservar la excursión."),
    ("Conakry (mercados, zonas urbanas densas)", "permitido con condiciones", "Correa corta y bozal de repuesto; calor y tráfico intenso."),
    ("Fouta Djallon, cascadas, Boké", "permitido", "Sin restricción específica publicada; agua y sombra en trekking."),
]

SOURCES = [
    ("Visamundi · e-Visa Guinea Conakry", "https://www.visamundi.co/en/destinations/guinea/"),
    ("PAF Guinée · información de visado", "https://www.paf.gov.gn/dnpaf/?page_id=335&lang=en"),
    ("Digital Logistics Capacity Assessment · paso fronterizo de Sambaïlo", "https://lca.logcluster.org/235-guinea-border-crossing-sambailo"),
    ("Embajada de España en Guinea · horario, localización y contacto", "https://www.exteriores.gob.es/Embajadas/conakry/es/Embajada/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx"),
    ("Scoot West Africa · guía del Fouta Djallon", "https://scootwestafrica.com/guide-fouta-djallon-guinea/"),
    ("Travel.State.gov · Guinea travel advisory (referencia internacional)", "https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Guinea.html"),
    ("Starlink · mapa de disponibilidad", "https://starlink.com/map"),
    ("Comisión Europea · animales de compañía", "https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_es.htm"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

CORRIDOR = [
    (12.5500, -13.3500),  # Sambaïlo (entrada desde Senegal)
    (11.3167, -12.2833),  # Labé
    (10.9833, -12.4000),  # Pita / Kinkon
    (9.5092, -13.7122),   # Conakry
    (10.9333, -14.3000),  # Boké
]

HISTORIA_RESUMEN = ("Guinea (Guinea-Conakry) fue la primera colonia francesa en África en optar por la independencia inmediata en 1958, rechazando en referéndum la propuesta de comunidad francesa de De Gaulle, un gesto de dignidad que le costó una ruptura brutal con Francia "
                     "y décadas de dictaduras (Sékou Touré, luego Lansana Conté) sostenidas sobre una de las mayores reservas de bauxita del planeta, con una frágil transición democrática interrumpida por sucesivos golpes de Estado, el último en 2021.")

HISTORIA_SECCIONES = [
    ("Imperios y reinos previos a la colonización",
     "El territorio formó parte de la periferia del imperio de Malí y albergó posteriormente el imperio fulani del Futa Jalón (siglo XVIII), una teocracia islámica en las tierras altas centrales que dejó una fuerte impronta religiosa y política en la Guinea actual."),
    ("Colonización francesa y resistencia armada",
     "Francia encontró una resistencia prolongada a la conquista, encabezada por el almamy Samory Touré, cuyo imperio Wassulu resistió durante casi dos décadas antes de su derrota en 1898; Guinea fue integrada después en el África Occidental Francesa como colonia de plantación y extracción minera."),
    ("El «no» de 1958 y la era de Sékou Touré",
     "En el referéndum de 1958 sobre la comunidad francesa propuesta por De Gaulle, Guinea fue la única colonia en votar «no», bajo el liderazgo de Ahmed Sékou Touré, obteniendo la independencia inmediata; Francia respondió retirando abruptamente personal y equipamiento, y Sékou Touré gobernó hasta su muerte en 1984 con un régimen de partido único marcado por la represión política."),
    ("Situación actual: recursos minerales y fragilidad democrática",
     "Tras la muerte de Sékou Touré, el país vivió otra larga dictadura militar bajo Lansana Conté (1984-2008) y sucesivos golpes de Estado, el más reciente en 2021, que derrocó al presidente Alpha Condé. Guinea alberga algunas de las mayores reservas mundiales de bauxita (aluminio) y hierro, una riqueza mineral que convive con niveles de pobreza elevados y una transición política hacia elecciones civiles aún en curso."),
]

HISTORIA_FUENTES = [
    ("BBC News · Guinea country profile", "https://www.bbc.com/news/world-africa-13442051"),
    ("Encyclopaedia Britannica · Guinea, History", "https://www.britannica.com/place/Guinea/History"),
    ("Reuters · cobertura de la transición política en Guinea", "https://www.reuters.com/world/africa/"),
]

SPEC = dict(
    slug="guinea", name="Guinea", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Sambaïlo / Diaobé (desde Kédougou, Senegal)"),
        ("SALIDA", "Hacia Sierra Leona (frontera de Pamelap)"),
        ("SEGURIDAD", "precaución · situación política a vigilar"),
        ("FRONTERA TERRESTRE", "operativa, con demoras (ferry sobre el Bantala)"),
        ("VISADO", "eVisa previa obligatoria (~90 días, ~129 €)"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[10.8, -12.8], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada. La frontera con Guinea-Bissau queda excluida sin excepción por protocolo del proyecto.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Guinea se recorre entrando directamente desde Senegal por Sambaïlo/Diaobé, evitando por completo el territorio de Guinea-Bissau (excluido por protocolo). "
                   "El interés principal es el altiplano fresco del Fouta Djallon (Labé, Pita, cascadas de Kinkon y Kambadaga), con Conakry como única base logística de talla nacional "
                   "y Boké como paso final hacia el corredor costero de Sierra Leona."),
    decision="Entrada exclusivamente por Sambaïlo/Diaobé desde la región de Kédougou (Senegal); ninguna ruta que roce Guinea-Bissau se considera, ni siquiera como atajo.",
    facts=[
        ("Ventana prevista", "Dentro del corredor de bajada, tras Senegal."),
        ("Entrada", "Sambaïlo/Diaobé desde Kédougou (Senegal); ~20 km de tierra de nadie y ferry antiguo sobre el Bantala."),
        ("Salida", "Hacia Sierra Leona por el paso de Pamelap (a verificar estado operativo cercano a la fecha del viaje)."),
        ("Visado", "eVisa previa obligatoria para pasaporte español; ~90 días de validez, entrada única, coste aproximado 129 €, 72 h de trámite (recomendable pedir con 10 días de margen)."),
        ("Seguridad", "Precaución general; situación política guineana sujeta a cambios — revisar avisos 72 h antes de entrar."),
        ("Comunicaciones", "Cobertura aceptable en Conakry y Labé; se degrada en pistas secundarias del Fouta Djallon."),
    ],
    alerts=[
        "Frontera de Guinea-Bissau: exclusión total por protocolo del proyecto — ninguna variante de ruta debe rozar su territorio, ni siquiera como atajo de emergencia.",
        "El ferry de Sambaïlo sobre el río Bantala es antiguo y a menudo no funciona: prever demoras de horas y tener combustible/agua de margen.",
        "Certificado de fiebre amarilla obligatorio sin excepción para entrar en Guinea: llevarlo siempre encima junto al pasaporte.",
        "Retirada máxima de efectivo limitada (~40 € por operación en cajeros); llevar euros en efectivo como respaldo.",
    ],
    ruta_intro="Bloque relativamente corto dentro del corredor de bajada; el Fouta Djallon concentra el interés principal.",
    route_rows=[
        ("Entrada y Fouta Djallon", "Sambaïlo → Labé → Dalaba/Pita", "Clima fresco de altiplano; base para cascadas y trekking"),
        ("Cascadas", "Kinkon y Kambadaga (Pita)", "Accesibles por pista corta; combinar en el mismo día"),
        ("Conakry", "Capital y costa", "Única gran base de servicios, talleres y trámites consulares"),
        ("Hacia Sierra Leona", "Boké → frontera de Pamelap", "Última etapa; confirmar estado de la carretera y del paso antes de salir"),
    ],
    offroad=[
        "Pistas secundarias del Fouta Djallon (entorno de Doucki, gargantas de arenisca): solo en estación seca (noviembre-marzo); tramos rocosos y estrechos que exigen 4x4 real.",
        "Acceso a las cascadas de Kambadaga desde Pita: pista de tierra con baches, transitable en 4x4 durante todo el año salvo lluvias fuertes.",
    ],
    acampada=[
        "Labé y Dalaba: alojamientos sencillos tipo bungalow con acceso para vehículo; opción más práctica que la acampada libre.",
        "Conakry: aparcamiento vigilado recomendado por la densidad urbana y el tráfico; evitar dejar los vehículos sin vigilancia toda la noche.",
    ],
    visado=[
        "eVisa obligatoria para pasaporte español, tramitada antes de llegar a la frontera terrestre (no confirmado visado a la llegada en pasos terrestres — gestionar con antelación).",
        "Requisitos: pasaporte con 6+ meses de vigencia, certificado internacional de fiebre amarilla, billete de salida o justificante de itinerario, foto biométrica reciente.",
        "Confirmar 30–60 días antes si el paso de Sambaïlo acepta la eVisa impresa o exige trámite adicional en el propio puesto.",
    ],
    fronteras_rows=[
        ("Entrada", "Sambaïlo/Diaobé (desde Kédougou, Senegal)", "Ferry antiguo sobre el Bantala puede estar averiado; documentación del vehículo pre-aprobada recomendable."),
        ("Salida", "Pamelap (hacia Sierra Leona)", "Verificar estado operativo y horarios 72 h antes de la salida prevista."),
    ],
    vehiculos=[
        "CPD recomendado; laissez-passer temporal en frontera como alternativa si no se dispone de carnet.",
        "Carte Brune (CEDEAO) como seguro de responsabilidad civil regional; confirmar que cubre el tramo guineano antes de entrar.",
        "Llevar copias impresas de toda la documentación: el paso de Sambaïlo no siempre dispone de medios para verificar documentos digitales.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Sin procedimiento turístico publicado: solicitar autorización previa por escrito a la autoridad de aviación civil o, en su defecto, no volar el dron en el país.",
        "Evitar sobrevolar Conakry (aeropuerto, puerto, edificios de gobierno) bajo cualquier circunstancia.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Revisar el mapa oficial de Starlink 30–60 días antes de entrar; no está confirmado como mercado activo a fecha de esta revisión.",
        "SIM/eSIM local (Orange Guinée, MTN/Areeba) como conectividad principal en Conakry y el Fouta Djallon.",
    ],
    perro_intro=[
        "No se ha localizado normativa pública específica de importación de perros para Guinea: aplicar como base el pasaporte UE de mascota, microchip y certificado antirrábico vigente, y confirmar por escrito con la embajada de Guinea en España o la autoridad veterinaria antes de entrar.",
        "Llevar certificado sanitario reciente y cartilla de vacunación visible para el control fronterizo de Sambaïlo.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional obligatorio, sin excepciones, para entrar en el país.",
        "Malaria presente en todo el territorio: profilaxis a valorar con Sanidad Exterior antes del viaje.",
        "Agua embotellada o tratada; el saneamiento urbano en Conakry es limitado fuera de las zonas turísticas.",
        "Seguro con evacuación médica: la capacidad hospitalaria fuera de Conakry es muy limitada.",
    ],
    seguridad_intro="Guinea atraviesa una situación política cambiante; sin conflicto activo en el itinerario previsto, pero con recomendación de revisar avisos oficiales justo antes de entrar y evitar concentraciones o manifestaciones.",
    seguridad=[
        "Evitar desplazamientos nocturnos fuera de núcleos urbanos por el estado de las carreteras y la señalización deficiente.",
        "No fotografiar infraestructura militar, puertos ni aeropuertos sin autorización expresa.",
        "Llevar siempre efectivo en euros como respaldo ante límites de retirada en cajeros.",
        "Revisar el aviso de Exteriores 72 h antes de entrar por si cambia la clasificación de seguridad del país.",
    ],
    agua=[
        "Conakry y Labé: agua embotellada en supermercados y tiendas; fuera de estas ciudades, tratar o hervir el agua local.",
        "Cascadas y ríos del Fouta Djallon no son fuente potable fiable sin tratamiento.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio de Conakry y Labé y los hoteles/misiones católicas del Fouta Djallon suelen aceptar llenar bidones con manguera; en zona rural, confirmar con la comunidad antes de usar un pozo compartido.",
    ],
    combustible=[
        "Sin riesgo de gap de 500 km: Sambaïlo → Labé (~140 km) → Conakry (~440 km) → Boké (~300 km) cubren el itinerario con estaciones formales en cada núcleo.",
        "Calidad variable fuera de Conakry: repostar con margen en la capital antes de tramos del interior y evitar combustible de garrafa informal salvo necesidad.",
        "Confirmar puntos recientes en iOverlander antes de cada tramo: la red formal es limitada y algunas estaciones rurales pueden estar secas.",
    ],
    pendientes=[
        ("Requisitos veterinarios del perro", "Confirmar por escrito con la embajada de Guinea o la autoridad veterinaria antes del viaje"),
        ("Estado del ferry de Sambaïlo", "Verificar 7-15 días antes; tener plan B de tiempo si está averiado"),
        ("Frontera de salida (Pamelap)", "Confirmar horario y estado operativo 72 h antes"),
        ("Dron", "Resolver autorización por escrito o excluirlo del país"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía/Gendarmería 117 (variable según región, verificar localmente) · Emergencia consular española: +224 664 33 54 93 (uso exclusivo para emergencias graves).",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

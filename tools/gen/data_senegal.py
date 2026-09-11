# -*- coding: utf-8 -*-
"""Senegal ficha data (revision 8 sep 2026)."""
from site_common import table, callout, bullets, st_pill, gmaps, esc
from kmldata import parse_kml, clean_desc

HISTORIA_RESUMEN = ("Senegal es, junto con Costa de Marfil y Ghana, uno de los países más estables democráticamente de África Occidental, con un pasado marcado por los grandes imperios sahelianos, el trauma de la trata negrera atlántica desde la isla de Gorea, "
                     "un colonialismo francés que hizo de Dakar su capital para toda el África Occidental Francesa, y una tradición ininterrumpida desde 1960 de transiciones de poder sin golpes de Estado, poco común en la región.")

HISTORIA_SECCIONES = [
    ("Imperios sahelianos y el reino de Yolof",
     "El territorio formó parte de la periferia de grandes imperios sahelianos como Ghana y Mali, y albergó el reino de Yolof (o Djolof), una confederación de reinos wólof que dominó la región entre los siglos XIV y XVI antes de fragmentarse en entidades más pequeñas como Cayor y Baol."),
    ("Gorea y la trata atlántica de esclavos",
     "La isla de Gorea, frente a Dakar y hoy Patrimonio de la Humanidad de la UNESCO, fue uno de los mayores puntos de partida de la trata negrera atlántica entre los siglos XV y XIX, con la llamada «Casa de los Esclavos» como testimonio conmovedor de ese comercio, gestionado sucesivamente por portugueses, holandeses, ingleses y franceses."),
    ("Colonia francesa y capital de la AOF",
     "Francia consolidó su control sobre Senegal a lo largo del siglo XIX, convirtiendo Dakar en 1902 en la capital de todo el África Occidental Francesa (AOF), un conjunto de ocho colonias; Senegal disfrutó de un estatus administrativo algo distinto a otras colonias, con representación parlamentaria en París desde 1848 para los habitantes de las «cuatro comunas», un precedente temprano poco habitual en el África colonial."),
    ("Independencia y una tradición democrática poco común",
     "Senegal se independizó en 1960 bajo el poeta-presidente Léopold Sédar Senghor, y ha mantenido desde entonces, con la excepción de tensiones puntuales, una tradición de alternancia democrática pacífica sin golpes de Estado militares, algo excepcional en la región; el conflicto de baja intensidad en la región sureña de Casamance, activo desde los años ochenta, se ha ido apagando en la última década sin llegar a afectar al eje turístico principal del país."),
]

HISTORIA_FUENTES = [
    ("BBC News · Senegal country profile", "https://www.bbc.com/news/world-africa-14093674"),
    ("UNESCO · Isla de Gorea, Patrimonio de la Humanidad", "https://whc.unesco.org/en/list/26/"),
    ("Encyclopaedia Britannica · Senegal, History", "https://www.britannica.com/place/Senegal/History"),
]

POI_META = {
    "Delta del Saloum": ("Naturaleza y cultura", "Imprescindible", "requiere autorización escrita en reservas; fuera de ellas, permitido con condiciones", "agua / manglar", "turquesa", "2 días"),
    "Parque Nacional de Djoudj": ("Parque nacional", "Imprescindible", "prohibido", "árbol / fauna", "verde", "1 día"),
    "Saint-Louis – isla histórica": ("Patrimonio UNESCO", "Imprescindible", "permitido con condiciones", "patrimonio", "marrón", "1–2 días"),
    "Guet Ndar – barrio pesquero": ("Cultura viva", "Muy recomendable", "permitido con condiciones", "cultura local", "naranja", "2–3 h"),
    "Parque Nacional de la Langue de Barbarie": ("Parque costero", "Muy recomendable", "requiere autorización escrita", "árbol / costa", "verde", "½–1 día"),
    "Lac Rose – lago Retba": ("Paisaje", "Recomendable", "permitido con condiciones", "agua", "turquesa", "½ día"),
    "Isla de Gorée": ("Patrimonio UNESCO", "Imprescindible", "pendiente de confirmación oficial para chalupa y museos", "patrimonio", "marrón", "½–1 día"),
    "Museo de las Civilizaciones Negras": ("Museo", "Muy recomendable", "prohibido en el interior", "museo", "morado", "2–3 h"),
    "Monumento del Renacimiento Africano": ("Monumento y mirador", "Recomendable", "permitido con condiciones en exterior", "monumento", "marrón", "1–2 h"),
    "Joal-Fadiouth – isla de conchas": ("Cultura y manglar", "Muy recomendable", "permitido con condiciones; confirmar puente y cementerio", "aldea / patrimonio", "marrón", "½ día"),
    "Toubacouta – base del delta del Saloum": ("Base de excursiones", "Imprescindible", "permitido con condiciones; confirmar alojamiento y piragua", "binoculares / base", "turquesa", "2 noches"),
    "Parque Nacional de Niokolo-Koba": ("Parque nacional", "Imprescindible", "prohibido", "árbol / fauna", "verde", "2 días"),
    "Kédougou – base del Senegal oriental": ("Base logística", "Operativa", "permitido con condiciones", "herramienta / base", "azul", "1–2 noches"),
    "Bandafassi – puerta del País Bassari": ("Paisaje cultural UNESCO", "Muy recomendable", "requiere autorización escrita del guía/comunidad", "aldea / cultura", "naranja", "½–1 día"),
    "Iwol – aldea bedik": ("Cultura y senderismo", "Imprescindible", "requiere autorización escrita del guía/comunidad", "senderismo / aldea", "naranja", "½–1 día"),
    "Cascada de Dindéfelo": ("Naturaleza y senderismo", "Muy recomendable", "requiere autorización escrita de la gestión local", "cascada", "turquesa", "½–1 día"),
    "Ethiolo – cultura bassari": ("Paisaje cultural UNESCO", "Recomendable", "requiere autorización escrita del guía/comunidad", "aldea / cultura", "naranja", "1 día"),
    "Museo Théodore Monod de Arte Africano": ("Museo", "Recomendable", "prohibido en el interior", "museo", "morado", "2 h"),
    "Reserva de Fauna del Ferlo Norte": ("Reserva de fauna", "Opcional", "requiere autorización escrita", "árbol / fauna", "verde", "1 día"),
    "Enclos de Katané — fauna saharosaheliana": ("Área de fauna", "Opcional", "requiere autorización escrita", "fauna", "verde", "½ día"),
    "Ranérou — puerta del Ferlo": ("Base logística", "Opcional", "permitido con condiciones", "herramienta / base", "azul", "1 noche"),
    "Reserva de Fauna del Ferlo Sur": ("Reserva de fauna", "Opcional", "requiere autorización escrita", "árbol / fauna", "verde", "½–1 día"),
    "Pista 4x4 Ranérou–Tambacounda — travesía del Ferlo": ("Pista 4x4", "Opcional", "pendiente de confirmación oficial si atraviesa núcleos protegidos", "vehículo 4x4", "gris", "1 día"),
}
POI_ORDER = list(POI_META)

LOGISTICS = [
    ("Embajada de España en Dakar", "Consular", 14.66040, -17.43520, "+221 33 889 65 80 / +221 33 821 30 81 · emb.dakar@maec.es"),
    ("Consulado General de España en Dakar", "Consular", 14.70320, -17.47020, "+221 33 869 07 07 · emergencia +221 77 569 28 89 · cog.dakar@maec.es"),
    ("Hôpital Principal de Dakar", "Hospital", 14.66128, -17.43479, "Urgencias; 1 Avenue Nelson Mandela. SAMU: 1515; confirmar antes de desplazarse."),
    ("Centre Hospitalier Régional de Saint-Louis", "Hospital", 16.02284, -16.50597, "+221 77 289 02 44 · Boulevard Abdoulaye Mar Diop."),
    ("Centre Hospitalier Régional de Tambacounda", "Hospital", 13.75328, -13.67261, "+221 33 981 10 28 / +221 33 981 12 18."),
    ("Centre Hospitalier Régional Amath Dansokho — Kédougou", "Hospital", 12.55200, -12.18500, "+221 78 163 78 39 · coordenada urbana aproximada."),
    ("Centre de santé de Ranérou", "Hospital", 15.29808, -13.96239, "Capacidad limitada; coordenada provisional; no sustituye evacuación."),
    ("Paso fronterizo Kalifourou — salida hacia Guinea", "Frontera", 12.92415, -13.63848, "Control senegalés del corredor base; revalidar apertura, horario y trámites."),
    ("Paso fronterizo Boundou Fourdou–Sambaïlo — entrada en Guinea", "Frontera", 12.58241, -13.37191, "Entrada guineana hacia Koundara; posición operativa a confirmar."),
    ("Paso Karang–Amdalai — Senegal/Gambia (alternativa)", "Frontera", 13.59169, -16.42208, "No forma parte del corredor base."),
    ("Paso Keur Ayib–Farafenni — Senegal/Gambia (alternativa)", "Frontera", 13.59335, -15.60578, "No forma parte del corredor base."),
    ("Combustible · Saint-Louis", "Combustible", 16.02940, -16.48940, "Estaciones formales (Total, Elton, Shell) en la entrada de la ciudad; repostar tras la frontera de Diama."),
    ("Combustible · Dakar", "Combustible", 14.71670, -17.46770, "Mejor oferta y calidad del país; repostar aquí antes del bloque del Ferlo o del Saloum."),
    ("Combustible · Tambacounda", "Combustible", 13.76670, -13.66670, "Última ciudad grande con oferta amplia antes de Kédougou y el bloque oriental."),
    ("Combustible · Kédougou", "Combustible", 12.55780, -12.17400, "Estaciones formales limitadas; repostar a fondo antes de Bandafassi, Iwol y Dindéfelo."),
    ("Agua potable · Dakar, Saint-Louis, Tambacounda (supermercados y garrafas)", "Agua potable", 14.71670, -17.46770, "Agua embotellada disponible en las ciudades principales del itinerario; en el bloque del Ferlo y del Bassari, cargar reserva completa antes de salir de Kédougou o Ranérou."),
]

ROUTE = [
    ("1", "Diama → Saint-Louis", "Entrada, aduanas, seguros, SIM y descanso", "No añadir Djoudj el día de frontera"),
    ("2", "Saint-Louis + Guet Ndar", "Patrimonio e inmersión local", "A pie; aparcamiento vigilado"),
    ("3", "Djoudj", "Piragua y observación de aves", "Perro prohibido; visita solo con cuidado resuelto"),
    ("4", "Langue de Barbarie", "Estuario, dunas y aves", "Autorización escrita para el perro o rotación"),
    ("5", "Saint-Louis → Lac Rose", "Traslado costero y parada paisajística", "Llegar con luz"),
    ("6–7", "Dakar + Gorée", "Gorée; uno o dos museos; reabastecimiento", "Vehículos vigilados; evitar sobrecargar la ciudad"),
    ("8", "Dakar → Joal-Fadiouth", "Isla de conchas y cultura local", "Confirmar acceso del perro"),
    ("9–10", "Toubacouta + Delta del Saloum", "Piragua, manglar, islas y aves", "Alojamiento con aparcamiento y cuidado canino acordados"),
    ("11–13", "Bloque Ferlo (opcional)", "Linguère–Ranérou–Katané–Tambacounda", "Solo con autorización, track reciente, autonomía y salida temprana"),
    ("14", "Tambacounda", "Revisión de vehículos, combustible y provisiones", "Confirmar pistas y seguridad oriental"),
    ("15–16", "Niokolo-Koba", "Parque con guía", "Perro prohibido; exige cuidado verificado o rotación"),
    ("17", "Kédougou", "Base, guía, salud y mantenimiento", "Resolver siguientes excursiones antes de salir"),
    ("18", "Bandafassi + Iwol", "Paisaje cultural y caminata", "Acuerdo previo con guía y comunidad"),
    ("19", "Dindéfelo", "Cascada y bosque", "Menos agua en estación seca; confirmar perro"),
    ("20", "Ethiolo / Salémata", "Cultura bassari", "Opcional si el ritmo o el calor aprietan"),
    ("21", "Kalifourou → Sambaïlo → Koundara", "Salida a Guinea", "Solo corredor oficial; no conducir de noche"),
]

SOURCES = [
    ("MAEC España · Recomendaciones de viaje Senegal", "https://www.exteriores.gob.es/Embajadas/dakar/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"),
    ("France Diplomatie · Sécurité Sénégal", "https://www.diplomatie.gouv.fr/fr/conseils-aux-voyageurs/conseils-par-pays-destination/senegal/"),
    ("FCDO Reino Unido · Regional risks", "https://www.gov.uk/foreign-travel-advice/senegal/regional-risks"),
    ("FCDO Reino Unido · Safety and security", "https://www.gov.uk/foreign-travel-advice/senegal/safety-and-security"),
    ("Embajada de España en Dakar · contacto", "https://www.exteriores.gob.es/Embajadas/dakar/es/Embajada/Paginas/Contacto.aspx"),
    ("Consulado General de España en Dakar · contacto", "https://www.exteriores.gob.es/Consulados/dakar/es/Consulado/Paginas/Horario%2C-Localizacion-y-Contacto.aspx"),
    ("Aduanas de Senegal · importación temporal", "https://www.douanes.sn/ndn217/?lang=en"),
    ("Aduanas de Senegal · admisión temporal excepcional", "https://www.douanes.sn/benefit-from-the-exceptional-temporary-admission-eta/"),
    ("RACE · Carnet de Passages en Douane", "https://www.race.es/servicios/carnet-de-passages"),
    ("CEDEAO · Estados de la Carte Brune", "https://www.cartebrune.org/-Etats-Membres-.html"),
    ("Dirección de Parques Nacionales de Senegal · ecoturismo", "https://www.dpn.sn/ecotourisme/"),
    ("UNESCO · Senegal", "https://whc.unesco.org/en/statesparties/sn/"),
    ("CDC · Senegal Traveler View", "https://wwwnc.cdc.gov/travel/destinations/traveler/none/senegal"),
    ("USDA APHIS · requisitos de entrada de mascotas en Senegal", "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-senegal"),
    ("ANACIM · anexo RPAS", "https://www.anacim.sn/IMG/pdf/annexe_5_au_ras_06_-_systemes_d_aeronefs_telepilotes_rpas_.pdf"),
    ("ANACIM · contacto", "https://anacim.sn/"),
    ("Starlink · mapa de disponibilidad Senegal", "https://starlink.com/sn/map"),
    ("APS · autorización de cinco años a Starlink", "https://aps.sn/starlink-une-autorisation-dexploitation-de-cinq-ans-accordee-au-fournisseur-dacces-a-internet-par-satellite-tutelle/"),
    ("CHVD Pikine · hospital veterinario", "https://chvd.sn/"),
    ("Hôtel de la Résidence Saint-Louis · servicios y mascotas", "https://www.hoteldelaresidence.com/services/"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

DOG_MATRIX = [
    ("Djoudj", "prohibido", "Cuidador en Saint-Louis confirmado o rotación"),
    ("Langue de Barbarie", "requiere autorización escrita", "Alojamiento/cuidador en Gandiol o Saint-Louis; rotación"),
    ("Gorée y museos de Dakar", "pendiente de confirmación oficial / prohibido en interiores", "Cuidador verificado o visitas por turnos"),
    ("Delta del Saloum", "requiere autorización escrita en reservas", "Acordar con alojamiento y patrón de piragua; rotación"),
    ("Niokolo-Koba", "prohibido", "Cuidado con pernocta verificado cerca de la entrada o rotación"),
    ("Bandafassi, Iwol, Ethiolo", "requiere autorización escrita", "Acuerdo con guía y comunidad; cuidador en Kédougou o rotación"),
    ("Dindéfelo", "requiere autorización escrita", "Confirmar con gestión comunitaria; cuidador o rotación"),
    ("Ferlo Norte/Sur y Katané", "requiere autorización escrita", "Sin residencia verificada; rotación es el respaldo real"),
]

CORRIDOR = ["Saint-Louis – isla histórica", "Parque Nacional de Djoudj", "Parque Nacional de la Langue de Barbarie",
            "Lac Rose – lago Retba", "Isla de Gorée", "Joal-Fadiouth – isla de conchas",
            "Toubacouta – base del delta del Saloum", "Parque Nacional de Niokolo-Koba",
            "Kédougou – base del Senegal oriental", "Bandafassi – puerta del País Bassari",
            "Cascada de Dindéfelo", "Ethiolo – cultura bassari"]
FERLO = ["Toubacouta – base del delta del Saloum", "Ranérou — puerta del Ferlo",
         "Pista 4x4 Ranérou–Tambacounda — travesía del Ferlo", "Parque Nacional de Niokolo-Koba"]


def get_data(root="../../"):
    """Build the country dict consumed by the generic ficha renderer."""
    kml = parse_kml()
    pois = []
    for n, name in enumerate(POI_ORDER, start=1):
        cat, prio, dog, icon, color, time = POI_META[name]
        it = kml[name]
        desc, dog_note = clean_desc(it["description"])
        pois.append({
            "n": n, "name": name, "cat": cat, "prio": prio, "dog": dog, "icon": icon,
            "color": color, "time": time, "lat": it["lat"], "lon": it["lon"],
            "desc": desc, "dog_note": dog_note, "credit": it["credit"], "source": it["source"],
            "img": f"assets/img/senegal/{n:02d}.jpg",
        })
    logistics = [{"name": n, "cat": c, "lat": la, "lon": lo, "info": i} for n, c, la, lo, i in LOGISTICS]
    corridor = [(kml[n]["lat"], kml[n]["lon"]) for n in CORRIDOR] + [(12.92415, -13.63848), (12.58241, -13.37191)]
    ferlo = [(kml[n]["lat"], kml[n]["lon"]) for n in FERLO]

    d = {
        "slug": "senegal", "name": "Senegal", "revision": "8 sep 2026", "estado": "completa",
        "sub": "Corredor overland · 2 vehículos 4x4 · 3 viajeros · 1 perro",
        "hero_img": "assets/img/senegal/01.jpg",
        "hero_credit": "Delta del Saloum · Unión Europea, Copernicus Sentinel-2",
        "chips": [
            ("CORREDOR", "Diama → Kalifourou"),
            ("RITMO", "17–21 días"),
            ("SEGURIDAD", st_pill("precaución en este y Casamance")),
            ("FRONTERA TERRESTRE", st_pill("abierta · verificar antes")),
            ("CPD", st_pill("recomendado")),
            ("REVALIDACIÓN", "dic 2026"),
        ],
        "center": [14.4, -14.7], "zoom": 7,
        "pois": pois, "logistics": logistics,
        "corridor": corridor, "corridor_alt": ferlo,
        "notice": "Documento operativo sujeto a revalidación final en diciembre de 2026 y en cada frontera.",
    }
    d["historia_resumen"] = HISTORIA_RESUMEN
    d["historia_secciones"] = HISTORIA_SECCIONES
    d["historia_fuentes"] = HISTORIA_FUENTES
    historia = (
        f"<p>{esc(HISTORIA_RESUMEN)}</p>"
        + callout("", "Historia completa · con audio",
                  'Orígenes, colonización, independencia y situación actual, con fuentes y '
                  '<strong>audio tipo podcast</strong> narrado por el propio dispositivo para escuchar mientras se conduce: '
                  '<a href="historia/">leer y escuchar la historia de Senegal →</a>', raw=True)
    )

    # -------- custom section HTML --------
    facts = [
        ("Duración", "17–18 días sin Ferlo; 20–21 días con el bloque Ferlo"),
        ("Perfil", "Naturaleza, cultura local y pocas ciudades; Dakar concentrado en 1–2 días"),
        ("Acampada", "Libre solo con validación local; en ciudades, fronteras y áreas protegidas usar recinto vigilado"),
        ("Conducción", "Evitar totalmente la noche; limitar jornadas largas y entrar en destino con luz"),
        ("Perro", "Restricción principal: autorización escrita en áreas protegidas y prohibición en Djoudj/Niokolo-Koba"),
        ("Vehículos", "CPD recomendado; seguro local y Carte Brune CEDEAO; ver documentación general para trámites"),
        ("Salud", "Malaria en todo el país; fiebre amarilla y documentación sanitaria; rabia canina presente"),
        ("Comunicaciones", "Starlink autorizado y disponible en 2026; mantener SIM local y mensajería satelital"),
    ]
    resumen = (
        callout("", "Decisión de ruta", "Entrada por Diama desde Mauritania. Salida base por Kalifourou–Boundou Fourdou–Sambaïlo hacia Koundara (Guinea). Mali y Guinea-Bissau quedan fuera; Gambia se conserva únicamente como alternativa.")
        + table(("Tema", "Decisión operativa"), facts)
        + "<h3>Alertas que condicionan la visita</h3>"
        + bullets([
            "Perro: no entrar en un área protegida sin autorización escrita; no asumir que permanecer dentro del vehículo resuelve la prohibición.",
            "Niokolo-Koba y Djoudj: visita únicamente con cuidado canino resuelto o rotación entre viajeros.",
            "Fronteras orientales: evitar la noche, usar ejes principales y confirmar seguridad y apertura inmediatamente antes de salir.",
            "CPD: para 17–21 días evita depender de extensiones del passavant; cada vehículo necesita su propia garantía y sellos completos.",
            "Dron: no volar sin autorización ANACIM; un dron con cámara añade autorización del Ministerio del Interior.",
        ], bold_split=True)
    )

    ruta = (
        "<p>Itinerario pensado para enero–febrero de 2027, estación seca. El Ferlo añade aislamiento y pista, pero no es imprescindible para la continuidad del viaje.</p>"
        + table(("Día", "Tramo / base", "Objetivo", "Condición"), ROUTE, cls="num")
        + callout("warn", "Criterio de recorte", "Si se pierde tiempo en frontera, mecánica o cuidado del perro, recortar primero Ferlo, luego uno de los museos de Dakar y finalmente Ethiolo. Mantener Djoudj, Saint-Louis, Gorée, Saloum, Niokolo-Koba y el País Bassari si las restricciones caninas están resueltas.")
        + "<h3>Acampada y pernocta</h3>"
        + bullets([
            "Priorizar campamento discreto y con consentimiento local, lejos de carreteras, puestos de control, fronteras, playas urbanas y núcleos de fauna.",
            "En Dakar, Saint-Louis, Toubacouta, Kédougou y antes de parques: elegir recinto con cierre físico y espacio para ambos 4x4.",
            "No dejar al perro solo en un vehículo cerrado; el calor sigue siendo peligroso en enero, especialmente en interior y este.",
            "En el Ferlo y pistas orientales: confirmar agua, combustible, track, cobertura y hora de llegada; compartir plan de etapa con un contacto.",
        ])
    )

    cpd_rows = [
        ("CPD", "Admisión temporal respaldada por garantía internacional", "Recomendado para 17–21 días y para el resto del viaje", "Cada entrada y salida debe sellarse; un fallo puede bloquear el aval"),
        ("Passavant", "Permiso local de circulación", "Máximo inicial de 10 días según Aduanas; hasta dos extensiones de 15 días", "Obliga a gestionar prórrogas; confirmar dónde y cuándo antes de depender de él"),
        ("Admisión temporal excepcional", "Régimen aduanero condicionado", "Puede alcanzar hasta 6 meses según el caso", "Requiere trámite específico; no asumir concesión en frontera"),
    ]
    fronteras = (
        "<h3>Visado</h3>"
        + bullets([
            "Ciudadanos españoles: MAEC indica exención de visado para estancias inferiores a 90 días; pasaporte con más de seis meses de validez y páginas libres.",
        ])
        + "<h3>Entrada por Diama</h3>"
        + bullets([
            "Cerrar primero la salida mauritana de personas, vehículos y perro; comprobar que cada CPD o permiso temporal queda sellado.",
            "En Senegal: inmigración de cada viajero; aduana de cada vehículo; seguro local/Carte Brune; control veterinario y permiso de importación del perro.",
            "No entregar originales a intermediarios fuera de ventanilla. Fotografiar cada sello antes de abandonar el puesto.",
            "Confirmar horario, tasas y aceptación de los documentos 48–72 h antes. Llegar a primera hora con moneda local y copias.",
        ])
        + "<h3>Vehículos: CPD frente a passavant en Senegal</h3>"
        + table(("Documento", "Qué es", "Encaje", "Riesgo práctico"), cpd_rows)
        + callout("ok", "Decisión", "Solicitar CPD para ambos vehículos antes de salir de España. El passavant queda como contingencia, no como plan principal.")
        + callout("", "Trámites comunes", 'Cómo tramitar el CPD, la autorización de empresa del Grenadier, la documentación de la Delica y el seguro/Carte Brune están en <a href="../../documentacion/">Documentación general</a> — aplican a todo el viaje, no solo a Senegal.', raw=True)
        + "<h3>Seguro en Senegal</h3>"
        + bullets([
            "Comprar responsabilidad civil válida en Senegal y solicitar Carte Brune CEDEAO para continuidad regional; verificar países, vehículo, fechas, matrícula y conductor.",
            "No asumir que la Carta Verde europea cubre Senegal. Conservar recibo y certificado por separado.",
        ])
    )

    drones = (
        callout("danger", "Regla simple", "No volar en Senegal sin autorización de ANACIM. Para un dron con cámara, la normativa publicada exige además autorización del Ministerio del Interior.")
        + bullets([
            "Presentar la solicitud con al menos siete días de antelación; para un viaje itinerante conviene iniciar el expediente varias semanas antes.",
            "Documentación publicada: identidad, antecedentes (<3 meses), justificación del uso para extranjeros, zona/fechas/ruta, características del RPAS, formación del piloto, manuales, seguro RC y formularios de impacto de seguridad.",
            "ANACIM: Aéroport militaire Léopold Sédar Senghor, Dakar-Yoff · anacim@anacim.sn · +221 33 865 60 00. Revalidar el procedimiento aplicable desde el 26 de noviembre de 2026.",
        ])
        + callout("", "Normas comunes de vuelo", 'Las reglas genéricas (aeropuertos, fronteras, multitudes, áreas protegidas) están en <a href="../../documentacion/#drones">Documentación general · drones</a>.', raw=True)
    )

    starlink = (
        callout("ok", "Estado 2026", "Starlink figura disponible en Senegal y recibió una autorización de explotación de cinco años. La página local muestra planes en CFA; el mapa y el plan Roam deben verificarse de nuevo antes de entrar.")
        + bullets([
            "Declarar el equipo si Aduanas lo solicita y conservar factura, número de serie y prueba de titularidad.",
        ])
        + callout("", "Reglas comunes de Starlink Roam", 'Los límites de itinerancia y la preparación del plan están en <a href="../../documentacion/#starlink">Documentación general · Starlink</a>.', raw=True)
    )

    dog_rows = [(z, st_pill(s), p) for z, s, p in DOG_MATRIX]
    perro = (
        "<h3>Entrada del perro en Senegal</h3>"
        + bullets([
            "Solicitar con antelación permiso de importación a la autoridad veterinaria senegalesa. La fuente oficial de viaje de USDA confirma que el permiso es obligatorio; revalidar la aceptación en frontera terrestre por Diama.",
            "Fuentes secundarias sitúan el certificado veterinario dentro de las 72 h previas; confirmar el plazo por escrito.",
        ])
        + callout("", "Requisitos comunes del perro", 'Microchip, pasaporte UE, rabia, titulación serológica y reentrada en la UE: ver <a href="../../documentacion/#perro">Documentación general · perro</a>.', raw=True)
        + "<h3>Matriz canina por zona</h3>"
        + table(("Zona", "Estado", "Plan B obligatorio"), dog_rows)
        + "<h3>Atención veterinaria y cuidado</h3>"
        + table(("Lugar", "Capacidad publicada", "Contacto", "Uso operativo"), [
            ("CHVD Pikine, Dakar", "Hospital veterinario de referencia; urgencias 24/7 publicitadas", "+221 33 838 70 10 · WhatsApp +221 77 749 68 60", "Confirmar hospitalización o guarda antes del viaje"),
            ("Vet Services, Dakar", "Clínica de pequeños animales", "+221 33 832 56 71 · vetservices@orange.sn", "Respaldo clínico; no publica pensión"),
            ("Hôtel de la Résidence, Saint-Louis", "Acepta mascotas con correa; comida/paseo bajo petición", "+221 33 961 12 60", "Candidato para apoyo en Djoudj; confirmar supervisión real"),
            ("Kédougou / Ranérou", "Sin residencia profesional verificada", "—", "Rotación entre viajeros como respaldo obligatorio"),
        ])
        + callout("warn", "Cuidado aún no cerrado", "No hay residencia profesional fiable documentada cerca de Niokolo-Koba, Kédougou o Ranérou. No reservar actividades incompatibles con el perro hasta obtener confirmación directa, fotos del recinto, supervisión, prueba de vacunación y contacto veterinario.")
        + "<h3>Salud humana en Senegal</h3>"
        + bullets([
            "Malaria: CDC sitúa el riesgo en todo Senegal. Elegir profilaxis con Sanidad Exterior; mosquitera, repelente y ropa larga.",
            "Fiebre amarilla: llevar certificado internacional; puede exigirse llegando desde país con riesgo.",
            "Estación seca: valorar vacuna meningocócica; no bañarse en aguas dulces por esquistosomiasis.",
        ])
    )

    seguridad = (
        "<p>MAEC España, France Diplomatie y FCDO coinciden en reforzar precauciones en zonas fronterizas remotas, Casamance y el este próximo a Mali. El corredor base evita Mali y Guinea-Bissau, pero exige revalidación local antes de Niokolo-Koba, Kédougou y la salida a Guinea.</p>"
        + bullets([
            "En Dakar y Saint-Louis: discreción con cámaras/teléfonos, puertas cerradas, nada visible en vehículos y aparcamiento vigilado.",
            "En el este: carreteras principales, no publicar ubicación en tiempo real, preguntar a gendarmería/alojamientos y no acercarse a la frontera de Mali.",
            "Comprar SIM local al inicio y probar llamadas de emergencia, hotspot y cobertura. Contactos con prefijo +221.",
            "Descargar Senegal y Guinea en OsmAnd y esta app en los teléfonos de los tres viajeros.",
        ])
        + callout("", "Protocolo común de seguridad", 'Conducción, controles, check-in diario y escalado están en <a href="../../documentacion/#seguridad">Documentación general · seguridad</a>.', raw=True)
    )

    checklist = [
        ("60–90 días antes", "CPD de ambos vehículos; carta de empresa; visado Guinea; permiso del perro; títulos de rabia"),
        ("30 días antes", "ANACIM si se pretende volar; confirmar Djoudj/Langue/Niokolo/Ferlo; pedir cuidado canino por escrito"),
        ("7–14 días antes", "Seguridad MAEC/Francia/FCDO; apertura Diama y Sambaïlo; seguro/Carte Brune; Starlink Roam"),
        ("48–72 h antes", "Estado de pista Ferlo y Niokolo; combustible; efectivo; alojamiento vigilado; certificados veterinarios"),
        ("En cada frontera", "Fotografiar sellos y documentos; verificar plazo del vehículo y del perro antes de salir del puesto"),
    ]
    pending = [
        ("Ferlo", "Incluir solo si hay autorización, track reciente y tres días de margen"),
        ("Cuidado del perro", "Cerrar opciones reales en Saint-Louis, Dakar y Niokolo/Kédougou; hacer prueba corta si es posible"),
        ("Dron", "Decidir si compensa el expediente; sin autorización, transportar apagado y no volar"),
        ("CPD", "Confirmar con RACE titular/aval del vehículo de empresa y documentación de la Delica"),
        ("Frontera Guinea", "Confirmar apertura y punto de control de Kalifourou/Sambaïlo una semana antes"),
    ]
    gpx = (
        table(("Momento", "Acciones"), checklist)
        + "<h3>Validación GPX específica</h3>"
        + bullets([
            "Marcar como aproximadas Katané, CHR Kédougou, Centre de santé Ranérou y el puesto exacto de Sambaïlo hasta verificación local.",
            "No convertir los puntos de parques en pistas transitables: las trazas internas requieren guía/autorización.",
        ])
        + "<h3>Decisiones pendientes</h3>"
        + table(("Tema", "Criterio de cierre"), pending)
    )

    agua_combustible = (
        "<h3>Agua: recarga de depósitos (beber, ducha, aseo y limpieza)</h3>"
        + "<p>No solo agua de boca: como vehículos de expedición autónomos necesitamos recargar también el depósito de uso general (ducha, aseo, vajilla, limpieza), no solo el agua potable de beber.</p>"
        + bullets([
            "Dakar, Saint-Louis y Tambacounda: agua embotellada en supermercados y tiendas sin ningún problema de suministro.",
            "Recarga de depósito de uso general: estaciones de servicio Total/Shell/Elton de Dakar, Saint-Louis, Tambacounda y Kédougou y los campings de la Petite Côte y Saint-Louis (Zebrabar, Camping de la Langue de Barbarie) aceptan llenar bidones/depósito con manguera; confirmar precio en recepción.",
            "Bloque del Ferlo y del país Bassari (Kédougou, Bandafassi, Iwol, Dindéfelo): cargar reserva completa (mínimo 20-30 l por vehículo, beber y uso general) antes de salir de Tambacounda o Kédougou; sin garantía fiable en pistas y aldeas.",
        ])
        + "<h3>Combustible</h3>"
        + bullets([
            "Sin riesgo de gap de 500 km en el eje principal: Diama → Saint-Louis (~40 km) → Dakar (~270 km) → Tambacounda (~440 km) → Kédougou (~220 km), todos con estaciones formales.",
            "Bloque del Ferlo (Linguère-Ranérou-Katané, opcional): oferta escasa e informal; repostar a fondo en Dakar o Saint-Louis antes de entrar y no confiar en encontrar gasóleo de calidad por el camino.",
            "Kédougou es la última plaza con estaciones formales antes de Bandafassi, Iwol, Dindéfelo y la frontera de Guinea: salir siempre con el depósito lleno.",
        ])
        + callout("", "Fuentes cruzadas", 'Puntos y comentarios recientes verificados también en <a href="https://ioverlander.com/" target="_blank" rel="noopener">iOverlander</a> y <a href="https://tracks4africa.co.za/" target="_blank" rel="noopener">Tracks4Africa</a>; revisar la fecha del último comentario antes de confiar en un punto.', raw=True)
        + callout("", "Criterio común del proyecto", 'Estrategia general de depósitos, potabilización y calidad de gasóleo: ver <a href="../../documentacion/#agua-combustible">Documentación general · agua y combustible</a>.', raw=True)
    )

    d["custom_sections"] = [
        ("resumen", "Resumen operativo", resumen),
        ("historia", "Historia y contexto", historia),
        ("ruta", "Ruta propuesta", ruta),
        ("agua-combustible", "Agua y combustible", agua_combustible),
    ]
    d["custom_sections_post"] = [
        ("fronteras", "Visado, fronteras y vehículos", fronteras),
        ("drones", "Drones", drones),
        ("starlink", "Starlink", starlink),
        ("perro", "Perro y salud", perro),
        ("seguridad", "Seguridad y comunicaciones", seguridad),
        ("gpx", "GPX, validación y decisiones", gpx),
    ]
    d["sources"] = SOURCES
    d["sources_note"] = "Consulta realizada el 8 de septiembre de 2026. Las fuentes cambian; el enlace y la fecha forman parte del dato operativo."
    d["emergency"] = "Policía 17 · Bomberos 18 · Gendarmería 123 · Ambulancia/SAMU: probar 15 y 1515. Consulado de España: +221 77 569 28 89. Guardar también en papel y comprobar al comprar la SIM."
    d["matrix_note"] = "Los nombres y coordenadas coinciden con la exportación KMZ del 8 de septiembre de 2026. Los puntos anónimos Punto 19, Punto 42 y Punto 43 no se consideran parte de Senegal."
    return d

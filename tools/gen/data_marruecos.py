# -*- coding: utf-8 -*-
"""Marruecos — ficha completa (9 sep 2026). Fotos: Wikimedia Commons (hotlink + crédito)."""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(n=1, name="Chefchaouen", cat="Patrimonio", prio="Media", dog="permitido", time="1 día",
         lat=35.1688, lon=-5.2636,
         desc="La «ciudad azul» del Rif: medina encalada en tonos añil, callejones peatonales y talleres de artesanía. Parada clásica de aclimatación tras el desembarco en Tánger Med, antes de bajar hacia Fez.",
         credit="Allenfleming · CC BY-SA 4.0", source=W + "Chefchaouen%20(Blue%20City).jpg?width=900"),
    dict(n=2, name="Volubilis", cat="Patrimonio romano", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=34.0742, lon=-5.5547,
         desc="Ruinas romanas mejor conservadas del Magreb (mosaicos, arco de Caracalla, capitolio); yacimiento UNESCO junto a Mulay Idriss. Perro con correa en el recinto abierto; sombra escasa en verano.",
         credit="FuriousYogi · CC BY-SA 4.0", source=W + "Ruins%20of%20Roman%20Mosaic%20floor%20in%20Volubilis%2C%20Morocco.jpg?width=900"),
    dict(n=3, name="Fez el Bali (medina y curtidurías)", cat="Patrimonio", prio="Media", dog="requiere autorización escrita", time="1 día",
         lat=34.0631, lon=-4.9787,
         desc="La medina medieval más grande y viva del mundo árabe: Chouara (curtidurías), Qaraouiyine y miles de callejones sin vehículos. Acceso de perro a curtidurías y zocos cubiertos sujeto a criterio del guía/propietario: confirmar antes de entrar.",
         credit="Tulit · CC BY-SA 4.0", source=W + "Tanneries%20in%20Fes.jpg?width=900"),
    dict(n=4, name="Erg Chebbi — Merzouga", cat="Desierto", prio="Alta", dog="permitido con condiciones", time="1–2 días",
         lat=31.0801, lon=-4.0134,
         desc="Las mayores dunas de Marruecos (hasta 150 m), puerta al Sáhara argelino. Bivac en auberges con parking para 4x4, salidas en pista de arena suelta; agua y sombra limitadas para el perro en las horas centrales.",
         credit="Nomadz · CC BY-SA 3.0", source=W + "Dunes-Merzouga-Erg%20Chebi.JPG?width=900"),
    dict(n=5, name="Garganta del Todra", cat="Naturaleza · 4x4", prio="Alta", dog="permitido", time="½–1 día",
         lat=31.5810, lon=-5.5809,
         desc="Cañón calizo de paredes de hasta 300 m; pista remontable en vehículo hasta el estrechamiento y a pie/con guía más allá. Combinar con Dades para un bucle de gargantas.",
         credit="Jon Lean · CC BY-SA 2.0", source=W + "Todra%20Gorge.jpg?width=900"),
    dict(n=6, name="Aït Benhaddou", cat="Patrimonio UNESCO", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=31.0472, lon=-7.1319,
         desc="Ksar de tierra apisonada, plató de cine (Gladiator, Juego de Tronos) y ejemplo mejor conservado de arquitectura preshariana del Alto Atlas. Cruce del río a pie o en pasarela improvisada según caudal.",
         credit="cliff williams · CC BY-SA 2.0", source=W + "A%C3%AFtBenhaddou%20Morocco%202.jpg?width=900"),
    dict(n=7, name="Marrakech — Jemaa el-Fnaa", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1–2 días",
         lat=31.6258, lon=-7.9891,
         desc="Plaza-mercado UNESCO (patrimonio inmaterial), base logística mayor del sur: talleres, recambios 4x4, hospitales de referencia y vuelos internacionales si hay que resolver una incidencia grave.",
         credit="Jakub Hałun · CC BY 4.0", source=W + "Jamaa%20El%20Fna%2C%20Marrakesh%2C%20Morocco%2C%2020250124%201804%207017.jpg?width=900"),
    dict(n=8, name="Puerto de Tizi n'Test", cat="4x4 · paso de montaña", prio="Alta", dog="permitido", time="½ día",
         lat=30.8697, lon=-8.3563,
         desc="Puerto de 2 092 m sobre el Alto Atlas occidental, carretera estrecha con curvas cerradas y caídas pronunciadas: alternativa panorámica al Tizi n'Tichka para bajar de Marrakech hacia el Sous. Evitar con niebla o de noche.",
         credit="Alexander Leisser · CC BY-SA 4.0", source=W + "Tizi-n-Test%20Marokko.jpg?width=900"),
    dict(n=9, name="Essaouira", cat="Costa", prio="Media", dog="permitido", time="1 día",
         lat=31.5085, lon=-9.7595,
         desc="Puerto pesquero amurallado (ex Mogador), vientos alisios constantes, medina UNESCO. Playa amplia para el perro fuera de las zonas de baño señalizadas del centro.",
         credit="CastlesCatalog · CC BY-SA 4.0", source=W + "Skala%20du%20Port%20Essaouira%20Morocco.jpg?width=900"),
    dict(n=10, name="Tafraout y valle de Ameln", cat="Paisaje", prio="Media", dog="permitido", time="1 día",
         lat=29.7181, lon=-8.9770,
         desc="Pueblos bereberes de adobe rosado bajo formaciones graníticas (Napoleón's Hat); pistas secundarias hacia pinturas rupestres y almendros. Base tranquila para descansar antes del tramo sahariano.",
         credit="Holger Uwe Schmitt · CC BY-SA 4.0", source=W + "%22Ein%20sch%C3%B6ner%20Ort%20im%20Tal%20der%20Ammeln%22.%2008.jpg?width=900"),
    dict(n=11, name="Arco de Legzira", cat="Naturaleza", prio="Media", dog="permitido", time="½ día",
         lat=29.3452, lon=-10.1263,
         desc="Playa de acantilados rojizos con arco natural (uno de los dos colapsó en 2020); acceso solo con marea baja, sin socorrista. No aparcar al pie del acantilado por desprendimientos.",
         credit="Roy Egloff · CC BY-SA 4.0", source=W + "MA.GN.Sidi-Ifni%20Legzira-Beach%20Stone-Arch%20756%2016x9-R%205120x2880.jpg?width=900"),
    dict(n=12, name="Sidi Ifni", cat="Costa", prio="Media", dog="permitido", time="½–1 día",
         lat=29.3797, lon=-10.1728,
         desc="Antiguo enclave español (Ifni), arquitectura art-déco colonial, puerto pesquero activo y surf. Última ciudad grande con servicios completos antes del tramo semidesértico hacia Guelmim.",
         credit="Anass Sedrati · CC BY-SA 4.0", source=W + "Sidi%20Ifni%20Commune%20House.jpg?width=900"),
    dict(n=13, name="Parque Nacional de Khnifiss", cat="Naturaleza", prio="Alta", dog="requiere autorización escrita", time="½ día",
         lat=27.9700, lon=-12.3400,
         desc="Mayor laguna costera de Marruecos, humedal Ramsar con flamencos y aves migratorias entre Tan-Tan y Tarfaya. Acceso de vehículo y perro restringido en la zona núcleo: confirmar con la delegación de Aguas y Bosques antes de desviarse de la pista principal.",
         credit="ElWaliElAlaoui · CC BY-SA 4.0", source=W + "Flamingo%20in%20Khenifiss%20National%20Park%20Tarfaya%20Morocco.jpg?width=900"),
    dict(n=14, name="Tarfaya", cat="Historia · logística", prio="Media", dog="permitido", time="2–3 h",
         lat=27.9394, lon=-12.9231,
         desc="Ciudad ligada a Saint-Exupéry y la Aeropostale (fuerte Casa del Mar en el islote frente a la costa), gran parque eólico. Última parada de repostaje y descanso antes de entrar en el corredor del Sáhara Occidental.",
         credit="TEDxTarfaya · CC BY-SA 2.0", source=W + "Camels%20near%20Tarfaya%20Morocco.jpg?width=900"),
]

_CAT_COLOR = {
    "patrimonio": "marron", "patrimonio romano": "marron", "patrimonio unesco": "marron",
    "desierto": "naranja", "naturaleza": "verde", "naturaleza · 4x4": "verde",
    "costa": "turquesa", "cultura": "azul", "paisaje": "verde",
    "4x4 · paso de montaña": "naranja", "historia · logística": "gris",
}
import re as _re
for _p in POIS:
    _url = _p.pop("source")
    _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower()
    _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada — Puerto de Tánger Med (ferry Tarifa/Algeciras)", "Frontera", 35.9010, -5.5150,
     "Entrada con vehículo y perro en el mismo ferry; control de pasaporte, ficha de importación temporal (TVIP) y, si procede, TIR/CPD de la Delica en el mismo trámite. Reservar plaza de vehículo con antelación en temporada alta."),
    ("Continuidad hacia el sur — límite de administración marroquí / Sáhara Occidental", "Frontera", 27.6600, -13.2000,
     "No hay control fronterizo internacional entre Tarfaya y Laayoune (administración marroquí continua); sí puede haber controles de gendarmería con petición de documentación. El control real de salida del conjunto Marruecos–Sáhara está en Guerguerat (ver ficha Sáhara Occidental)."),
    ("Embajada de España en Rabat", "Consular", 33.9832, -6.8558,
     "Rue Aïn Khalouiya, Rte. des Zaërs, Km. 5, Souissi. +212 537 63 39 00. Coordenada urbana aproximada (Souissi)."),
    ("Consulado General de España en Tánger", "Consular", 35.7767, -5.8043,
     "85, Av. Président Habib Bourguiba. +212 539 93 70 00. Referencia útil justo tras el desembarco en Tánger Med."),
    ("Consulado General de España en Casablanca", "Consular", 33.5883, -7.6114,
     "31, Rue d'Alger. +212 522 22 07 52. Coordenada urbana aproximada."),
    ("Consulado General de España en Agadir", "Consular", 30.4202, -9.5982,
     "49, Rue Ibn Batouta, secteur mixte. +212 528 84 56 81/71. Última oficina consular española antes del tramo sur; sin representación en Laayoune ni Dakhla."),
    ("Hôpital Ibn Sina — Rabat (CHU)", "Hospital", 34.0068, -6.8306,
     "Centro Hospitalario Universitario de referencia nacional. Coordenada urbana aproximada."),
    ("Hôpital Militaire Avicenne — Marrakech", "Hospital", 31.6183, -8.0064,
     "Hospital de referencia en el sur para urgencias graves; base logística antes de entrar en el Atlas y el desierto. Coordenada urbana aproximada."),
    ("Hôpital Hassan II — Agadir", "Hospital", 30.4278, -9.5981,
     "Hospital regional de referencia del Sous; punto de apoyo médico antes del tramo semidesértico. Coordenada urbana aproximada."),
    ("Combustible · red densa Afriquia/Shell/Total en todo el eje N1", "Combustible", 30.4, -9.6,
     "Sin problema de autonomía en Marruecos: estaciones cada pocos kilómetros en el eje Tánger–Agadir–Tarfaya, todas con gasóleo de calidad estándar europea. Punto representativo (Agadir); repostar siempre por debajo de medio depósito antes de Guelmim."),
    ("Agua potable · supermercados y garrafas en todas las ciudades", "Agua potable", 31.6, -8.0,
     "Agua embotellada disponible en todas las poblaciones del itinerario; grifo potable en riads y campings de las ciudades principales, no recomendable en el resto sin tratar. Punto representativo (Marrakech)."),
]

DRONE_CALLOUT = ("danger", "El dron se confisca en la práctica",
                 "Marruecos no tiene un régimen turístico de importación de drones: la práctica reiterada en aduana de Tánger Med y aeropuertos es la confiscación a la entrada, con devolución solo a la salida del país previo pago de una tasa. No introducir el dron sin autorización previa y por escrito de la autoridad de aviación civil (DGAC); si no se obtiene, dejarlo fuera del viaje o declarado en depósito.")

STARLINK_CALLOUT = ("danger", "Starlink aún no está licenciado en Marruecos",
                     "A fecha de esta revisión, Marruecos figura como mercado en trámite de licencia («Coming soon»), sin fecha de activación confirmada por Starlink ni por la ANRT. No planificar el kit Roam como comunicación primaria en el país; llevar eSIM/SIM local (Maroc Telecom, Orange, inwi) y mensajería satelital independiente.")

DOG_MATRIX = [
    ("Medinas y zocos cubiertos (Fez, Marrakech)", "requiere autorización escrita", "Consultar con el riad/guía antes de entrar; llevar bozal y correa corta de repuesto."),
    ("Parque Nacional de Khnifiss (zona núcleo)", "requiere autorización escrita", "Confirmar con la delegación de Aguas y Bosques de Tan-Tan; quedarse en la pista principal si no hay respuesta."),
    ("Playas, medinas abiertas, montaña, desierto", "permitido", "Sin restricción específica publicada; llevar agua y proteger almohadillas en dunas."),
]

SOURCES = [
    ("Consulat du Maroc · Admisión temporal de vehículos (D16ter)", "https://www.consulat.ma/en/temporary-admission-cars-morocco"),
    ("Sahara Overland · Marruecos, TVIP y pistas del sur", "https://sahara-overland.com/tag/morocco-d16/"),
    ("MAEC España · Recomendaciones de viaje Marruecos", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Marruecos"),
    ("Embajada de España en Rabat · Consulados en Marruecos", "https://www.exteriores.gob.es/Embajadas/RABAT/es/Embajada/Paginas/Consulados.aspx"),
    ("Entrybrief · Requisitos de entrada de perros en Marruecos", "https://entrybrief.com/pets/morocco/"),
    ("PetTravel · Morocco Pet Import Requirements", "https://www.pettravel.com/information/pet-passports/morocco-pet-import-requirements/"),
    ("Drone-Laws.com · Normativa de drones en Marruecos", "https://drone-laws.com/drone-laws-in-morocco/"),
    ("Starlink · mapa de disponibilidad", "https://starlink.com/map"),
    ("Mind of a Hitchhiker · cruce Guerguerat/Dakhla–Nuadibú", "https://mindofahitchhiker.com/through-the-berm-mauritania-border-crossing-with-western-sahara-morocco/"),
    ("Wikivoyage · Guerguerat", "https://en.wikivoyage.org/wiki/Guerguerat"),
    ("UNESCO · Volubilis, Aït Benhaddou, medinas de Fez y Marrakech", "https://whc.unesco.org/en/statesparties/ma"),
    ("Comisión Europea · animales de compañía", "https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_es.htm"),
]

CORRIDOR = [
    (35.9010, -5.5150), (35.1688, -5.2636), (34.0631, -4.9787), (34.0742, -5.5547),
    (31.0801, -4.0134), (31.5810, -5.5809), (31.0472, -7.1319), (31.6258, -7.9891),
    (30.8697, -8.3563), (31.5085, -9.7595), (29.7181, -8.9770), (29.3452, -10.1263),
    (29.3797, -10.1728), (27.9700, -12.3400), (27.9394, -12.9231),
]

HISTORIA_RESUMEN = ("Marruecos es uno de los pocos países africanos que nunca perdió del todo su soberanía formal durante la era colonial: heredero de dinastías bereberes y árabes que gobernaron gran parte del Magreb y el sur de España, "
                     "pasó a ser protectorado franco-español en 1912, recuperó la independencia en 1956 bajo la monarquía alauí que sigue en el trono hoy, y mantiene desde 1975 el contencioso más antiguo y sensible de la región: la disputa del Sáhara Occidental.")

HISTORIA_SECCIONES = [
    ("Dinastías bereberes y el apogeo magrebí-andalusí",
     "El territorio ha sido cuna de sucesivas dinastías bereberes y árabes —almorávides, almohades, meriníes, saadíes— que en su momento de mayor expansión gobernaron desde el Sáhara hasta buena parte de la península ibérica, dejando un legado arquitectónico y cultural que hoy se ve en medinas como Fez o Marrakech."),
    ("La dinastía alauí y el protectorado franco-español",
     "La dinastía alauí, en el trono desde el siglo XVII, gobierna Marruecos hasta hoy. Debilitado el poder central a finales del XIX, el país fue repartido en dos zonas de protectorado en 1912: la francesa (la mayor parte del territorio) y la española (el norte, en torno al Rif, y el sur sahariano), con Tánger bajo estatuto internacional."),
    ("Independencia y las «Marchas Verdes» hacia el Sáhara",
     "Marruecos recuperó la independencia en 1956 bajo el rey Mohamed V. Su sucesor, Hasan II, reclamó la soberanía sobre el Sáhara Occidental español y organizó en 1975 la Marcha Verde, una movilización civil masiva que forzó la retirada española y desembocó en la anexión del territorio, aún no resuelta ante la ONU y que sigue condicionando la logística de cualquier ruta hacia el sur."),
    ("Situación actual: estabilidad relativa bajo Mohamed VI",
     "Bajo el rey Mohamed VI (desde 1999) Marruecos combina una monarquía con amplios poderes ejecutivos y un parlamento elegido, con reformas económicas notables (infraestructura, energía renovable, industria automotriz) y restricciones persistentes a la libertad de prensa y al debate sobre la monarquía o el Sáhara Occidental, temas sensibles que conviene evitar en conversación pública durante el viaje."),
]

HISTORIA_FUENTES = [
    ("BBC News · Morocco country profile", "https://www.bbc.com/news/world-africa-14121438"),
    ("Encyclopaedia Britannica · Morocco, History", "https://www.britannica.com/place/Morocco/History"),
    ("United Nations · MINURSO (Sáhara Occidental)", "https://minurso.unmissions.org/"),
]

SPEC = dict(
    slug="marruecos", name="Marruecos", revision="9 sep 2026",
    sub="Ruta overland · documentación · seguridad · logística",
    chips=[
        ("ENTRADA", "Tánger Med (ferry) → bucle norte"),
        ("SALIDA", "Tarfaya → Sáhara Occidental"),
        ("SEGURIDAD", "precaución normal · verificar Rif interior"),
        ("FRONTERA TERRESTRE", "N/A al entrar (ferry); continuidad terrestre al sur"),
        ("VISADO", "exención 90 días (España)"),
        ("REVALIDACIÓN", "30–60 días antes"),
    ],
    center=[31.5, -8.0], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Marruecos es la puerta de entrada al continente: ferry con vehículos desde Tarifa o Algeciras a Tánger Med, sin necesidad de CPD para el tramo marroquí (admisión temporal D16ter en el propio puerto). "
                   "La propuesta traza primero un bucle norte-centro por patrimonio, Atlas y desierto (Chefchaouen, Fez, Merzouga, Todra, Aït Benhaddou, Marrakech), y baja después por la costa atlántica "
                   "(Essaouira, Tafraout, Sidi Ifni, Tarfaya) hasta el límite con la administración marroquí del Sáhara Occidental."),
    facts=[
        ("Ventana prevista", "Enero de 2027, al inicio del viaje."),
        ("Entrada", "Ferry con vehículos Tarifa/Algeciras → Tánger Med; TVIP (tarjeta blanca) en el propio puerto."),
        ("Salida del bloque Marruecos", "Sin frontera internacional hasta Guerguerat; el corredor continúa por el Sáhara Occidental (ficha aparte)."),
        ("Visado", "Exención de 90 días para pasaporte español; pasaporte con más de 6 meses de vigencia."),
        ("Seguridad", "Precaución normal en general; vigilancia reforzada en el interior del Rif (Ketama) y evitar pistas no señalizadas cerca de la frontera argelina."),
        ("Comunicaciones", "Redes móviles buenas en el eje norte-Atlántico; Starlink aún sin licencia — no usar como primario."),
    ],
    alerts=[
        "Dron: la práctica en aduana es la confiscación a la entrada sin autorización previa de la DGAC — dejarlo fuera del viaje salvo trámite cerrado por escrito.",
        "Vehículo: debe salir de Marruecos el mismo vehículo (mismo número de bastidor) que entró con la TVIP; no perder la tarjeta blanca bajo ningún concepto.",
        "Zona del Rif interior (Ketama y alrededores): vendedores insistentes de hachís dirigidos a extranjeros — no parar ni aceptar acompañantes.",
        "Franja este del Sáhara Occidental (más allá del corredor costero): terreno minado desde el conflicto — nunca abandonar la carretera asfaltada ni la pista oficial.",
    ],
    ruta_intro="Bloques de norte a sur; el bucle histórico-desértico es opcional pero recomendado antes de bajar por la costa.",
    route_rows=[
        ("Norte histórico", "Tánger Med, Chefchaouen, Fez, Volubilis", "Aclimatación y trámites de entrada; medinas sin tráfico rodado"),
        ("Atlas y desierto", "Merzouga (Erg Chebbi), Todra, Aït Benhaddou, Marrakech", "Bloque más largo; reservar días de margen para arena y meteorología"),
        ("Costa atlántica", "Essaouira, Tafraout, Legzira, Sidi Ifni", "Ritmo tranquilo; última zona con oferta turística densa"),
        ("Extremo sur", "Guelmim, Khnifiss, Tarfaya", "Repostaje y provisiones completas antes de Laayoune; tráfico de camiones hacia Mauritania"),
    ],
    offroad=[
        "Puerto de Tizi n'Test (2 092 m): alternativa panorámica al Tichka entre Marrakech y el Sous, curvas cerradas — evitar de noche o con niebla.",
        "Pistas de acceso a Erg Chebbi desde Merzouga/Khamlia: arena suelta, recomendable reducir presión de neumáticos y llevar placas de desenganche.",
        "Bucle de gargantas Todra–Dades: pista remontable en 4x4 más allá del asfalto turístico, con vadeos de caudal variable según deshielo/lluvias.",
    ],
    acampada=[
        "Auberges con parking cerrado en Merzouga y Aït Benhaddou: opción más segura para pernoctar con vehículos y perro que la acampada libre en duna.",
        "Costa entre Essaouira y Sidi Ifni: numerosas explanadas de autocaravanas informales; confirmar tranquilidad y agua antes de quedarse toda la noche.",
    ],
    visado=[
        "Exención de visado de 90 días para pasaporte español en estancias turísticas; llevar el pasaporte con margen de vigencia superior a 6 meses.",
        "El registro de entrada del vehículo queda vinculado al pasaporte del conductor: coordinar quién figura como titular de la TVIP en cada vehículo (Grenadier de empresa / Delica de Albert).",
        "Revisar 30–60 días antes si cambia el régimen de exención o se exige formulario adicional de entrada (no detectado a fecha de esta revisión).",
    ],
    fronteras_rows=[
        ("Entrada", "Ferry Tarifa/Algeciras → Tánger Med", "Reservar con vehículos con antelación en temporada alta; TVIP se emite en el propio puerto."),
        ("Continuidad sur", "Tarfaya → Laayoune (Sáhara Occidental)", "No es frontera internacional; puede haber controles de gendarmería. El corredor completo termina en Guerguerat (ficha Sáhara Occidental)."),
    ],
    vehiculos=[
        "TVIP (tarjeta blanca de importación temporal): se emite en Tánger Med al entrar, válida orientativamente hasta 6 meses; conservarla y presentarla obligatoriamente a la salida del país.",
        "No se exige CPD para el tramo marroquí: la admisión temporal D16ter sustituye al carnet en este país.",
        "Seguro: contratar cobertura válida en Marruecos (carta verde ampliada o seguro de frontera) antes de desembarcar; revisar validez para el Sáhara Occidental.",
        "Llevar en ambos vehículos: permiso de circulación, ficha técnica, seguro, autorización de empresa del Grenadier y documentación de titularidad de la Delica — ver documentación general.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No hay procedimiento turístico simplificado: la DGAC exige autorización previa por escrito; sin ella, el dron se confisca en la práctica al entrar por Tánger Med.",
        "Si se obtiene autorización, no volar sobre ciudades, infraestructuras militares, fronteras ni el entorno del Sáhara Occidental sin permiso expreso adicional.",
        "Alternativa operativa: declarar el dron en depósito aduanero a la entrada y recogerlo a la salida, o directamente no introducirlo en el país.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Revisar el mapa oficial de Starlink 30–60 días antes de entrar: Marruecos está en fase de licencia, no de servicio activo, a fecha de esta revisión.",
        "Llevar SIM/eSIM de operador local (Maroc Telecom, Orange, inwi) como conectividad principal en todo el país.",
        "Mensajería satelital independiente (Garmin inReach o equivalente) como respaldo en el Atlas y el extremo sur, donde la cobertura móvil se degrada.",
    ],
    perro_intro=[
        "Microchip ISO 11784/11785 implantado ANTES de la vacuna antirrábica (el orden importa: un chip posterior a la vacuna invalida la pauta).",
        "Vacuna antirrábica vigente, puesta al menos 21 días antes de la entrada; el perro debe tener 12 semanas o más en el momento de vacunar.",
        "No se exige test de titulación de anticuerpos (FAVN) para perros procedentes de la UE.",
        "Certificado sanitario oficial (o pasaporte UE de mascota) válido, presentado en frontera junto con la cartilla de vacunación.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Sin vacunas obligatorias adicionales para viajeros procedentes de España; revisar pauta habitual de tétanos/hepatitis A con el centro de vacunación internacional.",
        "Botiquín con protección solar alta y suero oral: golpe de calor es el riesgo más frecuente en el bloque del desierto (Merzouga, Khnifiss, Tarfaya).",
        "Seguro de viaje con evacuación médica y cobertura de actividades 4x4/off-road sin exclusión.",
    ],
    seguridad_intro="El MAEC recomienda precaución general en Marruecos: riesgo bajo de atentado en zonas aisladas, vigilancia en el interior del Rif y respeto estricto a las normas de importación del vehículo.",
    seguridad=[
        "No fotografiar instalaciones militares ni de la Gendarmería Real; guardar el dron fuera del país salvo autorización.",
        "Evitar conducción nocturna fuera de autopistas; controles frecuentes de la Gendarmería Real en carretera — llevar siempre la documentación de ambos vehículos a mano.",
        "En el Rif interior (zona de Ketama) no detenerse ante ofertas de hachís ni aceptar acompañantes desconocidos en el vehículo.",
        "Compartir plan diario y punto de control con la base en España, especialmente en los tramos de Atlas y desierto.",
    ],
    agua=[
        "Agua embotellada disponible en cualquier población, incluidas las pequeñas del extremo sur (Tan-Tan, Tarfaya).",
        "Grifo potable fiable en riads, campings y hoteles de las ciudades principales; no confiar en el grifo en zonas rurales sin tratar o hervir.",
        "Llevar 20-30 l de reserva en los vehículos igualmente, como colchón antes de entrar en el Sáhara Occidental.",
    ],
    combustible=[
        "Sin riesgo de gaps de 500 km en Marruecos: red densa Afriquia/Shell/Total/Winxo en todo el eje Tánger–Agadir–Tarfaya, con gasóleo de calidad estándar homologada europea.",
        "Repostar siempre en Guelmim o Tan-Tan antes de Tarfaya: última zona con oferta amplia y competencia de precios antes del tramo del Sáhara Occidental.",
        "Evitar combustible de garrafa/informal fuera de estaciones oficiales: en Marruecos no hace falta, a diferencia de tramos más al sur.",
    ],
    pendientes=[
        ("Autorización de dron", "Resolver por escrito con la DGAC antes de viajar, o excluir el dron del equipaje"),
        ("Starlink", "Revisar el mapa oficial 30–60 días antes; mantener SIM local como plan primario"),
        ("Acceso del perro a Khnifiss y medinas cerradas", "Confirmar por escrito con la delegación de Aguas y Bosques y con riads/guías"),
        ("Ruta exacta del bucle Atlas-desierto", "Cerrar días asignados según meteorología de enero-febrero de 2027"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 9 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía 19 · Gendarmería Real 177 · Protección Civil / Ambulancia 15 · Emergencia única móvil 112. Emergencia consular española (Rabat): +212 537 63 39 00.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

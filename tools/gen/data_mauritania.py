# -*- coding: utf-8 -*-
"""Mauritania ficha data (from the 6-sep-2026 reference dossier)."""
from site_common import table, callout, bullets, st_pill, esc

HISTORIA_RESUMEN = ("Mauritania es un puente cultural y político entre el Magreb árabe-bereber y el África subsahariana, con un pasado de rutas caravaneras transaharianas y ciudades santas del islam, una historia reciente marcada por la esclavitud "
                     "(abolida legalmente solo en 1981, y todavía documentada en formas residuales pese a estar penada desde 2007) y una notable inestabilidad política con varios golpes de Estado desde la independencia en 1960.")

HISTORIA_SECCIONES = [
    ("Ciudades santas y rutas transaharianas",
     "Ciudades como Chinguetti, Ouadane, Tichit y Oualata —hoy Patrimonio de la Humanidad de la UNESCO y parada de este itinerario— fueron centros religiosos y comerciales de primer orden en la Edad Media, puntos de encuentro de las caravanas de sal, oro y esclavos que cruzaban el Sáhara, y hogar de bibliotecas manuscritas que aún conservan miles de textos coránicos y científicos."),
    ("Colonización francesa y la construcción de una frontera artificial",
     "Francia integró el territorio en el África Occidental Francesa a comienzos del siglo XX, trazando fronteras que unieron bajo una misma administración a poblaciones árabe-bereberes del norte (bidan) y comunidades negroafricanas del valle del río Senegal en el sur, una convivencia desigual que sigue generando tensión política interna."),
    ("Independencia, golpes de Estado y el conflicto del Sáhara Occidental",
     "Mauritania se independizó en 1960 y ha vivido desde entonces una notable inestabilidad, con más de media docena de golpes de Estado militares. El país participó brevemente en la ocupación del Sáhara Occidental junto a Marruecos (1975-1979), retirándose tras la presión del Frente Polisario, y ha mantenido desde entonces una posición de neutralidad cautelosa en ese contencioso vecino."),
    ("Situación actual: esclavitud residual y equilibrio étnico",
     "Mauritania fue el último país del mundo en abolir legalmente la esclavitud, en 1981, y en tipificarla como delito, en 2007; organizaciones internacionales documentan que persisten formas de servidumbre hereditaria pese a la prohibición, un asunto de atención activa de derechos humanos. El equilibrio entre la población árabe-bereber y las comunidades negroafricanas del sur sigue siendo un eje central, aunque de bajo perfil para el visitante, de la política del país."),
]

HISTORIA_FUENTES = [
    ("BBC News · Mauritania country profile", "https://www.bbc.com/news/world-africa-13429623"),
    ("UNESCO · Ksour de Ouadane, Chinguetti, Tichit y Oualata", "https://whc.unesco.org/en/list/750/"),
    ("Encyclopaedia Britannica · Mauritania, History", "https://www.britannica.com/place/Mauritania/History"),
]

POIS = [
    (1, "Ben Amera", "Overland", "Alta", 21.23003, -13.66437, "Monolito y vivac; tramo remoto junto al eje ferroviario. Acceso solo con track reciente, autonomía y criterio local.", "Les3corbiers · CC BY-SA 3.0", "https://commons.wikimedia.org/wiki/File:Ben_Amira_2006.jpg", "1 noche"),
    (2, "Aïcha", "Arte y desierto", "Alta", 21.29208, -13.69197, "Monolito y conjunto escultórico próximo a Ben Amera; visita combinada por pista, a unos 7 km.", "Embajada de Alemania en Nuakchot · crédito institucional", "https://nouakchott.diplo.de/mr-de/2245892-2245892", "½ día"),
    (3, "Chinguetti", "Patrimonio", "Alta", 20.46343, -12.36648, "Ksar histórico, mezquita y bibliotecas; base cultural del Adrar y punto de apoyo para el bucle oriental.", "Radosław Botev · CC BY 3.0 PL", "https://commons.wikimedia.org/wiki/File:Chinguetti_Mosque.jpg", "1–2 días"),
    (4, "Ouadane", "Patrimonio", "Alta", 20.93373, -11.61737, "Antiguo ksar y puerta de acceso al entorno de Richat; reservar margen para pista, guía y meteorología.", "www.Bildtankstelle.de · CC BY-SA 1.0", "https://commons.wikimedia.org/wiki/File:Oudane_old_tower.jpg", "1 día"),
    (5, "Oasis de Terjit", "Excursión", "Alta", 20.25242, -13.08770, "Palmeral y surgencia de agua; parada de descanso en el Adrar combinable con Tifoujar y Valle Blanco.", "Ammar Hassan · CC BY 2.0", "https://commons.wikimedia.org/wiki/File:Oasis_In_The_Desert_(15166702115).jpg", "½ día"),
    (6, "Atar", "Servicios", "Logística", 20.51819, -13.05439, "Base principal para combustible, agua, talleres, provisiones, comunicaciones y contratación de guía.", "Ji-Elle · CC BY-SA 3.0", "https://commons.wikimedia.org/wiki/File:Atar_square.jpg", "1–2 noches"),
    (7, "Guelb er Richat", "4x4 y geología", "Alta", 21.11085, -11.39283, "Ojo del Sáhara; bloque 4x4 remoto desde Ouadane que exige navegación, combustible y margen de retorno.", "USGS/EROS/NASA Landsat · dominio público", "https://commons.wikimedia.org/wiki/File:Richat_Structure_by_Landsat_7.jpg", "1–2 días"),
    (8, "Iwik y Banc d'Arguin", "Naturaleza", "Alta", 19.87841, -16.30442, "Parque costero y hábitat de aves migratorias; acceso sujeto a autorización, guía, pistas permitidas y reglas sobre el perro.", "NASA Earth Observatory · dominio público", "https://commons.wikimedia.org/wiki/File:Bancdarguin_oli_2019362.jpg", "1–2 días"),
    (9, "Puerto pesquero de Nuakchot", "Cultura", "Media", 18.11029, -16.02292, "Actividad portuaria y parada urbana; extremar discreción fotográfica y confirmar restricciones locales antes de usar dron.", "Hugues · CC BY-SA 2.0", "https://commons.wikimedia.org/wiki/File:Port_de_peche_Nouakchott.jpg", "2–3 h"),
    (10, "Parque de Diawling", "Naturaleza y frontera", "Alta", 16.39078, -16.35094, "Humedales del delta y enlace potencial con Diama; confirmar acceso, guía, estado de pista y admisión del perro.", "Parc National du Diawling · kit de prensa oficial", "https://www.pnd.mr/espace-presse/", "1 día"),
    (11, "Paso de Tifoujar", "4x4", "Alta", 20.09967, -13.19672, "Descenso escénico y arenoso hacia Oued El Abiod; validar firme, trazado y sentido recomendado con información reciente.", "Clemens Schmillen · CC BY-SA 4.0", "https://commons.wikimedia.org/wiki/File:TifoujarPass.jpg", "½ día"),
    (12, "Valle Blanco", "4x4", "Alta", 20.17762, -13.21507, "Oued El Abiod; corredor natural entre Tifoujar y Terjit, sujeto a arena, agua y estado de la pista.", "Radosław Botev · CC BY 3.0 PL; imagen representativa del Adrar", "https://commons.wikimedia.org/wiki/File:Sahara_desert_Adrar_Province_Mauritania.jpg", "½–1 día"),
]

DOG_BY_POI = {
    8: "requiere autorización escrita; confirmar reglas del parque",
    10: "pendiente de confirmación oficial",
}

LOGISTICS = [
    ("Frontera · Entrada norte — puesto mauritano de Guerguerat", "Frontera", 21.333667, -16.947167, "Corredor oficial hacia Nuadibú. No abandonar la pista marcada en la zona intermedia."),
    ("Frontera · Salida Diama — presa y puesto fronterizo", "Frontera", 16.215814, -16.414842, "Opción preferente por Diawling; verificar horarios, tasas y trámite de ambos vehículos."),
    ("Frontera · Salida Rosso — embarcadero del ferry", "Frontera", 16.508730, -15.811760, "Alternativa a Diama; prever colas, ferry y controles en ambas orillas."),
    ("Embajada de España en Nuakchot", "Consular", 18.095114, -15.974247, "+222 4525 2080 / 4525 2579 · emergencia +222 4683 3662 · emb.nouakchott@maec.es"),
    ("Consulado de España en Nuadibú", "Consular", 20.930000, -17.033000, "+222 4574 5371 · emergencia +222 4670 7502 · con.nouadhibou@maec.es. Coordenada urbana provisional."),
    ("Consulado honorario de España en Rosso", "Consular", 16.512800, -15.805000, "+222 4690 1067. Coordenada urbana provisional; confirmar por teléfono."),
    ("Consulado honorario de España en Chinguetti", "Consular", 20.463434, -12.366484, "+222 3445 6929 · sasbureau@yahoo.fr. Coordenada urbana provisional."),
    ("Centre Hospitalier National — Nuakchot", "Hospital", 18.088061, -15.987981, "Hospital público de referencia; capacidad limitada para casos complejos."),
    ("Centre Hospitalier des Spécialités — Nuadibú", "Hospital", 20.928785, -17.044440, "Centro hospitalario de referencia en el norte de la ruta."),
    ("Centre Hospitalier d'Atar", "Hospital", 20.522141, -13.052103, "Recurso sanitario urbano para el bloque del Adrar; no sustituye seguro de evacuación."),
    ("Hôpital de la Fraternité — Chinguetti", "Hospital", 20.463786, -12.368122, "Centro local relevante en el itinerario interior."),
    ("Clinique Chiva — Nuakchot", "Hospital", 18.100592, -15.984603, "Clínica privada citada por Exteriores; confirmar servicio antes de desplazarse."),
    ("Clinique Kissi — Nuakchot", "Hospital", 18.098591, -15.981838, "Clínica privada citada por Exteriores; confirmar servicio antes de desplazarse."),
    ("Clinique Ibn Sina — Nuakchot", "Hospital", 18.099631, -15.994403, "Clínica privada citada por Exteriores; confirmar servicio antes de desplazarse."),
    ("Combustible · Nuadibú", "Combustible", 20.930000, -17.033000, "Primera plaza con oferta amplia tras la frontera de Guerguerat; repostar aquí antes del eje ferroviario."),
    ("Combustible · Atar", "Combustible", 20.51819, -13.05439, "Base del Adrar; última oferta formal fiable antes de los bloques de Tifoujar, Chinguetti, Ouadane y Richat — salir con el depósito lleno."),
    ("Combustible · Nuakchot", "Combustible", 18.11029, -16.02292, "Mejor oferta y calidad del país; repostar aquí antes del tramo final hacia Diawling/Diama o Rosso."),
    ("Agua potable · Nuadibú, Atar, Nuakchot (garrafas/supermercados)", "Agua potable", 20.51819, -13.05439, "Agua embotellada en las tres ciudades principales; en el eje ferroviario y el bucle del Adrar (Ben Amera, Tifoujar, Richat) no hay fuente fiable — cargar reserva completa en Atar."),
]

SOURCES = [
    ("Portal oficial eVisa ANRPTS", "https://anrpts.gov.mr/en?"),
    ("MAEC España · Recomendaciones de viaje Mauritania", "https://www.exteriores.gob.es/Embajadas/nouakchott/es/ViajarA/Paginas/Recomendaciones-de-viaje.aspx"),
    ("Directorio de la Embajada de España en Nuakchot", "https://exteriores.gob.es/Embajadas/nouakchott/es/Embajada/Paginas/Directorio.aspx"),
    ("Aduanas de Mauritania · vehículos de turistas", "https://www.douanes.mr/view/BDm2Xn9/B19A7B10eJG"),
    ("Aduanas de Mauritania · permiso temporal", "https://www.douanes.mr/view/9YnAzN0/1Qqpevd0YD8/Dlq6ZxmkeWrO8ngy2"),
    ("ANAC · RTA-Drone 2022 (PDF)", "https://www.anac.mr/wp-content/uploads/2025/08/RTA-Drone-2022.pdf"),
    ("ANAC Mauritania", "https://www.anac.mr/language/fr/"),
    ("Starlink · mapa de disponibilidad", "https://starlink.com/map"),
    ("Starlink · itinerancia internacional", "https://starlink.com/support/article/0dd1c2c0-7bae-8c8f-43d4-9a64eb66662f"),
    ("UNESCO · ksour de Ouadane y Chinguetti", "https://whc.unesco.org/en/list/750/"),
    ("UNESCO · Banc d'Arguin", "https://whc.unesco.org/en/list/506/"),
    ("Parc National du Diawling", "https://www.pnd.mr/"),
    ("Comisión Europea · animales de compañía", "https://europa.eu/youreurope/citizens/travel/carry/pets-and-other-animals/index_es.htm"),
    ("MAPA España · perros, gatos y hurones", "https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones"),
    ("CDC Travelers' Health · Mauritania", "https://wwwnc.cdc.gov/travel/destinations/traveler/none/mauritania"),
    ("Google Sheet · Visats Africa", "https://docs.google.com/spreadsheets/d/1lFy2f8XUxwQuT9Qhdmx8vgpYBaM5o4AqxgKs8jIAplo/edit"),
    ("iOverlander · puntos de combustible y agua verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]


def get_data(root="../../"):
    pois = []
    for n, name, cat, prio, lat, lon, desc, credit, source, time in POIS:
        pois.append({
            "n": n, "name": name, "cat": cat, "prio": prio,
            "dog": DOG_BY_POI.get(n, "pendiente de confirmación oficial"),
            "icon": cat.lower(), "color": "ámbar", "time": time,
            "lat": lat, "lon": lon, "desc": desc, "dog_note": "",
            "credit": credit, "source": source,
            "img": f"assets/img/mauritania/{n:02d}.jpg",
        })
    logistics = [{"name": n, "cat": c, "lat": la, "lon": lo, "info": i} for n, c, la, lo, i in LOGISTICS]
    corridor = [
        (21.333667, -16.947167),  # Guerguerat
        (20.930000, -17.033000),  # Nuadibú
        (21.23003, -13.66437),    # Ben Amera
        (21.29208, -13.69197),    # Aïcha
        (20.51819, -13.05439),    # Atar
        (20.09967, -13.19672),    # Tifoujar
        (20.17762, -13.21507),    # Valle Blanco
        (20.25242, -13.08770),    # Terjit
        (20.46343, -12.36648),    # Chinguetti
        (20.93373, -11.61737),    # Ouadane
        (21.11085, -11.39283),    # Richat
    ]
    corridor2 = [
        (21.11085, -11.39283), (20.46343, -12.36648), (20.51819, -13.05439),
        (19.87841, -16.30442),  # Banc d'Arguin
        (18.11029, -16.02292),  # Nuakchot
        (16.39078, -16.35094),  # Diawling
        (16.215814, -16.414842),  # Diama
    ]

    d = {
        "slug": "mauritania", "name": "Mauritania", "revision": "6 sep 2026", "estado": "completa",
        "sub": "Ruta overland · documentación · seguridad · logística",
        "hero_img": "assets/img/mauritania/01.jpg",
        "hero_credit": "Ben Amera · Foto: Les3corbiers, CC BY-SA 3.0",
        "chips": [
            ("ENTRADA", "Guerguerat → Nuadibú"),
            ("SALIDA", "Diama (alt. Rosso)"),
            ("SEGURIDAD", st_pill("naranja · Adrar con validación diaria")),
            ("FRONTERA TERRESTRE", st_pill("abierta · corredor oficial")),
            ("VISADO", st_pill("eVisa previa obligatoria")),
            ("REVALIDACIÓN", "30–60 días antes"),
        ],
        "center": [19.6, -13.9], "zoom": 6,
        "pois": pois, "logistics": logistics,
        "corridor": corridor, "corridor_alt": corridor2,
        "notice": "Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    }
    d["historia_resumen"] = HISTORIA_RESUMEN
    d["historia_secciones"] = HISTORIA_SECCIONES
    d["historia_fuentes"] = HISTORIA_FUENTES
    historia = (
        f"<p>{esc(HISTORIA_RESUMEN)}</p>"
        + callout("", "Historia completa · con audio",
                  'Orígenes, colonización, independencia y situación actual, con fuentes y '
                  '<strong>audio tipo podcast</strong> narrado por el propio dispositivo para escuchar mientras se conduce: '
                  '<a href="historia/">leer y escuchar la historia de Mauritania →</a>', raw=True)
    )

    resumen = (
        "<p>Mauritania es el primer gran tramo desértico del corredor occidental. La propuesta enlaza la entrada desde el norte con Nuadibú, el eje ferroviario y el Adrar; vuelve a la costa y continúa hacia Senegal. Combina pistas 4x4, patrimonio, oasis y parques, pero el track definitivo solo debe cerrarse tras confirmar seguridad, permisos, autonomía, estado de pistas y acceso del perro.</p>"
        + table(("Campo", "Estado de trabajo"), [
            ("Ventana prevista", "Enero de 2027, sujeta al calendario continental definitivo."),
            ("Entrada", "Guerguerat → Nuadibú, por el corredor oficial y señalizado."),
            ("Salida", "Diama como opción principal; Rosso como alternativa operativa."),
            ("Visado", "eVisa previa para pasaporte español; pasaporte con más de seis meses de vigencia."),
            ("Seguridad", "Clasificación naranja en la hoja del proyecto; el Adrar exige validación diaria y apoyo local."),
            ("Comunicaciones", "Telefonía local + mensajería satelital. Starlink no debe considerarse servicio primario."),
            ("Decisión actual", "Mantener los doce lugares como candidatos; no convertir el mapa en GPX sin validación."),
        ])
    )

    ruta = (
        "<p>Bloques de norte a sur; el orden interno del Adrar se cierra sobre el terreno con guía e información reciente.</p>"
        + table(("Bloque", "Contenido", "Condición"), [
            ("Entrada norte", "Guerguerat y Nuadibú", "Sin abandonar el corredor legal ni improvisar en la zona intermedia"),
            ("Eje ferroviario", "Nuadibú, Choum, Ben Amera y Aïcha", "Bloque remoto: navegación, autonomía y guía local si cambian las condiciones"),
            ("Base del Adrar", "Atar", "Combustible, agua, provisiones, reparaciones, salud y contratación de guía"),
            ("Bucle occidental", "Paso de Tifoujar, Valle Blanco y oasis de Terjit", "Evaluar arena, lluvias y estado de pista"),
            ("Patrimonio y geología", "Chinguetti, Ouadane y Guelb er Richat", "Reservar varios días y margen meteorológico"),
            ("Costa", "Iwik y Banc d'Arguin; después Nuakchot", "Solo con autorización y condiciones compatibles con el perro"),
            ("Hacia Senegal", "Diawling y salida por Diama", "Conservar Rosso como alternativa según frontera, ferry y trámites"),
        ])
    )

    fronteras = (
        "<h3>Visado</h3>"
        + bullets([
            "eVisa previa obligatoria para pasaporte español: desde el 5 de enero de 2025 no debe contarse con visado a la llegada. Solicitarla en el portal oficial ANRPTS y llevar copias impresa y digital.",
            "Confirmar por escrito que el paso terrestre previsto admite el documento y revisar los requisitos 30–60 días antes de entrar.",
            "Preparar fichas de ruta con nombres, pasaportes, nacionalidades, matrículas, origen y destino para los controles.",
        ])
        + "<h3>Fronteras de la ruta</h3>"
        + table(("Función", "Paso", "Comprobación operativa"), [
            ("Entrada", "Guerguerat → Nuadibú", "Usar el corredor oficial; revisar horarios, seguro, guía y procedimiento inmediatamente antes del viaje."),
            ("Salida principal", "Diama por Diawling", "Confirmar estado del paso, tasas y documentación de los dos vehículos."),
            ("Alternativa", "Rosso", "Comparar ferry, colas, horarios y formalidades con Diama antes de cerrar el GPX."),
        ])
        + "<h3>Vehículos 4x4 en Mauritania</h3>"
        + bullets([
            "La aduana mauritana publica un procedimiento para vehículos de turistas: en paso terrestre, el vehículo debe estar a nombre del conductor o ir acompañado de contrato de compraventa o autorización del propietario.",
            "La información oficial describe un permiso inicial de siete días para completar formalidades y un permiso APC de hasta noventa días.",
            "Conservar y fotografiar el permiso temporal de cada vehículo y comprobar que la salida quede registrada.",
            "Confirmar por escrito el seguro de responsabilidad civil válido en Mauritania y si debe comprarse en frontera.",
            "La documentación oficial consultada no confirma el CPD como obligatorio para un turismo extranjero: verificar con aduana y RACE antes de salir.",
        ])
        + callout("", "Trámites comunes", 'La autorización de empresa del Grenadier, la documentación de la Delica y el CPD se explican en <a href="../../documentacion/">Documentación general</a>.', raw=True)
    )

    drones = (
        callout("danger", "Decisión práctica", "No introducir ni volar el dron sin autorización escrita de ANAC.")
        + "<p>La regulación oficial RTA-Drone 2022, modificada el 14 de febrero de 2025, sitúa la competencia en la Agence Nationale de l'Aviation Civile (ANAC). Un operador no residente necesita autorización especial; ninguna aeronave no tripulada puede operar sin autorización de ANAC.</p>"
        + table(("Tema", "Regla operativa"), [
            ("Entrada e importación", "La identificación exige autorización o certificado de importación. No hay procedimiento turístico simplificado: pedir confirmación escrita antes de transportar el dron."),
            ("Registro y piloto", "El dron debe figurar en el registro de ANAC. Más de 800 g exige licencia emitida o validada por ANAC; la excepción de ocio es inferior a 150 g."),
            ("Solicitud", "Documentación, proyecto, zona, fechas, ruta, formación, manuales y seguro; al menos 30 días naturales antes de la operación."),
            ("Límites", "VLOS, de día, hasta 120 m AGL. Sin autorización especial: no sobre ciudades, multitudes ni zonas militares o restringidas."),
            ("Aeródromos", "Separación mínima 1,5 / 3 / 10 km según longitud de pista."),
            ("Cámaras", "Operaciones recreativas con cámara pueden requerir autorización ministerial; prohibido captar fuera del espectro visible en categoría A/B."),
        ])
        + "<p>ANAC: +222 4524 4005 / +222 4525 3578 · survol.dta@anac.mr · anac@anac.mr. Comprobado el 6 de septiembre de 2026.</p>"
    )

    starlink = (
        callout("danger", "No planificar Starlink como comunicación primaria en Mauritania", "El mapa oficial marca Mauritania como «Coming soon / Starting in 2026», no como servicio disponible. No existe oferta local confirmada a la fecha de comprobación.")
        + bullets([
            "La itinerancia Roam solo está prevista en países donde Starlink está autorizado; usarla en un país no autorizado puede provocar restricciones inmediatas.",
            "Mauritania no figura en la lista consultada de territorios con uso en movimiento autorizado; no usar el terminal durante la conducción.",
            "Mantener eSIM/SIM local y mensajería satelital independiente. Revalidar el mapa oficial y las reglas de importación 30–60 días antes de entrar.",
        ])
    )

    perro = (
        callout("warn", "Requisito no confirmado", "No se ha localizado una instrucción pública mauritana suficientemente clara para la entrada terrestre de un perro. No convertir prácticas informales de viajeros en requisito oficial: solicitar confirmación escrita a la Embajada de Mauritania o a la autoridad veterinaria sobre permiso de importación, certificado sanitario, rabia, desparasitación y controles de frontera.")
        + bullets([
            "Confirmar por escrito si el perro puede entrar en Banc d'Arguin, Diawling, alojamientos y campamentos.",
            "Planificar sombra, agua, protección de almohadillas, bozal, correa y botiquín veterinario para calor, arena y etapas largas.",
        ])
        + callout("", "Requisitos comunes del perro", 'Microchip, pasaporte UE, rabia, titulación serológica y reentrada en la UE: ver <a href="../../documentacion/#perro">Documentación general · perro</a>.', raw=True)
        + "<h3>Salud humana en Mauritania</h3>"
        + bullets([
            "Fiebre amarilla: llevar el certificado internacional aunque la primera entrada sea desde el norte; la exigencia depende del país de procedencia.",
            "La recomendación sobre malaria cambia entre el Sáhara y el sur; valorar profilaxis con Sanidad Exterior según el itinerario.",
            "Seguro con hospitalización, rescate y evacuación médica sin exclusión por pistas 4x4 — la capacidad asistencial local puede ser insuficiente.",
        ])
    )

    seguridad = (
        "<p>La hoja del proyecto clasifica Mauritania en naranja. Las recomendaciones oficiales diferencian el eje costero de las zonas interiores y orientales, donde el riesgo es mayor. El recorrido entra en áreas remotas del Adrar y necesita validación final de seguridad, guía, meteorología, combustible y comunicaciones antes de cada bloque.</p>"
        + bullets([
            "Compartir plan diario y hora de control; revisar el aviso de Exteriores 72 horas antes de entrar y antes de cada salida al interior.",
            "Mantener autonomía de agua y combustible para retorno, rescate, viento y arena blanda.",
            "Llevar teléfono local y mensajería satelital independiente; registrar contactos consulares y médicos sin conexión.",
        ])
        + callout("", "Protocolo común de seguridad", 'Conducción, controles y escalado: ver <a href="../../documentacion/#seguridad">Documentación general · seguridad</a>.', raw=True)
    )

    gpx = (
        "<h3>Criterios para construir el GPX</h3>"
        + bullets([
            "Separar tramos asfaltados, pistas sencillas y secciones de arena o navegación.",
            "Definir autonomía mínima de combustible y agua por vehículo y un punto de retorno por etapa.",
            "Validar el track con fuentes recientes y guía local; no convertir líneas de mapa en instrucciones de conducción.",
        ])
        + "<h3>Decisiones pendientes</h3>"
        + table(("Tema", "Criterio de cierre"), [
            ("Bloques", "Asignar días al bloque ferroviario y al bucle del Adrar"),
            ("Salida", "Elegir Diama o Rosso con datos recientes de horarios, tasas y tramitación de dos vehículos"),
            ("Documentos", "Confirmar eVisa terrestre, seguro, permiso temporal y posible CPD por vehículo"),
            ("Perro", "Obtener por escrito los requisitos y las reglas de parques y alojamientos"),
            ("Guías", "Contratar guía cuando proceda para Ben Amera, pistas del Adrar, Richat y Banc d'Arguin"),
            ("Dron", "Obtener autorización de ANAC o dejar el dron fuera del país"),
            ("Starlink", "Tratarlo como no disponible hasta que el mapa oficial cambie a Available"),
        ])
        + callout("warn", "Punto de control final", "Actualizar visados, salud, seguridad, fronteras, drones y comunicaciones entre 30 y 60 días antes de la entrada prevista.")
    )

    agua_combustible = (
        callout("warn", "Bloque del Adrar y eje ferroviario sin combustible garantizado", "Fuera de Nuadibú, Atar y Nuakchot no hay red formal fiable: el combustible en pista suele venderse en bidón, a hasta el cuádruple del precio oficial. Salir de Atar con el depósito lleno antes de Tifoujar, Chinguetti, Ouadane y Richat.")
        + "<h3>Agua: recarga de depósitos (beber, ducha, aseo y limpieza)</h3>"
        + "<p>No solo agua de boca: como vehículos de expedición autónomos necesitamos recargar también el depósito de uso general (ducha, aseo, vajilla, limpieza), no solo el agua potable de beber.</p>"
        + bullets([
            "Nuadibú, Atar y Nuakchot: agua embotellada en supermercados y garrafas sin problema.",
            "Recarga de depósito de uso general: estaciones de servicio de Nuadibú, Atar y Nuakchot aceptan llenar bidones/depósito con manguera; en Atar es el último punto fiable antes del bucle del Adrar, llenar a tope allí.",
            "Eje ferroviario (Choum, Ben Amera, Aïcha) y bucle del Adrar (Tifoujar, Valle Blanco, Chinguetti, Ouadane, Richat): sin fuente fiable — cargar reserva completa (mínimo 30-40 l por vehículo, beber y uso general) en Atar antes de salir.",
        ])
        + "<h3>Combustible</h3>"
        + bullets([
            "Guerguerat → Nuadibú (~4 h de pista/carretera): repostar al llegar a Nuadibú, primera plaza con oferta amplia.",
            "Nuadibú → Atar (~460 km) vía el eje ferroviario: sin estaciones formales fiables en el trayecto; salir con el depósito lleno y margen de reserva.",
            "Atar es el punto de no retorno para combustible de calidad: desde aquí, Tifoujar, Chinguetti, Ouadane y Richat dependen de bidón informal a precio muy superior — planificar el consumo total del bucle antes de salir.",
            "Atar → Nuakchot (~450 km): tramo con más estaciones intermedias (Chami), aunque puede haber roturas de suministro puntuales.",
        ])
        + callout("", "Fuentes cruzadas", 'Puntos y comentarios recientes verificados también en <a href="https://ioverlander.com/" target="_blank" rel="noopener">iOverlander</a> y <a href="https://tracks4africa.co.za/" target="_blank" rel="noopener">Tracks4Africa</a>; revisar la fecha del último comentario antes de confiar en un punto.', raw=True)
        + callout("", "Criterio común del proyecto", 'Estrategia general de depósitos, potabilización y calidad de gasóleo: ver <a href="../../documentacion/#agua-combustible">Documentación general · agua y combustible</a>.', raw=True)
    )

    d["custom_sections"] = [
        ("resumen", "Resumen operativo", resumen),
        ("historia", "Historia y contexto", historia),
        ("ruta", "Ruta propuesta de norte a sur", ruta),
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
    d["sources_note"] = "Última revisión de esta versión: 6 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación."
    d["emergency"] = "Ambulancia 101 · Gendarmería 116 · Policía 117 · Bomberos 118 · Tráfico 119. Emergencia consular española: +222 4683 3662."
    d["matrix_note"] = "Nombres y coordenadas según la tabla maestra del dossier del 6 de septiembre de 2026; consulados honorarios con posición urbana provisional."
    return d

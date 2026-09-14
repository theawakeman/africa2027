#!/usr/bin/env python3
"""Aplica enriquecimientos visuales y enlaces verificados del grupo 4.

El archivo conserva una lista explícita por PDI para que la ampliación sea
reproducible y auditable. No busca ni asigna resultados automáticamente.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote, unquote


ROOT = Path(__file__).resolve().parents[1]


def commons(filename: str, credit: str, caption: str) -> dict[str, str]:
    encoded = quote(filename.replace(" ", "_"), safe="(),-._~")
    return {
        "img": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}?width=1200",
        "source": f"https://commons.wikimedia.org/wiki/File:{encoded}",
        "credit": credit,
        "caption": caption,
    }


def canonical_source(value: str) -> str:
    """Iguala las variantes Commons con espacios, guiones bajos y escapes."""
    decoded = unquote(value).replace("_", " ")
    return " ".join(decoded.split()).casefold()


def photo_marker(item: dict[str, str]) -> str:
    """Deduplica el mismo archivo sin fundir fotos distintas de una página."""
    source = canonical_source(item.get("source", ""))
    if "commons.wikimedia.org/wiki/file:" in source:
        return source
    return canonical_source(item.get("img", "")) or source


LINKS: dict[str, dict[int, tuple[str, str]]] = {
    "gabon": {
        1: ("Cocobeach · contexto de la ciudad fronteriza", "https://en.wikipedia.org/wiki/Cocobeach"),
        2: ("Monts de Cristal · permisos y acceso por Kinguélé/Tchimbélé", "https://www.petitfute.com/v56184-parc-national-des-monts-de-cristal/c1173-visites-points-d-interet/c937-monuments/c967-ouvrage-d-art/342509-barrages-de-kinguele-et-tchimbele.html"),
        3: ("ANPN · cartografía y sectores del Parque Nacional de Akanda", "https://www.biotope.fr/gabon/parc_akanda.html"),
        4: ("Libreville · barrios, historia y transportes", "https://en.wikipedia.org/wiki/Libreville"),
        5: ("Pointe Denis · acceso, travesía y alojamiento", "https://lapointedenis.com/"),
        9: ("UNESCO · perfil actual de Makokou", "https://www.uil.unesco.org/en/learning-cities/makokou"),
        10: ("UNESCO · Grutas de Lastoursville y coordenadas de Pahon 1", "https://whc.unesco.org/en/tentativelists/6587/"),
        11: ("Franceville · historia, transportes y puntos del entorno", "https://en.wikipedia.org/wiki/Franceville"),
        12: ("Léconi · servicios y visitas del entorno", "https://www.petitfute.com/v56232-leconi/"),
        13: ("Mesetas Batéké · paisaje y preparación de la visita", "https://www.evaneos.fr/gabon/voyage/etape/17123-plateaux-bateke-national-park/"),
        14: ("Fundación Albert Schweitzer · historia del hospital de Lambaréné", "https://www.albert-schweitzer.ch/stiftung-albert-schweitzer-werk/lambarene"),
        15: ("Sainte-Anne du Fernan-Vaz · historia y visita", "https://gabon4you.com/multi_category_templ/eglise-de-la-mission-sainte-anne-du-fernanvaz-omboue/"),
        16: ("Loango Tourism · actividades y logística de la visita", "https://www.loango-tourism.com/activities"),
        17: ("Port-Gentil · transportes, ciudad y playas", "https://en.wikipedia.org/wiki/Port-Gentil"),
        18: ("Moukalaba-Doudou · investigación y turismo de gorilas", "https://www.rts.ch/info/monde/14153099-au-gabon-la-recherche-sur-les-gorilles-est-financee-par-le-tourisme.html"),
        19: ("WCS Gabón · tortugas marinas y temporada de seguimiento", "https://gabon.wcs.org/en-us/Wildlife/Marine-Turtles.aspx"),
    },
    "camerun": {
        1: ("Mamfe · contexto del paso y la ciudad", "https://en.wikipedia.org/wiki/Mamfe"),
        2: ("Lago Barombi Mbo · origen volcánico y biodiversidad", "https://en.wikipedia.org/wiki/Lake_Barombi_Mbo"),
        3: ("Limbe Wildlife Centre · historia y especies", "https://fr.wikipedia.org/wiki/Limbe_Wildlife_Centre"),
        5: ("Duala · puerto, barrios e historia urbana", "https://en.wikipedia.org/wiki/Douala"),
        6: ("Kribi · costa, puerto y visitas del entorno", "https://en.wikipedia.org/wiki/Kribi"),
        8: ("Campo Ma'an · acceso, permisos e infraestructura", "https://en.wikivoyage.org/wiki/Campo_Ma%27an_National_Park"),
        9: ("Sangmélima · contexto urbano y servicios", "https://en.wikipedia.org/wiki/Sangm%C3%A9lima"),
        11: ("Comuna de Djoum · territorio y servicios", "https://www.osidimbea.cm/collectivites/sud/djoum-commune/"),
        12: ("Yaundé · barrios, museos y contexto", "https://en.wikipedia.org/wiki/Yaound%C3%A9"),
        13: ("Comuna de Moloundou · río Ngoko, distancias y servicios", "https://www.osidimbea.cm/collectivites/est/moloundou-commune/"),
        15: ("Yokadouma · eje forestal y contexto local", "https://en.wikipedia.org/wiki/Yokadouma"),
        16: ("Bertoua · servicios y transportes del este", "https://en.wikipedia.org/wiki/Bertoua"),
        18: ("ORTOC · visita al Palacio de los Reyes Bamún", "https://tourismeouestcameroun.com/chefferie_musee/palais-des-rois-bamoun/"),
        19: ("Chefferie de Bandjoun · recinto, museo e historia", "https://fr.wikipedia.org/wiki/Chefferie_de_Bandjoun"),
        20: ("ORTOC · visita y memoria de la cascada de la Métché", "https://tourismeouestcameroun.com/nature_paysage/chute-de-la-metche/"),
        21: ("ORTOC · acceso y visita a Ekom-Nkam", "https://tourismeouestcameroun.com/nature_paysage/ekom-nkam/"),
    },
    "angola": {
        1: ("Luanda · contexto urbano e historia", "https://en.wikipedia.org/wiki/Luanda"),
        2: ("Miradouro da Lua · descripción del enclave", "https://pt.wikipedia.org/wiki/Miradouro_da_Lua"),
        3: ("Pungo Andongo · monolitos e historia", "https://en.wikipedia.org/wiki/Black_Rocks_at_Pungo_Andongo"),
        4: ("Kalandula Falls · geografía y acceso", "https://en.wikipedia.org/wiki/Kalandula_Falls"),
        7: ("Historia del Reino do Bailundo y visita a Ombala Mbalundu", "https://welcometoangola.co.ao/en/reino-do-bailundo/"),
        9: ("Luena · historia, servicios y transportes", "https://pt.wikipedia.org/wiki/Luena_(Angola)"),
        10: ("African Parks · visitar Iona", "https://www.africanparks.org/the-parks/iona"),
        11: ("Foz do Cunene · ficha e imagen del enclave", "https://medicareclub.ao/index.php?province_content_id=14&route=club%2Fguide%2Fattraction"),
        12: ("Expedición 4x4 a Baía dos Tigres y Foz do Cunene", "https://kumakonda.com/ilha-da-baia-dos-tigres-angola/"),
        13: ("UNESCO · sitio arqueológico de Tchitundu-Hulu", "https://whc.unesco.org/en/tentativelists/6251/"),
        14: ("Lagoa do Arco · historia y estado estacional", "https://en.wikipedia.org/wiki/Lake_Arco"),
        15: ("Moçâmedes · contexto urbano y costa", "https://en.wikipedia.org/wiki/Mo%C3%A7%C3%A2medes"),
        16: ("Serra da Leba · carretera y puerto", "https://en.wikipedia.org/wiki/Serra_da_Leba"),
        17: ("Tundavala Gap · geología y mirador", "https://en.wikipedia.org/wiki/Tundavala_Gap"),
        18: ("Benguela · historia y patrimonio urbano", "https://en.wikipedia.org/wiki/Benguela"),
        19: ("Lobito · bahía, restinga y ferrocarril", "https://en.wikipedia.org/wiki/Lobito"),
        20: ("Cabo Ledo · playa, surf e historia", "https://pt.wikipedia.org/wiki/Cabo_Ledo"),
        21: ("UNESCO · Reserva de la Biosfera Quiçama", "https://www.unesco.org/en/mab/quicama"),
        22: ("Mussulo · península, bahía y accesos", "https://en.wikipedia.org/wiki/Mussulo"),
    },
}


VISITS: dict[str, dict[int, dict[str, str]]] = {
    "gabon": {
        1: {
            "why": "Es una escala pequeña pero singular para entender el estuario del Muni y la vida de una frontera fluvial antes de bajar a Libreville.",
            "see": "El mercado junto al agua, la orilla del estuario, el ayuntamiento y el memorial de la batalla de Cocobeach; no es un destino de playa equipado.",
            "access": "El pin coincide con la ficha de Cocobeach en Google Maps. La posibilidad de cruzar a Cogo debe confirmarse con inmigración y transportista; no se presupone barcaza ni admisión del vehículo.",
            "when": "Llegar con luz, dedicar unas horas y obtener información fronteriza antes de acercarse al embarcadero.",
            "skip": "Omitir el desvío si la frontera fluvial no está confirmada, llueve con fuerza o la etapa hacia Libreville ya va justa de tiempo.",
        },
        2: {
            "why": "Compensa por la extraordinaria diversidad botánica del bosque montano, muy distinta de los parques de sabana y costa del resto de Gabón.",
            "see": "Relieve boscoso, arroyos, begonias, orquídeas y el paisaje de los embalses de Kinguélé y Tchimbélé; la fauna grande es posible, no una promesa.",
            "access": "El pin es la ficha del parque en Google Maps, no una puerta. Para el sector Mbé hay que cerrar permiso del parque, autorización de SEEG si se entra en instalaciones y guía con punto de encuentro exacto.",
            "when": "Con 4x4, permisos escritos y pista confirmada; la estación relativamente más seca ofrece mejor margen, pero el terreno sigue siendo húmedo.",
            "skip": "No entrar sin guía y autorizaciones ni convertir el pin cartográfico en destino de navegación: el parque está dividido en dos bloques y carece de una entrada única.",
        },
        3: {
            "why": "Es la visita de manglar y marisma más accesible desde Libreville y un buen enclave para aves migratorias si se organiza con la marea adecuada.",
            "see": "Canales de manglar, llanuras de marea y aves costeras; tortugas y manatíes forman parte del ecosistema, pero no son avistamientos previsibles.",
            "access": "El pin identifica el área protegida en Google Maps, no un embarcadero. Contratar barca y guía y acordar por escrito salida, regreso, punto de embarque y sector visitado.",
            "when": "En una salida de media jornada ajustada a mareas, meteorología y permiso; llevar protección solar y contra lluvia.",
            "skip": "Descartarlo sin operador confirmado, con mala mar o si no se puede dejar al perro de forma segura fuera del parque.",
        },
        9: {
            "why": "No es una atracción principal, sino la base decisiva para saber si Ivindo y Kongou son realmente viables y abastecerse antes de la logística fluvial.",
            "see": "Una capital provincial pequeña a orillas del Ivindo, su vida cotidiana y el punto de partida de expediciones hacia el parque.",
            "access": "El pin coincide con la ficha de Makokou en Google Maps. Llegar con luz por la N4 y no salir al río sin guía, piragua, combustible y campamento confirmados.",
            "when": "Reservar al menos una tarde laborable para provisiones y reuniones; la expedición a Kongou requiere días, no una excursión improvisada.",
            "skip": "Si Ivindo no está reservado, usar Makokou solo como escala logística; no prometerse una visita a las cataratas desde la ciudad en el mismo día.",
        },
        10: {
            "why": "Pahon permite ver un karst tropical con arqueología documentada, un tipo de patrimonio que no se repite en el resto de la ruta.",
            "see": "Galerías, concreciones y huellas de ocupación humana dentro del conjunto de 43 cavidades inventariadas; la visita no es una cueva turística acondicionada.",
            "access": "El pin procede de la coordenada publicada por UNESCO para Pahon 1. Aun así, hace falta guía local, permiso del terreno y confirmación de la aproximación; no seguir el navegador a ciegas.",
            "when": "Con suelo razonablemente seco, iluminación propia, casco y margen suficiente para regresar con luz.",
            "skip": "No entrar con lluvia fuerte, crecida, sin guía o si no se dispone de equipo básico de cueva; observar la boca no justifica asumir riesgos.",
        },
        11: {
            "why": "Funciona como terminal del Transgabonés y base para Léconi y Batéké; en la propia ciudad el interés es más urbano e histórico que monumental.",
            "see": "La estación, el mercado de Poto-Poto, el río Passa y el monumento a Savorgnan de Brazza; Oklo y las instalaciones científicas no son visitas públicas por defecto.",
            "access": "El pin se ha ajustado a la ficha real de Franceville en Google Maps. La estación queda al oeste y debe tratarse como un desplazamiento separado.",
            "when": "Parar para combustible, comida, efectivo y coordinación del sureste; verificar por separado el horario ferroviario y cualquier excursión.",
            "skip": "No añadir noches solo por las referencias geológicas si no existe una visita autorizada; priorizar Léconi o Batéké con guía confirmado.",
        },
        13: {
            "why": "Ofrece el paisaje de sabana y bosque-galería más característico del sureste y un programa de conservación de gorilas con larga trayectoria.",
            "see": "Mesetas abiertas, valles arenosos, aves y primates; el león fotografiado en 2015 fue un hallazgo científico excepcional, no una expectativa de safari.",
            "access": "El pin coincide con la ficha del parque en Google Maps, no con una puerta. Hay que acordar con parque u operador el sector, el guía y el punto de encuentro antes de salir de Franceville.",
            "when": "Solo con permiso, guía y 4x4 confirmados; reservar una jornada completa como mínimo y comprobar pistas tras la lluvia.",
            "skip": "Descartarlo sin contacto operativo o si se espera un safari clásico de alta densidad: la escala y la infraestructura son muy limitadas.",
        },
        15: {
            "why": "La iglesia metálica de Sainte-Anne y su aislamiento en la laguna forman una visita histórica y paisajística que no se parece a ningún otro PDI del país.",
            "see": "La nave de hierro de 1889, el interior de madera y bambú, el embarcadero y el entorno de la misión en Fernan Vaz.",
            "access": "El pin coincide con la misión real, verificada también por la geolocalización de una fotografía. Se llega en barca desde Omboué y hay que pactar embarque y regreso.",
            "when": "Con travesía reservada, tiempo estable y luz suficiente para visitar sin apresurar el regreso por la laguna.",
            "skip": "No salir si el barquero o la meteorología no están confirmados; el Projet Gorille de Evengué es otra visita y requiere gestión propia.",
        },
        17: {
            "why": "Aporta la cara petrolera y marítima de Gabón y permite llegar al cabo Lopez, el extremo occidental del país, con su faro corroído y largas playas.",
            "see": "Centro urbano, actividad portuaria desde espacios permitidos y, en un desplazamiento aparte, la playa y el faro del cabo Lopez.",
            "access": "El pin coincide con la ficha de Port-Gentil. Hay carretera asfaltada hasta Omboué, pero no debe asumirse una conexión terrestre terminada con Libreville; entre ambas ciudades siguen siendo normales el avión y el barco.",
            "when": "Con transporte y alojamiento cerrados; ir al cabo de día, comprobar mareas y estado de la pista final y evitar fotografiar instalaciones sensibles.",
            "skip": "No desviarse si la llegada o salida marítima/aérea no está confirmada, ni usar este PDI para forzar una continuidad por carretera que aún no sea operativa.",
        },
        18: {
            "why": "Es una de las pocas opciones gabonesas de seguimiento de gorilas vinculada a décadas de investigación, en un mosaico de selva y sabana muy remoto.",
            "see": "Rastreo a pie, bosque, sabana y aves; incluso con habituación, encontrar al grupo exige esfuerzo y el contacto visual nunca está garantizado.",
            "access": "El pin es la ficha del parque en Google Maps, no Doussala ni una entrada. La experiencia debe contratarse antes con operador verificable, que fije traslado, guía, alojamiento y protocolo sanitario.",
            "when": "Con varios días, buena forma física y reserva confirmada; revisar lluvia, pistas y reglas de distancia y salud inmediatamente antes.",
            "skip": "No viajar por una oferta informal o sin condiciones escritas, y renunciar ante síntomas respiratorios, pista impracticable o falta de permiso.",
        },
    },
    "camerun": {
        1: {
            "why": "No justifica un desvío turístico: se conserva porque es la primera parada administrativa y logística después de Mfum.",
            "see": "El Cross River y el antiguo puente alemán son el interés local, pero la prioridad de esta etapa es resolver el paso y continuar.",
            "access": "Está en el eje de entrada desde Ekok/Mfum. Circular solo de día y comprobar el estado de la carretera y de la seguridad antes de salir de la frontera.",
            "when": "Parada breve, con luz y sin convocatoria de lockdown; combustible y efectivo deben resolverse donde aparezcan, no darse por seguros.",
            "skip": "No pernoctar ni desviarse hacia Bamenda si continúa la crisis anglófona o hay alertas locales, cortes o actividad armada.",
        },
        2: {
            "why": "Interesa por ser un lago de cráter aislado con peces cíclidos endémicos; solo compensa si Kumba y el acceso local son seguros.",
            "see": "La lámina del lago dentro de la caldera boscosa y la vida de la comunidad barombi; no es un complejo turístico organizado.",
            "access": "El pin se ha movido del punto genérico de Kumba al objeto real de Google Maps. Confirmar en Kumba la pista, el permiso local y el regreso con luz.",
            "when": "Únicamente con una ventana de seguridad confirmada el mismo día y margen suficiente para entrar y salir antes de anochecer.",
            "skip": "Descartarlo ante cualquier lockdown, control irregular o duda de seguridad: es documental, no una parada imprescindible de la ruta.",
        },
        8: {
            "why": "Aporta selva atlántica, primates y el proyecto de tortugas de Ebodjé, una experiencia diferente de los parques de sabana posteriores.",
            "see": "Bosque cerrado y biodiversidad; los gorilas, elefantes y otros grandes mamíferos no son un avistamiento garantizado.",
            "access": "El pin representa el área protegida, no una puerta. Hay que acordar por escrito con MINFOF el sector, el guía y el punto de encuentro antes de desviarse desde Kribi.",
            "when": "Con permisos cerrados y pistas confirmadas practicables; reservar al menos una jornada completa y no improvisar al llegar.",
            "skip": "Renunciar si no se obtiene respuesta del parque, si las pistas están anegadas o si el desvío compromete el corredor hacia Sangmélima.",
        },
        9: {
            "why": "Es una parada logística esencial, no una visita: la última ciudad con servicios amplios antes del corredor forestal hacia Congo.",
            "see": "Mercado y vida urbana del sur; el valor real es reponer combustible, agua, comida y efectivo y revisar los dos vehículos.",
            "access": "Está sobre el eje hacia Djoum. Llegar con luz, comprar antes del cierre y no depender de encontrar suministros después.",
            "when": "Antes de abandonar la ciudad hay que salir con depósitos llenos y confirmar tanto la carretera como la frontera de Ntam.",
            "skip": "No saltarse la recarga; lo descartable es la pernocta si se completa todo temprano y existe alojamiento seguro más adelante.",
        },
        11: {
            "why": "Marca la última comprobación logística y administrativa antes de Mintom y Ntam y da nombre al corredor internacional.",
            "see": "Una pequeña ciudad forestal y su ayuntamiento; no se vende como atracción, sino como escala necesaria para tomar decisiones.",
            "access": "Seguir el eje desde Sangmélima, registrar el paso si lo requiere la gendarmería y preguntar por carretera, combustible y frontera.",
            "when": "Con luz suficiente para resolver gestiones y decidir si se continúa o se duerme en un lugar previamente comprobado.",
            "skip": "No continuar hacia Ntam por inercia si no hay confirmación reciente del puesto, del estado de la pista o de autonomía suficiente.",
        },
        13: {
            "why": "Es la cabecera camerunesa del cruce fluvial de Socambo y el arranque del tramo forestal hacia Lobéké y Yokadouma.",
            "see": "El río Ngoko y la vida de una población de frontera; la experiencia principal es operativa, no una excursión preparada.",
            "access": "El pin marca Moloundou. El embarcadero y el puesto de Socambo son otro punto y solo se usan si barcaza, inmigración y aduana confirman el vehículo.",
            "when": "Llegar de día y con comunicación previa; dejar margen para demoras y no contar con una frecuencia fija de embarcaciones.",
            "skip": "No intentar el cruce ni la pista con información antigua, de noche o sin combustible y autonomía para regresar.",
        },
        15: {
            "why": "Es la única base logística razonable del gran tramo forestal entre Moloundou y Bertoua y el punto para gestionar Lobéké.",
            "see": "Una ciudad marcada por la actividad maderera; sirve para comprender el territorio y preparar la pista, no por monumentos concretos.",
            "access": "Se llega por la pista de concesiones desde Moloundou. Mantener distancia de los camiones y no conducir con polvo denso o sin luz.",
            "when": "Con tiempo para buscar combustible, revisar neumáticos y bajos y recabar información local sobre el siguiente tramo.",
            "skip": "No saltarse la revisión logística; sí descartar Lobéké si no hay permiso, guía o pista confirmada.",
        },
        16: {
            "why": "Primera ciudad grande después de la selva y mejor lugar para recuperar autonomía, reparar y descansar antes de Yaundé.",
            "see": "Centro regional y mercado; su valor para el viaje es disponer de talleres, hospital, bancos y alojamiento con aparcamiento.",
            "access": "Entrada por el eje de Yokadouma y salida asfaltada hacia Yaundé. Evitar llegar de noche y escoger aparcamiento cerrado.",
            "when": "Parar el tiempo necesario para revisar los dos vehículos después de la pista y reponer consumibles y efectivo.",
            "skip": "Solo convertirla en paso rápido si ambos coches están bien y toda la logística quedó resuelta; no asumir existencias sin comprobar.",
        },
        19: {
            "why": "Permite ver arquitectura palaciega y arte bamileké en un recinto vivo, complementando el relato bamún de Foumban.",
            "see": "Gran plaza ceremonial, casas de altos tejados cónicos y museo con objetos de autoridad y memoria de la chefferie.",
            "access": "El pin corresponde al recinto real de la Chefferie de Bandjoun, no al centro de Bafoussam. Preguntar en la entrada por guía y fotografía.",
            "when": "Con una o dos horas y respetando ceremonias, zonas privadas y las indicaciones del responsable del recinto.",
            "skip": "Descartarla si hay ceremonia privada, no se autoriza la visita o el horario obliga a conducir de noche hacia la siguiente etapa.",
        },
        20: {
            "why": "No es solo un salto de agua de 50 m: ORTOC lo identifica como lugar de culto bamileké y memoria de ejecuciones durante la guerra de independencia.",
            "see": "La caída junto a la N6, el barranco y las ofrendas del lugar sagrado; se visita con discreción y sin tocar ni fotografiar rituales sin permiso.",
            "access": "El pin ahora coincide con Chutes de la Métché en Google Maps, cerca de Bafoussam. No vuelve a señalar el centro de Dschang, a decenas de kilómetros.",
            "when": "Con luz y suelo suficientemente seguro para bajar; el acceso puede estar resbaladizo y hay que preguntar localmente antes de acercar al perro.",
            "skip": "No bajar con lluvia fuerte, terreno inseguro, ceremonia en curso o si no puede mantenerse al perro controlado y lejos del borde.",
        },
    },
}


COORDS: dict[str, dict[int, tuple[float, float]]] = {
    "gabon": {
        1: (0.9931336, 9.5770844),
        2: (0.7787808, 10.2151578),
        9: (0.5698292, 12.8617355),
        11: (-1.6227921, 13.6036914),
        14: (-0.6769393, 10.2291301),
        17: (-0.7149503, 8.7843278),
        18: (-2.4983347, 10.3497895),
    },
    "camerun": {
        2: (4.6619533, 9.4033907),
        17: (3.6253619, 11.5812826),
        18: (5.7325002, 10.9015616),
        20: (5.5324938, 10.3297126),
    },
}


NAMES: dict[str, dict[int, str]] = {
    "camerun": {
        20: "Cataratas de la Métché (desde Bafoussam)",
    },
}


DESCRIPTIONS: dict[str, dict[int, str]] = {
    "gabon": {
        2: (
            "Parque de unos 1.200 km² dividido en dos bloques, Mbé al sur y Mont Séni al norte, creado en 2002 "
            "para proteger un bosque montano de excepcional diversidad vegetal. El sector Mbé reúne relieve "
            "abrupto, arroyos y el entorno de Kinguélé y Tchimbélé. El pin coincide con la ficha del parque en "
            "Google Maps, pero no es una puerta: permiso del parque, guía y autorización de SEEG para las "
            "instalaciones hidroeléctricas deben cerrarse antes de salir de Libreville."
        ),
        13: (
            "Parque de 2.034 km² creado en 2002, con sabana de altiplano, bosques-galería y valles arenosos. "
            "Una cámara trampa documentó allí en 2015 un único león macho; el análisis genético lo relacionó "
            "con poblaciones históricas de Gabón y Congo y con leones actuales del sur de África. El parque "
            "también alberga un programa de reintroducción de gorila de llanura occidental. El pin coincide con "
            "la ficha de Google Maps, no con una entrada; visita, guía y acceso deben confirmarse desde Franceville."
        ),
        14: (
            "Ciudad dividida por el río Ogooué y escala natural de la N1. Albert Schweitzer fundó aquí en 1913 "
            "su hospital y trabajó en Lambaréné hasta su muerte en 1965. El antiguo hospital conserva el museo, "
            "el cementerio y edificios históricos, mientras el hospital moderno continúa la actividad sanitaria "
            "en el entorno. El pin ya no marca el centro genérico de Lambaréné: coincide con el Hospital Albert "
            "Schweitzer de Google Maps, junto al conjunto histórico. Confirmar el horario del museo por teléfono."
        ),
        15: (
            "La misión de Sainte-Anne se alza en la laguna Fernan Vaz, con Omboué como base de acceso. Su iglesia "
            "de 1889 tiene una singular estructura metálica prefabricada, atribuida por las fuentes históricas y "
            "turísticas a los talleres de Gustave Eiffel, e interior de madera y bambú. El pin coincide con la "
            "misión real y con una fotografía geolocalizada; la visita exige acordar la travesía en barca. El "
            "santuario de gorilas de Evengué es otro enclave y no queda incluido automáticamente."
        ),
        17: (
            "Segunda ciudad de Gabón y centro petrolero y maderero de la isla de Mandji. No existe una carretera "
            "directa y terminada entre Libreville y Port-Gentil: el enlace habitual entre ambas sigue siendo por "
            "avión o barco. Sí hay una carretera asfaltada de unos 93 km hacia Omboué; la continuidad Yombi–Mandji–"
            "Omboué se encontraba en obras desde septiembre de 2025, por lo que debe verificarse antes de plantear "
            "una ruta nacional. Al norte, el cabo Lopez es el extremo occidental de Gabón y conserva un faro "
            "metálico muy degradado. El pin marca Port-Gentil; el cabo es un desplazamiento separado."
        ),
        18: (
            "Gran parque del suroeste con mosaico de selva húmeda y sabana, gorilas de llanura occidental, "
            "chimpancés, elefantes y aves. La investigación y habituación de gorilas en el sector de Doussala se "
            "desarrolla desde hace décadas y ha dado lugar a visitas de seguimiento muy limitadas. Aun así, la "
            "experiencia solo debe planearse con un operador verificable y reserva previa: el avistamiento nunca "
            "está garantizado. El pin coincide con la ficha del parque en Google Maps, no con Doussala ni una puerta."
        ),
    },
    "camerun": {
        20: (
            "A la salida de Bafoussam, cerca del cruce de Bamougoum, la Métché cae unos 50 m. "
            "ORTOC la identifica a la vez como lugar de culto tradicional bamileké y como lugar de memoria: "
            "durante la guerra de independencia se utilizó para ejecutar a nacionalistas. El PDI ya no mezcla "
            "esta cascada con Dschang: el pin coincide con la ficha real de Chutes de la Métché en Google Maps. "
            "El descenso puede estar resbaladizo; preguntar antes de bajar, respetar las ofrendas y confirmar si "
            "el perro puede mantenerse con seguridad lejos del borde."
        ),
    },
}


FICHA_REPLACEMENTS: dict[str, list[tuple[str, str]]] = {
    "camerun": [
        (
            "Foumban → Bafoussam → Bandjoun → Dschang → Métché",
            "Foumban → Bafoussam → Bandjoun → Métché → Dschang",
        ),
        (
            "Cataratas de la Métché (Dschang): corta bajada por el circo de selva hasta el pie del salto, a 12 km de Dschang; sitio de memoria de la guerra de independencia.",
            "Cataratas de la Métché (Bafoussam): corta bajada junto a la N6 hasta el salto de 50 m; lugar de culto bamileké y memoria de las ejecuciones de nacionalistas durante la guerra de independencia.",
        ),
        (
            '<tr ><td>Fotos pendientes de sustituir</td><td>Varios PDIs usan imágenes de referencia de otra localidad del país: sustituir por fotos propias o por archivos verificados de Wikimedia Commons</td></tr>',
            "",
        ),
    ],
}


def replace_nested(value, replacements: list[tuple[str, str]]):
    if isinstance(value, str):
        for before, after in replacements:
            value = value.replace(before, after)
        return value
    if isinstance(value, list):
        return [replace_nested(item, replacements) for item in value]
    if isinstance(value, dict):
        return {key: replace_nested(item, replacements) for key, item in value.items()}
    return value


PHOTOS: dict[str, dict[int, list[dict[str, str]]]] = {
    "gabon": {
        1: [
            commons("Cocobeach, Gabon (46432500881).jpg", "David Stanley · CC BY 2.0", "Cocobeach y la orilla del estuario del Muni"),
            commons("Cocobeach Market (46384653862).jpg", "David Stanley · CC BY 2.0", "Mercado de Cocobeach junto al agua"),
            commons("Monuments aux Morts Bataille de Cocobeach septembre 1914.jpg", "EVIVI · CC BY-SA 3.0", "Memorial de la batalla de Cocobeach de 1914"),
        ],
        2: [
            commons("Parc national des Monts de Cristal bannière.jpg", "Nitoni Noio · CC BY-SA 4.0", "Bosque montano del Parque Nacional de los Monts de Cristal"),
            commons("Vue de Monts de Cristal.jpg", "Nitoni Noio · CC BY-SA 4.0", "Relieve cubierto de selva en los Monts de Cristal"),
            commons("Kikandikila et mont-cristal.jpg", "Nitoni Noio · CC BY-SA 4.0", "Vista de los Monts de Cristal desde Kikandikila"),
        ],
        3: [
            {
                "img": "https://www.afd.fr/sites/default/files/styles/header_content/public/2022-06-03-04-48/mangrove.jpg.webp?itok=ViQ77v7A",
                "source": "https://www.afd.fr/en/actualites/un-ocean-conference-promise-blue-carbon",
                "credit": "Agence Française de Développement",
                "caption": "Navegación en los manglares del Parque Nacional de Akanda",
            },
            {
                "img": "https://4.bp.blogspot.com/-sYGLLtsumb8/WZnqXFrQ2NI/AAAAAAAATrc/eVMNVcxV-fED-qR3i2hXq4eejPKdPOlMQCLcBGAs/s1600/IMG_5631.JPG",
                "source": "https://notreaventureaugabon.blogspot.com/2017/08/la-mangrove-du-parc-national-de-lakanda.html",
                "credit": "Tristan · Notre aventure au Gabon",
                "caption": "Raíces de manglar fotografiadas durante una salida por el río Ntsini en Akanda",
            },
            {
                "img": "https://www.libreville-accueil-bal.org/medias/images/p1224445.jpg",
                "source": "https://www.libreville-accueil-bal.org/pages/archives/nos-activites/natures/061218-pirogue-akanda.html",
                "credit": "Libreville Accueil",
                "caption": "Desembarco de una excursión en piragua dentro de los manglares de Akanda",
            },
        ],
        9: [
            {
                "img": "https://www.uil.unesco.org/sites/default/files/structured_data/lc0001/2477320_Makokou%25252C%252520Gabon.jpg",
                "source": "https://www.uil.unesco.org/en/learning-cities/makokou",
                "credit": "UNESCO Institute for Lifelong Learning",
                "caption": "Espacio urbano de Makokou en el perfil de la Red Mundial de Ciudades del Aprendizaje",
            },
            {
                "img": "https://www.bdpmodwoam.org/wp-content/uploads/makokou-0580b1b9.jpg",
                "source": "https://www.bdpmodwoam.org/articles/2014/03/01/le-lycee-alexandre-sambat-de-makokou-a-lepreuve-des-examens-blancs/",
                "credit": "BDP Modwoam",
                "caption": "Vista del entorno urbano y fluvial de Makokou",
            },
            {
                "img": "https://static.wixstatic.com/media/ec9c0d_e2a43c4cb5c7428dba41ee8f1ce85888~mv2.webp/v1/fill/w_980,h_735,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/ec9c0d_e2a43c4cb5c7428dba41ee8f1ce85888~mv2.webp",
                "source": "https://www.gabon-voyage-afrique.online/trekking-parc-ivindo",
                "credit": "Le Tourisme en Afrique",
                "caption": "Salida de una expedición desde Makokou hacia el Parque Nacional de Ivindo",
            },
        ],
        10: [
            {
                "img": "https://carnetsdevoyages.jeanlou.fr/Les_Grottes_du_GABON/Lastoursville_3_la_Grotte_de_PAHON_01/Photos_Lastourville_3_la_Grotte_de_PAHON_01/files/page95-1066-full.jpg",
                "source": "https://carnetsdevoyages.jeanlou.fr/Les_Grottes_du_GABON/Lastoursville_3_la_Grotte_de_PAHON_01/Photos_Lastourville_3_la_Grotte_de_PAHON_01/files/page95-1066-full.html",
                "credit": "Jean Louis Albert",
                "caption": "Concreciones del techo de la cueva Pahon en Lastoursville",
            },
            {
                "img": "https://www.echosciences-grenoble.fr/uploads/article/image/attachment/1005164068/xl_lastoursville.jpg",
                "source": "https://www.echosciences-grenoble.fr/articles/suivez-en-direct-l-expedition-dans-les-grottes-de-lastoursville-au-gabon",
                "credit": "Échosciences Grenoble",
                "caption": "Expedición científica dentro del sistema de cuevas de Lastoursville",
            },
            {
                "img": "https://paloc.fr/sites/paloc/files/styles/umr_social_sharing/public/2025-04/Grotte-de-Pahon-Gabon.png?itok=2ehyVpVY",
                "source": "https://paloc.fr/fr/actualites/les-archives-de-pahon-10-000-ans-sous-le-guano-7129",
                "credit": "UMR PALOC",
                "caption": "Trabajo arqueológico en la cueva de Pahon, bajo los depósitos de guano",
            },
        ],
        11: [
            commons("Franceville Railway Station.jpg", "David Stanley · CC BY 2.0", "Estación del Transgabonés en Franceville"),
            commons("Poto-Poto Market Area (32503052828).jpg", "David Stanley · CC BY 2.0", "Mercado de Poto-Poto junto al río Passa en Franceville"),
            commons("Savorgnan de Brazza (46387342051).jpg", "David Stanley · CC BY 2.0", "Monumento a Savorgnan de Brazza en Franceville"),
        ],
        13: [
            {
                "img": "https://static1.evcdn.net/images/reduction/279557_w-1600_h-1200_q-70_m-crop.jpg",
                "source": "https://www.evaneos.fr/gabon/voyage/etape/17123-plateaux-bateke-national-park/",
                "credit": "Evaneos",
                "caption": "Sabana ondulada y bosque del Parque Nacional de las Mesetas Batéké",
            },
            commons("Miopithecus ogouensis (Batéké Plateau National Park).jpg", "Tony King · CC BY 4.0", "Talapoín fotografiado dentro del Parque Nacional de las Mesetas Batéké"),
            commons("Malimbus racheliae - Tony King - 468667118.jpeg", "Tony King · CC BY 4.0", "Malimbus de Rachel fotografiado junto al río Mpassa dentro del parque"),
        ],
        15: [
            commons("Sainte Anne du Fernan-Vaz.jpg", "Jean Louis Albert · CC BY-SA 4.0", "Misión de Sainte-Anne y su embarcadero vistos desde la laguna"),
            commons("Cap Lopez-La Mission Ste-Anne au Fernan Vaz.jpg", "Gabriel Gorce · dominio público", "Vista histórica de la misión Sainte-Anne du Fernan-Vaz"),
            commons("Cathédrale des bambous.jpg", "Jean Louis Albert · CC BY-SA 4.0", "Interior de madera y bambú de la iglesia de Sainte-Anne"),
        ],
        17: [
            commons("POG-From The Air.jpg", "Brian Ecton · dominio público", "Port-Gentil visto desde el aire"),
            commons("Port-Gentil - Nation coat of arms of Gabon - 2009.jpg", "AchilleT · dominio público", "Monumento urbano en el centro de Port-Gentil"),
            {
                "img": "https://cdn.shopify.com/s/files/1/0631/2896/1206/files/PORT-DE-CAP-LOPEZ-2.jpg",
                "source": "https://beauvoyage.com/blogs/magazine/gabon-5-raisons-de-partir-a-laventure-en-famille-par-la-fondatrice-de-micasaestucasa",
                "credit": "Beau Voyage / MiCasaEsTuCasa",
                "caption": "Faro metálico y playa del cabo Lopez, al norte de Port-Gentil",
            },
        ],
        18: [
            {
                "img": "https://img.rts.ch/articles/2023/image/u36r77-26153018.image?h=720&w=1280",
                "source": "https://www.rts.ch/info/monde/14153099-au-gabon-la-recherche-sur-les-gorilles-est-financee-par-le-tourisme.html",
                "credit": "RTS",
                "caption": "Seguimiento de gorilas en el bosque de Moukalaba-Doudou",
            },
            commons("Corythaeola christata Parc national Moukalaba-Doudou.jpg", "Wisi eu · CC0", "Turaco gigante fotografiado dentro de Moukalaba-Doudou"),
            commons("Agelastes niger - markusgmeiner - 593966031.jpeg", "markusgmeiner · CC BY 4.0", "Pintada negra fotografiada dentro del Parque Nacional de Moukalaba-Doudou"),
        ],
    },
    "camerun": {
        1: [
            commons("German Bridge (Cross River, Mamfe).jpg", "visulogik · CC BY 2.0", "Antiguo puente alemán sobre el Cross River en Mamfe"),
            commons("Afternoon sun in Mamfe, Cameroon.jpg", "Hans Kylberg · CC BY 2.0", "Vista urbana de Mamfe al final de la tarde"),
        ],
        2: [
            commons("Lac Barombi Mbo - Barombi Mbo Crater Lake - Region du Sud-ouest - Cameroun.jpg", "Eric Joel Mama Nke · CC BY-SA 4.0", "Orilla del lago de cráter Barombi Mbo"),
            commons("Lac Barombi Mbo en vue aérienne - Barombi crater lake - Sud-Ouest - Cameroun.jpg", "Eric Joel Mama Nke · CC BY-SA 4.0", "Vista aérea del lago Barombi Mbo"),
            commons("Lac Barombi Mbo en vue aérienne saison pluvieuse - Barombi crater lake - Sud-Ouest - Cameroun.jpg", "Eric Joel Mama Nke · CC BY-SA 4.0", "Barombi Mbo durante la estación lluviosa"),
        ],
        8: [
            commons("Peters Duiker (Cephalophus callipygus) from behind, Campo Maan National Park.jpg", "XKD · CC BY-SA 2.0", "Duíquero de Peters fotografiado dentro de Campo Ma'an"),
            commons("Habituation des Gorilles.jpg", "Campo Ma'an National Park · CC BY-SA 4.0", "Trabajo de habituación de gorilas en Campo Ma'an"),
            commons("Musée de l'arbre.jpg", "Campo Ma'an National Park · CC BY-SA 4.0", "Musée de l'arbre dentro de Campo Ma'an"),
        ],
        9: [
            commons("Sangmelima Cameroon.jpg", "Suzana K · CC0", "Calle de Sangmélima rodeada de vegetación"),
            commons("Champ de pastèques Sangmélima.jpg", "Nadnad30 · CC BY-SA 4.0", "Campo de sandías en el entorno de Sangmélima"),
        ],
        11: [
            {
                "img": "https://image.jimcdn.com/app/cms/image/transf/dimension%3Dorigxorig%3Aformat%3Djpg/path/s1084e755aa436055/image/i327fff11efaabe44/version/1604707031/image.jpg",
                "source": "https://www.osidimbea.cm/collectivites/sud/djoum-commune/",
                "credit": "Osidimbea",
                "caption": "Hôtel de Ville de Djoum, identificado por la fuente municipal de Osidimbea",
            },
            {
                "img": "https://journalmatila.info/wp-content/uploads/2025/10/de08b31e-47f5-423c-94da-993f70fce6f1-1024x768.jpeg",
                "source": "https://journalmatila.info/decentralisation-en-marche-le-minddevel-georges-elanga-obam-ratisse-large-dans-le-sud/",
                "credit": "Journal Matila",
                "caption": "Edificio de la cité municipale de Djoum durante la visita ministerial de septiembre de 2025",
            },
        ],
        13: [
            {
                "img": "https://image.jimcdn.com/app/cms/image/transf/none/path/s1084e755aa436055/image/ie21b20db8e5d57f8/version/1591490262/image.jpg",
                "source": "https://www.osidimbea.cm/collectivites/est/moloundou-commune/",
                "credit": "Osidimbea",
                "caption": "Paisaje fluvial de la región de Moloundou",
            },
            commons("Piste, Est, Cameroun.jpg", "Théo Vansteenkeste · CC BY-SA 4.0", "Pista forestal entre Yokadouma y Moloundou"),
        ],
        15: [
            commons("Route de Yokadouma.jpg", "Photokadaffi · CC BY-SA 4.0", "Carretera sin asfaltar en Yokadouma"),
            commons("Grumier dans la ville de Yokadouma.jpg", "Photokadaffi · CC BY-SA 4.0", "Camión maderero dentro de Yokadouma"),
            commons("Caravane de boeufs à Yokadouma.jpg", "Photokadaffi · CC BY-SA 4.0", "Caravana de ganado en una calle de Yokadouma"),
        ],
        16: [
            commons("Hotel de ville de Bertoua.jpg", "Serieminou · CC BY-SA 4.0", "Ayuntamiento de Bertoua"),
            commons("Plaque Bertoua.jpg", "Serieminou · CC BY-SA 4.0", "Señal urbana de Bertoua"),
            commons("Car de transport à Bertoua.jpg", "Photokadaffi · CC BY-SA 4.0", "Autobús interurbano en Bertoua"),
        ],
        19: [
            commons("A hut at Bandjoun palace.jpg", "Josephine Lifanje · CC BY-SA 4.0", "Casa tradicional dentro del palacio de Bandjoun"),
            commons("ChefferieBandjoun fevrier1982.jpg", "Christian Muir · CC BY-SA 2.5", "Chefferie de Bandjoun en 1982"),
            commons("Chefferie de Bandjoun en mars 1973.jpg", "Jean-Louis Heckly · CC BY-SA 4.0", "Recinto de la chefferie de Bandjoun en 1973"),
        ],
        20: [
            commons("Chutes de la Métchié-2.jpg", "KLO.J · CC BY 2.0", "Cascada de la Métché"),
            commons("Chutes de la Métché - 1.jpg", "Kondah · CC BY-SA 4.0", "Caída principal de la Métché"),
            commons("Les chutes de la metché.jpg", "Dilane Tayo · CC BY-SA 4.0", "Vista del lugar sagrado de la Métché"),
        ],
    },
    "angola": {
        6: [
            commons("Igreja Matriz de Waku Kungo - panoramio.jpg", "Rogério Melo · CC BY 3.0", "Iglesia principal de Waku Kungo"),
            commons("Waku Kungo, Angola - panoramio.jpg", "Rogério Melo · CC BY 3.0", "Paisaje urbano de Waku Kungo"),
            commons("Waku Kungo - panoramio - Rogério Melo (3).jpg", "Rogério Melo · CC BY 3.0", "Otra vista de Waku Kungo"),
        ],
        7: [
            {
                "img": "https://welcometoangola.co.ao/wp-content/uploads/2022/10/reino-bailundo-capa-1.jpg",
                "source": "https://welcometoangola.co.ao/en/reino-do-bailundo/",
                "credit": "Welcome to Angola",
                "caption": "Autoridades tradicionales bajo el rótulo de Ombala yo Mbalundo",
            },
        ],
        9: [
            commons("Jardim do Palacio do Governador Luena Moxico.jpg", "Pereira Santos Samuel · CC BY-SA 3.0", "Jardín del palacio provincial en Luena"),
            commons("Instituto Médio de Administração e Gestão.jpeg", "Diego Passos Costa · CC BY-SA 3.0", "Instituto de enseñanza de Luena"),
            commons("Por do Sol Imag Luena 08 novembro 2011 1600x1200 388KB.jpg", "Diego Passos Costa · CC BY-SA 3.0", "Atardecer urbano en Luena"),
        ],
        11: [
            {
                "img": "https://medicareclub.ao/image/cache/catalog/guia/namibe/foz/foz%20rio%20cunene%20pedro%20carreno-1240x827.jpg",
                "source": "https://medicareclub.ao/index.php?province_content_id=14&route=club%2Fguide%2Fattraction",
                "credit": "Pedro Carreño · Medicare Club Angola",
                "caption": "Desembocadura del río Cunene entre carrizos y dunas",
            },
        ],
        12: [
            commons("Ilha dos Tigres 1466538 960 720.jpg", "juls26 · CC0", "Antiguos depósitos de aceite de pescado junto a la bahía"),
            commons("Ilha dos Tigres 1466534 960 720.jpg", "juls26 · CC0", "Barracones abandonados del poblado pesquero"),
        ],
        15: [
            commons("Namibe Waterfront (19432713306).jpg", "David Stanley · CC BY 2.0", "Avenida costera y bahía de Moçâmedes"),
            commons("Governo Provincial do Namibe (19543179475) (cropped).jpg", "David Stanley · CC BY 2.0", "Edificio del gobierno provincial en Moçâmedes"),
        ],
        18: [
            commons("Igreja Benguela, Angola.jpg", "F. H. Mira · CC BY-SA 2.0", "Iglesia histórica de Benguela"),
            commons("Paços do Concelho, Benguela.jpg", "F. H. Mira · CC BY-SA 2.0", "Ayuntamiento de Benguela"),
        ],
        19: [
            commons("Igreja da Arrábida in Lobito - Angola 2015.jpg", "David Stanley · CC BY 2.0", "Iglesia da Arrábida en la Restinga de Lobito"),
            commons("Restinga Peninsula (18996958243) (cropped).jpg", "David Stanley · CC BY 2.0", "Restinga arenosa que protege la bahía de Lobito"),
        ],
        20: [
            commons("Cabo Ledo beach, Angola 02.jpg", "Felipe Miguel · CC BY-SA 2.0", "Playa y acantilados de Cabo Ledo"),
            commons("Cabo Ledo beach, Angola 03.jpg", "Felipe Miguel · CC BY-SA 2.0", "Otra vista de la ensenada de Cabo Ledo"),
        ],
        21: [
            commons("Kissama 001.JPG", "Àngel Sàez i Pedrero · CC BY-SA 4.0", "Paisaje de sabana en el Parque Nacional de Kissama"),
            commons("Río Cuanza en Kissama.JPG", "Àngel Sàez i Pedrero · CC BY-SA 4.0", "Río Cuanza en el Parque Nacional de Kissama"),
        ],
        22: [
            commons("Mussulo Island.jpg", "Juvenalia Brito · CC BY-SA 3.0", "Playa y casas de la península de Mussulo"),
            commons("Mussulo, Angola.jpg", "Juvenalia Brito · CC BY-SA 3.0", "Mussulo visto durante la travesía en barco"),
        ],
    },
}


REMOVE_LINKS: dict[str, set[str]] = {
    "gabon": {
        "https://www.amazinggabon.com/en/plateaux-bateke-national-park/",
        "https://gouvernement.ga/2026/06/08/tourisme-durable-marcelle-ibinga-itsitsa-en-mission-a-doussala-pour-valoriser-le-potentiel-du-parc-national-de-moukalaba-doudou/",
        "https://triptogabon.com/parc-national-des-plateaux-betekes/",
    },
    "camerun": {
        "https://limbewildlife.org/visit/",
        "https://limbewildlife.org/",
    },
    "angola": {
        "https://minamb.gov.ao/web/noticias/o-triunfo-da-palanca-negra-gigante-em-cangandala/",
        "https://vivreenangola.com/tourisme/en-province/kwanza-sul/waku-kungo/",
        "https://mcta.gov.ao/ao/noticias/governadora-visita-ombala-mbalundo/",
        "https://minamb.gov.ao/web/noticias/serra-do-pindo-e-morro-do-moco-elevados-a-areas-de-conservacao-ambiental/",
    },
}


REMOVE_PHOTOS: dict[str, set[str]] = {
    "gabon": {
        "https://www.amazinggabon.com/en/akanda-national-park/",
        "https://www.amazinggabon.com/en/plateaux-bateke-national-park/",
        "https://inivatourism.com/en/activities/excursion-doussala-moukalaba-doudou/",
        "https://triptogabon.com/parc-national-des-plateaux-betekes/",
    },
    "camerun": {
        "https://mindtrip.ai/location/djoum-south-region/djoum/lo-96LaqLCZ",
    },
    "angola": {
        "https://mcta.gov.ao/ao/noticias/governadora-visita-ombala-mbalundo/",
    },
}


PHOTO_LEADS: dict[str, dict[int, str]] = {
    "gabon": {
        13: "https://static1.evcdn.net/images/reduction/279557_w-1600_h-1200_q-70_m-crop.jpg",
        18: "https://img.rts.ch/articles/2023/image/u36r77-26153018.image?h=720&w=1280",
    },
}

SYNC_PRIMARY_PHOTO = {"gabon"}


def apply(country: str) -> None:
    path = ROOT / "content" / "pois" / f"{country}.json"
    pois = json.loads(path.read_text(encoding="utf-8"))
    by_number = {poi["n"]: poi for poi in pois}

    for poi in pois:
        blocked_links = REMOVE_LINKS.get(country, set())
        poi["links"] = [
            item for item in poi.get("links", [])
            if not isinstance(item, dict) or item.get("url") not in blocked_links
        ]
        blocked_photos = REMOVE_PHOTOS.get(country, set())
        poi["photos"] = [
            item for item in poi.get("photos", [])
            if not isinstance(item, dict) or item.get("source") not in blocked_photos
        ]

    for number, (label, url) in LINKS.get(country, {}).items():
        poi = by_number[number]
        links = poi.setdefault("links", [])
        if not any(item.get("url") == url for item in links if isinstance(item, dict)):
            links.append({"label": label, "url": url})

    for number, details in VISITS.get(country, {}).items():
        by_number[number]["visit"] = details

    for number, (lat, lon) in COORDS.get(country, {}).items():
        by_number[number]["lat"] = lat
        by_number[number]["lon"] = lon

    for number, name in NAMES.get(country, {}).items():
        by_number[number]["name"] = name

    for number, description in DESCRIPTIONS.get(country, {}).items():
        by_number[number]["desc"] = description

    for number, additions in PHOTOS.get(country, {}).items():
        poi = by_number[number]
        photos = poi.setdefault("photos", [])
        unique_photos = []
        existing_sources = set()
        for item in photos:
            if not isinstance(item, dict):
                continue
            marker = photo_marker(item)
            if marker in existing_sources:
                continue
            unique_photos.append(item)
            existing_sources.add(marker)
        poi["photos"] = photos = unique_photos
        for photo in additions:
            marker = photo_marker(photo)
            if marker not in existing_sources:
                photos.append(photo)
                existing_sources.add(marker)

    for number, lead in PHOTO_LEADS.get(country, {}).items():
        photos = by_number[number].get("photos", [])
        lead_marker = canonical_source(lead)
        photos.sort(key=lambda item: canonical_source(item.get("img", "")) != lead_marker)

    if country in SYNC_PRIMARY_PHOTO:
        for poi in pois:
            photos = poi.get("photos", [])
            if not photos:
                continue
            primary = photos[0]
            poi["img"] = primary["img"]
            poi["source"] = primary["source"]
            poi["credit"] = primary["credit"]

    path.write_text(json.dumps(pois, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    replacements = FICHA_REPLACEMENTS.get(country, [])
    ficha_path = ROOT / "content" / "ficha" / f"{country}.json"
    if replacements and ficha_path.exists():
        ficha = json.loads(ficha_path.read_text(encoding="utf-8"))
        ficha = replace_nested(ficha, replacements)
        ficha_path.write_text(json.dumps(ficha, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for country_name in sorted(set(LINKS) | set(PHOTOS)):
        apply(country_name)

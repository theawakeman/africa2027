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
    "congo": {
        1: ("Presidencia del Congo · apertura del corredor Sembé–Souanké–Ntam", "https://presidence.cg/2020/06/01/discours-du-president-de-la-republique-sur-letat-de-la-nation/"),
        2: ("Nouabalé-Ndoki · distancias y acceso desde Ouesso", "https://ndoki.org/fr-fr/Visiter/Infos"),
        3: ("Visita oficial · Nouabalé-Ndoki", "https://ndoki.org/en-us/Visit/Park-info"),
        4: ("UNESCO · Odzala-Kokoua, Patrimonio Mundial", "https://whc.unesco.org/en/list/692"),
        5: ("Visit Odzala · Ngaga Lodge y reservas", "https://visitodzala-kokoua.org/"),
        6: ("Visit Odzala · visita de día al bai de Imbalanga", "https://visitodzala-kokoua.org/visiteurs-a-la-journee/"),
        7: ("Basílica de Santa Ana · historia y arquitectura", "https://fr.wikipedia.org/wiki/Basilique_Sainte-Anne-du-Congo_de_Brazzaville"),
        8: ("Ramsar · ficha oficial del sitio Rapides du Congo-Djoué", "https://rsis.ramsar.org/RISapp/files/RISrep/CG1857RIS.pdf"),
        9: ("Loufoulakari · localización e historia de las cataratas", "https://fr.wikipedia.org/wiki/Chutes_de_la_Loufoulakari"),
        10: ("Escuela de Poto-Poto · historia y principales artistas", "https://www.cesbc.org/culture_et_arts/artsplastiques/potopoto/potopoto.htm"),
        11: ("Dolisie · historia, transporte y contexto urbano", "https://fr.wikipedia.org/wiki/Dolisie"),
        12: ("Pointe-Noire · historia, barrios y transportes", "https://fr.wikipedia.org/wiki/Pointe-Noire_(r%C3%A9publique_du_Congo)"),
        13: ("TotalEnergies · inauguración del nuevo Museo Mâ Loango", "https://totalenergies.cg/decouvrir-totalenergies/actualites/inauguration-du-nouveau-musee-ma-loango-de-diosso-le-musee-de"),
        14: ("Noé · visita y conservación en Conkouati-Douli", "https://noe.org/actions/gestion-du-parc-national-de-conkouati-douli/"),
        15: ("Archives nationales du monde du travail · memoria del Congo-Océan", "https://archives-nationales-travail.culture.gouv.fr/Decouvrir/Dossiers-du-mois/Le-chemin-de-fer-Congo-Ocean-effroyable-consommateur-de-vies-humaines"),
        16: ("Proyecto Lésio-Louna · sitios de ecoturismo y accesos", "https://www.ppgcongo.org/eco-tourisme/"),
        17: ("WCS · creación y patrimonio natural de Ogooué-Leketi", "https://congo.wcs.org/fr-fr/News/ID/25021/Creation-du-Parc-National-dOgoue-Leketi"),
        18: ("Monumento del Ecuador · ficha cartográfica y coordenadas", "https://virtualglobetrotting.com/map/equator-monument-2/"),
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
    "congo": {
        1: {
            "why": "No es una atracción aislada: es la primera escala para entender el corredor transfronterizo y decidir si el tramo forestal hacia Ouesso es viable ese día.",
            "see": "Mercado, vida de una pequeña cabecera forestal y el contraste entre la carretera internacional nueva y los servicios locales limitados.",
            "access": "El pin coincide con la ficha de Souanké en Google Maps. Resolver aquí cualquier sello pendiente y preguntar por combustible, carretera y cobertura antes de seguir.",
            "when": "Llegar de día; una tarde y una noche bastan si el paso fronterizo y los papeles están completos.",
            "skip": "No saltarse la comprobación administrativa; sí reducir la parada si todo está resuelto y queda luz suficiente para una siguiente etapa segura.",
        },
        2: {
            "why": "Es la base imprescindible del norte: desde aquí se preparan Nouabalé-Ndoki, la puerta oriental de Odzala y, en sentido inverso, el cruce hacia Camerún.",
            "see": "El puerto y el río Sangha muestran la función fluvial de la ciudad; el resto de la parada debe dedicarse a combustible, compras, salud y comunicaciones.",
            "access": "El pin identifica Ouesso, no un hotel ni un embarcadero. Pedir al operador de cada parque su punto de recogida y comprobar Socambo por separado.",
            "when": "Una o dos noches, preferiblemente incluyendo horas laborables para reservas y gestiones.",
            "skip": "No gastar días de parque en turismo urbano; tampoco abandonar Ouesso sin autonomía y confirmaciones escritas.",
        },
        3: {
            "why": "Permite entrar en una selva primaria excepcional y observar un bai de investigación dentro del Trinacional de la Sangha, Patrimonio Mundial.",
            "see": "Mbeli Bai, bosque inundado y posible fauna de selva; Mondika y Wali son experiencias distintas y ninguna observación está garantizada.",
            "access": "No navegar al centroide. La visita se cierra con el parque desde Ouesso y combina pista, barca y base en Bomassa según el programa contratado.",
            "when": "Reservar de tres a cinco días y confirmar temporada, transporte, campamento y cupos con mucha antelación.",
            "skip": "Descartarlo si no hay reserva oficial, si el traslado ocupa casi todo el tiempo disponible o si no se puede resolver el cuidado del perro fuera del parque.",
        },
        4: {
            "why": "Es el gran objetivo natural del país: selva del Congo, bais y uno de los principales refugios de gorila y elefante de bosque.",
            "see": "Caminatas guiadas, barca, claros forestales y fauna posible; cada campamento ofrece un sector y una experiencia diferentes.",
            "access": "El pin es la ficha oficial del parque en Google Maps, no una puerta. Elegir antes entre puerta oriental, Camp Imbalanga y lodges del sector occidental.",
            "when": "Mínimo cuatro días; confirmar lluvias, 4x4, alojamiento, traslados y actividades en la reserva.",
            "skip": "No entrar con un itinerario ambiguo ni esperar resolverlo al llegar: el tamaño del parque hace inútil un pin sin operador y sector definidos.",
        },
        5: {
            "why": "Es la experiencia especializada de seguimiento de gorila de llanura occidental habituado y una de las pocas de este tipo en África central.",
            "see": "Rastreo a pie en bosque denso, explicación de los investigadores y el propio lodge; el encuentro con gorilas nunca se garantiza.",
            "access": "El pin coincide con Ngaga Lodge en Google Maps. Solo ir con reserva, traslado y permiso confirmados por el operador.",
            "when": "Reservar con antelación y dejar margen por lluvia, salud y movimientos del grupo.",
            "skip": "Descartarlo si faltan precio total, protocolo sanitario, edad mínima, política de cancelación o un plan seguro para el perro.",
        },
        6: {
            "why": "Imbalanga permite observar con paciencia un claro forestal sin confundirlo con el producto de gorilas de Ngaga.",
            "see": "Bai, mirador, huellas, bosque y posibles gorilas, elefantes, búfalos o sitatungas; son animales libres y no hay garantía.",
            "access": "La coordenada es la localización científica publicada de Camp Imbalanga. El operador debe entregar la puerta y el punto final de encuentro; no hay un pin independiente fiable en Maps.",
            "when": "Como salida de día desde la puerta oriental o con noche en el campamento, siempre con actividad y traslado confirmados.",
            "skip": "No usar la coordenada de investigación como instrucciones de acceso ni mezclar en una sola reserva los bais de Lokoué, Moba e Imbalanga.",
        },
        7: {
            "why": "La basílica es la obra arquitectónica más reconocible de Brazzaville y la capital es la base real para preparar el ferry y reparar los vehículos.",
            "see": "Las tejas verdes, la nave de ladrillo y la luz interior de Santa Ana; completar con un paseo breve por el centro y el frente fluvial permitido.",
            "access": "El pin coincide con la basílica. Aparcar en recinto vigilado y evitar fotos del puerto, Beach, controles y edificios sensibles.",
            "when": "Visita con luz; reservar días laborables para gestor, bancos, talleres y trámites del ferry.",
            "skip": "No ampliar la estancia urbana si el ferry y ambos vehículos están resueltos; la logística prima sobre acumular paradas.",
        },
        8: {
            "why": "El Djoué hace visible el sistema de rápidos que impidió continuar la navegación hacia el Atlántico y condicionó la historia del transporte del Congo.",
            "see": "Canal rocoso, saltos y ribera dentro del humedal Ramsar Rapides du Congo-Djoué; no es una cascada acondicionada.",
            "access": "El pin coincide con el hito de Google Maps «cataracte bord du djoue». Confirmar acceso local, mantener distancia del caudal y no usar dron.",
            "when": "De día y con roca seca; el nivel del agua cambia mucho la seguridad y la visibilidad.",
            "skip": "Renunciar con lluvia, crecida, controles o cualquier restricción de fotografía en la zona sensible del río.",
        },
        9: {
            "why": "Es la excursión de naturaleza más potente al sur de Brazzaville: varias caídas del Loufoulakari sobre grandes estratos de arenisca.",
            "see": "Rápidos, escalones de roca y confluencia cercana con el Congo; las Chutes de Béla pertenecen al Louvoubi y son otro lugar.",
            "access": "El pin corresponde a Loufoulakari. Llegar por Mbanza-Ndounga/Kimpandzou con guía y estado de la pista confirmado; no seguir una etiqueta ambigua.",
            "when": "Jornada completa, salida temprana y roca razonablemente seca.",
            "skip": "No intentarlo tarde, con tormenta, sin acompañamiento local o si el último tramo no está practicable.",
        },
        10: {
            "why": "La escuela fundada por Pierre Lods en 1951 permite entender una corriente decisiva de la pintura moderna de África central y ver obra contemporánea en su lugar de producción.",
            "see": "Talleres, galería, artistas trabajando y pinturas de estilos muy distintos; preguntar antes de fotografiar o comprar.",
            "access": "El pin coincide con École de Peinture de Poto-Poto en Google Maps, Rue Mayama. Los mercados de Poto-Poto y Total son paradas separadas.",
            "when": "En horario diurno, idealmente contactando antes para confirmar que el taller está abierto.",
            "skip": "Omitirla si está cerrada; no sustituirla por una visita improvisada a un mercado concurrido con cámaras y perro.",
        },
        11: {
            "why": "Dolisie explica la unión entre carretera y Congo-Océan y es la escala de servicios más lógica entre Brazzaville y la costa.",
            "see": "La estación, edificios del periodo ferroviario y una ciudad de cruce más funcional que monumental.",
            "access": "El pin marca el centro de Dolisie; la estación tiene su propio acceso al este. Llegar con luz y escoger aparcamiento seguro.",
            "when": "Una noche para combustible, taller, comida y descanso si se realiza el gran desvío occidental.",
            "skip": "Si no se baja a Pointe-Noire o Conkouati, no justifica por sí sola el desvío desde la ruta principal.",
        },
        12: {
            "why": "Muestra la costa, el puerto y la economía petrolera del país, además de ofrecer los mejores servicios mecánicos del suroeste.",
            "see": "Centro, frente atlántico y Côte Sauvage; Pointe Indienne requiere un desplazamiento aparte y comprobación del acceso.",
            "access": "El pin identifica el centro urbano. No fotografiar instalaciones portuarias o petroleras y confirmar por teléfono cualquier repuesto antes de recorrer la RN1.",
            "when": "Dos noches si se combina ciudad, costa y mantenimiento; más si se continúa a Conkouati.",
            "skip": "El viaje de ida y vuelta desde Brazzaville ronda mil kilómetros: descartarlo si no aporta costa, parque o una reparación concreta.",
        },
        13: {
            "why": "El nuevo museo es la mejor introducción al reino de Loango, la cultura vili y la memoria de la trata atlántica antes de recorrer Diosso.",
            "see": "Colecciones permanentes y temporales en el complejo inaugurado en 2018; el antiguo palacio-museo queda como referencia histórica separada.",
            "access": "El pin se ha trasladado al nuevo Museo de Loango visible en Google Maps y satélite. Confirmar horario y reglas de fotografía.",
            "when": "Media jornada, combinable con la garganta de Diosso solo si se usa para esta última su acceso específico y seguro.",
            "skip": "No navegar a la antigua ficha de Musée Mâ Loango marcada como cerrada; tampoco acercarse al borde de la garganta sin guía local.",
        },
        14: {
            "why": "Reúne en un solo parque costa salvaje, lagunas, bosque y sabana, con tortugas marinas y un programa de rehabilitación de chimpancés.",
            "see": "Paisaje lagunar y atlántico, playas de puesta en temporada y recorridos autorizados; ninguna especie es un avistamiento seguro.",
            "access": "El pin es un punto de referencia dentro del parque, no una oficina ni una puerta. Noé u operador debe fijar sector, guía, alojamiento y encuentro desde Pointe-Noire.",
            "when": "Dos o tres días y reserva previa; preguntar por lluvias, pistas y temporada de tortugas.",
            "skip": "Descartarlo sin respuesta operativa, con pistas cerradas o si no existe una solución segura para dejar al perro fuera del área de fauna.",
        },
        15: {
            "why": "La estación permite contar tanto la ingeniería que conectó Brazzaville con el mar como el enorme coste humano del trabajo forzado colonial.",
            "see": "Estación terminal de Brazzaville, fotografías históricas y trazado; no se presenta el tren como transporte turístico disponible.",
            "access": "El pin coincide con Gare Centrale de Brazzaville. Preguntar en taquilla solo para información actual y fotografiar con permiso.",
            "when": "Media hora o una hora durante la estancia en la capital; integrar la memoria del ferrocarril con la visita a Djoué.",
            "skip": "No comprar ni organizar etapas basándose en horarios antiguos: no se ha confirmado un servicio de pasajeros utilizable para el viaje.",
        },
        16: {
            "why": "Es un proyecto de rehabilitación y reintroducción de gorilas cercano a la RN2, con una historia de conservación distinta de Odzala.",
            "see": "Según el circuito confirmado, vivero, lagos, sabana, navegación o gorilas reintroducidos; la web disponible es antigua y no garantiza que cada actividad siga abierta.",
            "access": "El pin coincide con la ficha de la reserva en Google Maps, pero no define la entrada. PPG debe confirmar si se entra por Iboubikro, Abio u otro punto.",
            "when": "Solo con cita, programa y precio actuales por escrito y con el cuidado del perro resuelto fuera del proyecto.",
            "skip": "No desplazarse usando el folleto histórico como confirmación operativa; sin respuesta reciente, tratar la visita como no disponible.",
        },
        17: {
            "why": "Djambala introduce la sabana ondulada y los bosques-galería de las mesetas Batéké y sirve de base para evaluar el corredor occidental de subida.",
            "see": "La ciudad, el altiplano y el paisaje de la P20. Ogooué-Leketi es un parque remoto distinto, no una excursión automática desde este pin.",
            "access": "El pin coincide con Djambala. Comprobar combustible y estado de la ruta hacia Lékana/Okoyo; no entrar al parque sin autoridad o guía que fije acceso.",
            "when": "Una noche como escala; reservar más solo si existe una actividad concreta y confirmada.",
            "skip": "No añadir días esperando turismo organizado en Ogooué-Leketi: la fuente de WCS documenta su valor y creación, no una visita abierta.",
        },
        18: {
            "why": "Es una parada breve y legible sobre el propio paralelo cero, mucho más precisa que representar a la vez Makoua y Owando.",
            "see": "La esfera armilar del monumento y el cruce de la línea del Ecuador; la antigua torre de Makoua puede verse como referencia urbana secundaria.",
            "access": "El pin coincide con el monumento junto a la carretera, validado por dos cartografías independientes. Detenerse fuera de la calzada y pedir permiso si hay gente.",
            "when": "Parada corta con luz durante la etapa de la RN2; usar Owando para los servicios importantes.",
            "skip": "No convertirlo en una noche adicional si se dispone de luz y autonomía para llegar a la escala planificada.",
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
    "congo": {
        4: (1.3206287, 14.8454619),
        6: (0.7630556, 15.2608333),
        8: (-4.3098988, 15.2287212),
        10: (-4.2544308, 15.2743693),
        13: (-4.62554, 11.85238),
        15: (-4.269353, 15.288332),
    },
}


NAMES: dict[str, dict[int, str]] = {
    "camerun": {
        20: "Cataratas de la Métché (desde Bafoussam)",
    },
    "congo": {
        6: "Camp Imbalanga y su bai · Odzala oriental",
        10: "Escuela de Pintura de Poto-Poto",
        13: "Nuevo Museo Mâ Loango de Diosso",
        15: "Estación de Brazzaville · memoria del Congo-Océan",
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
    "congo": {
        1: (
            "Souanké es la cabecera del distrito noroccidental por el que entra el corredor Brazzaville–Yaundé "
            "desde Ntam; Sembé queda más al este y no comparte este pin. El tramo Sembé–Souanké–Ntam, de "
            "unos 143 km, fue asfaltado dentro del programa de integración regional e inaugurado en marzo de 2020. "
            "La mejora de la calzada no convierte Souanké en una gran base: mercado, gendarmería y combustible "
            "pueden ser limitados. El pin coincide con la ficha de Google Maps; confirmar allí sellos, papeles del "
            "vehículo y estado del eje antes de internarse hacia Ouesso."
        ),
        2: (
            "Ouesso creció como puerto del Sangha y hoy es la capital del departamento de Sangha y la base logística "
            "del norte congoleño. Desde aquí se coordinan Nouabalé-Ndoki, la puerta oriental de Odzala y, en sentido "
            "inverso, el paso fluvial de Socambo hacia Camerún. El puerto, el mercado y el movimiento de piraguas y "
            "barcazas explican mejor la ciudad que un monumento aislado. Conviene resolver combustible, efectivo, "
            "compras, salud y comunicaciones antes de salir; cada parque debe proporcionar su punto real de recogida."
        ),
        4: (
            "Protegido desde 1935, Odzala-Kokoua ocupa un gran mosaico de selva, sabana y claros pantanosos en la "
            "Cuvette-Ouest. Es Reserva de la Biosfera y desde 2023 Patrimonio Mundial de la UNESCO por sus procesos "
            "ecológicos y poblaciones de elefante de bosque, gorila de llanura occidental y otros mamíferos. Los bais "
            "permiten que la fauna salga del bosque, pero ningún avistamiento se promete. La coordenada coincide con "
            "la ficha del parque en Google Maps y es representativa, no una puerta: sector, campamento, 4x4 y traslados "
            "deben cerrarse antes de trazar el acceso."
        ),
        6: (
            "Camp Imbalanga, abierto al ecoturismo en el sector oriental de Odzala, se encuentra junto a un bai donde "
            "la observación paciente puede revelar gorilas, elefantes, búfalos, sitatungas y primates. No debe fundirse "
            "en una sola ficha con Lokoué o Moba: son claros y logísticas distintos. La coordenada procede de la "
            "localización de Camp Imbalanga publicada en un estudio científico (00°45′47″ N, 15°15′39″ E); Google "
            "Maps no ofrece un pin propio fiable. African Parks publica salidas desde la puerta oriental, a unas dos "
            "horas de Ouesso, pero debe entregar el punto de encuentro y las condiciones vigentes."
        ),
        8: (
            "Los rápidos del Djoué forman parte del humedal Ramsar Rapides du Congo-Djoué, inscrito en 2009 y de unas "
            "2.500 ha, donde el Djoué y la Loua atraviesan canales rocosos antes de alcanzar el Congo. Este obstáculo "
            "natural ayuda a entender por qué la navegación entre el Pool Malebo y el Atlántico no es continua y por "
            "qué se construyó el ferrocarril Congo-Océan. El pin coincide con el hito «cataracte bord du djoue» de Google "
            "Maps, no con un restaurante ni con la presa. La ribera no está acondicionada: roca seca, distancia al "
            "caudal, permiso fotográfico local y nada de dron."
        ),
        9: (
            "A unos 75 km al sur de Brazzaville, el Loufoulakari se precipita en varias gradas sobre grandes estratos "
            "de arenisca poco antes de desembocar en el Congo. El acceso habitual deja la carretera principal hacia "
            "Mbanza-Ndounga y Kimpandzou y termina por pista, sin infraestructura turística consolidada. La coordenada "
            "se ha validado con la localización publicada de Loufoulakari. No es «Chutes de Béla»: Béla es otra cascada, "
            "sobre el Louvoubi y a más de 30 km. Salir temprano, ir con contacto local y evitar roca mojada o crecida."
        ),
        10: (
            "Pierre Lods fundó en 1951 el taller que se convertiría en la Escuela de Pintura de Poto-Poto. Su método "
            "inicial favoreció la experimentación libre y dio origen a estilos de gran influencia en el arte moderno de "
            "África central, desde las figuras «Mickey» hasta generaciones posteriores muy diversas. El pin ya no es un "
            "centroide del barrio: coincide con la escuela real en Rue Mayama, Google Maps. Taller, galería y artistas "
            "merecen la visita; los mercados de Poto-Poto, Plateau y Total son lugares distintos y no comparten pin."
        ),
        11: (
            "Dolisie nació como estación y nudo del ferrocarril Congo-Océan; entre 1975 y 1991 llevó oficialmente el "
            "nombre de Loubomo. Hoy enlaza la RN1 Brazzaville–Pointe-Noire con las rutas del Niari y hacia la frontera "
            "gabonesa. La estación y los edificios vinculados al ferrocarril conservan la huella de esa historia, pero "
            "su valor para el viaje es sobre todo práctico: talleres, combustible y hospital a mitad del largo desvío "
            "occidental. El pin representa el centro urbano; la estación se visita con su acceso propio."
        ),
        12: (
            "Pointe-Noire se desarrolló como terminal atlántica del Congo-Océan y desde la apertura del ferrocarril y "
            "el puerto en la década de 1930 se convirtió en la capital económica del país. El petróleo reforzó después "
            "su papel portuario y explica la presencia de talleres, recambios y sanidad privada. Côte Sauvage y el "
            "frente atlántico aportan una costa muy distinta del interior; Pointe Indienne es un desplazamiento separado. "
            "La RN1 desde Brazzaville supone unos 510 km por sentido, por lo que solo compensa por costa, Conkouati o una "
            "necesidad mecánica confirmada."
        ),
        13: (
            "El nuevo Museo Mâ Loango fue construido para sustituir al pequeño museo instalado desde 1982 en el antiguo "
            "palacio real, ya muy degradado. Inaugurado el 23 de agosto de 2018 en un complejo de 5.000 m², conserva "
            "colecciones sobre el reino de Loango, la cultura vili, los oficios y la trata atlántica. Google Maps aún "
            "muestra la ficha del antiguo palacio como cerrada; el pin se ha trasladado al nuevo «Musée de Loango», "
            "cuya posición también se comprobó por satélite. La garganta de Diosso es otra visita y exige un acceso seguro "
            "propio, lejos del borde erosionado."
        ),
        15: (
            "La estación terminal de Brazzaville abrió con el Congo-Océan en 1934, tras trece años de obras destinadas "
            "a salvar los rápidos que separan el Pool Malebo del Atlántico. La línea de unos 510 km quedó asociada al "
            "trabajo forzado colonial y a la muerte de al menos 17.000 trabajadores africanos, denunciada entonces por "
            "André Gide y Albert Londres. El pin coincide con la Gare Centrale. No se ha podido confirmar un servicio "
            "de pasajeros actual y utilizable para este viaje: las estadísticas de 2025 muestran un tráfico residual. "
            "La visita es histórica; no debe presentarse La Gazelle como alternativa operativa."
        ),
        16: (
            "El proyecto Lésio-Louna, impulsado por el Estado congoleño y The Aspinall Foundation, rehabilita gorilas "
            "huérfanos y desarrolla reintroducciones desde la década de 1990. Sus materiales describen varios lugares "
            "diferentes —Iboubikro, Abio y Confluent— con vivero, lagos, sabana y navegación; no son una sola puerta ni "
            "una garantía de ver gorilas en libertad. El pin coincide con la ficha de la reserva en Google Maps, pero la "
            "web operativa disponible es antigua. Solo planear la visita si PPG confirma por escrito sitio, acceso, "
            "actividad, tarifa y protocolo sanitario actuales."
        ),
        17: (
            "Djambala es la capital del departamento de Plateaux y una base para leer el paisaje de arenas antiguas, "
            "sabanas onduladas y estrechos bosques-galería de las mesetas Batéké. La ruta por Ngo, Djambala, Lékana y "
            "Okoyo ofrece un corredor occidental hacia el norte, sujeto a verificación de calzada y combustible. El "
            "Parque Nacional de Ogooué-Leketi, creado en 2018 con 350.000 ha y contiguo a Batéké en Gabón, protege la "
            "transición de sabana y selva y las cabeceras del Ogooué y el Leketi. Es un enclave remoto distinto: la "
            "fuente de WCS no confirma turismo abierto, por lo que no se promete como excursión desde Djambala."
        ),
        18: (
            "Makoua está atravesada por la línea del Ecuador. Junto a la carretera, una esfera armilar señala de forma "
            "visible el paso del paralelo cero y ofrece una parada breve con significado geográfico. La coordenada "
            "coincide con el monumento en dos cartografías independientes, no con un centroide municipal. La antigua "
            "torre de Makoua aporta una referencia urbana secundaria, mientras Owando, unos 80 km al sur, sigue siendo "
            "la base de servicios importante de la RN2. Detenerse fuera de la calzada y no confundir ambas ciudades."
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
    "congo": [
        (
            "&lt;strong&gt;",
            "<strong>",
        ),
        (
            "&lt;/strong&gt;",
            "</strong>",
        ),
        (
            "Si se descarta con los coches, el ferrocarril Congo-Océan permite hacerlo en tren dejando los vehículos en Brazzaville.",
            "No se ha confirmado un servicio de pasajeros utilizable; si se descarta el desvío con los coches, se renuncia al suroeste o se verifica en la estación una alternativa vigente, sin basar el plan en horarios antiguos.",
        ),
        (
            "Ngaga (trekking) + bais de Lokoué y Moba + río Mambili",
            "Ngaga (trekking) o Camp Imbalanga (bai), según la reserva cerrada",
        ),
        (
            "las excursiones guiadas desde Camp Imbalanga al complejo de bais de Moba y otros senderos del parque llevan a plataformas y claros pantanosos donde salen al descubierto elefantes de bosque, búfalos, sitatungas y a veces gorilas. Es la alternativa a pie que SÍ se puede reservar sin operador de lujo, y la que más fauna da por hora de esfuerzo.",
            "las salidas guiadas de Camp Imbalanga se concentran en su propio bai y en los senderos del sector oriental, con puntos de observación donde pueden aparecer elefantes de bosque, búfalos, sitatungas o gorilas. No se mezclan con los bais de Moba o Lokoué, que tienen otra localización y logística, y ninguna fauna está garantizada.",
        ),
        (
            '<tr ><td>Desvío suroeste · decisión</td><td>Decidir si Pointe-Noire, Diosso y Conkouati entran en el calendario (~1.000 km y 4-6 días) o si se sustituyen por más días en Odzala. Valorar la opción de hacerlo en el tren Congo-Océan dejando los vehículos en Brazzaville.</td></tr>',
            '<tr ><td>Desvío suroeste · decisión</td><td>Decidir si Pointe-Noire, Diosso y Conkouati entran en el calendario (~1.000 km y 4-6 días) o si se sustituyen por más días en Odzala. No contar con el tren: no se ha confirmado un servicio de pasajeros utilizable.</td></tr>',
        ),
        (
            '<tr ><td>Lésio-Louna · visita sin reserva</td><td>Confirmar con la Fundación Aspinall las tasas, el horario y si admiten visita de un día sin reserva previa, para encajarlo en el corredor de subida.</td></tr>',
            '<tr ><td>Lésio-Louna · visita actual</td><td>Exigir confirmación escrita y vigente de la Fundación Aspinall sobre acceso, reserva, tasas, horario y punto de encuentro. Sin respuesta, tratar la visita como no disponible.</td></tr>',
        ),
        (
            '<tr ><td>Ferrocarril Congo-Océan</td><td>Confirmar si el tren «La Gazelle» Brazzaville-Pointe-Noire circula con regularidad en 2027, frecuencia y precio: sería la forma de ver el suroeste sin mover los vehículos.</td></tr>',
            '<tr ><td>Ferrocarril Congo-Océan</td><td>No usarlo como alternativa planificada. Solo reconsiderarlo si CFCO confirma por escrito un servicio de pasajeros, fechas y condiciones vigentes.</td></tr>',
        ),
        (
            '<tr ><td>Fotos pendientes de sustituir</td><td>Souanké/Sembé, Ouesso, Nouabalé-Ndoki, los bais de Odzala, Loufoulakari, Diosso, Conkouati, el CFCO y las mesetas Batéké usan imágenes de referencia de la especie o de la región, no del propio sitio: sustituir por fotos propias cuando las tengamos.</td></tr>',
            "",
        ),
        (
            "Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Las tarifas de Odzala citadas son las públicas de 2025 y hay que revalidarlas para 2027.",
            "Última revisión de esta versión: 14 de septiembre de 2026. La historia, los PDI, sus fotografías, enlaces y coordenadas se han auditado; esta ficha sigue siendo una herramienta de planificación, no una autorización de entrada ni una guía de navegación. Las tarifas y condiciones operativas deben revalidarse para 2027.",
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
    "congo": {
        1: [
            commons("Sur les routes de la République du Congo. 01.jpg", "ArnoBOUJIKA · CC BY 4.0", "Entrada de Souanké en el corredor forestal del noroeste"),
            commons("Sur les routes de la République du Congo. 02.jpg", "ArnoBOUJIKA · CC BY 4.0", "Carretera y paisaje urbano de Souanké"),
            commons("Sur les routes de la République du Congo. 03.jpg", "ArnoBOUJIKA · CC BY 4.0", "Eje asfaltado fotografiado dentro de Souanké"),
        ],
        2: [
            commons("Ouesso.jpg", "OUesso · CC BY-SA 4.0", "Vista de Ouesso al anochecer, complemento del puerto y el río Sangha"),
        ],
        3: [
            commons("African elephant, Mbeli-Bai, Republic of Congo (18320426684).jpg", "Dirck Byler / USFWS · dominio público", "Elefante de bosque fotografiado en Mbeli Bai"),
            commons("Gorilla tool use-Leah.jpg", "Thomas Breuer et al. · CC BY 2.5", "La gorila Leah usando una rama para comprobar la profundidad del agua en Mbeli Bai"),
        ],
        5: [
            {
                "img": "https://canadiangeographic.ca/wp-content/uploads/2026/07/KAMBA-Gorilla-Tracking-at-Ngaga-Andrew-Howard-1024x724.jpg",
                "source": "https://canadiangeographic.ca/articles/the-good-life-a-walk-in-the-park-in-congo/",
                "credit": "Andrew Howard / Kamba Africa · Canadian Geographic",
                "caption": "Rastreo guiado de gorilas desde Ngaga Lodge",
            },
            {
                "img": "https://canadiangeographic.ca/wp-content/uploads/2026/07/Kamba-Primates-ANDREW-HOWARD-Wildlife13-1024x705.jpg",
                "source": "https://canadiangeographic.ca/articles/the-good-life-a-walk-in-the-park-in-congo/",
                "credit": "Andrew Howard / Kamba Africa · Canadian Geographic",
                "caption": "Gorila de llanura occidental observado durante el seguimiento de Ngaga",
            },
            {
                "img": "https://visitodzala-kokoua.org/wp-content/uploads/sites/7/2024/05/KAMBA-Odzala-Ngaga-Lodge-image_-Scott-Ramsey.jpg",
                "source": "https://visitodzala-kokoua.org/",
                "credit": "Scott Ramsey / Kamba Africa · Visit Odzala",
                "caption": "Zona común de Ngaga Lodge dentro del bosque",
            },
        ],
        6: [
            {
                "img": "https://africageographic.com/wp-content/uploads/2024/04/Camp-Imbalanga-1.jpg",
                "source": "https://africageographic.com/stories/odzala-kokoua-sojourn/",
                "credit": "Brendan Taylor · Africa Geographic",
                "caption": "Tiendas de Camp Imbalanga bajo el bosque de Odzala",
            },
            {
                "img": "https://africageographic.com/wp-content/uploads/2024/04/Imbalanga-Bai-lookout-Brendan-Taylor-DJI_0178.jpg",
                "source": "https://africageographic.com/stories/odzala-kokoua-sojourn/",
                "credit": "Brendan Taylor · Africa Geographic",
                "caption": "Mirador y claro inundado del bai de Imbalanga",
            },
            {
                "img": "https://africageographic.com/wp-content/uploads/2024/04/western-lowland-gorilla-silverback-Camp-Imbalanga-30.jpg",
                "source": "https://africageographic.com/stories/odzala-kokoua-sojourn/",
                "credit": "Brendan Taylor · Africa Geographic",
                "caption": "Gorila de llanura occidental fotografiado en Camp Imbalanga",
            },
        ],
        8: [
            {
                "img": "https://3.bp.blogspot.com/-o8EMkLexwmA/WbfenoYFXDI/AAAAAAAABKU/GKYWr418oz8FvFp3FUZ4JazS6nN3eGdEgCLcBGAs/s1600/5.jpg",
                "source": "https://congobrazzafrique.blogspot.com/2017/09/le-pont-du-djoue.html",
                "credit": "Congo Brazzafrique",
                "caption": "Puente sobre el Djoué y los rápidos rocosos",
            },
            {
                "img": "https://1.bp.blogspot.com/-oytQDabJllU/WbfeazTiKnI/AAAAAAAABKQ/YmKAkHUQGIECZKTBap1LC2j1rLWUogqogCLcBGAs/s1600/3.jpg",
                "source": "https://congobrazzafrique.blogspot.com/2017/09/le-pont-du-djoue.html",
                "credit": "Congo Brazzafrique",
                "caption": "Canal y saltos de agua en los rápidos del Djoué",
            },
            {
                "img": "https://3.bp.blogspot.com/-C6PcA7N5hK8/Wbff3sS2CBI/AAAAAAAABK4/Os_OejPUkFMrUMhpoasAUwh21_ka6MuCACEwYBhgL/s1600/13.jpg",
                "source": "https://congobrazzafrique.blogspot.com/2017/09/le-pont-du-djoue.html",
                "credit": "Congo Brazzafrique",
                "caption": "Tramo encajado del Djoué junto al acceso de los rápidos",
            },
        ],
        9: [
            commons("Miss Loufoulakari 01.jpg", "Simple fleur · CC0", "Caída y grandes losas de arenisca de Loufoulakari"),
            commons("Miss Loufoulakari 02.jpg", "Simple fleur · CC0", "Rápidos superiores de las cataratas de Loufoulakari"),
            commons("Miss Loufoulakari 09.jpg", "Simple fleur · CC0", "Vista frontal de uno de los saltos de Loufoulakari"),
        ],
        10: [
            commons("Ecole de peinture de Poto-Poto Brazzaville 07.jpg", "Africany · CC0", "Entrada de la Escuela de Pintura de Poto-Poto"),
            commons("Ecole de peinture de Poto-Poto Brazzaville 06.jpg", "Africany · CC0", "Galería y obras expuestas dentro de la escuela"),
            commons("Ecole de peinture de Poto-Poto Brazzaville 02.jpg", "Africany · CC0", "Artista trabajando en la Escuela de Poto-Poto"),
        ],
        11: [
            commons("Dolisie.jpg", "Jomako · CC BY-SA 3.0", "Vista urbana de Dolisie"),
            commons("Gare de Dolisie.jpg", "Allweno · CC BY-SA 4.0", "Fachada de la estación ferroviaria de Dolisie"),
            commons("Gare de Dolisie (arrière).jpg", "Allweno · CC BY-SA 4.0", "Andenes y parte posterior de la estación de Dolisie"),
        ],
        12: [
            commons("Pointe-Noire downtown.jpg", "David Stanley · CC BY 2.0", "Centro urbano de Pointe-Noire"),
            commons("Wikimédia République du Congo - Pointe Noire. 01.jpg", "ArnoBOUJIKA · CC BY 4.0", "Calle de Pointe-Noire; archivo geolocalizado en el centro"),
            commons("Un après-midi sur la Côte sauvage.jpg", "Krissima POBA NGOUMA · CC BY-SA 4.0", "Côte Sauvage, la playa atlántica de Pointe-Noire"),
        ],
        13: [
            commons("Guide du Mussée Ma Loango de Diosso.jpg", "Roly USD · CC0", "Guía ante el nuevo complejo del Museo Mâ Loango de Diosso"),
            commons("Wikimedien de la république du congo.jpg", "Roly USD · CC0", "Visitantes en el nuevo Museo Mâ Loango"),
            commons("Ma-Loango Regional Museum (19541380803).jpg", "David Stanley · CC BY 2.0", "Antiguo palacio real que albergó el museo desde 1982; no es el edificio actual"),
        ],
        14: [
            {
                "img": "https://noe.org/app/uploads/2025/05/PNCD_PIC_DJI_ARTHUR-24-2048x1536.jpeg",
                "source": "https://noe.org/actions/gestion-du-parc-national-de-conkouati-douli/",
                "credit": "Arthur · Noé",
                "caption": "Vista aérea de la laguna, la costa y el bosque de Conkouati-Douli",
            },
            {
                "img": "https://www.help-congo.org/thumbnail/eco-tourism/eco-tourisme.jpg?fit=crop&h=400&s=08cb10de852ff036d8de064f8af097b9&w=400",
                "source": "https://www.help-congo.org/ecotourisme",
                "credit": "HELP Congo",
                "caption": "Playa del parque dentro del circuito de ecoturismo de HELP Congo",
            },
            {
                "img": "https://www.help-congo.org/thumbnail/eco-tourism/jorda-grande-ile.jpg?h=600&s=c74fe553f1ec8411df7e148da864bf37&w=1080",
                "source": "https://www.help-congo.org/ecotourisme",
                "credit": "HELP Congo",
                "caption": "Aproximación en piragua al proyecto de chimpancés en la laguna",
            },
        ],
        15: [
            commons("Brazzaville-Congo-Ocean Railway-1932.jpg", "Autor desconocido · dominio público", "Estación y tren del Congo-Océan en Brazzaville en 1932"),
            commons("Travailleurs sur le chantier du chemin de fer Congo-Océan, dans la colonie française du Moyen-Congo, vers 1923.png", "Touring Club Italiano / Marka / UIG · dominio público", "Trabajadores del Congo-Océan hacia 1923"),
            commons("Photographie de travailleurs forcés sur le chantier du chemin de fer Congo-Océan (1924-1925).jpg", "Autor desconocido · dominio público", "Trabajadores forzados durante la construcción, 1924–1925"),
        ],
        16: [
            {
                "img": "https://blog.aspinallfoundation.org/hs-fs/hubfs/2020A-160%20Congo%20Camera%20Trap%20Image%20-%20Makouas%20Group%20Jan%202021%20.jpeg?name=2020A-160+Congo+Camera+Trap+Image+-+Makouas+Group+Jan+2021+.jpeg&width=8367",
                "source": "https://blog.aspinallfoundation.org/one-year-anniversary-of-our-big-cat-project-in-lesio-louna-reserve",
                "credit": "The Aspinall Foundation",
                "caption": "Grupo de Makoua registrado por cámara trampa en Lésio-Louna",
            },
            {
                "img": "https://blog.aspinallfoundation.org/hs-fs/hubfs/2020A-160%20Congo%20Makoua%20Group%20Matt%20Bonnet.jpg?name=2020A-160+Congo+Makoua+Group+Matt+Bonnet.jpg&width=3477",
                "source": "https://blog.aspinallfoundation.org/tracking-leopards-lions-in-l%C3%A9sio-louna-reserve-republic-of-congo",
                "credit": "Matt Bonnet · The Aspinall Foundation",
                "caption": "Seguimiento de gorilas reintroducidos del grupo de Makoua",
            },
            {
                "img": "https://blog.aspinallfoundation.org/hubfs/STG-CA-680%20Silverback%20Djeke%20in%20Lesio-Louna%20reserve%20Credit%20The%20Aspinall%20Foundation.jpg",
                "source": "https://blog.aspinallfoundation.org/the-benefits-of-smart-technology-on-our-conservation-programme-in-l%C3%A9sio-louna",
                "credit": "The Aspinall Foundation",
                "caption": "El espalda plateada Djeke dentro de la reserva de Lésio-Louna",
            },
        ],
        17: [
            {
                "img": "https://4.bp.blogspot.com/-IZ93F57i_70/W_UW4QZpkMI/AAAAAAAAAUk/JbAurMdZSjYkfieb4wHY8VKVjg15miCtQCLcBGAs/s1600/Boulevard%2BDenis%2BSASSOU%2BNGUESSO%2Bde%2BDjambala.jpg",
                "source": "https://cdpcongo.blogspot.com/2017/10/district-de-djambala.html",
                "credit": "Chemin de Développement Personnel Congo",
                "caption": "Boulevard principal de Djambala sobre la meseta",
            },
            {
                "img": "https://2.bp.blogspot.com/-BVbO2XZkyDc/W-PooWeVSQI/AAAAAAAAAOI/8EPNpURngqIPfX8T7WwpY0BuzlYIqxVLQCEwYBhgL/s1600/Djambala.jpg",
                "source": "https://cdpcongo.blogspot.com/2017/10/district-de-djambala.html",
                "credit": "Chemin de Développement Personnel Congo",
                "caption": "Edificio administrativo y rotonda de Djambala",
            },
            commons("Exploration axe P20 Ngo Djambala (2).jpg", "Vainqueur.2 · CC BY-SA 4.0", "Sabana y carretera P20 en el eje de Djambala"),
        ],
        18: [
            {
                "img": "https://pbs.twimg.com/media/D_BBxWbX4AANCKa.jpg",
                "source": "https://x.com/Kikilawanda/status/1148490255550619648",
                "credit": "Kikilawanda",
                "caption": "Esfera armilar del Monumento del Ecuador en Makoua",
            },
            {
                "img": "https://cdn.travelpal.ai/prod/places/-XeJAWu68rJ7jVBylj2X-HVXXtV/photos/google/webp/d319dab4f6301c5826522d18.webp",
                "source": "https://www.travelpal.ai/place/equator-monument-2",
                "credit": "Google / TravelPal",
                "caption": "El Monumento del Ecuador y su entorno inmediato junto a la carretera",
            },
            commons("Makoua (Republic of the Congo) - Former bell tower.JPG", "Bsm15 · CC BY-SA 3.0", "Antigua torre de Makoua, referencia urbana secundaria"),
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
    "congo": {
        "https://upr-info.org/sites/default/files/country-document/2024-03/A_HRC_WG.45_COG_1_E.pdf",
        "https://www.wcscongoblog.org/wp-content/uploads/2016/02/brochure-Guide-to-Nouabale-Ndoki.pdf",
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
    "congo": {
        "https://commons.wikimedia.org/wiki/File:Navigating%20through%20the%20Black%20Forest%2C%20Nouabal%C3%A9-Ndoki%20National%20Park.jpg",
        "https://commons.wikimedia.org/wiki/File:Flooded%20rainforest%20in%20the%20Black%20Forest%2C%20Nouabal%C3%A9-Ndoki%20National%20Park.jpg",
        "https://commons.wikimedia.org/wiki/File:Wikim%C3%A9dia_R%C3%A9publique_du_Congo_-_Pointe_Noire._02.jpg",
        "https://commons.wikimedia.org/wiki/File:Travailleurs_sur_le_chantier_du_chemin_de_fer_Congo-Oc%C3%A9an,_dans_la_colonie_fran%C3%A7aise_du_Moyen-Congo,_vers_1923.png",
    },
}


PHOTO_LEADS: dict[str, dict[int, str]] = {
    "gabon": {
        13: "https://static1.evcdn.net/images/reduction/279557_w-1600_h-1200_q-70_m-crop.jpg",
        18: "https://img.rts.ch/articles/2023/image/u36r77-26153018.image?h=720&w=1280",
    },
}

SYNC_PRIMARY_PHOTO = {"gabon", "congo"}


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

# -*- coding: utf-8 -*-
"""All-Africa country index for the Africa 2027 site.

Every entry that is not 'completa' is a DRAFT: quick orientation data to be
verified one by one. Fields: (slug, name, group, order, seguridad, frontera,
visado, cpd, perro, nota)
groups: bajada | bucle | subida | alternativa | vuelo | excluido | fuera

Ruta global confirmada (ver documento "Ruta global 2027" del proyecto):
ida y vuelta por la costa oeste (bajada), con un bucle de exploración fuerte
en el sur/este (bucle) entre Angola y Angola. Kenia es el punto más oriental
del viaje entero — no se llega a Etiopía, Sudán ni Egipto.
"""

C = [
 # --- Corredor fijo de bajada (oeste) — varios tramos se recorren también a
 # la subida, con corredor distinto donde tiene sentido (ver notas de cada
 # ficha, no aquí) ---
 ("marruecos","Marruecos","bajada",1,"estable · precaución normal","Abierta: entrada desde España por ferry (Algeciras/Tarifa–Tánger Med) con vehículos en el mismo barco","Exención de visado 90 días para españoles","No exige CPD: admisión temporal (D16ter) en frontera","Entrada con certificado sanitario y antirrábica; sin cuarentena publicada","De paso, ida y vuelta, ruta más rápida hasta la frontera de Mauritania — sin ninguna parada por decisión del proyecto"),
 ("sahara-occidental","Sahara Occidental (tránsito)","bajada",2,"precaución · zona bajo administración marroquí en el corredor costero","Tránsito por la carretera costera hasta Guerguerat; no salir del corredor","Cubierto por la entrada marroquí","Cubierto por la admisión temporal marroquí","Sin controles adicionales publicados","Territorio no autónomo; franja este minada — jamás abandonar la carretera; de paso ambas veces"),
 ("mauritania","Mauritania","bajada",3,"","","","","","Ruta ya establecida; mismo corredor previsto a la vuelta"),
 ("senegal","Senegal","bajada",4,"","","","","","Bajada por el Ferlo; SUBIDA distinta: entrada por el suroeste (Casamance), cruce a Gambia, subida a Dakar y Lac Rose"),
 ("guinea","Guinea","bajada",5,"precaución · situación política a vigilar","Entrada por Sambaïlo/Koundara desde Senegal (corredor base del proyecto)","Visado/eVisa previo para españoles","CPD recomendado; laissez-passer en frontera como alternativa","Requisitos veterinarios sin instrucción clara publicada — confirmar por escrito","Bajada directa hacia Costa de Marfil (sin pasar por Sierra Leona ni Liberia); corredor de subida distinto por confirmar. Fouta Djalon como interés principal"),
 ("costa-de-marfil","Costa de Marfil","bajada",6,"estable en el sur · precaución en el norte","Frontera con Guinea (Nzérékoré–Danané) o histórica con Liberia (Prollo/Tabou, ya no usada)","eVisa disponible (verificar para entrada terrestre)","CPD o laissez-passer; Carte Brune CEDEAO válida","Certificado veterinario + antirrábica","Con paradas variadas; corredor doble bajada/subida. Yamusukro, Grand-Bassam; buen estado general de carreteras principales"),
 ("ghana","Ghana","bajada",7,"estable · precaución normal","Frontera con Costa de Marfil (Elubo) muy transitada","Visado previo para españoles","CPD no obligatorio: importación temporal en frontera","Permiso de importación veterinario recomendado","Con paradas variadas; corredor doble. Costa de los fuertes, Cape Coast; anglófono"),
 ("togo","Togo","bajada",8,"estable en costa · precaución en el norte","Frontera con Ghana (Aflao) en la propia Lomé","eVisa o visa on arrival — verificar","CPD o laissez-passer; Carte Brune válida","Certificado veterinario","De paso, sin entretenerse, ambas veces (1-2 días)"),
 ("benin","Benín","bajada",9,"estable en costa · riesgo en el extremo norte (parques W/Pendjari)","Frontera con Togo (Hilla-Condji) operativa","eVisa disponible","CPD o laissez-passer; Carte Brune válida","Certificado veterinario","De paso, sin entretenerse, ambas veces; Ganvié como posible parada única"),
 ("nigeria","Nigeria","bajada",10,"riesgo alto en varias zonas · corredor costero Lagos–Benin City con precaución máxima","Frontera Seme (Benín) operativa; trámites lentos","Visado previo — trámite exigente; verificar opciones de tránsito","CPD exigido en la práctica en fronteras terrestres — imprescindible","Certificado veterinario + antirrábica","De paso por riesgo, lo más rápido posible por el sur, ambas veces — no entretenerse"),
 ("camerun","Camerún","bajada",11,"precaución · evitar Extremo Norte y regiones anglófonas NW/SW","Frontera Ekok/Mfum arriesgada (zona anglófona): valorar entrada por el norte de Ikom→Mamfé solo con validación, o corredor alternativo","Visado previo para españoles","CPD recomendado; laissez-passer posible","Certificado veterinario","De paso por riesgo regional, ambas veces; evitar NW/SW, corredor Douala–Yaundé"),
 ("congo","Congo (Brazzaville)","bajada",12,"estable · precaución en Pool","Frontera con Camerún (Ntam–Ouesso) si el cruce directo es viable; si no, tránsito por Gabón (Ndendé–Dolisie)","Visado previo","CPD recomendado","Certificado veterinario","BAJADA: parada específica para gorilas en el Parque Nacional de Odzala-Kokoua (expedición 4x4, ~16h de pista desde Brazzaville — asumida como parte del viaje). SUBIDA: de paso, sin parada"),
 ("rd-congo","RD Congo (tránsito Matadi)","bajada",13,"conflicto activo en el ESTE (lejos de la ruta) · tránsito oeste Matadi–Lufu con precaución","Cruce Brazzaville–Kinshasa en ferry o entrada por Luvo/Matadi hacia Angola","Visado previo — trámite exigente","CPD recomendado; controles frecuentes","Certificado veterinario","Solo tránsito corto oeste (Kinshasa–Matadi–frontera Angola), ambas veces, lo más rápido posible; el este del país queda a 2000 km de la ruta"),
 ("angola","Angola","bajada",14,"estable · precaución normal","Frontera Luvo (RDC) y Santa Clara (Namibia) operativas; Cabinda requiere tránsito por RDC","Exención de visado de turismo (30 días) para españoles — verificar vigencia","CPD recomendado — verificar; importación temporal posible","Certificado veterinario + antirrábica","PUERTA del bloque sur: corredor de ENTRADA (frontera RDC → zona de exploración) y corredor de SALIDA (frontera Namibia → frontera RDC) distintos. Hoy la ficha solo cubre la costa — ampliación prioritaria. Sierra de la Leba, Tundavala, desierto del Namibe"),
 # --- Bucle de exploración sur/este — cada país se cruza una sola vez salvo
 # aviso; es el bloque donde el viaje se toma con más calma ---
 ("zambia","Zambia","bucle",20,"estable","Fronteras Kazungula/Chirundu operativas","eVisa/visa on arrival — verificar","CPD recomendado — verificar","Permiso de importación veterinario","Enlace Angola→Tanzania, una sola vez; investigar a fondo (ficha borrador)"),
 ("tanzania","Tanzania","bucle",21,"estable · precaución normal","Frontera Songwe (Zambia/Malaui) y Namanga/Taveta (Kenia) operativas","eVisa disponible","CPD exigido en la práctica en frontera terrestre — imprescindible","Permiso de importación veterinario","Corredor doble: se cruza yendo hacia Kenia y volviendo desde Kenia, por rutas distintas. Parques con perro prohibido; planificar cuidado o rotación"),
 ("kenia","Kenia","bucle",22,"precaución · evitar zonas fronterizas con Somalia","Frontera Namanga/Taveta operativa","eTA obligatoria (autorización electrónica)","CPD exigido en la práctica — imprescindible","Permiso de importación veterinario previo","PUNTO MÁS ORIENTAL de todo el viaje. Corredor doble: entrada y salida por rutas distintas dentro del país. Base logística grande en Nairobi; parques con perro prohibido"),
 ("mozambique","Mozambique","bucle",23,"precaución · evitar Cabo Delgado norte","Fronteras con Tanzania (Unity Bridge/Ruvuma), Esuatini y Sudáfrica (Lebombo) operativas","Exención de visado corta para turismo — verificar","CPD no obligatorio: permiso temporal en frontera","Certificado veterinario + permiso de importación","Una sola vez, tramo del bucle hacia Zimbabue; buscar tramos costeros 4x4 en el norte"),
 ("zimbabue","Zimbabue","bucle",24,"estable · precaución económica","Beitbridge (Sudáfrica) congestionada; Plumtree/Vic Falls alternativas","Visa on arrival — verificar","CPD recomendado — verificar","Permiso de importación veterinario","Pasa de alternativa a ruta fija del bucle. Cataratas Victoria"),
 ("botsuana","Botsuana","bucle",25,"estable","Fronteras con Sudáfrica/Namibia/Zimbabue ágiles","Exención de visado — verificar","Permiso temporal en frontera","Permiso de importación veterinario","Pasa de alternativa a ruta fija del bucle. Travesía del Makgadikgadi y Kalahari central como tramos 4x4 destacados; parques con perro prohibido — investigar alternativas"),
 ("sudafrica","Sudáfrica","bucle",26,"estable · precaución urbana","Fronteras con Namibia (Vioolsdrif) y con Botsuana/Zimbabue/Mozambique/Esuatini/Lesoto operativas 24h","Exención de visado 90 días para españoles","CPD no obligatorio para turismo — verificar según aduana","Permiso de importación veterinario previo obligatorio","PUNTO MÁS AL SUR de todo el viaje. Corredor doble: entrada por el centro/este, salida por el oeste hacia Namibia. Mantenimiento a fondo de los vehículos"),
 ("namibia","Namibia","bucle",27,"estable","Frontera Santa Clara–Oshikango (Angola) y Vioolsdrif (Sudáfrica) operativas y ágiles","Visado a la llegada para españoles desde abril 2025 — verificar","CPD no obligatorio: permiso temporal en frontera (CBC)","Permiso de importación veterinario previo — tramitar con antelación","Cierre del bucle hacia Angola. Priorizar tramos 4x4 míticos: Skeleton Coast, dunas de Sandwich Harbour, Kaokoland/Van Zyl's Pass. Etosha con perro prohibido — investigar alternativas"),
 # --- Solo en la subida (no forman parte de la bajada) ---
 ("gambia","Gambia","subida",30,"estable","Cruces Karang–Amdalai y Keur Ayib–Farafenni","Exención — verificar","Permiso temporal en frontera","Certificado veterinario","Fijo en la SUBIDA final: suroeste de Senegal → Gambia → Dakar → Lac Rose. No forma parte de la bajada"),
 # --- Alternativas / opcionales: con tiempo, ganas y (en varios casos)
 # visado resuelto para frontera terrestre ---
 ("sierra-leona","Sierra Leona","alternativa",40,"estable · precaución normal","Frontera con Guinea (Pamelap) operativa en general","Visado o visa on arrival — verificar","CPD no imprescindible: permiso temporal en frontera","Certificado veterinario + antirrábica; confirmar en frontera","Fuera de la bajada (se va directo Guinea→Costa de Marfil); posible SOLO en la subida, si hay tiempo y ganas. Playas de la península de Freetown"),
 ("liberia","Liberia","alternativa",41,"estable · precaución normal","Frontera con Sierra Leona (Bo Waterside) operativa","Visado previo — el nuevo e-visa a la llegada (marzo 2025) es SOLO para el aeropuerto Roberts, no vale en frontera terrestre; hace falta visado tradicional en embajada (España no tiene embajada de Liberia)","CPD no exigido de forma general; permiso temporal","Confirmar requisitos veterinarios","Excluida de la ruta fija por el problema de visado en frontera terrestre. Se mantiene la ficha con su información por si en el futuro compensa gestionarlo"),
 ("gabon","Gabón","alternativa",42,"estable · precaución normal","Frontera con Camerún (Ambam–Bitam o Ntam) operativa","El eVisa oficial es SOLO para llegada aérea por Libreville — no vale en frontera terrestre ni marítima; para entrar por carretera hace falta visado tradicional en consulado, gestionado con antelación","CPD recomendado — verificar exigencia real","Certificado veterinario","No se hará por ahora (decisión del proyecto); se mantiene la ficha con su información. Selva ecuatorial; Lopé"),
 ("malaui","Malaui","alternativa",43,"estable","Fronteras Zóbuè/Dedza (Mozambique) y Songwe (Tanzania) operativas","Visado/eVisa — verificar exención","CPD recomendado — verificar","Permiso de importación veterinario","Alternativa dentro del bucle (enlace Zambia–Tanzania o Tanzania–Mozambique) si hay tiempo. Lago Malaui como eje del tramo"),
 ("uganda","Uganda","alternativa",44,"estable · precaución normal","Fronteras con Kenia (Malaba/Busia) operativas","eVisa disponible — verificar validez en frontera terrestre","CPD exigido en la práctica — verificar","Permiso de importación veterinario","Solo si se desvía hacia los Grandes Lagos con tiempo y visado resuelto en frontera terrestre"),
 ("ruanda","Ruanda","alternativa",45,"estable","Fronteras con Uganda/Tanzania operativas","Exención/visa on arrival — verificar validez en frontera terrestre","CPD recomendado — verificar","Permiso de importación veterinario","Solo en variante de Grandes Lagos, con tiempo y visado resuelto en frontera terrestre"),
 ("esuatini","Esuatini","alternativa",46,"estable","Fronteras con Sudáfrica/Mozambique operativas","Exención de visado — verificar","Permiso temporal sencillo","Certificado veterinario","Opcional en el bucle sur (enlace Sudáfrica–Mozambique) si hay tiempo"),
 ("lesoto","Lesoto","alternativa",47,"estable","Fronteras con Sudáfrica operativas","Exención de visado — verificar","Permiso temporal sencillo","Certificado veterinario","Opcional en el bucle sur si hay tiempo; Sani Pass como tramo de montaña 4x4"),
 # --- Solo alcanzable en avión: ficha propia para un posible viaje aparte,
 # no forma parte de la ruta overland con los vehículos ---
 ("madagascar","Madagascar","vuelo",50,"estable · precaución normal","Sin conexión terrestre ni ferry de pasajero+vehículo viable (solo transporte de carga comercial) — se llegaría en avión, dejando los 4x4 en el continente","eVisa","No aplica (no se lleva el vehículo)","Certificado veterinario si se lleva al perro en avión — trámite aparte","Posible escapada en avión si apetece durante el bucle sur/este; ficha propia para planificarlo aparte de la ruta 4x4"),
 # --- Excluidos por protocolo (conflicto activo) ---
 ("mali","Mali","excluido",90,"CONFLICTO ACTIVO — excluido totalmente por protocolo del proyecto","No utilizar ninguna frontera de Mali","—","—","—","Ninguna entrada, tránsito, desvío ni paso fronterizo; la localidad guineana llamada Mali se cita siempre como «Mali (localidad de Guinea)»"),
 ("guinea-bisau","Guinea-Bisáu","excluido",91,"inestabilidad política recurrente — fuera del itinerario por protocolo","No prevista","—","—","—","El corredor Senegal→Guinea (Kalifourou–Sambaïlo) la evita expresamente"),
 ("sudan","Sudán","excluido",92,"CONFLICTO ACTIVO (guerra civil desde 2023)","Fronteras no fiables mientras dure el conflicto","No planificable","No planificable","No planificable","Excluido por conflicto; en todo caso ya queda fuera de la ruta confirmada (el viaje no pasa de Kenia hacia el Cuerno de África)"),
 # --- Fuera de la ruta prevista (la ruta confirmada no llega hasta aquí) ---
 ("argelia","Argelia","fuera",100,"precaución · permisos y escolta en el sur","Frontera con Marruecos CERRADA desde 1994","Visado previo exigente","CPD no aplicable a esta ruta","—","Sin conexión útil con el corredor previsto"),
 ("tunez","Túnez","fuera",101,"estable · precaución normal","Sin conexión con el corredor (Argelia cerrada, Libia inviable)","Exención 90 días","—","—","Fuera de ruta"),
 ("libia","Libia","fuera",102,"CONFLICTO / inestabilidad grave","Fronteras no planificables","No planificable","—","—","Fuera de ruta"),
 ("burkina-faso","Burkina Faso","fuera",103,"CONFLICTO ACTIVO (insurgencia)","No prevista","—","—","—","Fuera de ruta; refuerza la exclusión de Mali"),
 ("niger","Níger","fuera",104,"riesgo alto / junta militar","No prevista","—","—","—","Fuera de ruta"),
 ("chad","Chad","fuera",105,"riesgo alto en varias zonas","No prevista","—","—","—","Fuera de ruta"),
 ("rca","República Centroafricana","fuera",106,"CONFLICTO ACTIVO","No prevista","—","—","—","Fuera de ruta"),
 ("sudan-del-sur","Sudán del Sur","fuera",107,"riesgo alto / inestabilidad","No prevista","—","—","—","Fuera de ruta"),
 ("somalia","Somalia","fuera",108,"CONFLICTO ACTIVO","No prevista","—","—","—","Fuera de ruta"),
 ("eritrea","Eritrea","fuera",109,"precaución · permisos internos restrictivos","Fronteras frecuentemente cerradas","Visado previo difícil","—","—","Fuera de ruta"),
 ("guinea-ecuatorial","Guinea Ecuatorial","fuera",110,"estable · precaución normal","Fronteras terrestres de apertura irregular","Visado previo (exención puntual a verificar)","—","—","Fuera de ruta; el corredor pasa por Camerún/Gabón"),
 ("santo-tome","Santo Tomé y Príncipe","fuera",111,"estable","Sin conexión terrestre (insular)","Exención — verificar","—","—","Insular; fuera de ruta"),
 ("cabo-verde","Cabo Verde","fuera",112,"estable","Sin conexión terrestre (insular)","Exención — verificar","—","—","Insular; fuera de ruta"),
 ("comoras","Comoras","fuera",113,"estable · precaución normal","Sin conexión terrestre (insular)","Visa on arrival","—","—","Insular; fuera de ruta"),
 ("seychelles","Seychelles","fuera",114,"estable","Sin conexión terrestre (insular)","Exención","—","—","Insular; fuera de ruta"),
 ("mauricio","Mauricio","fuera",115,"estable","Sin conexión terrestre (insular)","Exención","—","—","Insular; fuera de ruta"),
 ("burundi","Burundi","fuera",116,"precaución/riesgo","No prevista","Visado previo","—","—","Fuera de ruta"),
 ("etiopia","Etiopía","fuera",117,"precaución/riesgo según regiones (Amhara, Tigray, Oromía)","No prevista en la ruta confirmada","eVisa disponible","—","—","Fuera de la ruta confirmada: el viaje no pasa de Kenia hacia el Cuerno de África"),
 ("egipto","Egipto","fuera",118,"estable · precaución normal (evitar Sinaí norte)","Sin conexión terrestre útil con la ruta confirmada","Visado/eVisa disponible","—","—","Fuera de la ruta confirmada: el viaje no pasa de Kenia hacia el norte"),
 ("yibuti","Yibuti","fuera",119,"estable · precaución normal","Frontera con Etiopía (Galafi) operativa","eVisa disponible","—","—","Fuera de la ruta confirmada; ya no hace falta como puerto de salida al no plantearse el Cuerno de África"),
]

GROUP_LABELS = {
    "bajada": "Corredor fijo · bajada (y subida en varios países) · oeste",
    "bucle": "Bucle de exploración · sur y este",
    "subida": "Solo en la subida",
    "alternativa": "Alternativas y opcionales",
    "vuelo": "Solo alcanzable en avión",
    "excluido": "Excluidos por protocolo",
    "fuera": "Fuera de la ruta prevista",
}

# -*- coding: utf-8 -*-
"""All-Africa country index for the Africa 2027 site.

Every entry that is not 'completa' is a DRAFT: quick orientation data to be
verified one by one. Fields: (slug, name, group, order, seguridad, frontera,
visado, cpd, perro, nota)
groups: bajada | regreso | alternativa | excluido | fuera
"""

C = [
 # --- Corredor de bajada (oeste) ---
 ("marruecos","Marruecos","bajada",1,"estable · precaución normal","Abierta: entrada desde España por ferry (Algeciras/Tarifa–Tánger Med) con vehículos en el mismo barco","Exención de visado 90 días para españoles","No exige CPD: admisión temporal (D16ter) en frontera","Entrada con certificado sanitario y antirrábica; sin cuarentena publicada","Primer país del viaje; tránsito hacia el sur por El Aaiún–Dakhla"),
 ("sahara-occidental","Sahara Occidental (tránsito)","bajada",2,"precaución · zona bajo administración marroquí en el corredor costero","Tránsito por la carretera costera hasta Guerguerat; no salir del corredor","Cubierto por la entrada marroquí","Cubierto por la admisión temporal marroquí","Sin controles adicionales publicados","Territorio no autónomo; franja este minada — jamás abandonar la carretera"),
 ("mauritania","Mauritania","bajada",3,"","","","","",""),
 ("senegal","Senegal","bajada",4,"","","","","",""),
 ("guinea","Guinea","bajada",5,"precaución · situación política a vigilar","Entrada por Sambaïlo/Koundara desde Senegal (corredor base del proyecto)","Visado/eVisa previo para españoles","CPD recomendado; laissez-passer en frontera como alternativa","Requisitos veterinarios sin instrucción clara publicada — confirmar por escrito","Fouta Djalon como interés principal; carreteras interiores lentas"),
 ("sierra-leona","Sierra Leona","bajada",6,"estable · precaución normal","Frontera con Guinea (Pamelap) operativa en general","Visado o visa on arrival — verificar","CPD no imprescindible: permiso temporal en frontera","Certificado veterinario + antirrábica; confirmar en frontera","Playas de la península de Freetown; estación seca favorable en enero-febrero"),
 ("liberia","Liberia","bajada",7,"estable · precaución normal","Frontera con Sierra Leona (Bo Waterside) operativa","Visado previo para españoles — verificar","CPD no exigido de forma general; permiso temporal","Confirmar requisitos veterinarios","Tránsito relativamente rápido; carretera costera hacia Costa de Marfil"),
 ("costa-de-marfil","Costa de Marfil","bajada",8,"estable en el sur · precaución en el norte","Frontera con Liberia (Prollo/Tabou) o por Danané","eVisa disponible (verificar para entrada terrestre)","CPD o laissez-passer; Carte Brune CEDEAO válida","Certificado veterinario + antirrábica","Yamusukro, Grand-Bassam; buen estado general de carreteras principales"),
 ("ghana","Ghana","bajada",9,"estable · precaución normal","Frontera con Costa de Marfil (Elubo) muy transitada","Visado previo para españoles","CPD no obligatorio: importación temporal en frontera","Permiso de importación veterinario recomendado","Costa de los fuertes, Cape Coast; anglófono"),
 ("togo","Togo","bajada",10,"estable en costa · precaución en el norte","Frontera con Ghana (Aflao) en la propia Lomé","eVisa o visa on arrival — verificar","CPD o laissez-passer; Carte Brune válida","Certificado veterinario","Tránsito rápido previsto por el proyecto (1-2 días)"),
 ("benin","Benín","bajada",11,"estable en costa · riesgo en el extremo norte (parques W/Pendjari)","Frontera con Togo (Hilla-Condji) operativa","eVisa disponible","CPD o laissez-passer; Carte Brune válida","Certificado veterinario","Tránsito rápido; Ganvié como posible parada única"),
 ("nigeria","Nigeria","bajada",12,"riesgo alto en varias zonas · corredor costero Lagos–Benin City con precaución máxima","Frontera Seme (Benín) operativa; trámites lentos","Visado previo — trámite exigente; verificar opciones de tránsito","CPD exigido en la práctica en fronteras terrestres — imprescindible","Certificado veterinario + antirrábica","Tránsito lo más rápido posible por el sur según el protocolo del proyecto"),
 ("camerun","Camerún","bajada",13,"precaución · evitar Extremo Norte y regiones anglófonas NW/SW","Frontera Ekok/Mfum arriesgada (zona anglófona): valorar entrada por el norte de Ikom→Mamfé solo con validación, o corredor alternativo","Visado previo para españoles","CPD recomendado; laissez-passer posible","Certificado veterinario","Ruta interior por Bamenda desaconsejada; planificar por Douala/Yaundé"),
 ("gabon","Gabón","bajada",14,"estable · precaución normal","Frontera con Camerún (Ambam–Bitam) operativa","eVisa disponible","CPD recomendado — verificar exigencia real","Certificado veterinario","Selva ecuatorial; Lopé si el calendario lo permite"),
 ("congo","Congo (Brazzaville)","bajada",15,"estable · precaución en Pool","Frontera con Gabón (Ndendé–Dolisie) con pista variable","Visado previo","CPD recomendado","Certificado veterinario","Enlace hacia Pointe-Noire y el cruce a Cabinda/RDC"),
 ("rd-congo","RD Congo (tránsito Matadi)","bajada",16,"conflicto activo en el ESTE (lejos de la ruta) · tránsito oeste Matadi–Lufu con precaución","Cruce Brazzaville–Kinshasa en ferry o entrada por Luvo/Matadi hacia Angola","Visado previo — trámite exigente","CPD recomendado; controles frecuentes","Certificado veterinario","Solo tránsito corto oeste (Kinshasa–Matadi–frontera Angola); el este del país queda a 2000 km de la ruta"),
 ("angola","Angola","bajada",17,"estable · precaución normal","Frontera Luvo (RDC) y Santa Clara (Namibia) operativas; Cabinda requiere tránsito por RDC","Exención de visado de turismo (30 días) para españoles — verificar vigencia","CPD recomendado — verificar; importación temporal posible","Certificado veterinario + antirrábica","Sierra de la Leba, Tundavala, desierto del Namibe"),
 ("namibia","Namibia","bajada",18,"estable","Frontera Santa Clara–Oshikango operativa y ágil","Visado a la llegada para españoles desde abril 2025 — verificar","CPD no obligatorio: permiso temporal en frontera (CBC)","Permiso de importación veterinario previo — tramitar con antelación","Etosha (perro prohibido en parques), Skeleton Coast, Sossusvlei"),
 ("sudafrica","Sudáfrica","bajada",19,"estable · precaución urbana","Fronteras con Namibia (Vioolsdrif) operativas 24h","Exención de visado 90 días para españoles","CPD no obligatorio para turismo — verificar según aduana","Permiso de importación veterinario previo obligatorio","Punto de giro del viaje; mantenimiento a fondo de los vehículos"),
 # --- Corredor de regreso (este) ---
 ("mozambique","Mozambique","regreso",20,"precaución · evitar Cabo Delgado norte","Fronteras con Sudáfrica (Lebombo) y Esuatini operativas","Exención de visado corta para turismo — verificar","CPD no obligatorio: permiso temporal en frontera","Certificado veterinario + permiso de importación","Costa índica; tránsito hacia Malaui por Tete"),
 ("malaui","Malaui","regreso",21,"estable","Fronteras Zóbuè/Dedza operativas","Visado/eVisa — verificar exención","CPD recomendado — verificar","Permiso de importación veterinario","Lago Malaui como eje del tramo"),
 ("tanzania","Tanzania","regreso",22,"estable · precaución normal","Frontera Songwe (Malaui) operativa","eVisa disponible","CPD exigido en la práctica en frontera terrestre — imprescindible","Permiso de importación veterinario","Parques con perro prohibido; planificar cuidado o rotación"),
 ("kenia","Kenia","regreso",23,"precaución · evitar zonas fronterizas con Somalia","Frontera Namanga/Taveta operativa","eTA obligatoria (autorización electrónica)","CPD exigido en la práctica — imprescindible","Permiso de importación veterinario previo","Base logística grande en Nairobi; parques con perro prohibido"),
 ("etiopia","Etiopía","regreso",24,"precaución/riesgo según regiones (Amhara, Tigray, Oromía) — evaluación fina obligatoria","Frontera Moyale operativa; corredores internos a validar por regiones","eVisa disponible","CPD recomendado — verificar","Certificado veterinario","Norte histórico sujeto a seguridad; corredor hacia el norte depende de la decisión sobre Sudán"),
 ("sudan","Sudán","regreso",25,"CONFLICTO ACTIVO (guerra civil desde 2023) — corredor terrestre hacia Egipto bloqueado a efectos de planificación","Fronteras no fiables mientras dure el conflicto","No planificable","No planificable","No planificable","PUNTO CRÍTICO del corredor de regreso: sin Sudán, el enlace terrestre Etiopía→Egipto no existe; estudiar alternativas (RoRo/ferry desde Yibuti o Kenia, o replanteo del regreso)"),
 ("egipto","Egipto","regreso",26,"estable · precaución normal (evitar Sinaí norte)","Acceso terrestre desde el sur BLOQUEADO por la guerra de Sudán; estudiar llegada por mar (RoRo) o replanteo","Visado/eVisa disponible","CPD OBLIGATORIO con aval alto + trámites y matrícula egipcia temporal — el país más exigente del viaje en aduanas","Certificado veterinario + permisos","Desde Egipto: ferris/RoRo hacia Europa o Turquía a investigar (prioridad: viajeros y vehículos en el mismo barco)"),
 # --- Alternativas / opcionales ---
 ("gambia","Gambia","alternativa",30,"estable","Cruces Karang–Amdalai y Keur Ayib–Farafenni solo como alternativa (protocolo)","Exención — verificar","Permiso temporal en frontera","Certificado veterinario","Fuera del corredor base de Senegal; solo si obliga la logística"),
 ("lesoto","Lesoto","alternativa",31,"estable","Fronteras con Sudáfrica operativas","Exención de visado — verificar","Permiso temporal sencillo","Certificado veterinario","Opcional: montañas de Sani Pass si el calendario lo permite"),
 ("esuatini","Esuatini","alternativa",32,"estable","Fronteras con Sudáfrica/Mozambique operativas","Exención de visado — verificar","Permiso temporal sencillo","Certificado veterinario","Opcional en el enlace Sudáfrica→Mozambique"),
 ("zimbabue","Zimbabue","alternativa",33,"estable · precaución económica","Beitbridge (Sudáfrica) congestionada; Plumtree/Vic Falls alternativas","Visa on arrival — verificar","CPD recomendado — verificar","Permiso de importación veterinario","Alternativa interior con Cataratas Victoria si se ajusta el regreso"),
 ("botsuana","Botsuana","alternativa",34,"estable","Fronteras con Sudáfrica/Namibia ágiles","Exención de visado — verificar","Permiso temporal en frontera","Permiso de importación veterinario","Alternativa: Kalahari/Chobe; parques con perro prohibido"),
 ("zambia","Zambia","alternativa",35,"estable","Fronteras Kazungula/Chirundu operativas","eVisa/visa on arrival — verificar","CPD recomendado — verificar","Permiso de importación veterinario","Alternativa de enlace hacia Malaui/Tanzania"),
 ("uganda","Uganda","alternativa",36,"estable · precaución normal","Fronteras con Kenia (Malaba/Busia) operativas","eVisa disponible","CPD exigido en la práctica — verificar","Permiso de importación veterinario","Solo si el regreso se desvía hacia los Grandes Lagos"),
 ("ruanda","Ruanda","alternativa",37,"estable","Fronteras con Uganda/Tanzania operativas","Exención/visa on arrival — verificar","CPD recomendado — verificar","Permiso de importación veterinario","Solo en variante de Grandes Lagos"),
 ("yibuti","Yibuti","alternativa",38,"estable · precaución normal","Frontera con Etiopía (Galafi) operativa","eVisa disponible","CPD recomendado — verificar","Certificado veterinario","Posible puerto de salida RoRo si Sudán sigue bloqueado — investigar rutas marítimas"),
 # --- Excluidos por protocolo ---
 ("mali","Mali","excluido",90,"CONFLICTO ACTIVO — excluido totalmente por protocolo del proyecto","No utilizar ninguna frontera de Mali","—","—","—","Ninguna entrada, tránsito, desvío ni paso fronterizo; la localidad guineana llamada Mali se cita siempre como «Mali (localidad de Guinea)»"),
 ("guinea-bisau","Guinea-Bisáu","excluido",91,"inestabilidad política recurrente — fuera del itinerario por protocolo","No prevista","—","—","—","El corredor Senegal→Guinea (Kalifourou–Sambaïlo) la evita expresamente"),
 # --- Fuera de la ruta prevista ---
 ("argelia","Argelia","fuera",100,"precaución · permisos y escolta en el sur","Frontera con Marruecos CERRADA desde 1994","Visado previo exigente","CPD no aplicable a esta ruta","—","Sin conexión útil con el corredor previsto"),
 ("tunez","Túnez","fuera",101,"estable · precaución normal","Sin conexión con el corredor (Argelia cerrada, Libia inviable)","Exención 90 días","—","—","Fuera de ruta"),
 ("libia","Libia","fuera",102,"CONFLICTO / inestabilidad grave","Fronteras no planificables","No planificable","—","—","Descartada como alternativa de regreso por el norte"),
 ("burkina-faso","Burkina Faso","fuera",103,"CONFLICTO ACTIVO (insurgencia)","No prevista","—","—","—","Fuera de ruta; refuerza la exclusión de Mali"),
 ("niger","Níger","fuera",104,"riesgo alto / junta militar","No prevista","—","—","—","Fuera de ruta"),
 ("chad","Chad","fuera",105,"riesgo alto en varias zonas","No prevista","—","—","—","Fuera de ruta"),
 ("rca","República Centroafricana","fuera",106,"CONFLICTO ACTIVO","No prevista","—","—","—","Fuera de ruta"),
 ("sudan-del-sur","Sudán del Sur","fuera",107,"riesgo alto / inestabilidad","No prevista","—","—","—","Fuera de ruta"),
 ("somalia","Somalia","fuera",108,"CONFLICTO ACTIVO","No prevista","—","—","—","Fuera de ruta"),
 ("eritrea","Eritrea","fuera",109,"precaución · permisos internos restrictivos","Fronteras frecuentemente cerradas","Visado previo difícil","—","—","Fuera de ruta"),
 ("guinea-ecuatorial","Guinea Ecuatorial","fuera",110,"estable · precaución normal","Fronteras terrestres de apertura irregular","Visado previo (exención puntual a verificar)","—","—","Fuera de ruta; el corredor pasa por Gabón"),
 ("santo-tome","Santo Tomé y Príncipe","fuera",111,"estable","Sin conexión terrestre (insular)","Exención — verificar","—","—","Insular; fuera de ruta"),
 ("cabo-verde","Cabo Verde","fuera",112,"estable","Sin conexión terrestre (insular)","Exención — verificar","—","—","Insular; fuera de ruta"),
 ("comoras","Comoras","fuera",113,"estable · precaución normal","Sin conexión terrestre (insular)","Visa on arrival","—","—","Insular; fuera de ruta"),
 ("seychelles","Seychelles","fuera",114,"estable","Sin conexión terrestre (insular)","Exención","—","—","Insular; fuera de ruta"),
 ("mauricio","Mauricio","fuera",115,"estable","Sin conexión terrestre (insular)","Exención","—","—","Insular; fuera de ruta"),
 ("madagascar","Madagascar","fuera",116,"estable · precaución normal","Sin conexión terrestre (insular)","eVisa","—","—","Insular; fuera de ruta"),
 ("burundi","Burundi","fuera",117,"precaución/riesgo","No prevista","Visado previo","—","—","Fuera de ruta"),
]

GROUP_LABELS = {
    "bajada": "Corredor de bajada · África occidental",
    "regreso": "Corredor de regreso · África oriental",
    "alternativa": "Alternativas y opcionales",
    "excluido": "Excluidos por protocolo",
    "fuera": "Fuera de la ruta prevista",
}

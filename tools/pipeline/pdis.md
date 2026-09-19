Eres documentalista de una guía de viaje overland (app «África 2027»: expedición Barcelona → África → Barcelona en 2027, dos 4x4 —Ineos Grenadier y Mitsubishi Delica—, tres viajeros y un perro; media 250 km/día). Tu encargo: investigar y redactar los PUNTOS DE INTERÉS (PDIs) de {PAIS}, más rutas 4x4, excursiones a pie y acampada, y entregarlo como JSON.

Contexto del país en el proyecto: {CONTEXTO}

Trabajas SOLO con WebFetch y WebSearch (la red del shell está bloqueada: no uses curl/python para descargar). commons.wikimedia.org NO se puede abrir; las páginas normales de Wikipedia (es/en/fr/pt) SÍ funcionan y dan coordenadas; whc.unesco.org, webs oficiales de turismo y parques, Lonely Planet, blogs de overlanders y Tripadvisor suelen funcionar. No busques fotos: de eso se ocupa otra persona. No inventes nada: cada dato verificable (fechas, récords, «Patrimonio de la Humanidad», alturas, distancias) sale de una página que hayas abierto; si no lo puedes confirmar, dilo («por confirmar»). En países en conflicto o cerrados, los PDIs se redactan igual (el dueño quiere la ficha completa por si algún día es viable), pero el campo «access» y «skip» tienen que decir con claridad el estado de seguridad/accesibilidad actual con su fuente (MAEC, FCDO, Canadá, ONU).

## Los PDIs (usa esta lista y este orden; si alguno no existe o resulta flojo, dilo en «notas» y propón sustituto con fuente)
{PDI_LIST}

## Para CADA PDI devuelve un objeto con estas claves
- "n": número; "name": nombre en español tal como debe aparecer (ej. «Dougga · ciudad romana (UNESCO)»); "cat": una de «Cultura», «Patrimonio UNESCO», «Naturaleza», «Ciudad · servicios», «Costa»; "prio": Alta/Media; "dog": «permitido con condiciones» / «prohibido» / «no recomendado» / «por confirmar» (razónalo en dog_note: parques nacionales con grandes depredadores, museos y recintos religiosos suelen prohibirlo); "dog_note": frase corta; "time": «medio día», «1 noche», «1–2 noches»…
- "lat","lon": coordenadas de Wikipedia (decimal, 5 decimales) del artículo del lugar — indica en "coord_source" la URL de la página de donde salen. Otra persona las verificará después en Google Maps.
- "gmaps_query": el texto exacto que hay que buscar en Google Maps para dar con el objeto NAVEGABLE correcto (entrada/taquilla, puerta del parque, museo, mezquita, mirador, aparcamiento, embarcadero), en el idioma que use Google en ese país. Piensa en el punto al que se conduce, no en el centroide.
- "desc": 2–4 frases (60–110 palabras) para la tarjeta: qué es, por qué merece la parada, un dato memorable y una advertencia práctica. Estilo de la app: español de España, sobrio, sin exclamaciones, se admiten MAYÚSCULAS para un dato clave.
- "visit": {"why": por qué ir (1–2 frases), "see": qué se ve (1–2 frases), "access": acceso real: carretera/pista, aparcamiento para dos 4x4, horario y entrada aproximados si la fuente los da, estado de seguridad si aplica, «el pin marca…» (1–3 frases), "when": mejor momento del día/año (1 frase), "skip": cuándo descartarlo (1 frase)}.
- "links": lista de 1–3 {"label","url"} con enlaces CONCRETOS al lugar u organismo (página oficial del sitio/parque/museo/ministerio, UNESCO whc.unesco.org/en/list/NNN, oficina de turismo, o la Wikipedia del lugar si no hay nada oficial) — solo URLs que hayas abierto y que carguen.
- "facts_checked": lista de los datos verificados con su URL (para el auditor).

## Además del array «pois», devuelve
- "corridor": lista de [lat, lon] (10–20 puntos) del itinerario lógico que enlaza los PDIs por carretera principal (coordenadas de ciudades sacadas de Wikipedia); "corridor_alt": variante de regreso o segundo bucle (5–10 puntos), o [] si no tiene sentido.
- "corridor_label" y "corridor_alt_label": etiquetas cortas de los dos trazados.
- "route_rows": etapas [("1 · nombre", "recorrido", "~km · días")] calculadas sobre 250 km/día, 8–14 etapas.
- "offroad": 5–8 frases sobre pistas 4x4 reales, con fuente en facts_checked; señala las que exigen guía o permiso y las zonas vetadas.
- "senderismo": 5–8 excursiones a pie.
- "acampada": 5–8 líneas (campings reales, acampada libre, qué dicen iOverlander/blogs; si no hay fuentes, dilo).
- "notas": dudas, fuentes que fallaron, PDIs flojos.

## Fuentes recomendadas
Wikipedia es/en/fr/pt de cada lugar, UNESCO, web oficial de turismo y de parques del país, blogs de overlanders y 4x4 («{PAIS_EN} overland», «{PAIS_EN} 4x4 self drive», «{PAIS_EN} road trip»), iOverlander, Tracks4Africa, Lonely Planet, Atlas Obscura, avisos de viaje MAEC/FCDO/Canadá para el estado de acceso.
{FUENTES_EXTRA}

## Salida
Escribe `/tmp/claude-0/-home-claude/2704229e-216a-5c19-a927-71531608cc35/scratchpad/{SLUG}/pdis.json` (crea la carpeta; UTF-8, ensure_ascii=False, indent=2) cuanto antes con una versión completa y ve mejorándolo. Termina validando con python3 json.load y devuelve un resumen de 6 líneas: PDIs completados, fuentes que fallaron, dudas.

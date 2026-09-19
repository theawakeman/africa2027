Eres documentalista de una guía de viaje overland (app «África 2027»: expedición Barcelona → África → Barcelona en 2027, dos 4x4 matriculados en España —Ineos Grenadier y Mitsubishi Delica—, tres viajeros españoles y un perro; media 250 km/día). Tu encargo: investigar y redactar las SECCIONES OPERATIVAS de la ficha de {PAIS} y entregarlas como JSON.

Contexto del país en el proyecto: {CONTEXTO}

Trabajas SOLO con WebFetch y WebSearch (la red del shell está bloqueada; no uses curl/python para descargar). Las páginas de Wikipedia funcionan; los PDF y las recomendaciones de viaje del MAEC (exteriores.gob.es) también; Freedom House, FCDO (gov.uk), Canadá (travel.gc.ca), TravelHealthPro, EUR-Lex, MAPA, OFESAUTO y carnetdepassage.org suelen funcionar. No inventes nada: cada dato sale de una página abierta en esta sesión; si no lo puedes confirmar, escribe «por confirmar» y añádelo a «pendientes» con criterio de cierre. Estilo de la app: español de España, sobrio, directo; en burocracia (visados, permisos, plazos) MUY conciso; se admiten MAYÚSCULAS para el dato clave; nunca dejar nada «entendido» en el aire: si no se sabe, se dice.

## Fuentes obligatorias a intentar
- MAEC · Recomendaciones de viaje: https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc={MAEC_TRC} (zonas desaconsejadas, entrada, sanidad, drones si lo cita) y la Ficha País PDF: https://www.exteriores.gob.es/Documents/FichasPais/{MAEC_PDF}_FICHA%20PAIS.pdf
- Embajada de España competente (dirección, teléfono, emergencia consular): {EMBAJADA_HINT}
- Cómo se llega y con qué vehículo: {ACCESO_HINT}
- Aduana y vehículo: CPD/carnet de passages (carnetdepassage.org/country/<pais>, RACE, relatos de overlanders 2023–2026), admisión temporal, seguro obligatorio (OFESAUTO Carta Verde; seguro regional Carte Brune CEDEAO / Carte Rose CEMAC / COMESA Yellow Card si aplica), lado de conducción, carné internacional.
- Fronteras terrestres: estado 2025/26 de cada paso relevante (abiertos/cerrados a extranjeros) con fuente y fecha.
- Drones: normativa (autoridad de aviación civil, prohibición, confiscación) con fuente oficial o de embajadas + testimonios.
- Starlink: disponibilidad a fecha de 2026 (mapa de starlink.com, noticias 2025-2026); operadores móviles y SIM turística.
- Perro: requisitos de entrada (organismo veterinario oficial NACIONAL con su web, certificado, rabia, microchip, permiso previo, razas prohibidas) — busca la página oficial nacional (ministerio de agricultura/ganadería, servicios veterinarios, aduana, portal de trámites); si no se abre, dilo. Vuelta a la UE: régimen del Reg. Delegado (UE) 2026/131 y lista de terceros países del Reg. de Ejecución 2026/636 (la lista de 2026 no contiene países africanos continentales; comprueba si este país es una excepción insular) → titulación antirrábica anotada en el pasaporte antes de salir (vía A). Cita EUR-Lex/DG SANTE/MAPA.
- Salud: MAEC, TravelHealthPro/Sanidad Exterior (vacunas obligatorias —fiebre amarilla—, malaria, agua, sanidad privada), hospitales de referencia.
- Seguridad: MAEC, FCDO, Canadá (zonas vetadas, conflicto, terrorismo, secuestro, permisos, escoltas).
- Agua de uso general (llenar depósitos para ducha/lavado) y combustible (precio 2026, red, calidad, disponibilidad, racionamiento): blogs de autocaravanistas/overlanders, iOverlander, GlobalPetrolPrices.
- Experiencias de otros overlanders 2019-2026 (blogs, foros, Overland Bound, iOverlander, Tracks4Africa): 6–10 relatos con lo que aporta cada uno; si no hay relatos recientes por el conflicto, dilo y usa los últimos disponibles con su fecha.

## Salida
Escribe `/tmp/claude-0/-home-claude/2704229e-216a-5c19-a927-71531608cc35/scratchpad/{SLUG}/operativo.json` (crea la carpeta; UTF-8, ensure_ascii=False, indent=2) con estas claves (todas listas de strings salvo donde se indique; frases completas, 1–3 líneas cada una):
- "sub": subtítulo de la ficha (una línea, estilo «FUERA DE RUTA — solo alcanzable en ferry desde Italia/Francia · Sáhara, ruinas romanas y medinas» o «EXCLUIDO POR PROTOCOLO — conflicto activo · ficha informativa»).
- "decision": párrafo (150–250 palabras) sobre por qué está fuera de la ruta/excluido/solo en avión, cómo se podría hacer aparte si algún día es viable, coste orientativo y qué haría falta decidir.
- "facts": lista de [tema, estado] (10–12 filas: Estatus, Cómo llegar, Visado, Vehículo/aduana, Seguro, Moneda, Perro, Drones, Starlink, Seguridad, Clima, Sanidad).
- "alerts": 8–10 alertas que condicionan la visita.
- "visado": 4–6 puntos (españoles: modalidad, plazos, coste, dónde; validez en frontera terrestre).
- "fronteras_rows": lista de [función, paso, comprobación operativa] (puertos/aeropuertos/pasos terrestres relevantes con estado y fuente).
- "vehiculos": 6–8 puntos.
- "drones_callout": [tipo («danger»/«warn»/«»), título, cuerpo (60–100 palabras)] y "drones": 4–5 puntos.
- "starlink_callout": [tipo, título, cuerpo] y "starlink": 3–5 puntos.
- "perro_intro": 5–7 puntos (entrada con fuente oficial si existe, razas, vuelta a la UE, veterinarios, riesgos) y "dog_matrix": 5–6 [zona, estado («permitido con condiciones»/«prohibido»/«por confirmar»/«no recomendado»), plan B].
- "perro_contacto": objeto {"organismo", "url" (página OFICIAL NACIONAL del organismo veterinario o del portal de trámites; null si no hay), "url_verificada" (true si la abriste), "url_generica" (true si solo es la portada), "email", "tel", "cert" (true/false/null), "cert_dias" (número o null), "cert_quien", "nota" (3–5 frases con lo que se sabe y lo que no), "fuentes": [urls]} — para alimentar el dosier del perro del proyecto.
- "salud": 5–7 puntos.
- "seguridad_intro": párrafo (60–100 palabras) y "seguridad": 7–9 puntos.
- "agua": 4–6 puntos y "combustible": 4–6 puntos, con precios datados si los hay.
- "experiencias_intro": 1–2 frases y "experiencias": 6–10 relatos con formato «Titular: cuerpo del relato» (cada uno 40–80 palabras, con la fuente/blog y año citados dentro del texto).
- "pendientes": lista de [tema, criterio de cierre] (8–12).
- "logistics": lista de objetos {name, cat («Frontera»/«Consular»/«Hospital»/«Combustible»/«Agua potable»), lat, lon, info, gmaps_query, source_url}: puntos de entrada relevantes (puerto/aeropuerto/pasos), Embajada o consulado de España competente (dirección exacta), 1–2 hospitales/clínicas de referencia, combustible y agua (1–2 entradas). Coordenadas de Wikipedia/GeoNames con URL; otra persona las verificará en Google Maps.
- "emergency": texto (50–80 palabras) con teléfonos: emergencia consular, policía, ambulancia, bomberos (verifica en MAEC).
- "sources": lista de [título con editor y fecha, url] con TODAS las páginas abiertas realmente (mínimo 20).
- "sources_note": 2–3 frases (fecha de revisión {FECHA}; herramienta de planificación, no autorización).
- "chips_extra": lista de [ETIQUETA, valor corto ≤58 caracteres] para: SEGURIDAD, SEGURO, SALUD (vacunación), DRONES, STARLINK, 4x4, A PIE.
- "cabecera": {"rutas": [texto corto para la casilla BAJADA (≤40 car., p. ej. «Fuera de ruta · solo en avión» o «Excluido · conflicto activo»), texto para SUBIDA («No aplica»)], "peligro": texto ≤34 car. para la casilla PELIGROS, "seguro": texto ≤52 car. para SEGURO}.
- "visado_registro": {"nivel": una de «sin» (exención), «electronico» (eVisa/eTA previa), «presencial» (embajada), «frontera» (a la llegada), «no_viable» (país no utilizable), "resumen": 1 frase, "accion": 1 frase, "coste": texto o "", "alerta": 1 frase, "oficial": url oficial del visado o "", "entradas": texto corto} — para la tabla central de visados.
- "cpd_registro": {"nivel": «obligatorio»/«recomendable»/«no», "confianza": «CONFIRMADO»/«PROBABLE»/«SIN CONFIRMAR», "alternativa": trámite alternativo al CPD (texto corto), "coste": texto corto, "nota": 2–4 frases con fuentes} — para la tabla central del CPD.
- "notas": dudas y fuentes que fallaron.

Escribe el archivo cuanto antes con una versión completa y mejórala después. Termina validando con python3 json.load y devuelve un resumen de 6 líneas.

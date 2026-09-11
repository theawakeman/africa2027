# Brief común — reescritura de fichas de país · África 2027

## El proyecto
PWA de planificación de una expedición overland real: **Barcelona → Sudáfrica → Barcelona por tierra**,
enero–agosto 2027. **2 vehículos 4x4** (Ineos Grenadier + Mitsubishi Delica), **3 viajeros + 1 perro**.
Repo: `/home/claude/africa2027`. Generador estático en Python en `tools/gen/`.

El sitio se genera con `build.py`, que importa `data_<slug>.py` de cada país. Tu trabajo es
**reescribir y ampliar un único archivo `data_<slug>.py`**.

## La ruta global confirmada (contexto para TODOS los corredores)

**BAJADA (ida, por el oeste, de norte a sur):**
Barcelona → ferry → Tánger Med → Marruecos (tránsito directo) → Sáhara Occidental → Mauritania →
Senegal (bajando por el Ferlo) → Guinea → Costa de Marfil → Ghana → Togo → Benín →
Nigeria (tránsito) → Camerún (tránsito) → **Congo (PARADA: gorilas de Odzala-Kokoua)** →
RD Congo (tránsito) → Angola → Zambia

**BUCLE (exploración, sur y este):**
Zambia → Tanzania (subiendo) → **Kenia (punto más oriental del viaje)** → Tanzania (bajando, por ruta
distinta) → Mozambique → Zimbabue → Botsuana → **Sudáfrica (punto más al sur)** → Namibia

**SUBIDA (vuelta, por el oeste, de sur a norte):**
Namibia → Angola → RD Congo (tránsito) → Congo (tránsito rápido, SIN parada de gorilas) →
Camerún (tránsito) → Nigeria (tránsito) → Benín → Togo → Ghana → Costa de Marfil → Guinea →
[Sierra Leona opcional] → Senegal (Casamance, suroeste) → **Gambia** → Dakar → Lac Rose →
Mauritania → Sáhara Occidental → Marruecos → ferry → Barcelona

**Países excluidos de la ruta fija:** Liberia (visado imposible en frontera terrestre) y Gabón
(eVisa solo aéreo) quedan como alternativas informativas. Mali, Guinea-Bisáu y Sudán, excluidos por
conflicto. El viaje **no pasa de Kenia hacia el Cuerno de África**.

## Directrices explícitas del dueño del proyecto

1. **Corredor doble.** En todo país que se cruce dos veces (o que se entre y salga por puntos distintos),
   hay que definir un **corredor de bajada** y otro **de subida**, y que **pasen por sitios diferentes**
   en la medida de lo posible. Fronteras de entrada/salida distintas siempre que exista alternativa real.
2. **Tramos 4x4 míticos.** Especialmente en el bloque sur: pasos por la playa, dunas que llegan al mar,
   travesías de salinas, puertos de montaña. "Llevamos 4x4 y también vamos por eso." No te limites a
   los PDIs turísticos estándar.
3. **Reservas naturales con el perro.** El dueño quiere ver fauna salvaje en la zona sur "aunque sea
   con el perro". Investiga la política real de mascotas de cada parque y, cuando esté prohibido
   (lo habitual en parques con grandes depredadores), **propón alternativas concretas**: reservas
   privadas que sí admitan perro, concesiones comunales, miradores fuera del parque, guarderías
   caninas en la puerta, turnos entre los viajeros. No te limites a decir "prohibido".
4. **Sección "Experiencias de otros overlanders".** Obligatoria, al final de la ficha. Relatos reales
   de **iOverlander, Tracks4Africa y blogs/foros públicos de viajeros**. Separada del contenido
   oficial. (Los grupos de Facebook no son accesibles: no los uses.)
5. **Nunca borres la ficha de ningún país.** Solo se amplían y corrigen.

## Formato técnico — OBLIGATORIO

Tu plantilla de referencia es **`tools/gen/data_angola.py`**: léela entera antes de escribir nada.
Es la ficha más nueva y tiene ya todo el formato objetivo. `tools/gen/data_common.py` define
`make_ficha(spec)` y la lista de claves del SPEC.

Claves del SPEC que **debes** incluir (todas son obligatorias salvo donde se diga opcional):
`slug, name, revision, sub, chips, center, zoom, notice, pois, logistics, corridor, facts, alerts,
ruta_intro, route_rows, visado, fronteras_rows, vehiculos, drones_callout, drones, starlink_callout,
starlink, perro_intro, salud, seguridad_intro, seguridad, pendientes, sources, sources_note, emergency`

Claves nuevas que debes usar (opcionales en el código, obligatorias para esta tarea):
- `corridor` + `corridor_alt`: listas de tuplas `(lat, lon)` con el trazado de cada corredor.
- `corridor_label` / `corridor_alt_label`: normalmente `"Bajada"` y `"Subida"`.
  (Si el país se cruza una sola vez pero con entrada y salida distintas, usa etiquetas que describan
  los dos tramos reales, p. ej. `"Entrada y descenso"` / `"Salida hacia el oeste"`.)
- `experiencias_intro` (str) + `experiencias` (lista de str, formato `"Titular: cuerpo del relato"`,
  que se renderiza con el titular en negrita).
- `offroad` (lista de str): rutas y pistas 4x4 destacadas.
- `acampada`, `agua`, `combustible`, `dog_matrix` (lista de tuplas `(zona, estado, plan B)`).

Cada POI es un dict con: `n, name, cat, prio, dog, time, lat, lon, desc, credit, source`.
El bucle `for _p in POIS:` al final (cópialo de Angola) deriva `img`, `icon` y `color` a partir de
`source` y `cat`. Las categorías válidas y sus colores están en `_CAT_COLOR`; usa las que ya existen
en el proyecto (`"Ciudad · servicios"` → azul, `"Naturaleza"` → verde, `"Cultura"` → morado o marrón,
`"Patrimonio UNESCO"` → marrón, `"Costa"` → turquesa).

### Densidad de PDIs — REQUISITO CRÍTICO (corrección expresa del dueño)

La media de conducción del viaje es de **250 km/día**. Un corredor de 2.000 km son 8 días de ruta: no puede
tener 2 o 3 puntos. El dueño lo dijo literalmente: *"no puede ser que en un país tan grande solo tengamos
2 puntos de interés en el corredor de bajada. Estoy convencido que hay mucho más que ver."*

- **Países con parada (no de paso): 18–25 PDIs**, repartidos a lo largo de TODO el trazado, de forma que
  raramente haya más de ~400–500 km entre dos puntos. No hace falta un PDI cada día, pero sí que no queden
  huecos de varios días en blanco.
- **Países de tránsito puro** (Nigeria, Camerún, RD Congo en su papel de paso): 6–10 PDIs, centrados en el
  propio eje de tránsito (ciudades con servicios, una parada digna por jornada).
- Reparte los PDIs **entre los dos corredores** (bajada y subida) sin solapamiento, salvo los nudos
  logísticos inevitables (la capital, la frontera compartida).
- Incluye en `route_rows` **las etapas con distancia y días aproximados** (cabeceras
  `("Etapa", "Recorrido", "Distancia y días aprox.")`), calculadas sobre 250 km/día. Así se ve de un vistazo
  si un tramo está vacío.
- Además de los PDIs, usa `offroad` (pistas 4x4) y `senderismo` (**excursiones a pie**: cumbres, cañones,
  senderos a cascadas, miradores; el dueño lo pidió expresamente) para añadir cosas que hacer por el camino.

### Dónde buscar — amplía las fuentes
No te quedes en Wikipedia. El dueño pidió expresamente entrar en **las webs oficiales de turismo de cada
país** y buscar fuentes nuevas del mundo overland, 4x4, naturaleza y excursionismo. Fuentes que funcionan bien:
- Web oficial de turismo del país (busca "<país> tourism official site", "visit <país>", ministerio de turismo).
- **iOverlander** y **Tracks4Africa** (incluido el blog de Tracks4Africa, que tiene guías país por país).
- Blogs reales de overlanders y de viajes 4x4 (busca "<país> overland blog", "<país> self drive itinerary",
  "<país> 4x4 route", "driving across <país>").
- Comunidades 4x4 (p. ej. 4x4community.co.za) y operadores de expediciones (sus itinerarios revelan los
  tramos buenos, aunque no los contratemos).
- Excursionismo: busca "hiking in <país>", "<país> trails", peakvisor, wikiloc, guías de trekking.
- Parques: web del organismo gestor (SANParks, African Parks, Namibia Wildlife Resorts, TANAPA, KWS, DNPW…)
  — es donde está la verdad sobre tasas, reservas previas y normas de mascotas.
- Birdlife / Important Bird Areas para naturaleza menos obvia, y UNESCO (incluida la **lista indicativa**,
  que saca a la luz sitios poco conocidos como el arte rupestre de Tchitundu-Hulu en Angola).

Busca activamente categorías que se suelen olvidar: cascadas, cuevas, fuentes termales, lagos y cráteres,
picos y miradores, arte rupestre y yacimientos, reinos y monarquías tradicionales vivas, arquitectura
colonial, ferrocarriles históricos, mercados, playas y puntos de surf, observación de aves, y lugares donde
se puede ver fauna **fuera** de parques nacionales (clave por el perro).

**La ficha de Angola (`data_angola.py`) ya está al nivel objetivo: 22 PDIs, etapas con km y días, secciones
de 4x4 y de excursiones a pie. Úsala como vara de medir.**

## Imágenes — regla estricta
Las fotos se enlazan desde Wikimedia Commons con el patrón
`https://commons.wikimedia.org/wiki/Special:FilePath/<NOMBRE_ARCHIVO>?width=900`
(espacios como `%20`, comas como `%2C`).

**`commons.wikimedia.org` NO se puede abrir con WebFetch** (dominio solo-caché, da error).
Para verificar que un archivo existe, usa **WebSearch** con `site:commons.wikimedia.org <tema>`
y coge un nombre de archivo que aparezca literalmente en los resultados. **Nunca inventes un nombre
de archivo**: una imagen rota es peor que ninguna.
Si no puedes verificar el autor exacto de la foto, pon `credit="Wikimedia Commons"` — es honesto,
y el enlace a la página del archivo (que el código genera solo) permite comprobar autoría y licencia.
No inventes nunca un nombre de autor ni una licencia concreta.

## Rigor — esto es una herramienta de planificación real
- **Investiga antes de escribir.** Usa WebSearch y WebFetch de verdad para: visado (¿eVisa?, ¿válido en
  frontera terrestre o solo aéreo?), pasos fronterizos reales y sus horarios, CPD/carnet de paso,
  seguro obligatorio, salud (fiebre amarilla, malaria, agua), drones (autoridad y régimen real),
  Starlink (¿activo en 2026?), seguridad por zonas, y política de mascotas de los parques.
- **Solo cita URLs que hayas visitado de verdad.** La lista `sources` debe ser real y comprobable.
- **Coordenadas reales.** Verifícalas (Wikipedia suele dar las coordenadas exactas de cada sitio).
- **Marca lo que no sepas.** Si un dato no se puede confirmar, dilo en el texto ("por confirmar") y
  añádelo a `pendientes` con un criterio de cierre. Nunca rellenes con suposiciones disfrazadas de dato.
- Todo el contenido va **en español**.

## Qué NO debes tocar
- `build.py`, `data_common.py`, `data_countries.py`, `site_common.py`, `admin_panel.py`
- `content/pois/*.json` y `content/ficha/*.json` (el orquestador los regenera después)
- Cualquier `data_<slug>.py` que no sea el tuyo
- No hagas `git commit` ni `git add`. No ejecutes `build.py` (hay otros agentes trabajando en paralelo
  y se pisarían la salida).

## Cómo verificar tu trabajo (obligatorio antes de terminar)
```bash
cd /home/claude/africa2027/tools/gen && python3 -c "
import data_<slug_con_guiones_bajos> as m
d = m.get_data()
print('PDIs:', len(d['pois']))
print('corredor bajada:', len(d['corridor']), 'puntos')
print('corredor subida:', len(d['corridor_alt']), 'puntos')
print('secciones:', [s[0] for s in d['custom_sections_post']])
assert any(s[0]=='experiencias' for s in d['custom_sections_post']), 'falta la sección de experiencias'
print('OK')
"
```
Si eso da error, arréglalo antes de terminar. No entregues un archivo que no importe limpio.

## Qué devolver
Un resumen breve (10–15 líneas) con: nº de PDIs, fronteras de entrada/salida de cada corredor,
los 2–3 tramos 4x4 destacados, qué has averiguado sobre el perro en los parques, y **cualquier
decisión o duda que el dueño del proyecto deba resolver**.

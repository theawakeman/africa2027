# Encargo: auditoría de PDIs y puntos logísticos de un país (app África 2027)

Eres auditor de contenido de una guía de viaje overland (Barcelona → Kenia → Barcelona, 2027, dos vehículos, tres viajeros y un perro). El propietario ha detectado **coordenadas desplazadas** y desconfía de posibles **alucinaciones** en los puntos de interés (PDIs). Tu trabajo, para UN país (`<slug>`):

## Entradas

- `content/pois/<slug>.json` — lista de PDIs (claves: n, name, cat, prio, dog, time, lat, lon, desc, credit, img, source, icon, color, dog_note).
- `content/ficha/<slug>.json` → clave `logistics` — puntos logísticos (name, cat ∈ Frontera/Combustible/Hospital/Agua potable/Consular/Servicio, lat, lon, info).
- `audit/geo/<slug>_eval.md` y `audit/geo/<slug>_eval.json` — resultado de contrastar cada punto con OpenStreetMap (Photon) y Wikidata: veredicto por punto (OK / OK? / AREA / DESPLAZADO / DUDOSO / SIN_REF), candidatos con nombre, tipo OSM, coordenadas y distancia en km al punto actual de la app. Los ids son `poi-<n>` (campo n del PDI) y `log-<i>` (índice en `logistics`).

## Qué hacer, punto por punto

1. **DESPLAZADO** (referencia con el mismo nombre a más del umbral: 1,5 km punto concreto · 4 km ciudad · 15 km área): si el candidato es sin duda el mismo lugar, corrige `lat`/`lon` en el JSON con las coordenadas del candidato más adecuado. Criterio de elección: para hospitales, consulados, puertos y pasos fronterizos, el nodo OSM `amenity=…`/`office=diplomatic`/`ferry_terminal`/`barrier=border_control`, nunca el `boundary=administrative`; para pueblos y ciudades, el `place=*`; para parques, reservas, dunas, gargantas y otras áreas, un punto **al que se pueda conducir** (puerta, oficina del parque, mirador, aparcamiento, pueblo de acceso), no el centroide del polígono. Si ninguno de los candidatos es el punto navegable correcto, búscalo en Wikipedia (coordenadas del artículo, es/en/fr) o en OpenStreetMap vía `https://www.openstreetmap.org/search?query=…` con WebFetch, o describe el punto de acceso conocido.
2. **DUDOSO / SIN_REF / OK?**: comprueba a mano si el lugar existe y dónde está: WebFetch de la Wikipedia (es/en/fr/pt) del lugar, WebSearch del nombre + país, página oficial (parque, ministerio, embajada). Si lo localizas, corrige coordenadas si difieren más del umbral. Si **no existe** o no eres capaz de confirmar que existe con un nombre parecido → es candidato a alucinación: elimínalo de `content/pois/<slug>.json` **solo si estás seguro** de que no existe o de que el nombre mezcla dos lugares; si solo es incierto, déjalo y anótalo como «NO VERIFICADO». Los puntos logísticos nunca se eliminan: se anotan.
3. **Consulados y embajadas de España**: contrasta la dirección con `https://www.exteriores.gob.es/Embajadas/<CIUDAD>/es/Embajada/Paginas/...` o `.../Consulados/<CIUDAD>/...` (WebFetch o WebSearch «Consulado General de España en <ciudad> dirección») y ajusta el punto al edificio real; si OSM tiene el nodo `office=diplomatic` con el nombre correcto, úsalo.
4. **Descripciones (`desc`) e `info`**: lee cada una y comprueba lo verificable (fechas, «Patrimonio de la Humanidad», «el más grande de…», récords, distancias, nombres de etnias o dinastías). Corrige errores de hecho con la fuente abierta; no reescribas por estilo. Si el texto promete algo que no puedes confirmar, suaviza («según fuentes locales…») o elimina la frase.
5. **Interés**: evalúa si cada PDI aporta valor a una expedición overland con perro (paisaje, cultura, logística). No cambies `prio` salvo error evidente; anota en el informe los que consideras flojos o repetitivos y por qué, y hasta tres lugares de gran interés que falten en el país (con coordenadas verificadas y fuente), para que el propietario decida.
6. **No toques** los puntos genéricos de Combustible / Agua potable que no nombran un lugar concreto («red densa…», «supermercados y garrafas…»): se tratarán en la auditoría de agua y combustible. Tampoco toques otras claves del JSON.

## Salida

- JSON editados en sitio con `json.dump(..., ensure_ascii=False, indent=2)` para `content/pois/<slug>.json` y `indent=2` para `content/ficha/<slug>.json` (respeta el formato actual: comprueba con `git diff --stat` que solo cambian las líneas previstas). Redondea coordenadas a 5 decimales.
- Informe `audit/geo/<slug>_cambios.md` con: (a) tabla de correcciones aplicadas: id · nombre · lat/lon antes → después · distancia · fuente (URL); (b) PDIs eliminados y por qué; (c) puntos NO VERIFICADOS (con lo que probaste); (d) correcciones de texto; (e) opinión sobre interés y sugerencias de PDIs nuevos; (f) fuentes abiertas que fallaron.
- Escribe el informe **de forma incremental** (empieza el archivo nada más terminar los DESPLAZADO): si tu sesión se corta, lo escrito en disco es lo que cuenta.
- Termina validando los JSON (`python3 -c "import json;json.load(open(...))"`) y devuelve un resumen de 5 líneas.

Reglas: nunca inventes coordenadas de memoria; cada coordenada nueva viene de OSM/Wikidata/Wikipedia/fuente oficial abierta en esta sesión, con URL en el informe. Si WebFetch responde «cache-only» pero devuelve contenido, vale. Si una fuente no carga, prueba la Wikipedia en otro idioma antes de rendirte.

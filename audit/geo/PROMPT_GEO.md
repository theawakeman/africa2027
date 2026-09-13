# Encargo: geocodificar los puntos de varios países contra OpenStreetMap y Wikidata

Trabajas en `/home/claude/africa2027`. Tu única tarea es producir, para cada país de la lista que te den, los archivos `audit/geo/<slug>_ref.json` y `audit/geo/<slug>_eval.md` / `_eval.json`. **No edites nada bajo `content/`** ni redactes informes: de eso se encargan otros.

Desde este contenedor, Photon, Nominatim y Overpass están bloqueados por el proxy de salida. La única vía que funciona es ejecutar JavaScript en el navegador integrado, en una pestaña cuyo origen es `https://photon.komoot.io`.

## Herramientas del navegador

Si los tools `mcp__remote-devices__Claude_Browser__*` no están cargados, cárgalos primero con una sola llamada:

`ToolSearch` con `query: "select:mcp__remote-devices__Claude_Browser__tabs_context,mcp__remote-devices__Claude_Browser__javascript_tool,mcp__remote-devices__Claude_Browser__preview_start"`

Luego `tabs_context` para ver las pestañas. Debe existir una con origen `https://photon.komoot.io` (suele llamarse `seed`). Si no existe, ábrela con `preview_start` en `https://photon.komoot.io/api/?q=test&limit=1`.

## Procedimiento, país por país (en serie, nunca dos a la vez)

1. `cd /home/claude/africa2027 && python3 tools/gen/audit_geo_prep.py <slug>` — genera `audit/geo/<slug>_queries.json`.
2. Revisa las variantes de búsqueda que ha generado: `python3 -c "import json;d=json.load(open('audit/geo/<slug>_queries.json'));[print(i['id'],i['cat'],'|',i['name'][:60],'->',i['q']) for i in d['items']]"`. Si alguna variante es basura (frases descriptivas como «red densa de gasolineras», nombres en español que OSM no conoce, topónimos partidos por la mitad), **mejórala a mano**: el objetivo es que cada punto se busque por su topónimo real en el idioma del país (francés en Guinea, Costa de Marfil, Togo, Benín, Camerún, Gabón, Congo y RDC; portugués en Angola y Mozambique; inglés en el resto) y por su nombre internacional. Un punto sin buena consulta es un falso «sin referencia» que hace perder tiempo al auditor siguiente.
3. `python3 tools/gen/audit_geo_js.py <slug> --compact` — imprime una llamada `window.__geoRun([...], [bbox])`. Si has mejorado consultas a mano, edita esa llamada antes de ejecutarla.
4. Ejecuta esa llamada con `javascript_tool` en la pestaña de Photon. Debe responder `"started N"`. Si responde que `__geoRun` no está definida, primero pega la definición completa que imprime `python3 tools/gen/audit_geo_js.py <slug>` (sin `--compact`): ese JS define las funciones y arranca la consulta a la vez.
5. Espera. La consulta tarda del orden de 4 a 8 segundos por punto. Sondea con:
   `JSON.stringify({done:window.__geoDone,err:window.__geoErr,n:(window.__geoOut||[]).length})`
   y **no pidas el resultado completo hasta que `done` sea `true`** (pedirlo antes gasta contexto para nada). Entre sondeos, espera con `sleep 45` en Bash.
6. Cuando `done` sea `true`, recoge el resultado con
   `JSON.stringify(window.__geoOut)`
   y guárdalo **tal cual, sin reescribirlo ni resumirlo**, en `audit/geo/<slug>_ref.json` (es un array JSON; el texto que devuelve la herramienta viene escapado como cadena JSON, así que desescápalo antes de guardarlo — lo más seguro es usar la herramienta Write con el array ya desescapado, o guardar la cadena en un fichero y hacer `python3 -c "import json;open('audit/geo/<slug>_ref.json','w').write(json.load(open('/tmp/raw.txt')))"`). Comprueba después que `json.load` lo lee y que tiene tantos elementos como puntos.
7. `python3 tools/gen/audit_geo_eval.py <slug>` — escribe `<slug>_eval.json` y `<slug>_eval.md` e imprime el resumen de veredictos.
8. Pasa al país siguiente.

## Salida

Cuando hayas terminado todos los países, devuelve un resumen corto: por país, el recuento de veredictos que imprimió `audit_geo_eval.py`, y una lista de los ids con veredicto DESPLAZADO, DUDOSO o SIN_REF con su nombre y la distancia del mejor candidato, en una línea cada uno. Esa lista es lo que usarán los auditores de cada país, así que sé preciso y no la resumas de más. Indica también qué consultas tuviste que arreglar a mano y si alguna fuente falló.

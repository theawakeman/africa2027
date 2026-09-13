# Auditoría de PDIs y puntos logísticos · LIBERIA

Fecha: 2026-09-13 · Entradas: `content/pois/liberia.json` (17 PDIs), `content/ficha/liberia.json → logistics` (13 puntos), `audit/geo/liberia_eval.{md,json}`, `audit/geo/liberia_ref.json`.

Veredictos de partida: 19 OK · 1 AREA · **10 DESPLAZADO**. Se han corregido los 10.

> Nota de método: Photon, Nominatim y Overpass están bloqueados desde este contenedor. Todas las coordenadas nuevas se han obtenido en esta sesión vía **mapcarta.com** (que expone el objeto OSM con su id y sus etiquetas) y **Wikipedia (en)**, más los candidatos OSM ya registrados en `liberia_eval.json`. Ninguna coordenada sale de memoria.

---

## (a) Correcciones aplicadas

| id | nombre | antes (lat, lon) | después (lat, lon) | dist. | objeto / fuente |
|---|---|---|---|---|---|
| poi-8 | Greenville (Sinoe) · la puerta de Sapo | 5.4111, -8.4146 | **5.01111, -9.03889** | **82,2 km** | OSM `place=town` *Greenville*, vía eval; contrastado con Wikipedia (5.017 N, 9.033 W) — https://en.wikipedia.org/wiki/Greenville,_Liberia |
| poi-1 | Bo-Waterside · la frontera que no podemos cruzar | 6.85, -11.25 | **7.01212, -11.37447** | 22,7 km | OSM nodo **4529337830** `place=town` *Bo Waterside* — https://mapcarta.com/Bo_Waterside ; Wikipedia 7.0107 N, 11.373 W — https://en.wikipedia.org/wiki/Bo_Waterside |
| log-0 | Frontera · BLOQUEADA — Bo-Waterside / Jendema | 6.85, -11.25 | **7.01212, -11.37447** | 22,7 km | misma fuente que poi-1 (punto compartido) |
| poi-17 | Loguatuo · la salida hacia Costa de Marfil | 7.2833, -8.1667 | **7.23933, -8.36691** | 22,6 km | OSM nodo **3164768778** `place=hamlet` *Loguatuo* — https://mapcarta.com/Loguatuo |
| log-2 | Frontera · Salida hipotética — Loguatuo / Ganta | 7.2833, -8.1667 | **7.23933, -8.36691** | 22,6 km | misma fuente que poi-17 (punto compartido) |
| poi-15 | Cataratas de Kpatawee | 6.9667, -9.6167 | **7.1224, -9.6409** | 17,5 km | OSM nodo **6088844172** `tourism=attraction` *Kpatawe Waterfall* — https://mapcarta.com/Kpatawe_Waterfall ; pueblo de Kpatawee (nodo 3019315109, https://mapcarta.com/Kpatawee) a 3,8 km al sur |
| log-3 | Embajada de Liberia en Conakry | 9.535, -13.675 | **9.59904, -13.65485** | 7,5 km | OSM nodo **5861167941** `office=diplomatic` *Embassy of Liberia*, Ratoma (Conakry) — https://mapcarta.com/N5861167941 |
| log-4 | Embajada de Liberia en París | 48.8566, 2.3522 | **48.88279, 2.31135** | 4,2 km | OSM *Ambassade du Liberia*, 12 Place du Général Catroux, 75017 París — https://mapcarta.com/Ambassade_du_Liberia |
| log-5 | Embajada de España en Abiyán | 5.36, -3.97 | **5.34617, -4.00593** | 4,3 km | OSM `office=diplomatic` *Embassy of Spain* (candidato de `liberia_eval.json`); ver reservas en el apartado (c) |
| log-12 | Agua · sureste y Sapo | 5.4, -8.8 | **5.35392, -8.81508** | 5,4 km | OSM nodo **1111150081** *Sapo National Park Headquarters* — https://mapcarta.com/Sapo_National_Park_Headquarters |

### Detalle de los casos que lo merecen

**poi-8 Greenville — el error de origen está identificado.** La coordenada que tenía la app (5.4111, -8.4146) es, literalmente y hasta el cuarto decimal, la coordenada que Wikipedia da para el **Parque Nacional de Sapo** (5°24′40,01″N 8°24′52,65″W = 5.4111139, -8.4146250 — https://en.wikipedia.org/wiki/Sapo_National_Park). No era un redondeo ni una aproximación: era la ficha de Sapo pegada en la de Greenville. Greenville está 82 km al oeste-suroeste, en la costa, y el punto anterior caía en plena selva del interior de Sinoe, sin carretera. Corregido al nodo `place=town` de OSM, que coincide con Wikipedia dentro de 700 m. Dato colateral tranquilizador: `log-10` (Combustible · sureste) ya estaba bien, en 5.0167, -9.0333, es decir a 900 m del Greenville real — la ficha logística sabía dónde estaba la ciudad y la de PDIs no.

**poi-1 / log-0 Bo-Waterside — ¿sigue bloqueado?** El punto anterior (6.85, -11.25) caía 22,7 km al sureste, en el interior del condado de Grand Cape Mount, sin relación con el paso. Corregido al pueblo fronterizo. En OSM el puesto en sí no tiene topónimo propio: hay una *Immigration Office* y el *MRU Bridge* (puente del río Mano) entre Bo Waterside y Jendema, pero ninguno con nodo nombrado accesible desde mapcarta, así que el punto marca el pueblo liberiano, a un par de cientos de metros del puente. Jendema, al otro lado, está en 7.0223, -11.38414 (OSM nodo 3060898005, https://mapcarta.com/Jendema): 1,3 km. Es decir, las dos fichas —Liberia y Sierra Leona— deben quedar prácticamente encima la una de la otra, y ahora lo están.

**Sobre si el texto está desfasado: NO, sigue siendo correcto.** Verificado contra https://en.wikipedia.org/wiki/Visa_policy_of_Liberia (consultado en esta sesión): desde el **11 de marzo de 2025** Liberia opera un visado electrónico a la llegada (e-VOA) y *«a visa on arrival can only be issued at Monrovia international airport»* — no en frontera terrestre. Además, la propia política dice que si existe misión liberiana en tu país de residencia hay que tramitarlo en ella y no por el portal. España no figura entre los países exentos. Conclusión: la frase «este puesto es una pared» sigue vigente a día de hoy, el paso está operativo pero no para nosotros sin visado estampado previamente. **No se ha tocado el texto de poi-1 ni de log-0.** Lo que sí conviene es re-verificar este punto concreto a principios de 2027, porque es una política de menos de dos años y es exactamente el tipo de norma que cambia.

**poi-17 / log-2 Loguatuo.** El punto anterior (7.2833, -8.1667) estaba 22,6 km al este, ya **dentro de Costa de Marfil**. Corregido al pueblo. Igual que en Bo-Waterside, el puesto fronterizo no tiene nodo con nombre en OSM (mapcarta solo lista un genérico *«Poste frontière»* sin coordenada propia), así que el punto marca el pueblo.

**poi-15 Cataratas de Kpatawee.** El eval proponía el pueblo de Kpatawee (13,8 km) o Wikidata (13,5 km), pero ninguno de los dos es el salto. En OSM sí existe el nodo del salto (`tourism=attraction` *Kpatawe Waterfall*, id 6088844172), a 3,8 km al norte del pueblo, y es el que se ha usado: es el punto al que se conduce. Desplazamiento real respecto a lo que tenía la app: 17,5 km.

**log-12 Agua · sureste y Sapo.** Es un punto genérico de agua (no nombra un lugar concreto y, por la regla 6 del encargo, no se tocaría), pero el propietario ha pedido expresamente anclarlo. Se ha movido a la **sede del Parque Nacional de Sapo**, que es la única referencia navegable de esa zona y coherente con el texto («salir de Greenville con toda la reserva llena»).

---

## (b) PDIs eliminados

**Ninguno.** No se ha detectado ninguna alucinación en los 17 PDIs de Liberia: todos los topónimos tienen respaldo en OSM o Wikipedia. El caso de poi-8 no era un lugar inventado sino una coordenada intercambiada.

---

## (c) Puntos NO VERIFICADOS o verificados con reservas

- **log-5 · Embajada de España en Abiyán — coordenada OSM aplicada, dirección NO reverificada.** La coordenada nueva (5.34617, -4.00593) es el nodo `office=diplomatic` llamado *Embassy of Spain* que ya recogía `liberia_eval.json`, y es coherente con el segundo candidato (*Résidence de l'ambassadeur de l'Espagne*, 5.33175, -3.99296, a 1,8 km) y con el barrio que dice la ficha (Cocody). Lo que **no** se ha podido hacer es contrastarla contra la web del Ministerio: se probaron seis rutas distintas de `exteriores.gob.es` (`/Embajadas/abiyan/...`, `/embajadas/abiyan/...`, buscador de embajadas y consulados, ficha por país) y todas devolvieron 404 o una página sin la dirección postal. La dirección que figura en el `info` («Impasse Ablaha Pokou, Cocody Danga Nord») **se mantiene tal cual pero queda sin reverificar**: confirmarla antes de darla por buena en una emergencia.
- **poi-1 / log-0 y poi-17 / log-2 · el puesto fronterizo en sí no está cartografiado.** En los dos pasos el punto marca el **pueblo**, no la barrera. Se intentó obtener el GPS oficial del puesto en el Logistics Cluster de Naciones Unidas: `lca.logcluster.org/liberia` y `lca.logcluster.org/country/liberia` devuelven 404, `lca.logcluster.org/liberia-24-border-crossing` devuelve 403, y en el DLCA histórico (`dlca.logcluster.org/display/public/DLCA/Liberia`) el índice de Liberia **solo documenta cuatro pasos —Kablaken Point, Mandecoma Point, Konadu y Pedebo/Duokudi—, ninguno de los cuales es Bo Waterside ni Loguatuo**, y las cuatro subpáginas devolvieron 403 al intentar abrirlas. Error residual esperable: unos cientos de metros. Irrelevante para navegar, relevante solo si alguien espera que el pin caiga sobre la cabina.
- **poi-16 · Bosque de Gola liberiano (veredicto AREA, 16,6 km).** No estaba en el encargo y **no se ha tocado**. Su propio texto ya avisa de que la coordenada es aproximada y de que el estatus legal está por confirmar. Queda pendiente para una pasada futura: si se quiere un punto navegable habría que anclarlo a un pueblo de acceso (zona de Kongo/Bopolu) y no al polígono.

---

## (d) Correcciones de texto

| id | qué decía | qué dice ahora | por qué |
|---|---|---|---|
| poi-8 | «a unos **150 km** al sureste de Monrovia en línea recta pero mucho más por carretera» | «a unos **240 km** al sureste de Monrovia en línea recta y bastante más por carretera» | Con la coordenada correcta, Monrovia (6.3131, -10.8014) → Greenville (5.01111, -9.03889) son 243 km en línea recta. La cifra de 150 km venía arrastrada del punto equivocado. |
| poi-17 | «a unos **40 km** de Ganta» | «a unos **70 km** de Ganta» | Ganta (7.2333, -8.9833) → Loguatuo (7.23933, -8.36691) son 68 km en línea recta. |
| poi-17 | «POR CONFIRMAR horarios y si sella CPD. **Coordenada aproximada.**» | «…Coordenada corregida sobre el pueblo de Loguatuo en OpenStreetMap (nodo 3164768778); el puesto fronterizo en sí no está cartografiado con topónimo, así que el punto marca el pueblo, no la barrera.» | El aviso genérico ya no describe la situación real. |
| poi-15 | «**COORDENADA APROXIMADA: no se ha podido verificar en fuente cartográfica**, confirmar sobre el terreno.» | «Coordenada verificada sobre el nodo del salto en OpenStreetMap: el salto queda unos 4 km al norte del pueblo de Kpatawee.» | Ya está verificada. |
| log-2 | «…**Coordenada aproximada.**» | «…Coordenada corregida sobre el pueblo de Loguatuo (OpenStreetMap); antes caía 22,6 km al este, ya en territorio marfileño.» | ídem. |
| log-3 | «**Coordenada urbana aproximada** — localizar la dirección exacta al confirmar.» | «Coordenada corregida sobre el nodo `office=diplomatic` «Embassy of Liberia» de OpenStreetMap, en la comuna de Ratoma (Conakry); confirmar el número de calle al llamar.» | ídem. |
| log-4 | «**Coordenada de referencia de París.**» | «Dirección: 12 Place du Général Catroux, 75017 París · +33 1 47 63 58 55 · contact@embassyofliberia-paris.org. Coordenada corregida sobre el edificio.» | Dirección y teléfono verificados en https://mapcarta.com/Ambassade_du_Liberia (datos OSM del edificio). |
| log-12 | — | Se añade: «El punto está anclado en la sede del Parque Nacional de Sapo, que es la referencia navegable de la zona.» | Explica qué marca el pin tras moverlo. |

**Datos comprobados que resultaron CORRECTOS y se dejan intactos:**
- poi-8: 16.434 habitantes (censo 2008) ✓; tercer puerto del país, dos muelles (70 y 180 m) y 6 m de calado ✓; fundada hacia 1838 por la Mississippi Colonization Society ✓; nombre por James Green, juez y plantador del condado de Jefferson (Misisipi) que envió a Liberia a un grupo de sus antiguos esclavos ✓; **185 días de lluvia al año ✓** (el dato más llamativo de la ficha, y es exacto). Fuente: https://en.wikipedia.org/wiki/Greenville,_Liberia
- poi-1 / log-0: todo el bloque del visado electrónico de 11 de marzo de 2025 y su restricción al aeropuerto de Monrovia ✓ (https://en.wikipedia.org/wiki/Visa_policy_of_Liberia).
- poi-9 (Sapo, no tocado): 1.804 km² ✓, primer parque nacional del país ✓, acceso solo a pie y con autorización de la Forestry Development Authority ✓ (https://en.wikipedia.org/wiki/Sapo_National_Park).

---

## (e) Interés de los PDIs y sugerencias

**Valoración general.** Liberia está bien cubierta para lo que es: 17 PDIs con la costa (Robertsport, Buchanan, Harper), el interior (Gbarnga, Ganta, Yekepa, Kpatawee), la historia (Providence Island, Harbel) y la naturaleza (Sapo, Gola, Lago Piso). Ninguno sobra de forma evidente.

**Flojos o discutibles** (no se ha cambiado ningún `prio`, esto es solo opinión para que decida el propietario):
- **poi-1 Bo-Waterside** (`prio: Media`) y **poi-17 Loguatuo** (`prio: Baja`) son pasos fronterizos convertidos en PDI. Duplican exactamente lo que ya dicen log-0 y log-2, con el mismo texto en gran parte. Si la app muestra las dos capas juntas en el mapa, el usuario ve dos pines encima del otro diciendo lo mismo. Sugerencia: dejarlos solo como puntos logísticos, o recortar el `desc` del PDI a una línea que remita al bloque de visado.
- **poi-11 Zwedru** y **poi-14 Gbarnga** son «ciudad de paso con servicios» sin nada que ver. Tienen valor logístico real (combustible, hospital, dormir) pero como PDI son relleno. Están bien situados, así que es una cuestión de etiqueta, no de datos.
- **poi-9 Sapo** tiene `prio: Alta` y `time: 3–5 días` pero su propio texto explica que es una expedición a pie de varios días, con permiso previo y porteadores, y con el perro prohibido. Con dos vehículos, tres personas y un perro, es en la práctica invisitable. Merece seguir en la ficha por lo que cuenta, pero quizá con la prioridad rebajada o con un aviso de «no realizable en este viaje» más arriba en el texto.

**Hasta tres lugares de gran interés que faltan** (coordenadas verificadas en esta sesión, para que el propietario decida):

1. **Ducor Hotel, Monrovia** — **6.32021, -10.813** · OSM way 1513039481, Wikidata Q1263572 — https://mapcarta.com/Ducor_Hotel . Hotel de lujo abandonado de 1960, ocho plantas y 106 habitaciones, en lo alto del cabo de Monrovia. Es la ruina más fotografiada del país y el mejor mirador sobre la ciudad, el puerto y Providence Island. Se llega en coche hasta la puerta. Encaja perfectamente con el tono del resto de la ficha (Harper y sus mansiones en ruinas, Providence Island) y le da a Monrovia algo más que «la capital más lluviosa».
2. **Libassa (playa y laguna), condado de Margibi** — **6.17678, -10.4836** · OSM way 298006326 — https://mapcarta.com/Libassa_Ecolodge . Está justo sobre el eje Monrovia–Buchanan, a medio camino, con playa, laguna y un alojamiento con terreno donde parar. Es el punto obvio para una noche entre la capital y Grand Bassa, y de los pocos sitios de Liberia donde un perro tiene un uso claro (playa abierta, no área protegida). **Verificar antes** de prometer nada: la política de mascotas del establecimiento no se ha comprobado.
3. **Tubmanburg / colinas de Bomi** — **6.86869, -10.82482** · OSM — https://mapcarta.com/Tubmanburg . Capital del condado de Bomi, antiguo centro minero de hierro y diamantes arrasado en la primera guerra civil, en un paisaje de colinas raro para la costa liberiana. Es además el desvío natural en el trayecto Monrovia–Bo-Waterside, o sea que no cuesta nada meterlo. **Reserva honesta:** la atracción que la gente va a ver de verdad es el lago de la mina («Blue Lake»), y **no he conseguido verificar su coordenada** — mapcarta muestra una foto etiquetada «Bomi lake» en la página de Tubmanburg pero sin nodo ni coordenada propia, y `mapcarta.com/Blue_Lake` devuelve el Blue Lake de California. Lo que se propone, por tanto, es el punto del pueblo, con el lago descrito como excursión local por confirmar sobre el terreno.

---

## (f) Fuentes abiertas que fallaron

| Fuente | Resultado |
|---|---|
| Photon / Nominatim / Overpass | bloqueados desde el contenedor (premisa del encargo) |
| `https://lca.logcluster.org/liberia` · `/country/liberia` | 404 |
| `https://lca.logcluster.org/liberia-24-border-crossing` | 403 |
| `https://lca.logcluster.org/241-liberia-border-crossing-of-bo-waterside` (patrón tentativo) | 404 |
| `https://dlca.logcluster.org/display/public/DLCA/2.3.1..2.3.4 Liberia Border Crossing of …` | 404 la primera, **403** las otras tres. El índice de Liberia sí carga, pero **no documenta Bo Waterside, Ganta ni Loguatuo**: solo Kablaken Point, Mandecoma Point, Konadu y Pedebo/Duokudi |
| `https://dlca.logcluster.org/display/public/DLCA/2.3 Liberia Road Network` | carga, pero no contiene ningún paso fronterizo ni coordenada |
| `https://www.exteriores.gob.es/...` (6 rutas distintas para Abiyán) | 404 / sin dirección postal |
| `https://www.openstreetmap.org/node/…` | bloqueado por `robots.txt` |
| `https://www.evisa.gov.lr/` | bloqueado por `robots.txt` (la política se verificó vía Wikipedia) |
| `https://en.wikipedia.org/wiki/Kpatawee_Waterfall` · `https://es.wikipedia.org/wiki/Loguatuo` | no existen (dominio «cache-only») |
| `WebSearch` | presupuesto de la sesión agotado (200/200) antes de empezar; toda la investigación se hizo con WebFetch dirigido |

---

## Validación

```
python3 -c "import json;json.load(open('content/pois/liberia.json'));json.load(open('content/ficha/liberia.json'))"  → OK
git diff --stat  → content/ficha/liberia.json 32 líneas · content/pois/liberia.json 22 líneas, todas previstas
```

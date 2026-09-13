# Auditoría de PDIs y puntos logísticos · SIERRA LEONA

Fecha: 2026-09-13 · Entradas: `content/pois/sierra-leona.json` (20 PDIs), `content/ficha/sierra-leona.json → logistics` (14 puntos), `audit/geo/sierra-leona_eval.{md,json}`, `audit/geo/sierra-leona_ref.json`.

Veredictos de partida: 30 OK · 1 OK? · 1 DUDOSO · **2 DESPLAZADO**. Es, con diferencia, el país más limpio del grupo: **`content/pois/sierra-leona.json` no se ha tocado**, los tres puntos con problema estaban todos en `logistics` y los tres eran fronteras.

> Nota de método: Photon, Nominatim y Overpass están bloqueados desde este contenedor. Las coordenadas nuevas se han obtenido en esta sesión vía **mapcarta.com** (que expone el objeto OSM con su id y sus etiquetas) y **Wikipedia (en)**. El **Logistics Cluster de Naciones Unidas no ha sido accesible** en ninguna de sus rutas (ver apartado f), que es justo la fuente que se pedía para los pasos fronterizos: eso condiciona el resultado de log-3.

---

## (a) Correcciones aplicadas

| id | nombre | antes (lat, lon) | después (lat, lon) | dist. | objeto / fuente |
|---|---|---|---|---|---|
| log-4 | Frontera · Jendema / Bo-Waterside (hacia Liberia) | 6.85, -11.25 | **7.0223, -11.38414** | **24,2 km** | OSM nodo **3060898005** `place=hamlet` *Jendema* — https://mapcarta.com/Jendema |
| log-2 | Frontera · Salida alternativa norte — Kamakwie / Madina Oula | 9.95, -12.25 | **9.84509, -12.3796** | **18,4 km** | OSM nodo **5459864108**, *Border post of Sierra Leone* (control fronterizo) — https://mapcarta.com/N5459864108 |
| log-3 | Frontera · Salida alternativa noreste — Kabala / Faranah | 9.7, -11.2 | **sin cambio** | — | **NO VERIFICADO** — ver apartado (c) |

### log-4 · Jendema — coordinación con la ficha de Liberia

Este era el punto que había que cuadrar con el otro lado. El estado anterior era absurdo por partida doble: **la ficha de Sierra Leona y la de Liberia tenían literalmente la misma coordenada equivocada (6.85, -11.25)**, un punto en tierra de nadie a 22-24 km al sureste del paso, lo que significaba que el mismo error se copió en las dos direcciones.

Ahora cada ficha apunta a su propio lado del puente sobre el río Mano:

| | punto | coordenada | fuente |
|---|---|---|---|
| Sierra Leona (log-4) | Jendema | 7.0223, -11.38414 | OSM nodo 3060898005 |
| Liberia (poi-1 y log-0) | Bo Waterside | 7.01212, -11.37447 | OSM nodo 4529337830 |

**Separación entre los dos: 1,56 km**, que es aproximadamente lo que miden los dos puestos y el puente entre ellos. Coherencia conseguida: las dos fichas describen el mismo paso y ahora se ven como dos pines contiguos en el mapa, no como dos pines a 24 km cada uno de su sitio.

Como en Liberia, **OSM no tiene un nodo con topónimo para el puesto fronterizo sierraleonés en sí**: lo que hay alrededor de Jendema es el pueblo, el *Jendema Community Market* (7.02, -11.3831) y el *Jendema Community Health Centre* (7.02278, -11.38626), los tres dentro de 400 m. El punto marca el pueblo, no la barrera. Error residual esperable: unos cientos de metros.

Se ha comprobado además el dato del texto: **es cierto que Jendema es uno de los tres puntos donde Sierra Leona expide visado a la llegada** — los otros dos son el aeropuerto internacional de Freetown y Gbalamuya, programa en vigor desde el 5 de septiembre de 2019 (https://en.wikipedia.org/wiki/Visa_policy_of_Sierra_Leone). El `info` de log-4 no necesitaba corrección de fondo.

### log-2 · Kamakwie / Madina Oula — el mejor resultado de los tres

Aquí el eval había dado **DUDOSO** porque ninguno de sus candidatos hacía *match* de nombre: proponía «Sainya» a 18,8 km, y «Sanka» y «Sanda» a más de 100 km, que son ruido. Rastreando desde Sainya hacia el norte apareció lo que hacía falta: **OSM sí tiene cartografiados los dos puestos de este paso**, uno a cada lado, aunque sin el nombre «Kamakwie» ni «Madina Oula» que buscaba el eval:

- **Puesto sierraleonés** — *Border post of Sierra Leone*, nodo **5459864108**, **9.84509, -12.3796**, a 0,8 km al norte del pueblo de Sainya (https://mapcarta.com/N5459864108).
- **Puesto guineano** — *Guinéan border post*, nodo **5459864107**, 9.87692, -12.44125, a 7,6 km al noroeste del anterior (https://mapcarta.com/Guin%C3%A9an_border_post).
- **Madina Woula (Guinea)**, el pueblo de referencia del lado guineano, a 9 km al noroeste del puesto sierraleonés (https://mapcarta.com/Madina_Oula, 9.88333, -12.45).
- **Kamakwie**, el pueblo de referencia del lado sierraleonés, nodo 320060481, 9.4963, -12.24125, a **41,6 km al sur-sureste** del puesto (https://mapcarta.com/Kamakwie).

El punto se ha movido al puesto sierraleonés. Ojo con la lectura del nombre del punto: «Kamakwie / Madina Oula» describe el **eje**, no dos pueblos pegados — hay 42 km de Kamakwie a la frontera. El `info` ya avisaba de que es un paso menor y sin documentación; ese aviso se mantiene íntegro, porque **que OSM tenga cartografiado un control fronterizo no significa que haya aduana habilitada para vehículos extranjeros ni capacidad de sellar un CPD**, que es el riesgo real que señala el texto. Lo que ha mejorado es la coordenada, no la certeza operativa.

---

## (b) PDIs eliminados

**Ninguno, y no había candidatos.** Los 20 PDIs de Sierra Leona tienen respaldo en OSM o Wikidata y ninguno estaba fuera de umbral. `content/pois/sierra-leona.json` queda intacto: cero líneas modificadas.

---

## (c) Puntos NO VERIFICADOS

### log-3 · Salida alternativa noreste — Kabala / Faranah → **NO VERIFICADO, punto sin mover**

Siguiendo la instrucción del encargo, se buscó primero el GPS del paso en el **Logistics Cluster de Naciones Unidas** y, al no encontrarlo, **se ha dejado el punto donde estaba (9.7, -11.2)** y se ha anotado en el `info`.

**Lo que se probó, en orden:**

1. `lca.logcluster.org/sierra-leone` → **403**.
2. `dlca.logcluster.org/display/public/DLCA/Sierra+Leone` → **carga**, pero su índice solo lista cinco bloques (Country Profile, Logistics Infrastructure, Logistics Services, Contact Lists, Annexes) **sin ninguna sección de border crossing visible**, a diferencia del índice de Liberia, que sí las tiene.
3. `dlca.logcluster.org/.../2.4+Sierra+Leone+Border+Crossing` → **403**.
4. `dlca.logcluster.org/.../2.4.1+Sierra+Leone+Border+Crossing+of+Gbalamuya` → **403**.
5. `dlca.logcluster.org/.../2+Sierra+Leone+Logistics+Infrastructure` → **403**.
6. `dlca.logcluster.org/.../2.3+Sierra+Leone+Road+Network` → **403** (en Liberia esta misma página sí carga; el bloqueo es específico de Sierra Leona o intermitente).
7. En OSM, vía mapcarta: **no hay ningún nodo de control fronterizo cartografiado en ese eje**. Se revisaron las páginas de Falaba (mapcarta devuelve el *distrito*, 9.626, -11.134, no el pueblo), Gberia Fotombu, Musaia y Hérémakono, y **ninguna lista un *border post* entre sus proximidades**, al contrario de lo que ocurría en Sainya. La técnica que funcionó para log-2 aquí no da nada: el puesto simplemente no está en OSM.

**Por qué no se ha movido a Falaba.** El eval proponía el `place=town` de Falaba (9.85546, -11.32114) a 21,8 km, y Wikidata lo mismo a 21,7 km. Pero **Falaba no es el paso**: es un pueblo del interior del distrito, no el punto donde se cruza. Mover el pin allí cambiaría un error de 21 km por otro error de tamaño parecido, esta vez con apariencia de precisión, que es peor. Se ha preferido dejar el punto marcado como no verificado.

**Lo que sí ha quedado establecido, y se ha escrito en el `info` para la verificación futura:** el eje Kabala–Faranah cruza entre dos poblaciones sí localizadas —

- **Gberia Fotombu** (Sierra Leona, distrito de Falaba, ~3.030 hab.): **9.87852, -11.16548** — https://mapcarta.com/Gberia_Fotombu (GeoNames 2409019).
- **Hérémakono** (Guinea, subprefectura de la prefectura de Faranah, ~12.900 hab.): **9.8897, -11.0668**, OSM nodo 2758769042 — https://mapcarta.com/Heremakono.

Están a **10,9 km** el uno del otro y la frontera pasa entre ambos, o sea entre **20 y 26 km al noreste** del punto actual. Esa es la horquilla donde hay que buscar. **Recomendación para el propietario:** cuando el Logistics Cluster vuelva a estar accesible (o ante cualquier overlander reciente), lo que hay que preguntar es por el puesto entre Gberia Fotombu y Hérémakono, no por «Kabala–Faranah» en abstracto.

### Otros puntos anotados, sin cambio

- **log-2** — coordenada corregida y verificada, pero **la operatividad del paso sigue sin verificar**: no hay documentación de aduana ni de sellado de CPD. El texto conserva su «NO contar con este paso hasta verificarlo».
- **poi-11 Bo** (veredicto **OK?**, 0,7 km) y **log-0/log-1 Gbalamuya** (OK, 7 km del pueblo): dentro de umbral y **no tocados**. Lo de Gbalamuya merece una nota: 7 km es mucho para un paso fronterizo, pero el veredicto es OK porque el umbral aplicado fue el de «punto» sobre un candidato de tipo pueblo. Si en algún momento se quiere afinar, ese es el siguiente candidato de la lista — no estaba en este encargo y **no se ha movido**.
- **poi-20 Outamba-Kilimi** (OK gracias a Wikidata, a 0,3 km, pero el candidato OSM está a 19,4 km): el punto es bueno; la discrepancia es del candidato OSM, no de la app.

---

## (d) Correcciones de texto

Ninguna corrección de hecho: **no se ha encontrado ningún error factual** en los `info` de los tres puntos. Los tres cambios son de trazabilidad de la coordenada, que es lo que pide el encargo cuando el texto anuncia «coordenada aproximada» y deja de serlo.

| id | qué decía | qué dice ahora |
|---|---|---|
| log-2 | «…con la aduana. **Coordenada aproximada.**» | «…con la aduana. Coordenada corregida (18,4 km): el punto está ahora sobre el puesto fronterizo sierraleonés que sí está cartografiado en OpenStreetMap (nodo 5459864108), 1 km al norte del pueblo de Sainya; el puesto guineano de Madina Oula queda 8 km al noroeste (nodo 5459864107). Que el puesto exista como control no significa que tenga aduana: sigue sin documentación operativa.» |
| log-3 | «VERIFICAR ANTES DE CONTAR CON ÉL. **Coordenada aproximada.**» | «VERIFICAR ANTES DE CONTAR CON ÉL. COORDENADA NO VERIFICADA: el puesto no aparece con topónimo propio en OpenStreetMap y el Logistics Cluster de Naciones Unidas no ha sido accesible en esta revisión, así que el punto se ha dejado donde estaba. Lo único confirmado es el eje: el último pueblo sierraleonés es Gberia Fotombu (9,87852 / -11,16548) y el primero guineano, Hérémakono (9,8897 / -11,0668), a 11 km; el paso está entre los dos, entre 20 y 26 km al noreste de este punto.» |
| log-4 | «…sería la puerta de enlace natural desde Sulima y Zimmi.» | «…sería la puerta de enlace natural desde Sulima y Zimmi. Coordenada corregida (24,2 km) sobre el pueblo de Jendema en OpenStreetMap: queda a 1,6 km del punto de Bo-Waterside de la ficha de Liberia, que es lo que debe ser — son los dos lados del mismo puente sobre el río Mano.» |

**Datos comprobados que resultaron CORRECTOS y se dejan intactos:**
- log-4: «uno de los tres puntos donde Sierra Leona expide visado a la llegada» ✓ — Freetown International Airport, Jendema y Gbalamuya, desde el 5-9-2019 (https://en.wikipedia.org/wiki/Visa_policy_of_Sierra_Leone).
- log-4: «Liberia está excluida de la ruta fija por el problema del visado» ✓ — verificado en la auditoría de Liberia de esta misma sesión: el e-visa liberiano sigue siendo de expedición exclusiva en el aeropuerto de Monrovia (https://en.wikipedia.org/wiki/Visa_policy_of_Liberia). Las dos fichas siguen siendo coherentes entre sí también en el texto.
- log-2: la ubicación «en la zona de Outamba-Kilimi» ✓ — el puesto está unos 25 km al noreste del parque.

---

## (e) Interés de los PDIs y sugerencias

**Valoración general.** Sierra Leona está, de largo, mejor construida que sus vecinas del grupo: 20 PDIs, todos dentro de umbral, con un reparto muy equilibrado entre península de Freetown (playas), historia de la trata (Bunce Island, Old Fourah Bay en su entorno), naturaleza de primer nivel (Tiwai, Gola-UNESCO, Tacugama, Outamba-Kilimi) y montaña (Bintumani, Kabala). No hay relleno evidente y no se propone eliminar nada.

**Observaciones, no cambios** (no se ha tocado ningún `prio`):
- **Playas de la península: poi-6 River No. 2, poi-7 Tokeh y poi-8 Bureh** son tres PDIs para 15 km de costa y describen experiencias parecidas. No sobran —cada una tiene su carácter— pero para una expedición con dos vehículos y un perro probablemente se visite una y se pase de largo por las otras. Si alguna vez hace falta recortar la ficha, ese es el sitio.
- **poi-19 Bintumani (1.945 m)** tiene `prio` de peso pero, igual que Sapo en Liberia, es una ascensión de varios días a pie desde Sinkunia o Yifin. No es un desvío en coche. Vale la pena que el texto lo diga tan claro como lo dice la ficha de Sapo.
- **poi-16 Islas Turtle** y **poi-9 Islas Banana** dependen las dos de barco local; conviene que el propietario decida cuál es realista con los vehículos aparcados y el perro a bordo, porque hacer las dos es improbable.
- **Cobertura fronteriza**: con log-0/log-1 (Gbalamuya, entrada y salida), log-2, log-3 y log-4, la ficha tiene los cuatro pasos que importan. Es la mejor cobertura fronteriza de las fichas auditadas hasta ahora.

**Hasta tres lugares de gran interés que faltan** (coordenadas verificadas en esta sesión, para que el propietario decida):

1. **Bonthe, isla de Sherbro** — **7.5273, -12.502** · OSM nodo 498808721 — https://mapcarta.com/Bonthe . Unos 10.200 habitantes en la orilla este de la isla, en el estuario del Sherbro. Es el gran hueco del sur de la ficha: la app tiene las Islas Turtle (poi-16), que son el extremo del archipiélago sherbro, pero no su capital histórica, que es una ciudad colonial portuaria con calles trazadas y un aeropuerto internacional cerrado desde 2002 como testimonio de lo que fue. **Reserva:** se llega en barco, igual que Turtle y Banana, así que compite por el mismo hueco de agenda; y no se ha verificado en esta sesión el estado de su arquitectura colonial ni el servicio de barcos.
2. **Cataratas de Bumbuna** — **9.054, -11.737** · OSM nodo 7631279456 (`natural=cliff`) — https://mapcarta.com/Bumbuna_Falls . En la provincia del Norte, con la presa de Bumbuna 2,5 km al noreste. Está sobre el eje Makeni–Kabala, o sea justo en el tramo del bucle norte que ahora mismo va de ciudad a ciudad sin nada que ver entre medias, y sería el contrapeso natural a las playas del sur. Es también el punto donde se entiende de golpe la infraestructura eléctrica del país.
3. **Old Fourah Bay College, Cline Town (Freetown)** — **8.49225, -13.2097** · OSM nodo 10811645605 — https://mapcarta.com/Old_Fourah_Bay_College . La ruina del primer centro de educación superior de estilo occidental del África occidental, a 320 m del Museo Nacional del Ferrocarril, que **ya es poi-3**. Es decir: sale prácticamente gratis en tiempo, porque se visita en la misma parada, y completa el relato de Freetown como «ciudad de los libertos» que ya abre poi-2. De las tres, es la que mejor relación interés/coste tiene.

---

## (f) Fuentes abiertas que fallaron

| Fuente | Resultado |
|---|---|
| Photon / Nominatim / Overpass | bloqueados desde el contenedor (premisa del encargo) |
| **Logistics Cluster (ONU) — todas las rutas probadas** | `lca.logcluster.org/sierra-leone` **403** · `dlca…/2.4+Sierra+Leone+Border+Crossing` **403** · `dlca…/2.4.1+…+of+Gbalamuya` **403** · `dlca…/2+Sierra+Leone+Logistics+Infrastructure` **403** · `dlca…/2.3+Sierra+Leone+Road+Network` **403**. Solo cargó el índice `dlca…/Sierra+Leone`, y **su tabla de contenidos no expone ninguna sección de border crossing**. Esta es la razón directa de que log-3 quede NO VERIFICADO |
| `https://mapcarta.com/Kabala` | devuelve **Kavala (Grecia)**, no Kabala (Sierra Leona) — colisión de topónimo |
| `https://mapcarta.com/Falaba` | devuelve el **distrito** de Falaba (9.626, -11.134), no el pueblo; `mapcarta.com/Falaba,_Sierra_Leone` → 404 |
| `https://mapcarta.com/Charlotte_Falls` | devuelve el Charlotte Falls de **Tennessee (EE. UU.)** — colisión de topónimo |
| `https://en.wikipedia.org/wiki/Gberia_Fotombu` | no existe (dominio «cache-only»); la coordenada se obtuvo vía mapcarta/GeoNames |
| `https://www.openstreetmap.org/node/…` | bloqueado por `robots.txt` |
| `WebSearch` | presupuesto de la sesión agotado (200/200) antes de empezar; toda la investigación se hizo con WebFetch dirigido |

---

## Validación

```
python3 -c "import json;json.load(open('content/pois/sierra-leona.json'));json.load(open('content/ficha/sierra-leona.json'))"  → OK
git diff --stat  → content/ficha/sierra-leona.json 14 líneas (7 cambios) · content/pois/sierra-leona.json SIN CAMBIOS
```

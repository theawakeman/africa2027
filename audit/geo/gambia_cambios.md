# Auditoría de PDIs y puntos logísticos · Gambia

Fecha: 2026-09-13 · Entradas: `content/pois/gambia.json` (19 PDIs), `content/ficha/gambia.json` → `logistics` (13 puntos), `audit/geo/gambia_eval.md` / `_eval.json` / `_ref.json`.

**Nota metodológica.** Photon, Nominatim y Overpass están bloqueados desde este contenedor (por `curl`, `CONNECT tunnel failed, response 403`; por WebFetch, `robots.txt`). Toda coordenada nueva procede de fuentes abiertas consultadas en esta sesión:

- **mapcarta.com**, que publica nodos de OpenStreetMap con coordenadas decimales;
- **Logistics Cluster / WFP — Digital Logistics Capacity Assessment (LCA)**, que da GPS oficial y horarios de los pasos fronterizos gambianos;
- **Wikipedia** (en) y **Wikidata**;
- **exteriores.gob.es** (ficha de recomendaciones de viaje de Gambia y páginas de la Embajada en Dakar);
- el extracto OSM ya incorporado en `audit/geo/gambia_ref.json` (nodo `amenity=ferry_terminal` de Banjul);
- **geocoding-api.open-meteo.com** (gazetteer GeoNames) solo para las sugerencias del apartado (e).

No se ha inventado ninguna coordenada. El grueso del encargo eran los puntos de frontera y ferry, y ahí ha habido dos hallazgos que cambian el contenido, no solo el pin: **el cruce litoral de Kartong no admite vehículos** y **España sí tiene representación propia en Gambia**.

---

## (a) Correcciones aplicadas

| id | nombre | lat/lon antes | lat/lon después | dist. | fuente |
|---|---|---|---|---|---|
| log-0 | Frontera Séléti / Giboro | 13.1, -16.52 | **13.17333, -16.57583** | 10,15 km | LCA 2.3.3 *Gambia Giboroh Land Border Crossing*: GPS 13°10'24"N / 16°34'33"W y horario 07:00–22:00 → https://lca.logcluster.org/233-gambia-giboroh-land-border-crossing · contraste OSM: pueblo gambiano **Jiboro** 13.17607/-16.57516 (300 m del punto del LCA) → https://mapcarta.com/Jiboro · pueblo senegalés **Séléti** 13.14543/-16.57751, 3,5 km al sur (`gambia_ref.json`) |
| log-1 | Frontera Darsilami / Dimbaya | 13.0833, -16.7583 | **13.17693, -16.65673** | 15,14 km | OSM **Darsalami** (West Coast Region, Gambia) → https://mapcarta.com/Darsalami · OSM **Dimbaya** (Ziguinchor, Bignona, commune de Kataba I) 13.16954/-16.63477 **con aduana** («Dimbaya customs», police station) → https://mapcarta.com/Dimbaya · el puesto es real y está en Kombo Central: https://thepoint.gm/africa/gambia/headlines/commuters-continue-diverting-darsilami-checkpoint-to-enter-gambia · su contraparte senegalesa es Touba: https://allafrica.com/stories/202310190114.html |
| log-2 | Frontera Amdalai / Karang | 13.4917, -16.5333 | **13.58823, -16.42225** | 16,10 km | OSM **Amdalai** (el de la frontera) → https://mapcarta.com/Amdalai · OSM **Karang Poste** (Fatick, Senegal) 13.60632/-16.42352, 2 km al norte → https://mapcarta.com/Karang · Wikidata Q460354 13.58848/-16.42206 (`gambia_ref.json`) |
| log-4 | Ferry de vehículos Banjul – Barra | 13.4542, -16.5753 | **13.44653, -16.5721** | 0,92 km | Nodo OSM `amenity=ferry_terminal` de **Banjul**, ya presente en `audit/geo/gambia_ref.json` (candidato de poi-9, 0,9 km del centro) · **Barra Ferry Terminal** 13.48493/-16.54576 → https://mapcarta.com/Barra_Ferry_Terminal · control cruzado con Six-Gun Battery 13.45587/-16.57371 → https://mapcarta.com/Six-Gun_Battery |
| log-5 | Puente de Senegambia | 13.49, -15.55 | **13.51616, -15.57244** | 3,79 km | Nodo OSM `Senegambia Bridge` (`gambia_ref.json`) y Wikidata Q60851956 13.51639/-15.5725 · datos del puente: https://en.wikipedia.org/wiki/Senegambia_bridge |
| log-6 | Representación de España en Gambia | 13.4549, -16.579 | **13.47634, -16.68785** | 12,01 km | Dirección oficial *74, Atlantic Boulevard, Fajara, P.O. Box 512 Banjul* → https://www.exteriores.gob.es/Embajadas/dakar/es/Embajada/tambien-somos-tu-embajada-en/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx y https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Gambia · punto tomado en el **nº 64 de Atlantic Boulevard** (nodo OSM de Ngala Lodge, 13.476336/-16.687853, misma calle) → https://mapcarta.com/Ngala_Lodge |
| poi-4 | Makasutu | 13.28, -16.58 | **13.28478, -16.62163** | 4,54 km | Nodo OSM `tourism=attraction` **«Entrance makasutu»** → https://mapcarta.com/Entrance_makasutu |
| poi-7 | Katchikally (Bakau) | 13.4806, -16.6697 | **13.47653, -16.67256** | 0,55 km | Nodo OSM `Kachikally Crocodile Pool` (`gambia_ref.json`). *Refinamiento por debajo del umbral*, aplicado porque la `desc` declaraba «coordenada del centro de Bakau, aproximada» |
| poi-10 | Travesía del río Gambia (ferry) | 13.4667, -16.5667 | **13.44653, -16.5721** | 2,32 km | Misma fuente que log-4. Punto en la **terminal de Banjul** (embarque desde el sur), como se pidió |
| poi-16 | Bao Bolong · acceso | 13.5667, -15.8167 | **13.43895, -15.80732** | 14,24 km | Acceso navegable = **embarcadero de Tendaba** 13.43895/-15.80732 → https://mapcarta.com/Tendaba · la reserva (nodo OSM 13.5201/-15.8638) queda enfrente, en la orilla norte, junto a Njaba Kunda 13.55474/-15.91312 → https://mapcarta.com/Bao_Bolong_Wetland_Reserve y https://mapcarta.com/Njaba_Kunda |
| poi-19 | PN del río Gambia · acceso | 13.6417, -14.9639 | **13.67062, -14.88949** | 8,66 km | Acceso navegable = **Kuntaur** → https://mapcarta.com/Kuntaur (GeoNames 13.67085/-14.88977, https://geocoding-api.open-meteo.com/v1/search?name=Kuntaur) · el embarque al campamento de Badi Mayo del Chimp Rehab se hace desde Kuntaur, 4–4,5 h de coche desde la costa → https://www.accessgambia.com/hotelweb/chimpanzee-rehab-camp.html |

### Puntos comprobados que NO se mueven

- **log-3 · Keur Ayib / Farafenni — VERIFICADO, coordenada correcta.** El evaluador lo marcó `DESPLAZADO` porque la única referencia con nombre coincidente era la ciudad de Farafenni (3 km). Pero el punto de la app (13.5933, -15.6058) es el **puesto fronterizo**: la ficha LCA 2.3.2 lo sitúa en 13°35'27"N / 15°36'20"W = **13.59083 / -15.60556**, a **270 m**, con el nombre gambiano *Keur Ali Farafenni* y el senegalés *Keur Ayib*, a 2,68 km de Farafenni y horario 07:00–22:00 (festivos 08:00–17:00) → https://lca.logcluster.org/232-gambia-faraffeni-land-border-crossing. Se deja la coordenada tal cual para no romper la coherencia con la ficha de Senegal y se anota la verificación en el `info`.
- **log-12 · Agua potable — punto correcto, texto desdoblado.** El `DESPLAZADO` venía de que el nombre mezclaba «Kombos y Tendaba» y Wikidata devolvía Tendaba a 97,3 km. El punto (13.4526, -16.7069) está a 0,5 km del nodo OSM de Kotu, o sea bien. Se ha renombrado a *Kombos (Kotu / Kololi)* y Tendaba pasa al texto con su coordenada (13.43895 / -15.80732) y su distancia real.
- **log-9, log-10, log-11 (combustible) y log-7, log-8 (sanitarios)**: `OK` / `OK?` en el evaluador, sin desplazamiento; los de combustible entran además en la exclusión del punto 6 del encargo.

---

## (b) PDIs eliminados

**Ninguno.** No se ha encontrado ningún PDI inexistente ni ningún nombre que mezcle dos lugares distintos. Los 19 PDIs corresponden a lugares reales y verificables; el único `DUDOSO` del evaluador (poi-10, la travesía del ferry) era un problema de pin, no de existencia.

---

## (c) Puntos NO VERIFICADOS

1. **El portal exacto de la Oficina Diplomática de España (nº 74 de Atlantic Boulevard, Fajara).** Confirmada la calle y el número por fuente oficial, pero no he podido geolocalizar el edificio: Nominatim/Photon bloqueados y mapcarta no tiene nodo ni para la oficina española ni para la Delegación de la UE (con la que comparte edificio según la ficha de Exteriores). El punto queda anclado al nº 64 de la misma calle (Ngala Lodge, nodo OSM con su dirección postal), es decir, a **menos de 200–300 m** del destino. Anotado en el `info`.
2. **Si el paso de Darsilami admite extranjeros y vehículos de matrícula extranjera.** Confirmado que existe el puesto y la aduana senegalesa de Dimbaya, y confirmado que está en una franja con **litigio de demarcación documentado** entre los dos países (militares senegaleses en Darsilameh, acuerdo de 2023 para demarcar en tres años). No he encontrado ninguna fuente que diga que un turista motorizado pueda sellar ahí. Marcado como «CONFIRMAR» en el `info`.
3. **Horario del paso Amdalai / Karang.** No he conseguido abrir la ficha LCA 2.3.1 (ver apartado f); los relatos overland lo describen como trámite de ~30 minutos pero sin horario oficial. El `info` mantiene «horario amplio, cruzar por la mañana».
4. **Peaje del puente de Senegambia.** Sigue sin fuente; se mantiene el «POR CONFIRMAR» y la mención a la disputa entre Gambia Ferries Services y la National Roads Authority, que ya estaba en la ficha.
5. **Cifras de detalle de fauna/superficie** que arrastran los `desc` (612 ha de la reserva de Tanji, 268 especies/62 familias de Bao Bolong, 133 especies de Bijilo, 107 ha de Abuko, 300+ especies de Kiang West). Son coherentes con la literatura habitual y no contradictorias, pero no las he contrastado una a una con la fuente primaria (Ramsar / Departamento de Parques). No se han tocado.
6. **Que el ferry Banjul–Barra esté operativo en 2027.** Es un dato de temporada, no de auditoría; el aviso de confirmarlo la víspera ya estaba y se mantiene.

---

## (d) Correcciones de texto

**Reescrituras de fondo (el dato estaba mal, no solo el pin):**

- **log-6 · «Embajada de España en Banjul (referencia: Dakar)» → «Oficina Diplomática de España en Banjul (Fajara) · demarcación consular: Dakar».** El texto anterior decía que España «no tiene embajada residente» y que «existe representación honoraria — CONFIRMAR». Lo correcto, según Exteriores: existe una **Oficina (antena) Diplomática de España en Banjul**, dependiente de la Embajada de España en Senegal, en 74 Atlantic Boulevard, Fajara (P.O. Box 512), tel. +220 449 6863, fax +220 449 6864, `ant.banjul@maec.es`, con móvil de emergencia +221 77 569 28 89; **además** hay cónsul honorario (`ch.banjul@maec.es`). La **demarcación consular** de Gambia —pasaporte de emergencia, protección consular, documentos— es del **Consulado General de España en Dakar** (Corniche Ouest, Fann-Mermoz, villa nº 7, +221 33 869 07 07), que cubre Senegal y Gambia. Fuentes: https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Gambia · https://www.exteriores.gob.es/Embajadas/dakar/es/Embajada/tambien-somos-tu-embajada-en/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx · https://www.exteriores.gob.es/Embajadas/dakar/es/Embajada/Paginas/Consulados.aspx
  *(Nota: accessgambia.com da una dirección distinta —Bertil Harding Highway, edificio Deloitte/Brussels Airlines, Kololi— y un `emb.banjul@maec.es`. Es un directorio no oficial y probablemente desfasado; se ha usado la fuente del Ministerio.)*
- **log-1 · «Darsilami / Kartong-Allahein (litoral)» → «Darsilami / Dimbaya (pista de Kombo Central)».** El texto anterior dejaba abierto «si existe paso practicable con vehículo» en Kartong. **No existe.** El cruce del Allahein en Kartong es una **piragua de pasajeros** de unos diez minutos: hay sello de salida gambiano en la oficina de inmigración de Kartong, pero **no hay puesto de entrada senegalés**, de modo que hay que regularizar la entrada después en Séléti o Darsilami — y hay avisos recientes de que la inmigración senegalesa ha empezado a rechazar esa vía. Ninguna de las dos crónicas de primera mano menciona barcaza ni ferry de vehículos. Fuentes: https://scootwestafrica.com/smuggler-crossing-gambia-casamance/ · https://travelwithzoe.org/2019/05/22/gambia-to-senegal-unofficial-border-crossing/
- **log-0 · nombre** ampliado a «Séléti / Giboro» y `info` con los dos topónimos, sus coordenadas y el horario 07:00–22:00 del LCA. Se retira «COORDENADA APROXIMADA».
- **log-2 · `info`**: añadido el aviso de que **hay más de un Amdalai en Gambia** (ver apartado f), la coordenada del puesto senegalés de Karang Poste, y corregido «~30 km desde Barra» → «unos 20 km» (Barra–Amdalai son 17,7 km en línea recta).
- **log-3 · `info`**: añadida la verificación con la ficha LCA (nombres oficiales, GPS, horarios, 2,68 km de Farafenni).
- **log-4 · `info`**: «~4 km» → «unos 5 km» (la distancia real entre las dos terminales es 5,13 km); se explicita que el punto es la terminal de Banjul y se da la de Barra.
- **log-5 · `info`**: retirada la precisión «942 m sobre el río», que no he podido confirmar; Wikipedia da 1,9 km de longitud total, 21 de enero de 2019, 93 M$ de coste con 65 M$ del BAfD, Isolux Corsán + grupo Arezki, sustitución del ferry con esperas de 10–20 días. Todo lo demás del texto queda confirmado. Fuente: https://en.wikipedia.org/wiki/Senegambia_bridge
- **log-12 · nombre e `info`**: el nombre ya no promete Tendaba en el pin; Tendaba aparece en el texto con coordenada y con los 97 km reales.

**Ajustes menores en PDIs:**

- **poi-4 Makasutu**: fuera «Coordenada aproximada — confirmar sobre el terreno»; ahora el texto dice que el punto es la entrada señalizada junto a la carretera de Brikama y que el Mandina Lodge queda dentro, por pista.
- **poi-7 Katchikally**: fuera «Coordenada del centro de Bakau, aproximada»; ahora es el nodo de la poza.
- **poi-10**: «unos 4 km de estuario» → «unos 5 km»; añadida la aclaración de qué terminal marca el punto y la coordenada de la de Barra.
- **poi-16 Bao Bolong**: «a unos 18 km de Farafenni» → «aguas abajo de Farafenni». El nodo OSM de la reserva está a **28 km** al oeste de Farafenni en línea recta, así que los 18 km no se sostienen y tampoco hay una cifra alternativa fiable (la reserva son 220 km², el borde oriental sí puede estar a ~18 km). Añadida la explicación del pin (embarcadero de Tendaba) y la aproximación por la orilla norte.
- **poi-18 Wassu**: verificado contra Wikipedia —**11 círculos**, columna más alta de **2,59 m**, túmulos datados en **927–1305 d. C.**, inscripción UNESCO **2006**, Kerr Batch con **nueve círculos y uno doble**—. Corregido un solo dato: «KERR BATCH, **40 km** al oeste» → «**22 km** al oeste en línea recta (bastante más por la pista de la orilla norte)», porque Wassu (13.6914/-14.8731) y Kerr Batch (13.75427/-15.06945) están a 22,4 km. Fuente: https://en.wikipedia.org/wiki/Senegambian_stone_circles
- **poi-19**: añadido «hoy rondan el centenar» (Wikipedia da ~100 chimpancés en cuatro grupos sobre tres islas) y la explicación del acceso por Kuntaur. Se mantiene intacto el aviso de que el parque **no está abierto al público**, que es el dato más valioso de la ficha y está bien traído. Fuente: https://en.wikipedia.org/wiki/Chimpanzee_Rehabilitation_Project

---

## (e) Interés de los PDIs y sugerencias

**Funcionan muy bien para una expedición overland con perro:** poi-2 (Tanji), poi-6 (Kotu/Bakau como base logística real), poi-12 + poi-13 (Juffureh/Albreda + Kunta Kinteh, con el matiz honesto sobre la genealogía de *Raíces*), poi-15 (Kiang West/Tendaba), poi-17 (Janjanbureh) y poi-18 (Wassu). El bloque UNESCO del estuario y el bloque megalítico del río alto son lo que justifica subir por el interior en vez de cruzar Gambia en seis horas.

**Flojos o redundantes, para que decidas:**

- **poi-5 · Bijilo Forest Park.** Es el más prescindible del país: 51 ha valladas, perro prohibido, monos habituados y, según el propio texto, perdió parte de su estatus de reserva en 2018 por un centro de congresos. Está a 3 km de poi-6 y a 5 de poi-8. Si hay que adelgazar los Kombos, este es el candidato: se puede fundir en poi-6 como una línea («detrás de Kololi hay un bosque vallado con monos»).
- **Densidad del conurbano.** poi-5, poi-6, poi-8 y poi-9 son cuatro puntos en unos 12 km. Ninguno sobra del todo (Serrekunda es la base mecánica y veterinaria; Banjul, el ferry y el hospital), pero el mapa queda apelmazado.
- **poi-1 · Kartong.** Ahora que está claro que no es una frontera utilizable con vehículo, su valor se reduce a playa vacía + Folonko + ecoturismo. Se sostiene por el perro (arena abierta, sin gestión de parque), pero conviene que el texto no sugiera entrar por ahí: la frase «si se entra por el paso litoral en vez de por Séléti» debería matizarse en una revisión posterior de estilo — no la he tocado porque el encargo pedía no reescribir por estilo, pero queda avisado.
- **poi-19 · PN del río Gambia.** Con el parque cerrado al público y la navegación restringida, es más una advertencia que un destino. Vale la pena mantenerlo exactamente por eso (evita que alguien planifique una visita imposible), pero con prioridad Media está bien y no subiría.
- **poi-16 y poi-15** comparten base, excursión y ahora zona de pin. Se sostienen como dos salidas distintas (parque terrestre vs. manglar en piragua) y los textos lo dicen, pero si prefieres un solo punto, poi-16 se puede absorber dentro de poi-15.

**Tres lugares que faltan (coordenadas verificadas en esta sesión):**

1. **Kerr Batch · círculos de piedra (UNESCO)** — **13.75427, -15.06945** (OSM, pueblo con los círculos y su museo → https://mapcarta.com/Kerr_Batch; Wikipedia da 13°45′16″N 15°04′05″W → https://en.wikipedia.org/wiki/Senegambian_stone_circles). Es el segundo sitio gambiano del Patrimonio Mundial megalítico, con **nueve círculos, uno doble y la única piedra bífida en V de toda la región**, y hoy solo aparece como coletilla dentro de poi-18. Está en la orilla norte, en el mismo eje Kuntaur–Wassu–Farafenni que ya recorre la ruta: merece punto propio.
2. **Bintang Bolong** — **13.25085, -16.21204** (OSM, con el *Bintang Bolong Lodge* pegado al nodo → https://mapcarta.com/Bintang_Bolong). Brazo de manglar sobre la carretera sur, entre los Kombos y Tendaba, con alojamiento sobre pilotes y salidas en piragua. Es exactamente la parada intermedia que le falta al tramo Brikama–Tendaba (150 km sin nada en la ficha) y es terreno abierto, cómodo con perro.
3. **Sanyang · playa** — **13.26667, -16.76056** (GeoNames/open-meteo, pueblo; la playa queda 2–3 km al oeste y habría que afinar el pin sobre el terreno o con OSM cuando haya red). Playa larga con campamentos y chiringuitos, mucho menos edificada que Kololi y a medio camino entre Tanji y Kartong: la mejor opción de la costa para dormir con el perro sin meterse en la franja hotelera.

*(Las tres son sugerencias: no se ha añadido nada a `content/pois/gambia.json`.)*

---

## (f) Fuentes abiertas que fallaron y trampas encontradas

**Bloqueos de red (por eso no hay ni una sola consulta directa a OSM):**

| fuente | resultado |
|---|---|
| `photon.komoot.io`, `nominatim.openstreetmap.org`, `overpass-api.de` | `curl`: CONNECT tunnel failed 403 · WebFetch: `ROBOTS_DISALLOWED` |
| `www.openstreetmap.org/search`, `api.openstreetmap.org/api/0.6/...` | `ROBOTS_DISALLOWED` |
| `overpass.kumi.systems`, `overpass.monicz.dev` | read timeout (3 intentos entre los dos) |
| `overpass.osm.ch` | responde correctamente pero **solo indexa Suiza**: devuelve `elements: []` para Gambia |
| `overpass.osm.jp` | certificado TLS inválido (hostname mismatch) |
| `api.openstreetmap.fr`, `overpass.nchc.org.tw` | DNS no resuelve |
| `maps.mail.ru/osm/tools/overpass` | dominio en lista de bloqueo del proxy |
| `lca.logcluster.org/231-gambia-amdallai-land-border-crossing` | `PROVENANCE_REQUIRED` (2 intentos) — es la única ficha LCA de frontera que no he podido leer |
| `lca.logcluster.org/23-gambia-border-crossing`, `.../print-preview-entire-book/516` | 403 |
| `wca.iom.int`, `embassypages.com` | 403 |
| `geocode.xyz` | *Throttled* en todos los campos |
| `fr.wikipedia.org/wiki/Karang_(Sénégal)`, `en.wikipedia.org/wiki/Karang,_Senegal`, `en.wikipedia.org/wiki/Wassu_Stone_Circles` | «cache-only» / 404 — resueltos por otras vías (mapcarta y *Senegambian stone circles*) |
| `mapcarta.com/Seleti`, `/Giboro`, `/Makasutu`, `/Makasutu_Culture_Forest`, `/Banjul_Ferry_Terminal`, `/Amdallai`(→ redirige bien), `/Dimbaya_customs_post` | 404 o resolución a otro topónimo; resueltos probando variantes (`/Jiboro`, `/Entrance_makasutu`, `/Dimbaya`, `/Barra_Ferry_Terminal`) |

**Dos trampas de datos que conviene dejar por escrito:**

1. **Los Amdalai.** `en.wikipedia.org/wiki/Amdalai` da 13°25′55″N 16°43′21″W = **13.43194 / -16.72250** y lo sitúa en *Kombo North/Saint Mary District* — o sea, en los Kombos, al **sur** del río. Ése **no** es el paso fronterizo. El de la frontera es el nodo OSM 13.58823 / -16.42225, en la orilla norte, a 2 km de Karang Poste. Peor aún: mapcarta mezcla la **prosa de Wikipedia** («Kombo North/Saint Mary District») con las **coordenadas del nodo OSM** correcto, así que su ficha de Amdalai se lee contradictoria. El evaluador ya ofrecía además un tercer *Amdalai* a 13.2114/-16.4923. Lo he anotado en el `info` de log-2.
2. **`mapcarta.com/Seleti` devuelve Silety, Kazajistán** (52.96 N, 73.90 E). El slug no resuelve el topónimo senegalés, y si no se comprueba el país se firma una coordenada catastrófica. La coordenada buena de Séléti viene de `gambia_ref.json` (OSM 13.14543/-16.57751) y la del puesto, del LCA.

---

## Validación

```
python3 -c "import json;json.load(open('content/pois/gambia.json'));json.load(open('content/ficha/gambia.json'))"  → OK
git diff --numstat content/pois/gambia.json content/ficha/gambia.json  → 16/16 y 24/24 líneas
```

- `content/pois/gambia.json`: 16 líneas = 5 PDIs movidos × (lat + lon + desc) + 1 línea de `desc` de poi-18.
- `content/ficha/gambia.json`: 24 líneas = log-0 (name+lat+lon+info) + log-1 (4) + log-2 (3) + log-3 (1) + log-4 (3) + log-5 (3) + log-6 (4) + log-12 (2).
- Formato respetado (`ensure_ascii=False, indent=2` y `indent=2`), salto de línea final restaurado, coordenadas redondeadas a 5 decimales. No se ha tocado ninguna otra clave ni ningún otro país.

# Auditoría de PDIs y puntos logísticos · Marruecos

Entradas: `content/pois/marruecos.json` (14 PDIs), `content/ficha/marruecos.json → logistics`
(11 puntos), `audit/geo/marruecos_eval.md` + `marruecos_eval.json`.

Veredictos de partida: 11 OK · 2 OK? · 4 DUDOSO · 7 DESPLAZADO · 1 SIN_REF.

Archivos editados: solo `content/pois/marruecos.json` y `content/ficha/marruecos.json`.

---

## (a) Correcciones aplicadas

| id | nombre | antes (lat, lon) | después (lat, lon) | dist. | fuente |
|---|---|---|---|---|---|
| poi-5 | Garganta del Todra | 31.58100, -5.58090 | **31.58735, -5.59150** | 1,23 km | OSM vía [mapcarta.com/Todgha_Gorge](https://mapcarta.com/Todgha_Gorge) · contraste [SummitPost 31.58834/-5.59384](https://www.summitpost.org/todra-gorge/152570) · [en.wikipedia Todgha Gorge](https://en.wikipedia.org/wiki/Todgha_Gorge) |
| poi-8 | Puerto de Tizi n'Test | 30.86970, -8.35630 | **30.86822, -8.37889** | 2,16 km | nodo OSM `mountain_pass=yes` «Tizi n'Test» (marruecos_eval.json), con el `amenity=cafe` homónimo en el mismo punto; altitud 2 093 m en [en.wikipedia Tizi-n-Test pass](https://en.wikipedia.org/wiki/Tizi-n-Test_pass) |
| poi-11 | Arco de Legzira | 29.34520, -10.12630 | **29.44362, -10.11792** | 10,97 km | OSM `natural=beach` «Plage Legzira» (marruecos_eval.json) · caserío de acceso en la N1 [mapcarta.com/Legzira 29.4465/-10.1156](https://mapcarta.com/Legzira) |
| poi-13 | Parque Nacional de Khnifiss | 27.97000, -12.34000 | **28.02840, -12.23990** | 11,78 km | desvío señalizado «Naila» a pie de la N1, aparcamiento de tierra al borde de la laguna: [park4night nº 31602](https://park4night.com/en/place/31602) · el centroide del polígono OSM (27.9859/-12.3671, [mapcarta W396292244](https://mapcarta.com/W396292244)) queda fuera de la carretera |
| log-0 | Tánger Med (ferry) | 35.90100, -5.51500 | **35.87794, -5.51435** | 2,56 km | OSM `amenity=ferry_terminal` «Port Passagers Tanger Med» (marruecos_eval.json; [mapcarta W178877454](https://mapcarta.com/W178877454)) |
| log-1 | Límite administración marroquí / Sáhara | 27.66000, -13.20000 | **27.67200, -12.95630** | 24,04 km | el punto anterior caía ~24 km al oeste de la N1 (mar/hamada); referencia real: aldea de **Tah**, en la N1 sobre el paralelo 27°40′N — [mapcarta 25436978](https://mapcarta.com/25436978) |
| log-2 | Embajada de España en Rabat | 33.98320, -6.85580 | **33.96008, -6.82389** | 3,91 km | nodo OSM `office=diplomatic` «Embassy of Spain»; corroborado por la [Pharmacie Yamina, rue Aïn Khalouiya, 33.9591/-6.82332, con la embajada 110 m al NO](https://mapcarta.com/W611325366) · dirección oficial [exteriores.gob.es Rabat](https://www.exteriores.gob.es/Embajadas/rabat/es/Embajada/Paginas/Contacto.aspx) |
| log-3 | Consulado General en Tánger | 35.77670, -5.80430 | **35.78003, -5.82381** | 1,80 km | nodo OSM `office=diplomatic` «Consulado General de Espana» (marruecos_eval.json); parada de bus homónima [mapcarta N5000037824](https://mapcarta.com/N5000037824) · dirección [exteriores.gob.es Tánger](https://www.exteriores.gob.es/Consulados/tanger/es/Consulado/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx) |
| log-4 | Consulado General en Casablanca | 33.58830, -7.61140 | **33.59025, -7.62520** | 1,30 km | OSM way 415668650 `office=diplomatic` «Consulat d'Espagne», 120 m al SO de la catedral del Sagrado Corazón ([mapcarta W415668650](https://mapcarta.com/W415668650)) |
| log-5 | Consulado General en Agadir | 30.42020, -9.59820 | **30.42170, -9.58642** | 1,14 km | OSM way 663781154 «Consulat d'Espagne», con la sección de visados 130 m al este ([mapcarta W663781154](https://mapcarta.com/fr/W663781154)) |
| log-6 | Hôpital Ibn Sina — Rabat | 34.00680, -6.83060 | **33.98268, -6.85210** | 3,33 km | nodo OSM `amenity=hospital` «Hopital Ibn Sina / CHU Ibn Sina» ([mapcarta N1824603903](https://mapcarta.com/N1824603903)); Wikidata Q30253994 a 0,2 km |
| log-7 | Hôpital Militaire Avicenne — Marrakech | 31.61830, -8.00640 | **31.63475, -8.02171** | 2,33 km | OSM way 789241701 `amenity=hospital` ([mapcarta W789241701](https://mapcarta.com/W789241701)); Wikidata Q30281418 a 0,05 km |
| log-8 | Hospital de Agadir → **CHU Mohammed VI** | 30.42780, -9.59810 | **30.41096, -9.53499** | 6,33 km | OSM way 416680855 «centre hospitalier universitaire», junto a la Facultad de Medicina Ibn Zohr ([mapcarta W416680855](https://mapcarta.com/W416680855)) |

Coordenadas redondeadas a 5 decimales. Ambos JSON validan con `json.load`.

### Detalle de los casos con trampa

- **poi-5 (DUDOSO, «sin referencia útil»)**: Photon devolvió tres gargantas de la provincia de
  Cádiz a ~507 km. La garganta real (Gorges du Todgha / Todra, comuna de Toudgha El Oulia, al
  norte de Tinghir) está en 31.58735 / -5.59150 según OSM, coincidente a 0,2 km con la ficha de
  SummitPost. El punto anterior estaba 1,2 km al SE, en el palmeral de acceso, no en el
  estrechamiento. No es una alucinación: el lugar existe y el PDI se mantiene.
- **poi-8**: el `boundary=administrative` homónimo (30.83339/-8.45115, 9,9 km) es la comuna, no
  el collado. El collado real es el nodo `mountain_pass=yes` a 30.86822/-8.37889, donde OSM
  sitúa también el café de la cima. Mapcarta da 30.86464/-8.37795 para el mismo paso (400 m al
  sur, sobre la misma carretera): la diferencia es irrelevante para navegar.
- **log-4 (Casablanca)**: los candidatos de Photon eran los consulados de Senegal, Filipinas y
  EE. UU. El consulado español sí está en OSM, pero con el nombre «Consulat d'Espagne», que no
  casa por tokens con «Consulado General de España en Casablanca». Además la dirección de la app
  («31, Rue d'Alger») está obsoleta: la oficina se trasladó desde la rue d'Alger a **14, Bd. de
  Paris, 4ª planta, 20070** ([aviso oficial de traslado](https://www.exteriores.gob.es/Consulados/casablanca/es/Comunicacion/Noticias/Paginas/Articulos/20140320_NOT01.aspx),
  [ficha de contacto](https://www.exteriores.gob.es/Consulados/casablanca/es/Consulado/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx)).
- **log-5 (Agadir)**: Photon devolvió «Ambassy of Spain» de Rabat a 476 km. El consulado de
  Agadir existe y la dirección de la app (49, rue Ibn Batouta, secteur mixte) es correcta; se
  añade el apartado de correos y se corrige el teléfono al oficial (+212 528 299 140, antes
  «528 84 56 81/71»), más el móvil de emergencia consular 24 h
  ([exteriores.gob.es Agadir](https://www.exteriores.gob.es/Consulados/agadir/es/Consulado/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx)).
- **log-8 (falso positivo «OK»)**: el candidato «Hôpital Hassan II» que validó el veredicto está
  en **Beni Mellal**, a 374 km; lo único cercano era una farmacia homónima a 1,4 km. El Hôpital
  Hassan II de Agadir sí existe, en 30.43628 / -9.59078 ([mapcarta 29430260](https://mapcarta.com/29430260)),
  1,2 km del punto de la app. **Pero cierra a finales de marzo de 2026 para una reconstrucción
  de 1 100 M MAD y las urgencias y partos se derivan al CHU Mohammed VI de Agadir**
  ([Le Matin](https://lematin.ma/regions/fermeture-temporaire-hopital-hassan-ii-agadir/336300)),
  inaugurado en noviembre de 2025 ([Médias24](https://medias24.com/2025/11/03/le-roi-inaugure-le-chu-international-de-rabat-et-ordonne-louverture-du-chu-dagadir/)).
  Para un viaje en 2027 el punto útil es el CHU, así que se ha cambiado **nombre, coordenadas e
  info**, dejando la coordenada del Hassan II citada en el texto por si reabre.
- **log-1 (DUDOSO)**: no era solo una referencia mala — el punto (27.66 / -13.20) cae unos 24 km
  al oeste de la N1 a esa latitud, fuera de la carretera. Se reubica en Tah, la aldea de la N1
  justo sobre el paralelo 27°40′N que marcaba el límite del antiguo Sáhara español, coherente
  con lo que el texto describe.

---

## (b) PDIs eliminados

Ninguno. Los 14 PDIs corresponden a lugares reales y localizados; no se ha detectado ninguna
alucinación ni mezcla de dos lugares.

---

## (c) Puntos NO VERIFICADOS / verificados sin cambio

- **poi-10 «Tafraout y valle de Ameln» (OK?)** — **verificado, sin cambio**. El punto de la app
  (29.7181 / -8.9770) cae a 0,36 km del núcleo de Tafraout según OSM (29.7205 / -8.9745,
  [mapcarta.com/Tafraout](https://mapcarta.com/Tafraout)). Los candidatos que dieron el «OK?»
  eran un camping y un gîte del valle, no el pueblo.
- **poi-5, altura de las paredes**: la app dice «hasta 300 m». Wikipedia en inglés da 160 m en el
  tramo más espectacular y «hasta 400 m» en algunos puntos, así que la cifra queda dentro del
  rango documentado y se deja como está.
- **poi-8, altitud «2 092 m»**: Wikipedia da 2 093 m y mapcarta 2 100 m. Diferencia irrelevante;
  no se toca.
- **log-9 (combustible) y log-10 (agua potable)**: puntos genéricos representativos, no se tocan
  por indicación del encargo (auditoría de agua y combustible).
- **Estado de la carretera del Tizi n'Test tras el terremoto de Al Haouz (sept. 2023)**: NO
  VERIFICADO. El eje Marrakech–Asni–Ouirgane–Tin Mal sufrió daños graves y hay reportes de
  cortes y obras posteriores, pero no he podido confirmar con fuente oficial el estado a 2026/27,
  así que no se ha añadido nada al `desc`. Conviene comprobarlo antes de planificar ese tramo.

---

## (d) Correcciones de texto

| id | qué decía | qué dice ahora | motivo / fuente |
|---|---|---|---|
| poi-3 | «La medina medieval **más grande y viva del mundo árabe**» | «Medina medieval viva y **una de las mayores zonas urbanas sin tráfico del mundo (unas 300 ha)**» | El superlativo «la más grande del mundo árabe» no es verificable; lo documentado es la superficie peatonal ([en.wikipedia Fes el Bali](https://en.wikipedia.org/wiki/Fes_el_Bali)) |
| poi-11 | «uno de los dos [arcos] colapsó **en 2020**» | «el mayor de los dos arcos se derrumbó **en septiembre de 2016**» + acceso desde la N1 por el caserío de Legzira | Fecha errónea: el derrumbe fue el 23–25 de septiembre de 2016 ([Morocco World News](https://www.moroccoworldnews.com/2016/09/106188/legzira-beachs-archways-crumble/), [Natural Arch and Bridge Society](https://www.naturalarches.org/blog/major-arch-collapse-at-legzira-beach-morocco/)) |
| poi-13 | «humedal Ramsar» | «humedal Ramsar **desde 1980**» + referencia al desvío señalizado «Naila» de la N1 | Sitio Ramsar nº 209 «Baie de Khnifiss», designado el 20/06/1980; es efectivamente la mayor laguna costera de Marruecos ([en.wikipedia Khenifiss National Park](https://en.wikipedia.org/wiki/Khenifiss_National_Park)) |
| log-0 | — | se añade que el punto es la terminal de pasajeros, no las de contenedores | evita confundir con Tanger Med II (TC3/TC4), que quedan 3–5 km al oeste |
| log-1 | — | se añade la referencia a Tah y al paralelo 27°40′N | coherencia con la nueva coordenada |
| log-2 | «Rue Aïn Khalouiya, Rte. des Zaërs, Km. 5 … Coordenada urbana aproximada» | «3, Rue Aïn Khalouiya, Av. Mohammed VI (antigua Rte. des Zaërs), km 5,3, Souissi, 10170 Rabat» | dirección oficial actual; la Rte. des Zaërs pasó a llamarse Av. Mohammed VI |
| log-3 | «85, Av. Président Habib Bourguiba» | «85, Av. Président Habib Bourguiba, **90040 Tánger**» | código postal oficial |
| log-4 | «31, Rue d'Alger» | «14, Bd. de Paris, 4ª planta, 20070 Casablanca…» | sede trasladada (ver arriba) |
| log-5 | teléfono «+212 528 84 56 81/71» | «+212 528 299 140; emergencia consular 24 h +212 661 080 470» + B.P. 3179 | teléfonos oficiales actuales |
| log-6 / log-7 / log-8 | «Coordenada urbana aproximada» | se retira la coletilla y se sitúa el barrio (Souissi / L'Hivernage / salida SE de Agadir) | las coordenadas ya son del nodo del hospital |

---

## (e) Interés de los PDIs y sugerencias

**Sólidos para una expedición overland con perro**: poi-4 Erg Chebbi (dunas de hasta 150 m,
confirmado en [en.wikipedia Erg Chebbi](https://en.wikipedia.org/wiki/Erg_Chebbi)), poi-5 Todra,
poi-8 Tizi n'Test, poi-6 Aït Benhaddou, poi-11/12 Legzira–Sidi Ifni, poi-13 Khnifiss. Todos son
paisaje o patrimonio al aire libre, compatibles con perro y con vivac o camping cercano.

**Flojos o con fricción**:

- **poi-3 Fez el Bali** y **poi-7 Marrakech** son paradas urbanas con el perro «requiere
  autorización escrita» / «con condiciones»: en la práctica significan dejar al animal en el
  vehículo o en el alojamiento. Su valor real aquí es logístico (talleres, recambios, hospitales,
  vuelos). Merece la pena mantenerlos, pero el propietario debería saber que como «visita» son
  los más incómodos del país con perro.
- **poi-9 Essaouira** y **poi-12 Sidi Ifni** repiten categoría «Costa» y función (medina + puerto
  pesquero + playa). Si hay que recortar días, Essaouira es la prescindible: Sidi Ifni añade el
  vínculo con el enclave español y es la última ciudad con servicios completos antes de Guelmim.
- **poi-14 Tarfaya** es casi puramente logístico (repostaje, descanso); bien como está en
  prioridad «Media».
- **poi-1 Chefchaouen** obliga a un desvío de ida y vuelta desde el eje Tánger Med–Fez; se
  justifica solo como parada de aclimatación, como ya dice el `desc`.

**Hasta tres PDIs de gran interés que faltan** (coordenadas verificadas, decisión del
propietario):

1. **Gargantas del Dadès (Boumalne Dadès)** — 31.53542 / -5.91793
   ([mapcarta 17451944](https://mapcarta.com/17451944)). El propio `desc` de poi-5 ya invita a
   «combinar con Dades para un bucle de gargantas», pero Dadès no existe como PDI. Carretera
   asfaltada espectacular (las «curvas del Dadès»), campings a pie de río y sombra: probablemente
   el mejor sitio del sureste para pasar la noche con perro.
2. **Amtoudi (agadir/granero fortificado de Id Aïssa), Anti-Atlas** — 29.24274 / -9.18395
   ([mapcarta.com/Amtoudi](https://mapcarta.com/Amtoudi)). Pueblo bereber a 876 m con el granero
   colectivo mejor conservado del Anti-Atlas y un cañón con palmeral; encaja en el tramo
   Tafraout–Guelmim, es 100 % exterior y admite perro sin restricción conocida.
3. **Parque Nacional de Souss-Massa (sede del parque)** — 30.36754 / -9.56185
   ([mapcarta 33095452](https://mapcarta.com/33095452)). A 14 km de Agadir, sobre el eje hacia
   Tiznit: dunas, desembocadura del Massa, ibis eremita y órix reintroducido. Ojo: como en
   Khnifiss, el acceso con perro a la zona núcleo habría que confirmarlo con Aguas y Bosques, y
   por eso lo dejo como sugerencia y no como alta prioridad.

---

## (f) Fuentes abiertas que fallaron

- `curl` directo desde el contenedor: bloqueado por la política de egress del proxy (403 en
  CONNECT) para `*.wikipedia.org`, `www.exteriores.gob.es`, etc. Todo se ha resuelto con WebFetch.
- `nominatim.openstreetmap.org`, `www.openstreetmap.org/search`, `www.openstreetmap.org/node|way`,
  `photon.komoot.io`, `overpass-api.de` (y los espejos `z.` y `lz4.`), `maps.mail.ru`,
  `overpass.nchc.org.tw`: **robots.txt** los deja fuera de WebFetch.
- `overpass.kumi.systems` y `overpass.private.coffee`: *read timeout* repetido.
- `overpass.osm.ch`: responde, pero solo sirve el extracto de Suiza (0 elementos en Marruecos).
- `www.wikidata.org/w/api.php`: «cache-only domain».
- `fr.wikipedia.org/wiki/Tizi_n'Test` y `en.wikipedia.org/wiki/Tizi_n'Test`: «cache-only»
  (resuelto con `en.wikipedia.org/wiki/Tizi-n-Test_pass`).
- `fr.wikipedia.org/wiki/Gorges_du_Todgha`: carga, pero la conversión a markdown pierde la
  geolocalización de la ficha (resuelto con OSM/mapcarta + SummitPost).
- `climbingaway.fr`: devuelve página vacía.
- `www.embassypages.com`: HTTP 403.
- `www.chusm.ma`: fallo de verificación TLS al leer su robots.txt.

**Vía que sí funciona como sustituto de Photon/Overpass**: `mapcarta.com`, que publica los nodos
y ways de OSM con sus coordenadas y las entidades próximas con distancia y rumbo — muy útil para
triangular (así se ha confirmado, por ejemplo, la embajada de Rabat a 110 m de la farmacia de la
rue Aïn Khalouiya).

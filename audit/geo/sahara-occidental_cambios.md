# Auditoría de PDIs y logística · Sáhara Occidental

Encargo `audit/geo/PROMPT_PDI.md`, slug `sahara-occidental`.
Entradas: `content/pois/sahara-occidental.json` (16 PDIs), `content/ficha/sahara-occidental.json → logistics`
(14 puntos), `audit/geo/sahara-occidental_eval.md` / `_eval.json`.

Veredicto de partida: 11 OK · 11 DESPLAZADO · 6 DUDOSO · 1 OK? · 1 SIN_REF.
Se han corregido **14 puntos** (8 PDIs + 6 logísticos), **ninguno se ha eliminado** y quedan
**3 anotados como no verificados**. Coordenadas redondeadas a 5 decimales; los dos JSON validan
con `json.load`.

> Nota de método: desde este contenedor el proxy bloquea Photon, Nominatim, Overpass y
> `wikidata.org`, y `openstreetmap.org` está vetado por `robots.txt`. Todas las coordenadas
> nuevas salen de **Wikipedia**, de **mapcarta.com** (que publica el nodo/vía de OpenStreetMap
> con su id), de los candidatos OSM ya capturados en `_eval.json` de la pasada anterior, o de
> **publicaciones científicas y páginas oficiales**. Ninguna coordenada se ha escrito de memoria.

---

## (a) Correcciones aplicadas

| id | nombre | antes (lat/lon) | después (lat/lon) | distancia | fuente |
|---|---|---|---|---|---|
| poi-3 | Bu Craa | 26.32280 / -12.84970 | **26.35760 / -12.84435** | 3,91 km | nodo OSM `place=village` «Boucraa» **node 702231247** ([mapcarta.com/Bou_Craa](https://mapcarta.com/Bou_Craa)) — ver justificación abajo |
| poi-4 | Lemsid | 26.72000 / -13.63000 | **26.53933 / -13.83683** | 28,74 km | nodo OSM `place=village` «Lemseid» (`_eval.json`); Wikidata Q6521520 a 1,1 km |
| poi-6 | La Duna Blanca | 23.60000 / -15.85000 | **23.80284 / -15.73619** | 25,36 km | marcador del acceso «White Dune / White Dune Canyon, El Argoub» en [Travelocity](https://www.travelocity.com/El-Argoub-Hotels-White-Dune-Canyon.h105996534.Hotel-Information) y [Expedia](https://www.expedia.com/White-Dune-El-Argoub.d942182899437076480.Vacation-Attraction) (23.80284/-15.73619); la duna en sí, 23.822/-15.7448 según [MaJourneys](https://majourneys.com/en/dakhla/locations/white-dune-dakhla) |
| poi-9 | Kitesurf y spots de Dajla | 23.73000 / -15.92000 | **23.90167 / -15.78510** | 23,51 km | nodo OSM «PK25 Dakhla» (`_eval.json`), corroborado por [Kite Jungle · Dakhla Lagoon PK 25](https://kitejungle.com/kite-places/western-sahara/dakhla-lagoon-pk-25) (23.90009/-15.78720, 250 m) |
| poi-10 | Bir Gandouz | 21.01700 / -16.31700 | **21.61373 / -16.47107** | 68,25 km | nodo OSM `place=village` «Bir Gandus» (`_eval.json`); [en.wikipedia Bir Gandus](https://en.wikipedia.org/wiki/Bir_Gandus) 21°37′N 16°28′W; Wikidata Q2637709 a 0,3 km |
| poi-13 | Sebja de Imlili | 23.15000 / -15.85000 | **23.27681 / -15.91526** | 15,60 km | mirador OSM «Fish Pools» **node 6349333834** ([mapcarta.com/Fish_Pools](https://mapcarta.com/Fish_Pools)); coincide a 40 m con la poza nº 35 muestreada en [Parasite 2022](https://www.parasite-journal.org/articles/parasite/full_html/2022/01/parasite220122/parasite220122.html) (23°16′35,21″N 15°54′55,47″W) |
| poi-14 | Fuentes termales de Asmaa | 23.85000 / -15.80000 | **23.90271 / -15.78710** | 6,01 km | único `natural=spring` «Hot spring» cartografiado en la zona (`_eval.json`; confirmado como vecino de [DreamKite](https://mapcarta.com/N6181547543) y [Dakhla Attitude](https://mapcarta.com/N5249527142)). **Punto NO VERIFICADO**, ver (c) |
| poi-16 | Cabo Blanco y La Güera | 20.83330 / -17.08330 | **20.77139 / -17.04722** | 7,84 km | Wikidata Q1520946 «Cabo Blanco, cabo atlántico entre Sáhara Occidental y Mauritania» (referencia de `_eval.json`); contexto en [fr.wikipedia Cap Blanc (Mauritanie)](https://fr.wikipedia.org/wiki/Cap_Blanc_(Mauritanie)) |
| log-2 | Salida (subida) · Smara → Tan-Tan | 27.93940 / -12.92310 | **26.74358 / -11.66455** | 182,02 km | nodo OSM `place=city` «Smara» (`_eval.json`); Wikidata Q842810 a 0,7 km |
| log-3 | Hospital regional de El Aaiún | 27.14500 / -13.19500 | **27.15672 / -13.18926** | 1,42 km | [near-place · Hôpital Moulay Hassane Ben Mehdi, El-Aaiún](https://eh.near-place.com/hopital-moulay-hassane-ben-mehdi-laayounne-maroc/en) (27.156723/-13.1892582); nombre oficial en el [informe del Tribunal de Cuentas sobre el CHR de Laâyoune](https://www.courdescomptes.ma/wp-content/uploads/2023/01/16.-Hopital-regional-Laayoune.pdf) |
| log-4 | Hospital — Dajla | 23.68450 / -15.93500 | **23.71409 / -15.92269** | 3,52 km | vía OSM `amenity=hospital` «General Hospitals of Dakhla / Hôpital Hassan II» **way 251776350** ([mapcarta W251776350](https://mapcarta.com/W251776350)) |
| log-5 | Consulado de España — Agadir | 30.42020 / -9.59820 | **30.42170 / -9.58642** | 1,14 km | vía OSM `office=diplomatic` «Consulat d'Espagne» **way 663781154** ([mapcarta W663781154](https://mapcarta.com/fr/W663781154)); dirección oficial en [exteriores.gob.es · Agadir](https://www.exteriores.gob.es/Consulados/agadir/es/Consulado/Paginas/Horario,-localizaci%C3%B3n-y-contacto.aspx). Coincide con lo fijado en `marruecos_cambios.md` (log-5) |
| log-7 | Combustible · Lemsid | 26.72000 / -13.63000 | **26.53933 / -13.83683** | 28,74 km | igual que poi-4 |
| log-10 | Combustible · Bir Gandouz | 21.01700 / -16.31700 | **21.61373 / -16.47107** | 68,25 km | igual que poi-10 |

### Decisiones que merecen explicación

**poi-3 · Bu Craa (¿26.3228 o 26.3576?).** Hay dos coordenadas en circulación:
Wikipedia/Wikidata/Atlas Obscura dan 26.32278 / -12.84972 y OpenStreetMap sitúa el `place=village`
«Boucraa» en 26.3576 / -12.84435, a 3,9 km al SSO. Se ha elegido **el nodo de OSM** por tres
razones: (1) la regla del encargo manda usar el `place=*` para pueblos y ciudades; (2) es el
núcleo construido — mapcarta lista la mezquita del pueblo dentro de ese punto y sitúa la
cantera de la OCP 5 km al sureste y una instalación militar 6 km al oeste, es decir, el punto de
Wikipedia cae ya del lado de la explotación; (3) es lo que resuelve cualquier navegador que
busque «Boucraa». La coordenada de Wikipedia queda anotada aquí por si se prefiere apuntar a la
mina. En el texto se ha quitado «se mira desde **la carretera de Smara**»: la cinta va de Bu Craa
al puerto de El Marsa/El Aaiún, hacia el noroeste, y no acompaña al eje El Aaiún–Smara; queda
«se mira desde la carretera y a distancia».

**poi-6 · La Duna Blanca.** El único candidato de OSM era un `amenity=car_rental` llamado «Duna
Blanca» dentro de Dajla (a 13,8 km), es decir, una empresa que se llama como la duna. La duna
está en la **orilla continental (este) de la laguna**, en el término de El Argub: dos agregadores
independientes colocan el punto «White Dune / White Dune Canyon, El Argoub» en 23.80284 /
-15.73619, la web del propio establecimiento da la dirección **«Km 52 al Argoub»**
([whitedunecanyon.com](https://whitedunecanyon.com/)) y Travelocity añade «a 32 km del centro de
El Argub», lo que encaja con El Argub en 23.6111/-15.8583
([db-city](https://en.db-city.com/Morocco--Dakhla-Oued-Ed-Dahab--Oued-Ed-Dahab--El-Argoub)).
Se ha puesto **el punto de acceso en la orilla**, no la duna: la duna queda al otro lado del brazo
de agua (≈23.822/-15.745 según MaJourneys) y se alcanza en 4×4 por trazas de marea o en barca
—[ION CLUB](https://www.ion-club.net/dakhla-white-dune-canyon/) describe su centro como
«a la orilla de la laguna, enfrente de la Duna Blanca»—. Se ha corregido además el texto: **no
está «a 40 km al norte de la ciudad a pie de la N1»**, sino a ~20 km en línea recta al nordeste
y ~50 km por carretera rodeando la cabecera de la laguna.

**poi-9 · Kitesurf.** Se ancla en **PK25**, que es un topónimo real y cartografiado (el punto
kilométrico 25 de la carretera de la península) y el centro de gravedad de los campamentos:
alrededor del nuevo punto están PK25 Dakhla, Dakhla Club, Dakhla Attitude, Dakhla Spirit,
DreamKite y Dakhla Evasion, todos en mapcarta. El texto se ha ampliado para decirlo, manteniendo
la descripción de zona (laguna + spots de océano).

**poi-13 · Sebja de Imlili.** **Existe y está bien descrita.** Es una depresión endorreica de
~13 × 2,5 km con centenares de pozas hipersalinas permanentes habitadas por *Coptodon guineensis*
(el cíclido antes clasificado como *Tilapia guineensis*), a unos 50 km al sur de Dajla y ~15 km
del Atlántico. Fuentes: [Parasite 2022](https://www.parasite-journal.org/articles/parasite/full_html/2022/01/parasite220122/parasite220122.html),
la ficha «centre approximatif de la dépression : N 23°15′, W 15°55′» de
[ResearchGate](https://www.researchgate.net/figure/Location-of-the-sebkha-of-Imlili-and-of-the-water-holes-studied-A-Morocco-B-and-C_fig1_322916057)
y [en.wikipedia Imlili](https://en.wikipedia.org/wiki/Imlili) (el pueblo, 23.2349/-16.0792).
OSM tiene además el humedal «Sebkhet Imlily» y un **mirador «Fish Pools»**: se ha usado el
mirador, que es el punto visitable y coincide con una de las pozas muestreadas. Corregido el
texto: no está «al sureste» de Dajla sino **al sur**, y las tilapias no son «peces marinos» sino
un cíclido eurihalino de estuario.

**poi-16 · Cabo Blanco.** El veredicto DESPLAZADO venía de que Photon devolvió tres «Cabo Blanco»
de **Tenerife** a 806 km. El cabo real está en la punta sur de la península de Ras Nuadibú.
El texto del PDI ya era correcto (acceso solo por Mauritania desde Nuadibú, colonia en reserva
de acceso restringido) y se confirma: la península mide ~56 km y está partida por una frontera
trazada en 1900 que sigue aproximadamente su eje, Mauritania al este y Sáhara Occidental *de
iure* al oeste, con todo bajo control mauritano *de facto*
([fr.wikipedia](https://fr.wikipedia.org/wiki/Cap_Blanc_(Mauritanie))). Los números de la foca
monje también resisten: ~270 ejemplares en Cabo Blanco y más de 200 muertos —dos tercios de la
colonia— en dos meses de 1997 ([en.wikipedia](https://en.wikipedia.org/wiki/Mediterranean_monk_seal)).
Se mantiene marcado como NO accesible desde este corredor.

**log-2 · Salida (subida).** El punto estaba en Tarfaya, idéntico al de entrada (log-0), y por
tanto duplicado. Como el nombre encabeza con «Smara → Tan-Tan», se ha llevado a **Smara**, que es
donde se decide la variante interior; la variante costera sale por el mismo Tarfaya/Tah del punto
de entrada, y así se ha anotado en el `info`.

**log-3 · Hospital de El Aaiún.** El único candidato que devolvió Photon era el hospital **de
Dajla**, a 470 km. El Centro Hospitalario Regional de El Aaiún son en realidad **dos** hospitales
(informe del Tribunal de Cuentas marroquí): el **Moulay El Hassan Ben El Mehdi** (1986, 209 camas
funcionales) y el **Hassan II de especialidades** (1994, 80 camas). El de referencia —y el que
hizo la primera operación a corazón abierto de las provincias del sur— es el primero, así que se
ha cambiado el nombre del punto y se ha llevado la coordenada a su ubicación. Se retira la
coletilla «Coordenada urbana aproximada» en log-3 y log-4, porque ya no lo son.

---

## (b) PDIs eliminados

**Ninguno.** Los dos candidatos serios a alucinación —la Sebja de Imlili y las fuentes termales de
Asmaa— se han confirmado como lugares reales (ver (a) y (c)). Los 16 PDIs corresponden a lugares
existentes y documentados.

---

## (c) Puntos NO VERIFICADOS

1. **poi-14 · Fuentes termales de Asmaa — el lugar existe, el punto exacto no está confirmado.**
   Está bien documentado por prensa marroquí: agua sulfurosa de un sondeo artesiano de ~700 m,
   38 °C según [Le Reporter Express](https://lereporterexpress.ma/2022/10/21/asmaa-dakhla-source-thermale-sahara-marocain-connue-international/)
   y «en torno a 30 °C» según [Yabiladi](https://www.yabiladi.com/articles/details/59776/nomad-asmaa-source-thermale-plein.html);
   [Visit-Dakhla](https://visit-dakhla.com/la-source-thermale-asmaa/) la sitúa «a unos 45 km de
   Dajla» y Yabiladi «a 35 km, dejando el asfalto en una pista de arena pasado el kilómetro 25».
   Ninguna fuente da coordenadas. El único manantial cartografiado en OSM en toda la zona es un
   `natural=spring` llamado «Hot spring» a la altura del PK25, y ahí se ha puesto el punto, que
   como mucho es el arranque de la pista. **Queda marcado como COORDENADA NO VERIFICADA en la
   propia `desc`.** De paso se ha corregido el texto, que describía un balneario con «piscinas de
   obra, vestuarios y separación de horarios para hombres y mujeres» que las dos crónicas
   desmienten: son tres casetas, un pozo y un grifo, y un encargado que moja a la gente con una
   manguera. Añadido que el agua **no es potable**.
2. **log-9 · Combustible · cruce de Dajla (Dakhla Junction) — coordenada mala, sin sustituto
   verificable.** El punto de la app (23.735 / -15.87) cae **dentro de la laguna**, unos 4-5 km al
   este del eje de la península. El cruce real de la N1 con la carretera de la península está
   ~40 km al nordeste de Dajla (los locales lo llaman PK 40). No he podido fijarlo con ninguna
   fuente abierta: iOverlander —de donde sale la referencia del `info`— exige cuenta
   ([ficha «Dakhla Junction Fuel»](https://ioverlander.com/places/129505-dakhla-junction-fuel)),
   los hilos de [Horizons Unlimited](https://www.horizonsunlimited.com/hubb/morocco/fuel-stations-in-western-sahara-89474)
   y [Sahara Overland](https://sahara-overland.com/2020/04/03/a-if-for-atlantic-highway/) dan las
   distancias (Laayoune Plage +20, Lemsid +80, Bojador +80, cruce de Dajla +290, y 252 km del
   cruce a Bir Gandouz) pero ninguna coordenada, y las pistas GPS de Extrem-Sud están tras
   registro. **Se ha dejado la coordenada como estaba antes que inventarla**: hay que fijarla con
   un track real o sobre el terreno.
3. **poi-12 · Bahía de Cintra — dato de texto sin confirmar.** La coordenada es correcta (la de
   Wikidata; el polígono de OSM está a 6,5 km, dentro del umbral de área, y mapcarta confirma
   «unos 120 km al sur de Dajla», como dice la ficha). Lo que no he podido verificar es «**29
   millas náuticas de anchura**» ni la profundidad media de 10 m; tampoco el proyecto de parque
   nacional que abarcaría Cintra y Dajla. El aviso de **minas en el entorno de Cabo Barbas** sí es
   coherente con todo lo publicado sobre el territorio, y se mantiene. No se ha tocado el texto.

---

## (d) Correcciones de texto

| id | antes | después | motivo |
|---|---|---|---|
| poi-3 | «Se mira desde **la carretera de Smara**» | «Se mira desde la carretera y a distancia» | la cinta va de Bu Craa al puerto de El Aaiún, hacia el NO; el eje El Aaiún–Smara va en otra dirección |
| poi-6 | «en la orilla continental, a unos **40 km al norte** de la ciudad y **a pie de la N1**» | orilla este de la laguna, ~20 km en línea recta al NE y ~50 km por carretera por El Argub; **no** está a pie de la N1 | la duna está en el término de El Argub, km 52 |
| poi-6 | «COORDENADA APROXIMADA — el punto exacto de parada se ve desde la carretera» | se explica que el punto es el acceso en la orilla y que la duna requiere 4×4 por trazas de marea o barca | MaJourneys e ION CLUB coinciden en que no es un destino de turismo «self-drive» |
| poi-9 | — | se añade que el punto de la ficha es **PK25** y se nombran los campamentos del entorno | el PDI era una «zona» sin punto verificable |
| poi-13 | «a unas decenas de kilómetros **al sureste** de Dajla, en plena depresión salina» | «a unos **50 km al sur** de Dajla y a unos 15 km del Atlántico, en una depresión tectónica alargada de unos 13 × 2,5 km» | Parasite 2022 y la ficha de ResearchGate |
| poi-13 | «poblaciones aisladas de TILAPIA — **peces marinos** atrapados ahí» | «TILAPIA (***Coptodon guineensis***, un cíclido de estuario)» | especie identificada en la bibliografía; es eurihalina, no marina |
| poi-13 | «COORDENADA APROXIMADA y acceso POR CONFIRMAR» | se precisa que la coordenada es el mirador «Fish Pools» y que el desvío sale a la altura de Imlili/Tchika | OSM + mapcarta |
| poi-14 | «balneario muy modesto —piscinas de obra, vestuarios básicos, separación de horarios o espacios para hombres y mujeres—» y «unos 38 °C» | agua sulfurosa de 30-38 °C de un sondeo artesiano de ~700 m; tres casetas, un pozo y un grifo, sin vestuarios ni piscinas; agua **no potable**; acceso por pista desde el km 25-28; coordenada **no verificada** | Le Reporter Express y Yabiladi |
| log-2 | — | se añade que el punto está en Smara y que la variante costera coincide con el de entrada | el punto estaba duplicado en Tarfaya |
| log-3 | nombre «Hospital Regional **Hassan II**» | «Hospital Regional **Moulay Hassan Ben El Mehdi**» + mención a que el CHR son dos hospitales | Tribunal de Cuentas de Marruecos |
| log-3 / log-4 | «Coordenada urbana aproximada» | se retira | ya apuntan al nodo/vía del hospital |
| log-4 | «Recurso sanitario urbano de Dajla» | «Hospital Hassan II de Dajla («General Hospitals of Dakhla»)» | nombre real del centro en OSM |
| log-13 | «Coordenada meramente indicativa de la zona a evitar» | se añade que el punto cae **al este del muro**, entre Mehaires y Tifariti, en zona controlada por el Polisario | ver abajo |

### Comprobaciones de texto que NO han obligado a cambiar nada

- **poi-3**: yacimiento >1.700 Mt, explotación desde 1972, cinta de ~100 km y «la más larga del
  mundo», polvo visible desde el espacio, pueblo-empresa de Phosboucraa →
  [en.wikipedia Bou Craa](https://en.wikipedia.org/wiki/Bou_Craa). Todo correcto.
- **poi-7**: 400 km², 37 km de largo, SIBE + ZICO + **sitio Ramsar desde 2005** →
  [fr.wikipedia Baie de Dakhla](https://fr.wikipedia.org/wiki/Baie_de_Dakhla). Correcto.
- **poi-15**: Smara fundada en 1869 como oasis de caravanas, capital espiritual de Ma al-Aynayn
  en 1902, saqueada y biblioteca destruida por los franceses en **1913** y destruida de nuevo en
  **1934** tras las rebeliones saharauis contra la ocupación española →
  [en.wikipedia Smara](https://en.wikipedia.org/wiki/Smara). Todo correcto, punto a 0,7 km del
  `place=city`.
- **poi-16**: ~270 focas y >200 muertas (dos tercios) en dos meses de 1997 →
  [en.wikipedia Mediterranean monk seal](https://en.wikipedia.org/wiki/Mediterranean_monk_seal).
  Correcto.
- **poi-9**: el spot de **Foum Labouir «junto al faro»** es coherente: el faro de Dajla (Villa
  Cisneros, 1916, torre de 56 m) está en 23°43′35″N 15°57′16″W →
  [List of lighthouses in Western Sahara](https://en.wikipedia.org/wiki/List_of_lighthouses_in_Western_Sahara).
- **poi-10**: Bir Gandus es cabeza de la provincia de Aousserd y tenía 4.625 habitantes en el
  censo de 2014; el puesto fronterizo propiamente dicho está al oeste, en Guerguerat
  ([en.wikipedia](https://en.wikipedia.org/wiki/Bir_Gandus)). La ficha ya lo decía así.
- **log-13 · muro de arena**: el muro recorre ~2.700 km, va de Guerguerat hacia el este paralelo a
  la frontera mauritana ~200 km, gira al norte pasada Tichla y sube dejando Guelta Zemmur y Smara
  del lado marroquí, y su cinturón de minas es el campo de minas continuo más largo del mundo
  ([en.wikipedia Moroccan Western Sahara Wall](https://en.wikipedia.org/wiki/Moroccan_Western_Sahara_Wall)).
  **Comprobado que el punto de la ficha (26,0 / -11,0) queda al ESTE de la berma**: cae entre
  Mehaires ([al este del muro, zona del Polisario](https://en.wikipedia.org/wiki/Mehaires)) y
  Tifariti (26.15806 / -10.56694, [«east of the Moroccan Berm», capital de facto de la RASD](https://en.wikipedia.org/wiki/Tifariti)).
  Es decir, la coordenada indicativa señala efectivamente la zona prohibida. Anotado en el `info`.
- **log-11 y log-12**: los dos tienen nombre genérico de corredor («El Aaiún → Smara», «El Aaiún y
  Dajla») y el veredicto DESPLAZADO era un artefacto de comparar con la primera ciudad del
  nombre. log-11 está sobre **Smara** (0,7 km del `place=city`) y log-12 sobre **Dajla** (dentro
  del casco urbano). **No se tocan**, ni coordenada ni texto, como indica el encargo.

---

## (e) Interés de los PDIs y sugerencias

**Lo que sostiene la ficha.** Para una expedición overland con perro, el bloque fuerte es
evidente: **Dajla y su laguna** (poi-7, poi-8, poi-9, poi-6), **Bojador** (poi-5) por lo que
significa históricamente y por ser la última localidad con oferta antes del vacío,
**Guerguerat** (poi-11) porque es el trámite que condiciona el día entero, y **Smara** (poi-15)
como único desvío del corredor que no es ni costa ni gasolinera. La **Sebja de Imlili** (poi-13),
ahora que está localizada, es probablemente el PDI más singular del territorio: no hay nada
parecido en toda la ruta.

**Lo flojo o repetitivo, para que el propietario decida.**

- **poi-4 Lemsid** y **log-7** son el mismo punto con el mismo texto. Como PDI no aporta nada
  («no hay nada que ver», lo dice la propia ficha); su función es logística y ya está cubierta por
  log-7. Sugerencia: bajarlo a nota dentro del punto de combustible o dejarlo en `prio: Baja`
  como está, pero no es un PDI.
- **poi-2 Laayoune Plage** y **log-6** se solapan igual, aunque aquí el PDI sí tiene contenido
  propio (desembocadura, playa, lonja).
- **poi-6, poi-7, poi-9** describen tres veces la misma laguna desde ángulos distintos. Funciona,
  pero conviene que las tres fichas no repitan los mismos datos de viento y ostras.
- **poi-12 Bahía de Cintra** es un PDI que la propia ficha declara no visitable («no se baja, no
  se sale de la carretera»): es un mirador de paso. Correcto como está, pero `prio: Media` puede
  ser generoso.
- **poi-16 Cabo Blanco** es honesto y útil justamente porque dice que **no** se visita desde aquí;
  merece quedarse aunque su coordenada no sea un destino.
- **Imágenes**: nueve de los dieciséis PDIs usan la misma foto de la catedral de El Aaiún o la
  misma de la costa, y lo declaran en el texto. No es un problema de datos, pero es el defecto más
  visible de la ficha.

**Tres PDIs que faltan (coordenadas verificadas en esta sesión).**

1. **Señal del Trópico de Cáncer sobre la N1** — **23.43741 / -15.96747**
   (OSM `tourism`/`information` **node 3346406957**, [mapcarta.com/Tropic_of_Cancer_Sign](https://mapcarta.com/Tropic_of_Cancer_Sign)).
   Está literalmente a pie de la N1, entre el cruce de Dajla e Imlili. Parada de cinco minutos,
   gratis, al aire libre, foto obligada, perfecta con perro y con un valor simbólico grande en un
   viaje Barcelona–Kenia: es el momento en que la expedición entra en el trópico. Cuesta cero
   añadirlo y encaja en las dos pasadas.
2. **Faro de Dajla (Villa Cisneros, 1916) y el spot de Foum Labouir** — **23.72639 / -15.95444**
   (23°43′35″N 15°57′16″W, [List of lighthouses in Western Sahara](https://en.wikipedia.org/wiki/List_of_lighthouses_in_Western_Sahara)).
   Torre de 56 m levantada por España, en la punta de la península, con el lado océano y la
   derecha de Foum Labouir a sus pies. Es el resto español más fotogénico de Dajla después del
   trazado de Villa Cisneros, está a 3 km del centro y es exterior, gratuito y apto para perro.
3. **Lasarka (Lassarga), pueblo pesquero del lado océano** — **23.63374 / -15.99054**
   (OSM `place=village` **node 1829716252**, [mapcarta N1829716252](https://mapcarta.com/N1829716252)).
   A 12 km al sur de Dajla por la península: barcas, pesca artesanal y la playa larga de Lassarga,
   que es donde están los centros de surf/SUP. Es el contrapunto «vida local» a los campamentos de
   kite de la laguna y el mejor sitio para un paseo largo con el perro sin meterse en zona de aves
   protegidas.

---

## (f) Fuentes abiertas que fallaron

- **Photon, Nominatim, Overpass (y sus espejos kumi / private.coffee) y `wikidata.org`**:
  rechazados por el proxy de salida del contenedor (`CONNECT tunnel failed, 403`). Tampoco
  funcionan vía WebFetch: `nominatim.openstreetmap.org`, `www.openstreetmap.org/search`,
  `www.openstreetmap.org/api/0.6/map` y `overpass-api.de/api/interpreter` están **prohibidos por
  `robots.txt`**. Sustituidos por **mapcarta.com**, que publica el mismo dato de OSM con el id de
  nodo/vía, y por los candidatos ya capturados en `_eval.json`.
- **iOverlander**: la ficha «Dakhla Junction Fuel» redirige a la pantalla de login; `…/129505.json`
  devuelve 401. Es la fuente que cita el `info` de log-9 y no es consultable sin cuenta.
- **Extrem-Sud** (tracks GPS del Sáhara atlántico, ficha «H1. Parcours touristiques entre le PK 40
  et Dakhla»): la página carga pero los waypoints están tras registro.
- **mindat.org** (ficha «Bir Gandús»): 403.
- **geonames.org**: no tiene ningún registro para «dune blanche».
- **en.wikipedia.org / fr.wikipedia.org**: varias URLs concretas (`Lemsid`, `Cape_Blanc,_Mauritania`,
  `es.wikipedia Cabo Blanco (África)`, `wikivoyage Ad Dakhla`) devolvieron «this domain is
  cache-only and cannot be fetched»; se resolvieron con el artículo equivalente en otro idioma o
  con mapcarta.
- **maps.me** (catálogo de gasolineras de Dajla): prohibido por `robots.txt`.
- **communesmaroc.com** (ficha del hospital de El Aaiún): el directorio sanitario todavía no está
  publicado.

---

*Ambos JSON validados con `json.load`. `git diff` sobre `content/pois/sahara-occidental.json` y
`content/ficha/sahara-occidental.json`: 21 y 17 líneas cambiadas respectivamente, todas ellas
`lat`, `lon`, `name`, `desc` o `info` de los puntos listados arriba.*

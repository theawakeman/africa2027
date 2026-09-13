# Auditoría de PDIs y puntos logísticos · Guinea

Fecha: 2026-09-13 · Entradas: `content/pois/guinea.json` (20 PDIs), `content/ficha/guinea.json` → `logistics` (18 puntos), `audit/geo/guinea_eval.{md,json}`.

Punto de partida: 16 DESPLAZADO + 2 DUDOSO + 2 OK? sobre 38 puntos — el peor del grupo de África occidental.
Resultado: **15 coordenadas corregidas** (8 PDIs + 7 logísticos), 1 punto marcado NO VERIFICADO, 1 punto declarado no geocodificable, 3 renombrados, 0 PDIs eliminados.

Photon, Nominatim y Overpass están bloqueados desde este contenedor. Todas las coordenadas nuevas salen de **mapcarta.com** (que expone el nodo/way OSM y su id), de **Wikipedia (fr/en)** o de **páginas oficiales**, abiertas en esta sesión; los enlaces están en cada fila.

---

## (a) Correcciones aplicadas

### PDIs — `content/pois/guinea.json`

| id | nombre | lat/lon antes | lat/lon después | dist. | fuente |
|---|---|---|---|---|---|
| poi-3 | Monte Loura y la Dama de Mali | 12.0833 / -12.3 | **12.11208 / -12.25949** | 5,44 km | OSM node 2461691472 `natural=peak`, 1.515 m → https://mapcarta.com/Mount_Loura |
| poi-4 | Pita y las cataratas de Kinkon → **Cataratas de Kinkon (Pita)** | 10.9833 / -12.4 | **11.0562 / -12.45404** | 10,02 km | OSM `waterway=waterfall` (guinea_eval.json), corroborado por mapcarta: «Kinkon (waterfall) 8 km northeast» desde Kambadaga → https://mapcarta.com/N1905555486 · https://mapcarta.com/W180527799 |
| poi-5 | Cataratas de Kambadaga | 11.0167 / -12.5167 | **10.99718 / -12.49317** | 3,36 km | OSM node 1905555486 `waterway=waterfall` → https://mapcarta.com/N1905555486 |
| poi-6 | Doucki · «Gran Cañón de Guinea» | 11.15 / -12.6 | **10.9853 / -12.59924** | 18,31 km | OSM node 3662273160 `place=village`, subprefectura de Pita → https://mapcarta.com/Doucki |
| poi-8 | Cataratas de Ditinn | 10.75 / -12.1667 | **10.81622 / -12.18594** | 7,66 km | OSM node 2009723553 `waterway=waterfall` → https://mapcarta.com/N2009723553 |
| poi-14 | Bosque de Ziama (Macenta) | 8.4 / -9.3167 | **8.37447 / -9.28304** | 4,67 km | Punto navegable = **Sérédou**, OSM node 2595673190, subprefectura de Macenta → https://mapcarta.com/S%C3%A9r%C3%A9dou |
| poi-18 | Kouroussa y el PN del Alto Níger → **Kouroussa · puerta del PN del Alto Níger** | 10.65 / -9.8833 | **10.65 / -9.88333** | 0 km | Kouroussa 10°39′N 9°53′W → https://en.wikipedia.org/wiki/Kouroussa (solo se fija el 5.º decimal; ver nota abajo) |
| poi-19 | Dabola y las cataratas del Tinkisso → **Cataratas del Tinkisso (Dabola)** | 10.75 / -11.1167 | **10.7291 / -11.17002** | 6,27 km | OSM node 2522367033 `waterway=waterfall`, 70 m de ancho × 45 m de caída, 7 km al oeste de Dabola → https://mapcarta.com/N2522367033 |

**Notas de criterio**

- **poi-4 y poi-19 mezclaban pueblo y cascada.** En los dos casos he puesto la coordenada en **la cascada** (que es lo que justifica el PDI: categoría Naturaleza, ½ día) y lo he dicho en el nombre, dejando la ciudad como base logística dentro del texto y con su coordenada escrita en el `desc`. Además, el punto viejo de poi-4 (10.9833 / -12.4) no era ni Pita (11.05646 / -12.39505) ni la cascada: estaba 8 km al sur de la ciudad, en mitad del campo.
- **poi-14 (Ziama).** El candidato de Wikidata (Q27459435, 8.0 / -9.58333) **no es el bosque**: es el macizo Wonegizi/Ziama, a 53 km, ya sobre la frontera liberiana; el candidato OSM `landuse=forest` estaba a 447 km. Wikipedia sitúa el macizo de Ziama en 8°14′N 9°22′W, que es interior de selva sin acceso rodado. He usado **Sérédou**, que es lo que el propio `desc` daba como base y es una subprefectura con carretera, a unos 28 km al sureste de Macenta.
- **poi-18 (Alto Níger).** El punto de la app ya era Kouroussa —correcto como punto navegable— y el «desplazamiento» de 51,9 km era contra el polígono del parque. He conservado Kouroussa (ajustando el 5.º decimal al valor de Wikipedia), **renombrado** el PDI para que no prometa que la coordenada es el parque, y explicado en el `desc` dónde está de verdad la entrada: antena administrativa en **Somoria**, accesos documentados por el propio parque en Sérékoroba, Sidakoro y Bakaria.

### Puntos logísticos — `content/ficha/guinea.json` → `logistics`

| id | nombre | lat/lon antes | lat/lon después | dist. | fuente |
|---|---|---|---|---|---|
| log-0 | Frontera Sambaïlo / Koundara | 12.55 / -13.35 | **12.58241 / -13.37191** | 4,32 km | OSM node 2520267163 `place=town`, Sambaïlo → https://mapcarta.com/Sambailo |
| log-1 | Frontera salida N'Zo / Gbapleu | 7.55 / -8.45 | **7.60982 / -8.31122** | 16,68 km | OSM way 1023592767 «Poste Frontière», prefectura de Lola → https://mapcarta.com/fr/W1023592767 |
| log-2 | Frontera entrada N'Zo / Gbapleu | 7.55 / -8.45 | **7.60982 / -8.31122** | 16,68 km | Ídem (mismo puesto) |
| log-3 | Frontera variante Pamelap | 9.3 / -13.05 | **9.18013 / -12.96925** | 16,01 km | OSM «Pamélap» `place=village`, Forécariah → https://mapcarta.com/17178818 |
| log-5 | Embajada de España en Conakry | 9.53 / -13.68 | **9.52937 / -13.68384** | 0,43 km | Nodo OSM del barrio de **Coléah** (node 8637815005) → https://mapcarta.com/N8637815005 · dirección: https://www.exteriores.gob.es/Embajadas/conakry/es/Embajada/Paginas/Contacto.aspx — **NO VERIFICADO a nivel de edificio**, ver (c) |
| log-6 | Embajada de Costa de Marfil en Conakry | 9.535 / -13.675 | **9.50847 / -13.71541** | 5,32 km | OSM way 549630555 «Ambassade de Côte d'Ivoire», Boulevard du Commerce, Kaloum → https://mapcarta.com/fr/W549630555 |
| log-9 | Laboratoire Régional Vétérinaire de Labé | 11.3167 / -12.2833 | **11.3596 / -12.27487** | 4,86 km | OSM `healthcare=laboratory` con ese nombre exacto; corroborado a 24 m por el nodo OSM 6079505864 «CFEL», el centro que lo alberga → https://mapcarta.com/fr/N6079505864 |
| log-11 | Hôpital Régional de Kankan | 10.3853 / -9.3057 | **10.3686 / -9.30563** | 1,86 km | OSM way 788920328 `amenity=hospital` → https://mapcarta.com/W788920328 |

**Notas de criterio**

- **log-0 (Sambaïlo).** El candidato más cercano del `_eval` era el **aeródromo** de Sambaïlo (2,7 km), no el paso. He usado el nodo del **pueblo** de Sambaïlo, que es (i) donde se hacen los trámites guineanos según los relatos de viajeros y (ii) exactamente el mismo punto que la auditoría de Senegal fijó para su log-8, de modo que los dos países apuntan ahora al mismo sitio. OSM no cartografía aquí ningún `barrier=border_control`.
- **log-1 / log-2 (N'Zo).** Los dos compartían el mismo error de 20,8 km contra N'Zoo. Siguiendo el nodo del pueblo marfileño de Gbapleu he encontrado el **conjunto real de controles guineanos**, todo en OSM:
  - **Douanes** (node 12505503309): **7.677195 / -8.314697**, dentro del pueblo de N'Zoo, a 280 m del mercado semanal → https://mapcarta.com/fr/N12505503309
  - **Police aux frontières** (node 12505497948): **7.6206 / -8.30528**, 6 km al sur → https://mapcarta.com/fr/N12505497948
  - **Poste Frontière** (way 1023592767): **7.609819 / -8.311217**, en la raya, 4,5 km al noreste de Gbapleu → https://mapcarta.com/fr/W1023592767
  He puesto la coordenada en el **Poste Frontière** (es la frontera) y he escrito los tres puntos en el `info`, porque para un vehículo lo que importa es que la aduana —donde se sella el CPD— está **7,5 km antes**, en el pueblo.
- **log-3 (Pamelap).** He preferido el nodo del pueblo (verificado en mapcarta en esta sesión) al nodo `amenity=police` del `_eval` (9.17585 / -12.96357, 500 m al sursuroeste), que queda anotado en el `info`. Mapcarta confirma además un control fronterizo **en construcción** en OSM: cuando se construya, será la coordenada buena.
- **log-11.** El punto viejo era el punto urbano genérico de Kankan (compartido con poi-17 y con log-15, que son puntos de ciudad y siguen bien); ahora el hospital tiene el suyo.

---

## (b) PDIs eliminados

**Ninguno.** No he encontrado en Guinea ningún PDI alucinado: los 20 existen, tienen nombre correcto y referencia externa. Los dos casos que podían parecerlo eran mezclas de dos lugares reales (poi-4 Pita+Kinkon, poi-19 Dabola+Tinkisso) y se han resuelto renombrando y moviendo el punto, no borrando. Los puntos logísticos no se eliminan nunca: log-4 se ha anotado (ver abajo).

---

## (c) Puntos NO VERIFICADOS

### log-5 · Embajada de España en Conakry — coordenada de barrio, edificio sin verificar

Lo que sí está verificado, en la página oficial (https://www.exteriores.gob.es/Embajadas/conakry/es/Embajada/Paginas/Contacto.aspx):

- Dirección: **Place Almamy Samory Touré, Bâtiment R2000, 6.º piso, Moussoudougou, Coléah — B.P. 706, Conakry**. Coincide literalmente con lo que ya decía el `info`: el texto de la app era correcto.
- Cancillería +224 664 18 64 04 y +224 664 20 22 01 · Sección consular +224 613 33 90 90 · Emergencia consular grave +224 664 33 54 93.
- Correos: emb.conakry@maec.es · emb.conakry.sc@maec.es (consular) · emb.conakry.rgc@maec.es (registro civil).
- La embajada está **acreditada también en Sierra Leona** (dato nuevo y relevante si se ejecuta la variante de Freetown).

Lo que no he podido fijar: **el edificio**. OSM no tiene ningún `office=diplomatic` español en Conakry (los candidatos del `_eval` eran Alemania a 4,4 km, Francia a 4,4 km y EE. UU. a 8,7 km: ninguno sirve), Wikidata está bloqueado como cache-only desde este contenedor (Q61998973 existe pero no se puede leer) y la «Place Almamy Samory Touré» de Coléah no aparece cartografiada en mapcarta (solo salen el Camp y la escuela Almamy Samory Touré, que son otra cosa). He movido el punto **430 m**, del 9.53 / -13.68 «redondo» al nodo OSM real del barrio de **Coléah** (9.52937 / -13.68384), para que al menos la coordenada tenga fuente en lugar de ser un número inventado, y he escrito en el `info` que la precisión es **de barrio (±1 km)** y que hay que fijar el punto al llegar.

### Otros avisos de precisión (no son errores, pero conviene saberlo)

- **log-4** no es un punto: ver (d).
- **poi-13 (nacimiento del Níger)**: el propio `desc` ya avisa de que la coordenada del manantial es aproximada y hay que confirmarla en Faranah. No he tocado nada: el punto de la app es Faranah, que es correcto como base, y el `_eval` lo da OK.
- **poi-18**: la coordenada es Kouroussa, no el parque. Queda dicho en el nombre y en el texto.

---

## (d) log-4 «EXCLUIDA — pasos con Guinea-Bisáu y Malí»: no es geocodificable

El `_eval` lo marca DESPLAZADO con Kounsitel a 81,9 km, pero **es un falso positivo del pipeline**: log-4 no es un lugar, es una **regla de exclusión del protocolo del proyecto** (ni Guinea-Bisáu ni Malí, y por tanto fuera el eje Siguiri–Kourémalé y toda la franja de Siguiri y Mandiana). No tiene puesto, no tiene nombre de lugar y no admite geocodificación: su coordenada (12.0 / -13.8) es solo un ancla cartográfica para que el aviso aparezca en el noroeste del mapa.

**Acción: coordenada intacta.** He añadido una frase al principio del `info` diciendo explícitamente que no es un lugar y que no debe buscarse aquí ningún puesto, para que ni un futuro auditor ni el viajero lo interpreten como un paso real. Recomendación para el pipeline: excluir de la evaluación GPS los puntos cuyo nombre empiece por «Frontera · EXCLUIDA».

---

## (e) Correcciones de texto

| id | qué decía | qué dice ahora | por qué |
|---|---|---|---|
| poi-3 | «el punto más alto de **toda África occidental** fuera de las tierras altas camerunesas» | «el punto culminante **del macizo** —no de toda África occidental, donde hay cumbres más altas, el Nimba entre ellas—» | Falso, y **contradictorio con el propio archivo**: poi-16 describe los montes Nimba, que son más altos que los 1.515 m del Loura. fr.wikipedia define el Loura como «le point culminant du massif du Fouta-Djalon». → https://fr.wikipedia.org/wiki/Mont_Loura |
| poi-3 | «a unos 120 km al norte de Labé» | «a unos 88 km en línea recta al norte de Labé (unos 120 km de carretera)» | 87,8 km medidos entre el nodo de Labé y el pico; los 120 km son de carretera |
| poi-3 | «un perfil rocoso … que reproduce un rostro humano» | + «tallado por la **erosión eólica** y no por la mano humana … algo más abajo hay una segunda formación, **le Sage de Mali**» | Dato verificado en fr.wikipedia; el «Sage» es una segunda formación documentada |
| poi-4 | «Las chutes de Kinkon están a unos 12 km» | «en el **distrito de Sintaly**, a 6,4 km en línea recta del centro de Pita (unos 15 km por carretera)» | Wikipedia FR de Pita da 15 km por carretera y el distrito; la línea recta la he medido entre los dos nodos → https://fr.wikipedia.org/wiki/Pita_(Guin%C3%A9e) |
| poi-4 | «una caída de unos 80 m» | «unos 80 m **según las fuentes locales**» | No he encontrado fuente oficial de la altura |
| poi-4 | «una central hidroeléctrica en la parte alta» | «un **lago de embalse, una presa** y una central hidroeléctrica aguas arriba» | OSM tiene los tres elementos cartografiados (lake W180527799, dam, waterfall) |
| poi-5 | «a unos 25 km de Pita» | «en el **distrito de Bourouwal-Tappé**, a 12,6 km en línea recta (unos 16 km por carretera según la fuente local…)» | Wikipedia FR de Pita: 16 km y el distrito |
| poi-5 | — | + «A 200 m de la cascada hay un célebre **pont de lianes** … y 600 m al sur un mirador cartografiado (Kambadaga Falls View)» | Ambos verificados: el puente de lianas en Wikipedia FR y en mapcarta (200 m al noreste), el mirador como `tourism=viewpoint` |
| poi-6 | «Un pueblo de unos 500 habitantes» | «Un pueblo pequeño de la **subprefectura de Pita** … a 23,6 km en línea recta del centro de Pita» | La cifra de 500 habitantes no es verificable en fuente abierta; la subprefectura y la distancia sí |
| poi-8 | «A unos **50 km al noreste** de Dalaba» | «A **16 km en línea recta al nornoreste** de Dalaba, en el distrito de **Kaala** y **7 km al sur del pueblo de Ditinn**» | Error de bulto: 16,35 km medidos entre el nodo de Dalaba y la cascada. Los 7 km desde Ditinn los da mapcarta |
| poi-8 | «un labio de arenisca de unos 70-80 m» | «unos 70-80 m **según las fuentes locales**» | Altura no confirmada en fuente oficial |
| poi-14 | «Unas 116.000 hectáreas» | «Unas 116.000 hectáreas (**1.162 km²**) … **bosque clasificado desde 1932**» | Confirmado: 1.162 km², clasificado en 1932, Reserva de la Biosfera en 1980 → https://en.wikipedia.org/wiki/Ziama_Massif |
| poi-14 | «uno de los **34** focos mundiales de biodiversidad» | «uno de los focos mundiales de biodiversidad» + «más de **1.300 especies de plantas y 287 de aves** … Área Importante para las Aves de BirdLife» | La cifra de «34 hotspots» está desfasada (hoy se cuentan 36) y no aporta; a cambio, los números de Ziama sí son verificables |
| poi-14 | «con elefantes de bosque (la última población de Guinea…)» | «se le **atribuye** … pero eso **no lo he podido confirmar** en fuente oficial reciente» | Wikipedia no los lista; se suaviza en vez de borrar |
| poi-14 | — | + «LA COORDENADA ES SÉRÉDOU, el pueblo de acceso, no el centro del macizo» + coordenadas y altitud de Sérédou | Transparencia sobre qué es el punto |
| poi-18 | «unas **120.000 hectáreas** … con hipopótamos, chimpancés de sabana, **antílopes roanos**» | «**noyau central de 554 km² (55.400 ha)** en torno al bosque de la Mafou, dentro de un conjunto mucho mayor (~**12.470 km²**, sectores Mafou y Kouya) … hipopótamos, chimpancés, **cobos, antílopes acuáticos y potamoqueros gigantes; el elefante se extinguió aquí**» | Las 120.000 ha no cuadran con ninguna fuente. Wikipedia EN: noyau de 554 km², creado en enero de 1997, elefante extinguido, fauna = chimpancés, gálagos, cobos, waterbuck, potamoqueros gigantes. El plan de gestión oficial da 12.470 km² totales → https://en.wikipedia.org/wiki/Upper_Niger_National_Park · https://gn.chm-cbd.net/sites/gn/files/2022-03/PAG_PNHN-1.pdf |
| poi-18 | «núcleo de una Reserva de la Biosfera» | «Reserva de la Biosfera **y sitio Ramsar desde 2002**» + «creado por decreto en **enero de 1997**» + prefecturas (Kouroussa, Faranah, Dabola, Kankan) | Datos del plan de gestión oficial |
| poi-18 | «Se accede desde Kouroussa o desde Faranah» | + «antena administrativa en **Somoria**; accesos documentados: **Sérékoroba, Sidakoro y Bakaria**; campamentos ribereños (Wodonkobila, Bakoning, Tambo, Wassa, Yohaya)» | Documento turístico oficial del parque → https://gn.chm-cbd.net/sites/gn/files/2021-07/Sites%20tourist.PNHN_.PDF |
| poi-19 | «A pocos kilómetros están las cataratas del Tinkisso … una cortina ancha y escalonada» | «**6,3 km al oeste de Dabola** … una cortina de unos **70 m de anchura y 45 m de caída**, con un **embalse**» | Dimensiones y posición de mapcarta/OSM (node 2522367033) |
| log-0 | «del puesto senegalés de **Manda-Kalifourou**» + «hay ~20 km de tierra de nadie» | «El puesto SENEGALÉS real es **KALIFOUROU** (12,92415 / -13,63848, región de **Kolda**)» + explicación del PCJ de Boundou Fourdou + «las fuentes hablan de ~20 km, pero de Kalifourou a Sambaïlo hay ~48 km: POR CONFIRMAR» | Coordinado con la auditoría de Senegal (log-7/log-8): el puesto real es Kalifourou, y el puesto yuxtapuesto de **Boundou Fourdou**, entregado en diciembre de 2019, seguía con «une absence totale de vie administrative» en abril de 2023. La cifra de 20 km no cuadra con la distancia medida entre los dos puestos |
| log-1 | — | + la secuencia completa **Douanes (N'Zoo) → Police aux frontières → Poste Frontière**, con las tres coordenadas | Para un vehículo con CPD lo decisivo es que la aduana está 7,5 km antes del puesto de raya |
| log-2 | — | + remisión a log-1 para la secuencia | Comparten paso |
| log-3 | — | + nodo del pueblo, comisaría a 500 m, **control fronterizo en construcción** en OSM, y Gbalamuya (Kambia) al otro lado | Contexto del punto |
| log-4 | — | + «**NO ES UN LUGAR**: esto es una regla de exclusión, no un punto geocodificable…» | Ver (d) |
| log-5 | dirección + 3 teléfonos | + B.P. 706, cuarto teléfono de cancillería, tres correos, acreditación en Sierra Leona, y el aviso de precisión de barrio | Página oficial |
| log-6 | «Confirmar dirección … Coordenada urbana aproximada — POR CONFIRMAR» | «**Boulevard du Commerce, Kaloum** … Tel. **+224 656 34 34 34** · guinee.diplomatie.gouv.ci · horario OSM: L-J 9:00-15:00, V 9:00-14:00» | OSM way 549630555 trae dirección, teléfono, web y horario. Se mantiene el aviso de confirmar por teléfono al llegar |
| log-9 | «Coordenada urbana aproximada: localizar en Labé al llegar» | Ubicación exacta (**dentro del CFEL**, 5 km al norte del centro), **inaugurado el 18-12-2019**, rehabilitado con financiación **USAID** y coordinación **FAO**, uno de **tres** laboratorios regionales (Labé, Kankan, Nzérékoré), y el aviso de que es un laboratorio de **diagnóstico** —no una clínica— con muy poco personal | Punto del dossier del perro: convenía que el texto no prometiera una clínica. Unidades reales: microbiología/serología, parasitología-coprología y virología con **prueba rápida e inmunofluorescencia de rabia** → https://fr.wikipedia.org/wiki/Laboratoire_r%C3%A9gional_v%C3%A9t%C3%A9rinaire_de_Lab%C3%A9 · https://www.guinee360.com/19/12/2019/labe-inauguration-dun-laboratoire-regional-veterinaire/ |
| log-11 | «Referencia hospitalaria del corredor de subida» | + «Coordenada del recinto hospitalario (OSM way 788920328), unos 2 km al sur del punto urbano de Kankan, junto al gobernorado regional» | Transparencia |

### Puntos revisados y **no** modificados

- **log-17 · Agua · Fouta Djallon.** Marcado DESPLAZADO a 17 km del nodo `natural=mountain_range`, pero el nombre es genérico y el punto (11.0833 / -12.4) **cae de lleno dentro del Fouta Djallon**: está a 3 km del centro de Pita, en pleno altiplano y justo entre Kinkon, Kambadaga y Doucki, que es exactamente lo que el texto describe. Un `mountain_range` no tiene «centro» navegable. **Coordenada y texto intactos**, como pide el encargo.
- **log-12 a log-16** (combustible y agua genéricos, «todas las ciudades del eje…»): no tocados, corresponden a la auditoría de agua y combustible.
- **poi-11 · Islas de Los** (OK?, 3,7 km del `place=archipelago`): es un archipiélago y el punto está entre las islas; el umbral de área es 15 km. Sin cambios.
- **log-10 · Hôpital Régional de Nzérékoré** (OK?, 1 km): el punto de la app es el punto urbano de Nzérékoré, compartido con poi-15 y log-14. A 1 km del nodo `amenity=hospital` está dentro de tolerancia de ciudad; lo dejo, pero si se quiere afinar, el nodo OSM del hospital es el candidato del `_eval`.

---

## (f) Interés de los PDIs y sugerencias

### Lo que sostiene el país

Guinea es, con diferencia, el país con mejor relación paisaje/esfuerzo del tramo atlántico, y el bloque del **Fouta Djallon** (poi-2 a poi-8 más poi-20) es lo mejor del archivo: altiplano a 1.000-1.500 m, clima fresco, cuatro cascadas grandes en 60 km y un sitio —**Doucki** (poi-6)— que es probablemente el mejor trekking comunitario entre Marruecos y Camerún y el único PDI del país que justifica por sí solo tres noches. **Nimba** (poi-16) y **Ziama** (poi-14) sostienen el sureste, y **Kankan** (poi-17) y **Nzérékoré** (poi-15) son nudos logísticos reales, no relleno.

### Lo que veo flojo o repetitivo (decide el propietario)

1. **Cuatro cascadas de arenisca en el mismo macizo** — poi-4 (Kinkon), poi-5 (Kambadaga), poi-8 (Ditinn) y, a menor escala, el Velo de la Novia dentro de poi-9. Kinkon y Kambadaga están a 8 km una de otra, en el **mismo río Kokoulo** y en la misma prefectura. Con el caudal muy estacional (de julio a noviembre van llenas; en marzo-abril son un hilo), visitarlas las cuatro en la bajada es repetir. Sugerencia: dejar las cuatro en el archivo pero bajar a **Media** la prioridad de **poi-4 (Kinkon)**, que es la más condicionada por la presa —si la central retiene agua, no hay cascada— y quedarse con Kambadaga (bañable, con puente de lianas) y Ditinn (la más fotogénica) como imprescindibles. **No he tocado `prio`**: no es un error evidente, es criterio.
2. **poi-1 · Koundara y el Parque Nacional del Badiar** (Media). El propio texto admite que puede ser «un parque solo sobre el papel», y llega justo después de Niokolo-Koba (Senegal), que es el mismo ecosistema y está mucho mejor dotado. Como **primera noche del país** es imprescindible; como parque, es prescindible. El texto ya lo dice bien.
3. **poi-12 · Boké y la costa de Boffa** (Baja). Variante que roza el protocolo de exclusión de Guinea-Bisáu, con tráfico minero pesado y polvo de bauxita, para un fortín-museo y unas playas. Es el candidato natural a caer si hay que recortar días.
4. **poi-18 · Kouroussa/Alto Níger** (Media). El parque está a 50 km de la ciudad, sin puerta cartografiada, con dotación «POR CONFIRMAR» y sin garantía de guardas ni pistas. Kouroussa como ciudad del Níger navegable y patria de Camara Laye sí tiene valor; el parque, hasta confirmarlo, es una promesa.
5. **Perro.** Solo tres PDIs son verdaderamente compatibles sin condiciones (poi-4/5/8, las cascadas, y poi-20 Tougué); Nimba y Ziama están descartados o sin confirmar, y en Doucki depende de la ruta. Eso hace que **log-9 (laboratorio de Labé)** sea el punto más importante del país para el dossier del perro — de ahí que haya priorizado su coordenada y su texto.

### Tres PDIs que faltan (coordenadas verificadas en esta sesión)

| sugerencia | coordenada | por qué | fuente |
|---|---|---|---|
| **Cascadas de la Soumba (Dubréka)** | **9.91142 / -13.4512** | La excursión clásica a 50 km de Conakry, en la ruta natural Conakry→Kindia: cascada sobre roca con área recreativa, la parada de medio día que hoy falta entre poi-10 (Conakry) y poi-9 (Kindia). Fácil, asfaltada y compatible con el perro | OSM node 2776940460 → https://mapcarta.com/N2776940460 |
| **Chutes de Kilissi (Molota, Kindia)** | **9.94977 / -12.8815** | Dos saltos gemelos (Kilissi 1 y 2, a 170 m) de unos 10 m junto al eje Conakry-Kindia; alternativa menos masificada que el Velo de la Novia y buen sitio de baño para romper el tramo costa-Fouta | OSM node 5983983608 → https://mapcarta.com/N5983983608 |
| **Bossou (Lola)** | **7.65039 / -8.50617** | Subprefectura al pie del Nimba, célebre por su población de chimpancés habituados y estudiados desde los años setenta; a 9 km de Yekepa (Liberia) y en la misma salida que poi-16 y log-1. **Ojo: gran parte de la subprefectura es la Reserva Natural Integral del Nimba**, así que el perro queda fuera y el acceso es con permiso. Verificar la estación de investigación antes de incluirlo | OSM way 103686973 → https://mapcarta.com/17191160 |

---

## (g) Fuentes abiertas que fallaron

- **Photon / Nominatim / Overpass** — bloqueados desde este contenedor (es el motivo de usar mapcarta como espejo de OSM).
- **Wikidata** (`www.wikidata.org`, `Special:EntityData`) — responde «This domain is cache-only and cannot be fetched». Afecta directamente a **Q61998973 (Embassy of Spain, Conakry)**, que existe y podría tener la coordenada del edificio: es la vía que habría cerrado el único punto NO VERIFICADO.
- **`fr.wikipedia.org/wiki/Forêt_classée_de_Ziama`** — no existe / cache-only; resuelto con `en.wikipedia.org/wiki/Ziama_Massif`.
- **`www.labovetlabe.com`** y **`www.adsepguinee.com`** — robots.txt inaccesible (fallo de DNS del fetcher); resueltos con Wikipedia FR y Guinée360.
- **`mapcarta.com/Kinkon_Waterfall`**, **`mapcarta.com/Somoria`**, **`mapcarta.com/N5030261398`** — 404. La cascada de Kinkon se acabó validando por triangulación (mapcarta da «Kinkon (waterfall) 8 km al noreste» desde Kambadaga, que es exactamente la distancia y el rumbo del nodo del `_eval`); Somoria no está en OSM, así que la antena del parque solo queda citada en el texto, sin coordenada.
- **Presupuesto de WebSearch agotado** a mitad del trabajo (200/200). Los últimos puntos se resolvieron navegando mapcarta por enlaces desde páginas ya abiertas — así apareció, de hecho, el conjunto de tres puestos de N'Zoo, que ninguna búsqueda había encontrado.

---

## Validación

```
python3 -c "import json;json.load(open('content/pois/guinea.json'))"     → OK (20 PDIs)
python3 -c "import json;json.load(open('content/ficha/guinea.json'))"    → OK (18 logistics)
```

Coordenadas redondeadas a 5 decimales. Formato: `ensure_ascii=False, indent=2` en los dos archivos. No se ha tocado ninguna otra clave ni ningún otro archivo del proyecto.

### Dos cosas que quedan pendientes fuera de mi alcance

1. **Rebuild.** Las coordenadas viejas siguen en los derivados generados: `assets/js/points.json`, `paises/guinea/index.html`, `mapa/index.html`, `tools/gen/data_guinea.py`, `assets/kml/10 Emergencias y logistica.{csv,kml}` y `tools/doc.kml`. Hay que regenerarlos desde `content/` para que los cambios lleguen a la app y al KML.
2. **«Manda-Kalifourou» en la prosa.** El nombre antiguo del puesto senegalés sigue apareciendo en `custom_sections` y `custom_sections_post` de `content/ficha/guinea.json` (y en `content/ficha/senegal.json`), que son claves de texto libre fuera del encargo. Convendría armonizarlas con el nombre corregido —**Kalifourou**— en una pasada de redacción.

# Auditoría de PDIs y puntos logísticos · Mauritania

Fecha: 2026-09-13. Entradas: `content/pois/mauritania.json` (12 PDIs), `content/ficha/mauritania.json → logistics`
(18 puntos), `audit/geo/mauritania_eval.md` / `_eval.json`.

Veredicto del evaluador automático: 22 OK · 3 DESPLAZADO · 2 DUDOSO · 1 OK? · 2 SIN_REF.
Tras la revisión manual, **dos de los tres DESPLAZADO y los dos DUDOSO eran falsos positivos del geocodificador**
(comparaba con un homónimo lejano). Solo un punto necesitaba corrección real de coordenadas, más una de precisión.

Nota de método: Photon, Nominatim, Overpass (overpass-api.de, kumi, openstreetmap.fr) y `openstreetmap.org/search`
están bloqueados desde este contenedor (403 del proxy o `robots.txt`). Todas las coordenadas nuevas de esta sesión
se han obtenido de **mapcarta.com** (que publica los nodos de OSM con su id y sus coordenadas), de **Wikipedia**
(es/en/fr) y de **fuentes oficiales** (exteriores.gob.es, pnd.mr, pnba.mr). Ninguna coordenada procede de memoria.

---

## (a) Correcciones aplicadas

| id | nombre | lat/lon antes | lat/lon después | distancia | fuente |
|---|---|---|---|---|---|
| poi-2 | Aïcha | 21.29208 / -13.69197 | 21.29494 / -13.69584 | 0,5 km | OSM `natural=hill` «Aïsha», 8 km al NO de Ben Amera ([mapcarta Ben Amera, nodo 2152567098](https://mapcarta.com/27134378)) |
| poi-9 | Puerto pesquero de Nuakchot | 18.11029 / -16.02292 | 18.10338 / -16.02594 | 0,8 km | OSM «ميناء الصيد» (puerto de pesca); corroborado por [Atlas Obscura · Port de Pêche, 18.102845 / -16.025223](https://www.atlasobscura.com/places/port-de-peche) (0,1 km) |

Detalle:

- **poi-2 · Aïcha.** El DESPLAZADO era falso: el evaluador había emparejado con «Dhala Aïcha», un `natural=peak`
  a 268 km. El monolito real está donde dice la app, con 0,5 km de desviación respecto al nodo OSM con nombre.
  Verificado que existe y que es el conjunto correcto: Ben Amera es «el mayor monolito de África y el segundo del
  mundo tras Uluru», 633 m sobre el desierto, y **Aïsha** es el monolito menor, «a 20 minutos de coche» de Ben
  Amera, en cuya base una docena de artistas internacionales esculpieron los bloques en 1999
  ([en.wikipedia · Ben Amera](https://en.wikipedia.org/wiki/Ben_Amera)). mapcarta sitúa «Aïsha» (colina) **8 km al
  noroeste** del pico Ben Amera (nodo OSM 2152567098, 21.23003 / -13.66437, que es exactamente el punto de poi-1).
  Se ajusta poi-2 al nodo con nombre y se corrige la distancia del texto (decía «unos 7 km», sin rumbo).

- **poi-9 · Puerto pesquero de Nuakchot.** El punto de la app caía exactamente sobre un `highway=bus_stop`
  llamado «Plage des pecheurs» —una parada de autobús, no el puerto—. El punto de acceso real de la playa de
  pescadores / Port de Pêche Artisanal es el nodo OSM «ميناء الصيد» (18.10338 / -16.02594), 0,83 km al SSO,
  corroborado de forma independiente por Atlas Obscura (18.102845 / -16.025223, 0,1 km de diferencia). Es donde
  varan las piragues y está el mercado de pescado. Se mueve ahí.

---

## (b) PDIs eliminados

**Ninguno.** No se ha detectado ninguna alucinación en los 12 PDIs: los doce existen y están donde dice la app
(con las dos correcciones de arriba). Tampoco se ha eliminado ningún punto logístico (la norma no lo permite).

---

## (c) Puntos confirmados que el evaluador marcaba mal (y por qué)

### log-0 · Frontera · Entrada norte — puesto mauritano de Guerguerat — **CONFIRMADO, no se toca**

El evaluador lo dio por DESPLAZADO 10,5 km porque lo comparó con el nodo OSM `place=village` **Guerguerat**
(21.42699 / -16.95992), que es el **pueblo marroquí**, no el puesto mauritano. Son cosas distintas:

- La frontera Sáhara Occidental–Mauritania sigue **el paralelo 21°20′N** hacia el oeste y, al sur de Guerguerat,
  gira hacia el sur partiendo la península de Ras Nouadhibou
  ([en.wikipedia · Mauritania–Western Sahara border](https://en.wikipedia.org/wiki/Mauritania%E2%80%93Western_Sahara_border)).
  21°20′N = **21.33333**, es decir: la línea internacional pasa justo por el punto de la app.
- El **puesto marroquí** es «Poste Frontière El Guerguarat», nodo OSM 4359918855, en **21.362657 / -16.960837**
  ([mapcarta](https://mapcarta.com/fr/Poste-Fronti%C3%A8re-El-Guerguarat)), 7 km al sur del pueblo de Guerguerat
  (21.427 / -16.9599, [mapcarta N2577205740](https://mapcarta.com/N2577205740)).
- Entre medias está la **tierra de nadie**, llamada localmente «Kandahar» (aldea OSM 4359910656, 21.349957 /
  -16.955659, [mapcarta](https://mapcarta.com/N4359910656)), con las dos zonas tampón mapeadas en OSM:
  «Buffer zone road crossing area Morocco side» (W1521964595) y «…Mauritania side» (W1521964594, 21.33989 /
  -16.95036, [mapcarta](https://mapcarta.com/W1521964594)). Las fuentes de viajeros le dan entre 1 y 5 km; la más
  detallada habla de **4 km** ([Le P'tit Reporter](https://leptitreporter.com/formalites-pour-passer-la-frontiere-terrestre-maroc-mauritanie-a-guerguerat/)).
- El **puesto mauritano** es el complejo conocido como **PK 55** (por el punto kilométrico de la carretera de
  Nouadhibou; nombre usado en avisos sanitarios oficiales franceses,
  [Vidal](https://www.vidal.fr/actualites/23391-franchissement-du-poste-frontiere-pk55-entre-la-mauritanie-et-le-maroc-deconseille.html),
  y en relatos de paso, [Off2Africa](https://gillesdenizot.space/2017/03/24/off2africa-13-frontiere-nouadhibou-mauritanie/)).
  En OSM son tres edificios contiguos:
  - **Border Police / Police des frontières / أمن الحدود** — vía 251493752 — **21.33352 / -16.94704**
    ([mapcarta](https://mapcarta.com/W251493752))
  - **Visa Office** — vía 203766253 — contiguo al norte
  - **Douanes الجمارك** — vía 323855287 — **21.33167 / -16.94707**, 210 m al sur
    ([mapcarta](https://mapcarta.com/W323855287))

**El punto de la app (21.333667 / -16.947167, ahora 21.33367 / -16.94717 al redondear a 5 decimales) está a ~21 m de la oficina de la Policía de Fronteras mauritana.**
Es decir: ya era correcto, y con precisión de edificio. No se cambia la coordenada; se reescribe el `info` para
que diga explícitamente qué puesto es, dónde queda el marroquí (3,5 km al norte) y cuánta tierra de nadie hay en medio.

### poi-12 · Valle Blanco — **CONFIRMADO, no se toca**

DUDOSO porque el evaluador solo encontró «Goûr Amogjâr» y «Oued Amogjâr» a ~70 km. La coordenada de la app
(20.17762 / -13.21507) es **exactamente el nodo OSM 7739412465 «Oued el Abiod»**, Región de Adrar, 149 m de
altitud ([mapcarta](https://mapcarta.com/fr/Oued_el_Abiod)). Y «Vallée Blanche» es justamente el nombre francés
del **Oued el Abiod** («el blanco»): «Située au sud d'Atar, la Vallée Blanche est un boulevard de sable
s'étendant entre deux immenses falaises de grès sombre… aussi appelée El Abiod»
([Les Covoyageurs](https://www.les-covoyageurs.com/conseillez-moi/79-tourisme-mauritanie/1311-visiter-la-vallee-blanche),
[voyageavecnous](https://voyageavecnous.com/atar-et-le-desert-mauritanien-mauritanie/)). Los operadores que hacen
la travesía lo confirman: la Vallée Blanche se baja **desde la passe de Tifoujar** y se sale por Terjit
([Point Afrique · «De Chinguetti à la Vallée Blanche», etapas 12-14](https://www.point-afrique.com/tour-item/vallee-blanche-meharee-15-jours-chinguetti-tifoujar-terjit/)).
Eso es exactamente lo que dice la `desc` de la app («Oued El Abiod; corredor natural entre Tifoujar y Terjit»)
y encaja con poi-11 (Tifoujar, 9 km al sur del nodo) y poi-5 (Terjit).

Matiz honesto: **fr.wikipedia sitúa «la Vallée Blanche» al oeste de la passe d'Amogjar** (20°30′22″N 12°50′24″W,
[Passe d'Amogjar](https://wikimonde.com/article/Passe_d'Amogjar)), a unos 45 km al NE del punto de la app. Es un
uso distinto del mismo topónimo —o una imprecisión del artículo—, pero la acepción mayoritaria y documentada por
las agencias que la recorren es la del Oued el Abiod, al sur de Atar. Se mantiene el punto de la app.

### poi-8 · Iwik y Banc d'Arguin — **CONFIRMADO, no se toca**

Iwik **sí** es el punto de acceso correcto. Se llega «par une piste depuis l'axe routier principal qui relie
Nouakchott à Nouadhibou», hay que contratar guía y **se paga la entrada en la oficina del parque en Iwik**;
desde allí salen las *lanches* imraguen hacia Tidra y los bancos
([Routard · Iwik](https://www.routard.com/fr/guide/afrique/mauritanie/cote-atlantique/banc-d-arguin/iwik),
[Nomadays](https://www.voyagemauritanie.com/guide-mauritanie/attraction/banc-d-arguin-park)).
El PNBA confirma las condiciones: 200 MRU por persona y noche, **autorización previa del PNBA para todo vehículo
o embarcación**, guía obligatorio la primera vez, 4x4 y GPS recomendados, prohibido salir de las pistas y
desembarcar en las islas ([pnba.mr · Nous visiter](http://www.pnba.mr/nous-visiter/)).
La coordenada de la app (19.87841 / -16.30442) es el nodo OSM `place=village` de Iwik. en.wikipedia da
19.84944 / -16.33083 para «Iouik» ([en.wikipedia](https://en.wikipedia.org/wiki/Iouik)), 4,2 km al SO; se
mantiene el nodo de OSM, que es la fuente preferente para pueblos según el propio encargo.

### poi-10 · Parque de Diawling — coordenada mantenida, con salvedad

La coordenada de la app (16.39078 / -16.35094) **no es un centroide de polígono**: es el nodo OSM 7656035646
«Diawling National Park» ([mapcarta](https://mapcarta.com/30791176)). Aun así no es una puerta ni una oficina:
cae en pleno humedal, 4 km al este del pueblo de Ziré Taghrédient (nodo OSM 9074174945, 16.40221 / -16.3846,
[mapcarta](https://mapcarta.com/N9074174945)) y 21 km de Diama.

El punto de acceso oficial **sí está documentado, pero no cartografiado**: el propio parque dice que
«la maison du parc se trouve à 12 km après le poste de frontière de Diama» viniendo de Saint-Louis, que la
entrada cuesta 200 MRU por persona y noche, y describe la variante norte (carretera de Rosso → Tiguent → desvío
a la derecha a los 50 km → Keur Macène a 35 km → pista a la derecha hasta la dique internationale)
([pnd.mr · Venir au PND](https://www.pnd.mr/venir-au-pnd/)). **No he conseguido una coordenada verificable de esa
«maison du parc»**: no existe en OSM (ni oficina, ni puerta, ni puesto, según los listados de mapcarta del parque
y de Keur Macène), el mapa incrustado en pnd.mr apunta a 16.886745 / -16.494997 —fuera del parque, inservible— y
la ficha de Petit Futé da 21.00789 / -10.94084, que es un centroide por defecto de Mauritania, en pleno desierto.
**No invento el punto**: se deja la coordenada actual y se traslada al texto el dato accionable (12 km después de
Diama, entrada de pago). Queda como **NO VERIFICADO** más abajo.

---

## (d) Consulados de España: los dos SIN_REF **no son alucinaciones**

Esto era lo más grave que había sobre la mesa y la respuesta es tranquilizadora. La lista oficial de la Embajada
de España en Nuakchot ([exteriores.gob.es · Consulados](https://www.exteriores.gob.es/Embajadas/nouakchott/es/Embajada/Paginas/Consulados.aspx))
recoge **exactamente los tres** puntos de la ficha, con los mismos teléfonos y correos:

| ficha | oficial | contraste |
|---|---|---|
| log-4 · Consulado de España en Nuadibú · +222 4574 5371 · emerg. 4670 7502 · con.nouadhibou@maec.es | **Consulado en Nuadibú** (de carrera) · (+222) 45 74 53 71 · emerg. 46 70 75 02 · con.nouadhibou@maec.es | coincide al dígito |
| log-5 · Consulado honorario de España en Rosso · +222 4690 1067 | **Consulado Honorario en Rosso** · cónsul D. Al Hassane Diew · (+222) 46 90 10 67 · alhassanediew@gmail.com | coincide |
| log-6 · Consulado honorario de España en Chinguetti · +222 3445 6929 · sasbureau@yahoo.fr | **Consulado Honorario en Chinguetti** · cónsul D. Mohamed Amara · (+222) 34 45 69 29 · sasbureau@yahoo.fr | coincide |

Así que **log-5 y log-6 existen** y el SIN_REF era solo ausencia en OSM/Wikidata, no invención. Se ha añadido a
cada `info` el nombre del cónsul y el correo oficiales, y se ha dicho con claridad que la coordenada es urbana
aproximada porque **Exteriores no publica dirección postal de ninguno de los dos honorarios**.

El DUDOSO de **log-4** también era falso positivo: el único candidato OSM a 3 km era el Consulado Honorario de
Guinea-Bissau, sin relación. España sí tiene consulado **de carrera** en Nuadibú, y la ficha de recomendaciones de
viaje de Exteriores da la dirección: **Boulevard Médian s/n, B.P. 175**
([exteriores.gob.es · recomendaciones de viaje Mauritania](https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Mauritania)).
De la misma fuente se ha añadido la dirección de la embajada (log-3): **Rue Mamadou Konaté s/n, B.P. 232**.
No he logrado geolocalizar el edificio del consulado: no está en OSM (mapcarta no lista ninguna oficina
diplomática en Nuadibú) y no hay número en «Boulevard Médian s/n». La coordenada sigue siendo urbana y ahora el
texto lo dice.

De paso, esa misma página oficial valida los tres puntos sanitarios privados de Nuakchot de la ficha: Exteriores
recomienda **Medipol, Kissi, Chiva e Ibn Sina** en Nuakchot, el Centro Hospitalario Regional («Hospital Español»)
y el Centro de Especialidades en Nuadibú, y el «Hospital Español» / Hôpital de la Fraternité en Chinguetti — que
es justamente log-10.

---

## (e) Puntos NO VERIFICADOS

1. **poi-10 · «maison du parc» del Diawling.** Existe y está documentada por el parque (12 km después del puesto
   de Diama), pero **no he podido obtener su coordenada**. Probado: OSM vía mapcarta (parque, Ziré Taghrédient,
   Keur Macène, Diama — ninguna oficina, puerta ni puesto), pnd.mr (presentación, «venir au PND», contacto: 404),
   fr/en.wikipedia, Ramsar RSIS ficha 666, Petit Futé, Lonely Planet, IUCN, blogs de viaje (travelblog.org: 403).
   La coordenada de la app se mantiene porque al menos es el nodo OSM del parque.
2. **log-4 · edificio del Consulado de España en Nuadibú.** Dirección oficial conocida (Boulevard Médian s/n),
   edificio no cartografiado. La coordenada 20.93 / -17.033 es el centro de Nuadibú, no la puerta.
3. **log-5 y log-6 · sedes de los consulados honorarios de Rosso y Chinguetti.** La institución está confirmada;
   la **ubicación física no**, porque Exteriores no publica dirección. Son consulados honorarios: suelen operar
   desde el domicilio o el negocio del cónsul, así que lo sensato es telefonear antes, como ya dice el `info`.
4. **Anchura exacta de la tierra de nadie de Guerguerat.** Las fuentes de viajeros dan entre 1 km y 5 km; se ha
   puesto «unos 4 km», que es el dato de la fuente más detallada. Los puestos sí están medidos (3,5 km entre uno
   y otro en línea recta).

---

## (f) Correcciones de texto aplicadas

| id | qué se ha corregido |
|---|---|
| log-0 | El `info` no distinguía el puesto marroquí del mauritano —justo la confusión que provoca el error de 10 km—. Ahora nombra el complejo PK55, da la coordenada del puesto marroquí (21.36266 / -16.96084) y la tierra de nadie de ~4 km. |
| log-3 | Añadida la dirección oficial: Rue Mamadou Konaté s/n, B.P. 232. |
| log-4 | Añadido «consulado de carrera (no honorario)» y la dirección oficial Boulevard Médian s/n, B.P. 175. «Coordenada urbana provisional» → se explicita que el edificio no está en OSM y que el punto no es la puerta. |
| log-5 | Añadidos cónsul honorario (D. Al Hassane Diew) y correo oficial; se sustituye «provisional» por el motivo real (Exteriores no publica dirección). |
| log-6 | Ídem con D. Mohamed Amara. |
| poi-2 | «próximo a Ben Amera… a unos 7 km» → «a unos 8 km al noroeste de Ben Amera», y se fecha el conjunto escultórico en 1999, que es lo verificable ([en.wikipedia · Ben Amera](https://en.wikipedia.org/wiki/Ben_Amera)). |
| poi-10 | «enlace potencial con Diama» → dato accionable y verificado: casa del parque 12 km después del puesto de Diama, entrada de pago por persona y noche ([pnd.mr](https://www.pnd.mr/venir-au-pnd/)). |

Textos revisados y **dejados como estaban** por ser correctos: poi-1 (Ben Amera y el eje ferroviario — es el mayor
monolito de África y el segundo del mundo, 4 km al norte de la vía), poi-3, poi-4, poi-5, poi-7 (el punto está a
~1 km del centro de la estructura de Richat según en.wikipedia), poi-8 (autorización, guía y pistas: exactamente
lo que exige el PNBA), poi-11, poi-12.

---

## (g) Interés de los PDIs y sugerencias

**Lo que sostiene la ficha.** Mauritania es, con diferencia, el país mejor construido de los auditados hasta
ahora: 12 PDIs, ninguno inventado, y un bloque central —**Adrar**— que se defiende solo. Chinguetti (poi-3),
Ouadane (poi-4), Guelb er Richat (poi-7), Terjit (poi-5), Tifoujar (poi-11) y Valle Blanco (poi-12) forman un
circuito coherente de 4-6 días que se apoya en Atar y que no se repite en ningún otro país de la ruta. **Ben
Amera y Aïcha** (poi-1, poi-2) son el otro gran acierto: el mayor monolito de África con un conjunto escultórico
contemporáneo en mitad de la nada, y además caen sobre el eje ferroviario, así que no obligan a un desvío
gratuito. **Iwik / Banc d'Arguin** (poi-8) es el punto de mayor valor natural y el más problemático con el perro:
el PNBA exige autorización escrita previa para cada vehículo, guía la primera vez y prohíbe salir de las pistas;
la `dog` de la ficha ya lo refleja, y es el único PDI del país donde yo daría por probable un «no».

**Lo flojo o repetitivo, para que el propietario decida.**

- **poi-6 «Atar»** no es un PDI, es logística: `cat: Servicios`, `prio: Logística`, y su coordenada
  (20.51819 / -13.05439) es **idéntica** a la de log-15 (Combustible · Atar) y log-17 (Agua potable). Tres
  chinchetas sobre el mismo punto. Sugerencia: dejarlo como está si la app los pinta en capas distintas, pero si
  comparten mapa, sobra una.
- **poi-11 y poi-12** son el mismo día y están a 9 km: el paso de Tifoujar se baja *hacia* el Valle Blanco. No es
  duplicación —son dos cosas distintas— pero conviene que el texto de uno remita al otro para que no parezcan dos
  jornadas.
- **poi-9 Puerto pesquero de Nuakchot** es el único PDI urbano y su `prio: Media` me parece correcta. Advertencia
  que yo reforzaría: en Mauritania la fotografía de instalaciones portuarias y de personas sin permiso da
  problemas reales; la `desc` ya lo dice y está bien que lo diga.
- **poi-10 Diawling** solo tiene sentido si se sale por Diama. Si al final se sale por Rosso, es un desvío de 90 km
  por pista para ver lo mismo que el Djoudj senegalés, que está 9 km al sureste del mismo humedal.

**Hasta tres PDIs que faltan** (coordenadas verificadas en esta sesión, para que el propietario decida):

| propuesta | lat / lon | por qué | fuente |
|---|---|---|---|
| **Azougui** | 20.5682 / -13.1104 | Primera capital de los almorávides (s. XI), con ciudadela, grabados rupestres y la necrópolis del imán al-Hadrami; al-Bakri describía una fortaleza «rodeada de 20.000 palmeras». Está **8 km al noroeste de Atar**: coste logístico cero desde la base que la ficha ya usa, y es la pieza histórica que le falta al bloque del Adrar (que hoy es solo Chinguetti y Ouadane). | [mapcarta · Azougui, vía OSM 251644693](https://mapcarta.com/fr/Azougui) · [en.wikipedia](https://en.wikipedia.org/wiki/Azougui) |
| **Choum** | 21.300 / -13.067 | Parada del tren del hierro y del túnel de 2 km excavado en granito para que la línea no pisara el Sáhara español. Es donde los overlanders ven (o cargan) el tren, y está en el eje Atar–Nuadibú que la ruta ya recorre. Complementa a Ben Amera, que es el otro punto ferroviario. | [en.wikipedia · Choum](https://en.wikipedia.org/wiki/Choum) |
| **Baie de l'Étoile (Nuadibú)** | 21.03665 / -17.01685 | Laguna a 12 km al norte de Nuadibú, la excursión clásica de la ciudad y el único paisaje costero del norte antes del vacío hasta Nuakchot. **Aviso**: OSM tiene mapeado un «Champ de mines» en esa península, además del cementerio de barcos; antes de proponer vivac hay que verificar la zona sobre el terreno. | [mapcarta · Baie de l'Étoile, nodo OSM 3304354292](https://mapcarta.com/fr/Baie-de-l%27%C3%89toile) |

---

## (h) Fuentes abiertas que fallaron

- **Photon** (`photon.komoot.io`) — `robots.txt` lo prohíbe a WebFetch.
- **Nominatim** (`nominatim.openstreetmap.org`, mirror `nominatim.geocoding.ai`) — `robots.txt`.
- **openstreetmap.org** (`/search`, `/way/…`, `/node/…`) — `robots.txt`. El mirror `spike-03.openstreetmap.org`
  falla la verificación TLS.
- **Overpass**: `overpass-api.de` (robots), `overpass.kumi.systems` y `overpass.private.coffee` (timeout),
  `overpass.openstreetmap.fr` (403), `maps.mail.ru` (bloqueado), `overpass.nchc.org.tw` (DNS).
  `overpass.osm.ch` **sí responde**, pero es un extracto solo de Suiza: devuelve vacío para Mauritania.
- **curl directo**: el proxy del contenedor devuelve `403 CONNECT` para casi todo (overpass, exteriores.gob.es,
  wikipedia). Solo WebFetch/WebSearch atraviesan.
- **fr.wikivoyage.org** y **en.wikivoyage.org** — «cache-only, cannot be fetched». Se sustituyó por wikitravel
  (403) y, finalmente, por fr.wikipedia vía el espejo **wikimonde.com**.
- **wikidata.org** — «cache-only»; se usaron los datos de Wikidata ya presentes en `_eval.json`.
- **wikimapia.org** — bucle de redirección https→http.
- **embassypages.com**, **travelblog.org**, **wikitravel.org** — 403.
- **pnd.mr/contact/** — 404 (la información de contacto está en `presentation/` y `venir-au-pnd/`).
- **geonames.org** — no tiene «PK 55» ni el puesto fronterizo mauritano.

**Lo que sí funcionó y conviene apuntar para los siguientes países**: `mapcarta.com` expone los nodos de OSM con
su id (`/N…`, `/W…`) y sus coordenadas exactas, incluidos los nombres en árabe, y además lista los vecinos con
distancia y rumbo. Ha resuelto, él solo, Guerguerat, Ben Amera, Oued el Abiod, Diawling, Azougui y la Baie de
l'Étoile.

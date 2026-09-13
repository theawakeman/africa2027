# Auditoría de PDIs y puntos logísticos · Costa de Marfil

Encargo: resolver los 10 puntos marcados **DESPLAZADO** en `costa-de-marfil_eval.md` y revisar los 2 marcados **AREA**.
Ficheros editados: `content/pois/costa-de-marfil.json` y `content/ficha/costa-de-marfil.json` (clave `logistics`). Nada más.

Restricción de la sesión: **Photon, Nominatim y Overpass estaban bloqueados**. Toda coordenada nueva sale de
**mapcarta.com** (que publica el nodo/vía OSM con su id), de **Wikipedia (fr/en)**, de **whc.unesco.org** o de
**exteriores.gob.es**, abiertos en esta sesión y citados uno por uno más abajo. No hay ni una coordenada de memoria.

---

## (a) Correcciones aplicadas

| id | nombre | antes (lat/lon) | después (lat/lon) | dist. | fuente |
|---|---|---|---|---|---|
| poi-3 | Dent de Man (881 m) | 7.4553 / -7.5192 | **7.45635 / -7.54433** | 2,8 km | nodo OSM 2771375332 `natural=peak`, 881 m · https://mapcarta.com/fr/Dent_de_Man · concuerda con Wikidata Q23211571 |
| poi-4 | Mont Tonkoui (1.189 m) | 7.455 / -7.625 | **7.45409 / -7.63705** | 1,3 km | nodo OSM 2747243570 `natural=peak`, 1.189 m, `alt_name` «Mont Tonkpi» · https://mapcarta.com/fr/Mont_Tonkoui |
| poi-5 | La Cascade de Man | 7.3833 / -7.5667 | **7.41205 / -7.58638** | 3,9 km | nodo OSM 2747251631 `waterway=waterfall` «Les Cascades Naturelles de Man» · https://mapcarta.com/fr/Les_Cascades_Naturelles_de_Man |
| poi-6 | Puente de lianas de Lieupleu | 7.2667 / -7.7167 | **7.07981 / -8.11069** | 48,2 km | nodo OSM 3166611267 «Pont de Lianes» (`tourism`) · https://mapcarta.com/N3166611267 · duplicado en el nodo 7925196779 «Natural bridge Liana» (mirador) a 16 m · https://mapcarta.com/fr/Natural_bridge_Liana |
| poi-7 | Cascadas de Gbêtitapéa (Daloa) | 6.9167 / -6.4333 | **6.79001 / -6.45093** | 14,2 km | nodo OSM 2972278915, aldea de Gbétitapéa · https://mapcarta.com/N2972278915 — **la cascada no está verificada**, ver (c) |
| poi-15 | Assinie-Mafia y el cordón litoral | 5.1333 / -3.4667 | **5.13508 / -3.29166** | 19,4 km | nodo OSM 1625148248 `place=town` · https://mapcarta.com/fr/Assinie-Mafia · Wikidata Q2867185 y en.wikipedia coinciden |
| poi-17 | Parque Nacional de la Comoé | 8.75 / -3.7 | **8.65506 / -3.78235** | 13,9 km | nodo OSM 443375092, aldea-puerta de **Kakpin** · https://mapcarta.com/fr/Kakpin |
| log-0 | Frontera Gbapleu / N'Zoo | 7.1 / -8.4 | **7.57104 / -8.32829** | 53,0 km | nodo OSM 1207752423, pueblo marfileño de Gbapleu · https://mapcarta.com/16923022 |
| log-1 | Frontera Noé / Elubo | 5.1167 / -2.7667 | **5.28994 / -2.78675** | 19,4 km | nodo OSM 4787240562 «Poste frontière de Noé» · https://mapcarta.com/fr/Poste_Fronti%C3%A8re_de_No%C3%A9 |
| log-2 | Frontera Soko / Sampa | 7.9717 / -2.7189 | **7.98753 / -2.73859** | 2,8 km | nodo OSM 5104802536 «Poste Frontière de Soko» · https://mapcarta.com/fr/Poste_Fronti%C3%A8re_de_Soko |
| log-3 | Frontera Sipilou | 7.9833 / -8.0333 | **7.85747 / -8.10995** | 16,3 km | vía OSM 1379395777 «Poste Frontière» (comisaría) en Sipilou · https://mapcarta.com/fr/W1379395777 |
| log-4 | Embajada de España en Abiyán | 5.36 / -3.97 | **5.34617 / -4.00593** | 4,3 km | nodo `office=diplomatic` «Embassy of Spain» (de `costa-de-marfil_eval.json`); dirección confirmada en https://www.exteriores.gob.es/Embajadas/abidjan/es/Paginas/index.aspx |
| log-6 | Hospital regional de Man | 7.4125 / -7.5539 | **7.40638 / -7.54781** | 0,96 km | vía OSM 786544752 `amenity=hospital` «Centre Hospitalier Régional de Man» · https://mapcarta.com/fr/Centre_Hospitalier_R%C3%A9gional_de_Man |

### Los tres casos que el encargo marcaba como dudosos

**poi-4 · ¿Tonkoui y Tonkpi son la misma montaña? SÍ.** El nodo OSM 2747243570 se llama *Mont Tonkoui*, tiene 1.189 m
—exactamente la altitud que da la Wikipedia francesa para el Tonkoui— y lleva como nombres alternativos *Mont Tonkpi*
y *Mont Tounkui*. La Wikipedia francesa abre el artículo con «Mont Tonkoui ou Tonkpi». Es una sola cumbre con dos
nombres, y es la que da nombre a la región del Tonkpi. Lo que está mal es **Wikidata**, que tiene tres ítems para la
misma montaña (Q23092405 a 2,9 km y Q23092403 a 38 km del punto de la app): por eso la evaluación automática dio
DESPLAZADO contra un candidato equivocado. Se ha movido el punto al nodo OSM, a 1,3 km del anterior.

**poi-6 · el «Pont de Lianes» de OSM SÍ es el de Lieupleu; la evaluación se equivocaba al descartarlo.** El
candidato de `highway=track` a 47 km no era un puente cualquiera: está a **200 m del pueblo de Lieupleu**
(nodo OSM 3048233374, 7,095091 / -8,108132 · https://mapcarta.com/N3048233374) y es la pista de acceso. El puente en
sí está cartografiado 1,7 km al sur, dos veces en el mismo punto: como `tourism` «Pont de Lianes» (nodo 3166611267) y
como mirador «Natural bridge Liana» (nodo 7925196779). Las páginas de Lieupleu **y** de Vatouo lo listan como el
lugar notable de su entorno, y la de Séileu —chef-lieu de subprefectura, departamento de **Danané**— lo sitúa «7 km
al este». Es decir: el puente está en el par de aldeas **Lieupleu (1,7 km al norte) / Vatouo (0,5 km al oeste)**,
subprefectura de Séileu, departamento de Danané, a **21 km al sur de Danané** (nodo OSM 1597916993, 7,2631 / -8,1546)
y a **72 km al suroeste de Man**, no a los «20-40 km de Man» que decía la ficha. El punto se ha movido al puente y el
texto se ha reescrito con la geografía correcta. Reserva anotada en (c): de qué aldea es «propiedad» el puente
—Lieupleu o Vatouo— no se ha podido cerrar con fuente.

**log-0 · coherencia con la ficha de Guinea: cerrada.** La auditoría de Guinea fijó el Poste Frontière guineano en
7,609819 / -8,311217, la Police aux frontières en 7,6206 / -8,30528 y las Douanes en el pueblo de N'Zoo
(7,677195 / -8,314697), y dejó escrito que «del lado marfileño, el pueblo de Gbapleu queda 4,5 km al suroeste».
La página de mapcarta del Gbapleu correcto (nodo OSM 1207752423, 7,57104 / -8,32829) lo confirma desde el otro lado:
lista un «Poste Frontière» (comisaría) a 4½ km al noreste y una «Border Police» a 6 km al noreste — que son
exactamente los dos nodos guineanos de la ficha de Guinea. Distancia calculada Gbapleu → Poste Frontière guineano:
**4,7 km**. El punto marfileño queda en el lado marfileño del mismo paso y el `info` lo dice explícitamente, con la
secuencia completa de las cuatro paradas. De los tres «Gbapleu» de OSM, el de Duékoué (6,47932 / -7,15838) está a
153 km y el tercero es un **barrio de la propia Man** (nodo 3199171274, 7,40723 / -7,52887): ambos quedan anotados
en el `info` para que nadie vuelva a tropezar.

### Los dos AREA revisados

**poi-15 Assinie-Mafia.** El punto viejo (5,1333 / -3,4667) no era un centroide flojo: estaba **delante de
Assouindé** (nodo OSM 4197281156, 5,165291 / -3,469094), 20 km al oeste del pueblo de Assinie-Mafia. Movido al
`place=town`. De paso se corrige el texto, que colocaba Assouindé «hacia el este» cuando está al oeste, viniendo de
Grand-Bassam. La distancia al paso de Noé que promete la ficha («60 km») se sostiene: 58,5 km en línea recta hasta el
nuevo nodo del puesto fronterizo.

**poi-17 Comoé.** El encargo sugería Kafolo o Gansé. Se ha elegido **Kakpin** (8,65506 / -3,78235, subprefectura del
departamento de Nassian, región del Bounkani) por coherencia con el propio aviso de seguridad de la ficha, que dice
«solo por la puerta SUR de Kakpin… y NUNCA por Kafolo». Kafolo (nodo OSM 2775849322, 9,58611 / -4,31203) está a
118 km al noroeste y pegado a Burkina: es justo el sitio de los ataques de 2020-2021 que el propio texto cita.
Gansé (nodo OSM 443375211, 8,621739 / -3,914953) está a 15 km al oeste de Kakpin, mismo flanco sur, y queda anotado
en el texto como alternativa. Desde Kakpin, la Station de Recherche en Écologie de la Comoé queda 11-13 km al norte,
ya dentro del parque. Fuentes: https://mapcarta.com/fr/Kakpin · https://mapcarta.com/fr/Kafolo ·
https://mapcarta.com/fr/Gans%C3%A9

---

## (b) PDIs eliminados

**Ninguno.** No se ha encontrado ningún PDI que pueda darse por inexistente con seguridad. El único candidato serio a
alucinación —poi-7, las cascadas de Gbêtitapéa— se mantiene y queda marcado NO VERIFICADO, conforme a la regla de
que solo se borra lo que se sabe falso.

---

## (c) Puntos NO VERIFICADOS o verificados con reservas

- **poi-7 · Cascadas de Gbêtitapéa: la cascada no existe en ninguna fuente abierta que se haya podido abrir.**
  No está en OpenStreetMap (ni la página de Daloa ni la de Gbétitapéa listan ningún `waterfall`, `cascade` o `chute`),
  y el artículo de Daloa en la Wikipedia francesa no menciona ni cascadas ni sitios turísticos ni el topónimo
  Gbêtitapéa. Lo que **sí** está verificado es la **aldea** de Gbétitapéa (nodo OSM 2972278915, 6,79001 / -6,45093,
  subprefectura de Daloa, 1.190 habitantes), y ahí se ha anclado el punto — pero ojo: está **11 km al sur del centro
  de Daloa**, junto al aeródromo, no «a pocos kilómetros del centro» como decía la ficha. El texto lo dice ahora en
  la primera línea, en mayúsculas. Probado: mapcarta de Daloa, de Gbétitapéa y búsquedas directas de
  «Cascade de Gbêtitapéa» y «Chutes de Gbêtitapéa» (404 las dos), más fr.wikipedia/Daloa.
- **poi-6 · a qué aldea «pertenece» el puente de lianas.** El puente está localizado sin dudas (dos nodos OSM en el
  mismo punto), pero la atribución del nombre no se ha podido cerrar: está a 0,5 km de **Vatouo** y a 1,7 km de
  **Lieupleu**, y las páginas de las dos aldeas lo reclaman. Se ha conservado el nombre del PDI (Lieupleu) porque es
  el que usa la ficha y el que lleva la pista de acceso en OSM, pero el texto nombra ahora el par Lieupleu/Vatouo.
  No existen artículos «Lieupleu» ni «Pont de lianes» en la Wikipedia francesa. Los otros puentes que citaba el texto
  (Gbangbégouiné, Niahoin, y Gouéssesso que menciona poi-22) **no están cartografiados y no se han verificado**: el
  texto los degrada a «se citan… pero no se han podido verificar».
- **log-0, log-1, log-2, log-3 · el puesto de barrera solo está cartografiado en tres de los cuatro pasos.**
  En Noé, Soko y Sipilou el punto cae ahora sobre un nodo/vía OSM que es literalmente el puesto fronterizo. En
  **Gbapleu** OSM no cartografía nada del lado marfileño: el pin marca el pueblo, a 4,7 km de la barrera guineana.
  Error residual esperable en ese único caso: unos kilómetros. Irrelevante para navegar, relevante si alguien espera
  que el pin caiga sobre la cabina.
- **log-3 · horario y capacidad aduanera de Sipilou siguen sin confirmar.** Lo que sí se ha ganado es geografía: los
  trámites marfileños están en el extremo sur del pueblo de Sipilou (comisaría «Poste Frontière», con la **Douane**
  y el **Poste de Contrôle Sanitaire de Sipilou** 260-270 m al norte), no en la raya 16 km más al norte donde
  apuntaba la ficha. Que haya aduana y control sanitario cartografiados es un indicio fuerte de que el paso es
  formal, pero no sustituye a la llamada de confirmación 72 h antes que ya pedía el texto.
- **log-2 · la cita del Logistics Cluster no se ha podido reverificar.** El `info` atribuye al LCA de Naciones Unidas
  el horario 06:00-18:00, el tráfico diario y la aduana manual de Soko. No se ha tocado la cifra, pero **el LCA no
  se ha podido abrir** (ver (f)): queda como cita heredada, no como dato reverificado en esta sesión.
- **poi-3 · el punto de salida de la Dent de Man.** El texto decía «se sube desde el pueblo de Zadepleu / el barrio
  de Libreville». **Zadepleu está junto a la Cascade de Man**, 8 km al suroeste de la cumbre (la escuela EPP Zadepleu
  figura a 720 m del salto de agua): no puede ser el pie de la Dent. OSM sitúa al pie de la cumbre Glongouin,
  Zogoualé y Bantégouen. El texto se ha reescrito para decir eso y dejar la contratación del guía en Man; el barrio
  de Libreville no se ha podido verificar y se ha retirado.

---

## (d) Correcciones de texto

| id | qué decía | qué dice ahora | fuente |
|---|---|---|---|
| poi-3 | «se sube desde el pueblo de Zadepleu / el barrio de Libreville» | Zadepleu está en la Cascade, 8 km al SO; los pueblos al pie son Glongouin, Zogoualé y Bantégouen; guía contratado en Man | mapcarta Dent de Man y Les Cascades Naturelles de Man |
| poi-4 | «a unos 20 km al noroeste de Man» | «a unos 11 km en línea recta (una veintena por la pista)» + aclaración Tonkoui = Tonkpi = Tounkui | distancia calculada Man (nodo OSM) → cumbre; fr.wikipedia/Mont_Tonkoui; `alt_name` del nodo OSM |
| poi-5 | «A unos 5 km del centro de Man» | «A unos 4 km al oeste del centro de Man, junto a Zadepleu y al bosque sagrado de Gbêpleu» | distancia calculada; mapcarta del nodo de la cascada |
| poi-6 | «Lieupleu, Vatouo, Gbangbégouiné y Niahoin, a 20-40 km de Man» | par Lieupleu/Vatouo, subprefectura de Séileu, dpto. de Danané, 21 km al S de Danané y 72 km al SO de Man; el resto, «se citan pero no verificados» | mapcarta Lieupleu / Vatouo / Séileu / Danané |
| poi-7 | «A pocos kilómetros del centro de Daloa, en el barrio-aldea de Gbêtitapéa» | «NO VERIFICADO… la aldea de Gbêtitapéa, a unos 11 km al sur del centro de Daloa» | mapcarta Gbétitapéa; fr.wikipedia/Daloa |
| poi-15 | «Más allá, hacia el este, está Assouindé» | «Assouindé queda 20 km al OESTE, viniendo de Grand-Bassam, no al este» | mapcarta Assouindé (nodo 4197281156) |
| **poi-16** | «Samatiguila, Kong y Bondoukou forman el conjunto **candidato** a la Lista del Patrimonio Mundial» | el bien fue **inscrito en 2021** y sus ocho mezquitas están en Tengréla, Kouto, Sorobango, Samatiguila, Nambira, Kong (dos) y Kaouara: **Bondoukou NO forma parte**; la más cercana es Sorobango, 18 km al NE | https://whc.unesco.org/en/list/1648 · mapcarta Sorobango (nodo 1075803075) |
| poi-17 | «Coordenada del centro del parque» | Kakpin como puerta sur navegable; Kafolo descartado (>100 km al NO, pegado a Burkina); Gansé como alternativa | whc.unesco.org/en/list/227 · mapcarta Kakpin / Kafolo / Gansé |
| log-0 | «Coordenada aproximada del puesto» | geometría completa del paso (4 paradas, coordenadas de las 4) + aviso de los dos homónimos | ficha de Guinea + mapcarta Gbapleu |
| log-1/2/3 | sin nota de coordenada | cada una dice sobre qué nodo OSM se ha fijado y dónde caía la anterior | mapcarta de cada puesto |
| **log-4** | «Tel. +225 22 44 48 50. Demarcación que cubre también **Guinea** y otros países del entorno» | «08 B.P. 876 — Abidjan 08. Tel. +225 27 22 44 48 50 y +225 27 22 44 45 77 · fax 27 22 44 71 22 · urgencia consular +225 07 07 42 57 89. Demarcación: Costa de Marfil y **LIBERIA**» | https://www.exteriores.gob.es/Embajadas/abidjan/es/Paginas/index.aspx |
| log-6 | «Referencia hospitalaria del bloque de montaña» (coordenada = centro de Man) | nombre completo, barrio de Thérèse, junto al estadio y al mercado, 24 h, y la coordenada sobre el recinto | mapcarta Centre Hospitalier Régional de Man (vía OSM 786544752) |

### Verificado y correcto, sin cambios

- **poi-17 Comoé**: 11.500 km² (UNESCO da 1.149.450 ha), inscrito 1983, en Peligro 2003-2017. Los tres datos de la
  ficha son correctos. https://whc.unesco.org/en/list/227
- **poi-15**: «a 60 km del paso de Noé» → 58,5 km en línea recta con las coordenadas nuevas. Correcto.
- **log-0**: «48 km entre la frontera y Danané» → 40 km en línea recta de Gbapleu a Danané, compatible con 48 km de
  carretera. Correcto.
- **poi-3**: 881 m confirmados por el nodo OSM. **poi-4**: 1.189 m confirmados por OSM y por fr.wikipedia.

### La corrección que NO se ha podido aplicar aquí

La ficha de **Liberia** (`content/ficha/liberia.json`, log-5) lleva la misma embajada con el teléfono antiguo
(«+225 22 44 48 50») y sin el apartado de correos. La coordenada ya es la correcta (5.34617 / -4.00593), así que las
dos fichas son **coherentes en el mapa**, pero el texto de Liberia se ha quedado desactualizado. Queda fuera del
alcance de este encargo (solo se podían tocar los dos JSON de Costa de Marfil): **conviene propagarlo**. También
resuelve la reserva que dejó abierta la auditoría de Liberia: la dirección «Impasse Ablaha Pokou, Cocody Danga Nord»
**está confirmada** por el Ministerio, y la demarcación es Costa de Marfil + Liberia (no Guinea).

---

## (e) Interés de los PDIs y sugerencias

**El bloque de Man sale reforzado.** Con las coordenadas corregidas, Dent de Man, Tonkoui y la Cascade forman un
triángulo real de 4-5 km alrededor de Man: las tres se hacen desde la misma base, en dos días, y el Tonkoui es
además una subida 4x4 con cima conducible, que es exactamente lo que busca una expedición con vehículos. Alta
prioridad bien puesta.

**Puntos flojos o problemáticos:**

- **poi-7 · Cascadas de Gbêtitapéa (prio Media).** Es el punto más débil de la ficha: sitio no verificable, coordenada
  ahora anclada a una aldea a 11 km del centro de Daloa, y el propio texto ya lo vendía como «parada lógica a mitad
  de camino». Si en Daloa nadie sabe dar razón del sitio, es candidato a **bajar a prio Baja o a fusionarse con una
  parada de servicios en Daloa**. No se ha tocado `prio` porque la regla del encargo lo reserva a errores evidentes.
- **poi-21 Séguéla (prio Media)** y **poi-18 Bouaké (prio Media)** son, en el fondo, el mismo tipo de punto que
  log-12 y log-13 (combustible del eje de subida): útiles como logística, repetitivos como PDI. No molestan, pero el
  interés está en el `info`, no en el pin.
- **poi-17 Comoé** sigue siendo, con o sin coordenada arreglada, un PDI que probablemente no se ejecute: el propio
  texto lo declara condicional y desaconsejado. Está bien que siga en la ficha como decisión documentada.
- **poi-6, tras la corrección, cambia de sitio en la ruta.** Ya no es una excursión desde Man, sino un desvío de
  ~21 km al sur de **Danané** — es decir, cae de forma natural **el primer día**, nada más entrar por Gbapleu, antes
  de llegar a Man. Merece la pena replantear el orden de la etapa: el puente queda casi de paso, y no a 70 km de
  vuelta desde Man.

**Hasta tres PDIs que faltan (coordenadas verificadas en esta sesión, para que el propietario decida):**

1. **Parc National du Banco — Abiyán** · 5,38516 / -4,05233 · 30 km² de selva primaria **dentro** de la ciudad, con
   el célebre «lavoir de Banco» del río. La ficha ya lo menciona de pasada en la descripción de Abiyán (poi-13) pero
   no tiene pin propio. Es el único sitio del viaje donde se puede ver selva de galería sin salir de una capital, y
   está a tiro de la base canina de Cocody. Fuente: https://mapcarta.com/fr/Parc_national_du_Banco (Wikidata
   Q1858100). *Nota: esa coordenada es el centro del polígono; antes de publicarlo habría que anclarlo a la entrada
   de Attécoubé, que no se ha podido localizar en OSM en esta sesión.*
2. **Grand-Béréby (costa de San-Pédro)** · 4,65076 / -6,92474 · nodo OSM 2728722168, `place=town`. El texto de
   poi-11 ya lo cita —con la grafía «Grand-Bérébi»— como «las mejores playas que he visto en mi vida» según un
   overlander, pero no tiene punto propio y con la grafía de la ficha un GPS no lo encuentra. Es la última playa
   antes de la frontera de Liberia y la pareja lógica de Sassandra en el corredor de bajada.
   Fuente: https://mapcarta.com/fr/Grand-B%C3%A9r%C3%A9by
3. **Mezquita de Sorobango** · 8,17479 / -2,70921 · nodo OSM 1075803075, departamento de Bondoukou, 18 km al noreste
   de la ciudad. Es **la mezquita del bien UNESCO que realmente queda en la ruta de subida** (Bondoukou no está
   inscrita, ver (d)), y está muy lejos de la franja de seguridad del norte. Convierte la parada de Bondoukou de
   «ciudad de servicios con mezquitas de adobe» en una visita a Patrimonio Mundial de verdad.
   Fuentes: https://whc.unesco.org/en/list/1648 · https://mapcarta.com/fr/Sorobango

---

## (f) Fuentes abiertas que fallaron

- **Photon, Nominatim y Overpass**: bloqueados desde el contenedor por política de egreso (era la premisa del
  encargo). Toda la verificación se ha hecho contra mapcarta, que publica el id del nodo/vía OSM y sus coordenadas.
- **API de MediaWiki** (`fr.wikipedia.org/w/api.php`, `en.wikipedia.org/w/api.php`): devuelven
  «This domain is cache-only and cannot be fetched». Solo funcionan las URL de artículo (`/wiki/...`).
- **API de OpenStreetMap** (`api.openstreetmap.org/api/0.6/node/….json`): `ROBOTS_DISALLOWED`.
- **Logistics Cluster de Naciones Unidas**: la portada `lca.logcluster.org/` carga, pero **todas** las rutas de país
  fallan: `/cote-divoire` → 403, `/cote-d-ivoire` → 404, `/cote-divoire-24-border-crossing` → 403,
  `/24-cote-divoire-border-crossing` → 404, `/2-4-cote-divoire-border-crossing` → 404, `/country/civ` → 404, y el
  DLCA histórico `dlca.logcluster.org/display/public/DLCA/2.4+Cote+d'Ivoire+Border+Crossing` → 404. Consecuencia:
  la cita del LCA sobre el puesto de Soko (horario, tráfico, aduana manual) **no se ha podido reverificar**.
- **exteriores.gob.es**: cuatro rutas devolvieron 404 (`/Embajadas/abiyan/es/Paginas/index.aspx`,
  `/Embajadas/abiyan/es/Embajada/Paginas/index.aspx`, `/embajadas/abiyan/...`, `/Embajadas/abiyan/es/Paginas/`).
  **La que sí funciona es con la grafía francesa de la ciudad**: `https://www.exteriores.gob.es/Embajadas/abidjan/es/Paginas/index.aspx`.
  Anotado aquí para las próximas auditorías: la auditoría de Liberia se quedó sin verificar esta dirección por
  probar solo «abiyan».
- **Wikipedia (fr) — artículos inexistentes o no cacheados**: `Lieupleu`, `Pont_de_lianes`, `Noé_(Côte_d'Ivoire)`,
  `Cascade_de_Man`. `Dent_de_Man` en fr es una página de desambiguación sin coordenadas.
- **mapcarta — páginas que no existen**: `Cascade_de_Gbêtitapéa`, `Chutes_de_Gbêtitapéa`, `Poste_Frontière_de_Sipilou`
  (el nodo existe pero se llama solo «Poste Frontière»), `Poste_Frontière_de_Gbapleu`, `Cascades_Naturelles_de_Man`
  (la buena es `Les_Cascades_Naturelles_de_Man`). Además, `mapcarta.com/fr/<nombre>` resuelve al homónimo más
  poblado del mundo: «Noé» da la Baja Austria, «Soko» da Java, «Sampa» da São Paulo. La vía fiable es la lista de
  homónimos al pie de esa misma página, que enlaza a `mapcarta.com/fr/<id interno>` o a `mapcarta.com/N<id OSM>`.
- **WebSearch**: agotado el presupuesto de la sesión (200/200) antes de empezar; toda la investigación se ha hecho
  con WebFetch dirigido.

---

## Validación

```
python3 -c "import json; json.load(open('content/pois/costa-de-marfil.json'))"    → OK (22 PDIs)
python3 -c "import json; json.load(open('content/ficha/costa-de-marfil.json'))"   → OK (16 puntos logísticos)
git diff --stat  → content/ficha/costa-de-marfil.json | 36 ++++-----
                   content/pois/costa-de-marfil.json  | 44 +++++------
```
Solo cambian líneas `lat`, `lon`, `desc` e `info`. Coordenadas a 5 decimales. Formato
`ensure_ascii=False, indent=2` respetado en los dos ficheros.

# Auditoría de PDIs y puntos logísticos · Senegal

Fecha: 2026-09-13 · Entradas: `content/pois/senegal.json` (23 PDIs), `content/ficha/senegal.json` → `logistics` (16 puntos), `audit/geo/senegal_eval.md` / `_eval.json`.

**Nota metodológica.** Photon, Nominatim y Overpass están bloqueados desde este contenedor (`CONNECT tunnel failed, response 403`). Toda coordenada nueva procede de: (a) **mapcarta.com**, que publica los nodos de OpenStreetMap con su id (`N…`/`W…`) y coordenadas decimales; (b) **Wikipedia** (en/fr); (c) **fuentes oficiales** (exteriores.gob.es) o directorios sanitarios senegaleses (DIMO Santé). Cada fila de la tabla lleva la URL usada. No se ha inventado ninguna coordenada.

---

## (a) Correcciones aplicadas

| id | nombre | lat/lon antes | lat/lon después | dist. | fuente |
|---|---|---|---|---|---|
| log-0 | Embajada de España en Dakar | 14.6604, -17.4352 | **14.66292, -17.43621** | 0,30 km | OSM way 901800372 «Ambassade d'Espagne», con dirección *18-20 Avenue Nelson Mandela* y tel. +221 33 889 65 80 → https://mapcarta.com/fr/W901800372 · dirección oficial: https://www.exteriores.gob.es/Embajadas/dakar/es/Embajada/Paginas/Contacto.aspx |
| log-1 | Consulado General de España en Dakar | 14.7032, -17.4702 | **14.70041, -17.47550** | 0,65 km | OSM node 11200657138 «Consulat général d'Espagne», con tel. +221 33 869 07 07 y `cog.dakar@maec.es` (idénticos a los de la ficha) → https://mapcarta.com/fr/N11200657138 · dirección oficial *Corniche Ouest, Fann-Mermoz, Villa nº 7, B.P. 25908*: https://www.exteriores.gob.es/Embajadas/dakar/es/Embajada/Paginas/Contacto.aspx |
| log-4 | Centre Hospitalier Régional de Tambacounda | 13.75328, -13.67261 | **13.77345, -13.66970** | 2,26 km | DIMO Santé, *Hôpital régional de Tambacounda*, Av. Léopold Senghor, GPS 13.773447 / -13.669700 y **los mismos dos teléfonos que ya figuraban en la ficha** (+221 33 981 10 28 / 33 981 12 18) → https://dimomed.com/structure-de-sante/hopital-regional-de-tambacounda/ |
| log-5 | Centre Hospitalier Régional Amath Dansokho — Kédougou | 12.552, -12.185 | **12.53777, -12.15100** | 4,02 km | DIMO Santé, *Centre Hospitalier Régional Amath Dansokho de Kédougou (CHRADK)*, GPS 12.537770 / -12.151000 → https://dimomed.com/structure-de-sante/centre-hospitalier-regional-amath-dansokho-de-kedougou/ |
| poi-12 | Parque Nacional de Niokolo-Koba | 13.009999, -12.94482 | **13.25937, -13.20216** | 39,31 km | OSM node 4922208208 «Poste de Garde Dar Salam» → https://mapcarta.com/N4922208208 (aldea Dar Salam: https://mapcarta.com/16851890). Confirmado como entrada principal: «L'entrée principale du parc est située à Dar Salam», ~80 km al sur de Tambacounda → https://www.bouger-voyager.com/visiter-parc-national-niokolo-koba/ (la distancia real Dar Salam–Tambacounda es de 76 km en línea recta, coherente) |
| poi-20 | Enclos de Katané | 15.47, -14.1 | **15.48793, -14.11326** | 2,45 km | OSM node «Poste de sante Katane», localidad de Katané (ya presente en `senegal_ref.json` como candidato a 2,4 km). Confirmación documental de que el enclos está «à 30 km au nord de Ranérou» → https://laviesenegalaise.com/reserve-de-faune-du-ferlo-lenclos-de-katane-un-paradis-au-coeur-de-ranerou/ y https://www.seneplus.com/societe/lenclos-de-katane-un-paradis-au-coeur-de-ranerou (Katané está a 26,6 km de Ranérou: coherente) |

### Nota sobre los dos puntos consulares de Dakar

La ficha tenía razón al separarlos: **son dos edificios distintos**, confirmado en la página oficial de contacto de la Embajada:

- **Embajada de España**: 18-20, Av. Nelson Mandela, BP 2091 (Plateau) · +221 33 889 65 80 / 33 821 30 81 · emb.dakar@maec.es
- **Consulado General de España**: Corniche Ouest, Fann-Mermoz, Villa nº 7, B.P. 25908 · +221 33 869 07 07 · cog.dakar@maec.es

El punto de la app para el Consulado (14.7032, -17.4702) caía 650 m tierra adentro respecto del edificio; el nodo OSM `N11200657138` lleva el teléfono y el correo oficiales del Consulado, así que la identificación es segura. El «Embassy of Spain» que el evaluador ofrecía como candidato a 5,8 km es la Embajada (log-0), no el Consulado.

---

## (b) PDIs eliminados

**Ninguno.** No se ha encontrado ningún PDI que no exista o que mezcle dos lugares. Los dos `SIN_REF` (poi-8 y poi-23) se resuelven así:

- **poi-8 · Museo de las Civilizaciones Negras — EXISTE y la coordenada es correcta.** Inaugurado el 6 de diciembre de 2018, financiado por China (~30 M$), edificio circular inspirado en las *cases à impluvium* de Casamance, ~18.000 piezas, 13.785 m². Coordenadas del artículo de Wikipedia: 14°40′39″N 17°26′06″W = **14.67751, -17.4351**, a **25 metros** del punto de la app (14.677288, -17.435131). No se toca. La ausencia en OSM/Wikidata del índice Photon es un vacío del índice, no del museo.
  Fuentes: https://en.wikipedia.org/wiki/Museum_of_Black_Civilisations · https://fr.wikipedia.org/wiki/Mus%C3%A9e_des_civilisations_noires
- **poi-23 · Pista 4x4 Ranérou–Tambacounda — NO VERIFICADO** (ver apartado c).

---

## (c) Puntos NO VERIFICADOS

### poi-23 · «Pista 4x4 Ranérou–Tambacounda — travesía del Ferlo» → NO VERIFICADO

Qué se probó: búsquedas de un itinerario continuo Ranérou→Tambacounda, la fuente citada en el propio PDI (relato Kap2Cap), prensa local sobre infraestructuras de Ranérou y wikis de los departamentos de Koungheul y Koumpentoum.

Lo que sí está documentado contradice parcialmente el texto del PDI: el departamento de Ranérou está **enclavado**; solo dispone de la RN3 (que lo cruza en más de 150 km), de una pista laterítica hacia Vélingara Ferlo y de la pista Younouféré–Nakara–Louguéré Thiolly *en construcción*; el propio prefecto declaraba que solo **cuando se construya** el tramo Vélingara Ferlo–Thionokh (junto a Koungheul) «los usuarios podrán desplazarse fácilmente a Tambacounda». Es decir: en la fecha de esa fuente **no existía una conexión directa cómoda Ranérou–Tambacounda**.
Fuente: https://www.tambacounda.info/2017/09/21/manque-dinfrastructures-de-base-de-reseaux-routiers-a-ranerou-lenclavement-freine-developpement-potentialites/

Distancia real en línea recta Ranérou–Tambacounda: **172 km** (los «unos 230 km» del texto son plausibles para un trazado por pista, pero no verificados).

Acción: coordenada conservada (14.35, -13.8) pero **marcada como punto indicativo**, texto suavizado y añadida la alternativa asfaltada. No se elimina: el corredor existe como concepto y la decisión de hacerlo o no es del propietario. **Con dos vehículos y un perro, mi recomendación es no comprometerse a esta travesía sin una traza GPX contrastada y reciente.**

### poi-19 · «Reserva de Fauna del Ferlo Norte» — sin punto navegable verificado

La coordenada actual (15.5452, -14.01075) **no es un invento**: coincide exactamente con las coordenadas del artículo de Wikipedia en inglés (15°32′43″N 14°00′39″W = 15.54528, -14.01083) → https://en.wikipedia.org/wiki/Ferlo_Nord_Wildlife_Reserve. Es el punto de referencia del área, en pleno Ferlo y sin acceso directo.

No he encontrado ninguna puerta, oficina ni aparcamiento de la reserva en fuentes abiertas: **la Réserve de faune du Ferlo Nord no tiene infraestructura de visita**. La única infraestructura verificable dentro del área es Katané (poi-20). Para no duplicar el pin con poi-20 he **conservado la coordenada** y he explicitado en la descripción que es una referencia de área y que el acceso real es la pista Ranérou → Katané (≈30 km). Queda anotado como excepción consciente a la regla de «punto navegable».

### poi-22 · «Reserva de Fauna del Ferlo Sur» — sin punto navegable verificado

Igual que la anterior, sin puerta ni oficina localizables. Datos confirmados: 6.337 km², creada en 1972, limita al norte con Ferlo Norte; referencia de Wikipedia 14°50′00″N 14°00′00″W y referencia OSM 14.84163, -13.92164 (https://en.wikipedia.org/wiki/Ferlo_Sud_Wildlife_Reserve · https://mapcarta.com/16849458). El punto de la app (14.9167, -13.9167) está 8,4 km al NE de la referencia OSM, dentro del área en cualquier caso. **Coordenada conservada** y descripción anotada: acceso NO VERIFICADO, a resolver en Ranérou con el conservador.

**¿Son redundantes poi-19 y poi-22?** Como entidades administrativas, **no**: son dos reservas distintas creadas por el mismo decreto de 1972, contiguas pero separadas (Ferlo Norte 4.870–6.000 km² al norte, Ferlo Sur 6.337 km² al sur). Como PDIs de un viaje overland, **sí lo son en la práctica**: mismo bioma (estepa saheliana con acacias), misma ausencia de infraestructura, mismo acceso desde Ranérou y ninguna de las dos con fauna visible garantizada fuera del enclos de Katané. Ver apartado (e).

### log-8 · «Paso Boundou Fourdou–Sambaïlo» — el nombre era engañoso

Hallazgos:

1. **El puesto senegalés real de salida hacia Guinea es Kalifourou** (log-7), y su coordenada es exacta: el nodo OSM «Poste Frontalier» está en **12.924151, -13.638479**, a 4 metros del punto de la app. Kalifourou está en la región de **Kolda** (no Tambacounda) y tiene además Gendarmerie y Poste de Garde. → https://mapcarta.com/16847570 · https://mapcarta.com/N6050972389
2. **El «PCJ de Boundou Fourdou» existe pero es otra cosa**: es un *poste de contrôle juxtaposé* de la UEMOA/BAD construido **a caballo sobre la frontera** (15 ha: 10 del lado guineano, 5 del senegalés; dos edificios separados unos 50 m que albergan aduanas y policía de los dos países; 3.400 M FCFA). Llaves entregadas el **17 de diciembre de 2019**. → https://24heureinfo.com/a-la-une/trafic-sur-le-corridor-dakar-conakry-remise-des-postes-de-controle-juxtaposes-de-boundou-fourdou/ · https://tambaactu1.com/les-cles-des-postes-de-controle-juxtaposes-de-boundou-fourdou-sont-remises-aux-autorites-senegalaise-et-guineenne/
3. **Pero no está operativo**, o no lo estaba en la última fuente localizada: en el encuentro de la UEMOA en Tambacounda (abril de 2023) se describía «un site réalisé dans les règles de l'art sur 15 hectares, avec des infrastructures opérationnelles» pero con «une **absence totale de vie administrative**». → https://echoriental.com/tamba-operationnalisation-des-postes-de-controle-juxtaposes-de-boundou-fourdou-des-acteurs-en-conclave/
4. **El punto de la app (12.58241, -13.37191) es el pueblo guineano de Sambaïlo**, a 0,6 km de la coordenada de Wikidata (Q7408982) — no es un puesto fronterizo, sino la primera localidad guineana del corredor, con su aerodromo. La ruta usual descrita por viajeros es «Manda–Kalifourou → Sambaïlo–Koundara, route bitumée en bon état». → https://www.foutadecouverte.com/2017/01/pour-entrer-en-guinee-infos-aux-frontieres.html
5. La aldea «Boundou Fourdou» que OSM sitúa en 12.66783, -13.55848 está catalogada en la **prefectura de Koundara (Guinea)**, a 22 km del punto de la app y a ~30 km de Kalifourou. **No he podido confirmar que ese nodo sea el PCJ**, así que no lo uso como coordenada.

Acción: **coordenada conservada** (es Sambaïlo y Sambaïlo es un waypoint útil y verificado), **nombre corregido** para dejar de llamar «paso Boundou Fourdou» a lo que es el pueblo de Sambaïlo, e `info` reescrita con los tres datos operativos. No se elimina (los puntos logísticos no se eliminan).

### log-10 · «Paso Keur Ayib–Farafenni» — el punto SÍ es el corredor fronterizo

Comprobado: el punto de la app (13.59335, -15.60578) **no es el centro del pueblo**. Está a **272 m al sur** del centro de Keur Ayip Guèye (nodo OSM 3720434196, 13.59579 / -15.60563) y a **326 m al norte** de las oficinas gambianas del paso, que OSM tiene cartografiadas junto a la aldea de Kerr Ali:

- Custom office (Gambia): **13.590437, -15.605408** → https://mapcarta.com/N10787904493
- Immigration (Gambia): **13.590251, -15.605437** → https://mapcarta.com/N10788030823
- Public Health Office POE: nodo 10787732408 · Kerr Ali (aldea gambiana): 13.58928, -15.60693

Es decir, el punto cae exactamente entre el pueblo senegalés y el control gambiano: **es la zona de trámites, correcta como waypoint**. Coordenada conservada. Referencia: https://mapcarta.com/N3720434196

Sí había un **error de hecho en el texto**, corregido (ver apartado d).

---

## (d) Correcciones de texto

| id | qué decía | qué dice ahora | por qué |
|---|---|---|---|
| log-10 | «junto al puente de Senegambia» | «a una decena de kilómetros al norte del puente de Senegambia (Farafenni–Soma)» + coordenadas del control gambiano | El puente está en el eje Farafenni–Soma, ~13 km al sur del paso de Keur Ayib. Son dos puntos distintos. Wikidata Trans-Gambia Highway: 13.51639, -15.57083 |
| log-8 | «Paso fronterizo Boundou Fourdou–Sambaïlo — entrada en Guinea» / «posición operativa a confirmar» | Renombrado a «Sambaïlo (Koundara) — primeros controles guineanos» + explicación del PCJ de Boundou Fourdou y su estado | Ver apartado (c). El nombre atribuía a la coordenada un puesto que está en otro sitio |
| log-1 | solo teléfonos | + dirección oficial «Corniche Ouest, Fann-Mermoz, Villa nº 7 (B.P. 25908)» | Dirección verificada en exteriores.gob.es |
| log-0 | solo teléfonos | + dirección oficial «18-20 Av. Nelson Mandela (Plateau)» | Ídem |
| log-4 | solo teléfonos | + «Av. Léopold Sédar Senghor» | Dirección de DIMO Santé, coherente con los teléfonos ya presentes |
| log-5 | «coordenada urbana aproximada» | + «único hospital de la región de Kédougou, urgencias 24 h y unidad de diálisis; coordenada de DIMO Santé (fuente única)» | Datos verificados; se mantiene la advertencia de fuente única |
| poi-12 | — | + frase de acceso: entrada de Dar Salam sobre la RN7 (~80 km al sur de Tambacounda) y campamento/sede de Simenti (13.02636, -13.29349) 40 km dentro | El PDI ahora apunta a la puerta; el texto explica dónde está el interior navegable |
| poi-19 | «Enlace: …» | + «Coordenada: punto de referencia del área (no accesible por pista). Acceso real: Ranérou → Katané, ~30 km de pista al norte» | Transparencia sobre qué es la coordenada |
| poi-20 | «Coordenada: aproximada, a unos 30 km al norte de Ranérou» | «Coordenada: aldea de Katané (OSM), a 26,6 km al noroeste de Ranérou; el enclos está contiguo» | Coordenada ahora verificada; la distancia «30 km al norte» de la prensa se afina |
| poi-22 | «Enlace: …» | + «Coordenada: referencia del área; NO VERIFICADO ningún punto de acceso o puerta» | Honestidad sobre el dato |
| poi-23 | «Travesía overland de unos 230 km…» / «Estado: referencia de planificación» | Texto suavizado: «NO VERIFICADO», 172 km en línea recta, mención al enclavamiento documentado y a la alternativa asfaltada por la RN3 | Ver apartado (c) |

Datos **comprobados y correctos** que se dejan tal cual: Niokolo-Koba atravesado por el río Gambia y Patrimonio de la Humanidad (inscrito en 1981, 9.130 km²); Saint-Louis, Gorée y País Bassari como UNESCO; el enclos de Katané con oryx algazelle (>300 ejemplares descendientes de 18 introducidos en 2003), gacelas dorcas y dama mhorr y tortugas sulcata, gestionado por la Direction des Parcs nationaux con apoyo de la **Cooperación Española** (dato que, por cierto, es un buen argumento para pedir el permiso); Ferlo Norte con más de 180 especies de aves registradas.

---

## (e) Interés: PDIs flojos y sugerencias

### PDIs que considero flojos o repetitivos (no se ha tocado `prio`)

1. **poi-19 (Ferlo Norte) + poi-20 (Katané) + poi-22 (Ferlo Sur) + poi-21 (Ranérou) = cuatro pines para un solo destino.** El bloque del Ferlo tiene un único contenido real: ir a Katané a ver los oryx, con base en Ranérou. Ferlo Sur no aporta nada distinto (mismo paisaje, sin acceso, sin fauna concentrada) y Ferlo Norte sin Katané es estepa sin puerta. **Sugerencia: fusionar poi-19 en poi-20** (o degradar poi-19 y poi-22 a contexto dentro de la ficha) y dejar Ranérou + Katané como los dos pines operativos. Los cuatro están en «Opcional», así que el coste de mantenerlos es bajo, pero ensucian el mapa.
2. **poi-22 (Ferlo Sur)** es, de todo el país, el único PDI que no sé cómo se visita. Si el propietario no consigue en Ranérou una pista concreta, yo lo quitaría del mapa.
3. **poi-23 (pista Ranérou–Tambacounda)** es el punto de mayor riesgo operativo de la ficha: pista larga, sin servicios, sin traza verificada, con dos vehículos y un perro a bordo y calor saheliano. Mantener solo como opción condicionada a GPX reciente.
4. **poi-18 (Museo Théodore Monod) frente a poi-8 (Civilizaciones Negras)**: no son redundantes (IFAN es etnográfico e histórico; el MCN es un museo-continente nuevo), pero con perro los dos implican cuidador o turnos. Si hay que sacrificar uno, el Théodore Monod es el prescindible.
5. **poi-9 (Monumento del Renacimiento)**: parada corta y de valor discutible, pero es el mejor mirador libre sobre Dakar y está bien colocado como relleno de la Corniche. Se mantiene.

### Hasta tres PDIs de gran interés que faltan (coordenadas verificadas, para que decida el propietario)

1. **Campamento/sede de Simenti, Parque Nacional de Niokolo-Koba — 13.02636, -13.29349.** Es el corazón visitable del parque: hotel junto al río Gambia, *mare de Simenti* con hipopótamos y cocodrilos, dos miradores sobre la charca, poste de garde (13.026206, -13.294358) y aerodromo. Convierte Niokolo-Koba de «parque que se atraviesa» en «parque donde se duerme». Fuentes: https://mapcarta.com/fr/N739391135 (hotel) · https://mapcarta.com/fr/N5444921763 (poste de garde) · https://mapcarta.com/fr/16836768 (aerodromo)
2. **Campement Hôtel de Wassadou — nodo OSM 2594256233, en el río Gambia al norte del parque** → https://mapcarta.com/N2594256233. Es el alojamiento clásico con aparcamiento y ribera para quien no puede entrar en el parque; **encaja exactamente con el problema del perro** (base fuera del área protegida mientras dos viajeros entran por turnos). Habría que leer sus coordenadas exactas de esa ficha antes de añadirlo.
3. **Puente de Senegambia (Farafenni–Soma)** ya está en la ficha de Gambia, pero **no en la de Senegal**, y es la pieza que hace viable el corredor de subida. Merece al menos una mención cruzada en `logistics` de Senegal junto a log-10.

---

## (f) Fuentes abiertas que fallaron

- **Photon** (`photon.komoot.io`), **Nominatim** (`nominatim.openstreetmap.org`) y **Overpass** (`overpass-api.de`, `overpass.kumi.systems`): todas rechazadas por el proxy del contenedor con `CONNECT tunnel failed, response 403` o `robots.txt disallowed` / timeout. Sustituidas por mapcarta.com, que expone los mismos nodos OSM con su id.
- `www.openstreetmap.org/node/<id>`: bloqueado por robots.txt vía WebFetch.
- `www.exteriores.gob.es/Consulados/dakar/...`: *Read timeout* y 404 en varias rutas. Resuelto con la página de contacto de la Embajada, que lista **todas** las representaciones españolas en Senegal.
- `chr-kedougou.com` (web oficial del hospital de Kédougou): el robots.txt no resuelve DNS desde aquí (`Name or service not known`). El nombre y la existencia del hospital quedan confirmados por el Ministerio de Sanidad senegalés y la Primatura; la coordenada viene de DIMO Santé y es **fuente única**.
- `consejeria.mites.gob.es`: certificado TLS rechazado.
- `ebird.org`: bloqueo antibot (Anubis).
- `vfmatch.org`, `uemoa.int`, `museedescivilisationsnoires.org`: contenido no renderizado / robots.txt inaccesible.
- `es.wikipedia.org`: «This domain is cache-only and cannot be fetched» en esta sesión; se usaron las versiones **en** y **fr**.

---

## Anexo · coordenadas verificadas usadas o comprobadas en esta auditoría

| lugar | lat | lon | fuente |
|---|---|---|---|
| Ambassade d'Espagne, Dakar (OSM W901800372) | 14.662917 | -17.436214 | mapcarta |
| Consulat général d'Espagne, Dakar (OSM N11200657138) | 14.700413 | -17.475504 | mapcarta |
| Hôpital régional de Tambacounda | 13.773447 | -13.669700 | DIMO Santé |
| Centre de santé de Tambacounda (OSM W422397104) | 13.778852 | -13.673656 | mapcarta (control cruzado, 0,7 km del anterior) |
| CHR Amath Dansokho, Kédougou | 12.537770 | -12.151000 | DIMO Santé |
| Poste Frontalier de Kalifourou (OSM N6050972389) | 12.924151 | -13.638479 | mapcarta |
| Kalifourou (aldea) | 12.92793 | -13.64196 | mapcarta |
| Sambaïlo, Guinea (Wikidata Q7408982) | 12.58333 | -13.36667 | senegal_ref.json |
| Custom office, paso de Keur Ayib (lado gambiano) | 13.590437 | -15.605408 | mapcarta |
| Immigration, paso de Keur Ayib (lado gambiano) | 13.590251 | -15.605437 | mapcarta |
| Keur Ayip Guèye (aldea senegalesa) | 13.59579 | -15.60563 | mapcarta |
| Poste de Garde Dar Salam (entrada Niokolo-Koba) | 13.259369 | -13.202159 | mapcarta |
| Hôtel de Simenti | 13.026359 | -13.293490 | mapcarta |
| Poste de Garde de Simenti | 13.026206 | -13.294358 | mapcarta |
| Aérodrome de Simenti | 13.046871 | -13.295220 | mapcarta |
| Poste de garde de Niokolo-Koba | 13.07452 | -12.72192 | mapcarta |
| Katané (poste de santé, acceso al enclos) | 15.48793 | -14.11326 | senegal_ref.json (OSM) |
| Museo de las Civilizaciones Negras | 14.67751 | -17.4351 | en.wikipedia |
| Réserve de faune du Ferlo Nord (referencia) | 15.54528 | -14.01083 | en.wikipedia |
| Réserve de faune du Ferlo Sud (referencia OSM) | 14.84163 | -13.92164 | senegal_ref.json / mapcarta |

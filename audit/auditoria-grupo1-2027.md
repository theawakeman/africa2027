# Auditoría del grupo 1 · Marruecos, Sáhara Occidental, Mauritania, Senegal y Gambia

Fecha: 13 de septiembre de 2026 · commit `482e857` · 149 puntos revisados, 46 recolocados, ninguno eliminado

Este bloque cubre dos encargos: verificar que las coordenadas de los puntos de interés y de los puntos logísticos caen donde de verdad está el sitio, y ampliar la ficha extendida de historia de cada país con política, economía, sociedad y fuentes nuevas. Los informes completos, con una URL por cada corrección, están en `audit/geo/<país>_cambios.md` y las dudas de los redactores de historia en `audit/historia/NOTAS.md`.

## Cómo se ha verificado

Cada punto se ha consultado contra dos bases independientes: OpenStreetMap (a través del geocodificador Photon) y Wikidata, buscando el nombre en español, en el idioma local y en inglés, y midiendo la distancia entre el candidato y el punto que tenía la app. Un punto concreto (un hospital, un consulado, un paso fronterizo) se considera correcto si la referencia está a menos de 1,5 km; una ciudad, a menos de 4 km; un parque o una zona extensa, a menos de 15 km. Todo lo que salía de esos márgenes, más todo lo que no encontraba referencia, se ha revisado a mano contra Wikipedia, mapcarta (que expone los datos de OSM con el identificador del nodo), las páginas de Exteriores, las fichas del Logistics Cluster de Naciones Unidas y las webs de los propios parques u hospitales. Ninguna coordenada nueva se ha escrito de memoria: todas llevan fuente en el informe del país.

## Resultado de la verificación GPS

| País | Puntos | Correctos | Recolocados | Sin confirmar |
|---|---|---|---|---|
| Marruecos | 25 | 13 | 13 | 1 |
| Sáhara Occidental | 30 | 12 | 14 | 3 |
| Mauritania | 30 | 26 | 2 | 2 |
| Senegal | 39 | 33 | 6 | 3 |
| Gambia | 32 | 21 | 11 | 1 |

Tenías razón en la sospecha: uno de cada tres puntos estaba mal situado, y algunos por mucho.

**Los errores graves.** Bir Gandouz, en el Sáhara Occidental, estaba a 68 km del pueblo real, y Lemsid a 29 km; los dos son paradas de repostaje obligadas en el tramo hacia Guerguerat, así que el error era de los que se pagan caro. Cabo Blanco aparecía en Tenerife, por una confusión de nombre del geocodificador. En Gambia estaban desplazados los cuatro pasos fronterizos (entre 3 y 16 km), las dos terminales del ferry Banjul–Barra y el puente de Senegambia. En Marruecos, el arco de Legzira estaba a 11 km del arco, el parque de Khnifiss en mitad de la nada en vez de en el desvío señalizado de la N1, y la embajada y los tres consulados de España estaban todos fuera de sitio. En Senegal, la puerta de Niokolo-Koba estaba a 39 km de la puerta de Dar Salam.

**Lo que no era un error.** Conviene decirlo también: el puesto fronterizo mauritano de Guerguerat, que el sistema marcaba como desplazado, estaba a 21 metros de la oficina real de la policía de fronteras; lo que pasa es que el puesto marroquí es otro, 3,5 km al norte, con unos cuatro kilómetros de tierra de nadie en medio. El paso de Keur Ayib estaba a 270 metros del GPS oficial del puesto. Y el Museo de las Civilizaciones Negras de Dakar, que no aparecía en ninguna base, existe y estaba bien situado.

**Hallazgos que no son de coordenadas.** El hospital Hassan II de Agadir cierra a finales de marzo de 2026 por reconstrucción, así que el punto de referencia pasa a ser el CHU Mohammed VI, que asume urgencias y partos. El cruce del río Allahein en Kartong (Gambia) no admite vehículos: es piragua de pasajeros, con sello de salida gambiano pero sin puesto de entrada senegalés, de modo que la alternativa real a Séléti es Darsilami/Dimbaya. España sí tiene representación propia en Gambia, una Oficina Diplomática en Fajara, aunque la demarcación consular siga siendo de Dakar. El paso que la app llamaba «Boundou Fourdou–Sambaïlo» es en realidad Kalifourou: el puesto yuxtapuesto de Boundou Fourdou se entregó en 2019 y seguía sin actividad administrativa en 2023. Y los tres consulados de España en Mauritania (Nuadibú de carrera, honorarios en Rosso y Chinguetti) existen y están en la lista oficial de la embajada, aunque Exteriores no publique su ubicación física.

**Puntos que quedan marcados como no verificados.** Trece en total, señalados así en los informes y con el texto de la app suavizado para que no afirme lo que no se puede probar: el estado de la carretera del Tizi n'Test tras el terremoto de 2023, el cruce de repostaje de Dajla (el punto cae dentro de la laguna y no he podido fijar el real), la casa del parque de Diawling, el acceso por pista a las reservas del Ferlo norte y sur, la pista 4x4 Ranérou–Tambacounda y el portal exacto de la oficina diplomática de Fajara, entre otros.

**Redundancias detectadas, para que decidas.** En Senegal, Ferlo Norte, Ferlo Sur, Katané y Ranérou son cuatro chinchetas para un solo destino real, que es ver los oryx en Katané con base en Ranérou. En el Sáhara Occidental, Lemsid aparece dos veces con el mismo texto (como PDI y como punto de combustible), y lo mismo pasa con Laayoune Plage; además, nueve de los dieciséis PDIs del territorio comparten la misma fotografía. En Gambia, los Kombos están apelmazados y Bijilo es el más prescindible. No he tocado nada de esto: son decisiones tuyas.

**Altas propuestas**, todas con coordenadas verificadas y fuente en los informes: gargantas del Dadès, Amtoudi y el parque de Souss-Massa en Marruecos; la señal del Trópico de Cáncer, el faro de Villa Cisneros y Lasarka en el Sáhara; Azougui, Choum y la Baie de l'Étoile en Mauritania (esta última con aviso de campo de minas cartografiado); Simenti y el campamento de Wassadou en Senegal, este último pensado precisamente por el problema del perro dentro del parque; Kerr Batch, Bintang Bolong y la playa de Sanyang en Gambia.

## Historia y contexto ampliados

Las cinco fichas extendidas se han reescrito enteras. Cada una tiene ahora siete secciones —orígenes anteriores a la colonización, colonización, independencia y construcción del Estado, historia reciente, política y gobierno en 2026, economía y recursos, y sociedad con idiomas, religión y cultura— con unas 1.750 palabras, que son unos doce minutos de audio. En total 112 fuentes citadas: fichas país del Ministerio de Asuntos Exteriores de 2026, Freedom House 2025 con puntuación y clasificación, Britannica, UNESCO, Banco Mundial y prensa contrastada. La sección de sociedad termina en cada país con dos o tres frases prácticas de costumbres para quien viaja.

La instrucción a los redactores fue explícita: cada dato tenía que salir de una página abierta en esa sesión, y lo que no se pudiera verificar debía quedar fuera o dicho como tal. Por eso los informes incluyen lo que se omitió a propósito.

**Clasificación política según Freedom House 2025**, que es la que da la app ahora: Marruecos parcialmente libre con 37 sobre 100; Sáhara Occidental no libre con 4 sobre 100; Mauritania parcialmente libre con 39; Senegal libre con 69; Gambia parcialmente libre con 50.

**La corrección más importante:** la app daba a Ousmane Sonko como primer ministro de Senegal. Ya no lo es. Fue destituido el 23 de mayo de 2026 y le sustituyó el economista Ahmadou Al Aminou Lo el 25; Sonko preside la Asamblea Nacional desde el 26 y PASTEF se retiró del Gobierno el 1 de junio. La ficha del MAEC de marzo de 2026 está desfasada en ese punto, así que solo se ha usado para jefe de Estado, economía y sociedad. Es exactamente el tipo de error que buscábamos.

**En el Sáhara Occidental** el texto atribuye cada posición a quien la sostiene y no adopta ninguna: qué dice Marruecos, qué reclama el Frente Polisario, cómo clasifica el territorio Naciones Unidas, y qué reconoce y qué no reconoce España desde la carta de Pedro Sánchez de marzo de 2022, frente a Estados Unidos desde diciembre de 2020 y Francia desde 2024. La resolución 2797 del Consejo de Seguridad prorrogó la MINURSO hasta el 31 de octubre de 2026, de modo que esa sección habrá que revisarla cuando se apruebe la resolución de ese mes.

**Fechas que caducan pronto** y conviene revisar antes de salir: las legislativas de Marruecos estaban convocadas para el 23 de septiembre de 2026 y las presidenciales de Gambia para el 5 de diciembre de 2026; el puente de Rosso, entre Mauritania y Senegal, tenía prevista su apertura a mediados de 2026 y ya iba retrasado, y es el dato más directamente útil para ese paso fronterizo.

## Qué queda pendiente

Los grupos 2 a 6 de países, con el mismo método: Guinea–Sierra Leona–Liberia–Costa de Marfil; Ghana–Togo–Benín–Nigeria; Camerún–Gabón–Congo–RDC–Angola; Zambia–Tanzania–Kenia–Uganda–Ruanda–Malaui; y Mozambique–Zimbabue–Botsuana–Sudáfrica–Namibia–Lesoto–Esuatini. Y, como último bloque, la auditoría del agua: puntos concretos de recarga para uso general (lavado y ducha), con coordenadas, en sustitución del texto genérico actual.

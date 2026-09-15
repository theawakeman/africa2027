# Grupo 8 · comprobación manual en Google Maps

Revisión realizada el 15 de septiembre de 2026. Los 36 PDIs se buscaron uno a
uno y se fijaron en el lugar, acceso, centro de visitantes, campamento, mercado,
cumbre o alojamiento que corresponde al texto. La distancia es el
desplazamiento en línea recta respecto al pin anterior.

## Esuatini

| # | PDI / ancla comprobada | Desplazamiento | Coordenadas finales |
|---:|---|---:|---|
| 1 | Lion Cavern | 1,1 km | -26.1925369, 31.0305069 |
| 2 | Ngwenya Glass | 2,5 km | -26.2220580, 31.0311897 |
| 3 | Objeto de acceso de Malolotja | 0,9 km | -26.1411446, 31.1175614 |
| 4 | Malolotja Canopy Tour | 1,6 km | -26.1407413, 31.1351138 |
| 5 | Maguga Dam | 4,6 km | -26.0639588, 31.2483291 |
| 6 | Nsangwini Rock Art | 12,0 km | -26.0693238, 31.2922655 |
| 7 | Phophonyane Falls Ecolodge | 11,0 km | -25.8980625, 31.2930625 |
| 8 | Swazi Plaza, Mbabane | 1,3 km | -26.3265299, 31.1409367 |
| 9 | Sibebe Rock | 2,5 km | -26.2615925, 31.1737208 |
| 10 | Ezulwini Handcraft Market | 2,2 km | -26.4162595, 31.1782678 |
| 11 | Mantenga Nature Reserve and Cultural Village | 2,1 km | -26.4461535, 31.1623541 |
| 12 | Mlilwane Wildlife Sanctuary | 3,5 km | -26.4799870, 31.1944294 |
| 13 | Manzini Main Market | 2,0 km | -26.4990422, 31.3756566 |
| 14 | Mkhaya Meeting Point, Phuzumoya | 6,6 km | -26.6838310, 31.7467220 |
| 15 | Hlane Ndlovu Camp | 1,4 km | -26.2596472, 31.8749574 |
| 16 | Main Camp Shewula Nature Reserve | 9,0 km | -26.1410060, 32.0395970 |

## Lesoto

| # | PDI / ancla comprobada | Desplazamiento | Coordenadas finales |
|---:|---|---:|---|
| 1 | Butha Buthe Mountain | 3,5 km | -28.7690886, 28.2861149 |
| 2 | Maliba Lodge, base dentro de Ts’ehlanyane | 14,3 km | -28.9141875, 28.4364375 |
| 3 | Liphofung Cave Chalets / visitantes | 13,2 km | -28.7529054, 28.4956766 |
| 4 | Moteng Pass | 8,5 km | -28.7558330, 28.6002780 |
| 5 | Afriski Mountain Resort | 0,3 km | -28.8203625, 28.7272528 |
| 6 | Tlaeeng Pass | 10,5 km | -28.9431975, 28.8285369 |
| 7 | Mokhotlong | 1,0 km | -29.2875557, 29.0605389 |
| 8 | Cumbre de Thabana Ntlenyana | 0,2 km | -29.4679580, 29.2690909 |
| 9 | Sani Pass, ancla alta compartida con Sudáfrica | 0,1 km | -29.5879785, 29.2921966 |
| 10 | Sani Mountain Escape | 0,1 km | -29.5846507, 29.2882526 |
| 11 | Katse Dam Information Center | 0,8 km | -29.3440910, 28.5065405 |
| 12 | Bokong Visitors’ Centre | 21,2 km | -29.0714444, 28.4255278 |
| 13 | Mohale Lodge | 2,5 km | -29.4785420, 28.0613873 |
| 14 | Basotho Hat, Maseru | 0,4 km | -29.3130504, 27.4784482 |
| 15 | Thaba Bosiu Cultural Village | 0,9 km | -29.3463224, 27.6638307 |
| 16 | Morija Museum & Archives | 1,2 km | -29.6263228, 27.5088085 |
| 17 | Malealea Lodge | 2,9 km | -29.8280062, 27.5999060 |
| 18 | Maletsunyane Falls | 0,2 km | -29.8701526, 28.0535076 |
| 19 | Masitise Cave House and Museum | 5,5 km | -30.4050444, 27.6432830 |
| 20 | Objeto Sehlabathebe National Park | 1,1 km | -29.9035304, 29.1107486 |

## Decisiones en referencias compuestas

Los ficheros `*_eval.*`, `*_queries.json` y `*_ref.json` conservan una segunda
comprobación independiente con OpenStreetMap/Wikidata. La decisión manual
prevalece cuando el buscador abierto comparó elementos distintos:

- Mkhaya es una excepción deliberada. Big Game Parks advierte en su página
  oficial que Google lleva a una puerta trasera sin personal y publica el punto
  de encuentro correcto en Phuzumoya: 26.683831 S, 31.746722 E. Ese punto
  oficial sustituye tanto al pin anterior como al resultado engañoso de Google.
- Malolotja y Sehlabathebe son áreas, no edificios. Sus nombres y textos no
  prometen que el centro geométrico sea una puerta. En Sehlabathebe se conserva
  el objeto reconocido por Google, pero la ficha obliga a confirmar recepción,
  lodge y pista antes de salir.
- La ficha genérica de Ts’ehlanyane que devolvía Google estaba fuera del parque.
  Se usa Maliba Lodge como base operativa, identificable y navegable dentro de
  la reserva. Mohale se fija igualmente en Mohale Lodge; la presa y el centro de
  información son destinos posteriores que deben concertarse con LHDA.
- Bokong usa la coordenada publicada por Visit Lesotho, convertida desde
  S29°04’17.2 E28°25’31.9. Sani Pass reutiliza exactamente el punto ya comprobado
  en la ficha sudafricana para no crear dos versiones del mismo lugar.

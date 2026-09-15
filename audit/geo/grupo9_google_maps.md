# Grupo 9 · comprobación manual en Google Maps

Revisión realizada el 15 de septiembre de 2026. Los 24 PDIs de Namibia se
buscaron uno a uno y se fijaron en el objeto, acceso, recepción, mirador o
elemento visitable que corresponde al texto. La distancia es el desplazamiento
en línea recta respecto al pin anterior.

| # | PDI / ancla comprobada | Desplazamiento | Coordenadas finales |
|---:|---|---:|---|
| 1 | Fish River Canyon Viewpoint | 0,6 km | -27.5891682, 17.6145749 |
| 2 | Quivertree Forest Rest Camp | 1,7 km | -26.4814114, 18.2375665 |
| 3 | Garub Desert Horses | 7,3 km | -26.5947881, 16.0757057 |
| 4 | Lüderitz Waterfront Development Company | 0,8 km | -26.6477353, 15.1518021 |
| 5 | Kolmanskop Entrance | 0,4 km | -26.7016875, 15.2320625 |
| 6 | Dune 45 | 13,0 km | -24.7277568, 15.4725668 |
| 7 | Deadvlei | 0,0 km | -24.7592732, 15.2923894 |
| 8 | Kuiseb River Viewpoint | 19,2 km | -23.3030703, 15.7736518 |
| 9 | Flamingo Lagoon, Walvis Bay | 2,1 km | -22.9733978, 14.4785799 |
| 10 | Sandwich Harbour | 4,4 km | -23.3571081, 14.4986540 |
| 11 | Jetty Pier, extremo del muelle | 0,8 km | -22.6806338, 14.5191099 |
| 12 | Spitzkoppe Community Restcamp | 1,6 km | -21.8395132, 15.2015866 |
| 13 | Cape Cross Seal Reserve | 0,2 km | -21.7716993, 13.9524077 |
| 14 | Messum Crater | 2,2 km | -21.4112059, 14.2163411 |
| 15 | Panel White Lady, Brandberg | 11,7 km | -21.1106969, 14.6625695 |
| 16 | Twyfelfontein Visitors Centre | 0,1 km | -20.5904535, 14.3720279 |
| 17 | Palmwag Lodge | 1,4 km | -19.8863142, 13.9365328 |
| 18 | Ugab Gate, Skeleton Coast | 109,5 km | -21.1727036, 13.6696429 |
| 19 | Okaukuejo Waterhole | 0,4 km | -19.1809447, 15.9163519 |
| 20 | Van Zyl's Pass | 12,3 km | -17.6333333, 12.7000000 |
| 21 | Epupa Falls Viewpoint | 0,5 km | -17.0018086, 13.2408032 |
| 22 | Viewpoint to Ruacana Falls | 0,5 km | -17.3941201, 14.2194575 |
| 23 | Independence Memorial Museum, Windhoek | 2,4 km | -22.5688266, 17.0879955 |
| 24 | Waterberg Camp, recepción de NWR | 2,2 km | -20.5163693, 17.2452939 |

## Decisiones en referencias compuestas

Los ficheros `namibia_eval.*`, `namibia_queries.json` y `namibia_ref.json`
conservan una segunda comprobación con OpenStreetMap/Photon y Wikidata. La
decisión manual prevalece cuando el buscador abierto devuelve un elemento
distinto o carece del objeto concreto:

- Skeleton Coast deja de usar un centroide situado 109,5 km al norte y se ancla
  en Ugab Gate, la puerta sur que convierte el PDI en una decisión navegable.
- El punto antiguo de Kuiseb mezclaba el mirador de la C14 con Welwitschia
  Drive. Son recorridos distintos; el PDI se fija exclusivamente en Kuiseb River
  Viewpoint y su texto ya no promete la segunda visita.
- White Lady se fija en el panel arqueológico, no en el lodge ni en un supuesto
  aparcamiento. El punto coincide con Google Maps y con las coordenadas
  publicadas del panel; la ficha explica que se llega a pie desde la entrada.
- Dune 45 y Van Zyl's Pass corrigen desplazamientos de más de 12 km. Photon no
  encuentra Dune 45 y propone por similitud Dune 40; ese falso positivo no se
  utiliza para mover el pin comprobado en Google.
- Twyfelfontein, Palmwag, Waterberg, Spitzkoppe y Kolmanskop quedan en centros de
  visitantes, recepciones o entradas reconocibles, no en centroides de áreas.

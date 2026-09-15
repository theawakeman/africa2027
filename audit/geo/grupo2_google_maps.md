# Grupo 2 · comprobación final de pines y anclas

Revisión cerrada el 15 de septiembre de 2026. Esta pasada complementa los
informes detallados `*_cambios.md`, `*_eval.*` y `*_ref.json` de cada país. Cada
coordenada se contrastó con el objeto real de Google Maps y, cuando no existe
una ficha inequívoca, con cartografía abierta y fuentes del gestor. La excepción
queda declarada en la ficha en vez de sustituirse por un negocio de nombre
parecido.

## Correcciones de mayor entidad

La distancia es el movimiento respecto al contenido publicado al empezar esta
pasada. La tabla recoge desplazamientos próximos o superiores a 3 km y el caso
especial de Islas Banana; los restantes puntos también se comprobaron y constan
en los informes de cada país.

| País | PDI / ancla comprobada | Desplazamiento | Coordenadas finales |
|---|---|---:|---|
| Guinea | Voile de la Mariée | 10,1 km | 9.9816544, -12.7938486 |
| Guinea | Islas de Los | 5,7 km | 9.4769000, -13.7855000 |
| Guinea | Monte Nimba | 4,9 km | 7.6378125, -8.4184375 |
| Sierra Leona | Tacugama Chimpanzee Sanctuary | 3,0 km | 8.4169179, -13.2072019 |
| Sierra Leona | Bureh Beach | 6,6 km | 8.2113922, -13.1554723 |
| Sierra Leona | Islas Banana | 0,6 km | 8.1158998, -13.2115287 |
| Sierra Leona | Gola Rainforest National Park | 20,4 km | 7.6663373, -10.8415290 |
| Liberia | Sapo National Park | 40,4 km | 5.4603195, -8.4403573 |
| Liberia | East Nimba Nature Reserve / Yekepa | 7,3 km | 7.5558497, -8.4732243 |
| Costa de Marfil | Monte Nimba | 6,4 km | 7.5819758, -8.4183833 |
| Costa de Marfil | Parc national de Taï, sector operativo | 45,9 km | 5.6900000, -6.9394444 |
| Costa de Marfil | Assinie | 3,6 km | 5.1398055, -3.3237824 |
| Costa de Marfil | Mezquita de Sorobango | 17,9 km | 8.1737936, -2.7089936 |

## Excepciones documentadas

- Mount Loura aparece desplazado en la ficha nominal de Google Maps. Se mantiene
  el pico cartográfico auditado y el texto advierte de que no debe usarse el
  resultado automático como acceso.
- Kambadaga, Dent de Man y el puente de lianas de Lieupleu no tienen una ficha
  inequívoca del accidente concreto en Google Maps. Se usan los objetos
  cartográficos auditados y los enlaces de Maps se plantean como búsqueda o
  referencia, no como una puerta inventada.
- En Islas Banana la ficha real de Google Maps corresponde al archipiélago; el
  embarque por Kent se explica por separado. Bintumani es una cumbre, no un
  inicio de sendero, y Outamba exige confirmar el acceso operativo.
- Gola es una referencia de área; Providence Island conserva el ancla real de la
  isla; Sapo y Taï usan un sector operativo y no prometen una entrada libre.
  East Nimba se desplazó al entorno real de reserva/acceso de Yekepa.
- En Comoé el pin corresponde a la referencia meridional de Kakpin, no al
  centroide del parque. La ficha mantiene acceso y seguridad como condicionales.

La validación generada confirma 42/42 objetos sincronizados entre JSON fuente,
tarjetas, mapa de país y mapa general.

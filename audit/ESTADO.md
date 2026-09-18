# Estado de la auditoría integral

Última actualización: 18 de septiembre de 2026.

Este archivo separa las capas de revisión para que «país revisado» no oculte
trabajo pendiente. Un grupo solo se considera cerrado cuando su commit está en
`origin/main`.

| Grupo | Países | Historia | GPS/PDIs | Profundidad PDI | Enlaces concretos | Fotografías exactas/galerías | Agua de servicio |
|---|---|---|---|---|---|---|---|
| 1 | Marruecos, Sáhara Occidental, Mauritania, Senegal, Gambia | Cerrado | Cerrado: 74/74 | Cerrado: 74/74 | Cerrado: 74/74 | Cerrado: 74/74 con galería; 222 fotos | Cerrado: 15 puntos exactos; 5 genéricos retirados |
| 2 | Guinea, Sierra Leona, Liberia, Costa de Marfil | Cerrado | Cerrado: 42/42 | Cerrado: 42/42 | Cerrado: 42/42 | Cerrado: 42/42 con galería; 126 fotos | Cerrado: 10 puntos exactos; 7 genéricos retirados |
| 3 | Ghana, Togo, Benín, Nigeria | Cerrado | Cerrado: 60/60 | Cerrado: 60/60 | Cerrado: 60/60 | Cerrado: 60/60 con galería; 180 fotos | Cerrado: 14 puntos exactos; 8 genéricos retirados |
| 4 | Camerún, Gabón, Congo, RD Congo, Angola | Cerrado | Cerrado | Cerrado: 93/93 | Cerrado: 93/93 | Cerrado: 93/93 con foto y enlace; 90 galerías | Cerrado: 11 puntos exactos; 4 pines genéricos retirados |
| 5 | Zambia, Tanzania, Kenia, Mozambique | Cerrado | Cerrado: 75/75 | Cerrado: 75/75 | Cerrado: 75/75 | Cerrado: 75/75 con foto; 74 galerías | Cerrado: 9 puntos exactos; 8 genéricos retirados |
| 6 | Uganda, Ruanda, Malaui | Cerrado | Cerrado: 60/60 | Cerrado: 60/60 | Cerrado: 60/60 | Cerrado: 60/60 con foto; 58 galerías | Cerrado: 7 puntos exactos; 4 genéricos retirados |
| 7 | Zimbabue, Botsuana, Sudáfrica | Cerrado | Cerrado: 69/69 | Cerrado: 69/69 | Cerrado: 69/69 | Cerrado: 69/69 con foto; 44 galerías | Cerrado: 10 puntos exactos; 6 genéricos retirados |
| 8 | Esuatini, Lesoto | Cerrado | Cerrado: 36/36 | Cerrado: 36/36 | Cerrado: 36/36 | Cerrado: 36/36 con foto; 36 galerías | Cerrado: 5 puntos exactos; 2 genéricos retirados |
| 9 | Namibia | Cerrado | Cerrado: 24/24 | Cerrado: 24/24 | Cerrado: 24/24 | Cerrado: 24/24 con galería; 72 fotos | Cerrado: 6 puntos exactos; 2 genéricos retirados |
| 10 (piloto) | Túnez | Hecho, por validar | Hecho: 20/20 en Google Maps | Hecho: 20/20 | Hecho: 20/20 | Hecho: 20/20 con galería; 60 fotos | No auditada (solo campings documentados) |
| 10 | Madagascar | Hecho, por validar | Hecho: 20/20 en Google Maps | Hecho: 20/20 | Hecho: 20/20 | Hecho: 20/20 con galería; 60 fotos | No auditada (supermercados y hotel documentados) |
| 10 | Mali | Hecho, por validar | Hecho: 17/18 en Google Maps (Boucle du Baoulé sin objeto) | Hecho: 18/18 | Hecho: 18/18 | Hecho: 18/18 con foto; 17 galerías; 49 fotos | No auditada (Sleeping Camel documentado) |
| 10 | Guinea-Bisáu | Hecho, por validar | Hecho: 17/17 en Google Maps | Hecho: 17/17 | Hecho: 17/17 | Hecho: 17/17 con foto; 15 galerías; 45 fotos (3 PDIs sin foto del lugar exacto) | No auditada (hoteles de Bissau) |
| 10 | Sudán | Hecho, por validar | Hecho: 18/18 en Google Maps | Hecho: 18/18 | Hecho: 18/18 | Hecho: 18/18 con galería; 52 fotos | No auditada (Wadi Halfa documentado) |

## Países fuera del itinerario (grupos «Alternativas», «Avión», «Excluidos», «Fuera de ruta»)

Túnez es el piloto del formato para los 23 países sin ficha completa o con
ficha corta. Método: 15–20 PDIs por país (decisión del propietario, 18-09-2026)
con pin comprobado en Google Maps, galería de Commons con autor y licencia,
ficha de decisión y enlaces concretos; historia de siete secciones con fuentes;
cabecera uniforme (entradas en `data_cabeceras`, `data_visados` y `data_cpd`).
Alta en el CMS con `tools/gen/exporta_contenido.py <slug>`. Cada ficha alimenta
además el bloque del perro (`data_perro_contactos`, dosier §2.4 y §3.x).
Hechos (19-09-2026): Túnez (piloto validado), Madagascar, Mali, Guinea-Bisáu y
Sudán — expedientes en [`audit/pdi/tunez.md`](pdi/tunez.md),
[`madagascar.md`](pdi/madagascar.md), [`mali.md`](pdi/mali.md),
[`guinea-bisau.md`](pdi/guinea-bisau.md) y [`sudan.md`](pdi/sudan.md).
Pendientes: Egipto, Etiopía y Yibuti (ampliar) y Argelia, Libia, Burkina Faso,
Níger, Chad, RCA, Sudán del Sur, Somalia, Eritrea, Guinea Ecuatorial, Santo
Tomé, Cabo Verde, Comoras, Seychelles, Mauricio y Burundi (nuevos).

## Línea de corte de la nueva pasada PDI

La auditoría de profundidad editorial, enlaces útiles y fotografías múltiples
empezó en el **grupo 4** y ya se ha aplicado de forma retroactiva a los
**grupos 1–3**. La pasada ampliada queda así cerrada para los nueve grupos.

El detalle cuantitativo está en [`audit/pdi/grupo1.md`](pdi/grupo1.md),
[`audit/pdi/grupo2.md`](pdi/grupo2.md), [`audit/pdi/grupo3.md`](pdi/grupo3.md),
[`audit/pdi/grupo4.md`](pdi/grupo4.md),
[`audit/pdi/grupo5.md`](pdi/grupo5.md), [`audit/pdi/grupo6.md`](pdi/grupo6.md),
[`audit/pdi/grupo7.md`](pdi/grupo7.md), [`audit/pdi/grupo8.md`](pdi/grupo8.md) y
[`audit/pdi/grupo9.md`](pdi/grupo9.md). Los grupos 1–9 ya cumplen el nuevo
estándar en el contenido fuente. El corredor Congo–RD Congo también ha quedado
rehecho por Cabinda; la fase activa es la auditoría de agua de servicio por grupos.

## Criterio de cierre por PDI

- La descripción permite decidir si merece el tiempo y el desvío: singularidad,
  experiencia real, acceso, duración, mejor momento y motivo para descartarlo.
- Los datos cambiantes quedan como «por confirmar» y no como hechos permanentes.
- Los enlaces apuntan al lugar u organismo concreto, no a una portada genérica.
- Cada PDI tiene al menos una foto pertinente. La imagen identifica el enclave
  exacto o su contexto inmediato declarado; una imagen ajena no se presenta como
  si fuera el lugar.
- Cuando existan archivos verificables, la ficha muestra una galería de varias
  vistas con autor, licencia y página de origen trazables.
- El pin abre el objeto real en Google Maps o documenta expresamente que es un
  área/entrada aproximada.

## Cambios globales

- Mapa general: cerrado. Solo los corredores de bajada y subida y los PDIs están
  conectados de inicio; ramales, fronteras y servicios quedan apagados.
- Tarjeta, globo del mapa y ficha ampliada usan el mismo objeto fuente: el globo
  repite el resumen corto y la portada representativa de la tarjeta; «Ver ficha
  ampliada» abre el modal sobre el mapa y al cerrarlo conserva centro, zoom y
  capas. La validación global confirma esa sincronía en todos los PDIs que ya
  tienen fotografía. En el grupo 8 los 36 PDIs comparten fuente, resumen y
  portada entre tarjeta, globo y modal, y todos disponen de galería.
- Agua para lavar/ducharse en el vehículo: grupos 1–9 cerrados con 87 puntos
  físicos, condiciones de acceso y descartes explícitos; expedientes en
  [`audit/agua/grupo1.md`](agua/grupo1.md) y
  [`audit/agua/grupo2.md`](agua/grupo2.md) y
  [`audit/agua/grupo3.md`](agua/grupo3.md),
  [`audit/agua/grupo4.md`](agua/grupo4.md),
  [`audit/agua/grupo5.md`](agua/grupo5.md),
  [`audit/agua/grupo6.md`](agua/grupo6.md) y
  [`audit/agua/grupo7.md`](agua/grupo7.md) y
  [`audit/agua/grupo8.md`](agua/grupo8.md) y
  [`audit/agua/grupo9.md`](agua/grupo9.md). Auditoría cerrada para los nueve
  grupos. No se da por
  válido un grifo genérico ni una instalación con duchas sin acceso documentado.
- Corredor Congo–RD Congo: cerrado el replanteamiento de contenido y mapa.
  La ruta principal usa Pointe-Noire → Massabi → Cabinda → Yema → Muanda →
  Boma → Matadi → Lufu en bajada y el mismo eje en subida. El ferry
  Brazzaville/Kinshasa se conserva en la capa secundaria, apagada de inicio.
  Se han rehecho las secciones operativas de Congo, RD Congo y Angola/Cabinda:
  fronteras, visados, vehículos, etapas, costes, riesgos y agua. El expediente
  de fuentes y las incógnitas que deben cerrarse en 2027 están en
  [`audit/corredor-congo-cabinda.md`](corredor-congo-cabinda.md).

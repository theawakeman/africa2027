# Grupo 4 · auditoría editorial y visual de PDIs

Países: Camerún, Gabón, Congo, RD Congo y Angola. Revisión realizada el 14 de
septiembre de 2026.

## Alcance cerrado en este grupo

- Se revisaron las asignaciones fotográficas de los 92 PDIs. Cada ficha tiene
  ahora un campo `photos`, incluso cuando el resultado responsable es una lista
  vacía.
- Los 48 PDIs de prioridad alta tienen una ficha de decisión estructurada:
  por qué ir, qué se ve realmente, acceso, cuándo conviene y cuándo descartarlo.
- Se comprobaron 125 archivos contra la API de Wikimedia Commons: todos existen
  y conservan una página de origen trazable. No se reutiliza ningún archivo en
  dos PDIs diferentes del grupo.
- Se eliminaron fotografías genéricas o correspondientes a otro lugar. No se
  sustituyeron por relleno: seis PDIs prioritarios y treinta y cuatro secundarios
  quedan sin foto cuando no se encontró una coincidencia suficientemente sólida.
- Los enlaces añadidos apuntan a la ficha concreta del parque, santuario,
  organismo o bien patrimonial; no se considera que una portada genérica resuelva
  la verificación operativa.

## Resultado por país

| País | PDIs | Prioridad alta con ficha de decisión | PDIs con foto | Galerías (2+ fotos) | Archivos verificados | Sin foto exacta |
|---|---:|---:|---:|---:|---:|---:|
| Camerún | 21 | 11/11 | 11 | 11 | 32 | 10 |
| Gabón | 19 | 9/9 | 9 | 9 | 25 | 10 |
| Congo | 18 | 8/8 | 4 | 4 | 11 | 14 |
| RD Congo | 12 | 9/9 | 10 | 6 | 22 | 2 |
| Angola | 22 | 11/11 | 18 | 10 | 35 | 4 |
| **Total** | **92** | **48/48** | **52** | **40** | **125** | **40** |

## Problema inicial y criterio aplicado

Antes de esta pasada, Camerún tenía solo cuatro fuentes visuales para 21 PDIs y
todos sus PDIs estaban dentro de algún grupo de duplicados; en Gabón la
duplicación afectaba a 18 de 19 fichas, y en Congo a 13 de 18. RD Congo y Angola
tenían menos duplicados, pero sí imágenes asignadas a lugares distintos del PDI.

El resultado no se mide por llenar todas las tarjetas. Una foto solo se mantiene
cuando el archivo identifica el lugar exacto por descripción, categoría o GPS.
Las excepciones informativas se rotulan sin ambigüedad: Cangandala usa una foto
de la palanca negra gigante tomada en Luando y un mapa de distribución;
Tchitundu-Hulu usa una reproducción del motivo «Sol de Angola», no una vista del
yacimiento.

## Huecos deliberados en prioridad alta

- **Congo:** Ngaga Camp; bais de Odzala; rápidos del Djoué; cataratas de
  Loufoulakari; reserva de Lésio-Louna.
- **RD Congo:** rápidos de Kinsuka / Chez Tintin.

Estos seis PDIs mantienen toda la información de decisión, pero no muestran la
vieja imagen incorrecta. Se podrán completar cuando exista una fotografía libre
que identifique inequívocamente el sitio o cuando se incorporen fotografías
propias.

## Hallazgos de actualidad incorporados

- Ape Action Africa publica que Mefou permanece cerrado a visitantes hasta nuevo
  aviso; la ficha ya no lo propone como una visita disponible.
- Morro do Moco obtuvo protección legal en abril de 2026; se retiró la afirmación
  obsoleta de que carecía de estatus de protección.
- La cifra de más de 200 palancas observadas en Cangandala en agosto de 2026 se
  presenta como una concentración documentada, no como censo ni promesa de
  avistamiento.

## Pendiente conocido

La ampliación equivalente de los PDIs de prioridad media y baja no forma parte
del cierre editorial de este bloque: sus fotos sí se han auditado, pero todavía
no todos tienen los cinco campos de decisión ni enlaces específicos. Esta deuda
queda visible en `audit/ESTADO.md` y no debe confundirse con un grupo totalmente
terminado bajo el nuevo estándar.

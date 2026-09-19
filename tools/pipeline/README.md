# Pipeline de alta de países (formato «piloto de Túnez»)

Todo lo necesario para crear la ficha completa de un país del portal: 18–20 PDIs
con ficha de decisión, enlaces y galería de Wikimedia Commons con autor y
licencia; historia de siete secciones con fuentes; cabecera uniforme de 14 chips;
y la fila y la ficha correspondientes en el dosier del perro.

Validado en Túnez (piloto) y aplicado a veinte países entre el 18 y el 19 de
septiembre de 2026.

## Qué hay aquí

- `paises.json` — parámetros por país (PAIS, PAIS_EN, MAEC_PDF, MAEC_TRC,
  FH_SLUG, BRIT, CC, CONTEXTO, EMBAJADA_HINT, ACCESO_HINT, PDIS).
- `historia.md`, `pdis.md`, `operativo.md` — las tres plantillas de encargo.
- `render.py <slug>...` — rellena las plantillas con los parámetros del país y
  escribe `<scratch>/<slug>/prompt_{historia,pdis,operativo}.md`.
- `geo_js.py <slug> <PaisEn>` — imprime el JavaScript que geocodifica todos los
  puntos del país contra Google Maps desde una pestaña de google.com.
- `commons_js.py`, `geo_batches.py` — ayudas para trocear consultas.
- `assemble_country.py <slug>` — monta `tools/gen/data_<slug>.py` y da de alta el
  país en build.py, los migradores, `data_cabeceras`, `data_visados`, `data_cpd`,
  `data_perro_contactos` y el dosier del perro. Es idempotente.
- `audit_md.py <slug> "<Nombre>" "<grupo>" [notas.md]` — escribe
  `audit/pdi/<slug>.md`.

Variables de entorno: `A27_REPO` (raíz del repo, por defecto
`/home/claude/africa2027`) y `A27_SCRATCH` (carpeta de trabajo con un
subdirectorio por país, por defecto el padre de este directorio).

## Procedimiento, paso a paso

1. **Parámetros.** Añade el país a `paises.json` si no está. El campo `CONTEXTO`
   es el que más pesa: mete ahí lo que decide la ficha (régimen político,
   visados, fronteras, avisos del MAEC, bienes UNESCO) y pide explícitamente que
   se verifique con fuente fechada, porque los agentes corrigen el contexto a
   menudo y esas correcciones son el hallazgo más valioso de cada tanda.
2. **Encargos.** `python3 render.py <slug>`.
3. **Investigación.** Tres agentes por país en paralelo (historia / PDIs /
   operativo), cada uno con su `prompt_*.md`. Solo WebFetch y WebSearch:
   `commons.wikimedia.org` y Google Maps están bloqueados para los agentes.
   Dales instrucción de escribir su JSON a disco en cuanto lo tengan, y de usar
   nombres de script distintos, porque comparten carpeta.
   - historia → `audit/historia/<slug>.json`
   - PDIs → `<scratch>/<slug>/pdis.json`
   - operativo → `<scratch>/<slug>/operativo.json`
4. **Geocodificación.** Desde el navegador del propietario, con una pestaña
   abierta en google.com: `python3 geo_js.py <slug> "<PaisEn>"` y pega el
   resultado en el ejecutor de JavaScript. El JS llama a
   `/search?tbm=map&hl=es&q=…` y saca nombre y coordenadas. Mira el nombre que
   devuelve CADA punto: Google cuela objetos de otros continentes con pasmosa
   facilidad (una lechería de Barcelona por un pueblo de Burkina, un mirador de
   Cascaes por la Boca do Inferno santomense, una agencia de viajes de Asmara por
   el yacimiento de Adulis). Lo que no tenga objeto navegable conserva la
   coordenada de la fuente y se etiqueta «(sin objeto en Google Maps; coordenada
   de la fuente)». Guarda todo en `<scratch>/<slug>/gm_results.json` con la forma
   `{clave: {q, name, lat, lon}}`.
5. **Fotografías.** API de Commons desde el navegador, con `origin=*`. Filtrar
   por `width>=height` y `width>=900` mejora muchísimo la selección. Escribe
   `photo_sel.json` (`{n_pdi: [[fichero, pie], …]}`) y verifica autoría y
   licencia de todas juntas en una sola llamada que devuelva solo
   `[missing, autor, licencia]` en el orden de los títulos: ahorra la mitad de
   tokens. **Escribe `photo_meta.json` a disco en cuanto llegue la respuesta**;
   si la sesión se corta antes, hay que repetir las doscientas consultas.
6. **Portada.** `extra.json` con `{"hero": n}`, el PDI cuya primera foto abre la
   ficha.
7. **Montaje.** `python3 assemble_country.py <slug>`.
8. **Dosier del perro.** La fila que `assemble_country.py` inserta en §2.4 se
   **reescribe siempre a mano**, con las ocho columnas y las tres últimas como
   `| — | — | — |`; después `python3 tools/gen/actualiza_dosier.py` las rellena.
   Si se deja la fila corta, el actualizador se come las columnas del medio.
9. **Publicación.** `python3 tools/gen/exporta_contenido.py <slug> --force`,
   luego `python3 tools/gen/build.py`.
10. **Validación.** `python3 tools/validate_poi_sync.py <slug>` y
    `python3 tools/validate_gps.py <slug>...`. El segundo comprueba que cada
    coordenada cae dentro del país, detecta latitudes y longitudes
    intercambiadas, decimales insuficientes, pines duplicados y PDIs muy alejados
    del centro. Si avisa de que dos PDIs comparten pin, casi siempre es que uno
    de los dos no tiene objeto en Google Maps y ha caído sobre el otro: devuélvelo
    a su coordenada de origen.
11. **Expediente.** `python3 audit_md.py <slug> "<Nombre>" "<grupo>" notas.md`,
    con un fichero de notas que recoja las correcciones y los límites de la tanda.
12. **Estado.** Una fila por país en la tabla del grupo 10 de `audit/ESTADO.md` y
    un párrafo en la sección «Países fuera del itinerario».
13. **Entrega.** El contenedor recibe 403 al empujar, así que la entrega es por
    `git bundle`, y **el bundle se genera desde el HEAD del clon del propietario,
    no desde origin/main**: el bot de GitHub añade un commit de reconstrucción
    después de cada push, así que `origin/main..main` produce un bundle que su
    clon no puede aplicar. Comprueba su HEAD en su máquina y usa `<su-HEAD>..main`.

## Régimen del perro para la vuelta a la UE

Reglamento Delegado (UE) 2026/131 más la lista del Reglamento de Ejecución (UE)
2026/636. Ningún país de África continental está listado, así que todos exigen la
«vía A»: titulación antirrábica de 0,5 UI/ml o más, hecha en la UE y anotada en el
pasaporte **antes** de salir. **Mauricio sí está listado**, junto con Santa Elena
y Ascensión: su ficha del perro es la única distinta de toda la guía.

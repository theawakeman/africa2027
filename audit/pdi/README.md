# Auditoría editorial y visual de PDIs

Esta pasada comienza en el grupo 4. Su estado maestro está en
[`audit/ESTADO.md`](../ESTADO.md).

Una fotografía solo se acepta cuando el título, la descripción, las categorías
o las coordenadas del archivo permiten atribuirla al PDI concreto. Una búsqueda
por nombre produce candidatos, no una validación automática. Se conserva la
página del archivo, autor y licencia. Si no hay coincidencia sólida, la ficha se
queda sin imagen.

El generador admite desde esta revisión un campo opcional `photos` por PDI. Cada
elemento contiene `img`, `source`, `credit` y `caption`; la ausencia de fotos se
representa con `photos: []`. También admite `visit` (`why`, `see`, `access`,
`when`, `skip`) y `links` para información oficial o específica del lugar.

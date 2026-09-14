# Auditoría editorial y visual de PDIs

Esta pasada comienza en el grupo 4. Su estado maestro está en
[`audit/ESTADO.md`](../ESTADO.md).

Una fotografía solo se acepta cuando el título, la descripción, las categorías,
las coordenadas o la página original permiten atribuirla al PDI concreto. Una
búsqueda por nombre produce candidatos, no una validación automática. Se
conservan fuente, autor y licencia cuando está publicada. Si para un enclave muy
remoto no existe una imagen libre, se admite una fotografía enlazada de Google
Maps, una web oficial o una fuente local identificable, siempre con pie exacto y
sin presentar un lugar vecino como si fuera el PDI.

Desde la reapertura del grupo 4, ninguna ficha se considera cerrada sin al menos
una fotografía pertinente y un enlace informativo propio. El crédito de la foto
y el simple pin de Google Maps no cuentan como ese enlace de interés.

El generador admite desde esta revisión un campo opcional `photos` por PDI. Cada
elemento contiene `img`, `source`, `credit` y `caption`; la ausencia de fotos se
representa con `photos: []`. También admite `visit` (`why`, `see`, `access`,
`when`, `skip`) y `links` para información oficial o específica del lugar.

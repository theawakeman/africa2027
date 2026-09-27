# Datos del Planificador por puntos (fase 1)

Generado por `tools/gen/planificador_puntos.py` en cada reconstrucción. No se edita a mano:
si algo está mal, se corrige en la ficha del país (tiempo, perro o punto de frontera).

- Puntos de interés: 1318; tiempo leído directamente en 1307, con criterio en 11.
- Puestos fronterizos terrestres: 190; emparejados con seguridad 173, a revisar 26. Puertos y aeropuertos: 56 (no unen dos países por carretera).
- Perro: si 95, condiciones 565, no 528, sin_dato 130.

## Tiempos leídos con criterio

| País | Punto | Texto de la ficha | Días | Criterio |
| --- | --- | --- | --- | --- |
| benin | Parque Nacional de la Pendjari — FUERA DEL ITINERARIO 2027 | — | 0.5 | sin tiempo en la ficha: medio día por defecto |
| benin | Cascadas de Tanougou y la cordillera de la Atacora — FUERA DEL ITINERARIO 2027 | — | 0.5 | sin tiempo en la ficha: medio día por defecto |
| benin | Parque Nacional W (UNESCO, transfronterizo) — FUERA DEL ITINERARIO 2027 | — | 0.5 | sin tiempo en la ficha: medio día por defecto |
| camerun | Mamfe (paso obligado de entrada) | sin pernocta | 0.5 | sin pernocta: medio día |
| camerun | Kumba y el lago cratérico de Barombi Mbo | paso, sin parada | 0.25 | parada breve |
| camerun | Mefou · santuario de primates (Ape Action Africa) | cerrado hasta nuevo aviso; revalidar | 0 | la ficha dice que no se visita o está cerrado |
| mozambique | Reserva Especial de Niassa · excluida por seguridad | no se visita | 0 | la ficha dice que no se visita o está cerrado |
| mozambique | Pemba y Quirimbas · excluidos por seguridad | no se visita | 0 | la ficha dice que no se visita o está cerrado |
| sahara-occidental | Lemsid · la etapa intermedia | parada técnica | 0.25 | parada breve |
| sahara-occidental | Cabo Blanco y La Güera · la foca monje (NO accesible desde aquí) | no visitable en este tramo | 0 | la ficha dice que no se visita o está cerrado |
| zimbabue | Zambezi National Park | incluido arriba | 0 | la ficha dice que no se visita o está cerrado |

## Puestos fronterizos a revisar

`fiable` = a menos de 25 km de los dos países; `oficial` = la ficha no dice que no es un puesto.

| País | Punto | Une con | km al otro país | km al propio | Estado | Oficial |
| --- | --- | --- | --- | --- | --- | --- |
| argelia | Tamanrasset (base del Hoggar y puerta del sur) | — | None | 0.0 | abierta | sí |
| burkina-faso | Paso fronterizo de Kantchari (Níger – Burkina Faso) | niger | 30.1 | 0.0 | abierta | sí |
| chad | Paso fronterizo de Adré (Sudán) — CERRADO | sudan | 7.9 | 0.0 | cerrada | sí |
| chad | Macizo del Enedi (Patrimonio Mundial UNESCO, 2016) | — | None | 0.0 | abierta | sí |
| egipto | Paso fronterizo de Taba (Egipto-Israel) | — | None | 0.0 | abierta | sí |
| egipto | Paso fronterizo de El Salloum (Egipto-Libia) | libia | 0.0 | 6.1 | cerrada | sí |
| eritrea | Teseney (paso hacia Kassala, Sudán) | sudan | 26.4 | 0.0 | revisar | sí |
| etiopia | Paso fronterizo de Togochale / Tog Wajaale (Somalilandia) | — | None | 7.9 | abierta | sí |
| guinea | Frontera · Entrada bajada — Sambaïlo / Koundara (desde Kalifourou, Senegal) | senegal | 0.1 | 0.0 | abierta | no |
| guinea | Frontera · Salida bajada — N'Zo / Gbapleu (hacia Danané, Costa de Marfil) | costa-de-marfil | 0.0 | 8.9 | revisar | sí |
| libia | Paso fronterizo de Sallum–Amsaad (Egipto–Libia) | egipto | 10.9 | 0.0 | cerrada | sí |
| mauritania | Aïn Bentili — puesto militar y tienda | sahara-occidental | 1.9 | 0.0 | abierta | no |
| mauritania | Aduana de Zuérat — trámite del vehículo tras entrar desde Argelia | argelia | 647.9 | 0.0 | abierta | sí |
| niger | Puesto fronterizo de Assamakka (Argelia) | argelia | 31.1 | 0.0 | abierta | sí |
| niger | Paso de Gaya - Malanville (Benín) | benin | 9.4 | 0.0 | cerrada | sí |
| sahara-occidental | Entrada (bajada) · Tarfaya → Tah: sin frontera internacional | marruecos | 11.3 | 30.3 | abierta | sí |
| sahara-occidental | Salida (subida) · Smara → Tan-Tan o El Aaiún → Tarfaya | marruecos | 102.7 | 0.0 | abierta | sí |
| senegal | Paso fronterizo Kalifourou — salida hacia Guinea | guinea | 37.3 | 0.0 | abierta | sí |
| senegal | Sambaïlo (Koundara) — primeros controles guineanos tras Kalifourou | guinea | 0.0 | 0.1 | abierta | no |
| seychelles | Port Victoria (puerto de entrada marítimo e Inter Island Quay) | — | None | None | abierta | sí |
| sierra-leona | Frontera · Salida alternativa noreste — Kabala / Faranah (hacia la Alta Guinea) | guinea | 30.6 | 0.0 | abierta | sí |
| somalia | Paso fronterizo de Tog Wajaale (Etiopía–Somalilandia) | etiopia | 7.9 | 478.5 | abierta | sí |
| somalia | Paso fronterizo de Loyada (Yibuti–Somalilandia) | yibuti | 10.9 | 620.2 | abierta | sí |
| sudan | Paso de Argeen / Arqin (Egipto) | egipto | 0.4 | 0.0 | cerrada | sí |
| sudan-del-sur | Parque Nacional de Badingilo (Patrimonio Mundial de la UNESCO) | — | None | 0.0 | abierta | sí |
| yibuti | Paso fronterizo de Loyada (Yibuti → Somalilandia) | somalia | 620.2 | 10.9 | abierta | sí |

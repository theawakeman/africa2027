# -*- coding: utf-8 -*-
"""Eritrea — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Eritrea está FUERA DE LA RUTA PREVISTA y es además uno de los países más cerrados del mundo: partido único desde 1993 sin elecciones ni constitución en vigor, servicio militar indefinido, prensa clausurada desde 2001 y últimos puestos de Freedom House y RSF. La app solo tiene una ficha stub: créala entera con el formato del piloto de Túnez. La ficha es INFORMATIVA. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: el visado turístico es difícil y se concede con cuentagotas; hace falta un PERMISO DE VIAJE INTERIOR (travel permit) para salir de Asmara, que se tramita en el Ministerio de Turismo y no cubre todas las zonas; está prohibido fotografiar instalaciones militares, puertos y puentes; y las fronteras terrestres con Etiopía llevan cerradas desde 2020-2021 pese al acuerdo de paz de 2018. Asmara es Patrimonio de la Humanidad desde 2017 por su arquitectura modernista italiana, y el ferrocarril Asmara-Massawa sigue funcionando a ratos con locomotoras de vapor de los años treinta.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/eritrea.json y audit/pdi/eritrea.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Asmara · la ciudad modernista africana (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="permitido con condiciones", time="2 noches",
        lat=15.3364254, lon=38.9386724,  # Google Maps: Harnet Avenue (Asmara)
        desc="Capital a 2.325 m que Italia levantó entre 1893 y 1941 como laboratorio del racionalismo: trazado ortogonal y radial, cines, bares, garajes y ministerios casi intactos. La UNESCO la inscribió en 2017 con los criterios (ii) y (iv) sobre 481 hectáreas y 1.203 de zona tampón. Se recorre entera a pie y en un día largo. Advertencia: PROHIBIDO FOTOGRAFIAR edificios gubernamentales, cuarteles y uniformados, y para salir de la provincia hace falta permiso de viaje interior.",
        dog_note="Se puede pasear por la ciudad, pero museos, iglesias y mezquitas no admiten perros y el control veterinario de entrada al país está por confirmar.",
        visit={
            "why": "Es el conjunto modernista de los años treinta mejor conservado del mundo y el único lugar de Eritrea al que se llega sin permiso especial.",
            "see": "Harnet Avenue con su paseo vespertino, la catedral católica, Cinema Impero, el Fiat Tagliero, la mezquita Al Khulafa Al Rashiudin y el barrio de villas.",
            "access": "Se entra por el aeropuerto internacional de Asmara; las fronteras terrestres están cerradas (MAEC, 28-02-2025). Dentro de Zoba Maekel NO hace falta permiso de viaje interior, pero sí para cualquier salida y el Ministerio de Turismo está en Harnet Avenue frente a la catedral. Aparcar dos 4x4 es fácil en las calles del centro. El pin marca la avenida Harnet, eje del área inscrita.",
            "when": "De noviembre a febrero; a 2.325 m las tardes son frescas y la ciudad sale a pasear entre las 18:00 y las 20:00.",
            "skip": "No se descarta: si se llega a Eritrea, Asmara es el viaje; lo que se descarta es el país entero mientras el MAEC desaconseje viajar.",
        },
        links=[
            {"label": "UNESCO · Asmara: A Modernist African City (1550)", "url": "https://whc.unesco.org/en/list/1550/"},
            {"label": "Wikipedia · Asmara", "url": "https://en.wikipedia.org/wiki/Asmara"},
            {"label": "MAEC · Recomendaciones de viaje Eritrea", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Eritrea"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Piccola_Roma_(Asmara).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Piccola_Roma_(Asmara).jpg",
                "credit": "Awet Amine · CC0",
                "caption": "Atardecer sobre Asmara, la «Piccola Roma».",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Plan_for_Asmara_1913.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Plan_for_Asmara_1913.jpg",
                "credit": "Autor desconocido · Public domain",
                "caption": "El plano de Asmara de 1913.",
            },
        ],
    ),
    dict(
        n=2, name="Cinema Impero y la avenida Harnet · el art déco de los años treinta", cat="Cultura", prio="Alta",
        dog="prohibido", time="medio día",
        lat=15.3367639, lon=38.9402282,  # Google Maps: Cinema Impero
        desc="El Impero abrió en 1937 en la avenida Harnet, obra de Mario Messina, y los expertos lo consideran uno de los mejores edificios art déco del mundo. SIGUE PROYECTANDO, hoy en DVD, con su fachada de bandas horizontales y leones en relieve. Alrededor, la avenida concentra el Bar Zilli, el Cinema Roma y la catedral. Advertencia: es la misma calle donde está el Ministerio de Turismo, y conviene no sacar la cámara hacia los edificios oficiales.",
        dog_note="Sala de cine en funcionamiento: no se admiten animales dentro; el perro se queda en la avenida con uno de los tres.",
        visit={
            "why": "Condensa en cien metros el argumento por el que Asmara es Patrimonio de la Humanidad y sigue siendo un cine vivo, no un museo.",
            "see": "La fachada de 1937 con sus tres bandas verticales y los leones, el vestíbulo original y el paseo de la avenida al caer la tarde.",
            "access": "Pleno centro de Asmara, en Harnet Avenue: sin permiso de viaje interior, porque no se sale de Zoba Maekel. Aparcamiento en batería en la propia avenida, suficiente para dos 4x4 fuera de las horas del paseo. Entrada al cine de pocos nakfa; el pin marca la fachada del Impero sobre Harnet Avenue.",
            "when": "Al atardecer, cuando la avenida se llena para la passeggiata y la luz rasante saca el relieve de las fachadas.",
            "skip": "Si solo hay una tarde en Asmara y se prefiere el Fiat Tagliero, que es más espectacular de ver por fuera.",
        },
        links=[
            {"label": "Wikipedia · Cinema Impero", "url": "https://en.wikipedia.org/wiki/Cinema_Impero"},
            {"label": "Cinema Treasures · Cinema Impero, Asmara", "url": "https://cinematreasures.org/theaters/7910"},
            {"label": "UNESCO · Asmara (1550)", "url": "https://whc.unesco.org/en/list/1550/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cinema_Impero_Asmara,_Eritrea_(30660837982).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cinema_Impero_Asmara,_Eritrea_(30660837982).jpg",
                "credit": "Clay Gilliland from Chandler, U.S.A. · CC BY-SA 2.0",
                "caption": "El Cinema Impero, en Harnet Avenue.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Asmara,_cinema_impero,_01.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Asmara,_cinema_impero,_01.JPG",
                "credit": "sailko · CC BY-SA 3.0",
                "caption": "La fachada art déco del Impero.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Asmara,_cinema_impero,_07.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Asmara,_cinema_impero,_07.JPG",
                "credit": "sailko · CC BY-SA 3.0",
                "caption": "Detalle del Cinema Impero.",
            },
        ],
    ),
    dict(
        n=3, name="La estación Fiat Tagliero · la gasolinera con alas", cat="Cultura", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=15.3284088, lon=38.9259084,  # Google Maps: Fiat Tagliero
        desc="Gasolinera de 1938 del ingeniero Giuseppe Pettazzi: dos alas de hormigón armado de unos quince metros voladas sin un solo pilar, como un avión a punto de despegar. Cuenta la leyenda que Pettazzi resolvió la discusión con el contratista A PUNTA DE PISTOLA para que retirasen los puntales. Restaurada en 2003 y catalogada en Categoría I, no admite alteraciones. Advertencia: sigue siendo una instalación en uso y conviene pedir permiso antes de fotografiar a quien trabaja allí.",
        dog_note="Es una gasolinera a pie de calle, sin recinto: el perro puede estar atado al lado, pero hay tráfico.",
        visit={
            "why": "Es el icono del futurismo italiano en África y la imagen que todo el mundo asocia a Asmara.",
            "see": "Las dos alas en voladizo, la torre central acristalada con caja y tienda y la rotulación original de FIAT.",
            "access": "En el centro de Asmara, en la esquina de Mereb Street; no requiere permiso de viaje interior. Se puede parar un momento junto al bordillo, pero no hay aparcamiento propio para dos 4x4: mejor dejarlos en Harnet y acercarse andando. El pin marca el edificio de la estación de servicio.",
            "when": "Por la mañana temprano, con el sol de frente sobre la fachada y poco tráfico.",
            "skip": "Nunca si se está en Asmara; son diez minutos de desvío desde la avenida principal.",
        },
        links=[
            {"label": "Wikipedia · Fiat Tagliero Building", "url": "https://en.wikipedia.org/wiki/Fiat_Tagliero_Building"},
            {"label": "Atlas Obscura · Fiat Tagliero Service Station", "url": "https://www.atlasobscura.com/places/fiat-tagliero-service-station-asmara-eritrea"},
            {"label": "UNESCO · Asmara (1550)", "url": "https://whc.unesco.org/en/list/1550/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fiat_Tagliero_Building.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fiat_Tagliero_Building.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La estación Fiat Tagliero, la gasolinera con alas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fiat_Tagliero_petrol_station_in_Asmara.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fiat_Tagliero_petrol_station_in_Asmara.jpg",
                "credit": "JanNeysan · CC BY-SA 4.0",
                "caption": "Los voladizos de hormigón del Tagliero.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fiat_tagliero,_08.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fiat_tagliero,_08.JPG",
                "credit": "sailko · CC BY-SA 3.0",
                "caption": "El Tagliero de cerca.",
            },
        ],
    ),
    dict(
        n=4, name="Mercado de Medeber y el zoco de Asmara · el reciclaje hecho oficio", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=15.3442297, lon=38.9454433,  # Google Maps: Medebar Market
        desc="Al este del centro, detrás del mercado principal, Medeber es un taller colectivo donde decenas de artesanos convierten chatarra, caucho, madera y plástico en cubos, cocinas, muebles y bicicletas. Las sandalias hechas con neumático usado son el souvenir clásico. Hay también una zona de molinos de especias. Advertencia: es un lugar de trabajo y muy ruidoso; se pide permiso antes de fotografiar a cada persona y se camina con cuidado entre soldadores.",
        dog_note="Chapa, soldadura, chispas y hierro en el suelo: un perro suelto se corta; mejor dejarlo en el vehículo a la sombra o con un acompañante fuera.",
        visit={
            "why": "Explica mejor que ningún museo cómo funciona la economía eritrea bajo sanciones y escasez.",
            "see": "Soldadores, hojalateros y zapateros trabajando con material recuperado, molinos de especias y puestos de artesanía.",
            "access": "A quince minutos a pie del centro de Asmara, dentro de Zoba Maekel: sin permiso de viaje interior. Se puede aparcar en las calles del entorno del mercado grande. Sin taquilla ni horario formal; funciona de mañana los días laborables. El pin marca la entrada del recinto de Medeber.",
            "when": "Media mañana entre semana, cuando todos los talleres están abiertos.",
            "skip": "Si el grupo va justo de tiempo y prefiere concentrar el día en la arquitectura de Harnet.",
        },
        links=[
            {"label": "Atlas Obscura · Medeber Market", "url": "https://www.atlasobscura.com/places/medeber-market"},
            {"label": "UNESCO · Asmara (1550)", "url": "https://whc.unesco.org/en/list/1550/"},
            {"label": "FCDO · Eritrea safety and security (normas de fotografía)", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/safety-and-security"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Medebar_Market,_Asmara.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Medebar_Market,_Asmara.jpg",
                "credit": "Mheidegger · CC BY 4.0",
                "caption": "El mercado de Medeber, donde se recicla todo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Medebar_Market_in_Asmara_2024_(1).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Medebar_Market_in_Asmara_2024_(1).jpg",
                "credit": "Mheidegger · CC BY-SA 4.0",
                "caption": "Chavales trabajando en Medeber.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Asmara_Market_(2013).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Asmara_Market_(2013).jpg",
                "credit": "JanNeysan · CC BY-SA 4.0",
                "caption": "El mercado de Asmara.",
            },
        ],
    ),
    dict(
        n=5, name="Massawa · el puerto otomano y egipcio del mar Rojo", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=15.6080391, lon=39.4531069,  # Google Maps: Massawa
        desc="Puerto desde los siglos VIII-X, otomano en 1557, egipcio desde 1865 e italiano desde 1885, cuando fue capital de la colonia hasta 1897. El casco viejo, coral y madera, quedó arrasado por los bombardeos de 1990 tras la Operación Fenkil y todavía enseña las ruinas. Advertencia: PROHIBIDO FOTOGRAFIAR el puerto, y para visitar la ciudad vieja hace falta el permiso de viaje interior tramitado en Asmara.",
        dog_note="Calor extremo: en Massawa la media anual roza los 30 °C y en verano es inviable sacar al perro de día; mezquitas y museo, vetados.",
        visit={
            "why": "Es el contrapunto costero de Asmara y la base logística para Dahlak, Gurgusum y Adulis.",
            "see": "El Palacio Imperial de 1872-1874, la mezquita de Sheikh Hanafi del siglo XV, la catedral de Santa María y los edificios acribillados de la isla de Batse.",
            "access": "Carretera asfaltada P-1 desde Asmara (unos 115 km, descenso de 2.300 m). EXIGE PERMISO DE VIAJE INTERIOR con matrícula del vehículo y fechas; los puestos de control lo comprueban (FCDO, 27-07-2026). Against the Compass advierte de que «para visitar la ciudad vieja de Massawa hace falta permiso». Aparcamiento amplio junto a los puentes de acceso a la isla. El pin marca la ciudad vieja de Batse.",
            "when": "De noviembre a febrero; el resto del año el calor con humedad la hace una de las costas más duras del mundo.",
            "skip": "Si no se ha conseguido el permiso en Asmara: en el control de carretera dan la vuelta.",
        },
        links=[
            {"label": "Wikipedia · Massawa", "url": "https://en.wikipedia.org/wiki/Massawa"},
            {"label": "FCDO · Eritrea safety and security", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/safety-and-security"},
            {"label": "Against the Compass · How to travel to Eritrea", "url": "https://againstthecompass.com/en/travel-eritrea/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Historic_Center_Massawa_Panorama.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Historic_Center_Massawa_Panorama.JPG",
                "credit": "Reinhard Dietrich · CC0",
                "caption": "El centro histórico de Massawa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Massawa_Old_City_2024.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Massawa_Old_City_2024.jpg",
                "credit": "Mheidegger · CC BY 4.0",
                "caption": "La ciudad vieja de Massawa en 2024.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Massawa_harbour.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Massawa_harbour.JPG",
                "credit": "Reinhard Dietrich · CC0",
                "caption": "El puerto de Massawa.",
            },
        ],
    ),
    dict(
        n=6, name="Archipiélago de Dahlak · las islas y el buceo del mar Rojo", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="1–2 noches",
        lat=15.833, lon=40.2,  # Google Maps: Archipiélago de Dahlak (sin objeto en Google Maps; coordenada de la fuente)
        desc="Dos islas grandes y 124 pequeñas frente a Massawa, de las que solo TRES están habitadas de forma permanente. Sus pesquerías de perlas son famosas desde época romana y siguen dando perlas; Dahlak Kebir, la mayor, conserva cisternas antiguas y una necrópolis datada al menos en el año 912. BirdLife la declaró Área Importante para las Aves. Advertencia: se llega solo en barco desde Massawa, con permiso y precio alto, y el puerto no se fotografía.",
        dog_note="Salida en barco de varias horas con calor extremo y sin sombra; en las islas no hay agua dulce ni veterinario.",
        visit={
            "why": "Arrecifes poco buceados y una de las colonias de aves marinas más importantes del mar Rojo.",
            "see": "Fondos de coral, tortugas y dugongos por confirmar, las cisternas y la necrópolis de Dahlak Kebir y aldeas de pescadores dahalik.",
            "access": "Solo por mar desde Massawa; hay ferris a Dahlak Kebir y excursiones de un día que Wild Junket cifró en unos 11.000 nakfa (≈733 USD). Requiere permiso de viaje interior y, en la práctica, agencia local. Los 4x4 se quedan en Massawa. FCDO desaconseja las islas Hanish, más al sur, donde ha habido detenciones. El pin de referencia es el archipiélago; se navega desde el puerto de Massawa.",
            "when": "De noviembre a febrero, con mar más manejable y temperaturas soportables.",
            "skip": "Si no hay presupuesto para la lancha o si el permiso no incluye la salida marítima.",
        },
        links=[
            {"label": "Wikipedia · Dahlak Archipelago", "url": "https://en.wikipedia.org/wiki/Dahlak_Archipelago"},
            {"label": "Wikipedia · Dahlak Kebir", "url": "https://en.wikipedia.org/wiki/Dahlak_Kebir"},
            {"label": "FCDO · Eritrea regional risks", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/regional-risks"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dahlak_Islands_ISS042.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dahlak_Islands_ISS042.jpg",
                "credit": "Tripulación de la Expedición 42 (ISS) · Public domain",
                "caption": "El archipiélago de Dahlak desde la ISS.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Wrecks_on_Dahlak_Island.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Wrecks_on_Dahlak_Island.jpg",
                "credit": "Amod Photography · CC BY-SA 4.0",
                "caption": "Pecios hundidos frente a Dahlak.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Dahlak_Archipelago,_Red_Sea.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Dahlak_Archipelago,_Red_Sea.jpg",
                "credit": "INPE / Coordenação-Geral de Observação da Terra · CC BY-SA 2.0",
                "caption": "Dahlak en el mar Rojo.",
            },
        ],
    ),
    dict(
        n=7, name="El ferrocarril Asmara–Massawa · el tren de vapor y sus viaductos", cat="Cultura", prio="Alta",
        dog="prohibido", time="medio día",
        lat=15.338298, lon=38.951478,  # Google Maps: Estación de ferrocarril de Asmara
        desc="Vía métrica de 950 mm construida entre 1887 y 1932, con el tramo Massawa-Asmara terminado en 1911: 65 puentes —incluido un viaducto de catorce arcos sobre el río Obel— y 39 túneles para subir a 2.394 m. Sobreviven cuatro Mallet compound de Ansaldo de 1938, TRES DE ELLAS OPERATIVAS. No hay servicio regular: solo chárteres turísticos en el tramo alto hacia Arbaroba y Nefasit. Advertencia: no se fotografían los puentes.",
        dog_note="Tren chárter con vagones históricos y operadores muy estrictos; no se admiten animales a bordo.",
        visit={
            "why": "Es uno de los poquísimos lugares del mundo donde locomotoras de vapor de 1938 siguen trabajando en su línea original.",
            "see": "La estación de Asmara, la subida en zigzag por el escarpe, los viaductos de piedra y las Mallet 0-4-4-0T resoplando.",
            "access": "El chárter sale de la estación de Asmara y solo funciona bajo reserva previa (Adulis Travel pide de 3 a 7 días); Against the Compass cita unos 50 USD por persona en grupos de quince. Dentro de Zoba Maekel no hace falta permiso, pero bajar a Nefasit o Ghinda sí lo exige. Aparcamiento de los 4x4 en la explanada de la estación. El pin de coordenadas marca Nefasit, final histórico del tramo turístico.",
            "when": "De noviembre a febrero y a primera hora: el chárter suele salir sobre las 9:00 y ocupa la mañana.",
            "skip": "Si no se ha reservado con días de antelación: no hay billetes sueltos ni horario público.",
        },
        links=[
            {"label": "Wikipedia · Eritrean Railway", "url": "https://en.wikipedia.org/wiki/Eritrean_Railway"},
            {"label": "Adulis Travel · The Eritrean Railway", "url": "https://adulistravel.com/the-eritrean-railway/"},
            {"label": "Wikipedia · Nefasit", "url": "https://en.wikipedia.org/wiki/Nefasit"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Eritrean_Railway_-_2008-11-04-edit1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Eritrean_Railway_-_2008-11-04-edit1.jpg",
                "credit": "Voice of Clam · Public domain",
                "caption": "El ferrocarril de Eritrea entre las montañas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Eritrea_banner_Eritrean_railway_bridge.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Eritrea_banner_Eritrean_railway_bridge.jpg",
                "credit": "Voice of Clam · Public domain",
                "caption": "Uno de los viaductos de la línea a Massawa.",
            },
        ],
    ),
    dict(
        n=8, name="Filfil Solomuna · el último bosque nuboso de Eritrea", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=15.616667, lon=38.966667,  # Google Maps: Fil Fil (Semienawi Bahri)
        desc="El «cinturón verde» de Semienawi Bahri es el resto de bosque nuboso del país: montañas y valles entre 900 y 2.400 m donde condensa la humedad del mar Rojo. Se llega por la carretera de Keren desviándose pasada Serejeka y se desciende unos 77 km por asfalto nuevo entre Moguo, Sabur, Fagiena y Filfil. De las 558 ESPECIES DE AVES de Eritrea, buena parte están aquí. Advertencia: niebla densa y curvas cerradas; nada de conducir de noche.",
        dog_note="Parque nacional con leopardo confirmado en la fauna del área: no conviene llevar al perro fuera del vehículo.",
        visit={
            "why": "Es el único paisaje verdaderamente selvático de Eritrea y la mejor jornada de observación de aves del país.",
            "see": "Bosque siempreverde, arroyos y pozas, dik-diks y duikers, klipspringer, facóquero, bushbuck y kudú mayor; con suerte, alcaudones rosados junto al agua.",
            "access": "Carretera asfaltada de montaña desde Asmara por Serejeka; hay centros recreativos en Meguo, Medhanit y Sabur. SALE DE ZOBA MAEKEL, así que exige permiso de viaje interior del Ministerio de Turismo con la matrícula de cada 4x4. Explanadas junto a los miradores para aparcar. El pin marca el área del parque de Semienawi Bahri.",
            "when": "De junio a septiembre llega la niebla que da vida al bosque; para conducir cómodo, de noviembre a febrero.",
            "skip": "Si el permiso solo cubre el eje Asmara-Massawa: el desvío de Keren queda fuera.",
        },
        links=[
            {"label": "Wikipedia · Semenawi Bahri National Park", "url": "https://en.wikipedia.org/wiki/Semenawi_Bahri_National_Park"},
            {"label": "Visit Eritrea · Filfil Solomuna", "url": "https://www.visiteritrea.net/filfil-solomuna"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Massawa_Highway_(8527952867).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Massawa_Highway_(8527952867).jpg",
                "credit": "David Stanley from Nanaimo, Canada · CC BY 2.0",
                "caption": "La carretera de Asmara a Massawa, que cruza el bosque de Filfil.",
            },
        ],
    ),
    dict(
        n=9, name="Debre Bizen · el monasterio sobre el escarpe", cat="Cultura", prio="Media",
        dog="prohibido", time="1 día",
        lat=15.3305065, lon=39.0639896,  # Google Maps: Nefasit (inicio del sendero a Debre Bizen)
        desc="Monasterio fundado en la década de 1350 por Filipos, discípulo de Absadi, encaramado a 2.460 m sobre el pueblo de Nefasit, en el borde del escarpe que cae hacia el mar Rojo. Su biblioteca guarda MUCHOS MANUSCRITOS IMPORTANTES EN GEEZ. Se sube a pie por una vereda empinada desde Nefasit, en la carretera de Massawa. Advertencia: la tradición restringe la entrada a los varones y conviene confirmarlo antes de subir en grupo mixto.",
        dog_note="Monasterio ortodoxo en clausura: no admite animales y, por confirmar, tampoco mujeres ni hembras de ganado.",
        visit={
            "why": "Es el monasterio más venerado de Eritrea y la vista desde el filo abarca todo el descenso al mar Rojo.",
            "see": "El complejo monástico, la biblioteca de manuscritos en geez y el panorama del escarpe con la vía férrea abajo.",
            "access": "Nefasit está en la P-1 Asmara-Massawa, a 15.33333 N / 39.06194 E y 1.700 m; desde allí sube una vereda de varias horas. SALE DE ZOBA MAEKEL: permiso de viaje interior obligatorio. Los dos 4x4 se quedan en Nefasit. La autorización de entrada la da la comunidad monástica; suele pedirse con antelación. El pin de coordenadas marca el monasterio; se conduce hasta Nefasit.",
            "when": "De noviembre a febrero y saliendo de madrugada: la subida es larga y sin sombra.",
            "skip": "Si el grupo es mixto y no se ha confirmado el acceso, o si no hay día entero disponible.",
        },
        links=[
            {"label": "Wikipedia · Debre Bizen", "url": "https://en.wikipedia.org/wiki/Debre_Bizen"},
            {"label": "Wikipedia · Nefasit", "url": "https://en.wikipedia.org/wiki/Nefasit"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Debre_Bizen.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Debre_Bizen.jpg",
                "credit": "Grullab · CC BY-SA 4.0",
                "caption": "El monasterio de Debre Bizen sobre el escarpe.",
            },
        ],
    ),
    dict(
        n=10, name="Keren · el mercado del lunes y el cementerio de guerra británico", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=15.780151, lon=38.4524487,  # Google Maps: Keren
        desc="Segunda ciudad del país, a 1.590 m y de mayoría musulmana, nacida como asentamiento comercial adonde los hedareb llevaban el grano en camello. En febrero y marzo de 1941 fue escenario de la batalla clave entre italianos y británicos, y conserva los cementerios militares de ambos ejércitos. La capilla de Santa María Deari OCUPA EL HUECO DE UN BAOBAB alcanzado por una bomba en 1941. Advertencia: exige permiso de viaje interior.",
        dog_note="En el mercado de ganado molesta y se estresa; el cementerio de guerra es recinto cerrado y suele exigir dejarlo fuera.",
        visit={
            "why": "El mercado semanal es el más famoso de Eritrea y el conjunto de guerra da la medida de la campaña de África Oriental.",
            "see": "El mercado del lunes con camellos y ganado, el cementerio de guerra británico, el italiano y la capilla dentro del baobab de Mariam Dearit.",
            "access": "Asfalto P-2 desde Asmara, unos 90 km y unas tres horas en autobús según las guías. PERMISO DE VIAJE INTERIOR OBLIGATORIO; Keren figura entre los destinos que las fuentes dan por abiertos con permiso (Against the Compass). Aparcamiento amplio junto al mercado para dos 4x4. El pin marca el recinto del mercado del lunes.",
            "when": "Lunes por la mañana, día del gran mercado; de noviembre a febrero para el clima.",
            "skip": "Si no se llega en lunes y el permiso no da para pernoctar: el resto de la semana el mercado es una sombra de sí mismo.",
        },
        links=[
            {"label": "Wikipedia · Keren, Eritrea", "url": "https://en.wikipedia.org/wiki/Keren,_Eritrea"},
            {"label": "Against the Compass · How to travel to Eritrea", "url": "https://againstthecompass.com/en/travel-eritrea/"},
            {"label": "FCDO · Eritrea safety and security", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/safety-and-security"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Keren,_Eritrea,_2024.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Keren,_Eritrea,_2024.jpg",
                "credit": "Mheidegger · CC BY 4.0",
                "caption": "Keren en 2024.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Keren_-_2008-11-01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Keren_-_2008-11-01.jpg",
                "credit": "Voice of Clam · Public domain",
                "caption": "La ciudad de Keren.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Photo_Eritrea,_Keren,_The_market_square_1953_-_Touring_Club_Italiano_BA0_610.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Photo_Eritrea,_Keren,_The_market_square_1953_-_Touring_Club_Italiano_BA0_610.jpg",
                "credit": "Autor desconocido · CC BY-SA 4.0",
                "caption": "La plaza del mercado de Keren en 1953.",
            },
        ],
    ),
    dict(
        n=11, name="Nakfa · las trincheras de la guerra de independencia", cat="Cultura", prio="Media",
        dog="no recomendado", time="1–2 noches",
        lat=16.6663939, lon=38.476514,  # Google Maps: Nakfa
        desc="En 1977 el EPLF tomó Nakfa tras seis meses de asedio y la convirtió durante una década en su capital clandestina: hospitales, imprentas, fábricas, una emisora y hasta una universidad EXCAVADOS BAJO TIERRA, protegidos por anillos de trincheras y campos de minas. Resistió ocho intentos etíopes de reconquista y la ciudad de superficie quedó destruida. La moneda nacional lleva su nombre. Advertencia: no se sale de la pista por el riesgo de minas.",
        dog_note="Terreno con minas documentadas en la zona y pistas largas sin agua; el perro no debe salir del vehículo fuera de la pista.",
        visit={
            "why": "Es el santuario laico del país y el mejor sitio para entender por qué Eritrea es como es.",
            "see": "Las trincheras del frente, los túneles y talleres subterráneos del EPLF y los restos de la ciudad arrasada.",
            "access": "Pistas largas desde Keren por el macizo de Sahel; la zona está lejos de la costa y a pocas horas de la frontera sudanesa. PERMISO DE VIAJE INTERIOR IMPRESCINDIBLE y, por confirmar, no siempre se concede para Sahel. Canadá avisa de minas sin señalizar en zonas fronterizas y recomienda no salir del asfalto (09-09-2026). El pin marca la localidad de Nakfa.",
            "when": "De noviembre a febrero; en la estación de lluvias las pistas de Sahel se cortan.",
            "skip": "Descártalo de entrada si el permiso no menciona expresamente Nakfa o si la ruta obligaría a acercarse a menos de 25 km de la frontera con Sudán.",
        },
        links=[
            {"label": "Wikipedia · Nakfa, Eritrea", "url": "https://en.wikipedia.org/wiki/Nakfa,_Eritrea"},
            {"label": "Canadá · Travel advice Eritrea", "url": "https://travel.gc.ca/destinations/eritrea"},
            {"label": "FCDO · Eritrea regional risks", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/regional-risks"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nakfa_Village.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Nakfa_Village.jpg",
                "credit": "Prof tpms · CC BY-SA 3.0",
                "caption": "Nakfa, la ciudad de las trincheras.",
            },
        ],
    ),
    dict(
        n=12, name="Qohaito · la meseta aksumita y sus columnas", cat="Cultura", prio="Alta",
        dog="permitido con condiciones", time="1 día",
        lat=14.8708928, lon=39.4167999,  # Google Maps: Qohaito
        desc="Asentamiento preaksumita que floreció en época aksumita, a más de 2.500 m en el borde del Gran Valle del Rift. El llamado templo de Mariam Wakino conserva una planta rectangular de 14 por 25 metros con tres naves separadas por seis pilares cada una; cerca, la presa de Safira mide unos 70 metros de lado. En un barranco hay tumbas con PINTURAS RUPESTRES DE CAMELLOS Y VACAS. Advertencia: el cortado no tiene protección alguna.",
        dog_note="Yacimiento abierto sin vallas ni templos en uso; atado y lejos del ganado de los pastores saho no plantea problema.",
        visit={
            "why": "Es el yacimiento más espectacular del país y está en la lista indicativa de la UNESCO desde 2011.",
            "see": "Las columnas de Mariam Wakino, la presa de Safira, las tumbas con pinturas rupestres de Adi Alauti y el cañón que se abre al este.",
            "access": "Desvío de pista desde Adi Keyh (14°50′N 39°22′E, 2.393 m), en la carretera del sur; Wild Junket cifra el trayecto desde Asmara en unas 4 horas y media y recomienda taxi privado. PERMISO DE VIAJE INTERIOR OBLIGATORIO: Qohaito y Senafe figuran entre los destinos abiertos con permiso. Se aparca en la explanada del yacimiento. El pin marca el área arqueológica.",
            "when": "De noviembre a febrero, a primera hora, con el cañón todavía en sombra y sin calima.",
            "skip": "Si llueve: la pista de acceso desde Adi Keyh se embarra y el borde del cañón es resbaladizo.",
        },
        links=[
            {"label": "Wikipedia · Qohaito", "url": "https://en.wikipedia.org/wiki/Qohaito"},
            {"label": "Wikipedia · Adi Keyh", "url": "https://en.wikipedia.org/wiki/Adi_Keyh"},
            {"label": "Wild Junket · Eritrea travel guide", "url": "https://www.wildjunket.com/eritrea-travel/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kohaito,_zona_dei_palazzi_axumiti_09.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kohaito,_zona_dei_palazzi_axumiti_09.JPG",
                "credit": "Sailko · CC BY 3.0",
                "caption": "La zona de los palacios aksumitas de Qohaito.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kohaito,_zona_dei_palazzi_axumiti_00.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kohaito,_zona_dei_palazzi_axumiti_00.JPG",
                "credit": "Sailko · CC BY 3.0",
                "caption": "Columnas de Qohaito.",
            },
        ],
    ),
    dict(
        n=13, name="Metera y Senafe · las estelas y el yacimiento preaksumita", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=14.5151472, lon=39.3075614,  # Google Maps: Matara
        desc="Metera, o Balaw Kalaw, está unos kilómetros al sur de Senafe y a unos 136 km al sureste de Asmara. Las excavaciones han encontrado varios niveles de ocupación, con al menos dos ciudades distintas superpuestas a lo largo de más de MIL AÑOS. Preside el conjunto el Hawulti, obelisco preaksumita o aksumita temprano que porta el ejemplo más antiguo conocido de escritura geez. Advertencia: Senafe quedó muy dañada en la guerra con Etiopía y está cerca de la frontera.",
        dog_note="Yacimiento al aire libre sin recinto religioso activo; atado y a la sombra, sin problema.",
        visit={
            "why": "El Hawulti es el monumento escrito más antiguo de Eritrea y cierra bien el circuito del altiplano sur con Qohaito.",
            "see": "El obelisco Hawulti, los cimientos de las dos ciudades superpuestas y, desde Senafe, el paisaje de ambas.",
            "access": "Carretera del sur desde Adi Keyh hasta Senafe (14.700 N / 39.417 E, 2.446 m) y desvío corto al yacimiento. PERMISO DE VIAJE INTERIOR OBLIGATORIO; Senafe es uno de los pocos núcleos próximos a la frontera que las fuentes citan como accesible con permiso, pero el FCDO desaconseja todo viaje a menos de 25 km de la frontera etíope (27-07-2026). Se aparca a pie de yacimiento. El pin marca Metera.",
            "when": "De noviembre a febrero, por la mañana; a 2.400 m las tardes se nublan.",
            "skip": "Descártalo si el permiso no nombra Senafe o si hay tensión abierta en la frontera etíope.",
        },
        links=[
            {"label": "Wikipedia · Matara, Eritrea", "url": "https://en.wikipedia.org/wiki/Matara,_Eritrea"},
            {"label": "Wikipedia · Senafe", "url": "https://en.wikipedia.org/wiki/Senafe"},
            {"label": "FCDO · Eritrea regional risks", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/regional-risks"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Qohaito,_Eritrea_(33628113490).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Qohaito,_Eritrea_(33628113490).jpg",
                "credit": "Clay Gilliland from Chandler, U.S.A. · CC BY-SA 2.0",
                "caption": "Ruinas de Matara, cerca de Senafe.",
            },
        ],
    ),
    dict(
        n=14, name="Adulis · el puerto antiguo del mar Rojo", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=15.2636, lon=39.6606,  # Google Maps: (sin objeto en Google Maps; coordenada de la fuente)
        desc="Puerto del reino de Aksum junto a la actual Zula, unos 40 km al sur de Massawa, y emporio de marfil, pieles y esclavos del interior. Conserva una BASÍLICA CRISTIANA DEL SIGLO V y aquí vio Cosmas Indicopleustes, hacia el año 520, el Monumentum Adulitanum con las victorias de un rey aksumita en Arabia y el norte de Etiopía. Excavado desde 1906 con Sundström y Paribeni. Advertencia: calor extremo y sin sombra ni agua.",
        dog_note="Yacimiento abierto en llano costero, sin recinto; el problema es el calor, no la norma.",
        visit={
            "why": "Es la puerta marítima del reino de Aksum y el yacimiento costero más importante del país.",
            "see": "Los cimientos de la basílica bizantina del siglo V, las estructuras excavadas y la cerámica dispersa junto al golfo de Zula.",
            "access": "Desde Massawa por la P-6 hacia el sur, unos 40 km hasta Zula, en el golfo de Zula (15°16′N 39°45′E, a 15 km al este de Massawa). PERMISO DE VIAJE INTERIOR OBLIGATORIO; Foro, la población de referencia de la zona, figura entre los destinos abiertos con permiso. Terreno llano para aparcar dos 4x4. El pin marca el yacimiento, junto a la aldea de Zula.",
            "when": "De noviembre a febrero y al amanecer: a media mañana el llano costero es insoportable.",
            "skip": "Si el grupo ya ha visto Qohaito y Metera y el calor de la costa aprieta: aquí queda poco en pie.",
        },
        links=[
            {"label": "Wikipedia · Adulis", "url": "https://en.wikipedia.org/wiki/Adulis"},
            {"label": "Wikipedia · Gulf of Zula", "url": "https://en.wikipedia.org/wiki/Gulf_of_Zula"},
            {"label": "Against the Compass · How to travel to Eritrea", "url": "https://againstthecompass.com/en/travel-eritrea/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Adulis_(8529061940).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Adulis_(8529061940).jpg",
                "credit": "David Stanley from Nanaimo, Canada · CC BY 2.0",
                "caption": "Las excavaciones de Adulis, el puerto antiguo.",
            },
        ],
    ),
    dict(
        n=15, name="Gurgusum · las playas al norte de Massawa", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=15.6569606, lon=39.468939,  # Google Maps: Gurgusum Beach Resort
        desc="Arenal del mar Rojo inmediatamente al norte de Massawa, la playa urbana de la ciudad y la salida de fin de semana de los asmarinos. No es espectacular —así la describen los viajeros que la han visitado— pero es agua tibia, palmeras y un hotel-resort a pie de arena. Advertencia: el agua ronda los 30 °C y no refresca; y aunque se esté en la playa, PROHIBIDO FOTOGRAFIAR el puerto y las instalaciones militares vecinas.",
        dog_note="Playa abierta donde el perro puede bañarse al amanecer; el hotel-resort puede no admitirlo y a mediodía la arena quema.",
        visit={
            "why": "Es el descanso lógico tras el calor de Massawa y la base más cómoda antes de una salida a Dahlak.",
            "see": "Playa larga de arena clara, palmeras, barcas de pescadores y el horizonte del archipiélago.",
            "access": "Unos kilómetros al norte de Massawa por asfalto; misma zona de permiso que Massawa, así que el PERMISO DE VIAJE INTERIOR debe incluir Massawa y sus alrededores. Aparcamiento del resort suficiente para dos 4x4. El pin marca el Gurgusum Beach Resort, a pie de playa.",
            "when": "De noviembre a febrero; al amanecer o después de las 17:00, nunca a mediodía.",
            "skip": "Si se busca buceo o playa virgen: para eso está Dahlak, no Gurgusum.",
        },
        links=[
            {"label": "GetAMap · Gurgusum Bota (playa)", "url": "https://www.getamap.net/maps/eritrea/eritrea_(general)/_gurgusumbota/"},
            {"label": "Travel2Unlimited · Massawa – Gurgusum Beach", "url": "https://travel2unlimited.com/eritrea-massawa-gurgusum-beach/"},
            {"label": "Wikipedia · Massawa", "url": "https://en.wikipedia.org/wiki/Massawa"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/The_beach_at_Massawa_Eritrea_(30460971830).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:The_beach_at_Massawa_Eritrea_(30460971830).jpg",
                "credit": "Clay Gilliland from Chandler, U.S.A. · CC BY-SA 2.0",
                "caption": "La playa al norte de Massawa.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Massawa_Eritrea.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Massawa_Eritrea.jpg",
                "credit": "Clay Gilliland · CC BY-SA 2.0",
                "caption": "Un atardecer en la playa del mar Rojo.",
            },
        ],
    ),
    dict(
        n=16, name="Dankalia · la costa hacia el Danakil y las salinas", cat="Naturaleza", prio="Media",
        dog="prohibido", time="1–2 noches",
        lat=15.2636172, lon=39.620713,  # Google Maps: Foro
        desc="La antigua provincia de Dankalia, hoy repartida entre las regiones del mar Rojo Septentrional y Meridional, forma la mayor parte del desierto de Danakil: una franja de MÁS DE 500 KM DE LARGO Y APENAS 50 DE ANCHO entre el mar y el escarpe. Por ella baja la P-6, de grava, de Massawa a Assab. Advertencia: es el corredor de acceso a la frontera con Yibuti, desaconsejada por el FCDO en sus 25 km, y el permiso para recorrerla entera es muy improbable.",
        dog_note="Más de 500 km de desierto sin agua ni sombra, con temperaturas letales para un perro: no se lleva.",
        visit={
            "why": "Es uno de los desiertos costeros más extremos del planeta y la puerta eritrea de la depresión del Danakil.",
            "see": "Salinas, conos volcánicos, la península de Buri con sus coladas de lava y arrecifes y las aldeas afar de la costa.",
            "access": "P-6 de grava desde Massawa hacia Assab (13°00′28″N 42°44′28″E). PERMISO DE VIAJE INTERIOR OBLIGATORIO y, salvo el tramo norte hasta Foro y Zula, NO ESTÁ ENTRE LOS DESTINOS QUE LAS FUENTES DAN POR ABIERTOS. FCDO desaconseja todo viaje a 25 km de la frontera con Yibuti, y las islas Hanish están vetadas. Autonomía total de combustible y agua; sin talleres. El pin marca el golfo de Zula, arranque practicable del corredor.",
            "when": "De diciembre a enero, lo más frío del año, y nunca entre mayo y septiembre.",
            "skip": "Descártalo por defecto: es la zona donde más probable es que el permiso se deniegue y donde peor cubre cualquier seguro.",
        },
        links=[
            {"label": "Wikipedia · Southern Red Sea Region", "url": "https://en.wikipedia.org/wiki/Southern_Red_Sea_Region"},
            {"label": "Wikipedia · Assab", "url": "https://en.wikipedia.org/wiki/Assab"},
            {"label": "FCDO · Eritrea regional risks", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/regional-risks"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Foro_(8529062386).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Foro_(8529062386).jpg",
                "credit": "David Stanley from Nanaimo, Canada · CC BY 2.0",
                "caption": "Aldeanos en Foro.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Foro_Water_Reservoir.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Foro_Water_Reservoir.jpg",
                "credit": "Krokodilien71 · CC0",
                "caption": "El depósito de agua de Foro.",
            },
        ],
    ),
    dict(
        n=17, name="Mendefera y el altiplano del sur", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=14.8841369, lon=38.812898,  # Google Maps: Mendefera
        desc="Capital de la región de Debub, a 1.972 m y con unos 63.500 habitantes en 2012. El nombre significa «quien se atrevió» y alude a la colina que domina el centro. Alberga la escuela San Giorgio, de las más antiguas del país, y en sus alrededores se excavan desde 1959 tumbas aksumitas del siglo II a. C. con cerámica, joyas y brazaletes de bronce, además de edificios con cruces y MONEDAS ROMANAS Y LOCALES. Advertencia: exige permiso de viaje interior.",
        dog_note="Ciudad tranquila de altiplano donde pasear es fácil; escuelas, iglesias y yacimientos cerrados, no.",
        visit={
            "why": "Es la parada de servicios del altiplano sur y un yacimiento aksumita menos visitado que Qohaito.",
            "see": "La colina del centro, la escuela San Giorgio y las excavaciones aksumitas del entorno.",
            "access": "Asfalto desde Asmara por el altiplano, unos 55 km al sur. PERMISO DE VIAJE INTERIOR OBLIGATORIO; el yacimiento no está entre los destinos que las guías citan expresamente como abiertos, así que conviene incluirlo por nombre en la solicitud. Hay combustible, taller básico y alojamiento sencillo. El pin marca el centro de Mendefera.",
            "when": "De noviembre a febrero, de paso hacia Adi Keyh y Senafe.",
            "skip": "Si el día ya está lleno con Qohaito y Metera: Mendefera es una parada de apoyo, no un destino.",
        },
        links=[
            {"label": "Wikipedia · Mendefera", "url": "https://en.wikipedia.org/wiki/Mendefera"},
            {"label": "FCDO · Eritrea safety and security", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/safety-and-security"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mendefera_Market_(8351469299).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mendefera_Market_(8351469299).jpg",
                "credit": "David Stanley from Nanaimo, Canada · CC BY 2.0",
                "caption": "El mercado de Mendefera.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/St_George's_Orthodox_Church.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:St_George's_Orthodox_Church.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "La iglesia ortodoxa de San Jorge, sobre Mendefera.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mendefera_Bus_Station_(8351468499).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mendefera_Bus_Station_(8351468499).jpg",
                "credit": "David Stanley from Nanaimo, Canada · CC BY 2.0",
                "caption": "La estación de autobuses de Mendefera.",
            },
        ],
    ),
    dict(
        n=18, name="Barentu y el Gash-Barka · el oeste de las tierras bajas", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=15.1093615, lon=37.5895692,  # Google Maps: Barentu
        desc="Capital del Gash-Barka y antigua capital de la provincia de Gash-Setit, llamada así por los ríos Gash y Setit (Tekezé). Tenía 21.460 habitantes en 2001 y reúne a kunama, nara, tigré y tigriña. Los JUEVES Y SÁBADOS se llena de agricultores y pastores que traen sorgo, mijo, sésamo y ganado. Advertencia: el MAEC desaconseja expresamente Tesseney, Gash-Barka, Agordat y Barentu por la cercanía de la frontera sudanesa (28-02-2025).",
        dog_note="Mercado de ganado muy concurrido y calor de tierras bajas; el perro estorba y sufre.",
        visit={
            "why": "Es la ventana a la Eritrea kunama y a las tierras bajas del oeste, el país opuesto al del altiplano.",
            "see": "El mercado de jueves y sábado, la cultura kunama y el paisaje de sabana del valle del Gash.",
            "access": "P-2 asfaltada desde Asmara por Keren y Agordat (15°33′N 37°53′E). PERMISO DE VIAJE INTERIOR OBLIGATORIO y aquí es donde más probable es que lo denieguen: el MAEC desaconseja expresamente estas localidades y el FCDO veta los 25 km de frontera con Sudán, donde hay grupos armados y minas. El pin marca el mercado de Barentu.",
            "when": "Jueves o sábado de mercado, entre noviembre y febrero.",
            "skip": "Descártalo mientras el MAEC siga nombrando Barentu entre las zonas desaconsejadas.",
        },
        links=[
            {"label": "Wikipedia · Barentu, Eritrea", "url": "https://en.wikipedia.org/wiki/Barentu,_Eritrea"},
            {"label": "MAEC · Recomendaciones de viaje Eritrea", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Eritrea"},
            {"label": "FCDO · Eritrea regional risks", "url": "https://www.gov.uk/foreign-travel-advice/eritrea/regional-risks"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Gash_Barkahouses.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Gash_Barkahouses.jpg",
                "credit": "Blofeld of Spain · CC BY-SA 3.0",
                "caption": "Casas del Gash-Barka.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Esterh%C3%A1zy-Gal%C3%A1ntha_-_Flu%C3%9Fbett_des_Barka_bei_Einm%C3%BCndung_von_Chor_Mogareb.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Esterh%C3%A1zy-Gal%C3%A1ntha_-_Flu%C3%9Fbett_des_Barka_bei_Einm%C3%BCndung_von_Chor_Mogareb.jpg",
                "credit": "Michael Graf Esterházy-Galántha · Public domain",
                "caption": "El lecho del Barka (grabado histórico).",
            },
        ],
    ),
]

_CAT_COLOR = {"naturaleza": "verde", "ciudad · servicios": "azul", "cultura": "morado",
              "patrimonio unesco": "marron", "costa": "turquesa"}
for _p in POIS:
    # La portada de la tarjeta, el globo del mapa y el modal es siempre la primera foto de la galería.
    _p["img"] = _p["photos"][0]["img"]
    _p["source"] = _p["photos"][0]["source"]
    _p["credit"] = _p["photos"][0]["credit"]
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")

LOGISTICS = [
    ("Aeropuerto Internacional de Asmara (ASM)", "Frontera", 15.2936607, 38.9059886,  # Google Maps: Asmara International Airport
     "ÚNICA ENTRADA VIABLE al país. Vuelos con El Cairo, Estambul, Dubái, Yeda y Port Sudan. Terminal pequeña, pista de unos 3.000 m a 2.325 m de altitud. Hay que declarar todos los aparatos electrónicos al entrar; prohibido fotografiar el recinto. Pin comprobado en Google Maps («Asmara International Airport»)."),
    ("Puerto de Massawa", "Frontera", 15.6126427, 39.4796486,  # Google Maps: Puerto de Massawa
     "Puerto principal de Eritrea, a 115 km de Asmara. Salen ferris locales a las islas Dahlak y a Sheikh Said, siempre con permiso interior. Sin línea internacional de pasajeros documentada. Prohibido fotografiar el recinto portuario. Pin comprobado en Google Maps («Puerto de Massawa»)."),
    ("Paso fronterizo Serha – Zalambessa (Etiopía)", "Frontera", 14.5295692, 39.3854488,  # Google Maps: Zalambessa (lado etíope)
     "CERRADO. Reabierto el 11 de septiembre de 2018 y cerrado unilateralmente por Eritrea en diciembre de 2018. Zona minada y desaconsejada por el MAEC. Pin comprobado en Google Maps («Zalambessa (lado etíope)»)."),
    ("Teseney (paso hacia Kassala, Sudán)", "Frontera", 15.104832, 36.6592026,  # Google Maps: Teseney
     "CERRADO a extranjeros. Ciudad a 45 km de la frontera sudanesa, en la región de Gash-Barka. El MAEC señala Tesseney y toda Gash Barka como zona a evitar desde el conflicto sudanés de abril de 2023. Pin comprobado en Google Maps («Teseney»)."),
    ("Embajada de España en Jartum, desplazada temporalmente a El Cairo", "Consular", 30.0623764, 31.2225602,  # Google Maps: Embajada de España en El Cairo
     "COMPETENCIA CONSULAR para los españoles en Eritrea desde septiembre de 2023. Dirección: 41, Ismail Mohamed st., Zamalek, El Cairo. Teléfonos: +20 2 2735 6437 y +20 2 2735 5813. EMERGENCIA CONSULAR: +20 122 318 3783. Correos: emb.jartum@maec.es y emb.elcairo@maec.es. Pin comprobado en Google Maps («Embajada de España en El Cairo»)."),
    ("Ministerio de Turismo / Tourism Service Center, Asmara", "Consular", 15.3364254, 38.9386724,  # Google Maps: Harnet Avenue (Ministerio de Turismo; no figura como objeto)
     "DONDE SE PIDE EL PERMISO DE VIAJE INTERIOR. Tourism Service Center en Harnet Avenue, junto al Sweet Asmara Cafe, tel. +291 1 124 871; Ministerio de Turismo, tel. +291 1 154 100 y 154 111. Cerrado los domingos. Pin comprobado en Google Maps («Harnet Avenue (Ministerio de Turismo; no figura como objeto)»)."),
    ("Orotta National Referral Hospital, Asmara", "Hospital", 15.3348735, 38.9240727,  # Google Maps: Orotta Hospital
     "Hospital nacional de referencia de Eritrea, gestionado por el Ministerio de Sanidad, con servicio de urgencias. Medios muy por debajo del estándar europeo. COORDENADA APROXIMADA (centro de Asmara): verificar la ubicación exacta. Pin comprobado en Google Maps («Orotta Hospital»)."),
    ("Hanssenian National Referral Hospital, Asmara", "Hospital", 15.3119716, 38.9397603,  # Google Maps: Halibet Hospital
     "Segundo hospital nacional de referencia de la región central, gestionado por una ONG. En total el país tenía 22 hospitales en 2019. Cualquier caso grave exige evacuación a El Cairo, Dubái o Nairobi. COORDENADA APROXIMADA: verificar. Pin comprobado en Google Maps («Halibet Hospital»)."),
    ("Repostaje en Asmara (eje Asmara-Keren-Massawa)", "Combustible", 15.3317304, 38.9300394,  # Google Maps: Asmara (sin gasolinera concreta como objeto)
     "Las estaciones fiables están en Asmara y en el eje hacia Keren y Massawa. Pago solo en efectivo y en nakfa, cambiados en Himbol. Suministro irregular. Precio 2026 POR CONFIRMAR; último dato fiable, 1,33 USD/litro de gasóleo en 2016. Pin comprobado en Google Maps («Asmara (sin gasolinera concreta como objeto)»)."),
    ("Carga de agua en Asmara", "Agua potable", 15.3317304, 38.9300394,  # Google Maps: Asmara
     "Agua de red de Asmara, a 2.325 m: sirve para llenar depósitos de ducha y lavado con prefiltro, NO para beber sin tratar. Cortes frecuentes. Los hoteles del centro son el punto de carga más fiable del país. Pin comprobado en Google Maps («Asmara»)."),
    ("Carga de agua en Massawa", "Agua potable", 15.6080391, 39.4531069,  # Google Maps: Massawa
     "Último punto de carga antes de la costa sur. Agua salobre y escasa en toda la franja del mar Rojo, con 40-41 °C en junio y julio. Tratar siempre antes de beber y salir con depósitos llenos desde Asmara. Pin comprobado en Google Maps («Massawa»)."),
]

DRONE_CALLOUT = ("danger", "Dron fuera: ni lo metas en la maleta",
                 "Eritrea no ha publicado normativa de drones, y en un país donde está prohibido fotografiar cuarteles, puertos, puentes, aeropuertos y hasta personal uniformado ese vacío no es permiso: es discrecionalidad total del funcionario. UAV Coach documenta que unos confiscan el aparato y otros no, sin manera de saberlo hasta llegar, y el Departamento de Estado obliga a declarar todos los electrónicos a la entrada bajo pena de confiscación a la salida. Volar cerca de algo sensible puede leerse como espionaje: en un Estado con prensa clausurada desde 2001, eso no es una multa. Déjalo en España.")

STARLINK_CALLOUT = ("danger", "Starlink: no está y no se espera",
                    "Eritrea es el único país costero de África sin estación de amarre de cable submarino, y toda la conectividad pasa por EriTel, monopolio estatal sin proveedores privados. Starlink figura en los mapas de SpaceX sin fecha de lanzamiento prevista porque el Gobierno no ha concedido licencia, y la diáspora lleva años pidiéndolo sin éxito. Entrar con un terminal supone confiscación segura y riesgo de acusación de comunicación no autorizada. Cuenta con estar desconectado: la red móvil civil es 2G, no hay internet móvil, las SIM extranjeras no funcionan y hace falta VPN hasta para abrir el correo.")

DOG_MATRIX = [
    ("Entrada al país por el aeropuerto de Asmara", "por confirmar", "Sin normativa nacional localizada. Pedir por escrito los requisitos a la embajada eritrea de París o Bruselas antes de comprar billete; si no hay respuesta documentada, el perro no viaja."),
    ("Entrada por frontera terrestre", "prohibido", "No aplica: todos los pasos terrestres están cerrados a extranjeros. El perro se queda en el país base con uno de los tres viajeros."),
    ("Asmara y ciudades con permiso (Keren, Massawa, Dekemhare, Mendefera, Qohaito, Senafe, Foro)", "no recomendado", "Aun con permiso interior hay unos quince controles en 550 km, el permiso va ligado a la matrícula del coche y no hay infraestructura veterinaria fiable. Dejarlo fuera del país."),
    ("Zonas fronterizas y resto del país", "prohibido", "Vetadas a extranjeros por el Ministerio de Turismo y desaconsejadas por el MAEC por minas y conflicto. Ni con perro ni sin él."),
    ("Alojamientos y transporte local", "por confirmar", "No hay información sobre hoteles que admitan perros ni sobre transporte con animales, y a los extranjeros se les prohíbe el autobús interurbano. Reservar alojamiento pet-friendly en el país base durante el desvío."),
    ("Regreso a la UE desde Eritrea", "permitido con condiciones", "Tercer país no listado en el Reg. de Ejecución (UE) 2026/636: microchip, vacuna y titulación antirrábica ≥0,5 UI/ml. Hecha la serología en España ANTES de salir y anotada en el pasaporte, no hay espera de 90 días; hecha fuera, tres meses de bloqueo."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Eritrea (Ministerio de Asuntos Exteriores, UE y Cooperación, consultado el 18 de septiembre de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Eritrea"),
    ("MAEC · Ficha País de Eritrea, PDF (Oficina de Información Diplomática, datos de 2024-2025, consultado en septiembre de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/ERITREA_FICHA%20PAIS.pdf"),
    ("MAEC · Embajada de España en El Cairo: contacto y emergencia consular (consultado en septiembre de 2026)", "https://www.exteriores.gob.es/Embajadas/ElCairo/es/Paginas/index.aspx"),
    ("FCDO · Eritrea travel advice: Entry requirements (Foreign, Commonwealth & Development Office, consultado en septiembre de 2026)", "https://www.gov.uk/foreign-travel-advice/eritrea/entry-requirements"),
    ("FCDO · Eritrea travel advice: Safety and security (Foreign, Commonwealth & Development Office, consultado en septiembre de 2026)", "https://www.gov.uk/foreign-travel-advice/eritrea/safety-and-security"),
    ("Government of Canada · Travel advice and advisories for Eritrea (consultado en septiembre de 2026)", "https://travel.gc.ca/destinations/eritrea"),
    ("U.S. Department of State · Eritrea International Travel Information (consultado en septiembre de 2026)", "https://travel.state.gov/content/travel/en/international-travel/International-Travel-Country-Information-Pages/Eritrea.html"),
    ("NaTHNaC / TravelHealthPro · Eritrea country page (consultado en septiembre de 2026)", "https://travelhealthpro.org.uk/countries/eritrea"),
    ("MAPA · Viajar con la mascota: perros, gatos y hurones (Ministerio de Agricultura, Pesca y Alimentación, consultado en septiembre de 2026)", "https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones"),
    ("BOE / DOUE · Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía", "https://www.boe.es/doue/2026/636/L00001-00007.pdf"),
    ("EUR-Lex · Reglamento Delegado (UE) 2026/131 de la Comisión, de 20 de enero de 2026", "https://eur-lex.europa.eu/legal-content/ES/TXT/PDF/?uri=OJ%3AL_202600131"),
    ("Wikipedia · Visa policy of Eritrea (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Eritrea"),
    ("Wikipedia · Eritrea–Ethiopia border (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Eritrea%E2%80%93Ethiopia_border"),
    ("Wikipedia · Zalambessa (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Zalambessa"),
    ("Wikipedia · Teseney (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Teseney"),
    ("Wikipedia · Asmara (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Asmara"),
    ("Wikipedia · Asmara International Airport (datos de abril de 2026, consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Asmara_International_Airport"),
    ("Wikipedia · Massawa (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Massawa"),
    ("Wikipedia · Health in Eritrea (consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Health_in_Eritrea"),
    ("Young Pioneer Tours · Eritrea unilaterally closes land borders with Ethiopia (2019, consultado en septiembre de 2026)", "https://www.youngpioneertours.com/eritrea-closes-borders-ethiopia/"),
    ("Against the Compass · How to travel to Eritrea in 2026 (actualizado el 30 de agosto de 2026)", "https://againstthecompass.com/en/travel-eritrea/"),
    ("Wild Junket · Eritrea Travel: A Detailed Guide on Safety, Visa and Budget (Nellie Huang, consultado en septiembre de 2026)", "https://www.wildjunket.com/eritrea-travel/"),
    ("Rainer Mautz · Exploring Eritrea: A Week of Independent Travel (mautz.blog, viaje de 2024-2025)", "https://mautz.blog/exploring-eritrea-a-week-of-independent-travel/"),
    ("Horizons Unlimited · The HUBB: Overlanding Eritrea (hilo de 2018-2019, consultado en septiembre de 2026)", "https://www.horizonsunlimited.com/hubb/sub-saharan-africa/overlanding-eritrea-96469"),
    ("Tripadvisor · Border Sudan-Eritrea & Permit for regions about Asmara (foro de Eritrea, consultado en septiembre de 2026)", "https://www.tripadvisor.com/ShowTopic-g293788-i9762-k10118116-o10-Border_Sudan_Eritrea_Permit_for_regions_about_Asmara-Eritrea.html"),
    ("Ministerio de Turismo de Eritrea · Tourism Service Center, vía eritrea.be (consultado en septiembre de 2026)", "http://www.eritrea.be/MoT.htm"),
    ("UAV Coach · Drone Laws in Eritrea (actualizado el 9 de diciembre de 2022, consultado en septiembre de 2026)", "https://uavcoach.com/drone-laws-in-eritrea/"),
    ("TS2 Space · Eritrea's Digital Desert: Inside the World's Most Isolated Internet (publicado en junio de 2025, actualizado el 17 de septiembre de 2026)", "https://ts2.tech/en/eritreas-digital-desert-inside-the-worlds-most-isolated-internet-and-the-satellite-lifeline-on-the-horizon/"),
    ("Carnet de Passages en Douane · Ficha de Eritrea, AIT/FIA (consultado en septiembre de 2026)", "https://carnetdepassage.org/country/eritrea"),
    ("IndexMundi / GIZ · Eritrea, pump price for diesel fuel, US$ per litre (último dato: 2016)", "https://www.indexmundi.com/facts/eritrea/indicator/EP.PMP.DESL.CD"),
    ("OilPricez · Petroleum prices in Eritrea y tipo de cambio ERN (consultado el 19 de septiembre de 2026)", "https://oilpricez.com/er/eritrea-oil-price"),
    ("Visados.es · Embajadas y consulados de Eritrea para residentes en España (consultado en septiembre de 2026)", "https://www.visados.es/Paises/Eritrea-28/Embajadas.html"),
    ("UNESCO · Asmara: A Modernist African City (1550)", "https://whc.unesco.org/en/list/1550/"),
    ("Wikipedia · Cinema Impero", "https://en.wikipedia.org/wiki/Cinema_Impero"),
    ("Cinema Treasures · Cinema Impero, Asmara", "https://cinematreasures.org/theaters/7910"),
    ("Wikipedia · Fiat Tagliero Building", "https://en.wikipedia.org/wiki/Fiat_Tagliero_Building"),
    ("Atlas Obscura · Fiat Tagliero Service Station", "https://www.atlasobscura.com/places/fiat-tagliero-service-station-asmara-eritrea"),
    ("Atlas Obscura · Medeber Market", "https://www.atlasobscura.com/places/medeber-market"),
    ("Wikipedia · Dahlak Archipelago", "https://en.wikipedia.org/wiki/Dahlak_Archipelago"),
    ("Wikipedia · Dahlak Kebir", "https://en.wikipedia.org/wiki/Dahlak_Kebir"),
    ("FCDO · Eritrea regional risks", "https://www.gov.uk/foreign-travel-advice/eritrea/regional-risks"),
    ("Wikipedia · Eritrean Railway", "https://en.wikipedia.org/wiki/Eritrean_Railway"),
    ("Adulis Travel · The Eritrean Railway", "https://adulistravel.com/the-eritrean-railway/"),
    ("Wikipedia · Nefasit", "https://en.wikipedia.org/wiki/Nefasit"),
    ("Wikipedia · Semenawi Bahri National Park", "https://en.wikipedia.org/wiki/Semenawi_Bahri_National_Park"),
    ("Visit Eritrea · Filfil Solomuna", "https://www.visiteritrea.net/filfil-solomuna"),
    ("Wikipedia · Debre Bizen", "https://en.wikipedia.org/wiki/Debre_Bizen"),
    ("Wikipedia · Keren, Eritrea", "https://en.wikipedia.org/wiki/Keren,_Eritrea"),
    ("Wikipedia · Nakfa, Eritrea", "https://en.wikipedia.org/wiki/Nakfa,_Eritrea"),
    ("Wikipedia · Qohaito", "https://en.wikipedia.org/wiki/Qohaito"),
    ("Wikipedia · Adi Keyh", "https://en.wikipedia.org/wiki/Adi_Keyh"),
    ("Wikipedia · Matara, Eritrea", "https://en.wikipedia.org/wiki/Matara,_Eritrea"),
    ("Wikipedia · Senafe", "https://en.wikipedia.org/wiki/Senafe"),
    ("Wikipedia · Adulis", "https://en.wikipedia.org/wiki/Adulis"),
    ("Wikipedia · Gulf of Zula", "https://en.wikipedia.org/wiki/Gulf_of_Zula"),
    ("GetAMap · Gurgusum Bota (playa)", "https://www.getamap.net/maps/eritrea/eritrea_(general)/_gurgusumbota/"),
    ("Travel2Unlimited · Massawa – Gurgusum Beach", "https://travel2unlimited.com/eritrea-massawa-gurgusum-beach/"),
    ("Wikipedia · Southern Red Sea Region", "https://en.wikipedia.org/wiki/Southern_Red_Sea_Region"),
    ("Wikipedia · Assab", "https://en.wikipedia.org/wiki/Assab"),
    ("Wikipedia · Mendefera", "https://en.wikipedia.org/wiki/Mendefera"),
    ("Wikipedia · Barentu, Eritrea", "https://en.wikipedia.org/wiki/Barentu,_Eritrea"),
]

# Bucle del escarpe y el mar Rojo: Asmara – Massawa – Dahlak – Zula – altiplano sur
CORRIDOR = [
    (15.33676, 38.94023),
    (15.33051, 39.06399),
    (15.60804, 39.45311),
    (15.65696, 39.46894),
    (15.833, 40.2),
    (15.60804, 39.45311),
    (15.2636, 39.6606),
    (15.067, 39.033),
    (14.87089, 39.4168),
    (14.7, 39.41667),
    (14.67472, 39.42472),
    (14.88414, 38.8129),
    (15.33676, 38.94023),
]

# Bucle oeste y norte: Asmara – Filfil – Keren – Agordat – Barentu – Nakfa (solo con permiso; zonas desaconsejadas)
CORRIDOR_ALT = [
    (15.33676, 38.94023),
    (15.61667, 38.96667),
    (15.78015, 38.45245),
    (15.55, 37.88333),
    (15.10936, 37.58957),
    (15.55, 37.88333),
    (15.78015, 38.45245),
    (16.66639, 38.47651),
    (15.33676, 38.94023),
]

HISTORIA_RESUMEN = "Eritrea es un país del Cuerno de África nacido de la guerra más larga del continente. Colonia italiana entre 1890 y 1941, administrada después por los británicos y federada con Etiopía en 1952, vio anulada esa federación en 1962 y libró treinta años de guerra hasta entrar en Asmara en mayo de 1991. El referéndum de abril de 1993 selló la independencia con un 99,83 % de votos a favor, y desde entonces gobierna el mismo hombre, Isaias Afewerki, sin elecciones ni constitución en vigor. La guerra de 1998-2000 con Etiopía y la clausura de la prensa en 2001 consolidaron un Estado militarizado que Freedom House puntúa con 3 sobre 100 y Reporteros Sin Fronteras sitúa el último del mundo."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>El territorio que hoy ocupa Eritrea forma parte de uno de los corredores más antiguos de intercambio entre África y la península arábiga. Entre los siglos I y II de nuestra era floreció allí el <strong>reino de Aksum</strong>, que adoptó el cristianismo poco después de su fundación y convirtió el puerto de Adulis, en la costa del mar Rojo, en una de las grandes escalas comerciales de la Antigüedad tardía. La Enciclopedia Británica sitúa esta región dentro del núcleo aksumita, del que procede la matriz cultural y religiosa que todavía comparten las tierras altas eritreas y el norte de Etiopía.</p><p>Tras la decadencia de Aksum, las mesetas quedaron organizadas en entidades propias. La Wikipedia en español menciona el reino de <em>Medri Bahri</em> —literalmente «tierra del mar»— y la república campesina de Hamasien como las formaciones que articularon las tierras altas durante el periodo medieval. La franja costera siguió otro camino: en el siglo XVI los <strong>otomanos</strong> conquistaron partes del litoral eritreo y establecieron su autoridad sobre Massawa, y en el siglo XIX fue <strong>Egipto</strong> quien invadió y administró esas mismas zonas. De esa doble herencia —cristiana y de montaña en el interior, musulmana y de puerto en la costa— procede la división que ha marcado la historia moderna del país.</p>"),
    ("Colonización",
     "<p>La colonización eritrea fue obra de <strong>Italia</strong>, que llegó tarde al reparto africano y buscó en el mar Rojo su puerta de entrada. Según la Wikipedia en español, Italia tomó posesión de <strong>Assab en 1882</strong> —oficialmente el 5 de julio— y ocupó <strong>Massawa en 1885</strong>, tras la retirada egipcia. En <strong>1890</strong> declaró formalmente Eritrea colonia suya, fecha que también recoge la Británica. La expansión hacia el interior chocó con el Imperio etíope y se detuvo en seco en la <strong>batalla de Adua (1896)</strong>, después de la cual Italia reconoció la independencia etíope en el Tratado de Paz de Addis Abeba y se conformó con consolidar la colonia.</p><p>Lo que Italia dejó fue, sobre todo, infraestructura y ciudad. El <strong>ferrocarril de vía estrecha</strong> de 950 milímetros se construyó entre 1887 y 1932: arrancó en Massawa, alcanzó Asmara en 1911 y llegó a sumar 337 kilómetros, con 65 puentes y 39 túneles en el solo tramo de la costa a la capital. Asmara se reconstruyó como escaparate del racionalismo italiano entre 1893 y 1941. La aventura colonial se amplió con la guerra de 1935-1936 y el África Oriental Italiana, y terminó en <strong>1941</strong>, cuando el Imperio británico conquistó el territorio y lo administró durante la década siguiente.</p>"),
    ("Independencia y construcción del Estado",
     "<p>La suerte de Eritrea se decidió en Naciones Unidas. La <strong>Resolución 390A</strong> de la Asamblea General, de 2 de diciembre de 1950, estableció una <strong>federación con Etiopía</strong> que entró en vigor en <strong>1952</strong>. Casi de inmediato, según la Wikipedia en inglés, los derechos reconocidos a Eritrea empezaron a recortarse o vulnerarse, hasta que en <strong>1962</strong> el emperador Haile Selassie disolvió unilateralmente el parlamento eritreo y anexionó el territorio como una provincia más.</p><p>La respuesta fue la lucha armada. El <strong>Frente de Liberación Eritreo</strong> inició las operaciones militares en <strong>1961</strong>, y el <strong>Frente Popular de Liberación de Eritrea</strong>, fundado en 1972, acabó imponiéndose como fuerza dominante. Fueron <strong>treinta años de guerra</strong> contra el régimen imperial primero y contra la junta militar del Derg después; la retirada del apoyo soviético a Etiopía a finales de los ochenta inclinó la balanza. Los combatientes entraron en <strong>Asmara el 24 de mayo de 1991</strong>.</p><p>El <strong>referéndum</strong> supervisado internacionalmente se celebró del <strong>23 al 25 de abril de 1993</strong> y arrojó un <strong>99,83 % a favor de la independencia</strong>, proclamada el 24 de mayo de ese año con <strong>Isaias Afewerki</strong> como presidente. España estableció relaciones diplomáticas con el nuevo Estado el 5 de octubre de 1993. En <strong>mayo de 1997</strong> se aprobó una constitución que, según la ficha del Ministerio de Asuntos Exteriores español, <em>todavía no ha entrado en vigor</em>.</p>"),
    ("Historia reciente (2000-2026)",
     "<p>La década de los noventa terminó en guerra. El conflicto fronterizo de <strong>1998-2000</strong> con Etiopía, desencadenado por la localidad de <strong>Badme</strong>, se cerró con el <strong>Acuerdo de Argel</strong> de diciembre de 2000 y una misión de paz de Naciones Unidas. Una comisión internacional delimitó la frontera en 2002, pero, según la ficha del Ministerio de Asuntos Exteriores (enero de 2026), Etiopía siguió ocupando Badme y ese contencioso <em>continúa siendo uno de los obstáculos para normalizar las relaciones</em>.</p><p>Hacia dentro, el giro llegó en <strong>septiembre de 2001</strong>: la detención del grupo reformista conocido como G-15 fue acompañada del <strong>cierre de todos los medios independientes</strong>. Reporteros Sin Fronteras data ahí «la transición a la dictadura» y recuerda que el periodista sueco-eritreo <strong>Dawit Isaak</strong> sigue incomunicado desde entonces, sin juicio. Las elecciones previstas para diciembre de 2001 se aplazaron sin fecha. El <strong>servicio nacional</strong>, legalmente de dieciocho meses, se volvió indefinido: Human Rights Watch afirma que la mayoría sirve años, y algunos décadas.</p><p>El <strong>9 de julio de 2018</strong>, tras la cumbre de Abiy Ahmed en Asmara, ambos países firmaron una declaración conjunta de paz. El deshielo duró poco: desde <strong>noviembre de 2020</strong> las fuerzas eritreas combatieron en la <strong>guerra de Tigray</strong> —se las acusa de la matanza de Axum de finales de ese mes—, no fueron parte del acuerdo de Pretoria de noviembre de 2022 y siguieron ocupando zonas del norte etíope.</p>"),
    ("Política y gobierno en 2026",
     "<p>A fecha de septiembre de 2026, y según la ficha país del Ministerio de Asuntos Exteriores español (enero de 2026), el jefe de Estado y de Gobierno es <strong>Isaias Afewerki</strong>, nacido en 1946, presidente <strong>desde 1993</strong>; llegó al poder al frente del movimiento independentista que derrotó a Etiopía en 1991, no mediante elecciones. Eritrea es formalmente una república unitaria de seis regiones, pero en la práctica funciona como un <strong>régimen autoritario de partido único</strong>: el Frente Popular para la Democracia y la Justicia es <em>el único partido legal</em>, la constitución de 1997 nunca entró en vigor, la asamblea de 150 diputados la componen solo miembros del partido y las elecciones de diciembre de 2001 se aplazaron sin fecha. Human Rights Watch añade que el legislativo no se reúne desde 2010.</p><p>No es, por tanto, una democracia ni una democracia limitada. <strong>Freedom House</strong>, en <em>Freedom in the World 2025</em>, lo clasifica como <strong>«Not Free»</strong> con <strong>3 puntos sobre 100</strong> —1 sobre 40 en derechos políticos y 2 sobre 60 en libertades civiles— y lo describe como «un Estado autoritario militarizado que no ha celebrado elecciones nacionales desde la independencia». <strong>Reporteros Sin Fronteras</strong> lo sitúa en el <strong>puesto 180 de 180</strong> de su índice de 2025, con 11,32 puntos y catorce periodistas y trabajadores de medios detenidos. Con España las relaciones son buenas pero de perfil modesto, con embajador residente en Jartum.</p>"),
    ("Economía y recursos",
     "<p>La economía eritrea descansa en tres patas desiguales: la minería, la agricultura de subsistencia y el dinero que llega de fuera. Según la ficha del Ministerio de Asuntos Exteriores (enero de 2026), las principales exportaciones de 2021 fueron <strong>zinc (39,9 %), cobre (31,3 %) y oro (27 %)</strong>, es decir, prácticamente todo mineral. La agricultura, en cambio, ocupa al <strong>80 % de la población activa</strong> pero solo aportaba el 12,1 % del producto interior bruto en 2017, frente al 29,5 % de la industria y el 58,5 % de los servicios. La pesca y los puertos de Massawa y Assab completan el cuadro.</p><p>La <strong>moneda</strong> es el <strong>nakfa</strong> (ERN); el mismo documento daba un cambio de 1 euro por 17,06 nakfas en abril de 2025. Las tarjetas de crédito extranjeras no se aceptan en ningún punto del país. La dependencia exterior es estructural: el Ministerio cifra las <strong>remesas de la diáspora en torno al 30 % del producto interior bruto</strong>, una proporción altísima que se explica por el éxodo de población. El Banco Mundial refleja la opacidad estadística del país: su último dato completo de renta per cápita es de 2011, unos <strong>690 dólares</strong>, y muchos indicadores figuran sin datos. El acceso a la electricidad era del 55,3 % en 2024 y los usuarios de internet, del 14 % en 2020.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Sin censo, las cifras bailan: el Ministerio de Asuntos Exteriores da <strong>3,5 millones</strong> de habitantes (2024) y el Banco Mundial 3,6 millones (2025). Asmara ronda los 713.000. El Ministerio señala como <strong>idiomas oficiales el tigriña, el árabe y el inglés</strong>; la Wikipedia en inglés matiza que hay <strong>nueve lenguas nacionales</strong> en pie de igualdad y que esos tres son lenguas de trabajo de hecho. El tigriña sirve en las tierras altas y el árabe en la costa.</p><p>En religión las fuentes divergen: el Ministerio da aproximadamente un <strong>45 % de cristianos coptos, un 45 % de musulmanes y un 10 % de creencias tradicionales</strong>, y la Wikipedia en español un 62,9 % de ortodoxos y un 36,2 % de suníes. Dos tercios de la población son tigriña y tigré. Se come <em>injera</em> de teff con guisos de <em>berbere</em> y la ceremonia del café es un ritual social. Asmara es <strong>Patrimonio de la Humanidad desde 2017</strong> por su urbanismo modernista, y el ferrocarril hasta Massawa aún mueve locomotoras de vapor de los años treinta.</p><p>Conviene vestir con discreción, hombros y rodillas cubiertos, en iglesias y mezquitas por igual. <strong>Está prohibido fotografiar instalaciones militares, puentes, puertos y edificios oficiales</strong>. En ramadán —que en 2027 empieza en torno al 8 de febrero— es cortés no comer ni beber en público de día en zonas musulmanas; el alcohol es normal en las tierras altas cristianas.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Eritrea (Ministerio de Asuntos Exteriores, España · PDF · enero de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/ERITREA_FICHA%20PAIS.pdf"),
    ("Eritrea: Freedom in the World 2025 (Freedom House · informe de país · 2025)", "https://freedomhouse.org/country/eritrea/freedom-world/2025"),
    ("Eritrea · Índice Mundial de la Libertad de Prensa (Reporteros Sin Fronteras · ficha de país · 2025)", "https://rsf.org/en/country/eritrea"),
    ("Eritrea: History (Encyclopaedia Britannica · consultada en septiembre de 2026)", "https://www.britannica.com/place/Eritrea/History"),
    ("Eritrea (Wikipedia en español · consultada en septiembre de 2026)", "https://es.wikipedia.org/wiki/Eritrea"),
    ("Eritrea (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Eritrea"),
    ("History of Eritrea (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/History_of_Eritrea"),
    ("Eritrea–Ethiopia relations (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Eritrea%E2%80%93Ethiopia_relations"),
    ("Tigray War (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Tigray_war"),
    ("Eritrean Railway (Wikipedia en inglés · consultada en septiembre de 2026)", "https://en.wikipedia.org/wiki/Eritrean_Railway"),
    ("Gastronomía de Eritrea (Wikipedia en español · consultada en septiembre de 2026)", "https://es.wikipedia.org/wiki/Gastronom%C3%ADa_de_Eritrea"),
    ("Eritrea · Estado parte de la Convención del Patrimonio Mundial (UNESCO · consultada en septiembre de 2026)", "https://whc.unesco.org/en/statesparties/er"),
    ("Asmara: A Modernist African City (UNESCO · Lista del Patrimonio Mundial · inscrita en 2017)", "https://whc.unesco.org/en/list/1550/"),
    ("Eritrea · World Report 2025 (Human Rights Watch · 2025)", "https://www.hrw.org/world-report/2025/country-chapters/eritrea"),
    ("Eritrea · Datos (Banco Mundial · consultada en septiembre de 2026)", "https://data.worldbank.org/country/eritrea"),
    ("Recomendaciones de viaje: Eritrea (Ministerio de Asuntos Exteriores, España · consultada en septiembre de 2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Eritrea"),
]

SPEC = dict(
    slug="eritrea", name="Eritrea", revision="18 sep 2026",
    sub="FUERA DE RUTA — país cerrado, solo se entra en avión · Asmara Patrimonio Mundial y permiso interior obligatorio",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. Todas las fronteras terrestres cerradas y el MAEC desaconseja el viaje…"),
        ("CÓMO LLEGAR", "SOLO EN AVIÓN, al Aeropuerto Internacional de Asmara (ASM)…"),
        ("VISADO", "OBLIGATORIO y previo. No hay embajada de Eritrea en España: el embajador reside en París y…"),
        ("VEHÍCULO", "INVIABLE con vehículo propio: no hay paso terrestre abierto…"),
        ("SEGURIDAD", "MAEC desaconseja el viaje · minas en fronteras"),
        ("SEGURO", "Carta Verde NO válida · seguro local por confirmar"),
        ("SALUD", "Fiebre amarilla solo si llegas de zona de riesgo"),
        ("DRONES", "Sin ley publicada · confiscación en aduana"),
        ("STARLINK", "No disponible · sin licencia · solo 2G"),
        ("4x4", "Inviable: fronteras cerradas · coche con conductor"),
        ("A PIE", "Prohibido moverse entre ciudades a pie"),
        ("PERRO", "Sin normativa nacional de importación localizable en fuente oficial…"),
        ("MONEDA", "Nakfa (ERN). 1 USD = 15 ERN (MAEC, febrero de 2025) y 1 EUR = 17,06 ERN (Ficha País del…"),
        ("VENTANA", "Asmara a 2.325 m: templado y seco, unos 23 °C de día y 6 °C de noche entre noviembre y…"),
    ],
    center=[15.59, 38.89], zoom=7,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle del escarpe y el mar Rojo: Asmara – Massawa – Dahlak – Zula – altiplano sur",
    corridor_alt_label="Bucle oeste y norte: Asmara – Filfil – Keren – Agordat – Barentu – Nakfa (solo con permiso; zonas desaconsejadas)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Fiat_Tagliero_Building.jpg?width=1200",
    hero_credit="La estación Fiat Tagliero · David Stanley · CC BY 2.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Eritrea queda fuera de la ruta de 2027 por una razón sencilla y comprobable: no se puede entrar con vehículo propio. Las tres fronteras terrestres con Etiopía que se abrieron tras el acuerdo de paz de 2018 las volvió a cerrar Asmara unilateralmente entre diciembre de 2018 y abril de 2019 —Serha-Zalambessa, Om Hajer-Humera y Bure-Assab—, y el MAEC, el Gobierno de Canadá, el Departamento de Estado y las guías de viaje actualizadas en agosto de 2026 siguen dando por cerrados todos los pasos terrestres con Sudán, Etiopía y Yibuti. Aunque se abriera un paso, seguiría haciendo falta un PERMISO DE VIAJE INTERIOR para alejarse más de 25 km de Asmara: se tramita en el Ministerio de Turismo, cuesta unos 10 dólares por destino y solo cubre Keren, Massawa, Dekemhare, Mendefera, Qohaito, Senafe y Foro, con la matrícula del vehículo anotada. La alternativa realista es un viaje aparte y en avión: vuelo a Asmara vía El Cairo, Estambul o Dubái, visado tramitado con más de un mes de antelación en la embajada eritrea de París o Bruselas —o visado a la llegada por 70 dólares con carta de invitación de un operador local—, y conductor con coche, unos 150 dólares al día. Siete a diez días salen por del orden de 1.500-2.000 € por persona. Habría que decidir quién hace ese desvío mientras los vehículos y el perro esperan fuera.",
    facts=[
        ("Estatus", "FUERA DE RUTA. Todas las fronteras terrestres cerradas y el MAEC desaconseja el viaje. Ficha informativa, no operativa."),
        ("Cómo llegar", "SOLO EN AVIÓN, al Aeropuerto Internacional de Asmara (ASM). Vuelan EgyptAir (El Cairo), Turkish (Estambul), flydubai (Dubái), flynas (Yeda) y Tarco (Port Sudan); Etihad anuncia Abu Dabi desde noviembre de 2026."),
        ("Visado", "OBLIGATORIO y previo. No hay embajada de Eritrea en España: el embajador reside en París y también atiende Bruselas. Tramitación de más de un mes; alternativa de visado a la llegada con carta de invitación de operador local (70 USD)."),
        ("Vehículo/aduana", "INVIABLE con vehículo propio: no hay paso terrestre abierto. AIT/FIA no tiene organización emisora de CPD en el país. Se conduce por la derecha y hace falta permiso internacional de 1949 más licencia local."),
        ("Seguro", "La Carta Verde NO cubre Eritrea. El país no está en Carte Brune CEDEAO ni en Carte Rose CEMAC; la COMESA Yellow Card para vehículos extranjeros está por confirmar."),
        ("Moneda", "Nakfa (ERN). 1 USD = 15 ERN (MAEC, febrero de 2025) y 1 EUR = 17,06 ERN (Ficha País del MAEC, abril de 2025). Economía de efectivo: no hay cajeros ni se aceptan tarjetas. Cambio solo en Himbol. Declarar más de 10.000 USD y sacar como máximo 1.000 ERN."),
        ("Perro", "Sin normativa nacional de importación localizable en fuente oficial. Con las fronteras cerradas y acceso solo aéreo, el perro NO entra en el plan."),
        ("Drones", "NO LLEVAR. No hay normativa publicada, la aduana confisca de forma imprevisible, todos los aparatos electrónicos deben declararse al entrar y está prohibido fotografiar instalaciones militares, puertos, puentes y edificios oficiales."),
        ("Starlink", "NO DISPONIBLE. Sin licencia en Eritrea; EriTel es monopolio estatal, la red móvil civil es solo 2G y no hay internet móvil. VPN imprescindible para cualquier conexión."),
        ("Seguridad", "Delincuencia común muy baja —Asmara se camina de noche— pero riesgo terrorista medio según el MAEC, minas sin retirar en zonas fronterizas y control policial permanente con puestos de control."),
        ("Clima", "Asmara a 2.325 m: templado y seco, unos 23 °C de día y 6 °C de noche entre noviembre y febrero, con lluvias en julio y agosto. Massawa, en la costa, ronda los 30 °C de media anual y 40-41 °C en junio-julio."),
        ("Sanidad", "22 hospitales en todo el país (2019) y medios muy por debajo del estándar europeo. Seguro con evacuación imprescindible. Paludismo por debajo de 2.200 m; Asmara está libre."),
    ],
    alerts=[
        "El MAEC DESACONSEJA EL VIAJE a Eritrea y, si aun así se viaja, pide evitar las zonas fronterizas con Sudán, Etiopía y Yibuti (recomendación consultada el 18 de septiembre de 2026).",
        "TODAS LAS FRONTERAS TERRESTRES ESTÁN CERRADAS a turistas: el MAEC lo indica expresamente, el Gobierno de Canadá da por cerrados los pasos con Etiopía y Yibuti y el Departamento de Estado confirma que los extranjeros no pueden siquiera acercarse a la frontera con Yibuti.",
        "PERMISO DE VIAJE INTERIOR OBLIGATORIO para alejarse más de 25 km de Asmara, incluso para el personal diplomático. Se tramita en el Ministerio de Turismo y, según el FCDO, tarda varios días y no siempre se concede.",
        "EL PERMISO NO CUBRE TODO EL PAÍS: solo Keren, Massawa, Dekemhare, Mendefera, Qohaito, Senafe y Foro. El resto de Eritrea está vetado a extranjeros, empezando por toda la franja fronteriza.",
        "EL PERMISO EXIGE AHORA LA MATRÍCULA del vehículo en el que se viajará y las fechas exactas de cada destino (Against the Compass, actualizado el 30 de agosto de 2026): no se puede improvisar ruta.",
        "PROHIBIDO FOTOGRAFIAR instalaciones militares, aeropuertos, puertos, puentes, edificios oficiales y personal uniformado. El Departamento de Estado avisa de que el riesgo es confiscación, detención o interrogatorio, no una multa.",
        "HAY QUE DECLARAR TODOS LOS APARATOS ELECTRÓNICOS al entrar o pueden ser confiscados a la salida (Departamento de Estado de EE. UU.). Un dron declarado es un dron que se queda en la aduana.",
        "MINAS ANTIPERSONA sin retirar en las zonas fronterizas y desminado incompleto: no salir de las carreteras principales ni conducir de noche (MAEC).",
        "SIN DINERO ELECTRÓNICO: no hay cajeros ni se aceptan tarjetas en ningún sitio. Todo el viaje se paga en efectivo y el cambio solo es legal en las oficinas estatales Himbol.",
        "Los españoles no tienen embajada en Asmara: la competencia consular la tiene la Embajada de España en Jartum, desplazada temporalmente a El Cairo desde septiembre de 2023. Solo hay dos residentes españoles en el país.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Asmara y permisos", "Llegada por aire a Asmara; trámite del permiso de viaje interior en el Ministerio de Turismo (Harnet Avenue, frente a la catedral); ciudad UNESCO a pie", "0 km · 2 días"),
        ("2 · Asmara modernista", "Harnet Avenue, Cinema Impero, Fiat Tagliero, mercado de Medeber y tren de vapor chárter hacia Arbaroba", "~40 km · 1 día"),
        ("3 · Asmara → Nefasit → Debre Bizen", "P-1 por el escarpe hasta Nefasit y subida a pie al monasterio", "~25 km + subida · 1 día"),
        ("4 · Nefasit → Ghinda → Massawa", "Descenso de 2.300 m por la P-1 hasta el mar Rojo; ciudad vieja de Batse", "~90 km · 1 día"),
        ("5 · Massawa → Gurgusum → Dahlak", "Playa de Gurgusum y salida en barco al archipiélago desde el puerto de Massawa", "~15 km + barco · 2 días"),
        ("6 · Massawa → Foro/Zula → Adulis", "P-6 sur hasta el golfo de Zula y yacimiento de Adulis; regreso a Massawa", "~90 km · 1 día"),
        ("7 · Massawa → Asmara", "Subida de vuelta por la P-1 con parada fotográfica fuera de puentes y puerto", "~115 km · 1 día"),
        ("8 · Asmara → Filfil Solomuna → Asmara", "Carretera de Keren, desvío en Serejeka y descenso al bosque nuboso de Semienawi Bahri", "~160 km · 1 día"),
        ("9 · Asmara → Keren", "P-2 al noroeste; llegada la víspera del mercado del lunes", "~90 km · 1 día"),
        ("10 · Keren → Agordat → Barentu", "Tierras bajas del Gash-Barka (zona desaconsejada por el MAEC; solo si el permiso lo cubre)", "~150 km · 1 día"),
        ("11 · Barentu → Agordat → Keren → Asmara", "Regreso por la P-2 al altiplano", "~240 km · 1 día"),
        ("12 · Asmara → Dekemhare → Adi Keyh → Qohaito", "Altiplano sur hasta el borde del Rift y el yacimiento de Qohaito", "~110 km · 1 día"),
        ("13 · Qohaito → Senafe → Metera", "Estelas de Metera y regreso al eje sur (no acercarse a 25 km de la frontera etíope)", "~35 km · 1 día"),
        ("14 · Metera → Mendefera → Asmara", "Cierre del bucle por el altiplano y salida por el aeropuerto de Asmara", "~135 km · 1 día"),
    ],
    offroad=[
        "La red viaria eritrea es corta y mayoritariamente de tierra: 4.010 km totales, de los que solo 874 km están asfaltados y 3.136 km sin asfaltar, con clasificación primaria (asfalto), secundaria (asfalto de una capa) y terciaria (tierra mejorada) según la ficha de transporte de Wikipedia.",
        "El único gran eje asfaltado es la P-1 Asmara-Massawa, que baja 2.300 m por el escarpe en unos 115 km: no es off-road, pero sí conducción técnica de montaña con curvas cerradas, camiones y niebla, y conviene hacerla de día.",
        "La P-6 de Massawa a Assab es de GRAVA a lo largo de más de 500 km de desierto costero sin servicios: es la única pista larga de verdad del país y exige autonomía total de combustible, agua y repuestos; además es la zona donde el permiso de viaje interior tiene menos probabilidades de concederse.",
        "El descenso a Filfil Solomuna por Serejeka, Moguo, Sabur y Fagiena se ha asfaltado de nuevo (Visit Eritrea), así que ya no es una pista, pero sigue siendo un tramo de montaña de 77 km con humedad y niebla en verano.",
        "Las pistas del macizo de Sahel hacia Nakfa y las del Gash-Barka hacia Barentu y Tesseney son las únicas rutas 4x4 de largo recorrido que quedan, y ambas están en zonas que el MAEC desaconseja expresamente y el FCDO veta a menos de 25 km de frontera.",
        "Cualquier salida fuera de la provincia de Asmara exige PERMISO DE VIAJE INTERIOR con la matrícula del vehículo declarada y fechas exactas por destino; hay controles de carretera que lo comprueban y el FCDO advierte de que las solicitudes «no siempre prosperan» (27-07-2026).",
        "Canadá recomienda mantenerse en las carreteras asfaltadas y no entrar en campos ni zonas rurales por las MINAS SIN SEÑALIZAR de las áreas fronterizas, lo que en la práctica elimina el off-road libre en Sahel, Gash-Barka y la franja de Yibuti (09-09-2026).",
        "Alquilar vehículo en Asmara es posible pero casi siempre con conductor, desde unos 100-150 USD al día (Against the Compass), lo que indica que la conducción autónoma de extranjeros es excepcional aun con permiso: dar por hecho que los dos 4x4 propios necesitarían trámite adicional, POR CONFIRMAR.",
    ],
    senderismo=[
        "Subida a Debre Bizen desde Nefasit (1.700 m) hasta el monasterio a 2.460 m: varias horas de vereda empinada por el escarpe, la caminata clásica del país; acceso restringido a varones, por confirmar con la comunidad.",
        "Recorrido a pie de la Asmara modernista: Harnet Avenue, catedral católica, Cinema Impero, Fiat Tagliero y barrio de villas, unas tres horas sin desnivel, sin permiso especial.",
        "Paseo al pueblo de Tselot, a las afueras de Asmara, que según Wild Junket es el único destino de los alrededores que NO exige permiso de viaje interior.",
        "Borde del cañón de Qohaito, a más de 2.500 m: recorrido corto entre el templo de Mariam Wakino, la presa de Safira y el barranco con tumbas y pinturas rupestres de camellos y vacas; sin barandillas.",
        "Senderos de observación de aves en Semienawi Bahri, entre los centros recreativos de Meguo, Medhanit y Sabur, con pozas y bosque siempreverde entre 900 y 2.400 m.",
        "Vuelta a Metera y Senafe a pie desde la carretera del sur: yacimiento llano de dos ciudades superpuestas en torno al obelisco Hawulti.",
        "Paseo por la isla de Batse en Massawa entre el Palacio Imperial, la mezquita de Sheikh Hanafi y las ruinas de 1990, mejor al amanecer por el calor y SIN FOTOGRAFIAR el puerto.",
        "Trincheras y túneles de Nakfa: recorrido guiado obligatorio y estrictamente sobre sendero marcado por el riesgo de minas; solo si el permiso nombra Nakfa.",
    ],
    acampada=[
        "No se ha encontrado NINGÚN camping formal en Eritrea en las fuentes consultadas: ni Against the Compass ni Wild Junket mencionan campings, y ambas guías organizan el viaje en hoteles.",
        "La acampada libre choca de frente con el sistema de permisos: el permiso de viaje interior obliga a declarar las fechas exactas de estancia en cada lugar, de modo que dormir donde surja es incompatible con lo que se ha autorizado.",
        "No se ha podido consultar iOverlander ni Tracks4Africa para Eritrea en esta sesión: queda POR CONFIRMAR si hay puntos registrados, aunque con las fronteras terrestres cerradas desde 2020-2021 es improbable que haya registros recientes de overlanders.",
        "En Asmara las guías citan alojamiento desde unos 10 USD en pensiones (African Village, Top Five Hotel), 20-40 USD en gama media y 60-150 USD en el Sunshine, el Crystal o el Albergo Italia; Booking.com no funciona y hay que reservar por teléfono.",
        "En Massawa: Luna Hotel (20-40 USD), Dahlak Hotel (60-70 USD) y el Grand Dahlak; en Gurgusum, el resort de playa es la única opción a pie de arena.",
        "Dormir en el vehículo junto a instalaciones militares, puertos, puentes o presas está descartado: son precisamente los lugares donde está prohibido incluso fotografiar y donde el FCDO recomienda no detenerse.",
        "En el desierto de Dankalia la acampada es teóricamente posible por la ausencia de población, pero sin agua, sin sombra, con más de 500 km sin servicios y con el permiso improbable: desaconsejada.",
        "Con un perro la ecuación empeora: sin campings, con hoteles que en su mayoría no admiten animales (por confirmar) y sin posibilidad de entrar por tierra, la logística canina en Eritrea no tiene solución razonable hoy.",
    ],
    visado=[
        "VISADO OBLIGATORIO Y PREVIO para españoles, en una de estas cuatro categorías: turismo, negocios, oficial o diplomático (MAEC). No existe exención ni eVisa.",
        "DÓNDE SE PIDE: Eritrea no tiene embajada ni consulado en España. La Ficha País del MAEC precisa que EL EMBAJADOR DE ERITREA RESIDE EN PARÍS (1 rue de Staël, 75015). La misión de Bruselas (15-17 Wolvendaellaan, 1180 Ukkel; +32 2 374 44 34) también aparece como acreditada para España en el directorio consultado.",
        "PLAZOS: más de un mes por la vía de embajada, que es la más barata (Against the Compass, agosto de 2026). Un viajero independiente relata que en 2024-2025 los consulados no contestaban, que una plataforma en línea le denegó la solicitud y que acabó obteniéndolo en Ginebra tras dos semanas de espera.",
        "ALTERNATIVA DE VISADO A LA LLEGADA: solo con carta de invitación tramitada por un operador turístico eritreo autorizado. Cuesta unos 70 USD en efectivo en el aeropuerto y vale 30 días; el operador cobra aparte, del orden de 50 USD de gestión. Wikipedia lo describe como «confirmación de visado preacordada» que el patrocinador debe pedir con al menos 48 horas de antelación.",
        "COSTE DE LA VÍA EMBAJADA: por confirmar. Las tarifas oficiales de las misiones eritreas en París y Bruselas no se han podido abrir en esta sesión.",
        "PASAPORTE: validez mínima de seis meses y DOS PÁGINAS EN BLANCO CONSECUTIVAS para los sellos (FCDO y Departamento de Estado). El visado no da derecho a salir de Asmara: eso es el permiso interior, que se pide ya dentro del país.",
    ],
    fronteras_rows=[
        ("Aeropuerto internacional", "Asmara (ASM / HHAS)", "ÚNICA ENTRADA VIABLE. Conexiones con El Cairo (EgyptAir), Estambul (Turkish), Dubái (flydubai), Yeda (flynas) y Port Sudan (Tarco); Etihad anuncia Abu Dabi desde el 7 de noviembre de 2026. Pista de unos 3.000 m a 2.325 m de altitud y terminal pequeña, con restricciones de capacidad (Wikipedia, abril de 2026). Declarar todos los electrónicos al entrar."),
        ("Paso terrestre con Etiopía", "Serha (ER) – Zalambessa (ET)", "CERRADO. Reabierto el 11 de septiembre de 2018 tras veinte años y cerrado unilateralmente por Eritrea en diciembre de 2018 (Young Pioneer Tours; Wikipedia)."),
        ("Paso terrestre con Etiopía", "Om Hajer (ER) – Humera (ET)", "CERRADO desde abril de 2019, cierre unilateral eritreo (Young Pioneer Tours)."),
        ("Paso terrestre con Etiopía", "Bure (ER) – corredor de Assab", "CERRADO desde el 23 de abril de 2019, el último de los tres en cerrarse (Young Pioneer Tours)."),
        ("Paso terrestre con Etiopía", "Rama (ET) – Adi Kwala / Ksad Ika (ER)", "CERRADO. Un overlander relató en septiembre de 2018 que ni con la frontera abierta le concedieron el permiso interior para llegar a Adi Kwala (Horizons Unlimited)."),
        ("Paso terrestre con Sudán", "Teseney (ER) – Kassala (SD)", "CERRADO a extranjeros y en zona desaconsejada: el MAEC señala Tesseney, Gash Barka, Agordat y Barentu como área a evitar por el conflicto sudanés desde abril de 2023. Teseney está a 45 km de la frontera (15°06′36″N 36°39′27″E, Wikipedia). En el foro de Tripadvisor nadie aporta un cruce de primera mano."),
        ("Paso terrestre con Yibuti", "Frontera sureste, zona de Assab", "CERRADO. El Departamento de Estado afirma que a los extranjeros por lo general no se les permite ni acercarse a la frontera con Yibuti; Canadá pide evitar los 25 km próximos."),
        ("Puerto marítimo", "Massawa", "Puerto principal del país, a 115 km de Asmara por carretera. Salen ferris a las islas Dahlak y a Sheikh Said, con permiso interior. No consta línea internacional de pasajeros ni ro-ro abierta a turistas: POR CONFIRMAR (Wikipedia)."),
        ("Puerto marítimo", "Assab", "Puerto del sur, históricamente ligado al tráfico etíope. Sin servicio de pasajeros documentado y en zona vetada al turismo: POR CONFIRMAR."),
        ("Ferrocarril", "Asmara – Massawa", "Línea histórica de vía estrecha reconstruida tras la independencia, reabierta por tramos hacia 2009 y operada a ratos con locomotoras de vapor de los años treinta, normalmente en charters contratados. No es transporte regular ni sustituye al permiso de viaje (Wikipedia; Ministerio de Turismo)."),
    ],
    vehiculos=[
        "NO SE PUEDE ENTRAR CON EL GRENADIER NI CON LA DELICA: todas las fronteras terrestres están cerradas a turistas y no consta línea ro-ro de pasajeros a Massawa. La única forma de rodar por Eritrea es con vehículo local.",
        "CARNET DE PASSAGES: el AIT/FIA no tiene ninguna organización emisora en Eritrea y su web indica que, para un vehículo matriculado allí, el carnet hay que pedirlo en un país vecino con asociación autorizada. Ninguna fuente confirma si la aduana eritrea exigiría CPD a un vehículo extranjero, porque no hay cruces desde 2019: POR CONFIRMAR.",
        "ADMISIÓN TEMPORAL: sin documentar. Los relatos de la ventana de 2018 describen un vacío administrativo total: «no había formalidades aduanales reales, no podías obtener sellos de entrada ni de salida» (Horizons Unlimited, noviembre de 2018). Cruzar sin sello deja al vehículo y al conductor en un limbo legal.",
        "CONDUCCIÓN POR LA DERECHA. El FCDO exige el permiso internacional de conducción en la VERSIÓN DE 1949 junto al permiso nacional; el Gobierno de Canadá añade que hace falta licencia local.",
        "LICENCIA ERITREA TEMPORAL: un viajero independiente la sacó en 2024-2025 por 500 nakfa para poder conducir un coche de alquiler, y pagó 5.000 nakfa por cinco días (mautz.blog). Lo habitual hoy es contratar conductor: unos 150 USD al día (Against the Compass, agosto de 2026).",
        "EL PERMISO INTERIOR VA LIGADO AL VEHÍCULO: desde hace poco hay que dar la matrícula del coche en el que se viajará al pedir el permiso, además de las fechas exactas de cada destino. Cambiar de vehículo obliga a rehacer el trámite.",
        "SEGURO: la Carta Verde europea no cubre Eritrea y el país no pertenece a Carte Brune CEDEAO ni a Carte Rose CEMAC. Con coche de alquiler, el seguro lo aporta la empresa; condiciones y cobertura POR CONFIRMAR.",
        "ESTADO DE LAS CARRETERAS: señalización y quitamiedos escasos, firme irregular, alumbrado mínimo, conductores erráticos y vías impracticables en época de lluvias (FCDO). No conducir de noche. Unos quince controles en 550 km.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "NO HAY LEY DE DRONES PUBLICADA. UAV Coach afirma literalmente que no ha encontrado ninguna normativa eritrea (actualización del 9 de diciembre de 2022) y advierte de que la ausencia de ley no equivale a permiso.",
        "CONFISCACIÓN DISCRECIONAL EN ADUANA: la misma fuente indica que unos funcionarios requisan el dron y otros no, sin criterio previsible. Además, todos los aparatos electrónicos deben declararse al entrar o pueden ser confiscados al salir (Departamento de Estado de EE. UU.).",
        "PROHIBIDO FOTOGRAFIAR instalaciones militares, aeropuertos, puertos, puentes, edificios gubernamentales y personal uniformado (MAEC, FCDO, Canadá y Departamento de Estado). Las consecuencias documentadas van del aviso a la detención e interrogatorio.",
        "EL CEMENTERIO DE TANQUES DE ASMARA, uno de los iconos fotográficos del país, requiere permiso específico del Ministerio de Turismo incluso para fotos a pie (FCDO).",
        "AUTORIDAD DE AVIACIÓN CIVIL DE ERITREA: teléfono +291 1 120 555, según UAV Coach. Es el único contacto localizado; su web oficial no se ha podido abrir en esta sesión. La recomendación de la ficha es NO llevar dron bajo ninguna circunstancia.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "STARLINK NO DISPONIBLE. Eritrea aparece sin fecha de lanzamiento prevista en los mapas de cobertura de SpaceX y el Gobierno no ha otorgado licencia (ts2.tech, publicado en junio de 2025 y actualizado el 17 de septiembre de 2026).",
        "EriTel es el único operador y no existen ISP privados. El país no tiene estaciones de amarre de cable de fibra submarina, único caso entre los países costeros africanos, y solo un 26 % de la población usa internet.",
        "RED MÓVIL: solo 2G GSM para usuarios civiles, con 3G y 4G deshabilitados. El FCDO confirma que las tarjetas SIM internacionales no funcionan y las guías de 2026 hablan directamente de que «no existe internet móvil».",
        "SIM LOCAL: prácticamente inaccesible para turistas; cuando se han vendido, la tarjeta costaba unos 46 USD. Hay menos de diez cibercafés en Asmara y un centenar en todo el país, con equipos antiguos y conexiones compartidas.",
        "PLAN REALISTA: llevar VPN instalada y configurada ANTES de llegar, asumir desconexión casi total y dejar avisada la posición y las fechas al resto del grupo. Ningún plan de viaje debe depender de poder comunicar desde Eritrea.",
    ],
    perro_intro=[
        "EL PERRO NO VIENE. Con las fronteras terrestres cerradas y entrada solo aérea, meter al perro en Eritrea exigiría vuelo en bodega desde El Cairo, Estambul o Dubái: desproporcionado para un país que está fuera de ruta y donde ni siquiera se puede circular sin permiso.",
        "NO SE HA LOCALIZADO NORMATIVA NACIONAL de importación de animales de compañía. El Ministerio de Agricultura eritreo y sus servicios veterinarios no tienen portal de trámites accesible en esta sesión: requisitos POR CONFIRMAR.",
        "Tampoco consta lista de razas prohibidas ni exigencia publicada de permiso previo de importación. Ausencia de fuente no es ausencia de requisito: sin requisitos por escrito de la embajada eritrea, el perro no se mueve.",
        "RABIA PRESENTE en animales domésticos según TravelHealthPro: cualquier mordedura o lametón sobre herida obliga a buscar profilaxis posexposición inmediata, que en Eritrea puede no estar disponible y obligaría a evacuar.",
        "VUELTA A LA UE: Eritrea NO figura en las listas del Reglamento de Ejecución (UE) 2026/636 —cuyos anexos no incluyen ningún país africano continental, solo Ascensión, Mauricio, Santa Elena y Malvinas—, así que se aplica el régimen de tercer país no listado del Reglamento Delegado (UE) 2026/131: microchip, vacuna antirrábica completa al menos 21 días antes y TITULACIÓN DE ANTICUERPOS ANTIRRÁBICOS con resultado igual o superior a 0,5 UI/ml en laboratorio autorizado.",
        "LA CLAVE ESTÁ EN HACER LA TITULACIÓN EN ESPAÑA ANTES DE SALIR y anotarla en el pasaporte europeo: el MAPA confirma que, si la serología se hizo antes de abandonar la UE, NO se aplica el plazo de espera de 90 días al volver. Si se hace fuera, hay que esperar tres meses desde la extracción para poder entrar.",
        "ATENCIÓN VETERINARIA en Eritrea: sin clínica privada de referencia documentada. Medicación, antiparasitarios, collar y pienso específico hay que llevarlos desde fuera, y la entrada a la UE debe hacerse por un Punto de Entrada de Viajeros declarando el animal a la Guardia Civil.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "FIEBRE AMARILLA: el certificado NO es obligatorio con carácter general, pero sí se exige a los viajeros de nueve meses en adelante que lleguen desde países con riesgo de transmisión (TravelHealthPro y Departamento de Estado). Viniendo de España no se pide; viniendo de Etiopía, Sudán o Kenia, sí.",
        "VACUNAS RECOMENDADAS: hepatitis A, tétanos y fiebre tifoidea para todos, además del calendario habitual. Según el perfil del viaje: hepatitis B, rabia, meningococo ACWY, tuberculosis, dengue y chikunguña (TravelHealthPro). El MAEC añade cólera y meningitis.",
        "PALUDISMO: riesgo por debajo de 2.200 m de altitud y sin riesgo en Asmara. Quimioprofilaxis con atovacuona-proguanil, doxiciclina o mefloquina si se baja a Massawa o Assab (TravelHealthPro; el MAEC coincide). Eritrea redujo un 85 % la mortalidad por malaria entre 1998 y 2006.",
        "OTROS RIESGOS: dengue y chikunguña con mosquito de picadura diurna, esquistosomiasis en agua dulce, rabia en animales domésticos y mal de altura por encima de 2.500 m; Asmara está a 2.325 m y conviene aclimatarse el primer día sin esfuerzo.",
        "AGUA Y COMIDA: no beber agua sin tratar ni tomar alimentos crudos (MAEC). Extremar la higiene de manos y no bañarse en agua dulce.",
        "ASISTENCIA SANITARIA muy por debajo del estándar europeo: 22 hospitales en todo el país en 2019 y muy pocos médicos por habitante. El MAEC recomienda expresamente seguro médico con cobertura de evacuación. Un caso grave se resuelve evacuando a El Cairo, Dubái o Nairobi.",
        "MEDICACIÓN: llevarlo todo desde España, incluida la crónica, en envase original y con receta traducida. No contar con farmacias surtidas ni con reposición local.",
    ],
    seguridad_intro="Eritrea no es peligrosa por delincuencia, sino por Estado. La criminalidad común es de las más bajas de África y Asmara se camina de noche sin problema, pero el MAEC desaconseja el viaje y sitúa el riesgo terrorista en nivel medio, hay minas antipersona sin retirar en las franjas fronterizas y el desminado está incompleto. A eso se suma un control administrativo permanente: permiso para moverse, puestos de control cada pocos kilómetros, prohibición de fotografiar casi cualquier cosa oficial y una embajada española que está en El Cairo.",
    seguridad=[
        "EL MAEC DESACONSEJA EL VIAJE. Si se viaja, evitar la franja fronteriza con Sudán —especialmente Tesseney, Gash Barka, Agordat y Barentu, señaladas desde el conflicto sudanés de abril de 2023—, la frontera etíope y la yibutiana.",
        "EL GOBIERNO DE CANADÁ pide evitar todo viaje a menos de 25 km de las fronteras con Etiopía, Sudán y Yibuti por actividad militar y conflictos territoriales, y desaconseja los viajes no esenciales al resto del país.",
        "EL FCDO desaconseja todo viaje a partes de Eritrea y advierte de que la tensión con Etiopía sigue alta y la situación puede cambiar sin aviso.",
        "MINAS ANTIPERSONA: el desminado está incompleto. No salir de las carreteras principales, no aparcar fuera del asfalto y no caminar campo a través en zonas fronterizas (MAEC).",
        "PUESTOS DE CONTROL constantes fuera de Asmara: llevar siempre el pasaporte o fotocopia y varias copias del permiso interior. Un viajero de 2024-2025 contó unos quince controles en 550 km, aunque solo en uno, en Keren, le pidieron el papel (mautz.blog).",
        "FOTOGRAFÍA: prohibido fotografiar o grabar lugares considerados estratégicos para la seguridad nacional. El Departamento de Estado enumera las consecuencias posibles: aviso, acoso, confiscación del teléfono o la cámara, detención, arresto e interrogatorio.",
        "MILICIA CIVIL ARMADA generalizada y servicio militar indefinido: es normal cruzarse con personal armado de aspecto no profesional. No discutir, no grabar y no hablar de política con desconocidos, ni siquiera en tono amable.",
        "LA HOMOSEXUALIDAD ES ILEGAL en Eritrea, como advierten expresamente el MAEC y el FCDO. Discreción absoluta.",
        "MAR ROJO: actividad militar y riesgo de piratería en las aguas próximas, lo que afecta a cualquier plan marítimo hacia Massawa o las islas Dahlak (FCDO).",
    ],
    agua=[
        "AGUA NO POTABLE: el MAEC recomienda no beber agua sin tratar ni consumir alimentos crudos. Para beber, agua embotellada o filtrada y tratada con lámpara UV o pastillas.",
        "PARA LLENAR DEPÓSITOS de ducha y lavado, el agua de red de Asmara sirve con prefiltro y depósito propio, pero hay cortes frecuentes: no fiarse de un único punto de carga ni salir con los depósitos a medias.",
        "ESCASEZ ESTRUCTURAL fuera de Asmara: en la franja costera de Massawa y hacia el sur el agua es salobre y muy escasa, con temperaturas que superan los 40 °C en verano. Salir siempre con carga completa desde la capital.",
        "ESQUISTOSOMIASIS en agua dulce (TravelHealthPro): no bañarse ni llenar depósitos en ríos, embalses ni charcas, ni siquiera para lavar ropa o al perro.",
        "PUNTOS DE CARGA FIABLES: solo hoteles de Asmara y Massawa. No hay red de campings ni de áreas de autocaravanas documentada en el país, ni registros de iOverlander utilizables: POR CONFIRMAR.",
    ],
    combustible=[
        "PRECIO 2026: POR CONFIRMAR. No hay ninguna fuente oficial ni agregador que publique hoy el litro de gasolina o gasóleo eritreo: GlobalPetrolPrices no tiene ficha de Eritrea y TheGlobalEconomy ha retirado la suya.",
        "ÚLTIMO DATO DATADO: 1,33 USD por litro de gasóleo en 2016, según la serie de la agencia alemana GIZ recogida por IndexMundi, con un máximo histórico de 3,00 USD en 2014. Diez años después no sirve para presupuestar, pero da el orden de magnitud.",
        "RACIONAMIENTO Y ESCASEZ CRÓNICA: Eritrea arrastra desde hace años un suministro irregular con venta controlada. Ninguna fuente abierta en esta sesión documenta el sistema de cupones vigente en 2026: POR CONFIRMAR.",
        "PAGO EN EFECTIVO Y EN NAKFA: no hay cajeros ni se aceptan tarjetas en ningún punto del país (MAEC y Departamento de Estado), y el cambio solo es legal en las oficinas estatales Himbol.",
        "RED DE ESTACIONES muy escasa fuera del eje Asmara-Keren-Massawa. Si algún día se pudiera entrar con vehículo propio, habría que asumir 400-500 km entre repostajes seguros y llevar depósito auxiliar.",
        "EN LA PRÁCTICA HOY: con conductor y coche local (unos 150 USD al día) el combustible y el cupo los gestiona la empresa. Preguntar antes de salir de Asmara cuánta asignación tienen para la ruta autorizada en el permiso.",
    ],
    experiencias_intro="No hay relatos recientes de overlanders entrando en Eritrea con vehículo propio: la ventana terrestre se abrió unos meses en 2018 y se cerró en 2019. Lo que sigue son los últimos testimonios disponibles, con su fecha, más los de viajeros independientes que han entrado en avión hasta 2026.",
    experiencias=[
        "Una semana por libre en Eritrea (2024-2025): Rainer Mautz cuenta en mautz.blog cómo entró en Nochevieja tras semanas de silencio consular. Los consulados no contestaban, una plataforma en línea le denegó la solicitud y acabó obteniendo el visado en Ginebra tras dos semanas de espera y un viaje de cuatro horas. Es el relato independiente más detallado que se ha podido abrir para esta ficha.",
        "El permiso de viaje interior, en cifras (mautz.blog, 2024-2025): se tramita en el Ministerio de Turismo de Asmara, cuesta 200 nakfa —unos 13 dólares— y suele estar listo en un día. Cubre Dekemhare, Mendefera, Keren y Massawa; el resto del país está cerrado a turistas. Es la fuente más concreta sobre el coste y el alcance real del permiso.",
        "Quince controles en 550 kilómetros (mautz.blog, 2024-2025): el mismo viajero relata que en 550 km pasó por unos quince puestos de control, pero que solo en uno, en Keren, le pidieron copia del permiso. La lección operativa es llevar varias fotocopias y no improvisar rutas, porque el papel fija destinos y fechas.",
        "Conducir en Eritrea siendo extranjero (mautz.blog, 2024-2025): está prohibido moverse entre ciudades a pie o en transporte público; solo se permite coche de alquiler. Tuvo que sacar una licencia de conducción eritrea temporal por 500 nakfa y pagó 5.000 nakfa por cinco días de alquiler. Es el dato más útil para calcular un desvío aéreo.",
        "Cómo se viaja a Eritrea en 2026 (Against the Compass, actualizado el 30 de agosto de 2026): confirma que todas las fronteras terrestres siguen cerradas, que el visado por embajada tarda más de un mes y que la alternativa es un visado a la llegada de 70 dólares con carta de invitación de un operador. Los permisos, unos 10 dólares por destino, medio día de trámite y oficina cerrada los domingos.",
        "El permiso ya lleva matrícula (Against the Compass, 2026): la novedad que más condiciona la logística es que el permiso interior exige ahora el número de matrícula del vehículo en el que se viajará y las fechas exactas en cada sitio. Se acabó el autobús por libre: casi todos los turistas contratan conductor por unos 150 dólares al día.",
        "Presupuesto real de una semana (Wild Junket): la bloguera Nellie Huang cifra una semana en Eritrea en unos 600 dólares por persona, con hoteles de 80 a 150 dólares, permisos de 50 nakfa por zona tramitados en el Ministerio de Turismo de Harnet Avenue en un día, autobús Asmara-Massawa por 50 nakfa y taxi del aeropuerto al centro por 300 nakfa. Insiste en llevar VPN.",
        "La ventana de 2018 (Horizons Unlimited, noviembre de 2018): cuando se abrió la frontera con Etiopía en septiembre de 2018, un usuario del foro relató que incluso algunos extranjeros pudieron pasar sin documentación, en un ambiente de euforia y sin procedimiento fijado. Dejó claro que era una situación fluida y probablemente temporal. Acertó.",
        "Sin sellos y sin aduana (Horizons Unlimited, 2018): el problema de aquella ventana no fue el control, sino su ausencia: «no había formalidades aduanales reales, no podías obtener sellos de entrada ni de salida». Otro usuario, chris.perjalanan, explicó en septiembre de 2018 que ni con la frontera abierta le dieron permiso para llegar a Adi Kwala.",
        "Vuelta al cierre y visado solo para Asmara (Horizons Unlimited, 2019): cuatro meses después de la apertura, los mensajes dan la frontera terrestre de nuevo cerrada a extranjeros y describen visados de 90 días que había que pedir en el país de residencia y que solo daban acceso a Asmara. En el foro de Tripadvisor, Erik van M resumió el estado de la información sobre el paso Kassala-Teseney: «leo cosas muy contradictorias», y nadie aportó una experiencia de primera mano.",
    ],
    pendientes=[
        ("Tarifa oficial del visado eritreo para españoles", "Tarifario publicado o respuesta por escrito de la Embajada de Eritrea en París o Bruselas con importe en euros y plazo real de tramitación."),
        ("Misión eritrea competente para España", "Confirmación en fuente oficial eritrea o en el directorio del MAEC de si la acreditación para España la ejerce París (donde reside el embajador) o Bruselas."),
        ("Coste y alcance del permiso interior en 2027", "Fuente de 2027 —MAEC, FCDO o relato fechado— que confirme el precio por destino y la lista vigente de zonas autorizadas, que ha cambiado entre 2024 y 2026."),
        ("Requisitos de importación de animales de compañía", "Página oficial del Ministerio de Agricultura eritreo o respuesta por escrito de su servicio veterinario con certificado, plazos, permiso previo y razas."),
        ("Exigencia de CPD a vehículo extranjero", "Confirmación de la aduana eritrea o relato de un overlander que haya entrado con vehículo matriculado fuera después de 2018."),
        ("Seguro de vehículo obligatorio", "Verificar con OFESAUTO si la Carta Verde cubre Eritrea y si el país participa en la COMESA Yellow Card para vehículos extranjeros."),
        ("Precio del combustible en 2026-2027", "Dato con fecha del Gobierno eritreo, de GlobalPetrolPrices o de un relato de 2026 con precio por litro en nakfa; el último dato fiable es de 2016."),
        ("Sistema de racionamiento de carburante", "Documentar si sigue vigente la venta por cupones y cómo afecta a un vehículo alquilado por un extranjero."),
        ("Coordenadas verificadas del hospital de referencia", "Localizar el Orotta National Referral Hospital de Asmara en GeoNames o en una web oficial con coordenadas, y confirmar si admite extranjeros de urgencia."),
        ("Teléfono de emergencia consular aplicable a Eritrea", "Confirmar con la Embajada de España en Jartum/El Cairo si su línea de emergencia (+20 122 318 3783) cubre a los españoles que estén en Eritrea."),
        ("Ferry o línea marítima a Massawa", "Comprobar si existe algún servicio internacional de pasajeros o ro-ro operativo hacia Massawa desde Yeda, Port Sudan o Yibuti."),
        ("Estado del ferrocarril Asmara-Massawa", "Confirmar con el Ministerio de Turismo (+291 1 154100) si hay circulaciones regulares o solo charters, y a qué precio."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con todas las páginas abiertas en esa fecha, salvo las indicadas en «notas» que no cargaron. Es una herramienta de planificación, no una autorización ni un documento oficial: las condiciones de entrada, el permiso de viaje interior y el estado de las fronteras eritreas cambian sin aviso y solo valen los requisitos que confirmen por escrito la misión eritrea competente y el MAEC antes de salir. Lo marcado como «por confirmar» no está verificado y no debe usarse para decidir.",
    emergency="Policía 113, ambulancia 114 y bomberos 116 (Gobierno de Canadá). El Departamento de Estado añade policía +291 1 127 799, bomberos +291 1 202 099 y urgencias +291 1 202 914. El MAEC da la policía por ciudad: Asmara +291 1 116 219, Massawa +291 552 113, Keren +291 401 049, Assab +291 660 690. Sin embajada española en Asmara: competencia de la de Jartum, hoy en El Cairo (emb.jartum@maec.es), emergencia consular +20 122 318 3783.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

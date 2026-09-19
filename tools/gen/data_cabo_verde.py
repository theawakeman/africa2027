# -*- coding: utf-8 -*-
"""Cabo Verde — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Cabo Verde está FUERA DE LA RUTA PREVISTA por ser insular: diez islas a 570 km de la costa africana, sin conexión terrestre ni ferry de vehículos desde el continente. La app solo tiene un stub: créala entera con el formato del piloto de Túnez. Es la democracia más sólida de África occidental — alternancia pacífica desde 1991, primeros puestos de Freedom House en el continente — y uno de los destinos más seguros: decirlo con claridad es parte de la ficha. Claves que DECIDEN la ficha y hay que documentar con fuente fechada: desde enero de 2019 los ciudadanos de la UE NO necesitan visado para estancias cortas, pero SÍ hay que registrarse antes en la plataforma EASE y pagar la Taxa de Segurança Aeroportuária (TSA); verifica importe y vigencia. El archipiélago tiene dos bienes en la Lista del Patrimonio Mundial o en la indicativa: Cidade Velha (Ribeira Grande de Santiago), inscrita en 2009. Las islas son MUY distintas entre sí — Santo Antão y Fogo son de montaña y senderismo; Sal y Boa Vista, de playa y desierto; Santiago y São Vicente, las urbanas — y la ficha tiene que ordenar los PDIs por isla para que se entienda.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/cabo-verde.json y audit/pdi/cabo-verde.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Cidade Velha · Ribeira Grande de Santiago, la primera ciudad europea del trópico (UNESCO)", cat="Patrimonio UNESCO", prio="Alta",
        dog="permitido con condiciones", time="medio día",
        lat=14.9160854, lon=-23.6020515,  # Google Maps: Fuerte Real de San Felipe
        desc="Fundada en 1462 por comerciantes portugueses al mando de António da Noli, Ribeira Grande fue el PRIMER ASENTAMIENTO COLONIAL EUROPEO DE LOS TRÓPICOS y la bisagra del comercio atlántico de esclavos entre África, Brasil y el Caribe. La UNESCO la inscribió en 2009 con los criterios ii, iii y vi. Quedan el trazado original, la iglesia de Nossa Senhora do Rosário, las ruinas de la Sé, el pelourinho de mármol del siglo XVI y el Forte Real de São Filipe, a 120 m sobre el mar. La pista de subida al fuerte es corta pero empinada y sin sombra: agua y calzado cerrado.",
        dog_note="Todo el conjunto es calle abierta y se recorre con perro atado; dentro de las iglesias y del centro de interpretación, no.",
        visit={
            "why": "Es el único bien caboverdiano inscrito en la Lista del Patrimonio Mundial y explica en una mañana por qué existe Cabo Verde: escala atlántica, esclavitud y nacimiento de la primera sociedad criolla.",
            "see": "Rua Banana, la plaza del pelourinho con su columna de mármol (1512-1520), las ruinas de la Sé (1556-1705), la iglesia de Nossa Senhora do Rosário y el Forte Real de São Filipe (1587-1593) con vistas al valle.",
            "access": "Asfalto bueno desde Praia por la costa sur, unos 15 km; el ramal al fuerte es hormigón/pista corta y empinada, sin problema para dos 4x4, con explanada arriba para aparcar. El pueblo tiene aparcamiento junto al paseo marítimo. Entrada de pago al fuerte (importe por confirmar). El pin marca la explanada del Forte Real de São Filipe, no el pelourinho.",
            "when": "Primera hora de la mañana: el fuerte no tiene sombra y el calor aprieta desde media mañana. De noviembre a junio, tiempo seco.",
            "skip": "Si solo se dispone de un día en Santiago y ya se ha visto el Platô, no: este es el que no se descarta.",
        },
        links=[
            {"label": "UNESCO · Cidade Velha, Historic Centre of Ribeira Grande", "url": "https://whc.unesco.org/en/list/1310/"},
            {"label": "Wikipedia · Cidade Velha", "url": "https://en.wikipedia.org/wiki/Cidade_Velha"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cidade_Velha_Ilha_de_Santiago,_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cidade_Velha_Ilha_de_Santiago,_Cabo_Verde.jpg",
                "credit": "TxetxeCV · CC0",
                "caption": "Cidade Velha, la primera ciudad europea del trópico.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cidade_Velha_Pelourinho_square_b_2011.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cidade_Velha_Pelourinho_square_b_2011.jpg",
                "credit": "Cayambe · CC BY-SA 3.0",
                "caption": "La plaza del pelourinho.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Kids_playing_football_near_fisherman_boats_in_Cidade_Velha,_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Kids_playing_football_near_fisherman_boats_in_Cidade_Velha,_Cabo_Verde.jpg",
                "credit": "Loulesanggg · CC BY-SA 4.0",
                "caption": "La playa de Cidade Velha.",
            },
        ],
    ),
    dict(
        n=2, name="Praia y el Platô · la capital y su meseta colonial", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=14.9173291, lon=-23.5093458,  # Google Maps: Praça Alexandre Albuquerque
        desc="La capital creció alrededor del Platô, una meseta plana sobre el puerto que se reordenó en el siglo XIX con trama en cuadrícula y caserones coloniales. Ahí están la plaza de Alexandre Albuquerque, el Palácio Presidencial de finales del XIX, el ayuntamiento de los años veinte, el cuartel Jaime Mota (1826) y el Museu Etnográfico, abierto en 1997. El centro histórico figura en la LISTA INDICATIVA de la UNESCO desde 2016. Es la base logística obligada del archipiélago: talleres, repuestos, bancos y el puerto de ferris. Tráfico denso y aparcamiento escaso en el Platô.",
        dog_note="Calle y plazas sin problema con correa; el Museu Etnográfico y los edificios oficiales, no.",
        visit={
            "why": "Es el nudo de servicios del país —puerto, aeropuerto, talleres, embajadas— y el Platô concentra en diez manzanas toda la arquitectura administrativa portuguesa de Santiago.",
            "see": "La cuadrícula decimonónica del Platô, la Praça Alexandre Albuquerque con su quiosco, el Palácio Presidencial, el monumento a Diogo Gomes y el mercado; abajo, el puerto y la playa de Quebra Canela.",
            "access": "Asfalto en todo el acceso; la subida al Platô es corta y con curvas cerradas, apta para vehículos largos pero con poco sitio para maniobrar. Aparcar dos 4x4 en el Platô es complicado: mejor dejarlos en Achada Santo António o junto al puerto y subir a pie. El pin marca la Praça Alexandre Albuquerque, centro peatonal del Platô.",
            "when": "Entre semana por la mañana para trámites y talleres; el ambiente de calle es mejor a última hora de la tarde.",
            "skip": "Si no se necesitan ni servicios ni ferri, una noche basta y el interés cultural es menor que el de Cidade Velha o Mindelo.",
        },
        links=[
            {"label": "Wikipedia · Praia", "url": "https://en.wikipedia.org/wiki/Praia"},
            {"label": "Instituto do Património Cultural de Cabo Verde", "url": "https://ipc.cv/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cidade_da_Praia_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cidade_da_Praia_Cabo_Verde.jpg",
                "credit": "TxetxeCV · CC BY-SA 4.0",
                "caption": "Praia y su meseta, el Platô.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mercado_do_Plateau,_Praia.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mercado_do_Plateau,_Praia.jpg",
                "credit": "Alvaro Ludgero Andrade (VOA) · Public domain",
                "caption": "El mercado del Platô.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Rua_Pedonal,_Praia,_Cabo_Verde_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Rua_Pedonal,_Praia,_Cabo_Verde_01.jpg",
                "credit": "GualdimG · CC BY-SA 4.0",
                "caption": "Calle peatonal del Platô.",
            },
        ],
    ),
    dict(
        n=3, name="Tarrafal de Santiago · la playa y el campo de concentración", cat="Cultura", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=15.2634799, lon=-23.7437356,  # Google Maps: Museu do Campo de Concentração do Tarrafal
        desc="Tarrafal junta las dos caras del país en cinco kilómetros: la mejor playa de arena blanca de Santiago y el campo donde el Estado Novo portugués encerró a sus presos políticos ENTRE 1936 Y 1974. Murieron allí al menos 32 personas; el recinto, construido en 1936 y rehabilitado en 2021, es hoy el Museu da Resistência, abierto todos los días de 9:00 a 17:00 por 200 escudos para extranjeros. El pueblo es un puerto pesquero en la costa noroeste, al fondo de la Baía de Tarrafal. La visita es dura y conviene reservarle tiempo: no es una parada de playa con museo al lado.",
        dog_note="La playa y el pueblo, sí, con correa; el recinto museizado del campo, por confirmar y en principio no.",
        visit={
            "why": "Por el contraste entre la bahía y el campo de Chão Bom, la pieza central de la memoria antifascista de Portugal y de sus colonias africanas.",
            "see": "Los barracones, las dependencias administrativas y el polvorín, recorridos por un circuito que arranca en la puerta del recinto; dos salas, una para los presos antifascistas portugueses (1936-1956) y otra para los anticoloniales de Angola, Guinea-Bisáu y Cabo Verde (1962-1974). Fuera, la bahía y el puerto pesquero.",
            "access": "Asfalto desde Praia por la costa este o por el interior vía Assomada y Serra Malagueta (unos 70 km). El campo está en Chão Bom, 2 km antes del pueblo, con aparcamiento amplio delante del recinto; en la playa hay explanada de tierra donde caben dos 4x4. Museo abierto a diario de 9:00 a 17:00 (festivos hasta las 13:00; cerrado el 1 y el 15 de enero, el 1 de mayo y el 25 de diciembre); entrada 200 escudos para extranjeros. El pin marca la puerta del recinto del campo, no la playa.",
            "when": "Mañana para el campo (la visita se hace larga con calor) y tarde para la bahía.",
            "skip": "Si el viaje es solo de costa y no interesa la parte histórica, la playa por sí sola no justifica el desvío frente a Sal o Boa Vista.",
        },
        links=[
            {"label": "IPC · Museu da Resistência (Tarrafal)", "url": "https://ipc.cv/en/museu/museu-da-resistencia/"},
            {"label": "Wikipedia · Tarrafal, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Tarrafal,_Cape_Verde"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/City_of_Tarrafal_Santiago_CV.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:City_of_Tarrafal_Santiago_CV.jpg",
                "credit": "Iwoelbern · Public domain",
                "caption": "Tarrafal, en el norte de Santiago.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Interior_do_Campo_de_Concentra%C3%A7%C3%A3o_do_Tarrafal,_Tarrafal,_Ilha_de_Santiago,_Cabo_Verde_14.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Interior_do_Campo_de_Concentra%C3%A7%C3%A3o_do_Tarrafal,_Tarrafal,_Ilha_de_Santiago,_Cabo_Verde_14.jpg",
                "credit": "GualdimG · CC BY-SA 4.0",
                "caption": "Interior del campo de concentración del Tarrafal.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Costa_de_Tarrafal,_Tarrafal,_Ilha_de_Santiago,_Cabo_Verde_01.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Costa_de_Tarrafal,_Tarrafal,_Ilha_de_Santiago,_Cabo_Verde_01.jpg",
                "credit": "GualdimG · CC BY-SA 4.0",
                "caption": "La costa de Tarrafal.",
            },
        ],
    ),
    dict(
        n=4, name="Serra Malagueta y Assomada · el interior de Santiago", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=15.1856012, lon=-23.6770012,  # Google Maps: Parque Natural de Serra Malagueta
        desc="La carretera del interior de Santiago cruza la Serra Malagueta por un collado con niebla y bosque, muy lejos de la imagen de playa del archipiélago. La cumbre llega a 1.064 m y el parque natural, creado el 24 DE FEBRERO DE 2005, protege 774 hectáreas con unas 124 especies vegetales, 28 de ellas endémicas; la carqueja de Santiago (Limonium lobinii) no crece en ningún otro sitio. Abajo queda Assomada, a 560 m, con uno de los mercados mayores de la isla, fundado en 1931. Niebla frecuente y curvas cerradas: se conduce despacio.",
        dog_note="Parque natural sin grandes depredadores; atado y fuera de los cultivos. El mercado de Assomada, no.",
        visit={
            "why": "Es la vertiente verde y agrícola de Santiago y el mejor sitio del país para entender su flora endémica sin salir de la carretera principal.",
            "see": "El collado del parque y sus senderos hacia Ribeira Principal, las terrazas de caña y maíz, y el mercado de Assomada con producto agrícola y artesanía.",
            "access": "Asfalto en toda la travesía Praia-Assomada-Tarrafal; el centro de visitantes está a pie de carretera con explanada para varios vehículos. Entrada y horario del parque, por confirmar. El pin marca el centro de visitantes del parque, junto a la carretera.",
            "when": "Mañana temprano, antes de que suba la niebla; el mercado de Assomada funciona a diario y se anima los miércoles y sábados (por confirmar).",
            "skip": "Con niebla cerrada no se ve nada y los senderos resbalan; en ese caso, seguir a Tarrafal.",
        },
        links=[
            {"label": "Wikipedia · Serra Malagueta", "url": "https://en.wikipedia.org/wiki/Serra_Malagueta"},
            {"label": "Wikipedia · Assomada", "url": "https://en.wikipedia.org/wiki/Assomada"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Serra_Malagueta_CV.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Serra_Malagueta_CV.jpg",
                "credit": "Ingo Wölbern · Public domain",
                "caption": "La Serra Malagueta.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Serra_de_Malagueta_(23303159495).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Serra_de_Malagueta_(23303159495).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "El interior montañoso de Santiago.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Serra_Malagueta,_Santa_Catarina.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Serra_Malagueta,_Santa_Catarina.jpg",
                "credit": "Somada · CC BY-SA 4.0",
                "caption": "Cultivos en Santa Catarina.",
            },
        ],
    ),
    dict(
        n=5, name="Mindelo (São Vicente) · el puerto criollo y la morna", cat="Ciudad · servicios", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=16.8843537, lon=-24.9900854,  # Google Maps: Torre de Belém / Museu do Mar (Mindelo)
        desc="Mindelo ocupa el gran puerto natural de Porto Grande, que desde 1838 fue depósito de carbón de las navieras británicas. Es la capital cultural del país: carnaval, morna y la ciudad natal de CESÁRIA ÉVORA (1941-2011), que da nombre al aeropuerto. En el frente marítimo está la réplica de la Torre de Belém levantada entre 1918 y 1937; detrás, el mercado municipal de 1878 y la antigua Rua Lisboa, hoy Rua Libertadores de África, con arquitectura colonial del XIX. Es el puerto del ferri a Santo Antão y el mejor sitio para reparaciones después de Praia.",
        dog_note="Calle, paseo y muelle sin problema con correa; mercado municipal e iglesias, no.",
        visit={
            "why": "Es el enlace obligado con Santo Antão y la ciudad más viva del archipiélago, con música en directo casi cada noche.",
            "see": "La bahía de Porto Grande, la Torre de Belém, el mercado de 1878, la Rua Libertadores de África, el Palácio do Povo y los bares de morna y coladeira.",
            "access": "Asfalto en toda la isla. Aparcar dos 4x4 en el centro es posible en la avenida marítima, con vigilancia informal. El embarcadero del ferri a Porto Novo está al sur del centro; conviene sacar billete el día antes. El pin marca la Torre de Belém, en la avenida marítima, buena referencia para aparcar.",
            "when": "Febrero para el carnaval; cualquier noche para música en directo. Evitar la llegada en domingo, con servicios cerrados.",
            "skip": "Solo si no se va a cruzar a Santo Antão y se prefiere tiempo en Fogo.",
        },
        links=[
            {"label": "Wikipedia · Mindelo", "url": "https://en.wikipedia.org/wiki/Mindelo"},
            {"label": "Câmara Municipal de São Vicente", "url": "https://www.cmsv.cv/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Mindelo_(S_Vicente,_Cabo_Verde).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Mindelo_(S_Vicente,_Cabo_Verde).JPG",
                "credit": "Manuel de Sousa · CC BY-SA 3.0",
                "caption": "Mindelo, en São Vicente.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Praia_da_Laginha_-_Mindelo_-_S%C3%A3o_Vicente_-_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Praia_da_Laginha_-_Mindelo_-_S%C3%A3o_Vicente_-_Cabo_Verde.jpg",
                "credit": "Kisoliveira · CC BY-SA 4.0",
                "caption": "La playa de Laginha.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Liceu_Gil_Eanes_-liceu_velho-_Mindelo,_S%C3%A3o_Vicente_.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Liceu_Gil_Eanes_-liceu_velho-_Mindelo,_S%C3%A3o_Vicente_.jpg",
                "credit": "TxetxeCV · CC BY-SA 4.0",
                "caption": "El viejo liceo Gil Eanes.",
            },
        ],
    ),
    dict(
        n=6, name="Monte Verde y la bahía de São Pedro · las alturas de São Vicente", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=16.8684279, lon=-24.9329397,  # Google Maps: Monte Verde
        desc="Monte Verde es el techo de São Vicente con 744 m y el único punto de la isla donde la niebla deja verde la ladera; forma parte del Parque Natural de Monte Verde, de 3,12 km². Desde arriba se ve la bahía de Porto Grande, el islote de Santa Luzia y, con aire limpio, el perfil de Santo Antão. En la costa sur, la bahía de SÃO PEDRO queda justo al sur del aeropuerto Cesária Évora: arena clara, viento constante y acantilado. La pista de subida a la cumbre está muy expuesta al viento; con ráfagas fuertes, no compensa.",
        dog_note="Parque natural sin fauna peligrosa; atado por las antenas de la cumbre y por el viento.",
        visit={
            "why": "Dos miradores en medio día: la cumbre de la isla y la bahía más fotogénica de São Vicente, ambas a menos de media hora de Mindelo.",
            "see": "Desde Monte Verde, Porto Grande, Santa Luzia y Santo Antão; en São Pedro, la playa de arena clara al pie del acantilado y los kitesurfistas.",
            "access": "Asfalto hasta el desvío y pista de tierra y hormigón hasta las antenas de la cumbre, transitable con 4x4 y con sitio para aparcar arriba. A São Pedro se llega por asfalto desde la carretera del aeropuerto. Sin entrada ni horario conocidos. El pin marca el mirador de la cumbre de Monte Verde.",
            "when": "Media mañana, cuando la niebla de la cumbre ya se ha levantado; el viento arrecia por la tarde.",
            "skip": "Con nube baja sobre la cumbre no se ve nada: bajar directamente a São Pedro.",
        },
        links=[
            {"label": "Wikipedia · Monte Verde (Cabo Verde)", "url": "https://en.wikipedia.org/wiki/Monte_Verde_(Cape_Verde)"},
            {"label": "Wikipedia · São Pedro, Cabo Verde", "url": "https://en.wikipedia.org/wiki/S%C3%A3o_Pedro,_Cape_Verde"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Monte_Verde_(S_Vicente,_Cabo_Verde).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Monte_Verde_(S_Vicente,_Cabo_Verde).JPG",
                "credit": "Manuel de Sousa · CC BY-SA 3.0",
                "caption": "El Monte Verde.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Monte_Cara_(S_Vicente,_Cabo_Verde).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Monte_Cara_(S_Vicente,_Cabo_Verde).JPG",
                "credit": "Manuel de Sousa · CC BY-SA 3.0",
                "caption": "El Monte Cara sobre la bahía.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Praia_Grande_Calhau_(S_Vicente,_Cabo_Verde).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Praia_Grande_Calhau_(S_Vicente,_Cabo_Verde).JPG",
                "credit": "Manuel de Sousa · CC BY-SA 3.0",
                "caption": "La costa de Calhau.",
            },
        ],
    ),
    dict(
        n=7, name="Baía das Gatas · la bahía y su festival de agosto", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="medio día",
        lat=16.9037558, lon=-24.908671,  # Google Maps: Baía das Gatas
        desc="En la costa este de São Vicente, una barrera de roca volcánica cierra una piscina natural de agua tranquila, rara en un archipiélago de oleaje duro. El navegante portugués Diogo Afonso ya la registró en 1462. DESDE 1984 acoge el Festival de Música da Baía das Gatas, que se celebra el fin de semana de luna llena de agosto y mezcla cartel local e internacional. El resto del año es un caserío casi vacío a veinte minutos de Mindelo. En festival, el acceso se colapsa y no hay sombra ni servicios: conviene llegar temprano y con agua.",
        dog_note="Playa abierta sin restricción conocida; durante el festival, mejor dejarlo fuera por el ruido y la multitud.",
        visit={
            "why": "Es el baño seguro de São Vicente y, en agosto, la cita musical más multitudinaria del país.",
            "see": "La piscina natural cerrada por la barra de lava, la playa y, en festival, el escenario montado sobre la arena.",
            "access": "Asfalto desde Mindelo, unos 12 km por Calhau; explanada de tierra junto a la playa donde caben dos 4x4 de sobra fuera de temporada. Sin entrada. El pin marca el acceso a la playa y su explanada.",
            "when": "Fin de semana de luna llena de agosto para el festival; el resto del año, cualquier mañana con marea alta.",
            "skip": "Si se busca tranquilidad y se coincide con el festival, cambiar por Calhau o São Pedro.",
        },
        links=[
            {"label": "Wikipedia · Baía das Gatas", "url": "https://en.wikipedia.org/wiki/Ba%C3%ADa_das_Gatas"},
            {"label": "Câmara Municipal de São Vicente", "url": "https://www.cmsv.cv/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Baia_das_gatas.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Baia_das_gatas.jpg",
                "credit": "Autor desconocido · CC BY-SA 3.0",
                "caption": "La bahía de Baía das Gatas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Baia_Gatas_(S_Vicente,_Cabo_Verde).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Baia_Gatas_(S_Vicente,_Cabo_Verde).JPG",
                "credit": "Manuel de Sousa · CC BY-SA 3.0",
                "caption": "La laguna natural de Baía das Gatas.",
            },
        ],
    ),
    dict(
        n=8, name="Santo Antão · la Cova, el valle de Paúl y el camino a Ribeira Grande", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=17.1083948, lon=-25.0622762,  # Google Maps: Cratera da Cova
        desc="El cráter de la Cova, de un kilómetro de diámetro y con el fondo a 1.166 m, se cultiva con maíz y judías gracias a la niebla del alisio; el borde ronda los 1.500 m. De ahí baja el valle de Paúl, un corredor de terrazas, cañaverales y alambiques de grogue hasta el mar. Todo forma el Parque Natural Cova-Paúl-Ribeira da Torre, unas 2.092 ha con 85 ESPECIES ENDÉMICAS, 13 exclusivas de Santo Antão, en la LISTA INDICATIVA de la UNESCO desde el 15 de marzo de 2016. La carretera de cumbre desde Porto Novo es estrecha y con niebla constante.",
        dog_note="Terreno abierto y agrícola, sin grandes depredadores; atado por los cultivos en terraza y el ganado.",
        visit={
            "why": "Es el paisaje más espectacular del archipiélago y la razón principal para cruzar en ferri desde Mindelo.",
            "see": "El cráter cultivado de la Cova desde el borde, el descenso al valle de Paúl entre terrazas, los trapiches de grogue y la llegada a Ribeira Grande, en la desembocadura del río.",
            "access": "Ferri Mindelo-Porto Novo, cuatro conexiones diarias; los vehículos embarcan en el mismo buque (tarifa y cupo, por confirmar con antelación). Desde Porto Novo, la carretera nacional EN1-SA01 cruza el interior montañoso hasta Ribeira Grande: tramo empedrado histórico, estrecho, sin quitamiedos y con niebla. Hay explanada en el collado de la Cova para dos 4x4. El pin marca el mirador del borde del cráter, junto a la carretera de cumbre.",
            "when": "Mañana, antes de que la niebla cierre el collado; de noviembre a junio, más estable.",
            "skip": "Con niebla cerrada o lluvia, el empedrado se vuelve muy resbaladizo y no se ve el cráter: esperar al día siguiente.",
        },
        links=[
            {"label": "UNESCO · Parc Naturel Cova, Paúl et Ribeira da Torre (lista indicativa)", "url": "https://whc.unesco.org/en/tentativelists/6105/"},
            {"label": "IPC · Parque Natural de Cova, Paúl e Ribeira da Torre", "url": "https://ipc.cv/en/monumento-e-sitio/parque-natural-de-cova-paul-e-ribeira-da-torre-pncprt/"},
            {"label": "Wikipedia · Cova (cráter)", "url": "https://en.wikipedia.org/wiki/Cova_(crater)"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Santo_Ant%C3%A3o_294A8976_Cova.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Santo_Ant%C3%A3o_294A8976_Cova.jpg",
                "credit": "Christian Pirkl · CC BY-SA 4.0",
                "caption": "El cráter de la Cova.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Vale_do_Pa%C3%BAl,_Santo_Ant%C3%A3o,_Cape_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Vale_do_Pa%C3%BAl,_Santo_Ant%C3%A3o,_Cape_Verde.jpg",
                "credit": "CaptainDarwin · CC BY-SA 4.0",
                "caption": "El valle de Paúl.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/ValeRibeiraGrande.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:ValeRibeiraGrande.JPG",
                "credit": "CorreiaPM · Public domain",
                "caption": "El valle de Ribeira Grande.",
            },
        ],
    ),
    dict(
        n=9, name="Ponta do Sol y Fontainhas · los pueblos colgados del norte", cat="Naturaleza", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=17.192387, lon=-25.107441,  # Google Maps: Fontainhas
        desc="Fontainhas son 282 habitantes (censo de 2010) repartidos en un espolón a 158 m sobre el mar, con las casas encajadas en la ladera y las terrazas colgando del acantilado; es la imagen más repetida de Cabo Verde. Está a 2 km al suroeste de Ponta do Sol, LA CIUDAD MÁS SEPTENTRIONAL DEL PAÍS, un antiguo pueblo de pescadores que creció a partir de 1880 y conserva la iglesia de Nossa Senhora do Livramento (1894) y un cementerio judío. La carretera de cornisa hasta el mirador es estrecha, sin quitamiedos y con cruces difíciles.",
        dog_note="Sendero costero abierto; atado en el pueblo y vigilado en los tramos expuestos del acantilado.",
        visit={
            "why": "Por el mirador sobre Fontainhas y por el arranque del sendero costero más conocido del archipiélago, que sigue hasta Corvo, Formiguinhas y Cruzinha.",
            "see": "El caserío de Fontainhas sobre el espolón, las terrazas de caña sobre el acantilado, el puerto y el frente marítimo de Ponta do Sol.",
            "access": "Asfalto hasta Ponta do Sol desde Ribeira Grande; desde ahí, carretera estrecha de cornisa, parte empedrada, hasta el mirador de Fontainhas. Sitio para aparcar dos 4x4 solo en algún ensanche: mejor dejarlos en Ponta do Sol y caminar. Sin entrada. El pin marca el mirador sobre el pueblo, en la carretera.",
            "when": "Primera hora de la mañana, con el sol por el este iluminando el acantilado; al mediodía queda a contraluz.",
            "skip": "Con lluvia o viento fuerte, la cornisa y el sendero costero no son sitio para ir con prisa ni con perro suelto.",
        },
        links=[
            {"label": "Wikipedia · Fontainhas", "url": "https://en.wikipedia.org/wiki/Fontainhas"},
            {"label": "Wikipedia · Ponta do Sol, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Ponta_do_Sol,_Cape_Verde"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fontainhas.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fontainhas.jpg",
                "credit": "Kogo · GFDL",
                "caption": "Fontainhas, colgado sobre el mar.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Stra%C3%9Fe_nach_Fontainhas,_Santo_Antao.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Stra%C3%9Fe_nach_Fontainhas,_Santo_Antao.JPG",
                "credit": "Herbert wie · CC BY-SA 4.0",
                "caption": "El camino a Fontainhas.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Littoral_nord_de_Santo_Antao.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Littoral_nord_de_Santo_Antao.jpg",
                "credit": "Cadouf · CC BY-SA 4.0",
                "caption": "La costa norte de Santo Antão.",
            },
        ],
    ),
    dict(
        n=10, name="Tarrafal de Monte Trigo · el extremo seco de Santo Antão", cat="Costa", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=16.962416, lon=-25.305119,  # Google Maps: Tarrafal de Monte Trigo
        desc="En la esquina suroeste de Santo Antão, 841 habitantes (2010) viven entre el mar y las laderas peladas del Tope de Coroa, a 27 km al oeste de Porto Novo. El nombre viene del tarrafe (Tamarix senegalensis). Es la cara árida de la isla, sin nada del verde de Paúl. La carretera que lo conecta con Porto Novo se INAUGURÓ EN FEBRERO DE 2021: hasta entonces se llegaba en barca o andando. Sigue siendo un tramo largo, aislado y sin servicios; conviene ir con depósito lleno, agua y repuestos.",
        dog_note="Pueblo y playa de arena negra sin restricción conocida; atado por el ganado suelto.",
        visit={
            "why": "Es el rincón más aislado y menos turístico de Santo Antão, con playa de cantos y arena negra, aguas termales y una travesía costera de paisaje volcánico puro.",
            "see": "El caserío blanco entre la lava, la playa negra, los cocoteros del regadío y el macizo del Tope de Coroa (1.979 m) al fondo.",
            "access": "Desde Porto Novo, 27 km de carretera costera nueva desde 2021, con tramos estrechos y desprendimientos; apta para dos 4x4 pero sin gasolinera ni taller en destino. Aparcamiento informal a la entrada del pueblo. El pin marca el acceso a la playa del pueblo.",
            "when": "De noviembre a junio; evitar días de mar gruesa, que dejan la playa impracticable.",
            "skip": "Si el tiempo en Santo Antão es corto, Paúl y Ponta do Sol dan más por kilómetro recorrido.",
        },
        links=[
            {"label": "Wikipedia · Tarrafal de Monte Trigo", "url": "https://en.wikipedia.org/wiki/Tarrafal_de_Monte_Trigo"},
            {"label": "Wikipedia · Santo Antão, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Santo_Ant%C3%A3o,_Cape_Verde"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tarrafal_de_Monte_Trigo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tarrafal_de_Monte_Trigo.jpg",
                "credit": "Kogo · GFDL",
                "caption": "Tarrafal de Monte Trigo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Beach_at_Tarrafal_de_Monte_Trigo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Beach_at_Tarrafal_de_Monte_Trigo.jpg",
                "credit": "Mar Tranquilidade · CC BY-SA 4.0",
                "caption": "La playa negra de Monte Trigo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/P%C3%AAche_traditionnelle_%C3%A0_Tarafal_de_Monte_Trigo,_%C3%AEle_de_Santo_Antao,_Cap-Vert.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:P%C3%AAche_traditionnelle_%C3%A0_Tarafal_de_Monte_Trigo,_%C3%AEle_de_Santo_Antao,_Cap-Vert.jpg",
                "credit": "Julien saison · CC BY-SA 4.0",
                "caption": "Pesca artesanal en Monte Trigo.",
            },
        ],
    ),
    dict(
        n=11, name="Chã das Caldeiras y el Pico do Fogo · vivir dentro de un volcán", cat="Naturaleza", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=14.9675732, lon=-24.3745152,  # Google Maps: Chã das Caldeiras
        desc="Dentro de una caldera de unos 10 por 7 km vive la ALDEA MÁS ALTA DE CABO VERDE, a unos 1.700 m: Portela y Bangaeira, con 697 habitantes en 2010. El Pico do Fogo, de 2.829 m, es el techo del país. La erupción del 23 de noviembre de 2014 al 8 de febrero de 2015 destruyó el 75 % de las casas de Portela, Bangaeira e Ilhéu de Losna y obligó a evacuar a unas mil personas; el pueblo se reconstruyó sobre la lava. Toda la caldera, 67 km², está protegida. La ascensión al pico exige guía local y sale de noche.",
        dog_note="Parque natural con acceso regulado y ascensión sobre lapilli cortante: mal terreno para almohadillas y difícil de justificar ante los guardas.",
        visit={
            "why": "No hay nada comparable en el Atlántico medio: un pueblo reconstruido sobre su propia colada, viñedos entre lapilli y el volcán activo encima.",
            "see": "El anillo de la Bordeira a 2.700 m, el cono del Pico do Fogo, las casas enterradas por la lava de 2014-2015, los viñedos y las bodegas de manecom y Adega de Monte Barro.",
            "access": "Asfalto y empedrado desde São Filipe hasta la entrada de la caldera; el último tramo, sobre lava reconstruida, es pista irregular pero pasable con 4x4. Hay sitio para aparcar en Portela. Entrada al parque y guía obligatorio para el pico: tarifas por confirmar en la sede del Parque Natural do Fogo. El pin marca el núcleo de Portela, dentro de la caldera.",
            "when": "Ascensión de madrugada para llegar a la cumbre al amanecer; temporada seca, de noviembre a junio. En Chã hace frío de noche.",
            "skip": "Con aviso de actividad volcánica o con viento fuerte y ceniza en suspensión, el parque cierra el acceso al cono.",
        },
        links=[
            {"label": "Wikipedia · Chã das Caldeiras", "url": "https://en.wikipedia.org/wiki/Ch%C3%A3_das_Caldeiras"},
            {"label": "Wikipedia · Pico do Fogo", "url": "https://en.wikipedia.org/wiki/Pico_do_Fogo"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cape_Verde_Fogo_landscape_with_Pico_do_Fogo_road.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cape_Verde_Fogo_landscape_with_Pico_do_Fogo_road.jpg",
                "credit": "Cayambe · CC BY-SA 3.0",
                "caption": "El Pico do Fogo desde la pista de Chã.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cape_Verde_Fogo_Ch%C3%A3_das_Caldeiras_school.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cape_Verde_Fogo_Ch%C3%A3_das_Caldeiras_school.jpg",
                "credit": "Cayambe · CC BY-SA 3.0 lu",
                "caption": "La escuela de Chã das Caldeiras.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ch%C3%A3_das_Caldeiras-Vinho_do_Fogo_(5).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ch%C3%A3_das_Caldeiras-Vinho_do_Fogo_(5).jpg",
                "credit": "Ji-Elle · CC BY-SA 3.0",
                "caption": "El vino de Chã das Caldeiras.",
            },
        ],
    ),
    dict(
        n=12, name="São Filipe (Fogo) · los sobrados y la playa negra", cat="Cultura", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=14.896811, lon=-24.4934927,  # Google Maps: São Filipe
        desc="São Filipe es la ciudad colonial mejor conservada del archipiélago después de Cidade Velha: EL 70 % DE LAS CASAS DEL CENTRO son del siglo XIX y se conservan medio centenar de sobrados, las casonas de dos plantas con patio y balcón corrido. La Casa da Memória ocupa una casa de comerciante de 1820 en la Praça 12 de Setembro, junto al Museu Municipal, con jardín de plantas endémicas de Fogo y un funco reconstruido en piedra volcánica. Abajo, a 40 m, la Praia da Bila, de arena negra: sucia algunos días y con mar duro.",
        dog_note="Calles y playa sin restricción conocida; Casa da Memória y Museu Municipal, no.",
        visit={
            "why": "Es la puerta de entrada a Fogo y el conjunto de arquitectura civil portuguesa más completo del país, con dos museos pequeños pero bien montados.",
            "see": "Los sobrados del centro, la Praça 12 de Setembro, la Casa da Memória, el Museu Municipal con su funco de piedra volcánica y la playa negra al pie del acantilado.",
            "access": "Asfalto desde el puerto y el aeropuerto; calles estrechas en el centro, mejor aparcar en la periferia de la plaza. Horario y entrada de los museos, por confirmar. El pin marca la Casa da Memória, en la Praça 12 de Setembro.",
            "when": "Final de la tarde, cuando la luz cae sobre las fachadas; abril para las Bandeiras de São Filipe (fecha por confirmar).",
            "skip": "Si se va directo a Chã das Caldeiras y el tiempo aprieta, se puede reducir a dos horas de paseo.",
        },
        links=[
            {"label": "Wikipedia · São Filipe, Cabo Verde", "url": "https://en.wikipedia.org/wiki/S%C3%A3o_Filipe,_Cape_Verde"},
            {"label": "Instituto do Património Cultural de Cabo Verde", "url": "https://ipc.cv/"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sao_Filipe_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sao_Filipe_Cabo_Verde.jpg",
                "credit": "Iwoelbern · Public domain",
                "caption": "São Filipe, en Fogo.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Fogo_S%C3%A3o_Filipe_houses.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Fogo_S%C3%A3o_Filipe_houses.jpg",
                "credit": "Cayambe · CC BY-SA 3.0",
                "caption": "Sobrados de São Filipe.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/S%C3%A3o_Filipe-Vins_de_Fogo.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:S%C3%A3o_Filipe-Vins_de_Fogo.jpg",
                "credit": "Ji-Elle · CC BY-SA 3.0",
                "caption": "Los vinos de Fogo.",
            },
        ],
    ),
    dict(
        n=13, name="Brava y Vila Nova Sintra · la isla de las flores", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="1–2 noches",
        lat=14.871038, lon=-24.6949966,  # Google Maps: Nova Sintra
        desc="Brava es la isla habitada más pequeña, 62,51 km² y 5.698 habitantes (2015), y la más verde del archipiélago; su punto más alto es el Monte Fontainhas, de 976 m. Nova Sintra, la capital, está a 520 m y lleva el nombre de la Sintra de los reyes portugueses. En la plaza Eugénio Tavares se conserva la casa del poeta, hoy museo, y frente al banco crece un dragoeiro (Dracaena draco). SOLO SE LLEGA EN FERRI: el aeropuerto de Esperadinha, inaugurado en 1992, cerró en 2004 por los vientos. El puerto es Furna, con enlaces a Fogo y Santiago.",
        dog_note="Calles y caminos abiertos; la casa-museo de Eugénio Tavares, no. Embarque en ferri con perro, por confirmar con la naviera.",
        visit={
            "why": "Es la isla menos visitada y la más fértil, con caminos empedrados entre hortensias y buganvillas y ningún turismo de masas.",
            "see": "Nova Sintra y su plaza, la casa-museo de Eugénio Tavares, el dragoeiro junto al banco, el descenso en cornisa al puerto de Furna y la bahía de Fajã d'Água.",
            "access": "Solo por mar, desde Vale de Cavaleiros (Fogo) y Praia; la travesía tiene fama de dura y las cancelaciones por mar gruesa son frecuentes. Desde Furna, una carretera empedrada de fuerte pendiente sube a Nova Sintra. Aparcar dos 4x4 en la plaza es posible fuera de horas de mercado. El pin marca la Praça Eugénio Tavares, centro de Nova Sintra.",
            "when": "De septiembre a noviembre, con la isla más verde tras las lluvias; comprobar el parte de mar antes de embarcar.",
            "skip": "Si el calendario es ajustado: un ferri cancelado puede dejar los vehículos bloqueados varios días.",
        },
        links=[
            {"label": "Wikipedia · Brava, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Brava,_Cape_Verde"},
            {"label": "Wikipedia · Nova Sintra", "url": "https://en.wikipedia.org/wiki/Nova_Sintra"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cidade_de_Nova_Sintra,_ilha_Brava_-_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cidade_de_Nova_Sintra,_ilha_Brava_-_Cabo_Verde.jpg",
                "credit": "TxetxeCV · CC BY-SA 4.0",
                "caption": "Nova Sintra, en Brava.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Faj%C3%A3_d'%C3%A1gua,_Ilha_Brava_-_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Faj%C3%A3_d'%C3%A1gua,_Ilha_Brava_-_Cabo_Verde.jpg",
                "credit": "TxetxeCV · CC BY-SA 4.0",
                "caption": "Fajã d'Água, en la costa de Brava.",
            },
        ],
    ),
    dict(
        n=14, name="Santa Maria (Sal) · la playa, el muelle y la pesca", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=16.5967453, lon=-22.9075449,  # Google Maps: Pontão de Santa Maria
        desc="Santa Maria nació del comercio de sal —hubo un muelle de embarque en Ponta de Vera Cruz— y vive hoy del turismo: el primer hotel de playa, el Morabeza, abrió en 1967 y EN 2017 LA ISLA DE SAL CONCENTRABA EL 48,2 % DE LAS PLAZAS HOTELERAS DEL PAÍS. La playa es de arena clara y kilómetros de largo, con viento constante que la ha convertido en centro de kitesurf. En el pontão se descarga y se despieza el pescado a media mañana, con los mejores momentos del pueblo. Fuera del casco, las pistas de tierra levantan mucho polvo.",
        dog_note="Playa pública y muelle sin restricción conocida; playas de resort y establecimientos, según el hotel.",
        visit={
            "why": "Es la playa más accesible del archipiélago y la mejor base para el viento: kite, windsurf y pesca de altura.",
            "see": "La playa larga de arena clara, el pontão con la subasta informal de pescado, las casas de colores del casco y las salinas del interior.",
            "access": "Asfalto desde el aeropuerto de Espargos, unos 18 km. Aparcamiento de tierra a la entrada del casco y en el paseo; el centro es peatonal en buena parte. Sin entrada. El pin marca el pontão (muelle) de Santa Maria, el punto al que se conduce.",
            "when": "Media mañana para la descarga de pescado; de noviembre a marzo para el viento fuerte del kite.",
            "skip": "Si se busca costa salvaje y no resorts, Boa Vista da lo mismo con menos hormigón.",
        },
        links=[
            {"label": "Wikipedia · Santa Maria, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Santa_Maria,_Cape_Verde"},
            {"label": "Wikipedia · Sal, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Sal,_Cape_Verde"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Santa_Maria_Sal_Cabo_Verde2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Santa_Maria_Sal_Cabo_Verde2.jpg",
                "credit": "Adrião · CC BY 3.0",
                "caption": "Santa Maria, en Sal.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/20231226_113956_Santa_Maria,_Sal,_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:20231226_113956_Santa_Maria,_Sal,_Cabo_Verde.jpg",
                "credit": "Tbo47 · CC0",
                "caption": "El muelle de Santa Maria.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Santa_Maria_2_(Sal,_Cabo_Verde).JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Santa_Maria_2_(Sal,_Cabo_Verde).JPG",
                "credit": "Manuel de Sousa · CC BY-SA 3.0",
                "caption": "La playa de Santa Maria.",
            },
        ],
    ),
    dict(
        n=15, name="Pedra de Lume · el cráter de las salinas", cat="Cultura", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=16.7682648, lon=-22.8964426,  # Google Maps: Salinas de Pedra de Lume
        desc="Dentro del cráter de un volcán extinto, unas salinas alimentadas por agua que asciende desde el subsuelo —no por filtración lateral del mar— forman un paisaje blanco y rosa al que se entra por un TÚNEL EXCAVADO EN 1804 a través de la pared del cráter. La explotación arrancó en 1796 con Manuel António Martins y se hundió cuando Brasil prohibió la sal importada en 1887; en 1921 los franceses de Salins du Cap Vert instalaron un teleférico de 1.100 m. Hoy la producción va a cosmética y talasoterapia, y se puede flotar en las balsas.",
        dog_note="Recinto de pago con pasarelas y salmuera; la sal irrita almohadillas y ojos. Mejor dejarlo en el vehículo a la sombra o no ir con él.",
        visit={
            "why": "Es el sitio industrial más fotogénico del país y el único lugar donde se flota en salmuera dentro de un cráter volcánico.",
            "see": "El túnel de 1804, las balsas de evaporación de colores cambiantes, los restos del teleférico de 1921 y el anillo del cráter.",
            "access": "Asfalto desde Espargos, unos 7 km, y ramal corto de tierra hasta el aparcamiento, amplio y sin problema para dos 4x4. Recinto de pago con horario diurno; importe por confirmar. El pin marca la taquilla y la boca del túnel, no el fondo del cráter.",
            "when": "Primera hora de la mañana: al mediodía el cráter es un horno sin sombra y llegan los autocares.",
            "skip": "Con cruceros en Palmeira el recinto se llena; en ese caso, ir a última hora de la tarde.",
        },
        links=[
            {"label": "Wikipedia · Pedra de Lume", "url": "https://en.wikipedia.org/wiki/Pedra_de_Lume"},
            {"label": "Wikipedia · Sal, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Sal,_Cape_Verde"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pedra_Lume_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pedra_Lume_Cabo_Verde.jpg",
                "credit": "Ingo Wölbern · Public domain",
                "caption": "Las salinas de Pedra de Lume.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Pedra_Lume,_Salinas_2007.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Pedra_Lume,_Salinas_2007.jpg",
                "credit": "Ingo Wölbern · Public domain",
                "caption": "El cráter de Pedra de Lume.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Salt_Pedra_Lume.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Salt_Pedra_Lume.jpg",
                "credit": "Ingo Wölbern · Public domain",
                "caption": "Sal amontonada en Pedra de Lume.",
            },
        ],
    ),
    dict(
        n=16, name="Praia de Santa Mónica y el desierto de Viana (Boa Vista)", cat="Costa", prio="Alta",
        dog="permitido con condiciones", time="1 noche",
        lat=16.0012526, lon=-22.9194076,  # Google Maps: Praia de Santa Mónica
        desc="Santa Mónica es la gran playa vacía del suroeste de Boa Vista, pegada a la reserva natural de Morro de Areia, importante para aves endémicas y tortugas. El pueblo más cercano es Povoação Velha, 5 km al norte. En el interior, el DESERTO DE VIANA es un campo de dunas considerado una de las siete maravillas naturales del país, junto a la reserva de Boa Esperança, que incluye la Lagoa do Rabil. Sin sombra, sin servicios y con corriente: conviene no bañarse solo y llevar agua para todo el día.",
        dog_note="Playa de nidificación de tortugas: correa obligatoria de hecho y prohibido acercarse a los nidos o salir de noche en temporada.",
        visit={
            "why": "Kilómetros de arena sin una sola construcción y, a media hora, un campo de dunas en mitad del Atlántico: el contraste que define Boa Vista.",
            "see": "La playa abierta de Santa Mónica, la reserva de Morro de Areia al norte, las dunas del Deserto de Viana y, cerca, la Lagoa do Rabil.",
            "access": "Desde Sal Rei, asfalto hasta Povoação Velha y pista de arena y roca los últimos kilómetros hasta la playa: 4x4 recomendable y reducida útil en los arenales. Al Deserto de Viana se entra por pista desde la carretera de Rabil. Sin entrada ni vigilancia. El pin marca el acceso rodado a la playa desde Povoação Velha.",
            "when": "Mañana temprano o última hora de la tarde; de junio a octubre hay desove de tortugas y el acceso nocturno está restringido.",
            "skip": "Con harmattan y polvo sahariano en suspensión no se ve nada y la arena es insoportable.",
        },
        links=[
            {"label": "Wikipedia · Praia de Santa Mónica", "url": "https://en.wikipedia.org/wiki/Praia_de_Santa_M%C3%B3nica"},
            {"label": "Wikipedia · Deserto de Viana", "url": "https://en.wikipedia.org/wiki/Deserto_de_Viana"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Praia_de_Santa_M%C3%B3nica.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Praia_de_Santa_M%C3%B3nica.JPG",
                "credit": "Adrião · CC BY 3.0",
                "caption": "La praia de Santa Mónica.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Deserto_Viana,_Boa_Vista.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Deserto_Viana,_Boa_Vista.jpg",
                "credit": "Ingo Wölbern · Public domain",
                "caption": "El deserto de Viana.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Deserto_de_Viana_(Boa_Vista).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Deserto_de_Viana_(Boa_Vista).jpg",
                "credit": "Felitsata · CC BY-SA 3.0",
                "caption": "Dunas del deserto de Viana.",
            },
        ],
    ),
    dict(
        n=17, name="Sal Rei y la costa de Boa Vista · las tortugas y los naufragios", cat="Ciudad · servicios", prio="Media",
        dog="permitido con condiciones", time="1 noche",
        lat=16.1791389, lon=-22.9237431,  # Google Maps: Porto de Sal Rei
        desc="Sal Rei —«sal del rey»— es la capital de Boa Vista, 5.778 habitantes en 2010, y vivió de la sal antes que del turismo. Frente al puerto está el ilhéu de Sal Rei con el FORTE DUQUE DE BRAGANÇA, levantado tras los asaltos piratas de 1815 y 1817. El puerto, con muelle nuevo desde 2015, enlaza con Santiago, Sal y Maio. La isla tiene 14 ÁREAS PROTEGIDAS, varias de ellas playas de desove de tortuga boba. El turismo se concentra en la Praia de Cabral. Para ver tortugas hay que ir con operador autorizado: acercarse por libre está prohibido.",
        dog_note="Pueblo y playa urbana con correa; en las playas de desove, restricciones estacionales y prohibición de acceso nocturno.",
        visit={
            "why": "Es la base logística de Boa Vista —ferri, combustible, comida— y el punto de partida de las salidas a las playas de tortugas y a los naufragios de la costa este.",
            "see": "El frente marítimo y la Praia de Cabral, el ilhéu de Sal Rei con el Forte Duque de Bragança, el puerto y la plaza del pueblo.",
            "access": "Asfalto desde el aeropuerto de Rabil, unos 6 km; el resto de la isla se recorre por pistas de arena y piedra que exigen 4x4. Hay aparcamiento amplio junto al puerto y en la entrada del casco. El pin marca el puerto de Sal Rei, donde atracan los ferris.",
            "when": "De junio a octubre para el desove de tortugas, siempre con guía autorizado; el resto del año, cualquier momento.",
            "skip": "Si ya se han visto Sal y sus salinas, Boa Vista repite esquema con menos servicios.",
        },
        links=[
            {"label": "Wikipedia · Sal Rei", "url": "https://en.wikipedia.org/wiki/Sal_Rei"},
            {"label": "Wikipedia · Boa Vista, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Boa_Vista,_Cape_Verde"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sal_Rei,_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sal_Rei,_Cabo_Verde.jpg",
                "credit": "Ingo Wölbern · Public domain",
                "caption": "Sal Rei, en Boa Vista.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sal_Rei_Port.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sal_Rei_Port.jpg",
                "credit": "Kojote · CC BY-SA 3.0",
                "caption": "El puerto de Sal Rei.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sal_Rei_Beach.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sal_Rei_Beach.jpg",
                "credit": "Kojote · CC BY-SA 3.0",
                "caption": "La playa de Sal Rei.",
            },
        ],
    ),
    dict(
        n=18, name="São Nicolau y el Monte Gordo · la isla del dragoeiro", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="1–2 noches",
        lat=16.6220426, lon=-24.3362671,  # Google Maps: Parque Natural do Monte Gordo
        desc="São Nicolau es la isla que nadie visita y la más arbolada del norte: 343 km² con el Monte Gordo, de 1.312 m, cubierto de pinos, eucaliptos y cipreses. El parque natural, creado EL 24 DE FEBRERO DE 2003, protege 9,52 km² con seis especies vegetales endémicas —entre ellas Aeonium gorgoneum y Campanula jacobaea— y fauna como la lagartija de São Nicolau y el gon-gon; es Área Importante para las Aves. La capital, Ribeira Brava (1.936 hab. en 2010), fue sede episcopal entre 1786 y 1943 y conserva su Seminário-Liceu de 1866.",
        dog_note="Parque natural sin grandes depredadores, pero con lagartos y aves endémicas: atado obligatorio fuera de las pistas.",
        visit={
            "why": "Es la isla más tranquila del archipiélago y la única donde se combinan bosque de altura, pueblos coloniales intactos y ausencia total de turismo.",
            "see": "El macizo del Monte Gordo y sus senderos, el valle y el casco colonial de Ribeira Brava con el Seminário-Liceu, y los dragoeiros dispersos por el interior.",
            "access": "Se llega en ferri desde Mindelo o São Vicente y en avión a Preguiça; las carreteras principales son asfalto y empedrado, con ramales de pista. La subida al parque desde Cachaço tiene explanadas donde caben dos 4x4. Entrada y horario del parque, por confirmar. El pin marca el acceso al parque desde Cachaço.",
            "when": "De septiembre a noviembre, cuando la isla está verde; la niebla de cumbre es frecuente por la tarde.",
            "skip": "Si los enlaces de ferri no cuadran: São Nicolau es fácil de alcanzar y difícil de abandonar en fecha fija.",
        },
        links=[
            {"label": "Wikipedia · Monte Gordo Natural Park", "url": "https://en.wikipedia.org/wiki/Monte_Gordo_Natural_Park"},
            {"label": "Wikipedia · Ribeira Brava, Cabo Verde", "url": "https://en.wikipedia.org/wiki/Ribeira_Brava,_Cape_Verde"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/View_Ribeira_Brava_S%C3%A3o_Nicolau,_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:View_Ribeira_Brava_S%C3%A3o_Nicolau,_Cabo_Verde.jpg",
                "credit": "Herbert wie · CC BY-SA 4.0",
                "caption": "Ribeira Brava, en São Nicolau.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Seminary_Ribeira_Brava_S%C3%A3o_Nicolau,_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Seminary_Ribeira_Brava_S%C3%A3o_Nicolau,_Cabo_Verde.jpg",
                "credit": "Herbert wie · CC BY-SA 4.0",
                "caption": "El seminario de Ribeira Brava.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Porto_do_Tarrafal_S%C3%A3o_Nicolau,_Cabo_Verde.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Porto_do_Tarrafal_S%C3%A3o_Nicolau,_Cabo_Verde.jpg",
                "credit": "Herbert wie · CC BY-SA 4.0",
                "caption": "El puerto de Tarrafal de São Nicolau.",
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
    ("Aeropuerto Internacional Amílcar Cabral (SID) — Sal", "Frontera", 16.7345785, -22.9439763,  # Google Maps: Aeropuerto Amílcar Cabral
     "Principal aeropuerto internacional del país y hub de Cabo Verde Airlines, 2 km al oeste-suroeste de Espargos. Pista de 3.272 m. Control de la DEF: aquí se verifica el pre-registro EASE y el pago de la TSA. Pin comprobado en Google Maps («Aeropuerto Amílcar Cabral»)."),
    ("Aeropuerto Internacional Nelson Mandela (RAI) — Praia", "Frontera", 14.9449232, -23.4861872,  # Google Maps: Aeropuerto Internacional Nelson Mandela
     "Aeropuerto de la capital, 3 km al noreste de Praia, abierto en 2005 y gestionado por Vinci Airports desde julio de 2023. Vuelos a Lisboa, París, Zúrich, Ámsterdam, Casablanca, Dakar y Luanda. Pin comprobado en Google Maps («Aeropuerto Internacional Nelson Mandela»)."),
    ("Puerto de Porto Novo — Santo Antão", "Frontera", 17.0215176, -25.0673575,  # Google Maps: Porto Novo (Santo Antão)
     "Terminal del ferry de CV Interilhas con Mindelo: cuatro conexiones diarias, unos 60 minutos, buque Chiquinho, admite vehículos. Única vía de acceso a Santo Antão, que no tiene aeropuerto operativo. Pin comprobado en Google Maps («Porto Novo (Santo Antão)»)."),
    ("Embajada de España en Praia", "Consular", 14.908051, -23.5175979,  # Google Maps: Embajada de España en Cabo Verde
     "Rua de Espanha, 1, Achada de Santo António, Praia. Tel. +238 260 1800 / 1801 / 1802 / 1803, fax +238 262 1322. EMERGENCIA CONSULAR 24 H: +238 991 0124. emb.praia@maec.es (visados: emb.praia.vis@maec.es). Viceconsulados honorarios en Mindelo (+238 231 74 81), Santa Maria/Sal (+238 242 20 61) y Sal Rei/Boa Vista (+238 251 19 15). Pin comprobado en Google Maps («Embajada de España en Cabo Verde»)."),
    ("Hospital Agostinho Neto — Praia", "Hospital", 14.9203286, -23.5054786,  # Google Maps: Hospital Agostinho Neto
     "Hospital público de referencia de Santiago y del país. Tel. +238 333 76 50; urgencias +238 260 21 69. Red sanitaria muy precaria frente a la europea: para casos graves, evacuación aérea medicalizada a Europa. Pin comprobado en Google Maps («Hospital Agostinho Neto»)."),
    ("Hospital Dr. Baptista de Sousa — Mindelo", "Hospital", 16.8843064, -24.9848207,  # Google Maps: Hospital Dr. Baptista de Sousa
     "Hospital de referencia de São Vicente y de las islas de Barlavento, incluida Santo Antão. Urgencias +238 232 73 55. Pin comprobado en Google Maps («Hospital Dr. Baptista de Sousa»)."),
    ("Hospital do Sal — Espargos", "Hospital", 16.7489327, -22.9353854,  # Google Maps: Hospital do Sal
     "Hospital de referencia de la isla de Sal, la más turística. Urgencias +238 241 11 30. Hay además clínicas privadas en Santa Maria. NO hay cámara hiperbárica en todo el país. Pin comprobado en Google Maps («Hospital do Sal»)."),
    ("Estaciones de servicio de Espargos y Santa Maria — Sal", "Combustible", 16.7560469, -22.9386472,  # Google Maps: Espargos (sin gasolinera concreta como objeto)
     "Eje con la mejor densidad de gasolineras del país, sobre la autovía Espargos–Santa Maria. Precios máximos oficiales de septiembre de 2026: gasolina 175,40 CVE/l, gasóleo 169,40 CVE/l (ARME). Pin comprobado en Google Maps («Espargos (sin gasolinera concreta como objeto)»)."),
    ("Palmeira — puerto de combustible de Sal", "Combustible", 16.7555873, -22.9824523,  # Google Maps: Porto de Palmeira
     "Puerto de suministro de combustible del archipiélago y puesto de control marítimo de la DEF. Desde aquí se redistribuye el carburante al resto de islas. Pin comprobado en Google Maps («Porto de Palmeira»)."),
    ("Red de agua de ELECTRA — Praia", "Agua potable", 14.9159545, -23.5102665,  # Google Maps: ELECTRA (Praia)
     "ELECTRA es el operador nacional de agua y electricidad; más del 70 % del agua potable del país se produce por desalinización. El agua de red sirve para ducha y lavado, NO para beber: agua embotellada siempre (MAEC). Pin comprobado en Google Maps («ELECTRA (Praia)»)."),
    ("Red de agua de ELECTRA — Mindelo", "Agua potable", 16.8839948, -24.9874331,  # Google Maps: Mindelo
     "Punto de referencia para llenar depósitos en São Vicente antes de cruzar a Santo Antão, donde el abastecimiento rural es más irregular. Agua desalinizada, dura y no potable sin tratar. Pin comprobado en Google Maps («Mindelo»)."),
]

DRONE_CALLOUT = ("warn", "DRONES: legales con límites claros, pero la AAC manda",
                 "Cabo Verde no prohíbe los drones. La Agência de Aviação Civil (AAC) permite volar SIN autorización si se cumplen a la vez cuatro condiciones: por debajo de 120 m, fuera de áreas restringidas, con el operador a menos de 100 m y control directo, y con buena visibilidad. Fuera de ese sobre hace falta autorización escrita, presentando el formulario de servidumbre aeronáutica con AL MENOS 10 DÍAS HÁBILES de antelación. Prohibido volar a menos de 2.000 m de un aeródromo y sobre rutas de tráfico aéreo. No se exige registro ni licencia al turista.")

STARLINK_CALLOUT = ("", "STARLINK: autorizado y operativo desde diciembre de 2024",
                    "Cabo Verde es de los pocos países africanos donde Starlink está plenamente legalizado. La ARME, el regulador multisectorial, autorizó el 11 de octubre de 2024 a Starlink Cabo Verde, Lda a prestar servicios de comunicaciones electrónicas EN TODO EL TERRITORIO NACIONAL, y el servicio se abrió al público a finales de diciembre de 2024. En el mismo marco autorizó a Airtel y a Ed Solutions. Para un viaje sin vehículo propio es poco relevante: la cobertura 4G de Unitel T+ y CVMóvel cubre los núcleos habitados de las nueve islas.")

DOG_MATRIX = [
    ("Entrada al país (aeropuertos internacionales)", "permitido con condiciones", "Certificado veterinario oficial (validez 10 días), microchip, rabia y serología ≥0,5 UI/ml a los 30 días. Pedir el atestado previo a la Embajada de Cabo Verde en Madrid con semanas de margen."),
    ("Vuelos interinsulares (TICV/Bestfly)", "por confirmar", "Política de animales en cabina y bodega no documentada en fuente abierta. Plan B: mover al perro por ferry de CV Interilhas o limitar el viaje a una sola isla."),
    ("Ferry Mindelo–Porto Novo (Santo Antão)", "por confirmar", "El enlace admite vehículos y es corto (60 min), pero no hay norma publicada sobre perros. Preguntar a CV Interilhas en taquilla; plan B, llevarlo en transportín en cubierta."),
    ("Senderismo en Santo Antão y Fogo", "no recomendado", "Roca volcánica abrasiva, desniveles largos y calor: destroza almohadillas y deshidrata. Plan B: botines, rutas cortas al amanecer y dejarlo en la casa rural los días de travesía larga."),
    ("Playas y hoteles de Sal y Boa Vista", "por confirmar", "El grueso del alojamiento son resorts que no suelen admitir animales. Plan B: apartamentos y guesthouses en Santa Maria y Sal Rei que sí lo hagan, reservados con antelación."),
    ("Regreso a la UE desde cualquier aeropuerto", "permitido con condiciones", "País NO listado en el anexo II del Reg. (UE) 2026/636: titulación antirrábica previa anotada en el pasaporte antes de salir de España. Plan B si no se hizo: titulación en destino y 3 meses de espera."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Cabo Verde — Ministerio de Asuntos Exteriores, UE y Cooperación (consultada 18/09/2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Cabo%20Verde"),
    ("EASE · Pré-registo de Viajantes — Gobierno de Cabo Verde (consultada 18/09/2026)", "https://www.ease.gov.cv/"),
    ("Taxa de «Segurança Aeroportuária»: pagamento no aeroporto custa o dobro em 2026 — Caboverde24, 28/02/2026", "https://caboverde24.info/2026/02/28/taxa-de-seguranca-aeroportuaria-pagamento-no-aeroporto-custa-o-dobro-em-2026/"),
    ("Cabo Verde substitui vistos para europeus por um sistema de pré-registo e uma taxa de segurança aeroportuária — EEAS, Unión Europea, enero de 2019 (archivado)", "https://www.eeas.europa.eu/node/56170_en"),
    ("Cape Verde — Wikipedia (consultada 18/09/2026)", "https://en.wikipedia.org/wiki/Cape_Verde"),
    ("Transport in Cape Verde — Wikipedia (consultada 18/09/2026)", "https://en.wikipedia.org/wiki/Transport_in_Cape_Verde"),
    ("Nelson Mandela International Airport — Wikipedia (consultada 18/09/2026)", "https://en.wikipedia.org/wiki/Nelson_Mandela_International_Airport"),
    ("Amílcar Cabral International Airport — Wikipedia (consultada 18/09/2026)", "https://en.wikipedia.org/wiki/Am%C3%ADlcar_Cabral_International_Airport"),
    ("Porto Novo, Cape Verde — Wikipedia (consultada 18/09/2026)", "https://en.wikipedia.org/wiki/Porto_Novo,_Cape_Verde"),
    ("Cidade Velha, Historic Centre of Ribeira Grande — UNESCO World Heritage Centre, inscrita en 2009", "https://whc.unesco.org/en/list/1310/"),
    ("Cabo Verde: Freedom in the World 2025 — Freedom House, 2025 (92/100, Free)", "https://freedomhouse.org/country/cabo-verde/freedom-world/2025"),
    ("Cape Verde travel advice: safety and security — FCDO, Reino Unido (consultada 18/09/2026)", "https://www.gov.uk/foreign-travel-advice/cape-verde/safety-and-security"),
    ("Drones — Agência de Aviação Civil (AAC) de Cabo Verde (consultada 18/09/2026)", "https://www.aac.cv/artigos/drones"),
    ("Cape Verde Drone Laws 2026 — Drone-Laws.com, 2026", "https://drone-laws.com/drone-laws-in-cape-verde/"),
    ("ARME autoriza primeiros serviços via satélite em Cabo Verde — ARME, 16/10/2024 (decisión de 11/10/2024)", "https://www.arme.cv/index.php?option=com_content&view=article&id=1128%3Aarme-autoriza-primeiros-servicos-via-satelite-em-cabo-verde&catid=79&Itemid=878"),
    ("ARME atualiza preços máximos dos combustíveis para setembro 2026 — ARME, septiembre de 2026", "https://www.arme.cv/index.php/noticia-geral/1399-arme-atualiza-precos-maximos-dos-combustiveis-para-setembro-2026"),
    ("Certificação sanitária para Cabo Verde — cães e gatos (MOD 970-DGV-01-2012) — DGAV, Portugal", "https://www.dgav.pt/wp-content/uploads/2021/04/CERTIFICACAO-SANITARIA-CABO-VERDE-CAES-E-GATOS.pdf"),
    ("Viagem com animais — Embaixada da República de Cabo Verde no Brasil (consultada 18/09/2026)", "http://www.embcv.org.br/portal/viagem-com-animais/"),
    ("Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026 (listas de terceros países para desplazamientos de animales de compañía; aplicable desde el 22/04/2026) — EUR-Lex", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("Send my Campervan by shipping or ferry to Cape Verde — foro de Expat.com, Cabo Verde", "https://www.expat.com/en/forum/africa/cape-verde/1065960-send-my-campervan-by-shipping-or-ferry-to-cape-verde.html"),
    ("CV Interilhas 2026 Schedule — All Routes, Times & Prices — Ondas.cv, 2026", "https://www.ondas.cv/cv-interilhas"),
    ("Carnet de Passages en Douane: Cape Verde — carnetdepassage.org (AIT/FIA), consultada 18/09/2026", "https://www.carnetdepassage.org/country/cape-verde"),
    ("112 Cabo Verde é o número único de emergência — Governo de Cabo Verde", "https://www.governo.cv/112-cabo-verde-e-o-numero-unico-de-emergencia/"),
    ("Carlos Ramos destaca desafio de tornar a água acessível em Cabo Verde quando «mais de 70% é produzida por dessalinização» — JM Madeira", "https://www.jm-madeira.pt/not%C3%ADcias/regi-o/17826135/carlos-ramos-destaca-desafio-de-tornar-a-agua-acessivel-em-cabo-verde-quando-mais-de-70-e-produzida-por-dessalinizacao.html"),
    ("Hiking in Santo Antão: Cape Verde's Mountain Paradise — Erika's Travels", "https://www.erikastravels.com/hiking-santo-antao-cape-verde/"),
    ("Travel Guide to Santo Antão, A Wonderland For Hikers — Indie Traveller", "https://www.indietraveller.co/santo-antao-travel-guide/"),
    ("Walking in Santo Antão — CapeVerde.co.uk", "https://www.capeverde.co.uk/blog/walking-in-santo-antao"),
    ("18 Top Hikes in Santo Antao, Cape Verde — Paulina on the Road", "https://paulinaontheroad.com/6-top-hikes-in-santo-antao-cape-verde-travel-trekking/"),
    ("Trekking in Cabo Verde: Santo Antão, São Vicente and Fogo — Kuluar", "https://kuluarpohod.com/en/routes/cabo-verde-trekking/"),
    ("Cape Verde: Fogo and Santo Antão — CapeVerde.com", "https://www.capeverde.com/holidays-travel/individual-round-trips/fogo-and-santo-antao"),
    ("SIM Cards in Cape Verde: The Best Prepaid Plans, 2025 Guide — Phone Travel Wiz", "https://www.phonetravelwiz.com/buying-a-sim-card-in-cape-verde-guide/"),
    ("ELECTRA — operador nacional de agua y electricidad de Cabo Verde", "https://www.electra.cv/"),
    ("Left- and right-hand traffic — Wikipedia (Cabo Verde: RHT desde 1928), consultada 18/09/2026", "https://en.wikipedia.org/wiki/Left-_and_right-hand_traffic"),
    ("Direção Geral das Alfândegas — Direção Nacional das Receitas de Estado, Ministério das Finanças de Cabo Verde (consultada 18/09/2026)", "https://www.mf.gov.cv/web/dnre/direca-geral-das-alfandegas"),
    ("Mindelo → Porto Novo Ferry 2026: Schedule, Prices & Times — Ondas.cv, 2026", "https://www.ondas.cv/routes/mindelo-porto-novo"),
    ("Cape Verde Ferries: Routes, Times, Tickets & Prices — CapeVerde.com (consultada 18/09/2026)", "https://www.capeverde.com/travel-tips/ferries"),
    ("Embajada de España en Cabo Verde (Praia) — Ministerio de Asuntos Exteriores, UE y Cooperación (consultada 18/09/2026)", "https://www.exteriores.gob.es/Embajadas/praia/es/Paginas/index.aspx"),
    ("Wikipedia · Cidade Velha", "https://en.wikipedia.org/wiki/Cidade_Velha"),
    ("Wikipedia · Praia", "https://en.wikipedia.org/wiki/Praia"),
    ("Instituto do Património Cultural de Cabo Verde", "https://ipc.cv/"),
    ("IPC · Museu da Resistência (Tarrafal)", "https://ipc.cv/en/museu/museu-da-resistencia/"),
    ("Wikipedia · Tarrafal, Cabo Verde", "https://en.wikipedia.org/wiki/Tarrafal,_Cape_Verde"),
    ("Wikipedia · Serra Malagueta", "https://en.wikipedia.org/wiki/Serra_Malagueta"),
    ("Wikipedia · Assomada", "https://en.wikipedia.org/wiki/Assomada"),
    ("Wikipedia · Mindelo", "https://en.wikipedia.org/wiki/Mindelo"),
    ("Câmara Municipal de São Vicente", "https://www.cmsv.cv/"),
    ("Wikipedia · Monte Verde (Cabo Verde)", "https://en.wikipedia.org/wiki/Monte_Verde_(Cape_Verde)"),
    ("Wikipedia · São Pedro, Cabo Verde", "https://en.wikipedia.org/wiki/S%C3%A3o_Pedro,_Cape_Verde"),
    ("Wikipedia · Baía das Gatas", "https://en.wikipedia.org/wiki/Ba%C3%ADa_das_Gatas"),
    ("UNESCO · Parc Naturel Cova, Paúl et Ribeira da Torre (lista indicativa)", "https://whc.unesco.org/en/tentativelists/6105/"),
    ("IPC · Parque Natural de Cova, Paúl e Ribeira da Torre", "https://ipc.cv/en/monumento-e-sitio/parque-natural-de-cova-paul-e-ribeira-da-torre-pncprt/"),
    ("Wikipedia · Cova (cráter)", "https://en.wikipedia.org/wiki/Cova_(crater)"),
    ("Wikipedia · Fontainhas", "https://en.wikipedia.org/wiki/Fontainhas"),
    ("Wikipedia · Ponta do Sol, Cabo Verde", "https://en.wikipedia.org/wiki/Ponta_do_Sol,_Cape_Verde"),
    ("Wikipedia · Tarrafal de Monte Trigo", "https://en.wikipedia.org/wiki/Tarrafal_de_Monte_Trigo"),
    ("Wikipedia · Santo Antão, Cabo Verde", "https://en.wikipedia.org/wiki/Santo_Ant%C3%A3o,_Cape_Verde"),
    ("Wikipedia · Chã das Caldeiras", "https://en.wikipedia.org/wiki/Ch%C3%A3_das_Caldeiras"),
    ("Wikipedia · Pico do Fogo", "https://en.wikipedia.org/wiki/Pico_do_Fogo"),
    ("Wikipedia · São Filipe, Cabo Verde", "https://en.wikipedia.org/wiki/S%C3%A3o_Filipe,_Cape_Verde"),
    ("Wikipedia · Brava, Cabo Verde", "https://en.wikipedia.org/wiki/Brava,_Cape_Verde"),
    ("Wikipedia · Nova Sintra", "https://en.wikipedia.org/wiki/Nova_Sintra"),
    ("Wikipedia · Santa Maria, Cabo Verde", "https://en.wikipedia.org/wiki/Santa_Maria,_Cape_Verde"),
    ("Wikipedia · Sal, Cabo Verde", "https://en.wikipedia.org/wiki/Sal,_Cape_Verde"),
    ("Wikipedia · Pedra de Lume", "https://en.wikipedia.org/wiki/Pedra_de_Lume"),
    ("Wikipedia · Praia de Santa Mónica", "https://en.wikipedia.org/wiki/Praia_de_Santa_M%C3%B3nica"),
    ("Wikipedia · Deserto de Viana", "https://en.wikipedia.org/wiki/Deserto_de_Viana"),
    ("Wikipedia · Sal Rei", "https://en.wikipedia.org/wiki/Sal_Rei"),
    ("Wikipedia · Boa Vista, Cabo Verde", "https://en.wikipedia.org/wiki/Boa_Vista,_Cape_Verde"),
    ("Wikipedia · Monte Gordo Natural Park", "https://en.wikipedia.org/wiki/Monte_Gordo_Natural_Park"),
    ("Wikipedia · Ribeira Brava, Cabo Verde", "https://en.wikipedia.org/wiki/Ribeira_Brava,_Cape_Verde"),
]

# Bucle norte · Santiago, São Vicente y Santo Antão (con dos ferris)
CORRIDOR = [
    (14.91733, -23.50935),
    (14.91609, -23.60205),
    (15.1856, -23.677),
    (15.26348, -23.74374),
    (14.91733, -23.50935),
    (16.88435, -24.99009),
    (16.86843, -24.93294),
    (16.90376, -24.90867),
    (16.88435, -24.99009),
    (17.10839, -25.06228),
    (17.19239, -25.10744),
    (16.96242, -25.30512),
    (17.10839, -25.06228),
    (16.88435, -24.99009),
]

# Bucle sur y este · Fogo, Brava, Sal, Boa Vista y São Nicolau (solo por mar o aire)
CORRIDOR_ALT = [
    (14.91733, -23.50935),
    (14.89681, -24.49349),
    (14.96757, -24.37452),
    (14.87104, -24.695),
    (16.59675, -22.90754),
    (16.76826, -22.89644),
    (16.17914, -22.92374),
    (16.00125, -22.91941),
    (16.62204, -24.33627),
]

HISTORIA_RESUMEN = "Cabo Verde es una anomalía africana y conviene decirlo desde el principio: diez islas volcánicas deshabitadas hasta que los navegantes portugueses llegaron hacia 1456 y fundaron en 1462 Ribeira Grande, el primer asentamiento europeo permanente del trópico y una de las grandes plataformas de la trata atlántica. De aquel encuentro forzado nació una sociedad criolla propia, con su lengua, su música y una diáspora mayor que la población residente. Independiente de Portugal el 5 de julio de 1975 y multipartidista desde 1990, el archipiélago es hoy la democracia más estable de África occidental: Freedom House le da 92 puntos sobre 100 y la califica de «libre» en su informe de 2025. Queda fuera de la ruta overland por su condición insular."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>Cabo Verde es el único país de esta guía que no tuvo reinos previos a la colonización, sencillamente porque no tuvo habitantes. Las diez islas volcánicas y los cinco islotes que forman el archipiélago, poco más de 4.000 kilómetros cuadrados en pleno Atlántico, estaban vacíos cuando los primeros navegantes europeos llegaron a ellos. En 1456 Alvise Cadamosto, Antoniotto Usodimare y un capitán portugués avistaron algunas de las islas, y en la década siguiente Diogo Gomes y António de Noli completaron el reconocimiento del resto.</p><p>La prehistoria de Cabo Verde hay que buscarla, por tanto, enfrente. La población del archipiélago se formó con gentes traídas por la fuerza desde la costa africana y con colonos llegados de Portugal, y de ese contacto nació, en palabras de la UNESCO, la primera cultura criolla surgida del encuentro entre África y Europa. Es una diferencia que conviene tener presente al viajar: aquí no hay ruinas anteriores a 1460, ni linajes precoloniales, ni fronteras heredadas de reinos antiguos. Todo lo que se ve —los topónimos, la lengua, la música, los apellidos— pertenece a los cinco siglos y medio posteriores al desembarco portugués, y eso explica por qué el país se parece tan poco a sus vecinos del continente.</p>"),
    ("Colonización",
     "<p>La potencia colonial fue Portugal y su instrumento, el poblamiento dirigido. En 1462 los primeros colonos desembarcaron en Santiago y fundaron Ribeira Grande, hoy Cidade Velha, el primer asentamiento europeo permanente del trópico. La UNESCO, que la inscribió en 2009 en la Lista del Patrimonio Mundial, la describe como el primer puesto colonial europeo en los trópicos y subraya su papel central en la trata atlántica, concentrando personas esclavizadas en las rutas que unían África con Brasil y el Caribe. De aquella ciudad quedan dos iglesias, la Fortaleza Real de São Filipe, el trazado original de las calles y una picota de mármol del siglo XVI en estilo manuelino.</p><p>Cuando la trata decayó, el archipiélago quedó reducido a una colonia pobre y periódicamente hambrienta. A partir de 1747 se suceden las sequías: tres grandes hambrunas de los siglos XVIII y XIX causaron bastante más de cien mil muertos, y las dos peores del siglo XX, en 1941-1943 y 1947-1948, unas cuarenta y cinco mil. Portugal convirtió el territorio en provincia de ultramar en 1951. La herencia colonial es doble y sigue muy viva: el portugués como lengua oficial y una emigración masiva que nunca se ha detenido.</p>"),
    ("Independencia y construcción del Estado",
     "<p>El movimiento independentista no nació en las islas, sino en un proyecto compartido con Guinea-Bisáu. En 1956 Amílcar Cabral fundó el Partido Africano para la Independencia de Guinea y Cabo Verde, el PAIGC, que libró una guerra prolongada en el continente mientras el archipiélago permanecía relativamente al margen. Tras la Revolución de los Claveles portuguesa de 1974 la independencia llegó sin guerrilla: el 5 de julio de 1975, en Praia, el primer ministro portugués Vasco Gonçalves entregó el poder al presidente de la Asamblea Nacional, Abílio Duarte. La ficha país del Ministerio de Asuntos Exteriores español confirma esa fecha.</p><p>El golpe de Estado de 1980 en Guinea-Bisáu enterró la unión entre los dos países y el partido caboverdiano se reorganizó como PAICV, Partido Africano para la Independencia de Cabo Verde. Siguió un régimen de partido único hasta que, el 28 de septiembre de 1990, quedó abolido el monopartidismo. Las primeras elecciones multipartidistas se celebraron en enero de 1991 y las ganó el opositor Movimiento para la Democracia; António Mascarenhas Monteiro alcanzó la presidencia con el 73,5 por ciento de los votos. La transición fue pacífica y negociada, y marcó el tono de todo lo que vino después.</p>"),
    ("Historia reciente (2000–2026)",
     "<p>El siglo XXI empieza con una de las elecciones más ajustadas que se recuerdan en África: en la presidencial de 2001 Pedro Pires, del PAICV, se impuso a Carlos Veiga, del MpD, por doce votos, y el resultado se aceptó sin violencia. Pires gobernó dos mandatos; en 2011 le sucedió Jorge Carlos Fonseca, del MpD, reelegido en octubre de 2016, el mismo año en que Ulisses Correia e Silva llegó a primer ministro. En 2021 la presidencia volvió al PAICV con José María Neves, que tomó posesión el 9 de noviembre tras haber sido primer ministro entre 2001 y 2015.</p><p>El episodio natural más recordado de estos años es la erupción del Pico do Fogo en 2014, que arrasó los pueblos de Chã das Caldeiras. En lo económico, la pandemia disparó la deuda pública hasta el 149,1 por ciento del PIB en 2021, según el MAEC, y la recuperación posterior se apoyó en el turismo. El ciclo se cierra en 2026 con una nueva alternancia: el 17 de mayo el PAICV ganó las legislativas con el 47 por ciento de los votos y 37 de los 72 escaños y regresó al gobierno tras diez años en la oposición.</p>"),
    ("Política y gobierno en 2026",
     "<p>Cabo Verde es una república semipresidencialista; el MAEC la define como «república soberana, unitaria y democrática», con una Asamblea Nacional de 72 escaños. A fecha de septiembre de 2026, según la ficha país del MAEC actualizada en agosto de 2026, el jefe del Estado es José María Neves, del PAICV, desde el 9 de noviembre de 2021, y el jefe del Gobierno es Francisco Avelino Vieira de Carvalho, designado el 19 de junio de 2026 tras ganar su partido las legislativas del 17 de mayo con 37 escaños frente a 33 del MpD y 2 de la UCID, con una abstención del 53 por ciento. Las presidenciales estaban convocadas para el 15 de noviembre de 2026.</p><p>Es una democracia real, no una fachada. Freedom House, en su informe de 2025, la clasifica como <strong>«libre»</strong> con 92 puntos sobre 100, 38 sobre 40 en derechos políticos y 54 sobre 60 en libertades civiles, y la describe como una democracia estable con elecciones competitivas y alternancias periódicas entre partidos rivales; apunta como problemas un sistema judicial sobrecargado y la desigualdad que sufren mujeres y migrantes. Reporteros Sin Fronteras la situó en 2025 en el puesto 30 de 180 y Transparencia Internacional le da 62 sobre 100. No hay conflicto armado. Con España mantiene relaciones desde 1977 y un Acuerdo de Cooperación Avanzada para 2022-2030; con la UE, una Asociación Especial desde 2007.</p>"),
    ("Economía y recursos",
     "<p>La riqueza de Cabo Verde no sale del suelo, sino del mar, del turismo y de la diáspora. El sector terciario supone el 74 por ciento del PIB y el turismo aporta alrededor del 25 por ciento, según el MAEC en agosto de 2026; el primario apenas llega al 6 por ciento, con la pesca por delante, y el secundario al 20, sobre todo conservero. El país importa mucho más de lo que vende: en 2025 exportó unos 319 millones de dólares frente a 1.330 millones de importaciones, un déficit estructural que tapan el turismo y las remesas de los emigrantes, cercanas al 12 por ciento del PIB.</p><p>La moneda es el escudo caboverdiano, con paridad fija con el euro a 110,265 escudos, muy cómodo sobre el terreno. El PIB rondó los 2.920 millones de dólares en 2025 y el PIB per cápita los 5.670 euros; el Banco Mundial lo sitúa en unos 5.800 dólares. La deuda pública, disparada al 149,1 por ciento del PIB en 2021 por la pandemia, bajó al 102,5 por ciento en 2025. España es el primer cliente de las exportaciones caboverdianas, sobre todo conservas de pescado, y Cabo Verde es el tercer destino de la inversión española en África subsahariana. Los grandes proyectos en marcha —puertos, digitalización y renovables— se apoyan en los 300 millones de euros firmados con la UE en 2024.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>En el archipiélago viven poco más de medio millón de personas —522.331 según el MAEC, datos de 2023— y la diáspora, sobre todo en Portugal, ronda el millón. El idioma oficial es el portugués, lengua de administración y escuela, pero la lengua materna de casi todos es el criollo caboverdiano, el <em>kriolu</em>; por carretera uno se entiende en portugués. En religión las fuentes discrepan: el MAEC habla de más del 90 por ciento de católicos; el censo de 2021, citado por la Wikipedia inglesa, de un 72,5 por ciento, con un 15,6 sin religión y un 1,3 de musulmanes.</p><p>La cultura es criolla y musical: morna, coladeira, funaná y batuque, con Cesária Évora como gran embajadora. En la mesa manda la <em>cachupa</em>, guiso lento de maíz y alubias. El patrimonio UNESCO se reduce a Cidade Velha, inscrita en 2009, y ocho bienes en lista indicativa desde 2016. Las islas no se parecen entre sí: Santo Antão y Fogo son montaña y senderismo; Sal y Boa Vista, playa y desierto; Santiago y São Vicente, las urbanas. Para el viajero: ropa normal, con más recato fuera de la playa y en las iglesias; pedir permiso para fotografiar a personas; y ninguna restricción al alcohol. El ramadán, que en 2027 empieza en torno al 8 de febrero, apenas altera la vida diaria: los musulmanes no llegan al 2 por ciento.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Cabo Verde (Ministerio de Asuntos Exteriores de España · Oficina de Información Diplomática · agosto de 2026)", "https://www.exteriores.gob.es/documents/fichaspais/caboverde_ficha%20pais.pdf"),
    ("Cabo Verde: Freedom in the World 2025 (Freedom House · ficha de país · 2025)", "https://freedomhouse.org/country/cabo-verde/freedom-world/2025"),
    ("Cabo Verde – States Parties (UNESCO · Centro del Patrimonio Mundial · consultado en septiembre de 2026)", "https://whc.unesco.org/en/statesparties/cv"),
    ("Cidade Velha, Historic Centre of Ribeira Grande (UNESCO · ficha del bien 1310 · inscrito en 2009)", "https://whc.unesco.org/en/list/1310/"),
    ("History of Cape Verde (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/History_of_Cape_Verde"),
    ("Cape Verde (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Cape_Verde"),
    ("Cabo Verde (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Cabo_Verde"),
    ("Cabo Verde (Reporteros Sin Fronteras · Clasificación Mundial de la Libertad de Prensa 2025)", "https://rsf.org/en/country/cabo-verde"),
    ("Cape Verde (Transparency International · Índice de Percepción de la Corrupción)", "https://www.transparency.org/en/countries/cape-verde"),
    ("Eleições levam Francisco Carvalho e o PAICV ao poder em Cabo Verde (Euronews Portugal · 18 de mayo de 2026)", "https://pt.euronews.com/2026/05/18/eleicoes-levam-francisco-carvalho-e-o-paicv-ao-poder-em-cabo-verde"),
    ("Cabo Verde replaces visa for Europeans by pre-registration system and airport security tax (Servicio Europeo de Acción Exterior · 4 de enero de 2019)", "https://www.eeas.europa.eu/node/56167_en"),
    ("Taxa de «Segurança Aeroportuária»: pagamento no aeroporto custa o dobro em 2026 (Caboverde24 · 28 de febrero de 2026)", "https://caboverde24.info/2026/02/28/taxa-de-seguranca-aeroportuaria-pagamento-no-aeroporto-custa-o-dobro-em-2026/"),
    ("EASE · Plataforma oficial de preregistro de viajeros (Gobierno de Cabo Verde · consultado en septiembre de 2026)", "https://www.ease.gov.cv/"),
    ("Cabo Verde · Datos del Banco Mundial (Banco Mundial · consultado en septiembre de 2026)", "https://data.worldbank.org/country/cabo-verde"),
]

SPEC = dict(
    slug="cabo-verde", name="Cabo Verde", revision="18 sep 2026",
    sub="FUERA DE RUTA — archipiélago a 570–850 km de la costa · sin ferry de vehículos desde el continente · volcanes, senderismo y criollo atlántico",
    chips=[
        ("ESTATUS", "FUERA DE RUTA. País insular sin conexión terrestre; solo en avión o en contenedor…"),
        ("CÓMO LLEGAR", "Vuelo a Sal (SID), Praia (RAI), Boa Vista (BVC) o São Vicente/Mindelo (VXE) desde Lisboa, Madrid…"),
        ("VISADO", "EXENTO para ciudadanos UE hasta 30 días desde el 1 de enero de 2019…"),
        ("VEHÍCULO", "No hay ro-ro ni ferry de coches desde el continente. Entrada solo en contenedor y tratada como importación:…"),
        ("SEGURIDAD", "92/100 Freedom House · delincuencia en Praia"),
        ("SEGURO", "Carta Verde NO vale · póliza local obligatoria"),
        ("SALUD", "Sin vacunas obligatorias · dengue activo"),
        ("DRONES", "Libre bajo 120 m · encima, permiso AAC 10 días"),
        ("STARLINK", "Autorizado por ARME · activo desde dic. 2024"),
        ("4x4", "Solo alquiler local · sin ro-ro desde el continente"),
        ("A PIE", "Santo Antão y Fogo: el mejor senderismo insular"),
        ("PERRO", "Entrada con certificado veterinario oficial, microchip, rabia y serología ≥0,5 UI/ml…"),
        ("MONEDA", "Escudo caboverdiano (CVE), con PARIDAD FIJA al euro: 1 EUR = 110,265 CVE…"),
        ("VENTANA", "Árido y suave, 22–27 °C todo el año. Lluvias de mediados de agosto a mediados de octubre…"),
    ],
    center=[16.03, -24.1], zoom=7,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Bucle norte · Santiago, São Vicente y Santo Antão (con dos ferris)",
    corridor_alt_label="Bucle sur y este · Fogo, Brava, Sal, Boa Vista y São Nicolau (solo por mar o aire)",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Cape_Verde_Fogo_landscape_with_Pico_do_Fogo_road.jpg?width=1200",
    hero_credit="Chã das Caldeiras y el Pico do Fogo · Cayambe · CC BY-SA 3.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Cabo Verde queda FUERA DE LA RUTA 2027 por una razón puramente física: son diez islas volcánicas a entre 600 y 850 km al oeste de Cap-Vert (Wikipedia), sin ningún enlace terrestre y sin ferry de pasajeros ni ro-ro regular desde el continente africano ni desde Europa. Cualquier vehículo llega metido en un contenedor, y la aduana caboverdiana trata esa entrada como importación: exige conocimiento de embarque, certificado de exportación y un depósito que los propios residentes cifran en el 100–200 % del valor del coche, recuperable en parte al reexportar (foro Expat.com, Cabo Verde). A eso hay que sumar dos desembarcos de contenedor, dos despachos y dos esperas de puerto. Para dos 4x4 españoles en una expedición de 250 km/día no sale a cuenta: el archipiélago entero tiene 1.113 km de carretera nacional, de los cuales solo un 36 % está asfaltado, y las islas no están conectadas entre sí por carretera. Si algún día quiere hacerse, la forma sensata es un viaje APARTE y SIN COCHE: vuelo directo desde Lisboa, Madrid o Las Palmas a Sal, Praia, Boa Vista o São Vicente (unos 200–450 € ida y vuelta según temporada, por confirmar), coches de alquiler o aluguer local en cada isla y CV Interilhas entre ellas. Lo único que habría que decidir es cuándo: dos o tres semanas fuera del calendario overland, y qué se hace con el perro, porque la vuelta a la UE desde Cabo Verde exige titulación antirrábica previa (ver sección del perro).",
    facts=[
        ("Estatus", "FUERA DE RUTA. País insular sin conexión terrestre; solo en avión o en contenedor. Ficha informativa para un viaje aparte."),
        ("Cómo llegar", "Vuelo a Sal (SID), Praia (RAI), Boa Vista (BVC) o São Vicente/Mindelo (VXE) desde Lisboa, Madrid, Las Palmas y varias ciudades europeas. Entre islas, CV Interilhas, Nôs Ferry y vuelos domésticos; el salto Mindelo–Porto Novo cuesta 1.500 CVE (unos 13,60 €) por pasajero no residente."),
        ("Visado", "EXENTO para ciudadanos UE hasta 30 días desde el 1 de enero de 2019. OBLIGATORIO el pre-registro en EASE (ease.gov.cv) y pagar la TSA. Más de 30 días: visado."),
        ("Vehículo/aduana", "No hay ro-ro ni ferry de coches desde el continente. Entrada solo en contenedor y tratada como importación: depósito de derechos del 100–200 % del valor (foro de residentes). Sin organismo emisor de CPD en el país."),
        ("Seguro", "La Carta Verde española NO cubre Cabo Verde. Tampoco aplican Carte Brune CEDEAO ni COMESA Yellow Card. Seguro local obligatorio si se conduce; el alquiler lo incluye."),
        ("Moneda", "Escudo caboverdiano (CVE), con PARIDAD FIJA al euro: 1 EUR = 110,265 CVE. Tarjeta solo en hoteles y restaurantes de gama alta; efectivo en el resto."),
        ("Perro", "Entrada con certificado veterinario oficial, microchip, rabia y serología ≥0,5 UI/ml; certificado válido 10 días. VUELTA A LA UE: Cabo Verde NO está en el anexo II del Reg. (UE) 2026/636, así que hace falta titulación antirrábica previa anotada en el pasaporte."),
        ("Drones", "Permitidos por debajo de 120 m y fuera de zonas restringidas, sin autorización. Por encima de 120 m o en zona restringida: autorización escrita de la AAC con 10 días hábiles de antelación. Prohibido a menos de 2.000 m de aeródromos."),
        ("Starlink", "AUTORIZADO. La ARME concedió licencia a Starlink Cabo Verde, Lda el 11 de octubre de 2024 y el servicio se abrió al público a finales de diciembre de 2024, con cobertura en todo el territorio nacional."),
        ("Seguridad", "Uno de los países más seguros de África y la democracia más sólida de la región: 92/100 y estatus «Free» en Freedom in the World 2025. El problema real es la delincuencia común urbana, no el terrorismo."),
        ("Clima", "Árido y suave, 22–27 °C todo el año. Lluvias de mediados de agosto a mediados de octubre (riesgo de riadas). Calima y tormentas de arena de diciembre a febrero, que retrasan vuelos."),
        ("Sanidad", "Red pública muy precaria frente a la europea y SIN cámara hiperbárica en el país. Brote de dengue activo desde noviembre de 2023 y situación de contingencia declarada en julio de 2025. Seguro con evacuación a Europa imprescindible."),
    ],
    alerts=[
        "No existe ferry ni ro-ro de vehículos entre el continente africano o Europa y Cabo Verde: el coche del viaje solo entra en contenedor, y eso convierte la visita en una operación logística independiente.",
        "El pre-registro EASE es OBLIGATORIO aunque no haga falta visado, y hay que hacerlo al menos 5 días antes de volar. Llegar sin él se paga con una tasa de regularización del doble.",
        "La TSA cuesta 3.400 CVE (unos 31 €) pagada online y 6.800 CVE (unos 62 €) si se paga en el mostrador del aeropuerto desde 2026.",
        "Santo Antão, la isla de montaña más espectacular del archipiélago, NO tiene aeropuerto operativo: solo se llega en ferry desde Mindelo a Porto Novo.",
        "Los enlaces interinsulares, aéreos y marítimos, sufren retrasos y cancelaciones frecuentes (MAEC): nunca encajar un vuelo internacional el mismo día que un salto entre islas.",
        "Brote de dengue activo desde noviembre de 2023; el Gobierno declaró situación de contingencia por tres meses en julio de 2025 para frenar la propagación y la reintroducción de la malaria.",
        "No hay cámara hiperbárica en todo el país y el rescate acuático es limitado: cualquier inmersión o deporte de agua exige seguro específico con evacuación medicalizada a Europa.",
        "La delincuencia común ha subido: atracos con arma blanca y pistola en Praia (Gamboa, Prainha, Quebra Canela, Cruz de Papa) y robos a turistas en playas de Sal y Boa Vista.",
        "Solo un 36 % de los 1.113 km de carretera nacional está asfaltado; el resto es calçada de basalto y pistas, durísimas para la suspensión y muy lentas.",
        "El agua corriente procede en más del 70 % de plantas desalinizadoras y no es potable sin tratar: agua embotellada para beber, siempre (MAEC).",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Llegada a Santiago", "Praia (Platô) · registro EASE y TSA hechos antes del vuelo, recogida de vehículos y trámites", "~20 km · 1 día"),
        ("2 · Sur de Santiago", "Praia → Cidade Velha (UNESCO) → Praia", "~35 km · 1 día"),
        ("3 · Interior de Santiago", "Praia → Assomada → Serra Malagueta → Tarrafal", "~75 km · 1 día"),
        ("4 · Vuelta y ferri", "Tarrafal → Praia (costa este) · embarque a São Vicente", "~80 km + ferri · 1–2 días"),
        ("5 · São Vicente", "Mindelo → Monte Verde → Baía das Gatas → Calhau → São Pedro → Mindelo", "~70 km · 1 día"),
        ("6 · Cruce a Santo Antão", "Ferri Mindelo → Porto Novo · subida a la Cova por la EN1-SA01", "~30 km + ferri · 1 día"),
        ("7 · Cova y valle de Paúl", "Cova → Ribeira de Paúl (Pombas) → Ribeira Grande", "~40 km · 1 día"),
        ("8 · Norte de Santo Antão", "Ribeira Grande → Ponta do Sol → mirador de Fontainhas → Ribeira Grande", "~25 km · 1 día"),
        ("9 · Suroeste de Santo Antão", "Ribeira Grande → Porto Novo → Tarrafal de Monte Trigo (ida y vuelta)", "~110 km · 1–2 días"),
        ("10 · Regreso y salto a Fogo", "Porto Novo → ferri a Mindelo → ferri/avión a Fogo (São Filipe)", "ferri · 1–2 días"),
        ("11 · Fogo", "São Filipe → Chã das Caldeiras · ascensión al Pico do Fogo con guía", "~45 km · 2 días"),
        ("12 · Brava", "Vale de Cavaleiros → ferri a Furna → Nova Sintra → Fajã d'Água", "~25 km + ferri · 1–2 días"),
        ("13 · Sal", "Espargos → Santa Maria → Pedra de Lume → Espargos", "~60 km · 1–2 días"),
        ("14 · Boa Vista y São Nicolau", "Sal Rei → Deserto de Viana → Povoação Velha → Praia de Santa Mónica; opcional São Nicolau (Ribeira Brava y Monte Gordo)", "~120 km · 2 días"),
    ],
    offroad=[
        "AVISO DE PARTIDA: Cabo Verde está a unos 570 km de la costa africana y no hay ferri de vehículos desde el continente, así que los dos 4x4 del proyecto no pueden llegar rodando; cualquier conducción aquí implica embarque marítimo de los vehículos desde Europa o alquiler local (tramitación y coste, por confirmar).",
        "El eje de conducción exigente del archipiélago es la EN1-SA01 de Santo Antão, que une Porto Novo con Ribeira Grande cruzando el interior montañoso: empedrado histórico, calzada estrecha, curvas de horquilla sin quitamiedos y niebla persistente en el collado de la Cova (fuente: Wikipedia, Porto Novo).",
        "La costera Porto Novo - Tarrafal de Monte Trigo, 27 km por el suroeste árido, es el otro tramo serio: la carretera se inauguró en febrero de 2021 y antes solo se llegaba por mar o a pie; sin gasolinera ni taller en destino (fuente: Wikipedia, Tarrafal de Monte Trigo).",
        "En Fogo, el acceso a Chã das Caldeiras discurre sobre las coladas de 2014-2015 dentro de un área protegida de 67 km²: pista irregular de lava, sin firme homogéneo; el interior de la caldera es Parque Natural do Fogo y la ascensión al cono del Pico do Fogo (2.829 m) se hace a pie y con guía local, no en vehículo.",
        "En Boa Vista, casi todo lo que no es el eje Rabil - Sal Rei son pistas de arena y roca: el Deserto de Viana y el acceso a Praia de Santa Mónica desde Povoação Velha exigen 4x4 real, desinflado de neumáticos y prudencia; 14 áreas protegidas y playas de nidificación de tortuga boba limitan por dónde se puede circular (fuente: Wikipedia, Boa Vista).",
        "ZONAS VETADAS DE FACTO: las playas de desove de Boa Vista y Sal en temporada (junio-octubre), el interior de los parques naturales fuera de pista (Serra Malagueta, Monte Verde, Monte Gordo, Cova-Paúl-Ribeira da Torre, Fogo) y los terrenos agrícolas en terraza de Paúl y de la Cova, donde el maíz y las judías se cultivan en el propio fondo del cráter.",
        "Se circula POR LA DERECHA y el firme va «del asfalto liso al empedrado y la pista de tierra»; el 4x4 no es obligatorio pero sí muy recomendable en Boa Vista, Santo Antão y São Vicente, mientras que en Sal y Santiago basta un turismo (fuente: capeverdeislands.org, guía de alquiler de coches).",
        "Cartografía y comunidad: no se ha localizado cobertura específica de Cabo Verde en Tracks4Africa ni fichas útiles de iOverlander para el archipiélago; conviene planificar sobre OpenStreetMap y contactos locales, y asumir que la información de pistas es escasa (ver «notas»).",
    ],
    senderismo=[
        "Ponta do Sol → Fontainhas → Corvo/Formiguinhas → Cruzinha da Garça (Santo Antão): el sendero costero clásico del país, sobre acantilado, con Fontainhas colgado a 158 m; jornada completa y regreso en transporte por carretera.",
        "Cova → Ribeira de Paúl → Pombas (Santo Antão): descenso de unos 1.100 m de desnivel desde el borde del cráter hasta el mar, entre terrazas de caña y alambiques de grogue; es la excursión más hecha de la isla.",
        "Vuelta al cráter de la Cova por el borde (Santo Antão): recorrido corto y casi llano alrededor del fondo cultivado, con vistas a Paúl y Ribeira da Torre; buena opción con niebla baja.",
        "Ascensión al Pico do Fogo desde Chã das Caldeiras: 2.829 m, salida nocturna, terreno de lapilli suelto y guía local obligatoria; el descenso por la ceniza es rápido y muy abrasivo para el calzado.",
        "Vuelta por la Bordeira y las coladas de 2014-2015 (Fogo): recorrido de media jornada por el anillo de la caldera a 2.700 m y por las casas sepultadas de Portela y Bangaeira, sin necesidad de subir al cono.",
        "Senderos del Parque Natural de Serra Malagueta (Santiago): red señalizada desde el centro de visitantes hacia el valle de Ribeira Principal, en el único bosque de niebla de la isla, con 28 endemismos vegetales.",
        "Subida a Monte Verde (São Vicente): 744 m, corta y muy expuesta al viento; se puede hacer a pie desde el desvío en lugar de subir con el vehículo hasta las antenas.",
        "Monte Gordo (São Nicolau): ascensión al techo de la isla, 1.312 m, por el parque natural desde Cachaço, entre pinar y endemismos como Aeonium gorgoneum; niebla frecuente por la tarde.",
    ],
    acampada=[
        "NO SE HAN LOCALIZADO fuentes fiables de campings formales en Cabo Verde: las búsquedas devuelven sobre todo agregadores comerciales (Tripadvisor, BookRetreats, Glamping Hub) y ningún camping municipal o privado verificable. Tratar la acampada como excepción, no como plan base.",
        "iOverlander y Tracks4Africa no arrojan fichas útiles para el archipiélago en las búsquedas hechas: la comunidad overlander apenas cubre Cabo Verde porque no se llega rodando desde el continente.",
        "La oferta real documentada es de trekking con vivac organizado: Actour Cabo Verde vende un programa de 8 días y 7 noches en Santo Antão con dos noches en tienda —en la aldea de Chã de Feijoal y en la meseta de Lagoa— por unos 1.000 € por persona, lo que confirma que la acampada con guía se practica en el interior de la isla; la propia ficha no menciona permisos ni normativa de acampada libre (https://www.actourhiking.com/en/trekking/trek-et-camping-a-santo-antao).",
        "En Chã das Caldeiras, dentro del Parque Natural do Fogo, el alojamiento documentado es en casas y pensiones del pueblo reconstruido tras la erupción de 2014-2015; acampar dentro del área protegida de 67 km² requeriría autorización del parque (por confirmar).",
        "En las playas de Boa Vista y Sal, pernoctar en arena es desaconsejable en temporada de desove (junio-octubre): son 14 áreas protegidas y playas de nidificación de tortuga boba, con acceso nocturno restringido.",
        "En Santo Antão y São Nicolau la acampada libre choca con un problema físico: casi todo el terreno llano está cultivado en terrazas y pertenece a alguien; sin permiso del propietario no hay sitio.",
        "Alternativa realista para dos vehículos: dormir en el 4x4 en explanadas de pueblos costeros (Tarrafal de Santiago, Calhau, Tarrafal de Monte Trigo) pidiendo permiso en el bar o a la câmara municipal; no hay normativa publicada que lo prohíba ni que lo ampare (por confirmar).",
        "Con perro, la opción más segura sigue siendo la pensión o residencial familiar: el sector es pequeño y las condiciones se negocian caso por caso.",
    ],
    visado=[
        "ESPAÑOLES: SIN VISADO para estancias de hasta 30 días desde el 1 de enero de 2019. La exención cubre toda la UE más Reino Unido, Suiza, Liechtenstein, Noruega, Mónaco, San Marino y Andorra.",
        "OBLIGATORIO el pre-registro previo en la plataforma EASE (https://www.ease.gov.cv) y el pago de la Taxa de Segurança Aeroportuária (TSA). No es un visado, pero sin él no se embarca con tranquilidad.",
        "PLAZO: el pre-registro debe presentarse al menos 5 días antes del viaje. Se puede hacer también a través de la agencia de viajes.",
        "COSTE 2026: 3.400 CVE (unos 31 €) si se paga online por EASE; 6.800 CVE (unos 62 €) de tasa de regularización si se llega sin registrar y se paga en el aeropuerto.",
        "Pasaporte con validez mínima de 6 meses (MAEC). Para más de 30 días hace falta visado; la prórroga se pide en la Direção de Estrangeiros e Fronteiras (DEF) y no hacerlo se paga con multa antes de salir del país.",
        "NO HAY FRONTERA TERRESTRE: la entrada es siempre por aeropuerto o por puerto. Llegando en barco propio hay que presentarse en los puestos de control de Praia, Mindelo o Palmeira y declarar las escalas previas para obtener el salvoconducto.",
    ],
    fronteras_rows=[
        ("Entrada aérea principal", "Aeropuerto Internacional Amílcar Cabral (SID), Espargos, Sal", "El más transitado del país y hub de Cabo Verde Airlines. Vuelos a Lisboa, Porto, París, Ámsterdam, Londres, Mánchester, Casablanca y Dakar. Operativo; EASE y TSA verificados en el control de la DEF. Fuente: Wikipedia, consultada 18/09/2026."),
        ("Entrada aérea capital", "Aeropuerto Internacional Nelson Mandela (RAI), Praia, Santiago", "Abierto en 2005, 3 km al noreste de Praia, gestionado por Vinci Airports desde julio de 2023. Enlaces con Lisboa, París, Zúrich, Ámsterdam, Casablanca, Dakar y Luanda. Operativo. Fuente: Wikipedia, consultada 18/09/2026."),
        ("Entrada aérea turística", "Aeropuerto Internacional Aristides Pereira (BVC), Boa Vista", "Tráfico internacional desde 2007, muy orientado al chárter europeo. Tormentas de arena entre diciembre y febrero pueden cerrarlo o desviar vuelos (FCDO). Operativo."),
        ("Entrada aérea norte", "Aeropuerto Cesária Évora (VXE), São Pedro, São Vicente", "Estatus internacional desde 2009. Es la puerta práctica para Santo Antão, que no tiene aeropuerto operativo. Operativo."),
        ("Puerto de entrada / control", "Porto da Praia, Santiago", "Puesto de control de la DEF para llegadas por mar. Hay que declarar las escalas previas y pedir salvoconducto (MAEC). Principal puerto de contenedores del país."),
        ("Puerto de entrada / control", "Porto Grande, Mindelo, São Vicente", "Puesto de control por mar y principal puerto de cruceros. Terminal del ferry a Porto Novo (Santo Antão). Fuente: MAEC y Wikipedia."),
        ("Puerto de entrada / control", "Palmeira, Sal", "Tercer puesto de control marítimo citado por el MAEC. Puerto de suministro de combustible."),
        ("Enlace interinsular con vehículo", "Mindelo (São Vicente) ⇄ Porto Novo (Santo Antão)", "El enlace más usado y más fiable del archipiélago: 50–60 minutos, varias salidas diarias en ambos sentidos desde el Cais Marítima de Mindelo. Dos operadores: CV Interilhas (buque Chiquinho) y Nôs Ferry/ARMAS (Mar d'Canal). Billete de pasajero no residente 1.500 CVE (CV Interilhas) y 1.470 CVE (Nôs Ferry), unos 13–14 € (Ondas.cv, 2026). Tarifa de VEHÍCULO POR CONFIRMAR: la página de tarifas de Tiver.cv no se abrió."),
        ("Enlace interinsular sur", "Línea Sotavento: Praia ⇄ Fogo ⇄ Brava ⇄ Maio", "Buque Liberdadi, rotación semanal. Mar duro y cancelaciones frecuentes (FCDO menciona interrupciones hacia las islas del sur). Admisión de vehículos POR CONFIRMAR."),
        ("Enlace interinsular largo", "Línea Redonda: São Vicente ⇄ São Nicolau ⇄ Sal ⇄ Boa Vista ⇄ Santiago", "Buque Dona Tututa, dos salidas semanales. Es la única forma de mover un vehículo entre los dos grupos de islas. Tarifas y capacidad de carga rodada POR CONFIRMAR con el operador."),
        ("Frontera terrestre", "NO EXISTE", "Cabo Verde es un archipiélago: no tiene ningún paso terrestre. Ninguna de las claves habituales de la ruta (CEDEAO, escoltas, convoyes) aplica aquí."),
    ],
    vehiculos=[
        "LLEVAR EL COCHE DEL VIAJE NO ES VIABLE en la práctica: no hay ferry ni ro-ro desde el continente ni desde Europa. La única vía es contenedor desde un puerto europeo (los buques suelen escalar en Canarias viniendo de Portugal y España) o desde Dakar, y no hay línea regular pensada para vehículos.",
        "La aduana caboverdiana trata la entrada de un vehículo como IMPORTACIÓN: bill of lading, certificado de exportación del país de origen y depósito de derechos que los residentes del foro Expat.com sitúan en el 100–200 % del valor del vehículo, recuperable en parte al reexportar. Se puede pedir exención por estancia temporal. Interlocutor: Direção Geral das Alfândegas, Av. Amílcar Cabral, Praia · +238 261 7758 · helpdesk@dnre.gov.cv. Su web solo publica regímenes de viajero —franquicia de equipaje hasta 15.000 CVE y régimen simplificado hasta 100.000 CVE con tasa única del 30 %— y la exención del emigrante que regresa: NO publica ningún régimen de admisión temporal para el vehículo de un turista, y ese es el agujero principal de esta ficha.",
        "NO HAY organismo emisor de Carnet de Passages en Cabo Verde: la propia base de datos de carnetdepassage.org indica que «AIT/FIA currently does not have any official CPD-issuing organization in the country». Si alguien quisiera llevar el coche, el CPD se emitiría en España (RACE) y habría que negociar su aceptación con la aduana caboverdiana, que no está documentada.",
        "La Carta Verde española NO tiene validez en Cabo Verde, y el país no pertenece ni a la Carte Brune CEDEAO ni a la Carte Rose CEMAC ni a la COMESA Yellow Card. Quien conduzca allí necesita póliza local; los alquileres la llevan incluida.",
        "Se conduce POR LA DERECHA: Cabo Verde cambió al tráfico por la derecha en 1928, siendo colonia portuguesa (Wikipedia, «Left- and right-hand traffic»). Permiso internacional de conducción recomendado junto al permiso español; requisito exacto de las compañías de alquiler POR CONFIRMAR.",
        "La red es corta y dura: 1.113 km de carretera nacional con solo un 36 % asfaltado (unos 400 km) y unos 5.000 km de calçada de basalto empedrada. Los tramos asfaltados buenos son Praia–Tarrafal (Santiago) y la autovía Espargos–Santa Maria (Sal).",
        "En Santo Antão, la mítica carretera de la Cova a Ribeira Grande es de empedrado en cornisa y exige conducción lenta; el resto de la isla se mueve en aluguer (furgonetas compartidas) o en 4x4 de alquiler con conductor.",
        "ALTERNATIVA RECOMENDADA: alquilar en cada isla. La mayoría de los ferries interinsulares admiten vehículos, pero CapeVerde.com concluye que alquilar por separado en cada isla sale más barato que pasear un coche en barco, y solo el enlace São Vicente–Santo Antão es fiable; el resto sufre cancelaciones por avería o mar gruesa que duran días. Un 4x4 local con seguro incluido evita el contenedor, el depósito aduanero y el transporte interinsular del vehículo.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Autoridad competente: Agência de Aviação Civil (AAC), https://www.aac.cv/artigos/drones · Tel. +238 260 34 30. Es el único interlocutor válido; ni MAEC ni FCDO mencionan restricciones de drones en sus fichas de Cabo Verde.",
        "Sin autorización se puede volar hasta 120 m de altura, fuera de zonas restringidas, con el dron a menos de 100 m del operador y bajo control directo, y con buena visibilidad. El piloto es responsable de ceder el paso a cualquier aeronave tripulada.",
        "Para superar los 120 m o volar en zona restringida hay que presentar el formulario de servidumbre aeronáutica a la AAC con al menos 10 días hábiles de antelación.",
        "PROHIBIDO volar a menos de 2.000 metros de cualquier aeródromo. Eso descarta de hecho buena parte de Espargos (Sal) y del entorno de los cuatro aeropuertos internacionales.",
        "No se exige registro del aparato, remote ID ni licencia de piloto a los visitantes (drone-laws.com, 2026). Lo que NO está documentado es el trato en aduana al entrar con el dron: POR CONFIRMAR con la AAC antes de volar.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "AUTORIZADO. Decisión de la ARME de 11 de octubre de 2024, comunicada el 16 de octubre; operador Starlink Cabo Verde, Lda, con cobertura autorizada en todo el territorio nacional.",
        "Servicio comercial abierto al público a finales de diciembre de 2024 (Expresso das Ilhas y O País, 30–31 de diciembre de 2024). La ARME publicó después una nota aclarando la tasa de utilización de los servicios de Starlink.",
        "Para una visita sin vehículo propio no hace falta: la cobertura móvil de Unitel T+ y CVMóvel llega a los núcleos habitados de las nueve islas pobladas y hay SIM de prepago y eSIM turística (Unitel T+ tiene portal de eSIM propio).",
        "Donde sí tiene sentido es en los valles interiores de Santo Antão y en Brava, donde la cobertura terrestre flojea. Precio del plan roam/regional POR CONFIRMAR en el mapa de disponibilidad de starlink.com.",
    ],
    perro_intro=[
        "ENTRADA: certificado veterinario oficial del país de origen según modelo OIE/WOAH, con identificación del animal, vacunación antirrábica y desparasitación interna y externa documentadas. El modelo que usa Portugal para exportar a Cabo Verde (DGAV, MOD 970-DGV-01-2012) exige MICROCHIP obligatorio vinculado a la vacuna y a la titulación.",
        "RABIA Y SEROLOGÍA: la vacuna antirrábica no puede administrarse antes de los 3 meses de edad, y hace falta análisis serológico en laboratorio autorizado por la OIE realizado AL MENOS 30 DÍAS después de la vacunación, con título ≥0,5 UI/ml. El certificado sanitario tiene una validez de solo 10 DÍAS, así que hay que cuadrarlo con la fecha exacta del vuelo.",
        "AUTORIZACIÓN PREVIA: las representaciones caboverdianas exigen enviar la documentación al consulado o embajada para obtener un «atestado de que o animal pode viajar para Cabo Verde» (la Embajada de Cabo Verde en Brasil lo cobra a 15,71 USD). Si el trámite es equivalente en la Embajada de Cabo Verde en Madrid está POR CONFIRMAR.",
        "RAZAS PROHIBIDAS: no se ha localizado ninguna lista de razas prohibidas o restringidas de Cabo Verde en fuente oficial. POR CONFIRMAR con la DGASP o con la Embajada de Cabo Verde en Madrid.",
        "VUELTA A LA UE: Cabo Verde NO figura en el anexo II del Reglamento de Ejecución (UE) 2026/636 (aplicable desde el 22 de abril de 2026), que sí lista 52 países. Eso obliga a la vía de país no listado: TITULACIÓN ANTIRRÁBICA en laboratorio autorizado por la UE con muestra tomada al menos 30 días después de la vacunación, anotada en el pasaporte europeo ANTES DE SALIR de España, y entrada por un punto de entrada de viajeros autorizado.",
        "En la práctica esto es una ventaja: si el perro sale de España con la titulación ya hecha y anotada, el regreso desde Cabo Verde no exige repetir nada ni esperar tres meses en destino. Si no se hace antes, hay que hacerla allí y esperar 3 meses.",
        "VETERINARIOS: hay clínicas privadas en Praia, Mindelo y Sal, pero la atención especializada es limitada y el abastecimiento de fármacos, irregular. Riesgos reales: calor, deshidratación, garrapatas y el terreno volcánico abrasivo de Fogo y Santo Antão, que destroza almohadillas.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "VACUNAS: ninguna obligatoria para entrar desde España (MAEC). Recomendadas fiebre amarilla, hepatitis A y B, fiebre tifoidea y tétanos-difteria. El certificado de fiebre amarilla sí puede exigirse si se llega desde un país endémico.",
        "DENGUE: brote activo desde noviembre de 2023. En julio de 2025 el Gobierno declaró «situación de contingencia» por tres meses para frenar la propagación y la reintroducción de la malaria. Repelente, manga larga y mosquitera al amanecer y al anochecer.",
        "MALARIA: no es endémica en el archipiélago, pero se registran casos puntuales, sobre todo en Santiago. No hay profilaxis generalizada recomendada; consultar en Sanidad Exterior antes de salir.",
        "RED SANITARIA muy precaria comparada con Europa (MAEC). Hospitales de referencia: Agostinho Neto en Praia, Baptista de Sousa en Mindelo y Hospital do Sal en Espargos, más clínicas privadas en Praia, Mindelo, São Filipe y Sal.",
        "NO HAY CÁMARA HIPERBÁRICA en todo el país y los sistemas de rescate acuático son limitados. Para buceo, surf, kite o windsurf hace falta seguro específico.",
        "SEGURO OBLIGATORIO en la práctica: debe incluir evacuación medicalizada intercontinental A EUROPA. El MAEC avisa expresamente de no contratar pólizas que solo repatríen a países africanos cercanos.",
        "MEDICAMENTOS: las farmacias tienen lo básico, pero el abastecimiento de especialidades es irregular y puede tardar semanas. Llevar la medicación crónica desde España, repartida entre maleta y equipaje de mano. Agua embotellada para beber; evitar hielo, zumos naturales y lácteos sin garantía.",
    ],
    seguridad_intro="Cabo Verde es, con diferencia, el país más seguro y más democrático de esta guía. Freedom in the World 2025 le da 92/100 y estatus «Free» —38/40 en derechos políticos y 54/60 en libertades civiles—, con alternancia pacífica en el poder desde 1991 y elecciones competitivas. El FCDO dice que no hay historial reciente de terrorismo. El riesgo real no es político: es la delincuencia común urbana, que ha crecido con la crisis, y son los fenómenos naturales —riadas de agosto a octubre, sismicidad en Fogo y Brava, calima en invierno.",
    seguridad=[
        "El MAEC recomienda viajar con precaución, sin desaconsejar ninguna isla ni zona. No hay ninguna región vetada, ni escoltas, ni permisos especiales de circulación: nada de la mecánica habitual del Sahel aplica aquí.",
        "Freedom House 2025: 92/100, estatus «Free». Señala como puntos débiles un sistema judicial sobrecargado, casos de corrupción, desigualdad de género y la situación de los trabajadores migrantes; no la libertad política.",
        "PRAIA (Santiago) es donde se concentra el problema: atracos con arma blanca y pistola en Gamboa, Prainha, Quebra Canela y las escalinatas de Cruz de Papa. Barrios a evitar: Tira Chapéu, Brasil, Várzea, Eugénio Lima, Safende y Terra Branca.",
        "SAL y BOA VISTA: aumento de asaltos a turistas y robos en playas, sobre todo en temporada alta. En Mindelo y São Filipe los atracos se concentran en los barrios periféricos.",
        "Reglas básicas del MAEC: no caminar solo de noche, nada de valor a la vista, documentación en la caja fuerte del hotel y desplazamientos nocturnos en taxi o vehículo. Taxis y hoteles se consideran fiables.",
        "TERRORISMO: el FCDO señala que «no hay historial reciente de terrorismo en Cabo Verde», aunque no descarta atentados como en cualquier destino. No hay riesgo de secuestro documentado.",
        "NATURALEZA: la temporada de lluvias va de mediados de agosto a mediados de octubre, con lluvias torrenciales y deslizamientos. En agosto de 2024 el Gobierno declaró zona de calamidad en seis municipios por una tormenta tropical. Sismicidad en Fogo y Brava, sin alerta activa.",
        "MAR: mareas y corrientes fuertes. Bañarse solo en playas con socorrista y respetar el sistema de banderas (roja peligro, amarilla precaución, verde seguro). El FCDO advierte además de la peligrosidad de los autobuses interurbanos por la conducción.",
        "DROGAS: penas duras. Hasta 3 meses de cárcel más multa por drogas blandas y de 1 a 20 años por drogas duras, según cantidad y antecedentes (MAEC).",
    ],
    agua=[
        "Más del 70 % del agua potable consumida en Cabo Verde se produce por DESALINIZACIÓN (declaraciones recogidas por JM Madeira; otras fuentes del sector elevan la cifra al 90 %). Es un país estructuralmente seco: no hay ríos permanentes.",
        "El operador principal es ELECTRA (electra.cv), con la ANAS como agencia nacional de agua y saneamiento. El abastecimiento en algunas islas es por turnos y llenar depósitos grandes puede no ser inmediato.",
        "PARA BEBER: agua embotellada siempre, también para lavarse los dientes. El MAEC lo dice expresamente y añade evitar hielo y zumos naturales.",
        "PARA DUCHA Y LAVADO el agua de red desalinizada sirve, pero es dura y cara. Si algún día se llevara un vehículo, conviene llenar en puerto o en estaciones de servicio de Praia, Mindelo, Espargos y Santa Maria, no en zonas rurales.",
        "En los valles de Santo Antão (Paúl, Ribeira Grande) hay manantiales y levadas, pero el agua se destina al regadío y no es potable sin tratar. Llevar filtro y pastillas si se hacen travesías largas.",
    ],
    combustible=[
        "PRECIOS MÁXIMOS OFICIALES DE SEPTIEMBRE DE 2026 (ARME, regulador multisectorial): gasolina 175,40 CVE/litro y gasóleo normal 169,40 CVE/litro. A la paridad fija de 110,265 CVE/€, salen unos 1,59 €/l de gasolina y 1,54 €/l de gasóleo.",
        "Los precios los fija y publica mensualmente la ARME como PRECIO MÁXIMO, así que son homogéneos en todo el país. La subida media de septiembre de 2026 fue del 4,51 % respecto a agosto.",
        "Gas butano, útil si se cocina: 1.767 CVE la bombona de 12,5 kg y 848 CVE la de 6 kg (ARME, septiembre de 2026).",
        "RED: estaciones de servicio en todos los núcleos principales de las islas habitadas, concentradas en Praia, Mindelo, Espargos, Santa Maria, Sal Rei y São Filipe. En el interior de Santo Antão, Fogo y Brava son escasas: repostar lleno antes de subir a los valles.",
        "No hay racionamiento documentado a 2026, pero el combustible llega por mar a Palmeira (Sal) y se redistribuye: una avería logística puede secar una isla pequeña unos días. POR CONFIRMAR la disponibilidad real de gasóleo de bajo azufre para motores europeos modernos.",
    ],
    experiencias_intro="No existen relatos de overlanders que hayan llevado su vehículo a Cabo Verde: el archipiélago está fuera del circuito por la imposibilidad del ro-ro. Lo que sí hay es abundante literatura de viajeros por islas y algún hilo de foro que explica precisamente por qué no se hace.",
    experiencias=[
        "Por qué nadie lleva el coche: en el hilo «Send my Campervan by shipping or ferry to Cape Verde» de Expat.com, residentes de larga duración responden sin rodeos que no hay ferry de pasajeros ni servicio ro-ro a Cabo Verde desde ningún puerto internacional, que los buques que llegan pasan por Canarias desde Portugal y España, y que cualquier vehículo entra como importación con depósito de derechos del 100–200 % del valor. Su consejo es directo: en islas tan pequeñas, alojarse y alquilar sale por una fracción del precio.",
        "Santo Antão a pie, sin coche: en «Hiking in Santo Antão: Cape Verde's Mountain Paradise» (Erika's Travels), la autora describe la isla como un paraíso de senderismo donde el transporte real son los aluguer compartidos y el acceso es el ferry desde Mindelo, porque el aeropuerto de la isla está cerrado. Confirma la lógica de la ficha: el vehículo propio no aporta nada y el ferry de Porto Novo es el cuello de botella.",
        "La travesía de la Cova: la guía «Walking in Santo Antão» de CapeVerde.co.uk detalla el descenso desde el cráter de la Cova hacia Paúl y la ruta de cornisa de Cruzinha a Ponta do Sol, con horarios y desniveles. Deja claro que el empedrado en cornisa se conduce a paso de hombre y que las mejores partes de la isla solo se ven andando.",
        "Guía práctica de una isla sin aeropuerto: el «Travel Guide to Santo Antão, A Wonderland For Hikers» de Indie Traveller explica el encadenado real —volar a São Vicente, dormir en Mindelo, coger el ferry de la mañana a Porto Novo— y cómo se organizan los aluguer hacia Ribeira Grande y Paúl. Es el itinerario que tendría que seguir cualquiera que llegue sin vehículo.",
        "Circuito de tres islas: el operador Kuluar describe en «Trekking in Cabo Verde» un itinerario que encadena Santo Antão, São Vicente y Fogo con ascensión al Pico do Fogo, apoyándose en ferries y vuelos internos. Sirve como plantilla de lo que sería el viaje aparte: dos o tres semanas, sin coche propio y con márgenes para cancelaciones.",
        "Fogo y el volcán: la ficha «Cape Verde: Fogo and Santo Antão» de CapeVerde.com plantea el combinado clásico del archipiélago —el caldera de Chã das Caldeiras y los valles de Santo Antão— y confirma que el eje del viaje son las dos islas de montaña, no las playas de Sal y Boa Vista.",
        "Dieciocho rutas catalogadas: «18 Top Hikes in Santo Antao, Cape Verde» de Paulina on the Road inventaría las rutas con distancia, desnivel y dificultad, desde Ponta do Sol–Cruzinha hasta las levadas de Paúl. Es el mejor punto de partida para dimensionar cuántos días necesita la isla y por qué no conviene llevar al perro a las travesías largas.",
        "Conectividad sobre el terreno: la guía de SIM de Phone Travel Wiz (2025) compara las prepago de CVMóvel y Unitel T+ y confirma que la cobertura 4G cubre los núcleos habitados de las islas pobladas, con eSIM disponible. Para un viaje de dos semanas por islas no hace falta Starlink.",
        "El salto que sí admite coche: la programación de la Linha Barlavento de CV Interilhas recogida por Ondas.cv (2026) describe la conexión diaria São Vicente–Santo Antão con el buque Chiquinho, unos 60 minutos, y señala que algunas rutas admiten vehículos aunque remite al operador para tarifas. Es el único enlace del archipiélago donde mover un coche tiene sentido práctico.",
    ],
    pendientes=[
        ("Página oficial del organismo veterinario caboverdiano (DGASP)", "Localizar un portal activo del Ministério da Agricultura e Ambiente o de la DGASP con la circular de importación de animales de compañía; cerrar cuando se pueda citar la URL y el modelo de certificado vigente."),
        ("Razas de perro prohibidas o restringidas en Cabo Verde", "Confirmar por escrito con la Embajada de Cabo Verde en Madrid (+34 915 70 25 68) o con la DGASP si existe lista de razas vetadas; cerrar con respuesta oficial fechada."),
        ("Atestado consular previo para el perro desde España", "Verificar si la Embajada de Cabo Verde en Madrid exige el mismo atestado previo que la de Brasil y a qué coste; cerrar con correo o nota consular."),
        ("Tarifa de transporte de vehículo en el ferry Mindelo–Porto Novo", "El billete de pasajero no residente está confirmado (1.500 CVE, Ondas.cv 2026), pero no el de viatura. Pedir el tarifario vigente a CV Interilhas o a Nôs Ferry; cerrar con importe en CVE y fecha."),
        ("Admisión de vehículos en las líneas Sotavento y Redonda", "Confirmar con CV Interilhas qué buques admiten carga rodada y con qué frecuencia; cerrar con la programación oficial."),
        ("Coste real del contenedor Europa–Cabo Verde (y Dakar–Praia)", "Pedir cotización a una naviera de línea Canarias/Lisboa–Praia para un contenedor de 20 o 40 pies con un 4x4; cerrar con presupuesto fechado."),
        ("Régimen de admisión temporal de vehículo en la aduana caboverdiana", "La DGA (+238 261 7758 · helpdesk@dnre.gov.cv) no publica ningún régimen de admisión temporal para turistas. Escribirles y pedir por escrito si existe y si aceptan CPD; cerrar con referencia normativa."),
        ("Exigencia del permiso internacional de conducción", "Confirmar con dos compañías de alquiler locales si exigen PIC además del permiso español; cerrar con respuesta de ambas."),
        ("Trato aduanero del dron a la entrada", "Preguntar a la AAC (+238 260 34 30) si el dron se declara en aduana y si hay registro previo; cerrar con respuesta escrita."),
        ("Número de emergencia operativo: 112 frente a 130/131/132", "Verificar en fuente del Gobierno de Cabo Verde o en la Policía Nacional si el 112 sustituye a los números antiguos o convive con ellos; cerrar con nota oficial fechada."),
        ("Precio real del vuelo ida y vuelta desde España", "Comprobar tarifas de temporada a SID/RAI desde Madrid, Lisboa y Las Palmas; cerrar con rango de precios y fecha de consulta."),
        ("Disponibilidad y precio de Starlink Roam en Cabo Verde", "Consultar el mapa de disponibilidad de starlink.com y la tasa de utilización que aclaró la ARME; cerrar con plan y precio mensual."),
    ],
    sources=SOURCES,
    sources_note="Todas las páginas de esta lista se abrieron y se leyeron durante la revisión del 18 de septiembre de 2026; cuando un dato no pudo confirmarse en una fuente abierta se ha escrito «por confirmar» y se ha llevado a la lista de pendientes. Precios, tasas y horarios cambian con frecuencia en Cabo Verde: la ARME actualiza los combustibles cada mes y la TSA se revisó en 2026. Esta ficha es una herramienta de planificación, no una autorización ni una fuente legal: antes de moverse hay que verificar con la Embajada de Cabo Verde en Madrid, con la AAC y con CV Interilhas.",
    emergency="EMERGENCIA CONSULAR 24 H de la Embajada de España en Praia: +238 991 0124. Centralita: +238 260 1800. Policía Nacional: 132. Bomberos: 131 y +238 261 27 27 (MAEC). Cabo Verde adoptó además el 112 como número único nacional de emergencia; si no responde, usar los antiguos. Urgencias: Agostinho Neto (Praia) +238 260 21 69, Baptista de Sousa (Mindelo) +238 232 73 55, Hospital do Sal +238 241 11 30.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

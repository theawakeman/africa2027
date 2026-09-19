# -*- coding: utf-8 -*-
"""Libia — ficha completa (18 sep 2026): FUERA DE LA RUTA PREVISTA.

Libia está FUERA DE LA RUTA PREVISTA y además EXCLUIDA en la práctica: el país sigue partido entre el Gobierno de Unidad Nacional en Trípoli y el bloque de Bengasi y las fuerzas de Haftar, con milicias, minas y secuestro de extranjeros; el MAEC desaconseja viajar bajo cualquier circunstancia. NO se expiden visados turísticos ordinarios: hay que documentar con fuente fechada qué vías existen (invitación de empresa, agencia autorizada, periodistas) y si en 2025-2026 ha habido algún grupo de turistas con permiso. La app solo tiene una ficha stub: créala entera con el formato del piloto de Túnez. La ficha es INFORMATIVA e histórica: Libia guarda cinco sitios UNESCO, TODOS en la Lista del Patrimonio Mundial en Peligro desde 2016, y eso hay que decirlo en cada PDI afectado. Marca con claridad qué zonas controla quién y cuál es el estado de conservación y de saqueo.

Método: PDIs con pin comprobado uno a uno en Google Maps, tres fotografías de Wikimedia Commons por PDI (autor y licencia leídos de la API), fichas de decisión y enlaces concretos; historia de siete secciones con fuentes abiertas en la sesión; secciones operativas con fuente y fecha, y «por confirmar» donde no hay fuente. Expediente: audit/historia/libia.json y audit/pdi/libia.md.
"""
from data_common import make_ficha

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    dict(
        n=1, name="Trípoli · medina otomana, arco de Marco Aurelio y castillo Rojo", cat="Ciudad · servicios", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=32.8999699, lon=13.1759706,  # Google Maps: Arco de Marco Aurelio (Trípoli)
        desc="La capital conserva una medina otomana amurallada de planta pentagonal, el castillo Rojo (Assaraya al-Hamra) y el arco cuadrifronte de Marco Aurelio, levantado enteramente en mármol en el año 165 y ÚNICO resto romano visible de la antigua Oea. El castillo alberga el museo nacional, cerrado desde 2011 y reabierto el 12 de diciembre de 2025 como Museo Nacional de Libia, con acceso inicialmente limitado a grupos escolares. Advertencia: el MAEC desaconseja viajar al país salvo necesidad y en Trípoli y en la vecina Zauiya hay enfrentamientos recurrentes entre milicias.",
        dog_note="Medina, mezquitas y el museo del castillo Rojo no son sitio para un perro; solo paseos cortos con correa por el frente marítimo y en horas frescas.",
        visit={
            "why": "Es la única ciudad libia donde se concentran medina, museo nacional y un monumento romano en pie a diez minutos a pie uno de otro. Es además la base logística obligada de cualquier recorrido por Tripolitania.",
            "see": "El arco de Marco Aurelio con su cúpula octogonal y los frontones de Apolo y Minerva en carros tirados por grifos y esfinges; el laberinto de zocos y mezquitas otomanas con columnas romanas reaprovechadas; el castillo Rojo, un gran complejo palaciego de patios sobre el borde de la medina.",
            "access": "Autopista costera desde Ras Ajdir (frontera tunecina) o desde Misrata. Los callejones de la medina no admiten vehículos: hay que dejar los dos 4x4 fuera, en la franja del paseo marítimo junto al castillo. El pin marca el arco de Marco Aurelio, en la entrada noreste de la medina. Control: Gobierno de Unidad Nacional (Dbeibah), con su autoridad debilitada tras los choques de mayo de 2025 (Asharq Al-Awsat, 5-6-2025); el MAEC (actualizado 19-11-2025) clasifica todo el país como riesgo extremo y advierte de secuestros exprés en cualquier punto.",
            "when": "De noviembre a marzo; la medina se recorre mejor a primera hora de la mañana, antes del calor y del tráfico.",
            "skip": "Descártalo mientras el MAEC mantenga la recomendación de no viajar salvo necesidad, o si hay choques activos entre milicias en Trípoli, Zauiya o Tayura.",
        },
        links=[
            {"label": "Trípoli (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Tripoli,_Libya"},
            {"label": "Arco de Marco Aurelio (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Arch_of_Marcus_Aurelius_(Tripoli)"},
            {"label": "Museo del castillo Rojo / Museo Nacional de Libia (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Red_Castle_Museum"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Marcus_Aurelius_Arch_Tripoli_Libya.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Marcus_Aurelius_Arch_Tripoli_Libya.jpg",
                "credit": "Daniel and Kate Pett · CC BY 2.0",
                "caption": "El arco de Marco Aurelio, en la medina de Trípoli.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tripoli_Skyline_edit.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tripoli_Skyline_edit.jpg",
                "credit": "hakeem.gadi · GFDL 1.2",
                "caption": "El frente marítimo de Trípoli.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/LIBYA-Tripoli.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:LIBYA-Tripoli.jpg",
                "credit": "HussinAiad · CC BY-SA 4.0",
                "caption": "Trípoli hoy.",
            },
        ],
    ),
    dict(
        n=2, name="Leptis Magna · ciudad romana de Septimio Severo (UNESCO, en peligro)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=32.6343016, lon=14.2948353,  # Google Maps: Leptis Magna
        desc="A 130 km al este de Trípoli, junto a Al Khums, está la ciudad natal de Septimio Severo, que la engrandeció hasta convertirla en una de las más bellas del Imperio. Inscrita por la UNESCO en 1982 y en la LISTA DEL PATRIMONIO MUNDIAL EN PELIGRO desde el 14 de julio de 2016, junto con las otras cuatro libias, por la inestabilidad y la presencia de grupos armados. Se conservan el arco de Septimio Severo, la basílica severiana, el teatro, las termas adrianas y un anfiteatro de época de Nerón. El mayor riesgo hoy no es el saqueo sino el mar: erosión costera y subida del nivel.",
        dog_note="Recinto arqueológico vallado con taquilla; no he encontrado norma publicada sobre perros, pero el suelo de mármol al sol y la vigilancia militar desaconsejan llevarlo.",
        visit={
            "why": "Es el conjunto romano mejor conservado del Mediterráneo y el monumento mayor de Libia; una visita explica de golpe por qué el país figura en la lista de la UNESCO.",
            "see": "El arco cuadrifronte de Septimio Severo, la basílica severiana, el foro nuevo, las termas adrianas, el teatro sobre el mar y el anfiteatro con el circo al borde del agua. En Al Khums está además el museo de Leptis Magna.",
            "access": "Carretera costera asfaltada desde Trípoli (~130 km) hasta Al Khums; desvío señalizado y aparcamiento de tierra amplio junto a la puerta, suficiente para dos 4x4. Horario y entrada: no he encontrado tarifa oficial publicada — por confirmar. El pin marca la puerta principal y la taquilla, no el centro del yacimiento. Control: Tripolitania, bajo el Gobierno de Unidad Nacional (Asharq Al-Awsat, 5-6-2025). Conservación: en 2011 fuerzas pro-Gadafi usaron el yacimiento como cobertura de blindados, pero el arqueólogo Hafed Walda no registró pérdidas visibles por combates ni bombardeos; desde 2014 son vecinos organizados quienes lo protegen y mantienen.",
            "when": "De octubre a abril, y a primera hora o a última: no hay sombra en el foro ni en el circo.",
            "skip": "Si no llevas permiso y escolta en regla, o si hay tensión en Al Khums o en la ruta costera Trípoli–Misrata.",
        },
        links=[
            {"label": "UNESCO · Archaeological Site of Leptis Magna (ref. 183)", "url": "https://whc.unesco.org/en/list/183"},
            {"label": "Leptis Magna (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Leptis_Magna"},
            {"label": "UNESCO · los cinco sitios libios pasan a la Lista en Peligro (14-7-2016)", "url": "https://whc.unesco.org/en/news/1523"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Leptis_Magna_-_Severan_Basilika.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Leptis_Magna_-_Severan_Basilika.jpg",
                "credit": "Franzfoto · CC BY-SA 3.0",
                "caption": "La basílica severiana de Leptis Magna.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Severan_Basilica.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Severan_Basilica.JPG",
                "credit": "SashaCoachman · CC BY-SA 3.0",
                "caption": "Detalle de la basílica del siglo II.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Leptis_Magna_-_Labdah,_Libya_November_2004_(6769449483).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Leptis_Magna_-_Labdah,_Libya_November_2004_(6769449483).jpg",
                "credit": "Sludge G · CC BY-SA 2.0",
                "caption": "Leptis Magna, junto a Al Khums.",
            },
        ],
    ),
    dict(
        n=3, name="Sabratha · teatro romano frente al mar (UNESCO, en peligro)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="medio día",
        lat=32.7811016, lon=12.4495221,  # Google Maps: Sabratha
        desc="A 70 km al oeste de Trípoli, Sabratha nació como factoría fenicia y salida de los productos del interior africano, pasó por el reino númida de Masinisa y fue reconstruida en los siglos II y III. Su teatro conserva el frente escénico DE TRES PISOS, caso rarísimo en el Mediterráneo, con el mar detrás. Inscrita en 1982 y en la Lista del Patrimonio Mundial en Peligro desde 2016. Ojo con el estado: la piedra es calcarenita blanda y la erosión marina castiga sobre todo las termas, la almazara y el puerto; los rompeolas no bastan.",
        dog_note="Recinto vallado con museo anexo; los museos no admiten animales y el yacimiento no tiene sombra ni agua.",
        visit={
            "why": "El frente escénico de tres pisos sobre el mar es la imagen más reconocible de la arqueología libia y no tiene equivalente en el Magreb.",
            "see": "El teatro del siglo II con sus bajorrelieves en el frente de la escena, las termas, la almazara y el barrio portuario. El yacimiento tiene dos museos, el Púnico y el Romano, con mosaicos, esculturas de mármol y bustos de divinidades.",
            "access": "Autopista costera desde Trípoli (~70 km al oeste) y desvío al mar; aparcamiento junto al museo con espacio para dos 4x4. Horario y precio: por confirmar, no hay tarifa oficial publicada que haya podido abrir. El pin marca la entrada del recinto y el museo. Control: Tripolitania occidental, bajo autoridades alineadas con el GNU (Asharq Al-Awsat, 5-6-2025), pero el MAEC (19-11-2025) señala choques de milicias en la vecina Zauiya, en la misma carretera.",
            "when": "De octubre a abril; la luz de tarde sobre el frente escénico y el mar es la mejor.",
            "skip": "Si hay enfrentamientos en el eje Zauiya–Zauara, o si viajas sin la escolta policial que exige el régimen de visados.",
        },
        links=[
            {"label": "UNESCO · Archaeological Site of Sabratha (ref. 184)", "url": "https://whc.unesco.org/en/list/184"},
            {"label": "Sabratha (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Sabratha"},
            {"label": "UNESCO · los cinco sitios libios pasan a la Lista en Peligro (14-7-2016)", "url": "https://whc.unesco.org/en/news/1523"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Theatre_of_Sabratha,_Libya.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Theatre_of_Sabratha,_Libya.jpg",
                "credit": "Autor desconocido · CC BY-SA 2.0",
                "caption": "El teatro romano de Sabratha.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sabratha_-_Antonine_Temple_166-169_AD.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sabratha_-_Antonine_Temple_166-169_AD.jpg",
                "credit": "Franzfoto · CC BY-SA 3.0",
                "caption": "El templo antonino de Sabratha.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Portic_Antonine_Temple_Sabratha.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Portic_Antonine_Temple_Sabratha.JPG",
                "credit": "SashaCoachman · CC BY-SA 3.0",
                "caption": "Pórtico del templo antonino.",
            },
        ],
    ),
    dict(
        n=4, name="Cirene · la Atenas de África (UNESCO, en peligro)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1 noche",
        lat=32.8035826, lon=21.8621694,  # Google Maps: Shahat (Cirene)
        desc="Colonia griega del siglo VII a.C. en el Yebel Ajdar, fue una de las principales ciudades del mundo helénico y siguió siendo capital hasta el terremoto de 365. Su templo de Zeus es uno de los mayores templos griegos jamás construidos, de dimensiones comparables al Partenón. Inscrita en 1982 y en la LISTA EN PELIGRO desde 2016. El problema es el avance de la ciudad moderna: desde 2013 se han arrasado con bulldozer numerosas tumbas del sector sur, y la necrópolis de unos 20 km² sigue sin protección efectiva.",
        dog_note="Yacimiento enorme y sin vallar en muchos tramos, con perros sueltos y rebaños; no compensa el riesgo.",
        visit={
            "why": "Es el gran yacimiento griego de África y el argumento central de Cirenaica; nada comparable entre Egipto y Túnez.",
            "see": "El santuario y el templo de Apolo (siglo VII a.C.), el templo de Zeus, el ágora con sus stoas oriental y occidental, y una necrópolis de unos 20 km² con tumbas rupestres escalonadas del siglo VI a.C. al V d.C.",
            "access": "Carretera asfaltada desde Bayda o desde Susa, en el Yebel Ajdar; el yacimiento se recorre en coche por pistas interiores y hay explanadas donde caben dos 4x4. Horario y entrada: por confirmar. El pin marca el santuario de Apolo, el acceso habitual desde Shahhat. Control: Cirenaica, bajo el Ejército Nacional Libio de Haftar (Asharq Al-Awsat, 5-6-2025). Conservación: la riada de octubre de 2023 dejó restos al descubierto y a la vez creó riesgo de daño y de expolio.",
            "when": "De marzo a mayo y de septiembre a noviembre: el Yebel Ajdar es la zona más lluviosa de Libia, con unos 600 mm al año, y en invierno hay barro.",
            "skip": "Si el permiso especial de Cirenaica no está concedido; el visado ordinario cubre solo Tripolitania.",
        },
        links=[
            {"label": "UNESCO · Archaeological Site of Cyrene (ref. 190)", "url": "https://whc.unesco.org/en/list/190"},
            {"label": "Cirene (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Cyrene,_Libya"},
            {"label": "Shahhat, la población actual junto al yacimiento (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Shahhat"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Archaeological_Site_of_Cyrene-109025.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Archaeological_Site_of_Cyrene-109025.jpg",
                "credit": "Giovanni Boccardi · CC BY-SA 3.0 IGO",
                "caption": "El yacimiento de Cirene.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/%D9%85%D8%B9%D8%A8%D8%AF_%D8%AF%D9%8A%D9%85%D9%8A%D8%AA%D8%B1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:%D9%85%D8%B9%D8%A8%D8%AF_%D8%AF%D9%8A%D9%85%D9%8A%D8%AA%D8%B1.jpg",
                "credit": "عدسة قوريني · CC BY-SA 4.0",
                "caption": "El santuario de Deméter, en Cirene.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Cyrene,_Libya.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Cyrene,_Libya.jpg",
                "credit": "Travcoa Travel · CC BY 2.0",
                "caption": "El templo de Zeus de Cirene.",
            },
        ],
    ),
    dict(
        n=5, name="Apolonia · el puerto sumergido de Cirene", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=32.8953986, lon=21.9611919,  # Google Maps: Susah (Apolonia)
        desc="Fundada hacia el 630 a.C. como puerto de Cirene, a unos 20 km al noreste, Apolonia llegó a ser capital de la Libia Pentapolitana en el siglo VI. Lo excepcional está BAJO EL AGUA: el terremoto y tsunami de Creta de 365 hundió la línea de costa unos 3,7–3,8 m y el puerto quedó sumergido, por lo que se conserva casi completo, uno de los más antiguos que se conocen. En tierra quedan el palacio del Dux con más de cien estancias, basílicas bizantinas y un teatro griego del siglo III a.C. con 28 gradas.",
        dog_note="Recinto arqueológico junto al pueblo de Susa, con museo; ruinas resbaladizas al borde del agua.",
        visit={
            "why": "Es la única ocasión en el Mediterráneo de ver el trazado íntegro de un puerto griego arcaico, conservado porque se hundió.",
            "see": "Las basílicas bizantinas con columnas reaprovechadas del teatro, el palacio del Dux excavado entre 1959 y 1962, el teatro griego fuera de las murallas y, desde la orilla, los muelles y diques sumergidos. El museo de Apolonia (Susa) guarda las piezas del yacimiento.",
            "access": "Desde Cirene, ~20 km de carretera asfaltada bajando al mar hasta Susa; el recinto está pegado al pueblo, con aparcamiento junto al museo. El pin marca la entrada del yacimiento y el museo, no el puerto sumergido. Horario y entrada: por confirmar. Control: Cirenaica, bajo el LNA de Haftar (Asharq Al-Awsat, 5-6-2025); el permiso especial para Libia oriental es imprescindible.",
            "when": "Primavera y otoño; a mediodía con mar en calma se distinguen mejor las estructuras sumergidas.",
            "skip": "Si vas justo de tiempo en Cirenaica: Cirene y Tolmeita dan más por hora invertida.",
        },
        links=[
            {"label": "Apolonia de Cirenaica (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Apollonia,_Cyrenaica"},
            {"label": "Susa / Marsa Susa (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Susa,_Libya"},
            {"label": "Lista de museos de Libia (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/List_of_museums_in_Libya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Apollonia_Libya.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Apollonia_Libya.jpg",
                "credit": "David Holt · CC BY-SA 2.0",
                "caption": "Las ruinas de Apolonia, el puerto de Cirene.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Apollonia_beach.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Apollonia_beach.jpg",
                "credit": "Maher27777 · Public domain",
                "caption": "El puerto sumergido de Apolonia (Susa).",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Apollonia_ruins_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Apollonia_ruins_2.jpg",
                "credit": "Maher27777 · Public domain",
                "caption": "La iglesia oriental de Apolonia.",
            },
        ],
    ),
    dict(
        n=6, name="Tolmeita · Ptolemais y su museo", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=32.7059625, lon=20.9539531,  # Google Maps: Ptolemais Archeological Park (Tolmeita)
        desc="Una de las cinco ciudades de la Pentápolis cirenaica, entre Bengasi y Cirene. Enterrada por la arena durante siglos, se conserva notablemente bien: destacan el Palazzo delle Colonne, mansión del gobernador con peristilo y mosaicos, un hipódromo, un anfiteatro, tres teatros y un acueducto romano con DIECISIETE cisternas abovedadas. La Universidad de Varsovia excava allí desde 2001 y el yacimiento tiene su propio museo de Tolmeita. Nota negra: en 2011 desaparecieron piezas robadas de la cámara acorazada de un banco de Bengasi.",
        dog_note="Yacimiento abierto con cisternas y pozos sin proteger; peligroso para un perro suelto.",
        visit={
            "why": "Es el yacimiento menos visitado y mejor conservado de la Pentápolis; la arena lo protegió de la reutilización de sus piedras.",
            "see": "El Palazzo delle Colonne con sus mosaicos, las diecisiete cisternas abovedadas, el mausoleo helenístico llamado Qasr Faraoun y las tumbas de cámara excavadas en las canteras. El museo de Tolmeita guarda las piezas del yacimiento.",
            "access": "Carretera costera desde Bengasi hacia el este (~110 km) y desvío al mar; explanada de tierra junto al recinto. El museo de Tolmeita existe y figura en la lista de museos de Libia, pero no he podido confirmar horario, tarifa ni si está abierto hoy — POR CONFIRMAR. El pin marca el acceso al recinto arqueológico y al museo. Control: Cirenaica, bajo el Ejército Nacional Libio de Haftar (Asharq Al-Awsat, 5-6-2025); requiere el permiso especial para Libia oriental.",
            "when": "Primavera y otoño, a media mañana; el conjunto se recorre a pie en dos o tres horas.",
            "skip": "Si no consigues guía local: el yacimiento no está señalizado y las cisternas abiertas son un peligro real.",
        },
        links=[
            {"label": "Ptolemais de Cirenaica (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ptolemais,_Cyrenaica"},
            {"label": "Bengasi, base logística más próxima (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Benghazi"},
            {"label": "Lista de museos de Libia (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/List_of_museums_in_Libya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ptolemais_(5283376622).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ptolemais_(5283376622).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "Las ruinas del palacio de Ptolemais.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ptolemais,_Villa_of_the_Four_Seasons.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ptolemais,_Villa_of_the_Four_Seasons.jpg",
                "credit": "Mrs Colvin (años sesenta) · CC BY-SA 4.0",
                "caption": "La villa de las Cuatro Estaciones, en Tolmeita.",
            },
        ],
    ),
    dict(
        n=7, name="Gadamés · la ciudad de barro del oasis (UNESCO, retirada de la Lista en Peligro en 2025)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="1–2 noches",
        lat=30.1317637, lon=9.4950555,  # Google Maps: Gadamés
        desc="«La perla del desierto», una de las ciudades presaharianas más antiguas, a unos 460 km al suroeste de Trípoli, junto a la triple frontera con Argelia y Túnez. Su arquitectura se ordena en vertical: planta baja para el almacén, planta intermedia para la familia sobre callejones cubiertos que parecen túneles, y terrazas reservadas a las mujeres; siete clanes ocupaban barrios separados. Inscrita en 1986, entró en la Lista en Peligro en 2016 y FUE RETIRADA DE ELLA EN JULIO DE 2025, tras la restauración impulsada por la propia comunidad. Es el único sitio libio que ha salido de la lista.",
        dog_note="Los pasajes cubiertos de la ciudad vieja son espacio doméstico y comunitario; un perro suelto no es bien recibido.",
        visit={
            "why": "Es la ciudad de barro mejor conservada del Sáhara y el único caso libio de recuperación patrimonial reconocida internacionalmente en 2025.",
            "see": "Los callejones cubiertos entre casas encaladas, las terrazas, los patios de los siete barrios clánicos, el palmeral y el sistema tradicional de riego rehabilitado por los vecinos desde 2011.",
            "access": "Carretera asfaltada desde Nalut o desde Trípoli por el Yebel Nafusa; hay aparcamiento fuera de la ciudad vieja, que se recorre a pie. El pin marca la puerta de acceso a la medina antigua. Control: Tripolitania interior; el visado ordinario incluye Gadamés en el circuito occidental habitual (Against the Compass, 24-7-2026). Aviso: el MAEC mantiene riesgo extremo para todo el país y advierte de secuestros y de la inseguridad en las regiones fronterizas del sur.",
            "when": "De noviembre a marzo; en verano se superan con holgura los 45 °C y la ciudad vieja se repuebla estacionalmente precisamente porque protege del calor.",
            "skip": "Si hay tensión en la frontera argelina o tunecina, o si el operador no cubre el trayecto Nalut–Gadamés.",
        },
        links=[
            {"label": "UNESCO · Old Town of Ghadamès (ref. 362)", "url": "https://whc.unesco.org/en/list/362"},
            {"label": "Gadamés (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ghadames"},
            {"label": "Libya Observer · la UNESCO retira Gadamés de la Lista en Peligro (2025)", "url": "https://libyaobserver.ly/culture/unesco-old-ghadames-no-longer-considered-world-heritage-danger"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Libya_4432_Ghadames_Luca_Galuzzi_2007.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Libya_4432_Ghadames_Luca_Galuzzi_2007.jpg",
                "credit": "Luca Galuzzi · CC BY-SA 2.5",
                "caption": "La ciudad vieja de Gadamés.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ghadames_Old_city_from_the_air.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ghadames_Old_city_from_the_air.jpg",
                "credit": "Mohamed Alazrak · CC BY-SA 4.0",
                "caption": "Gadamés desde el aire.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Ghadames,_2006.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Ghadames,_2006.jpg",
                "credit": "Autor desconocido · Public domain",
                "caption": "Callejones cubiertos de la medina de Gadamés.",
            },
        ],
    ),
    dict(
        n=8, name="Tadrart Acacus · arte rupestre del Fezán (UNESCO, en peligro)", cat="Patrimonio UNESCO", prio="Alta",
        dog="no recomendado", time="3–4 noches",
        lat=24.8333333, lon=10.3333333,  # Google Maps: Tadrart Acacus
        desc="Macizo rocoso al este de Ghat, en la frontera argelina y contiguo al Tassili n'Ajjer. Guarda MILES de pinturas rupestres de estilos muy distintos, fechadas entre el 12.000 a.C. y el 100 d.C., con jirafas, elefantes, avestruces, camellos, caballos y escenas de música y danza que registran el paso del Sáhara verde al desierto actual. Inscrito en 1985 y en la Lista en Peligro desde 2016. Conservación muy mala: la UNESCO documenta destrucción deliberada en al menos diez sitios desde abril de 2009, grafitis modernos junto a las pinturas y borrado con disolventes químicos.",
        dog_note="Expedición de varios días en el desierto sin agua ni veterinario a cientos de kilómetros; inviable con perro.",
        visit={
            "why": "Es uno de los conjuntos de arte rupestre más extensos y antiguos del mundo y el testimonio visual del Sáhara verde.",
            "see": "Abrigos y paredes con pinturas y grabados de fauna, pastores y escenas cotidianas repartidos por un macizo de casi 3,9 millones de hectáreas, entre dunas y agujas de arenisca.",
            "access": "Solo con guía tuareg, vehículo 4x4 y permiso: no es zona de conducción libre. Base en Ghat, con aeropuerto propio al norte de la ciudad. El pin marca el macizo; el punto NAVEGABLE real es Ghat, desde donde arrancan las pistas. Control: el sur y el extremo suroeste, incluidos Ubari y Ghat, figuran bajo control del LNA de Haftar (Asharq Al-Awsat, 5-6-2025). El MAEC (19-11-2025) desaconseja las regiones fronterizas del sur y advierte de minas; el visado turístico ordinario no cubre el Fezán.",
            "when": "De noviembre a febrero; en verano es impracticable.",
            "skip": "Descártalo mientras no exista un operador con permiso vigente para el Fezán: hoy no es un destino abierto.",
        },
        links=[
            {"label": "UNESCO · Rock-Art Sites of Tadrart Acacus (ref. 287)", "url": "https://whc.unesco.org/en/list/287"},
            {"label": "UNESCO · estado de conservación 2024 (se mantiene en la Lista en Peligro)", "url": "https://whc.unesco.org/en/soc/4547"},
            {"label": "Montes Acacus (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Tadrart_Acacus"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Libya_4985_Tadrart_Acacus_Luca_Galuzzi_2007.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Libya_4985_Tadrart_Acacus_Luca_Galuzzi_2007.jpg",
                "credit": "Luca Galuzzi · CC BY-SA 2.5",
                "caption": "Dunas del Tadrart Acacus.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Libya_5076_Tadrart_Acacus_Luca_Galuzzi_2007.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Libya_5076_Tadrart_Acacus_Luca_Galuzzi_2007.jpg",
                "credit": "Luca Galuzzi · CC BY-SA 2.5",
                "caption": "Formaciones rocosas del Acacus.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tadrart01.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tadrart01.JPG",
                "credit": "Pir6mon · CC BY-SA 3.0",
                "caption": "El circo de Moul n'ga, en el Tadrart.",
            },
        ],
    ),
    dict(
        n=9, name="Lagos de Ubari · el erg y los lagos salados del Fezán", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="1–2 noches",
        lat=26.803056, lon=13.535278,  # Google Maps: Lago Gaberoun (Ubari)
        desc="En el Idehan Ubari, un erg de unos 58.000 km², sobreviven lagos alimentados por manantiales entre las dunas, rodeados de gramíneas y palmeras datileras. El mayor, Gaberoun, alcanza 7,5 m de profundidad y es TAN SALADO que se flota sin esfuerzo; pese a la sal, hay crustáceos en abundancia. En la orilla noreste funcionaba un campamento turístico básico con patio, cabañas y tienda de recuerdos, abierto solo en invierno; el poblado beduino de la orilla oeste está en ruinas desde el traslado de la tribu a Wadi Bashir en los años ochenta.",
        dog_note="Travesía de erg sin asistencia; el agua es hipersalina y no sirve para el perro, y en verano hay plagas de mosquitos.",
        visit={
            "why": "Es la imagen clásica del Sáhara libio: agua turquesa y palmeras al pie de dunas de cien metros.",
            "see": "El lago de Gaberoun con su campamento y el poblado abandonado; las dunas del Idehan Ubari; los lagos Mandara, en el mismo sector. Cuántos siguen con agua hoy, POR CONFIRMAR: no he encontrado fuente fiable y reciente sobre su desecación.",
            "access": "Pista de arena desde la carretera Sebha–Ubari; travesía de erg que exige dos vehículos, deshinchado de neumáticos y guía local. El pin marca el lago de Gaberoun, no la pista de entrada. Control: Ubari bajo el LNA de Haftar (Asharq Al-Awsat, 5-6-2025). El MAEC (19-11-2025) cita expresamente Ubari entre las ciudades peligrosas y advierte de minas y de no salirse de las rodadas.",
            "when": "De octubre a mayo; en verano hay mosquitos y calor extremo.",
            "skip": "Descártalo sin guía y sin permiso para el Fezán: perderse en el erg o salirse de las rodadas en zona minada son riesgos reales.",
        },
        links=[
            {"label": "Gaberoun (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Gaberoun"},
            {"label": "Idehan Ubari (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Idehan_Ubari"},
            {"label": "Ubari (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Ubari"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Lake_Gaberoun_(5282881127).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Lake_Gaberoun_(5282881127).jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "El lago Gaberoun, en el erg de Ubari.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Libya_4709_Idehan_Ubari_Luca_Galuzzi_2007.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Libya_4709_Idehan_Ubari_Luca_Galuzzi_2007.jpg",
                "credit": "Luca Galuzzi · CC BY-SA 2.5",
                "caption": "Las dunas del Idehan Ubari.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Oasis_in_Libya.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Oasis_in_Libya.jpg",
                "credit": "Sfivat · Public domain",
                "caption": "Oum el Ma, uno de los lagos del Fezán.",
            },
        ],
    ),
    dict(
        n=10, name="Waw an Namus · el volcán negro en el corazón del Sáhara", cat="Naturaleza", prio="Media",
        dog="no recomendado", time="3–4 noches",
        lat=24.916667, lon=17.766667,  # Google Maps: Waw an Namus
        desc="Caldera volcánica en el Fezán oriental: una depresión de 4 km de anchura y 100 m de profundidad con un cono de escorias central y tres lagos que suman 0,3 km². El manto de tefra basáltica NEGRA cubre unos 300 km² de desierto y el contraste con la arena clara se ve desde el espacio; el lago mayor tiene 12,5 m de fondo y está a 434 m de altitud. Está prácticamente deshabitado: pasa cerca la ruta caravanera entre Kufra y Sebha, pero la logística y la guerra civil hacen muy difícil llegar.",
        dog_note="Tres días de desierto profundo sin agua ni evacuación posible; con perro es inasumible.",
        visit={
            "why": "Es uno de los lugares más aislados y fotogénicos del Sáhara: un anillo negro con lagos verdes y palmeras en mitad de la nada.",
            "see": "El cono de escorias central, los tres lagos de la caldera y el manto de tefra negra que rodea el volcán en trescientos kilómetros cuadrados.",
            "access": "Sin carretera: expedición de varios días por pista desde Sebha o desde la ruta Kufra–Sebha, con dos vehículos, guía y autonomía total de combustible y agua. El pin marca el cráter; no hay objeto navegable en el terreno. Control: zona desértica del Fezán oriental, en el área de influencia del LNA, que controla Sebha, Kufra y Al-Jawf (Asharq Al-Awsat, 5-6-2025). El MAEC (19-11-2025) advierte de minas en la región de Kufra y el Tibesti, herencia del conflicto con Chad.",
            "when": "De diciembre a febrero, la única ventana con temperaturas manejables.",
            "skip": "Descártalo por completo mientras persistan las minas, la ausencia de rescate y la prohibición de viaje independiente.",
        },
        links=[
            {"label": "Waw an Namus (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Waw_an_Namus"},
            {"label": "MAEC · recomendaciones de viaje a Libia", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Libia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Waw_an-Namus-gr%C3%BCner_See.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Waw_an-Namus-gr%C3%BCner_See.jpg",
                "credit": "StFr · CC0",
                "caption": "El lago verde del Waw an Namus.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Wau-en-Namus-1.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Wau-en-Namus-1.jpg",
                "credit": "Rolfcosar · CC BY-SA 3.0",
                "caption": "El cono de escorias dentro de la caldera.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Waw_an-Namus-roter_See.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Waw_an-Namus-roter_See.jpg",
                "credit": "DasPumm · CC0",
                "caption": "El lago rojo del cráter.",
            },
        ],
    ),
    dict(
        n=11, name="Bengasi · la ciudad reconstruida y su puerto", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=32.1194242, lon=20.0867909,  # Google Maps: Bengasi
        desc="Segunda ciudad del país, con unos 859.000 habitantes en 2023 y la capital de facto de Cirenaica. El centro urbano quedó arrasado en la batalla de 2014–2017, sobre todo los barrios costeros de Suq Al-Hout y al-Sabri. El Ejército Nacional Libio de Haftar la declaró libre de milicias el 5 de julio de 2017 y tomó el último barrio en diciembre de ese año. La reconstrucción avanza con polémica: en marzo de 2023 el ejército DEMOLIÓ edificios históricos de época italiana sin avisar al municipio.",
        dog_note="Ciudad grande, con escombros y solares aún sin despejar en el centro; nada adaptado a animales.",
        visit={
            "why": "Es la base logística obligada de Cirenaica: combustible, talleres, hospitales y el único aeropuerto internacional del este.",
            "see": "El puerto y la corniche, los barrios reconstruidos del centro, y lo que queda de la arquitectura colonial italiana, cada vez menos.",
            "access": "Carretera costera asfaltada desde Ajdabiya (~150 km al sur) o desde Tolmeita al este; aparcamiento amplio en la zona del puerto. Control: el LNA de Haftar, que mantiene Bengasi desde 2017 y la integró en la estructura de gobierno unificada de marzo de 2021 (Wikipedia EN; Asharq Al-Awsat, 5-6-2025). El MAEC (19-11-2025) cita Bengasi entre las ciudades expresamente peligrosas. Against the Compass (24-7-2026) señala que el acceso a Bengasi está especialmente restringido incluso con el permiso del este.",
            "when": "De octubre a mayo; la ciudad se ve en medio día.",
            "skip": "Si el permiso especial para Libia oriental no incluye expresamente Bengasi.",
        },
        links=[
            {"label": "Bengasi (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Benghazi"},
            {"label": "Asharq Al-Awsat · mapa de control en Libia (5-6-2025)", "url": "https://english.aawsat.com/features/5151154-haftar-dbeibah-map-control-and-influence-libya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Benghazi_maisons_italiennes.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Benghazi_maisons_italiennes.jpg",
                "credit": "Gabrielle22fkflmd · CC BY-SA 4.0",
                "caption": "Casas italianas de Bengasi.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/%D8%AC%D8%B2%D9%8A%D8%B1%D8%A9_%D8%A7%D9%84%D8%AC%D8%B9%D8%A8,_%D8%A8%D9%86%D8%BA%D8%A7%D8%B2%D9%8A,_%D9%84%D9%8A%D8%A8%D9%8A%D8%A7.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:%D8%AC%D8%B2%D9%8A%D8%B1%D8%A9_%D8%A7%D9%84%D8%AC%D8%B9%D8%A8,_%D8%A8%D9%86%D8%BA%D8%A7%D8%B2%D9%8A,_%D9%84%D9%8A%D8%A8%D9%8A%D8%A7.jpg",
                "credit": "56ab118 · CC BY-SA 4.0",
                "caption": "Una rotonda del centro de Bengasi.",
            },
        ],
    ),
    dict(
        n=12, name="Derna y el Yebel Ajdar · la montaña verde", cat="Naturaleza", prio="Media",
        dog="permitido con condiciones", time="1–2 noches",
        lat=32.7582618, lon=22.649677,  # Google Maps: Derna
        desc="El Yebel Ajdar es la zona MÁS LLUVIOSA de Libia, con unos 600 mm anuales, unos 3.200 km² de bosque mediterráneo de enebro y lentisco, y cumbres de hasta 900 m; viven allí hienas rayadas, zorros rojos y erizos norteafricanos. En su extremo oriental está Derna, devastada el 11 de septiembre de 2023 cuando la tormenta Daniel reventó dos presas sobre el Wadi Derna: al menos 4.352 muertos confirmados y un ministro llegó a decir que había desaparecido el 25 % de la ciudad. La reconstrucción avanza, lastrada por la política.",
        dog_note="Es paisaje abierto de bosque y wadi, sin recinto ni taquilla: el perro puede ir con correa, pero hay hienas rayadas y rebaños con mastines.",
        visit={
            "why": "Es el único paisaje verdaderamente verde del país, un contraste absoluto con el resto de Libia, y el escenario del mayor desastre libio reciente.",
            "see": "Los bosques de enebro y lentisco de la meseta, los wadis encajados que bajan al mar, y en Derna la cicatriz del cauce arrasado y el frente marítimo en obras.",
            "access": "Carretera costera asfaltada entre Susa/Cirene y Tobruk; el tramo del Yebel Ajdar tiene curvas y pendientes largas pero es apto para cualquier vehículo. El pin marca el Wadi Derna a su paso por la ciudad. Control: el LNA de Haftar tomó Derna el 28 de junio de 2018 tras dos años de asedio y el consejo municipal fue destituido tras la riada de 2023; Cirenaica sigue bajo el LNA (Asharq Al-Awsat, 5-6-2025). El MAEC (19-11-2025) cita Derna entre las ciudades expresamente peligrosas.",
            "when": "De marzo a mayo, con la montaña verde y florida; evita el invierno lluvioso por el riesgo de riadas en los wadis.",
            "skip": "Si hay avisos de lluvias fuertes: los wadis del Yebel Ajdar ya demostraron en 2023 lo que pueden hacer.",
        },
        links=[
            {"label": "Derna (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Derna,_Libya"},
            {"label": "Yebel Ajdar (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Jebel_Akhdar,_Libya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Derna,_Libya.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Derna,_Libya.jpg",
                "credit": "مريم محمد الروادي · CC0",
                "caption": "La mezquita de los Sahaba, en Derna.",
            },
        ],
    ),
    dict(
        n=13, name="Tobruk · cementerios de guerra y el desierto de 1942", cat="Cultura", prio="Media",
        dog="no recomendado", time="medio día",
        lat=32.0246717, lon=23.9648005,  # Google Maps: Tobruk War Cemetery
        desc="Puerto del extremo oriental libio, cerca de la frontera egipcia, con unos 120.000 habitantes. Aquí se libró uno de los asedios más famosos de la Segunda Guerra Mundial: los aliados tomaron la plaza el 22 de enero de 1941, la 9ª División australiana —LAS RATAS DE TOBRUK— llegó el 9 de abril, la operación Crusader levantó el cerco en noviembre, Rommel la recuperó en junio de 1942 y los aliados la retomaron tras El Alamein. Desde 2014 la ciudad alberga la Cámara de Representantes, primero en un ferry griego y luego en el hotel Al Masira.",
        dog_note="Los cementerios militares son recintos de respeto y no admiten animales sueltos; el resto es desierto sin sombra.",
        visit={
            "why": "Es el lugar donde la campaña del desierto se vuelve tangible: cementerios, búnkeres y una bahía que explica por sí sola por qué se peleó tanto por ella.",
            "see": "Los cementerios de guerra de la Commonwealth. El de Knightsbridge, en Acroma, 25 km al oeste de Tobruk y 750 m al sur de la carretera Bengasi–Tobruk, reúne 3.651 militares de la Commonwealth, de ellos 2.676 identificados, más 18 sepulturas no pertenecientes a la Commonwealth. El total de enterramientos del cementerio de la ciudad de Tobruk queda POR CONFIRMAR: la web de la CWGC devolvió error 403.",
            "access": "Carretera costera asfaltada desde Derna (~160 km) o desde la frontera egipcia de Musaid; aparcamiento propio en los cementerios, sin problema para dos 4x4. El pin marca el cementerio de guerra de Tobruk; el de Knightsbridge está 25 km al oeste, junto a la misma carretera. Control: Cirenaica bajo el LNA de Haftar; en Tobruk tiene su sede la Cámara de Representantes desde 2014 (Asharq Al-Awsat, 5-6-2025). El MAEC mantiene riesgo extremo para todo el país (19-11-2025).",
            "when": "De octubre a abril, a primera hora; el viento de arena es constante.",
            "skip": "Si no te interesa la historia militar: la ciudad en sí ofrece poco más.",
        },
        links=[
            {"label": "Tobruk (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Tobruk"},
            {"label": "MAEC · recomendaciones de viaje a Libia", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Libia"},
            {"label": "Knightsbridge War Cemetery, Acroma (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Knightsbridge_War_Cemetery"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Commonwealth_cemetery_Tobruk3.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Commonwealth_cemetery_Tobruk3.JPG",
                "credit": "Maher A. A. Abdussalam · Public domain",
                "caption": "El cementerio de la Commonwealth en Tobruk.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/German_war_memorial,_Tobruk03.JPG?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:German_war_memorial,_Tobruk03.JPG",
                "credit": "Maher27777 · Public domain",
                "caption": "El memorial alemán de Tobruk.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Tobruk,_Libya_-_panoramio.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Tobruk,_Libya_-_panoramio.jpg",
                "credit": "Mujaddara · CC BY-SA 3.0",
                "caption": "La ciudad de Tobruk.",
            },
        ],
    ),
    dict(
        n=14, name="Misrata · el puerto y la ciudad mercantil", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=32.3255884, lon=15.0992556,  # Google Maps: Misrata
        desc="Tercera ciudad del país, con unos 881.000 habitantes en 2020, es la CAPITAL ECONÓMICA Y COMERCIAL de Libia: acerías estatales de la Libyan Iron and Steel Company, alfombras y textiles tradicionales, y la lechera Al-Naseem con unos 750 empleados. Su puerto está en la vecina Qasr Ahmad. Resistió el asedio de las fuerzas de Gadafi desde el 20 de marzo de 2011, con más de cuarenta días de artillería, tanques y francotiradores y el agua cortada; más de mil muertos. Sus brigadas siguen siendo un factor de poder en el oeste.",
        dog_note="Ciudad industrial y portuaria, sin espacios verdes accesibles ni alojamiento que admita animales.",
        visit={
            "why": "Es la parada logística lógica entre Trípoli y Sirte: puerto, talleres, repuestos y combustible.",
            "see": "El puerto de Qasr Ahmad, los zocos de alfombras y textiles, y las huellas todavía visibles del asedio de 2011 en la calle Trípoli.",
            "access": "Autopista costera desde Al Khums o Trípoli (~187 km al este de la capital); aparcamiento sin problema. El pin marca el puerto de Qasr Ahmad. Control: ciudad alineada con el Gobierno de Unidad Nacional; Misrata y su entorno figuran en el bloque de Dbeibah (Asharq Al-Awsat, 5-6-2025), y sus milicias se despliegan en las afueras de Sirte. Riesgo extremo en todo el país según el MAEC (19-11-2025).",
            "when": "Cualquier época; en verano el calor húmedo de la costa es incómodo.",
            "skip": "Si no necesitas reabastecer: no hay patrimonio destacado que justifique la parada por sí mismo.",
        },
        links=[
            {"label": "Misrata (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Misrata"},
            {"label": "Asharq Al-Awsat · mapa de control en Libia (5-6-2025)", "url": "https://english.aawsat.com/features/5151154-haftar-dbeibah-map-control-and-influence-libya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Misrata,_Libya.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Misrata,_Libya.jpg",
                "credit": "Mrwan elGobee · CC BY-SA 4.0",
                "caption": "Vista general de Misrata.",
            },
        ],
    ),
    dict(
        n=15, name="Sirte · la ciudad arrasada y el golfo", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=31.189689, lon=16.5701927,  # Google Maps: Sirte
        desc="Ciudad natal de Gadafi y escenario de su muerte, a mitad de camino entre Trípoli y Bengasi, con 128.123 habitantes en el censo de 2013. En 2011 quedó casi completamente en ruinas, aunque más del 70 % de la población había vuelto seis meses después. El Estado Islámico la tomó en mayo de 2015 y la ofensiva respaldada por la ONU la recuperó en 2016, con MÁS DE 400 ataques aéreos estadounidenses y unos 2.000 muertos del EI. El centro de conferencias de Uagadugú, convertido en fortaleza improvisada, quedó destrozado por la artillería.",
        dog_note="Zona con restos de combate y artefactos sin explotar; no es lugar para soltar un perro.",
        visit={
            "why": "Es la lección más clara de los últimos quince años libios: tres guerras seguidas sobre la misma ciudad en una década.",
            "see": "El centro de conferencias de Uagadugú en ruinas, el frente marítimo del golfo de Sidra y los barrios reconstruidos junto a los que siguen destruidos.",
            "access": "Autopista costera desde Misrata (~250 km) o desde Ajdabiya; hay combustible y aparcamiento. El pin marca el centro de conferencias de Uagadugú. Control: es LA LÍNEA DE FRACTURA del país. Las fuerzas de Haftar controlan la ciudad y las milicias de Dbeibah se despliegan en las afueras, hacia Misrata, con Buwairat al-Husun como principal línea de demarcación (Asharq Al-Awsat, 5-6-2025). El MAEC (19-11-2025) cita Sirte entre las ciudades expresamente peligrosas.",
            "when": "De octubre a abril; el tránsito conviene hacerlo de día y de una tirada.",
            "skip": "Si hay tensión entre el LNA y las brigadas de Misrata: la carretera se corta en Buwairat al-Husun.",
        },
        links=[
            {"label": "Sirte (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Sirte"},
            {"label": "Asharq Al-Awsat · mapa de control en Libia (5-6-2025)", "url": "https://english.aawsat.com/features/5151154-haftar-dbeibah-map-control-and-influence-libya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sirte_Libia_2016.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sirte_Libia_2016.jpg",
                "credit": "Gabriele Micalizzi · CC BY-SA 4.0",
                "caption": "Sirte en 2016, frente al centro de conferencias de Uagadugú.",
            },
        ],
    ),
    dict(
        n=16, name="Sebha · la capital del Fezán y el fuerte italiano", cat="Ciudad · servicios", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=27.0365406, lon=14.4290236,  # Google Maps: Sabha
        desc="Capital histórica del Fezán, a unos 640 km al sur de Trípoli, con 99.028 habitantes en el censo de 2012, fue uno de los grandes centros del comercio caravanero libio y la ciudad donde Gadafi creció y cursó la secundaria. Su castillo, el fuerte Elena —originalmente Fortezza Margherita, de época colonial italiana—, aparece en el BILLETE DE DIEZ DINARES, pero hoy es una instalación militar en uso y no se puede visitar. Es el nudo obligado hacia Ubari, Murzuq y el desierto profundo.",
        dog_note="Ciudad de paso con fuerte presencia armada; el fuerte es instalación militar y no se visita.",
        visit={
            "why": "Es el punto de reabastecimiento imprescindible antes de cualquier incursión al Fezán: combustible, agua, talleres y aeropuerto.",
            "see": "La silueta del fuerte Elena desde fuera, el mercado caravanero y los sistemas de riego que sostienen la agricultura del oasis. La universidad de Sebha mantiene trabajo de campo en el desierto.",
            "access": "Carretera asfaltada desde la costa por Brak al-Shati; aeropuerto ampliado a finales de los años setenta. El pin marca el fuerte; recuerda que es acuartelamiento y NO se entra. Control: las fuerzas de Haftar tomaron Sebha en enero de 2019; en mayo de 2020 políticos y activistas locales viraron hacia el GNA y hubo municipios pro-GNA, pero en junio de 2025 Sebha figura bajo control del LNA junto a Brak al-Shati, Ubari y Ghat (Asharq Al-Awsat, 5-6-2025). El MAEC (19-11-2025) desaconseja las regiones fronterizas del sur.",
            "when": "De noviembre a marzo; el verano del Fezán es inviable.",
            "skip": "Si el Fezán no está en el permiso: sin la autorización del sur, Sebha no lleva a ninguna parte.",
        },
        links=[
            {"label": "Sebha (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Sabha,_Libya"},
            {"label": "Asharq Al-Awsat · mapa de control en Libia (5-6-2025)", "url": "https://english.aawsat.com/features/5151154-haftar-dbeibah-map-control-and-influence-libya"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Sebha_Bank_from_Kazem_hotel_2010-02-08.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Sebha_Bank_from_Kazem_hotel_2010-02-08.jpg",
                "credit": "Pierre-Marie Tricaud · CC BY-SA 3.0",
                "caption": "La avenida principal de Sebha, capital del Fezán.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Al-Fadl_ibn_Abbas_Mosque,_Sabha.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Al-Fadl_ibn_Abbas_Mosque,_Sabha.jpg",
                "credit": "مريم محمد الروادي · CC0",
                "caption": "La mezquita Al-Fadl ibn Abbas, en Sebha.",
            },
        ],
    ),
    dict(
        n=17, name="Nalut y el Yebel Nafusa · los graneros bereberes", cat="Cultura", prio="Alta",
        dog="permitido con condiciones", time="1–2 noches",
        lat=31.8742348, lon=10.9750484,  # Google Maps: Nalut
        desc="El Yebel Nafusa es una cadena de 250 km entre Gharyan y Wazzin, en la frontera tunecina, con cumbres de hasta 975 m y población amazig que habla tamazight, lengua reprimida bajo Gadafi. En Nalut, a 789 m y con 26.788 habitantes en 2012, está el Qasr Nalut: un granero fortificado donde las familias guardaban el grano en tiempos de conflicto, una colmena de celdas de barro sobre el barranco. La mezquita de Alal'a, la más antigua del pueblo, se reconstruyó en 1312. Hay además un museo de dinosaurios con fósiles hallados desde 1998.",
        dog_note="El paisaje de meseta y los pueblos se recorren al aire libre; dentro del qasr y de la mezquita de Alal'a, no.",
        visit={
            "why": "Es el equivalente libio de los ksour tunecinos de Tataouine, menos visitado y con una comunidad amazig que reivindica abiertamente su lengua desde 2011.",
            "see": "Las celdas superpuestas del Qasr Nalut sobre el escarpe, la mezquita de Alal'a, los pueblos de Yefren, Jadu, Kabaw y Zintan, y las casas trogloditas de Gharyan, donde el poblamiento original era subterráneo.",
            "access": "Carretera asfaltada desde Trípoli por Gharyan, o desde el paso tunecino de Dehiba–Wazzin; Nalut está a medio camino entre Trípoli y Gadamés. Aparcamiento junto al qasr, con sitio para dos 4x4. El pin marca el Qasr Nalut. Control: Tripolitania, con fuertes consejos locales amazigs; durante 2011 la sierra fue frente y bastión rebelde. Riesgo extremo en todo el país según el MAEC (19-11-2025).",
            "when": "De octubre a mayo. En julio se han registrado 45 °C en Nalut.",
            "skip": "Si ya has hecho los ksour de Tataouine en Túnez y vas corto de días: la tipología se repite.",
        },
        links=[
            {"label": "Nalut (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Nalut"},
            {"label": "Montes Nafusa (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Nafusa_Mountains"},
            {"label": "Gharyan y sus casas trogloditas (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Gharyan"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nalut_ruins.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Nalut_ruins.jpg",
                "credit": "David Stanley · CC BY 2.0",
                "caption": "El qasr de Nalut, el granero bereber.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nalut_old_2.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Nalut_old_2.jpg",
                "credit": "محمد علي يحمد · CC BY-SA 4.0",
                "caption": "Vista general del qasr de Nalut.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Nafusa_Mountains,Libya,_Novembe_2004_(6224205850).jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Nafusa_Mountains,Libya,_Novembe_2004_(6224205850).jpg",
                "credit": "Sludge G · CC BY-SA 2.0",
                "caption": "El Yebel Nafusa.",
            },
        ],
    ),
    dict(
        n=18, name="Murzuq · el ksar y la puerta del Sáhara profundo", cat="Cultura", prio="Media",
        dog="no recomendado", time="1 noche",
        lat=25.9139526, lon=13.9170288,  # Google Maps: Murzuq
        desc="Oasis del Fezán a 453 m, al borde del Idehan Murzuq, un erg extremadamente árido. Fue capital del imperio garamante y, bajo dominio otomano entre 1574 y 1912, se ganó el apodo de «PARÍS DEL SÁHARA» como nudo del comercio transahariano; el viejo fuerte otomano sigue siendo su referencia. Los exploradores británicos del siglo XIX partían de aquí, castigados por la «fiebre de Murzuk». Hoy tiene unos 12.700 habitantes, llueven 7 mm al año y es un lugar castigado: un ataque aéreo contra una boda dejó 43 muertos y 60 heridos.",
        dog_note="Zona de conflicto activo entre comunidades y a cientos de kilómetros de cualquier veterinario.",
        visit={
            "why": "Es la última población antes del desierto profundo y la puerta histórica del comercio transahariano libio.",
            "see": "El fuerte otomano, el palmeral y el borde del Idehan Murzuq, con dunas de gran altura.",
            "access": "Carretera y pista desde Sebha; autonomía total de combustible. El pin marca el fuerte otomano. Control: zona del Fezán en disputa entre comunidades tebu y las fuerzas del LNA, que en 2025 reorganizó su despliegue en el sur; no he encontrado fuente única y fechada que fije quién manda hoy en la ciudad — POR CONFIRMAR. El MAEC (19-11-2025) desaconseja expresamente las regiones fronterizas del sur y advierte de minas y secuestros.",
            "when": "De noviembre a febrero; el verano supera con frecuencia los 40 °C.",
            "skip": "Descártalo salvo que sea etapa obligada hacia el Acacus o Waw an Namus con guía y permiso.",
        },
        links=[
            {"label": "Murzuk (Wikipedia EN)", "url": "https://en.wikipedia.org/wiki/Murzuk"},
            {"label": "MAEC · recomendaciones de viaje a Libia", "url": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Libia"},
        ],
        photos=[
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Murzuq_-_Berberschmuck.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Murzuq_-_Berberschmuck.jpg",
                "credit": "Franzfoto · CC BY-SA 3.0",
                "caption": "Joyería bereber en Murzuq.",
            },
            {
                "img": "https://commons.wikimedia.org/wiki/Special:FilePath/Butcher_at_Murzuq_Libya.jpg?width=1200",
                "source": "https://commons.wikimedia.org/wiki/File:Butcher_at_Murzuq_Libya.jpg",
                "credit": "Bernhard Holub · CC BY-SA 4.0",
                "caption": "Carnicería en Murzuq.",
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
    ("Paso fronterizo de Ras Jedir (Túnez–Libia)", "Frontera", 33.1482141, 11.5624638,  # Google Maps: Libya Border Crossing Station Ra's Ajdir
     "Única entrada terrestre viable a Libia. Reabrió a mediados de 2024; trámites muy lentos y cierres sin aviso. Túnez abrió en abril de 2026 un corredor de tránsito africano por aquí. Control libio variable según la milicia: por confirmar. Pin comprobado en Google Maps («Libya Border Crossing Station Ra's Ajdir»)."),
    ("Paso fronterizo de Dehiba–Wazzin", "Frontera", 32.0134494, 10.6956979,  # Google Maps: Dehiba (lado tunecino de Wazzin)
     "Dehiba (Túnez, gobernación de Tataouine) está a 4 km de la frontera; Wazzin queda al otro lado. Estado para extranjeros SIN CONFIRMAR: Wikipedia solo documenta su uso como vía de suministro en 2011. Pin comprobado en Google Maps («Dehiba (lado tunecino de Wazzin)»)."),
    ("Paso fronterizo de Sallum–Amsaad (Egipto–Libia)", "Frontera", 31.605101, 25.04965,  # Google Maps: Musaid (lado libio de Sallum)
     "Sallum está 8 km al este de la frontera libia. CERRADO A EXTRANJEROS: desde mayo de 2026 el paso queda reservado a nacionales libios y egipcios según el gobierno paralelo del este. Pin comprobado en Google Maps («Musaid (lado libio de Sallum)»)."),
    ("Aeropuerto Internacional de Mitiga, Trípoli", "Frontera", 32.9051438, 13.2738186,  # Google Maps: Mitiga International Airport
     "Único aeropuerto internacional de Trípoli, 8 km al este del centro. Vuelos a Túnez, El Cairo, Estambul, Ammán, Casablanca y Yeda; ITA vuela a diario desde Roma. Puerta de entrada real para cualquier visita autorizada. Pin comprobado en Google Maps («Mitiga International Airport»)."),
    ("Aeropuerto Internacional de Benina, Bengasi", "Frontera", 32.0857184, 20.2651687,  # Google Maps: Aeropuerto Internacional de Benina
     "19 km al este de Bengasi, en zona controlada por el bloque del este. Vuelos a Roma, Estambul, Ammán, El Cairo, Alejandría, Túnez, Dubái y Atenas. Bengasi está en la lista de zonas a evitar del MAEC. Pin comprobado en Google Maps («Aeropuerto Internacional de Benina»)."),
    ("Puerto de Trípoli", "Frontera", 32.9022222, 13.1858333,  # Google Maps: Puerto de Trípoli
     "Carga general, granel y pasajeros según Wikipedia. SIN LÍNEA REGULAR DE PASAJEROS CONFIRMADA para 2026: no sirve como vía de entrada con vehículo desde Europa mientras no lo confirme una naviera. Pin comprobado en Google Maps («Puerto de Trípoli»)."),
    ("Embajada de España en Trípoli", "Consular", 32.8877109, 13.187186,  # Google Maps: Trípoli (la embajada de España no figura como objeto)
     "Al Hawana - Bin Ashour, frente a la Mezquita «Bagui», P.O.B. 23302, Trípoli. Tel. +218 21 362 00 51 / 52, fax +218 21 362 00 61, TRIPOLI-EM@maec.es. Los asuntos consulares se atienden temporalmente desde Túnez. Emergencia consular 24 h: +218 91 320 39 04 y +216 29 174 445. Pin comprobado en Google Maps («Trípoli (la embajada de España no figura como objeto)»)."),
    ("Embajada de España en Túnez (competente en la práctica)", "Consular", 36.8251875, 10.1811875,  # Google Maps: Embajada de España en Túnez
     "22 y 24, Avenue Ernest Conseil, Cité Jardin, 1002 Túnez. Tel. +216 71 782 217, emb.tunez@maec.es, consular emb.tunez.sc@maec.es. Para Libia el MAEC da los fijos +216 71 750 802 y +216 71 801 729. Pin comprobado en Google Maps («Embajada de España en Túnez»)."),
    ("Tripoli Central Hospital", "Hospital", 32.8813641, 13.1905276,  # Google Maps: Hospital central de Trípoli
     "Hospital general, universitario y principal centro de trauma del centro de Trípoli, entre la calle Zawia y la calle Saidi. Segundo mayor del país. Para un europeo, referencia de estabilización antes de evacuar: el MAEC da por normal la evacuación a Europa. Pin comprobado en Google Maps («Hospital central de Trípoli»)."),
    ("Hospital de referencia en Bengasi", "Hospital", 32.0777707, 20.0968138,  # Google Maps: Benghazi Medical Center (1200 Hospital)
     "POR CONFIRMAR. No hemos podido abrir en esta sesión una ficha con coordenadas de un hospital de Bengasi. Las coordenadas son las del centro de Bengasi, no las del hospital: sirven solo para situar la ciudad. Pin comprobado en Google Maps («Benghazi Medical Center (1200 Hospital)»)."),
    ("Combustible en Trípoli (gasolineras autorizadas)", "Combustible", 32.8877109, 13.187186,  # Google Maps: Trípoli (sin gasolinera concreta como objeto)
     "Gasolina a 0,024 USD/litro (GlobalPetrolPrices, 09-02-2026), la más barata del mundo, pero con colas y racionamiento de hecho: en septiembre de 2026 Interior cerró 490 gasolineras por contrabando y autorizó 365. Pin comprobado en Google Maps («Trípoli (sin gasolinera concreta como objeto)»)."),
    ("Agua potable en Libia", "Agua potable", 32.8877109, 13.187186,  # Google Maps: Trípoli
     "SIN PUNTO VERIFICADO. El MAEC advierte de que el suministro no es fiable y recomienda agua embotellada; los apagones desde junio de 2026 dejan sin bombeo depósitos y estaciones. Filtrar y clorar siempre. Pin comprobado en Google Maps («Trípoli»)."),
]

DRONE_CALLOUT = ("danger", "DRONES: PROHIBIDOS SIN PERMISO PREVIO",
                 "La Autoridad de Aviación Civil de Libia prohíbe expresamente operar aeronaves no tripuladas en el espacio aéreo libio sin permiso previo (drone-laws.com, actualizado el 14-01-2026). En un país donde los drones armados han sido protagonistas del conflicto desde 2019, sacar uno de la mochila en un control es buscarse una detención, no una multa. Canadá añade que está prohibido fotografiar instalaciones militares y gubernamentales. Nuestra regla para Libia es tajante: el dron se queda en Túnez, dentro de su maleta y apagado.")

STARLINK_CALLOUT = ("warn", "STARLINK: NO DISPONIBLE EN LIBIA",
                    "Starlink sigue SIN LICENCIA en Libia. Space in Africa informó el 13-09-2026 de que las negociaciones con la General Authority for Communications and Informatics están en suspenso desde agosto de 2026: la autoridad exige una pasarela o hub dentro del país y Starlink se niega, aunque sí acepta registrar una filial local. El servicio no está operativo. Contar con Starlink para comunicarse dentro de Libia no es un plan: es una suposición sin base.")

DOG_MATRIX = [
    ("Entrada al país (aeropuerto de Mitiga, con tour)", "por confirmar", "No hay fuente oficial libia abierta ni relato de nadie que haya entrado con perro. Plan B: dejar al perro en Túnez con residencia canina concertada y no intentarlo."),
    ("Entrada por Ras Jedir con vehículo propio", "prohibido", "El viaje independiente con vehículo no está permitido en la práctica y no hay relatos desde 2012. Plan B: descartado; Libia no se cruza con el perro."),
    ("Tour organizado por Trípoli, Sabratha y Leptis Magna", "no recomendado", "Los itinerarios son en vehículo compartido con guía y policía turística y no contemplan animales. Plan B: quien quiera hacerlo, que lo haga sin perro y con el grupo partido."),
    ("Sur y desierto (Acacus, Ubari, Ghat, Sebha)", "prohibido", "Zonas a evitar según el MAEC y con riesgo de secuestro alto. Plan B: el arte rupestre equivalente se ve en el Tassili n'Ajjer argelino o en el Acacus solo sobre el papel."),
    ("Este (Bengasi, Cirene, Derna)", "prohibido", "Zona de Haftar y todas ellas en la lista de zonas a evitar del MAEC. Plan B: ninguno; queda como capítulo histórico de la ficha."),
    ("Vuelta a la UE desde Libia", "permitido con condiciones", "Solo con titulación antirrábica válida anotada en el pasaporte ANTES de salir de la UE (Reg. 2026/636 no lista a Libia). Plan B: hacer la titulación en España a todos los perros del viaje aunque no se pise Libia."),
]

SOURCES = [
    ("MAEC · Recomendaciones de viaje: Libia (Ministerio de Asuntos Exteriores, consultado el 19-09-2026)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Libia"),
    ("MAEC · Ficha País de Libia, PDF (Oficina de Información Diplomática, enero de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/LIBIA_FICHA%20PAIS.pdf"),
    ("Embajada de España en Trípoli · portada y contacto (MAEC, consultado el 19-09-2026)", "https://www.exteriores.gob.es/Embajadas/tripoli/es/Paginas/index.aspx"),
    ("Embajada de España en Túnez · direcciones y teléfonos (MAEC, consultado el 19-09-2026)", "https://www.exteriores.gob.es/Embajadas/tunez/es/Embajada/Paginas/Contacto.aspx"),
    ("Foreign travel advice: Libya (FCDO, Reino Unido, actualizado el 21-07-2026)", "https://www.gov.uk/foreign-travel-advice/libya"),
    ("Foreign travel advice: Libya — Entry requirements (FCDO, Reino Unido, actualizado el 21-07-2026)", "https://www.gov.uk/foreign-travel-advice/libya/entry-requirements"),
    ("Travel advice and advisories for Libya (Gobierno de Canadá, actualizado el 09-09-2026)", "https://travel.gc.ca/destinations/libya"),
    ("Libya Travel Advisory · Level 4: Do Not Travel (Departamento de Estado de EEUU, 31-08-2026)", "https://travel.state.gov/en/international-travel/travel-advisories/libya.html"),
    ("World Report 2026: Libya (Human Rights Watch, 2026)", "https://www.hrw.org/world-report/2026/country-chapters/libya"),
    ("Libya · Country information (TravelHealthPro / NaTHNaC, consultado el 19-09-2026)", "https://travelhealthpro.org.uk/country/129/libya"),
    ("How to Travel to Libya in 2026 (Against the Compass, actualizado el 24-07-2026)", "https://againstthecompass.com/en/travel-libya/"),
    ("Traveling to Libya; Visiting Libya in 2026, My Experience (OneStep4Ward, 2026)", "https://onestep4ward.com/traveling-to-libya/"),
    ("Can You Enter Libya Overland? A Guide to Land Border Crossings (Saiga Tours, actualizado en 2026)", "https://www.saigatours.com/article/guide-to-libyan-land-border-crossings"),
    ("How to Visit Libya in 2026 (Very Hungry Nomads, 2026)", "https://www.veryhungrynomads.com/how-to-visit-libya/"),
    ("Trip report: Libya, país 172/197 (roadto197, 02-06-2024, viaje de mayo de 2024)", "https://www.roadto197.com/2024/06/02/trip-report-libya/"),
    ("Trip to Libya, the Akakus Mountains, the Ubari Lakes and Leptis Magna (Kumakonda, viaje del 14 al 24-11-2026)", "https://kumakonda.com/trip/trip-to-libya-tadrart-akakus-and-letis-magna/"),
    ("Libya Overland from Egypt (foro Horizons Unlimited / The HUBB, hilo 2012-2014)", "https://www.horizonsunlimited.com/hubb/north-africa/libya-overland-from-egypt-75610"),
    ("Visa policy of Libya (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Visa_policy_of_Libya"),
    ("Tourism in Libya (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Tourism_in_Libya"),
    ("282,000 tourists visited Libya in the first half of 2025 (The Libya Observer, 17-01-2026)", "https://libyaobserver.ly/travel/282000-tourists-visited-libya-first-half-2025"),
    ("Tunisia's New African Transit Corridor via Ras Jedir (Libya Herald, 05-04-2026)", "https://libyaherald.com/2026/04/tunisias-new-african-transit-corridor-via-ras-jedir-an-opportunity-for-libya-to-become-a-trade-gateway-to-sub-saharan-africa/"),
    ("Fuel crisis: 490 petrol stations involved in fuel smuggling closed by Interior Ministry (Libya Herald, septiembre de 2026)", "https://libyaherald.com/2026/09/fuel-crisis-490-petrol-stations-involved-in-fuel-smuggling-closed-by-interior-ministry"),
    ("Libya gasoline prices (GlobalPetrolPrices, dato del 09-02-2026)", "https://www.globalpetrolprices.com/Libya/gasoline_prices/"),
    ("Starlink's Libya Market Entry Remains on Hold as Negotiations Continue (Space in Africa, 13-09-2026)", "https://spaceinafrica.com/2026/09/13/starlinks-libya-market-entry-remains-on-hold-as-negotiations-continue/"),
    ("Libya SIM Card & eSIM · Internet & WiFi Guide (Things To Do In Libya, guía de 2026)", "https://thingstodoinlibya.com/connectivity/"),
    ("Libya Drone Laws (drone-laws.com, actualizado el 14-01-2026)", "https://drone-laws.com/drone-laws-in-libya/"),
    ("Libya Pet Import Requirements (PetTravel.com, consultado el 19-09-2026)", "https://www.pettravel.com/information/pet-passports/libya-pet-import-requirements/"),
    ("Reglamento de Ejecución (UE) 2026/636 de la Comisión, de 20 de marzo de 2026, sobre listas de terceros países para desplazamientos sin ánimo comercial de animales de compañía (EUR-Lex)", "https://eur-lex.europa.eu/legal-content/ES/TXT/HTML/?uri=OJ%3AL_202600636"),
    ("Carnet de Passages · ficha de Libia y emisor nacional (carnetdepassage.org, consultado el 19-09-2026)", "https://www.carnetdepassage.org/country/libya"),
    ("International Motor Insurance Card System · miembros del sistema Carta Verde (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/International_Motor_Insurance_Card_System"),
    ("Libya · States Parties del Patrimonio Mundial (UNESCO, consultado el 19-09-2026)", "https://whc.unesco.org/en/statesparties/ly"),
    ("List of World Heritage in Danger (UNESCO, consultado el 19-09-2026)", "https://whc.unesco.org/en/danger/"),
    ("Rock-Art Sites of Tadrart Acacus (UNESCO, ficha del sitio 287, consultado el 19-09-2026)", "https://whc.unesco.org/en/list/287/"),
    ("Ras Ajdir (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Ras_Ajdir"),
    ("Dehiba (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Dehiba"),
    ("Sallum (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Sallum"),
    ("Ghat, Libya (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Ghat,_Libya"),
    ("Mitiga International Airport (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Mitiga_International_Airport"),
    ("Benina International Airport (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Benina_International_Airport"),
    ("Port of Tripoli (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Port_of_Tripoli"),
    ("Tripoli Central Hospital (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/Tripoli_Central_Hospital"),
    ("2026 in Libya · cronología de sucesos (Wikipedia, consultado el 19-09-2026)", "https://en.wikipedia.org/wiki/2026_in_Libya"),
    ("Trípoli (Wikipedia EN)", "https://en.wikipedia.org/wiki/Tripoli,_Libya"),
    ("Arco de Marco Aurelio (Wikipedia EN)", "https://en.wikipedia.org/wiki/Arch_of_Marcus_Aurelius_(Tripoli)"),
    ("Museo del castillo Rojo / Museo Nacional de Libia (Wikipedia EN)", "https://en.wikipedia.org/wiki/Red_Castle_Museum"),
    ("UNESCO · Archaeological Site of Leptis Magna (ref. 183)", "https://whc.unesco.org/en/list/183"),
    ("Leptis Magna (Wikipedia EN)", "https://en.wikipedia.org/wiki/Leptis_Magna"),
    ("UNESCO · los cinco sitios libios pasan a la Lista en Peligro (14-7-2016)", "https://whc.unesco.org/en/news/1523"),
    ("UNESCO · Archaeological Site of Sabratha (ref. 184)", "https://whc.unesco.org/en/list/184"),
    ("Sabratha (Wikipedia EN)", "https://en.wikipedia.org/wiki/Sabratha"),
    ("UNESCO · Archaeological Site of Cyrene (ref. 190)", "https://whc.unesco.org/en/list/190"),
    ("Cirene (Wikipedia EN)", "https://en.wikipedia.org/wiki/Cyrene,_Libya"),
    ("Shahhat, la población actual junto al yacimiento (Wikipedia EN)", "https://en.wikipedia.org/wiki/Shahhat"),
    ("Apolonia de Cirenaica (Wikipedia EN)", "https://en.wikipedia.org/wiki/Apollonia,_Cyrenaica"),
    ("Susa / Marsa Susa (Wikipedia EN)", "https://en.wikipedia.org/wiki/Susa,_Libya"),
    ("Lista de museos de Libia (Wikipedia EN)", "https://en.wikipedia.org/wiki/List_of_museums_in_Libya"),
    ("Ptolemais de Cirenaica (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ptolemais,_Cyrenaica"),
    ("Bengasi, base logística más próxima (Wikipedia EN)", "https://en.wikipedia.org/wiki/Benghazi"),
    ("UNESCO · Old Town of Ghadamès (ref. 362)", "https://whc.unesco.org/en/list/362"),
    ("Gadamés (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ghadames"),
    ("Libya Observer · la UNESCO retira Gadamés de la Lista en Peligro (2025)", "https://libyaobserver.ly/culture/unesco-old-ghadames-no-longer-considered-world-heritage-danger"),
    ("UNESCO · Rock-Art Sites of Tadrart Acacus (ref. 287)", "https://whc.unesco.org/en/list/287"),
    ("UNESCO · estado de conservación 2024 (se mantiene en la Lista en Peligro)", "https://whc.unesco.org/en/soc/4547"),
    ("Montes Acacus (Wikipedia EN)", "https://en.wikipedia.org/wiki/Tadrart_Acacus"),
    ("Gaberoun (Wikipedia EN)", "https://en.wikipedia.org/wiki/Gaberoun"),
    ("Idehan Ubari (Wikipedia EN)", "https://en.wikipedia.org/wiki/Idehan_Ubari"),
    ("Ubari (Wikipedia EN)", "https://en.wikipedia.org/wiki/Ubari"),
    ("Waw an Namus (Wikipedia EN)", "https://en.wikipedia.org/wiki/Waw_an_Namus"),
    ("Asharq Al-Awsat · mapa de control en Libia (5-6-2025)", "https://english.aawsat.com/features/5151154-haftar-dbeibah-map-control-and-influence-libya"),
    ("Derna (Wikipedia EN)", "https://en.wikipedia.org/wiki/Derna,_Libya"),
    ("Yebel Ajdar (Wikipedia EN)", "https://en.wikipedia.org/wiki/Jebel_Akhdar,_Libya"),
    ("Tobruk (Wikipedia EN)", "https://en.wikipedia.org/wiki/Tobruk"),
    ("Knightsbridge War Cemetery, Acroma (Wikipedia EN)", "https://en.wikipedia.org/wiki/Knightsbridge_War_Cemetery"),
    ("Misrata (Wikipedia EN)", "https://en.wikipedia.org/wiki/Misrata"),
    ("Sirte (Wikipedia EN)", "https://en.wikipedia.org/wiki/Sirte"),
    ("Sebha (Wikipedia EN)", "https://en.wikipedia.org/wiki/Sabha,_Libya"),
    ("Nalut (Wikipedia EN)", "https://en.wikipedia.org/wiki/Nalut"),
    ("Montes Nafusa (Wikipedia EN)", "https://en.wikipedia.org/wiki/Nafusa_Mountains"),
    ("Gharyan y sus casas trogloditas (Wikipedia EN)", "https://en.wikipedia.org/wiki/Gharyan"),
    ("Murzuk (Wikipedia EN)", "https://en.wikipedia.org/wiki/Murzuk"),
]

# Franja costera: Ras Ajdir → Sabratha → Trípoli → Leptis Magna → Misrata → Sirte → Bengasi → Pentápolis → Tobruk
CORRIDOR = [
    (32.933, 12.083),
    (32.7811, 12.44952),
    (32.89997, 13.17597),
    (32.6343, 14.29484),
    (32.32559, 15.09926),
    (31.18969, 16.57019),
    (30.75556, 20.22528),
    (32.11942, 20.08679),
    (32.70596, 20.95395),
    (32.80358, 21.86217),
    (32.8954, 21.96119),
    (32.75826, 22.64968),
    (32.02467, 23.9648),
]

# Bucle interior y Fezán: Trípoli → Gharyan → Nalut → Gadamés → Sebha → lagos de Ubari → Murzuq → Ghat → Acacus
CORRIDOR_ALT = [
    (32.89997, 13.17597),
    (32.16972, 13.01667),
    (31.87423, 10.97505),
    (30.13176, 9.49506),
    (27.03654, 14.42902),
    (26.583, 12.767),
    (26.80306, 13.53528),
    (25.91395, 13.91703),
    (24.95944, 10.17583),
    (24.83333, 10.33333),
]

HISTORIA_RESUMEN = "Libia es un país de historia densa y presente roto. En su costa se superpusieron la Tripolitania fenicia y púnica, la Cirenaica griega, Roma, el islam y cuatro siglos otomanos, antes de que Italia la ocupara en 1911 y la gobernara con una violencia que diezmó Cirenaica. Fue reino independiente desde 1951 con Idris I, y desde 1969 el escenario de los cuarenta y dos años de Muamar el Gadafi, sostenidos por el petróleo. La revuelta de 2011 acabó con él y abrió una fractura que sigue abierta: a fecha de 2026 conviven el Gobierno de Unidad Nacional de Trípoli y el bloque oriental de Bengasi asociado a Jalifa Haftar. El país está fuera de cualquier ruta overland: España desaconseja viajar y no se expiden visados turísticos ordinarios."

HISTORIA_SECCIONES = [
    ("Orígenes y reinos anteriores a la colonización",
     "<p>Lo que hoy llamamos Libia fueron durante milenios tres países distintos: la <strong>Tripolitania</strong> al oeste, la <strong>Cirenaica</strong> al este y el <strong>Fezán</strong> en el desierto meridional, una división que el MAEC todavía usa para explicar el país. En la costa occidental los fenicios y después Cartago levantaron los emporios que dieron nombre a la región —Oea, Sabratha y Leptis Magna—, mientras que en la oriental fueron colonos griegos quienes fundaron Cirene, cabeza de la Pentápolis. Roma heredó ambas y convirtió Leptis Magna en una de las ciudades más monumentales del Mediterráneo africano; sus ruinas figuran hoy entre los cinco bienes libios del Patrimonio Mundial.</p><p>En el siglo VII la conquista árabe islamizó y arabizó el territorio de forma duradera, aunque los oasis y las montañas conservaron población amazigh, tuareg y tebu. A comienzos del siglo XVI el litoral pasó al <strong>Imperio otomano</strong>, que lo gobernó, con la autonomía casi dinástica de los <em>Karamanlí</em> entre 1711 y 1835, hasta la invasión italiana. En 1837 nació en Cirenaica la cofradía <strong>senusí</strong>, una orden islámica que, según Britannica, dio a las tribus del interior una estructura común y que acabaría proporcionando al país su primera dinastía nacional.</p>"),
    ("Colonización",
     "<p>La potencia colonial fue <strong>Italia</strong>, que invadió en 1911 en el curso de la guerra ítalo-turca y obtuvo el reconocimiento formal del traspaso otomano en 1912. La ocupación efectiva, sin embargo, tardó veinte años: la resistencia senusí, encabezada en Cirenaica por <strong>Omar al-Mujtar</strong>, mantuvo en jaque a los italianos hasta que las llamadas campañas de pacificación de 1923 a 1932, dirigidas por los generales Badoglio y Graziani, la aplastaron con ejecuciones masivas, armas químicas y deportaciones.</p><p>El coste demográfico fue enorme. Según la documentación recogida en Wikipedia, murió en torno a <strong>una cuarta parte de los 225.000 habitantes de Cirenaica</strong>; unos 12.000 cirenaicos fueron ejecutados entre 1930 y 1931 y, de los 100.000 internados en campos de concentración, 40.000 habían muerto en septiembre de 1933. En 1934 el gobernador Italo Balbo unificó Tripolitania y Cirenaica en la colonia de Libia, con Trípoli por capital, y promovió una colonización agrícola que llevó el número de italianos de 26.000 en 1927 a 119.139 en 1939, un trece por ciento de la población. Dejó también infraestructura —unos 400 kilómetros de ferrocarril y 4.000 de carretera— y un país sin élites propias. El dominio italiano terminó en mayo de 1943, arrasado por la campaña del norte de África.</p>"),
    ("Independencia y construcción del Estado",
     "<p>Tras la guerra, Libia quedó bajo administración aliada. En noviembre de 1949 Naciones Unidas decidió que debía convertirse en un reino unido e independiente antes del 1 de enero de 1952, y el <strong>24 de diciembre de 1951</strong> el emir senusí <strong>Idris I</strong> proclamó la independencia. Nacía una monarquía federal que unía las tres provincias históricas y que, según Britannica, ingresó en la Liga Árabe en 1953. Era uno de los países más pobres del mundo; el hallazgo de petróleo a finales de aquella década lo transformó por completo.</p><p>En <strong>1969</strong> un golpe de Estado encabezado por el coronel <strong>Muamar el Gadafi</strong> derrocó al rey. La ficha del MAEC lo describe como «un régimen autoritario personalista inspirado en el panarabismo y el socialismo», y se prolongó cuarenta y dos años. Gadafi nacionalizó el petróleo, refundó el Estado como <em>Yamahiriya</em> —una supuesta democracia directa de comités populares, sin partidos ni parlamento— y empleó la renta del crudo en educación, sanidad y grandes obras hidráulicas tanto como en aventuras exteriores. Wikipedia recoge que la esperanza de vida se acercó entonces a los setenta y ocho años y la renta por habitante superó los once mil dólares. El precio fue la ausencia de instituciones autónomas, un vacío decisivo cuando el régimen cayó.</p>"),
    ("Historia reciente (2000-2026)",
     "<p>El <strong>17 de febrero de 2011</strong> comenzó en Bengasi un levantamiento contra Gadafi que derivó en guerra civil. Una coalición dirigida por la OTAN intervino el 21 de marzo de 2011 y, el <strong>20 de octubre de 2011</strong>, Gadafi murió a manos de los sublevados. La euforia duró poco: las milicias vencedoras se negaron a desarmarse.</p><p>En 2014 el país se partió en dos. La <strong>Cámara de Representantes</strong> inició sus sesiones el 5 de agosto de 2014 y acabó instalándose en <strong>Tobruk</strong>, respaldada por el <strong>Ejército Nacional Libio</strong> de <strong>Jalifa Haftar</strong>, frente a las autoridades de Trípoli. El acuerdo de la ONU de diciembre de 2015 creó un Gobierno de Acuerdo Nacional, presidido por Fayez al-Sarraj, que la Cámara nunca ratificó. En abril de 2019 Haftar lanzó una ofensiva sobre Trípoli que fracasó y desembocó en el <strong>alto el fuego permanente del 23 de octubre de 2020</strong>, del que salió el <strong>16 de marzo de 2021</strong> el actual Consejo Presidencial y el Gobierno de Unidad Nacional. Las elecciones del <strong>24 de diciembre de 2021</strong> se aplazaron <em>sine die</em> y desde marzo de 2022 hay de nuevo un gobierno paralelo en el este. En septiembre de 2023 el derrumbe de dos presas arrasó Derna; en mayo de 2025 Trípoli volvió a los combates entre milicias.</p>"),
    ("Política y gobierno en 2026",
     "<p>Libia es una república en transición sin constitución: la ficha del MAEC, de <strong>enero de 2026</strong>, señala que la forma del Estado se decidirá en un texto aún sin aprobar. El jefe de Estado colegiado es el <strong>Consejo Presidencial</strong> que preside <strong>Mohamed Yunus al-Menfi</strong>, y el jefe de Gobierno <strong>Abdul Hamid Dbeiba</strong>, del <strong>Gobierno de Unidad Nacional</strong>: ambos ocupan el cargo <strong>desde el 16 de marzo de 2021</strong>, designados por el Foro de Diálogo Político Libio, no elegidos en las urnas. Frente a ellos, la Cámara de Representantes de Tobruk, que preside Aguila Saleh, sostiene desde marzo de 2022 un ejecutivo paralelo —el Gobierno de Estabilidad Nacional, de Osama Hammad— apoyado en las fuerzas de Haftar, que según Human Rights Watch controlan el este y el sur, mientras Trípoli controla el oeste.</p><p>El proceso electoral sigue parado. Tras el fracaso de 2021, el <strong>30 de agosto de 2026</strong> delegaciones de ambos bloques firmaron con la misión de la ONU, que encabeza Hanna Tetteh, un acuerdo para celebrar presidenciales y legislativas <strong>en un plazo máximo de dos años</strong>, no más tarde de 2028; el Consejo Presidencial y el Alto Consejo de Estado no participaron. <strong>Freedom House</strong> la clasifica en 2025 como <em>Not Free</em>, «no libre», con <strong>10 puntos sobre 100</strong>, 2 sobre 40 en derechos políticos y 8 sobre 60 en libertades civiles: no es una democracia, ni siquiera limitada, sino un territorio repartido entre autoridades rivales y grupos armados donde no se vota. Reporteros Sin Fronteras lo sitúa en 2026 en el <strong>puesto 138 de 180</strong> y habla de un «agujero negro informativo». El MAEC llama a la seguridad «inestable y volátil», <strong>desaconseja viajar salvo necesidad absoluta</strong> y confirma que no se expiden visados de turismo. España reabrió embajada en Trípoli en junio de 2021; la UE mantiene las operaciones IRINI y EUBAM.</p>"),
    ("Economía y recursos",
     "<p>La riqueza libia es el <strong>petróleo</strong>, y casi solo el petróleo. La ficha del MAEC da para 2024 un PIB de unos <strong>46.600 millones de dólares</strong> y una renta por habitante de aproximadamente <strong>6.570 dólares</strong>, con una caída del 2,9 por ciento y una inflación media del 2,1 por ciento. La industria, dominada por el crudo y el gas, supone el 56,2 por ciento de la economía; los servicios el 42,1 y la agricultura apenas un 3. Las exportaciones sumaron 35.400 millones de dólares en 2023 frente a 22.400 de importaciones, y los hidrocarburos son cerca del noventa y cinco por ciento de lo que el país vende fuera. Libia pertenece a la OPEP y posee, según Wikipedia, las décimas reservas probadas de crudo del mundo.</p><p>La moneda es el <strong>dinar libio</strong>, de mil dirhams. Los principales clientes son Italia (22,5 por ciento), Alemania (14,6) y España (8,72); los proveedores, China, Turquía y los Emiratos Árabes Unidos. El reverso es duro: apenas un uno por ciento del territorio es cultivable y el país importa la mayor parte de sus alimentos, el desempleo rondaba el 19,1 por ciento —cerca del cincuenta entre los jóvenes— y el control de la Corporación Nacional del Petróleo y del banco central ha sido una y otra vez el verdadero objeto de la disputa entre ambos gobiernos. El turismo es hoy testimonial.</p>"),
    ("Sociedad: idiomas, religión y cultura",
     "<p>Libia tiene unos <strong>7,3 millones de habitantes</strong> (2023) en 1.759.540 kilómetros cuadrados, más de tres veces España, con cuatro habitantes por kilómetro y un 81,6 por ciento de población urbana en la costa: Trípoli, Misrata, Bengasi, Zauiya y Tobruk. El idioma oficial es el <strong>árabe</strong>, en variante libia; el MAEC señala el inglés como segunda lengua y es con lo que un extranjero se entiende por carretera, con algo de italiano entre los mayores. En los oasis y las montañas se hablan además <strong>amazigh, tuareg y tebu</strong>. La religión es abrumadoramente musulmana: el MAEC da un 98 por ciento, mayoría suní con minoría ibadí; el resto son cristianos y otros credos, casi todos extranjeros.</p><p>La cocina mezcla Mediterráneo y Magreb: cuscús, la sopa <em>sharba libiya</em>, pasta heredada de los italianos, dátiles y té. El patrimonio es excepcional —Leptis Magna, Sabratha, Cirene, el arte rupestre del Tadrart Acacus y el casco antiguo de Gadamés—, pero los cinco bienes entraron en la <strong>Lista del Patrimonio Mundial en Peligro en 2016</strong> y cuatro siguen en ella; solo Gadamés salió en 2025. Quien llegue hasta aquí debe vestir cubierto, hombres y mujeres, no fotografiar personas ni militares ni controles sin permiso, y contar con que el alcohol está prohibido. Durante el <strong>ramadán</strong>, que en 2027 empieza en torno al 8 de febrero, no se come, bebe ni fuma en público de día y los horarios se trastocan.</p>"),
]

HISTORIA_FUENTES = [
    ("Ficha País Libia (MAEC España · PDF · enero de 2026)", "https://www.exteriores.gob.es/Documents/FichasPais/LIBIA_FICHA%20PAIS.pdf"),
    ("Recomendaciones de viaje: Libia (MAEC España · actualizado 19 de noviembre de 2025)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Libia"),
    ("Libya: Freedom in the World 2025 (Freedom House · 2025)", "https://freedomhouse.org/country/libya/freedom-world/2025"),
    ("Libya: History (Britannica · consultado en septiembre de 2026)", "https://www.britannica.com/place/Libya/History"),
    ("Libya — States Parties (UNESCO Centro del Patrimonio Mundial)", "https://whc.unesco.org/en/statesparties/ly"),
    ("List of World Heritage in Danger (UNESCO · consultado en septiembre de 2026)", "https://whc.unesco.org/en/danger-list/"),
    ("Old Town of Ghadamès (UNESCO · en peligro 2016-2025)", "https://whc.unesco.org/en/list/362/"),
    ("Libia (Wikipedia en español · consultado en septiembre de 2026)", "https://es.wikipedia.org/wiki/Libia"),
    ("Libya (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Libya"),
    ("Italian Libya (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Italian_Libya"),
    ("Libyan crisis (2011-present) (Wikipedia en inglés · consultado en septiembre de 2026)", "https://en.wikipedia.org/wiki/Libyan_crisis_(2011%E2%80%93present)"),
    ("Libya: Events of 2025 (Human Rights Watch · World Report 2026)", "https://www.hrw.org/world-report/2026/country-chapters/libya"),
    ("Libya (Reporteros Sin Fronteras · Índice 2026, puesto 138 de 180)", "https://rsf.org/en/country/libya"),
    ("El este y el oeste de Libia acuerdan celebrar elecciones en un plazo máximo de dos años (EFE / SWI swissinfo.ch · 30 de agosto de 2026)", "https://www.swissinfo.ch/spa/el-este-y-el-oeste-de-libia-acuerdan-celebrar-elecciones-en-un-plazo-m%C3%A1ximo-de-dos-a%C3%B1os/91976926"),
    ("How to travel to Libya in 2026 (Against the Compass · actualizado 24 de julio de 2026)", "https://againstthecompass.com/en/travel-libya/"),
]

SPEC = dict(
    slug="libia", name="Libia", revision="18 sep 2026",
    sub="EXCLUIDO POR PROTOCOLO — conflicto activo y país partido en dos gobiernos · ficha informativa e histórica: cinco sitios UNESCO, TODOS en la Lista del Patrimonio Mundial en Peligro desde 2016",
    chips=[
        ("ESTATUS", "EXCLUIDO. Fuera de la ruta prevista. Ficha informativa; no se planifica entrada con los vehículos."),
        ("CÓMO LLEGAR", "Solo en avión y con tour cerrado: Túnez–Mitiga (Libyan Wings, Tunisair) o Roma–Mitiga (ITA)…"),
        ("VISADO", "NO hay visado turístico independiente. eVisa turístico desde el 21-03-2024 en…"),
        ("VEHÍCULO", "Sin dato oficial abierto sobre admisión temporal de vehículos extranjeros…"),
        ("SEGURIDAD", "MAEC: no viajar salvo necesidad · EEUU nivel 4"),
        ("SEGURO", "Sin Carta Verde · seguro libio en frontera, sin confirmar"),
        ("SALUD", "Sin vacunas obligatorias · fiebre amarilla si procede"),
        ("DRONES", "PROHIBIDOS sin permiso de Aviación Civil libia"),
        ("STARLINK", "NO disponible · sin licencia (septiembre de 2026)"),
        ("4x4", "Sin entrada documentada con vehículo propio desde 2012"),
        ("A PIE", "Imposible: guía y policía turística obligatorios"),
        ("PERRO", "Microchip ISO y rabia entre 30 días y 12 meses, con certificado veterinario oficial (PetTravel)…"),
        ("MONEDA", "Dinar libio (LYD). Prohibido sacar dinares del país…"),
        ("VENTANA", "Mediterráneo en la costa y desértico en el interior…"),
    ],
    center=[28.87, 16.73], zoom=5,
    notice="Documento de planificación de un país FUERA DE LA RUTA PREVISTA: no forma parte de la ruta 2027. La ficha se mantiene completa por si en el futuro cambia la situación o se plantea un viaje aparte. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de cualquier entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label="Franja costera: Ras Ajdir → Sabratha → Trípoli → Leptis Magna → Misrata → Sirte → Bengasi → Pentápolis → Tobruk",
    corridor_alt_label="Bucle interior y Fezán: Trípoli → Gharyan → Nalut → Gadamés → Sebha → lagos de Ubari → Murzuq → Ghat → Acacus",
    hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Leptis_Magna_-_Severan_Basilika.jpg?width=1200",
    hero_credit="Leptis Magna · Franzfoto · CC BY-SA 3.0",
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    decision="Libia queda FUERA DE LA RUTA y excluida en la práctica, y no por capricho: el MAEC desaconseja viajar al país salvo caso de necesidad y enumera como zonas a evitar Derna, Bengasi, Beni Walid, Sirte, Ubari, Ghadames, Ghat, Sebha y toda la franja fronteriza sur con Chad, Níger, Sudán y Argelia; el FCDO desaconseja todo viaje a casi todo el territorio (21-07-2026) y el Departamento de Estado mantiene el nivel 4 «do not travel» desde el 31-08-2026. El país está partido entre el Gobierno de Unidad Nacional en Trípoli y el bloque de Bengasi con las fuerzas de Haftar, con milicias armadas, munición sin explotar a las afueras de Trípoli y secuestro de extranjeros como riesgo real (HRW, informe 2026). Además el viaje independiente NO está permitido: el visado turístico electrónico existe desde marzo de 2024, pero lo patrocina una agencia libia autorizada y obliga a guía y policía turística; ningún relato reciente describe entrada con vehículo propio matriculado en Europa. Si algún día fuera viable, se haría APARTE de la expedición: vuelo Túnez–Mitiga y tour cerrado de 3 a 6 días con agencia autorizada, entre 1.100 € (Trípoli, Sabratha y Leptis Magna, roadto197, mayo de 2024) y 2.850 € (Acacus y Ubari, Kumakonda, noviembre de 2026), más eVisa de 63 USD. Lo que habría que decidir: quién se queda con los dos coches y el perro en Túnez, y si el seguro de la expedición cubre siquiera la escala.",
    facts=[
        ("Estatus", "EXCLUIDO. Fuera de la ruta prevista. Ficha informativa; no se planifica entrada con los vehículos."),
        ("Cómo llegar", "Solo en avión y con tour cerrado: Túnez–Mitiga (Libyan Wings, Tunisair) o Roma–Mitiga (ITA). Por tierra, solo Ras Jedir desde Túnez y con trámites muy lentos."),
        ("Visado", "NO hay visado turístico independiente. eVisa turístico desde el 21-03-2024 en evisa.gov.ly: 63 USD, una entrada, 30 días, patrocinado por agencia libia autorizada. El MAEC sigue diciendo que no se expiden visados de turismo y que hacen falta visado de entrada Y de salida."),
        ("Vehículo/aduana", "Sin dato oficial abierto sobre admisión temporal de vehículos extranjeros. El emisor de CPD es el Automobile and Touring Club of Libya (+218 213403201). Conducción por la derecha."),
        ("Seguro", "Libia NO es miembro del sistema de Carta Verde (solo Marruecos y Túnez en el norte de África). Habría que contratar seguro libio en frontera; sin confirmar que exista ventanilla para extranjeros."),
        ("Moneda", "Dinar libio (LYD). Prohibido sacar dinares del país. Tarjetas prácticamente inútiles: solo efectivo en euros o dólares y cambio en mercado paralelo. 1 EUR = 6,24 LYD (Ficha País MAEC, enero de 2026)."),
        ("Perro", "Microchip ISO y rabia entre 30 días y 12 meses, con certificado veterinario oficial (PetTravel). NO hemos localizado la web del servicio veterinario nacional libio. De vuelta a la UE: Libia no está en la lista del Reg. (UE) 2026/636, así que titulación antirrábica previa."),
        ("Drones", "PROHIBIDO volar sin permiso previo de la Autoridad de Aviación Civil libia. Canadá añade que está prohibido fotografiar instalaciones militares y gubernamentales."),
        ("Starlink", "NO disponible. Sin licencia: las negociaciones con la General Authority for Communications and Informatics siguen suspendidas (Space in Africa, 13-09-2026)."),
        ("Seguridad", "MAEC: desaconseja viajar salvo necesidad. FCDO: todo viaje desaconsejado en casi todo el país. EEUU: nivel 4. Canadá: evitar todo viaje. Milicias, falsos controles, secuestros y minas."),
        ("Clima", "Mediterráneo en la costa y desértico en el interior. La mejor ventana para el desierto y las ruinas es de octubre a abril (OneStep4Ward, 2026)."),
        ("Sanidad", "Red sanitaria muy degradada y desabastecimiento de medicamentos; el MAEC da por normal la evacuación a Europa. Seguro con evacuación aérea imprescindible."),
    ],
    alerts=[
        "El MAEC DESACONSEJA VIAJAR A LIBIA SALVO CASO DE NECESIDAD y señala como zonas a evitar Derna, Bengasi, Beni Walid, Sirte, Ubari, Ghadames, Ghat, Sebha y toda la frontera sur con Chad, Níger, Sudán y Argelia.",
        "País partido: el Gobierno de Unidad Nacional controla el oeste desde Trípoli y las fuerzas de Haftar el este y el sur. Un visado emitido por un lado puede no ser reconocido por el otro (FCDO, 21-07-2026).",
        "VIAJE INDEPENDIENTE PROHIBIDO en la práctica: la agencia libia que patrocina el eVisa debe acompañarte con guía y policía turística; Canadá añade que salir de Trípoli exige autorización libia.",
        "Registro policial obligatorio al llegar: en 7 días según el FCDO, en 3 días según el Departamento de Estado de EEUU. La contradicción está sin resolver y las multas son reales.",
        "Pasaporte con cualquier rastro de viaje a Israel: entrada denegada. Lo dicen el MAEC, el FCDO y Wikipedia sobre la política de visados.",
        "Minas y munición sin explotar. HRW documenta en su informe de 2026 que en septiembre de 2025 tres menores resultaron heridos por artefactos sin detonar en Khallet al-Ferjan, a las afueras de Trípoli.",
        "Enfrentamientos armados sin aviso: en mayo de 2025 la muerte del comandante Ghneiwa al-Kikli desató combates intensos entre grupos armados en Trípoli (HRW, 2026); un viajero presenció un tiroteo en Trípoli en 2026 (OneStep4Ward).",
        "Crisis de combustible pese a tener la gasolina más barata del mundo: en septiembre de 2026 Interior cerró 490 gasolineras por contrabando y solo autorizó 365; colas largas de gasolina y gasóleo (Libya Herald).",
        "Starlink NO tiene licencia en Libia y el país ordena apagones nacionales de internet en época de exámenes y en momentos políticos.",
        "Los cinco sitios UNESCO del país —Cirene, Leptis Magna, Sabratha, Ghadamès y el arte rupestre del Tadrart Acacus— están en la Lista del Patrimonio Mundial en Peligro desde el 14 de julio de 2016.",
    ],
    ruta_intro="Itinerario de referencia que enlaza los 18 puntos de interés por las carreteras principales, calculado sobre 250 km/día. No es una ruta aprobada del proyecto: sirve para dimensionar un posible viaje aparte y para saber qué hay en cada tramo.",
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("1 · Frontera y litoral oeste", "Ras Ajdir → Zuwara → Sabratha", "~110 km · 1 día"),
        ("2 · Trípoli", "Sabratha → Trípoli (medina, arco, castillo Rojo)", "~70 km · 2 días"),
        ("3 · Leptis Magna", "Trípoli → Al Khums (Leptis Magna)", "~130 km · 1 día"),
        ("4 · Misrata", "Al Khums → Misrata (puerto de Qasr Ahmad)", "~90 km · 1 día"),
        ("5 · Golfo de Sidra I", "Misrata → Sirte", "~250 km · 1 día"),
        ("6 · Golfo de Sidra II", "Sirte → Ajdabiya", "~470 km · 2 días"),
        ("7 · Bengasi", "Ajdabiya → Bengasi", "~160 km · 1 día"),
        ("8 · Pentápolis I", "Bengasi → Tolmeita (Ptolemais)", "~110 km · 1 día"),
        ("9 · Pentápolis II", "Tolmeita → Shahhat (Cirene)", "~100 km · 1 día"),
        ("10 · Apolonia", "Cirene → Susa (Apolonia) y Yebel Ajdar", "~25 km · 1 día"),
        ("11 · Derna", "Susa → Derna (Wadi Derna)", "~70 km · 1 día"),
        ("12 · Tobruk", "Derna → Tobruk (cementerios de guerra)", "~160 km · 1 día"),
        ("13 · Yebel Nafusa (bucle alt.)", "Trípoli → Gharyan → Nalut", "~260 km · 1–2 días"),
        ("14 · Gadamés (bucle alt.)", "Nalut → Gadamés", "~350 km · 1–2 días"),
    ],
    offroad=[
        "Punto de partida legal: NO existe conducción libre. El régimen de visados exige operador turístico o patrocinador y escolta de policía turística, y declara que «el viaje independiente en Libia con fines turísticos no está permitido en general»; cualquier pista que se describa aquí se recorre con guía y permiso o no se recorre.",
        "Tadrart Acacus: el acceso a los abrigos es por pista de arena y roca desde Ghat, con guía tuareg obligatorio; el macizo tiene casi 3,9 millones de hectáreas y linda con el Tassili n'Ajjer argelino, por lo que la navegación sin guía es temeraria. La UNESCO lo mantiene en la Lista en Peligro en su informe de 2024, con vandalismo y tráfico ilícito entre las amenazas.",
        "Lagos de Ubari: travesía del Idehan Ubari, un erg de unos 58.000 km², desde la carretera Sebha–Ubari hasta Gaberoun; exige deshinchado, dos vehículos y guía local. El MAEC cita Ubari entre las ciudades peligrosas.",
        "Waw an Namus: expedición de varios días sin carretera desde Sebha o desde la ruta caravanera Kufra–Sebha, con autonomía total. La propia ficha del volcán reconoce que «los problemas logísticos y la guerra civil hacen difícil el acceso a la zona».",
        "ZONAS MINADAS: el MAEC advierte de minas persistentes en Kufra y el Tibesti, herencia del conflicto con Chad, y en el entorno de Brega y Ajdabiya, y recomienda expresamente NO SALIRSE DE LAS RODADAS de los vehículos. Esto afecta de lleno al acceso sur y al tramo Sirte–Ajdabiya.",
        "Zonas vetadas de facto: el visado ordinario cubre solo Tripolitania. Libia oriental requiere un permiso especial de unos 510 € y Bengasi está especialmente restringido; el Fezán no figura como accesible para turistas en la fuente comercial más reciente que he podido abrir (julio de 2026).",
        "Frontera y pistas del sur: el MAEC desaconseja las regiones fronterizas meridionales en bloque; las pistas hacia Níger, Chad y Sudán están en manos de redes de contrabando y no son practicables.",
        "Pista de conexión interior: el eje Trípoli–Gharyan–Nalut–Gadamés es asfalto, no pista; la aventura 4x4 real en Libia está toda en el Fezán, que es justo la zona que hoy no tiene vía de acceso legal.",
    ],
    senderismo=[
        "Medina de Trípoli: recorrido urbano a pie de 2–3 horas entre el arco de Marco Aurelio, los zocos otomanos y el castillo Rojo; es el único paseo realmente cómodo del país.",
        "Leptis Magna: circuito a pie de 3–4 horas por el foro severiano, la basílica, las termas adrianas, el teatro y el circo junto al mar; sin sombra, agua encima.",
        "Cirene: la caminata más larga del país, del santuario de Apolo al templo de Zeus y bajando a la necrópolis; el yacimiento y su necrópolis de ~20 km² dan para una jornada completa.",
        "Apolonia: paseo corto por el frente marítimo, entre basílicas bizantinas y el palacio del Dux, mirando los muelles sumergidos desde la orilla.",
        "Yebel Ajdar: senderos sin señalizar por bosques de enebro y lentisco y wadis encajados; ~3.200 km² arbolados y hasta 900 m de altitud. Cuidado con las riadas repentinas, como demostró la tormenta Daniel en 2023.",
        "Qasr Nalut y el Yebel Nafusa: subida corta al granero fortificado sobre el escarpe y enlace a pie con la mezquita de Alal'a; ampliable con los pueblos de Yefren, Jadu y Kabaw.",
        "Gadamés: la ciudad vieja SOLO se recorre andando, por los pasajes cubiertos y las terrazas; es el paseo con más carácter de Libia y desde 2025 fuera de la Lista en Peligro.",
        "Tadrart Acacus: caminatas cortas desde el campamento hasta los abrigos pintados, siempre con guía; no es trekking libre sino aproximación a los paneles.",
    ],
    acampada=[
        "NO he podido verificar ningún camping formal en Libia: ni iOverlander ni Tracks4Africa han podido consultarse en esta sesión (solo tengo WebFetch y WebSearch y no los abrí), así que todo lo que sigue va con esa reserva.",
        "Gaberoun (lagos de Ubari): la fuente describe un campamento turístico básico en la orilla noreste, con patio abierto, cabañas y tienda de recuerdos, atendido en temporada de invierno; es la única instalación de acampada concreta que he podido documentar.",
        "Gaberoun, poblado abandonado: el antiguo asentamiento beduino de la orilla oeste está en ruinas desde que la tribu fue trasladada a Wadi Bashir en los años ochenta; no es alojamiento, sí referencia de orientación.",
        "Acampada libre en el Fezán: es la práctica normal en las expediciones al Acacus y a Waw an Namus, siempre dentro del campamento del operador; no hay infraestructura y la autonomía de agua y combustible debe ser total.",
        "Costa: no he encontrado ninguna fuente que documente áreas de acampada autorizadas en el litoral libio — POR CONFIRMAR.",
        "Condicionante legal: con escolta policial obligatoria y sin viaje independiente permitido, el pernocta lo fija el operador, normalmente en hotel; la acampada por libre no es una opción realista hoy.",
        "Condicionante de seguridad: el MAEC advierte de minas fuera de las rodadas en Kufra, el Tibesti y el entorno de Brega y Ajdabiya, lo que descarta acampar fuera de pista en esas zonas.",
        "Mosquitos: en los lagos de Ubari son abundantes en verano; la ventana buena para dormir allí es de octubre a mayo.",
    ],
    visado=[
        "NO EXISTE VISADO TURÍSTICO INDEPENDIENTE. El MAEC lo dice sin matices: hacen falta visado de entrada Y de salida, y solo se expiden de trabajo, misión, visita o reagrupación familiar, siempre con invitación de una entidad legal libia.",
        "VÍA REAL EN 2026: eVisa turístico en evisa.gov.ly, en marcha desde el 21-03-2024. 63 USD, una sola entrada, validez de 90 días y estancia máxima de 30 días. Lo patrocina una agencia libia autorizada, no el viajero.",
        "Plazos reales contradictorios: Against the Compass da unos 5 días hábiles y aprobación del 100 % desde 2025; OneStep4Ward habla de 2 a 4 semanas en 2026; roadto197 obtuvo la eVisa en una semana en mayo de 2024 tras tres meses fracasando con el visado ordinario. El MAEC pide solicitar con un mes de antelación.",
        "Canadá (09-09-2026) sostiene que los visados solo se conceden a residentes y que el trámite presencial tarda unos 20 días hábiles, y no menciona el eVisa: la vía presencial de embajada sigue existiendo y es más lenta.",
        "Agencias que aparecen citadas como autorizadas: Sherwes Travel, Wadi Smalos, Wadi Tidwa, Momizon y Soqor Libya (Very Hungry Nomads, 2026). Exentos de visado: tunecinos y, en aeropuertos concretos, argelinos y mauritanos.",
        "VALIDEZ EN FRONTERA TERRESTRE SIN CONFIRMAR: el FCDO avisa de que un visado emitido en el extranjero puede no ser reconocido en algunas zonas, y ningún relato de 2024-2026 describe una entrada terrestre con eVisa. Hay que exigir por escrito a la agencia que el permiso sirve en el paso concreto.",
    ],
    fronteras_rows=[
        ("Paso terrestre principal", "Ras Jedir / Ras Ajdir (Túnez–Libia, 33.1481 N 11.5663 E)", "ABIERTO. Reabrió a mediados de 2024 y es la única entrada terrestre viable; los trámites son lentos y puede cerrar sin aviso (Saiga Tours, 2026). Túnez lanzó en abril de 2026 un corredor de tránsito africano por este paso (Libya Herald, 05-04-2026). Quién manda del lado libio depende de la milicia de turno: sin confirmar."),
        ("Paso terrestre secundario", "Dehiba–Wazzin (Túnez–Libia, Dehiba 32.017 N 10.700 E)", "SIN CONFIRMAR para extranjeros. Wikipedia solo documenta su uso como vía de suministro en 2011 y no da el estado actual. Del lado libio cae en el área de influencia de Zintan y la montaña de Nafusa: por confirmar."),
        ("Paso terrestre a Egipto", "Salloum–Musaid / Amsaad (Sallum 31.55 N 25.16 E, a 8 km de la frontera)", "CERRADO A EXTRANJEROS. En mayo de 2026 el ministerio de Exteriores del gobierno paralelo del este anunció que el paso queda reservado a nacionales libios y egipcios (Saiga Tours, 2026). Against the Compass lo da por cerrado al turismo desde Gadafi."),
        ("Paso terrestre a Argelia", "Ghadames–Debdeb y Tinkarine, cerca de Ghat (24.9594 N 10.1758 E)", "CERRADO. Canadá (09-09-2026) dice literalmente que la frontera con Argelia está cerrada; Saiga Tours lo confirma y describe zona militarizada sin acceso turístico. Ghadames y Ghat, además, están en la lista de zonas a evitar del MAEC."),
        ("Paso terrestre a Níger", "Toummo (Libia–Níger)", "NO VIABLE. Zona de secuestro, bandidaje y grupos armados según Saiga Tours; Canadá sitúa ahí el riesgo de secuestro más alto. En enero y febrero de 2026 hubo muertos en choques en la frontera con Níger y Chad. No hemos podido abrir ficha de Wikipedia del paso: coordenadas por confirmar."),
        ("Aeropuerto de entrada (oeste)", "Mitiga International Airport, Trípoli (32.900 N 13.283 E, 8 km al este del centro)", "OPERATIVO y único aeropuerto internacional de Trípoli. Vuelos a Túnez, El Cairo, Estambul, Ammán, Casablanca y Yeda; ITA vuela a diario desde Roma (Against the Compass, 24-07-2026). Cierres puntuales, el último por meteorología en enero de 2026."),
        ("Aeropuerto de entrada (este)", "Benina International Airport, Bengasi (32.09722 N 20.26944 E, 19 km al este)", "OPERATIVO con vuelos a Roma, Estambul, Ammán, El Cairo, Alejandría, Túnez, Dubái y Atenas. Está en zona de Haftar y Bengasi es zona a evitar según el MAEC. La AESA mantiene Libia como zona de no sobrevuelo con excepciones."),
        ("Puerto", "Puerto de Trípoli (32.90472 N 13.19333 E)", "Carga general, granel y pasajeros según Wikipedia, pero SIN LÍNEA REGULAR DE PASAJEROS CONFIRMADA para 2026. No hay ferry utilizable desde Europa: por confirmar con la naviera, no con la ficha del puerto."),
        ("Puertos alternativos", "Misrata y Bengasi", "Puertos comerciales. No hemos encontrado ninguna fuente abierta que documente embarque de pasajeros o de vehículos particulares desde Europa en 2025-2026. Por confirmar."),
    ],
    vehiculos=[
        "NO HAY NINGÚN RELATO RECIENTE DE ENTRADA CON VEHÍCULO PROPIO EUROPEO. El último cruce overland documentado que hemos podido abrir es el de «Trumpton» en el foro Horizons Unlimited: cruzó en 2012 en los dos sentidos por Sollum «sin ningún problema burocrático», y hay viajeros neerlandeses que atravesaron el país entre 2012 y 2013.",
        "Ese mismo hilo deja claro que la ruta Túnez–Egipto la sacaron adelante un puñado de personas y casi nadie en sentido contrario, y describe Sollum como «la peor pesadilla burocrática». En mayo de 2014 los propios participantes desaconsejaban ya entrar por los combates en Trípoli y Bengasi.",
        "Conducción POR LA DERECHA. Permiso internacional de conducción recomendable; ninguna fuente oficial abierta en esta sesión lo confirma como obligatorio para Libia.",
        "CPD: el emisor nacional es el Automobile and Touring Club of Libya, +218 213403201, según carnetdepassage.org; la ficha de ese sitio NO dice si el CPD es obligatorio para entrar. En el hilo de Horizons Unlimited el carnet de passage figura entre la documentación exigida. Su web (atcl.ly) devolvió error 404.",
        "SEGURO: Libia NO forma parte del sistema de Carta Verde —en el norte de África solo Marruecos y Túnez—, así que la Carta Verde española no sirve. Egipto va por Tarjeta Naranja. Habría que comprar seguro libio en frontera y no hemos podido confirmar que exista ventanilla para extranjeros.",
        "Combustible baratísimo pero racionado de hecho: la gasolina está subvencionada desde tiempos de Gadafi y eso alimenta el contrabando. Depósitos llenos antes de entrar y salir.",
        "Movimiento restringido: Canadá avisa de que viajar fuera de Trípoli está prohibido sin autorización libia, y los relatos de 2024 y 2026 describen controles donde se revisan los permisos del grupo camino de Leptis Magna.",
        "Para dos 4x4 matriculados en España la conclusión operativa es simple: no hay vía documentada ni asegurable. Si algún día se intentara, el paquete mínimo sería eVisa patrocinada, carta de la agencia con el paso concreto, CPD, seguro local y escolta contratada.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "PROHIBIDO operar drones en espacio aéreo libio sin permiso previo de la Autoridad de Aviación Civil (Civil Aviation Authority) libia; así lo recoge drone-laws.com el 14-01-2026 citando el texto de la autoridad.",
        "No hemos localizado ningún formulario ni tasa publicada para pedir ese permiso: en la práctica, para un turista es inaccesible. Por confirmar con la propia autoridad.",
        "Canadá (09-09-2026) prohíbe fotografiar edificios militares y gubernamentales; el dron entra de lleno en esa categoría a ojos de cualquier miliciano de control.",
        "Contexto que lo explica: el dron es un arma de guerra corriente en Libia, con ataques atribuidos a células desmanteladas por las autoridades. Nadie va a interpretar tu Mini como juguete.",
        "Ni el MAEC ni el FCDO mencionan drones en sus fichas de Libia: no hay confiscaciones documentadas en fuente oficial abierta en esta sesión. Que no esté documentado no significa que no ocurra.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "NO OPERATIVO. Sin licencia y con negociaciones suspendidas desde agosto de 2026 (Space in Africa, 13-09-2026). Amazon Leo y AST SpaceMobile también han mostrado interés en el mercado libio.",
        "El punto de fricción es la pasarela local que exige la General Authority for Communications and Informatics; de las conversaciones salió una propuesta de internet gratis en escuelas y universidades remotas, nada más.",
        "Alternativa real: SIM local. Libyana domina el oeste con Trípoli, Almadar (Al-Madar Aljadid) el este con Bengasi y Tobruk, y Libya Phone (LTT) el fijo. 4G en Trípoli, Bengasi, Misrata, Sebha y la costa, con 5-15 Mbps; el Fezán y el desierto, sin señal.",
        "Comprar SIM siendo extranjero exige registro con pasaporte y visado, y la activación va de minutos a un par de horas. Against the Compass da unos 8 USD por 20 GB en el aeropuerto (julio de 2026).",
        "APAGONES: las autoridades ordenan cortes nacionales de internet en época de exámenes y en momentos políticos, y los cortes de luz tumban las torres. No cuentes con estar localizable.",
    ],
    perro_intro=[
        "ENTRADA: no hemos localizado la página oficial del servicio veterinario nacional libio. El único pliego de requisitos que hemos podido abrir es el de PetTravel: microchip ISO 11784 o anexo A del 11785, vacuna antirrábica puesta entre 30 días y 12 meses antes de la entrada y certificado veterinario internacional emitido o avalado por un veterinario oficial poco antes del viaje.",
        "Las mascotas que entran acompañando a su dueño NO necesitan permiso de importación según PetTravel; sí lo necesitan los envíos comerciales. No hay cuarentena si se cumple todo, pero el incumplimiento puede acabar en cuarentena, devolución o sacrificio a cargo del importador.",
        "RAZAS: Libia no publica lista de razas prohibidas (PetTravel). No es lo mismo que decir que no exista: es que no se publica.",
        "VUELTA A LA UE: Libia NO figura en las listas del Reglamento de Ejecución (UE) 2026/636, de 20 de marzo de 2026 —de África solo aparecen territorios insulares: Ascensión, Mauricio y Santa Elena—. Eso obliga a la vía A: titulación de anticuerpos antirrábicos en laboratorio autorizado por la UE, con la muestra tomada al menos 30 días después de la vacunación, ANOTADA EN EL PASAPORTE ANTES DE SALIR de la Unión. Sin ese análisis hecho en España, el perro no vuelve.",
        "VETERINARIOS: no hemos encontrado ninguna clínica veterinaria de referencia en Trípoli en fuente abierta. Con la red sanitaria humana degradada y el desabastecimiento de medicamentos que describe el MAEC, dar por hecho que hay atención veterinaria de urgencia para un perro europeo es imprudente.",
        "RIESGOS: TravelHealthPro considera la rabia riesgo presente en Libia, con exposición posible a murciélagos. Añade leishmaniasis transmitida por insectos, que afecta al perro tanto o más que a las personas.",
        "CONCLUSIÓN: aunque Libia fuera viable para las personas, para el perro NO LO ES. Los tours autorizados son en furgoneta con guía y policía turística; ninguna agencia de las citadas menciona animales. El perro se queda fuera.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "VACUNAS: el MAEC no exige ninguna salvo el certificado de fiebre amarilla a quien llegue de zona endémica, y recomienda el tétanos. TravelHealthPro (ficha de Libia) añade hepatitis A y tétanos para todos, y hepatitis B, sarampión, rabia, BCG y fiebre tifoidea para algunos viajeros.",
        "FIEBRE AMARILLA: no hay requisito de certificado bajo el Reglamento Sanitario Internacional según TravelHealthPro. Ojo: eso choca con lo que dice el MAEC para procedentes de zona endémica. En un viaje que venga de África subsahariana, llevar el certificado sí o sí.",
        "MALARIA: la ficha de TravelHealthPro no señala riesgo de malaria en Libia. Por confirmar con la ficha completa de malaria del propio NaTHNaC.",
        "OTROS RIESGOS: leishmaniasis, fiebre del Valle del Rift y virus del Nilo Occidental transmitidos por insectos y garrapatas; esquistosomiasis en agua dulce, así que nada de bañarse en oasis ni lagos. La rabia se considera riesgo presente.",
        "SANIDAD: el MAEC describe una red sanitaria muy degradada, con desabastecimiento frecuente de medicamentos, y da por normal la evacuación a Europa en casos graves. Canadá coincide: instalaciones muy limitadas.",
        "SEGURO: el MAEC considera imprescindible un seguro amplio con cobertura de evacuación aérea. El FCDO avisa además de que el seguro puede quedar INVALIDADO por viajar contra su recomendación: hay que leerse la letra pequeña antes, no después.",
        "AGUA Y COMIDA: el MAEC avisa de que el suministro de agua no es fiable y recomienda agua embotellada. TravelHealthPro insiste en higiene personal, de alimentos y de agua.",
    ],
    seguridad_intro="Libia es el peor escenario de toda la ruta y no hay matiz que lo salve. Cuatro administraciones coinciden: el MAEC desaconseja viajar salvo necesidad, el FCDO desaconseja todo viaje a casi todo el país, Estados Unidos mantiene el nivel 4 desde el 31 de agosto de 2026 y Canadá pide evitar todo viaje. El país está partido entre el Gobierno de Unidad Nacional y las fuerzas de Haftar, con milicias que combaten sin aviso, falsos controles, secuestros y minas. Ninguna embajada puede sacarte de allí.",
    seguridad=[
        "MAEC: «SE DESACONSEJA VIAJAR AL PAÍS SALVO CASO DE NECESIDAD». Zonas a evitar: Derna, Bengasi, Beni Walid, Sirte, Ubari, Ghadames, Ghat, Sebha y las fronteras sur con Chad, Níger, Sudán y Argelia.",
        "FCDO (21-07-2026): desaconseja todo viaje a la mayor parte de Libia y todo viaje salvo el esencial a Trípoli, Bengasi, Al-Bayda, Derna, el Jebel Akhdar, Misrata y las carreteras entre Al-Maqrun y Al-Tamimi. Sin asistencia presencial: el apoyo se da desde la embajada británica en Túnez.",
        "EEUU (31-08-2026): nivel 4. No hay embajada estadounidense operativa en Libia y no pueden prestar servicios de emergencia; el secuestro se describe como generalizado y afecta a ciudadanos estadounidenses. La aviación comercial de EEUU tiene prohibido el espacio aéreo libio.",
        "Canadá (09-09-2026): evitar todo viaje. Terrorismo contra edificios oficiales y aeropuertos, secuestro en las zonas fronterizas del sur con Níger, Chad y Sudán, minas y munición sin explotar por todo el país, controles armados y detención arbitraria.",
        "COMBATES RECIENTES: en mayo de 2025 la muerte del comandante Ghneiwa al-Kikli desencadenó combates intensos entre grupos armados en Trípoli, con víctimas civiles y daños en infraestructuras (HRW, informe mundial 2026).",
        "En 2026: tres militares del Ejército Nacional Libio muertos en un ataque en la frontera con Níger el 31 de enero; decenas de muertos en choques fronterizos con Níger y Chad el 24 de febrero; coche bomba en Bengasi el 10 de agosto que mató a un comandante de inteligencia; protestas en Trípoli el 27 de julio por los cortes de luz.",
        "MINAS: HRW documenta en septiembre de 2025 tres menores heridos por artefactos sin detonar en Khallet al-Ferjan, a las afueras de Trípoli. Salir del asfalto en Libia es jugar con explosivos, no con arena.",
        "FALSOS CONTROLES Y ROBO A MANO ARMADA: el MAEC los cita expresamente, junto con secuestros de civiles, y desaconseja con firmeza circular de noche.",
        "LEY LOCAL: Canadá recuerda que el proselitismo religioso y la blasfemia son delito, que las relaciones LGTBI y las extramatrimoniales están criminalizadas y que fotografiar instalaciones militares o gubernamentales está prohibido.",
        "Y una obviedad operativa: si el seguro de viaje se invalida por ir contra la recomendación oficial, una evacuación médica desde Trípoli se paga íntegra del bolsillo.",
    ],
    agua=[
        "El MAEC avisa de que el suministro de agua NO es fiable en Libia y recomienda beber solo agua embotellada. Para el depósito de ducha y lavado, eso significa filtrar y clorar siempre.",
        "El país vive del Gran Río Artificial, el acuífero fósil bombeado desde el sur; el proyecto arrastra daños de guerra y falta de mantenimiento, y el suministro urbano es intermitente. Cantidad y calidad dependen del barrio y del día.",
        "Los cortes de luz agravan el problema: desde junio de 2026 hay apagones severos que dejan sin bombeo depósitos y estaciones (Libya Herald / Arab News, septiembre de 2026).",
        "En el desierto no hay red: fuera de Trípoli, Misrata, Bengasi y la franja costera, el agua sale de pozos y de lo que te dé la agencia. Autonomía completa o nada.",
        "TravelHealthPro añade riesgo de esquistosomiasis en agua dulce: nada de bañarse ni de llenar depósitos en lagos y oasis como los de Ubari.",
        "PENDIENTE: no hemos localizado ningún punto de agua potable concreto y verificable en Libia en fuente abierta. Lo que se ponga en el mapa hasta entonces es orientativo.",
    ],
    combustible=[
        "LA GASOLINA MÁS BARATA DEL MUNDO: 0,024 USD por litro de 95 octanos según GlobalPetrolPrices el 09-02-2026. Un viajero lo resumió así en mayo de 2024: «20 litros costaban unos 0,50 €» (roadto197).",
        "Ese precio es subvención heredada de la época de Gadafi y es exactamente lo que alimenta el contrabando: mientras no se retire la subvención, el contrabando no parará (Libya Herald, septiembre de 2026).",
        "CRISIS DE SUMINISTRO EN 2026: el Ministerio del Interior cerró 490 gasolineras implicadas en contrabando y autorizó unas 365 según demanda (Libya Herald, septiembre de 2026). El mes anterior hubo colas largas de gasolina y gasóleo.",
        "La demanda se disparó de los 6,5 millones de litros diarios habituales a 9,5 millones (presidente de la NOC, Libya Herald, junio de 2026), en parte por los generadores diésel que compensan los apagones.",
        "Gasóleo en mercado negro con precios al alza desde junio de 2026 por la crisis eléctrica. Barato sobre el papel no significa disponible en la práctica.",
        "CALIDAD Y RED: sin dato verificado sobre la calidad del gasóleo libio ni sobre la disponibilidad real fuera de la costa. Para un Grenadier y una Delica, eso solo se resuelve con prefiltro de agua y depósitos llenos antes de entrar.",
    ],
    experiencias_intro="No hay relatos de overlanders con vehículo propio en Libia desde 2012-2013: el conflicto los cortó de raíz. Lo que sí hay, y crece desde 2024, son relatos de tours cerrados con agencia autorizada, guía y policía turística. Los recogemos con su fecha para que se vea qué es posible hoy y qué dejó de serlo.",
    experiencias=[
        "El último cruce overland documentado es de 2012: en el foro Horizons Unlimited, el usuario «Trumpton» cuenta que en 2012 cruzó Libia en los dos sentidos por el paso de Sollum «sin ningún problema burocrático», y otro participante enlaza blogs de viajeros neerlandeses que atravesaron el país entre 2012 y 2013 con vehículo. Es la referencia más reciente que hemos podido abrir de alguien pasando Libia con coche propio.",
        "El mismo hilo explica por qué se acabó: «Andrasz» advierte de que solo un puñado de personas logró la ruta Túnez–Egipto y casi nadie en sentido contrario, describe Sollum como «la peor pesadilla burocrática», y en mayo de 2014 ya recomendaba evitar Libia indefinidamente por los combates en Trípoli y Bengasi. «Dubai355» citaba en abril de 2014 a un contacto libio: controles de los propios pueblos y seguridad «cero por ciento».",
        "Vuelve el turismo con correa corta: roadto197 viajó en mayo de 2024, voló con Libyan Wings desde Túnez a Mitiga tras tres meses fracasando con el visado ordinario y conseguir la eVisa en una semana. Contrató con la agencia Sherwes y le asignaron un guía, un agente de policía turística y un funcionario del Ministerio de Turismo. Vio Trípoli, Sabratha y Leptis Magna, pasó varios controles y pagó 1.100 € por tres días. Nunca se sintió inseguro.",
        "El recordatorio de que Libia sigue en guerra: Johnny Ward (OneStep4Ward) viajó en 2026 con guardia armado todo el tiempo y el último día presenció un tiroteo en Trípoli entre fuerzas del gobierno y rebeldes por el traslado de un preso, con su grupo dentro del autobús. Ruta Trípoli, Jebel Nafusa, Ghadames, Kabaw, Gharyan, Leptis Magna y Sabratha; 2.200 USD por seis días más unos 100 USD de gastos.",
        "Cómo se entra en 2026, según Against the Compass (actualizado el 24-07-2026): eVisa en evisa.gov.ly por 63 USD en unos cinco días hábiles y con aprobación del 100 % desde 2025, entrada terrestre posible desde Túnez aunque los trámites «llevan muchísimo tiempo», frontera egipcia cerrada desde tiempos de Gadafi, ITA volando a diario de Roma a Mitiga, SIM por 8 USD con 20 GB y una frase que lo resume todo: «el viaje independiente en Libia no es posible hoy».",
        "El sur sí se visita, pero con escolta y precio de expedición: Kumakonda ofrece un viaje del 14 al 24 de noviembre de 2026 por el Acacus, los lagos de Ubari, el Wadi Matkhendoush y Leptis Magna por 2.850 € por persona en grupos de 7 a 11, con escoltas policiales y asistencia de visado incluidas, y evitando los vuelos domésticos libios por poco fiables: se va por carretera desde Trípoli hasta el corazón del Sáhara.",
        "Quién te puede llevar: Very Hungry Nomads (guía de 2026) enumera cinco agencias certificadas —Sherwes Travel, Wadi Smalos, Wadi Tidwa, Momizon y Soqor Libya—, tours de tres a cinco días por Trípoli, Leptis Magna, Sabratha, la montaña de Nafusa y Ghadames, entrada volando desde Túnez con Tunisair o Libyan Wings, y la advertencia de que con avisos de «no viaje» el seguro puede no valer y las embajadas no pueden ayudarte.",
        "El dato que mide la reapertura: el Ministerio de Turismo libio cifró en 282.000 los visitantes del primer semestre de 2025, un 60 % más que el periodo anterior, atribuido al eVisa de 2024, a nuevas conexiones aéreas y a una mejora de la seguridad interna (The Libya Observer, 17-01-2026). Son cifras oficiales de un ministerio, no auditadas, y mezclan turismo con otros flujos.",
        "El contraste incómodo: Wikipedia recoge que en 2007 Libia recibió 180.000 turistas más un millón de excursionistas de un día, que ahora ronda los 100.000 anuales y que el país «no está emitiendo visados de turismo». La foto que sale de juntar esa entrada con las cifras del ministerio es la de un turismo minúsculo, controlado y mal documentado.",
        "Y lo que ningún relato cuenta: en ninguno de los textos que hemos podido abrir —2024, 2025 ni 2026— aparece nadie entrando en Libia con vehículo propio matriculado en Europa, ni con perro. Ese silencio, en un país con esta densidad de blogueros de «los 197 países», es en sí mismo el dato.",
    ],
    pendientes=[
        ("Validez del eVisa en frontera terrestre", "Carta firmada por una agencia libia autorizada que diga expresamente que el permiso sirve para entrar por Ras Jedir con vehículo extranjero, o confirmación del consulado libio en Madrid."),
        ("Plazo del registro policial al llegar", "Resolver la contradicción entre los 7 días del FCDO y los 3 días del Departamento de Estado con una fuente libia oficial o con la agencia que patrocine el visado."),
        ("¿Es obligatorio el CPD en Libia?", "Respuesta por escrito del Automobile and Touring Club of Libya (+218 213403201) o del RACE sobre si la aduana libia exige carnet de passages a un vehículo español."),
        ("Seguro de vehículo válido en Libia", "Confirmación de OFESAUTO o de una aseguradora de que existe póliza contratable en frontera para extranjeros y con qué cobertura, dado que Libia no está en el sistema de Carta Verde."),
        ("Estado real del paso de Dehiba–Wazzin", "Fuente de 2026 (aduana tunecina, agencia o prensa libia) que diga si admite extranjeros y quién lo controla del lado libio."),
        ("Coordenadas y estado del paso de Toummo", "Ficha de Wikipedia o fuente geográfica que dé lat/lon del paso Libia–Níger; la búsqueda de «Tummo» devuelve la práctica budista tibetana."),
        ("Servicio veterinario oficial de Libia", "Localizar la web del organismo veterinario nacional (Ministerio de Agricultura o Centro Nacional de Salud Animal) con su procedimiento de importación de animales de compañía."),
        ("Días de validez del certificado veterinario", "Número exacto de días que acepta la aduana libia entre la emisión del certificado y la entrada, en fuente libia."),
        ("Ferry o línea de pasajeros a Trípoli, Misrata o Bengasi", "Confirmación de una naviera con horarios publicados para 2027, o cierre definitivo de la vía marítima como opción."),
        ("Salida de los tres sitios libios de la Lista en Peligro", "UNESCO anunció en julio de 2025 la retirada de tres sitios africanos de la Lista en Peligro; falta confirmar en la ficha de cada sitio libio si alguno es de Libia o si siguen los cinco."),
        ("Riesgo de malaria en Libia", "Ficha completa de malaria de NaTHNaC o del Ministerio de Sanidad español que confirme que no hay riesgo, ya que la página de país no lo menciona."),
        ("Punto de agua potable verificable", "Al menos una fuente o estación de servicio en la costa libia con coordenadas y testimonio reciente; hoy no tenemos ninguna."),
    ],
    sources=SOURCES,
    sources_note="Ficha revisada el 18 de septiembre de 2026 con las páginas efectivamente abiertas en esa sesión de documentación; cada dato procede de una de las fuentes listadas y lo que no se pudo confirmar aparece como «por confirmar» en «pendientes». Es una herramienta de planificación, NO una autorización de viaje ni un permiso: la recomendación oficial del MAEC es no viajar a Libia salvo caso de necesidad. En un país con dos gobiernos y milicias, cualquier dato de frontera, visado o seguridad puede quedar obsoleto en cuestión de días: reverificar siempre antes de moverse.",
    emergency="EMERGENCIA CONSULAR ESPAÑOLA 24 H: +218 91 320 39 04 y +216 29 174 445 (MAEC). Embajada de España en Trípoli: +218 21 362 00 51 / 52; los asuntos consulares se atienden desde Túnez en +216 71 750 802 y +216 71 801 729. POLICÍA DEL ESTADO: 193. Trípoli: 333 54 05. Bengasi: 061 25 900. Prefijo: +218. No hay número nacional de ambulancia ni bomberos verificado: Canadá pide localizar policía y hospital de la zona antes de moverse.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

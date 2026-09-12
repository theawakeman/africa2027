# -*- coding: utf-8 -*-
"""Costa de Marfil — ficha completa, corredor doble bajada/subida (12 sep 2026)."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== BAJADA: Gbapleu/N'Zoo (Guinea) -> Danané -> Man -> Daloa -> Yamoussoukro -> Taï -> costa oeste -> Abiyán -> Noé/Elubo (Ghana) =====
    dict(n=1, name="Monte Nimba (Reserva Natural Integral, UNESCO)", cat="Patrimonio UNESCO", prio="Alta", dog="no confirmado — tratar como prohibido", time="1–2 días",
         lat=7.5406, lon=-8.4581,
         desc="La cadena del Nimba se levanta sobre la triple frontera de Costa de Marfil, Guinea y Liberia y culmina en el monte Richard-Molard (1.752 m), techo de los dos primeros países. Es Patrimonio Mundial de la UNESCO desde 1981-1982 (bien transfronterizo Guinea/Costa de Marfil) y Reserva de la Biosfera: praderas de altura sobre selva densa, con endemismos célebres como el sapo vivíparo del Nimba (Nimbaphrynoides occidentalis, que pare crías vivas — único entre los anfibios) y micromamíferos exclusivos de la sierra. La parte marfileña (~5.000 ha) es RESERVA INTEGRAL: el acceso está restringido y no es un parque de visita libre. Hay que gestionar el permiso con la OIPR (Office Ivoirien des Parcs et Réserves) y guía local desde Danané o Biankouma. Está también en la Lista del Patrimonio Mundial en Peligro por la presión minera del lado guineano. Coordenada del punto culminante; el acceso marfileño se hace desde el noroeste de Danané. CONFIRMAR acceso y permiso antes de desviarse.",
         credit="Wikimedia Commons", source=W + "Mont%20Nimba%20landscape.jpg?width=900"),
    dict(n=2, name="Man · la ciudad de las dieciocho montañas", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=7.4125, lon=-7.5539,
         desc="Capital de la región de Tonkpi y del oeste forestal marfileño, encajada en un anfiteatro de cumbres que le ha dado el apodo de «la ciudad de las 18 montañas». Clima notablemente más fresco que la costa (está a ~340 m, rodeada de cerros de 900-1.200 m), combustible, bancos, hospital regional, mercado grande y la mejor oferta de alojamiento del oeste. Es la base natural de todo el bloque de montaña: Dent de Man, mont Tonkoui, la Cascade, los puentes de lianas y los pueblos dan y toura. Punto de partida y de regreso de casi todas las excursiones a pie del país.",
         credit="Zenman/Letsgoforward · CC BY-SA 3.0", source=W + "Dent%20de%20Man%20montagne.jpg?width=900"),
    dict(n=4, name="Dent de Man (881 m)", cat="Naturaleza · montaña", prio="Alta", dog="permitido con correa", time="½–1 día",
         lat=7.4553, lon=-7.5192,
         desc="El diente de roca que domina Man y símbolo de toda la región: una cumbre puntiaguda de unos 881 m que se sube a pie en una jornada corta (unas 2-3 h de subida) por sendero de selva y bloques, con vistas de 360º sobre el mar de montañas del Tonkpi. Es LA excursión clásica del oeste marfileño. No hay señalización fiable ni control de acceso formal: se sube desde el pueblo de Zadepleu / el barrio de Libreville con guía local, que además evita problemas con los bosques sagrados de los alrededores. Tramo final expuesto y resbaladizo en lluvias.",
         credit="Zenman/Letsgoforward · CC BY-SA 3.0", source=W + "Dent%20de%20Man%20montagne.jpg?width=900"),
    dict(n=5, name="Mont Tonkoui (1.189 m)", cat="Naturaleza · montaña", prio="Alta", dog="permitido con correa", time="½ día",
         lat=7.4550, lon=-7.6250,
         desc="La segunda cumbre más alta de Costa de Marfil, a unos 20 km al noroeste de Man. Tiene la particularidad de que una pista de tierra sube casi hasta la cima (antigua estación climática y repetidores), lo que la convierte en el mejor mirador del país accesible en 4x4: en los días claros se ven las montañas de Guinea y de Liberia y el mar de selva hasta el horizonte. Amanecer frecuentemente por encima de un mar de nubes. La pista es de tierra roja, con cárcavas y tramos lavados en temporada de lluvias — es una de las subidas 4x4 más divertidas del corredor de bajada. También se puede subir a pie desde la carretera de Biankouma. Coordenada aproximada de la cima.",
         credit="Wikimedia Commons", source=W + "Dent%20de%20Man%20montagne.jpg?width=900"),
    dict(n=6, name="La Cascade de Man", cat="Naturaleza", prio="Media", dog="permitido con correa", time="½ día",
         lat=7.3833, lon=-7.5667,
         desc="A unos 5 km del centro de Man, un salto de agua encajado en un bosque de bambúes gigantes que forma un túnel vegetal sobre el sendero de acceso — la imagen más reproducida de la región después de la Dent de Man. Paseo corto y fácil desde el aparcamiento, con tasa de entrada local y guías del pueblo. El caudal depende mucho de la estación: espectacular entre junio y octubre, reducido a un hilo en pleno enero-febrero. Pozas donde se puede uno mojar los pies; bañarse depende del caudal y del criterio del guía.",
         credit="Wikimedia Commons", source=W + "Les%20cascades%20de%20Man.jpg?width=900"),
    dict(n=7, name="Puente de lianas de Lieupleu (y los puentes dan)", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=7.2667, lon=-7.7167,
         desc="Los puentes de lianas del país dan son pasarelas colgantes tejidas enteramente con lianas vivas sobre los ríos de la selva, sin un solo clavo, mantenidas y renovadas por especialistas rituales de cada aldea; la tradición dice que se «hacen crecer» de noche y su construcción está rodeada de secreto iniciático. Los más visitados están en los pueblos de Lieupleu, Vatouo, Gbangbégouiné y Niahoin, a 20-40 km de Man por pistas de tierra. Es patrimonio vivo, no un decorado: se paga una tasa a la aldea, se pide permiso al jefe y conviene ir con guía de Man. Cruzarlo es parte de la visita. Coordenada aproximada de Lieupleu: confirmar en Man cuál de los puentes está en mejor estado en el momento del paso.",
         credit="Wikimedia Commons", source=W + "Pont%20de%20lianes%20de%20Lieupleu.jpg?width=900"),
    dict(n=8, name="Cascadas de Gbêtitapéa (Daloa)", cat="Naturaleza", prio="Media", dog="permitido con correa", time="½ día",
         lat=6.9167, lon=-6.4333,
         desc="A pocos kilómetros del centro de Daloa, en el barrio-aldea de Gbêtitapéa, el río se despeña en una serie de saltos y marmitas de granito rodeados de vegetación: el sitio natural más conocido del centro-oeste y parada lógica a mitad de camino entre Man y Yamoussoukro. Acceso sencillo en vehículo hasta muy cerca y paseo corto entre las rocas. Daloa es además la tercera ciudad del país y capital del cacao: combustible, talleres, bancos y hospital regional. Coordenada aproximada del sitio; confirmar el acceso exacto en Daloa.",
         credit="Wikimedia Commons", source=W + "La%20Cascade%20de%20Man%201990.jpg?width=900"),
    dict(n=9, name="Yamoussoukro · Basílica de Nuestra Señora de la Paz", cat="Patrimonio", prio="Alta", dog="permitido con condiciones", time="1 día",
         lat=6.8094, lon=-5.2966,
         desc="La iglesia más grande del mundo, plantada en medio de la sabana de la aldea natal de Félix Houphouët-Boigny, que hizo de ella la capital política del país. Inaugurada en 1990 y consagrada por Juan Pablo II, es una réplica ampliada de San Pedro del Vaticano: unos 30.000 m² de superficie total y una cúpula que, con su cruz, supera los 158 m — más alta que la de San Pedro, aunque la nave sea menor. Cabe de pie una multitud inmensa bajo 7.000 m² de vidrieras francesas; el conjunto costó una fortuna en un país de renta media y sigue siendo objeto de polémica. Visita guiada (subida a la cúpula incluida en algunas modalidades), vestimenta correcta obligatoria. En la misma ciudad: el palacio presidencial con su lago de cocodrilos, la Fondation Houphouët-Boigny y avenidas de seis carriles vacías que son una experiencia en sí misma. El perro no entra en la basílica: se queda con un miembro del grupo en los jardines o en el vehículo a la sombra.",
         credit="Didierwiki · CC0", source=W + "Basilique%20notre%20Dame%20de%20la%20Paix%20de%20Yamoussoukro%20(2).jpg?width=900"),
    dict(n=10, name="Parque Nacional de Taï (UNESCO) · chimpancés con herramientas", cat="Patrimonio UNESCO", prio="Alta", dog="no confirmado — tratar como prohibido", time="2–3 días",
         lat=5.7500, lon=-7.3500,
         desc="Unos 5.400 km² del último gran bloque de selva primaria de África occidental, Patrimonio Mundial de la UNESCO desde 1982 y Reserva de la Biosfera. Aquí vive la población de chimpancés occidentales mejor estudiada del mundo: los chimpancés de Taï usan más de 25 herramientas distintas y, sobre todo, rompen nueces con yunques y martillos de piedra y madera — una cultura material transmitida entre generaciones, documentada desde los años 70 por el Taï Chimpanzee Project. Además: hipopótamo pigmeo, cefalofo de Jentink, colobo rojo, mono de Diana, elefante de bosque y más de 230 especies de aves. Se visita a pie con guía obligatorio del ecoturismo de Taï/OIPR; los dos accesos son la ciudad de Taï (oeste, cerca del río Cavally y la frontera de Liberia) y sobre todo Djouroutou (sur), donde está el grupo de chimpancés habituado a la presencia humana y desde donde sale también la subida al mont Niénokoué (396 m), un inselberg con vista sobre el dosel. Reserva previa imprescindible, número de visitantes limitado y protocolo sanitario estricto (distancia y mascarilla, por el riesgo de contagiar enfermedades respiratorias a los chimpancés).",
         credit="Wikimedia Commons", source=W + "Ta%C3%AF%20National%20Park%20(24148248710).jpg?width=900"),
    dict(n=11, name="Mont Niénokoué (396 m) · mirador sobre la selva de Taï", cat="Naturaleza · montaña", prio="Media", dog="no confirmado — tratar como prohibido", time="½–1 día",
         lat=5.4333, lon=-7.1833,
         desc="Inselberg de granito que emerge del mar de selva en el sur del Parque Nacional de Taï, accesible desde el campamento ecoturístico de Djouroutou. La subida a pie con guía atraviesa selva cerrada y termina en una plataforma rocosa desde la que se domina el dosel de la selva primaria hasta el horizonte, sin una sola construcción a la vista: probablemente el mirador más impresionante del corredor de bajada. Media jornada larga, calor y humedad extremos, sanguijuelas en temporada húmeda. Coordenada aproximada.",
         credit="Wikimedia Commons", source=W + "For%C3%AAt%20du%20banco%20(%20C%C3%B4te%20d'Ivoire%20).jpg?width=900"),
    dict(n=12, name="Sassandra y la costa oeste", cat="Costa", prio="Alta", dog="permitido", time="2 noches",
         lat=4.9500, lon=-6.0833,
         desc="Antiguo puesto comercial francés en la desembocadura del río Sassandra, con casas coloniales desconchadas sobre el acantilado, un puerto pesquero muy vivo y, justo al este, la mejor tanda de playas del país fuera del circuito de Abiyán: Poly Plage, Batelebré, Drewin y Niega, largos arenales de cocoteros con campamentos sencillos y pocas construcciones. Más al oeste, entre San-Pédro y la frontera de Liberia, está Grand-Bérébi, la playa que un overlander que ha recorrido África entera (The Road Chose Me) describe sin matices como «las mejores playas que he visto en mi vida, mejores que Australia, mejores que Costa Rica»; allí y en Sassandra hay campamentos (Chez JoJo, Chez Jules) que dejan aparcar y dormir directamente sobre la arena. Se puede subir en piragua por el río y por la laguna. Es la parada de descanso natural tras el bloque de selva de Taï y uno de los sitios más cómodos del viaje para el perro. Atención a las corrientes de resaca en toda esta costa: bañarse solo donde lo hagan los locales.",
         credit="Wikimedia Commons", source=W + "Fleuve%20Sassandra%20%C3%A0%20Soubr%C3%A9.JPG?width=900"),
    dict(n=13, name="Grand-Lahou y el Parque Nacional de Azagny", cat="Naturaleza", prio="Media", dog="no confirmado — tratar como prohibido (parque)", time="1 día",
         lat=5.1333, lon=-5.0167,
         desc="Grand-Lahou es la aldea del cordón litoral donde el río Bandama se encuentra con el Atlántico, con las ruinas del viejo Grand-Lahou colonial siendo literalmente devoradas por el mar (uno de los casos de erosión costera más citados de África occidental). Enfrente, al otro lado de la laguna, el Parque Nacional de Azagny protege ~190 km² de manglar, pantanos y sabana costera con elefante de bosque, búfalo enano, manatí africano y una gran población de aves acuáticas; se recorre en piragua con guías de la OIPR desde Grand-Lahou o Irobo. Es la última parada tranquila antes de meterse en Abiyán. Como parque nacional, tratar la entrada del perro como prohibida: el pueblo y las playas de Grand-Lahou sí son compatibles.",
         credit="Wikimedia Commons", source=W + "For%C3%AAt%20du%20banco%20(%20C%C3%B4te%20d'Ivoire%20).jpg?width=900"),
    dict(n=14, name="Abiyán · Le Plateau y la laguna Ébrié", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="2–3 noches",
         lat=5.3250, lon=-4.0200,
         desc="Capital económica y mayor base logística de todo el golfo de Guinea occidental: puerto, aeropuerto internacional, Embajada de España, talleres y recambios 4x4 de referencia regional, veterinarios de nivel europeo y residencias caninas (el mejor punto de respiro del perro en África occidental según el dosier canino del proyecto). Le Plateau es el distrito de negocios de los rascacielos que le valieron el apodo de «la Manhattan de la laguna»: la catedral de San Pablo —una vela de hormigón sostenida por la silueta de un personaje gigante—, la Tour F, la pirámide de Rinaldo Olivieri y el puente Charles-de-Gaulle. Enfrente, al otro lado de la laguna Ébrié, Treichville y su gran mercado, Cocody con las embajadas, y el barrio-pueblo de Blockhauss donde se cruza en barco-taxi (los «bateaux-bus» amarillos, la mejor forma de ver la ciudad). Dentro del propio término municipal está el Parque Nacional del Banco, 30 km² de selva primaria rodeada de ciudad. Tráfico denso y caótico: aparcamiento vigilado imprescindible.",
         credit="Wikimedia Commons", source=W + "Plateau%20abidjan.jpg?width=900"),
    dict(n=15, name="Grand-Bassam (UNESCO)", cat="Patrimonio UNESCO", prio="Alta", dog="permitido", time="1–2 días",
         lat=5.1961, lon=-3.7389,
         desc="Primera capital de la Costa de Marfil colonial (1893-1896) y Patrimonio Mundial de la UNESCO desde 2012 como «ciudad histórica colonial». El Quartier France, encajado entre el mar y la laguna, conserva una trama urbana completa de finales del XIX y principios del XX —palacio del gobernador, aduana, oficina de correos, casas de comercio, tribunal— en una decadencia elegante de muros desconchados y buganvillas, con el Museo Nacional del Traje instalado en el antiguo palacio. Al lado, el barrio N'zima de los pescadores, la playa y una fila de maquis y talleres de artesanía. A solo 40 km de Abiyán: es la escapada de fin de semana de la capital, y de las mejores paradas del viaje con el perro, que aquí no plantea ningún problema. Ojo con la resaca del mar, muy fuerte.",
         credit="Adoscam · CC BY-SA 4.0", source=W + "WikiConvFr23%20Visite%20B%C3%A2timents%20sites%20historiques%20de%20Grand-Bassam%20(boblioth%C3%A8que%20municicpale%20de%20Grand-Bassam%20)%2002.jpg?width=900"),
    dict(n=16, name="Assinie-Mafia y el cordón litoral", cat="Costa", prio="Alta", dog="permitido", time="2 noches",
         lat=5.1333, lon=-3.4667,
         desc="La última playa antes de Ghana y la más conocida del país: una lengua de arena entre el Atlántico y la laguna Aby, con cocoteros, campamentos, piraguas y el estuario de la Bassin d'Assinie. Más allá, hacia el este, está Assouindé y el cordón que llega hasta la frontera. Es el sitio donde se rodó «Les Bronzés» y donde Abiyán se va el fin de semana, así que en sábado se llena: entre semana está prácticamente vacío. Kitesurf y paddle en la laguna, pesca en el mar, playa larguísima para el perro. Buena pernocta final del corredor de bajada, a 60 km del paso de Noé.",
         credit="Wikimedia Commons", source=W + "Grand-Bassam-Plage.jpg?width=900"),
    # ===== SUBIDA: Soko/Sampa (Ghana) -> Bondoukou -> Comoé (condicional) -> Bouaké -> Katiola -> Korhogo -> Séguéla -> Biankouma -> Sipilou (Guinea) =====
    dict(n=17, name="Bondoukou y las mezquitas de estilo sudanés", cat="Cultura", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=8.0402, lon=-2.8000,
         desc="Capital del Zanzan y una de las ciudades más antiguas del país: fue etapa mayor de las rutas caravaneras dyula entre el Sahel y el bosque, y conserva una notable concentración de mezquitas de adobe de estilo sudanés (Samatiguila, Kong y Bondoukou forman el conjunto candidato a la Lista del Patrimonio Mundial de la UNESCO por sus mezquitas de estilo sudanés del norte marfileño). Barrios koulango, dyula y abron, mercado importante y el palacio del rey del Gyaman. Primera plaza de servicios de la subida tras entrar desde Ghana por Soko/Sampa: combustible, banco, hospital.",
         credit="Wikimedia Commons", source=W + "Mosque%20in%20Korhogo%20ap%20001.jpg?width=900"),
    dict(n=18, name="Parque Nacional de la Comoé (UNESCO) · CONDICIONAL por seguridad", cat="Patrimonio UNESCO", prio="Media", dog="no confirmado — tratar como prohibido", time="2–3 días",
         lat=8.7500, lon=-3.7000,
         desc="Con unos 11.500 km² es el mayor parque nacional de África occidental y uno de los mayores del continente, Patrimonio Mundial de la UNESCO desde 1983 y Reserva de la Biosfera: un gradiente completo desde la sabana sudanesa del norte hasta el bosque denso húmedo del sur, atravesado por el río Comoé. Elefante, búfalo, hipopótamo, cobo de Buffon, hipotrago, babuino, chimpancé (población de sabana, rara) y más de 500 especies de aves. Salió de la Lista del Patrimonio en Peligro en 2017 tras una recuperación notable. PERO: los avisos de viaje occidentales vigentes en 2026 desaconsejan todo viaje al Parque Nacional de la Comoé y al norte de los distritos de Zanzan y Savanes por el riesgo de atentado y secuestro procedente del Sahel; el norte del parque toca la frontera de Burkina Faso, donde se produjeron los ataques de Kafolo (2020 y 2021). Si se entra, solo por la puerta SUR de Kakpin y con acompañamiento de la OIPR, y NUNCA por Kafolo ni por el flanco norte. Es un PDI condicional: la decisión se toma con el aviso de Exteriores en la mano 72 h antes. Coordenada del centro del parque.",
         credit="Wikimedia Commons", source=W + "Fleuve%20Como%C3%A9%20du%20Parc%20National%20de%20la%20Como%C3%A9%20(Nord-Est%20de%20la%20C%C3%B4te%20d'Ivoire).jpg?width=900"),
    dict(n=19, name="Bouaké", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=7.6906, lon=-5.0300,
         desc="Segunda ciudad del país y capital del centro, en pleno país baulé. Fue la capital de facto de la zona rebelde durante la partición del país entre 2002 y 2011, y hoy es un gran nudo de carreteras y ferrocarril (línea Abiyán–Uagadugú) plenamente reintegrado. Gran mercado textil, catedral de Sainte-Thérèse, estadio de la Paz y la mejor oferta de servicios entre Abiyán y el norte: combustible, talleres, recambios, hospital universitario, bancos y supermercados. Nudo logístico central de la subida.",
         credit="Wikimedia Commons", source=W + "Stade%20de%20la%20Paix%20de%20Bouak%C3%A9.jpg?width=900"),
    dict(n=20, name="Katiola · la alfarería mangoro", cat="Cultura", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=8.1333, lon=-5.1000,
         desc="A 50 km al norte de Bouaké, Katiola es la capital de la cerámica marfileña: las mujeres mangoro (subgrupo de los tagbana) modelan a mano, sin torno, grandes canaris de agua, braseros y jarras que se venden en todo el país, y la cooperativa de alfareras recibe visitas y hace demostraciones del proceso completo, desde la extracción de la arcilla hasta la cocción a cielo abierto. Parada corta y muy rentable en el eje Bouaké–Korhogo, justo en la transición del bosque a la sabana. Confirmar horario de la cooperativa al llegar.",
         credit="Wikimedia Commons", source=W + "Tenue%20traditionnelle%20des%20S%C3%A9noufo.jpg?width=900"),
    dict(n=21, name="Korhogo y el país senufo", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="2 noches",
         lat=9.4578, lon=-5.6294,
         desc="Capital del norte y del pueblo senufo, la gran parada cultural de la subida. Aquí están: los TEJIDOS DE KORHOGO, telas de algodón cubiertas de animales estilizados, máscaras y figuras rituales, que se hacen sobre todo en la aldea de tejedores de WARANIÉNÉ, a 5 km al suroeste (allí los hombres tejen bandas estrechas de algodón en telares de pedales bajo los árboles, las bandas se cosen entre sí formando el paño y después los pintores dibujan a mano, con un pincel de cuchillo y un barro fermentado que fija el pigmento, los motivos del imaginario senufo; se ve el proceso completo y se compra en el taller, mucho mejor y más barato que en Abiyán); el mercado y el barrio de los artesanos (escultores de máscaras, forjadores, tejedores de cestas); los BOSQUES SAGRADOS (sinzanga) del poro, la sociedad iniciática senufo, que se visitan solo con autorización y guía —hay uno accesible en Korhogo, con las esculturas y los tambores del poro—, y las danzas de máscaras (boloye, la danza de la pantera de los niños iniciados). A 10 km, el mont Korhogo ofrece una subida corta con vista sobre la sabana. AVISO: Korhogo está en el distrito de Savanes y a unos 100-120 km de la frontera de Mali; los avisos occidentales desaconsejan todo viaje al norte de Savanes y a menos de 40 km de las fronteras de Mali y Burkina. La ciudad en sí no está expresamente excluida en la redacción actual, pero es el PDI de la ficha que más hay que revalidar antes de ir.",
         credit="Wikimedia Commons", source=W + "Mosque%20in%20Korhogo%20ap%20001.jpg?width=900"),
    dict(n=22, name="Séguéla", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=7.9611, lon=-6.6731,
         desc="Capital del Worodougou, en el centro-oeste, y tradicionalmente la ciudad de los diamantes aluviales marfileños (los yacimientos de Séguéla y Tortiya estuvieron bajo embargo internacional del Proceso de Kimberley entre 2005 y 2014 por su papel en la financiación del conflicto). Es la última plaza de servicios de tamaño medio —combustible formal, taller, hospital, banco, mercado— antes del tramo final de la subida hacia Touba, Biankouma y la frontera de Guinea por Sipilou. Punto de no retorno logístico del corredor de subida.",
         credit="Wikimedia Commons", source=W + "Stade%20de%20la%20Paix%20de%20Bouak%C3%A9.jpg?width=900"),
    dict(n=24, name="Biankouma y la pista de Sipilou", cat="Naturaleza · montaña", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=7.7333, lon=-7.6167,
         desc="Biankouma es la otra capital de montaña del oeste, al norte de Man, en pleno macizo del Tonkpi y rodeada de aldeas toura y dan con arquitectura tradicional de adobe y techo cónico de paja (los pueblos de Gouessesso y Sémien son los más citados). Desde aquí sale la carretera del norte hacia Sipilou y la frontera guineana, y también un acceso alternativo al mont Tonkoui por su vertiente septentrional. Es la última pernocta marfileña de la subida antes de entrar de nuevo en Guinea por un paso distinto al de la bajada. Combustible limitado: repostar a fondo en Séguéla o en Man.",
         credit="Wikimedia Commons", source=W + "Mont%20Nimba%20landscape.jpg?width=900"),
]

_CAT_COLOR = {
    "ciudad · servicios": "azul",
    "naturaleza": "verde",
    "naturaleza · montaña": "verde",
    "cultura": "morado",
    "costa": "turquesa",
    "patrimonio": "marron",
    "patrimonio unesco": "marron",
}
for _i, _p in enumerate(POIS, 1):
    _p["n"] = _i
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada bajada — Gbapleu / N'Zoo (desde Guinea)", "Frontera", 7.1000, -8.4000,
     "Paso principal del oeste, en el eje Nzérékoré–Lola–N'Zoo (Guinea) → Gbapleu–Danané (Costa de Marfil). Los 48 km entre la frontera y Danané están asfaltados desde 2017; el lado guineano (Lola–N'Zoo, 32 km) sigue en obras y en muy mal estado, y el tramo Sérédou–Nzérékoré está descrito por la prensa guineana como «nidos de elefante» (~4 h para 97 km). Zona de triple frontera Costa de Marfil–Guinea–Liberia: no desviarse hacia el sur. ATENCIÓN: el visado marfileño NO se puede sacar aquí — hay que llevarlo ya estampado desde la embajada de Conakry. Coordenada aproximada del puesto."),
    ("Frontera · Salida bajada — Noé / Elubo (hacia Ghana)", "Frontera", 5.1167, -2.7667,
     "El paso más transitado de toda África occidental francófona-anglófona: carretera asfaltada en buen estado a ambos lados y puente sobre el río Tanoé. Horario habitual 06:00–18:00. Cambio de franco CFA a cedi, cambio de conducción no (ambos por la derecha) pero sí de idioma administrativo. Presentar Carte Brune CEDEAO, CPD y certificado de fiebre amarilla."),
    ("Frontera · Entrada subida — Soko / Sampa (desde Ghana)", "Frontera", 7.9717, -2.7189,
     "Paso interior del este: Sampa (región de Bono, Ghana) del lado ghanés, Soko del lado marfileño, camino de Bondoukou. La evaluación logística del Logistics Cluster lo documenta como puesto formal abierto TODOS LOS DÍAS de 06:00 a 18:00, sin cierres anuales, con tráfico modesto (~10 camiones y ~20 vehículos privados al día) y aduana de tramitación MANUAL, no informatizada — es decir, lento pero sin colas. Sampa tiene siete gasolineras y mercado los lunes; Tema Port queda a 520 km. Se elige expresamente para no repetir Noé en la subida. CONFIRMAR que la aduana marfileña de Soko puede tramitar el passavant/CPD de un vehículo extranjero; alternativa de respaldo: Takikro/Tanoso o volver a Noé."),
    ("Frontera · Salida subida — Sipilou (hacia Guinea)", "Frontera", 7.9833, -8.0333,
     "Segundo paso marfileño hacia Guinea, al norte del de Gbapleu, en el departamento de Biankouma; figura en la evaluación logística del Logistics Cluster como puesto fronterizo formal. Da a la región guineana de Beyla/Sinko. Pista y asfalto degradado, menos tráfico y menos servicios que Gbapleu — pero es lo que permite que la subida no repita el paso de la bajada. CONFIRMAR horario, existencia de aduana con capacidad de tramitar CPD y estado de la pista 72 h antes. Coordenada aproximada."),
    ("Embajada de España en Abiyán", "Consular", 5.3600, -3.9700,
     "Impasse Ablaha Pokou, Cocody Danga Nord, Abiyán. Tel. +225 22 44 48 50 · emb.abidjan@maec.es. Demarcación que cubre también Guinea y otros países del entorno: es el punto consular de referencia de todo este tramo del viaje."),
    ("CHU de Cocody — Abiyán", "Hospital", 5.3550, -3.9850,
     "Centro Hospitalario Universitario de Cocody, referencia de la capital económica y la mejor capacidad de urgencias graves de la subregión junto con la PISAM (clínica privada de Cocody, la opción habitual para extranjeros). Coordenada urbana aproximada."),
    ("Hospital regional de Man", "Hospital", 7.4125, -7.5539,
     "Referencia hospitalaria del bloque de montaña del oeste (Nimba, Dent de Man, Tonkoui, puentes de lianas). Capacidad limitada: para algo grave, evacuación a Abiyán."),
    ("CHU de Bouaké", "Hospital", 7.6906, -5.0300,
     "Centro hospitalario universitario del centro del país y única referencia seria del corredor de subida entre Abiyán y el norte."),
    ("Combustible · Danané / Man", "Combustible", 7.4125, -7.5539,
     "Primer repostaje formal tras la frontera de Guinea (Total, Petro Ivoire, Ola Energy). Llenar a fondo en Man antes de las pistas de montaña y del desvío al Nimba: fuera de las ciudades del oeste la oferta es informal y de calidad dudosa."),
    ("Combustible · Daloa / Yamoussoukro", "Combustible", 6.8097, -5.2758,
     "Eje central con la mejor red del interior; Yamoussoukro es además el mejor punto para repostar antes de bajar hacia Gagnoa, Soubré y el bloque forestal de Taï."),
    ("Combustible · Soubré y San-Pédro (bloque de Taï)", "Combustible", 4.7485, -6.6363,
     "Soubré es la última plaza formal antes de las pistas forestales de Taï por el norte, y San-Pédro —segundo puerto del país, con talleres, recambios y hospital— lo es por el sur al salir del parque hacia la costa. Entre ambos, dentro del bloque forestal, la oferta es escasa: entrar con depósitos llenos y garrafas."),
    ("Combustible · Abiyán", "Combustible", 5.3250, -4.0200,
     "Mejor oferta y mejor calidad del país, con diferencia. Repostar a fondo aquí antes del tramo final a Ghana y, en la subida, al volver a entrar en el país."),
    ("Combustible · Bondoukou / Bouaké / Korhogo (eje de subida)", "Combustible", 7.6906, -5.0300,
     "Tres plazas formales bien espaciadas en el corredor de subida (Bondoukou ~330 km de Bouaké, Bouaké ~230 km de Korhogo). Bouaké es la mejor de las tres para talleres y recambios."),
    ("Combustible · Séguéla (último del oeste en la subida)", "Combustible", 7.9611, -6.6731,
     "Última estación formal fiable antes de Touba, Biankouma y la frontera de Sipilou. Salir de aquí con depósitos y garrafas llenos: el tramo final de la subida tiene oferta escasa e irregular."),
    ("Agua potable y de uso general · Abiyán, Yamoussoukro, Bouaké, Man", "Agua potable", 5.3250, -4.0200,
     "Agua embotellada sin problema de suministro en supermercados (Carrefour, Prosuma, Sococé) de Abiyán y en las capitales regionales. Para la recarga del depósito de uso general, las estaciones Total/Petro Ivoire y los hoteles con aparcamiento de estas cuatro ciudades permiten llenar con manguera; confirmar precio o donativo en recepción."),
    ("Base canina · Abiyán (veterinarios y residencias)", "Consular", 5.3450, -3.9900,
     "Abiyán concentra clínicas veterinarias de nivel europeo y residencias caninas — según el dosier canino del proyecto, el mejor punto de respiro del perro en toda África occidental. Es también donde hay que dejarlo si se entra en el Parque Nacional de Taï o en el de la Comoé. Coordenada aproximada de la zona de Cocody/Deux-Plateaux."),
]

DRONE_CALLOUT = ("warn", "Régimen formal y caro: agrément de explotación de 3 millones de FCFA · tratar el dron como no viable",
                 "Costa de Marfil regula el dron civil desde 2019 mediante la ANAC (Autorité Nationale de l'Aviation Civile) y el reglamento RACI 3009. El agrément de explotación de dron civil se fijó en 3.000.000 FCFA (~4.575 €), y los pilotos deben estar acreditados por la ANAC; para un visitante extranjero se exige licencia de telepiloto reconocida y registro del aparato. Las reglas generales (día, vista directa, máximo ~90 m, 50 m de distancia a personas y edificios, prohibido sobre zonas urbanas densas, 10 km de aeródromos) dejan fuera casi todo lo que querríamos filmar. Norma prudente del proyecto: NO introducir el dron en Costa de Marfil salvo que se consiga autorización escrita previa de la ANAC; el riesgo real es la incautación en aduana en Gbapleu, Noé o Soko.")

STARLINK_CALLOUT = ("ok", "Starlink ACTIVO en Costa de Marfil desde julio de 2026",
                    "La ARTCI concedió a Starlink una licencia provisional de 12 meses y el servicio de internet fijo por satélite se lanzó comercialmente en julio de 2026, convirtiendo a Costa de Marfil en uno de los ~29 mercados africanos activos. Es, junto con Ghana y Senegal, uno de los pocos países del corredor oeste con Starlink confirmado y no solo anunciado. Aun así, la licencia es PROVISIONAL (12 meses) y el régimen de itinerancia regional con el kit comprado en otro país está por confirmar: revisar el mapa oficial y el estado de la licencia 30-60 días antes de entrar, y mantener SIM local como respaldo.")

DOG_MATRIX = [
    ("Abiyán (Cocody, Deux-Plateaux, Plateau)", "permitido con condiciones",
     "El mejor punto canino de toda África occidental según el dosier del proyecto: clínicas veterinarias de nivel europeo y residencias caninas donde dejarlo mientras se hace Taï o Comoé. Calor húmedo muy intenso y tráfico denso: paseos a primera y última hora, correa siempre, y aparcamiento con sombra."),
    ("Grand-Bassam, Assinie, Sassandra, Grand-Lahou (pueblo y playa)", "permitido",
     "Las playas y los campamentos del cordón litoral son, con diferencia, lo más fácil del país con el perro: arena larguísima, alojamientos sencillos con parking y ninguna normativa restrictiva localizada. Cuidado con la resaca del mar (muy fuerte en toda la costa marfileña) y con las serpientes en la vegetación de duna."),
    ("Man, Danané, Biankouma y las montañas del Tonkpi", "permitido con correa",
     "Ciudades y senderos abiertos, sin gestión de parque nacional: Dent de Man, mont Tonkoui, La Cascade y los puentes de lianas son compatibles con el perro. Correa corta obligatoria en la cumbre de la Dent de Man y en los puentes de lianas (el paso es estrecho y las lianas ceden). En los BOSQUES SAGRADOS y en los puentes hay que preguntar al jefe de la aldea: son lugares rituales y la respuesta puede ser que no."),
    ("Parque Nacional de Taï y Parque Nacional de la Comoé", "no confirmado — tratar como prohibido",
     "Los dos son parques nacionales gestionados por la OIPR con grandes mamíferos (elefante de bosque, búfalo, leopardo) y, en Taï, chimpancés con protocolo sanitario estricto por el riesgo de transmisión de enfermedades — un perro es exactamente lo que ese protocolo pretende evitar. Tratarlos como prohibidos hasta confirmación escrita de la OIPR. PLAN B REAL: dejar al perro en una residencia canina de Abiyán (2-4 días) o, si no se quiere ese desvío, turnos entre los tres viajeros con el perro en el campamento de Djouroutou / en el hotel de Soubré o de Bondoukou mientras los otros dos entran con el guía."),
    ("Parque Nacional de Azagny (Grand-Lahou)", "no confirmado — tratar como prohibido",
     "Parque nacional con elefante de bosque y manatí, recorrido en piragua: el perro no entra. Plan B inmediato y cómodo: el pueblo y la playa de Grand-Lahou, a la otra orilla, son perfectamente compatibles y hay alojamiento con parking — un viajero se queda con el perro mientras los otros hacen la piragua."),
    ("Reserva Natural Integral del Monte Nimba", "prohibido (reserva integral)",
     "Por definición una reserva natural INTEGRAL restringe incluso la presencia humana: la entrada del perro es impensable. Alternativa: los miradores y las aldeas del piedemonte en el eje Danané–Gouan-Houo, fuera del perímetro protegido, donde sí puede ir."),
    ("Korhogo, Waraniéné, Katiola, Bondoukou (país senufo y norte)", "permitido con condiciones",
     "Sin restricción localizada en ciudades y aldeas artesanas. En los sinzanga (bosques sagrados senufo) y en los recintos del poro, preguntar SIEMPRE antes: son espacios rituales con prohibiciones propias y un perro puede ser un problema serio. Calor seco muy alto en el norte entre febrero y mayo: agua y sombra."),
]

SOURCES = [
    ("WhirledAway · guía de viaje a Costa de Marfil (e-visa, fronteras, rutas)", "https://whirled-away.com/ivory-coast-travel-guide/"),
    ("WAAfrica · visado de Costa de Marfil 2026: e-visa SNEDAI, trámites y tarifas", "https://waafrica.travel/visa-cote-divoire/"),
    ("SNEDAI Groupe · visa biométrique de Côte d'Ivoire", "https://snedai.com/visabiometrique/"),
    ("FCDO (Reino Unido) · Côte d'Ivoire, riesgos regionales y zonas desaconsejadas", "https://gov.uk/foreign-travel-advice/cote-d-ivoire/regional-risks"),
    ("Embajada de EE. UU. en Abiyán · travel advisory de Côte d'Ivoire (feb. 2026)", "https://ci.usembassy.gov/travel-advisory-cote-divoire-february-18-2026/"),
    ("International Crisis Group · Keeping Jihadists Out of Northern Côte d'Ivoire", "https://www.crisisgroup.org/brf/africa/west-africa/cote-divoire/b192-keeping-jihadists-out-northern-cote-divoire"),
    ("ACLED · el ataque de Kafolo y la amenaza yihadista en la frontera Burkina–Costa de Marfil", "https://acleddata.com/report/light-kafolo-attack-jihadi-militant-threat-burkina-faso-and-ivory-coast-borderlands"),
    ("Le Lynx (Guinea) · estado real del eje Guinea–Costa de Marfil vía Nzérékoré (mayo 2026)", "https://lelynx.net/2026/05/carnet-deroutant-laxe-guinee-cote-divoire-via-nzerekore-encore-en-piteux-etat/"),
    ("Travel2Unlimited · carretera Man (Costa de Marfil) – Nzérékoré (Guinea)", "https://travel2unlimited.com/ivory-coast-guinea-road-from-man-to-nzerekore/"),
    ("Logistics Cluster (LCA) · paso de la frontera de Sipilou", "https://lca.logcluster.org/fr/cote-divoire-237-passage-de-la-frontiere-de-sipilou"),
    ("Logistics Cluster (LCA) · paso fronterizo de Elubo (Ghana)", "https://lca.logcluster.org/ghana-232-border-crossing-elubo"),
    ("Logistics Cluster (LCA) · paso fronterizo de Sampa / Soko (Ghana–Costa de Marfil)", "https://lca.logcluster.org/ghana-231-border-crossing-sampa"),
    ("The Road Chose Me · «Ivory Coast… Coast», travesía en 4x4 por el litoral marfileño", "https://theroadchoseme.com/ivory-coast-coast"),
    ("Lost In A 4x4 · guía del cruce terrestre Costa de Marfil → Ghana", "https://lostina4x4.com/ivory-coast-to-ghana-border-crossing-guide-overland-travel-step-by-step/"),
    ("iOverlander · punto «4x4 Off-Road CI» y puntos verificados en Costa de Marfil", "http://www.ioverlander.com/places/90137-4x4-off-road-ci"),
    ("Overlanding West Africa · Sierra Leona, la región forestal de Guinea y el oeste salvaje de Costa de Marfil", "https://www.overlandingwestafrica.com/news/sierraleone-guinea-ivorycoast/"),
    ("Brendan's Adventures · de Guinea a Costa de Marfil por tierra, llegada a Man", "https://brendansadventures.com/man-i-needed-this-ivory-coast/"),
    ("Kumakonda · Parque Nacional de Taï, experiencia con los chimpancés", "https://kumakonda.com/tai-national-park-ivory-coast-chimpanzees-experience/"),
    ("Écotourisme Taï · actividades de Djouroutou (chimpancés y mont Niénokoué)", "https://ecotourismetai.com/en/activities/djouroutou/"),
    ("Mammal Watching · informe de campo del Parque Nacional de Taï (2024)", "https://www.mammalwatching.com/community-post/tai-national-park-cote-divoire-2024/"),
    ("Discover Ivorycoast · safari en el Parque Nacional de la Comoé", "https://discover-ivorycoast.com/safari-in-comoe-national-park/"),
    ("Discover Ivorycoast · senderismo y cultura en Costa de Marfil", "https://discover-ivorycoast.com/hiking-and-culture-in-ivory-coast/"),
    ("Mon Doux Pays (turismo de Costa de Marfil) · los puentes de lianas de Man", "https://www.mondouxpays.com/choses-a-faire/les-ponts-de-liane"),
    ("Rezo-Ivoire · Man, la ciudad de las 18 montañas", "https://rezoivoire.net/ivoire/villes-villages/367/man-la-capitale-des-18-montagnes.html"),
    ("Baab.ci · escapada a Man, el país de las 18 montañas", "https://baab.ci/articles_baab/escapade-man-ou-le-voyage-au-pays-des-18-montagnes/"),
    ("Guinéematin · inmersión en las cascadas de Man y el puente de lianas", "https://guineematin.com/2025/02/13/cote-divoire-immersion-dans-les-cascades-naturelles-de-man-abritant-le-mythique-pont-de-lianes/"),
    ("UNESCO · Ville historique de Grand-Bassam", "https://whc.unesco.org/en/list/1322/"),
    ("UNESCO · Réserve naturelle intégrale du mont Nimba", "https://whc.unesco.org/en/list/155/"),
    ("Drone Laws · normativa de drones de Costa de Marfil (ANAC, RACI 3009)", "https://drone-laws.com/drone-laws-in-the-ivory-coast/"),
    ("KOACI · reglamento de drones civiles en Costa de Marfil y coste del agrément (3 M FCFA)", "https://www.koaci.com/article/2019/07/09/cote-divoire/societe/cote-divoire-une-reglementation-pour-lutilisation-des-drones-civils-est-en-vigueur-le-prix-de-lagrement-fixe-a-trois-millions-fcfa_132764.html"),
    ("Space in Africa · Starlink entra en servicio en Costa de Marfil (julio 2026)", "https://spaceinafrica.com/2026/07/16/starlink-goes-live-in-cote-divoire/"),
    ("Technext · Starlink se lanza en Costa de Marfil, su mercado africano nº 29", "https://technext24.com/news/starlink-launches-in-cote-divoire/"),
    ("WOAH (OIE) · ficha sanitaria de Côte d'Ivoire", "https://rr-africa.woah.org/en/information-sheet-cote-divoire/"),
    ("Embajada de España en Abiyán · consulados y demarcación", "https://www.exteriores.gob.es/Embajadas/abidjan/es/Embajada/Paginas/Consulados.aspx"),
    ("Comisión Europea · movimiento no comercial de animales de compañía desde terceros países", "https://food.ec.europa.eu/animals/movement-pets/eu-legislation/non-commercial-movement-non-eu-countries_en"),
    ("iOverlander · puntos de combustible, agua y fronteras verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Bajada: Gbapleu/N'Zoo -> Danané -> Man -> Daloa -> Yamoussoukro -> Gagnoa/Soubré -> Taï -> San-Pédro -> Sassandra -> Grand-Lahou -> Abiyán -> Grand-Bassam -> Assinie -> Noé
CORRIDOR = [(7.1000, -8.4000), (7.5406, -8.4581), (7.2597, -8.1550), (7.4125, -7.5539),
            (7.4550, -7.6250), (7.2667, -7.7167), (6.9167, -6.4333), (6.8094, -5.2966),
            (5.7847, -6.5936), (5.7500, -7.3500), (5.4333, -7.1833), (4.7485, -6.6363),
            (4.9500, -6.0833), (5.1333, -5.0167), (5.3250, -4.0200), (5.1961, -3.7389),
            (5.1333, -3.4667), (5.1167, -2.7667)]

# Subida: Soko/Sampa -> Bondoukou -> Comoé (condicional) -> M'Bahiakro -> Bouaké -> Katiola -> Korhogo -> Mankono -> Séguéla -> Touba -> Biankouma -> Sipilou
CORRIDOR_ALT = [(7.9500, -2.7200), (8.0402, -2.8000), (8.7500, -3.7000), (7.4500, -4.3000),
                (7.6906, -5.0300), (8.1333, -5.1000), (9.4578, -5.6294), (9.4028, -5.6700),
                (8.0500, -6.1833), (7.9611, -6.6731), (8.2833, -7.6833), (7.7333, -7.6167),
                (7.9833, -8.0333)]

EXPERIENCIAS = [
    "El e-visa NO sirve por tierra (WhirledAway, guía de Costa de Marfil): «conseguirlo a la llegada por tierra no es posible» — el e-visa SNEDAI solo se valida en el aeropuerto Félix Houphouët-Boigny de Abiyán. Los viajeros terrestres tienen que sacar el visado por adelantado en una embajada marfileña, y lo habitual es hacerlo en el país anterior (para nosotros: Conakry en la bajada, Accra en la subida). Es el dato más crítico de esta ficha y el que puede romper el corredor si se descuida.",
    "El contraste de carreteras en la frontera de Guinea (Travel2Unlimited, ruta Man–Nzérékoré, 210 km / ~4 h): del lado marfileño, «una carretera preciosa en excelente estado con paisajes espectaculares»; nada más pasar la frontera, «se acaba el asfalto y empiezan los baches, el polvo y alguna plantación de cacao». El mismo blog avisa de que «el lado guineano va a dar un infierno total» en el trámite. Le Lynx (prensa guineana, mayo 2026) lo confirma desde el otro lado: Lola–N'Zoo (32 km) sigue en obras desde 2015 y el tramo Sérédou–Nzérékoré (97 km) está lleno de «nidos de elefante» y se tarda unas 4 h; en cambio los 48 km de Danané a la frontera están asfaltados y transitables desde 2017.",
    "Man como premio tras Guinea (Brendan's Adventures, «Man, I needed this»): el relato de un viajero que llega por tierra desde Guinea describe Man como el alivio del oeste africano — clima fresco de montaña, cascadas, puentes de lianas y una ciudad tranquila y organizada después del desgaste de la región forestal guineana. Coincide con la elección de Man como base de 2-3 noches del corredor de bajada.",
    "Taï, el parque que casi nadie visita (Mammal Watching, informe de campo 2024, y Kumakonda): la visita se organiza con el ecoturismo de Taï/OIPR, hay que reservar con antelación, el número de visitantes al grupo de chimpancés habituado de Djouroutou está limitado y se aplica protocolo sanitario (distancia mínima y mascarilla). Los accesos son pistas forestales que en temporada de lluvias se vuelven lentas y embarradas; el avistamiento del uso de herramientas —romper nueces con yunque y martillo de piedra— no está garantizado pero es la razón por la que se va.",
    "El norte que hay que evitar (ACLED e International Crisis Group): los ataques de Kafolo de junio de 2020 y marzo de 2021, contra puestos militares en la frontera con Burkina Faso junto al Parque Nacional de la Comoé, marcaron el desbordamiento del conflicto del Sahel hacia el norte marfileño. El Estado respondió con un despliegue militar importante y la situación se ha contenido, pero los avisos de viaje occidentales siguen desaconsejando en 2026 todo viaje al Parque Nacional de la Comoé, al norte de Zanzan y Savanes y a menos de 40 km de las fronteras de Mali y Burkina Faso. Nuestro corredor de subida está diseñado para no entrar en esa franja.",
    "Overlanding West Africa (operador de expediciones, itinerario Sierra Leona–Guinea forestal–oeste de Costa de Marfil): sus rutas comerciales confirman que el eje Nzérékoré → Danané → Man → Yamoussoukro es la vía overland estándar de entrada por el oeste, y que el bloque de montaña de Man (Dent de Man, cascadas, puentes de lianas, aldeas dan) es el contenido principal de ese tramo. Los itinerarios de operadores son útiles aunque no se contraten: revelan qué tramos funcionan de verdad.",
    "«Las mejores playas que he visto en mi vida» (The Road Chose Me, travesía África completa en Jeep): recorrió la costa marfileña de oeste a este —Grand-Bérébi, cerca de Liberia, Sassandra y Assinie— y la califica por encima de Australia y de Costa Rica. Dos referencias concretas de pernocta con vehículo directamente sobre la arena: Chez JoJo, cerca de Grand-Bérébi, y Chez Jules, cerca de Sassandra. Del contraste al llegar a la capital dice: «después de conducir tanto tiempo por carreteras espantosas, es un shock llegar a una ciudad tan moderna, con autopistas, farolas, señales y rascacielos». Ni una mención a problemas con la policía o los controles.",
    "Frontera de Sampa/Soko (Logistics Cluster, evaluación logística de Ghana): abierta todos los días de 06:00 a 18:00 sin cierres anuales, con solo ~10 camiones y ~20 vehículos privados al día y aduana de tramitación manual. Es decir: lento en el trámite pero sin colas, justo lo contrario de Noé. Sampa tiene siete gasolineras y mercado los lunes, lo que resuelve el repostaje justo antes de cruzar.",
    "Perro en Abiyán (dosier canino del proyecto, §3.6): Abiyán tiene veterinarios de nivel europeo y residencias caninas, y está catalogado como «buen punto de respiro» de África occidental. Es la plaza donde conviene concentrar cualquier revisión, desparasitación o tratamiento del perro en todo el tramo Senegal–Ghana, y donde dejarlo si se entra en Taï o en la Comoé.",
]

CORRIDOR_LABEL = "Bajada"
CORRIDOR_ALT_LABEL = "Subida"

HISTORIA_RESUMEN = ("Costa de Marfil fue durante décadas el «milagro económico» del África Occidental francófona bajo su primer presidente, Félix Houphouët-Boigny, gracias al cacao y al café; tras su muerte en 1993 el país cayó en una crisis de identidad nacional "
                    "en torno al concepto de «ivoirité» que desembocó en dos guerras civiles (2002-2007 y 2010-2011), superadas con una recuperación económica notable en la última década bajo el presidente Alassane Ouattara, aunque la cuestión de la sucesión presidencial y la presión yihadista procedente del Sahel siguen marcando la agenda del norte.")

HISTORIA_SECCIONES = [
    ("Reinos akan, senufo y colonización francesa",
     "El territorio fue hogar de reinos y jefaturas akan (como el Baulé del centro o el Gyaman de Bondoukou), de los senufo del norte y de los pueblos dan, gouro y bété del oeste forestal, con intensas redes comerciales dyula que conectaban el bosque con las rutas transaharianas —Kong y Bondoukou fueron grandes plazas caravaneras. Francia estableció su colonia a finales del siglo XIX e integró el territorio en el África Occidental Francesa como colonia agrícola de plantación (café, cacao, madera), con Grand-Bassam como primera capital antes del traslado a Bingerville y después a Abiyán."),
    ("El «milagro» de Houphouët-Boigny",
     "Félix Houphouët-Boigny, líder independentista convertido en primer presidente en 1960, gobernó hasta su muerte en 1993 con un modelo de estabilidad política, apertura a la inversión francesa y desarrollo agrícola exportador (cacao, del que Costa de Marfil es hoy el mayor productor mundial) que convirtió al país en uno de los más prósperos de la región y atrajo a millones de trabajadores migrantes de los países vecinos. Su proyecto más visible y más discutido fue convertir su aldea natal, Yamoussoukro, en capital política y coronarla con la basílica más grande del mundo."),
    ("La crisis de la «ivoirité» y las guerras civiles",
     "Tras la muerte de Houphouët-Boigny, la disputa por su sucesión reavivó tensiones entre el sur cristiano-animista y el norte musulmán, agravadas por el concepto político de «ivoirité» que cuestionaba la nacionalidad de ciudadanos de origen extranjero (muchos del norte); el país se dividió de facto tras un intento de golpe en 2002, con las Forces Nouvelles controlando el norte desde Bouaké, y vivió una segunda guerra civil en 2010-2011 tras una disputada elección presidencial, resuelta con la intervención de fuerzas francesas y de la ONU. Esa partición explica por qué muchas de las carreteras del centro y del norte se reconstruyeron solo a partir de 2012."),
    ("Situación actual: recuperación, presión del Sahel y el horizonte 2027",
     "Desde 2011, bajo la presidencia de Alassane Ouattara, Costa de Marfil ha experimentado una notable recuperación económica, con Abiyán consolidada como uno de los grandes centros financieros y logísticos del África Occidental francófona. Persisten dos focos de tensión relevantes para un viaje en 2027: la cuestión política de la sucesión presidencial y de la duración de los mandatos, que ha generado episodios de violencia en cada ciclo electoral reciente, y la presión de los grupos armados yihadistas del Sahel sobre la frontera norte con Burkina Faso y Mali, que produjo los ataques de Kafolo en 2020 y 2021 y ha convertido el extremo septentrional del país en zona de despliegue militar permanente."),
]

HISTORIA_FUENTES = [
    ("BBC News · Ivory Coast country profile", "https://www.bbc.com/news/world-africa-13287585"),
    ("Encyclopaedia Britannica · Côte d'Ivoire, History", "https://www.britannica.com/place/Ivory-Coast/History"),
    ("International Crisis Group · Côte d'Ivoire", "https://www.crisisgroup.org/africa/west-africa/cote-divoire"),
    ("ACLED · el ataque de Kafolo y la amenaza yihadista en la frontera con Burkina Faso", "https://acleddata.com/report/light-kafolo-attack-jihadi-militant-threat-burkina-faso-and-ivory-coast-borderlands"),
]

SPEC = dict(
    slug="costa-de-marfil", name="Costa de Marfil", revision="12 sep 2026",
    sub="Corredor doble bajada/subida · documentación · seguridad · logística",
    chips=[
        ("BAJADA", "Gbapleu/N'Zoo → Man → Yamoussoukro → Taï → costa oeste → Abiyán → Noé/Elubo · ~1.700 km"),
        ("SUBIDA", "Soko/Sampa → Bondoukou → Bouaké → Korhogo → Séguéla → Biankouma → Sipilou · ~1.500 km"),
        ("PDIs", "22 puntos repartidos entre los dos corredores, sin solapamiento"),
        ("VISADO", "eVisa SOLO por el aeropuerto de Abiyán — por tierra, visado previo en embajada"),
        ("4x4", "pista a la cima del mont Tonkoui · pistas forestales de Taï · accesos a los puentes de lianas"),
        ("A PIE", "Dent de Man 881 m · mont Niénokoué sobre la selva de Taï · Cascade de Man · Nimba (permiso)"),
        ("PERRO", "Abiyán = mejor base canina de África occidental · playas del litoral sin problema"),
        ("SEGURIDAD", "norte fronterizo con Mali y Burkina y Parque de la Comoé: desaconsejados"),
        ("STARLINK", "activo desde julio de 2026 (licencia provisional 12 meses)"),
    ],
    center=[7.2, -5.5], zoom=6,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Costa de Marfil se cruza DOS VECES por mitades completamente distintas del país. En la <strong>bajada</strong>, "
                   "entrando desde Guinea por Gbapleu/N'Zoo, el corredor recorre el oeste: el macizo del Nimba, las montañas de Man, "
                   "la basílica de Yamoussoukro, la selva primaria de Taï con sus chimpancés que usan herramientas de piedra, y después "
                   "toda la costa de oeste a este —Sassandra, Grand-Lahou, Abiyán, Grand-Bassam y Assinie— hasta salir a Ghana por Noé/Elubo. "
                   "En la <strong>subida</strong>, de vuelta desde Ghana, se entra por el paso interior de Soko/Sampa y se sube por el INTERIOR: "
                   "Bondoukou, el país baulé de Bouaké, la alfarería de Katiola, el país senufo de Korhogo y sus tejidos, y el regreso al oeste "
                   "por Séguéla y Biankouma para salir a Guinea por Sipilou, un paso distinto al de la bajada. "
                   "Los dos corredores no comparten ni una sola etapa. "
                   "<strong>El punto crítico de todo el país es el visado</strong>: el eVisa marfileño solo se valida en el aeropuerto de Abiyán, "
                   "de modo que ambas entradas terrestres exigen visado estampado previamente en una embajada."),
    facts=[
        ("Ventana prevista", "Bajada: tras Guinea, antes de Ghana. Subida: tras Ghana, antes de volver a Guinea."),
        ("Entrada bajada", "Gbapleu / N'Zoo desde Guinea (eje Nzérékoré–Lola–Danané); 48 km asfaltados hasta Danané."),
        ("Salida bajada", "Noé → Elubo (Ghana): el paso más transitado de la subregión, asfaltado en ambos lados."),
        ("Entrada subida", "Soko / Sampa desde Ghana (Bondoukou): paso interior del este, deliberadamente distinto de Noé."),
        ("Salida subida", "Sipilou (Biankouma) hacia Guinea (región de Beyla): segundo paso marfileño hacia Guinea."),
        ("Visado", "CRÍTICO: el eVisa SNEDAI solo es válido en el aeropuerto Félix Houphouët-Boigny de Abiyán. Por tierra hace falta visado estampado previamente: tramitarlo en la Embajada de Costa de Marfil en Conakry (bajada) y en Accra (subida)."),
        ("Vehículos", "CPD o passavant de aduanas; Carte Brune CEDEAO válida en todo el corredor (Guinea, Costa de Marfil y Ghana son miembros de la CEDEAO)."),
        ("Seguridad", "Sur y centro estables. Desaconsejados: franja de 40 km con Mali y Burkina Faso, norte de Zanzan y Savanes, Parque Nacional de la Comoé, y franja de 20 km con Liberia."),
        ("Comunicaciones", "Starlink ACTIVO desde julio de 2026 (licencia provisional de 12 meses); SIM local Orange/MTN/Moov con buena cobertura en todo el eje."),
        ("Salud", "Certificado de fiebre amarilla obligatorio y verificado en frontera; malaria en todo el territorio."),
    ],
    alerts=[
        "VISADO — el riesgo número uno del país: el eVisa de Costa de Marfil (SNEDAI) solo se valida en el aeropuerto internacional Félix Houphouët-Boigny de Abiyán. Presentarse en Gbapleu, Soko o Noé con un eVisa es exponerse a que no lo acepten. Para las DOS entradas terrestres hay que llevar visado estampado por una embajada marfileña: lo lógico es tramitarlo en Conakry antes de la bajada y en Accra antes de la subida. Confirmar por escrito con cada embajada, y preguntar expresamente si emiten visado de entrada múltiple que cubra las dos pasadas.",
        "Norte del país: los avisos occidentales vigentes desaconsejan todo viaje a menos de 40 km de las fronteras de Mali y Burkina Faso, al norte de los distritos de Zanzan y Savanes y al Parque Nacional de la Comoé, por riesgo de atentado y secuestro procedente del Sahel (ataques de Kafolo de 2020 y 2021). El corredor de subida está trazado para no entrar en esa franja, pero KORHOGO está en el distrito de Savanes: es el punto de la ficha que más hay que revalidar.",
        "Parque Nacional de la Comoé: es Patrimonio de la UNESCO y el mayor parque de África occidental, pero está expresamente desaconsejado en los avisos de viaje de 2026. Queda en la ficha como PDI CONDICIONAL: solo se entra si la situación ha cambiado, solo por la puerta sur de Kakpin y nunca por Kafolo o el flanco norte.",
        "Frontera con Liberia: varios avisos desaconsejan acercarse a menos de 20 km por presencia de milicias. Afecta al entorno de Danané, Toulepleu y al flanco oeste del Parque de Taï (río Cavally): mantenerse en el eje Danané–Man y acceder a Taï por el norte (Soubré) o por el sur (Djouroutou), no por la frontera.",
        "Dron: el régimen marfileño es formal y caro (agrément de 3 M FCFA, acreditación de telepiloto por la ANAC). Norma prudente del proyecto: no introducir el dron en el país sin autorización escrita previa — el riesgo real es la incautación en aduana.",
        "Contexto político: el ciclo electoral marfileño ha producido episodios de violencia urbana en cada convocatoria reciente. Revisar el calendario político del país antes de fijar las fechas de 2027 y evitar coincidir con una convocatoria electoral, especialmente en Abiyán y Bouaké.",
    ],
    ruta_intro=("Costa de Marfil se recorre dos veces por mitades distintas: la <strong>bajada</strong> hace el OESTE y la COSTA "
                "(Nimba, Man, Yamoussoukro, Taï y todo el litoral hasta Ghana) y la <strong>subida</strong> hace el INTERIOR "
                "(Bondoukou, Bouaké, Katiola, Korhogo y el regreso al oeste por Séguéla y Biankouma). "
                "Etapas calculadas sobre una media de <strong>250 km/día</strong>: ~1.700 km en la bajada (unos 13-16 días con "
                "las paradas de montaña y de selva) y ~1.500 km en la subida (unos 10-13 días)."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Entrada y triple frontera", "Gbapleu/N'Zoo → Danané → (desvío Monte Nimba, con permiso OIPR)", "~140 km · 2-3 días con el Nimba"),
        ("Bajada 2 · Las dieciocho montañas", "Danané → Man · Dent de Man, mont Tonkoui, La Cascade, puentes de lianas", "~90 km + ~150 km en bucles · 3-4 días"),
        ("Bajada 3 · Centro y basílica", "Man → Daloa (cascadas de Gbêtitapéa) → Yamoussoukro", "~330 km · 2-3 días"),
        ("Bajada 4 · Hacia la selva del suroeste", "Yamoussoukro → Gagnoa → Soubré", "~230 km · 1-2 días"),
        ("Bajada 5 · Parque Nacional de Taï", "Soubré → Taï / Djouroutou · chimpancés y mont Niénokoué", "~180 km de pista · 3 días"),
        ("Bajada 6 · Salida al mar", "Taï → San-Pédro → Sassandra y las playas del oeste", "~310 km · 2-3 días"),
        ("Bajada 7 · Costa central", "Sassandra → Grand-Lahou (Azagny) → Abiyán", "~360 km · 3 días"),
        ("Bajada 8 · Abiyán y el litoral este", "Abiyán → Grand-Bassam → Assinie → Noé/Elubo", "~140 km · 3-4 días"),
        ("Subida 1 · Entrada interior desde Ghana", "Soko/Sampa → Bondoukou", "~40 km · 1 día (más el trámite)"),
        ("Subida 2 · Comoé (CONDICIONAL)", "Bondoukou → puerta sur de Kakpin → Parque Nacional de la Comoé", "~180 km · 2-3 días · solo si el aviso de seguridad lo permite"),
        ("Subida 3 · Travesía al centro", "Bondoukou → M'Bahiakro → Bouaké", "~330 km · 2 días"),
        ("Subida 4 · Sabana y alfarería", "Bouaké → Katiola → Ferkessédougou → Korhogo", "~280 km · 2-3 días"),
        ("Subida 5 · País senufo", "Korhogo · Waraniéné, bosque sagrado, mercado de artesanos", "~60 km en bucle · 2 días"),
        ("Subida 6 · Bajada al oeste", "Korhogo → Mankono → Séguéla", "~330 km · 2 días"),
        ("Subida 7 · Vuelta a la montaña y frontera", "Séguéla → Touba → Biankouma → Sipilou (frontera de Guinea)", "~380 km · 2-3 días"),
    ],
    offroad=[
        "Pista a la cima del mont Tonkoui (1.189 m): ~25 km de tierra roja desde Man, con cárcavas, roderas profundas y tramos lavados que empeoran mucho en lluvias. Es la subida 4x4 más divertida del corredor de bajada y termina en el mejor mirador del país, con Guinea y Liberia a la vista. Amanecer sobre un mar de nubes si se madruga.",
        "Accesos a los puentes de lianas (Lieupleu, Vatouo, Gbangbégouiné, Niahoin): 20-40 km de pistas de tierra por la selva desde Man, con vados y pasos estrechos entre plantaciones de café y cacao. Ninguna está señalizada: guía de Man muy recomendable.",
        "Pistas forestales del Parque Nacional de Taï: los accesos desde Soubré (norte) y hacia Djouroutou (sur) son pistas de laterita en pleno bloque forestal, con puentes de madera y barro profundo en temporada húmeda. Es el tramo del país donde más riesgo hay de quedarse atascado; llevar equipo de recuperación y planificar días de margen.",
        "Costa oeste entre San-Pédro y Sassandra: desvíos de pista de arena hacia las playas (Poly Plage, Batelebré, Drewin, Niega) que no aparecen en las cartografías generalistas y que son el mejor vivac del litoral. Arena blanda cerca de la duna: bajar presiones.",
        "Grand-Lahou: acceso por la lengua de arena y cruce en pinaza hasta el cordón litoral y la boca del Bandama; combinación de pista de arena y transporte fluvial, con las ruinas del viejo Grand-Lahou comidas por el mar como recompensa.",
        "Acceso al Monte Nimba desde Danané / Gouan-Houo: pista de montaña hacia el piedemonte del macizo, sin servicios y con el condicionante de que la reserva es INTEGRAL y exige permiso previo de la OIPR. Confirmar antes de comprometer el día.",
        "Tramo final de la subida, Séguéla → Touba → Biankouma → Sipilou: asfalto degradado que alterna con pista, sin apenas estaciones formales y con un puesto fronterizo pequeño al final. Depósitos llenos desde Séguéla.",
        "Estado general en lluvias: la gran estación húmeda del sur y el oeste va de mayo a julio, con una segunda de octubre a noviembre; el norte tiene una única estación de junio a octubre. Las pistas de laterita del bloque forestal (Taï, Man) se vuelven jabón en ese periodo y los vados suben rápido. En seco, casi todo el corredor es asumible con 4x4 estándar.",
    ],
    senderismo=[
        "Dent de Man (881 m): LA excursión clásica del país. Unas 2-3 h de subida por selva y bloques de roca desde los barrios altos de Man, con vistas de 360º sobre el mar de montañas del Tonkpi. Guía local recomendable, tanto por la falta de señalización como por los bosques sagrados que rodean la ruta. Tramo final expuesto; resbaladizo en lluvias.",
        "Mont Tonkoui (1.189 m), techo del oeste: se puede subir a pie desde la carretera de Biankouma, o subir en 4x4 y caminar por la cresta y los antiguos aterrazamientos de la estación climática. Bosque de altura con orquídeas y aves de montaña.",
        "Mont Niénokoué (396 m), Parque Nacional de Taï: media jornada larga con guía desde Djouroutou, atravesando selva primaria hasta una plataforma rocosa que domina el dosel hasta el horizonte. El mejor mirador de selva del viaje. Calor y humedad extremos.",
        "Seguimiento de chimpancés en Taï (Djouroutou): caminata de varias horas por el interior de la selva con rastreadores del proyecto, siguiendo al grupo habituado. Protocolo sanitario estricto (distancia mínima y mascarilla). No es un paseo: es selva cerrada, barro y sanguijuelas en época húmeda.",
        "La Cascade de Man: paseo corto y fácil desde el aparcamiento por un túnel de bambúes gigantes hasta el salto. Apto para todos y compatible con el perro con correa.",
        "Puentes de lianas de Lieupleu y Vatouo: caminata corta desde el aparcamiento hasta el río y cruce del puente (que se mueve mucho). Tasa a la aldea y permiso del jefe.",
        "Cascadas de Gbêtitapéa (Daloa): recorrido corto entre las marmitas de granito y los saltos, buena parada para estirar las piernas en el eje Man–Yamoussoukro.",
        "Monte Nimba (1.752 m en el pico Richard-Molard): la gran cumbre de la región, pero es RESERVA INTEGRAL en su parte marfileña — la subida solo es posible con permiso de la OIPR y guía. La alternativa habitual de los viajeros es hacer la cumbre desde el lado guineano; decidir de qué lado se intenta forma parte de la coordinación con la ficha de Guinea.",
        "Mont Korhogo: subida corta de una hora a las afueras de Korhogo, con vista sobre la sabana arbolada del norte y sobre la ciudad. Buena excursión de amanecer antes de que apriete el calor.",
    ],
    acampada=[
        "Playas del oeste (Grand-Bérébi, Poly Plage, Batelebré, Drewin, Niega, entre San-Pédro y Sassandra): campamentos sencillos junto a la arena con sitio para aparcar los vehículos — la mejor pernocta del corredor de bajada y la más cómoda con el perro. Dos referencias concretas citadas por otros overlanders: Chez JoJo (Grand-Bérébi) y Chez Jules (Sassandra), que dejan dormir con el vehículo sobre la propia playa.",
        "Assinie-Mafia y Assouindé: campamentos y alojamientos de playa con parking; entre semana están prácticamente vacíos, el fin de semana se llenan de Abiyán. Reservar si se cae en sábado.",
        "Grand-Bassam: hoteles y maquis con aparcamiento en el Quartier France y junto a la playa; opción más práctica que la acampada libre por la afluencia de la zona.",
        "Man y Biankouma: hoteles de montaña con aparcamiento cerrado, base para los bucles a pie del Tonkpi. La acampada libre en el bosque del oeste no es buena idea sin permiso de la aldea: casi todo el monte está repartido entre comunidades y hay bosques sagrados.",
        "Djouroutou / Taï: campamento ecoturístico del parque con alojamiento básico — es el único sitio razonable para dormir dentro del bloque forestal, y hay que reservarlo junto con la visita.",
        "Abiyán y Bouaké: aparcamiento vigilado obligatorio, hotel con parking mejor que cualquier alternativa. No acampar en la periferia de ninguna de las dos.",
        "Regla general del país: pedir permiso al jefe de la aldea (el «chef du village») antes de plantar el campamento en cualquier sitio rural — es la práctica normal y resuelve a la vez la seguridad y la cortesía.",
    ],
    visado=[
        "CRÍTICO: el eVisa marfileño (plataforma SNEDAI) SOLO se valida en el aeropuerto internacional Félix Houphouët-Boigny de Abiyán. Las fuentes consultadas son explícitas: «el aeropuerto Félix Houphouët-Boigny es el único punto de entrada para los titulares de un eVisa SNEDAI», y los viajeros terrestres «no pueden obtenerlo a la llegada por tierra».",
        "Para las dos entradas terrestres hay que llevar visado ESTAMPADO por una representación marfileña. Plan del proyecto: tramitarlo en la Embajada de Costa de Marfil en Conakry antes de la bajada, y en la de Accra antes de la subida. Confirmar por escrito plazos, documentación y si emiten visado de entrada múltiple que cubra las dos pasadas.",
        "Coste de referencia del eVisa: ~73 € / 90 días de validez desde la emisión (no desde la llegada) y 3-4 días laborables de tramitación; el visado estampado en embajada tiene tarifa y plazo propios — por confirmar en cada embajada.",
        "Certificado internacional de fiebre amarilla obligatorio y verificado con frecuencia en los pasos terrestres.",
        "Llevar itinerario, reservas o carta de invitación, y prueba de fondos: en los consulados de la región se piden con más rigor que en el trámite online.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Gbapleu / N'Zoo (Guinea)", "Eje Nzérékoré–Lola–N'Zoo; 48 km asfaltados hasta Danané. Visado ya estampado: aquí NO se emite. Lado guineano lento y degradado."),
        ("Salida bajada", "Noé → Elubo (Ghana)", "Paso más transitado de la subregión; asfaltado en ambos lados, horario habitual 06:00–18:00. Carte Brune, CPD y fiebre amarilla."),
        ("Entrada subida", "Soko / Sampa (Ghana)", "Paso interior del este hacia Bondoukou, elegido para no repetir Noé. CONFIRMAR horario y capacidad aduanera para CPD; respaldo: Takikro o el propio Noé."),
        ("Salida subida", "Sipilou (hacia Guinea, región de Beyla)", "Segundo paso marfileño hacia Guinea, al norte de Gbapleu (departamento de Biankouma). Puesto pequeño: confirmar horario, aduana y estado de la pista 72 h antes."),
        ("Excluido", "Fronteras del norte (Mali y Burkina Faso)", "Fuera de la ruta por seguridad: franja de 40 km desaconsejada por riesgo de atentado y secuestro procedente del Sahel."),
        ("Excluido", "Frontera de Liberia (Toulepleu, Prollo, Danané sur)", "Fuera de la ruta: franja de 20 km desaconsejada por presencia de milicias. Además, el visado de Liberia no se obtiene en frontera terrestre."),
    ],
    vehiculos=[
        "CPD (carnet de passages en douane) o passavant emitido en frontera; llevar copias impresas de la documentación de ambos vehículos para los numerosos controles internos — Costa de Marfil tiene más puestos de control en carretera que la media de la región.",
        "Carte Brune CEDEAO: Guinea, Costa de Marfil y Ghana son los tres miembros de la CEDEAO, así que una Carte Brune en vigor cubre todo el corredor. Comprobar que la póliza incluye expresamente Costa de Marfil y las fechas de las dos pasadas; si no, se compra en el propio puesto fronterizo.",
        "Carnet de conducir internacional: exigido en los controles junto con el permiso nacional.",
        "Depósitos y garrafas llenos antes de: el bloque forestal de Taï (desde Soubré o San-Pédro) y el tramo final de la subida (desde Séguéla). Son los dos únicos puntos del país sin garantía de suministro formal.",
        "Neumáticos y suspensiones: Abiyán y Bouaké son las dos plazas con talleres y recambios reales; Abiyán es además el mejor punto de todo el corredor oeste africano para una revisión seria antes o después del bloque centroafricano.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "No introducir el dron sin autorización previa escrita de la ANAC: el régimen marfileño exige registro del aparato y acreditación del telepiloto, y el agrément de explotación de dron civil está fijado en 3.000.000 FCFA.",
        "Reglas de vuelo del RACI 3009: solo de día, vista directa permanente, altura máxima en torno a 90 m, 50 m de separación de personas, edificios y animales, prohibido sobre zonas urbanas densas y a menos de 10 km de aeródromos.",
        "No sobrevolar nunca Abiyán, Yamoussoukro (zona presidencial y basílica), instalaciones portuarias de Abiyán y San-Pédro, ni ninguna instalación militar — el norte del país está en despliegue militar permanente.",
        "Decisión recomendada del proyecto: dejar el dron guardado y declarado, o directamente no llevarlo en este país. El coste de una incautación en aduana supera cualquier plano que se pueda conseguir.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Servicio comercial activo desde julio de 2026 tras la licencia provisional de 12 meses concedida por la ARTCI: es uno de los pocos países del corredor oeste con Starlink confirmado y no solo anunciado.",
        "Verificar el estado de la licencia 30-60 días antes: al ser provisional (12 meses), su renovación en 2027 no está garantizada.",
        "Confirmar el régimen de itinerancia regional (Starlink Roaming / Global) para usar el kit comprado fuera del país: es lo que determina si funciona de verdad en ruta.",
        "SIM local (Orange, MTN, Moov) como respaldo: la cobertura móvil es buena en todo el eje Abiyán–Yamoussoukro–Bouaké–Korhogo y razonable en Man; floja en el bloque forestal de Taï.",
    ],
    perro_intro=[
        "Régimen francófono típico, sin fuente oficial marfileña localizada: certificado veterinario internacional en francés, vacuna antirrábica en vigor (varios países francófonos de la región exigen que se haya puesto hace MENOS de 12 meses, lo que choca con las vacunas trienales — revacunar anualmente) y tratamiento antiparasitario documentado.",
        "Permiso de importación previo PROBABLE, a solicitar a la Direction des Services Vétérinaires del Ministère des Ressources Animales et Halieutiques, en Abiyán. Plazo estimado ~2 semanas. Sin confirmación oficial: pedirla por escrito antes de salir de Europa.",
        "Se cruza DOS veces: contar con la posibilidad de necesitar dos permisos separados, uno para la bajada (tramitado desde Guinea o antes) y otro para la subida (tramitado desde Ghana). Es la misma pauta que en el resto de países de doble paso de la ruta.",
        "Abiyán es el mejor punto veterinario de África occidental en esta ruta: clínicas de nivel europeo y residencias caninas. Aprovecharlo para revisión, desparasitación y, si toca, revacunación antirrábica con trazabilidad.",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO para entrar y verificado con frecuencia en los pasos terrestres. Llevarlo siempre a mano, no en el fondo de la mochila.",
        "Malaria presente en todo el territorio y durante todo el año, con mayor intensidad en el oeste forestal y en la estación de lluvias: profilaxis a valorar con Sanidad Exterior y mosquitera/repelente sin excepciones.",
        "Agua: no beber de la red fuera de las grandes ciudades; agua embotellada abundante en todo el eje. Fiebre tifoidea y hepatitis A recomendadas.",
        "Bloque forestal de Taï: humedad y calor extremos, sanguijuelas en época húmeda, y presencia de mosca tsetsé en zonas de bosque — ropa cubierta y repelente potente.",
        "Referencias hospitalarias: CHU de Cocody y la clínica PISAM en Abiyán (lo mejor de la subregión), CHU de Bouaké en el corredor de subida, hospital regional de Man en el bloque de montaña. Seguro con evacuación médica imprescindible: desde Taï o desde el norte, la evacuación a Abiyán es larga.",
    ],
    seguridad_intro=("El sur, el centro y el oeste montañoso del país son estables y se recorren con precaución normal; los dos focos reales "
                     "son el NORTE FRONTERIZO con Mali y Burkina Faso, afectado por el desbordamiento del conflicto del Sahel, y los ciclos "
                     "electorales, que han producido violencia urbana en cada convocatoria reciente. La ruta está trazada para mantenerse lejos "
                     "de la franja norte."),
    seguridad=[
        "Zonas desaconsejadas por los avisos vigentes en 2026: franja de 40 km con las fronteras de Mali y Burkina Faso, norte de los distritos de Zanzan y Savanes, y el Parque Nacional de la Comoé (todo viaje desaconsejado); franja de 20 km con la frontera de Liberia (todo viaje no esencial).",
        "Kafolo y el flanco norte de la Comoé: escenario de los ataques yihadistas de junio de 2020 y marzo de 2021 contra puestos militares. Zona excluida sin discusión.",
        "Korhogo está en el distrito de Savanes, a unos 100-120 km de la frontera de Mali: la ciudad no está expresamente excluida en la redacción actual de los avisos, pero es el punto de la ruta que hay que revalidar con más cuidado 30-60 días antes y de nuevo 72 h antes. Plan B si el aviso empeora: sustituir la etapa de Korhogo por Bouaké → Séguéla directamente vía Mankono, perdiendo el país senufo pero manteniendo el corredor.",
        "Ciclo electoral: evitar coincidir con una convocatoria electoral, sobre todo en Abiyán, Bouaké y las ciudades del norte. Revisar el calendario político antes de fijar fechas.",
        "Conducción: no conducir de noche en ningún tramo (vehículos sin luces, peatones, ganado y baches). Costa de Marfil tiene muchos controles de carretera: documentación completa, actitud tranquila y copias impresas resuelven casi todos.",
        "Abiyán: hurtos y robos con violencia en zonas concurridas y en playas al atardecer; aparcamiento vigilado y nada de valor a la vista en los vehículos.",
        "Mar: la resaca del litoral marfileño es notoriamente fuerte y hay ahogamientos cada año en Grand-Bassam y Assinie. Bañarse solo donde se bañen los locales y nunca solos.",
        "Revisar el aviso del Ministerio de Asuntos Exteriores 72 h antes de cada una de las dos entradas.",
    ],
    agua=[
        "Agua embotellada abundante y barata en supermercados y estaciones de servicio de Abiyán, Yamoussoukro, Bouaké, Daloa, Man y Korhogo: es el tramo con mejor suministro desde Marruecos.",
        "Recarga del depósito de uso general (ducha, aseo, vajilla, limpieza): estaciones Total / Petro Ivoire / Ola Energy y hoteles con aparcamiento de esas mismas ciudades permiten llenar con manguera; confirmar precio o donativo en recepción.",
        "Bloque forestal de Taï y tramo Séguéla–Sipilou: salir con los depósitos llenos al 100 %; en el interior del bloque forestal no hay suministro fiable ni embotellado garantizado.",
        "No rellenar de la red fuera de las capitales regionales sin filtrar y potabilizar.",
    ],
    combustible=[
        "Bajada, sin gap de 500 km: Danané/Man (tras la frontera) → Daloa ~180 km → Yamoussoukro ~150 km → Soubré ~230 km → San-Pédro ~200 km → Sassandra ~110 km → Abiyán ~360 km, todos con estaciones formales (Total, Petro Ivoire, Ola Energy, Vivo). El único tramo delicado es el interior del bloque de Taï: entrar con depósitos y garrafas llenos desde Soubré o San-Pédro.",
        "Subida: Bondoukou → Bouaké ~330 km → Katiola ~50 km → Korhogo ~230 km → Séguéla ~330 km, todos con estación formal. El tramo final Séguéla → Touba → Biankouma → Sipilou (~380 km) es el que tiene la oferta más escasa e irregular: llenar a fondo en Séguéla y llevar garrafas.",
        "Calidad del gasóleo razonable en la red formal de las grandes ciudades; desconfiar del combustible informal en garrafas del oeste forestal y del norte. Llevar embudo con filtro.",
        "Abiyán tiene la mejor calidad y el mejor precio del país: repostar a fondo allí en las dos pasadas.",
    ],
    experiencias_intro=("Relatos y comentarios reales de otros overlanders y de prensa local sobre Costa de Marfil, para contrastar con la "
                        "planificación oficial de esta ficha. El país está mucho mejor documentado que sus vecinos del bloque forestal, "
                        "pero el dato del visado terrestre aparece casi solo en blogs de viajeros, no en las webs oficiales:"),
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Visado terrestre — PRIORIDAD MÁXIMA", "Confirmar por escrito con las embajadas de Costa de Marfil en Conakry y en Accra que emiten visado estampado a extranjeros en tránsito, plazo, coste y si existe entrada múltiple que cubra las dos pasadas"),
        ("Paso de Soko / Sampa (entrada subida)", "Confirmar horario, si tiene aduana con capacidad de tramitar CPD/passavant para vehículos extranjeros, y estado de la carretera; si no, decidir alternativa (Takikro o repetir Noé)"),
        ("Paso de Sipilou (salida subida)", "Confirmar que está operativo para extranjeros con vehículo propio, horario, aduana y estado de la pista Biankouma–Sipilou; respaldo: volver a salir por Gbapleu"),
        ("Parque Nacional de la Comoé", "Decisión GO/NO-GO con el aviso de Exteriores en la mano 72 h antes; si se va, solo puerta sur de Kakpin y con acompañamiento de la OIPR"),
        ("Korhogo y el distrito de Savanes", "Revalidar el aviso de seguridad 30-60 días antes y de nuevo 72 h antes; plan B ya definido (Bouaké → Mankono → Séguéla sin Korhogo)"),
        ("Monte Nimba", "Confirmar con la OIPR si la reserva integral marfileña admite visita con permiso y guía, o si conviene hacer el Nimba desde el lado guineano — coordinar con la ficha de Guinea"),
        ("Parque Nacional de Taï · reserva y tasas", "Reservar con antelación la visita a los chimpancés de Djouroutou (cupo limitado), confirmar tasas, protocolo sanitario y estado de las pistas de acceso según la estación"),
        ("Perro · permiso de importación", "Escribir a la Direction des Services Vétérinaires (Ministère des Ressources Animales et Halieutiques, Abiyán) para confirmar si hace falta permiso previo y si se necesitan dos permisos para las dos pasadas"),
        ("Perro en Taï, Comoé y Azagny", "Confirmar por escrito con la OIPR la política de mascotas; reservar residencia canina en Abiyán como plan B por defecto"),
        ("Starlink", "Verificar la renovación de la licencia provisional (12 meses desde julio de 2026) y el régimen de itinerancia del kit propio, 30-60 días antes"),
        ("Dron", "Resolver la autorización con la ANAC o, más probablemente, excluir el dron del país"),
        ("Calendario político 2027", "Comprobar el calendario electoral marfileño antes de fijar las fechas de las dos pasadas y evitar coincidir con una convocatoria"),
        ("Fotos pendientes de sustituir", "Danané, mont Tonkoui, Gbêtitapéa, Bondoukou, Séguéla, Katiola, Biankouma y Niénokoué usan imágenes de referencia de su región o de su temática, no del propio sitio: sustituir por fotos propias cuando las tengamos"),
        ("Coordenadas a afinar", "Puestos de Gbapleu, Soko y Sipilou, y los sitios de Lieupleu, Gbêtitapéa, Niénokoué y Waraniéné están marcados como aproximados: afinar con track real o con iOverlander antes de generar los GPX"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación.",
    emergency="Policía 110/111 · Bomberos 180 · SAMU 185 (verificar localmente al entrar). Embajada de España en Abiyán: +225 22 44 48 50 · emb.abidjan@maec.es.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

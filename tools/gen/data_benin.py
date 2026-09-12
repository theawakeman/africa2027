# -*- coding: utf-8 -*-
"""Benín — ficha completa, corredor doble bajada (costa) / subida (interior) — 12 sep 2026."""
from data_common import make_ficha
import re as _re

W = "https://commons.wikimedia.org/wiki/Special:FilePath/"

POIS = [
    # ===== BAJADA: Hillacondji (Togo) -> Grand-Popo -> Ouidah -> lago Ahémé -> Ganvié -> Cotonú -> Porto-Novo -> Sèmè-Kraké (Nigeria) =====
    dict(n=1, name="Grand-Popo, la Bouche du Roy y las playas del Mono", cat="Costa", prio="Alta", dog="permitido", time="1–2 noches",
         lat=6.2833, lon=1.8167,
         desc="Primera parada nada más entrar desde Togo: antigua ciudad comercial afro-brasileña, hoy pueblo de playa tranquilo con casas coloniales en ruina y una franja de arena inmensa. A 15 km, la BOUCHE DU ROY es el punto donde el río Mono rompe el cordón litoral y desemboca en el Atlántico: un delta de manglares, bancos de arena y aves acuáticas que se recorre en piragua desde Avlo, con un proyecto de ecoturismo comunitario y la playa donde desovan tortugas marinas entre noviembre y marzo. La costa tiene resaca fuerte: bañarse solo donde lo hagan los locales. Es la mejor pernocta de todo el corredor con el perro.",
         credit="Wikimedia Commons", source=W + "Fleuve%20de%20la%20Bouche%20du%20Roy%20à%20Grand-popo%20au%20Bénin.jpg?width=900"),
    dict(n=2, name="Ouidah · Ruta de los Esclavos y Puerta del No Retorno", cat="Patrimonio", prio="Alta", dog="permitido con condiciones", time="½–1 día",
         lat=6.3467, lon=2.0800,
         desc="Los 3,5 km que separaban la plaza de subastas de la playa de embarque, jalonados hoy por monumentos: el Árbol del Olvido (donde se obligaba a los cautivos a dar vueltas para borrar su identidad), el Árbol del Retorno, la fosa común de Zoungbodji y, al final, la PUERTA DEL NO RETORNO, arco monumental de 1995 frente al océano. Ouidah fue durante casi dos siglos uno de los mayores puertos de embarque de la trata atlántica. El conjunto forma parte de los «Sites marquants de la Route de l'Esclave au Bénin», en la lista indicativa de la UNESCO desde febrero de 2021. Recorrerlo a pie, a primera hora, es la visita más fuerte del país.",
         credit="Borisghost · CC0", source=W + "Porte%20du%20non-retour%20au%20Benin.jpg?width=900"),
    dict(n=3, name="Ouidah · Templo de las Pitones, basílica y fuerte portugués", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=6.3639, lon=2.0856,
         desc="El casco de Ouidah concentra el corazón religioso del vudú y su choque con el catolicismo: el TEMPLO DE LAS PITONES, donde se guardan pitones reales (Python regius) sagradas del culto a Dangbé y que se pueden sostener, está literalmente ENFRENTE de la Basílica de la Inmaculada Concepción. A pocas manzanas, el FUERTE PORTUGUÉS DE SÃO JOÃO BAPTISTA DE AJUDÁ (1721) —que fue el territorio portugués más pequeño del mundo hasta 1961— alberga hoy el Museo de Historia de Ouidah, y el bosque sagrado de Kpassè guarda estatuas de las divinidades vodun entre árboles centenarios. Todo se hace a pie en una mañana.",
         credit="Wikimedia Commons", source=W + "Le%20Temple%20des%20Pythons%20de%20Ouidah.jpg?width=900"),
    dict(n=4, name="Vodun Days · fiesta nacional del vudú (10 de enero, Ouidah)", cat="Cultura", prio="Alta", dog="prohibido", time="2–3 días",
         lat=6.3450, lon=2.0800,
         desc="⚠️ COMPROBAR CALENDARIO: el 10 de enero es fiesta nacional en Benín (Fête du Vodoun) desde el reconocimiento oficial de la religión en 1996, y desde 2024 el gobierno la ha convertido en el festival VODUN DAYS, un evento de tres días —habitualmente 8, 9 y 10 de enero— con epicentro en la playa de Ouidah: procesiones, zangbeto (los «guardianes de la noche» que giran como pajares vivientes), egungun, tambores y miles de peregrinos y visitantes. SI EL VIAJE ARRANCA EN ENERO DE 2027, EL PASO POR BENÍN PUEDE COINCIDIR: merece la pena forzar el calendario para estar aquí, pero implica reservar alojamiento con mucha antelación y contar con una Ouidah abrumada de gente. Confirmar fechas exactas de 2027 en vodundays.bj. Con multitudes así, el perro se queda en el vehículo.",
         credit="Wikimedia Commons", source=W + "Le%20Temple%20des%20Pythons%20à%20Ouidah.jpg?width=900"),
    dict(n=5, name="Lago Ahémé y Possotomé", cat="Naturaleza", prio="Media", dog="permitido con condiciones", time="1–2 noches",
         lat=6.4500, lon=1.9833,
         desc="Laguna de 78 km² tierra adentro desde Grand-Popo, con aldeas de pescadores en las dos orillas, dos bosques sagrados y numerosos templos vodun. POSSOTOMÉ, en la orilla este, fue el primer «pueblo ecológico» creado por Eco-Bénin: hay fuentes de agua mineral explotadas desde 1952 (las «sources thermales»), un albergue comunitario con camping a orillas del lago, y circuitos de medio día en piragua (técnicas de pesca tradicionales, acadjas), caminatas por las aldeas de alfareros y rutas de plantas medicinales. Es la parada tranquila del corredor costero y una de las pocas con camping organizado.",
         credit="Wikimedia Commons", source=W + "Barque%20motorisée%20à%20la%20bouche%20du%20Roy%20sur%20le%20fleuve%20Mono.jpg?width=900"),
    dict(n=6, name="Route des Pêches y playas de Avlékété", cat="Costa", prio="Media", dog="permitido", time="½ día",
         lat=6.3400, lon=2.1700,
         desc="La franja de cocoteros entre Cotonú y Ouidah, recorrida por la ROUTE DES PÊCHES: un eje costero de unos 40 km, históricamente pista de arena entre el mar y la laguna, hoy en obras de asfaltado por tramos, con aldeas de pescadores, playas vacías y algunos alojamientos de playa (Avlékété, Djègbadji, Fidjrossè). Cuando queda pista es el tramo de conducción más divertido del sur del país. Salinas artesanales de Djègbadji cerca del embarcadero histórico de la trata. Confirmar el estado real del asfaltado en 2027.",
         credit="Wikimedia Commons", source=W + "Fleuve%20de%20la%20Bouche%20du%20Roy%20à%20Grand-popo%20au%20Bénin.jpg?width=900"),
    dict(n=7, name="Embarcadero de Abomey-Calavi (acceso a Ganvié)", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="½ día",
         lat=6.4478, lon=2.3556,
         desc="Punto logístico obligado: es de aquí de donde salen las piraguas —motorizadas o a pértiga— hacia Ganvié, a unos 30-45 minutos de travesía por el lago Nokoué. Hay aparcamiento vigilado, oficina de tarifas oficial (el precio va por piragua, no por persona, y conviene cerrarlo antes de embarcar) y guías acreditados. ES AQUÍ DONDE SE QUEDA EL PERRO, en el vehículo a la sombra y con uno de los viajeros, mientras los otros dos hacen la visita: la piragua no es sitio para él.",
         credit="Wikimedia Commons", source=W + "Embarcadère%20de%20Ganvié%20Abomey-Calavi%20-Bénin5%20vue%20de%20coté.jpg?width=900"),
    dict(n=8, name="Ganvié · la «Venecia de África»", cat="Cultura", prio="Alta", dog="prohibido", time="½ día",
         lat=6.4667, lon=2.4167,
         desc="Unas 3.000 viviendas sobre pilotes y más de 20.000 habitantes en medio del lago Nokoué: el mayor poblado lacustre de África. Lo fundó el pueblo TOFINU en los siglos XVII-XVIII huyendo de los cazadores de esclavos del reino de Dahomey, que por prohibición religiosa no podía combatir sobre el agua — de ahí el nombre, que significa «por fin estamos a salvo». Todo funciona en piragua: el mercado flotante de mujeres, la escuela, la iglesia, el hospital; se pesca con acadjas, cercados de ramas que hacen de criaderos. Se visita solo en piragua con guía local desde Abomey-Calavi. El perro no tiene cabida ni en la piragua ni en las viviendas.",
         credit="jbdodane · CC BY 2.0", source=W + "Ganvié%20fishing%20village%20on%20stilts%20in%20Benin%20(10282059623)%20(2).jpg?width=900"),
    dict(n=9, name="Cotonú · mercado de Dantokpa", cat="Ciudad · servicios", prio="Alta", dog="permitido con condiciones", time="1–2 noches",
         lat=6.3703, lon=2.3912,
         desc="Capital económica y única gran base logística del país: puerto, aeropuerto internacional, talleres y recambios de todo tipo, supermercados, bancos y clínicas privadas. El MERCADO DE DANTOKPA, sobre la orilla del lago Nokoué, es uno de los mayores de África occidental (más de 20 hectáreas) y tiene desde telas wax hasta un célebre y perturbador rincón de fetiches vudú. La ciudad es densa, caótica y de tráfico brutal por los zémidjan (mototaxis amarillos): conducir con calma y aparcar vigilado. Nudo compartido por los dos corredores.",
         credit="Alacoolwiki · CC BY 4.0", source=W + "Marché%20Dantokpa%201.jpg?width=900"),
    dict(n=10, name="Porto-Novo", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="½–1 día",
         lat=6.4969, lon=2.6289,
         desc="La capital oficial (aunque el gobierno está en Cotonú), a 35 km, sobre la laguna de Porto-Novo: mucho más tranquila y paseable que Cotonú, con arquitectura afro-brasileña de los agudás, la Gran Mezquita —una antigua iglesia baptista convertida en mezquita, con fachada de colores que parece una iglesia portuguesa—, el Palacio Real de Honmé, el Museo Etnográfico y el Jardín de las Plantas y de la Naturaleza. Es la última parada digna antes del caos de Sèmè-Kraké. Imagen de referencia de la laguna de Nokoué, no del propio Porto-Novo.",
         credit="Wikimedia Commons", source=W + "La%20Venise%20de%20l'Afrique.jpg?width=900"),
    # ===== SUBIDA: Ilara/Kétou (Nigeria) -> Savè -> Dassa -> Abomey -> Savalou -> Bassila -> Djougou -> Taneka -> Ouaké (Togo) =====
    dict(n=11, name="Savè · Oké Shabè y los inselbergs de las Collines", cat="Naturaleza", prio="Media", dog="permitido", time="½–1 día",
         lat=8.0333, lon=2.4833,
         desc="Primera parada del corredor interior: Savè se levanta entre enormes domos de granito que emergen de la sabana. La colina de OKÉ SHABÈ figura en la lista indicativa de la UNESCO como uno de los «Sites marquants de la Route de l'Esclave»: fue refugio y bastión de resistencia de las poblaciones shabè frente a las razias esclavistas, con cuevas y estructuras defensivas en lo alto. Se sube a pie con guía local en un par de horas; vistas de toda la llanura del Ouémé. Ciudad con servicios básicos sobre el eje N2 Cotonú-Parakou.",
         credit="Wikimedia Commons", source=W + "Acento%20de%20gun.%20Dassá%20Benin.jpg?width=900"),
    dict(n=12, name="Dassa-Zoumè · las 41 colinas, la gruta de Arigbo y Savalou", cat="Naturaleza", prio="Alta", dog="permitido con correa", time="1–2 días",
         lat=7.7500, lon=2.1833,
         desc="La «ciudad de las 41 colinas», a 209 km de Cotonú, encajada entre domos de granito que son a la vez alto lugar del vudú (todavía se hacen iniciaciones y ofrendas en ellos) y escondite histórico frente a las razias del Dahomey — las colinas sagradas de Yaka están en la lista indicativa de la UNESCO por eso mismo. La PIEDRA HENDIDA DE OKÈYTÉ, un bloque gigante partido en dos, se alcanza en 20 minutos de sendero y da una panorámica de 360°. La GRUTA DE NOTRE-DAME D'ARIGBO es el gran santuario mariano del país, con peregrinación masiva cada 15 de agosto. El Palacio Real conserva la genealogía de 23 reyes. A 40 km, SAVALOU añade otro reino tradicional vivo y su colina sagrada.",
         credit="Wikimedia Commons", source=W + "Acento%20de%20gun.%20Dassá%20Benin.jpg?width=900"),
    dict(n=13, name="Palacios Reales de Abomey (UNESCO)", cat="Patrimonio UNESCO", prio="Alta", dog="permitido con condiciones", time="1 día",
         lat=7.1833, lon=1.9833,
         desc="Patrimonio Mundial desde 1985: el recinto de los doce palacios sucesivos de los reyes del REINO DE DAHOMEY (s. XVII-XIX), cada uno construido por un soberano dentro del mismo muro de tierra de 44 hectáreas. Lo excepcional son los BAJORRELIEVES DE BARRO POLICROMADO que narran, como un cómic monumental, las guerras, los emblemas y los proverbios de cada rey; el Museo Histórico de Abomey ocupa los palacios de Ghézo y Glélé y expone tronos, recados y objetos de las AGOJIE, el cuerpo de guerreras del reino que Europa llamó «amazonas». Varios de los bronces y tesoros saqueados en 1892 fueron devueltos por Francia en 2021 y se exponen en el país. Abomey está a 130 km de Cotonú, en pleno corredor interior.",
         credit="Willem Heerbaart · CC BY 2.0", source=W + "Royal%20Palaces%2C%20Abomey%20(Benin)%20banner.jpg?width=900"),
    dict(n=14, name="Bassila y los montes Kouffé", cat="Naturaleza", prio="Media", dog="permitido", time="1 día",
         lat=9.0167, lon=1.6667,
         desc="Punto medio del corredor interior, en el departamento de la Donga: bosque clasificado de Bassila y la cadena de los MONTES KOUFFÉ, una de las últimas grandes manchas de bosque seco y galería del centro de Benín, con babuinos, cefalofos, hipopótamos en el río Ouémé y una avifauna rica. Sin infraestructura turística formal: pistas forestales, guías locales y caminatas a la medida. Es la etapa que rompe los 210 km entre Savalou y Djougou. Imagen de referencia del paisaje de montaña del norte de Benín, no del propio sitio.",
         credit="Wikimedia Commons", source=W + "Benin%20Natitingou.JPG?width=900"),
    dict(n=15, name="Taneka-Koko y Taneka-Béri", cat="Cultura", prio="Alta", dog="permitido con condiciones", time="½ día",
         lat=9.8667, lon=1.5000,
         desc="A unos 20 km de Djougou, agarrados a la ladera de una colina, dos pueblos taneka de cabañas redondas de barro con techo cónico de paja rematado en una vasija invertida, cocinas exteriores y calles de piedra. Es uno de los conjuntos tradicionales mejor conservados de África occidental. La visita se hace con guía de la comunidad y tasa de entrada (unos 10.000 FCFA), dura unos 45 minutos e incluye normalmente el encuentro con el sacerdote-curandero, vestido solo con pieles y fibras vegetales, que fuma en una larga pipa ceremonial para comunicarse con los ancestros. ⚠️ El sacerdote histórico falleció en 2024 y buena parte de la población se ha trasladado al pueblo nuevo de abajo, volviendo solo para las ceremonias: confirmar qué se visita realmente antes de desviarse. Purificación colectiva cada cinco años.",
         credit="Wikimedia Commons", source=W + "Benin%20Natitingou.JPG?width=900"),
    dict(n=16, name="Djougou", cat="Ciudad · servicios", prio="Media", dog="permitido con condiciones", time="1 noche",
         lat=9.7000, lon=1.6667,
         desc="Capital de la Donga y última base logística real antes de salir a Togo por Ouaké (37 km): combustible, mercado —uno de los grandes mercados de tejidos y de ganado del interior—, hospital de zona y alojamientos con aparcamiento. Ciudad de mayoría musulmana y tradición comerciante dendi/yoruba, con una mezquita antigua y talleres de tejedores. Punto de partida de Taneka-Koko. Imagen de referencia de una ciudad del norte de Benín, no de la propia Djougou.",
         credit="Wikimedia Commons", source=W + "Benin%20Natitingou.JPG?width=900"),
    # ===== LO QUE NOS PERDEMOS: el norte, fuera del itinerario por seguridad =====
    dict(n=17, name="Parque Nacional de la Pendjari — FUERA DEL ITINERARIO 2027", cat="Naturaleza", prio="Baja", dog="prohibido", time="—",
         lat=11.1000, lon=1.3000,
         desc="🚫 EL GRAN SACRIFICIO DE ESTA FICHA. 6.445 km² gestionados por AFRICAN PARKS desde 2017 y considerados el mejor parque de África occidental: unos 2.800 elefantes —la mayor población de la región—, búfalos, hipopótamos, y sobre todo uno de los ÚLTIMOS REFUGIOS DEL LEÓN DE ÁFRICA OCCIDENTAL, subespecie en peligro crítico de la que el complejo W-Arly-Pendjari conserva en torno al 90% de la población superviviente. También guepardo y licaón. PERO: la insurgencia yihadista del norte de Benín, iniciada en noviembre de 2021, ha convertido Pendjari y el vecino Parque W en santuario y base operativa del JNIM, con ataques recurrentes a puestos militares y guardas en la zona (Point Triple, cataratas de Koudou, Koalou) y bajas continuadas hasta 2026. Los avisos de viaje de España, Australia, Canadá y EE. UU. coinciden en «no viajar» a los departamentos de Atakora, Alibori y Borgou y expresamente a Pendjari y W. ESTE PARQUE ESTÁ FUERA DEL ITINERARIO DE 2027. Imagen de referencia de la región de la Atacora.",
         credit="Wikimedia Commons", source=W + "Jeune%20homme%20sautant%20des%20cascades%20de%20Tanougou%20(Bénin).jpg?width=900"),
    dict(n=18, name="Cascadas de Tanougou y la cordillera de la Atacora — FUERA DEL ITINERARIO 2027", cat="Naturaleza", prio="Baja", dog="prohibido", time="—",
         lat=10.7500, lon=1.4300,
         desc="🚫 Lo otro que se pierde. Las CASCADAS DE TANOUGOU, a unos 25 km de Tanguiéta, caen en tres saltos escalonados sobre pozas de baño al pie de la cordillera de la ATACORA, la única cadena montañosa de verdad del país (punto más alto: monte Sokbaro, 658 m) y el paisaje más bonito de Benín: cuestas de cuarcita, aldeas somba con sus tata —las mismas torres-vivienda takienta del Koutammakou togolés, aquí llamadas tata somba, en Boukoumbé y Natitingou—, y rutas de senderismo reales. Toda la zona está en el departamento de ATAKORA, marcado como «no viajar» por la insurgencia del norte. Se conserva en la ficha porque es lo que habría que recuperar si la situación cambiara — y porque el Koutammakou togolés, al otro lado de la frontera, sufre exactamente el mismo problema.",
         credit="Wikimedia Commons", source=W + "Jeune%20homme%20sautant%20des%20cascades%20de%20Tanougou%20(Bénin).jpg?width=900"),
    dict(n=19, name="Parque Nacional W (UNESCO, transfronterizo) — FUERA DEL ITINERARIO 2027", cat="Patrimonio UNESCO", prio="Baja", dog="prohibido", time="—",
         lat=11.8500, lon=2.5000,
         desc="🚫 Patrimonio Mundial transfronterizo entre Benín, Níger y Burkina Faso, nombrado por el meandro en forma de W que dibuja el río Níger; junto con Arly y Pendjari forma el complejo WAP, el mayor ecosistema de sabana intacto de África occidental. El sector beninés está igualmente gestionado por African Parks y, según los análisis publicados de la insurgencia, es hoy base operativa del JNIM: en 2024 se describía abiertamente como «cuartel general» de los grupos armados, y African Parks ha publicado partes de incidentes con guardas muertos. Zona de «no viajar» sin matices. Fuera del itinerario. Imagen de referencia del norte de Benín.",
         credit="Wikimedia Commons", source=W + "Benin%20Natitingou.JPG?width=900"),
]

_CAT_COLOR = {"ciudad · servicios": "azul", "patrimonio": "marron", "cultura": "morado",
              "patrimonio unesco": "marron", "naturaleza": "verde", "costa": "turquesa"}
for _p in POIS:
    _url = _p.pop("source"); _p["img"] = _url
    _m = _re.search(r"Special:FilePath/([^?]+)", _url)
    _p["source"] = "https://commons.wikimedia.org/wiki/File:" + (_m.group(1) if _m else "")
    _p["icon"] = _p["cat"].lower(); _p["color"] = _CAT_COLOR.get(_p["cat"].lower(), "ambar")
    _p.setdefault("dog_note", "")

LOGISTICS = [
    ("Frontera · Entrada bajada — Hillacondji/Sanvee-Condji (desde Togo)", "Frontera", 6.1667, 1.6333,
     "Puesto conjunto (yuxtapuesto) Togo-Benín, con los dos países tramitando en la misma instalación, a 85 km de Cotonú. Cruzar por la mañana: el tráfico comercial satura el mediodía."),
    ("Frontera · Salida bajada — Sèmè-Kraké (hacia Nigeria)", "Frontera", 6.3697, 2.7275,
     "El paso más transitado de toda África occidental, a 20 km de Cotonú y en la puerta de Lagos: congestión permanente, controles múltiples (inmigración, aduana, sanidad, policía) y presión constante de intermediarios. Tramitar el e-Visa nigeriano ANTES de llegar: no existe visado de turismo en frontera. Cruzar a primerísima hora."),
    ("Frontera · Entrada subida — Ilara/Kétou (desde Nigeria, eje interior)", "Frontera", 7.3700, 2.7300,
     "Paso interior mucho más tranquilo que Sèmè-Kraké, sobre el eje Ilara (Ogun, Nigeria) – Kétou. Kétou es además una de las capitales históricas yoruba y conserva la PUERTA AKABA IDÉNA, puerta fortificada de la muralla del reino y símbolo de resistencia frente a las razias del Dahomey, incluida en la lista indicativa de la UNESCO. COORDENADA APROXIMADA: verificar posición exacta, horario y si admite vehículo extranjero con carnet antes de planificar por aquí."),
    ("Frontera · Alternativa subida — Igolo/Idiroko (desde Nigeria)", "Frontera", 6.6500, 2.7700,
     "Segundo paso más transitado con Nigeria, al norte de Porto-Novo; más ágil que Sèmè-Kraké pero todavía muy concurrido. Alternativa razonable si Ilara/Kétou no resulta viable. Coordenada aproximada, por verificar."),
    ("Frontera · Salida subida — Ouaké (hacia Togo, eje Djougou-Kara)", "Frontera", 9.6719, 1.3637,
     "A 37 km de Djougou. Según la evaluación logística del Logistics Cluster opera 24 h los 7 días de la semana salvo festivos nacionales de Benín, y exige seguro CEDEAO y laissez-passer del vehículo; sin báscula en el puesto de aduanas. ⚠️ Está en el departamento de la Donga, que NO figura en las listas de «no viajar» (Atakora, Alibori, Borgou) pero sí dentro de la «mitad norte» que el Ministerio español desaconseja en bloque: revalidar antes de usarlo."),
    ("Frontera · Alternativa subida — Azovè/Tohoun (hacia Togo, eje central)", "Frontera", 6.9833, 1.6667,
     "Paso interior muy al sur, sobre el eje Azovè-Tohoun, completamente fuera de cualquier zona de riesgo. Es el PLAN B del corredor de subida si la situación del norte desaconseja subir hasta Djougou: obliga a acortar el corredor interior (se pierden Bassila, Djougou y Taneka) pero mantiene Kétou, Savè, Dassa, Savalou y Abomey."),
    ("Consulado General de España en Lagos (demarcación de Benín)", "Consular", 6.4400, 3.4200,
     "Benín depende consularmente de la representación española en Nigeria. Emergencia consular: +234 80 3360 1658. Hay además Consulado Honorario en Cotonú: +229 21 339 219 / 220 / 726. Confirmar teléfonos vigentes en exteriores.gob.es antes de viajar."),
    ("CNHU-HKM (Centre National Hospitalier Universitaire) — Cotonú", "Hospital", 6.3667, 2.4333,
     "Principal hospital universitario y de referencia del país; Cotonú tiene además varias clínicas privadas de nivel aceptable, las mejores del corredor. Coordenada urbana aproximada."),
    ("Hospital de zona · Dassa-Zoumè / Abomey", "Hospital", 7.1833, 1.9833,
     "Referencias sanitarias intermedias del corredor interior; entre Abomey y Djougou no hay nada de nivel. Coordenadas urbanas aproximadas."),
    ("Combustible · Cotonú", "Combustible", 6.3703, 2.3912,
     "Mejor oferta y calidad del país (Total, Oryx, Petro Ivoire, MRS); repostar a fondo aquí antes de Sèmè-Kraké o antes de subir al interior. ATENCIÓN: buena parte del combustible que se vende en Benín es «kpayo», gasolina de contrabando nigeriana vendida en garrafas al borde de la carretera, muy barata y de calidad impredecible — NO usarla en los vehículos del proyecto."),
    ("Combustible · Ouidah / Grand-Popo", "Combustible", 6.3628, 2.0853,
     "Estaciones formales en el eje costero entre Hillacondji y Cotonú, sin problema de suministro."),
    ("Combustible · Bohicon (nudo de Abomey)", "Combustible", 7.1786, 2.0667,
     "Bohicon, a 9 km de Abomey, es el verdadero nudo de carreteras y de servicios del centro del país: combustible, talleres, mercado y la estación de ferrocarril. Repostar aquí, no en Abomey."),
    ("Combustible · Dassa-Zoumè y Savalou", "Combustible", 7.7500, 2.1833,
     "Estaciones formales sobre la N2 y la N3; últimos puntos fiables antes del tramo Savalou-Bassila-Djougou."),
    ("Combustible · Djougou", "Combustible", 9.7000, 1.6667,
     "Última plaza con combustible formal antes de salir a Togo por Ouaké. Llenar depósitos y garrafas aquí."),
    ("Agua potable y de uso general · Cotonú", "Agua potable", 6.3703, 2.3912,
     "Agua embotellada sin problema en supermercados; estaciones de servicio y hoteles de Cotonú y Ouidah permiten llenar el depósito de uso general con manguera."),
    ("Agua potable y de uso general · Possotomé (lago Ahémé)", "Agua potable", 6.4500, 1.9833,
     "Albergue y camping comunitario de Eco-Bénin a orillas del lago, con agua corriente; además, fuentes de agua mineral explotadas desde 1952 en el propio pueblo."),
    ("Agua potable y de uso general · Dassa y Djougou", "Agua potable", 7.7500, 2.1833,
     "Hoteles con aparcamiento en ambas ciudades permiten normalmente la recarga del depósito de uso general; confirmar en recepción. Agua de boca siempre embotellada o tratada."),
]

DRONE_CALLOUT = ("warn", "Autorización previa obligatoria: tratar como restringido",
                  "Benín no publica un procedimiento civil turístico simple y estable para drones; la Autorité Nationale de l'Aviation Civile (ANAC-Bénin) exige autorización previa para cualquier vuelo. A esto se suma que el norte del país está en operación militar activa contra grupos armados: un dron al norte de Parakou o de Djougou es un problema de seguridad, no administrativo. Norma prudente del proyecto: no volar sin permiso escrito, mantener el equipo declarable, y no sacar el dron de la caja en ninguna zona del norte ni cerca de Sèmè-Kraké.")

STARLINK_CALLOUT = ("ok", "Starlink ACTIVO en Benín — el mejor punto de conectividad del tramo",
                     "A diferencia de Togo, Benín SÍ figura en los recuentos de septiembre de 2026 entre los países africanos con servicio Starlink operativo; fue además uno de los primeros mercados de África occidental en abrirse. Los planes residenciales de la región se mueven en la horquilla de 30-55 USD/mes con equipo de 200-390 USD, pero no hay tarifa publicada específica para Benín: confirmar precio y cobertura real 30-60 días antes. Mantener SIM local (MTN Bénin, Moov Africa, Celtiis) como respaldo.")

DOG_MATRIX = [
    ("Ganvié y cualquier travesía en piragua", "prohibido",
     "Las piraguas son estrechas, inestables y van cargadas, y el poblado entero está sobre el agua. PLAN B DEFINIDO: el perro se queda en el vehículo, a la sombra y con uno de los tres viajeros, en el embarcadero de Abomey-Calavi (hay aparcamiento vigilado); la visita dura 2-3 horas. Turnarse para que todos la hagan en dos tandas."),
    ("Vodun Days de Ouidah (8-10 de enero)", "prohibido",
     "Multitudes de decenas de miles de personas, tambores, fuego y animales sacrificados. Ni intentarlo. Plan B: dejarlo en el alojamiento con uno de los viajeros, o programar la visita a Ouidah fuera de las fechas del festival si la prioridad es el perro."),
    ("Grand-Popo, Bouche du Roy, Route des Pêches, playas de Avlékété", "permitido",
     "La mejor zona del país para el perro: playas largas y vacías, alojamientos de playa tolerantes y sombra de cocoteros. Cuidado con la resaca del Atlántico —no dejarlo suelto en la orilla— y con las tortugas anidando entre noviembre y marzo en la Bouche du Roy: correa obligatoria en esa zona."),
    ("Lago Ahémé y Possotomé", "permitido con condiciones",
     "El albergue y el camping comunitario de Eco-Bénin admiten normalmente perro (confirmar al reservar). En las salidas en piragua por el lago, mismo criterio que en Ganvié: se queda en tierra."),
    ("Cotonú, Porto-Novo, Ouidah, Abomey, Dassa, Djougou", "permitido con condiciones",
     "Sin restricciones específicas conocidas. Tráfico brutal de mototaxis en Cotonú: correa corta y nunca suelto en calle. Calor y humedad altos todo el año en el sur."),
    ("41 colinas de Dassa, Oké Shabè (Savè), montes Kouffé, Taneka", "permitido con correa",
     "Senderos comunitarios abiertos, sin gestión de parque nacional — son la mejor opción del país para caminar con él. En Taneka y en las colinas sagradas hay perros de aldea sueltos y ganado: correa corta y consultar al guía antes de entrar en los recintos."),
    ("Parque Nacional de la Pendjari y Parque W", "prohibido · y además fuera del itinerario",
     "Doblemente descartados. Por un lado son parques nacionales de African Parks con leones, guepardos, licaones y elefantes: la práctica estándar en parques africanos comparables es prohibir las mascotas, y African Parks no publica política alguna de mascotas para Pendjari — hay que darlo por prohibido. Por otro lado, y esto es lo determinante, LA ZONA ESTÁ FUERA DEL ITINERARIO POR SEGURIDAD. No hay plan B que valga: no se va."),
]

SOURCES = [
    ("Bénin Tourisme · portal oficial del país (benin.bj)", "https://benin.bj/"),
    ("Vodun Days · web oficial del festival de Ouidah", "https://vodundays.bj/en/"),
    ("UNESCO · Palacios Reales de Abomey (Patrimonio Mundial)", "https://whc.unesco.org/en/list/323/"),
    ("UNESCO · Sites marquants de la Route de l'Esclave au Bénin (lista indicativa, 2021)", "https://whc.unesco.org/en/tentativelists/6512/"),
    ("African Parks · Parque Nacional de la Pendjari (superficie, elefantes, leones de África occidental)", "https://www.africanparks.org/the-parks/pendjari"),
    ("African Parks · parte de incidentes en el Parque W de Benín", "https://www.africanparks.org/update-incidents-w-national-park-benin"),
    ("International Crisis Group · Containing Militancy in West Africa's Park W", "https://www.crisisgroup.org/rpt/africa/sahel/burkina-faso-niger-benin/310-containing-militancy-west-africas-park-w"),
    ("Africa Defense Forum · el Parque W convertido en «cuartel general» de los terroristas", "https://adf-magazine.com/2024/05/benins-w-national-park-becomes-headquarters-for-terrorists/"),
    ("Wikipedia · Islamist insurgency in Northern Benin (cronología y ataques 2021-2026)", "https://en.wikipedia.org/wiki/Islamist_insurgency_in_Northern_Benin"),
    ("MAEC · Recomendaciones de viaje para Benín (mitad norte desaconsejada; Alibori, Atakora, Pendjari, W, Kalalé)", "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Ben%C3%ADn"),
    ("Smartraveller (Australia) · Benín: no viajar a Atakora, Alibori y Borgou ni a Pendjari y W", "https://www.smartraveller.gov.au/destinations/africa/benin"),
    ("The Conversation · grupos armados en las reservas forestales de Benín", "https://theconversation.com/armed-groups-are-invading-benins-forest-reserves-why-and-what-to-do-about-it-256136"),
    ("Benin eVisa · actualización de tarifas, validez y entrada múltiple", "https://www.beninevisa.com/benin-visa-update/"),
    ("Wikipedia · Vodun Days / Fête du Vodoun", "https://en.wikipedia.org/wiki/Vodun_Days"),
    ("Eco-Bénin · Possotomé y el lago Ahémé (ecoaldea, camping, circuitos en piragua)", "https://www.ecobenin.org/possotome/"),
    ("Eco-Bénin · circuitos de turismo comunitario en Benín", "https://www.ecobenin.org/le-circuit-touristique/"),
    ("Nomadays / Voyage-Bénin · Dassa-Zoumè, las 41 colinas y la gruta de Arigbo", "https://www.voyage-benin.com/guide/destination/les-collines-de-dassa-un-endroit-magnifique"),
    ("Laure Wanders · visita a Taneka-Koko (tasas, guía, estado actual del pueblo)", "https://www.laurewanders.com/taneka-koko-a-traditional-taneka-village-in-benin/"),
    ("Logistics Cluster (LCA) · paso fronterizo Ouaké (Djougou) Benín–Togo", "https://lca.logcluster.org/benin-234-togo-ouake-djougou-border-crossing"),
    ("Scoot West Africa · cruce de Sèmè/Kraké con e-Visa nigeriano", "https://scootwestafrica.com/crossing-at-seme-krake-with-an-e-visa-for-nigeria/"),
    ("Scoot West Africa · guía de visados de África Occidental", "https://scootwestafrica.com/guide-visas/"),
    ("Scoot West Africa · el festival Vodun Days", "https://scootwestafrica.com/the-vodun-days-festival-in-benin/"),
    ("tech.africa · disponibilidad de Starlink en África (2026): Benín, activo", "https://tech.africa/starlink-africa/"),
    ("ECOWAS Brown Card · esquema regional de seguro (CEDEAO)", "https://www.browncard.org/"),
    ("Embajada de España en Nigeria, Benín y CEDEAO (Abuja)", "https://www.exteriores.gob.es/Embajadas/abuja/es/Paginas/index.aspx"),
    ("iOverlander · puntos de combustible, agua y acampada verificados por la comunidad", "https://ioverlander.com/"),
    ("Tracks4Africa · cartografía y puntos overland de África", "https://tracks4africa.co.za/"),
]

# Bajada: Hillacondji -> Grand-Popo -> Ouidah -> lago Ahémé -> Route des Pêches -> Calavi/Ganvié -> Cotonú -> Porto-Novo -> Sèmè-Kraké
CORRIDOR = [(6.1667, 1.6333), (6.2833, 1.8167), (6.4500, 1.9833), (6.3467, 2.0800),
            (6.3639, 2.0856), (6.3400, 2.1700), (6.4478, 2.3556), (6.4667, 2.4167),
            (6.3703, 2.3912), (6.4969, 2.6289), (6.3697, 2.7275)]

# Subida: Ilara/Kétou -> Savè -> Dassa -> Abomey -> Savalou -> Bassila -> Djougou -> Taneka -> Ouaké
CORRIDOR_ALT = [(7.3700, 2.7300), (7.3600, 2.6000), (8.0333, 2.4833), (7.7500, 2.1833),
                (7.1786, 2.0667), (7.1833, 1.9833), (7.9333, 1.9750), (9.0167, 1.6667),
                (9.7000, 1.6667), (9.8667, 1.5000), (9.6719, 1.3637)]

CORRIDOR_LABEL = "Bajada · eje costero"
CORRIDOR_ALT_LABEL = "Subida · corredor interior"

EXPERIENCIAS = [
    "Sèmè-Kraké, el peor paso del tramo: los relatos coinciden en que es la frontera más congestionada y más agresiva de África occidental, con controles encadenados (inmigración, aduana, sanidad, policía) y una nube de intermediarios que se ofrecen a «agilizar». El consejo repetido es cruzar a primerísima hora de la mañana, llevar el e-Visa nigeriano ya emitido e impreso —NO hay visado de turismo en frontera—, tener toda la documentación del vehículo por triplicado y no aceptar ayuda de nadie que no esté detrás de una ventanilla. Quien puede, evita el paso costero y cruza por Ilara o por Igolo.",
    "El combustible «kpayo»: la gasolina de contrabando nigeriana vendida en garrafas de vidrio al borde de la carretera es omnipresente en Benín y cuesta la mitad, pero es de calidad impredecible y con frecuencia adulterada. Todos los relatos de viajeros con vehículo propio recomiendan lo mismo: repostar SOLO en estaciones de marca (Total, Oryx, MRS) de Cotonú, Bohicon, Dassa y Djougou, y llevar embudo con filtro por si acaso.",
    "Ganvié y el precio de la piragua: la queja recurrente de los visitantes es el regateo del precio de la piragua y la presión para comprar en las tiendas flotantes. Lo que funciona es cerrar el precio POR PIRAGUA (no por persona) en la oficina oficial del embarcadero de Abomey-Calavi antes de subir, acordar de antemano la duración del recorrido y llevar el dinero justo. La versión a pértiga es más lenta y más silenciosa que la motorizada, y compensa.",
    "Taneka-Koko, expectativas realistas (Laure Wanders y otros relatos recientes): la visita cuesta unos 10.000 FCFA, dura 40-45 minutos e incluye guía de la comunidad. Pero el sacerdote-curandero histórico murió en 2024 y buena parte de los habitantes se han mudado al pueblo nuevo de la carretera, volviendo solo para las ceremonias — varios viajeros describen hoy el pueblo alto como semivacío. Sigue mereciendo la pena por la arquitectura, pero conviene ir sabiéndolo.",
    "El norte, en primera persona de los informes: no hay ya relatos de overlanders recientes por Pendjari y el Parque W, y eso en sí mismo es el dato. Los análisis publicados describen el complejo WAP como zona de implantación estable del JNIM desde 2022-2023, con ataques a puestos militares y a guardas de African Parks, y con picos de letalidad en 2025 y 2026 (Point Triple, cataratas de Koudou, Koalou). African Parks ha publicado partes de incidentes sobre el Parque W. Cuando desaparecen los relatos de viajeros de una zona, la zona está cerrada de hecho aunque nadie lo haya declarado.",
    "Vodun Days: quienes han estado coinciden en que es el mejor momento del año para ver Benín —zangbeto, egungun, procesiones y tambores en la playa de Ouidah— y también el peor para encontrar alojamiento: hay que reservar con meses de antelación y asumir precios multiplicados. Si el paso por Benín cae en la primera quincena de enero, la decisión es forzar el calendario para estar ahí; si no, no merece la pena esperar semanas.",
]

HISTORIA_RESUMEN = ("Benín fue el corazón del poderoso reino de Dahomey, temido por su ejército y tristemente célebre por su papel en la trata negrera atlántica desde el «Puerto de No Retorno» de Ouidah; hoy es reconocido como uno de los grandes bastiones democráticos de África "
                     "Occidental desde su pionera transición pacífica del socialismo al multipartidismo en 1990, y sigue siendo cuna del vudú, religión que aquí tiene su origen histórico y su reconocimiento oficial. Desde 2021, sin embargo, el norte del país sufre la expansión de la insurgencia yihadista del Sahel.")

HISTORIA_SECCIONES = [
    ("El reino de Dahomey y su ejército de amazonas",
     "El reino de Dahomey, con capital en Abomey, se consolidó desde el siglo XVII como una de las potencias militares más organizadas de África Occidental, célebre por su cuerpo de guerreras —las agojie, que Europa llamó «amazonas» de Dahomey— y por un Estado centralizado que sostenía su economía en gran medida sobre la captura y venta de esclavos a comerciantes europeos en la costa. Los doce palacios reales de Abomey, Patrimonio Mundial desde 1985, conservan los bajorrelieves de barro que narran el reinado de cada soberano."),
    ("Ouidah y el «Puerto de No Retorno»",
     "La ciudad costera de Ouidah fue uno de los mayores puertos de embarque de esclavos hacia América durante los siglos XVII a XIX, un pasado hoy conmemorado en la «Ruta de los Esclavos» y su monumento del Puerto de No Retorno; Ouidah es también, junto con Abomey, uno de los grandes centros espirituales del vudú, religión reconocida oficialmente en Benín en 1996 y con festival nacional propio cada 10 de enero. Otros pueblos, como los tofinu de Ganvié o los shabè de Savè, sobrevivieron a las razias refugiándose en el agua o en las colinas."),
    ("Colonia francesa y la efímera «República Popular de Benín»",
     "Francia colonizó el territorio como Dahomey a finales del siglo XIX, integrándolo en el África Occidental Francesa; tras la independencia en 1960, el país vivió una notable inestabilidad con varios golpes de Estado hasta que el militar Mathieu Kérékou instauró en 1972 un régimen marxista-leninista de partido único, renombrando el país República Popular de Benín en 1975."),
    ("Pionero de la transición democrática africana",
     "En 1990, Benín fue pionero al organizar una «Conferencia Nacional» que condujo pacíficamente del marxismo al multipartidismo, un modelo que después inspiraría transiciones similares en otros países africanos; el propio Kérékou aceptó la derrota electoral en 1991, un hecho poco común en la época, y desde entonces el país mantiene una de las democracias más estables de la región, aunque con tensiones en torno a reformas constitucionales y a la exclusión de candidaturas opositoras."),
    ("Situación actual: la presión del Sahel sobre el norte",
     "Desde noviembre de 2021, la insurgencia yihadista que asola Burkina Faso y Níger se ha extendido a los departamentos septentrionales de Benín. El grupo JNIM, afiliado a Al Qaeda, se ha implantado en los parques nacionales de la Pendjari y W, que utiliza como santuario y base logística, y los ataques a posiciones militares se han multiplicado, con picos de letalidad en 2025 y 2026. Benín ha reforzado su ejército, creado nuevas unidades y recibido apoyo material de Francia, la UE y Estados Unidos, pero el turismo del norte —que era el activo natural del país— está de hecho suspendido."),
]

HISTORIA_FUENTES = [
    ("BBC News · Benin country profile", "https://www.bbc.com/news/world-africa-13037572"),
    ("UNESCO · Palacios reales de Abomey", "https://whc.unesco.org/en/list/323/"),
    ("Encyclopaedia Britannica · Benin, History", "https://www.britannica.com/place/Benin"),
    ("Wikipedia · Islamist insurgency in Northern Benin", "https://en.wikipedia.org/wiki/Islamist_insurgency_in_Northern_Benin"),
]

SPEC = dict(
    slug="benin", name="Benín", revision="12 sep 2026",
    sub="Corredor doble bajada (costa) / subida (interior) · documentación · seguridad · logística",
    chips=[
        ("BAJADA", "Hillacondji → Grand-Popo → Ouidah → Ganvié → Cotonú → Sèmè-Kraké · ~270 km"),
        ("SUBIDA", "Ilara/Kétou → Savè → Dassa → Abomey → Savalou → Djougou → Ouaké (Togo) · ~700 km"),
        ("PDIs", "19 puntos: 16 visitables repartidos entre los dos corredores + 3 del norte documentados como excluidos"),
        ("PENDJARI Y W", "🚫 FUERA DEL ITINERARIO 2027 — JNIM implantado en ambos parques"),
        ("A PIE", "41 colinas de Dassa · Oké Shabè (Savè) · montes Kouffé · Taneka"),
        ("4x4", "Route des Pêches (arena costera) · pistas de Kouffé y de las Collines"),
        ("VODUN DAYS", "8-10 de enero en Ouidah — puede coincidir con nuestro paso"),
        ("STARLINK", "ACTIVO en Benín (a diferencia de Togo)"),
        ("VISADO NIGERIA", "tramitar ANTES de llegar a la frontera — sin visado en frontera"),
    ],
    center=[8.0, 2.2], zoom=7,
    notice="Documento de planificación. Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada.",
    pois=POIS, logistics=LOGISTICS, corridor=CORRIDOR, corridor_alt=CORRIDOR_ALT,
    corridor_label=CORRIDOR_LABEL, corridor_alt_label=CORRIDOR_ALT_LABEL,
    historia_resumen=HISTORIA_RESUMEN, historia_secciones=HISTORIA_SECCIONES, historia_fuentes=HISTORIA_FUENTES,
    resumen_intro=("Benín se cruza DOS VECES por dos mitades distintas. En la <strong>bajada</strong>, viniendo de Togo por Hillacondji, se recorre el eje costero: Grand-Popo y la Bouche du Roy, Ouidah con la Ruta de los Esclavos y el Templo de las Pitones, "
                   "el lago Ahémé, Ganvié sobre el lago Nokoué, Cotonú y Porto-Novo, para salir a Nigeria por Sèmè-Kraké. En la <strong>subida</strong>, ya de vuelta desde Nigeria, se entra por el interior (Ilara/Kétou) y se sube por las Collines: "
                   "Savè, Dassa-Zoumè y sus 41 colinas, los Palacios Reales de Abomey (UNESCO), Savalou, los montes Kouffé, Djougou y los pueblos taneka, saliendo a Togo por Ouaké. Los dos corredores solo comparten la geografía general, ningún punto. "
                   "<strong>El gran condicionante es que el norte está cerrado</strong>: la Pendjari y el Parque W —el mejor parque de fauna de África occidental y uno de los últimos refugios del león de África occidental— son hoy santuario del JNIM y quedan fuera del itinerario. "
                   "Y una oportunidad: si el paso cae en la primera quincena de enero, coincidimos con los <strong>Vodun Days</strong> de Ouidah."),
    facts=[
        ("Ventana prevista", "Bajada: tras Togo, antes de Nigeria. Subida: tras Nigeria, antes de Togo."),
        ("Entrada bajada", "Hillacondji/Sanvee-Condji desde Togo: puesto conjunto, cruzar por la mañana."),
        ("Salida bajada", "Sèmè-Kraké hacia Nigeria: el paso más transitado de África occidental; visado nigeriano ya emitido es obligatorio."),
        ("Entrada subida", "Ilara/Kétou desde Nigeria (eje interior, mucho más tranquilo); alternativa: Igolo/Idiroko."),
        ("Salida subida", "Ouaké hacia Togo (eje Djougou-Kara), 24/7 según el Logistics Cluster; PLAN B más al sur: Azovè/Tohoun."),
        ("Visado Benín", "e-Visa obligatorio y exclusivamente electrónico a través de evisa.bj — no se emiten visados en puesto terrestre. Tarifas publicadas: 50 € (30 días, entrada única), 75 € (30 días, multientrada), 100 € (90 días, multientrada). Tramitación rápida (de 1 h a 96 h según la fuente oficial), pero pedirlo con al menos 7 días. LA MULTIENTRADA DE 90 DÍAS PUEDE CUBRIR LAS DOS PASADAS si caben en la ventana — comprobarlo contra el calendario real."),
        ("Visado Nigeria", "No existe visado de turismo en frontera — tramitar el e-Visa o el visado consular con semanas de antelación, tanto para la salida de la bajada como para la entrada de la subida."),
        ("Seguridad", "Sur y centro estables con precaución normal. DEPARTAMENTOS DE ATAKORA, ALIBORI Y BORGOU (incluidos Pendjari, W y las zonas de caza de Mékrou y Djona): «no viajar» para España, Australia, Canadá y EE. UU. La mitad norte del país está desaconsejada en bloque por el Ministerio español."),
        ("Comunicaciones", "Starlink ACTIVO en Benín — el mejor punto de conectividad de todo el tramo Ghana-Togo-Benín-Nigeria. SIM local (MTN Bénin, Moov Africa, Celtiis) como respaldo."),
        ("Fauna con el perro", "No hay ninguna opción real: los dos parques con fauna están fuera del itinerario. Lo que queda es avifauna de laguna (Bouche du Roy, lago Ahémé) y hipopótamos del Ouémé en la zona de Kouffé, todo fuera de parque nacional y por tanto compatible con el perro."),
    ],
    alerts=[
        "🚫 PENDJARI Y PARQUE W, FUERA DEL ITINERARIO. El mejor parque de África occidental cae del viaje. Desde noviembre de 2021 la insurgencia yihadista del Sahel se ha implantado en el norte de Benín y los análisis publicados describen ambos parques como santuario y base operativa del JNIM, con ataques recurrentes a militares y a guardas de African Parks y picos de letalidad en 2025 y 2026. España, Australia, Canadá y EE. UU. coinciden en «no viajar» a Atakora, Alibori y Borgou y expresamente a Pendjari y W. Con ello se pierden también Natitingou, Boukoumbé y sus tata somba, las cascadas de Tanougou y toda la cordillera de la Atacora.",
        "Mitad norte del país desaconsejada en bloque por el Ministerio español, además de los departamentos concretos. El corredor de subida de esta ficha llega hasta Djougou y Ouaké, en el departamento de la DONGA, que no está en la lista de «no viajar» pero sí dentro de esa mitad norte: es el punto de la ruta que hay que revalidar con más cuidado, y para el que existe un plan B (salir a Togo mucho más al sur, por Azovè/Tohoun).",
        "Visado de Nigeria: NO se emite en frontera para turismo, ni en Sèmè-Kraké ni en Ilara. Tramitarlo por e-Visa o consulado antes de salir de España o desde Cotonú, con margen de varias semanas, y contar con DOS trámites (salida de la bajada y entrada de la subida).",
        "Sèmè-Kraké es el paso más congestionado de África occidental: cruzar a primera hora, documentación por triplicado y cero trato con intermediarios. Para la subida se ha elegido deliberadamente un paso interior (Ilara/Kétou) para no repetirlo.",
        "Combustible «kpayo»: la gasolina de contrabando nigeriana en garrafas al borde de la carretera es barata y está en todas partes, pero es de calidad impredecible y adulterada con frecuencia. Repostar SOLO en estaciones de marca.",
        "Vodun Days (8-10 de enero, Ouidah): si el paso por Benín cae en esas fechas, es la mejor oportunidad cultural de todo el tramo, pero exige reservar alojamiento con meses de antelación. Confirmar las fechas exactas de 2027 en vodundays.bj.",
        "Ganvié: el perro no puede subir a la piragua. Plan B definido: se queda en el vehículo en el embarcadero de Abomey-Calavi con uno de los tres viajeros, y se hace la visita en dos turnos.",
    ],
    ruta_intro=("Benín se recorre por dos mitades sin solapamiento. La <strong>bajada</strong> es el eje costero y lagunar, unos 270 km de frontera a frontera con desvíos: sobre la media de <strong>250 km/día</strong> del proyecto sería una jornada, "
                "pero por densidad de contenido hay que contar <strong>5-7 días</strong>. La <strong>subida</strong> es el corredor interior completo, unos 650-700 km de Kétou a Ouaké incluyendo el desvío a Abomey: "
                "unos 3 días de conducción pura y <strong>7-9 días</strong> con las paradas. Lo que NO aparece aquí, y que en otras circunstancias sería el plato fuerte, es el bloque del norte (Pendjari, Atacora, Tanougou, W): está fuera por seguridad."),
    route_headers=("Etapa", "Recorrido", "Distancia y días aprox."),
    route_rows=[
        ("Bajada 1 · Entrada y costa del Mono", "Hillacondji → Grand-Popo → Bouche du Roy (Avlo)", "~30 km · 1-2 días"),
        ("Bajada 2 · Lago Ahémé", "Grand-Popo → Possotomé (lago Ahémé)", "~45 km · 1-2 días"),
        ("Bajada 3 · Ouidah", "Possotomé → Ouidah (Route des Esclaves, Pitones, fuerte)", "~50 km · 1-2 días · +2 si coinciden los Vodun Days"),
        ("Bajada 4 · Route des Pêches", "Ouidah → Avlékété → Fidjrossè → Abomey-Calavi", "~45 km · ½-1 día"),
        ("Bajada 5 · Ganvié", "Abomey-Calavi → Ganvié (piragua) → vuelta", "~10 km + travesía · ½ día"),
        ("Bajada 6 · Capitales", "Abomey-Calavi → Cotonú → Porto-Novo", "~55 km · 1-2 días"),
        ("Bajada 7 · Hacia Nigeria", "Porto-Novo → Sèmè-Kraké", "~30 km · ½ día + frontera"),
        ("Subida 1 · Entrada interior", "Ilara (Nigeria) → Kétou (puerta Akaba Idéna) → Savè", "~140 km · 1-2 días"),
        ("Subida 2 · Las Collines", "Savè (Oké Shabè) → Dassa-Zoumè (41 colinas, gruta de Arigbo)", "~50 km · 1-2 días"),
        ("Subida 3 · Abomey", "Dassa-Zoumè → Bohicon → Abomey (palacios UNESCO) → Bohicon", "~140 km ida y vuelta · 1-2 días"),
        ("Subida 4 · Savalou y el norte de las Collines", "Bohicon → Savalou", "~90 km · 1 día"),
        ("Subida 5 · Montes Kouffé", "Savalou → Bassila (bosque clasificado y montes Kouffé)", "~130 km · 1-2 días"),
        ("Subida 6 · Donga", "Bassila → Djougou → Taneka-Koko / Taneka-Béri", "~100 km · 1-2 días"),
        ("Subida 7 · Salida a Togo", "Djougou → Ouaké (frontera)", "~37 km · ½ día + frontera"),
        ("PLAN B de la subida", "Abomey → Azovè → Tohoun (Togo), sin subir a la Donga", "~120 km · 1 día · si el norte se complica"),
    ],
    offroad=[
        "ROUTE DES PÊCHES (Cotonú → Ouidah): el tramo de conducción más divertido del sur, unos 40 km entre el Atlántico y la laguna, históricamente pista de arena entre aldeas de pescadores y cocoteros. Está siendo asfaltada por tramos, así que el porcentaje de arena que quede en 2027 es una incógnita — confirmar sobre el terreno; si queda pista, es arena blanda de verdad y exige bajar presiones.",
        "Acceso a la Bouche du Roy (Grand-Popo → Avlo): pista de arena y tierra por el cordón litoral del Mono hasta el embarcadero de Avlo, entre manglares y salinas. Vados y arena; en crecida del Mono, tramos cortados.",
        "Pistas de las Collines (Dassa, Savè, Savalou): red de caminos de tierra roja entre los inselbergs de granito, de aldea en aldea y hasta los pies de las colinas sagradas. Sin señalización y con pasos de agua; es el mejor terreno del país para conducir por gusto y llegar a los senderos de subida.",
        "Bosque clasificado de Bassila y montes Kouffé: pistas forestales en el centro del país, con vados sobre afluentes del Ouémé y tramos que se embarran a fondo en la estación de lluvias. Guía local recomendable — no hay cartografía fiable.",
        "Subida a los pueblos taneka (Copargo): los 20 km desde Djougou terminan en una pista de piedra hasta el pie de la colina, y el pueblo alto se sube a pie. Vehículo hasta abajo, sin problema para un 4x4.",
        "ESTADO DE LAS CARRETERAS EN LLUVIAS: el sur tiene dos estaciones húmedas (abril-julio, la fuerte, y septiembre-octubre) y el norte una sola (mayo-octubre). Los ejes principales (RNIE1 costera, RNIE2 Cotonú-Parakou, RNIE3 hacia Djougou) están asfaltados y aguantan, con baches y tramos hundidos; TODAS las pistas laterales —Route des Pêches, Kouffé, Collines, Avlo— se degradan mucho en el pico de lluvias, y las de la zona lagunar del sur pueden quedar anegadas. La ventana buena es de noviembre a febrero, que además es cuando caen los Vodun Days.",
        "Tráfico: los zémidjan (mototaxis) de Cotonú y los camiones del corredor de Nigeria son el verdadero peligro de conducción del país, no el terreno. Evitar conducir de noche entre ciudades, según recomienda expresamente el Ministerio español.",
    ],
    senderismo=[
        "LAS 41 COLINAS DE DASSA-ZOUMÈ: la mejor caminata accesible del corredor. Subidas cortas y medias por los domos de granito con guía local autorizado (son lugares sagrados del vudú, no se entra por libre), incluida la PIEDRA HENDIDA DE OKÈYTÉ, a 20 minutos de sendero, con panorámica de 360° sobre el valle. Se combina con la gruta de Notre-Dame d'Arigbo.",
        "Oké Shabè (Savè): subida de un par de horas a la colina-refugio de la Ruta del Esclavo, con cuevas y estructuras defensivas en lo alto y vistas sobre la llanura del Ouémé. Guía local de Savè.",
        "Colina sagrada de Savalou y recorrido del reino: caminata corta hasta el punto alto de la ciudad, combinada con la visita al palacio real.",
        "Montes Kouffé y bosque de Bassila: caminatas a medida con guías locales por bosque seco y de galería, con babuinos y buena avifauna; sin senderos señalizados ni infraestructura — hay que concertarlo en Bassila.",
        "Pueblos taneka (Copargo): recorrido a pie por la ladera entre las cabañas cónicas de Taneka-Koko y Taneka-Béri, unos 45 minutos con guía de la comunidad. Piedra suelta y desnivel corto pero incómodo.",
        "Bouche du Roy (Grand-Popo): recorrido a pie y en piragua por el delta del Mono, entre manglares y bancos de arena, con observación de aves acuáticas y, en temporada (noviembre-marzo), de nidos de tortuga.",
        "🚫 LO QUE SE PIERDE: la cordillera de la ATACORA —el único relieve serio del país, con el monte Sokbaro (658 m), las aldeas somba y los tres saltos escalonados de las CASCADAS DE TANOUGOU con sus pozas de baño— es, de largo, la mejor zona de senderismo de Benín, y está fuera del itinerario por seguridad.",
    ],
    acampada=[
        "Grand-Popo y la costa del Mono: varios alojamientos de playa con jardín y aparcamiento que admiten acampada o pernocta en vehículo; la mejor zona del país para parar dos días con el perro.",
        "Possotomé (lago Ahémé): albergue comunitario de Eco-Bénin con capacidad para 25 personas, bar-restaurante y CAMPING a orillas del lago — la pernocta organizada más cómoda del corredor de bajada.",
        "Ouidah: pequeños hoteles con patio cerrado cerca del centro histórico y algunos alojamientos de playa en la zona de la Puerta del No Retorno. En Vodun Days, todo lleno con meses de antelación.",
        "Cotonú y Porto-Novo: hoteles con parking vigilado; en la capital económica la acampada libre no es opción.",
        "Abomey/Bohicon, Dassa-Zoumè, Savalou, Djougou: hoteles sencillos con aparcamiento en cada etapa del corredor interior.",
        "Acampada libre: posible en el interior con permiso del jefe de la aldea, como en el resto de África occidental, pero NO al norte de Djougou ni en ninguna zona del norte, y evitando las playas de Cotonú (expresamente desaconsejadas de día y de noche por el Ministerio español).",
    ],
    visado=[
        "e-Visa beninés OBLIGATORIO y exclusivamente electrónico a través del portal oficial evisa.bj: Benín no emite visados en ningún puesto fronterizo terrestre.",
        "Tarifas publicadas: 50 € (30 días, entrada única), 75 € (30 días, entrada múltiple), 100 € (90 días, entrada múltiple). Tramitación de 1 h a 96 h según la fuente oficial; pedirlo con al menos 7 días de margen.",
        "COMPROBAR SI LA MULTIENTRADA DE 90 DÍAS CUBRE LAS DOS PASADAS: si entre la bajada y la subida pasan menos de 90 días, un solo e-Visa de 100 € resuelve el país entero. Si pasan más, hacen falta dos trámites.",
        "Pasaporte con validez mínima de 6 meses y páginas en blanco.",
        "Certificado internacional de fiebre amarilla OBLIGATORIO para todos los mayores de 1 año, y se exige de verdad.",
        "Visado nigeriano: imprescindible antes de llegar a Sèmè-Kraké (bajada) y de nuevo para la entrada de la subida. El visa on arrival nigeriano está limitado a negocios con invitación y no aplica a overlanders.",
    ],
    fronteras_rows=[
        ("Entrada bajada", "Hillacondji/Sanvee-Condji (Togo)", "Puesto conjunto (yuxtapuesto); cruzar por la mañana, el tráfico comercial satura el mediodía."),
        ("Salida bajada", "Sèmè-Kraké (Nigeria)", "El paso más transitado de África occidental; congestión y controles múltiples; visado nigeriano ya emitido, documentación por triplicado, cruzar a primera hora."),
        ("Entrada subida", "Ilara/Kétou (Nigeria)", "Paso interior mucho más tranquilo, elegido para no repetir Sèmè-Kraké. Coordenada aproximada: verificar posición, horario y admisión de vehículo extranjero."),
        ("Alternativa entrada subida", "Igolo/Idiroko (Nigeria)", "Segundo paso más transitado con Nigeria, al norte de Porto-Novo; más ágil que Sèmè-Kraké pero concurrido."),
        ("Salida subida", "Ouaké (Togo, eje Djougou-Kara)", "24/7 salvo festivos beninenses según el Logistics Cluster; exige seguro CEDEAO y laissez-passer. Está en la Donga: revalidar seguridad antes de usarlo."),
        ("PLAN B salida subida", "Azovè/Tohoun (Togo, eje central)", "Muy al sur y fuera de toda zona de riesgo; acorta el corredor interior pero lo pone a salvo."),
    ],
    vehiculos=[
        "CPD con todos los pares de sellos en regla; sin carnet, contar con un laissez-passer de importación temporal, como en los países vecinos — pedirlo expresamente al entrar y conservarlo hasta la salida.",
        "Carte Brune CEDEAO como seguro de responsabilidad civil regional: Benín es Estado miembro del esquema y el seguro se exige expresamente en los pasos de Ouaké y Kraké.",
        "Carnet de conducir internacional obligatorio en todos los controles.",
        "Documentación del vehículo en copias adicionales para Sèmè-Kraké, el control documental más exhaustivo del tramo.",
        "Repostar solo en estaciones de marca: el combustible de garrafa («kpayo») es contrabando nigeriano de calidad impredecible.",
        "No conducir de noche entre ciudades: es la recomendación explícita del Ministerio español para Benín.",
    ],
    drones_callout=DRONE_CALLOUT,
    drones=[
        "Solicitar autorización previa por escrito a la ANAC-Bénin antes de intentar introducir el dron en el país.",
        "No volar en la zona de Pendjari y W ni en ningún punto al norte de Parakou o Djougou: hay operación militar activa y el dron se interpretará como reconocimiento hostil.",
        "No volar cerca de Sèmè-Kraké, del puerto de Cotonú ni de instalaciones militares, tampoco con autorización genérica.",
    ],
    starlink_callout=STARLINK_CALLOUT,
    starlink=[
        "Benín figura como mercado Starlink ACTIVO en los recuentos de septiembre de 2026 — es el mejor punto de conectividad de todo el tramo Ghana-Togo-Benín-Nigeria, y conviene aprovecharlo para descargas pesadas, copias de seguridad y trámites.",
        "Sin tarifa publicada específica para Benín: la horquilla regional es de 30-55 USD/mes de servicio y 200-390 USD de equipo. Confirmar precio, modalidad (fija o roaming) y cobertura real 30-60 días antes.",
        "SIM local (MTN Bénin, Moov Africa, Celtiis) como respaldo; buena cobertura en el eje costero y en la RNIE2, más floja en las pistas de las Collines y de Kouffé.",
    ],
    perro_intro=[
        "Certificado veterinario internacional reciente (<10 días) y vacuna antirrábica en vigor, exigibles en el control fronterizo. Documentación en francés.",
        "Régimen francófono típico: conviene que la antirrábica tenga menos de 12 meses, no solo que esté «en vigor».",
        "El dosier del proyecto marca Benín como [SIN CONFIRMAR] en cuanto a permiso de importación previo. A quién escribir: Direction de l'Élevage, Cotonú. Al cruzarse el país DOS VECES, contar con dos trámites separados salvo confirmación escrita en contra.",
        "Cotonú es el mejor punto veterinario del tramo entre Accra y Lagos: hay clínicas privadas de nivel razonable. Aprovecharlo para revisiones, desparasitación y renovación de antiparasitarios.",
        "Sin requisitos adicionales específicos identificados más allá de los comunes del proyecto (microchip, pasaporte UE, titulación de anticuerpos ya obtenida antes de salir de la UE).",
    ],
    dog_matrix=DOG_MATRIX,
    salud=[
        "Fiebre amarilla: certificado internacional OBLIGATORIO para todos los mayores de 1 año, y se exige en frontera.",
        "Malaria: riesgo alto en todo el territorio y todo el año — profilaxis antipalúdica recomendada expresamente por el Ministerio español.",
        "Vacunas adicionales recomendadas: hepatitis A y B, tétanos, fiebre tifoidea y meningitis.",
        "FIEBRE DE LASSA: se han notificado casos en Benín. Evitar el contacto con roedores y con alimentos expuestos en mercados, y no dormir a nivel del suelo en zonas rurales sin protección.",
        "Agua: no beber de la red en ningún punto del país. Embotellada o tratada siempre.",
        "CNHU-HKM y las clínicas privadas de Cotonú son la única referencia sanitaria seria del corredor; seguro con evacuación médica imprescindible.",
        "Costa con resaca fuerte: el Ministerio español desaconseja expresamente las playas de Cotonú, de día y de noche.",
    ],
    seguridad_intro=("Benín se parte en dos con la misma nitidez que Togo. El sur y el centro —Cotonú, Porto-Novo, Ouidah, Grand-Popo, Abomey, Dassa, Savalou, Parakou— son estables, con precaución normal y delincuencia común de oportunidad. "
                     "El NORTE no: desde noviembre de 2021 la insurgencia yihadista del Sahel se ha implantado en los departamentos de ATAKORA, ALIBORI y BORGOU, y los análisis publicados describen los parques nacionales de la PENDJARI y W como santuario y base operativa del JNIM, "
                     "con ataques recurrentes a posiciones militares y a guardas de African Parks y picos de letalidad en 2025 y 2026. España desaconseja la mitad norte del país en bloque; Australia, Canadá y EE. UU. marcan «no viajar» a esos tres departamentos y expresamente a Pendjari y W. "
                     "Por eso el corredor de subida de esta ficha se detiene en Djougou y sale a Togo por Ouaké, y por eso existe un plan B todavía más al sur."),
    seguridad=[
        "🚫 DEPARTAMENTOS DE ATAKORA, ALIBORI Y BORGOU, PARQUES DE PENDJARI Y W, Y ZONAS DE CAZA DE MÉKROU Y DJONA: «no viajar». Excluidos del itinerario en cualquier escenario. Esto elimina también Natitingou, Boukoumbé, Tanguiéta y las cascadas de Tanougou.",
        "Frontera con Nigeria dentro de Alibori y Borgou: «no viajar». La única frontera nigeriana utilizable es la del sur (Sèmè-Kraké, Ilara/Kétou, Igolo), y aun ahí los avisos piden reconsiderar el viaje.",
        "Departamento de la DONGA (Djougou, Copargo/Taneka, Bassila, Ouaké): no está en la lista de «no viajar», pero sí dentro de la mitad norte desaconsejada en bloque por España. Es el tramo de la ruta que hay que revalidar con más cuidado a 30 días vista; si empeora, usar el plan B de Azovè/Tohoun.",
        "Kalalé (Borgou) y el eje hacia Níger: excluidos.",
        "No conducir de noche entre ciudades en ningún punto del país: recomendación explícita del Ministerio español, tanto por asaltos en carretera como por el estado del tráfico.",
        "Playas de Cotonú: desaconsejadas de día y de noche por robos; no dejar el vehículo aparcado con material a la vista.",
        "Sèmè-Kraké: preparar toda la documentación antes de llegar; es el control más exhaustivo y el entorno con más presión de intermediarios de todo el tramo.",
        "Manifestaciones y periodos electorales: evitar concentraciones; Benín ha tenido tensiones en torno a la exclusión de candidaturas opositoras.",
        "Llevar siempre el certificado de fiebre amarilla, el e-Visa impreso y copias de la documentación del vehículo.",
    ],
    agua=[
        "Cotonú, Ouidah, Porto-Novo, Abomey/Bohicon, Dassa y Djougou: agua embotellada en supermercados y tiendas sin problema de suministro.",
        "Recarga de depósito de uso general (ducha, aseo, limpieza): estaciones de servicio de Cotonú y hoteles con aparcamiento de Ouidah, Bohicon, Dassa y Djougou permiten llenar el depósito con manguera; confirmar en recepción.",
        "Possotomé (lago Ahémé): albergue y camping comunitario de Eco-Bénin con agua corriente, y fuentes de agua mineral explotadas desde 1952 en el propio pueblo — el mejor punto de recarga del corredor costero.",
        "Nunca beber de la red pública ni de pozos sin tratar en ningún punto del país.",
    ],
    combustible=[
        "Bajada: sin ningún riesgo de gap — Hillacondji → Grand-Popo (~10 km) → Possotomé (~45 km) → Ouidah (~50 km) → Cotonú (~40 km) → Porto-Novo (~35 km) → Sèmè-Kraké (~30 km), todos con estaciones formales. Repostar a fondo en Cotonú.",
        "Subida: tampoco hay gap de 500 km — Ilara/Kétou → Savè (~140 km) → Dassa (~50 km) → Bohicon/Abomey (~70 km) → Savalou (~90 km) → Bassila (~130 km) → Djougou (~80 km) → Ouaké (~37 km). Los tramos más largos sin nada son Kétou-Savè y Savalou-Bassila.",
        "Los desvíos SÍ exigen autonomía propia: montes Kouffé, pistas de las Collines y Bouche du Roy no tienen oferta fiable. Salir con el depósito lleno desde Bohicon, Dassa o Djougou según el tramo.",
        "NO usar el combustible «kpayo» de garrafa que se vende al borde de la carretera en todo el país: es contrabando nigeriano, barato y de calidad impredecible, con frecuencia adulterado. Solo estaciones de marca (Total, Oryx, MRS, Petro Ivoire).",
    ],
    experiencias_intro="Relatos y comentarios reales de otros overlanders y viajeros sobre Benín, para contrastar con el contenido oficial de esta ficha:",
    experiencias=EXPERIENCIAS,
    pendientes=[
        ("Pendjari y Parque W · ¿algún escenario de reapertura?", "DECISIÓN YA TOMADA: fuera del itinerario. Reevaluar solo si a 60 días vista los avisos de España y Francia levantasen el «no viajar» sobre Atakora y Alibori, cosa hoy improbable. Contactar con African Parks igualmente para conocer el estado operativo del parque"),
        ("Corredor de subida · ¿Donga o plan B?", "Decidir a 30 días vista entre subir hasta Djougou/Ouaké (más contenido: Bassila, Taneka, y enlaza con Kara en Togo) o cortar por Azovè/Tohoun (más seguro, pero se pierden tres etapas y obliga a replantear el corredor togolés)"),
        ("e-Visa de 90 días multientrada", "Comprobar contra el calendario real si entre la bajada y la subida pasan menos de 90 días: si es así, un solo e-Visa de 100 € cubre el país entero"),
        ("Visado de Nigeria ×2", "Tramitar con semanas de antelación los DOS visados nigerianos (salida de la bajada por Kraké, entrada de la subida por Ilara). Condiciona todo el tramo"),
        ("Frontera de Ilara/Kétou", "Verificar coordenada exacta, horario y si admite vehículo extranjero con carnet; si no, usar Igolo/Idiroko"),
        ("Frontera de Azovè/Tohoun", "Verificar coordenada, horario y viabilidad con vehículo propio como plan B de salida a Togo"),
        ("Vodun Days 2027", "Confirmar fechas exactas en vodundays.bj y decidir si se fuerza el calendario para coincidir; si sí, reservar alojamiento en Ouidah con meses de antelación"),
        ("Perro · permiso de importación", "Escribir a la Direction de l'Élevage de Cotonú: ¿hace falta permiso previo?, ¿vale uno para las dos entradas?"),
        ("Route des Pêches", "Confirmar cuánto queda de pista de arena tras las obras de asfaltado: es el único tramo 4x4 real del sur del país"),
        ("Taneka-Koko", "Confirmar qué se visita realmente hoy: el sacerdote histórico murió en 2024 y buena parte del pueblo alto está deshabitado"),
        ("Montes Kouffé", "Confirmar en Bassila si hay guías y qué caminatas son realmente practicables; no hay información publicada fiable"),
        ("Starlink en Benín", "Confirmar tarifa, modalidad (fija o roaming regional) y cobertura real antes de contar con él"),
        ("Dron", "Contactar con la ANAC-Bénin o descartar el vuelo en el país"),
        ("Fotos pendientes de sustituir", "Porto-Novo, Savè, Dassa, Bassila, Djougou, Taneka, Pendjari y W usan imágenes de referencia de su región o del país, no del propio sitio: sustituir por fotos propias cuando las tengamos"),
        ("Coordenadas aproximadas", "Fronteras de Ilara/Kétou, Igolo y Azovè, y los centroides de Pendjari, Tanougou y W están fijados con coordenada aproximada: afinarlas con cartografía Tracks4Africa"),
    ],
    sources=SOURCES,
    sources_note="Última revisión de esta versión: 12 de septiembre de 2026. Esta ficha es una herramienta de planificación, no una autorización de entrada ni una guía de navegación. La situación de seguridad del norte de Benín es dinámica y ha empeorado de forma sostenida desde 2021: revalidarla obligatoriamente antes de cada entrada.",
    emergency="Policía 117 · Bomberos/Ambulancia 118 · Consulado Honorario de España en Cotonú: +229 21 339 219 · Emergencia consular (Consulado General en Lagos): +234 80 3360 1658.",
)


def get_data(root="../../"):
    return make_ficha(SPEC)

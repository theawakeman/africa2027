# -*- coding: utf-8 -*-
# Datos de contacto de los organismos que emiten el permiso de importacion
# de animales de compania (perro) - ruta overland Africa Centro/Golfo de Guinea 2027.
# Paises: Ghana, Togo, Benin, Nigeria, Camerun, Gabon, Congo-Brazzaville, RD Congo, Angola.
#
# METODO Y CONVENCIONES:
#   - "url_verificada": True SOLO si la URL se ha abierto en esta investigacion y su
#     contenido trata realmente del permiso o de los requisitos de importacion de perros.
#     False = no se ha podido abrir (robots.txt, error de servidor, certificado TLS roto)
#     aunque la pagina aparezca indexada en buscadores.
#   - "url_generica": True si lo unico enlazable es una portada o pagina de contacto,
#     no la pagina del tramite.
#   - Campo sin fuente = None, siempre explicado en "nota".
#   - Las fuentes comerciales (pettravel.com, anivetvoyage.com) se han usado SOLO como
#     ultimo recurso, y van marcadas expresamente como tales en la "nota".
#
# AVISO TRANSVERSAL SOBRE cert_dias:
#   Varios paises (Ghana, Nigeria, Camerun, Congo) solo tienen cifra publicada en el
#   modelo de certificado de la USDA-APHIS, que dice literalmente "This certificate is
#   valid for 30 days after issuance". Ese 30 es la validez DEL FORMULARIO ESTADOUNIDENSE
#   (identica en los cuatro paises, es texto de plantilla), NO un plazo publicado por el
#   pais de destino. Saliendo de Espana el documento sera un certificado zoosanitario
#   espanol y el plazo real puede ser mas corto: confirmar por escrito antes de viajar.
DATOS = {
    "ghana": {
        "organismo": "Veterinary Services Department (VSD), Ministry of Food and Agriculture (MoFA)",
        "url": "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ghana",
        "url_generica": False,
        "url_verificada": True,
        "email": "vsd@mofa.gov.gh",
        "tel": "+233 24 264 9497",
        "cert": True,
        "cert_dias": 30,
        "cert_quien": "Veterinario oficial del pais de salida ('International Health Certificate'; desde EEUU lo emite veterinario acreditado y lo refrenda APHIS, que acepta refrendo digital)",
        "nota": (
            "OJO AL NOMBRE: el organismo existe y su sitio oficial es vsd.gov.gh, pero se llama a si "
            "mismo 'Veterinary Services Department', no 'Directorate'. La portada vsd.gov.gh SI se ha "
            "abierto y verificado, y de ahi salen el email (vsd@mofa.gov.gh), la direccion postal "
            "(P.O. Box M161, Accra) y el telefono que se da aqui, que es la linea de emergencia "
            "publicada (0242649497). El otro numero de la portada aparece como '(233) 030-1234567', "
            "que es evidentemente un numero de relleno: NO usarlo. "
            "LA PAGINA DEL TRAMITE NO SIRVE: la portada enlaza 'Import Requirements' en "
            "https://vsd.gov.gh/255-2/, pero esa URL devuelve error de servidor en TRES intentos "
            "distintos, asi que no se ha podido verificar y no se da como 'url'. El sitio tampoco "
            "tiene pagina dedicada a mascotas, solo 'Import Requirements'/'Export Requirements' "
            "genericos. Por eso la 'url' que se da es la ficha de USDA-APHIS, que SI se ha abierto y "
            "SI trata de perros y gatos hacia Ghana. "
            "cert_dias=30 sale del modelo APHIS (ver aviso transversal de cabecera). "
            "DATO UTIL DE FUENTE COMERCIAL (pettravel.com, marcada como tal, abierta y verificada): "
            "en Ghana SI hace falta permiso de importacion incluso para mascota personal, se pide "
            "despues de las analiticas y el permiso vale 8 semanas; vacuna antirrabica entre 30 dias "
            "y 6 meses antes de entrar; microchip ISO 11784/11785. NO CONFIRMADO POR EL VSD. "
            "PROCEDIMIENTO (wikiprocedure, fuente terciaria NO oficial, verificada): formulario en la "
            "oficina del VSD (Government Animal Clinic, Okodan Rd, Accra), solicitud por escrito con "
            "al menos 7 dias de antelacion, aviso al puesto de entrada 3 dias antes, y cuarentena "
            "teorica de 21-30 dias. Telefonos de MoFA citados alli: +233 21 662961 / 663036 / 662810. "
            "La cuarentena es el riesgo serio a aclarar por escrito ANTES de salir."
        ),
        "fuentes": [
            "https://vsd.gov.gh/",
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ghana",
            "https://www.aphis.usda.gov/sites/default/files/ghana-dog-cat.pdf",
            "https://www.pettravel.com/information/pet-passports/ghana-pet-import-requirements/",
            "https://www.wikiprocedure.com/index.php/Ghana_-_Apply_for_Live_Animal_and_Animal_Products_Import",
        ],
    },
    "togo": {
        "organismo": "Ministère de l'Agriculture, de la Production Animale (Ressources Animales) et de la Souveraineté Alimentaire (MAPRASA) - servicios veterinarios / Direction de l'Élevage",
        "url": "https://www.pettravel.com/information/pet-passports/togo-pet-import-requirements/",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": None,
        "cert": True,
        "cert_dias": 3,
        "cert_quien": "Veterinario oficial del pais de salida, o veterinario habilitado con refrendo de veterinario oficial",
        "nota": (
            "URL DE FUENTE COMERCIAL, MARCADA COMO TAL (pettravel.com): es el ULTIMO RECURSO porque "
            "NO EXISTE ninguna pagina oficial togolesa localizable sobre importacion de animales de "
            "compania. Se ha abierto y verificado que trata del tema. "
            "NOMBRE DEL MINISTERIO SI VERIFICADO en fuente oficial: la ficha de USDA-APHIS 'Export "
            "Live Animals to Togo' (abierta y verificada) cita expresamente al 'Ministry of "
            "Agriculture, Fisheries Animal resources and Food Sovereignty (MAPRASA) of the Togolese "
            "Republic' como la autoridad que acepta los certificados; pero esa ficha va de ganado y "
            "aves, NO de mascotas, por eso no se usa como 'url'. "
            "APHIS NO tiene ficha de mascotas de Togo: .../pet-travel-us-togo da 404 comprobado. "
            "No se ha encontrado email ni telefono del servicio veterinario togoles. "
            "PERMISO DE IMPORTACION - PUNTO CRITICO PARA ESTA RUTA: pettravel dice que SI hace falta "
            "permiso salvo que se entre desde una lista cerrada de paises que incluye Benin, Burkina, "
            "Costa de Marfil, Camerun, Gabon, los dos Congos, Mali, Niger, Senegal y FRANCIA, pero "
            "NO incluye ESPANA ni GHANA. Es decir: entrando a Togo desde Ghana, que es lo que hara "
            "este viaje, segun esta fuente HARIA FALTA PERMISO. Dato no confirmado oficialmente pero "
            "demasiado importante para ignorarlo: preguntar por escrito. "
            "cert_dias=3 lo dan DOS fuentes comerciales independientes que coinciden (pettravel: "
            "'within 3 days of entry'; anivetvoyage: emitido como maximo 3 dias antes de la llegada). "
            "Vacuna antirrabica: al menos 21 dias antes (pettravel) / entre 21 dias y 12 meses "
            "(anivetvoyage). Microchip recomendado, no exigido segun pettravel."
        ),
        "fuentes": [
            "https://www.aphis.usda.gov/live-animal-export/export-live-animals-togo",
            "https://www.pettravel.com/information/pet-passports/togo-pet-import-requirements/",
            "https://www.anivetvoyage.com/formalites-pays/t/174-togo.html",
        ],
    },
    "benin": {
        "organismo": "Direction de l'Élevage (DE), Ministère de l'Agriculture, de l'Élevage et de la Pêche (MAEP)",
        "url": "https://catis.xroad.bj/publicservices/PS00501",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": None,
        "cert": True,
        "cert_dias": 10,
        "cert_quien": "Veterinario oficial del pais de salida; en Benin el certificado sanitario internacional lo expide la Direction de l'Élevage",
        "nota": (
            "EL MEJOR RESULTADO OFICIAL DE TODA LA LISTA JUNTO CON ANGOLA. La URL es el catalogo "
            "oficial de servicios publicos del Gobierno de Benin (CatIS, catis.xroad.bj), abierto y "
            "verificado, y el servicio PS00501 se titula literalmente 'Controle sanitaire et "
            "delivrance des certificats sanitaires internationaux a l'importation et a l'exportation "
            "des animaux vivants' y su descripcion incluye EXPRESAMENTE 'animaux de compagnie'. Es "
            "exactamente el tramite que se busca, nombrado por el propio Estado benines. "
            "ORGANISMO: lo presta la Direction de l'Elevage, del MAEP (ficha de institucion verificada "
            "en https://catis.xroad.bj/institutions/IN00173). "
            "BASE LEGAL citada en la ficha: Arrete N.045/MAEP/MEF/MDGLAAT/D-CAB/SGM/DRH/DRFM/DE/SA de "
            "15 de febrero de 2008, sobre tasas de los servicios veterinarios. "
            "DIRECCION FISICA VERIFICADA de la Direction de l'Elevage: Cotonou, Akpakpa, apres ancien "
            "pont, domaine avant Societe 'la Roche'. Horario 8:00-12:30 y 14:00-17:30, lunes a viernes. "
            "LO QUE NO HAY: ni la ficha del servicio ni la de la institucion publican email ni "
            "telefono, por eso ambos van a None. Los unicos correos que aparecen en CatIS "
            "(info@ega.ee, info@upmind.ee) son de los administradores estonios de la plataforma, NO "
            "de Benin: no escribir ahi. Hay que presentarse o llamar por otra via. "
            "cert_dias=10 procede de fuente COMERCIAL (anivetvoyage, marcada, verificada): certificado "
            "valido diez dias desde su emision, y emitido menos de 72 h antes de la llegada; vacuna "
            "antirrabica de mas de 1 mes y menos de 1 ano. NO confirmado por el MAEP."
        ),
        "fuentes": [
            "https://catis.xroad.bj/publicservices/PS00501",
            "https://catis.xroad.bj/institutions/IN00173",
            "https://anivetvoyage.com/pays/benin/",
        ],
    },
    "nigeria": {
        "organismo": "Federal Department of Veterinary and Pest Control Services (FDVPCS) - Chief Veterinary Officer of Nigeria (CVO), Federal Ministry of Agriculture. La Nigeria Agricultural Quarantine Service (NAQS) NO emite el permiso: inspecciona y pone en cuarentena a la llegada",
        "url": "https://naqs.gov.ng/animal/",
        "url_generica": False,
        "url_verificada": True,
        "email": "contact@naqs.gov.ng",
        "tel": "+234 807 777 8943",
        "cert": True,
        "cert_dias": 30,
        "cert_quien": "Veterinario oficial del pais de salida ('Sanitary/Health certificate'); desde EEUU, veterinario acreditado MAS refrendo de APHIS en TINTA ORIGINAL y con sello en relieve",
        "nota": (
            "CORRECCION IMPORTANTE AL PLANTEAMIENTO DE PARTIDA: el permiso de importacion NO lo emite "
            "NAQS. El SOP oficial de la propia NAQS (PDF abierto y verificado) dice literalmente "
            "'Apply for import permit to the chief Veterinary Officer (CVO), Federal Department of "
            "Veterinary and Pest Control Services', con direccion en el Federal Ministry of "
            "Agriculture, Area 11, Abuja. NAQS es quien inspecciona en el puesto fronterizo y quien "
            "manda los animales vivos a estacion de cuarentena para observacion. HAY QUE HACER LAS DOS "
            "COSAS: pedir el permiso al CVO y notificar a NAQS. "
            "URL VERIFICADA: naqs.gov.ng/animal/ se ha abierto y trata de cuarentena animal citando "
            "expresamente perros ('including dogs, cattle, cats, horses...'). Es la pagina del "
            "departamento competente, no un formulario de permiso. "
            "CONTACTOS VERIFICADOS EN ESA PAGINA: contact@naqs.gov.ng, info@naqs.gov.ng, "
            "+234 8077778943, +234 8091333385; jefe de departamento Dr. Emeka Asiegbu "
            "(emeka.asiegbu@naqs.gov.ng, hod.aq@naqs.gov.ng); Plot 81, Ralph Shodeinde Street, "
            "Central Business District, Abuja. "
            "NO se ha localizado email ni telefono directos del CVO/FDVPCS, que es a quien hay que "
            "dirigir formalmente la solicitud: usar NAQS como puerta de entrada y pedir que la "
            "deriven. "
            "cert_dias=30 sale del modelo APHIS (ver aviso transversal de cabecera). "
            "REQUISITOS VERIFICADOS en el certificado APHIS de Nigeria: MICROCHIP OBLIGATORIO ('All "
            "pets (dogs and/or cats) must be microchipped') y vacuna antirrabica con vacuna inactivada "
            "dentro del ano anterior a la fecha de salida. ATENCION: Nigeria es de los pocos que NO "
            "acepta refrendo digital, exige tinta original y sello en relieve."
        ),
        "fuentes": [
            "https://naqs.gov.ng/animal/",
            "https://naqs.gov.ng/wp-content/uploads/2020/07/NAQS_SOP.pdf",
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-nigeria",
            "https://www.aphis.usda.gov/sites/default/files/nigeria-dog-cat.pdf",
        ],
    },
    "camerun": {
        "organismo": "Ministère de l'Élevage, des Pêches et des Industries Animales (MINEPIA) - Direction des Services Vétérinaires",
        "url": "https://www.aphis.usda.gov/pet-travel/pet-travel-united-states-cameroon",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": None,
        "cert": True,
        "cert_dias": 30,
        "cert_quien": "Veterinario oficial del pais de salida (desde EEUU, veterinario acreditado MAS refrendo de APHIS en tinta original y con sello en relieve)",
        "nota": (
            "MINEPIA es el ministerio competente, confirmado por el nombre y por la existencia en su "
            "web de una ficha de tramite titulada 'OBTENTION D'UNE AUTORISATION D'IMPORTATION DES "
            "POUSSINS D'UN JOUR, DES OEUFS A COUVER, DES ANIMAUX D'ELEVAGE ET DE COMPAGNIE' en "
            "minepia.cm/site/services/productions-et-industries-animales/obtention-dune-autorisation-"
            "dimportation-des-poussins-dun-jour-des-oeufs-a-couver-des-animaux-delevage-et-de-compagnie/ "
            "Por el titulo es EXACTAMENTE el tramite buscado (dice 'animaux de compagnie'), pero NO SE "
            "HA PODIDO ABRIR NI VERIFICAR: el dominio minepia.cm tiene la cadena de certificado TLS "
            "rota y bloquea el acceso automatico, en cuatro intentos y por tres rutas distintas "
            "(pagina del tramite, /site/contact/ y www.minepia.cm). Por eso NO se da como 'url' y no "
            "hay email ni telefono: MERECE LA PENA ABRIRLA A MANO EN UN NAVEGADOR, es previsiblemente "
            "la mejor fuente para Camerun. "
            "La 'url' que se da es la ficha de USDA-APHIS de Camerun, abierta y verificada, con "
            "certificado veterinario descargable para perros y gatos. OJO: esta en el patron de URL "
            "ANTIGUO (/pet-travel/pet-travel-united-states-cameroon); el patron nuevo "
            "(/pet-travel/us-to-another-country-export/pet-travel-us-cameroon) da 404. "
            "cert_dias=30 sale del modelo APHIS (ver aviso transversal de cabecera). El certificado "
            "verificado exige verificacion de microchip. "
            "DATO DE FUENTE COMERCIAL (pettravel.com, marcada, verificada): afirma que NO hace falta "
            "permiso de importacion para mascota personal que viaja con su dueno, y que la vacuna "
            "antirrabica debe tener al menos 30 dias y no mas de 12 meses, con animal mayor de 3 "
            "meses. CONTRADICE la existencia del tramite de MINEPIA: no fiarse, preguntar."
        ),
        "fuentes": [
            "https://www.aphis.usda.gov/pet-travel/pet-travel-united-states-cameroon",
            "https://www.aphis.usda.gov/sites/default/files/cameroon-dog-cat.pdf",
            "https://minepia.cm/site/services/productions-et-industries-animales/obtention-dune-autorisation-dimportation-des-poussins-dun-jour-des-oeufs-a-couver-des-animaux-delevage-et-de-compagnie/",
            "https://www.pettravel.com/information/pet-passports/cameroon-pet-import-requirements/",
        ],
    },
    "gabon": {
        "organismo": "Direction Générale de l'Élevage, Ministère de l'Agriculture et de l'Alimentation",
        "url": "https://www.pettravel.com/information/pet-passports/gabon-pet-import-requirements/",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": None,
        "cert": True,
        "cert_dias": 10,
        "cert_quien": "Veterinario habilitado del pais de salida (certificat sanitaire international)",
        "nota": (
            "EL PAIS CON MENOS RESPALDO OFICIAL DE LOS NUEVE, junto con Togo. "
            "URL DE FUENTE COMERCIAL, MARCADA COMO TAL (pettravel.com), usada como ultimo recurso: se "
            "ha abierto y verificado que trata de los requisitos de entrada de perros a Gabon. "
            "ORGANISMO IDENTIFICADO PERO NO VERIFICADO: existe agriculture.gouv.ga con una pagina de "
            "la Direction Generale de l'Elevage en "
            "www.agriculture.gouv.ga/8-ministere/2-autres-contenus-ministere/10-directions-generales/"
            "14-direction-generale-de-l-elevage/ , pero el dominio hace timeout y bloquea el acceso "
            "automatico, asi que no se ha podido abrir ni sacar de ahi nombre del director, email ni "
            "telefono. Merece la pena intentarlo a mano. "
            "APHIS NO tiene ficha de Gabon en NINGUNO de sus dos patrones de URL (404 comprobado en "
            "ambos), asi que no hay respaldo estadounidense tampoco. "
            "REQUISITOS SEGUN LAS DOS FUENTES COMERCIALES (coinciden en lo esencial): pettravel dice "
            "que NO hace falta permiso de importacion para mascota personal y que el certificado "
            "sanitario se emite dentro de los 10 dias previos al transporte, con vacuna antirrabica "
            "entre 30 dias y 12 meses antes y microchip recomendado pero no obligatorio; anivetvoyage "
            "endurece el plazo a 72 horas antes de la llegada y exige microchip y pasaporte, con "
            "vacuna de mas de 30 dias y menos de un ano. ANTE LA DISCREPANCIA 10 DIAS / 72 HORAS, "
            "ir a lo seguro y llevar el certificado emitido en las 72 h previas. "
            "Gabon es tercer pais de riesgo rabico no favorable: para VOLVER a la UE hace falta "
            "titulacion de anticuerpos antirrabicos hecha ANTES de salir de Europa."
        ),
        "fuentes": [
            "https://www.pettravel.com/information/pet-passports/gabon-pet-import-requirements/",
            "https://www.anivetvoyage.com/formalites-pays/g/182-gabon.html",
            "https://www.agriculture.gouv.ga/8-ministere/2-autres-contenus-ministere/10-directions-generales/14-direction-generale-de-l-elevage/",
        ],
    },
    "congo": {
        "organismo": "Direction Générale de l'Élevage (servicios veterinarios), Ministère de l'Agriculture, de l'Élevage et de la Pêche, Brazzaville",
        "url": "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-republic-congo-brazzaville",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": None,
        "cert": True,
        "cert_dias": 30,
        "cert_quien": "Veterinario oficial del pais de salida (desde EEUU, veterinario acreditado mas refrendo de APHIS; aqui SI se acepta refrendo digital)",
        "nota": (
            "YA NO ES UN AGUJERO NEGRO. SI EXISTE ficha oficial de USDA-APHIS para Congo-Brazzaville, "
            "abierta y verificada, con un 'Veterinary Health Certificate' descargable especifico para "
            "perros y gatos (congo-dog-cat.pdf, tambien abierto y verificado). Es la unica fuente "
            "OFICIAL localizada que documenta el tramite, por eso se da como 'url' aunque sea "
            "estadounidense y no congolena. "
            "AVISO QUE DA LA PROPIA APHIS: 'For pet travel requirements not listed, APHIS has not been "
            "officially informed by the foreign country about the requirements for your pet's travel'. "
            "Traducido: Congo no le ha comunicado requisitos adicionales, asi que la existencia o no "
            "de un permiso de importacion local sigue SIN DOCUMENTAR. "
            "MINISTERIO IDENTIFICADO PERO NO VERIFICADO: existe agriculture.gouv.cg con pagina propia "
            "de la Direction Generale de l'Elevage "
            "(https://agriculture.gouv.cg/direction-generale-de-lelevage-2/). El dominio bloquea el "
            "acceso automatico (robots.txt inaccesible, timeout) en dos intentos, tanto en la pagina "
            "de la direccion como en la portada, asi que no se ha podido extraer email ni telefono. "
            "Merece la pena abrirlo a mano. "
            "cert_dias=30 sale del modelo APHIS (ver aviso transversal de cabecera). Como contraste, "
            "la fuente comercial anivetvoyage (marcada, verificada) dice 'certificat de sante "
            "international etabli par un veterinaire, moins de 72 heures avant l'arrivee' y exige "
            "microchip y pasaporte, con validacion por veterinario oficial. ANTE LA DISCREPANCIA, "
            "llevar el certificado emitido en las 72 h previas. "
            "VIA ALTERNATIVA REAL: escribir a la embajada del Congo en Paris. No se ha podido "
            "verificar su web oficial (ambacongofr.org dio 404 en la pagina interna y el acceso a la "
            "portada quedo sin autorizar), por lo que NO se da ningun correo de embajada sin "
            "comprobar. Preferir la Direction Generale de l'Elevage."
        ),
        "fuentes": [
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-republic-congo-brazzaville",
            "https://www.aphis.usda.gov/sites/default/files/congo-dog-cat.pdf",
            "https://www.aphis.usda.gov/live-animal-export/export-live-animals-republic-congo-brazzaville",
            "https://agriculture.gouv.cg/direction-generale-de-lelevage-2/",
            "https://anivetvoyage.com/pays/congo-brazzaville/",
        ],
    },
    "rd-congo": {
        "organismo": "Ministère de l'Agriculture et Sécurité Alimentaire (MINASA) - servicios veterinarios; el control en frontera lo ejerce el Service de la Quarantaine Animale et Végétale (SQAV)",
        "url": "https://agriculture.gouv.cd/contact.php",
        "url_generica": True,
        "url_verificada": True,
        "email": "info@agriculture.gouv.cd",
        "tel": "+243 828 174 932",
        "cert": True,
        "cert_dias": 10,
        "cert_quien": "Veterinario oficial del pais de salida (certificat sanitaire international)",
        "nota": (
            "DEJA DE SER UN AGUJERO NEGRO EN LA PARTE DE CONTACTO, PERO NO EN LA DEL TRAMITE. "
            "HALLAZGO: existe portal oficial del ministerio, agriculture.gouv.cd, y su pagina de "
            "contacto se ha abierto y VERIFICADO. De ahi salen el email y el telefono que se dan: "
            "info@agriculture.gouv.cd, +243 828 174 932 y +243 826 927 162, en el cruce de la Avenue "
            "Batetela y el Blvd du 30 Juin, Gombe, Kinshasa. Nombre oficial: 'Ministere de "
            "l'agriculture et securite alimentaire'. "
            "POR QUE url_generica=True: se ha recorrido el portal entero (index, ministere.php, "
            "service.php, legislation.php) y NO HAY ninguna pagina sobre importacion de animales, "
            "cuarentena animal, servicios veterinarios ni certificados sanitarios. Lo unico enlazable "
            "es la pagina de contacto, que no explica el tramite. "
            "SQAV: el 'Service de la Quarantaine Animale et Vegetale' aparece citado como el organismo "
            "de control fronterizo en prensa congolena (Le Courrier de Kinshasa / ADIAC), pero NO se "
            "ha podido confirmar en fuente gubernamental ni encontrar contacto propio, por eso va en "
            "'organismo' como matiz y no como emisor principal. "
            "APHIS NO tiene ficha de mascotas de la RDC (404 comprobado en los dos patrones de URL); "
            "su ficha de animales vivos existe pero solo cubre bovinos y aves. "
            "SEGUNDA VIA VERIFICADA, muy util si el ministerio no contesta - las dos embajadas: "
            "BRUSELAS (ambardc.be, abierta y verificada): info@ambardc.be, secretariat@ambardc.be, "
            "+32 2 213 49 80, Rue Marie de Bourgogne 30, 1000 Bruxelles. "
            "PARIS (ambardcparis.com, abierta y verificada): contact@ambardcparis.com, "
            "ambacongoparis@orange.fr, 01 42 25 57 50, 32 cours Albert 1er, 75008 Paris. "
            "Ninguna de las dos menciona importacion de animales en su web: hay que preguntar. "
            "cert_dias=10 procede de fuente COMERCIAL (anivetvoyage, marcada, verificada): certificado "
            "sanitario internacional emitido menos de 10 dias antes de la llegada y valido diez dias, "
            "vacuna antirrabica de mas de 1 mes y menos de 1 ano, microchip y pasaporte. NO "
            "CONFIRMADO OFICIALMENTE."
        ),
        "fuentes": [
            "https://agriculture.gouv.cd/contact.php",
            "https://agriculture.gouv.cd/index.php",
            "https://ambardc.be/",
            "https://ambardcparis.com/contact/",
            "https://www.aphis.usda.gov/live-animal-export/export-live-animals-democratic-republic-congo",
            "https://anivetvoyage.com/pays/republique-democratique-du-congo/",
        ],
    },
    "angola": {
        "organismo": "Instituto dos Serviços de Veterinária (ISV), Ministério da Agricultura e Florestas (MINAGRIF)",
        "url": "https://www.dgav.pt/wp-content/uploads/2023/11/CERTIFICACAO-SANITARIA-ANGOLA-CAES-E-GATOS-2023.pdf",
        "url_generica": False,
        "url_verificada": True,
        "email": "gticii@minagrif.gov.ao",
        "tel": None,
        "cert": True,
        "cert_dias": 10,
        "cert_quien": "Médico veterinário oficial del pais de salida; el examen clinico debe acreditarse con documentacion emitida por un medico veterinario clinico",
        "nota": (
            "LA MEJOR FUENTE DE TODA LA LISTA PARA QUIEN SALE DE LA PENINSULA. La DGAV portuguesa "
            "(autoridad veterinaria de un Estado miembro de la UE) publica el documento oficial de "
            "certificacion sanitaria para exportar PERROS Y GATOS a Angola, edicion 2023, abierto y "
            "verificado. Al ser un acuerdo bilateral con Angola describe los requisitos REALES del "
            "lado angolano, y es directamente utilizable saliendo de Espana coordinandolo con los "
            "servicios veterinarios espanoles. "
            "REQUISITOS VERIFICADOS EN ESE DOCUMENTO: "
            "(1) HACE FALTA LICENCIA DE IMPORTACION PREVIA, llamada 'licenca Zoo-Sanitaria', que debe "
            "solicitar el interesado - este es el permiso que se buscaba; "
            "(2) el certificado veterinario es VALIDO 10 DIAS; "
            "(3) identificacion por MICROCHIP OBLIGATORIA; "
            "(4) la vacuna antirrabica no puede administrarse antes de los 3 meses de edad del animal "
            "y debe ponerse mas de 72 horas antes de la salida. "
            "LO QUE EL DOCUMENTO NO DICE: no nombra al organismo angolano que emite la licencia "
            "zoo-sanitaria ni da su contacto. El ISV es el organismo competente, confirmado en el "
            "portal oficial minagrif.gov.ao (pagina de entidades tuteladas, abierta y verificada), "
            "donde figura como 'orgao publico, tutelado pelo Ministerio da Agricultura e Florestas' "
            "responsable de sanidad animal y salud publica veterinaria. "
            "EMAIL: gticii@minagrif.gov.ao es el correo GENERAL del ministerio (pagina de contactos "
            "verificada), NO del ISV, que no publica correo propio. Direccion del ministerio: Largo "
            "Antonio Jacinto, Edificio B, Luanda. No hay telefono publicado: la pagina de contactos "
            "esta a medio montar, con campos vacios. Por eso tel=None. "
            "DESCARTADO TRAS COMPROBARLO: el servicio del portal de tramites SEPE "
            "'Pre-licenciamento MINAGRIF - Instituto dos Servicos de Veterinaria' se abrio y NO SIRVE: "
            "es pre-licenciamiento de PRODUCTOS de origen animal para empresas con licencia industrial "
            "o mayorista, no de animales de compania. "
            "APHIS NO tiene ficha de mascotas de Angola (404 comprobado)."
        ),
        "fuentes": [
            "https://www.dgav.pt/wp-content/uploads/2023/11/CERTIFICACAO-SANITARIA-ANGOLA-CAES-E-GATOS-2023.pdf",
            "https://minagrif.gov.ao/web/entidades-tutela",
            "https://minagrif.gov.ao/web/contactos",
            "https://sepe.gov.ao/catalogo/mais-servicos/pedido-de-licenciamento/pre-licenciamento-minagrif-br-instituto-dos-servicos-de-veterinaria-br-produtos-de-origem-animal",
        ],
    },
}

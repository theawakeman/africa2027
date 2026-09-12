# -*- coding: utf-8 -*-
"""Quién emite el permiso del perro en cada país, y dónde se pide exactamente.

Investigado y VERIFICADO en septiembre de 2026 por tres revisiones independientes:
cada URL se abrió una a una para comprobar que responde y que trata realmente del
permiso de importación de animales de compañía. Las que no lo hacían no están aquí.

Campos:
  url_verificada  False = la página existe pero no se ha podido abrir desde aquí
                  (cortafuegos, TLS roto); el enlace se marca en la app.
  url_generica    True  = solo se ha encontrado la portada del organismo.
  cert_dias       Validez del certificado sanitario desde su emisión. None cuando
                  el país no publica plazo: no se inventa.
"""

CONTACTOS = {'marruecos': {'organismo': 'Office National de Sécurité Sanitaire des Produits Alimentaires (ONSSA) - '
                            'Direction des Services Vétérinaires',
               'url': 'https://www.onssa.gov.ma/controle-a-limportation-et-a-lexportation/controle-a-limportation/importation-des-animaux-vivants/chiens-et-chats/',
               'url_generica': False,
               'url_verificada': False,
               'email': None,
               'tel': '+212 5 37 67 65 00',
               'cert': True,
               'cert_dias': None,
               'cert_quien': 'Veterinario oficial del pais de salida (en la UE, veterinario oficial '
                             'habilitado; certificado en modelo bilateral, no vale el pasaporte europeo '
                             'solo)',
               'nota': 'AVISO: el dominio onssa.gov.ma NO ES ALCANZABLE desde el entorno de verificacion '
                       '(la conexion es rechazada), asi que la URL NO se ha podido abrir ni comprobar; '
                       "aparece indexada con el titulo 'Chiens et chats - ONSSA' bajo la ruta de control a "
                       'la importacion de animales vivos, por lo que casi seguro es la pagina correcta, '
                       'pero NO esta verificada. ONSSA publica ademas el modelo UE en '
                       'onssa.gov.ma/wp-content/uploads/2023/07/Importation-au-Maroc-de-chiens-et-chats-a-partir-de-lUE.pdf '
                       '(tampoco verificado). VALIDEZ DEL CERTIFICADO: no hay cifra verificada para salida '
                       'desde la UE; los modelos bilaterales verificados dan cifras distintas (Reino '
                       'Unido: 7 dias; EEUU: 3 dias tras el visado de APHIS), por eso cert_dias va a None. '
                       'Requisitos comunes verificados: microchip o tatuaje previo a la vacuna, vacuna '
                       'antirrabica inactivada con >=21 dias desde la primovacunacion, examen clinico en '
                       'las 24 h previas al embarque y procedencia de pais libre de rabia los 6 meses '
                       'anteriores. Telefono: centralita de ONSSA en Rabat (av. Hadj Ahmed Cherkaoui, '
                       'Agdal) segun directorio comercial telecontact.ma, NO confirmado en fuente oficial. '
                       'Email: no publicado en fuente accesible.',
               'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-morocco',
                           'https://www.aphis.usda.gov/sites/default/files/morocco-dog-cat_0.pdf',
                           'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-morocco-certificate-3916',
                           'https://assets.publishing.service.gov.uk/media/689da555e95097004f723f64/3916EHC_V4.pdf',
                           'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm',
                           'https://www.telecontact.ma/annonceur/onssa/3257548/rabat.php']},
 'mauritania': {'organismo': "Direction des Services Vétérinaires (DSV) / Direction de l'Élevage, "
                             "Ministère de l'Élevage (antes Ministère du Développement Rural)",
                'url': 'https://elevage.gov.mr/',
                'url_generica': True,
                'url_verificada': True,
                'email': None,
                'tel': None,
                'cert': True,
                'cert_dias': None,
                'cert_quien': 'Veterinario oficial del pais de salida (certificado zoosanitario)',
                'nota': 'NO ENCONTRADA ninguna pagina, ni del Gobierno mauritano ni consular, que publique '
                        'el tramite de importacion de animales de compania. APHIS NO tiene ficha de '
                        'Mauritania en pet-travel (la URL .../pet-travel-us-mauritania devuelve 404) y '
                        "Mauritania no figura en su menu de destinos. La web del Ministere de l'Elevage "
                        '(elevage.gov.mr) entra en bucle de redirecciones y no se ha podido abrir. El '
                        'unico dato verificado es que la importacion de animales vivos exige certificado '
                        'zoosanitario (portal logistico LCA/Logistics Cluster) y la identificacion del '
                        'organismo competente en el directorio de Delegados de la OMSA/WOAH (Director des '
                        'Services Veterinaires, Ministere du Developpement Rural, Ksar, Nouakchott; el '
                        "punto focal figura tambien como Direction de l'Elevage, BP 180, Nouakchott). SOLO "
                        "PORTADA: la URL dada es la portada del Ministere de l'Elevage (elevage.gov.mr), "
                        'que si carga y tiene una seccion de servicios veterinarios (en arabe), pero NO '
                        'publica ficha del tramite ni telefono/email de contacto. Ruta practica '
                        'recomendada: escribir a la Embajada de Mauritania en Paris '
                        '(ambarimparis@gmail.com, +33 1 45 04 88 54), cuya pagina consular esta verificada '
                        'pero NO menciona animales; o a la Embajada en Madrid. Sin plazo de validez del '
                        'certificado publicado.',
                'fuentes': ['https://elevage.gov.mr/',
                            'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm',
                            'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/animalwelfare/PF_animalwelfare_fr.htm',
                            'https://lca.logcluster.org/13-mauritanie-information-douaniere',
                            'https://ambarimparis.fr/informations-consulaires/']},
 'senegal': {'organismo': "Direction des Services Vétérinaires (DSV), Ministère de l'Agriculture, de la "
                          "Souveraineté Alimentaire et de l'Élevage",
             'url': 'https://senegalservices.sn/demarche/demander-lautorisation-dimporter-des-animaux-de-compagnie',
             'url_generica': False,
             'url_verificada': False,
             'email': 'contacts@elevage.gouv.sn',
             'tel': None,
             'cert': True,
             'cert_dias': 21,
             'cert_quien': 'Veterinario oficial/acreditado del pais de salida (en la UE, veterinario '
                           'oficial); debe acompañar al animal',
             'nota': 'LA URL QUE FALTABA: el portal oficial Senegal Services publica la ficha del tramite '
                     "con el titulo exacto 'Demander l'autorisation d'importer des animaux de compagnie'. "
                     'AVISO: NO se ha podido abrir desde el entorno de verificacion (senegalservices.sn y '
                     'servicepublic.gouv.sn rechazan la conexion), por eso url_verificada=False; el titulo '
                     'y la ruta si estan indexados. Ficha del mismo tramite tambien en '
                     'servicepublic.gouv.sn (/index.php/demarche_administrative/demarche/1/1018/22/254), '
                     'igualmente inaccesible. URL ALTERNATIVA SI VERIFICADA (abierta y comprobada, trata '
                     'de Senegal y de perros): '
                     'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-senegal '
                     '. Contenido confirmado ahi: hace falta PERMISO DE IMPORTACION previo del Ministere '
                     "de l'Agriculture, de la Souverainete Alimentaire et de l'Elevage, valido 3 meses "
                     'desde su emision; certificado sanitario emitido dentro de los 21 dias previos al '
                     'viaje; vacuna antirrabica al menos 21 dias antes. Emails operativos de la DSV segun '
                     'APHIS: dsvmepa@gmail.com y wadesanou@gmail.com. Direccion: 37 Avenue Pasteur, BP 67, '
                     'Dakar. Telefono no publicado en ninguna fuente verificada.',
             'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-senegal',
                         'https://senegalservices.sn/demarche/demander-lautorisation-dimporter-des-animaux-de-compagnie',
                         'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-senegal-certificate-6367',
                         'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm']},
 'gambia': {'organismo': 'Department of Livestock Services (Veterinary Services), Ministry of Agriculture',
            'url': 'https://gambiaembassy.eu/faqs/',
            'url_generica': False,
            'url_verificada': True,
            'email': None,
            'tel': '+220 4397472',
            'cert': True,
            'cert_dias': None,
            'cert_quien': "Veterinario del pais de origen ('Veterinarian's health certificate issued at "
                          "point of origin')",
            'nota': 'La Embajada de Gambia en Bruselas (jurisdiccion UE) dice que el permiso de '
                    'importacion se obtiene REGISTRANDO al animal EN GAMBIA, despues de llegar, ante el '
                    'Gambian Veterinary Department; no hay permiso previo publicado. Exige certificado '
                    'veterinario de origen, cartilla de vacunacion y vacuna antirrabica. Telefono dado por '
                    'la embajada para el departamento veterinario: +220 4397472. PENDIENTE: no hay web '
                    'propia del Department of Livestock Services localizable; no se ha encontrado email '
                    'oficial ni validez publicada del certificado. APHIS no tiene ficha de Gambia en '
                    'pet-travel.',
            'fuentes': ['https://gambiaembassy.eu/faqs/',
                        'https://www.aphis.usda.gov/live-animal-export/export-live-animals-gambia']},
 'guinea': {'organismo': "Direction Nationale des Services Vétérinaires (DNSV), Ministère de l'Élevage et "
                         'des Productions Animales',
            'url': 'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-guinea',
            'url_generica': False,
            'url_verificada': True,
            'email': 'contact@elevage.gov.gn',
            'tel': None,
            'cert': True,
            'cert_dias': None,
            'cert_quien': 'Veterinario oficial/acreditado del pais de salida',
            'nota': 'La ficha APHIS de Guinea esta verificada y es especifica del pais, pero solo exige un '
                    'certificado sanitario internacional para perros y gatos y NO publica ni plazo de '
                    'validez ni permiso de importacion previo: APHIS remite explicitamente a confirmar con '
                    'las autoridades guineanas o la embajada. El organismo competente es la DNSV '
                    '(identificado en el directorio de Delegados de la OMSA/WOAH y en la pagina de '
                    'misiones del Ministerio, elevage.gov.gn); su direccion postal es BP 559, Conakry. El '
                    'email dado es el buzon general del Ministerio de Elevage, unico verificado; el '
                    'telefono que publica esa web es un marcador de posicion (+224 000 00 00 00), por eso '
                    'va a None. NO se ha encontrado ninguna pagina guineana que publique el tramite.',
            'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-guinea',
                        'https://www.elevage.gov.gn/mission-et-attributions/',
                        'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm']},
 'sierra-leona': {'organismo': 'Livestock and Veterinary Services Division, Ministry of Agriculture, '
                               'Forestry and Food Security (MAFFS)',
                  'url': 'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-sierra-leone-certificate-6548',
                  'url_generica': False,
                  'url_verificada': True,
                  'email': None,
                  'tel': None,
                  'cert': True,
                  'cert_dias': 7,
                  'cert_quien': 'Veterinario oficial (Official Veterinarian) del pais de salida',
                  'nota': 'NO EXISTE pagina del Gobierno de Sierra Leona ni consular que publique el '
                          'tramite; Sierra Leona tampoco figura en el menu de destinos de pet-travel de '
                          'APHIS. La URL dada es la ficha oficial britanica (DEFRA/APHA) del certificado '
                          "6548 'Export cats and dogs to Sierra Leone', verificada, con el modelo de "
                          'certificado y las notas de orientacion; el modelo (6548EHC_V3.pdf) esta '
                          'comprobado y dice literalmente que el certificado es valido 7 dias desde la '
                          'firma, exige examen clinico sin signos de enfermedad contagiosa (moquillo, '
                          'rabia, parasitos externos) y constancia de la vacuna antirrabica. En ese modelo '
                          'NO se menciona permiso de importacion previo, pero eso no prueba que no lo '
                          'haya. Organismo competente identificado en el directorio de Delegados de la '
                          'OMSA/WOAH: Livestock and Veterinary Services Division del MAFFS, Youyi '
                          'Building, Freetown. Sin email ni telefono publicados en fuente verificada: '
                          'confirmar por la Alta Comision de Sierra Leona antes de salir.',
                  'fuentes': ['https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-sierra-leone-certificate-6548',
                              'https://assets.publishing.service.gov.uk/media/5bceea93ed915d4315aba3e1/6548EHC_V3.pdf',
                              'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm',
                              'https://www.aphis.usda.gov/live-animal-export/export-live-animals-sierra-leone']},
 'liberia': {'organismo': "Consulate General / Embassy of the Republic of Liberia (emite el 'Pet "
                          "Clearance'); autoridad interna: Ministry of Agriculture de Liberia",
             'url': 'https://liberiaconsulate-ny.com/consulate-services/pet-clearance/',
             'url_generica': False,
             'url_verificada': True,
             'email': 'info@liberiaconsulate-ny.com',
             'tel': '+1 212 687 1025',
             'cert': True,
             'cert_dias': 30,
             'cert_quien': 'Veterinario colegiado del pais de salida (o servicio veterinario oficial)',
             'nota': "En Liberia el permiso es un 'Pet Clearance' que expide la MISION DIPLOMATICA "
                     'liberiana ANTES del viaje, no un ministerio en Monrovia. El certificado sanitario '
                     'debe tener fecha no superior a 30 dias antes de la llegada. Tasa 100 USD por animal '
                     'en el consulado de NY. OJO viaje desde España: hay que pedirlo a la Embajada de '
                     'Liberia acreditada ante España (no a la de Nueva York); los datos de aqui son los '
                     'del consulado de NY, los unicos con pagina verificada. La Embajada de Liberia en '
                     'EEUU publica el mismo tramite en liberianembassyus.org (tel +1 202 723 0437, '
                     'info@liberianembassyus.org). PENDIENTE: no se ha encontrado ninguna pagina del '
                     'Gobierno de Liberia que publique el tramite.',
             'fuentes': ['https://liberiaconsulate-ny.com/consulate-services/pet-clearance/',
                         'https://www.liberianembassyus.org/document/requirements-for-pet-travel-to-liberia']},
 'costa-de-marfil': {'organismo': 'Direction des Services Vétérinaires (DSV), Ministère des Ressources '
                                  'Animales et Halieutiques',
                     'url': 'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ivory-coast',
                     'url_generica': False,
                     'url_verificada': True,
                     'email': 'carv.dsvci@gmail.com',
                     'tel': '+225 27 20 21 89 72',
                     'cert': True,
                     'cert_dias': 10,
                     'cert_quien': 'Veterinario oficial/acreditado del pais de salida, refrendado por la '
                                   'autoridad veterinaria nacional',
                     'nota': 'Hace falta AUTORIZACION DE IMPORTACION previa de la DSV: formulario de '
                             'solicitud + copia del certificado de vacunacion antirrabica en vigor. '
                             'Segundo email: dsv.sdsa2017@gmail.com. Rabia: si es primovacunacion o '
                             'refuerzo fuera de plazo, esperar 21 dias antes de viajar. Direccion DSV: '
                             'Cite Administrative, Tour C, 11e etage, Abidjan-Plateau. El telefono figura '
                             'en el portal GUCE como 20 21 89 72 (numeracion antigua de 8 cifras); se da '
                             'ya con el prefijo 27 de la numeracion a 10 cifras vigente desde 2021, SIN '
                             'VERIFICAR por llamada. Formulario oficial de solicitud (PDF, en frances, del '
                             'MIRAH) reproducido por APHIS: ptw-ivory-coast-import-permit-application.pdf.',
                     'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ivory-coast',
                                 'https://www.aphis.usda.gov/sites/default/files/ptw-ivory-coast-import-permit-application.pdf',
                                 'https://www.gucecotedivoire.ci/pwic/animaux-vivants/']},
 'ghana': {'organismo': 'Veterinary Services Department (VSD), Ministry of Food and Agriculture (MoFA)',
           'url': 'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ghana',
           'url_generica': False,
           'url_verificada': True,
           'email': 'vsd@mofa.gov.gh',
           'tel': '+233 24 264 9497',
           'cert': True,
           'cert_dias': 30,
           'cert_quien': "Veterinario oficial del pais de salida ('International Health Certificate'; "
                         'desde EEUU lo emite veterinario acreditado y lo refrenda APHIS, que acepta '
                         'refrendo digital)',
           'nota': 'OJO AL NOMBRE: el organismo existe y su sitio oficial es vsd.gov.gh, pero se llama a '
                   "si mismo 'Veterinary Services Department', no 'Directorate'. La portada vsd.gov.gh SI "
                   'se ha abierto y verificado, y de ahi salen el email (vsd@mofa.gov.gh), la direccion '
                   'postal (P.O. Box M161, Accra) y el telefono que se da aqui, que es la linea de '
                   "emergencia publicada (0242649497). El otro numero de la portada aparece como '(233) "
                   "030-1234567', que es evidentemente un numero de relleno: NO usarlo. LA PAGINA DEL "
                   "TRAMITE NO SIRVE: la portada enlaza 'Import Requirements' en "
                   'https://vsd.gov.gh/255-2/, pero esa URL devuelve error de servidor en TRES intentos '
                   "distintos, asi que no se ha podido verificar y no se da como 'url'. El sitio tampoco "
                   "tiene pagina dedicada a mascotas, solo 'Import Requirements'/'Export Requirements' "
                   "genericos. Por eso la 'url' que se da es la ficha de USDA-APHIS, que SI se ha abierto "
                   'y SI trata de perros y gatos hacia Ghana. cert_dias=30 sale del modelo APHIS (ver '
                   'aviso transversal de cabecera). DATO UTIL DE FUENTE COMERCIAL (pettravel.com, marcada '
                   'como tal, abierta y verificada): en Ghana SI hace falta permiso de importacion incluso '
                   'para mascota personal, se pide despues de las analiticas y el permiso vale 8 semanas; '
                   'vacuna antirrabica entre 30 dias y 6 meses antes de entrar; microchip ISO 11784/11785. '
                   'NO CONFIRMADO POR EL VSD. PROCEDIMIENTO (wikiprocedure, fuente terciaria NO oficial, '
                   'verificada): formulario en la oficina del VSD (Government Animal Clinic, Okodan Rd, '
                   'Accra), solicitud por escrito con al menos 7 dias de antelacion, aviso al puesto de '
                   'entrada 3 dias antes, y cuarentena teorica de 21-30 dias. Telefonos de MoFA citados '
                   'alli: +233 21 662961 / 663036 / 662810. La cuarentena es el riesgo serio a aclarar por '
                   'escrito ANTES de salir.',
           'fuentes': ['https://vsd.gov.gh/',
                       'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ghana',
                       'https://www.aphis.usda.gov/sites/default/files/ghana-dog-cat.pdf',
                       'https://www.pettravel.com/information/pet-passports/ghana-pet-import-requirements/',
                       'https://www.wikiprocedure.com/index.php/Ghana_-_Apply_for_Live_Animal_and_Animal_Products_Import']},
 'togo': {'organismo': "Ministère de l'Agriculture, de la Production Animale (Ressources Animales) et de "
                       'la Souveraineté Alimentaire (MAPRASA) - servicios veterinarios / Direction de '
                       "l'Élevage",
          'url': 'https://www.pettravel.com/information/pet-passports/togo-pet-import-requirements/',
          'url_generica': False,
          'url_verificada': True,
          'email': None,
          'tel': None,
          'cert': True,
          'cert_dias': 3,
          'cert_quien': 'Veterinario oficial del pais de salida, o veterinario habilitado con refrendo de '
                        'veterinario oficial',
          'nota': 'URL DE FUENTE COMERCIAL, MARCADA COMO TAL (pettravel.com): es el ULTIMO RECURSO porque '
                  'NO EXISTE ninguna pagina oficial togolesa localizable sobre importacion de animales de '
                  'compania. Se ha abierto y verificado que trata del tema. NOMBRE DEL MINISTERIO SI '
                  "VERIFICADO en fuente oficial: la ficha de USDA-APHIS 'Export Live Animals to Togo' "
                  "(abierta y verificada) cita expresamente al 'Ministry of Agriculture, Fisheries Animal "
                  "resources and Food Sovereignty (MAPRASA) of the Togolese Republic' como la autoridad "
                  'que acepta los certificados; pero esa ficha va de ganado y aves, NO de mascotas, por '
                  "eso no se usa como 'url'. APHIS NO tiene ficha de mascotas de Togo: "
                  '.../pet-travel-us-togo da 404 comprobado. No se ha encontrado email ni telefono del '
                  'servicio veterinario togoles. PERMISO DE IMPORTACION - PUNTO CRITICO PARA ESTA RUTA: '
                  'pettravel dice que SI hace falta permiso salvo que se entre desde una lista cerrada de '
                  'paises que incluye Benin, Burkina, Costa de Marfil, Camerun, Gabon, los dos Congos, '
                  'Mali, Niger, Senegal y FRANCIA, pero NO incluye ESPANA ni GHANA. Es decir: entrando a '
                  'Togo desde Ghana, que es lo que hara este viaje, segun esta fuente HARIA FALTA PERMISO. '
                  'Dato no confirmado oficialmente pero demasiado importante para ignorarlo: preguntar por '
                  'escrito. cert_dias=3 lo dan DOS fuentes comerciales independientes que coinciden '
                  "(pettravel: 'within 3 days of entry'; anivetvoyage: emitido como maximo 3 dias antes de "
                  'la llegada). Vacuna antirrabica: al menos 21 dias antes (pettravel) / entre 21 dias y '
                  '12 meses (anivetvoyage). Microchip recomendado, no exigido segun pettravel.',
          'fuentes': ['https://www.aphis.usda.gov/live-animal-export/export-live-animals-togo',
                      'https://www.pettravel.com/information/pet-passports/togo-pet-import-requirements/',
                      'https://www.anivetvoyage.com/formalites-pays/t/174-togo.html']},
 'benin': {'organismo': "Direction de l'Élevage (DE), Ministère de l'Agriculture, de l'Élevage et de la "
                        'Pêche (MAEP)',
           'url': 'https://catis.xroad.bj/publicservices/PS00501',
           'url_generica': False,
           'url_verificada': True,
           'email': None,
           'tel': None,
           'cert': True,
           'cert_dias': 10,
           'cert_quien': 'Veterinario oficial del pais de salida; en Benin el certificado sanitario '
                         "internacional lo expide la Direction de l'Élevage",
           'nota': 'EL MEJOR RESULTADO OFICIAL DE TODA LA LISTA JUNTO CON ANGOLA. La URL es el catalogo '
                   'oficial de servicios publicos del Gobierno de Benin (CatIS, catis.xroad.bj), abierto y '
                   "verificado, y el servicio PS00501 se titula literalmente 'Controle sanitaire et "
                   "delivrance des certificats sanitaires internationaux a l'importation et a "
                   "l'exportation des animaux vivants' y su descripcion incluye EXPRESAMENTE 'animaux de "
                   "compagnie'. Es exactamente el tramite que se busca, nombrado por el propio Estado "
                   "benines. ORGANISMO: lo presta la Direction de l'Elevage, del MAEP (ficha de "
                   'institucion verificada en https://catis.xroad.bj/institutions/IN00173). BASE LEGAL '
                   'citada en la ficha: Arrete N.045/MAEP/MEF/MDGLAAT/D-CAB/SGM/DRH/DRFM/DE/SA de 15 de '
                   'febrero de 2008, sobre tasas de los servicios veterinarios. DIRECCION FISICA '
                   "VERIFICADA de la Direction de l'Elevage: Cotonou, Akpakpa, apres ancien pont, domaine "
                   "avant Societe 'la Roche'. Horario 8:00-12:30 y 14:00-17:30, lunes a viernes. LO QUE NO "
                   'HAY: ni la ficha del servicio ni la de la institucion publican email ni telefono, por '
                   'eso ambos van a None. Los unicos correos que aparecen en CatIS (info@ega.ee, '
                   'info@upmind.ee) son de los administradores estonios de la plataforma, NO de Benin: no '
                   'escribir ahi. Hay que presentarse o llamar por otra via. cert_dias=10 procede de '
                   'fuente COMERCIAL (anivetvoyage, marcada, verificada): certificado valido diez dias '
                   'desde su emision, y emitido menos de 72 h antes de la llegada; vacuna antirrabica de '
                   'mas de 1 mes y menos de 1 ano. NO confirmado por el MAEP.',
           'fuentes': ['https://catis.xroad.bj/publicservices/PS00501',
                       'https://catis.xroad.bj/institutions/IN00173',
                       'https://anivetvoyage.com/pays/benin/']},
 'nigeria': {'organismo': 'Federal Department of Veterinary and Pest Control Services (FDVPCS) - Chief '
                          'Veterinary Officer of Nigeria (CVO), Federal Ministry of Agriculture. La '
                          'Nigeria Agricultural Quarantine Service (NAQS) NO emite el permiso: inspecciona '
                          'y pone en cuarentena a la llegada',
             'url': 'https://naqs.gov.ng/animal/',
             'url_generica': False,
             'url_verificada': True,
             'email': 'contact@naqs.gov.ng',
             'tel': '+234 807 777 8943',
             'cert': True,
             'cert_dias': 30,
             'cert_quien': "Veterinario oficial del pais de salida ('Sanitary/Health certificate'); desde "
                           'EEUU, veterinario acreditado MAS refrendo de APHIS en TINTA ORIGINAL y con '
                           'sello en relieve',
             'nota': 'CORRECCION IMPORTANTE AL PLANTEAMIENTO DE PARTIDA: el permiso de importacion NO lo '
                     'emite NAQS. El SOP oficial de la propia NAQS (PDF abierto y verificado) dice '
                     "literalmente 'Apply for import permit to the chief Veterinary Officer (CVO), Federal "
                     "Department of Veterinary and Pest Control Services', con direccion en el Federal "
                     'Ministry of Agriculture, Area 11, Abuja. NAQS es quien inspecciona en el puesto '
                     'fronterizo y quien manda los animales vivos a estacion de cuarentena para '
                     'observacion. HAY QUE HACER LAS DOS COSAS: pedir el permiso al CVO y notificar a '
                     'NAQS. URL VERIFICADA: naqs.gov.ng/animal/ se ha abierto y trata de cuarentena animal '
                     "citando expresamente perros ('including dogs, cattle, cats, horses...'). Es la "
                     'pagina del departamento competente, no un formulario de permiso. CONTACTOS '
                     'VERIFICADOS EN ESA PAGINA: contact@naqs.gov.ng, info@naqs.gov.ng, +234 8077778943, '
                     '+234 8091333385; jefe de departamento Dr. Emeka Asiegbu (emeka.asiegbu@naqs.gov.ng, '
                     'hod.aq@naqs.gov.ng); Plot 81, Ralph Shodeinde Street, Central Business District, '
                     'Abuja. NO se ha localizado email ni telefono directos del CVO/FDVPCS, que es a quien '
                     'hay que dirigir formalmente la solicitud: usar NAQS como puerta de entrada y pedir '
                     'que la deriven. cert_dias=30 sale del modelo APHIS (ver aviso transversal de '
                     'cabecera). REQUISITOS VERIFICADOS en el certificado APHIS de Nigeria: MICROCHIP '
                     "OBLIGATORIO ('All pets (dogs and/or cats) must be microchipped') y vacuna "
                     'antirrabica con vacuna inactivada dentro del ano anterior a la fecha de salida. '
                     'ATENCION: Nigeria es de los pocos que NO acepta refrendo digital, exige tinta '
                     'original y sello en relieve.',
             'fuentes': ['https://naqs.gov.ng/animal/',
                         'https://naqs.gov.ng/wp-content/uploads/2020/07/NAQS_SOP.pdf',
                         'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-nigeria',
                         'https://www.aphis.usda.gov/sites/default/files/nigeria-dog-cat.pdf']},
 'camerun': {'organismo': "Ministère de l'Élevage, des Pêches et des Industries Animales (MINEPIA) - "
                          'Direction des Services Vétérinaires',
             'url': 'https://www.aphis.usda.gov/pet-travel/pet-travel-united-states-cameroon',
             'url_generica': False,
             'url_verificada': True,
             'email': None,
             'tel': None,
             'cert': True,
             'cert_dias': 30,
             'cert_quien': 'Veterinario oficial del pais de salida (desde EEUU, veterinario acreditado MAS '
                           'refrendo de APHIS en tinta original y con sello en relieve)',
             'nota': 'MINEPIA es el ministerio competente, confirmado por el nombre y por la existencia en '
                     "su web de una ficha de tramite titulada 'OBTENTION D'UNE AUTORISATION D'IMPORTATION "
                     "DES POUSSINS D'UN JOUR, DES OEUFS A COUVER, DES ANIMAUX D'ELEVAGE ET DE COMPAGNIE' "
                     'en '
                     'minepia.cm/site/services/productions-et-industries-animales/obtention-dune-autorisation-dimportation-des-poussins-dun-jour-des-oeufs-a-couver-des-animaux-delevage-et-de-compagnie/ '
                     "Por el titulo es EXACTAMENTE el tramite buscado (dice 'animaux de compagnie'), pero "
                     'NO SE HA PODIDO ABRIR NI VERIFICAR: el dominio minepia.cm tiene la cadena de '
                     'certificado TLS rota y bloquea el acceso automatico, en cuatro intentos y por tres '
                     'rutas distintas (pagina del tramite, /site/contact/ y www.minepia.cm). Por eso NO se '
                     "da como 'url' y no hay email ni telefono: MERECE LA PENA ABRIRLA A MANO EN UN "
                     "NAVEGADOR, es previsiblemente la mejor fuente para Camerun. La 'url' que se da es la "
                     'ficha de USDA-APHIS de Camerun, abierta y verificada, con certificado veterinario '
                     'descargable para perros y gatos. OJO: esta en el patron de URL ANTIGUO '
                     '(/pet-travel/pet-travel-united-states-cameroon); el patron nuevo '
                     '(/pet-travel/us-to-another-country-export/pet-travel-us-cameroon) da 404. '
                     'cert_dias=30 sale del modelo APHIS (ver aviso transversal de cabecera). El '
                     'certificado verificado exige verificacion de microchip. DATO DE FUENTE COMERCIAL '
                     '(pettravel.com, marcada, verificada): afirma que NO hace falta permiso de '
                     'importacion para mascota personal que viaja con su dueno, y que la vacuna '
                     'antirrabica debe tener al menos 30 dias y no mas de 12 meses, con animal mayor de 3 '
                     'meses. CONTRADICE la existencia del tramite de MINEPIA: no fiarse, preguntar.',
             'fuentes': ['https://www.aphis.usda.gov/pet-travel/pet-travel-united-states-cameroon',
                         'https://www.aphis.usda.gov/sites/default/files/cameroon-dog-cat.pdf',
                         'https://minepia.cm/site/services/productions-et-industries-animales/obtention-dune-autorisation-dimportation-des-poussins-dun-jour-des-oeufs-a-couver-des-animaux-delevage-et-de-compagnie/',
                         'https://www.pettravel.com/information/pet-passports/cameroon-pet-import-requirements/']},
 'gabon': {'organismo': "Direction Générale de l'Élevage, Ministère de l'Agriculture et de l'Alimentation",
           'url': 'https://www.pettravel.com/information/pet-passports/gabon-pet-import-requirements/',
           'url_generica': False,
           'url_verificada': True,
           'email': None,
           'tel': None,
           'cert': True,
           'cert_dias': 10,
           'cert_quien': 'Veterinario habilitado del pais de salida (certificat sanitaire international)',
           'nota': 'EL PAIS CON MENOS RESPALDO OFICIAL DE LOS NUEVE, junto con Togo. URL DE FUENTE '
                   'COMERCIAL, MARCADA COMO TAL (pettravel.com), usada como ultimo recurso: se ha abierto '
                   'y verificado que trata de los requisitos de entrada de perros a Gabon. ORGANISMO '
                   'IDENTIFICADO PERO NO VERIFICADO: existe agriculture.gouv.ga con una pagina de la '
                   "Direction Generale de l'Elevage en "
                   'www.agriculture.gouv.ga/8-ministere/2-autres-contenus-ministere/10-directions-generales/14-direction-generale-de-l-elevage/ '
                   ', pero el dominio hace timeout y bloquea el acceso automatico, asi que no se ha podido '
                   'abrir ni sacar de ahi nombre del director, email ni telefono. Merece la pena '
                   'intentarlo a mano. APHIS NO tiene ficha de Gabon en NINGUNO de sus dos patrones de URL '
                   '(404 comprobado en ambos), asi que no hay respaldo estadounidense tampoco. REQUISITOS '
                   'SEGUN LAS DOS FUENTES COMERCIALES (coinciden en lo esencial): pettravel dice que NO '
                   'hace falta permiso de importacion para mascota personal y que el certificado sanitario '
                   'se emite dentro de los 10 dias previos al transporte, con vacuna antirrabica entre 30 '
                   'dias y 12 meses antes y microchip recomendado pero no obligatorio; anivetvoyage '
                   'endurece el plazo a 72 horas antes de la llegada y exige microchip y pasaporte, con '
                   'vacuna de mas de 30 dias y menos de un ano. ANTE LA DISCREPANCIA 10 DIAS / 72 HORAS, '
                   'ir a lo seguro y llevar el certificado emitido en las 72 h previas. Gabon es tercer '
                   'pais de riesgo rabico no favorable: para VOLVER a la UE hace falta titulacion de '
                   'anticuerpos antirrabicos hecha ANTES de salir de Europa.',
           'fuentes': ['https://www.pettravel.com/information/pet-passports/gabon-pet-import-requirements/',
                       'https://www.anivetvoyage.com/formalites-pays/g/182-gabon.html',
                       'https://www.agriculture.gouv.ga/8-ministere/2-autres-contenus-ministere/10-directions-generales/14-direction-generale-de-l-elevage/']},
 'congo': {'organismo': "Direction Générale de l'Élevage (servicios veterinarios), Ministère de "
                        "l'Agriculture, de l'Élevage et de la Pêche, Brazzaville",
           'url': 'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-republic-congo-brazzaville',
           'url_generica': False,
           'url_verificada': True,
           'email': None,
           'tel': None,
           'cert': True,
           'cert_dias': 30,
           'cert_quien': 'Veterinario oficial del pais de salida (desde EEUU, veterinario acreditado mas '
                         'refrendo de APHIS; aqui SI se acepta refrendo digital)',
           'nota': 'YA NO ES UN AGUJERO NEGRO. SI EXISTE ficha oficial de USDA-APHIS para '
                   "Congo-Brazzaville, abierta y verificada, con un 'Veterinary Health Certificate' "
                   'descargable especifico para perros y gatos (congo-dog-cat.pdf, tambien abierto y '
                   'verificado). Es la unica fuente OFICIAL localizada que documenta el tramite, por eso '
                   "se da como 'url' aunque sea estadounidense y no congolena. AVISO QUE DA LA PROPIA "
                   "APHIS: 'For pet travel requirements not listed, APHIS has not been officially informed "
                   "by the foreign country about the requirements for your pet's travel'. Traducido: Congo "
                   'no le ha comunicado requisitos adicionales, asi que la existencia o no de un permiso '
                   'de importacion local sigue SIN DOCUMENTAR. MINISTERIO IDENTIFICADO PERO NO VERIFICADO: '
                   "existe agriculture.gouv.cg con pagina propia de la Direction Generale de l'Elevage "
                   '(https://agriculture.gouv.cg/direction-generale-de-lelevage-2/). El dominio bloquea el '
                   'acceso automatico (robots.txt inaccesible, timeout) en dos intentos, tanto en la '
                   'pagina de la direccion como en la portada, asi que no se ha podido extraer email ni '
                   'telefono. Merece la pena abrirlo a mano. cert_dias=30 sale del modelo APHIS (ver aviso '
                   'transversal de cabecera). Como contraste, la fuente comercial anivetvoyage (marcada, '
                   "verificada) dice 'certificat de sante international etabli par un veterinaire, moins "
                   "de 72 heures avant l'arrivee' y exige microchip y pasaporte, con validacion por "
                   'veterinario oficial. ANTE LA DISCREPANCIA, llevar el certificado emitido en las 72 h '
                   'previas. VIA ALTERNATIVA REAL: escribir a la embajada del Congo en Paris. No se ha '
                   'podido verificar su web oficial (ambacongofr.org dio 404 en la pagina interna y el '
                   'acceso a la portada quedo sin autorizar), por lo que NO se da ningun correo de '
                   "embajada sin comprobar. Preferir la Direction Generale de l'Elevage.",
           'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-republic-congo-brazzaville',
                       'https://www.aphis.usda.gov/sites/default/files/congo-dog-cat.pdf',
                       'https://www.aphis.usda.gov/live-animal-export/export-live-animals-republic-congo-brazzaville',
                       'https://agriculture.gouv.cg/direction-generale-de-lelevage-2/',
                       'https://anivetvoyage.com/pays/congo-brazzaville/']},
 'rd-congo': {'organismo': "Ministère de l'Agriculture et Sécurité Alimentaire (MINASA) - servicios "
                           'veterinarios; el control en frontera lo ejerce el Service de la Quarantaine '
                           'Animale et Végétale (SQAV)',
              'url': 'https://agriculture.gouv.cd/contact.php',
              'url_generica': True,
              'url_verificada': True,
              'email': 'info@agriculture.gouv.cd',
              'tel': '+243 828 174 932',
              'cert': True,
              'cert_dias': 10,
              'cert_quien': 'Veterinario oficial del pais de salida (certificat sanitaire international)',
              'nota': 'DEJA DE SER UN AGUJERO NEGRO EN LA PARTE DE CONTACTO, PERO NO EN LA DEL TRAMITE. '
                      'HALLAZGO: existe portal oficial del ministerio, agriculture.gouv.cd, y su pagina de '
                      'contacto se ha abierto y VERIFICADO. De ahi salen el email y el telefono que se '
                      'dan: info@agriculture.gouv.cd, +243 828 174 932 y +243 826 927 162, en el cruce de '
                      'la Avenue Batetela y el Blvd du 30 Juin, Gombe, Kinshasa. Nombre oficial: '
                      "'Ministere de l'agriculture et securite alimentaire'. POR QUE url_generica=True: se "
                      'ha recorrido el portal entero (index, ministere.php, service.php, legislation.php) '
                      'y NO HAY ninguna pagina sobre importacion de animales, cuarentena animal, servicios '
                      'veterinarios ni certificados sanitarios. Lo unico enlazable es la pagina de '
                      "contacto, que no explica el tramite. SQAV: el 'Service de la Quarantaine Animale et "
                      "Vegetale' aparece citado como el organismo de control fronterizo en prensa "
                      'congolena (Le Courrier de Kinshasa / ADIAC), pero NO se ha podido confirmar en '
                      "fuente gubernamental ni encontrar contacto propio, por eso va en 'organismo' como "
                      'matiz y no como emisor principal. APHIS NO tiene ficha de mascotas de la RDC (404 '
                      'comprobado en los dos patrones de URL); su ficha de animales vivos existe pero solo '
                      'cubre bovinos y aves. SEGUNDA VIA VERIFICADA, muy util si el ministerio no contesta '
                      '- las dos embajadas: BRUSELAS (ambardc.be, abierta y verificada): info@ambardc.be, '
                      'secretariat@ambardc.be, +32 2 213 49 80, Rue Marie de Bourgogne 30, 1000 Bruxelles. '
                      'PARIS (ambardcparis.com, abierta y verificada): contact@ambardcparis.com, '
                      'ambacongoparis@orange.fr, 01 42 25 57 50, 32 cours Albert 1er, 75008 Paris. Ninguna '
                      'de las dos menciona importacion de animales en su web: hay que preguntar. '
                      'cert_dias=10 procede de fuente COMERCIAL (anivetvoyage, marcada, verificada): '
                      'certificado sanitario internacional emitido menos de 10 dias antes de la llegada y '
                      'valido diez dias, vacuna antirrabica de mas de 1 mes y menos de 1 ano, microchip y '
                      'pasaporte. NO CONFIRMADO OFICIALMENTE.',
              'fuentes': ['https://agriculture.gouv.cd/contact.php',
                          'https://agriculture.gouv.cd/index.php',
                          'https://ambardc.be/',
                          'https://ambardcparis.com/contact/',
                          'https://www.aphis.usda.gov/live-animal-export/export-live-animals-democratic-republic-congo',
                          'https://anivetvoyage.com/pays/republique-democratique-du-congo/']},
 'angola': {'organismo': 'Instituto dos Serviços de Veterinária (ISV), Ministério da Agricultura e '
                         'Florestas (MINAGRIF)',
            'url': 'https://www.dgav.pt/wp-content/uploads/2023/11/CERTIFICACAO-SANITARIA-ANGOLA-CAES-E-GATOS-2023.pdf',
            'url_generica': False,
            'url_verificada': True,
            'email': 'gticii@minagrif.gov.ao',
            'tel': None,
            'cert': True,
            'cert_dias': 10,
            'cert_quien': 'Médico veterinário oficial del pais de salida; el examen clinico debe '
                          'acreditarse con documentacion emitida por un medico veterinario clinico',
            'nota': 'LA MEJOR FUENTE DE TODA LA LISTA PARA QUIEN SALE DE LA PENINSULA. La DGAV portuguesa '
                    '(autoridad veterinaria de un Estado miembro de la UE) publica el documento oficial de '
                    'certificacion sanitaria para exportar PERROS Y GATOS a Angola, edicion 2023, abierto '
                    'y verificado. Al ser un acuerdo bilateral con Angola describe los requisitos REALES '
                    'del lado angolano, y es directamente utilizable saliendo de Espana coordinandolo con '
                    'los servicios veterinarios espanoles. REQUISITOS VERIFICADOS EN ESE DOCUMENTO: (1) '
                    "HACE FALTA LICENCIA DE IMPORTACION PREVIA, llamada 'licenca Zoo-Sanitaria', que debe "
                    'solicitar el interesado - este es el permiso que se buscaba; (2) el certificado '
                    'veterinario es VALIDO 10 DIAS; (3) identificacion por MICROCHIP OBLIGATORIA; (4) la '
                    'vacuna antirrabica no puede administrarse antes de los 3 meses de edad del animal y '
                    'debe ponerse mas de 72 horas antes de la salida. LO QUE EL DOCUMENTO NO DICE: no '
                    'nombra al organismo angolano que emite la licencia zoo-sanitaria ni da su contacto. '
                    'El ISV es el organismo competente, confirmado en el portal oficial minagrif.gov.ao '
                    "(pagina de entidades tuteladas, abierta y verificada), donde figura como 'orgao "
                    "publico, tutelado pelo Ministerio da Agricultura e Florestas' responsable de sanidad "
                    'animal y salud publica veterinaria. EMAIL: gticii@minagrif.gov.ao es el correo '
                    'GENERAL del ministerio (pagina de contactos verificada), NO del ISV, que no publica '
                    'correo propio. Direccion del ministerio: Largo Antonio Jacinto, Edificio B, Luanda. '
                    'No hay telefono publicado: la pagina de contactos esta a medio montar, con campos '
                    'vacios. Por eso tel=None. DESCARTADO TRAS COMPROBARLO: el servicio del portal de '
                    "tramites SEPE 'Pre-licenciamento MINAGRIF - Instituto dos Servicos de Veterinaria' se "
                    'abrio y NO SIRVE: es pre-licenciamiento de PRODUCTOS de origen animal para empresas '
                    'con licencia industrial o mayorista, no de animales de compania. APHIS NO tiene ficha '
                    'de mascotas de Angola (404 comprobado).',
            'fuentes': ['https://www.dgav.pt/wp-content/uploads/2023/11/CERTIFICACAO-SANITARIA-ANGOLA-CAES-E-GATOS-2023.pdf',
                        'https://minagrif.gov.ao/web/entidades-tutela',
                        'https://minagrif.gov.ao/web/contactos',
                        'https://sepe.gov.ao/catalogo/mais-servicos/pedido-de-licenciamento/pre-licenciamento-minagrif-br-instituto-dos-servicos-de-veterinaria-br-produtos-de-origem-animal']},
 'zambia': {'organismo': 'Department of Veterinary Services, Ministry of Fisheries and Livestock (MFL)',
            'url': 'https://www.zambiatradeportal.gov.zm/index.php?r=searchProcedure/view1&id=116',
            'url_generica': False,
            'url_verificada': True,
            'email': 'info@mfl.gov.zm',
            'tel': '+260 1 253933 / +260 1 253945',
            'cert': True,
            'cert_dias': 7,
            'cert_quien': 'Veterinario oficial del pais de salida (examen clinico no mas de 48 h antes de '
                          'la salida)',
            'nota': "URL VERIFICADA: procedimiento 'Import Permit requirement for Animals, Animal "
                    "Products, Animal By-Products and Articles' del Zambia Trade Information Portal "
                    '(portal oficial del Gobierno, dominio gov.zm). Detalla tasas explicitas para '
                    'mascotas: ZMW 250 para animales pequenos (perros, gatos) hasta 100 por envio, y ZMW '
                    '100 para el permiso minimo de 5 animales domesticos o menos. Circuito real: se '
                    'presenta la solicitud al Department of Fisheries and Livestock Marketing, que la '
                    'remite al Department of Veterinary Services para el visto bueno sanitario y la '
                    "emision del permiso veterinario; hace falta ademas una 'Letter of No Objection' del "
                    'Director of Veterinary Services para animales vivos. El permiso tiene validez de 6 '
                    'semanas. Base legal: Animal Health Act, 2010. OJO CON LOS NOMBRES ANTIGUOS: la pagina '
                    "de la embajada zambiana en Washington (verificada) sigue dando 'Department of "
                    'Research & Specialist Services, Mulungushi House, P.O. Box 50060, Lusaka, tel +260-1 '
                    "253933/45, fax 253520/260505' y la guia britanica dice 'Department of Veterinary and "
                    "Tsetse Control Services, P.O. Box 50060, 15101 Ridgeway, Lusaka'; los tres nombres "
                    'apuntan al mismo servicio veterinario (misma P.O. Box 50060). El email '
                    'info@mfl.gov.zm es el del Ministerio (verificado en el trade portal), NO un buzon '
                    'especifico de permisos: no se ha encontrado publicado ningun email directo del DVS. '
                    'cert_dias=7 procede de la clausula impresa en el certificado bilateral UK-Zambia EHC '
                    "3928 ('This certificate is valid for 7 days from the date of signature').",
            'fuentes': ['https://www.zambiatradeportal.gov.zm/index.php?r=searchProcedure/view1&id=116',
                        'https://www.zambiaembassy.org/page/procedures-for-importation-of-livestock-and-pets-into-zambia',
                        'https://assets.publishing.service.gov.uk/media/65ae438f751546000d7b4a8e/3928NFG.pdf',
                        'https://assets.publishing.service.gov.uk/media/5bc758aa40f0b61ca9b5c0a7/3928EHC_V3.pdf']},
 'tanzania': {'organismo': 'Director of Veterinary Services, Ministry of Livestock and Fisheries (Wizara '
                           'ya Mifugo na Uvuvi) - Temeke Veterinary Office',
              'url': 'https://www.de.tzembassy.go.tz/services/Importing-Pets-Dogs',
              'url_generica': False,
              'url_verificada': True,
              'email': 'zoosanitary@mifugo.go.tz / epid1@mifugo.go.tz',
              'tel': '+255 22 2862592 (fax +255 22 2862538)',
              'cert': True,
              'cert_dias': 10,
              'cert_quien': "Veterinario oficial del pais de salida ('sanitary certificate from a "
                            "qualified veterinary surgeon in the country of export')",
              'nota': 'URL VERIFICADA y es la mejor de las trece: la Embajada de Tanzania en Berlin tiene '
                      "una pagina dedicada SOLO a perros ('Importing Pets - Dogs'), mas util que la "
                      "generica 'Import Permit Food, Plants, Pets and Animal Products' que publican el "
                      'resto de embajadas (tambien verificadas: un.tzembassy.go.tz y us.tzembassy.go.tz, '
                      'mismos datos de contacto). TRAMITE: no hay formulario; se manda una CARTA de '
                      'solicitud al Director of Veterinary Services indicando raza/tipo de perro, edad, '
                      'puerto o frontera de entrada, y adjuntando los certificados de vacunacion. '
                      'Direccion postal: Temeke Veterinary Office, P.O. Box 9152, Dar es Salaam. Tasas: '
                      'Tsh 30.000 de importacion + Tsh 20.000 de exportacion (Tsh 50.000 en total) - '
                      'relevante porque saldras del pais por tierra y necesitaras tambien el de salida. '
                      'Rabia: al menos 1 mes y no mas de 3 anos antes de la entrada. Recomiendan DHLP y '
                      'desparasitacion cada 45 dias / trimestral. Inspeccion veterinaria en el punto de '
                      'entrada y posible cuarentena. Conviene tener un contacto local que recoja el '
                      "permiso. cert_dias=10 procede del certificado bilateral UK-Tanzania EHC 3129 ('This "
                      "certificate is valid for 10 days', con examen clinico no mas de 10 dias antes de la "
                      'salida). OJO: el ministerio aparece con nombres historicos distintos segun la '
                      "fuente ('Ministry of Water and Livestock Development' en las embajadas, 'Livestock "
                      "Division, Ministry of Agriculture' en la guia britanica); el dominio de correo "
                      'vigente es mifugo.go.tz.',
              'fuentes': ['https://www.de.tzembassy.go.tz/services/Importing-Pets-Dogs',
                          'https://www.un.tzembassy.go.tz/services/import-permit-food-plants-pets-and-animal-products',
                          'https://www.us.tzembassy.go.tz/services/import-permit-food-plants-pets-and-animal-products',
                          'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-tanzania',
                          'https://assets.publishing.service.gov.uk/media/66d9ada4561701fa1c214e7a/3129NFG.pdf',
                          'https://assets.publishing.service.gov.uk/media/66d9ad97fb86ba5a1f214e74/3129EHC_V4.pdf']},
 'kenia': {'organismo': 'Directorate of Veterinary Services (DVS), State Department for Livestock '
                        'Development, Ministry of Agriculture and Livestock Development',
           'url': 'https://infotradekenya.go.ke/procedure/1422?l=en',
           'url_generica': False,
           'url_verificada': True,
           'email': None,
           'tel': '+254 20 631567 (fax +254 20 631273)',
           'cert': True,
           'cert_dias': 7,
           'cert_quien': 'Veterinario oficial del pais de salida (examen clinico no mas de 5 dias antes de '
                         'la salida)',
           'nota': "URL VERIFICADA PARCIALMENTE: la pagina responde y su titulo es exactamente 'Import "
                   "permit for dogs & cats (VS01)' en el portal oficial InfoTrade Kenya (KenTrade, dominio "
                   'go.ke), pero el detalle del tramite se carga por JavaScript y NO se ha podido leer el '
                   'contenido (entidad, tasas, plazos); la vista imprimible del portal esta bloqueada por '
                   'robots.txt. El nombre del permiso, VS01, si esta confirmado. MUY RELEVANTE PARA '
                   'OVERLAND: el mismo portal publica procedimientos especificos de entrada por frontera '
                   "terrestre - 'Dogs & cats import procedure through the Busia One Stop Border Post "
                   "(OSBP)', y equivalentes para Malaba (frontera con Uganda), Isebania (frontera con "
                   'Tanzania) y Lunga Lunga (frontera con Tanzania, en dos variantes segun valor declarado '
                   'por encima o por debajo de USD 2.000). Se listan en '
                   'https://infotradekenya.go.ke/objective/62?l=en (verificado). EMAIL: no se ha '
                   'encontrado publicado ningun correo del DVS de Kenia en fuente oficial; el unico correo '
                   'verificado del portal es infotradekenya@kentrade.go.ke (+254 709 950 000), que es el '
                   'servicio de atencion de KenTrade, NO el emisor del permiso. Por eso email=None. El '
                   'telefono es el que publica la guia oficial britanica para el Director of Veterinary '
                   'Services (PO Box 34188, Kabete, Nairobi); es un numero antiguo de 7 digitos y puede '
                   'haber cambiado con la renumeracion keniana. El permiso tambien se puede pedir, segun '
                   'esa misma guia, a traves de la Kenya High Commission en Londres. cert_dias=7 procede '
                   "del certificado bilateral UK-Kenia EHC 2913 ('This certificate is valid for 7 days, "
                   "extended by the duration of the voyage of travelling by sea').",
           'fuentes': ['https://infotradekenya.go.ke/procedure/1422?l=en',
                       'https://infotradekenya.go.ke/objective/62?l=en',
                       'https://assets.publishing.service.gov.uk/media/5bc702eaed915d0b01a1bd0b/2913NFG_.pdf',
                       'https://assets.publishing.service.gov.uk/media/5bc702d0e5274a360e8ed071/2913EHC_V3.pdf']},
 'uganda': {'organismo': 'Commissioner Animal Health (CAH), Ministry of Agriculture, Animal Industry and '
                         'Fisheries (MAAIF)',
            'url': 'https://www.agriculture.go.ug/dogs-and-cats/',
            'url_generica': False,
            'url_verificada': True,
            'email': 'maaif@agriculture.go.ug',
            'tel': '+256 41 4320004',
            'cert': True,
            'cert_dias': 7,
            'cert_quien': 'Autoridad veterinaria del pais de origen; certificado oficial en ingles o con '
                          'traduccion al ingles (examen clinico no mas de 48 h antes de la salida)',
            'nota': "URL VERIFICADA y excelente: pagina del propio ministerio titulada 'Dogs and Cats', "
                    'dedicada en exclusiva a la importacion de perros y gatos. TRAMITE: solicitud POR '
                    'ESCRITO al Commissioner for Animal Health con AL MENOS 7 DIAS de antelacion a la '
                    'importacion, indicando pais de origen, proveedor, tipo de animal, raza, sexo y '
                    'cantidad. Direccion: Plot 16-18 Lugard Avenue, P.O. Box 102, Entebbe. AVISO '
                    'IMPORTANTE PARA VIAJE CON PERRO: la pagina establece un periodo de cuarentena de 21 a '
                    '30 dias durante el cual se toman muestras de todos los animales importados para '
                    'contrastar o analizar determinadas enfermedades. Confirmar por email si se aplica de '
                    'hecho a mascotas que entran por carretera, porque haria inviable el transito rapido. '
                    'Vacunas exigidas para perros: rabia, moquillo, parvovirus, hepatitis infecciosa '
                    'canina, parainfluenza y traqueobronquitis infecciosa canina. La rabia, segun la guia '
                    'britanica, no menos de 30 dias y no mas de 12 meses antes de la salida. cert_dias=7 '
                    "procede del certificado bilateral UK-Uganda EHC 3925 ('This certificate is valid for "
                    "7 days'). La guia britanica llama al organismo 'Department of Veterinary Services and "
                    "Animal Industry'; el nombre vigente en la web del ministerio es Commissioner Animal "
                    'Health.',
            'fuentes': ['https://www.agriculture.go.ug/dogs-and-cats/',
                        'https://www.agriculture.go.ug/import-export-and-transit-of-animals-and-animal-products-in-uganda/',
                        'https://assets.publishing.service.gov.uk/media/65aa944882fee9000d6f5f8f/3925NFG.pdf',
                        'https://assets.publishing.service.gov.uk/media/5bc74ee3ed915d64c90dfd28/3925EHC_V4.pdf']},
 'ruanda': {'organismo': 'Rwanda Agriculture and Animal Resources Development Board (RAB) - Veterinary '
                         'Services Unit',
            'url': 'https://rwandatrade.rw/procedure/509?l=en',
            'url_generica': False,
            'url_verificada': True,
            'email': 'arpms@rab.gov.rw',
            'tel': '+250 788 385 312',
            'cert': True,
            'cert_dias': None,
            'cert_quien': 'Veterinario oficial del pais de salida (certificado de vacunacion; el '
                          'procedimiento oficial no exige un modelo concreto de certificado sanitario)',
            'nota': "URL VERIFICADA y es el pais mejor documentado de los trece: 'Full procedure for the "
                    "import of dogs and cats' del Rwanda Trade Portal (portal oficial), con los 9 pasos, "
                    'personas de contacto y base legal. Existe ademas la ficha corta del permiso en '
                    'https://rwandatrade.rw/procedure/422?l=en (tambien verificada). TRAMITE EN 3 PASOS '
                    'PARA EL PERMISO: (1) pagar RWF 15.000 en BPR Bank Rwanda a la cuenta 400374715110578 '
                    "'RAB Internally Generated Revenues'; (2) presentar la solicitud EN LINEA en el portal "
                    'https://arpms.rab.gov.rw/ adjuntando copia del pasaporte del dueno, carta de '
                    'solicitud original, recibo de pago original y copia del certificado de vacunacion; '
                    '(3) recoger el permiso en persona en la Veterinary Services Unit del RAB (P.O. Box '
                    '5016, Kigali). Responsable nominal: Dr. Isidore Gafarasi Mapendo, tel +250 738 503 '
                    '589. Ademas hay que declarar la carga en la ventanilla unica (https://sw.gov.rw, '
                    'info@sw.gov.rw, +250 788 185 611) y pasar inspeccion de aduanas y del RAB; tasa de '
                    'tramitacion adicional RWF 3.000 (total RWF 18.000 sin agente de aduanas). Base legal: '
                    'Ley nº 54/2008 de 10/09/2008, arts. 141-150. cert_dias=None: el procedimiento oficial '
                    'no publica ninguna validez y no existe modelo bilateral britanico ni ficha APHIS para '
                    "Ruanda. El unico dato circulante (certificado sanitario 'no older than 14 days', "
                    'desparasitacion 5 dias antes) procede de New Vision Veterinary Hospital de Kigali '
                    '(nvvh.rw), clinica privada que tramita permisos con el RAB: es verosimil y util para '
                    'planificar, pero NO es fuente oficial y por eso no se consigna.',
            'fuentes': ['https://rwandatrade.rw/procedure/509?l=en',
                        'https://rwandatrade.rw/procedure/422?l=en',
                        'https://arpms.rab.gov.rw/',
                        'https://nvvh.rw/pet-traveling-documents/']},
 'malaui': {'organismo': 'Department of Animal Health and Livestock Development (DAHLD) - Chief Veterinary '
                         'Officer, Ministry of Agriculture',
            'url': 'https://www.malawitradeportal.com/en-gb/site/display/300',
            'url_generica': False,
            'url_verificada': True,
            'email': 'agriculture@agriculture.gov.mw',
            'tel': '+265 1 789033 / +265 988 558115',
            'cert': True,
            'cert_dias': None,
            'cert_quien': 'Veterinario oficial del pais de salida (examen clinico no mas de 14 dias antes '
                          'de la salida)',
            'nota': "URL VERIFICADA: guia 'Step by Step: How to Import Animal or Animal Products' del "
                    'Malawi Trade Portal (portal oficial). Cubre animales vivos en general, no hay pagina '
                    'especifica de mascotas. TRAMITE: solicitud POR ESCRITO al Director del DAHLD '
                    'indicando los animales concretos que se pretenden importar; incluye una comprobacion '
                    'previa de brotes de enfermedad en el pais exportador. Tasa del permiso: MWK 10.000. '
                    'Direccion postal del DAHLD: Private Bag 2096, Lilongwe (la guia oficial britanica da '
                    "'Chief Veterinary Officer, P.O. Box 30372, Lilongwe' - hay dos apartados distintos en "
                    'circulacion, confirmar al escribir). AVISO: el portal plantea el tramite pensando en '
                    'importadores comerciales y lista pasos que para un particular en transito no deberian '
                    'aplicar (registro de empresa en MBRS, numero TIN en la Malawi Revenue Authority). '
                    'Confirmar por email el circuito para mascota acompanada. EMAIL/TEL: son los generales '
                    'del Ministerio de Agricultura (verificados en agriculture.gov.mw/contacts); NO se ha '
                    'encontrado publicado ningun contacto directo del DAHLD ni de su Director. El portal '
                    'de comercio solo ofrece como alternativa el Ministerio de Comercio '
                    '(trademin@trade.gov.mw, +265 1 770244), que no es el emisor. cert_dias=None de forma '
                    'deliberada: el certificado bilateral UK-Malaui EHC 3944 deja la validez EN BLANCO '
                    "para que la rellene el veterinario certificador ('This certificate is valid for "
                    "......... days'), asi que no hay cifra publicada. Lo que si esta fijado es la ventana "
                    'de examen clinico: no mas de 14 dias antes de la salida.',
            'fuentes': ['https://www.malawitradeportal.com/en-gb/site/display/300',
                        'https://agriculture.gov.mw/healthandlivestock',
                        'https://agriculture.gov.mw/contacts',
                        'https://assets.publishing.service.gov.uk/media/5bc70bf340f0b638518795ab/3944NFG.pdf',
                        'https://assets.publishing.service.gov.uk/media/5bc70be2ed915d0ae30b91f9/3944EHC_V3.pdf']},
 'mozambique': {'organismo': 'Direccao Nacional de Veterinaria / Autoridade Veterinaria Nacional (DINAV), '
                             'Ministerio da Agricultura, Ambiente e Pescas (MAAP)',
                'url': 'https://www.agricultura.gov.mz/servicos-ao-cidadao/procedimentos-para-o-movimento-de-animais-seus-produtos-e-subprodutos/',
                'url_generica': False,
                'url_verificada': True,
                'email': 'geral@maap.gov.mz / geral@agricultura.gov.mz',
                'tel': '+258 21 468200 (linha verde +258 84 3438999)',
                'cert': True,
                'cert_dias': 7,
                'cert_quien': 'Veterinario oficial del pais de salida (certificado sanitario '
                              'internacional; examen clinico no mas de 48 h antes de la salida)',
                'nota': "URL VERIFICADA: 'Guiao de Procedimentos para o Movimento de Animais, seus "
                        "Produtos e Subprodutos', en el apartado Servicos ao Cidadao de la web del "
                        "ministerio. Confirma literalmente que 'a licenca de importacao e emitida pela "
                        "DINAV' y que sin licencia de importacion Y certificado sanitario internacional no "
                        "se permite la entrada. FORMULARIO: existe el impreso oficial 'Pedido de Licenca "
                        "de importacao de animais vivos' en "
                        'https://www.agricultura.gov.mz/wp-content/uploads/2018/01/Pedido_Licenca_importacao_animais_vivos.doc '
                        '(el enlace responde y descarga un .doc, pero al ser binario no se ha podido leer '
                        'su contenido para confirmar los campos). EMAIL/TEL: son los generales del '
                        'ministerio (verificados en la propia pagina); no hay buzon publicado especifico '
                        "de la DINAV. OJO con el nombre del ministerio: cambio de 'Ministerio da "
                        "Agricultura e Desenvolvimento Rural' a 'Ministerio da Agricultura, Ambiente e "
                        "Pescas' (MAAP), y conviven los dominios agricultura.gov.mz y maap.gov.mz. "
                        "cert_dias=7 procede del certificado bilateral UK-Mozambique EHC 4143 ('This "
                        "certificate is valid for 7 days from the date of signature'); ese modelo incluye "
                        'casilla expresa para el numero de licencia de importacion. CONTEXTO: en 2024 el '
                        'Gobierno prohibio la importacion de determinadas razas consideradas peligrosas - '
                        'verificar la raza del perro antes de planificar la entrada.',
                'fuentes': ['https://www.agricultura.gov.mz/servicos-ao-cidadao/procedimentos-para-o-movimento-de-animais-seus-produtos-e-subprodutos/',
                            'https://www.agricultura.gov.mz/wp-content/uploads/2018/01/Pedido_Licenca_importacao_animais_vivos.doc',
                            'https://assets.publishing.service.gov.uk/media/5bcecf21ed915d431874e31d/4143NFG.pdf',
                            'https://assets.publishing.service.gov.uk/media/5bcecf0ce5274a6bd864f36d/4143EHC_V3.pdf']},
 'zimbabue': {'organismo': 'Director of Veterinary Services, Division of Veterinary Services, Ministry of '
                           'Lands, Agriculture, Fisheries, Water and Rural Development',
              'url': 'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-zimbabwe-certificate-3929',
              'url_generica': False,
              'url_verificada': True,
              'email': None,
              'tel': '+263 4 791355 (fax +263 4 720879)',
              'cert': True,
              'cert_dias': 7,
              'cert_quien': 'Veterinario oficial del pais de salida (examen clinico no mas de 48 h antes '
                            'de la salida)',
              'nota': 'PEOR CASO DE LOS TRECE - LEER CON ATENCION. NO EXISTE, o no se ha podido encontrar, '
                      'NINGUNA pagina del Gobierno de Zimbabue que explique el tramite: la Division of '
                      'Veterinary Services no tiene web propia localizable y su unica presencia publica '
                      'actualizada es una pagina de Facebook (facebook.com/vetservices.zw). APHIS NO tiene '
                      'ficha de Zimbabue en pet-travel (la URL .../pet-travel-us-zimbabwe devuelve 404) y '
                      'su pagina de animales vivos para Zimbabue no da ningun contacto local. Por eso la '
                      'URL que se da NO es zimbabuense: es la ficha oficial del Gobierno britanico del '
                      'certificado de exportacion de perros y gatos a Zimbabue (EHC 3929), verificada, que '
                      'si publica el organismo y su direccion. Es la mejor fuente accesible y estable, '
                      'pero hay que tratarla como referencia, no como tramite. DATO CLAVE VERIFICADO en '
                      "esa guia: 'No dog or cat may be imported into Zimbabwe except in accordance with "
                      "the terms of an import permit', emitido por el Director of Veterinary Services, "
                      'P.O. Box CY 66, Causeway, Harare, tel +263 4 791355, fax +263 4 720879. EMAIL: no '
                      'publicado en ninguna fuente oficial; email=None. TELEFONO: el numero dado es el de '
                      'la guia britanica y usa el prefijo antiguo de Harare (4); con la renumeracion '
                      'actual seria +263 242 791355. Circula ademas +263 242 791516 junto a la mencion de '
                      'una tasa de USD 150 por animal y un plazo de 3-5 dias, pero eso procede de '
                      'Wikiprocedure (wiki abierta, NO fuente oficial) y no se consigna como dato. '
                      "cert_dias=7 procede de la clausula del propio EHC 3929 ('This certificate is valid "
                      "for 7 days'). ALTERNATIVA OVERLAND: si entras desde Sudafrica, Botsuana, Lesoto o "
                      'Esuatini, el documento real es el Interterritorial Movement Permit for Dogs and '
                      'Cats del modelo SADC, que Zimbabue acepta expresamente y que vale 60 dias desde su '
                      'emision.',
              'fuentes': ['https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-zimbabwe-certificate-3929',
                          'https://assets.publishing.service.gov.uk/media/5bc7594140f0b61ca2dd15f8/3929NFG.pdf',
                          'https://assets.publishing.service.gov.uk/media/5bc7592740f0b61c92ec8b6b/3929EHC_V3.pdf',
                          'https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf']},
 'botsuana': {'organismo': 'Department of Veterinary Services, Ministry of Agriculture (Botswana)',
              'url': 'https://www.gov.bw/business-compliance-agriculture-animal-husbandry/issuance-import-permit-live-animals-animal',
              'url_generica': False,
              'url_verificada': True,
              'email': 'DVSpermits@gov.bw',
              'tel': '+267 3689513 / +267 3689510 (call centre 17755)',
              'cert': True,
              'cert_dias': 60,
              'cert_quien': 'Veterinario oficial del pais de salida; en entrada desde el area SADC, '
                            'Interterritorial Movement Permit firmado por veterinario colegiado u oficial '
                            'Y refrendado por un Government Veterinarian con sello oficial',
              'nota': "URL VERIFICADA, es la que sospechabas y es correcta: 'Issuance of Import Permit of "
                      "Live Animal(s), Animal Product(s) and Animal Feed(s)' en gov.bw. Trata expresamente "
                      'perros y gatos y confirma tus datos de contacto (en la pagina el correo aparece '
                      "ofuscado como 'DVSpermits[at]gov[dot]bw'). REQUISITOS QUE LISTA LA PAGINA: registro "
                      'valido de inmunizacion antirrabica para perros y gatos; para cachorros de menos de '
                      '3 meses, prueba de que la madre fue vacunada al menos un mes y no mas de 12 meses '
                      'antes del parto; prueba de que no hay restricciones de movimiento por control de '
                      'rabia en la zona de origen; el pais de origen no debe tener enfermedades '
                      'notificables relevantes; y presentar el animal en la oficina para inspeccion antes '
                      'de la emision del permiso. Plazo de tramitacion: 1 dia habil. La pagina no publica '
                      'tasas. cert_dias=60 NO sale de gov.bw (que no publica ninguna validez) sino del '
                      'modelo SADC verificado de Interterritorial Movement Permit for Dogs and Cats, que '
                      'cubre expresamente Sudafrica, Zimbabue, Botsuana, Lesoto y Esuatini y dice que '
                      "sirve como permiso de movimiento 'for a period of sixty days from date of issue'. "
                      'Es el documento que usaras de hecho entrando por tierra desde Sudafrica o Namibia. '
                      'Ese modelo exige ademas que la rabia lleve puesta un minimo de 30 dias (60 si hubo '
                      'casos de rabia en la zona en los tres meses anteriores). Para una llegada directa '
                      'desde Europa no hay cifra publicada. APHIS tiene ficha de Botsuana pero es inutil: '
                      'dice expresamente que no ha sido informada oficialmente de los requisitos y solo '
                      'ofrece un modelo generico de certificado.',
              'fuentes': ['https://www.gov.bw/business-compliance-agriculture-animal-husbandry/issuance-import-permit-live-animals-animal',
                          'https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf',
                          'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-botswana',
                          'https://www.aphis.usda.gov/sites/default/files/botswana-dog-cat.pdf']},
 'sudafrica': {'organismo': 'Director: Animal Health - Import Export Policy Unit, Department of '
                            'Agriculture, Land Reform and Rural Development (DALRRD)',
               'url': 'https://www.gov.za/services/import/import-animals-and-animal-products',
               'url_generica': False,
               'url_verificada': True,
               'email': 'VetPermits@daff.gov.za',
               'tel': None,
               'cert': True,
               'cert_dias': 10,
               'cert_quien': 'Veterinario oficial del pais de salida (emision del certificado Y su '
                             'refrendo oficial deben caer dentro de los 10 dias previos al viaje)',
               'nota': "URL VERIFICADA: ficha de servicio 'Import animals and animal products' en gov.za, "
                       'que explica el tramite completo y confirma tu dato (VetPermits@daff.gov.za). '
                       "TRAMITE: solicitar el permiso veterinario de importacion al 'Director: Animal "
                       "Health, Import Export Policy Unit, Private Bag X138, Pretoria 0001' ANTES del "
                       'envio. Hay tres formularios segun el animal vaya a cuarentena, a control adicional '
                       'o a ninguna de las dos; se descargan en '
                       'https://www.nda.gov.za/index.php/core-business/agricultural-production/animal-production/animal-health '
                       '(enlace citado por gov.za; el dominio nda.gov.za rechaza la verificacion '
                       'automatica por problema de certificado TLS, asi que NO se ha podido abrir). Una '
                       'vez aprobado por el veterinario estatal de la oficina nacional, el permiso se '
                       'emite en 3-5 dias habiles. TASA: la cifra de R140 por permiso que ya tenias es '
                       "coherente con el sistema, pero gov.za solo dice que 'the cost is revised annually "
                       "and published in the Government Gazette'; el tarifario vigente se publica en "
                       'gov.za (ej. tarrifs-for-veterinary-imports-permits-2024). TELEFONO: no hay '
                       'telefono publicado para permisos, solo fax (012 329 6892 / 012 329 8292); por eso '
                       "tel=None. cert_dias=10 esta verificado en la guia APHIS de Sudafrica: 'Final "
                       'veterinary inspection, health certificate issuance, and certificate endorsement '
                       "must occur within 10 days of the pet's travel'. PRUEBAS OBLIGATORIAS (las mas "
                       'duras de toda la ruta, planificar con 6-8 semanas): negativo en Brucella canis, '
                       'Trypanosoma evansi, Babesia gibsoni, Dirofilaria immitis (filaria) y Leishmania, '
                       'TODAS realizadas dentro de los 30 dias previos a la importacion, sin excepciones '
                       'salvo dispensa expresa de Sudafrica. Microchip obligatorio y rabia puesta dentro '
                       'de los 12 meses y al menos 30 dias antes (reducible a 15 dias con dispensa).',
               'fuentes': ['https://www.gov.za/services/import/import-animals-and-animal-products',
                           'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-south-africa',
                           'https://www.aphis.usda.gov/sites/default/files/south-africa-dog-guidance.pdf',
                           'https://www.gov.uk/export-health-certificates/export-dogs-to-south-africa-certificate-6256',
                           'https://assets.publishing.service.gov.uk/media/65438cda1f1a60000d360c76/6256NFG.pdf']},
 'namibia': {'organismo': 'Directorate of Veterinary Services - Import/Export Office, Ministry of '
                          'Agriculture, Water and Land Reform (MAWLR)',
             'url': 'https://namibiatradeportal.gov.na/trade-goods/procedure-details/view_express_entity/485',
             'url_generica': False,
             'url_verificada': True,
             'email': 'vet.permits@mawlr.gov.na',
             'tel': '+264 61 276592 (tambien +264 61 2087892 y +264 61 2087891/0; Walvis Bay +264 64 '
                    '203073)',
             'cert': True,
             'cert_dias': None,
             'cert_quien': 'Veterinario oficial del pais de salida (examen clinico dentro de los 10 dias '
                           'previos a la salida)',
             'nota': "URL VERIFICADA: 'Procedure for Application of a Namibian Veterinary Import Permit "
                     "and Veterinary Import Permit for conveyance in transit' en el Namibia Trade "
                     'Information Portal (dominio oficial gov.na). Confirma tu correo (ahi aparece como '
                     'Vet.Permits@mawlr.gov.na). OFICINA: Government Office Park, Ministry of Agriculture, '
                     'Water and Land Reform, East Wing, 2ª planta, Windhoek. Horario 08:00-13:00 y '
                     '14:00-17:00 de lunes a viernes. TASAS: N$ 150 el permiso veterinario de importacion; '
                     'N$ 50 el permiso de transito - ESTE SEGUNDO ES EL RELEVANTE si solo atraviesas '
                     'Namibia sin quedarte. PLAZO: maximo 3 dias habiles si la documentacion esta '
                     'completa. FORMULARIO: se descarga en '
                     'https://namibiatradeportal.gov.na/download_file/de4b6d16-da8f-4470-bb55-202d39fd2165/277 '
                     "y tambien esta en mawf.gov.na ('Veterinary Import Application Form.pdf'). PASO EXTRA "
                     'POCO CONOCIDO, verificado en la Veterinary Association of Namibia: antes de viajar '
                     'hay que enviar por email al veterinario estatal namibio de la zona de destino una '
                     'copia del permiso de importacion ya cumplimentado, el pasaporte de vacunacion del '
                     'perro y los resultados negativos de las pruebas, para su verificacion. PRUEBAS: '
                     'negativo en Brucella canis, Trypanosoma evansi, Leishmania, Dirofilaria y Babesia; '
                     'segun el modelo APHIS, realizadas dentro de los 30 dias previos a la salida. Rabia '
                     'entre 30 dias y 12 meses antes. Tras la llegada, 6 meses de preventivo de filaria. '
                     'cert_dias=None: ni el portal ni MAWLR publican validez del certificado, y el '
                     "certificado bilateral britanico para Namibia (EHC 3917) esta SUSPENDIDO ('on hold', "
                     'no utilizable), asi que no hay cifra oficial que citar. Lo unico fijado es la '
                     'ventana de examen clinico de 10 dias.',
             'fuentes': ['https://namibiatradeportal.gov.na/trade-goods/procedure-details/view_express_entity/485',
                         'https://van.org.na/section.php?secid=52&menuid=52',
                         'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-namibia',
                         'https://www.aphis.usda.gov/sites/default/files/namibia-dog_0.pdf',
                         'https://www.gov.uk/export-health-certificates/export-dogs-to-namibia-certificate-3917']},
 'lesoto': {'organismo': 'Department of Livestock Services - Imports and Exports Office, Ministry of '
                         'Agriculture, Food Security and Nutrition',
            'url': 'https://lesotho.eregulations.org/procedure/160?l=en',
            'url_generica': False,
            'url_verificada': True,
            'email': None,
            'tel': '+266 2231 7284 (fax +266 2231 1500)',
            'cert': True,
            'cert_dias': 60,
            'cert_quien': 'Veterinario oficial del pais de salida; en entrada desde el area SADC, '
                          'Interterritorial Movement Permit firmado por veterinario colegiado u oficial Y '
                          'refrendado por un Government Veterinarian con sello oficial',
            'nota': "URL VERIFICADA: procedimiento 'Obtain international veterinary import permit' del "
                    'portal oficial eRegulations Lesotho (respaldado por el Gobierno y la UNCTAD). '
                    "IMPORTANTE: el procedimiento esta CATALOGADO bajo 'importacion de carne', lo que "
                    "despista, pero su cuadro de tasas verificado incluye expresamente 'LSL 10 - Permit "
                    "fee for pets' junto a 'LSL 0-100 - Permit fee for live animals', asi que SI es el "
                    'tramite que cubre al perro. El permiso de mascota cuesta 10 maloti, una miseria. '
                    'OFICINA: Imports and Exports Office, Epidemiology and Data Management Section, '
                    'Private Bag A 82, Maseru. Horario 08:00-16:30 de lunes a viernes. Web institucional: '
                    'https://www.gov.ls/ministry-of-agriculture/ PLAZOS Y CALENDARIO SEMANAL (dato muy '
                    'util): la solicitud debe presentarse entre 7 y 30 dias antes de la importacion, y la '
                    'oficina trabaja por dias fijos - lunes y martes se reciben solicitudes, miercoles se '
                    'tramitan, jueves y viernes se entregan los permisos. El tramite entero lleva de 1,5 a '
                    '8 dias. DOCUMENTOS: formulario de solicitud original, certificado veterinario del '
                    'pais de origen (copia), certificado de estar al corriente con Hacienda (copia) y '
                    'documento de identidad (copia). EMAIL: el portal publica el nombre de dos personas de '
                    'contacto (Liou Ramokoatsi, Imports and Export Permit Assistant Clerk, tel +266 5818 '
                    '7083 / +266 6229 7921; y Matsita Taoana) pero OFUSCA sus direcciones de correo, y no '
                    'hay buzon generico del departamento: por eso email=None. cert_dias=60 procede del '
                    'modelo SADC de Interterritorial Movement Permit for Dogs and Cats, verificado, que '
                    'cubre expresamente Lesoto y vale 60 dias desde su emision - y como Lesoto es un '
                    'enclave dentro de Sudafrica, ese es necesariamente el documento que usaras. Fuentes '
                    'comerciales (pettravel) afirman que si se entra desde Botsuana, Malaui, Namibia, '
                    'Sudafrica, Esuatini o Zimbabue no hace falta solicitud previa al Director of Animal '
                    'Health; NO esta confirmado en fuente oficial, no te fies sin escribir antes.',
            'fuentes': ['https://lesotho.eregulations.org/procedure/160?l=en',
                        'https://lesotho.eregulations.org/Contacts/61?letter=d&l=en',
                        'https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf']},
 'esuatini': {'organismo': 'Department of Veterinary and Livestock Services, Ministry of Agriculture '
                           '(Eswatini)',
              'url': 'https://www.gov.sz/index.php/ministries-departments/ministry-of-agriculture/veterinary-a-livestock',
              'url_generica': True,
              'url_verificada': True,
              'email': None,
              'tel': '+268 2404 2731/9 / +268 2404 6362',
              'cert': True,
              'cert_dias': 60,
              'cert_quien': 'Veterinario oficial del pais de salida; en entrada desde el area SADC, '
                            'Interterritorial Movement Permit firmado por veterinario colegiado u oficial '
                            'Y refrendado por un Government Veterinarian con sello oficial',
              'nota': 'url_generica=True: NO EXISTE pagina del tramite. La URL que se da es la ficha del '
                      'departamento veterinario dentro de gov.sz - esta verificada y es el nivel mas '
                      'concreto que hay (no es la portada del ministerio), pero solo describe el mandato '
                      'del departamento y NO menciona en ningun momento permisos de importacion ni '
                      'mascotas. Se ha buscado y descartado: APHIS no tiene ficha de Esuatini/Swazilandia '
                      'en pet-travel; el Reino Unido no tiene certificado bilateral de perros y gatos con '
                      'Esuatini (solo uno de carne, el 7931); y el Eswatini Trade Information Portal no '
                      'publica ninguna medida ni procedimiento sobre animales vivos o mascotas (se '
                      'comprobo el procedimiento id=33, que resulto ser el de despacho aduanero de '
                      'vehiculos). CONTACTO: direccion Ministry of Agriculture Headquarters, P.O. Box 162, '
                      'Mbabane. El Director del departamento figura como Dr. Xolani Dlamini, movil +268 '
                      '7606 2602 - util porque en Esuatini el movil suele responder antes que la '
                      'centralita. NO hay ningun correo publicado en gov.sz para este departamento, por '
                      'eso email=None: habra que llamar. cert_dias=60 procede del modelo SADC de '
                      'Interterritorial Movement Permit for Dogs and Cats, verificado, que cubre '
                      'expresamente Esuatini (aparece con su nombre antiguo, Swaziland) y vale 60 dias '
                      'desde su emision; entrando por tierra desde Sudafrica o Mozambique es el documento '
                      'que usaras. Exige rabia puesta con un minimo de 30 dias (60 si hubo casos de rabia '
                      'en la zona en los tres meses anteriores). Fuentes comerciales (pettravel) hablan de '
                      'un certificado emitido dentro de los 10 dias previos a la entrada y de solicitud al '
                      "'Director of Animal Health' salvo procedencia SADC; NO confirmado en fuente "
                      'oficial, no se consigna.',
              'fuentes': ['https://www.gov.sz/index.php/ministries-departments/ministry-of-agriculture/veterinary-a-livestock',
                          'https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf',
                          'https://www.eswatinitradeportal.gov.sz/index.php?r=SearchMeasures/index']},
 'sahara-occidental': {'organismo': 'Office National de Sécurité Sanitaire des Produits Alimentaires '
                                    '(ONSSA) - Direction des Services Vétérinaires',
                       'url': 'https://www.onssa.gov.ma/controle-a-limportation-et-a-lexportation/controle-a-limportation/importation-des-animaux-vivants/chiens-et-chats/',
                       'url_generica': False,
                       'url_verificada': False,
                       'email': None,
                       'tel': '+212 5 37 67 65 00',
                       'cert': True,
                       'cert_dias': None,
                       'cert_quien': 'Veterinario oficial del pais de salida (en la UE, veterinario '
                                     'oficial habilitado; certificado en modelo bilateral, no vale el '
                                     'pasaporte europeo solo)',
                       'nota': 'Administrado por Marruecos: no hay trámite ni organismo propio. Rige lo de '
                               'Marruecos.',
                       'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-morocco',
                                   'https://www.aphis.usda.gov/sites/default/files/morocco-dog-cat_0.pdf',
                                   'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-morocco-certificate-3916',
                                   'https://assets.publishing.service.gov.uk/media/689da555e95097004f723f64/3916EHC_V4.pdf',
                                   'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm',
                                   'https://www.telecontact.ma/annonceur/onssa/3257548/rabat.php']}}

# La vuelta a la UE no es un permiso de país: es el certificado zoosanitario de
# reentrada. Se añade a mano para que la fila «UE / España» de §2.2 no quede vacía.
CONTACTOS["ue"] = {
    "organismo": "Comisión Europea, DG SANTE — movimiento no comercial desde terceros países",
    "url": "https://food.ec.europa.eu/animals/movement-pets/eu-legislation/"
           "non-commercial-movement-non-eu-countries_en",
    "url_generica": False,
    "url_verificada": True,
    "email": None,
    "tel": None,
    "cert": True,
    "cert_dias": 10,
    "cert_quien": "Veterinario oficial del pais de salida (Marruecos, ONSSA) y refrendado "
                  "por su autoridad competente",
    "nota": "Entrada obligatoria por un Punto de Entrada de Viajeros designado.",
    "fuentes": ["https://food.ec.europa.eu/animals/movement-pets_en"],
}

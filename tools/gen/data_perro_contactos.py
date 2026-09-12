# -*- coding: utf-8 -*-
"""Quién emite el permiso del perro en cada país, y dónde se pide exactamente.

Investigado en septiembre de 2026 y AUDITADO el 12-09-2026 contra las fuentes
reales (informe «auditoria-perro-2027» del proyecto): cada URL, correo, teléfono
y plazo se ha vuelto a comprobar; lo que no se pudo abrir se dice.

Criterio del campo url: la página OFICIAL NACIONAL del organismo veterinario o
del portal de trámites del país. Los modelos de APHIS (EE. UU.), gov.uk,
dgav.pt y las webs comerciales se relegan a «fuentes»: describen el circuito de
otro país exportador, no la norma del país de destino.

Campos:
  url_verificada  False = la página existe (indexada) pero no se ha podido abrir
                  desde aquí (bloqueo, TLS roto, servidor caído); se marca en la app.
  url_generica    True  = solo se ha encontrado la portada o una página que no
                  trata expresamente de animales de compañía.
  cert_dias       Validez del certificado sanitario desde su emisión, en días
                  (3 = 72 h). None cuando el país no publica plazo: no se inventa.
  auditado        Fecha de la última verificación de la entrada.
"""

CONTACTOS = {'marruecos': {'organismo': 'Office National de Sécurité Sanitaire des Produits Alimentaires '
                            '(ONSSA) - Direction des Services Vétérinaires',
               'url': 'https://www.onssa.gov.ma/controle-a-limportation-et-a-lexportation/controle-a-limportation/importation-des-animaux-vivants/chiens-et-chats/',
               'url_generica': False,
               'url_verificada': False,
               'email': None,
               'tel': '+212 5 37 67 65 13 (Direccion de Control Fronterizo y Acuerdos SPS de '
                      'ONSSA, segun FAO/Codex) · +212 5 37 67 65 00 (solo en directorios '
                      'comerciales)',
               'cert': True,
               'cert_dias': None,
               'cert_quien': 'Veterinario oficial espanol, certificado bilateral ASE-3131 «perros '
                             'y gatos a Marruecos» tramitado por CEXGAN (digital desde el '
                             '01-09-2025, sin apostilla): chip anterior a la vacuna, vacuna '
                             'antirrabica inactivada con >=21 dias si es primovacunacion, examen '
                             'clinico en las 24 h previas al embarque y titulacion >=0,5 UI/ml '
                             'para exportacion temporal',
               'nota': 'Sin permiso previo de importacion para un perro de la UE con su dueno '
                       '(ninguno de los tres modelos oficiales, ES/UK/EEUU, lo menciona). La '
                       'pagina de ONSSA es la correcta por titulo pero no se ha podido abrir desde '
                       'el entorno de verificacion: comprobarla a mano. No hay validez publicada '
                       'en dias para el certificado espanol: lo que fija es el examen clinico en '
                       'las 24 h previas (el modelo britanico vale 7 dias y el estadounidense 3). '
                       'El «limite de 3 animales» no tiene fuente. Email oficial de ONSSA/DSV: no '
                       'publicado en fuente accesible.',
               'fuentes': ['https://servicio.mapama.gob.es/cexgan/documentacionpublica/perrosgatosmarruecosase-3131.pdf',
                           'https://colegioveterinarios.net/wp-content/uploads/2025/07/Nota-informativa-CEXGAN-Perros-y-gatos-Marruecos-2025.pdf',
                           'https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones',
                           'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-morocco-certificate-3916',
                           'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-morocco',
                           'https://www.consulat.ma/en/introduction-pets',
                           'https://www.fao.org/fao-who-codexalimentarius/about-codex/members/detail/en/c/15642/',
                           'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
               'auditado': '2026-09-12'},
 'mauritania': {'organismo': "Direction des Services Vétérinaires (DSV) / Direction de l'Élevage, "
                             "Ministère de l'Élevage (antes Ministère du Développement Rural)",
                'url': 'https://elevage.gov.mr/?lang=fr',
                'url_generica': True,
                'url_verificada': True,
                'email': None,
                'tel': None,
                'cert': True,
                'cert_dias': None,
                'cert_quien': 'Veterinario oficial del pais de salida; segun Anivetvoyage (verif. '
                              '10-10-2025) emitido <48 h antes de la salida; segun PetTravel, '
                              'dentro de los 10 dias previos. Sin cifra oficial',
                'nota': 'No existe ninguna pagina oficial mauritana ni consular con el tramite; la '
                        "web del Ministere de l'Elevage abre pero su seccion de servicios "
                        'veterinarios solo tiene noticias. Lo unico publicado son dos fichas '
                        'comerciales coincidentes: microchip, rabia puesta hace menos de 12 meses, '
                        'certificado reciente y sin titulacion; PetTravel anade que no hace falta '
                        'permiso previo para una mascota que viaja con su dueno.',
                'fuentes': ['https://www.anivetvoyage.com/formalites-pays/m/253-mauritanie.html',
                            'https://www.pettravel.com/information/pet-passports/mauritania-pet-import-requirements/',
                            'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
                'auditado': '2026-09-12'},
 'senegal': {'organismo': "Direction des Services Vétérinaires (DSV), Ministère de l'Agriculture, "
                          "de la Souveraineté Alimentaire et de l'Élevage",
             'url': 'https://senegalservices.sn/demarche/demander-lautorisation-dimporter-des-animaux-de-compagnie',
             'url_generica': False,
             'url_verificada': False,
             'email': 'contacts@elevage.gouv.sn (buzon general del ministerio) / '
                      'wadesanou@gmail.com (secretaria DSV) / dsvmepa@gmail.com (DSV, segun APHIS)',
             'tel': '+221 33 859 06 31 (ministerio, portal geosenegal.gouv.sn)',
             'cert': True,
             'cert_dias': 3,
             'cert_quien': 'Veterinario oficial del pais de salida, emitido MENOS DE 72 H antes de '
                           'la llegada (Anivetvoyage, verif. 24-01-2026); PetTravel y el modelo '
                           'britanico hablan de examen en las 48 h previas; los «21 dias» que '
                           'circulan son solo la validez del modelo estadounidense',
             'nota': 'Permiso de importacion previo obligatorio, emitido por la Direction des '
                     'Services Veterinaires (37 Avenue Pasteur, BP 67, Dakar), valido 3 meses: lo '
                     'confirman tres fuentes independientes. Rabia puesta hace mas de 1 mes y '
                     'menos de 12; titulacion no exigida; antiparasitario obligatorio. La ficha '
                     'oficial de Senegal Services tiene el titulo correcto pero no se ha podido '
                     'abrir desde el entorno de verificacion: comprobarla a mano. Ninguna fuente '
                     'publica el plazo de tramitacion.',
             'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-senegal',
                         'https://anivetvoyage.com/pays/senegal/',
                         'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-senegal-certificate-6367',
                         'https://geosenegal.gouv.sn/',
                         'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
             'auditado': '2026-09-12'},
 'gambia': {'organismo': 'Department of Livestock Services (Veterinary Services), Ministry of '
                         'Agriculture',
            'url': 'https://gambiaembassy.eu/faqs/',
            'url_generica': False,
            'url_verificada': True,
            'email': None,
            'tel': '+220 4397472',
            'cert': True,
            'cert_dias': None,
            'cert_quien': "Veterinario del pais de origen ('Veterinarian's health certificate "
                          "issued at point of origin')",
            'nota': 'La FAQ de la embajada (unica fuente) pide certificado sanitario del '
                    'veterinario de origen, cartilla de vacunas y pasaporte, con el animal '
                    '«certified as healthy, fit for travel and vaccinated for rabies»; el permiso '
                    'de importacion se obtiene registrando al animal en el Gambian Veterinary '
                    'Department DESPUES de llegar. No se ha localizado pagina del Department of '
                    'Livestock Services.',
            'fuentes': ['https://gambiaembassy.eu/faqs/',
                        'https://www.aphis.usda.gov/live-animal-export/export-live-animals-gambia'],
            'auditado': '2026-09-12'},
 'guinea': {'organismo': 'Direction Nationale des Services Vétérinaires (DNSV), Ministère de '
                         "l'Élevage et des Productions Animales",
            'url': 'https://www.elevage.gov.gn/',
            'url_generica': True,
            'url_verificada': True,
            'email': 'contact@elevage.gov.gn',
            'tel': None,
            'cert': True,
            'cert_dias': 3,
            'cert_quien': 'Veterinario oficial del pais de salida, <72 h antes de la llegada '
                          '(Anivetvoyage, verif. 06-04-2024; sin fuente oficial guineana)',
            'nota': "No hay pagina oficial del tramite: la web del Ministere de l'Elevage es solo "
                    "portada (su telefono es un numero de relleno). El Code de l'Elevage (Loi "
                    'L/2018/026/AN, art. 41) somete a control veterinario todo animal vivo que '
                    'entre «par voie terrestre, ferroviaire, fluviale, maritime ou aerienne» y el '
                    'art. 150 prohibe importar perros de primera categoria. Anivetvoyage: '
                    'microchip, rabia <12 meses, certificado <72 h, sin titulacion. Sin testimonio '
                    'de cruce con perro.',
            'fuentes': ['https://cnt.gov.gn/archive.assemblee/www.assemblee.gov.gn/conakry-le-03-juillet-2018-l2018026an-loi-portant-code-de-lelevage-et-des-produits-animaux.html',
                        'https://www.anivetvoyage.com/formalites-pays/g/301-guinee.html',
                        'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-guinea',
                        'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
            'auditado': '2026-09-12'},
 'sierra-leona': {'organismo': 'Livestock and Veterinary Services Division, Ministry of '
                               'Agriculture, Forestry and Food Security (MAFFS)',
                  'url': 'https://maf.gov.sl/',
                  'url_generica': True,
                  'url_verificada': True,
                  'email': None,
                  'tel': None,
                  'cert': True,
                  'cert_dias': 7,
                  'cert_quien': 'Veterinario oficial del pais de salida; el modelo britanico (EHC '
                                '6548) vale 7 dias y admite incluso animal no vacunado de rabia',
                  'nota': 'No existe ninguna pagina oficial sierraleonesa sobre importacion de '
                          'animales de compania: la web del Ministry of Agriculture and Food '
                          'Security es solo portada y el Unified Permit Portal no se ha podido '
                          'abrir. La unica descripcion del regimen es el certificado bilateral '
                          'britanico.',
                  'fuentes': ['https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-sierra-leone-certificate-6548',
                              'https://assets.publishing.service.gov.uk/media/65ae3d20751546000d7b4a8d/6548EHC_V3.pdf',
                              'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
                  'auditado': '2026-09-12'},
 'liberia': {'organismo': 'Ministry of Agriculture — Animal Resources Division (su director es el '
                          'Chief Veterinary Officer); el «Pet Clearance» previo lo expiden tambien '
                          'los consulados y embajadas de Liberia',
             'url': 'https://www.moa.gov.lr/general/sps-national-enquiry-pointnational-notification-authority',
             'url_generica': False,
             'url_verificada': True,
             'email': 'gvoupawoe@moa.gov.lr (CVO) / SPSNEP@moa.gov.lr / '
                      'info@liberiaconsulate-ny.com (consulado NY)',
             'tel': '+231 886 400 600 (CVO) · +231 880 745 449 (SPS NEP) · +1 212 687 1025 '
                    '(consulado NY)',
             'cert': True,
             'cert_dias': 30,
             'cert_quien': 'Veterinario colegiado del pais de salida, fechado no mas de 30 dias '
                           'antes de la llegada (pet clearance consular); el ministerio pide '
                           'ademas las pegatinas de las vacunas en el certificado',
             'nota': 'La pagina del Ministry of Agriculture describe el procedimiento: carta de '
                     'solicitud al Director of Animal Resources «for companion or domestic '
                     'animals», certificado sanitario con las pegatinas de vacunacion, y permisos '
                     'expedidos en 48 h. El consulado de Nueva York y la embajada en Washington '
                     'ofrecen un «Pet Clearance» previo por 100 USD (giro postal, no '
                     'reembolsable). Liberia no tiene embajada en Espana.',
             'fuentes': ['https://liberiaconsulate-ny.com/consulate-services/pet-clearance/',
                         'https://liberianembassyus.org/document/requirements-for-pet-travel-to-liberia',
                         'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
             'auditado': '2026-09-12'},
 'costa-de-marfil': {'organismo': 'Direction des Services Vétérinaires (DSV), Ministère des '
                                  'Ressources Animales et Halieutiques',
                     'url': 'https://www.gucecotedivoire.ci/pwic/animaux-vivants/',
                     'url_generica': True,
                     'url_verificada': True,
                     'email': 'carv.dsvci@gmail.com / dsv.sdsa2017@gmail.com (ambos publicados por '
                              'APHIS para pedir el permiso)',
                     'tel': '+225 27 20 21 89 72 (DSV, Cite Administrative Tour C 11.º, '
                            'Abidjan-Plateau; el prefijo 27 es la renumeracion de 2021 y no esta '
                            'verificado por llamada)',
                     'cert': True,
                     'cert_dias': 10,
                     'cert_quien': 'Veterinario oficial/acreditado del pais de salida, refrendado '
                                   'por la autoridad veterinaria nacional dentro de los 10 dias '
                                   'previos al viaje (dato del modelo estadounidense; sin cifra '
                                   'marfilena)',
                     'nota': 'Permiso previo confirmado: existe formulario oficial del Ministere '
                             'des Ressources Animales et Halieutiques / DSV para «carnivores '
                             'domestiques» (reproducido por APHIS), que se pide por correo '
                             'adjuntando el certificado antirrabico. La ventanilla unica GUCE '
                             'describe la importacion de animales vivos (autorizacion previa del '
                             'MIRAH + laissez-passer sanitario de la DSV) pero no menciona '
                             'mascotas; ninguna pagina marfilena lo hace. Rabia: al menos 21 dias '
                             'tras primovacunacion.',
                     'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ivory-coast',
                                 'https://www.aphis.usda.gov/sites/default/files/ptw-ivory-coast-import-permit-application.pdf',
                                 'https://ressourcesanimales.gouv.ci/direction/direction-des-services-veterinaires-dsv/',
                                 'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
                     'auditado': '2026-09-12'},
 'ghana': {'organismo': 'Veterinary Services Directorate / Department (VSD), Ministry of Food and '
                        'Agriculture (MoFA)',
           'url': 'https://mofa.gov.gh/site/directorates/technical-directorates/veterinary-services',
           'url_generica': True,
           'url_verificada': True,
           'email': 'vsd@mofa.gov.gh',
           'tel': '+233 24 264 9497 (linea de emergencia de la VSD; los otros dos numeros de su '
                  'web son de relleno)',
           'cert': True,
           'cert_dias': 30,
           'cert_quien': "Veterinario oficial del pais de salida ('International Health "
                         "Certificate'); los 30 dias son la validez del modelo estadounidense, no "
                         'una norma ghanesa publicada',
           'nota': 'Permiso de importacion previo (PetTravel: valido 8 semanas; wikiprocedure: '
                   'solicitud escrita con al menos 7 dias de antelacion), rabia entre 30 dias y 6 '
                   'meses antes, microchip ISO. La pagina especifica «Import Requirements» de '
                   'vsd.gov.gh (/255-2/) existe pero no se ha podido abrir: comprobarla a mano. El '
                   'plazo «2-4 semanas» no tiene fuente.',
           'fuentes': ['https://vsd.gov.gh/255-2/',
                       'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ghana',
                       'https://www.pettravel.com/information/pet-passports/ghana-pet-import-requirements/',
                       'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
           'auditado': '2026-09-12'},
 'togo': {'organismo': "Ministère de l'Agriculture, de la Production Animale (Ressources Animales) "
                       'et de la Souveraineté Alimentaire (MAPRASA) - servicios veterinarios / '
                       "Direction de l'Élevage",
          'url': 'https://agriculture.gouv.tg/',
          'url_generica': True,
          'url_verificada': True,
          'email': None,
          'tel': None,
          'cert': True,
          'cert_dias': 3,
          'cert_quien': 'Veterinario oficial del pais de salida, o veterinario habilitado con '
                        'refrendo de veterinario oficial',
          'nota': 'Ninguna pagina togolesa trata de animales vivos ni mascotas (el portal de '
                  'tramites del Estado dice «Aucun service digitalise pour le moment»). Fuentes '
                  'comerciales coincidentes: certificado emitido no mas de 3 dias antes de la '
                  'llegada, rabia >21 dias y <12 meses, microchip recomendado. PetTravel: permiso '
                  'de importacion exigido salvo que se llegue desde una lista cerrada de paises '
                  '(Benin, Burkina, Camerun, Costa de Marfil, Francia, Gabon, Mali, Mauritania, '
                  'Niger, Senegal...): ni Ghana ni Espana estan en ella. Direccion postal (WOAH): '
                  "Direction de l'Elevage, 59 rue de la Kozah, Lome.",
          'fuentes': ['https://www.pettravel.com/information/pet-passports/togo-pet-import-requirements/',
                      'https://www.anivetvoyage.com/formalites-pays/t/174-togo.html',
                      'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
          'auditado': '2026-09-12'},
 'benin': {'organismo': "Direction de l'Élevage (DE), Ministère de l'Agriculture, de l'Élevage et "
                        'de la Pêche (MAEP)',
           'url': 'https://catis.xroad.bj/publicservices/PS00501',
           'url_generica': False,
           'url_verificada': True,
           'email': None,
           'tel': None,
           'cert': True,
           'cert_dias': 3,
           'cert_quien': 'Veterinario oficial del pais de salida, emitido MENOS DE 72 H antes de '
                         'la llegada (Anivetvoyage). Los «10 dias» que figuraban antes eran la '
                         'validez del certificado UE de reentrada, no del de entrada en Benin',
           'nota': 'La ficha oficial CatIS PS00501 («controle sanitaire et delivrance des '
                   "certificats sanitaires internationaux a l'importation et a l'exportation des "
                   "animaux vivants (betail, animaux de compagnie...)», Direction de l'Elevage, "
                   'arrete 045/MAEP de 2008) no da documentos, coste, plazo ni contacto. Oficina: '
                   'Cotonou, Akpakpa, tras el antiguo puente (L-V 8:00-12:30 / 14:00-17:30); BP '
                   '2041 (WOAH). Rabia >1 mes y <1 ano, microchip y pasaporte. Permiso previo: sin '
                   'fuente.',
           'fuentes': ['https://catis.xroad.bj/institutions/IN00173',
                       'https://anivetvoyage.com/pays/benin/',
                       'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
           'auditado': '2026-09-12'},
 'nigeria': {'organismo': 'Chief Veterinary Officer (CVO) — Federal Department of Veterinary and '
                          'Pest Control Services, desde 2024 en el Federal Ministry of Livestock '
                          'Development (FMLD). La Nigeria Agricultural Quarantine Service (NAQS) '
                          'NO emite el permiso: inspecciona y pone en cuarentena a la llegada',
             'url': 'https://www.fmld.gov.ng/structure/',
             'url_generica': True,
             'url_verificada': True,
             'email': 'vpcs@fmard.gov.ng (CVO, segun nota del servicio veterinario ruso, sin '
                      'fecha) / info@fmld.gov.ng / contact@naqs.gov.ng (NAQS)',
             'tel': '+234 807 777 8943 (NAQS, Abuja)',
             'cert': True,
             'cert_dias': None,
             'cert_quien': 'Veterinario oficial del pais de salida. Las fuentes discrepan: el '
                           'modelo estadounidense vale 30 dias con refrendo en tinta original y '
                           'sello en relieve; PetTravel dice 48 h; una nota del servicio '
                           'veterinario ruso pide certificado con al menos 2 semanas de validez',
             'nota': 'El SOP oficial de NAQS es claro: «Apply for import permit to the Chief '
                     'Veterinary Officer (CVO), Federal Department of Veterinary and Pest Control '
                     'Services». Pista del procedimiento (nota rusa, sin fecha): escribir al CVO '
                     'con pasaporte veterinario, certificado antirrabico (<1 ano) y carta firmada, '
                     'pagar 5.000 NGN por Remita y recibir el permiso en 3-4 dias; otras fuentes '
                     'hablan de hasta 3 meses, o del mismo dia en persona. El portal de permisos '
                     'fmard.gov.ng/l_page/vetpermit/ existe pero esta caido: probarlo a mano. '
                     'Rabia inactivada <1 ano, microchip obligatorio, cuarentena posible (2-3 '
                     'semanas). PetTravel confunde Nigeria con Niger en su propia ficha: no '
                     'usarla.',
             'fuentes': ['https://naqs.gov.ng/wp-content/uploads/2020/07/NAQS_SOP.pdf',
                         'https://naqs.gov.ng/animal/',
                         'https://fmard.gov.ng/l_page/vetpermit/',
                         'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-nigeria',
                         'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
             'auditado': '2026-09-12'},
 'camerun': {'organismo': "Ministère de l'Élevage, des Pêches et des Industries Animales (MINEPIA) "
                          '- Direction des Services Vétérinaires',
             'url': 'https://minepia.cm/site/services/productions-et-industries-animales/obtention-dune-autorisation-dimportation-des-poussins-dun-jour-des-oeufs-a-couver-des-animaux-delevage-et-de-compagnie/',
             'url_generica': False,
             'url_verificada': False,
             'email': None,
             'tel': None,
             'cert': True,
             'cert_dias': None,
             'cert_quien': 'Veterinario oficial del pais de salida; los «30 dias» son la validez '
                           'del modelo estadounidense, no una norma camerunesa publicada',
             'nota': "La ficha de MINEPIA «Obtention d'une autorisation d'importation... des "
                     "animaux d'elevage et de compagnie» es, por titulo, exactamente el tramite, "
                     'pero el certificado TLS del dominio esta roto y no se ha podido abrir (el '
                     'navegador avisara): comprobarla a mano. Permiso previo sin resolver: MINEPIA '
                     'publica el tramite, PetTravel dice que no hace falta para mascotas con '
                     'dueno. Rabia al menos 30 dias antes (PetTravel). Sin email ni telefono '
                     'verificables.',
             'fuentes': ['https://www.aphis.usda.gov/pet-travel/pet-travel-united-states-cameroon',
                         'https://www.pettravel.com/information/pet-passports/cameroon-pet-import-requirements/',
                         'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
             'auditado': '2026-09-12'},
 'gabon': {'organismo': "Direction Générale de l'Élevage, Ministère de l'Agriculture et de "
                        "l'Alimentation",
           'url': 'https://www.agriculture.gouv.ga/',
           'url_generica': True,
           'url_verificada': True,
           'email': None,
           'tel': None,
           'cert': True,
           'cert_dias': None,
           'cert_quien': 'Veterinario oficial del pais de salida; PetTravel dice dentro de los 10 '
                         'dias previos y Anivetvoyage (que bebe de PetTravel/IATA) <72 h: sin '
                         'respaldo gabones',
           'nota': 'La web del ministerio abre pero es solo portada; la pagina de la Direction '
                   "Generale de l'Elevage esta indexada y da timeout. Ninguna fuente gabonesa "
                   'sobre mascotas. PetTravel: sin permiso previo para mascota con dueno, rabia '
                   'entre 30 dias y 12 meses, microchip recomendado.',
           'fuentes': ['https://www.pettravel.com/information/pet-passports/gabon-pet-import-requirements/',
                       'https://anivetvoyage.com/formalites-pays/g/182-gabon.html',
                       'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
           'auditado': '2026-09-12'},
 'congo': {'organismo': "Direction Générale de l'Élevage (servicios veterinarios), Ministère de "
                        "l'Agriculture, de l'Élevage et de la Pêche, Brazzaville",
           'url': 'https://agriculture.gouv.cg/',
           'url_generica': True,
           'url_verificada': False,
           'email': None,
           'tel': None,
           'cert': True,
           'cert_dias': None,
           'cert_quien': 'Veterinario oficial del pais de salida; los «30 dias» son la validez del '
                         'modelo estadounidense',
           'nota': "El portal del Ministere de l'Agriculture, de l'Elevage et de la Peche esta en "
                   "mantenimiento y la pagina de la Direction Generale de l'Elevage devuelve 404 "
                   '(reintentar). Ninguna fuente, oficial o de campo, documenta los papeles del '
                   'perro en esta frontera; el unico precedente localizado (The Pack Track, 2017, '
                   'dos perros) cruzo Gabon y Congo por tierra pero no cuenta que le pidieron. '
                   "Direccion postal (WOAH): DG de l'Elevage, BP 2453, Brazzaville.",
           'fuentes': ['https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-republic-congo-brazzaville',
                       'https://www.thepacktrack.com/blogs/dog-blog/bongo-in-the-congo',
                       'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
           'auditado': '2026-09-12'},
 'rd-congo': {'organismo': 'Direction des Services Veterinaires (Blvd du 30 juin / Av. Batetela, '
                           'Kinshasa-Gombe), que probablemente depende del Ministere de la Peche '
                           'et Elevage y no del MINASA; el control en frontera lo ejerce el '
                           'Service de la Quarantaine Animale et Vegetale (SQAV, decreto 05/161 de '
                           '2005)',
              'url': 'https://agriculture.gouv.cd/contact.php',
              'url_generica': True,
              'url_verificada': True,
              'email': 'info@agriculture.gouv.cd',
              'tel': '+243 828 174 932',
              'cert': True,
              'cert_dias': 10,
              'cert_quien': 'Veterinario oficial del pais de salida, <10 dias antes de la llegada '
                            '(Anivetvoyage; sin fuente oficial)',
              'nota': 'El portal del MINASA solo tiene portada y contacto (email y telefono '
                      'confirmados); no hay ninguna pagina oficial del tramite ni contacto propio '
                      'del SQAV. Escribir a los dos ministerios. Rabia >1 mes y <1 ano, microchip. '
                      'Ningun relato de overlander con perro ha cruzado la RDC: el precedente de '
                      '2017 la evito entrando en Angola por Cabinda.',
              'fuentes': ['https://agriculture.gouv.cd/index.php',
                          'https://anivetvoyage.com/pays/republique-democratique-du-congo/',
                          'https://www.ecolex.org/',
                          'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
              'auditado': '2026-09-12'},
 'angola': {'organismo': 'Instituto dos Serviços de Veterinária (ISV), Ministério da Agricultura e '
                         'Florestas (MINAGRIF)',
            'url': 'https://minagrif.gov.ao/',
            'url_generica': True,
            'url_verificada': True,
            'email': 'gticii@minagrif.gov.ao',
            'tel': None,
            'cert': True,
            'cert_dias': 10,
            'cert_quien': 'Veterinario oficial del pais de salida. Modelo oficial DGAV '
                          '(Portugal→Angola, 2023): licenca zoo-sanitaria previa, microchip, '
                          'vacuna antirrabica >72 h antes del embarque, examen clinico y '
                          'TITULACION >=0,5 UI/ml en laboratorio autorizado OIE (>=30 dias tras la '
                          'vacuna); valido 10 dias. Confirmar en CEXGAN si Espana usa el mismo '
                          'modelo',
            'nota': 'Ninguna pagina angolena describe el tramite (no existe isv.gov.ao; '
                    'minagrif.gov.ao solo cita al ISV como entidad tutelada). El certificado '
                    'bilateral portugues es la unica descripcion de la licenca zoo-sanitaria y '
                    'exige titulacion antirrabica: llevar el original vinculado al microchip. '
                    'PetTravel contradice todo eso (sin permiso, 14 dias, sin titulacion, «air '
                    'cargo»): se conserva la oficial. El buzon gticii@ es el unico publicado por '
                    'el ministerio (gabinete TIC, no el ISV).',
            'fuentes': ['https://www.dgav.pt/wp-content/uploads/2023/11/CERTIFICACAO-SANITARIA-ANGOLA-CAES-E-GATOS-2023.pdf',
                        'https://minagrif.gov.ao/web/contactos',
                        'https://minagrif.gov.ao/web/entidades-tutela',
                        'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
            'auditado': '2026-09-12'},
 'zambia': {'organismo': 'Department of Veterinary Services, Ministry of Fisheries and Livestock '
                         '(MFL) — antes «Department of Research & Specialist Services / Veterinary '
                         '& Tsetse Control Services», nombre que aun usa la embajada',
            'url': 'https://www.zambiatradeportal.gov.zm/index.php?r=searchProcedure/view1&id=116',
            'url_generica': False,
            'url_verificada': True,
            'email': 'info@mfl.gov.zm',
            'tel': '+260 1 253933 / +260 1 253945 (numeracion antigua publicada por la embajada; '
                   'probablemente obsoleta)',
            'cert': True,
            'cert_dias': 7,
            'cert_quien': 'Veterinario oficial del pais de salida (examen clinico no mas de 48 h '
                          'antes de la salida)',
            'nota': 'Portal oficial de comercio: permiso bajo la Animal Health Act 2010, valido 6 '
                    'semanas, con Letter of No Objection del Director of Veterinary Services; tasa '
                    '«Pets (cats and dogs)... maximum 2 pets: ZMW 50». Primero el permiso, despues '
                    'el certificado (redactado segun las condiciones del permiso); admite gestor '
                    'en Lusaka; a la llegada hay que avisar al Veterinary Officer mas cercano. Sin '
                    'plazo publicado.',
            'fuentes': ['https://www.zambiatradeportal.gov.zm/index.php?r=searchProcedure/view1&id=116',
                        'https://www.zambiaembassy.org/page/procedures-for-importation-of-livestock-and-pets-into-zambia',
                        'https://assets.publishing.service.gov.uk/media/65ae438f751546000d7b4a8e/3928NFG.pdf',
                        'https://assets.publishing.service.gov.uk/media/5bc758aa40f0b61ca9b5c0a7/3928EHC_V3.pdf'],
            'auditado': '2026-09-12'},
 'tanzania': {'organismo': 'Director of Veterinary Services, Ministry of Livestock and Fisheries '
                           '(Wizara ya Mifugo na Uvuvi), Dodoma; permisos por el sistema '
                           'electronico MIMIS. La guia de las embajadas (Temeke Veterinary Office, '
                           'Dar es Salaam) es de hacia 2005',
              'url': 'https://www.mifugouvuvi.go.tz/services/vibali-vya-mifugo',
              'url_generica': False,
              'url_verificada': True,
              'email': 'barua@mlf.go.tz (ministerio) / helpdesk@mlf.go.tz (MIMIS) / '
                       'zoosanitary@mifugo.go.tz / epid1@mifugo.go.tz (guia de embajadas) / '
                       'barua@mifugo.go.tz (DVS)',
              'tel': '+255 22 2861908 y +255 26 2322610 (ministerio) · +255 668 217 882 (MIMIS) · '
                     '+255 713 840 853 (DVS, Dr. Benezeth Malinda, vigente en 2025) · +255 22 '
                     '2862592 (Temeke, guia antigua)',
              'cert': True,
              'cert_dias': 10,
              'cert_quien': 'Veterinario oficial del pais de salida. Las fuentes discrepan: modelo '
                            'britanico 10 dias, Keringa (comercial) 4 dias, PetTravel 14 dias: '
                            'emitirlo lo mas tarde posible',
              'nota': 'El ministerio dice que los permisos de importacion y exportacion de '
                      'animales se piden en el sistema electronico MIMIS (mimis.mifugo.go.tz, '
                      'requiere cuenta). Guia de embajadas: carta al DVS indicando «type/breed, '
                      'age, port of entry», rabia entre 1 mes y 3 anos, DHLP recomendado, '
                      'desparasitacion cada 3 meses o comprimidos cada 45 dias, tasas 30.000 TSH '
                      '(entrada) + 20.000 (permiso de EXPORTACION al salir); un testimonio '
                      'reciente lo obtuvo gratis por email via la oficina veterinaria de Arusha, '
                      'valido 30 dias y nombrando el puesto (cruzo por Tunduma). P.O. Box 2847 '
                      'segun el ministerio, 2870 segun el portal de comercio.',
              'fuentes': ['https://mimis.mifugo.go.tz',
                          'https://www.de.tzembassy.go.tz/services/Importing-Pets-Dogs',
                          'https://trade.tanzania.go.tz/media/en1516634461-ZOOSANITARY_INSPECTORATE_EXPORT_AND_IMPORT_PROTOCOLS_.pdf',
                          'https://trade.tanzania.go.tz/Contacts/65?l=en',
                          'https://ondjila-travel.com/reisen-mit-tieren/',
                          'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
              'auditado': '2026-09-12'},
 'kenia': {'organismo': 'Directorate of Veterinary Services (DVS), State Department for Livestock '
                        'Development, Ministry of Agriculture and Livestock Development',
           'url': 'https://infotradekenya.go.ke/procedure/1422?l=en',
           'url_generica': False,
           'url_verificada': True,
           'email': None,
           'tel': '+254 20 631567 (DVS Kabete, numeracion antigua publicada por gov.uk; '
                  'probablemente obsoleta)',
           'cert': True,
           'cert_dias': 7,
           'cert_quien': 'Veterinario oficial del pais de salida (examen clinico no mas de 5 dias '
                         'antes de la salida)',
           'nota': 'El portal oficial InfoTrade Kenya publica el «Import permit for dogs & cats '
                   '(VS01)» y procedimientos especificos de importacion de perros por los puestos '
                   'terrestres de Busia, Malaba, Isebania y Lunga Lunga (el detalle solo se ve en '
                   'navegador). Las embajadas tramitan el permiso con carta de peticion, cartilla '
                   'y copia del pasaporte (Washington 50 USD, Berna 70 CHF; consultar la de '
                   'Madrid). Todo animal que entre por via distinta a Mombasa (mar) o Nairobi '
                   '(aire) debe presentarse en la oficina veterinaria mas cercana en 3 dias '
                   '(gov.uk 2913NFG). No hay email del DVS publicado.',
           'fuentes': ['https://infotradekenya.go.ke/objective/62?l=en',
                       'https://kenyaembassydc.org/petimport/',
                       'https://assets.publishing.service.gov.uk/media/5bc702eaed915d0b01a1bd0b/2913NFG_.pdf',
                       'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
           'auditado': '2026-09-12'},
 'uganda': {'organismo': 'Commissioner Animal Health (CAH), Ministry of Agriculture, Animal '
                         'Industry and Fisheries (MAAIF)',
            'url': 'https://www.agriculture.go.ug/dogs-and-cats/',
            'url_generica': False,
            'url_verificada': True,
            'email': 'maaif@agriculture.go.ug',
            'tel': '+256 41 4320004',
            'cert': True,
            'cert_dias': 7,
            'cert_quien': 'Autoridad veterinaria del pais de origen; certificado oficial en ingles '
                          'o con traduccion al ingles (examen clinico no mas de 48 h antes de la '
                          'salida)',
            'nota': 'Pagina oficial del MAAIF especifica de perros y gatos: solicitud al '
                    'Commissioner Animal Health (Plot 16-18 Lugard Avenue, Entebbe) al menos 7 '
                    'dias antes, indicando pais de origen, tipo, raza y sexo; cuarentena publicada '
                    'de 21-30 dias (un testimonio reciente entro por Mutukula sin que se '
                    'aplicara); vacunas de rabia, moquillo, parvo, hepatitis, parainfluenza y '
                    'traqueobronquitis.',
            'fuentes': ['https://www.agriculture.go.ug/dogs-and-cats/',
                        'https://www.agriculture.go.ug/import-export-and-transit-of-animals-and-animal-products-in-uganda/',
                        'https://assets.publishing.service.gov.uk/media/65aa944882fee9000d6f5f8f/3925NFG.pdf',
                        'https://assets.publishing.service.gov.uk/media/5bc74ee3ed915d64c90dfd28/3925EHC_V4.pdf'],
            'auditado': '2026-09-12'},
 'ruanda': {'organismo': 'Rwanda Agriculture and Animal Resources Development Board (RAB) - '
                         'Veterinary Services Unit',
            'url': 'https://rwandatrade.rw/procedure/509?l=en',
            'url_generica': False,
            'url_verificada': True,
            'email': 'arpms@rab.gov.rw',
            'tel': '+250 788 385 312',
            'cert': True,
            'cert_dias': None,
            'cert_quien': 'Veterinario oficial del pais de salida (certificado de vacunacion; el '
                          'procedimiento oficial no exige un modelo concreto de certificado '
                          'sanitario)',
            'nota': 'Portal oficial RwandaTrade con «Full procedure for the import of dogs and '
                    'cats» (509), «Obtain import permit - Dogs and cats» (422) y fichas de '
                    '«Clearance of dogs and cats» en distintos puestos fronterizos. El contenido '
                    '(tasas, contactos) se carga por JavaScript y no se ha podido releer: email y '
                    'telefono proceden de la verificacion anterior.',
            'fuentes': ['https://rwandatrade.rw/procedure/509?l=en',
                        'https://rwandatrade.rw/procedure/422?l=en',
                        'https://arpms.rab.gov.rw/',
                        'https://nvvh.rw/pet-traveling-documents/'],
            'auditado': '2026-09-12'},
 'malaui': {'organismo': 'Department of Animal Health and Livestock Development (DAHLD) - Chief '
                         'Veterinary Officer, Ministry of Agriculture',
            'url': 'https://www.malawitradeportal.com/en-gb/site/display/300',
            'url_generica': False,
            'url_verificada': True,
            'email': 'agriculture@agriculture.gov.mw',
            'tel': '+265 1 789033 / +265 988 558115',
            'cert': True,
            'cert_dias': None,
            'cert_quien': 'Veterinario oficial del pais de salida (examen clinico no mas de 14 '
                          'dias antes de la salida)',
            'nota': 'Portal de comercio (generico, sin mascotas): solicitud escrita al Director '
                    'del DAHLD (Private Bag 2096, Lilongwe), MWK 10.000, con preinspeccion. Email '
                    'y telefonos del ministerio no reverificados.',
            'fuentes': ['https://www.malawitradeportal.com/en-gb/site/display/300',
                        'https://agriculture.gov.mw/healthandlivestock',
                        'https://agriculture.gov.mw/contacts',
                        'https://assets.publishing.service.gov.uk/media/5bc70bf340f0b638518795ab/3944NFG.pdf',
                        'https://assets.publishing.service.gov.uk/media/5bc70be2ed915d0ae30b91f9/3944EHC_V3.pdf'],
            'auditado': '2026-09-12'},
 'mozambique': {'organismo': 'Direccao Nacional de Veterinaria (DINAV) / Autoridade Veterinaria, '
                             'Ministerio da Agricultura, Ambiente e Pescas (MAAP), Praca dos '
                             'Herois Mocambicanos, Maputo',
                'url': 'https://www.agricultura.gov.mz/servicos-ao-cidadao/procedimentos-para-o-movimento-de-animais-seus-produtos-e-subprodutos/',
                'url_generica': True,
                'url_verificada': True,
                'email': 'geral@maap.gov.mz / geral@agricultura.gov.mz',
                'tel': '+258 21 468200 (linha verde +258 84 3438999)',
                'cert': True,
                'cert_dias': 7,
                'cert_quien': 'Veterinario oficial del pais de salida (certificado sanitario '
                              'internacional; examen clinico no mas de 48 h antes de la salida)',
                'nota': 'La pagina oficial describe la licenca de importacion de animales vivos '
                        '(emitida por la DINAV) y el certificado sanitario internacional, pero no '
                        'menciona mascotas. Emails y telefonos son los generales del ministerio. '
                        'Modelo britanico: certificado valido 7 dias, examen en las 48 h previas, '
                        'rabia entre 30 dias y 12 meses. Desde abril de 2024 esta prohibida la '
                        'importacion de Pit-bull, Rottweiler, Staffordshire americano, Bull '
                        'Terrier, Dogo Argentino, Fila Brasileiro, Tosa Inu, San Bernardo y cruces '
                        'con lobo, entre otras razas.',
                'fuentes': ['https://www.agricultura.gov.mz/instituicional/ministerio/estrutura-organica/direccao-nacional-de-veterinaria/',
                            'https://assets.publishing.service.gov.uk/media/5bcecf21ed915d431874e31d/4143NFG.pdf',
                            'https://aimnews.org/',
                            'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
                'auditado': '2026-09-12'},
 'zimbabue': {'organismo': 'Directorate of Veterinary Services, Ministry of Lands, Agriculture, '
                           'Fisheries, Water and Rural Development (P.O. Box CY 66, Causeway, '
                           'Harare)',
              'url': 'https://www.agric.gov.zw/wordpress/?page_id=7883',
              'url_generica': True,
              'url_verificada': True,
              'email': None,
              'tel': '+263 4 791355 / fax +263 4 720879 (numeracion antigua publicada por gov.uk; '
                     'hoy probablemente +263 242 791355)',
              'cert': True,
              'cert_dias': 7,
              'cert_quien': 'Veterinario oficial del pais de salida (examen clinico no mas de 48 h '
                            'antes de la salida)',
              'nota': 'No existe pagina nacional del tramite que abra (dlvs.gov.zw no responde). '
                      'ZIMRA confirma que los animales domesticos necesitan permiso del Department '
                      'of Veterinary Services; la guia britanica: «no dog or cat may be imported '
                      'into Zimbabwe except in accordance with the terms of an import permit», '
                      'certificado valido 7 dias con examen en las 48 h previas. Zimbabue no exige '
                      'rabia previa (vacuna a la llegada).',
              'fuentes': ['https://www.zimra.co.zw/customs/restricted-and-prohibited-goods',
                          'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-zimbabwe-certificate-3929',
                          'https://assets.publishing.service.gov.uk/media/5bc7594140f0b61ca2dd15f8/3929NFG.pdf',
                          'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
              'auditado': '2026-09-12'},
 'botsuana': {'organismo': 'Department of Veterinary Services, Ministry of Agriculture (Botswana)',
              'url': 'https://www.gov.bw/business-compliance-agriculture-animal-husbandry/issuance-import-permit-live-animals-animal',
              'url_generica': False,
              'url_verificada': True,
              'email': 'DVSpermits@gov.bw',
              'tel': '+267 3689513 / +267 3689510 (call centre 17755)',
              'cert': True,
              'cert_dias': None,
              'cert_quien': 'Veterinario oficial del pais de salida; entrando desde el area SADC, '
                            'Interterritorial Movement Permit (valido 60 dias) firmado por '
                            'veterinario y refrendado por un Government Veterinarian. Para un '
                            'perro que llega de fuera de la SADC no hay validez publicada',
              'nota': 'La mejor pagina oficial de toda la ruta: permiso en un dia habil en '
                      'cualquier District Veterinary Office, con inspeccion del animal, cartilla '
                      'de rabia valida y prueba de que no hay restricciones por rabia en la zona '
                      'de origen; documentos en ingles o setsuana; sin restriccion de puesto '
                      'fronterizo; sin analiticas publicadas. El «Animal Transit Permit» de gov.bw '
                      'es de fauna silvestre y excluye expresamente a los animales domesticos.',
              'fuentes': ['https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf',
                          'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-botswana',
                          'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
              'auditado': '2026-09-12'},
 'sudafrica': {'organismo': 'Director: Animal Health - Import Export Policy Unit, Department of '
                            'Agriculture, Land Reform and Rural Development (DALRRD)',
               'url': 'https://www.gov.za/services/import/import-animals-and-animal-products',
               'url_generica': False,
               'url_verificada': True,
               'email': 'vetpermits@dalrrd.gov.za (vigente, pagina de contactos de DALRRD) / '
                        'VetPermits@daff.gov.za (heredado, aun publicado en gov.za y DIRCO)',
               'tel': '+27 12 319 7514 / +27 12 319 7559 (Import-Export Policy Unit) · fax +27 12 '
                      '329 8292',
               'cert': True,
               'cert_dias': 10,
               'cert_quien': 'Veterinario oficial del pais de salida: emision del certificado Y su '
                             'refrendo dentro de los 10 dias previos al viaje. CINCO analiticas '
                             'negativas hechas en los 30 dias previos, con metodo fijado (Brucella '
                             'canis SAT o RSAT; Trypanosoma evansi CATT Y frotis Giemsa; Babesia '
                             'gibsoni dos pruebas; Dirofilaria immitis filtracion de '
                             'microfilarias, unico metodo aceptado; Leishmania IFAT, ELISA, DAT o '
                             'Western blot), con el numero de microchip en todos los informes; '
                             'rabia puesta hace menos de 12 meses',
               'nota': 'Permiso veterinario de importacion del Director: Animal Health, valido '
                       '«for one consignment only» (una sola entrada), a solicitar con al menos 4 '
                       'semanas; tasa R140 segun la embajada (cifra de 2014, se revisa cada ano); '
                       'los certificados originales se presentan solo en el puesto de entrada. La '
                       'pagina gov.za del tramite excluye expresamente «cats and dogs»: el detalle '
                       'esta en el certificado IMP.DOG.GEN (reproducido por APHIS, sept. 2024). '
                       'Testimonio 2017: entregar los papeles en mano en la oficina veterinaria '
                       'estatal acelero un tramite que por correo tardaba 3 semanas.',
               'fuentes': ['https://old.dalrrd.gov.za/Branches/Agricultural-Production-Health-Food-Safety/Animal-Health/contacts/importexport',
                           'https://www.aphis.usda.gov/sites/default/files/south-africa-dog-guidance.pdf',
                           'https://dirco.gov.za/washingtondc/importing-pets-to-south-africa/',
                           'https://www.elsenburg.com/exporting-pets-and-products/',
                           'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
               'auditado': '2026-09-12'},
 'namibia': {'organismo': 'Directorate of Veterinary Services - Import/Export Office, Ministry of '
                          'Agriculture, Water and Land Reform (MAWLR)',
             'url': 'https://namibiatradeportal.gov.na/trade-goods/procedure-details/view_express_entity/485',
             'url_generica': False,
             'url_verificada': True,
             'email': 'vet.permits@mawlr.gov.na',
             'tel': '+264 61 276592 (Import/Export) · +264 61 2087892, 2087891/0 y 303150 · Walvis '
                    'Bay +264 64 203073',
             'cert': True,
             'cert_dias': None,
             'cert_quien': 'Veterinario oficial del pais de salida (examen clinico en los 10 dias '
                           'previos), sobre el formulario del permiso namibio enviado por '
                           'mensajeria; CINCO analiticas negativas (Brucella canis, Trypanosoma '
                           'evansi, Leishmania, Dirofilaria, Babesia) con los metodos que fije el '
                           'permiso y, segun el modelo estadounidense, hechas en los 30 dias '
                           'previos; rabia entre 30 dias y 12 meses si es primovacunacion; '
                           'prevencion de filaria durante 6 meses tras la llegada',
             'nota': 'Portal oficial de comercio: permiso de importacion N$150, «maximum of three '
                     'working days» con la documentacion completa (lo que tarda semanas es la '
                     'mensajeria del permiso original y las analiticas). Antes de viajar hay que '
                     'enviar por email al veterinario estatal namibio el permiso cumplimentado, la '
                     'cartilla y los resultados negativos para obtener el «landing permission». '
                     'Desde Botsuana basta cartilla y certificado sanitario; desde Sudafrica, '
                     'Inter-Territorial Movement Permit SA-Namibia (30 dias, sin analiticas, para '
                     'animales residentes; preguntar si vale para un perro UE ya importado a '
                     'Sudafrica). La pagina mawlr.gov.na/directorate-of-veterinary-services existe '
                     'pero no abre.',
             'fuentes': ['https://van.org.na/section.php?secid=52&menuid=52',
                         'https://www.van.org.na/pdf/Namibian%20Interterritorial%20Movement%20Permit.pdf',
                         'https://www.aphis.usda.gov/sites/default/files/namibia-dog_0.pdf',
                         'https://mawlr.gov.na/directorate-of-veterinary-services',
                         'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
             'auditado': '2026-09-12'},
 'lesoto': {'organismo': 'Department of Livestock Services - Imports and Exports Office, Ministry '
                         'of Agriculture, Food Security and Nutrition',
            'url': 'https://lesotho.eregulations.org/procedure/160?l=en',
            'url_generica': False,
            'url_verificada': True,
            'email': None,
            'tel': '+266 2231 7284 (fax +266 2231 1500)',
            'cert': True,
            'cert_dias': None,
            'cert_quien': 'Veterinario oficial del pais de salida; el modelo SADC de permiso '
                          'interterritorial (60 dias) cubre Lesoto, pero no hay validez lesotense '
                          'publicada para un perro que llega de fuera',
            'nota': 'Portal oficial eRegulations: «International Veterinary import permit» del '
                    'Department of Livestock Services (contenido por JavaScript; tasas y '
                    'calendario no reverificados). Contacto de importacion y exportacion: Private '
                    'Bag A 82, Maseru, +266 2231 7284, L-V 8:00-16:30.',
            'fuentes': ['https://lesotho.eregulations.org/Contacts/61?letter=d&l=en',
                        'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
            'auditado': '2026-09-12'},
 'esuatini': {'organismo': 'Department of Veterinary and Livestock Services, Ministry of '
                           'Agriculture (Eswatini)',
              'url': 'https://www.gov.sz/index.php/ministries-departments/ministry-of-agriculture/veterinary-a-livestock',
              'url_generica': True,
              'url_verificada': True,
              'email': None,
              'tel': '+268 2404 2731/9 / +268 2404 6362',
              'cert': True,
              'cert_dias': None,
              'cert_quien': 'Veterinario oficial del pais de salida; el modelo SADC de permiso '
                            'interterritorial (60 dias) cubre Esuatini, pero no hay validez propia '
                            'publicada',
              'nota': 'La pagina del Department of Veterinary and Livestock Services es '
                      'institucional: no existe pagina del tramite. Testimonio 2017: entrada '
                      'sencilla con el permiso de importacion SACU, que quisieron quedarse en la '
                      'frontera (insistir en conservarlo).',
              'fuentes': ['https://www.gov.sz/index.php/ministries-departments/ministry-of-agriculture/veterinary-a-livestock',
                          'https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf',
                          'https://www.eswatinitradeportal.gov.sz/index.php?r=SearchMeasures/index'],
              'auditado': '2026-09-12'},
 'sahara-occidental': {'organismo': 'Office National de Sécurité Sanitaire des Produits '
                                    'Alimentaires (ONSSA) - Direction des Services Vétérinaires',
                       'url': 'https://www.onssa.gov.ma/controle-a-limportation-et-a-lexportation/controle-a-limportation/importation-des-animaux-vivants/chiens-et-chats/',
                       'url_generica': False,
                       'url_verificada': False,
                       'email': None,
                       'tel': '+212 5 37 67 65 13 (Direccion de Control Fronterizo y Acuerdos SPS '
                              'de ONSSA, segun FAO/Codex) · +212 5 37 67 65 00 (solo en '
                              'directorios comerciales)',
                       'cert': True,
                       'cert_dias': None,
                       'cert_quien': 'Veterinario oficial espanol, certificado bilateral ASE-3131 '
                                     '«perros y gatos a Marruecos» tramitado por CEXGAN (digital '
                                     'desde el 01-09-2025, sin apostilla): chip anterior a la '
                                     'vacuna, vacuna antirrabica inactivada con >=21 dias si es '
                                     'primovacunacion, examen clinico en las 24 h previas al '
                                     'embarque y titulacion >=0,5 UI/ml para exportacion temporal',
                       'nota': 'Administrado por Marruecos: no hay tramite ni organismo propio. El '
                               'control se hace al salir hacia Mauritania, en Guerguerat. Sin '
                               'permiso previo de importacion para un perro de la UE con su dueno '
                               '(ninguno de los tres modelos oficiales, ES/UK/EEUU, lo menciona). '
                               'La pagina de ONSSA es la correcta por titulo pero no se ha podido '
                               'abrir desde el entorno de verificacion: comprobarla a mano. No hay '
                               'validez publicada en dias para el certificado espanol: lo que fija '
                               'es el examen clinico en las 24 h previas (el modelo britanico vale '
                               '7 dias y el estadounidense 3). El «limite de 3 animales» no tiene '
                               'fuente. Email oficial de ONSSA/DSV: no publicado en fuente '
                               'accesible.',
                       'fuentes': ['https://servicio.mapama.gob.es/cexgan/documentacionpublica/perrosgatosmarruecosase-3131.pdf',
                                   'https://colegioveterinarios.net/wp-content/uploads/2025/07/Nota-informativa-CEXGAN-Perros-y-gatos-Marruecos-2025.pdf',
                                   'https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones',
                                   'https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-morocco-certificate-3916',
                                   'https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-morocco',
                                   'https://www.consulat.ma/en/introduction-pets',
                                   'https://www.fao.org/fao-who-codexalimentarius/about-codex/members/detail/en/c/15642/',
                                   'https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm'],
                       'auditado': '2026-09-12'},
 'ue': {'organismo': 'Comisión Europea, DG SANTE — movimiento no comercial desde terceros países',
        'url': 'https://food.ec.europa.eu/animals/movement-pets/eu-legislation/non-commercial-movement-non-eu-countries_en',
        'url_generica': False,
        'url_verificada': True,
        'email': None,
        'tel': None,
        'cert': True,
        'cert_dias': 10,
        'cert_quien': 'SOLO si falla la via del pasaporte: veterinario oficial de Marruecos '
                      '(ONSSA) o veterinario autorizado con refrendo de la autoridad competente, '
                      'modelo del Reg. de Ejecucion (UE) 2026/705 anexo III, valido 10 dias desde '
                      'la emision hasta el control en el Punto de Entrada de Viajeros',
        'nota': 'Normativa vigente desde el 22-04-2026: Reg. Delegado (UE) 2026/131 (requisitos), '
                'Reg. de Ejecucion 2026/636 (listas de paises: ningun pais africano continental) y '
                '2026/705 (modelos). VIA A, por defecto: un perro con pasaporte UE, rabia puesta '
                'en la UE antes de salir y aun valida al volver, y titulacion >=0,5 UI/ml anotada '
                'en el pasaporte antes de salir, reentra SOLO CON EL PASAPORTE, sin certificado y '
                'sin los 90 dias (art. 20(b) del Reg. 2026/131); la revacunacion fuera de la UE '
                'rompe esta via. VIA B: certificado. Puntos de Entrada de Viajeros: Algeciras y '
                'Tarifa (puerto, todas las categorias; servicio en Muelle Juan Carlos I s/n, '
                'Algeciras), tambien Ceuta-El Tarajal por tierra. Unico laboratorio aprobado en '
                'Africa: ARC-Onderstepoort (Sudafrica), aprobado el 24-05-2024.',
        'fuentes': ['https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=OJ%3AL_202600131',
                    'https://food.ec.europa.eu/animals/movement-pets/approved-rabies-serology-laboratories/non-eu-countries_en',
                    'https://www.mapa.gob.es/es/ganaderia/temas/comercio-exterior-ganadero/desplazamiento-animales-compania/viajar-perros-gatos-hurones',
                    'https://agriculture.gouv.fr/faq-modalites-dimportation-des-animaux-de-compagnie-en-provenance-de-pays-tiers'],
        'auditado': '2026-09-12'}}

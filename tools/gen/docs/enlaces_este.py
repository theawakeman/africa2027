# -*- coding: utf-8 -*-
# Datos de contacto de los organismos que emiten el permiso de importacion
# de animales de compania (perro) - ruta overland Africa Oriental y Austral 2027.
#
# TODAS las URL del campo "url" se han abierto y comprobado (url_verificada=True)
# salvo donde se indica lo contrario. Campo sin fuente = None y explicado en "nota".
#
# NOTA TRANSVERSAL SOBRE cert_dias: casi ningun ministerio africano publica en su web
# la validez del certificado sanitario. Donde hay cifra, procede de (a) el modelo de
# certificado bilateral oficial Reino Unido-pais (Export Health Certificate de DEFRA,
# que lleva impresa la clausula "This certificate is valid for N days"), o (b) el
# modelo SADC de Interterritorial Movement Permit for Dogs and Cats. La UE/Espana no
# tiene modelos bilaterales publicados con estos paises, asi que la cifra britanica es
# el mejor indicador disponible pero NO es juridicamente el certificado que emitira un
# veterinario oficial espanol: confirmar siempre por email con el organismo emisor.
DATOS = {
    "zambia": {
        "organismo": "Department of Veterinary Services, Ministry of Fisheries and Livestock (MFL)",
        "url": "https://www.zambiatradeportal.gov.zm/index.php?r=searchProcedure/view1&id=116",
        "url_generica": False,
        "url_verificada": True,
        "email": "info@mfl.gov.zm",
        "tel": "+260 1 253933 / +260 1 253945",
        "cert": True,
        "cert_dias": 7,
        "cert_quien": "Veterinario oficial del pais de salida (examen clinico no mas de 48 h antes de la salida)",
        "nota": (
            "URL VERIFICADA: procedimiento 'Import Permit requirement for Animals, Animal Products, "
            "Animal By-Products and Articles' del Zambia Trade Information Portal (portal oficial del "
            "Gobierno, dominio gov.zm). Detalla tasas explicitas para mascotas: ZMW 250 para animales "
            "pequenos (perros, gatos) hasta 100 por envio, y ZMW 100 para el permiso minimo de 5 "
            "animales domesticos o menos. Circuito real: se presenta la solicitud al Department of "
            "Fisheries and Livestock Marketing, que la remite al Department of Veterinary Services para "
            "el visto bueno sanitario y la emision del permiso veterinario; hace falta ademas una "
            "'Letter of No Objection' del Director of Veterinary Services para animales vivos. "
            "El permiso tiene validez de 6 semanas. Base legal: Animal Health Act, 2010. "
            "OJO CON LOS NOMBRES ANTIGUOS: la pagina de la embajada zambiana en Washington (verificada) "
            "sigue dando 'Department of Research & Specialist Services, Mulungushi House, P.O. Box "
            "50060, Lusaka, tel +260-1 253933/45, fax 253520/260505' y la guia britanica dice "
            "'Department of Veterinary and Tsetse Control Services, P.O. Box 50060, 15101 Ridgeway, "
            "Lusaka'; los tres nombres apuntan al mismo servicio veterinario (misma P.O. Box 50060). "
            "El email info@mfl.gov.zm es el del Ministerio (verificado en el trade portal), NO un buzon "
            "especifico de permisos: no se ha encontrado publicado ningun email directo del DVS. "
            "cert_dias=7 procede de la clausula impresa en el certificado bilateral UK-Zambia EHC 3928 "
            "('This certificate is valid for 7 days from the date of signature')."
        ),
        "fuentes": [
            "https://www.zambiatradeportal.gov.zm/index.php?r=searchProcedure/view1&id=116",
            "https://www.zambiaembassy.org/page/procedures-for-importation-of-livestock-and-pets-into-zambia",
            "https://assets.publishing.service.gov.uk/media/65ae438f751546000d7b4a8e/3928NFG.pdf",
            "https://assets.publishing.service.gov.uk/media/5bc758aa40f0b61ca9b5c0a7/3928EHC_V3.pdf",
        ],
    },
    "tanzania": {
        "organismo": "Director of Veterinary Services, Ministry of Livestock and Fisheries (Wizara ya Mifugo na Uvuvi) - Temeke Veterinary Office",
        "url": "https://www.de.tzembassy.go.tz/services/Importing-Pets-Dogs",
        "url_generica": False,
        "url_verificada": True,
        "email": "zoosanitary@mifugo.go.tz / epid1@mifugo.go.tz",
        "tel": "+255 22 2862592 (fax +255 22 2862538)",
        "cert": True,
        "cert_dias": 10,
        "cert_quien": "Veterinario oficial del pais de salida ('sanitary certificate from a qualified veterinary surgeon in the country of export')",
        "nota": (
            "URL VERIFICADA y es la mejor de las trece: la Embajada de Tanzania en Berlin tiene una "
            "pagina dedicada SOLO a perros ('Importing Pets - Dogs'), mas util que la generica "
            "'Import Permit Food, Plants, Pets and Animal Products' que publican el resto de embajadas "
            "(tambien verificadas: un.tzembassy.go.tz y us.tzembassy.go.tz, mismos datos de contacto). "
            "TRAMITE: no hay formulario; se manda una CARTA de solicitud al Director of Veterinary "
            "Services indicando raza/tipo de perro, edad, puerto o frontera de entrada, y adjuntando "
            "los certificados de vacunacion. Direccion postal: Temeke Veterinary Office, P.O. Box 9152, "
            "Dar es Salaam. Tasas: Tsh 30.000 de importacion + Tsh 20.000 de exportacion (Tsh 50.000 "
            "en total) - relevante porque saldras del pais por tierra y necesitaras tambien el de "
            "salida. Rabia: al menos 1 mes y no mas de 3 anos antes de la entrada. Recomiendan DHLP y "
            "desparasitacion cada 45 dias / trimestral. Inspeccion veterinaria en el punto de entrada y "
            "posible cuarentena. Conviene tener un contacto local que recoja el permiso. "
            "cert_dias=10 procede del certificado bilateral UK-Tanzania EHC 3129 ('This certificate is "
            "valid for 10 days', con examen clinico no mas de 10 dias antes de la salida). "
            "OJO: el ministerio aparece con nombres historicos distintos segun la fuente ('Ministry of "
            "Water and Livestock Development' en las embajadas, 'Livestock Division, Ministry of "
            "Agriculture' en la guia britanica); el dominio de correo vigente es mifugo.go.tz."
        ),
        "fuentes": [
            "https://www.de.tzembassy.go.tz/services/Importing-Pets-Dogs",
            "https://www.un.tzembassy.go.tz/services/import-permit-food-plants-pets-and-animal-products",
            "https://www.us.tzembassy.go.tz/services/import-permit-food-plants-pets-and-animal-products",
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-tanzania",
            "https://assets.publishing.service.gov.uk/media/66d9ada4561701fa1c214e7a/3129NFG.pdf",
            "https://assets.publishing.service.gov.uk/media/66d9ad97fb86ba5a1f214e74/3129EHC_V4.pdf",
        ],
    },
    "kenia": {
        "organismo": "Directorate of Veterinary Services (DVS), State Department for Livestock Development, Ministry of Agriculture and Livestock Development",
        "url": "https://infotradekenya.go.ke/procedure/1422?l=en",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": "+254 20 631567 (fax +254 20 631273)",
        "cert": True,
        "cert_dias": 7,
        "cert_quien": "Veterinario oficial del pais de salida (examen clinico no mas de 5 dias antes de la salida)",
        "nota": (
            "URL VERIFICADA PARCIALMENTE: la pagina responde y su titulo es exactamente 'Import permit "
            "for dogs & cats (VS01)' en el portal oficial InfoTrade Kenya (KenTrade, dominio go.ke), "
            "pero el detalle del tramite se carga por JavaScript y NO se ha podido leer el contenido "
            "(entidad, tasas, plazos); la vista imprimible del portal esta bloqueada por robots.txt. "
            "El nombre del permiso, VS01, si esta confirmado. "
            "MUY RELEVANTE PARA OVERLAND: el mismo portal publica procedimientos especificos de entrada "
            "por frontera terrestre - 'Dogs & cats import procedure through the Busia One Stop Border "
            "Post (OSBP)', y equivalentes para Malaba (frontera con Uganda), Isebania (frontera con "
            "Tanzania) y Lunga Lunga (frontera con Tanzania, en dos variantes segun valor declarado "
            "por encima o por debajo de USD 2.000). Se listan en "
            "https://infotradekenya.go.ke/objective/62?l=en (verificado). "
            "EMAIL: no se ha encontrado publicado ningun correo del DVS de Kenia en fuente oficial; el "
            "unico correo verificado del portal es infotradekenya@kentrade.go.ke (+254 709 950 000), "
            "que es el servicio de atencion de KenTrade, NO el emisor del permiso. Por eso email=None. "
            "El telefono es el que publica la guia oficial britanica para el Director of Veterinary "
            "Services (PO Box 34188, Kabete, Nairobi); es un numero antiguo de 7 digitos y puede haber "
            "cambiado con la renumeracion keniana. El permiso tambien se puede pedir, segun esa misma "
            "guia, a traves de la Kenya High Commission en Londres. "
            "cert_dias=7 procede del certificado bilateral UK-Kenia EHC 2913 ('This certificate is "
            "valid for 7 days, extended by the duration of the voyage of travelling by sea')."
        ),
        "fuentes": [
            "https://infotradekenya.go.ke/procedure/1422?l=en",
            "https://infotradekenya.go.ke/objective/62?l=en",
            "https://assets.publishing.service.gov.uk/media/5bc702eaed915d0b01a1bd0b/2913NFG_.pdf",
            "https://assets.publishing.service.gov.uk/media/5bc702d0e5274a360e8ed071/2913EHC_V3.pdf",
        ],
    },
    "uganda": {
        "organismo": "Commissioner Animal Health (CAH), Ministry of Agriculture, Animal Industry and Fisheries (MAAIF)",
        "url": "https://www.agriculture.go.ug/dogs-and-cats/",
        "url_generica": False,
        "url_verificada": True,
        "email": "maaif@agriculture.go.ug",
        "tel": "+256 41 4320004",
        "cert": True,
        "cert_dias": 7,
        "cert_quien": "Autoridad veterinaria del pais de origen; certificado oficial en ingles o con traduccion al ingles (examen clinico no mas de 48 h antes de la salida)",
        "nota": (
            "URL VERIFICADA y excelente: pagina del propio ministerio titulada 'Dogs and Cats', "
            "dedicada en exclusiva a la importacion de perros y gatos. "
            "TRAMITE: solicitud POR ESCRITO al Commissioner for Animal Health con AL MENOS 7 DIAS de "
            "antelacion a la importacion, indicando pais de origen, proveedor, tipo de animal, raza, "
            "sexo y cantidad. Direccion: Plot 16-18 Lugard Avenue, P.O. Box 102, Entebbe. "
            "AVISO IMPORTANTE PARA VIAJE CON PERRO: la pagina establece un periodo de cuarentena de "
            "21 a 30 dias durante el cual se toman muestras de todos los animales importados para "
            "contrastar o analizar determinadas enfermedades. Confirmar por email si se aplica de "
            "hecho a mascotas que entran por carretera, porque haria inviable el transito rapido. "
            "Vacunas exigidas para perros: rabia, moquillo, parvovirus, hepatitis infecciosa canina, "
            "parainfluenza y traqueobronquitis infecciosa canina. La rabia, segun la guia britanica, "
            "no menos de 30 dias y no mas de 12 meses antes de la salida. "
            "cert_dias=7 procede del certificado bilateral UK-Uganda EHC 3925 ('This certificate is "
            "valid for 7 days'). La guia britanica llama al organismo 'Department of Veterinary "
            "Services and Animal Industry'; el nombre vigente en la web del ministerio es Commissioner "
            "Animal Health."
        ),
        "fuentes": [
            "https://www.agriculture.go.ug/dogs-and-cats/",
            "https://www.agriculture.go.ug/import-export-and-transit-of-animals-and-animal-products-in-uganda/",
            "https://assets.publishing.service.gov.uk/media/65aa944882fee9000d6f5f8f/3925NFG.pdf",
            "https://assets.publishing.service.gov.uk/media/5bc74ee3ed915d64c90dfd28/3925EHC_V4.pdf",
        ],
    },
    "ruanda": {
        "organismo": "Rwanda Agriculture and Animal Resources Development Board (RAB) - Veterinary Services Unit",
        "url": "https://rwandatrade.rw/procedure/509?l=en",
        "url_generica": False,
        "url_verificada": True,
        "email": "arpms@rab.gov.rw",
        "tel": "+250 788 385 312",
        "cert": True,
        "cert_dias": None,
        "cert_quien": "Veterinario oficial del pais de salida (certificado de vacunacion; el procedimiento oficial no exige un modelo concreto de certificado sanitario)",
        "nota": (
            "URL VERIFICADA y es el pais mejor documentado de los trece: 'Full procedure for the import "
            "of dogs and cats' del Rwanda Trade Portal (portal oficial), con los 9 pasos, personas de "
            "contacto y base legal. Existe ademas la ficha corta del permiso en "
            "https://rwandatrade.rw/procedure/422?l=en (tambien verificada). "
            "TRAMITE EN 3 PASOS PARA EL PERMISO: (1) pagar RWF 15.000 en BPR Bank Rwanda a la cuenta "
            "400374715110578 'RAB Internally Generated Revenues'; (2) presentar la solicitud EN LINEA "
            "en el portal https://arpms.rab.gov.rw/ adjuntando copia del pasaporte del dueno, carta de "
            "solicitud original, recibo de pago original y copia del certificado de vacunacion; "
            "(3) recoger el permiso en persona en la Veterinary Services Unit del RAB (P.O. Box 5016, "
            "Kigali). Responsable nominal: Dr. Isidore Gafarasi Mapendo, tel +250 738 503 589. "
            "Ademas hay que declarar la carga en la ventanilla unica (https://sw.gov.rw, "
            "info@sw.gov.rw, +250 788 185 611) y pasar inspeccion de aduanas y del RAB; tasa de "
            "tramitacion adicional RWF 3.000 (total RWF 18.000 sin agente de aduanas). "
            "Base legal: Ley nº 54/2008 de 10/09/2008, arts. 141-150. "
            "cert_dias=None: el procedimiento oficial no publica ninguna validez y no existe modelo "
            "bilateral britanico ni ficha APHIS para Ruanda. El unico dato circulante (certificado "
            "sanitario 'no older than 14 days', desparasitacion 5 dias antes) procede de New Vision "
            "Veterinary Hospital de Kigali (nvvh.rw), clinica privada que tramita permisos con el RAB: "
            "es verosimil y util para planificar, pero NO es fuente oficial y por eso no se consigna."
        ),
        "fuentes": [
            "https://rwandatrade.rw/procedure/509?l=en",
            "https://rwandatrade.rw/procedure/422?l=en",
            "https://arpms.rab.gov.rw/",
            "https://nvvh.rw/pet-traveling-documents/",
        ],
    },
    "malaui": {
        "organismo": "Department of Animal Health and Livestock Development (DAHLD) - Chief Veterinary Officer, Ministry of Agriculture",
        "url": "https://www.malawitradeportal.com/en-gb/site/display/300",
        "url_generica": False,
        "url_verificada": True,
        "email": "agriculture@agriculture.gov.mw",
        "tel": "+265 1 789033 / +265 988 558115",
        "cert": True,
        "cert_dias": None,
        "cert_quien": "Veterinario oficial del pais de salida (examen clinico no mas de 14 dias antes de la salida)",
        "nota": (
            "URL VERIFICADA: guia 'Step by Step: How to Import Animal or Animal Products' del Malawi "
            "Trade Portal (portal oficial). Cubre animales vivos en general, no hay pagina especifica "
            "de mascotas. "
            "TRAMITE: solicitud POR ESCRITO al Director del DAHLD indicando los animales concretos que "
            "se pretenden importar; incluye una comprobacion previa de brotes de enfermedad en el pais "
            "exportador. Tasa del permiso: MWK 10.000. Direccion postal del DAHLD: Private Bag 2096, "
            "Lilongwe (la guia oficial britanica da 'Chief Veterinary Officer, P.O. Box 30372, "
            "Lilongwe' - hay dos apartados distintos en circulacion, confirmar al escribir). "
            "AVISO: el portal plantea el tramite pensando en importadores comerciales y lista pasos que "
            "para un particular en transito no deberian aplicar (registro de empresa en MBRS, numero "
            "TIN en la Malawi Revenue Authority). Confirmar por email el circuito para mascota "
            "acompanada. "
            "EMAIL/TEL: son los generales del Ministerio de Agricultura (verificados en "
            "agriculture.gov.mw/contacts); NO se ha encontrado publicado ningun contacto directo del "
            "DAHLD ni de su Director. El portal de comercio solo ofrece como alternativa el Ministerio "
            "de Comercio (trademin@trade.gov.mw, +265 1 770244), que no es el emisor. "
            "cert_dias=None de forma deliberada: el certificado bilateral UK-Malaui EHC 3944 deja la "
            "validez EN BLANCO para que la rellene el veterinario certificador ('This certificate is "
            "valid for ......... days'), asi que no hay cifra publicada. Lo que si esta fijado es la "
            "ventana de examen clinico: no mas de 14 dias antes de la salida."
        ),
        "fuentes": [
            "https://www.malawitradeportal.com/en-gb/site/display/300",
            "https://agriculture.gov.mw/healthandlivestock",
            "https://agriculture.gov.mw/contacts",
            "https://assets.publishing.service.gov.uk/media/5bc70bf340f0b638518795ab/3944NFG.pdf",
            "https://assets.publishing.service.gov.uk/media/5bc70be2ed915d0ae30b91f9/3944EHC_V3.pdf",
        ],
    },
    "mozambique": {
        "organismo": "Direccao Nacional de Veterinaria / Autoridade Veterinaria Nacional (DINAV), Ministerio da Agricultura, Ambiente e Pescas (MAAP)",
        "url": "https://www.agricultura.gov.mz/servicos-ao-cidadao/procedimentos-para-o-movimento-de-animais-seus-produtos-e-subprodutos/",
        "url_generica": False,
        "url_verificada": True,
        "email": "geral@maap.gov.mz / geral@agricultura.gov.mz",
        "tel": "+258 21 468200 (linha verde +258 84 3438999)",
        "cert": True,
        "cert_dias": 7,
        "cert_quien": "Veterinario oficial del pais de salida (certificado sanitario internacional; examen clinico no mas de 48 h antes de la salida)",
        "nota": (
            "URL VERIFICADA: 'Guiao de Procedimentos para o Movimento de Animais, seus Produtos e "
            "Subprodutos', en el apartado Servicos ao Cidadao de la web del ministerio. Confirma "
            "literalmente que 'a licenca de importacao e emitida pela DINAV' y que sin licencia de "
            "importacion Y certificado sanitario internacional no se permite la entrada. "
            "FORMULARIO: existe el impreso oficial 'Pedido de Licenca de importacao de animais vivos' "
            "en https://www.agricultura.gov.mz/wp-content/uploads/2018/01/Pedido_Licenca_importacao_animais_vivos.doc "
            "(el enlace responde y descarga un .doc, pero al ser binario no se ha podido leer su "
            "contenido para confirmar los campos). "
            "EMAIL/TEL: son los generales del ministerio (verificados en la propia pagina); no hay "
            "buzon publicado especifico de la DINAV. OJO con el nombre del ministerio: cambio de "
            "'Ministerio da Agricultura e Desenvolvimento Rural' a 'Ministerio da Agricultura, Ambiente "
            "e Pescas' (MAAP), y conviven los dominios agricultura.gov.mz y maap.gov.mz. "
            "cert_dias=7 procede del certificado bilateral UK-Mozambique EHC 4143 ('This certificate is "
            "valid for 7 days from the date of signature'); ese modelo incluye casilla expresa para el "
            "numero de licencia de importacion. "
            "CONTEXTO: en 2024 el Gobierno prohibio la importacion de determinadas razas consideradas "
            "peligrosas - verificar la raza del perro antes de planificar la entrada."
        ),
        "fuentes": [
            "https://www.agricultura.gov.mz/servicos-ao-cidadao/procedimentos-para-o-movimento-de-animais-seus-produtos-e-subprodutos/",
            "https://www.agricultura.gov.mz/wp-content/uploads/2018/01/Pedido_Licenca_importacao_animais_vivos.doc",
            "https://assets.publishing.service.gov.uk/media/5bcecf21ed915d431874e31d/4143NFG.pdf",
            "https://assets.publishing.service.gov.uk/media/5bcecf0ce5274a6bd864f36d/4143EHC_V3.pdf",
        ],
    },
    "zimbabue": {
        "organismo": "Director of Veterinary Services, Division of Veterinary Services, Ministry of Lands, Agriculture, Fisheries, Water and Rural Development",
        "url": "https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-zimbabwe-certificate-3929",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": "+263 4 791355 (fax +263 4 720879)",
        "cert": True,
        "cert_dias": 7,
        "cert_quien": "Veterinario oficial del pais de salida (examen clinico no mas de 48 h antes de la salida)",
        "nota": (
            "PEOR CASO DE LOS TRECE - LEER CON ATENCION. NO EXISTE, o no se ha podido encontrar, "
            "NINGUNA pagina del Gobierno de Zimbabue que explique el tramite: la Division of "
            "Veterinary Services no tiene web propia localizable y su unica presencia publica "
            "actualizada es una pagina de Facebook (facebook.com/vetservices.zw). APHIS NO tiene ficha "
            "de Zimbabue en pet-travel (la URL .../pet-travel-us-zimbabwe devuelve 404) y su pagina de "
            "animales vivos para Zimbabue no da ningun contacto local. "
            "Por eso la URL que se da NO es zimbabuense: es la ficha oficial del Gobierno britanico "
            "del certificado de exportacion de perros y gatos a Zimbabue (EHC 3929), verificada, que "
            "si publica el organismo y su direccion. Es la mejor fuente accesible y estable, pero hay "
            "que tratarla como referencia, no como tramite. "
            "DATO CLAVE VERIFICADO en esa guia: 'No dog or cat may be imported into Zimbabwe except in "
            "accordance with the terms of an import permit', emitido por el Director of Veterinary "
            "Services, P.O. Box CY 66, Causeway, Harare, tel +263 4 791355, fax +263 4 720879. "
            "EMAIL: no publicado en ninguna fuente oficial; email=None. "
            "TELEFONO: el numero dado es el de la guia britanica y usa el prefijo antiguo de Harare "
            "(4); con la renumeracion actual seria +263 242 791355. Circula ademas +263 242 791516 "
            "junto a la mencion de una tasa de USD 150 por animal y un plazo de 3-5 dias, pero eso "
            "procede de Wikiprocedure (wiki abierta, NO fuente oficial) y no se consigna como dato. "
            "cert_dias=7 procede de la clausula del propio EHC 3929 ('This certificate is valid for 7 "
            "days'). ALTERNATIVA OVERLAND: si entras desde Sudafrica, Botsuana, Lesoto o Esuatini, el "
            "documento real es el Interterritorial Movement Permit for Dogs and Cats del modelo SADC, "
            "que Zimbabue acepta expresamente y que vale 60 dias desde su emision."
        ),
        "fuentes": [
            "https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-zimbabwe-certificate-3929",
            "https://assets.publishing.service.gov.uk/media/5bc7594140f0b61ca2dd15f8/3929NFG.pdf",
            "https://assets.publishing.service.gov.uk/media/5bc7592740f0b61c92ec8b6b/3929EHC_V3.pdf",
            "https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf",
        ],
    },
    "botsuana": {
        "organismo": "Department of Veterinary Services, Ministry of Agriculture (Botswana)",
        "url": "https://www.gov.bw/business-compliance-agriculture-animal-husbandry/issuance-import-permit-live-animals-animal",
        "url_generica": False,
        "url_verificada": True,
        "email": "DVSpermits@gov.bw",
        "tel": "+267 3689513 / +267 3689510 (call centre 17755)",
        "cert": True,
        "cert_dias": 60,
        "cert_quien": "Veterinario oficial del pais de salida; en entrada desde el area SADC, Interterritorial Movement Permit firmado por veterinario colegiado u oficial Y refrendado por un Government Veterinarian con sello oficial",
        "nota": (
            "URL VERIFICADA, es la que sospechabas y es correcta: 'Issuance of Import Permit of Live "
            "Animal(s), Animal Product(s) and Animal Feed(s)' en gov.bw. Trata expresamente perros y "
            "gatos y confirma tus datos de contacto (en la pagina el correo aparece ofuscado como "
            "'DVSpermits[at]gov[dot]bw'). "
            "REQUISITOS QUE LISTA LA PAGINA: registro valido de inmunizacion antirrabica para perros y "
            "gatos; para cachorros de menos de 3 meses, prueba de que la madre fue vacunada al menos un "
            "mes y no mas de 12 meses antes del parto; prueba de que no hay restricciones de movimiento "
            "por control de rabia en la zona de origen; el pais de origen no debe tener enfermedades "
            "notificables relevantes; y presentar el animal en la oficina para inspeccion antes de la "
            "emision del permiso. Plazo de tramitacion: 1 dia habil. La pagina no publica tasas. "
            "cert_dias=60 NO sale de gov.bw (que no publica ninguna validez) sino del modelo SADC "
            "verificado de Interterritorial Movement Permit for Dogs and Cats, que cubre expresamente "
            "Sudafrica, Zimbabue, Botsuana, Lesoto y Esuatini y dice que sirve como permiso de "
            "movimiento 'for a period of sixty days from date of issue'. Es el documento que usaras "
            "de hecho entrando por tierra desde Sudafrica o Namibia. Ese modelo exige ademas que la "
            "rabia lleve puesta un minimo de 30 dias (60 si hubo casos de rabia en la zona en los tres "
            "meses anteriores). Para una llegada directa desde Europa no hay cifra publicada. "
            "APHIS tiene ficha de Botsuana pero es inutil: dice expresamente que no ha sido informada "
            "oficialmente de los requisitos y solo ofrece un modelo generico de certificado."
        ),
        "fuentes": [
            "https://www.gov.bw/business-compliance-agriculture-animal-husbandry/issuance-import-permit-live-animals-animal",
            "https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf",
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-botswana",
            "https://www.aphis.usda.gov/sites/default/files/botswana-dog-cat.pdf",
        ],
    },
    "sudafrica": {
        "organismo": "Director: Animal Health - Import Export Policy Unit, Department of Agriculture, Land Reform and Rural Development (DALRRD)",
        "url": "https://www.gov.za/services/import/import-animals-and-animal-products",
        "url_generica": False,
        "url_verificada": True,
        "email": "VetPermits@daff.gov.za",
        "tel": None,
        "cert": True,
        "cert_dias": 10,
        "cert_quien": "Veterinario oficial del pais de salida (emision del certificado Y su refrendo oficial deben caer dentro de los 10 dias previos al viaje)",
        "nota": (
            "URL VERIFICADA: ficha de servicio 'Import animals and animal products' en gov.za, que "
            "explica el tramite completo y confirma tu dato (VetPermits@daff.gov.za). "
            "TRAMITE: solicitar el permiso veterinario de importacion al 'Director: Animal Health, "
            "Import Export Policy Unit, Private Bag X138, Pretoria 0001' ANTES del envio. Hay tres "
            "formularios segun el animal vaya a cuarentena, a control adicional o a ninguna de las dos; "
            "se descargan en "
            "https://www.nda.gov.za/index.php/core-business/agricultural-production/animal-production/animal-health "
            "(enlace citado por gov.za; el dominio nda.gov.za rechaza la verificacion automatica por "
            "problema de certificado TLS, asi que NO se ha podido abrir). Una vez aprobado por el "
            "veterinario estatal de la oficina nacional, el permiso se emite en 3-5 dias habiles. "
            "TASA: la cifra de R140 por permiso que ya tenias es coherente con el sistema, pero gov.za "
            "solo dice que 'the cost is revised annually and published in the Government Gazette'; el "
            "tarifario vigente se publica en gov.za (ej. tarrifs-for-veterinary-imports-permits-2024). "
            "TELEFONO: no hay telefono publicado para permisos, solo fax (012 329 6892 / 012 329 8292); "
            "por eso tel=None. "
            "cert_dias=10 esta verificado en la guia APHIS de Sudafrica: 'Final veterinary inspection, "
            "health certificate issuance, and certificate endorsement must occur within 10 days of the "
            "pet's travel'. "
            "PRUEBAS OBLIGATORIAS (las mas duras de toda la ruta, planificar con 6-8 semanas): "
            "negativo en Brucella canis, Trypanosoma evansi, Babesia gibsoni, Dirofilaria immitis "
            "(filaria) y Leishmania, TODAS realizadas dentro de los 30 dias previos a la importacion, "
            "sin excepciones salvo dispensa expresa de Sudafrica. Microchip obligatorio y rabia puesta "
            "dentro de los 12 meses y al menos 30 dias antes (reducible a 15 dias con dispensa)."
        ),
        "fuentes": [
            "https://www.gov.za/services/import/import-animals-and-animal-products",
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-south-africa",
            "https://www.aphis.usda.gov/sites/default/files/south-africa-dog-guidance.pdf",
            "https://www.gov.uk/export-health-certificates/export-dogs-to-south-africa-certificate-6256",
            "https://assets.publishing.service.gov.uk/media/65438cda1f1a60000d360c76/6256NFG.pdf",
        ],
    },
    "namibia": {
        "organismo": "Directorate of Veterinary Services - Import/Export Office, Ministry of Agriculture, Water and Land Reform (MAWLR)",
        "url": "https://namibiatradeportal.gov.na/trade-goods/procedure-details/view_express_entity/485",
        "url_generica": False,
        "url_verificada": True,
        "email": "vet.permits@mawlr.gov.na",
        "tel": "+264 61 276592 (tambien +264 61 2087892 y +264 61 2087891/0; Walvis Bay +264 64 203073)",
        "cert": True,
        "cert_dias": None,
        "cert_quien": "Veterinario oficial del pais de salida (examen clinico dentro de los 10 dias previos a la salida)",
        "nota": (
            "URL VERIFICADA: 'Procedure for Application of a Namibian Veterinary Import Permit and "
            "Veterinary Import Permit for conveyance in transit' en el Namibia Trade Information Portal "
            "(dominio oficial gov.na). Confirma tu correo (ahi aparece como Vet.Permits@mawlr.gov.na). "
            "OFICINA: Government Office Park, Ministry of Agriculture, Water and Land Reform, East "
            "Wing, 2ª planta, Windhoek. Horario 08:00-13:00 y 14:00-17:00 de lunes a viernes. "
            "TASAS: N$ 150 el permiso veterinario de importacion; N$ 50 el permiso de transito - "
            "ESTE SEGUNDO ES EL RELEVANTE si solo atraviesas Namibia sin quedarte. "
            "PLAZO: maximo 3 dias habiles si la documentacion esta completa. "
            "FORMULARIO: se descarga en "
            "https://namibiatradeportal.gov.na/download_file/de4b6d16-da8f-4470-bb55-202d39fd2165/277 "
            "y tambien esta en mawf.gov.na ('Veterinary Import Application Form.pdf'). "
            "PASO EXTRA POCO CONOCIDO, verificado en la Veterinary Association of Namibia: antes de "
            "viajar hay que enviar por email al veterinario estatal namibio de la zona de destino una "
            "copia del permiso de importacion ya cumplimentado, el pasaporte de vacunacion del perro y "
            "los resultados negativos de las pruebas, para su verificacion. "
            "PRUEBAS: negativo en Brucella canis, Trypanosoma evansi, Leishmania, Dirofilaria y "
            "Babesia; segun el modelo APHIS, realizadas dentro de los 30 dias previos a la salida. "
            "Rabia entre 30 dias y 12 meses antes. Tras la llegada, 6 meses de preventivo de filaria. "
            "cert_dias=None: ni el portal ni MAWLR publican validez del certificado, y el certificado "
            "bilateral britanico para Namibia (EHC 3917) esta SUSPENDIDO ('on hold', no utilizable), "
            "asi que no hay cifra oficial que citar. Lo unico fijado es la ventana de examen clinico "
            "de 10 dias."
        ),
        "fuentes": [
            "https://namibiatradeportal.gov.na/trade-goods/procedure-details/view_express_entity/485",
            "https://van.org.na/section.php?secid=52&menuid=52",
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-namibia",
            "https://www.aphis.usda.gov/sites/default/files/namibia-dog_0.pdf",
            "https://www.gov.uk/export-health-certificates/export-dogs-to-namibia-certificate-3917",
        ],
    },
    "lesoto": {
        "organismo": "Department of Livestock Services - Imports and Exports Office, Ministry of Agriculture, Food Security and Nutrition",
        "url": "https://lesotho.eregulations.org/procedure/160?l=en",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": "+266 2231 7284 (fax +266 2231 1500)",
        "cert": True,
        "cert_dias": 60,
        "cert_quien": "Veterinario oficial del pais de salida; en entrada desde el area SADC, Interterritorial Movement Permit firmado por veterinario colegiado u oficial Y refrendado por un Government Veterinarian con sello oficial",
        "nota": (
            "URL VERIFICADA: procedimiento 'Obtain international veterinary import permit' del portal "
            "oficial eRegulations Lesotho (respaldado por el Gobierno y la UNCTAD). "
            "IMPORTANTE: el procedimiento esta CATALOGADO bajo 'importacion de carne', lo que despista, "
            "pero su cuadro de tasas verificado incluye expresamente 'LSL 10 - Permit fee for pets' "
            "junto a 'LSL 0-100 - Permit fee for live animals', asi que SI es el tramite que cubre al "
            "perro. El permiso de mascota cuesta 10 maloti, una miseria. "
            "OFICINA: Imports and Exports Office, Epidemiology and Data Management Section, Private Bag "
            "A 82, Maseru. Horario 08:00-16:30 de lunes a viernes. Web institucional: "
            "https://www.gov.ls/ministry-of-agriculture/ "
            "PLAZOS Y CALENDARIO SEMANAL (dato muy util): la solicitud debe presentarse entre 7 y 30 "
            "dias antes de la importacion, y la oficina trabaja por dias fijos - lunes y martes se "
            "reciben solicitudes, miercoles se tramitan, jueves y viernes se entregan los permisos. "
            "El tramite entero lleva de 1,5 a 8 dias. "
            "DOCUMENTOS: formulario de solicitud original, certificado veterinario del pais de origen "
            "(copia), certificado de estar al corriente con Hacienda (copia) y documento de identidad "
            "(copia). "
            "EMAIL: el portal publica el nombre de dos personas de contacto (Liou Ramokoatsi, Imports "
            "and Export Permit Assistant Clerk, tel +266 5818 7083 / +266 6229 7921; y Matsita Taoana) "
            "pero OFUSCA sus direcciones de correo, y no hay buzon generico del departamento: por eso "
            "email=None. "
            "cert_dias=60 procede del modelo SADC de Interterritorial Movement Permit for Dogs and "
            "Cats, verificado, que cubre expresamente Lesoto y vale 60 dias desde su emision - y como "
            "Lesoto es un enclave dentro de Sudafrica, ese es necesariamente el documento que usaras. "
            "Fuentes comerciales (pettravel) afirman que si se entra desde Botsuana, Malaui, Namibia, "
            "Sudafrica, Esuatini o Zimbabue no hace falta solicitud previa al Director of Animal "
            "Health; NO esta confirmado en fuente oficial, no te fies sin escribir antes."
        ),
        "fuentes": [
            "https://lesotho.eregulations.org/procedure/160?l=en",
            "https://lesotho.eregulations.org/Contacts/61?letter=d&l=en",
            "https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf",
        ],
    },
    "esuatini": {
        "organismo": "Department of Veterinary and Livestock Services, Ministry of Agriculture (Eswatini)",
        "url": "https://www.gov.sz/index.php/ministries-departments/ministry-of-agriculture/veterinary-a-livestock",
        "url_generica": True,
        "url_verificada": True,
        "email": None,
        "tel": "+268 2404 2731/9 / +268 2404 6362",
        "cert": True,
        "cert_dias": 60,
        "cert_quien": "Veterinario oficial del pais de salida; en entrada desde el area SADC, Interterritorial Movement Permit firmado por veterinario colegiado u oficial Y refrendado por un Government Veterinarian con sello oficial",
        "nota": (
            "url_generica=True: NO EXISTE pagina del tramite. La URL que se da es la ficha del "
            "departamento veterinario dentro de gov.sz - esta verificada y es el nivel mas concreto "
            "que hay (no es la portada del ministerio), pero solo describe el mandato del "
            "departamento y NO menciona en ningun momento permisos de importacion ni mascotas. "
            "Se ha buscado y descartado: APHIS no tiene ficha de Esuatini/Swazilandia en pet-travel; "
            "el Reino Unido no tiene certificado bilateral de perros y gatos con Esuatini (solo uno de "
            "carne, el 7931); y el Eswatini Trade Information Portal no publica ninguna medida ni "
            "procedimiento sobre animales vivos o mascotas (se comprobo el procedimiento id=33, que "
            "resulto ser el de despacho aduanero de vehiculos). "
            "CONTACTO: direccion Ministry of Agriculture Headquarters, P.O. Box 162, Mbabane. El "
            "Director del departamento figura como Dr. Xolani Dlamini, movil +268 7606 2602 - util "
            "porque en Esuatini el movil suele responder antes que la centralita. NO hay ningun correo "
            "publicado en gov.sz para este departamento, por eso email=None: habra que llamar. "
            "cert_dias=60 procede del modelo SADC de Interterritorial Movement Permit for Dogs and "
            "Cats, verificado, que cubre expresamente Esuatini (aparece con su nombre antiguo, "
            "Swaziland) y vale 60 dias desde su emision; entrando por tierra desde Sudafrica o "
            "Mozambique es el documento que usaras. Exige rabia puesta con un minimo de 30 dias (60 si "
            "hubo casos de rabia en la zona en los tres meses anteriores). "
            "Fuentes comerciales (pettravel) hablan de un certificado emitido dentro de los 10 dias "
            "previos a la entrada y de solicitud al 'Director of Animal Health' salvo procedencia SADC; "
            "NO confirmado en fuente oficial, no se consigna."
        ),
        "fuentes": [
            "https://www.gov.sz/index.php/ministries-departments/ministry-of-agriculture/veterinary-a-livestock",
            "https://www.elsenburg.com/wp-content/uploads/2022/02/VHC-Interterritorial-Movement-permit-SADC-dogs_cats-template-2012_0.pdf",
            "https://www.eswatinitradeportal.gov.sz/index.php?r=SearchMeasures/index",
        ],
    },
}

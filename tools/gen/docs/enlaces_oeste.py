# -*- coding: utf-8 -*-
# Datos de contacto de los organismos que emiten el permiso de importacion
# de animales de compania (perro) - ruta overland Africa Occidental 2027.
# Estado: EN CONSTRUCCION (rellenado incremental).
DATOS = {
    "marruecos": {
        "organismo": "Office National de Sécurité Sanitaire des Produits Alimentaires (ONSSA) - Direction des Services Vétérinaires",
        "url": "https://www.onssa.gov.ma/controle-a-limportation-et-a-lexportation/controle-a-limportation/importation-des-animaux-vivants/chiens-et-chats/",
        "url_generica": False,
        "url_verificada": False,
        "email": None,
        "tel": "+212 5 37 67 65 00",
        "cert": True,
        "cert_dias": None,
        "cert_quien": "Veterinario oficial del pais de salida (en la UE, veterinario oficial habilitado; certificado en modelo bilateral, no vale el pasaporte europeo solo)",
        "nota": (
            "AVISO: el dominio onssa.gov.ma NO ES ALCANZABLE desde el entorno de verificacion (la "
            "conexion es rechazada), asi que la URL NO se ha podido abrir ni comprobar; aparece "
            "indexada con el titulo 'Chiens et chats - ONSSA' bajo la ruta de control a la importacion "
            "de animales vivos, por lo que casi seguro es la pagina correcta, pero NO esta verificada. "
            "ONSSA publica ademas el modelo UE en "
            "onssa.gov.ma/wp-content/uploads/2023/07/Importation-au-Maroc-de-chiens-et-chats-a-partir-de-lUE.pdf "
            "(tampoco verificado). VALIDEZ DEL CERTIFICADO: no hay cifra verificada para salida desde "
            "la UE; los modelos bilaterales verificados dan cifras distintas (Reino Unido: 7 dias; "
            "EEUU: 3 dias tras el visado de APHIS), por eso cert_dias va a None. "
            "Requisitos comunes verificados: microchip o tatuaje previo a la vacuna, vacuna antirrabica "
            "inactivada con >=21 dias desde la primovacunacion, examen clinico en las 24 h previas al "
            "embarque y procedencia de pais libre de rabia los 6 meses anteriores. "
            "Telefono: centralita de ONSSA en Rabat (av. Hadj Ahmed Cherkaoui, Agdal) segun directorio "
            "comercial telecontact.ma, NO confirmado en fuente oficial. Email: no publicado en fuente "
            "accesible."
        ),
        "fuentes": [
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-morocco",
            "https://www.aphis.usda.gov/sites/default/files/morocco-dog-cat_0.pdf",
            "https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-morocco-certificate-3916",
            "https://assets.publishing.service.gov.uk/media/689da555e95097004f723f64/3916EHC_V4.pdf",
            "https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm",
            "https://www.telecontact.ma/annonceur/onssa/3257548/rabat.php",
        ],
    },
    "mauritania": {
        "organismo": "Direction des Services Vétérinaires (DSV) / Direction de l'Élevage, Ministère de l'Élevage (antes Ministère du Développement Rural)",
        "url": "https://elevage.gov.mr/",
        "url_generica": True,
        "url_verificada": True,
        "email": None,
        "tel": None,
        "cert": True,
        "cert_dias": None,
        "cert_quien": "Veterinario oficial del pais de salida (certificado zoosanitario)",
        "nota": (
            "NO ENCONTRADA ninguna pagina, ni del Gobierno mauritano ni consular, que publique el "
            "tramite de importacion de animales de compania. APHIS NO tiene ficha de Mauritania en "
            "pet-travel (la URL .../pet-travel-us-mauritania devuelve 404) y Mauritania no figura en "
            "su menu de destinos. La web del Ministere de l'Elevage (elevage.gov.mr) entra en bucle de "
            "redirecciones y no se ha podido abrir. El unico dato verificado es que la importacion de "
            "animales vivos exige certificado zoosanitario (portal logistico LCA/Logistics Cluster) y "
            "la identificacion del organismo competente en el directorio de Delegados de la OMSA/WOAH "
            "(Director des Services Veterinaires, Ministere du Developpement Rural, Ksar, Nouakchott; "
            "el punto focal figura tambien como Direction de l'Elevage, BP 180, Nouakchott). "
            "SOLO PORTADA: la URL dada es la portada del Ministere de l'Elevage (elevage.gov.mr), que "
            "si carga y tiene una seccion de servicios veterinarios (en arabe), pero NO publica ficha "
            "del tramite ni telefono/email de contacto. "
            "Ruta practica recomendada: escribir a la Embajada de Mauritania en Paris "
            "(ambarimparis@gmail.com, +33 1 45 04 88 54), cuya pagina consular esta verificada pero NO "
            "menciona animales; o a la Embajada en Madrid. Sin plazo de validez del certificado publicado."
        ),
        "fuentes": [
            "https://elevage.gov.mr/",
            "https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm",
            "https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/animalwelfare/PF_animalwelfare_fr.htm",
            "https://lca.logcluster.org/13-mauritanie-information-douaniere",
            "https://ambarimparis.fr/informations-consulaires/",
        ],
    },
    "senegal": {
        "organismo": "Direction des Services Vétérinaires (DSV), Ministère de l'Agriculture, de la Souveraineté Alimentaire et de l'Élevage",
        "url": "https://senegalservices.sn/demarche/demander-lautorisation-dimporter-des-animaux-de-compagnie",
        "url_generica": False,
        "url_verificada": False,
        "email": "contacts@elevage.gouv.sn",
        "tel": None,
        "cert": True,
        "cert_dias": 21,
        "cert_quien": "Veterinario oficial/acreditado del pais de salida (en la UE, veterinario oficial); debe acompañar al animal",
        "nota": (
            "LA URL QUE FALTABA: el portal oficial Senegal Services publica la ficha del tramite con el "
            "titulo exacto 'Demander l'autorisation d'importer des animaux de compagnie'. AVISO: NO se ha "
            "podido abrir desde el entorno de verificacion (senegalservices.sn y servicepublic.gouv.sn "
            "rechazan la conexion), por eso url_verificada=False; el titulo y la ruta si estan indexados. "
            "Ficha del mismo tramite tambien en servicepublic.gouv.sn "
            "(/index.php/demarche_administrative/demarche/1/1018/22/254), igualmente inaccesible. "
            "URL ALTERNATIVA SI VERIFICADA (abierta y comprobada, trata de Senegal y de perros): "
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-senegal . "
            "Contenido confirmado ahi: hace falta PERMISO DE IMPORTACION previo del Ministere de "
            "l'Agriculture, de la Souverainete Alimentaire et de l'Elevage, valido 3 meses desde su "
            "emision; certificado sanitario emitido dentro de los 21 dias previos al viaje; vacuna "
            "antirrabica al menos 21 dias antes. Emails operativos de la DSV segun APHIS: "
            "dsvmepa@gmail.com y wadesanou@gmail.com. Direccion: 37 Avenue Pasteur, BP 67, Dakar. "
            "Telefono no publicado en ninguna fuente verificada."
        ),
        "fuentes": [
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-senegal",
            "https://senegalservices.sn/demarche/demander-lautorisation-dimporter-des-animaux-de-compagnie",
            "https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-senegal-certificate-6367",
            "https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm",
        ],
    },
    "gambia": {
        "organismo": "Department of Livestock Services (Veterinary Services), Ministry of Agriculture",
        "url": "https://gambiaembassy.eu/faqs/",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": "+220 4397472",
        "cert": True,
        "cert_dias": None,
        "cert_quien": "Veterinario del pais de origen ('Veterinarian's health certificate issued at point of origin')",
        "nota": (
            "La Embajada de Gambia en Bruselas (jurisdiccion UE) dice que el permiso de importacion se "
            "obtiene REGISTRANDO al animal EN GAMBIA, despues de llegar, ante el Gambian Veterinary "
            "Department; no hay permiso previo publicado. Exige certificado veterinario de origen, "
            "cartilla de vacunacion y vacuna antirrabica. Telefono dado por la embajada para el "
            "departamento veterinario: +220 4397472. "
            "PENDIENTE: no hay web propia del Department of Livestock Services localizable; no se ha "
            "encontrado email oficial ni validez publicada del certificado. APHIS no tiene ficha de "
            "Gambia en pet-travel."
        ),
        "fuentes": [
            "https://gambiaembassy.eu/faqs/",
            "https://www.aphis.usda.gov/live-animal-export/export-live-animals-gambia",
        ],
    },
    "guinea": {
        "organismo": "Direction Nationale des Services Vétérinaires (DNSV), Ministère de l'Élevage et des Productions Animales",
        "url": "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-guinea",
        "url_generica": False,
        "url_verificada": True,
        "email": "contact@elevage.gov.gn",
        "tel": None,
        "cert": True,
        "cert_dias": None,
        "cert_quien": "Veterinario oficial/acreditado del pais de salida",
        "nota": (
            "La ficha APHIS de Guinea esta verificada y es especifica del pais, pero solo exige un "
            "certificado sanitario internacional para perros y gatos y NO publica ni plazo de validez "
            "ni permiso de importacion previo: APHIS remite explicitamente a confirmar con las "
            "autoridades guineanas o la embajada. El organismo competente es la DNSV (identificado en "
            "el directorio de Delegados de la OMSA/WOAH y en la pagina de misiones del Ministerio, "
            "elevage.gov.gn); su direccion postal es BP 559, Conakry. "
            "El email dado es el buzon general del Ministerio de Elevage, unico verificado; el "
            "telefono que publica esa web es un marcador de posicion (+224 000 00 00 00), por eso va a None. "
            "NO se ha encontrado ninguna pagina guineana que publique el tramite."
        ),
        "fuentes": [
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-guinea",
            "https://www.elevage.gov.gn/mission-et-attributions/",
            "https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm",
        ],
    },
    "sierra-leona": {
        "organismo": "Livestock and Veterinary Services Division, Ministry of Agriculture, Forestry and Food Security (MAFFS)",
        "url": "https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-sierra-leone-certificate-6548",
        "url_generica": False,
        "url_verificada": True,
        "email": None,
        "tel": None,
        "cert": True,
        "cert_dias": 7,
        "cert_quien": "Veterinario oficial (Official Veterinarian) del pais de salida",
        "nota": (
            "NO EXISTE pagina del Gobierno de Sierra Leona ni consular que publique el tramite; Sierra "
            "Leona tampoco figura en el menu de destinos de pet-travel de APHIS. La URL dada es la "
            "ficha oficial britanica (DEFRA/APHA) del certificado 6548 'Export cats and dogs to Sierra "
            "Leone', verificada, con el modelo de certificado y las notas de orientacion; el modelo "
            "(6548EHC_V3.pdf) esta comprobado y dice literalmente que el certificado es valido 7 dias "
            "desde la firma, exige examen clinico sin signos de enfermedad contagiosa (moquillo, rabia, "
            "parasitos externos) y constancia de la vacuna antirrabica. En ese modelo NO se menciona "
            "permiso de importacion previo, pero eso no prueba que no lo haya. "
            "Organismo competente identificado en el directorio de Delegados de la OMSA/WOAH: "
            "Livestock and Veterinary Services Division del MAFFS, Youyi Building, Freetown. "
            "Sin email ni telefono publicados en fuente verificada: confirmar por la Alta Comision de "
            "Sierra Leona antes de salir."
        ),
        "fuentes": [
            "https://www.gov.uk/export-health-certificates/export-cats-and-dogs-to-sierra-leone-certificate-6548",
            "https://assets.publishing.service.gov.uk/media/5bceea93ed915d4315aba3e1/6548EHC_V3.pdf",
            "https://www.woah.org/fileadmin/Home/eng/About_us/RRData/africa/Delegates/Delegates_en.htm",
            "https://www.aphis.usda.gov/live-animal-export/export-live-animals-sierra-leone",
        ],
    },
    "liberia": {
        "organismo": "Consulate General / Embassy of the Republic of Liberia (emite el 'Pet Clearance'); autoridad interna: Ministry of Agriculture de Liberia",
        "url": "https://liberiaconsulate-ny.com/consulate-services/pet-clearance/",
        "url_generica": False,
        "url_verificada": True,
        "email": "info@liberiaconsulate-ny.com",
        "tel": "+1 212 687 1025",
        "cert": True,
        "cert_dias": 30,
        "cert_quien": "Veterinario colegiado del pais de salida (o servicio veterinario oficial)",
        "nota": (
            "En Liberia el permiso es un 'Pet Clearance' que expide la MISION DIPLOMATICA liberiana "
            "ANTES del viaje, no un ministerio en Monrovia. El certificado sanitario debe tener fecha "
            "no superior a 30 dias antes de la llegada. Tasa 100 USD por animal en el consulado de NY. "
            "OJO viaje desde España: hay que pedirlo a la Embajada de Liberia acreditada ante España "
            "(no a la de Nueva York); los datos de aqui son los del consulado de NY, los unicos con "
            "pagina verificada. La Embajada de Liberia en EEUU publica el mismo tramite en "
            "liberianembassyus.org (tel +1 202 723 0437, info@liberianembassyus.org). "
            "PENDIENTE: no se ha encontrado ninguna pagina del Gobierno de Liberia que publique el tramite."
        ),
        "fuentes": [
            "https://liberiaconsulate-ny.com/consulate-services/pet-clearance/",
            "https://www.liberianembassyus.org/document/requirements-for-pet-travel-to-liberia",
        ],
    },
    "costa-de-marfil": {
        "organismo": "Direction des Services Vétérinaires (DSV), Ministère des Ressources Animales et Halieutiques",
        "url": "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ivory-coast",
        "url_generica": False,
        "url_verificada": True,
        "email": "carv.dsvci@gmail.com",
        "tel": "+225 27 20 21 89 72",
        "cert": True,
        "cert_dias": 10,
        "cert_quien": "Veterinario oficial/acreditado del pais de salida, refrendado por la autoridad veterinaria nacional",
        "nota": (
            "Hace falta AUTORIZACION DE IMPORTACION previa de la DSV: formulario de solicitud + copia "
            "del certificado de vacunacion antirrabica en vigor. Segundo email: dsv.sdsa2017@gmail.com. "
            "Rabia: si es primovacunacion o refuerzo fuera de plazo, esperar 21 dias antes de viajar. "
            "Direccion DSV: Cite Administrative, Tour C, 11e etage, Abidjan-Plateau. El telefono "
            "figura en el portal GUCE como 20 21 89 72 (numeracion antigua de 8 cifras); se da ya "
            "con el prefijo 27 de la numeracion a 10 cifras vigente desde 2021, SIN VERIFICAR por llamada. "
            "Formulario oficial de solicitud (PDF, en frances, del MIRAH) reproducido por APHIS: "
            "ptw-ivory-coast-import-permit-application.pdf."
        ),
        "fuentes": [
            "https://www.aphis.usda.gov/pet-travel/us-to-another-country-export/pet-travel-us-ivory-coast",
            "https://www.aphis.usda.gov/sites/default/files/ptw-ivory-coast-import-permit-application.pdf",
            "https://www.gucecotedivoire.ci/pwic/animaux-vivants/",
        ],
    },
}

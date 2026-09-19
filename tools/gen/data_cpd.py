# -*- coding: utf-8 -*-
"""Carnet de Passages en Douane: situación país por país.

Clasificación para un vehículo particular matriculado en España que entra y
sale POR TIERRA. El régimen cambia por completo si el vehículo llega o sale
en barco: ahí el CPD pasa a ser muy recomendable en casi todas partes.

Niveles:
  obligatorio  — sin CPD no se entra. Rojo.
  recomendable — hay alternativa, pero el CPD evita un coste o una pelea. Naranja.
  no           — no hace falta; se resuelve en frontera. Verde.

Investigación de septiembre de 2026, auditada afirmación por afirmación el
12-09-2026 contra las fuentes reales (informe «auditoria-cpd-2027» del proyecto).
Aviso general: casi todos los importes en USD de África occidental y central
salen de UNA sola fuente, el relato de Rogue Wanderers de marzo de 2023; se
indica «(2023)» donde es el caso.
"""

# slug: (nivel, confianza, alternativa, coste, nota)
CPD = {
    # ---------------------------------------------------------- ruta de bajada
    "marruecos": ("no", "CONFIRMADO", "Declaración D16ter (admisión temporal)",
                  "Gratis · 180 días por año civil",
                  "Se tramita en la frontera (una fuente antigua habla de rellenarla en línea; las de "
                  "2026 hablan de trámite al paso). Los 180 días son acumulados por año natural. No "
                  "aparece en ninguna lista de países que exijan CPD."),
    "sahara-occidental": ("no", "PROBABLE", "Cubierto por el D16ter marroquí", "—",
                          "No hay aduana propia: se entra con el trámite hecho en Tánger o Tarfaya. "
                          "Coherente con todos los relatos del cruce de Guerguerat; sin cita directa."),
    "mauritania": ("no", "CONFIRMADO", "Passavant / laissez-passer en frontera", "~10 € / 100 MAD",
                   "Guerguerat. Validez mínima 10 días: pedir más si no se va directo a Senegal. "
                   "No es miembro de la CEDEAO ni de la Carte Brune, así que ese seguro no sirve aquí."),
    "senegal": ("recomendable", "CONFIRMADO", "Passavant (norma: 10 días + 2 prórrogas de 15; práctica: 48-72 h prorrogables)",
                "5.000 FCFA (~8 €) si el vehículo tiene 8 años o menos · ~250 € si los supera",
                "Figura en la lista de países en los que el RACE dice que el CPD «es requerido». "
                "El problema no es el CPD en sí: es el límite de edad del vehículo (8 años; el decreto "
                "de octubre de 2025 lo sube a 10 para turismos, pero ningún relato de 2026 ha visto "
                "aplicarlo todavía en frontera). Es norma de importación definitiva, pero la aduana la "
                "aplica igual al turista, y la aplica TANTO en Rosso COMO en Diama (los 250 € están "
                "documentados en Diama en 2017, 2020, 2024, 2025 y 2026). Con carnet también se paga el "
                "passavant de 5.000 FCFA y hay que sellarlo en la aduana de Dakar. Única vía barata "
                "documentada: entrar desde Mali por Kidira (4 €, relato de 2017, sin confirmar después)."),
    "gambia": ("recomendable", "EN DISPUTA", "TIP en frontera", "~11 USD (2023)",
               "Solo en la subida. La Gambia Revenue Authority dice que «para extranjeros hay que "
               "obtener un carnet de passage», y Horizons Unlimited la pone en su tabla de países que lo "
               "EXIGEN; en la práctica un overlander sin carnet pagó 11 USD de TIP (2023) y otro con "
               "carnet entró sin pagar (2026). Con carnet, resuelto; sin él, contar con el TIP."),
    "guinea": ("no", "PROBABLE", "Laissez-passer en frontera", "Gratis (2023) · 50.000 GNF (~5 €, 2017)",
               "Moneda: franco guineano (GNF), no FCFA. Horizons Unlimited la incluye en su tabla de "
               "países que EXIGEN carnet, pero es una tabla antigua («to the best of our knowledge») y "
               "los relatos recientes entran con laissez-passer."),
    "sierra-leona": ("no", "PROBABLE", "TIP en frontera", "~17 USD (2023)",
                     "Una sola fuente de campo (2023). La guía Visit Sierra Leone 2026 dice: carnet o TIP en frontera."),
    "liberia": ("no", "PROBABLE", "Laissez-passer, tramitado en la embajada de Liberia en Conakry (no en frontera)",
                "~90 USD (2023)",
                "Una sola fuente primaria (2023): el papel se pidió en la embajada de Conakry con "
                "entrega al día siguiente, no en el puesto fronterizo."),
    "costa-de-marfil": ("no", "PROBABLE", "Admisión temporal en frontera", "Sin dato posterior a 2023",
                        "El CPD se acepta pero no se exige (Horizons Unlimited la lista solo en la tabla "
                        "de países que lo ACEPTAN). Fronteras terrestres reabiertas el 15 de febrero de "
                        "2023: los 82 USD que circulan eran el laissez-passer de ministerio de la época de "
                        "fronteras cerradas, que ya no aplica. No hay relato verificado de entrada terrestre "
                        "sin carnet después de 2023."),
    "ghana": ("recomendable", "CONFIRMADO", "Permiso de tránsito con localizador GPS",
              "~490 USD con tracker (2023) · ~12 € (150 GHS) si lo dan como excepción (2026)",
              "El permiso más caro de África occidental sin CPD: 490 de los 795 USD que un overlander "
              "documentó en toda la región (Elubo, 2023). Obliga a ruta directa y seguimiento. En julio "
              "de 2026 otra pareja entró por Aflao con una carta del cónsul de Ghana en Benín y pagó los "
              "150 GHS de todo el mundo; según su propio relato la clave fue la paciencia y la "
              "negociación más que la carta, y otros overlanders de la misma temporada pagaron 600 € o más."),
    "togo": ("no", "PROBABLE", "TIP", "~11 USD (2023)",
             "Duración del TIP sin fuente. Referencia local: laissez-passer de 6.000 FCFA (enero de 2025)."),
    "benin": ("no", "CONFIRMADO", "Laissez-passer de aduanas (desmaterializado desde el 15-09-2026 en la plataforma CUSTOMS WEBB)",
              "~16 USD (2023)",
              "Circular del director general de Aduanas de 2 de septiembre de 2026: el laissez-passer "
              "para vehículos con matrícula extranjera se emite en CUSTOMS WEBB con código QR que se "
              "presenta en frontera; se paga por TresorPay o en caja y caduca a los 3 días si no se "
              "paga. Tarifa de 2026 sin publicar."),
    "nigeria": ("recomendable", "EN DISPUTA", "Temporary Vehicle Admission Permit («Safe Passage»), 90 + 30 días",
                "Gratuito en 2023 · importe de 2026 sin publicar",
                "LAS FUENTES NO COINCIDEN. El 7 de enero de 2026 el Nigeria Customs Service puso en marcha "
                "un permiso de admisión temporal de 90 días (prorrogable 30), «electronically recorded». "
                "El comunicado oficial lista el CPD ENTRE LOS DOCUMENTOS A PRESENTAR en frontera "
                "(«international passport, international driver's license, vehicle registration, "
                "insurance, and CPD») y dice que el sistema se alinea con las «CPD regulations»: el texto "
                "oficial refuerza el carnet, no lo relaja. Horizons Unlimited también la pone entre los "
                "países que lo EXIGEN. En contra: en 2023, antes del permiso, un overlander entró sin "
                "carnet y gratis. No hay ningún relato de entrada sin carnet posterior a enero de 2026. "
                "Con carnet: TVAP + CPD y sin discusión. Sin carnet: nadie ha documentado que lo concedan."),
    "camerun": ("no", "PROBABLE", "Passavant (corto en frontera, definitivo en Banyo)", "~15 USD (2023)",
                "Una sola fuente de campo (2023)."),
    "congo": ("no", "PROBABLE", "TIP / laissez-passer por confirmar en Massabi", "Sin tarifa pública localizada",
              "La ruta principal ya no usa el ferry: sale y entra por Tchiamba-Nzassi/Massabi. El puesto "
              "está operativo y tiene aduana, pero no se ha localizado el procedimiento ni el coste oficial "
              "para un turismo extranjero. Llevar el CPD y pedir confirmación escrita antes del paso."),
    "rd-congo": ("no", "PROBABLE", "TIP / laissez-passer por confirmar en Yema y Lufu", "Sin tarifa pública localizada",
                 "La ruta principal cruza Kongo Central por Yema–Muanda–Matadi–Lufu, dos veces y sin ferry. "
                 "Cada entrada puede exigir seguro y documento temporal nuevos. Kinshasa y la barcaza quedan "
                 "solo como contingencia secundaria."),
    "angola": ("no", "PROBABLE", "Importación temporal por confirmar en cada entrada",
               "43.236,78 AOA por entrada de turismo ligero (aviso oficial, julio de 2025)",
               "La referencia oficial suma pase fronterizo y autorización de transporte turístico. El viaje "
               "genera hasta cuatro entradas angoleñas entre Cabinda y el territorio continental: presupuestar "
               "cada una hasta que ANTT confirme por escrito si el pase de 30 días puede reutilizarse. Llevar "
               "el CPD, pero no permitir un sellado incorrecto ni asumir que sustituye el trámite local."),
    # ------------------------------------------------------------------ bucle
    "zambia": ("no", "CONFIRMADO", "Sin TIP: paquete de tasas en frontera", "~60-100 USD (datos 2014-2019)",
               "Carbon tax (se paga en kwachas según cilindrada: 150-275 ZMW en 2017-2019, unos 6-11 "
               "USD; sin dato de 2025-26), Road Toll de la NRFA (~20 USD), council levy (varía por "
               "frontera: 30 ZMW o hasta 20 USD por coche) y seguro de responsabilidad civil. Ninguna "
               "fuente menciona fianza alguna para turistas."),
    "tanzania": ("no", "CONFIRMADO", "TIP en frontera + road tax", "25 USD/mes (+5 USD de tasa menor, dato de 2014)",
                 "Horizons Unlimited la incluye en su tabla de países que EXIGEN carnet, pero el TIP en "
                 "frontera sin carnet está documentado (vehículo canadiense en 2018; relatos de 2025 con "
                 "una nueva app en el puesto)."),
    "kenia": ("obligatorio", "CONFIRMADO", "Form C32 (gratis, 14 días, prorrogable hasta 90) + Foreign Vehicle Permit",
              "C32 gratis · FVP 21-101 USD según cilindrada y plazo (cifras de 2018, no oficiales)",
              "EL MÁS EXIGENTE DE LA RUTA. Lo dicen los dos emisores de carnets consultados: el RACE lo "
              "lista como país en el que el CPD «es requerido», y la Automobile Association de Sudáfrica "
              "escribe que es «obligatorio para Egipto y Kenia». La KRA tiene dos avisos que no casan: "
              "el 774 (efectivo desde el 15-12-2017) exige «International Circulation Permit (Carnet de "
              "Passage en Douane)» a vehículos de fuera de la EAC/COMESA; el 1870 (sin fecha visible) "
              "admite «Form C32 OR carnet» y da un permiso temporal gratuito de 14 días a quien entra "
              "solo con el C32. La alternativa existe sobre el papel, pero en el mostrador la discuten: "
              "un viajero en Loitoktok relata que «even with the C32 printed online form he told me it's "
              "not possible without carnet». El FVP lo emite la NTSA vía eCitizen; las tarifas "
              "(<2000cc 21 USD/mes o 51 USD/3 meses; >2000cc 41 y 101) son de un blog de 2018 y no se "
              "ha localizado tarifa oficial vigente. Sin CPD: cuenta eCitizen hecha antes de llegar, "
              "respuesta escrita de la KRA guardada y el aviso 1870 impreso."),
    "uganda": ("no", "CONFIRMADO", "Temporary Road Licence de la URA (máx. 90 días)", "~71.000 UGX/mes (~17 €, dato de 2019)",
               "Uganda NO acepta el carnet. Tracks4Africa (2016, actualizado en 2023): «some countries "
               "(like Uganda) do not accept or recognise a Carnet». Llevarlo aquí es aval inmovilizado a "
               "cambio de nada."),
    "ruanda": ("no", "PROBABLE", "TIP de 15 días + seguro", "TIP 15.000 RWF (~11 €) · seguro aparte (Yellow Card, 20-60 USD)",
               "Ojo al calendario, no al carnet: 15 días sin prórroga posible en frontera (Tracks4Africa, 2019)."),
    "malaui": ("no", "CONFIRMADO", "TIP + Road Access Fee + seguro", "TIP 5.000-10.000 MWK + 20 USD de RAF",
               "Road Access Fee de 20 USD por vehículo desde noviembre de 2017; no pagarla son 500 USD "
               "de multa valorada en frontera (fuente de 2017, sin confirmación posterior)."),
    "mozambique": ("no", "CONFIRMADO", "TIP obligatorio (30 días) + seguro local obligatorio", "~11-17 € (2026)",
                   "El carnet no ahorra nada: el TIP es obligatorio aunque se lleve (Tucks' Truck 2015: "
                   "«not accepted»; AA de Sudáfrica 2020: TIP «compulsory»). Seguro de una aseguradora "
                   "mozambiqueña en frontera (si la Yellow Card COMESA vale aquí no está verificado). Dos "
                   "triángulos, dos chalecos y extintor de 1 kg. Verificar el sello del TIP antes de salir "
                   "del puesto."),
    "zimbabue": ("no", "CONFIRMADO", "TIP de ZIMRA (hasta 3 meses, sin prórroga) + carbon tax + seguro + peajes", "~45-70 USD",
                 "El Road Access Fee fue eliminado por el Statutory Instrument 113 de 2026 (24-07-2026): "
                 "las guías que aún lo listan están desactualizadas. Quedan seguro (~30 USD/mes), carbon "
                 "tax (~10 USD) y peajes ZINARA (~10 USD por sentido)."),
    "botsuana": ("no", "CONFIRMADO", "Temporary Import Permit de BURS + National Road Safety Fund levy (P40)", "~8-11 €",
                 "La página de BURS habla de vehículos temporales «not exceeding 14 days»: pendiente de "
                 "aclarar si aplica al turista de estancia larga (los overlanders citan 30-90 días)."),
    "namibia": ("no", "CONFIRMADO", "Cross-Border Charge del RFA + permiso temporal en frontera", "N$534 (~27 €) por entrada",
                "Tarifa del Road Fund Administration vigente desde el 01-08-2026 (tipo 2: turismos y "
                "pick-ups; N$340 para motos y caravanas). Las guías que aún dicen R220 están "
                "desactualizadas. El permiso temporal de aduanas no tiene página oficial localizada."),
    "sudafrica": ("recomendable", "EN DISPUTA", "TIP de 6 meses multientrada, gratuito, vía SARS Traveller Management System",
                  "Gratis (TIP) · con carnet, según ADAC, se evita el depósito del arancel",
                  "LAS FUENTES NO COINCIDEN, y hay que decidir con eso encima de la mesa. Lo seguro: desde "
                  "el 1 de junio de 2026 hay que declarar el vehículo en el TMS de SARS antes de llegar a "
                  "la frontera (SARS «encourages» hacerlo en línea; se puede en el puesto); el TIP es de "
                  "seis meses, multientrada, gratuito, y SARS es explícito en que no hay exención por ser "
                  "SACU. Lo que NO está resuelto es si a un vehículo de fuera de la SACU se lo dan sin "
                  "garantía: las páginas del TMS no mencionan el carnet, pero SARS mantiene una política "
                  "de carnets (SC-TA-01-04, 2024) y el ADAC —emisor alemán, página del 02-06-2026— afirma "
                  "que «this Traveller Declaration does not replace the Carnet», que para vehículos "
                  "matriculados fuera de la SACU «a Carnet de Passages remains mandatory» y que sin él "
                  "hay TIP con depósito del arancel y agente aduanero (SAD500). El RACE lista Sudáfrica "
                  "entre los países en los que el CPD «es requerido». La cita de la AA sudafricana "
                  "(«compulsory for Egypt and Kenya… recommended outside the SACU») es real, pero va "
                  "dirigida a conductores sudafricanos que SALEN de la SACU, no a vehículos extranjeros "
                  "que entran: no sirve para relajar el caso. Ningún overlander no-SACU ha contado por "
                  "escrito una entrada terrestre posterior al 1 de junio de 2026. Hasta tener respuesta "
                  "escrita de SARS se trata como recomendable-casi-obligatorio."),
    "lesoto": ("no", "PROBABLE", "Permiso en frontera + peaje por peso + seguro", "~1,5-4,5 €",
               "Peaje por peso (~R30 en 2026). Seguro y permiso sin fuente reciente."),
    "esuatini": ("no", "PROBABLE", "TIP en frontera + road tax", "~3-6 €", "Road tax de R50 a la entrada (AA 2020; Drive SA 2026)."),
    "gabon": ("no", "PROBABLE", "TIP (se tramita en Bitam, no en la frontera)", "Gratis (2023)", "Una sola fuente de campo (2023)."),
    "madagascar": ("no", "SIN CONFIRMAR", "No aplica: 4x4 de alquiler con conductor; los propios se quedan en el continente", "0 €",
              "carnetdepassage.org (AIT/FIA) confirma que no hay club emisor en Madagascar y no dice si la aduana acepta el CPD. Como no existe ferry de pasajeros con vehículo (Rough Guides) y a Toamasina solo llega carga, el vehículo propio no entra en el plan. Si algún día se embarcara, la admisión temporal se gestionaría con un transitario de Toamasina; ningún relato overland 2019–2026 abierto en esta sesión describe ese trámite."),
    # ------------------------------------------------- fuera de la ruta, de referencia
    "egipto": ("obligatorio", "CONFIRMADO", "CPD local emitido en frontera por el club automovilístico egipcio (200-500 USD más depósito)", "200-500 USD el local; el europeo, con depósito de hasta el 200% del valor del vehículo",
              "Egipto es uno de los pocos países de África que sigue exigiendo el Carnet de Passages, según la Overlanding Association. El emisor egipcio es el Automobile et Touring Club d'Egypte (10 rue Kasr el Nil, El Cairo, +202 257 43 355), con validez de un año renovable, según carnetdepassage.org. Dan Grec documentó en abril de 2019 la emisión de un carnet local en la propia frontera por 500 USD. Además del carnet hacen falta matrícula egipcia temporal, permiso de conducir egipcio y seguro de terceros local, y a la salida un certificado de tráfico sin multas para poder cancelarlo."),
    "tunez": ("no", "PROBABLE", "Admisión temporal anotada en el pasaporte + registro previo Smart Traveller (QR)", "Gratis · 3 meses (tasa de 30 TND citada en 2023, por confirmar)",
              "FUERA DE LA RUTA (solo viaje aparte en ferry). Ningún relato de 2023–2026 usó CPD: la aduana "
              "de La Goulette anota el vehículo en el pasaporte del conductor y desde junio de 2025 exige "
              "registro previo en douane.gov.tn con código QR. Confirmación oficial pendiente (la web de la "
              "aduana no se pudo abrir); el Touring Club de Tunisie es el emisor local del carnet."),
    "mali": ("no", "PROBABLE", "Pase de aduana temporal (laissez-passer/passavant) en frontera; permiso internacional de conducir obligatorio", "Por confirmar (sin relatos con vehículo desde 2017)",
              "carnetdepassage.org no marca el CPD como obligatorio en Mali y señala que no hay club emisor AIT/FIA en el país. Los últimos relatos con vehículo propio (Oasis Overland 2016, Land Cruiser y Jeep 2017) no mencionan exigencia de carnet. El MAEC exige permiso internacional y seguro. Todo es teórico: FCDO (07-2026) pide no entrar ni salir por carretera."),
    "guinea-bisau": ("recomendable", "PROBABLE", "Passavant aduanero de 2 semanas (2.500 XOF, prorrogable en Bissau)", "0 XOF con CPD; 2.500 XOF passavant (dato de 2016)",
              "carnetdepassage.org no lista requisito ni club emisor; Horizons Unlimited lo pone en la tabla «se puede usar». Relatos con vehículo propio (WikiOverland y The Road Chose Me, 2016) pagaron passavant de 2 semanas por 2.500 XOF sin CPD; Overlandbirds (2019) salió por Buruntuma con CPD y personal confuso. Sin testimonio 2025-26: PROBABLE que el CPD del RACE se acepte pero que la aduana prefiera su passavant."),
    "sudan": ("recomendable", "PROBABLE", "Admisión temporal con fianza y fixer en Wadi Halfa (histórico, sin datos desde 2023)", "Incluido en el CPD del RACE si se lista Sudán; fianza local por confirmar",
              "carnetdepassage.org lista Sudán como país que acepta el CPD, con el Sudanese Automobile and Touring Club de Jartum como club garante (+249 183 403 402). Sahara Overland (enero 2026) marca el carnet como «puede seguir siendo necesario» y tacha todo el procedimiento de cruce por la guerra. No existe ningún cruce documentado con vehículo extranjero desde abril de 2023, así que el nivel real es PROBABLE y el país queda excluido."),
    "etiopia": ("recomendable", "SIN CONFIRMAR", "Depósito en aduana o despacho a través de agencia local", "Sin dato oficial; los relatos hablan de depósitos altos",
              "La AIT/FIA no tiene organización emisora de CPD en Etiopía, según carnetdepassage.org. El hilo «Entering Ethiopia with a car» de Overland Bound (agosto de 2023) afirma que el país dejó de aceptar carnet de passages y TIP a finales de 2022 y que el tránsito pasó a exigir depósitos elevados en aduana o la intervención de una agencia. Antes de ese cambio el procedimiento era el clásico: Goanna Tracks (marzo de 2018) y Bosman's Big Adventure describen el sellado del carnet en la aduana de Moyale con cotejo de todos los números de chasis y motor, y Dan Grec obtuvo en 2020 por Omorate un permiso de importación temporal de 60 días (Tread Magazine). No se ha localizado confirmación de la Ethiopian Customs Commission: llevar el CPD por si sigue sirviendo y contar con un despachante local."),
    "yibuti": ("no", "PROBABLE", "Permiso temporal de importación emitido en frontera (10 días documentados en Galafi)", "Sin coste documentado; tasas de frontera por confirmar",
              "carnetdepassage.org (AIT/FIA) confirma que no existe ninguna organización emisora de CPD en Yibuti, y el país no figura en la lista de países que exigen carnet de Horizons Unlimited (revisión de 2023). El testimonio operativo más claro es el de Dan Grec (The Road Chose Me): cruzó por Galafi sin carnet y la aduana, tras dudar y consultar con el superior, le emitió un Temporary Import Permit válido 10 días. Ese plazo es corto para un circuito tranquilo y no se ha localizado el procedimiento oficial de prórroga, que hay que preguntar en la aduana central de la capital. Llevar carnet no estorba si ya se tiene por otros países de la ruta, pero no parece imprescindible."),
    "argelia": ("no", "SIN CONFIRMAR", "Permiso de importación temporal (TIP) gratuito emitido en el puerto, 90 días prorrogables otros 90", "TIP gratuito; seguro argelino obligatorio aparte, unos 3.000 DZD por cuatro semanas",
              "El MAEC (7 de mayo de 2026) describe la importación temporal del vehículo como un régimen de 90 días prorrogables otros 90, con obligación de salir con el mismo vehículo, y no menciona el carnet de passages. Los relatos de overlanders en Horizons Unlimited describen la entrada con un TIP gratuito válido tres meses emitido en el puerto, sin CPD. No se ha podido abrir la web de la Direction Générale des Douanes argelina (douane.gov.dz), así que no hay confirmación oficial ni en un sentido ni en otro. Antes de embarcar conviene preguntarlo por escrito al consulado argelino y valorar llevar CPD del RACE como seguro, ya que el trámite se hace en España."),
    "burkina-faso": ("recomendable", "SIN CONFIRMAR", "Admisión temporal con laissez-passer de aduanas en el propio puesto fronterizo", "Laissez-passer 5.000 FCFA (dato de 2011, sin reconfirmar); el CPD se rige por la tarifa del RACE",
              "carnetdepassage.org confirma que no existe ninguna organización emisora de CPD reconocida por AIT/FIA dentro de Burkina Faso, de modo que el carnet debe emitirse en el país de matriculación: el RACE en el caso español. La misma fuente fija la validez del carnet en un año desde su emisión. No hemos encontrado ninguna fuente oficial burkinesa que declare el CPD obligatorio, y el único importe documentado del laissez-passer alternativo, 5.000 FCFA en aduana, procede de un relato de viaje de septiembre de 2011, así que la fiabilidad del dato es baja. Como el país está excluido por protocolo la cuestión es teórica; si se reactivara, habría que confirmarlo con la Direction Générale des Douanes antes de salir de España."),
    "niger": ("no", "SIN CONFIRMAR", "Laissez-passer local emitido en frontera (referencia histórica)", "por confirmar",
              "Sahara Overland recoge que históricamente los vehículos en Níger circulaban con un laissez-passer local y un seguro válido para toda la zona CFA, no con carnet de passages. No se ha podido abrir en esta sesión ninguna página de la aduana nigerina ni de carnetdepassage.org que confirme la práctica vigente en 2026, ni hay relatos de overlanders posteriores a 2022 que la documenten. Con el país excluido por protocolo y la escolta militar obligatoria fuera de Niamey, la cuestión es teórica: la entrada con vehículo propio no es una opción."),
    "chad": ("recomendable", "SIN CONFIRMAR", "Laissez-passer de aduana chadiana (admisión temporal) + autorisation de circuler", "Por confirmar",
              "Carnetdepassage.org indica que la AIT/FIA NO tiene organización emisora de CPD en Chad, pero no aclara si la aduana chadiana exige carnet a un vehículo extranjero en entrada temporal. Ninguna fuente abierta en esta sesión documenta un CPD obligatorio para Chad. Lo que sí está confirmado por FCDO, Canadá y Sahara Overland es que hace falta una autorización administrativa para circular fuera de Yamena y guía local obligatorio en el BET. Dado que el viaje pasa por países vecinos que sí lo exigen, llevar CPD es lo prudente, pero el dato de Chad hay que cerrarlo con la Direction Générale des Douanes."),
    "rca": ("recomendable", "SIN CONFIRMAR", "Admisión temporal con laissez-passer aduanero emitido en frontera", "Emisión y aval del CPD en España vía RACE; importe por confirmar",
              "La base de datos de la AIT/FIA en carnetdepassage.org indica que NO existe organización emisora de CPD en la República Centroafricana, y que los vehículos matriculados allí deben obtenerlo en otro país. Esa página dice quién lo emite, no si el país lo exige a la entrada, de modo que la obligatoriedad real queda sin confirmar. En la práctica regional, un CPD emitido por el RACE es la vía limpia para evitar depósito de fianza, y el laissez-passer aduanero de admisión temporal es la alternativa que se tramita en el propio puesto fronterizo. Confirmar con la Direction Générale des Douanes centroafricana antes de dar nada por hecho."),
    "sudan-del-sur": ("no", "PROBABLE", "Laissez-passer / admisión temporal en el puesto fronterizo, procedimiento no publicado", "Por confirmar",
              "AIT/FIA no tiene ninguna organización emisora de carnet de passages en Sudán del Sur, según carnetdepassage.org (ficha con actualización de 15 de noviembre de 2022), y no consta que el país exija CPD a los vehículos extranjeros. Eso no significa que la entrada del vehículo sea sencilla: ninguna fuente oficial abierta en esta sesión describe el trámite aduanero real en Nimule, ni el documento que se emite, ni las tasas. Al no haber tampoco un régimen de seguro reconocido (la Carta Verde no cubre el país y no se ha verificado la COMESA Yellow Card), el paso con vehículo propio queda sin documentar. Clasificado como PROBABLE y no CONFIRMADO por esa razón."),
    "eritrea": ("no", "SIN CONFIRMAR", "Ninguna aplicable: no hay paso terrestre abierto. Dentro del país se circula con coche de alquiler o con conductor, y el permiso interior va ligado a la matrícula.", "No aplica",
              "La web de AIT/FIA indica que no existe ninguna organización emisora de carnet de passages en Eritrea y que, para un vehículo matriculado allí, hay que pedirlo en un país vecino. Ninguna fuente abierta en esta sesión confirma si la aduana eritrea exigiría CPD a un vehículo extranjero, porque no hay cruces terrestres desde 2019. Los relatos de la ventana de 2018 en Horizons Unlimited describen justo lo contrario: ausencia total de formalidades aduaneras y ni siquiera sellos de entrada o salida. Mientras no haya cruces reales, la ficha lo deja en «no aplica, sin confirmar»."),
    "somalia": ("no", "SIN CONFIRMAR", "Ninguna vía documentada; no consta régimen de admisión temporal", "No aplica",
              "carnetdepassage.org indica textualmente que AIT/FIA no tiene ninguna organización emisora de CPD en Somalia y que los vehículos matriculados en el país deben obtener el carnet en otro donde sí exista emisor. No hay ninguna fuente que confirme que la aduana somalí o la somalilandesa acepten o exijan un CPD para un vehículo extranjero de turismo, ni que exista un procedimiento publicado de admisión temporal. Tampoco hay relatos de overlanders europeos recientes que lo hayan probado: los únicos cruces documentados en Tog Wajaale son de carga y de viajeros sin vehículo propio. Se deja como SIN CONFIRMAR y sin relevancia práctica, porque el país está excluido de la ruta."),
    "guinea-ecuatorial": ("no", "SIN CONFIRMAR", "Passavant o laissez-passer de aduana emitido en el puesto fronterizo (procedimiento no publicado)", "por confirmar",
              "Carnetdepassage.org confirma que AIT/FIA no tiene ninguna organización emisora de CPD en Guinea Ecuatorial y que los vehículos matriculados en el país deben obtenerlo en el extranjero. No se ha localizado ninguna norma aduanera ecuatoguineana que exija ni excluya el CPD para vehículos extranjeros, ni relato de overlander posterior a 2016 que lo documente. Como el país no es practicable por carretera —Bioko es una isla y las fronteras continentales están cerradas o son erráticas desde diciembre de 2025—, la cuestión es hoy teórica. Si alguna vez se planteara, habría que preguntar por escrito a la Dirección General de Aduanas a través de la Embajada de España en Malabo."),
    "cabo-verde": ("no", "SIN CONFIRMAR", "Importación temporal ante la Direção Geral das Alfândegas con depósito de derechos", "Depósito del 100–200 % del valor del vehículo (sin confirmar)",
              "La base de datos de carnetdepassage.org indica que AIT/FIA no tiene ningún organismo emisor de CPD en Cabo Verde, y no se ha localizado ninguna norma caboverdiana que lo exija o lo acepte. En la práctica la cuestión es teórica: no hay ro-ro ni ferry de vehículos desde el continente, así que el coche solo entra en contenedor y la aduana lo trata como importación. Residentes en el foro de Expat.com describen bill of lading, certificado de exportación y depósito de derechos del 100–200 % del valor, con posibilidad de exención por estancia temporal y recuperación parcial al reexportar. Sigue SIN CONFIRMAR en fuente oficial: la web de la Direção Geral das Alfândegas (Av. Amílcar Cabral, Praia · +238 261 7758 · helpdesk@dnre.gov.cv) solo publica franquicias de viajero y la exención del emigrante que regresa, no un régimen de admisión temporal para turistas."),
    "santo-tome": ("no", "SIN CONFIRMAR", "No aplica: no se puede llegar rodando. Un vehículo propio solo entra en contenedor, con despacho aduanero ordinario en el puerto de Ana Chaves.", "Sin dato",
              "carnetdepassage.org confirma que «AIT/FIA currently does not have any official CPD-issuing organization in the country»: no hay club emisor santotomense, y si alguien quisiera un CPD tendría que emitirlo en su país de origen (RACE en España). Ninguna fuente oficial del país describe un régimen de admisión temporal para vehículos de turistas, sencillamente porque nadie llega con el suyo. Para la ruta 2027 el dato es irrelevante: el país es insular y no hay ninguna travesía regular que admita vehículos."),
    "libia": ("obligatorio", "SIN CONFIRMAR", "Admisión temporal en aduana gestionada por la agencia libia patrocinadora (procedimiento sin documentar)", "Sin tarifa publicada; el CPD se emite en España a través del RACE con aval bancario",
              "El emisor nacional libio es el Automobile and Touring Club of Libya, +218 213403201, según carnetdepassage.org, pero esa misma ficha NO dice si el carnet es obligatorio para entrar y la web del club (atcl.ly) devuelve error 404. En el hilo de Horizons Unlimited sobre el cruce overland de Libia el carnet de passage figura entre la documentación exigida, junto con el visado. Ninguna fuente oficial libia abierta en esta sesión lo confirma ni lo desmiente. Dado que no hay entrada documentada con vehículo europeo desde 2012, el dato es histórico: antes de mover un coche habría que pedirlo por escrito al RACE y al propio club libio."),
}

NIVELES = {
    "obligatorio":  ("#C0392B", "Obligatorio", "Sin CPD no se entra."),
    "recomendable": ("#E08A1E", "Recomendable", "Hay alternativa, pero el CPD ahorra dinero o una discusión."),
    "no":           ("#3C9A5F", "No necesario", "Se resuelve en la frontera con un permiso temporal."),
}

FUERA_DE_RUTA = {"egipto", "libia", "tunez", "santo-tome", "cabo-verde", "guinea-ecuatorial", "somalia", "eritrea", "sudan-del-sur", "rca", "chad", "niger", "burkina-faso", "argelia", "yibuti", "etiopia", "sudan", "guinea-bisau", "mali", "madagascar"}

COSTE_CPD = [
    ("Emisión del carnet (10 o 25 hojas)", "~230 €"),
    ("Aval bancario, según valor GANVAM del vehículo", "mínimo 2.780 € inmovilizados"),
    ("Comisión bancaria del aval", "~100 €"),
    ("Validez", "1 año"),
]

FUENTES = [
    ("RACE", "https://www.race.es/servicios/carnet-de-passages", "Emisor exclusivo en España. Su lista de países "
     "en los que el CPD «es requerido» incluye, de toda África: Kenia, Sudáfrica y países de la Commonwealth, "
     "Libia y Senegal (Egipto no está). Precios, aval mínimo de 2.780 € y validez de un año, literales. "
     "No expide carnets a vehículos de matrícula extranjera."),
    ("Automobile Association of South Africa — «Travelling in Africa? You need to read this first» (2020)",
     "https://aa.co.za/travelling-in-africa-you-need-to-read-this-first-2/",
     "Emisor sudafricano: el CPD es «compulsory for Egypt and Kenya» y «recommended for travel to countries "
     "outside of the Southern African Customs Union». Escrito para conductores sudafricanos que salen de la SACU."),
    ("ADAC — Carnet de Passages (02-06-2026)", "https://www.adac.de/reise-freizeit/reiseplanung/fahrzeug-weltreise/carnet-de-passages-english/",
     "Emisor alemán: la Traveller Declaration de SARS «does not replace the Carnet»; para vehículos de fuera de la "
     "SACU el carnet «remains mandatory»; sin él, TIP con depósito y agente aduanero. Etiopía no acepta el carnet; "
     "Sudán, sin emisión."),
    ("SARS — Traveller Management System (notas de prensa de 19-05 y 01-06-2026 y FAQ)",
     "https://www.sars.gov.za/travellerdeclaration/declaration-of-foreign-registered-vehicles-used-by-travellers/",
     "Régimen sudafricano vigente desde el 1 de junio de 2026: TIP de seis meses, multientrada, sin tasa, sin "
     "exención SACU. No menciona el carnet."),
    ("Nigeria — comunicado oficial del Nigeria Customs Service (FMINO, 07-01-2026)",
     "https://fmino.gov.ng/nigeria-customs-service-commences-implementation-of-safe-passage-for-personal-vehicles-under-temporary-admission/",
     "Temporary Vehicle Admission Permit de 90 días (+30): lista el CPD entre los documentos a presentar en frontera."),
    ("KRA — avisos 774 y 1870", "https://www.kra.go.ke/news-center/public-notices/1870-foreign-motor-vehicle-notice",
     "El 774 (2017) exige carnet a vehículos de fuera de la EAC/COMESA; el 1870 admite Form C32 o carnet y da 14 días gratis."),
    ("Overlanding Association", "https://overlandingassociation.org/carnet-de-passage/",
     "«Travellers are reporting a carnet is not required if crossing via a land border; if you plan to ship in or "
     "out of any of the countries in the Customs Union we would strongly recommend obtaining a carnet.» Testimonio, no norma."),
    ("Horizons Unlimited", "https://www.horizonsunlimited.com/get-ready/paperwork/carnet-de-passages-en-douanes-list-of-countries",
     "Tiene DOS tablas: una de países donde «CAN use» el carnet (con la nota de que no significa que haya que "
     "usarlo) y otra, «to the best of our knowledge», de países donde el turista está «REQUIRED» a presentarlo, en la "
     "que aparecen Guinea, Gambia, Nigeria, Tanzania, Kenia y la SACU. Es la lista más copiada; está desactualizada "
     "frente a la práctica de los TIP, pero no es solo una lista de países que lo aceptan."),
    ("Rogue Wanderers — costes de visados y permisos de vehículo en África occidental sin carnet (17-03-2023)",
     "https://www.roguewanderers.com/blog/west-africa-visa-and-vehicle-permit-costs-traveling-wo-carnet",
     "Origen de casi todos los importes en USD de Gambia a Angola (795 USD en total, 490 de ellos en Ghana)."),
    ("Pistenkuh — Reise-Info Senegal y relato de Angola",
     "https://pistenkuh.de/reisen/afrika/mali-guinea/reise-info-senegal/",
     "Senegal: passavant de 48-72 h y «mindestens 250 Euro» para vehículos de más de 8 años, también en Diama. "
     "Angola (2022): carnet sellado mal al salir hacia Namibia."),
    ("Road Fund Administration de Namibia — tarifas desde el 01-08-2026", "https://rfanam.com.na/fees-tariffs/",
     "Cross-Border Charge: N$534 por entrada para turismos y pick-ups; N$340 motos y caravanas."),
    ("Tracks4Africa", "https://tracks4africa.co.za/", "Fuente de campo para el bloque austral y oriental (Uganda no reconoce el carnet)."),
]

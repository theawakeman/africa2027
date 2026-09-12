# -*- coding: utf-8 -*-
"""Carnet de Passages en Douane: situación país por país.

Clasificación para un vehículo particular matriculado en España que entra y
sale POR TIERRA. El régimen cambia por completo si el vehículo llega o sale
en barco: ahí el CPD pasa a ser muy recomendable en casi todas partes.

Niveles:
  obligatorio  — sin CPD no se entra. Rojo.
  recomendable — hay alternativa, pero el CPD evita un coste o una pelea. Naranja.
  no           — no hace falta; se resuelve en frontera. Verde.

Investigación de septiembre de 2026. Fuentes al final de cada ficha.
"""

# slug: (nivel, confianza, alternativa, coste, nota)
CPD = {
    # ---------------------------------------------------------- ruta de bajada
    "marruecos": ("no", "CONFIRMADO", "Declaración D16ter (admisión temporal)", "Gratis · 180 días",
                  "Se rellena en línea antes de embarcar. No aparece en ninguna lista de países que exijan CPD."),
    "sahara-occidental": ("no", "PROBABLE", "Cubierto por el D16ter marroquí", "—",
                          "No hay aduana propia: se entra con el trámite hecho en Tánger o Tarfaya."),
    "mauritania": ("no", "CONFIRMADO", "Passavant / laissez-passer en frontera", "~8-10 €",
                   "Guerguerat. No es miembro de la CEDEAO, así que la Carte Brune no sirve aquí."),
    "senegal": ("recomendable", "CONFIRMADO", "Passavant (10 días + 2 prórrogas de 15)",
                "~4 € si el vehículo es «joven» · ~250 € si supera el límite de edad",
                "El único país de la ruta que aparece en la lista del RACE. El problema no es el CPD "
                "en sí: es el límite de edad del vehículo (5 años hasta 2016, 8 desde 2016, 10 por "
                "decreto de octubre de 2025). Es norma de importación definitiva, pero la aduana de "
                "Rosso la aplica igual. Dos alternativas sin CPD: entrar por Diama en vez de Rosso, o "
                "entrar desde Mali por Kidira, donde el passavant cuesta 4 € y el trámite es trivial."),
    "gambia": ("no", "PROBABLE", "Laissez-passer / TIP en frontera", "~11 USD", ""),
    "guinea": ("no", "PROBABLE", "Laissez-passer en frontera", "0-5.000 FCFA (~8 €)",
               "Te lo retiran al salir. Horizons Unlimited la lista como «carnet required», pero es "
               "una lista de países que lo ACEPTAN, no que lo exijan."),
    "sierra-leona": ("no", "PROBABLE", "TIP en frontera", "~17 USD", ""),
    "liberia": ("no", "PROBABLE", "Laissez-passer", "~90 USD",
                "Una sola fuente primaria (2023), sin contrastar."),
    "costa-de-marfil": ("no", "PROBABLE", "Admisión temporal en frontera", "~82 USD (2023)",
                        "El CPD se acepta pero no se exige. Fronteras reabiertas en febrero de 2023: "
                        "los relatos anteriores hablan de un laissez-passer de ministerio que ya no aplica."),
    "ghana": ("recomendable", "CONFIRMADO", "Permiso de tránsito con localizador GPS",
              "~490 USD con tracker · ~12 € si lo dan como excepción",
              "El permiso más caro de África occidental sin CPD: 490 de los 795 USD que un overlander "
              "documentó en toda la región. Obliga a ruta directa y seguimiento. Lo que sí funcionó: "
              "conseguir una carta del cónsul de Ghana en Benín antes de presentarse en Aflao."),
    "togo": ("no", "PROBABLE", "TIP (1 mes)", "~11 USD", ""),
    "benin": ("no", "CONFIRMADO", "Laissez-passer de aduanas (digital desde septiembre de 2026)", "~16 USD", ""),
    "nigeria": ("no", "CONFIRMADO", "Temporary Vehicle Admission Permit («Safe Passage»), 90 + 30 días",
                "Gratuito en 2023 · importe de 2026 sin publicar",
                "CAMBIO IMPORTANTE: el 7 de enero de 2026 el Nigeria Customs Service lanzó un permiso "
                "electrónico de 90 días que menciona el CPD solo «si procede». Su fama de exigirlo sin "
                "excepción viene de listas anteriores a esa fecha."),
    "camerun": ("no", "PROBABLE", "Passavant (corto en frontera, definitivo tierra adentro)", "~15 USD", ""),
    "congo": ("no", "PROBABLE", "TIP / laissez-passer", "~16 USD", ""),
    "rd-congo": ("no", "PROBABLE", "TIP", "~15 USD",
                 "El problema del tramo no es aduanero: el ferry de pasajeros Brazzaville-Kinshasa no "
                 "lleva vehículos y el servicio especializado parte de ~4.000 €. La ruta habitual evita "
                 "Kinshasa por Pointe-Noire → Cabinda."),
    "angola": ("no", "CONFIRMADO", "TIP en frontera", "~10 USD",
               "Aquí el CPD puede ESTORBAR. El ADAC, que los emite, avisa: «a veces surgen problemas al "
               "entrar en Angola y Mozambique porque el carnet no es necesario». Un carnet mal sellado "
               "es justo lo que hace perder el aval."),
    # ------------------------------------------------------------------ bucle
    "zambia": ("no", "CONFIRMADO", "Sin TIP: paquete de cuatro tasas", "~80-120 USD",
               "Carbon Emission Surtax (~30 USD), Road Toll de la RDA (~20 USD), Council Levy (~30 ZMW, "
               "se paga kilómetros después de la frontera) y seguro de responsabilidad civil. La fianza "
               "de ~250 USD que circula por los foros es de tránsito comercial: no aplica al turista."),
    "tanzania": ("no", "CONFIRMADO", "TIP en frontera + road tax", "25 USD/mes (+5 USD de tasa menor)",
                 "Aparece como obligatorio en listas antiguas. No lo es."),
    "kenia": ("recomendable", "CONFIRMADO", "Form C32 (gratis, 14 días) + Foreign Vehicle Permit",
              "C32 gratis · FVP 21-101 USD según cilindrada y plazo",
              "El único de la ruta que figura en la lista del RACE, y la propia KRA se contradice: el "
              "aviso 774 (2017) exige CPD a vehículos de fuera de la EAC/COMESA, y el 1870, posterior, "
              "abre la vía del Form C32 sin carnet. Pasó de obligatorio a recomendable. Mitigación sin "
              "CPD: cuenta eCitizen hecha antes de llegar, correo a la KRA guardado por escrito y el "
              "aviso 1870 impreso. Tarifas del FVP: <2000cc 21 USD/mes o 51 USD/3 meses; >2000cc 41 y 101."),
    "uganda": ("no", "CONFIRMADO", "Temporary Road Licence de la URA", "~13-18 €/mes",
               "Uganda NO acepta el carnet. Tracks4Africa, 2023: «Uganda does not accept or recognise a "
               "Carnet». Llevarlo aquí es aval inmovilizado a cambio de nada."),
    "ruanda": ("no", "PROBABLE", "TIP de 15 días + seguro", "~11 €",
               "Ojo al calendario, no al carnet: 15 días sin prórroga posible en frontera."),
    "malaui": ("no", "CONFIRMADO", "TIP (Form 12) + Road Access Fee + seguro", "TIP barato + 20 USD de RAF",
               "No pagar el Road Access Fee son 500 USD de multa valorada en frontera."),
    "mozambique": ("no", "CONFIRMADO", "TIP obligatorio + seguro local obligatorio", "~15-30 €",
                   "Mozambique NO acepta el carnet, y tampoco la Yellow Card COMESA. Dos triángulos, "
                   "dos chalecos y extintor de 1 kg. Verificar el sello del TIP antes de salir del puesto."),
    "zimbabue": ("no", "CONFIRMADO", "TIP de ZIMRA (hasta 3 meses) + carbon tax + seguro + peajes", "~45-70 USD", ""),
    "botsuana": ("no", "CONFIRMADO", "Temporary Import Permit de BURS + Road Safety levy", "~11 €", ""),
    "namibia": ("no", "CONFIRMADO", "Cross-Border Charge del RFA + TIP de NamRA", "N$534 (~27 €)", ""),
    "sudafrica": ("no", "CONFIRMADO", "TIP de 6 meses multientrada, gratuito, vía SARS Traveller Management System",
                  "Gratis",
                  "CAMBIO IMPORTANTE para 2027: desde el 1 de junio de 2026 hay que declarar el vehículo "
                  "en línea en el TMS de SARS ANTES de llegar a la frontera. A cambio, el TIP es de seis "
                  "meses, multientrada y gratuito, y cubre las escapadas a Lesoto y Esuatini. SARS es "
                  "explícito en que no hay exención por ser SACU."),
    "lesoto": ("no", "PROBABLE", "Permiso en frontera + peaje por peso + seguro", "~2-5 €", ""),
    "esuatini": ("no", "PROBABLE", "TIP en frontera + road tax", "~3-6 €", ""),
    "gabon": ("no", "PROBABLE", "TIP (se tramita en Bitam, no en la frontera)", "Gratis", ""),
    "madagascar": ("no", "CONFIRMADO", "No aplica", "—", "No se lleva el vehículo: el tramo es en avión."),
    # ------------------------------------------------- fuera de la ruta, de referencia
    "egipto": ("obligatorio", "CONFIRMADO", "No hay alternativa", "Aval elevado + matrícula temporal",
               "FUERA DE LA RUTA. Es, con Libia, el único sitio de África donde el CPD es realmente "
               "obligatorio. Se incluye aquí como referencia, porque es lo que explica que el carnet "
               "tenga la fama que tiene."),
    "libia": ("obligatorio", "CONFIRMADO", "No hay alternativa", "—",
              "FUERA DE LA RUTA. Figura en la lista del RACE."),
}

NIVELES = {
    "obligatorio":  ("#C0392B", "Obligatorio", "Sin CPD no se entra."),
    "recomendable": ("#E08A1E", "Recomendable", "Hay alternativa, pero el CPD ahorra dinero o una discusión."),
    "no":           ("#3C9A5F", "No necesario", "Se resuelve en la frontera con un permiso temporal."),
}

FUERA_DE_RUTA = {"egipto", "libia"}

COSTE_CPD = [
    ("Emisión del carnet (10 o 25 hojas)", "~230 €"),
    ("Aval bancario, según valor GANVAM del vehículo", "mínimo 2.780 € inmovilizados"),
    ("Comisión bancaria del aval", "~100 €"),
    ("Validez", "1 año"),
]

FUENTES = [
    ("RACE", "https://www.race.es/servicios/carnet-de-passages", "Emisor exclusivo en España. Su lista de países que exigen CPD "
     "incluye, de toda África: Kenia, Sudáfrica y países de la Commonwealth, Libia y Senegal."),
    ("Automobile Association of South Africa", "https://aa.co.za/travel/carnet-de-passage-en-douane/",
     "Emisor sudafricano: el CPD es «obligatorio para Egipto y Kenia y recomendable para viajar a "
     "países fuera de la unión aduanera de África austral»."),
    ("Overlanding Association", "https://overlandingassociation.org/carnet-de-passage/",
     "«No hace falta carnet si se cruza por una frontera terrestre; si se piensa embarcar el vehículo "
     "en alguno de los países de la unión aduanera, lo recomendamos encarecidamente.»"),
    ("Horizons Unlimited", "https://www.horizonsunlimited.com/get-ready/paperwork/carnet-de-passages-en-douanes-list-of-countries",
     "La lista más copiada y peor leída. Lleva escrito: «esto NO significa que DEBAS usar carnet en "
     "estos países, solo que PUEDES si quieres». Es una lista de países que lo aceptan."),
    ("SARS — Traveller Management System", "https://www.sars.gov.za/",
     "Régimen sudafricano vigente desde el 1 de junio de 2026."),
    ("Nigeria Customs Service", "https://customs.gov.ng/",
     "Permiso electrónico «Safe Passage», 7 de enero de 2026."),
    ("Tracks4Africa", "https://tracks4africa.co.za/", "Fuente de campo para el bloque austral y oriental."),
]

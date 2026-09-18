# -*- coding: utf-8 -*-
"""Visados para pasaporte ordinario español y entrada turística.

La clasificación está pensada para la ruta overland: cuando un eVisa solo se
entrega o valida en un aeropuerto, el país figura como ``presencial``. La hoja
de Drive es el inventario de partida; la modalidad publicada aquí se ha
contrastado con MAEC y, cuando existe, con el portal oficial del país.

Auditoría: 15-09-2026. Revalidar 30-60 días antes de cada entrada y 72 horas
antes de llegar a la frontera.
"""

AUDIT_DATE = "15 de septiembre de 2026"
SOURCE_SHEET = "https://docs.google.com/spreadsheets/d/1lFy2f8XUxwQuT9Qhdmx8vgpYBaM5o4AqxgKs8jIAplo/edit?gid=227464872#gid=227464872"

NIVELES = {
    "sin": ("#2E7D32", "Sin visado", "Turismo corto con pasaporte español; pueden existir formularios de entrada."),
    "electronico": ("#2B6CB0", "Electrónico previo", "eVisa, eTA o permiso que debe estar aprobado antes de la frontera."),
    "presencial": ("#D97B29", "Presencial previo", "El pasaporte debe llevar el visado emitido por embajada o consulado."),
    "frontera": ("#9A6410", "En frontera", "Se obtiene al llegar; llevar efectivo y documentación de apoyo."),
    "no_viable": ("#B43A3A", "No viable ahora", "La frontera o el viaje no son utilizables para esta ruta, aunque exista un visado."),
}


def _maec(country):
    from urllib.parse import quote_plus
    return ("https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/"
            "Detalle-recomendaciones-de-viaje.aspx?trc=" + quote_plus(country))


def visa(nivel, resumen, accion, *, pasos="", entradas="", coste="", alerta="",
         oficial="", maec="", ruta="principal"):
    return {
        "nivel": nivel,
        "resumen": resumen,
        "accion": accion,
        "pasos": pasos,
        "entradas": entradas,
        "coste": coste,
        "alerta": alerta,
        "oficial": oficial,
        "maec": maec,
        "ruta": ruta,
    }


VISADOS = {
    # Corredor occidental, bajada y regreso.
    "marruecos": visa(
        "sin", "Exención turística de hasta 90 días.",
        "Pasaporte en vigor; no se admite el DNI.", pasos="12 ene · 20 jul", entradas="2 entradas",
        alerta="El pasaporte debe cubrir toda la estancia y MAEC pide más de 6 meses de validez.",
        maec=_maec("Marruecos")),
    "sahara-occidental": visa(
        "sin", "El corredor costero está bajo el mismo régimen de entrada de Marruecos.",
        "Conservar el sello marroquí y no abandonar el corredor habilitado.", pasos="tránsito ida y vuelta",
        entradas="incluido en Marruecos", alerta="No es un Estado separado a efectos del control migratorio de esta ruta.",
        maec=_maec("Marruecos")),
    "mauritania": visa(
        "electronico", "Visado obligatorio con solicitud electrónica previa.",
        "Solicitar el código en ANRPTS; biometría y pago al llegar.", pasos="18 ene · 15 jul", entradas="2 visados",
        coste="Referencia: 55 € por 30 días y entrada única.",
        alerta="El sistema oficial enumera PK55, Rosso y Diama entre los puestos que completan el trámite.",
        oficial="https://anrpts.gov.mr/visa/requestvisa", maec=_maec("Mauritania")),
    "senegal": visa(
        "sin", "Exención para estancias inferiores a 90 días.",
        "Pasaporte con validez superior a 6 meses.", pasos="27 ene · 3 jul · 8 jul", entradas="3 entradas",
        alerta="No confundir el visado personal con el passavant o CPD del vehículo.", maec=_maec("Senegal")),
    "gambia": visa(
        "sin", "No se exige visado a españoles que cruzan por tierra desde Senegal.",
        "Llevar impresa la recomendación MAEC y efectivo por si cambia la práctica.", pasos="4 jul", entradas="1 entrada",
        alerta="MAEC advierte que la gestión puede cambiar sin aviso; la exención aérea tiene además tasas de seguridad.",
        maec=_maec("Gambia")),
    "guinea": visa(
        "electronico", "Visado obligatorio; solicitud en la plataforma de la Policía de Fronteras.",
        "Tramitar online y confirmar en paralelo con la Embajada de Guinea en Madrid.", pasos="2 feb · 28 jun",
        entradas="2 entradas", alerta="La propia recomendación española pide coordinar la solicitud con la Embajada; no viajar solo con el justificante.",
        oficial="https://www.paf.gov.gn/visa", maec=_maec("Guinea")),
    "guinea-bisau": visa(
        "no_viable", "Visado obligatorio para españoles; país excluido por protocolo tras el golpe de noviembre de 2025.",
        "Si se reabriera el desvío: visado en el consulado de Ziguinchor (25.000 XOF/30 días, en el día) o en la Embajada de Madrid; nunca contar con el de frontera.",
        ruta="excluido", entradas="Simple (doble entrada citada en 2016); 30/60/90 días", coste="25.000 XOF (~40 €) 30 días en Ziguinchor (2025); Madrid por confirmar",
        alerta="eVisa paralizada y visado en frontera terrestre «ni claro ni estable» (MAEC, 19-3-2026).",
        oficial="", maec=_maec("Guinea Bissau")),
    "sierra-leona": visa(
        "presencial", "Para entrar por tierra hace falta visado consular previo.",
        "Consultar el Consulado Honorario en Las Palmas y llevar el visado en el pasaporte.", entradas="alternativa de subida",
        ruta="alternativa", alerta="El eVisa publicado por MAEC es una autorización para expedir el visado al llegar al aeropuerto de Lungi, no en la frontera terrestre.",
        oficial="https://www.evisa.sl/", maec=_maec("Sierra Leona")),
    "liberia": visa(
        "presencial", "Visado obligatorio; no se obtiene al llegar.",
        "Tramitarlo en el Consulado Honorario de Liberia en Madrid.", entradas="alternativa terrestre", ruta="alternativa",
        coste="MAEC publica 100 € una entrada y 200 € múltiple.",
        alerta="El procedimiento de llegada/eVisa no resuelve una entrada por carretera.", maec=_maec("Liberia")),
    "costa-de-marfil": visa(
        "presencial", "Visado previo estampado para cualquier entrada terrestre.",
        "Pedir entrada múltiple en Madrid o confirmar emisión en Conakry y Accra.", pasos="9 feb · 23 jun", entradas="2 entradas",
        coste="Referencia MAEC: 50 € más gastos para el visado presencial corto.",
        alerta="El eVisa SNEDAI se expide exclusivamente en el aeropuerto de Abiyán y no sirve en carretera.",
        oficial="https://snedai.com/e-visa/", maec=_maec("Costa de Marfil")),
    "ghana": visa(
        "electronico", "eVisa obligatorio para pasaporte español.",
        "Solicitarlo online y comprobar que cubre las dos entradas previstas.", pasos="14 feb · 19 jun", entradas="2 entradas",
        coste="260 USD según MAEC; verificar la tarifa al solicitar.",
        alerta="El portal oficial declara el eVisa válido en aeropuertos y fronteras terrestres; el de una entrada caduca 90 días después de emitirse.",
        oficial="https://evisa.immigration.gov.gh/", maec=_maec("Ghana")),
    "togo": visa(
        "electronico", "eVisa obligatorio y aprobado antes de llegar.",
        "Solicitarlo en Togo Voyage al menos 5 días antes; prever dos entradas.", pasos="17 feb · 18 jun", entradas="2 entradas",
        alerta="El portal oficial dice que sin autorización aprobada se rechaza la entrada; confirmar que ambos pasos terrestres están ya digitalizados.",
        oficial="https://voyage.gouv.tg/", maec=_maec("Togo")),
    "benin": visa(
        "electronico", "Benín solo concede visados por vía electrónica.",
        "Solicitar dos eVisas o uno que cubra ambas entradas.", pasos="18 feb · 16 jun", entradas="2 entradas",
        alerta="La validez empieza en la fecha de emisión; no pedirlo demasiado pronto.",
        oficial="https://evisa.bj/", maec=_maec("Benín")),
    "nigeria": visa(
        "electronico", "Visado turístico electrónico disponible; 30 días y una entrada.",
        "Tramitar cada eVisa, imprimir la aprobación y completar landing/exit card.", pasos="19 feb · 11 jun", entradas="2 eVisas",
        coste="MAEC sitúa una entrada alrededor de 250 €.",
        alerta="La web oficial habla de presentarlo en el «port of entry», pero no enumera Seme/Ekok: pedir confirmación escrita para ambos pasos terrestres.",
        oficial="https://immigration.gov.ng/info-center/tourism-visa-f5a/", maec=_maec("Nigeria")),

    # África central y enlace a Angola.
    "camerun": visa(
        "electronico", "Visado obligatorio; solicitud exclusivamente online en EvisaCam.",
        "Obtener la preautorización y el QR antes de viajar; comprobar la validez para cada paso.", pasos="24 feb · 7 jun", entradas="2 entradas",
        coste="Referencia de la hoja: 153 €; comprobar en la plataforma.",
        alerta="La mera solicitud no basta. El QR permite la expedición en frontera, pero hay que confirmar por escrito los puestos exactos de la ruta.",
        oficial="https://www.evisacam.cm/ords/dl_portal/r/public_portal/home", maec=_maec("Camerún")),
    "guinea-ecuatorial": visa(
        "no_viable", "Visado obligatorio y fronteras terrestres continentales cerradas por tiempo indeterminado.",
        "No incorporarlo a la ruta; solo reevaluar con reapertura oficial y visado emitido en España.", ruta="fuera",
        alerta="MAEC fecha el cierre terrestre desde el 15 de diciembre de 2025; la vía aérea no sirve al viaje con vehículos.",
        maec=_maec("Guinea Ecuatorial")),
    "gabon": visa(
        "presencial", "Para entrar por carretera se necesita visado consular previo.",
        "Tramitarlo en la Embajada de Gabón antes de salir de Europa.", entradas="solo si se reactiva la alternativa", ruta="alternativa",
        alerta="El eVisa se materializa exclusivamente en el aeropuerto de Libreville; no es válido para la frontera terrestre.",
        oficial="https://evisa.dgdi.ga/", maec=_maec("Gabón")),
    "congo": visa(
        "presencial", "Visado obligatorio antes del viaje.",
        "Tramitar en la Embajada de la República del Congo en París y pedir modalidad que cubra dos pasos.", pasos="28 feb · 2 jun",
        entradas="2 entradas", alerta="No hay embajada congoleña en España; no confundir Congo-Brazzaville con RD Congo.",
        oficial="https://girafe.ambacongofr.org/", maec=_maec("República del Congo")),
    "rd-congo": visa(
        "presencial", "Visado obligatorio expedido en el país de residencia.",
        "Solicitar en la Embajada de la RDC en Madrid una modalidad que cubra los dos tránsitos de Kongo Central.", pasos="6 mar · 1 jun",
        entradas="2 entradas", alerta="No puede obtenerse en Brazzaville; llevar itinerario terrestre Cabinda–Muanda–Boma–Matadi–Lufu y documentación de salida.",
        oficial="https://ambardcmadrid.com/", maec=_maec("República Democrática del Congo")),
    "angola": visa(
        "sin", "Exención turística: 30 días por entrada y 90 días por año.",
        "Llevar prueba de continuación y controlar todos los sellos de Cabinda y Angola continental.", pasos="7 mar · 20 may",
        entradas="4 controles angoleños", alerta="La exención es solo turística; la suma anual no puede superar 90 días.",
        maec=_maec("Angola")),

    # Bucle sur y este.
    "zambia": visa(
        "sin", "Los españoles no necesitan visado.",
        "Pasaporte con al menos 6 meses y 3 páginas libres.", pasos="17 mar", entradas="1 entrada",
        alerta="El KAZA Univisa solo interesa si se necesita cubrir también Zimbabue; no es requisito para Zambia.", maec=_maec("Zambia")),
    "malaui": visa(
        "electronico", "Visado obligatorio; eVisa oficial disponible.",
        "Usar el asistente de elegibilidad y obtener el eVisa antes de llegar.", pasos="1 abr", entradas="alternativa",
        ruta="alternativa", coste="Referencia de la hoja: 50 USD; verificar.",
        alerta="Desde febrero de 2026 algunas nacionalidades obtienen visado al llegar, pero la lista de categorías debe comprobarse en el asistente; el eVisa evita esa incertidumbre.",
        oficial="https://www.evisa.gov.mw/", maec=_maec("Malaui")),
    "tanzania": visa(
        "electronico", "Visado obligatorio; para nuestra entrada terrestre conviene eVisa previo.",
        "Solicitar online antes de la frontera y prever la posible segunda entrada desde Kenia.", pasos="6 abr", entradas="2 entradas si se vuelve desde Kenia",
        coste="Referencia habitual: 50 USD; verificar al solicitar.",
        alerta="MAEC solo enumera visado a la llegada en aeropuertos y puertos; no lo ofrece como solución general en frontera terrestre.",
        oficial="https://visa.immigration.go.tz/", maec=_maec("Tanzania")),
    "kenia": visa(
        "electronico", "No exige visado, pero sí una eTA antes de viajar.",
        "Solicitar la eTA oficial con margen y llevarla impresa o descargada.", entradas="1 entrada",
        alerta="La eTA es de una sola entrada y expira al salir; si cambia el bucle y se reentra, hace falta otra.",
        oficial="https://www.etakenya.go.ke/", maec=_maec("Kenia")),
    "uganda": visa(
        "electronico", "Visado obligatorio y exclusivamente electrónico.",
        "Obtener el eVisa y llevar impresa la aprobación antes de la frontera.", entradas="alternativa Grandes Lagos", ruta="alternativa",
        alerta="Uganda ya no expide visados en frontera.",
        oficial="https://visas.immigration.go.ug/", maec=_maec("Uganda")),
    "ruanda": visa(
        "frontera", "Visado turístico disponible online o al llegar, también en frontera terrestre.",
        "Puede tramitarse online; si se hace al llegar, llevar efectivo.", entradas="alternativa Grandes Lagos", ruta="alternativa",
        coste="50 USD entrada única; 70 USD múltiple según MAEC.",
        alerta="Las tarjetas no se aceptan en todas las fronteras terrestres.",
        oficial="https://irembo.gov.rw/rolportal/en/web/dgie/newhome", maec=_maec("Ruanda")),
    "mozambique": visa(
        "electronico", "Exento de visado hasta 30 días, pero con permiso electrónico previo obligatorio.",
        "Registrar la entrada en el portal oficial al menos 5 días antes.", pasos="21 abr", entradas="1 entrada",
        alerta="No tratar la exención como entrada sin trámite: MAEC exige la solicitud digital a todos los viajeros españoles.",
        oficial="https://evisa.gov.mz/", maec=_maec("Mozambique")),
    "zimbabue": visa(
        "frontera", "Visado obligatorio disponible en frontera terrestre.",
        "Pagar al llegar y comprobar duración y número de entradas antes de alejarse del puesto.", pasos="1 may", entradas="1 entrada",
        coste="30 USD una entrada; 45 USD dos entradas según MAEC.",
        alerta="El visado múltiple no se expide en frontera; el KAZA puede convenir si se cruza también Zambia.", maec=_maec("Zimbabue")),
    "botsuana": visa(
        "sin", "Exención turística para estancias inferiores a 90 días.",
        "Pasaporte con validez mínima de 6 meses desde la salida prevista.", pasos="10 may", entradas="1 entrada",
        alerta="Comprobar el sello y la duración concedida antes de abandonar el puesto.", maec=_maec("Botsuana")),
    "sudafrica": visa(
        "sin", "Exención turística de hasta 90 días.",
        "Pasaporte con 2 páginas libres y declaración aduanera electrónica de viajero.", pasos="20 may", entradas="según ramales",
        alerta="Desde el 1 de julio de 2026 la declaración aduanera electrónica se exige también por tierra; no es un visado.",
        oficial="https://www.sars.gov.za/traveller-declaration/", maec=_maec("Sudáfrica")),
    "esuatini": visa(
        "sin", "Los ciudadanos de la UE no necesitan visado.",
        "Pasaporte con al menos 3 meses de validez posterior a la entrada y hojas libres.", entradas="ramal opcional", ruta="alternativa",
        alerta="Los 13 puestos terrestres tienen horarios distintos; comprobar el elegido.",
        oficial="https://www.gov.sz/index.php/component/content/article/309-entry-requirements?Itemid=630&catid=61",
        maec=_maec("Esuatini")),
    "lesoto": visa(
        "sin", "Exención para turismo de hasta 14 días.",
        "Pasaporte con 2 páginas libres y validez mínima de 30 días tras la salida.", entradas="ramal opcional", ruta="alternativa",
        alerta="La exención es de solo 14 días, no 90.", maec=_maec("Lesoto")),
    "namibia": visa(
        "electronico", "Desde abril de 2025 España necesita visado; puede tramitarse online o al llegar.",
        "Solicitar el eVisa antes de la entrada para no depender del servicio del puesto.", pasos="5 may", entradas="1 entrada",
        coste="1.600 NAD (unos 78 €) según MAEC.",
        alerta="Oshikango y Noordoewer aceptan eVisa y visado presencial al llegar; otros pasos solo admiten eVisa o aún no están operativos.",
        oficial="https://eservices.mhaiss.gov.na/", maec=_maec("Namibia")),

    # Países de la hoja que ya no forman parte de la ruta confirmada.
    "etiopia": visa(
        "electronico", "eVisa obligatorio y previo para españoles, de entrada única y pensado para el aeropuerto de Bole.",
        "Tramitar el eVisa en evisa.gov.et con al menos una semana de margen y llevarlo impreso junto al certificado de fiebre amarilla.",
        ruta="fuera", entradas="Entrada única; para varias entradas, varios visados", coste="82 USD (30 días) / 102 USD (90 días), a reconfirmar en la web oficial",
        alerta="El MAEC afirma que NO se conceden visados en fronteras terrestres: llegar a Moyale sin visado emitido es arriesgarse al rechazo.",
        oficial="https://www.evisa.gov.et/", maec=_maec("Etiopía")),
    "sudan": visa(
        "no_viable", "Visado obligatorio previo en la Embajada de Sudán en Madrid (5 semanas–2 meses), pero el país está excluido por guerra y el MAEC desaconseja viajar bajo cualquier circunstancia.",
        "Ninguna: no se tramita; si algún día se reconsidera, pedirlo en Madrid (Av. Miraflores 63) con 2 meses de margen y registrarse en Interior en 3 días.",
        ruta="excluido", entradas="Solo aeropuertos de Port Sudán y Jartum; pasos terrestres cerrados a extranjeros (MAEC)", coste="Por confirmar (150 USD en Asuán en 2023, relato de viajero)",
        alerta="Sello israelí en el pasaporte = entrada denegada; permiso de viaje para salir del estado del Mar Rojo o de Jartum.",
        oficial="", maec=_maec("Sudán")),
    "egipto": visa(
        "frontera", "Los españoles necesitan visado y lo obtienen a la llegada en aeropuerto, puerto o paso terrestre por 30 USD.",
        "Llevar 30 USD en efectivo en billetes nuevos, o sacar la eVisa en visa2egypt.gov.eg antes de salir.",
        ruta="fuera", entradas="30 días, una entrada", coste="30 USD (25 USD la exención limitada al Sinaí)",
        alerta="Pasaporte con seis meses de validez y hay que conservar el sello de entrada: lo piden al salir.",
        oficial="https://visa2egypt.gov.eg", maec=_maec("Egipto")),
    "somalia": visa(
        "no_viable", "Visado obligatorio, disponible también al llegar, pero el viaje no es viable.",
        "Excluir por completo de la ruta.", ruta="fuera",
        alerta="MAEC desaconseja el viaje bajo cualquier circunstancia y advierte de amenaza terrorista y secuestro muy altas.",
        maec=_maec("Somalia")),
    "yibuti": visa(
        "electronico", "Visado obligatorio para españoles: eVisa oficial en evisa.gouv.dj, o visado en la embajada de Yibuti en París o en Adís Abeba.",
        "Solicitar el eVisa con semanas de antelación y, si se entra por tierra con vehículo, pedir además visado físico en el pasaporte en la embajada de Yibuti en Adís Abeba.",
        ruta="fuera", entradas="Una entrada, hasta 90 días", coste="12 USD tránsito (1-14 días) y 23 USD estancia corta (15-90 días); el MAEC cifra el coste en 50-80 €",
        alerta="La validez del eVisa en las fronteras terrestres NO está confirmada: hay fuentes contradictorias y una agencia local niega que exista visado a la llegada en los pasos con Etiopía.",
        oficial="https://www.evisa.gouv.dj/", maec=_maec("Yibuti")),
    "madagascar": visa(
        "frontera", "Españoles: exención 15 días con tasa o visado a la llegada/eVisa de 30, 60 o 90 días.",
        "Pagar en Ivato (efectivo EUR/USD o tarjeta) o tramitar eVisa 1–2 semanas antes.",
        ruta="vuelo", entradas="Solo aeropuerto; sin frontera terrestre", coste="15 d 10–30 € · 30 d 35 € · 60 d 40 € · 90 d 50 €",
        alerta="Tasa de 15 días subió a 30 € en feb-2026 según prensa; MAEC (may-2026) aún dice 10 €.",
        oficial="https://evisamada-mg.com", maec=_maec("Madagascar")),
    "tunez": visa(
        "sin", "Exención turística de hasta 90 días para pasaporte español.",
        "Pasaporte con 3 meses de validez (llevar 6); el DNI no sirve. Por vía marítima pueden pedir dirección en Túnez y billete de vuelta.",
        ruta="fuera", entradas="solo en un viaje aparte en ferry",
        alerta="Fuera de la ruta 2027: sin conexión terrestre (Marruecos–Argelia cerrada desde 1994; Libia inviable). El vehículo se anota en el pasaporte del conductor.",
        maec=_maec("Túnez")),
    "mali": visa(
        "no_viable", "Visado obligatorio y previo en la Embajada de Mali en Madrid (presencia personal); Mali no expide visados en frontera, y el país está vetado por el MAEC.",
        "Ninguna: país excluido; si se reabriera, pedir cita en Madrid con formulario, fotos, carta de invitación y certificado de fiebre amarilla.",
        ruta="excluido", entradas="Visado de 30 días, entrada única (según relatos); por confirmar", coste="Por confirmar en Madrid (referencia regional: ~45 € en Nuakchot, 2024)",
        alerta="Algunas embajadas europeas han dejado de emitir visados turísticos y otras tardan semanas (2024-2026).",
        oficial="https://www.embajadademali.es/", maec=_maec("Malí")),
    "burkina-faso": visa(
        "electronico", "Visado obligatorio; eVisa prioritario y sin visado en frontera.",
        "Tramitar online e imprimirlo; completar además la ficha de viaje dentro de las 72 h previas.", ruta="fuera",
        alerta="Fuera del itinerario por conflicto; disponer de eVisa no convierte el viaje en aceptable.",
        oficial="https://www.visaburkina.bf/", maec=_maec("Burkina Faso")),
    "libia": visa(
        "no_viable", "No se expiden visados turísticos.",
        "Excluir del viaje.", ruta="fuera",
        alerta="MAEC desaconseja el viaje y el país exige además visado de salida.", maec=_maec("Libia")),
}

# La imagen de planificación es la fuente única de fechas aproximadas. Las
# notas manuales de esta tabla solo se conservan para países sin fecha propia.
from data_planificacion import pasos_visado
for _slug, _datos in VISADOS.items():
    _pasos = pasos_visado(_slug)
    if _pasos:
        _datos["pasos"] = _pasos

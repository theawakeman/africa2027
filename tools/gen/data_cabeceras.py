# -*- coding: utf-8 -*-
"""Resumen uniforme y compacto de las cabeceras de país.

La cabecera no es una segunda ficha: solo permite comparar países de un
vistazo. Los detalles y matices permanecen en las secciones de cada página.
Los valores se construyen a partir de los datos ya auditados de la app; cuando
un tema no está verificado se dice expresamente en vez de inferirlo.
"""

import re

from data_cpd import CPD
from data_planificacion import resumen as resumen_planificacion
from data_visados import NIVELES as NIVELES_VISADO, VISADOS


CAMPOS = (
    "FECHAS", "BAJADA", "SUBIDA", "VISADO", "CPD", "SEGURO", "SEGURIDAD",
    "PDIs", "4x4", "A PIE", "VACUNACIÓN", "DRONES", "STARLINK", "PELIGROS",
)


# Solo se resumen extremos y kilometraje. El itinerario completo sigue en la
# sección Ruta y no debe volver a copiarse en la cabecera.
RUTAS = {
    "marruecos": ("Tánger Med → Tarfaya", "Tarfaya → Tánger Med"),
    "sahara-occidental": ("Tarfaya → Guerguerat · ~1.100 km", "Guerguerat → Tan-Tan · ~1.500 km"),
    "mauritania": ("Guerguerat → Diama", "Diama → Guerguerat"),
    "senegal": ("Diama → Kalifourou", "Casamance → Gambia → Dakar"),
    "guinea": ("Koundara → N'Zo · ~1.900 km", "N'Zo → Koundara · ~1.250 km"),
    "costa-de-marfil": ("N'Zoo → Elubo · ~1.700 km", "Sampa → Sipilou · ~1.500 km"),
    "ghana": ("Elubo → Aflao · ~900 km", "Akanu → Sampa · ~1.600 km"),
    "togo": ("Aflao → Hillacondji · ~70 km", "Ouaké → Wli · ~800 km"),
    "benin": ("Hillacondji → Sèmè · ~270 km", "Ilara → Ouaké · ~700 km"),
    "nigeria": ("Sèmè → Ekok · ~1.135 km", "Ekok → Idiroko · ~1.350 km"),
    "camerun": ("Ekok → Ntam · ~1.500 km", "Moloundou → Ekok · ~1.900 km"),
    "congo": ("Ntam → Massabi", "Massabi → Camerún"),
    "rd-congo": ("Yema → Lufu · sin ferry", "Lufu → Yema · sin ferry"),
    "angola": ("Massabi → Cabinda → Yema · Lufu → Luanda", "Luanda → Luvo · Yema → Cabinda → Massabi"),
    "zambia": ("Chavuma → Nakonde · ~3.200 km", "No aplica"),
    "tanzania": ("Tunduma → Namanga · ~3.000 km", "Horohoro → Mtwara · ~1.700 km"),
    "kenia": ("Namanga → Diani", "Diani → Lunga Lunga"),
    "mozambique": ("Matchedje → Machipanda", "No aplica"),
    "zimbabue": ("Forbes → Kazungula · ~2.400 km", "No aplica"),
    "botsuana": ("Kazungula → Martin's Drift · ~2.300 km", "No aplica"),
    "sudafrica": ("Martin's Drift → Ciudad del Cabo", "Ciudad del Cabo → Vioolsdrif"),
    "namibia": ("Noordoewer → Oshikango · ~3.500 km", "No aplica"),
    "gambia": ("No aplica", "Séléti → Banjul → Karang · ~220 km"),
    "sierra-leona": ("No aplica", "Opcional: Pamelap ↔ Freetown"),
    "liberia": ("Fuera de la ruta fija", "Solo si se resuelve el visado"),
    "gabon": ("No aplica", "Opcional: Camerún → Congo"),
    "malaui": ("Opcional: Tanzania → Malaui", "Malaui → Mozambique"),
    "uganda": ("Opcional: Kenia → Uganda", "Uganda → Ruanda/Tanzania"),
    "ruanda": ("Opcional: Uganda → Ruanda", "Ruanda → Tanzania"),
    "esuatini": ("Opcional: Sudáfrica → Esuatini", "Esuatini → Mozambique"),
    "lesoto": ("Opcional: entrada desde Sudáfrica", "Regreso a Sudáfrica"),
    "madagascar": ("Solo en avión", "No aplica"),
    "etiopia": ("Fuera de ruta · no se sube al Cuerno", "No aplica"),
    "sudan": ("Excluido · conflicto activo", "No aplica"),
    "egipto": ("Fuera de ruta · viaje aparte", "No aplica"),
    "yibuti": ("Fuera de ruta · viaje aparte", "No aplica"),
    "tunez": ("Fuera de ruta · ferry desde Italia/Francia", "No aplica"),
    "mali": ("Excluido · conflicto activo", "No aplica"),
    "guinea-bisau": ("Excluido · junta militar", "No aplica"),
    "argelia": ("Fuera de ruta · ferry desde España", "No aplica"),
    "libia": ("Excluido · conflicto activo", "No aplica"),
    "burkina-faso": ("Excluido · conflicto activo", "No aplica"),
    "niger": ("Excluido · conflicto activo", "No aplica"),
    "chad": ("Excluido · conflicto activo", "No aplica"),
    "rca": ("Excluido · conflicto activo", "No aplica"),
    "sudan-del-sur": ("Excluido · conflicto activo", "No aplica"),
    "eritrea": ("Fuera de ruta · solo en avión", "No aplica"),
    "somalia": ("Excluido · conflicto activo", "No aplica"),
    "guinea-ecuatorial": ("Fuera de ruta · solo en avión", "No aplica"),
    "cabo-verde": ("Fuera de ruta · solo en avión", "No aplica"),
    "santo-tome": ("Fuera de ruta · solo en avión", "No aplica"),
    "comoras": ("Fuera de ruta · solo en avión", "No aplica"),
    "seychelles": ("Fuera de ruta · solo en avión", "No aplica"),
    "mauricio": ("Fuera de ruta · solo en avión", "No aplica"),
    "burundi": ("Fuera de ruta · frontera RW cerrada", "No aplica"),
}


FECHAS_CORTAS = {
    "sahara-occidental": "Incluido en Marruecos",
    "kenia": "Sin fecha · encajar en el bucle",
}


ACTIVIDADES = {
    "marruecos": ("Atlas · Tizi n'Test", "Medinas y senderos del Atlas"),
    "sahara-occidental": ("No salir del corredor validado", "Paradas solo en zonas seguras"),
    "mauritania": ("Adrar · Tifoujar · Richat", "Oasis y cañones del Adrar"),
    "senegal": ("Ferlo y pistas de Casamance", "Dindefelo y costa"),
    "congo": ("Odzala y pistas forestales", "Odzala · Diosso · costa"),
    "rd-congo": ("Muanda–Yema tras lluvias", "Sin hito prioritario"),
    "angola": ("Baía dos Tigres · Iona · Serra da Leba", "Morro do Moco · Tundavala"),
    "gabon": ("Red mayoritariamente sin asfaltar", "Lopé y Loango con guía"),
    "gambia": ("Variante del río", "Costa · aves · sitios UNESCO"),
    "esuatini": ("Pistas de Malolotja", "Sibebe · Malolotja · Mlilwane"),
    "lesoto": ("Sani Pass", "Sani Top y montaña"),
    "madagascar": ("Sin los vehículos", "Rutas locales por auditar"),
    "tunez": ("Erg de Douz · Ksar Ghilane · sur con guía", "Cañón de Midès · cabo Angela · Ichkeul"),
    "mali": ("Solo en avión: nadie cruza Mali con vehículo propio", "Bamako y Siby con guía, si algún día se levanta el veto"),
    "guinea-bisau": ("Asfalto roto · pistas · lluvias jun–oct intransitables", "Bissau de día sí · Bijagós solo sin coche"),
    "sudan": ("Sin cruces de overlanders desde 2023 · CPD aceptado", "No: riesgo de detención y secuestro en todo el país"),
    "egipto": ("CPD obligatorio + matrícula y carné egipcios", "Valle del Nilo sí; desierto y norte del Sinaí, no"),
    "etiopia": ("Imprescindible fuera del asfalto · 250 km/día, irreal", "Solo de día y en la capital; nunca solo de noche"),
    "yibuti": ("Imprescindible · convoy de dos · nunca de noche", "Solo en la capital y de día · nada fuera del asfalto"),
    "argelia": ("Sí, con TIP 90 días · gasóleo con mucho azufre", "Solo ciudades del norte · sur con agencia"),
    "libia": ("Sin entrada documentada con vehículo propio desde 2012", "Imposible: guía y policía turística obligatorios"),
    "burkina-faso": ("Diésel 675 XOF/l (feb-2026) · minas en los ejes", "Solo casco urbano y de día · nunca interurbano"),
    "niger": ("Inviable: escolta militar obligatoria fuera de Niamey", "No: el MAEC desaconseja caminar por Niamey"),
    "chad": ("Autorización del Interior para salir de Yamena", "Desaconsejado andar por Yamena, incluso de día"),
    "rca": ("Corredor único Béloko–Bangui · IED en el noroeste", "Descartado · secuestro frecuente fuera de Bangui"),
    "sudan-del-sur": ("Obligatorio fuera de Yuba · permiso y minas", "Descartado · asaltos armados día y noche"),
    "eritrea": ("Inviable: fronteras cerradas · coche con conductor", "Prohibido moverse entre ciudades a pie"),
    "somalia": ("Solo con escolta armada privada", "Descartado fuera de recinto fortificado"),
    "guinea-ecuatorial": ("Inviable: Bioko es isla y el continente está cerrado", "Solo de día · pasaporte y visado siempre encima"),
    "cabo-verde": ("Solo alquiler local · sin ro-ro desde el continente", "Santo Antão y Fogo: el mejor senderismo insular"),
    "santo-tome": ("Solo para el sur, Praia Jalé y el Obô", "Capital y roças sin problema · de noche, no"),
    "comoras": ("Inútil: sin ferry al continente · 40 €/día con chófer", "Moroni de día sí · nunca solo de noche"),
    "seychelles": ("Inútil: 453 km de carretera y se conduce por la izquierda", "Excelente: senderos de Mahé, Valle de Mai y La Digue"),
    "mauricio": ("Innecesario · asfalto y conducción por la izquierda", "Sí · Black River Gorges, Le Morne y Le Pouce"),
    "burundi": ("Solo por Tanzania · entrar con depósito lleno", "No de noche · ni calle ni transporte tras el ocaso"),
}


SEGUROS = {
    "marruecos": "Seguro válido en Marruecos",
    "sahara-occidental": "Cobertura de Marruecos",
    "mauritania": "Seguro local · confirmar",
    "senegal": "Brown Card CEDEAO",
    "gambia": "Brown Card CEDEAO",
    "guinea": "Brown Card CEDEAO",
    "sierra-leona": "Brown Card CEDEAO",
    "liberia": "Brown Card CEDEAO",
    "costa-de-marfil": "Brown Card CEDEAO",
    "ghana": "Brown Card CEDEAO",
    "togo": "Brown Card CEDEAO",
    "benin": "Brown Card CEDEAO",
    "nigeria": "Brown Card CEDEAO",
    "camerun": "Carte Rose CEMAC",
    "gabon": "Carte Rose CEMAC",
    "congo": "Carte Rose CEMAC · confirmar",
    "tunez": "Carta Verde española válida (TN) · solo terceros",
    "madagascar": "Sin Carta Verde · seguro incluido en alquiler con chófer",
    "mali": "Carta Verde no válida · Carte Brune por confirmar",
    "guinea-bisau": "Carte Brune CEDEAO obligatoria · Carta Verde no vale",
    "sudan": "Carta Verde no válida · seguro viaje no cubre",
    "egipto": "Carta Verde y Yellow Card NO valen · local",
    "etiopia": "Sin Carta Verde · Yellow Card COMESA obligatoria",
    "yibuti": "Carta Verde no vale · COMESA Yellow Card",
    "argelia": "Carta Verde NO vale · seguro local en frontera",
    "libia": "Sin Carta Verde · seguro local sin confirmar",
    "burkina-faso": "Carta Verde NO cubre · Carte Brune CEDEAO",
    "niger": "Sin cobertura: MAEC desaconseja absolutamente",
    "chad": "Carta Verde no cubre · Carte Rose CEMAC",
    "rca": "Sin cobertura española · Carte Rose CEMAC",
    "sudan-del-sur": "Ninguna póliza cubre el país: no hay cobertura",
    "eritrea": "Carta Verde no vale · seguro local por confirmar",
    "somalia": "Sin cobertura estándar · evacuación obligatoria",
    "guinea-ecuatorial": "Carta Verde no vale · Carte Rose CEMAC s/confirmar",
    "cabo-verde": "Carta Verde no vale · póliza local",
    "santo-tome": "Carta Verde no vale · repatriación obligatoria",
    "comoras": "Carta Verde no vale · póliza local en destino",
    "seychelles": "Seguro médico OBLIGATORIO para entrar",
    "mauricio": "Sin Carta Verde · seguro local obligatorio",
    "burundi": "Carta Verde no vale · Yellow Card COMESA",
}


PELIGROS = {
    "sahara-occidental": "Minas al este del muro",
    "mauritania": "Adrar: validación diaria",
    "senegal": "Este y Casamance: precaución",
    "guinea": "Frontera con Malí excluida",
    "sierra-leona": "Lluvias fuertes mayo–noviembre",
    "liberia": "Visado terrestre bloqueante",
    "costa-de-marfil": "Norte y Comoé desaconsejados",
    "togo": "No viajar al norte de Kandé",
    "benin": "Pendjari y W excluidos",
    "nigeria": "Corredor sur sin desvíos",
    "camerun": "NO, SO y Extremo Norte excluidos",
    "gabon": "Visado terrestre bloqueante",
    "congo": "RN4 degradada · solo de día",
    "rd-congo": "MAEC desaconseja la carretera",
    "angola": "Cabinda: validar antes de entrar",
    "namibia": "Grava y aislamiento",
    "sudafrica": "Criminalidad urbana alta",
    "mozambique": "Cabo Delgado y Niassa excluidos",
    "malaui": "Esquistosomiasis en agua dulce",
    "tanzania": "Situación política a revalidar",
    "kenia": "Evitar frontera con Somalia",
    "botsuana": "Aislamiento y fauna en pistas",
    "zimbabue": "Controles y efectivo",
    "uganda": "Tsetsé en Bwindi/QENP",
    "ruanda": "Bolsas de plástico prohibidas",
    "sudan": "Guerra civil · drones · secuestro",
    "etiopia": "Conflicto armado en 7 regiones",
    "egipto": "Norte del Sinaí desaconsejado",
    "tunez": "Fronteras con Argelia y Libia vetadas",
    "madagascar": "Dahalo · asaltos · noche",
    "mali": "Terrorismo, secuestro, minas",
    "guinea-bisau": "Golpe 2025 · minas · carreteras",
    "yibuti": "Calor 45 °C · minas · fronteras",
    "argelia": "Sur y fronteras · terrorismo",
    "libia": "Milicias, minas y secuestros",
    "burkina-faso": "Terrorismo y secuestro: todo BF",
    "niger": "Terrorismo y secuestro: máximo",
    "chad": "Secuestro en todo el país",
    "rca": "Guerra civil · secuestro · IED",
    "sudan-del-sur": "Conflicto armado y secuestros",
    "eritrea": "Minas y control militar",
    "somalia": "Terrorismo y secuestro: extremo",
    "guinea-ecuatorial": "Retenes y detención por fotos",
    "cabo-verde": "Delincuencia urbana en Praia",
    "santo-tome": "Malaria alta · sanidad básica",
    "comoras": "Inestable · sin sanidad fiable",
    "seychelles": "Mar y robos · país muy seguro",
    "mauricio": "Ciclones y chikungunya",
    "burundi": "Conflicto al oeste · granadas",
}


def _clean(value):
    value = re.sub(r"<[^>]+>", "", str(value or ""))
    return re.sub(r"\s+", " ", value).strip(" .")


def _short(value, limit=58):
    value = _clean(value)
    if len(value) <= limit:
        return value
    cut = value[: limit + 1]
    for sep in (" · ", " — ", "; ", ". ", " "):
        pos = cut.rfind(sep)
        if pos >= max(20, limit // 2):
            return cut[:pos].rstrip() + "…"
    return cut[:limit].rstrip() + "…"


def _chip_map(data):
    return {_clean(label).upper(): _clean(value) for label, value in data.get("chips", [])}


def _pick(chips, *needles):
    for needle in needles:
        needle = needle.upper()
        for label, value in chips.items():
            if needle == label or needle in label:
                return value
    return ""


def _section_html(data, section_id):
    for sid, _title, body in data.get("custom_sections_post", []):
        if sid == section_id:
            return body
    return ""


def _section_summary(data, section_id):
    """Extrae el estado breve ya auditado del callout de una sección."""
    body = _section_html(data, section_id)
    if not body:
        return ""
    match = re.search(r'class="callout-title">([^<]+)', body)
    title = _clean(match.group(1)) if match else ""
    generic = {"regla simple", "decisión práctica", "estado 2026"}
    if title.lower() not in generic:
        return title
    text = _clean(body)
    if title and text.startswith(title):
        text = text[len(title):].strip()
    return re.split(r"(?<=[.!?])\s", text, maxsplit=1)[0]


def _visa(slug, fallback=""):
    item = VISADOS.get(slug)
    if item:
        return NIVELES_VISADO[item["nivel"]][1]
    return "Por auditar" if not fallback or fallback == "—" else _short(fallback)


def _cpd(slug, fallback=""):
    item = CPD.get(slug)
    if not item:
        return "Por auditar" if not fallback or fallback == "—" else _short(fallback)
    nivel, _confianza, alternativa, _coste, _nota = item
    estado = {"no": "No obligatorio", "recomendable": "Recomendable", "obligatorio": "Obligatorio"}[nivel]
    tramite = re.sub(r"\s*\([^)]*\)", "", alternativa).strip()
    reemplazos = {
        "Temporary Vehicle Admission Permit «Safe Passage»": "TVAP / Safe Passage",
        "Temporary Import Permit de BURS + National Road Safety Fund levy": "TIP de BURS + tasa vial",
        "Permiso de tránsito con localizador GPS": "Permiso con localizador",
        "Cross-Border Charge del RFA + permiso temporal en frontera": "Tasa RFA + permiso temporal",
        "Sin TIP: paquete de tasas en frontera": "Tasas en frontera",
        "TIP obligatorio + seguro local obligatorio": "TIP + seguro local",
        "TIP de ZIMRA + carbon tax + seguro + peajes": "TIP ZIMRA + tasas",
    }
    tramite = reemplazos.get(tramite, tramite)
    tramite = _short(tramite, 32)
    return f"{estado} · {tramite}" if tramite and tramite != "No aplica" else estado


def _rutas(slug, group):
    if slug in RUTAS:
        return RUTAS[slug]
    if group == "excluido":
        return "Excluido por protocolo", "No aplica"
    if group == "fuera":
        return "Fuera de la ruta prevista", "No aplica"
    if group == "vuelo":
        return "Solo en avión", "No aplica"
    if group == "subida":
        return "No aplica", "Por auditar"
    if group == "alternativa":
        return "Alternativa · por auditar", "No aplica"
    return "Por auditar", "Por auditar"


def construir(slug, group, *, data=None, fallback=None):
    """Devuelve siempre los catorce campos, en el orden visual aprobado."""
    data = data or {}
    fallback = fallback or {}
    chips = _chip_map(data)
    bajada, subida = _rutas(slug, group)
    actividades = ACTIVIDADES.get(slug, ("", ""))

    cuatro = _pick(chips, "4X4", "EXPEDICIÓN 4X4") or actividades[0]
    pie = _pick(chips, "A PIE") or actividades[1]
    if not cuatro:
        cuatro = "Por auditar" if not data else "Sin hito resumido"
    if not pie:
        pie = "Por auditar" if not data else "Sin hito resumido"

    seguridad = _pick(chips, "SEGURIDAD") or fallback.get("seguridad", "")
    if not seguridad:
        seguridad = "Por auditar"

    dron = _pick(chips, "DRONES", "DRON") or _section_summary(data, "drones") or "Por verificar"
    starlink = _pick(chips, "STARLINK")
    if not starlink:
        comunicaciones = _pick(chips, "COMUNICACIONES")
        starlink = (comunicaciones if "starlink" in comunicaciones.lower()
                    else _section_summary(data, "starlink") or "Por verificar")

    salud = _pick(chips, "SALUD")
    if salud:
        vacunacion = _short(salud, 52)
    elif "fiebre amarilla" in _clean(_section_html(data, "perro")).lower():
        vacunacion = "Fiebre amarilla · ver ficha"
    else:
        vacunacion = "Por verificar" if data else "Por auditar"

    if data:
        pois = sum(1 for p in data.get("pois", []) if p.get("type", "poi") == "poi")
        pdis = f"{pois} puntos" if pois else "Sin PDIs publicados"
    else:
        pdis = "Pendiente de ficha"

    seguro = SEGUROS.get(slug) or _pick(chips, "SEGURO") or "Por verificar"
    peligro = PELIGROS.get(slug)
    if not peligro:
        if group == "excluido":
            peligro = "Conflicto · país excluido"
        elif group == "fuera":
            peligro = "Fuera de la ruta"
        elif not data:
            peligro = "Por auditar"
        else:
            peligro = "Por verificar"

    values = (
        FECHAS_CORTAS.get(slug, resumen_planificacion(slug, group)), bajada, subida,
        _visa(slug, fallback.get("visado", "")), _cpd(slug, fallback.get("cpd", "")),
        _short(seguro, 52), _short(seguridad, 58), pdis, _short(cuatro, 58), _short(pie, 58),
        vacunacion, _short(dron, 52), _short(starlink, 52), peligro,
    )
    return list(zip(CAMPOS, values))

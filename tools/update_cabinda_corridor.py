#!/usr/bin/env python3
"""Replantea Congo, Cabinda y Kongo Central sin convertir el ferry en ruta principal.

Actualiza las fichas operativas, los puntos logísticos y los PDIs afectados. La
historia larga ya auditada de cada país se conserva; cambian todas las secciones
que dependen del itinerario, fronteras, vehículo, agua, seguridad o costes.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote


ROOT = Path(__file__).resolve().parents[1]


def load(relative: str):
    return json.loads((ROOT / relative).read_text(encoding="utf-8"))


def save(relative: str, value) -> None:
    (ROOT / relative).write_text(
        json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )


def ticks(items: list[str]) -> str:
    return '<ul class="ticks">' + "".join(f"<li>{item}</li>" for item in items) + "</ul>"


def table(headers: tuple[str, ...], rows: list[tuple[str, ...]], cls: str = "") -> str:
    head = "".join(f"<th>{cell}</th>" for cell in headers)
    body = "".join(
        "<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in rows
    )
    return (
        f'<div class="tblwrap"><table class="{cls}"><thead><tr>{head}</tr></thead>'
        f"<tbody>{body}</tbody></table></div>"
    )


def callout(title: str, body: str, style: str = "") -> str:
    return (
        f'<div class="callout {style}"><div class="callout-title">{title}</div>'
        f"<p>{body}</p></div>"
    )


def section(section_id: str, title: str, body: str) -> list[str]:
    return [section_id, title, body]


def history_section(data: dict) -> list[str]:
    for item in data["custom_sections"]:
        if item[0] == "historia":
            return item
    raise KeyError("Falta la sección de historia")


OFFICIAL = {
    "congo_border": "https://www.unicongo.cg/wp-content/uploads/2025/11/Rapport-sur-le-mouvement-de-fonds-dans-les-frontieres-4eme-trimestre-2024.pdf",
    "congo_road": "https://www.lecourrierdekinshasa.com/node/163031",
    "congo_visa": "https://v2.ambacongofr.org/site/services?cat=visas",
    "congo_girafe": "https://girafe.ambacongofr.org/",
    "angola_border": "https://antt.gov.ao/pt/noticias/ANTT-e-CGCF-Iniciam-Actividades-Transfronteiricas-no-Yema-e-Visitam-Delegacao-Aduaneira-de-Massabi",
    "angola_fees": "https://www.antt.gov.ao/docs/content/NoticeOfApplicableBorderFeesReciprocityMeasuresWithDRC.pdf",
    "angola_visa": "https://governo.gov.ao/noticias/1046/governo/decreto-presidencial/angola-isenta-cidadaos-de-98-paises-de-vistos-de-turismo",
    "angola_history": "https://www.ciam.gov.ao/ao/angola/historia",
    "cabinda_profile": "https://cabinda.gov.ao/web/sobrenos",
    "angola_maec": "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Angola",
    "angola_fcdo": "https://www.gov.uk/foreign-travel-advice/angola",
    "drc_yema": "https://acp.cd/science-sante-environnement/muanda-inauguration-du-batiment-de-poste-controle-sanitaire-de-la-frontiere-de-yema/",
    "drc_road": "https://acgt.cd/2025/09/29/kongo-central-la-premiere-ministre-lance-les-travaux-de-la-route-moanda-yema/",
    "drc_bridge": "https://www.radiookapi.net/2026/02/07/actualite/societe/pluies-diluviennes-muanda-effondrement-du-pont-budubudu-et-isolement-de",
    "drc_visa": "https://ambardcmadrid.com/visa/",
    "drc_maec": "https://exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/Detalle-recomendaciones-de-viaje.aspx?trc=Rep%C3%BAblica+Democr%C3%A1tica+del+Congo",
    "sadc_hours": "https://www.sadc.int/file/2956/download?token=MkUQM75V",
}


def congo() -> None:
    path = "content/ficha/congo.json"
    data = load(path)
    history = section(
        "historia",
        "Historia y contexto",
        "<p>El sur del Congo enlaza con los antiguos reinos de Kongo y Loango; el centro, con las mesetas teke; y el norte, con las sociedades de la gran selva. Brazzaville fue capital del África Ecuatorial Francesa y uno de los centros de la Francia Libre, mientras Pointe-Noire creció como puerto del ferrocarril Congo–Océan. La independencia de 1960, el periodo marxista y las guerras de los años noventa explican un Estado hoy muy centralizado y dependiente del petróleo.</p>"
        + callout(
            "Historia completa · con audio",
            "Orígenes, Loango, colonización, independencia y situación actual, con fuentes y audio narrado para escuchar en ruta: <a href=\"historia/\">leer y escuchar la historia de Congo (Brazzaville) →</a>",
        ),
    )
    data.update(
        revision="15 sep 2026",
        verificado=True,
        chips=[
            ["BAJADA", "Ntam → Ouesso → Odzala → Brazzaville → Dolisie → Pointe-Noire → Massabi"],
            ["SUBIDA", "Massabi → Pointe-Noire → Brazzaville → mesetas Batéké → Ouesso → Camerún"],
            ["CRUCE PRINCIPAL", "Tchiamba-Nzassi / Massabi · terrestre hacia Cabinda · sin ferry"],
            ["ALTERNATIVA", "Ferry Brazzaville–Kinshasa · conservado, secundario y apagado en el mapa"],
            ["PDIs", "18 puntos · Odzala, Brazzaville, Loango, Diosso y costa"],
            ["PERRO", "Prohibido en áreas de gorilas; plan de cuidado cerrado antes de Odzala"],
            ["AGUA", "Sin grifos públicos verificados: recarga pactada en bases urbanas"],
            ["RIESGO", "RN4 degradada y controles; todo el tramo solo de día"],
        ],
        notice=(
            "Ruta revisada para usar Massabi–Cabinda como corredor principal. Revalidar por escrito "
            "visados, vehículo y apertura de Massabi/Yema 30–60 días antes y otra vez 72 h antes; "
            "las horas publicadas son referencia, no garantía operativa."
        ),
        logistics=[
            {
                "name": "Frontera · Entrada bajada — Ntam / Souanké (desde Camerún)",
                "cat": "Frontera", "lat": 2.1720894, "lon": 13.6984289,
                "info": "Pin del Poste de Contrôle Unique Frontalier. Confirmar admisión de turismos extranjeros, inmigración y sellado aduanero antes de usar el corredor.",
            },
            {
                "name": "Frontera principal · Tchiamba-Nzassi / Massabi (hacia Cabinda)",
                "cat": "Frontera", "lat": -4.98944, "lon": 12.05712,
                "info": "Puesto terrestre real en la RN4. UniCongo documenta presencia de policía, gendarmería, inteligencia, aduanas y ARTF, y movimiento de viajeros en 2024. La referencia SADC indica 08:00–17:00; confirmar horario, importación temporal y coste para vehículo particular 72 h antes.",
            },
            {
                "name": "Frontera principal · Massabi / Tchiamba-Nzassi (entrada subida)",
                "cat": "Frontera", "lat": -4.98944, "lon": 12.05712,
                "info": "Mismo puesto terrestre de regreso desde Cabinda. El visado congoleño debe cubrir esta segunda entrada; no presentarse confiando en una entrada anterior ya consumida.",
            },
            {
                "name": "Alternativa secundaria · Beach de Brazzaville / ferry a Kinshasa",
                "cat": "Frontera", "lat": -4.279, "lon": 15.286,
                "info": "Cruce fluvial conservado solo como plan alternativo. No es ruta principal por coste, esperas, despacho separado del vehículo y ausencia de puente. No reservar ni acercarse sin gestor y presupuesto escrito.",
            },
            {
                "name": "Frontera · Salida subida — Socambo / Moloundou (hacia Camerún)",
                "cat": "Frontera", "lat": 1.7062057, "lon": 16.1201673,
                "info": "Paso fluvial todavía condicionado a confirmar barcaza para vehículos, aduana y horario. Plan B: salir otra vez por Ntam/Souanké.",
            },
            {
                "name": "CHU de Brazzaville",
                "cat": "Hospital", "lat": -4.264965, "lon": 15.2691522,
                "info": "El pin marca el complejo hospitalario real. Referencia nacional; confirmar admisión y cobertura del seguro antes del viaje.",
            },
            {
                "name": "Pointe-Noire · zona urbana de servicios",
                "cat": "Servicios", "lat": -4.7975, "lon": 11.8481,
                "info": "Referencia del centro urbano, no una gasolinera, taller, hospital ni grifo concretos. Aquí debe cerrarse una base vigilada que confirme por escrito estacionamiento, reparación si hace falta y recarga de agua de servicio antes de Massabi.",
            },
            {
                "name": "Ouesso · zona urbana de servicios",
                "cat": "Servicios", "lat": 1.6167, "lon": 16.05,
                "info": "Referencia urbana, no instalación concreta. Reponer combustible, comida y agua mediante un hotel o misión que lo confirme antes de entrar en el bloque forestal.",
            },
            {
                "name": "Brazzaville · zona urbana de servicios",
                "cat": "Servicios", "lat": -4.2634, "lon": 15.2429,
                "info": "Referencia de área logística, no grifo público. Concertar alojamiento con patio, combustible formal y permiso explícito para recargar el depósito de ducha y lavado.",
            },
        ],
    )

    summary = (
        "<p>El país conserva su gran parada en <strong>Odzala-Kokoua</strong>, pero cambia la salida al sur. "
        "Después de Brazzaville, la bajada continúa por la RN1 hacia Dolisie y Pointe-Noire y enlaza con "
        "la RN4 hasta <strong>Tchiamba-Nzassi/Massabi</strong>. Desde allí se atraviesa Cabinda por carretera "
        "hasta Yema y se entra en RD Congo por Muanda. En la subida se repite este eje en sentido inverso. "
        "El ferry Brazzaville–Kinshasa queda documentado como alternativa, no como itinerario previsto.</p>"
        + callout(
            "Qué está demostrado",
            "Massabi es un puesto terrestre activo con los organismos fronterizos necesarios y tráfico documentado. Lo que no está publicado es un tarifario completo para dos vehículos particulares extranjeros: cualquier cifra de transporte colectivo se excluye del presupuesto del coche.",
            "ok",
        )
        + callout(
            "Condición de seguridad",
            "Evitar el ferry reduce un problema logístico y económico, pero obliga a atravesar Cabinda. La ruta solo se ejecuta si los avisos consulares, el seguro y un contacto local confirman el corredor Massabi–Cabinda–Yema; de lo contrario se activa el plan secundario.",
            "warn",
        )
        + table(
            ("Tema", "Decisión vigente"),
            [
                ("Salida y entrada sur", "Massabi por carretera, en ambos sentidos."),
                ("Ferry", "Alternativa secundaria, capa apagada por defecto."),
                ("RN4", "Asfalto existente, pero con degradación severa publicada en 2025; calcular con margen y luz."),
                ("Visado", "Sello físico tramitado mediante París; pedir una solución que cubra dos entradas."),
                ("Agua", "Nada se presenta como grifo confirmado: recarga acordada en Pointe-Noire, Brazzaville u Ouesso."),
            ],
        )
    )

    route = (
        "<p>El trazado ya no contiene un desvío opcional a la costa: <strong>Dolisie y Pointe-Noire pasan a formar parte del corredor principal</strong>. La RN4 termina en el puesto de Tchiamba-Nzassi/Massabi, conectado con Cabinda.</p>"
        + table(
            ("Etapa", "Recorrido", "Criterio"),
            [
                ("Bajada 1", "Ntam → Souanké → Ouesso", "Confirmar el paso camerunés y completar autonomía en Ouesso."),
                ("Bajada 2", "Ouesso → Odzala → Brazzaville", "Bloque de gorilas reservado; pistas según operador y estación."),
                ("Bajada 3", "Brazzaville → Dolisie → Pointe-Noire", "RN1; Pool y tráfico pesado, siempre de día."),
                ("Bajada 4", "Pointe-Noire → Massabi", "RN4; tramo degradado documentado después del peaje."),
                ("Subida 1", "Massabi → Pointe-Noire → Brazzaville", "Mismo eje; segunda entrada cubierta por el visado."),
                ("Subida 2", "Brazzaville → mesetas Batéké → Ouesso", "Corredor distinto hacia el norte; combustible planificado."),
            ],
            "num",
        )
        + ticks([
            "Pointe-Noire es ahora la última base completa antes de Cabinda: resolver taller, efectivo, SIM, víveres y agua antes de salir.",
            "No convertir los 10–12 km degradados de la RN4 en una velocidad media para toda la vía: comprobar estado local y asignar el día entero al cruce.",
            "No circular de noche ni detenerse a fotografiar frontera, instalaciones petroleras, puerto o controles.",
            "Diosso y Conkouati siguen siendo PDIs válidos, pero son excursiones laterales; el cruce no debe esperar por ellos.",
        ])
    )

    water = (
        "<h3>Recarga para ducha y lavado</h3>"
        + callout(
            "Sin puntos públicos verificados",
            "No se ha identificado un grifo público mantenido y accesible a un vehículo en el corredor. Los marcadores del mapa son zonas de servicio, nunca promesas de agua.",
            "warn",
        )
        + ticks([
            "Pointe-Noire: cerrar un hotel, campamento o taller con patio que autorice manguera y confirme presión/calidad. Es la recarga completa obligatoria antes de Massabi.",
            "Brazzaville, Ouesso y Owando: misma estrategia; pedir permiso, confirmar que el agua no es salobre y usar filtro de sedimentos al llenar.",
            "Odzala y pistas forestales: solo usar agua facilitada por el campamento u operador. Si procede de pozo o río, filtrar y desinfectar; no llenar a ciegas.",
            "Mantener separada el agua potable: garrafas selladas para beber y cocinar; el depósito de servicio no se declara potable por haber salido de una manguera.",
            "Entrar en Cabinda con depósito de servicio lleno y reserva mínima de dos días por posibles demoras en dos fronteras consecutivas.",
        ])
        + "<h3>Combustible</h3>"
        + ticks([
            "Llenar en Pointe-Noire y no depender de encontrar combustible inmediatamente en Massabi.",
            "En el norte, repostar formalmente en Ouesso y cada capital de departamento; para Odzala, obedecer la autonomía exigida por el operador.",
            "Cualquier combustible de bidón se filtra; no se promete disponibilidad por la presencia de un núcleo urbano en el mapa.",
        ])
    )

    borders = (
        "<h3>Visado</h3>"
        + ticks([
            "Pasaporte español: visado previo. La plataforma oficial GIRAFE prepara el expediente, pero el pasaporte físico se presenta o envía a la Embajada del Congo en París; no depender de una supuesta eVisa terrestre.",
            "La tarifa consular publicada para 91 días es 110 € ordinaria y 220 € urgente. Hotel o invitación con validación DDST, medios y justificantes forman parte del expediente.",
            "El país se visita dos veces. Pedir confirmación escrita de entradas múltiples y fechas que cubran ambas; si el documento emitido no lo hace, tramitar dos visados.",
        ])
        + "<h3>Pasos y vehículo</h3>"
        + table(
            ("Función", "Paso", "Estado real"),
            [
                ("Principal bajada", "Tchiamba-Nzassi / Massabi", "Puesto operativo documentado. Referencia horaria 08:00–17:00; reconfirmar 72 h."),
                ("Principal subida", "Massabi / Tchiamba-Nzassi", "Mismo puesto. Requiere segunda entrada válida."),
                ("Secundario", "Brazzaville / Kinshasa", "Ferry sin puente; vehículo y personas se procesan por separado. Solo contingencia."),
            ],
        )
        + ticks([
            "No existe una tarifa pública localizada para la importación temporal de un turismo extranjero en Massabi. Exigir recibo y desglose; no presupuestar con la tarifa de camiones de pasajeros publicada por UniCongo.",
            "Llevar CPD, permiso de circulación, autorización del titular, permisos internacionales y copias. Confirmar previamente qué documento temporal emite Aduanas del Congo.",
            "La Carte Rose solo sirve si la póliza concreta cubre República del Congo y las fechas; verificar certificado, no confiar en el nombre regional.",
            "El ferry se mantiene con toda su documentación histórica, pero no condiciona alojamiento, visado ni presupuesto de la ruta principal.",
        ])
    )

    dogs = (
        "<h3>Entrada del perro por el corredor real</h3>"
        + callout(
            "Massabi, no el ferry",
            "No se ha localizado una instrucción pública suficientemente completa para la entrada terrestre de una mascota extranjera por Tchiamba-Nzassi/Massabi. La documentación se prepara de forma conservadora y se confirma por escrito con los servicios veterinarios o consulares antes de las dos entradas.",
            "warn",
        )
        + ticks([
            "Llevar microchip, pasaporte UE, vacuna antirrábica en vigor, titulación serológica ya resuelta para el regreso a la UE y certificado veterinario internacional reciente. No se afirma un plazo local concreto sin respuesta oficial.",
            "El certificado de vigencia corta puede no cubrir la subida: reservar veterinario y nueva emisión antes del regreso. Guardar originales y varias copias en el expediente fronterizo.",
            "Confirmar dos cosas distintas para Massabi: admisión del perro en el puesto y documento exigido en la posterior entrada a Cabinda. Que el coche pueda cruzar no valida automáticamente al animal.",
            "Antiparasitario externo e interno revisado con veterinario: en el norte forestal hay garrapatas, filarias y mosca tsé-tsé, que también afecta a perros.",
        ])
        + callout(
            "Todo lo del perro, en su propia sección",
            "Requisitos comunes, salud en ruta y regreso a la UE: <a href=\"../../perro/\">ver la sección El perro →</a>. Documentación general en <a href=\"../../documentacion/#perro\">Documentación general</a>.",
        )
        + "<h3>Decisión por zona</h3>"
        + table(
            ("Zona", "Estado", "Plan operativo"),
            [
                ("Odzala-Kokoua y otros espacios de primates", '<span class="st st-red">perro fuera</span>', "No entrar con el perro. Cerrar cuidador o turnos antes de reservar; no dejarlo solo en el vehículo."),
                ("Brazzaville, Pointe-Noire, Dolisie, Ouesso", '<span class="st st-amber">con condiciones</span>', "Alojamiento que confirme admisión y patio, correa, sombra y evitar mercados densos."),
                ("Massabi y RN4", '<span class="st st-amber">trámite por confirmar</span>', "Papeles accesibles, perro controlado dentro del coche y ninguna parada suelta en frontera."),
                ("Selva del norte y mesetas", '<span class="st st-amber">precaución alta</span>', "Protección antiparasitaria, revisión diaria y autonomía de agua; no entrar en parques sin permiso."),
                ("Diosso, cataratas y corniche", '<span class="st st-green">correa corta</span>', "Bordes, roca mojada, tráfico y calor; confirmar la admisión cuando exista gestor."),
            ],
        )
        + "<h3>Salud humana</h3>"
        + ticks([
            "Certificado de fiebre amarilla obligatorio y accesible en cada frontera terrestre; paludismo durante todo el año y seguro de evacuación.",
            "No beber agua de grifo. Separar agua potable sellada del depósito de ducha y lavado; tratar por completo cualquier agua no embotellada destinada a consumo.",
            "Brazzaville y Pointe-Noire son las referencias sanitarias principales; Ouesso tiene capacidad limitada y una emergencia desde Odzala puede requerir evacuación aérea.",
            "Revisar alertas de cólera, mpox, ébola y otras enfermedades con Sanidad Exterior y OMS antes del viaje; no tocar ni consumir carne de caza.",
        ])
    )

    security = (
        "<p>El eje previsto combina selva remota, el Pool, la RN1, Pointe-Noire y una frontera terrestre. No se describe como «estable» sin matices.</p>"
        + ticks([
            "Consultar MAEC y seguro 30–60 días antes; evitar manifestaciones, edificios oficiales, instalaciones petroleras y zonas fronterizas fuera de la carretera.",
            "La RN4 Pointe-Noire–Cabinda fue descrita en febrero de 2025 con degradación avanzada y un tramo especialmente dañado tras el peaje. Obtener estado del día desde Pointe-Noire.",
            "Conducción únicamente diurna, dos vehículos juntos y alojamiento vigilado en Pointe-Noire antes y después del cruce.",
            "Nada de fotografía o dron en Massabi, puertos, puentes, aduanas, policía o infraestructura petrolera.",
            "Si Cabinda no queda cubierta por el seguro o un aviso desaconseja el corredor, no se fuerza el paso: se evalúa el ferry secundario con presupuesto cerrado o se pausa la ruta.",
        ])
    )

    decisions = (
        table(
            ("Cierre pendiente", "Evidencia exigida"),
            [
                ("Massabi", "Confirmación de apertura, horarios, turismos extranjeros, CPD/importación y tasas con recibo."),
                ("RN4", "Estado de los últimos kilómetros comunicado desde Pointe-Noire en las 24–48 h previas."),
                ("Visado", "Documento físico con dos entradas y fechas compatibles."),
                ("Cabinda", "Seguro válido + aviso consular revisado + contacto local que confirme Massabi–Yema."),
                ("Agua", "Nombre de establecimiento, persona que autoriza y fecha; si falta, el punto sigue como no verificado."),
                ("Socambo", "Barcaza, capacidad, aduana y horario; Ntam queda como plan B de salida norte."),
            ],
        )
        + callout("Regla", "Ningún comentario antiguo de un viajero sustituye la validación oficial y local de 2027.", "warn")
    )

    experiences = (
        "<p>Los relatos recientes sirven para estimar dificultad, nunca para fijar tasas o garantizar apertura.</p>"
        + ticks([
            "UniCongo registró movimiento real de pasajeros en Tchiamba-Nzassi durante el cuarto trimestre de 2024 y enumera los servicios fronterizos presentes: es la prueba más fuerte de que no es un paso inventado.",
            "Relatos de 2025 describen el trayecto terrestre Cabinda–Pointe-Noire como realizable pero lento, con barro y largas horas para unos 200 km. Se usa como advertencia cualitativa, no como tiempo garantizado.",
            "El ferry de las capitales conserva valor como contingencia, pero sus costes gestionados y demoras de aduana justifican que deje de ser la línea principal.",
        ])
    )

    existing_post = {item[0]: item for item in data["custom_sections_post"]}
    data["custom_sections"] = [
        section("resumen", "Resumen operativo", summary),
        history,
        section("ruta", "Ruta propuesta", route),
        section("agua-combustible", "Agua y combustible", water),
    ]
    data["custom_sections_post"] = [
        section("fronteras", "Visado, fronteras y vehículos", borders),
        existing_post["drones"],
        existing_post["starlink"],
        section("perro", "Perro y salud", dogs),
        section("seguridad", "Seguridad y comunicaciones", security),
        section("gpx", "Validación y decisiones", decisions),
        section("experiencias", "Experiencias de otros overlanders", experiences),
    ]
    data["sources"] = [
        ["UniCongo · actividad y organismos del puesto de Tchiamba-Nzassi (2024)", OFFICIAL["congo_border"]],
        ["Le Courrier de Kinshasa · estado de la RN4 Pointe-Noire–Cabinda (febrero de 2025)", OFFICIAL["congo_road"]],
        ["Embajada del Congo en Francia · visados y tarifas", OFFICIAL["congo_visa"]],
        ["Plataforma oficial consular GIRAFE", OFFICIAL["congo_girafe"]],
        ["ANTT Angola · actividad transfronteriza de Yema y aduana de Massabi", OFFICIAL["angola_border"]],
        ["SADC · directorio técnico de fronteras y horas de referencia", OFFICIAL["sadc_hours"]],
        ["FCDO · aviso de viaje de Angola/Cabinda", OFFICIAL["angola_fcdo"]],
    ]
    data["sources_note"] = "Prioridad a organismos oficiales. Los relatos de carretera solo se usan como evidencia secundaria del firme y los tiempos; las tasas de pasajeros nunca se convierten en tasas del vehículo."
    save(path, data)


def drc() -> None:
    path = "content/ficha/rd-congo.json"
    data = load(path)
    data["historia_resumen"] = (
        "La República Democrática del Congo reúne una extraordinaria diversidad humana y natural con una historia marcada por el Estado Libre de Leopoldo II, la colonización belga, la crisis de la independencia y la dictadura de Mobutu. Las guerras desde 1996 y sus secuelas siguen golpeando sobre todo al este. A septiembre de 2026, Félix Tshisekedi ejerce un segundo mandato en un sistema electoral muy limitado. Esta guía atraviesa solo Kongo Central por Yema, Muanda, Boma, Matadi y Lufu; queda lejos de los Kivus, pero no fuera de los riesgos de carretera, controles y fronteras."
    )
    for item in data["historia_secciones"]:
        if item[0] == "Colonización":
            item[1] = item[1].replace(
                "Esa infraestructura explica el itinerario, pero también materializa el coste humano y el propósito extractivo de la colonia.",
                "Ese eje explica la centralidad histórica de Matadi y Kinshasa, aunque el itinerario principal de esta guía gira hoy hacia la costa por Boma, Muanda y Yema. La infraestructura colonial también materializa el coste humano y el propósito extractivo de la colonia.",
            )
    history = section(
        "historia",
        "Historia y contexto",
        "<p>La historia del país no se reduce al conflicto del este. En el corredor actual, Kongo Central conserva la memoria del reino de Kongo, la primera capital colonial de Boma y el sistema extractivo que articuló Matadi con el interior. El Estado Libre de Leopoldo II impuso caucho y marfil mediante trabajo forzado y violencia de enorme escala; las estimaciones de víctimas difieren y por eso no se fija aquí una cifra cerrada. Tras la independencia de 1960 llegaron la crisis congoleña, la dictadura de Mobutu y las guerras de 1996–2003, cuyas secuelas siguen activas sobre todo en el este.</p>"
        + callout(
            "Historia completa · con audio",
            "Reino de Kongo, Boma, colonización, independencia y situación actual, con fuentes y audio narrado: <a href=\"historia/\">leer y escuchar la historia de RD Congo →</a>. El contexto de ruta corresponde a Yema–Muanda–Boma–Matadi–Lufu; Kinshasa es un ramal secundario.",
        ),
    )
    data.update(
        revision="15 sep 2026",
        verificado=True,
        hero_img="https://commons.wikimedia.org/wiki/Special:FilePath/Matadi%20Bridge%20DR%20Congo.jpg?width=1200",
        hero_credit="Puente y ciudad de Matadi · Χρίστος Ιμμανοελ · CC BY-SA 4.0",
        chips=[
            ["BAJADA", "Yema → Muanda → Boma → Matadi → Songololo → Lufu"],
            ["SUBIDA", "Lufu → Songololo → Matadi → Boma → Muanda → Yema"],
            ["CRUCE PRINCIPAL", "Dos fronteras terrestres · sin ferry"],
            ["ALTERNATIVA", "Kinshasa y ferry a Brazzaville · secundaria y apagada"],
            ["VISADO", "Solicitud física en Madrid · entradas múltiples o dos visados"],
            ["CARRETERA CLAVE", "Muanda–Yema · obras y drenaje; revalidar tras lluvia"],
            ["AGUA", "Muanda, Boma y Matadi: recarga pactada, ningún grifo público supuesto"],
            ["RIESGO", "Kongo Central no es el frente oriental, pero MAEC desaconseja viajar por carretera"],
        ],
        notice=(
            "Tránsito principal rediseñado íntegramente por Kongo Central: Yema–Muanda–Boma–Matadi–Lufu. "
            "Revisar visado, dos importaciones temporales, seguros, carretera Muanda–Yema y seguridad de Cabinda "
            "antes de cada paso. Kinshasa queda como ramal secundario."
        ),
        logistics=[
            {
                "name": "Frontera principal · Yema (entrada bajada desde Cabinda)",
                "cat": "Frontera", "lat": -5.74183, "lon": 12.29559,
                "info": "Pin de la frontera de Yema, no del centro de Muanda. ACP documenta su puesto sanitario y ANTT la actividad transfronteriza en 2026. Referencia horaria SADC 08:00–17:00; confirmar 72 h, especialmente tras lluvias.",
            },
            {
                "name": "Frontera principal · Lufu (salida bajada hacia Luvo, Angola)",
                "cat": "Frontera", "lat": -5.8431676, "lon": 14.0788529,
                "info": "Puesto terrestre real al sur de Songololo. Confirmar horario, salida de la importación temporal congoleña y nueva entrada del vehículo en Angola continental.",
            },
            {
                "name": "Frontera principal · Lufu (entrada subida desde Luvo, Angola)",
                "cat": "Frontera", "lat": -5.8431676, "lon": 14.0788529,
                "info": "Segundo ingreso en RD Congo. Requiere visado válido, seguro local y documento temporal del vehículo de nueva entrada.",
            },
            {
                "name": "Frontera principal · Yema (salida subida hacia Cabinda)",
                "cat": "Frontera", "lat": -5.74183, "lon": 12.29559,
                "info": "Salida hacia Cabinda por la carretera Muanda–Yema. Comprobar puentes, lluvia y permiso de entrada angoleño antes de dejar Muanda.",
            },
            {
                "name": "Alternativa secundaria · Beach Ngobila / ferry a Brazzaville",
                "cat": "Frontera", "lat": -4.2973574, "lon": 15.3195722,
                "info": "Cruce fluvial mantenido como contingencia. No forma parte del corredor previsto; vehículo y pasajeros se tramitan por separado y no existe puente.",
            },
            {
                "name": "Embajada de España en Kinshasa",
                "cat": "Consular", "lat": -4.3066182, "lon": 15.2769638,
                "info": "Bd. Colonel Tshatshi 37, Gombe. Emergencia consular +243 819 500 289. Está fuera del corredor principal: el contacto se realiza a distancia salvo emergencia que justifique el ramal a Kinshasa.",
            },
            {
                "name": "Hôpital de Kinkanda · Matadi",
                "cat": "Hospital", "lat": -5.8359027, "lon": 13.4458895,
                "info": "Pin del hospital real de Kinkanda. Referencia sanitaria del eje, con capacidad limitada frente a una evacuación internacional.",
            },
            {
                "name": "IME Kimpese",
                "cat": "Hospital", "lat": -5.5552303, "lon": 14.4618538,
                "info": "Referencia hospitalaria del corredor N1 al este de Songololo. El pin coincide con el recinto; confirmar atención y seguro.",
            },
            {
                "name": "Muanda · zona urbana de servicios",
                "cat": "Servicios", "lat": -5.9282219, "lon": 12.378028,
                "info": "Referencia urbana, no un surtidor, taller o grifo. Concertar base vigilada, combustible y recarga de agua de servicio antes de Yema.",
            },
            {
                "name": "Boma · zona urbana de servicios",
                "cat": "Servicios", "lat": -5.8594059, "lon": 13.0559152,
                "info": "Referencia urbana. Parada histórica y posible respaldo de alojamiento, combustible y agua solo tras confirmación concreta.",
            },
            {
                "name": "Matadi · zona urbana de servicios",
                "cat": "Servicios", "lat": -5.8249588, "lon": 13.4342982,
                "info": "Referencia del eje junto al puente, no una instalación de agua. Principal base de talleres, banco, hospital y suministro del tránsito por Kongo Central.",
            },
        ],
    )

    summary = (
        "<p>RD Congo deja de recorrerse desde Kinshasa. La ruta principal entra desde Cabinda por <strong>Yema</strong>, "
        "pasa por Muanda, Boma y Matadi y sale a Angola continental por <strong>Lufu/Luvo</strong>. En la subida se "
        "repite en sentido contrario. Así se evita la barcaza de vehículos y el despacho del ferry, pero aparecen dos "
        "puntos críticos nuevos: la carretera Muanda–Yema y la seguridad del tránsito por Cabinda.</p>"
        + callout(
            "Yema existe y está activo",
            "La inauguración oficial del puesto sanitario en 2025 y el inicio de actividad transfronteriza de ANTT en 2026 confirman el paso. No prueban por sí solos que cada trámite de un turismo extranjero esté resuelto: eso se valida por escrito.",
            "ok",
        )
        + callout(
            "Carretera en obras",
            "La reconstrucción de los 23,8 km Muanda–Yema empezó en septiembre de 2025; lluvias derribaron puentes en febrero de 2026. Informaciones de agosto la daban transitable, pero con obra y drenaje pendientes. Revalidar después de cada episodio de lluvia.",
            "warn",
        )
        + table(
            ("Tema", "Decisión"),
            [
                ("Corredor", "Yema–Muanda–Boma–Matadi–Lufu, en ambos sentidos."),
                ("Kinshasa", "Solo ramal cultural, consular o de contingencia; nunca paso obligatorio."),
                ("Ferry", "Secundario y apagado por defecto en el mapa."),
                ("Visado", "Físico en Madrid; validez y número de entradas deben cubrir dos cruces."),
                ("Tiempo", "Mínimo 2–3 días por sentido, sin conducir de noche y con día colchón."),
            ],
        )
    )

    route = (
        "<p>Todo el itinerario principal queda en <strong>Kongo Central</strong>. Las distancias son moderadas, pero no se convierten en jornadas rápidas por controles, camiones, lluvia y dos aduanas muy próximas.</p>"
        + table(
            ("Etapa", "Recorrido", "Plan realista"),
            [
                ("Bajada 1", "Yema → Muanda", "23,8 km en reconstrucción; hacer el cruce temprano y dormir en Muanda si se retrasa."),
                ("Bajada 2", "Muanda → Boma → Matadi", "Eje costero y puente; una jornada con paradas, sin fotografiar infraestructura."),
                ("Bajada 3", "Matadi → Songololo → Lufu", "Salir con luz; frontera a Angola continental y posible noche adicional."),
                ("Subida 1", "Lufu → Songololo → Matadi", "Nueva importación temporal y seguro local."),
                ("Subida 2", "Matadi → Boma → Muanda", "Reponer, comprobar Yema y cerrar contacto de Cabinda."),
                ("Subida 3", "Muanda → Yema", "Solo con carretera confirmada y llegada al puesto con horas de margen."),
            ],
            "num",
        )
        + ticks([
            "Matadi es el nodo logístico; Boma y Muanda son paradas principales, no excursiones desde Kinshasa.",
            "El puente de Matadi, puerto, Banana y las instalaciones petroleras son sensibles: no detenerse para fotos ni usar dron.",
            "El ramal Matadi–Kimpese–Kisantu–Kinshasa conserva sus PDIs, pero se etiqueta expresamente como secundario.",
            "No fijar una hora de llegada con datos de navegador: sumar frontera, controles y estado de puentes.",
        ])
    )

    water = (
        "<h3>Recarga para ducha y lavado</h3>"
        + callout(
            "No hay grifos públicos confirmados",
            "Los pines de Muanda, Boma y Matadi son zonas logísticas. Solo se convierten en punto de recarga cuando un establecimiento concreto autoriza el llenado y confirma que hay agua ese día.",
            "warn",
        )
        + ticks([
            "Muanda: recarga completa antes de Yema en ambos sentidos. Buscar hotel o misión con patio, manguera y vigilancia; registrar nombre y contacto.",
            "Matadi: principal respaldo del eje. Llenar a través de alojamiento o taller de confianza, usando prefiltro si el agua tiene sedimento.",
            "Boma: respaldo, no garantía. Preguntar antes y no bloquear el viaje esperando una fuente que solo figura en reseñas antiguas.",
            "Separar agua potable sellada del depósito de servicio. Ningún agua de red o pozo se bebe sin tratamiento completo.",
            "Transportar reserva de dos días desde Cabinda/Muanda para absorber cierres de Yema, averías o barro.",
        ])
        + "<h3>Combustible</h3>"
        + ticks([
            "Llenar en Muanda y Matadi en estaciones formales; repostar de nuevo antes de Lufu aunque la distancia sea corta.",
            "No usar el centroide de una ciudad como prueba de surtidor abierto. Confirmar estación y disponibilidad el mismo día.",
            "Billetes pequeños, filtro para trasvase y autonomía suficiente para volver a la última ciudad si una frontera cierra.",
        ])
    )

    borders = (
        "<h3>Visado</h3>"
        + ticks([
            "Desde el 28 de julio de 2025, la Embajada de RD Congo en Madrid exige solicitud física; indica 14 días laborables para extranjeros. Para residentes en España, el visado volante o en llegada está prohibido.",
            "Tarifas oficiales publicadas: 1 mes múltiple 130 €, 3 meses múltiple 225 € y 6 meses múltiple 320 €. Elegir la validez que cubra las dos fechas; si la separación excede lo emitible, hacen falta dos visados.",
            "El visado no garantiza la entrada. Llevar itinerario, alojamientos, medios, fiebre amarilla, copias y contactos del corredor terrestre.",
        ])
        + "<h3>Fronteras y vehículo</h3>"
        + table(
            ("Función", "Paso", "Comprobación"),
            [
                ("Entrada bajada", "Yema desde Cabinda", "Activo; horas de referencia 08:00–17:00. Confirmar turismo, aduana y carretera."),
                ("Salida bajada", "Lufu hacia Luvo", "Cerrar importación temporal y seguro congoleño antes de entrar de nuevo en Angola."),
                ("Entrada subida", "Lufu desde Luvo", "Nueva entrada: visado, seguro y documento del coche otra vez."),
                ("Salida subida", "Yema hacia Cabinda", "No dejar Muanda sin confirmar apertura de Yema y seguridad hasta Cabinda ciudad."),
                ("Alternativa", "Beach Ngobila / Kinshasa", "Ferry secundario; no es parte del plan ni de los tiempos base."),
            ],
        )
        + ticks([
            "Confirmar con DGDA si se usa CPD, laissez-passer o ambos en Yema y Lufu; no se ha localizado una norma pública suficiente para afirmarlo.",
            "RD Congo no queda cubierta automáticamente por seguros regionales de África occidental o CEMAC. Contratar y conservar comprobante del seguro local en cada entrada.",
            "Permiso internacional, autorización del titular, originales bajo control y varias copias. Exigir recibo de cada tasa oficial.",
            "MAEC advierte de extorsiones en pasos con Angola: protocolo calmado, francés, nada de pagos sin recibo y contacto de apoyo disponible.",
        ])
    )

    drones = (
        callout(
            "No volar: riesgo real de detención",
            "No se ha identificado un procedimiento turístico civil simple y estable. El corredor principal contiene fronteras, puerto, puente e instalaciones petroleras: el dron permanece embalado y se declara si lo exige Aduanas.",
            "bad",
        )
        + ticks([
            "No sacar ni volar el dron en ningún punto de RD Congo. El riesgo operativo es detención o acusación de espionaje, no solo una multa.",
            "Puntos especialmente sensibles del trazado principal: Yema, Lufu, puente y puerto de Matadi, Muanda, Banana e instalaciones petroleras. Kinshasa, Beach Ngobila e Inga también lo son si se activa un ramal.",
            "Declarar el equipo cuando corresponda y llevarlo embalado y accesible para una inspección; no intentar ocultarlo.",
            "La misma prudencia se aplica a la cámara: no fotografiar fronteras, puentes, puertos, edificios oficiales, policía o militares.",
        ])
    )

    starlink = (
        callout(
            "Servicio activo desde 2025, pero uso discreto",
            "La autorización comercial de Starlink no convierte cada despliegue en una acción prudente. Revisar disponibilidad y roaming antes del viaje y no montar una antena cerca de fronteras o infraestructura sensible.",
            "ok",
        )
        + ticks([
            "Tener el terminal activado y probado antes de entrar; usarlo en alojamiento seguro, nunca en Yema, Lufu, puerto, puente, control o cuneta visible.",
            "SIM local de Vodacom, Airtel u Orange como complemento. No se promete cobertura continua en Muanda–Yema ni en todo el tramo Boma–Matadi–Lufu: confirmarla localmente y prever huecos.",
            "Mantener check-in acordado para cada frontera y para la carretera Muanda–Yema. Si no hay señal, el convoy no se separa ni improvisa una pista.",
            "Revisar el mapa oficial, la legalidad del equipo y el régimen de itinerancia 30–60 días antes, porque pueden cambiar.",
        ])
    )

    dogs = (
        "<h3>Entrada y tránsito del perro</h3>"
        + ticks([
            "No hay una instrucción pública congoleña suficientemente clara para mascota terrestre: confirmar con la embajada certificado, rabia, microchip y cualquier permiso antes de ambos ingresos.",
            "Los certificados de vigencia corta deberán rehacerse antes de la subida. Guardar originales y copias junto al expediente de fiebre amarilla de los viajeros.",
            "Muanda, Boma y Matadi: correa, evitar perros locales, calor y tráfico. Alojamiento con patio cerrado confirmado previamente.",
            "Parque Marino de los Manglares: no asumir admisión; plan de turnos o cuidador. El perro nunca va en una piragua o zona de fauna sin permiso expreso.",
            "Los PDIs de bonobos y fauna de Kinshasa son secundarios y se consideran incompatibles con el perro salvo autorización escrita.",
        ])
        + "<h3>Salud humana</h3>"
        + ticks([
            "Fiebre amarilla obligatoria; paludismo, cólera y mpox requieren revisión sanitaria actualizada.",
            "Seguro con evacuación que cubra expresamente RD Congo y tránsito por carretera; no asumir que Kongo Central está incluido.",
            "Matadi y Kimpese son referencias del eje, pero una urgencia compleja puede exigir evacuación internacional.",
        ])
    )

    security = (
        "<p>Kongo Central está lejos del frente oriental, pero eso no lo convierte en una ruta de precaución normal. El MAEC desaconseja los desplazamientos por carretera en el país, cita extorsiones en la frontera angoleña y clasifica Kongo Central con riesgo intermedio.</p>"
        + ticks([
            "No conducir de noche, no acampar libre y mantener los dos vehículos juntos. Base vigilada en Muanda, Boma y Matadi.",
            "Revisar protestas y avisos el día anterior, aunque Kinshasa quede fuera del itinerario: una crisis nacional afecta controles y fronteras.",
            "No fotografiar ni volar dron en Yema, Lufu, puentes, puertos, instalaciones petroleras, policía o ejército.",
            "La carretera Muanda–Yema se valida después de lluvias; si hay puente cortado, no se intenta una variante por pista sin apoyo oficial.",
            "Avisar a la Embajada de España de las fechas previstas y mantener check-in del convoy. Un contacto local con experiencia en Kongo Central es una condición de salida, no un lujo.",
        ])
    )

    decisions = (
        table(
            ("Cierre pendiente", "Evidencia exigida"),
            [
                ("Yema", "Horario, turismos extranjeros, inmigración, DGDA, seguro y estado de la vía."),
                ("Muanda–Yema", "Confirmación posterior a la última lluvia y puentes abiertos; no solo una noticia de agosto de 2026."),
                ("Visado", "Sello físico de entradas múltiples y fechas que cubran bajada y subida, o dos visados."),
                ("Vehículo", "Documento temporal exacto y coste escrito en Yema y Lufu."),
                ("Agua", "Establecimiento y persona que autoriza en Muanda y Matadi; sin ello no hay punto verificado."),
                ("Cabinda", "Seguro y seguridad confirmados antes de salir por Yema."),
            ],
        )
        + callout("No confundir", "Que Yema esté abierto no demuestra que la carretera esté bien ni que Cabinda sea segura. Son tres validaciones separadas.", "warn")
    )

    experiences = (
        "<p>La experiencia útil del nuevo eje es limitada; por eso se separa evidencia oficial de relatos.</p>"
        + ticks([
            "ACP confirma infraestructura sanitaria en Yema y ANTT confirma actividad transfronteriza: el puesto no es una hipótesis cartográfica.",
            "ACGT documenta una obra de 23,8 km entre Muanda y Yema; el colapso de puentes en febrero de 2026 demuestra que la meteorología puede cambiar la ruta en horas.",
            "Relatos terrestres de 2025 coinciden en que Cabinda–Pointe-Noire es posible pero lento. No aportan garantía para 2027 ni sustituyen el aviso de seguridad.",
            "Las historias del ferry se conservan para el plan B y explican por qué se abandona como ruta principal, no para inflar el presupuesto actual.",
        ])
    )

    existing_post = {item[0]: item for item in data["custom_sections_post"]}
    data["custom_sections"] = [
        section("resumen", "Resumen operativo", summary),
        history,
        section("ruta", "Ruta propuesta", route),
        section("agua-combustible", "Agua y combustible", water),
    ]
    data["custom_sections_post"] = [
        section("fronteras", "Visado, fronteras y vehículos", borders),
        section("drones", "Drones", drones),
        section("starlink", "Starlink", starlink),
        section("perro", "Perro y salud", dogs),
        section("seguridad", "Seguridad y comunicaciones", security),
        section("gpx", "Validación y decisiones", decisions),
        section("experiencias", "Experiencias de otros overlanders", experiences),
    ]
    data["sources"] = [
        ["Embajada de RD Congo en Madrid · visados, plazos y tarifas", OFFICIAL["drc_visa"]],
        ["MAEC España · recomendaciones de viaje de RD Congo", OFFICIAL["drc_maec"]],
        ["ACP · puesto de control sanitario de Yema", OFFICIAL["drc_yema"]],
        ["ACGT · obras de la carretera Muanda–Yema (23,8 km)", OFFICIAL["drc_road"]],
        ["Radio Okapi · colapso de puentes en Muanda, febrero de 2026", OFFICIAL["drc_bridge"]],
        ["ANTT Angola · actividad transfronteriza en Yema y Massabi", OFFICIAL["angola_border"]],
        ["SADC · directorio técnico de fronteras y horas de referencia", OFFICIAL["sadc_hours"]],
        ["FCDO · aviso de viaje de Angola/Cabinda", OFFICIAL["angola_fcdo"]],
    ]
    data["sources_note"] = "La ficha distingue puesto activo, carretera transitable y corredor seguro: ninguna de esas tres condiciones prueba automáticamente las otras dos."
    save(path, data)


def angola() -> None:
    path = "content/ficha/angola.json"
    data = load(path)
    data["historia_resumen"] = (
        "Angola se formó sobre sociedades y reinos como Kongo, Ndongo y Matamba, y quedó profundamente marcada por la trata atlántica y el colonialismo portugués. Cabinda tiene una trayectoria propia: tradiciones kongo y fiote, el Tratado de Simulambuco de 1885 y una integración territorial separada del resto del país. La independencia de 1975 desembocó en una guerra civil internacionalizada hasta 2002. Desde entonces, el petróleo financió la reconstrucción sin eliminar pobreza ni desigualdad; Cabinda sigue siendo esencial para la economía petrolera y políticamente sensible."
    )
    if not any(item[0].startswith("Cabinda") for item in data["historia_secciones"]):
        data["historia_secciones"].insert(
            2,
            [
                "Cabinda: Simulambuco y el enclave",
                "<p>Cabinda pertenece al espacio histórico kongo de la costa atlántica y conserva tradiciones identificadas por el gobierno provincial como macongo, mangoio y maloango, además del fiote y el kikongo. El <strong>Tratado de Simulambuco</strong>, firmado en 1885 entre representantes portugueses y autoridades locales, estableció un protectorado portugués; la fuente histórica oficial angoleña lo incorpora al proceso colonial. La posterior frontera del Congo Belga separó físicamente Cabinda del resto de Angola.</p><p>Tras la independencia de 1975, movimientos separatistas disputaron la integración de Cabinda en Angola. La producción petrolera reforzó su importancia económica y su sensibilidad política. El conflicto no se presenta como cerrado: los avisos consulares siguen señalando riesgo de ataques y secuestro fuera de Cabinda ciudad. Esa historia explica por qué el corredor se limita a Massabi–Cabinda ciudad–Yema, con apoyo local, y no trata el enclave como una simple prolongación de la costa.</p>",
            ],
        )
    if not any(url == OFFICIAL["angola_history"] for _, url in data["historia_fuentes"]):
        data["historia_fuentes"].extend([
            ["CIAM / Gobierno de Angola · historia de Angola y Tratado de Simulambuco", OFFICIAL["angola_history"]],
            ["Gobierno Provincial de Cabinda · perfil cultural y territorial", OFFICIAL["cabinda_profile"]],
        ])
    history = section(
        "historia",
        "Historia y contexto",
        "<p>Angola no tiene una sola historia regional: Kongo, Ndongo, Matamba y los estados de la meseta precedieron a la ocupación portuguesa. La trata atlántica, la guerra de independencia y el conflicto civil de 1975–2002 marcaron todo el territorio. Cabinda exige además una lectura propia: el Tratado de Simulambuco de 1885, su separación geográfica, el separatismo posterior a 1975 y el peso del petróleo explican por qué no es un simple tramo administrativo de Angola.</p>"
        + callout(
            "Historia completa · con audio",
            "Reinos, colonización, Simulambuco, independencia, guerra civil y situación actual, con fuentes y audio narrado: <a href=\"historia/\">leer y escuchar la historia de Angola →</a>.",
        ),
    )
    data.update(
        revision="15 sep 2026",
        verificado=True,
        chips=[
            ["CABINDA BAJADA", "Massabi → Cabinda ciudad → Yema → RD Congo"],
            ["ANGOLA CONTINENTAL", "Luvo/Lufu → Luanda → altiplano → sur y bloque austral"],
            ["CABINDA SUBIDA", "Yema → Cabinda ciudad → Massabi → Pointe-Noire"],
            ["VISADO", "Españoles exentos para turismo: 30 días por entrada, máximo 90/año"],
            ["TASAS FRONTERA", "Referencia oficial: 43.236,78 AOA por turismo ligero y entrada"],
            ["PDIs", "23 puntos · nuevo PDI exacto de Cabinda con tres fotos"],
            ["AGUA", "Cabinda ciudad es recarga pactada; no se promete grifo público"],
            ["RIESGO CABINDA", "Aviso reforzado fuera de la ciudad; ejecutar solo con validación actual"],
        ],
        notice=(
            "Angola se entra y sale cuatro veces en el conjunto del viaje: Cabinda y territorio continental, bajada y subida. "
            "La exención de visado no elimina los trámites del vehículo ni el riesgo específico de Cabinda. "
            "Revalidar tasas, seguro y seguridad antes de cada entrada."
        ),
    )

    logistics = [item for item in data["logistics"] if "Cabinda" not in item.get("name", "") and "Massabi" not in item.get("name", "") and "Yema" not in item.get("name", "")]
    logistics[:0] = [
        {
            "name": "Frontera principal · Massabi (entrada bajada a Cabinda)",
            "cat": "Frontera", "lat": -4.98944, "lon": 12.05712,
            "info": "Posto Fiscal de Massabi. Entrada desde Congo-Brazzaville; actividad fronteriza confirmada por ANTT en 2026. Referencia horaria 08:00–17:00, a reconfirmar 72 h.",
        },
        {
            "name": "Frontera principal · Yema (salida bajada a RD Congo)",
            "cat": "Frontera", "lat": -5.74183, "lon": 12.29559,
            "info": "Puesto real al sur de Cabinda. Comprobar carretera, horario y cierre de importación temporal antes de salir de Angola.",
        },
        {
            "name": "Frontera principal · Yema (entrada subida a Cabinda)",
            "cat": "Frontera", "lat": -5.74183, "lon": 12.29559,
            "info": "Nueva entrada angoleña desde RD Congo. Presupuestar tasa de entrada del vehículo y no circular hacia Cabinda ciudad sin confirmación de seguridad.",
        },
        {
            "name": "Frontera principal · Massabi (salida subida a Congo-Brazzaville)",
            "cat": "Frontera", "lat": -4.98944, "lon": 12.05712,
            "info": "Salida terrestre hacia Pointe-Noire. Confirmar apertura y RN4 antes de dejar Cabinda ciudad.",
        },
        {
            "name": "Cabinda ciudad · zona urbana de servicios",
            "cat": "Servicios", "lat": -5.5576435, "lon": 12.1919468,
            "info": "Referencia urbana, no surtidor ni grifo. Único punto lógico para alojamiento vigilado, combustible y recarga pactada de agua entre Massabi y Yema.",
        },
    ]
    data["logistics"] = logistics

    summary = (
        "<p>La ficha incorpora ahora la provincia separada de <strong>Cabinda</strong> como pieza del corredor principal. "
        "En la bajada se entra desde Massabi, se pasa por Cabinda ciudad y se sale por Yema hacia Muanda. Después de "
        "Kongo Central se entra en Angola continental por Luvo/Lufu. La subida repite los dos pasos en sentido inverso.</p>"
        + callout(
            "Ventaja y coste",
            "Este trazado evita el ferry Brazzaville–Kinshasa, pero multiplica las entradas angoleñas y atraviesa una provincia con advertencia de seguridad reforzada. No se presenta como ruta fácil ni barata hasta recibir confirmación local.",
            "warn",
        )
        + table(
            ("Tema", "Consecuencia"),
            [
                ("Entradas Angola", "Cabinda y continente en bajada, continente y Cabinda en subida: cuatro eventos fronterizos."),
                ("Exención", "Pasaporte español: hasta 30 días por entrada y 90 días acumulados al año, según norma oficial."),
                ("Vehículo", "La tasa oficial de referencia se aplica al turismo ligero al entrar; presupuestar cada evento hasta aclaración escrita."),
                ("Cabinda", "Solo de día, alojamiento vigilado y sin excursiones remotas."),
                ("Agua", "Recarga completa pactada en Cabinda ciudad; dos días de reserva."),
            ],
        )
    )

    route = (
        "<h3>Tránsito de Cabinda</h3>"
        + table(
            ("Sentido", "Recorrido", "Condición"),
            [
                ("Bajada", "Massabi → Cabinda ciudad → Yema", "Llegar a Massabi a primera hora; dormir en ciudad si no se completa Yema con luz."),
                ("Subida", "Yema → Cabinda ciudad → Massabi", "No salir de Muanda sin confirmar ambos pasos y el corredor hasta alojamiento."),
            ],
            "num",
        )
        + ticks([
            "No enlazar gráficamente Yema con Luvo: entre ambos hay territorio de RD Congo. El mapa usa segmentos separados y correctos.",
            "Cabinda ciudad es parada operativa y PDI histórico; no se añaden playas, bosque de Maiombe ni desvíos a zonas remotas por el nivel de riesgo.",
            "Massabi y Yema se planifican con la referencia técnica 08:00–17:00, pero se valida el horario real 72 h antes.",
            "El resto de la gran ruta angoleña se mantiene: entrada continental de bajada por Luvo/Lufu, entrada continental de subida por Santa Clara/Oshikango y salida posterior por Luvo/Lufu.",
        ])
        + "<h3>Resto de Angola</h3><p>Luanda, Malanje, el altiplano, Namibe, Iona y los corredores del bloque austral mantienen sus rutas y PDIs ya auditados. La modificación de Cabinda no autoriza a recortar sus márgenes de combustible, agua o cuidado del perro.</p>"
    )

    water = (
        "<h3>Recarga para ducha y lavado</h3>"
        + callout(
            "Cabinda no tiene un grifo público verificado",
            "El marcador de la ciudad es una zona de búsqueda. Hay que cerrar alojamiento o taller con patio, manguera, vigilancia y permiso de llenado; la disponibilidad urbana no equivale a acceso público.",
            "warn",
        )
        + ticks([
            "Bajada: llegar desde Pointe-Noire con los depósitos llenos; completar en Cabinda ciudad solo si el establecimiento lo confirma y salir a Yema con reserva de dos días.",
            "Subida: recargar primero en Muanda y usar Cabinda ciudad como respaldo antes de Massabi.",
            "En Angola continental, mantener la estrategia ya auditada: recarga pactada en alojamientos y talleres, nunca en un punto genérico del mapa.",
            "Agua potable siempre separada y sellada. Para agua de red o pozo destinada a ducha/lavado, prefiltro; para beber, tratamiento completo.",
        ])
        + "<h3>Combustible</h3>"
        + ticks([
            "Llenar en Pointe-Noire antes de Massabi y en Cabinda ciudad antes de Yema; no depender de los puestos fronterizos.",
            "Llenar en Muanda antes de la subida por Yema. Conservar margen para regresar si el paso cierra.",
            "Presupuestar combustible y tasas por separado: un pago fronterizo no incluye seguro, combustible ni gestor.",
        ])
    )

    borders = (
        "<h3>Entrada de personas</h3>"
        + ticks([
            "España figura entre los países exentos de visado turístico: hasta 30 días por entrada y 90 días por año. Pasaporte con más de seis meses y certificado de fiebre amarilla cuando sea exigible.",
            "La exención permite las entradas sucesivas solo dentro de esos límites; conservar sellos legibles y contar días acumulados.",
        ])
        + "<h3>Vehículo y tasas</h3>"
        + callout(
            "Referencia oficial desde 1 julio 2025",
            "Para vehículo ligero que entra por turismo: pase fronterizo 6.000 AOA (vigencia publicada de 30 días) más autorización de transporte turístico 37.236,78 AOA; total de referencia 43.236,78 AOA, aproximadamente 47 USD, por entrada.",
            "ok",
        )
        + ticks([
            "El aviso oficial indica pago al entrar. Como la ruta genera cuatro entradas angoleñas, reservar hasta cuatro veces el total —172.947,12 AOA, unos 188 USD por vehículo— hasta que ANTT confirme por escrito si un pase de 30 días se reutiliza en una reentrada cercana.",
            "No confundir este cuadro de turismo ligero con tarifas de transporte comercial, mercancías o pasajeros.",
            "Confirmar CPD/importación temporal, seguro angoleño y documentos del conductor para Massabi, Yema y Luvo. Cada entrada abre un expediente nuevo salvo confirmación escrita en contrario.",
            "Exigir recibo oficial; no presentar la cifra en dólares como cambio fijo, porque la norma está denominada en AOA.",
        ])
        + table(
            ("Evento", "Paso"),
            [
                ("1 · entrada bajada", "Massabi → Cabinda"),
                ("2 · entrada bajada", "Lufu/Luvo → Angola continental"),
                ("3 · entrada subida", "Santa Clara/Oshikango → Angola continental"),
                ("4 · entrada subida", "Yema → Cabinda"),
            ],
        )
    )

    drones = (
        callout(
            "Autorización previa y zonas especialmente sensibles",
            "Angola exige autorización previa de INAVIC. Para este proyecto, el dron permanece embalado en Cabinda y no se vuela en ningún lugar sin permiso escrito y autorización específica del gestor del espacio.",
            "warn",
        )
        + ticks([
            "No volar ni exhibir el dron en Massabi, Yema, Cabinda ciudad, puerto, instalaciones petroleras, cuarteles o controles.",
            "También evitar Luanda, Lobito, presas, aeropuertos y parques nacionales salvo autorización escrita específica, además de la aeronáutica.",
            "Declarar el equipo cuando proceda y llevarlo embalado durante los cuatro eventos de entrada; una autorización de vuelo no elimina las reglas aduaneras ni locales.",
        ])
    )

    starlink = (
        callout(
            "No basar la ruta en Starlink",
            "La ficha conserva el estado no confirmado de servicio comercial a mediados de 2026. Revisar el mapa oficial 30–60 días antes; hasta entonces, planificar como si no estuviera disponible.",
            "warn",
        )
        + ticks([
            "SIM local de Unitel o Africell como conectividad principal, sin prometer cobertura continua en Cabinda, Moxico, Iona o pistas remotas.",
            "No desplegar antena en Massabi, Yema ni cerca de puerto, petróleo, fuerzas de seguridad o infraestructura sensible.",
            "El convoy mantiene check-in y contacto local para Cabinda; la ausencia de cobertura no autoriza a dividir vehículos ni buscar una pista alternativa.",
        ])
    )

    dogs = (
        "<h3>Cuatro entradas angoleñas con el perro</h3>"
        + callout(
            "No asumir que un certificado sirve para todo el viaje",
            "La bajada y la subida generan entradas separadas a Cabinda y a Angola continental. No se ha localizado una norma pública que confirme que un permiso veterinario cubra las cuatro; pedir respuesta escrita y prever certificados renovados.",
            "warn",
        )
        + ticks([
            "Llevar microchip, pasaporte UE, rabia en vigor, titulación serológica para el regreso y certificado veterinario internacional reciente. Confirmar con la autoridad angoleña el plazo y permiso exactos.",
            "Preparar un juego de copias para Massabi, Luvo y Yema y conservar siempre los originales. Los sellos del vehículo y los del perro son expedientes distintos.",
            "En Cabinda ciudad: alojamiento con admisión confirmada, patio cerrado, profilaxis antiparasitaria y cero paseos remotos. En frontera, el perro permanece controlado dentro del coche salvo instrucción oficial.",
        ])
        + callout(
            "Todo lo del perro, en su propia sección",
            "Requisitos comunes, salud en ruta y regreso a la UE: <a href=\"../../perro/\">ver la sección El perro →</a> y <a href=\"../../documentacion/#perro\">Documentación general</a>.",
        )
        + "<h3>Decisión por zona</h3>"
        + table(
            ("Zona", "Estado", "Plan operativo"),
            [
                ("Cabinda y sus dos fronteras", '<span class="st st-amber">con condiciones</span>', "Alojamiento y trámite confirmados; correa, vigilancia y sin playas o bosque remoto."),
                ("Iona, Kissama y Cangandala", '<span class="st st-red">tratar como prohibido</span>', "No entrar con el perro sin autorización escrita; turnos o cuidador fuera del parque."),
                ("Ciudades y costa", '<span class="st st-amber">confirmar cada lugar</span>', "Calor, tráfico, fauna y admisión del alojamiento; nunca dejarlo al sol en el vehículo."),
                ("Miradores, cascadas y arte rupestre", '<span class="st st-green">correa corta</span>', "Confirmar gestor; bordes, roca mojada, calor y encuentros con fauna."),
                ("Baía dos Tigres y Foz do Cunene", '<span class="st st-amber">precaución extrema</span>', "Sombra y agua propias; lejos del río y sin excursión si compromete la seguridad del animal."),
            ],
        )
        + "<h3>Salud humana</h3>"
        + ticks([
            "Certificado de fiebre amarilla y revisión de paludismo con Sanidad Exterior; actualizar alertas de mpox y brotes antes de Cabinda.",
            "Seguro con evacuación que cubra expresamente Cabinda y todos los pasos terrestres. Luanda y Lubango son referencias; en tramos remotos la evacuación domina el plan.",
        ])
    )

    security = (
        "<h3>Cabinda</h3>"
        + callout(
            "Riesgo superior al resto del corredor",
            "MAEC pide especial precaución en Cabinda y el FCDO desaconseja todo viaje no esencial en la provincia salvo Cabinda ciudad por ataques separatistas y riesgo de secuestro. Las dos carreteras fronterizas quedan fuera de la excepción urbana.",
            "danger",
        )
        + ticks([
            "La preferencia por esta ruta no anula el aviso: solo se ejecuta con seguro válido, información consular del momento y apoyo local que confirme Massabi–Cabinda–Yema.",
            "Circular de día, dos vehículos juntos, puertas cerradas, sin acampada libre y con alojamiento vigilado reservado en Cabinda ciudad.",
            "No buscar atajos, selva de Maiombe, playas aisladas ni pistas alternativas si un control o puente bloquea el eje.",
            "No fotografiar fronteras, fuerzas de seguridad, puerto, instalaciones petroleras ni infraestructura estratégica; dron embalado.",
            "Si el riesgo empeora o el seguro excluye Cabinda, la ruta principal queda suspendida y se reevalúa el ferry secundario o el calendario. No se improvisa.",
        ])
        + "<h3>Angola continental</h3><p>Se mantienen las cautelas ya auditadas: conducción diurna, minas fuera de rutas conocidas, combustible y agua planificados, y revisión sanitaria por el aumento de mpox comunicado en Cabinda.</p>"
    )

    decisions = (
        table(
            ("Cierre pendiente", "Evidencia exigida"),
            [
                ("Seguridad Cabinda", "MAEC/FCDO actualizados, seguro que no excluya la provincia y contacto local del día."),
                ("Tasas", "Confirmar vigencia 2027 y si el pase de 30 días se reutiliza tras salir y volver a entrar."),
                ("Importación temporal", "Documento exacto en Massabi, Yema y Luvo; CPD sellado o permiso alternativo."),
                ("Agua", "Alojamiento/taller concreto en Cabinda con permiso de manguera y fecha."),
                ("Carreteras", "RN4 desde Pointe-Noire y Muanda–Yema tras la última lluvia."),
            ],
        )
        + callout("Punto de no salida", "Si falta cualquiera de las tres piezas —seguridad, paso abierto o carretera transitable— el convoy no abandona la última base urbana.", "warn")
    )

    experiences = (
        "<p>La evidencia reciente confirma el eje, pero no rebaja el riesgo.</p>"
        + ticks([
            "ANTT informó en julio de 2026 del inicio de actividad transfronteriza en Yema y de una visita técnica a la aduana de Massabi.",
            "Relatos de carretera de 2025 muestran que el trayecto Cabinda–Pointe-Noire se ha realizado por tierra, con barro y muchas horas. Solo orientan sobre dificultad.",
            "Los avisos consulares actuales pesan más que un relato individual: la ausencia de incidentes de un viajero no demuestra seguridad para el siguiente.",
        ])
    )

    existing_post = {item[0]: item for item in data["custom_sections_post"]}
    data["custom_sections"] = [
        section("resumen", "Resumen operativo", summary),
        history,
        section("ruta", "Ruta propuesta", route),
        section("agua-combustible", "Agua y combustible", water),
    ]
    data["custom_sections_post"] = [
        section("fronteras", "Visado, fronteras y vehículos", borders),
        section("drones", "Drones", drones),
        section("starlink", "Starlink", starlink),
        section("perro", "Perro y salud", dogs),
        section("seguridad", "Seguridad y comunicaciones", security),
        section("gpx", "Validación y decisiones", decisions),
        section("experiencias", "Experiencias de otros overlanders", experiences),
    ]
    data["sources"] = [
        ["Gobierno de Angola · exención de visado de turismo para 98 países", OFFICIAL["angola_visa"]],
        ["ANTT Angola · tasas fronterizas aplicables desde julio de 2025", OFFICIAL["angola_fees"]],
        ["ANTT Angola · actividad transfronteriza de Yema y aduana de Massabi", OFFICIAL["angola_border"]],
        ["Gobierno Provincial de Cabinda · cooperación migratoria con Pointe-Noire", "https://cabinda.gov.ao/web/noticias/cabinda-e-ponta-negra-analisam-coopera%C3%A7%C3%A3o-migrat%C3%B3ria"],
        ["MAEC España · recomendaciones de viaje de Angola", OFFICIAL["angola_maec"]],
        ["FCDO · aviso de viaje de Angola/Cabinda", OFFICIAL["angola_fcdo"]],
        ["SADC · directorio técnico de fronteras y horas de referencia", OFFICIAL["sadc_hours"]],
        ["ACGT · obras de la carretera Muanda–Yema", OFFICIAL["drc_road"]],
    ]
    data["sources_note"] = "Cabinda se incorpora con una advertencia explícita: la existencia de los pasos y una ruta realizada por otros viajeros no equivale a seguridad garantizada."
    save(path, data)


def update_pois() -> None:
    congo_pois = load("content/pois/congo.json")
    for poi in congo_pois:
        if poi["n"] == 7:
            poi["desc"] = poi["desc"].replace(
                "y la gestión del ferry a Kinshasa.",
                "y la preparación del tramo RN1–RN4 hacia Pointe-Noire y Massabi. El ferry a Kinshasa queda como alternativa secundaria.",
            )
            poi["visit"]["access"] = "Base urbana principal antes de la RN1. Aparcamiento vigilado y salida diurna; el Beach solo se visita si se activa la alternativa del ferry."
            poi["visit"]["why"] = "La basílica es el hito arquitectónico de la capital y Brazzaville es la base principal antes del corredor RN1–RN4 hacia Massabi."
            poi["visit"]["when"] = "Visita con luz; reservar días laborables para bancos, talleres y preparativos de la carretera del sur."
            poi["visit"]["skip"] = "No ampliar la estancia si los vehículos, Pointe-Noire y Massabi ya están coordinados; la logística prima sobre acumular paradas."
        elif poi["n"] == 11:
            poi["desc"] = poi["desc"].replace("mitad del largo desvío occidental", "mitad del corredor principal hacia Pointe-Noire y Massabi")
            poi["visit"]["why"] = "Es el descanso y respaldo mecánico natural entre Brazzaville y Pointe-Noire dentro de la ruta principal."
        elif poi["n"] == 12:
            poi["desc"] = poi["desc"].replace(
                "La RN1 desde Brazzaville supone unos 510 km por sentido, por lo que solo compensa por costa, Conkouati o una necesidad mecánica confirmada.",
                "Ahora es la última base logística obligatoria antes de la RN4 y la frontera de Massabi: aquí se cierran combustible, agua, efectivo, alojamiento y estado de carretera.",
            )
            poi["visit"]["why"] = "Es la capital económica del país y la base imprescindible antes del cruce terrestre a Cabinda."
            poi["visit"]["access"] = "Llegar por RN1 y reservar aparcamiento vigilado. Antes de salir, confirmar la RN4, Massabi y el tránsito de Cabinda; conducir solo de día."
            poi["visit"]["skip"] = "No se omite como base logística; la visita costera sí se reduce si la frontera exige salir temprano."
        elif poi["n"] == 13:
            note = "Es una excursión desde el corredor, no una razón para retrasar Massabi."
            while poi["visit"]["access"].count(note) > 1:
                poi["visit"]["access"] = poi["visit"]["access"].replace(" " + note, "", 1)
            if note not in poi["visit"]["access"]:
                poi["visit"]["access"] += " " + note
        elif poi["n"] == 14:
            poi["visit"]["skip"] = "Descartarlo si consume el margen de Massabi, si la RN5 está mala o si el parque no confirma por escrito acceso y alojamiento."
    save("content/pois/congo.json", congo_pois)

    drc_pois = load("content/pois/rd-congo.json")
    main = {6, 7, 8}
    for poi in drc_pois:
        if poi["n"] == 1:
            poi["name"] = "Kinshasa · Gombe (ramal secundario)"
            poi["desc"] = (
                "Gombe concentra embajadas, bancos, supermercados y servicios útiles de Kinshasa. "
                "El pin coincide con Central Station Square, una referencia pública real, pero no implica hotel ni aparcamiento. "
                "Esta parada solo se activa por una necesidad consular, cultural o por el plan alternativo del ferry; no forma parte del corredor principal Yema–Muanda–Boma–Matadi–Lufu. "
                "Si se usa, reservar estacionamiento vigilado, desplazarse con luz y asumir tráfico muy lento."
            )
            poi["visit"]["why"] = "Aporta la principal concentración de servicios y representaciones diplomáticas del país, pero solo para una contingencia que justifique el ramal."
            poi["visit"]["access"] = "Llegar por el ramal de la N1, nunca como desvío improvisado. Alojamiento y aparcamiento vigilado cerrados antes de entrar en la capital."
            poi["visit"]["when"] = "Días laborables y solo con luz; asignar margen completo al tráfico y a cualquier trámite concreto."
            poi["visit"]["skip"] = "Omitirlo en la ruta normal. Activarlo solo por necesidad consular, cultural prioritaria o plan alternativo documentado."
        if poi["n"] in main:
            if poi["n"] == 6:
                poi["desc"] = poi["desc"].replace("antes de Angola", "entre Yema y Lufu, dentro del nuevo corredor principal")
                poi["visit"]["why"] = "Es la base logística central del tránsito Yema–Lufu y el gran hito geográfico de Kongo Central."
            elif poi["n"] == 7:
                note = "Boma queda ahora sobre la ruta principal entre Muanda y Matadi, no como excursión desde Kinshasa."
                if note not in poi["desc"]:
                    poi["desc"] += " " + note
                poi["visit"]["why"] = "Aporta la parada histórica más fuerte del corredor principal sin exigir un desvío relevante."
            else:
                note = "Muanda pasa a ser la primera y última base urbana junto a Yema en la ruta principal."
                if note not in poi["desc"]:
                    poi["desc"] += " " + note
                poi["visit"]["access"] = "Coordinar el acceso con ICCN. Aparte de la visita, usar Muanda para confirmar la carretera de Yema, alojamiento vigilado, combustible y agua pactada."
        else:
            marker = " Este PDI pertenece al ramal secundario de Kinshasa y no al corredor principal Yema–Lufu."
            if marker.strip() not in poi["desc"]:
                poi["desc"] += marker
            poi["visit"]["skip"] = "Omitirlo salvo que se active expresamente el ramal secundario de Kinshasa y exista margen, seguridad y logística para hacerlo."
    save("content/pois/rd-congo.json", drc_pois)

    angola_pois = load("content/pois/angola.json")
    angola_visits = {
        6: {
            "why": "Es una pausa útil del altiplano y solo gana interés faunístico si un guía local fiable confirma ese día un sector seguro del río Kene.",
            "see": "Las fotos muestran Waku Kungo, que es el punto fijado. Los hipopótamos son una posibilidad fuera del pin, no un avistamiento prometido.",
            "access": "El pin está en Waku Kungo. La referencia habla de unos 30 km de pista sin señalizar: no salir de la localidad sin guía, coordenada de encuentro y retorno con luz.",
            "when": "Con pista seca, guía disponible y varias horas de luz; una parada urbana basta si no se confirma el río.",
            "skip": "Descartarlo sin guía, con barro o si alguien propone acercarse a pie a la orilla; perro siempre lejos del agua.",
        },
        7: {
            "why": "Permite conocer una institución tradicional ovimbundu viva y aporta contexto histórico al altiplano, siempre como visita respetuosa y concertada.",
            "see": "El recinto de Ombala Mbalundu y, si las autoridades lo autorizan, los espacios históricos y ceremoniales que estén abiertos ese día.",
            "access": "El pin coincide con la ficha real del conjunto. Presentarse, pedir permiso y confirmar qué se visita y fotografía; una foto disponible no demuestra apertura pública permanente.",
            "when": "De día y con contacto local; reservar media jornada solo tras confirmar recepción.",
            "skip": "Omitir si no hay autorización, si se celebra una ceremonia privada o si la visita exigiría fotografiar personas sin consentimiento.",
        },
        9: {
            "why": "No es una gran visita turística: es la última base fiable para preparar vehículos y autonomía antes del este remoto de Moxico.",
            "see": "Centro provincial, mercado y huella urbana de la guerra; las fotografías enseñan la ciudad real, no la pista de Cazombo.",
            "access": "Entrar con luz y cerrar alojamiento vigilado. Verificar por separado taller, combustible y agua: el pin urbano no garantiza ningún servicio concreto.",
            "when": "Día laborable, con una noche mínima para compras, revisión y descanso.",
            "skip": "No se omite como nodo logístico; sí se reduce el paseo urbano si la salida remota exige una ventana de tiempo o seguridad mejor.",
        },
        11: {
            "why": "Es un final de río y desierto excepcional, pero solo compensa como expedición autorizada y coordinada desde Iona, no como desvío espontáneo.",
            "see": "La desembocadura del Cunene, dunas y humedal costero. La única foto localizada corresponde al lugar; no se promete fauna.",
            "access": "Pista remota desde el entorno de Iona. Obtener del parque ruta, guía, permisos, mareas y punto seguro; no navegar al pin como si fuera una carretera.",
            "when": "Estación seca, convoy de dos 4x4, autonomía completa y parte meteorológico estable.",
            "skip": "Descartarlo sin guía del parque, con marea/oleaje adversos, falta de agua o cualquier duda de ruta. Perro lejos del río por cocodrilos.",
        },
        12: {
            "why": "El poblado abandonado entre mar y desierto es uno de los paisajes más singulares de Angola, reservado para un bloque 4x4 serio.",
            "see": "Ruinas de la antigua industria pesquera de Baía dos Tigres; las tres fotos son del asentamiento, no de una duna genérica.",
            "access": "El pin marca la isla, no un acceso rodado. Contratar guía experto desde Tômbwa, plan de mareas, recuperación, comunicación y al menos dos vehículos.",
            "when": "Solo con varios días secos, oleaje y marea estudiados y margen de dos a tres días.",
            "skip": "Renunciar si el guía no confirma el corredor, si falta un segundo 4x4 o si agua, combustible y recuperación no cubren ida, espera y regreso.",
        },
        15: {
            "why": "Es la base logística imprescindible del desierto de Namibe y una escala urbana agradable entre costa, Tundavala, Iona y Tômbwa.",
            "see": "La Marginal, la bahía y arquitectura del centro; las tres fotografías muestran Moçâmedes de forma reconocible.",
            "access": "Reservar patio vigilado y agrupar taller, combustible, compras y agua. Confirmar por separado cualquier excursión al desierto.",
            "when": "Día laborable y una noche antes de una pista remota; paseo a primera o última hora por el calor.",
            "skip": "No se omite como base; se puede reducir la visita urbana si el convoy ya está preparado y la ventana del desierto manda.",
        },
        18: {
            "why": "Combina una parada costera cómoda con patrimonio urbano y servicios, sin requerir una excursión organizada.",
            "see": "Praia Morena, iglesias y edificios cívicos del centro; las fotos corresponden a esos elementos de Benguela.",
            "access": "Elegir alojamiento con aparcamiento y recorrer el centro con luz. No usar la playa como lugar de pernocta sin permiso local.",
            "when": "Final de tarde y una noche si encaja entre Namibe y Lobito.",
            "skip": "Elegir Benguela o Lobito como base si el calendario aprieta; no es obligatorio dormir en ambas ciudades separadas por unos 30 km.",
        },
        19: {
            "why": "La restinga, el puerto y el inicio histórico del ferrocarril crean un paisaje urbano distinto y ofrecen una base logística grande.",
            "see": "Restinga, bahía e Igreja da Arrábida; las tres fotos identifican el lugar y su forma peninsular.",
            "access": "Tráfico portuario y aparcamiento vigilado. Mantener cámaras y dron lejos del puerto e instalaciones estratégicas.",
            "when": "De día, una noche si se usa como base en lugar de Benguela.",
            "skip": "Reducirlo a paso si ya se durmió en Benguela o si la actividad portuaria y seguridad desaconsejan detenerse.",
        },
        20: {
            "why": "Ofrece una pausa de playa y acantilado antes de Luanda, especialmente útil después de varios días de carretera.",
            "see": "Bahía, arena y acantilados rojizos; las fotos corresponden a Cabo Ledo y no garantizan condiciones de surf.",
            "access": "Contactar un alojamiento concreto para pista, estacionamiento, camping y perro. El pin de la bahía no autoriza a acampar en cualquier arena.",
            "when": "Con mar moderado y llegada con luz; entre semana suele ser más tranquilo.",
            "skip": "Omitir con oleaje fuerte, acceso no confirmado o si no se consigue estacionamiento vigilado y compatible con el perro.",
        },
        21: {
            "why": "Es el parque de sabana más accesible desde Luanda y permite entender la restauración de fauna posterior a la guerra.",
            "see": "Paisajes de sabana y bajo Cuanza; la fauna varía y nunca se promete. Las fotos son del parque y su río.",
            "access": "Confirmar con la gestión la puerta activa, circuito, guía, tasas, vehículo y política canina. La Reserva de la Biosfera UNESCO es más amplia que el parque.",
            "when": "Primera hora y estación seca para pistas más previsibles.",
            "skip": "Descartarlo si no se resuelve el cuidado del perro, si la puerta o circuito no quedan confirmados o si la pista está cerrada.",
        },
        22: {
            "why": "Es una salida breve desde Luanda para descansar junto al agua sin convertirla en una nueva etapa de carretera.",
            "see": "Lengua de arena, laguna y costa; las tres fotografías se tomaron desde la travesía o en Mussulo.",
            "access": "Llegada en barco-taxi desde un embarcadero confirmado. Preguntar por último regreso, chalecos y admisión del perro antes de embarcar.",
            "when": "Primera salida y regreso con margen de luz; medio día suele bastar.",
            "skip": "Omitir con mar adversa, último barco incierto o si el perro no puede viajar o quedar atendido con seguridad.",
        },
    }
    for poi in angola_pois:
        if poi["n"] in angola_visits:
            poi["visit"] = angola_visits[poi["n"]]
    if not any(poi["n"] == 23 for poi in angola_pois):
        def commons(filename: str, credit: str, caption: str) -> dict[str, str]:
            encoded = quote(filename.replace(" ", "_"), safe="(),-._~'")
            return {
                "img": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}?width=1200",
                "source": f"https://commons.wikimedia.org/wiki/File:{encoded}",
                "credit": credit,
                "caption": caption,
            }

        photos = [
            commons("Église catholique paroquia.jpg", "Doxa kiziamina · CC0", "Iglesia de Nossa Senhora Rainha do Mundo y plaza de Cabinda."),
            commons("Séjour en Angola par Wikimédia Angola. 18.jpg", "ArnoBOUJIKA · CC BY 4.0", "Estatua mariana y campanario en la misma plaza."),
            commons("Image wikimedia Angola 01.jpg", "Kelly203 · CC0", "Fachada de la iglesia y actividad local en el centro de Cabinda."),
        ]
        angola_pois.append({
            "n": 23,
            "name": "Cabinda ciudad · Nossa Senhora Rainha do Mundo",
            "cat": "Ciudad · historia",
            "prio": "Alta",
            "dog": "permitido con condiciones",
            "time": "tránsito / 1 noche",
            "lat": -5.55817,
            "lon": 12.19284,
            "desc": "Cabinda es la capital del enclave angoleño entre Congo-Brazzaville y RD Congo. La iglesia de Nossa Senhora Rainha do Mundo ofrece un punto céntrico y verificable para una pausa histórica; la ciudad es, sobre todo, la base vigilada entre Massabi y Yema.",
            "credit": photos[0]["credit"],
            "img": photos[0]["img"],
            "source": photos[0]["source"],
            "icon": "ciudad · historia",
            "color": "azul",
            "dog_note": "Correa y alojamiento con patio; nada de excursiones remotas.",
            "photos": photos,
            "visit": {
                "why": "Permite entender la singularidad territorial de Cabinda y resolver alojamiento, combustible y agua entre dos fronteras terrestres.",
                "see": "La iglesia y su plaza son un hito urbano concreto. El Tratado de Simulambuco de 1885 forma parte del contexto histórico de la provincia, no una excusa para desviarse a zonas aisladas.",
                "access": "El pin coincide con la iglesia y con las coordenadas EXIF de las fotografías. Llegar de día, aparcar en recinto vigilado y limitarse a la ciudad y al eje confirmado.",
                "when": "Solo dentro de una ventana fronteriza confirmada; una noche si no se pueden completar Massabi y Yema con luz.",
                "skip": "Mantener únicamente la función logística si la situación desaconseja turismo urbano; suspender todo el tránsito si el seguro o los avisos excluyen las carreteras de Cabinda.",
            },
            "links": [
                {"label": "Gobierno Provincial de Cabinda", "url": "https://cabinda.gov.ao/"},
                {"label": "Wikimedia Commons · iglesia y plaza de Cabinda", "url": "https://commons.wikimedia.org/wiki/Category:Igreja_de_Nossa_Senhora_Rainha_do_Mundo_(Cabinda)"},
            ],
        })
    cabinda = next(poi for poi in angola_pois if poi["n"] == 23)
    # Una única portada para fuente, tarjeta y popups de ambos mapas.
    cabinda["img"] = cabinda["photos"][0]["img"]
    cabinda["source"] = cabinda["photos"][0]["source"]
    cabinda["credit"] = cabinda["photos"][0]["credit"]
    save("content/pois/angola.json", angola_pois)


def main() -> None:
    congo()
    drc()
    angola()
    update_pois()
    print("Actualizadas Congo, RD Congo, Angola/Cabinda y sus PDIs de corredor.")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Auditoría idempotente de agua de servicio del grupo 3.

Sustituye ciudades y permisos genéricos por instalaciones físicas documentadas.
El bloque de combustible existente se conserva sin cambios.
"""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FICHA = ROOT / "content" / "ficha"


COMMON = (
    '<div class="callout warn"><div class="callout-title">Regla operativa</div>'
    '<p><strong>Agua de servicio no significa agua potable.</strong> Para beber y cocinar, '
    'usar agua sellada o aplicar el tratamiento completo del vehículo. Una instalación '
    'con duchas no autoriza por sí sola a llenar el depósito: pedir permiso, confirmar '
    'caudal y precio el mismo día y llevar garrafa, manguera, adaptadores y bomba.</p></div>'
    '<div class="callout"><div class="callout-title">Criterio común del proyecto</div>'
    '<p>Estados, reservas, higiene del depósito y protocolo de potabilización: ver '
    '<a href="../../documentacion/#agua-combustible">Documentación general · agua y combustible</a>.</p></div>'
)


def a(url: str, label: str) -> str:
    return f'<a href="{url}" target="_blank" rel="noopener">{label}</a>'


def table(rows: list[tuple[str, str, str]]) -> str:
    body = "".join(
        f"<tr><td>{place}</td><td>{status}</td><td>{action}</td></tr>"
        for place, status, action in rows
    )
    return (
        '<div class="tblwrap"><table><thead><tr><th>Punto exacto</th>'
        '<th>Qué está acreditado</th><th>Decisión operativa</th></tr></thead>'
        f'<tbody>{body}</tbody></table></div>'
    )


WATER = {
    "ghana": {
        "intro": (
            "<h3>Agua de servicio: tres recargas publicadas y dos apoyos de higiene</h3>"
            "<p>Se elimina el pin urbano de Accra y la promesa genérica atribuida a cadenas de "
            "gasolineras y alojamientos. Cada punto siguiente corresponde a una instalación física:</p>"
        ),
        "rows": [
            (
                "Organic Beach Resort, Elonyi · 4.980900, -2.562800",
                "<strong>Agua y ducha para clientes; depósito condicionado.</strong> El camping acepta "
                "vehículos y publica agua, aseo y ducha. Cuatro reseñas, dos de 2026, mantienen activo el lugar, "
                "pero ninguna promete manguera o depósito completo. "
                + a("https://park4night.com/en/place/473944", "ficha, reseñas y GPS"),
                "Buen apoyo al entrar desde Costa de Marfil. Consumir o pagar la estancia y acordar litros y método antes de sacar la manguera.",
            ),
            (
                "Grifo Benab Oil, Akumadan · 7.392700, -1.941700",
                "<strong>Recarga de depósito publicada; agua no potable.</strong> Grifo en la parte trasera "
                "de la estación, frente a la pequeña mezquita. Punto creado en junio de 2025 y todavía sin reseñas. "
                + a("https://park4night.com/fr/place/601110", "ficha y coordenadas"),
                "Usarlo solo como agua de servicio, comprobar que funciona y no bloquear la estación. Tratar si entra en el circuito de cocina.",
            ),
            (
                "Grifos Benab Oil, Kintampo · 8.077100, -1.714300",
                "<strong>Recarga de depósito publicada; agua no potable.</strong> Grifos a la derecha de la "
                "mezquita, descritos como autoservicio y aptos para el depósito del vehículo. Sin reseñas. "
                + a("https://park4night.com/en/place/601859", "ficha y GPS"),
                "Anclaje del eje Kumasi–Tamale. Confirmar operatividad y reservar Akumadan como alternativa, no como garantía simultánea.",
            ),
            (
                "Grifo de gasolinera, Sawla · 9.269500, -2.408400",
                "<strong>Recarga de depósito publicada.</strong> Grifo en la pared de la estación; el autor "
                "avisa de que la boquilla no es estándar. Punto de junio de 2025 sin historial de reseñas. "
                + a("https://park4night.com/en/place/603058", "ficha y coordenadas"),
                "Llevar adaptador universal y garrafa. No asumir potabilidad ni disponibilidad hasta comprobar el grifo in situ.",
            ),
            (
                "Wli Water Heights Hotel, Likpe Bakwa · 7.121800, 0.586800",
                "<strong>Agua y ducha para huéspedes; depósito condicionado.</strong> Camping para vehículos "
                "con agua, aseos y duchas señalados, próximo a Wli. Ficha de agosto de 2025 sin reseñas. "
                + a("https://park4night.com/en/place/625574", "ficha y GPS"),
                "Reservar con Marta y preguntar si los dos 4x4 entran, cuántos litros pueden suministrar y desde qué toma.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>El corredor interior dispone de tres puntos que '
            "publican llenado de depósito, pero los tres son recientes y sin reseñas: comprobar uno antes de consumir la reserva del anterior.</li>"
            "<li>Accra, Cape Coast, Kumasi y Tamale quedan sin pin: comprar agua sellada es fácil, pero no se ha acreditado una toma vehicular exacta.</li>"
            "<li>Organic Beach y Wli resuelven ducha y posible agua por acuerdo; no sustituyen una recarga confirmada.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Organic Beach Resort (Elonyi)",
                "cat": "Agua de servicio",
                "lat": 4.9809,
                "lon": -2.5628,
                "info": "[AGUA Y DUCHA; DEPÓSITO CONDICIONAL] Camping activo con reseñas de 2026. El agua y la ducha son para clientes; acordar litros y método porque no consta llenado con manguera.",
                "source": "https://park4night.com/en/place/473944",
            },
            {
                "name": "Agua de servicio · grifo Benab Oil (Akumadan)",
                "cat": "Agua de servicio",
                "lat": 7.3927,
                "lon": -1.9417,
                "info": "[RECARGA DE DEPÓSITO PUBLICADA; NO POTABLE] Grifo tras la estación, frente a la mezquita. Punto de 2025 sin reseñas: comprobar funcionamiento y no bloquear.",
                "source": "https://park4night.com/fr/place/601110",
            },
            {
                "name": "Agua de servicio · grifos Benab Oil (Kintampo)",
                "cat": "Agua de servicio",
                "lat": 8.0771,
                "lon": -1.7143,
                "info": "[RECARGA DE DEPÓSITO PUBLICADA; NO POTABLE] Grifos de autoservicio a la derecha de la mezquita. Punto de 2025 sin reseñas: verificar antes de depender de él.",
                "source": "https://park4night.com/en/place/601859",
            },
            {
                "name": "Agua de servicio · grifo de gasolinera (Sawla)",
                "cat": "Agua de servicio",
                "lat": 9.2695,
                "lon": -2.4084,
                "info": "[RECARGA DE DEPÓSITO PUBLICADA] Grifo en la pared de la estación; boquilla no estándar. Punto de 2025 sin reseñas: llevar adaptadores y no asumir potabilidad.",
                "source": "https://park4night.com/en/place/603058",
            },
            {
                "name": "Agua de servicio · Wli Water Heights Hotel",
                "cat": "Agua de servicio",
                "lat": 7.1218,
                "lon": 0.5868,
                "info": "[AGUA Y DUCHAS; DEPÓSITO CONDICIONAL] Camping para vehículos con agua y sanitarios publicados. Ficha de 2025 sin reseñas: reservar y acordar litros, toma y acceso de los dos 4x4.",
                "source": "https://park4night.com/en/place/625574",
            },
        ],
        "sources": [
            ["park4night · Organic Beach Resort", "https://park4night.com/en/place/473944"],
            ["park4night · grifo Benab Oil de Akumadan", "https://park4night.com/fr/place/601110"],
            ["park4night · grifos Benab Oil de Kintampo", "https://park4night.com/en/place/601859"],
            ["park4night · grifo de gasolinera de Sawla", "https://park4night.com/en/place/603058"],
            ["park4night · Wli Water Heights Hotel", "https://park4night.com/en/place/625574"],
        ],
    },
    "togo": {
        "intro": (
            "<h3>Agua de servicio: una recarga y dos apoyos condicionados</h3>"
            "<p>Se retiran los pines genéricos de Lomé, Kara y Kpalimé y el permiso supuesto en hoteles y "
            "gasolineras. Los tres puntos aceptados identifican el recinto y el alcance real:</p>"
        ),
        "rows": [
            (
                "Coco Beach Chez Antoine, Lomé · 6.166600, 1.346500",
                "<strong>Agua y duchas para clientes; depósito condicionado.</strong> Camping de playa para "
                "vehículos con agua, aseos y duchas señalados. Creado en julio de 2025, sin reseñas. "
                + a("https://park4night.com/en/place/605423", "ficha y GPS"),
                "Llamar antes, confirmar firme para los dos coches y negociar una cantidad concreta. No interpretar el icono de agua como llenado libre.",
            ),
            (
                "GoldenEye, Kpélé Élé · 7.245400, 0.766900",
                "<strong>Agua y duchas para huéspedes; depósito condicionado.</strong> Camping de vehículos "
                "junto al recinto, con agua, aseos y ducha indicados. Ficha de agosto de 2025 sin reseñas. "
                + a("https://park4night.com/fr/place/625580", "ficha y coordenadas"),
                "Útil antes del corredor occidental. Confirmar acceso, litros, toma y tratamiento; no llegar con el depósito agotado.",
            ),
            (
                "Grifo TotalEnergies, Mango · 10.338700, 0.469300",
                "<strong>Recarga de depósito publicada.</strong> Grifo al fondo de la estación de la N1, "
                "descrito expresamente como apto para llenar el vehículo. Punto de julio de 2025 sin reseñas. "
                + a("https://park4night.com/en/place/605265", "ficha y GPS"),
                "Es la única recarga explícita del grupo togolés: verificar que sigue operativa, pedir permiso en caja y tratar el agua.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>En bajada, Coco Beach solo debe contarse como ducha y '
            "recarga negociada; entrar desde Ghana con margen.</li><li>En subida, completar en Mango antes de desviarse a Koutammakou; "
            "GoldenEye es respaldo condicionado para el oeste.</li><li>Kara, Sokodé, Atakpamé, Badou y Kpalimé quedan sin pin porque no se "
            "localizó una toma vehicular exacta que justifique la antigua promesa.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Coco Beach Chez Antoine",
                "cat": "Agua de servicio",
                "lat": 6.1666,
                "lon": 1.3465,
                "info": "[AGUA Y DUCHAS; DEPÓSITO CONDICIONAL] Camping para vehículos con servicios publicados. Punto de 2025 sin reseñas: llamar y acordar litros; el icono de agua no prueba llenado libre.",
                "source": "https://park4night.com/en/place/605423",
            },
            {
                "name": "Agua de servicio · GoldenEye (Kpélé Élé)",
                "cat": "Agua de servicio",
                "lat": 7.2454,
                "lon": 0.7669,
                "info": "[AGUA Y DUCHAS; DEPÓSITO CONDICIONAL] Camping para vehículos con agua y sanitarios indicados. Ficha de 2025 sin reseñas: confirmar litros, toma y acceso antes de desviarse.",
                "source": "https://park4night.com/fr/place/625580",
            },
            {
                "name": "Agua de servicio · grifo TotalEnergies (Mango)",
                "cat": "Agua de servicio",
                "lat": 10.3387,
                "lon": 0.4693,
                "info": "[RECARGA DE DEPÓSITO PUBLICADA] Grifo al fondo de la estación de la N1. Punto de 2025 sin reseñas: comprobar servicio, pedir permiso y tratar el agua.",
                "source": "https://park4night.com/en/place/605265",
            },
        ],
        "sources": [
            ["park4night · Coco Beach Chez Antoine", "https://park4night.com/en/place/605423"],
            ["park4night · GoldenEye, Kpélé Élé", "https://park4night.com/fr/place/625580"],
            ["park4night · grifo TotalEnergies de Mango", "https://park4night.com/en/place/605265"],
        ],
    },
    "benin": {
        "intro": (
            "<h3>Agua de servicio: tres alojamientos concretos, ninguna recarga libre</h3>"
            "<p>Se eliminan los pines de Cotonú, Possotomé y Dassa/Djougou y la afirmación de que hoteles o "
            "estaciones permiten manguera por sistema. Los apoyos documentados son para clientes:</p>"
        ),
        "rows": [
            (
                "Hôtel Awalé Plage, Grand-Popo · 6.269600, 1.787600",
                "<strong>Agua, duchas y lavandería señaladas; depósito condicionado.</strong> Camping en el "
                "recinto del hotel con una reseña positiva de marzo de 2026. El acceso a playa es arenoso y solo 4x4; "
                "el área interior está sombreada y cerrada. "
                + a("https://park4night.com/fr/place/612332", "ficha, reseña y GPS"),
                "Quedarse en la zona firme y pedir al guardia una toma y volumen concretos. No confundir los servicios del hotel con una estación camper.",
            ),
            (
                "Domaine de la Palmeraie, Ouidah · 6.345300, 2.088700",
                "<strong>Agua y ducha para huéspedes; depósito condicionado.</strong> Dos plazas para vehículos "
                "en recinto cerrado, sombreado y vigilado; agua, aseos y ducha constan en la ficha de julio de 2025, sin reseñas. "
                + a("https://park4night.com/fr/place/610713", "ficha y coordenadas"),
                "Reservar porque solo hay dos plazas. Preguntar por litros, caudal y acceso de cada coche; no depender de una llegada improvisada.",
            ),
            (
                "Auberge Chez Monique, Abomey · 7.197700, 1.980400",
                "<strong>Agua, ducha y lavado para clientes; depósito condicionado.</strong> Patio cerrado con "
                "cuatro plazas, bungalow con ducha y aseo y posibilidad de lavar. Ficha de julio de 2025 sin reseñas. "
                + a("https://park4night.com/fr/place/608956", "ficha y GPS"),
                "Buen apoyo interior para higiene y lavandería. Acordar por separado cualquier llenado del depósito y tratar el agua.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Los tres puntos requieren estancia o autorización; '
            "ninguno acredita manguera o depósito completo.</li><li>Possotomé deja de presentarse como «mejor recarga»: una fuente mineral "
            "o agua corriente del alojamiento no demuestra acceso del coche a una toma.</li><li>Cotonú, Porto-Novo, Dassa y Djougou quedan "
            "sin pin de agua. Concertar el volumen antes de los desvíos y mantener reserva redundante.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · Hôtel Awalé Plage (Grand-Popo)",
                "cat": "Agua de servicio",
                "lat": 6.2696,
                "lon": 1.7876,
                "info": "[AGUA, DUCHAS Y LAVADO; DEPÓSITO CONDICIONAL] Camping de hotel con reseña de marzo de 2026. Usar la zona firme; pedir al guardia litros y toma concreta.",
                "source": "https://park4night.com/fr/place/612332",
            },
            {
                "name": "Agua de servicio · Domaine de la Palmeraie (Ouidah)",
                "cat": "Agua de servicio",
                "lat": 6.3453,
                "lon": 2.0887,
                "info": "[AGUA Y DUCHAS; DEPÓSITO CONDICIONAL] Dos plazas en recinto cerrado con servicios publicados. Ficha de 2025 sin reseñas: reservar y confirmar acceso, litros y caudal.",
                "source": "https://park4night.com/fr/place/610713",
            },
            {
                "name": "Agua de servicio · Auberge Chez Monique (Abomey)",
                "cat": "Agua de servicio",
                "lat": 7.1977,
                "lon": 1.9804,
                "info": "[AGUA, DUCHA Y LAVADO; DEPÓSITO CONDICIONAL] Patio para cuatro vehículos y bungalow sanitario. La fuente no promete llenado: acordarlo aparte y tratar el agua.",
                "source": "https://park4night.com/fr/place/608956",
            },
        ],
        "sources": [
            ["park4night · Hôtel Awalé Plage", "https://park4night.com/fr/place/612332"],
            ["park4night · Domaine de la Palmeraie", "https://park4night.com/fr/place/610713"],
            ["park4night · Auberge Chez Monique", "https://park4night.com/fr/place/608956"],
        ],
    },
    "nigeria": {
        "intro": (
            "<h3>Agua de servicio: un punto de agua y dos duchas, sin promesas urbanas</h3>"
            "<p>Se retiran los pines genéricos de Lagos/Calabar e Ikom/Obudu. Tampoco se mantiene la afirmación "
            "de que gasolineras, hoteles o Marina Resort permiten llenar con manguera: no hay una toma exacta que la sostenga.</p>"
        ),
        "rows": [
            (
                "Recinto eclesial de Agbor · 6.257800, 6.221900",
                "<strong>Agua y duchas señaladas; depósito condicionado.</strong> Recinto cercado y vigilado que "
                "acepta hasta diez vehículos grandes; la ficha de marzo de 2026 marca agua potable, aseos y duchas, "
                "pero todavía no tiene reseñas ni confirma llenado con manguera. "
                + a("https://park4night.com/es/place/664691", "ficha y GPS"),
                "Es el único punto del país con una toma de agua identificada en esta auditoría. Pedir permiso, cantidad y método; no llegar con ambos depósitos vacíos.",
            ),
            (
                "Patio eclesial de Abakaliki · 6.311700, 8.154600",
                "<strong>Solo ducha; llenado no acreditado.</strong> Patio cerrado junto a un orfanato, con "
                "espacio publicado para cinco vehículos grandes, aseos y ducha. Punto de marzo de 2026 sin reseñas ni toma de agua indicada. "
                + a("https://park4night.com/en/place/664853", "ficha y coordenadas"),
                "Usarlo únicamente como apoyo de higiene y pernocta, previa aceptación del recinto. No solicitar agua del orfanato como si fuera un servicio público.",
            ),
            (
                "Betteh Hotel and Resort, Ikom · 5.956300, 8.717700",
                "<strong>Solo ducha de una habitación; llenado no acreditado.</strong> Camping en zona de hormigón "
                "con acceso al baño de una habitación. Una reseña de diciembre de 2025 confirma acogida, pero no agua para depósito. "
                + a("https://park4night.com/es/place/605421", "ficha, reseña y GPS"),
                "Último apoyo de ducha antes de Mfum/Ekok. Reservar y llegar a Ikom con el depósito resuelto por cita privada anterior.",
            ),
        ],
        "plan": (
            '<h3>Plan de tramo</h3><ul class="ticks"><li>Comprar agua sellada para beber no resuelve los litros '
            "de ducha. Para Lagos, Benin City y Calabar hay que concertar por escrito con un alojamiento vallado: acceso de dos 4x4, "
            "litros, toma, horario y precio.</li><li>Agbor es respaldo condicionado, no infraestructura pública. Abakaliki e Ikom solo "
            "resuelven higiene.</li><li>No captar de Afi, Old Ekuri, ríos o lluvia dentro del plan ordinario. Llevar reserva suficiente para "
            "alcanzar Camerún si falla la cita nigeriana.</li></ul>"
        ),
        "points": [
            {
                "name": "Agua de servicio · recinto eclesial de Agbor",
                "cat": "Agua de servicio",
                "lat": 6.2578,
                "lon": 6.2219,
                "info": "[AGUA Y DUCHAS; DEPÓSITO CONDICIONAL] Recinto cercado para vehículos grandes con agua y sanitarios señalados. Punto de marzo de 2026 sin reseñas: pedir permiso, litros y método.",
                "source": "https://park4night.com/es/place/664691",
            },
            {
                "name": "Agua de servicio · patio eclesial de Abakaliki",
                "cat": "Agua de servicio",
                "lat": 6.3117,
                "lon": 8.1546,
                "info": "[SOLO DUCHA] Patio cerrado junto a un orfanato con aseos y ducha publicados. No consta toma ni llenado: usar con autorización para higiene, no como recarga.",
                "source": "https://park4night.com/en/place/664853",
            },
            {
                "name": "Agua de servicio · Betteh Hotel and Resort (Ikom)",
                "cat": "Agua de servicio",
                "lat": 5.9563,
                "lon": 8.7177,
                "info": "[SOLO DUCHA] Camping en zona de hormigón con acceso al baño de una habitación; reseña de diciembre de 2025. No consta llenado del vehículo.",
                "source": "https://park4night.com/es/place/605421",
            },
        ],
        "sources": [
            ["park4night · recinto eclesial de Agbor", "https://park4night.com/es/place/664691"],
            ["park4night · patio eclesial de Abakaliki", "https://park4night.com/en/place/664853"],
            ["park4night · Betteh Hotel and Resort, Ikom", "https://park4night.com/es/place/605421"],
        ],
    },
}


def fuel_from(old: str) -> str:
    start = old.find("<h3>Combustible</h3>")
    if start < 0:
        raise ValueError("No se encontró el bloque de combustible")
    end = old.find('<div class="callout', start)
    return old[start:] if end < 0 else old[start:end]


def is_old_water(point: dict) -> bool:
    return "agua" in str(point.get("cat", "")).lower() or "agua" in str(point.get("name", "")).lower()


def update(slug: str, cfg: dict) -> None:
    path = FICHA / f"{slug}.json"
    data = json.loads(path.read_text(encoding="utf-8"))

    for section in data["custom_sections"]:
        if section[0] == "agua-combustible":
            section[2] = cfg["intro"] + table(cfg["rows"]) + cfg["plan"] + fuel_from(section[2]) + COMMON
            break
    else:
        raise ValueError(f"{slug}: falta la sección agua-combustible")

    data["logistics"] = [p for p in data.get("logistics", []) if not is_old_water(p)] + cfg["points"]
    existing = {tuple(item) for item in data.get("sources", []) if isinstance(item, list) and len(item) == 2}
    for source in cfg["sources"]:
        if tuple(source) not in existing:
            data.setdefault("sources", []).append(source)
            existing.add(tuple(source))

    if slug == "nigeria":
        old = (
            "Agua: no beber del grifo en ningún punto del país. El agua embotellada y en bolsa "
            "(«pure water») es barata y está en todas partes; para el depósito de uso general, "
            "manguera de estación de servicio u hotel, pero tratar siempre antes de beber."
        )
        new = (
            "Agua: no beber del grifo en ningún punto del país. El agua embotellada y en bolsa "
            "(«pure water») es barata y está en todas partes. La auditoría no acredita una recarga "
            "pública en Lagos o Calabar: usar los puntos exactos de esta ficha y concertar cualquier "
            "llenado privado con litros y permiso escritos; tratar toda agua que entre en el circuito."
        )
        for section in data.get("custom_sections_post", []):
            section[2] = section[2].replace(old, new)

    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"{slug}: {len(cfg['points'])} puntos de agua exactos")


for country, config in WATER.items():
    update(country, config)

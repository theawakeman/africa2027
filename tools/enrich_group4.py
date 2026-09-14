#!/usr/bin/env python3
"""Aplica enriquecimientos visuales y enlaces verificados del grupo 4.

El archivo conserva una lista explícita por PDI para que la ampliación sea
reproducible y auditable. No busca ni asigna resultados automáticamente.
"""
from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import quote, unquote


ROOT = Path(__file__).resolve().parents[1]


def commons(filename: str, credit: str, caption: str) -> dict[str, str]:
    encoded = quote(filename.replace(" ", "_"), safe="(),-._~")
    return {
        "img": f"https://commons.wikimedia.org/wiki/Special:FilePath/{encoded}?width=1200",
        "source": f"https://commons.wikimedia.org/wiki/File:{encoded}",
        "credit": credit,
        "caption": caption,
    }


def canonical_source(value: str) -> str:
    """Iguala las variantes Commons con espacios, guiones bajos y escapes."""
    decoded = unquote(value).replace("_", " ")
    return " ".join(decoded.split()).casefold()


LINKS: dict[str, dict[int, tuple[str, str]]] = {
    "angola": {
        1: ("Luanda · contexto urbano e historia", "https://en.wikipedia.org/wiki/Luanda"),
        2: ("Miradouro da Lua · descripción del enclave", "https://pt.wikipedia.org/wiki/Miradouro_da_Lua"),
        3: ("Pungo Andongo · monolitos e historia", "https://en.wikipedia.org/wiki/Black_Rocks_at_Pungo_Andongo"),
        4: ("Kalandula Falls · geografía y acceso", "https://en.wikipedia.org/wiki/Kalandula_Falls"),
        7: ("Historia del Reino do Bailundo y visita a Ombala Mbalundu", "https://welcometoangola.co.ao/en/reino-do-bailundo/"),
        9: ("Luena · historia, servicios y transportes", "https://pt.wikipedia.org/wiki/Luena_(Angola)"),
        10: ("African Parks · visitar Iona", "https://www.africanparks.org/the-parks/iona"),
        11: ("Foz do Cunene · ficha e imagen del enclave", "https://medicareclub.ao/index.php?province_content_id=14&route=club%2Fguide%2Fattraction"),
        12: ("Expedición 4x4 a Baía dos Tigres y Foz do Cunene", "https://kumakonda.com/ilha-da-baia-dos-tigres-angola/"),
        13: ("UNESCO · sitio arqueológico de Tchitundu-Hulu", "https://whc.unesco.org/en/tentativelists/6251/"),
        14: ("Lagoa do Arco · historia y estado estacional", "https://en.wikipedia.org/wiki/Lake_Arco"),
        15: ("Moçâmedes · contexto urbano y costa", "https://en.wikipedia.org/wiki/Mo%C3%A7%C3%A2medes"),
        16: ("Serra da Leba · carretera y puerto", "https://en.wikipedia.org/wiki/Serra_da_Leba"),
        17: ("Tundavala Gap · geología y mirador", "https://en.wikipedia.org/wiki/Tundavala_Gap"),
        18: ("Benguela · historia y patrimonio urbano", "https://en.wikipedia.org/wiki/Benguela"),
        19: ("Lobito · bahía, restinga y ferrocarril", "https://en.wikipedia.org/wiki/Lobito"),
        20: ("Cabo Ledo · playa, surf e historia", "https://pt.wikipedia.org/wiki/Cabo_Ledo"),
        21: ("UNESCO · Reserva de la Biosfera Quiçama", "https://www.unesco.org/en/mab/quicama"),
        22: ("Mussulo · península, bahía y accesos", "https://en.wikipedia.org/wiki/Mussulo"),
    },
}


PHOTOS: dict[str, dict[int, list[dict[str, str]]]] = {
    "angola": {
        6: [
            commons("Igreja Matriz de Waku Kungo - panoramio.jpg", "Rogério Melo · CC BY 3.0", "Iglesia principal de Waku Kungo"),
            commons("Waku Kungo, Angola - panoramio.jpg", "Rogério Melo · CC BY 3.0", "Paisaje urbano de Waku Kungo"),
            commons("Waku Kungo - panoramio - Rogério Melo (3).jpg", "Rogério Melo · CC BY 3.0", "Otra vista de Waku Kungo"),
        ],
        7: [
            {
                "img": "https://welcometoangola.co.ao/wp-content/uploads/2022/10/reino-bailundo-capa-1.jpg",
                "source": "https://welcometoangola.co.ao/en/reino-do-bailundo/",
                "credit": "Welcome to Angola",
                "caption": "Autoridades tradicionales bajo el rótulo de Ombala yo Mbalundo",
            },
        ],
        9: [
            commons("Jardim do Palacio do Governador Luena Moxico.jpg", "Pereira Santos Samuel · CC BY-SA 3.0", "Jardín del palacio provincial en Luena"),
            commons("Instituto Médio de Administração e Gestão.jpeg", "Diego Passos Costa · CC BY-SA 3.0", "Instituto de enseñanza de Luena"),
            commons("Por do Sol Imag Luena 08 novembro 2011 1600x1200 388KB.jpg", "Diego Passos Costa · CC BY-SA 3.0", "Atardecer urbano en Luena"),
        ],
        11: [
            {
                "img": "https://medicareclub.ao/image/cache/catalog/guia/namibe/foz/foz%20rio%20cunene%20pedro%20carreno-1240x827.jpg",
                "source": "https://medicareclub.ao/index.php?province_content_id=14&route=club%2Fguide%2Fattraction",
                "credit": "Pedro Carreño · Medicare Club Angola",
                "caption": "Desembocadura del río Cunene entre carrizos y dunas",
            },
        ],
        12: [
            commons("Ilha dos Tigres 1466538 960 720.jpg", "juls26 · CC0", "Antiguos depósitos de aceite de pescado junto a la bahía"),
            commons("Ilha dos Tigres 1466534 960 720.jpg", "juls26 · CC0", "Barracones abandonados del poblado pesquero"),
        ],
        15: [
            commons("Namibe Waterfront (19432713306).jpg", "David Stanley · CC BY 2.0", "Avenida costera y bahía de Moçâmedes"),
            commons("Governo Provincial do Namibe (19543179475) (cropped).jpg", "David Stanley · CC BY 2.0", "Edificio del gobierno provincial en Moçâmedes"),
        ],
        18: [
            commons("Igreja Benguela, Angola.jpg", "F. H. Mira · CC BY-SA 2.0", "Iglesia histórica de Benguela"),
            commons("Paços do Concelho, Benguela.jpg", "F. H. Mira · CC BY-SA 2.0", "Ayuntamiento de Benguela"),
        ],
        19: [
            commons("Igreja da Arrábida in Lobito - Angola 2015.jpg", "David Stanley · CC BY 2.0", "Iglesia da Arrábida en la Restinga de Lobito"),
            commons("Restinga Peninsula (18996958243) (cropped).jpg", "David Stanley · CC BY 2.0", "Restinga arenosa que protege la bahía de Lobito"),
        ],
        20: [
            commons("Cabo Ledo beach, Angola 02.jpg", "Felipe Miguel · CC BY-SA 2.0", "Playa y acantilados de Cabo Ledo"),
            commons("Cabo Ledo beach, Angola 03.jpg", "Felipe Miguel · CC BY-SA 2.0", "Otra vista de la ensenada de Cabo Ledo"),
        ],
        21: [
            commons("Kissama 001.JPG", "Àngel Sàez i Pedrero · CC BY-SA 4.0", "Paisaje de sabana en el Parque Nacional de Kissama"),
            commons("Río Cuanza en Kissama.JPG", "Àngel Sàez i Pedrero · CC BY-SA 4.0", "Río Cuanza en el Parque Nacional de Kissama"),
        ],
        22: [
            commons("Mussulo Island.jpg", "Juvenalia Brito · CC BY-SA 3.0", "Playa y casas de la península de Mussulo"),
            commons("Mussulo, Angola.jpg", "Juvenalia Brito · CC BY-SA 3.0", "Mussulo visto durante la travesía en barco"),
        ],
    },
}


REMOVE_LINKS: dict[str, set[str]] = {
    "angola": {
        "https://minamb.gov.ao/web/noticias/o-triunfo-da-palanca-negra-gigante-em-cangandala/",
        "https://vivreenangola.com/tourisme/en-province/kwanza-sul/waku-kungo/",
        "https://mcta.gov.ao/ao/noticias/governadora-visita-ombala-mbalundo/",
        "https://minamb.gov.ao/web/noticias/serra-do-pindo-e-morro-do-moco-elevados-a-areas-de-conservacao-ambiental/",
    },
}


REMOVE_PHOTOS: dict[str, set[str]] = {
    "angola": {
        "https://mcta.gov.ao/ao/noticias/governadora-visita-ombala-mbalundo/",
    },
}


def apply(country: str) -> None:
    path = ROOT / "content" / "pois" / f"{country}.json"
    pois = json.loads(path.read_text(encoding="utf-8"))
    by_number = {poi["n"]: poi for poi in pois}

    for poi in pois:
        blocked_links = REMOVE_LINKS.get(country, set())
        poi["links"] = [
            item for item in poi.get("links", [])
            if not isinstance(item, dict) or item.get("url") not in blocked_links
        ]
        blocked_photos = REMOVE_PHOTOS.get(country, set())
        poi["photos"] = [
            item for item in poi.get("photos", [])
            if not isinstance(item, dict) or item.get("source") not in blocked_photos
        ]

    for number, (label, url) in LINKS.get(country, {}).items():
        poi = by_number[number]
        links = poi.setdefault("links", [])
        if not any(item.get("url") == url for item in links if isinstance(item, dict)):
            links.append({"label": label, "url": url})

    for number, additions in PHOTOS.get(country, {}).items():
        poi = by_number[number]
        photos = poi.setdefault("photos", [])
        unique_photos = []
        existing_sources = set()
        for item in photos:
            if not isinstance(item, dict):
                continue
            marker = canonical_source(item.get("source", ""))
            if marker in existing_sources:
                continue
            unique_photos.append(item)
            existing_sources.add(marker)
        poi["photos"] = photos = unique_photos
        for photo in additions:
            marker = canonical_source(photo["source"])
            if marker not in existing_sources:
                photos.append(photo)
                existing_sources.add(marker)

    path.write_text(json.dumps(pois, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    for country_name in sorted(set(LINKS) | set(PHOTOS)):
        apply(country_name)

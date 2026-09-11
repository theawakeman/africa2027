# -*- coding: utf-8 -*-
"""Generic full-ficha builder: turns a compact country spec into the dict
consumed by build.render_ficha. Photos are hotlinked from Wikimedia with
credit+license; the service worker precaches them for offline use."""
from site_common import table, callout, bullets, st_pill, esc

def make_ficha(spec):
    """spec keys:
    slug, name, revision, sub, chips (list), center, zoom, notice,
    pois: list of dicts {n,name,cat,prio,dog,color,time,lat,lon,desc,img(url),credit,source,dog_note?}
    logistics: [(name,cat,lat,lon,info)]
    corridor: [(lat,lon)], corridor_alt: optional
    resumen_intro (html/p), facts [(k,v)], alerts [str],
    ruta_intro, route_rows [(...)], route_headers, acampada [str] optional,
    offroad: [str] optional  (rutas offroad destacadas)
    visado [str], fronteras_rows [(func,paso,check)], vehiculos [str],
    drones_callout (kind,title,body), drones [str],
    starlink_callout, starlink [str],
    perro_intro [str], dog_matrix [(zona,estado,planB)] optional, salud [str],
    seguridad_intro (str), seguridad [str],
    pendientes [(tema,criterio)], sources [(t,u)], sources_note, emergency, matrix_note
    """
    s = spec
    d = {k: s[k] for k in ("slug", "name", "revision", "sub", "chips", "center", "zoom", "notice")}
    d["estado"] = "completa"
    d["verificado"] = bool(s.get("verificado", False))
    d["hero_img"] = s["pois"][0]["img"] if s.get("hero_img") is None else s["hero_img"]
    d["hero_credit"] = s.get("hero_credit", f"{s['pois'][0]['name']} · {s['pois'][0]['credit']}")
    d["pois"] = [dict(p) for p in s["pois"]]
    d["logistics"] = [{"name": n, "cat": c, "lat": la, "lon": lo, "info": i} for n, c, la, lo, i in s["logistics"]]
    d["corridor"] = s.get("corridor", [])
    d["corridor_alt"] = s.get("corridor_alt", [])

    historia = ""
    if s.get("historia_resumen"):
        historia += f"<p>{esc(s['historia_resumen'])}</p>"
        historia += callout("", "Historia completa · con audio",
                             f'Orígenes, colonización, independencia y situación actual, con fuentes y '
                             f'<strong>audio tipo podcast</strong> narrado por el propio dispositivo para escuchar mientras se conduce: '
                             f'<a href="historia/">leer y escuchar la historia de {esc(s["name"])} →</a>', raw=True)
    d["historia_resumen"] = s.get("historia_resumen", "")
    d["historia_secciones"] = s.get("historia_secciones", [])
    d["historia_fuentes"] = s.get("historia_fuentes", [])

    resumen = ""
    if s.get("resumen_intro"):
        resumen += f"<p>{s['resumen_intro']}</p>"
    if s.get("decision"):
        resumen += callout("", "Decisión de ruta", s["decision"])
    resumen += table(("Tema", "Estado de trabajo"), s["facts"])
    if s.get("alerts"):
        resumen += "<h3>Alertas que condicionan la visita</h3>" + bullets(s["alerts"], bold_split=True)

    ruta = ""
    if s.get("ruta_intro"):
        ruta += f"<p>{s['ruta_intro']}</p>"
    ruta += table(s.get("route_headers", ("Bloque", "Contenido", "Condición")), s["route_rows"], cls="num")
    if s.get("offroad"):
        ruta += "<h3>Rutas y pistas 4x4 destacadas</h3>" + bullets(s["offroad"])
    if s.get("acampada"):
        ruta += "<h3>Acampada y pernocta</h3>" + bullets(s["acampada"])

    agua_combustible = ""
    if s.get("agua") or s.get("combustible") or s.get("agua_combustible_alerta"):
        if s.get("agua_combustible_alerta"):
            agua_combustible += callout("warn", "Tramo sin garantía de combustible cada 500 km", s["agua_combustible_alerta"])
        agua_combustible += "<h3>Agua: recarga de depósitos (beber, ducha, aseo y limpieza)</h3>"
        agua_combustible += "<p>No solo agua de boca: como vehículos de expedición autónomos necesitamos recargar el depósito de agua de uso general (ducha, aseo, vajilla, limpieza) además del agua potable de beber. Puntos verificados o de referencia para esta recarga:</p>"
        agua_combustible += bullets(s.get("agua", ["Sin puntos verificados todavía: confirmar en iOverlander/Tracks4Africa antes de cerrar la ruta."]))
        agua_combustible += "<h3>Combustible</h3>" + bullets(s.get("combustible", ["Sin puntos verificados todavía: confirmar en iOverlander/Tracks4Africa antes de cerrar la ruta."]))
        agua_combustible += callout("", "Fuentes cruzadas", 'Puntos y comentarios recientes verificados también en <a href="https://ioverlander.com/" target="_blank" rel="noopener">iOverlander</a> y <a href="https://tracks4africa.co.za/" target="_blank" rel="noopener">Tracks4Africa</a>; revisar la fecha del último comentario antes de confiar en un punto.', raw=True)
        agua_combustible += callout("", "Criterio común del proyecto", 'Estrategia general de depósitos, potabilización y calidad de gasóleo: ver <a href="../../documentacion/#agua-combustible">Documentación general · agua y combustible</a>.', raw=True)

    fronteras = "<h3>Visado</h3>" + bullets(s["visado"])
    fronteras += "<h3>Fronteras de la ruta</h3>" + table(("Función", "Paso", "Comprobación operativa"), s["fronteras_rows"])
    fronteras += "<h3>Vehículos</h3>" + bullets(s["vehiculos"])
    fronteras += callout("", "Trámites comunes", 'CPD, autorización del Grenadier, Delica y seguros: ver <a href="../../documentacion/">Documentación general</a>.', raw=True)

    dk, dt, db = s["drones_callout"]
    drones = callout(dk, dt, db) + bullets(s["drones"])
    sk, st_, sb = s["starlink_callout"]
    starlink = callout(sk, st_, sb) + bullets(s["starlink"])

    perro = "<h3>Entrada del perro</h3>" + bullets(s["perro_intro"])
    perro += callout("", "Requisitos comunes del perro", 'Microchip, pasaporte UE, rabia y titulación serológica: ver <a href="../../documentacion/#perro">Documentación general · perro</a>.', raw=True)
    if s.get("dog_matrix"):
        perro += "<h3>Matriz canina por zona</h3>" + table(("Zona", "Estado", "Plan B obligatorio"),
                                                          [(z, st_pill(e), p) for z, e, p in s["dog_matrix"]])
    perro += "<h3>Salud humana</h3>" + bullets(s["salud"])

    seguridad = f"<p>{s['seguridad_intro']}</p>" + bullets(s["seguridad"])
    seguridad += callout("", "Protocolo común", 'Conducción, controles y escalado: <a href="../../documentacion/#seguridad">Documentación general · seguridad</a>.', raw=True)

    gpx = "<h3>Decisiones pendientes</h3>" + table(("Tema", "Criterio de cierre"), s["pendientes"])
    gpx += callout("warn", "Punto de control", "Revalidar visados, fronteras, salud, seguridad, drones y comunicaciones 30–60 días antes de la entrada, y de nuevo 72 h antes de cada frontera.")

    d["custom_sections"] = [("resumen", "Resumen operativo", resumen)]
    if historia:
        d["custom_sections"].append(("historia", "Historia y contexto", historia))
    d["custom_sections"].append(("ruta", "Ruta propuesta", ruta))
    if agua_combustible:
        d["custom_sections"].append(("agua-combustible", "Agua y combustible", agua_combustible))
    d["custom_sections_post"] = [
        ("fronteras", "Visado, fronteras y vehículos", fronteras),
        ("drones", "Drones", drones),
        ("starlink", "Starlink", starlink),
        ("perro", "Perro y salud", perro),
        ("seguridad", "Seguridad y comunicaciones", seguridad),
        ("gpx", "Validación y decisiones", gpx),
    ]
    d["sources"] = s["sources"]
    d["sources_note"] = s["sources_note"]
    d["emergency"] = s["emergency"]
    d["matrix_note"] = s.get("matrix_note", "Puntos preparados para My Maps; importar desde los KML por capas y respetar los nombres exactos.")
    return d

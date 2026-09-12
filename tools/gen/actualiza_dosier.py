# -*- coding: utf-8 -*-
"""Reescribe las tablas de §2 del dosier del perro con los contactos verificados.

Añade a la tabla resumen tres columnas que antes no estaban: quién emite el
permiso (enlazado a la página concreta del trámite, no a la portada), a qué
correo hay que escribir, y si hace falta certificado sanitario y cuántos días
vale. Y añade a cada ficha de país de §3 un bloque «Dónde se pide».

Se ejecuta a mano cuando cambien los contactos:  python3 actualiza_dosier.py
Es idempotente: antes de escribir quita las columnas y los bloques que generó
la vez anterior, así que se puede lanzar tantas veces como haga falta.
"""
import re
from pathlib import Path

from data_perro_contactos import CONTACTOS

DOSIER = Path(__file__).parent / "docs" / "DOSSIER_PERRO.md"

# Nombre tal y como aparece en la tabla -> slug
FILA = {
    "Marruecos": "marruecos", "Sáhara Occidental": "sahara-occidental",
    "Sáhara Occ. / Marruecos": "sahara-occidental",
    "Mauritania": "mauritania", "Senegal": "senegal", "Guinea": "guinea",
    "Costa de Marfil": "costa-de-marfil", "Ghana": "ghana", "Togo": "togo",
    "Benín": "benin", "Nigeria": "nigeria", "Camerún": "camerun",
    "Congo-Brazzaville": "congo", "Congo": "congo", "RD Congo": "rd-congo",
    "Angola": "angola", "Zambia": "zambia", "Tanzania": "tanzania",
    "Kenia": "kenia", "Mozambique": "mozambique", "Zimbabue": "zimbabue",
    "Botsuana": "botsuana", "Sudáfrica": "sudafrica", "Namibia": "namibia",
    "Gambia": "gambia", "Sierra Leona": "sierra-leona", "Liberia": "liberia",
    "Gabón": "gabon", "Malaui": "malaui", "Uganda": "uganda", "Ruanda": "ruanda",
    "Esuatini": "esuatini", "Lesoto": "lesoto", "UE / España": "ue",
}

# Búsqueda tolerante: «COSTA DE MARFIL» y «Costa de Marfil» son el mismo país.
POR_NOMBRE = {k.lower(): v for k, v in FILA.items()}


def slug_de(nombre):
    n = re.sub(r"[*`🟢🟡🟠🔴]|—.*$|\(.*?\)", "", str(nombre)).strip().lower()
    return POR_NOMBRE.get(n)


def _organismo(slug):
    """Nombre del organismo, enlazado a la página concreta del trámite."""
    d = CONTACTOS.get(slug)
    if not d or not d.get("organismo"):
        return "—"
    nombre = d["organismo"].split(",")[0].split("(")[0].strip()
    if len(nombre) > 46:
        nombre = nombre[:44].rsplit(" ", 1)[0] + "…"
    url = d.get("url")
    if not url:
        return nombre
    marca = ""
    if d.get("url_generica"):
        marca = " ⚠️"          # solo se ha encontrado la portada
    elif not d.get("url_verificada"):
        marca = " ❓"          # no se ha podido abrir para comprobarla
    return f"[{nombre}]({url}){marca}"


EMAIL = re.compile(r"[\w.+-]+@[\w-]+(?:\.[\w-]+)+")


def _correo(slug):
    """Solo las direcciones; las anotaciones («vigente», «buzón general») van en la nota."""
    d = CONTACTOS.get(slug) or {}
    c = d.get("email")
    if not c:
        return "— *sin correo publicado*"
    return " · ".join(f"`{x}`" for x in EMAIL.findall(c))


def _certificado(slug):
    d = CONTACTOS.get(slug) or {}
    if d.get("cert") is None:
        return "sin confirmar"
    if not d.get("cert"):
        return "❌ No"
    dias = d.get("cert_dias")
    return f"✅ Sí · **{dias} días**" if dias else "✅ Sí · *validez sin publicar*"


def _celdas(linea):
    """Celdas de una fila de markdown, sin las barras de los extremos."""
    t = linea.strip()
    if t.startswith("|"):
        t = t[1:]
    if t.endswith("|"):
        t = t[:-1]
    return t.split("|")


def reescribe_tabla(texto, cabecera_vieja, col_pais):
    """Añade las tres columnas nuevas a una tabla de markdown ya existente.

    Cuidado con las filas que acaban en una celda vacía: si se recorta la línea
    por el final, esa celda desaparece y todo lo que se añada detrás queda
    desplazado una columna. Por eso se cuenta siempre contra la cabecera.
    """
    lineas = texto.split("\n")
    salida, dentro, ancho = [], False, 0
    NUEVAS = [" Quién lo emite ", " Correo ", " Certificado sanitario "]

    for ln in lineas:
        if ln.strip() == cabecera_vieja.strip():
            dentro = True
            ancho = len(_celdas(ln))
            salida.append("|" + "|".join(_celdas(ln) + NUEVAS) + "|")
            continue
        if dentro and re.match(r"^\|[\s:-]+\|", ln):
            salida.append("|" + "|".join(_celdas(ln) + ["---"] * 3) + "|")
            continue
        if dentro:
            if not ln.strip().startswith("|"):
                dentro = False
                salida.append(ln)
                continue
            cel = _celdas(ln)
            cel += [""] * (ancho - len(cel))          # completar las vacías del final
            slug = slug_de(cel[col_pais])
            nuevas = ([" " + _organismo(slug) + " ", " " + _correo(slug) + " ",
                       " " + _certificado(slug) + " "] if slug else [" — ", " — ", " — "])
            salida.append("|" + "|".join(cel[:ancho] + nuevas) + "|")
            continue
        salida.append(ln)
    return "\n".join(salida)


META = ("URL VERIFICADA", "LA URL QUE FALTABA", "EL MEJOR RESULTADO", "url_verificada",
        "AVISO: NO se ha podido", "no se ha podido abrir", "entorno de verificacion",
        "SIN VERIFICAR", "404", "robots")


def _limpia(t, tope=190):
    """Primera frase de la nota, y solo si le sirve de algo al viajero.

    Las notas vienen de la investigación y muchas hablan de la investigación
    misma («URL VERIFICADA y es la mejor de las trece»). Eso no pinta nada en
    el dosier: el estado de cada enlace ya se marca con ⚠️ o ❓.
    """
    t = re.sub(r"\s+", " ", t).strip()
    frase = re.split(r"(?<=[.:])\s+(?=[A-ZÁÉÍÓÚÑ])", t)[0]
    if not frase or len(frase) > tope:
        return ""
    if any(m.lower() in frase.lower() for m in META):
        return ""
    cabeza = frase[:60]
    if sum(c.isupper() for c in cabeza) > sum(c.islower() for c in cabeza):
        return ""          # titular en mayúsculas: es comentario de investigación
    return frase


def bloque_pais(slug, titulo="Dónde se pide"):
    d = CONTACTOS.get(slug)
    if not d:
        return ""
    org = d.get("organismo") or "Organismo sin localizar"
    url = d.get("url")
    if url and d.get("url_generica"):
        web = f" — [portada del organismo]({url}) ⚠️ *no se ha localizado la página del trámite*"
    elif url and not d.get("url_verificada"):
        web = f" — [página del trámite]({url}) ❓ *no se ha podido abrir para comprobarla*"
    elif url:
        web = f" — [página del trámite]({url})"
    else:
        web = " — *sin página localizada*"
    correo = ""
    if d.get("email"):
        # En la ficha se conservan las anotaciones («vigente», «buzón general»…)
        correo = "**Escribir a:** " + EMAIL.sub(lambda m: f"`{m.group(0)}`", d["email"]) + "  \n"
    tel = f"**Teléfono:** {d['tel']}  \n" if d.get("tel") else ""
    cert = _certificado(slug).replace("**", "")
    if d.get("cert_quien"):
        cert += f" · lo emite: {d['cert_quien']}"
    otras = [u for u in (d.get("fuentes") or []) if u != d.get("url")][:2]
    extra = ""
    if otras:
        sin_esquema = re.compile(r"^https?://(www\.)?")
        extra = "**Otra fuente:** " + " · ".join(
            "[" + sin_esquema.sub("", u).split("/")[0] + "](" + u + ")" for u in otras) + "  \n"
    txt = (f"\n**{titulo}.** {org}{web}  \n{correo}{tel}"
           f"**Certificado sanitario:** {cert}  \n{extra}")
    nota = _limpia(d.get("nota") or "")
    if nota:
        txt += f"\n> {nota}\n"
    return txt


NUEVAS_CAB = "| Quién lo emite | Correo | Certificado sanitario |"


def quita_generado(md):
    """Deja el dosier como estaba antes de la última ejecución.

    Quita las tres columnas añadidas a las tablas de §2 y los bloques «Dónde se
    pide» de §3, para que la siguiente pasada los regenere desde CONTACTOS.
    """
    salida, dentro = [], False
    for ln in md.split("\n"):
        t = ln.strip()
        if t.startswith("|") and t.endswith(NUEVAS_CAB):
            dentro = True
            salida.append("|" + "|".join(_celdas(ln)[:-3]) + "|")
            continue
        if dentro:
            if not t.startswith("|"):
                dentro = False
                salida.append(ln)
                continue
            salida.append("|" + "|".join(_celdas(ln)[:-3]) + "|")
            continue
        salida.append(ln)
    md = "\n".join(salida)
    # bloque «Dónde se pide…» (párrafo + líneas de detalle + cita opcional) hasta la línea en blanco doble
    md = re.sub(r"\n\*\*Dónde se pide[^\n]*\n(?:[^\n]+  \n)*(?:\n> [^\n]*\n)?", "\n", md)
    return re.sub(r"\n{3,}", "\n\n", md)


def main():
    md = DOSIER.read_text(encoding="utf-8")
    md = quita_generado(md)

    md = reescribe_tabla(
        md, "| # | País | Entrada terrestre | Permiso previo | Tiempo de tramitación | Dificultad | Nota clave |", 1)
    md = reescribe_tabla(
        md, "| # | País | ¿Permiso nuevo? | Dificultad | Nota |", 1)
    md = reescribe_tabla(
        md, "| País | Entrada terrestre | Permiso | Dificultad | Nota |", 0)

    # Bloque «Dónde se pide» al final de cada ficha de país de §3
    def inserta(m):
        titulo, cuerpo = m.group(1), m.group(2)
        if "**Dónde se pide" in cuerpo:
            return m.group(0)
        # «3.8 TOGO 🟡 · 3.9 BENÍN 🟡» lleva dos países en el mismo encabezado
        crudo = re.sub(r"^\d+(\.\d+)?\s*", "", titulo)
        trozos = [re.sub(r"\d+(\.\d+)?|[🟢🟡🟠🔴*_]|—.*$", "", t).strip()
                  for t in crudo.split("·")]
        bloques = ""
        for t in trozos:
            slug = slug_de(t)
            if slug:
                etiqueta = ("Dónde se pide" if len(trozos) == 1
                            else f"Dónde se pide · {t.title()}")
                bloques += bloque_pais(slug, etiqueta)
        if not bloques:
            return m.group(0)
        return f"## {titulo}\n{cuerpo.rstrip()}\n{bloques}\n"

    md = re.sub(r"^## (3\.\d+ [^\n]+)\n(.*?)(?=^## |\Z)", inserta, md, flags=re.M | re.S)

    DOSIER.write_text(md, encoding="utf-8")
    print("dosier actualizado")


if __name__ == "__main__":
    main()

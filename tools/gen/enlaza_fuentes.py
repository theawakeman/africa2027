# -*- coding: utf-8 -*-
"""Convierte en enlaces cliclables cualquier referencia externa del texto.

Se aplica a TODAS las páginas de la app, al final del render. Detecta, en el
texto visible (nunca dentro de un enlace, un <script>, un <style> ni un
atributo):

  1. URLs completas escritas a pelo:  https://mawf.gov.na/...
  2. Dominios sueltos citados en prosa o entre `comillas`:  tzembassy.go.tz
  3. Direcciones de correo:  zoosanitary@mifugo.go.tz  ->  mailto:
  4. Nombres de fuentes conocidas:  iOverlander, Tracks4Africa, SANParks...

Criterios para que no quede recargado ni se cuelen falsos positivos:
  - Los dominios solo se reconocen si terminan en una extensión de la lista
    blanca, así «data_common.py» o «index.html» nunca se convierten en enlace.
  - Los nombres de fuentes se enlazan una sola vez por bloque (párrafo, celda,
    elemento de lista o encabezado).
  - Todo sale con target="_blank" y rel="noopener", para no perder la página.
"""
import re

# ---------------------------------------------------------------- dominios

# Terminaciones admitidas. Lista blanca a propósito: evita que rutas de
# archivo («build.py», «site.css») acaben convertidas en enlaces.
TLD = r"""(?:
    go\.tz|gov\.(?:na|za|bw|ma|ke|ug|rw|zm|mw|mz|zw|ls|sz|ao|cm|cd|cg|sn|gm|gh|ng|ci|tg|bj|ml|mr|es|uk|us)
  | gouv\.(?:sn|ci|ga|cd|cg|ml|bf|tg|bj|mr|fr)
  | gob\.es
  | co\.(?:za|tz|ke|ug|bw|zw|mz|ao|uk)
  | org\.(?:za|na|zm|uk)
  | com\.(?:na|au|br|es)
  | ac\.(?:za|tz|ke|uk)
  | or\.(?:tz|ke)
  | com|org|net|info|int|travel|africa|africa|eu|es|fr|pt|it|de|be|nl|ch
  | za|na|bw|zm|zw|tz|ke|ug|rw|mw|mz|ls|sz|ao|cm|cd|cg|ga|sn|gm|gh|ng|ci|tg|bj|ma|mr|mg
)"""

RE_URL = re.compile(r"""(?<![\w/@.])(https?://[^\s<>"'()\[\]]+[^\s<>"'()\[\].,;:!?])""")

RE_MAIL = re.compile(r"""(?<![\w.+-])([A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.""" + TLD + r""")(?![\w.-])""",
                     re.X)

RE_DOMINIO = re.compile(r"""(?<![\w/@.\-])((?:www\.)?[a-z0-9][a-z0-9-]{1,}(?:\.[a-z0-9-]+)*\."""
                        + TLD + r""")(?![\w@.\-])""", re.X)


# ------------------------------------------------------------ fuentes con nombre

FUENTES = {
    "iOverlander":        "https://www.ioverlander.com/",
    "Tracks4Africa":      "https://tracks4africa.co.za/",
    "Horizons Unlimited": "https://www.horizonsunlimited.com/",
    "The Pack Track":     "https://www.thepacktrack.com/",
    "SANParks":           "https://www.sanparks.org/",
    "Peace Parks":        "https://www.peaceparks.org/",
    "OpenStreetMap":      "https://www.openstreetmap.org/",
    "Wikimedia Commons":  "https://commons.wikimedia.org/",
    "Wikiloc":            "https://es.wikiloc.com/",
    "AllTrails":          "https://www.alltrails.com/",
    "Wikivoyage":         "https://es.wikivoyage.org/",
    "Lonely Planet":      "https://www.lonelyplanet.com/",
    "Caravanistan":       "https://caravanistan.com/",
    "UNESCO":             "https://whc.unesco.org/es/list/",
    "Exteriores":         "https://www.exteriores.gob.es/es/ServiciosAlCiudadano/Paginas/"
                          "recomendaciones-de-viaje.aspx",
    "OMS":                "https://www.who.int/es",
    "WOAH":               "https://www.woah.org/es/inicio/",
    "FAO":                "https://www.fao.org/home/es",
}

# Se prueban primero los nombres largos: «The Pack Track» antes que «Track».
RE_FUENTES = re.compile(
    "(?<![\\w])(" + "|".join(re.escape(k) for k in sorted(FUENTES, key=len, reverse=True)) + ")(?![\\w])"
)

# ------------------------------------------------------------------ recorrido

# Etiquetas cuyo contenido no se toca nunca.
OPACAS = ("script", "style", "textarea", "head", "title", "a")

TROZOS = re.compile(r"(<[^>]+>)")
ABRE = re.compile(r"<\s*([a-zA-Z][\w-]*)")
CIERRA = re.compile(r"<\s*/\s*([a-zA-Z][\w-]*)")
AUTOCIERRA = re.compile(r"/\s*>$")

# Bloques dentro de los cuales una misma fuente solo se enlaza una vez.
BLOQUE = ("p", "li", "td", "th", "h1", "h2", "h3", "h4", "h5", "h6", "figcaption", "summary")


def _a(href, texto, clase="fuente"):
    return (f'<a class="{clase}" href="{href}" target="_blank" rel="noopener">{texto}</a>')


def _corta(url, maximo=58):
    """Texto visible para una URL larga: dominio + final reconocible."""
    if len(url) <= maximo:
        return url
    return url[:maximo - 1] + "…"


def _enlaza_texto(texto, usados):
    """Enlaza las referencias externas de un fragmento ya libre de etiquetas."""
    if "&" in texto:
        # Los & del HTML ya vienen escapados; para las URLs hay que deshacerlo
        # solo al construir el href, no en el texto visible.
        pass

    # 1) URLs completas
    def _url(m):
        bruto = m.group(1)
        href = bruto.replace("&amp;", "&")
        return _a(href, _corta(bruto))
    texto = RE_URL.sub(_url, texto)

    # 2) Correos
    texto = RE_MAIL.sub(lambda m: _a("mailto:" + m.group(1), m.group(1)), texto)

    # 3) Dominios sueltos
    def _dom(m):
        d = m.group(1)
        return _a("https://" + d, d)
    texto = RE_DOMINIO.sub(_dom, texto)

    # 4) Fuentes con nombre, una vez por bloque
    def _fuente(m):
        nombre = m.group(1)
        if nombre in usados:
            return nombre
        usados.add(nombre)
        return _a(FUENTES[nombre], nombre)
    texto = RE_FUENTES.sub(_fuente, texto)

    return texto


def enlazar_fuentes(html):
    """Devuelve el HTML con todas las referencias externas convertidas en enlaces."""
    partes = TROZOS.split(html)
    pila_opaca = 0
    usados = set()
    salida = []

    for trozo in partes:
        if trozo.startswith("<"):
            salida.append(trozo)
            c = CIERRA.match(trozo)
            if c:
                if c.group(1).lower() in OPACAS and pila_opaca:
                    pila_opaca -= 1
                if c.group(1).lower() in BLOQUE:
                    usados = set()
                continue
            a = ABRE.match(trozo)
            if a and not AUTOCIERRA.search(trozo):
                nombre = a.group(1).lower()
                if nombre in OPACAS:
                    pila_opaca += 1
                elif nombre in BLOQUE:
                    usados = set()
            continue

        if pila_opaca or not trozo.strip():
            salida.append(trozo)
        else:
            salida.append(_enlaza_texto(trozo, usados))

    return "".join(salida)

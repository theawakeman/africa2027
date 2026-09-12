# -*- coding: utf-8 -*-
"""Hace cliclables las referencias internas del tipo «§4» o «§1.1».

A diferencia de los nombres de país, que eran ruido, estas referencias sí
hacen falta: apuntan al sitio exacto donde está desarrollado lo que se acaba
de afirmar. Lo que no puede ser es que se queden en texto muerto.

Cada §N se convierte en un salto al encabezado correspondiente de la misma
página, y lleva en el atributo `title` el nombre de esa sección, de modo que
al pasar el ratón por encima se lee adónde va sin necesidad de ir.
"""
import re

# «## 3.16 TANZANIA 🟡 — *el caso...*»  ->  numero 3.16
ENCABEZADO = re.compile(r"^(#{1,4})\s+((\d+(?:\.\d+)?)\.?\s+.+?)\s*$", re.M)

REFERENCIA = re.compile(r"§\s?(\d+(?:\.\d+)?)")

# No se tocan los §N que ya estén dentro de un enlace o de un encabezado.
OPACAS = ("a", "script", "style", "h1", "h2", "h3", "h4", "h5", "h6")
TROZOS = re.compile(r"(<[^>]+>)")
ABRE = re.compile(r"<\s*([a-zA-Z][\w-]*)")
CIERRA = re.compile(r"<\s*/\s*([a-zA-Z][\w-]*)")
AUTOCIERRA = re.compile(r"/\s*>$")


def _limpia(titulo):
    """Título legible: sin markdown, sin emoji de dificultad, sin coletillas."""
    t = re.sub(r"[*_`]", "", titulo)
    t = re.sub(r"\s*[—–-]\s*$", "", t)
    t = "".join(c for c in t if c.isprintable() and not (0x1F300 <= ord(c) <= 0x1FAFF))
    return re.sub(r"\s+", " ", t).strip()


def indice(md):
    """{'4': ('4-la-vuelta-a-la-ue', 'La vuelta a la UE'), ...}"""
    out = {}
    for m in ENCABEZADO.finditer(md):
        texto, numero = m.group(2), m.group(3)
        # El ancla se calcula sobre el texto EXACTO del encabezado, igual que
        # hace md_mini; cualquier reconstrucción daría un ancla que no existe.
        ancla = re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")[:60]
        titulo = _limpia(texto[len(numero):].lstrip(". "))
        out.setdefault(numero, (ancla, titulo))
    return out


def enlazar_secciones(html, idx):
    """Convierte cada §N del texto visible en un salto a esa sección."""
    if not idx:
        return html

    def _ref(m):
        numero = m.group(1)
        destino = idx.get(numero)
        if not destino:
            # «§7.5» sin encabezado propio: se cae al capítulo que lo contiene.
            destino = idx.get(numero.split(".")[0])
        if not destino:
            return m.group(0)
        ancla, titulo = destino
        return (f'<a class="sec" href="#{ancla}" title="Ir a {numero}. {titulo}">'
                f'{m.group(0)}</a>')

    partes = TROZOS.split(html)
    opaca = 0
    salida = []
    for trozo in partes:
        if trozo.startswith("<"):
            salida.append(trozo)
            c = CIERRA.match(trozo)
            if c:
                if c.group(1).lower() in OPACAS and opaca:
                    opaca -= 1
                continue
            a = ABRE.match(trozo)
            if a and not AUTOCIERRA.search(trozo) and a.group(1).lower() in OPACAS:
                opaca += 1
            continue
        salida.append(trozo if opaca or "§" not in trozo else REFERENCIA.sub(_ref, trozo))
    return "".join(salida)

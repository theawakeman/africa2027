# -*- coding: utf-8 -*-
"""Convierte en enlaces los nombres de país que aparecen en un texto HTML.

Se usa en la sección del perro: cada vez que el dossier menciona un país,
el nombre lleva al apartado del perro de la ficha de ese país, que es donde
está la matriz canina por zonas y el plan B concreto.

Reglas para que no quede recargado:
  - Solo se enlaza la PRIMERA aparición de cada país dentro de cada bloque
    (párrafo, elemento de lista, celda de tabla o encabezado).
  - Nunca se toca nada que ya esté dentro de un <a>.
  - Se prueban primero los nombres largos, para que «RD Congo» no se coma
    el «Congo» de «Congo-Brazzaville».
"""
import re

from data_countries import C

# Variantes con las que el dossier puede nombrar a cada país.
ALIAS = {
    "sahara-occidental": ["Sáhara Occidental", "Sahara Occidental"],
    "costa-de-marfil":   ["Costa de Marfil", "Côte d'Ivoire"],
    "congo":             ["Congo-Brazzaville", "Congo Brazzaville", "República del Congo",
                          "Congo (Brazzaville)"],
    "rd-congo":          ["República Democrática del Congo", "RD Congo", "RDC", "RD del Congo"],
    "sudafrica":         ["Sudáfrica"],
    "camerun":           ["Camerún"],
    "benin":             ["Benín"],
    "gabon":             ["Gabón"],
    "malaui":            ["Malaui", "Malawi"],
    "esuatini":          ["Esuatini", "Suazilandia"],
    "sierra-leona":      ["Sierra Leona"],
    "guinea":            ["Guinea"],     # cuidado: ver EXCLUIR
    "zimbabue":          ["Zimbabue"],
    "botsuana":          ["Botsuana"],
    "kenia":             ["Kenia"],
    "lesoto":            ["Lesoto"],
}

# Fragmentos donde «Guinea» NO se refiere al país que nos interesa.
EXCLUIR_ANTES = ("Papúa Nueva ", "Nueva ")
EXCLUIR_DESPUES = ("-Bisáu", "-Bissau", " Bisáu", " Bissau", " Ecuatorial", " Conakry")

BLOQUES = re.compile(r"(<(p|li|td|th|h[2-6])(?:\s[^>]*)?>)(.*?)(</\2>)", re.S)
DENTRO_DE_ENLACE = re.compile(r"<a\b[^>]*>.*?</a>", re.S)


def _terminos():
    """[(término, slug)] ordenado de más largo a más corto."""
    fuera = {"fuera", "excluido"}
    out = []
    for slug, name, group, *_ in C:
        if group in fuera:
            continue
        nombres = set(ALIAS.get(slug, []))
        # el nombre del índice puede traer coletillas: «Sahara Occidental (tránsito)»
        nombres.add(re.sub(r"\s*\(.*?\)\s*$", "", name).strip())
        for n in nombres:
            if n:
                out.append((n, slug))
    return sorted(set(out), key=lambda t: -len(t[0]))


TERMINOS = _terminos()


def _enlaza_texto(texto, root, ya_usados):
    """Enlaza la primera aparición de cada país en un fragmento sin etiquetas."""
    for termino, slug in TERMINOS:
        if slug in ya_usados:
            continue
        for m in re.finditer(r"(?<![\w>])" + re.escape(termino) + r"(?![\wáéíóúñ])", texto):
            ini, fin = m.span()
            if any(texto[:ini].endswith(x) for x in EXCLUIR_ANTES):
                continue
            if any(texto[fin:].startswith(x) for x in EXCLUIR_DESPUES):
                continue
            enlace = (f'<a class="paislink" href="{root}paises/{slug}/#perro" '
                      f'title="Ver el apartado del perro en la ficha de {termino}">{termino}</a>')
            texto = texto[:ini] + enlace + texto[fin:]
            ya_usados.add(slug)
            break
    return texto


def enlazar(html, root="../"):
    """Devuelve el HTML con los nombres de país enlazados a su ficha."""
    def por_bloque(m):
        apertura, _, interior, cierre = m.groups()
        ya_usados = set()
        partes, pos = [], 0
        # saltarse lo que ya sea un enlace
        for a in DENTRO_DE_ENLACE.finditer(interior):
            partes.append(_enlaza_texto(interior[pos:a.start()], root, ya_usados))
            partes.append(a.group(0))
            pos = a.end()
        partes.append(_enlaza_texto(interior[pos:], root, ya_usados))
        return apertura + "".join(partes) + cierre

    return BLOQUES.sub(por_bloque, html)


def indice_paises(root="../"):
    """Fila de accesos directos a la ficha de cada país, para la cabecera."""
    fuera = {"fuera", "excluido"}
    chips = []
    for slug, name, group, *_ in C:
        if group in fuera:
            continue
        corto = re.sub(r"\s*\(.*?\)\s*$", "", name).strip()
        chips.append(f'<a class="paischip" href="{root}paises/{slug}/#perro">{corto}</a>')
    return ('<div class="paisidx"><span class="paisidx-lab">Ir al apartado del perro de cada ficha:</span>'
            + "".join(chips) + "</div>")

# -*- coding: utf-8 -*-
"""Conversor mínimo de Markdown a HTML, sin dependencias externas.

Existe para que el sitio pueda renderizar documentos escritos en Markdown
(como el dossier del perro) sin que el build dependa de ningún paquete que
haya que instalar: el workflow de GitHub Actions ejecuta build.py tal cual,
así que todo tiene que salir de la librería estándar.

Cubre el subconjunto que usamos: encabezados, tablas, listas (con y sin
numerar), citas, reglas horizontales, párrafos, negrita, cursiva, código
inline y enlaces.
"""
import re
from site_common import esc

_LINK = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
_BOLD = re.compile(r"\*\*([^*]+)\*\*")
_ITAL = re.compile(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)")
_CODE = re.compile(r"`([^`]+)`")


def _inline(text):
    """Escapa el texto y luego reaplica el formato inline como HTML."""
    out = esc(text)
    out = _CODE.sub(lambda m: f"<code>{m.group(1)}</code>", out)
    out = _LINK.sub(
        lambda m: f'<a href="{m.group(2)}" target="_blank" rel="noopener">{m.group(1)}</a>', out)
    out = _BOLD.sub(lambda m: f"<strong>{m.group(1)}</strong>", out)
    out = _ITAL.sub(lambda m: f"<em>{m.group(1)}</em>", out)
    return out


def _split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def _is_sep(line):
    return bool(re.match(r"^\|[\s:|-]+\|?$", line.strip())) and "-" in line


def md_to_html(md, base_level=2):
    """Convierte Markdown a HTML. base_level desplaza los encabezados para
    encajar en la jerarquía de la página (un '#' del documento pasa a <h2>)."""
    lines = md.replace("\r\n", "\n").split("\n")
    html, i, n = [], 0, len(lines)
    while i < n:
        raw = lines[i]
        s = raw.strip()

        if not s:
            i += 1
            continue

        if re.match(r"^(-{3,}|\*{3,}|_{3,})$", s):
            html.append("<hr>")
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", s)
        if m:
            lvl = min(len(m.group(1)) + base_level - 1, 6)
            text = m.group(2).strip()
            anchor = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]
            html.append(f'<h{lvl} id="{anchor}">{_inline(text)}</h{lvl}>')
            i += 1
            continue

        # Tabla: cabecera + separador + filas
        if s.startswith("|") and i + 1 < n and _is_sep(lines[i + 1]):
            headers = _split_row(s)
            i += 2
            rows = []
            while i < n and lines[i].strip().startswith("|"):
                rows.append(_split_row(lines[i]))
                i += 1
            th = "".join(f"<th>{_inline(h)}</th>" for h in headers)
            tb = ""
            for r in rows:
                r = (r + [""] * len(headers))[:len(headers)]
                tb += "<tr>" + "".join(f"<td>{_inline(c)}</td>" for c in r) + "</tr>"
            html.append(f'<div class="tblwrap"><table><thead><tr>{th}</tr>'
                        f"</thead><tbody>{tb}</tbody></table></div>")
            continue

        # Listas
        m = re.match(r"^([-*]|\d+\.)\s+(.*)$", s)
        if m:
            ordered = not m.group(1) in ("-", "*")
            items = []
            while i < n:
                mm = re.match(r"^([-*]|\d+\.)\s+(.*)$", lines[i].strip())
                if not mm or (not mm.group(1) in ("-", "*")) != ordered:
                    break
                item = mm.group(2).strip()
                i += 1
                # continuación indentada de la misma entrada
                while i < n and lines[i].startswith(("  ", "\t")) and lines[i].strip() \
                        and not re.match(r"^([-*]|\d+\.)\s+", lines[i].strip()):
                    item += " " + lines[i].strip()
                    i += 1
                items.append(item)
            tag = "ol" if ordered else "ul"
            cls = "" if ordered else ' class="ticks"'
            lis = "".join(f"<li>{_inline(x)}</li>" for x in items)
            html.append(f"<{tag}{cls}>{lis}</{tag}>")
            continue

        # Cita
        if s.startswith(">"):
            quote = []
            while i < n and lines[i].strip().startswith(">"):
                quote.append(lines[i].strip().lstrip(">").strip())
                i += 1
            body = " ".join(q for q in quote if q)
            html.append(f'<div class="callout"><p>{_inline(body)}</p></div>')
            continue

        # Bloque de código
        if s.startswith("```"):
            i += 1
            buf = []
            while i < n and not lines[i].strip().startswith("```"):
                buf.append(lines[i])
                i += 1
            i += 1
            html.append(f"<pre><code>{esc(chr(10).join(buf))}</code></pre>")
            continue

        # Párrafo
        para = []
        while i < n and lines[i].strip() and not re.match(
                r"^(#{1,6}\s|\||[-*]\s|\d+\.\s|>|```|(-{3,}|\*{3,}|_{3,})$)", lines[i].strip()):
            para.append(lines[i].strip())
            i += 1
        if para:
            html.append(f"<p>{_inline(' '.join(para))}</p>")

    return "\n".join(html)


def md_headings(md, levels=(1, 2)):
    """Devuelve [(texto, ancla, nivel)] de los encabezados, para el índice."""
    out = []
    for line in md.split("\n"):
        m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if m and len(m.group(1)) in levels:
            text = m.group(2).strip()
            anchor = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]
            out.append((text, anchor, len(m.group(1))))
    return out

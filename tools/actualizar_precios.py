#!/usr/bin/env python3
"""Actualización semanal de precios del Planificador (solo biblioteca estándar).

Lo lanza GitHub Actions cada lunes (.github/workflows/actualizar-precios.yml);
también se puede ejecutar a mano:  python3 tools/actualizar_precios.py

1. Gasóleo: página mundial de GlobalPetrolPrices (USD/l por país, una sola
   petición; su robots.txt lo permite).
2. Cambio euro/dólar: BCE vía api.frankfurter.dev (con el XML del BCE de
   reserva).
3. Visados: descarga cada fuente oficial citada en data_presupuesto.VISADOS,
   se queda con las frases que hablan de visados, precios o tasas y guarda su
   huella. Si cambia, marca la fecha: el Planificador avisa en esa fila hasta
   que alguien revise el importe y ponga la fecha en «confirmado».

Si una parte falla, se conservan los datos anteriores de esa parte y se anota
el error; el script no rompe la publicación.
"""
import datetime as dt
import hashlib
import html
import json
import re
import sys
import time
import urllib.request
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "tools" / "gen"))
from precios_auto import DIR, GPP_PAISES  # noqa: E402

GPP_URL = "https://www.globalpetrolprices.com/diesel_prices/"
CAMBIO_URL = "https://api.frankfurter.dev/v1/latest?from=USD&to=EUR"
BCE_URL = "https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml"
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
      "Chrome/126.0 Safari/537.36 africa2027-precios (+https://github.com/theawakeman/africa2027)")
MESES = {m: i for i, m in enumerate(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"], 1)}
CLAVES = re.compile(r"(visa|visado|e-?visa|fee|frais|tarif|precio|coste|cost|tasa|droits|montant|amount|price|"
                    r"usd|us\$|\$|€|eur\b|euros?|fcfa|xof|cfa|mru|gmd|nad|n\$|dollars?|prix)", re.I)
HOY = dt.date.today().strftime("%d-%m-%Y")


def bajar(url, timeout=40):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "es,en;q=0.8,fr;q=0.6"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode(r.headers.get_content_charset() or "utf-8", "replace")


def leer(nombre):
    try:
        return json.loads((DIR / nombre).read_text(encoding="utf-8"))
    except Exception:
        return {}


def escribir(nombre, datos):
    DIR.mkdir(parents=True, exist_ok=True)
    (DIR / nombre).write_text(json.dumps(datos, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


# ------------------------------------------------------------------ gasóleo
def gasoil_gpp(texto):
    """{'fecha': 'dd-mm-aaaa', 'usd': {pais_url: usd}} a partir del HTML de la página mundial."""
    nombres = re.findall(r'<a href="/([^/"]+)/diesel_prices/" class="graph_outside_link">', texto)
    valores = [float(v) for v in re.findall(r'background: #e2bb04;">\s*<div[^>]*>([\d.]+)</div>', texto)]
    if len(nombres) < 100 or len(nombres) != len(valores):
        raise ValueError(f"formato inesperado: {len(nombres)} países y {len(valores)} precios")
    m = re.search(r"(\d{2})-(\w{3})-(\d{4})", texto)
    fecha = f"{m.group(1)}-{MESES[m.group(2)]:02d}-{m.group(3)}" if m and m.group(2) in MESES else HOY
    usd = dict(zip(nombres, valores))
    if not 0.5 < usd.get("Morocco", 0) < 4:
        raise ValueError("precio de Marruecos fuera de rango")
    return {"fecha": fecha, "usd": usd}


def cambio_usd_eur():
    try:
        j = json.loads(bajar(CAMBIO_URL))
        return float(j["rates"]["EUR"]), dt.date.fromisoformat(j["date"]).strftime("%d-%m-%Y"), CAMBIO_URL
    except Exception:
        x = bajar(BCE_URL)
        usd = float(re.search(r"currency=['\"]USD['\"] rate=['\"]([\d.]+)", x).group(1))
        dia = re.search(r"time=['\"]([\d-]+)", x).group(1)
        return round(1 / usd, 5), dt.date.fromisoformat(dia).strftime("%d-%m-%Y"), BCE_URL


def actualizar_gasoil():
    antes = leer("auto.json")
    nuevo = dict(antes)
    avisos = []
    try:
        eur, dia, fuente = cambio_usd_eur()
        if not 0.5 < eur < 1.5:
            raise ValueError(f"cambio fuera de rango: {eur}")
        nuevo.update(usd_eur=round(eur, 5), ecb_fecha=dia, cambio_fuente=fuente)
    except Exception as e:  # se conserva el cambio anterior
        avisos.append(f"Cambio euro/dólar sin actualizar: {e}")
    try:
        g = gasoil_gpp(bajar(GPP_URL))
        usd = {slug: g["usd"][p] for p, slug in GPP_PAISES.items() if p in g["usd"]}
        viejo = antes.get("gasoil_usd", {})
        for s, v in usd.items():
            if s in viejo and viejo[s] and abs(v / viejo[s] - 1) > 0.35:
                avisos.append(f"{s}: el gasóleo pasa de {viejo[s]} a {v} USD/l (más del 35 %): revisar")
        faltan = sorted(set(viejo) - set(usd))
        if faltan:
            avisos.append("Sin precio esta semana (se mantiene el anterior): " + ", ".join(faltan))
            usd = {**{s: viejo[s] for s in faltan}, **usd}
        nuevo.update(gpp_fecha=g["fecha"], gpp_url=GPP_URL, gasoil_usd=dict(sorted(usd.items())))
    except Exception as e:
        avisos.append(f"Gasóleo sin actualizar: {e}")
    nuevo["actualizado"] = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    nuevo["avisos"] = avisos
    if nuevo.get("gasoil_usd") and nuevo.get("usd_eur"):
        escribir("auto.json", nuevo)
    return avisos


# ------------------------------------------------------------------ visados
def frases(texto):
    texto = re.sub(r"(?is)<(script|style|noscript|svg|head)[^>]*>.*?</\1>", " ", texto)
    texto = re.sub(r"(?i)<br\s*/?>|</(p|div|li|tr|td|th|h\d|section|article)>", "\n", texto)
    texto = html.unescape(re.sub(r"<[^>]+>", " ", texto))
    lineas = [re.sub(r"\s+", " ", l).strip() for l in texto.split("\n")]
    return [l for l in lineas if 12 <= len(l) <= 1200 and CLAVES.search(l)]


def vigilar_visados():
    from data_presupuesto import VISADOS
    fuentes = {}
    for slug, (_eur, _txt, url) in VISADOS.items():
        fuentes.setdefault(url, []).append(slug)
    antes = leer("vigilancia.json").get("fuentes", {})
    salida, avisos = {}, []
    for url, paises in sorted(fuentes.items()):
        f = dict(antes.get(url, {}))
        f["paises"] = sorted(paises)
        f.setdefault("confirmado", HOY)
        try:
            lineas = frases(bajar(url))
            if not lineas:
                raise ValueError("sin texto útil (¿página con JavaScript o bloqueada?)")
            huella = hashlib.sha1("\n".join(lineas).encode("utf-8")).hexdigest()
            if f.get("huella") and f["huella"] != huella:
                f["cambiado"] = HOY
                avisos.append(f"La fuente de {', '.join(paises)} ha cambiado: {url}")
            f.update(huella=huella, revisado=HOY, estado="ok", extracto=" · ".join(lineas)[:500])
        except Exception as e:
            f.update(revisado=HOY, estado=f"error: {str(e)[:160]}")
        salida[url] = f
        time.sleep(1.5)
    escribir("vigilancia.json", {"actualizado": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%MZ"),
                                 "fuentes": salida})
    return avisos


if __name__ == "__main__":
    solo = sys.argv[1] if len(sys.argv) > 1 else ""
    avisos = []
    if solo in ("", "gasoil"):
        avisos += actualizar_gasoil()
    if solo in ("", "visados"):
        avisos += vigilar_visados()
    print("\n".join(avisos) if avisos else "Precios actualizados sin avisos.")

# -*- coding: utf-8 -*-
"""Precios que se actualizan solos cada semana.

Los escribe tools/actualizar_precios.py (lo lanza GitHub Actions, ver
.github/workflows/actualizar-precios.yml) en content/precios/:

  auto.json        gasóleo de GlobalPetrolPrices (USD/l por país) y cambio
                   euro/dólar del BCE.
  vigilancia.json  huella del texto de cada fuente de visados: si la página
                   oficial cambia, el Planificador avisa hasta que alguien
                   revisa el importe y pone la fecha en «confirmado».

Si los archivos no existen o están rotos, la web usa los valores escritos a
mano en data_presupuesto.py y data_ruta.py.
"""
import json
from pathlib import Path

DIR = Path(__file__).resolve().parents[2] / "content" / "precios"

# Nombre del país en la URL de GlobalPetrolPrices → slug de la web.
GPP_PAISES = {
    "Morocco": "marruecos", "Senegal": "senegal", "Guinea": "guinea", "Ivory-Coast": "costa-de-marfil",
    "Ghana": "ghana", "Togo": "togo", "Benin": "benin", "Nigeria": "nigeria", "Cameroon": "camerun",
    "Democratic-Republic-of-the-Congo": "rd-congo", "Angola": "angola", "Zambia": "zambia", "Malawi": "malaui",
    "Tanzania": "tanzania", "Kenya": "kenia", "Mozambique": "mozambique", "Zimbabwe": "zimbabue",
    "Botswana": "botsuana", "South-Africa": "sudafrica", "Namibia": "namibia", "Sierra-Leone": "sierra-leona",
    "Liberia": "liberia", "Gabon": "gabon", "Uganda": "uganda", "Rwanda": "ruanda", "Swaziland": "esuatini",
    "Lesotho": "lesoto", "Ethiopia": "etiopia", "Egypt": "egipto", "Tunisia": "tunez", "Algeria": "argelia",
    "Burundi": "burundi", "Libya": "libia", "Niger": "niger", "Burkina-Faso": "burkina-faso", "Mali": "mali",
    "Sudan": "sudan", "Central-African-Republic": "rca", "Madagascar": "madagascar", "Cape-Verde": "cabo-verde",
    "Mauritius": "mauricio", "Seychelles": "seychelles",
    # Europa (carretera hasta el ferry)
    "Spain": "eu:es", "France": "eu:fr", "Italy": "eu:it",
}


def _leer(nombre):
    try:
        return json.loads((DIR / nombre).read_text(encoding="utf-8"))
    except Exception:
        return {}


def auto():
    """{'usd_eur', 'ecb_fecha', 'gpp_fecha', 'gasoil_usd': {slug: usd}, 'actualizado'} o {}."""
    d = _leer("auto.json")
    if not isinstance(d.get("gasoil_usd"), dict) or not d.get("usd_eur"):
        return {}
    return d


def vigilancia():
    """{url: {'huella', 'revisado', 'cambiado', 'confirmado', 'estado', 'extracto'}}."""
    d = _leer("vigilancia.json")
    return d.get("fuentes", {}) if isinstance(d, dict) else {}


def aviso_fuente(url):
    """Fecha (dd-mm-aaaa) del cambio detectado en la fuente si aún no se ha revisado; si no, ''."""
    f = vigilancia().get(url) or {}
    cambio, conf = f.get("cambiado") or "", f.get("confirmado") or ""
    iso = lambda s: s[6:10] + s[3:5] + s[0:2] if len(s) == 10 else ""
    return cambio if cambio and iso(cambio) > iso(conf) else ""

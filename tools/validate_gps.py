#!/usr/bin/env python3
"""Comprueba que los PDIs y los puntos de logística caen donde deben.

Uso: python3 tools/validate_gps.py [slug ...]    (sin argumentos, todos)

Qué mira, por orden de gravedad:

1. ERROR · la coordenada cae FUERA de la caja del país. Es el fallo que de verdad
   duele: un signo cambiado (Tiébélé a +0,96 en vez de -0,96 son 210 km) o una
   latitud y una longitud intercambiadas. Los puntos de logística que están fuera
   a propósito -embajadas en terceros países- se avisan aparte, no como error.
2. ERROR · latitud y longitud intercambiadas: si al permutarlas el punto entra en
   la caja, casi seguro que es eso.
3. AVISO · menos de tres decimales. Una coordenada redondeada a dos decimales
   tiene hasta 1,1 km de error y suele ser señal de que se perdieron dígitos por
   el camino.
4. AVISO · dos puntos con la misma coordenada exacta.
5. AVISO · un PDI a más de 600 km de la mediana de los demás del país. En países
   grandes es normal (Chad, Argelia, Mali), así que es solo para mirarlo.

No sustituye a comprobar el pin en Google Maps: dice que la coordenada es
plausible, no que el objeto sea el correcto.
"""
import importlib.util
import math
import statistics
import sys
from pathlib import Path

GEN = Path(__file__).resolve().parent / "gen"

# lat_min, lat_max, lon_min, lon_max — con margen generoso sobre la frontera real
CAJAS = {
    "marruecos": (27.5, 36.1, -13.3, -0.8), "sahara-occidental": (20.6, 27.8, -17.3, -8.5),
    "mauritania": (14.6, 27.4, -17.2, -4.7), "senegal": (12.2, 16.8, -17.7, -11.2),
    "gambia": (12.9, 14.0, -17.1, -13.6), "guinea": (7.0, 12.8, -15.2, -7.5),
    "sierra-leona": (6.8, 10.1, -13.5, -10.1), "liberia": (4.2, 8.7, -11.6, -7.2),
    "costa-de-marfil": (4.2, 10.9, -8.8, -2.3), "ghana": (4.6, 11.3, -3.4, 1.4),
    "togo": (6.0, 11.3, -0.3, 2.0), "benin": (6.1, 12.6, 0.6, 4.0),
    "nigeria": (4.1, 14.0, 2.5, 14.8), "camerun": (1.5, 13.2, 8.3, 16.3),
    "gabon": (-4.1, 2.5, 8.5, 14.7), "congo": (-5.2, 3.9, 11.0, 18.8),
    "rd-congo": (-13.6, 5.5, 12.1, 31.5), "angola": (-18.2, -4.2, 11.5, 24.2),
    "namibia": (-29.1, -16.8, 11.6, 25.4), "sudafrica": (-35.1, -22.0, 16.3, 33.1),
    "mozambique": (-27.0, -10.3, 30.1, 41.0), "malaui": (-17.3, -9.2, 32.5, 36.0),
    "tanzania": (-11.9, -0.8, 29.2, 40.6), "kenia": (-4.9, 5.2, 33.8, 42.0),
    "etiopia": (3.2, 15.0, 32.8, 48.1), "sudan": (8.5, 22.4, 21.7, 38.7),
    "egipto": (21.8, 31.8, 24.5, 37.0), "lesoto": (-30.8, -28.4, 26.9, 29.6),
    "esuatini": (-27.5, -25.6, 30.7, 32.3), "zimbabue": (-22.6, -15.5, 25.1, 33.2),
    "botsuana": (-27.0, -17.6, 19.8, 29.5), "zambia": (-18.2, -8.1, 21.8, 33.8),
    "uganda": (-1.6, 4.4, 29.4, 35.2), "ruanda": (-3.0, -0.9, 28.7, 31.0),
    "yibuti": (10.8, 12.9, 41.6, 43.6), "madagascar": (-25.8, -11.8, 43.0, 50.7),
    "tunez": (30.1, 37.7, 7.4, 11.8), "mali": (10.0, 25.2, -12.4, 4.4),
    "guinea-bisau": (10.7, 12.8, -16.9, -13.5), "argelia": (18.8, 37.2, -8.8, 12.1),
    "libia": (19.3, 33.3, 9.2, 25.3), "burkina-faso": (9.3, 15.2, -5.7, 2.6),
    "niger": (11.5, 23.7, 0.0, 16.1), "chad": (7.3, 23.6, 13.3, 24.2),
    "rca": (2.1, 11.2, 14.3, 27.6), "sudan-del-sur": (3.3, 12.4, 24.0, 36.0),
    "eritrea": (12.2, 18.2, 36.3, 43.3), "somalia": (-1.8, 12.1, 40.8, 51.6),
    "cabo-verde": (14.6, 17.4, -25.6, -22.5), "santo-tome": (-0.2, 1.9, 6.3, 7.6),
    "guinea-ecuatorial": (-1.7, 3.9, 5.4, 11.5), "comoras": (-12.6, -11.2, 43.1, 44.7),
    "seychelles": (-10.4, -3.6, 46.0, 56.5), "mauricio": (-20.7, -10.1, 56.3, 63.7),
    "burundi": (-4.6, -2.2, 28.8, 31.0),
}


def dentro(caja, lat, lon):
    a, b, c, d = caja
    return a <= lat <= b and c <= lon <= d


def dist(a, b, c, d):
    r = 6371.0
    p1, p2 = math.radians(a), math.radians(c)
    dp, dl = math.radians(c - a), math.radians(d - b)
    h = math.sin(dp / 2) ** 2 + math.cos(p1) * math.cos(p2) * math.sin(dl / 2) ** 2
    return 2 * r * math.asin(math.sqrt(h))


def decimales(x):
    s = repr(float(x))
    return len(s.split(".")[1].rstrip("0")) if "." in s else 0


def carga(slug):
    f = GEN / f"data_{slug.replace('-', '_')}.py"
    if not f.exists():
        return None
    spec = importlib.util.spec_from_file_location(f"data_{slug}", f)
    sys.path.insert(0, str(GEN))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def puntos(m):
    for p in getattr(m, "POIS", []):
        yield "PDI", p["n"], p["name"], float(p["lat"]), float(p["lon"])
    for i, l in enumerate(getattr(m, "LOGISTICS", []), 1):
        yield "LOG", i, l[0], float(l[2]), float(l[3])


def revisa(slug):
    caja = CAJAS.get(slug)
    m = carga(slug)
    if m is None:
        return None
    if caja is None:
        print(f"{slug}: sin caja definida en CAJAS, no se puede comprobar")
        return None
    errores, avisos, vistos, coords = [], [], {}, []
    for tipo, n, nombre, lat, lon in puntos(m):
        et = f"{tipo} {n} · {nombre[:44]}"
        if not dentro(caja, lat, lon):
            if dentro(caja, lon, lat):
                errores.append(f"{et}: lat/lon INTERCAMBIADAS ({lat}, {lon})")
            elif tipo == "LOG":
                avisos.append(f"{et}: fuera del país ({lat}, {lon}) — ¿embajada en tercer país?")
            else:
                errores.append(f"{et}: FUERA DE {slug.upper()} ({lat}, {lon})")
        elif tipo == "PDI":
            coords.append((n, nombre, lat, lon))
        if min(decimales(lat), decimales(lon)) < 3:
            avisos.append(f"{et}: pocos decimales ({lat}, {lon})")
        clave = (round(lat, 6), round(lon, 6))
        if clave in vistos:
            avisos.append(f"{et}: misma coordenada que {vistos[clave]}")
        vistos[clave] = et
    if len(coords) >= 5:
        mlat = statistics.median(c[2] for c in coords)
        mlon = statistics.median(c[3] for c in coords)
        for n, nombre, lat, lon in coords:
            d = dist(mlat, mlon, lat, lon)
            if d > 600:
                avisos.append(f"PDI {n} · {nombre[:44]}: a {d:.0f} km del centro del país")
    estado = "ERROR" if errores else ("avisos" if avisos else "OK")
    print(f"{slug}: {estado} · {len(list(puntos(m)))} puntos")
    for e in errores:
        print(f"   ERROR  {e}")
    for a in avisos:
        print(f"   aviso  {a}")
    return not errores


if __name__ == "__main__":
    slugs = sys.argv[1:] or sorted(CAJAS)
    malos = [s for s in slugs if revisa(s) is False]
    if malos:
        print("\nCon errores:", ", ".join(malos))
        sys.exit(1)

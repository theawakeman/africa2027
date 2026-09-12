# -*- coding: utf-8 -*-
"""Auditoría de coordenadas de todos los PDIs y puntos de logística.

Comprueba, sin necesidad de red:
  1. Que cada punto cae dentro (o muy cerca) de las fronteras de su país.
  2. Si parece que se han intercambiado latitud y longitud.
  3. Puntos duplicados exactos dentro del mismo país.
  4. Coordenadas sospechosamente redondas (suelen ser estimaciones).
  5. Puntos muy alejados del corredor declarado del país.

Uso:  python3 audit_gps.py [--csv salida.csv]
"""
import importlib
import math
import sys

from data_countries import C

# (lat_min, lat_max, lon_min, lon_max) aproximados de cada país.
# Margen de tolerancia aparte: los pasos fronterizos caen por definición en el borde.
BBOX = {
    "marruecos":        (27.6, 36.0, -13.3, -0.9),
    "sahara-occidental":(20.7, 27.8, -17.2, -8.6),
    "mauritania":       (14.7, 27.3, -17.2, -4.8),
    "senegal":          (12.2, 16.8, -17.6, -11.3),
    "gambia":           (13.0, 13.9, -17.0, -13.7),
    "guinea":           ( 7.1, 12.8, -15.2, -7.6),
    "sierra-leona":     ( 6.8, 10.1, -13.4, -10.2),
    "liberia":          ( 4.2,  8.6, -11.6, -7.3),
    "costa-de-marfil":  ( 4.2, 10.8,  -8.7, -2.4),
    "ghana":            ( 4.6, 11.2,  -3.3,  1.3),
    "togo":             ( 6.0, 11.2,  -0.2,  1.9),
    "benin":            ( 6.1, 12.5,   0.7,  3.9),
    "nigeria":          ( 4.2, 13.9,   2.6, 14.7),
    "camerun":          ( 1.6, 13.1,   8.4, 16.2),
    "gabon":            (-4.0,  2.4,   8.6, 14.6),
    "congo":            (-5.1,  3.8,  11.1, 18.7),
    "rd-congo":         (-13.5, 5.4,  12.1, 31.4),
    "angola":           (-18.1,-4.3,  11.6, 24.1),
    "zambia":           (-18.1,-8.2,  21.9, 33.8),
    "tanzania":         (-11.8,-0.9,  29.3, 40.5),
    "kenia":            (-4.7,  5.1,  33.9, 41.9),
    "uganda":           (-1.5,  4.3,  29.5, 35.1),
    "ruanda":           (-2.9, -1.0,  28.8, 30.9),
    "malaui":           (-17.2,-9.3,  32.6, 36.0),
    "mozambique":       (-27.0,-10.4, 30.2, 40.9),
    "zimbabue":         (-22.5,-15.6, 25.2, 33.1),
    "botsuana":         (-27.0,-17.7, 19.9, 29.4),
    "sudafrica":        (-35.0,-22.1, 16.4, 33.0),
    "namibia":          (-29.0,-16.9, 11.7, 25.3),
    "lesoto":           (-30.7,-28.5, 27.0, 29.5),
    "esuatini":         (-27.4,-25.7, 30.7, 32.2),
    "madagascar":       (-25.7,-11.9, 43.2, 50.5),
}

MARGEN_GRADOS = 0.35        # ~38 km: tolerancia para pasos fronterizos
LEJOS_CORREDOR_KM = 400     # aviso si un PDI queda a más de esto del corredor


def km(a, b):
    """Distancia aproximada en km entre (lat,lon)."""
    la1, lo1, la2, lo2 = map(math.radians, (a[0], a[1], b[0], b[1]))
    dla, dlo = la2 - la1, lo2 - lo1
    h = math.sin(dla/2)**2 + math.cos(la1)*math.cos(la2)*math.sin(dlo/2)**2
    return 6371 * 2 * math.asin(math.sqrt(h))


def fuera(bb, lat, lon, margen=0.0):
    la0, la1, lo0, lo1 = bb
    d_lat = max(la0 - margen - lat, lat - (la1 + margen), 0)
    d_lon = max(lo0 - margen - lon, lon - (lo1 + margen), 0)
    return d_lat, d_lon


def main():
    hallazgos = []
    revisados = 0

    for slug, name, group, *_ in C:
        mod = "data_" + slug.replace("-", "_")
        try:
            d = importlib.import_module(mod).get_data()
        except ModuleNotFoundError:
            continue
        bb = BBOX.get(slug)
        corredor = list(d.get("corridor", [])) + list(d.get("corridor_alt", []))

        FUERA_OK = ("embajada", "consulado", "consular", "referencia", "fuera de la ruta",
                    "cobertura", "competente")
        puntos = [("PDI", p["name"], p["lat"], p["lon"], False) for p in d["pois"]]
        puntos += [("LOG", l["name"], l["lat"], l["lon"],
                    any(w in (l["name"] + " " + l.get("cat", "")).lower() for w in FUERA_OK))
                   for l in d["logistics"]]

        vistos = {}
        for tipo, nombre, lat, lon, extranjero_ok in puntos:
            revisados += 1

            if lat is None or lon is None:
                hallazgos.append((slug, name, tipo, nombre, lat, lon, "GRAVE", "sin coordenadas"))
                continue

            if not (-90 <= lat <= 90 and -180 <= lon <= 180):
                hallazgos.append((slug, name, tipo, nombre, lat, lon, "GRAVE", "fuera de rango"))
                continue

            if bb and not extranjero_ok:
                d_lat, d_lon = fuera(bb, lat, lon, MARGEN_GRADOS)
                if d_lat or d_lon:
                    desv = max(d_lat, d_lon) * 111
                    # ¿estarían bien si se intercambian lat y lon?
                    sw_lat, sw_lon = fuera(bb, lon, lat, MARGEN_GRADOS)
                    nota = "lat/lon INTERCAMBIADAS" if not (sw_lat or sw_lon) else \
                           f"fuera del país por ~{desv:.0f} km"
                    nivel = "GRAVE" if desv > 120 else "REVISAR"
                    hallazgos.append((slug, name, tipo, nombre, lat, lon, nivel, nota))
                    continue

            clave = (round(lat, 4), round(lon, 4))
            if tipo == "PDI":
                if clave in vistos:
                    hallazgos.append((slug, name, tipo, nombre, lat, lon, "REVISAR",
                                      f"dos PDIs distintos en el mismo punto: «{vistos[clave]}»"))
                else:
                    vistos[clave] = nombre

            # Coordenadas demasiado redondas: casi siempre son estimaciones
            if abs(lat*100 - round(lat*100)) < 1e-9 and abs(lon*100 - round(lon*100)) < 1e-9:
                if (abs(lat*10 - round(lat*10)) < 1e-9 and abs(lon*10 - round(lon*10)) < 1e-9):
                    hallazgos.append((slug, name, tipo, nombre, lat, lon, "IMPRECISA",
                                      "coordenada redondeada a 0,1° (~11 km)"))

            if tipo == "PDI" and corredor:
                dmin = min(km((lat, lon), c) for c in corredor)
                if dmin > LEJOS_CORREDOR_KM:
                    hallazgos.append((slug, name, tipo, nombre, lat, lon, "REVISAR",
                                      f"a {dmin:.0f} km del corredor más cercano"))

    orden = {"GRAVE": 0, "REVISAR": 1, "IMPRECISA": 2}
    hallazgos.sort(key=lambda h: (orden[h[6]], h[0]))

    print(f"Revisados {revisados} puntos de {len(BBOX)} países\n")
    for nivel in ("GRAVE", "REVISAR", "IMPRECISA"):
        sub = [h for h in hallazgos if h[6] == nivel]
        print(f"== {nivel}: {len(sub)} ==")
        for slug, pais, tipo, nombre, lat, lon, _, nota in sub:
            print(f"  [{pais[:14]:14}] {tipo} {nombre[:46]:46} {lat:9.4f},{lon:9.4f}  {nota}")
        print()

    if "--csv" in sys.argv:
        import csv
        path = sys.argv[sys.argv.index("--csv") + 1]
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["slug", "pais", "tipo", "nombre", "lat", "lon", "nivel", "nota"])
            w.writerows(hallazgos)
        print(f"CSV escrito en {path}")


if __name__ == "__main__":
    main()

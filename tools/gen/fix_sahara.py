"""Separa el Sáhara Occidental de Marruecos en assets/js/africa.geo.json.

El contorno de origen trae Marruecos con el Sáhara Occidental dentro y un «W. Sahara»
parcial, así que el mapa decía «Marruecos» en Dajla o en Guerguerat. Se deja:
  · sahara-occidental = su contorno ∪ (Marruecos al sur de 27°40' N, el paralelo de la frontera)
  · marruecos          = Marruecos al norte de 27°40' N
Uso: python3 tools/gen/fix_sahara.py   (necesita shapely; se ejecuta una vez tras gen_geo.py)
"""
import json
from pathlib import Path
from shapely.geometry import shape, mapping, box
from shapely.ops import unary_union

GEO = Path(__file__).resolve().parents[2] / "assets/js/africa.geo.json"
LAT = 27.6667          # frontera Marruecos–Sáhara Occidental (27°40' N)


def a_json(g):
    g = g.buffer(0).simplify(0.01)
    polys = [g] if g.geom_type == "Polygon" else list(g.geoms)
    polys = [p for p in polys if p.area > 0.01]
    coords = [[[[round(x, 3), round(y, 3)] for x, y in p.exterior.coords]] for p in polys]
    return {"type": "Polygon", "coordinates": coords[0]} if len(coords) == 1 else {"type": "MultiPolygon", "coordinates": coords}


def main():
    d = json.loads(GEO.read_text(encoding="utf-8"))
    f = {x["properties"]["slug"]: x for x in d["features"]}
    ma, ws = shape(f["marruecos"]["geometry"]).buffer(0), shape(f["sahara-occidental"]["geometry"]).buffer(0)
    sur = box(-20, 15, 0, LAT)
    ws_n = unary_union([ws, ma.intersection(sur)])
    ma_n = ma.difference(sur).difference(ws_n)
    f["sahara-occidental"]["geometry"] = a_json(ws_n)
    f["marruecos"]["geometry"] = a_json(ma_n)
    GEO.write_text(json.dumps(d, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"marruecos {ma.area:.1f} → {ma_n.area:.1f} · sahara-occidental {ws.area:.1f} → {ws_n.area:.1f}")


if __name__ == "__main__":
    main()

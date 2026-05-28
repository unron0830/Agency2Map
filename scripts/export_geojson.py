"""Export Agency2Map resource rows as GeoJSON features."""

from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "sample_output" / "resource_items_scored.csv"
FALLBACK_INPUT = ROOT / "sample_data" / "resource_items.csv"
OUTPUT = ROOT / "sample_output" / "resource_items.geojson"


def load_rows() -> list[dict[str, str]]:
    source = INPUT if INPUT.exists() else FALLBACK_INPUT
    with source.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def to_feature(row: dict[str, str]) -> dict:
    lon = float(row.get("longitude") or 0)
    lat = float(row.get("latitude") or 0)
    properties = {k: v for k, v in row.items() if k not in {"longitude", "latitude"}}
    return {
        "type": "Feature",
        "properties": properties,
        "geometry": {
            "type": "Point",
            "coordinates": [lon, lat],
        },
    }


def main() -> None:
    features = [
        to_feature(row)
        for row in load_rows()
        if row.get("longitude") and row.get("latitude")
    ]
    collection = {
        "type": "FeatureCollection",
        "name": "resource_items",
        "features": features,
    }
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(collection, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()


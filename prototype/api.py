from __future__ import annotations

import csv
import json
from pathlib import Path
from typing import Optional

from fastapi import FastAPI, Query


ROOT = Path(__file__).resolve().parents[1]
RESOURCE_CSV = ROOT / "sample_output" / "resource_items_scored.csv"
RESOURCE_FALLBACK = ROOT / "sample_data" / "resource_items.csv"
SOURCE_CSV = ROOT / "sample_data" / "sources.csv"
GAPS_JSON = ROOT / "sample_output" / "gaps.json"

app = FastAPI(
    title="Agency2Map API",
    description="跨部會資源投入追蹤與空間化治理元件 API prototype",
    version="0.1.0",
)


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def resources() -> list[dict[str, str]]:
    return read_csv(RESOURCE_CSV if RESOURCE_CSV.exists() else RESOURCE_FALLBACK)


def filter_rows(rows: list[dict[str, str]], **filters: Optional[str]) -> list[dict[str, str]]:
    filtered = rows
    for key, value in filters.items():
        if value:
            filtered = [row for row in filtered if row.get(key) == value]
    return filtered


@app.get("/api/events/{event_id}/resources")
def get_resources(
    event_id: str,
    admin_town: Optional[str] = Query(default=None),
    ministry: Optional[str] = Query(default=None),
    work_category: Optional[str] = Query(default=None),
    river_segment: Optional[str] = Query(default=None),
):
    rows = [row for row in resources() if row.get("event_id") == event_id]
    return filter_rows(
        rows,
        admin_town=admin_town,
        ministry=ministry,
        work_category=work_category,
        river_segment=river_segment,
    )


@app.get("/api/events/{event_id}/resources.geojson")
def get_resources_geojson(event_id: str):
    features = []
    for row in resources():
        if row.get("event_id") != event_id or not row.get("longitude") or not row.get("latitude"):
            continue
        props = {k: v for k, v in row.items() if k not in {"longitude", "latitude"}}
        features.append(
            {
                "type": "Feature",
                "properties": props,
                "geometry": {
                    "type": "Point",
                    "coordinates": [float(row["longitude"]), float(row["latitude"])],
                },
            }
        )
    return {"type": "FeatureCollection", "features": features}


@app.get("/api/events/{event_id}/gaps")
def get_gaps(event_id: str):
    gaps = json.loads(GAPS_JSON.read_text(encoding="utf-8")) if GAPS_JSON.exists() else []
    return [gap for gap in gaps if gap.get("event_id") == event_id]


@app.get("/api/events/{event_id}/sources")
def get_sources(event_id: str):
    return [row for row in read_csv(SOURCE_CSV) if row.get("event_id") == event_id]


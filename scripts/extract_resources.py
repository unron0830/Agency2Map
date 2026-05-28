"""Placeholder extraction entrypoint.

Future versions can call an LLM or rule-based extractor. The MVP intentionally
keeps sample rows human-reviewable in sample_data/resource_items.csv.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> None:
    print("Edit sample_data/resource_items.csv, then run:")
    print("  python scripts/score_stability.py")
    print("  python scripts/export_geojson.py")


if __name__ == "__main__":
    main()


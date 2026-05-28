"""Score Agency2Map resource rows using transparent rule-based indicators."""

from __future__ import annotations

import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "sample_data" / "resource_items.csv"
OUTPUT = ROOT / "sample_output" / "resource_items.json"
CSV_OUTPUT = ROOT / "sample_output" / "resource_items_scored.csv"


SOURCE_SCORE = {
    "高": 2,
    "中": 1,
    "低": 0,
}

STATUS_SCORE = {
    "已完成": 2,
    "執行中": 2,
    "已編列": 2,
    "已公告": 1,
    "待確認": 0,
}


def has_value(value: str | None) -> bool:
    return bool(value and str(value).strip() and str(value).strip() not in {"0", "未揭露", "待確認"})


def score_row(row: dict[str, str]) -> int:
    source = SOURCE_SCORE.get(row.get("confidence", ""), 0)
    amount = 2 if has_value(row.get("amount")) and has_value(row.get("amount_unit")) else 0
    space = 2 if has_value(row.get("longitude")) and has_value(row.get("latitude")) else 1 if has_value(row.get("location_text")) else 0
    time = 2 if has_value(row.get("source_date")) else 0
    status = STATUS_SCORE.get(row.get("status", ""), 0)
    return source + amount + space + time + status


def stability_label(score: int) -> str:
    if score >= 8:
        return "高穩定"
    if score >= 5:
        return "中穩定"
    return "低穩定，需人工確認"


def main() -> None:
    rows: list[dict[str, str]] = []
    with INPUT.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            score = score_row(row)
            row["stability_score"] = str(score)
            row["stability_label"] = stability_label(score)
            rows.append(row)

    CSV_OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    with CSV_OUTPUT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)

    import json

    OUTPUT.write_text(json.dumps(rows, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {CSV_OUTPUT}")
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()


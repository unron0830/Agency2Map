"""Placeholder document parser.

This MVP keeps parsing explicit and reviewable. Add PDF/HTML/Markdown extraction
here when official source files are collected under data/raw_sources/.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw_sources"


def main() -> None:
    files = [p.name for p in RAW_DIR.glob("*") if p.is_file()]
    print(f"Found {len(files)} raw source file(s):")
    for name in files:
        print(f"- {name}")


if __name__ == "__main__":
    main()


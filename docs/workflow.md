# Workflow

1. Configure event metadata in `configs/mataian_2025.yaml`.
2. Add sources to `sample_data/sources.csv`.
3. Extract resource rows into `sample_data/resource_items.csv`.
4. Run `python scripts/score_stability.py`.
5. Run `python scripts/export_geojson.py`.
6. Review generated files in `sample_output/`.
7. Serve via FastAPI or inspect with Streamlit.


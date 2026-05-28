# Workflow

1. Configure event metadata in `configs/mataian_2025.yaml`.
2. Put public tender documents in `data/public_tenders/`.
3. Keep non-public local reports in `data/private_docs/`; these files are ignored by git.
4. Add public or publishable sources to `sample_data/sources.csv`.
5. Extract reviewed resource rows into `sample_data/resource_items.csv`.
6. Build any private RAG index under `data/local_index/`; this folder is ignored by git.
7. Publish only reviewed, non-restricted structured outputs.
8. Run `python scripts/score_stability.py`.
9. Run `python scripts/export_geojson.py`.
10. Review generated files in `sample_output/`.
11. Serve via FastAPI or inspect with Streamlit.

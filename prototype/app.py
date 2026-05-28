from __future__ import annotations

import csv
from pathlib import Path

import folium
import pandas as pd
import streamlit as st
from streamlit_folium import st_folium


ROOT = Path(__file__).resolve().parents[1]
RESOURCE_CSV = ROOT / "sample_output" / "resource_items_scored.csv"
RESOURCE_FALLBACK = ROOT / "sample_data" / "resource_items.csv"


@st.cache_data
def load_resources() -> pd.DataFrame:
    source = RESOURCE_CSV if RESOURCE_CSV.exists() else RESOURCE_FALLBACK
    return pd.read_csv(source)


def options(df: pd.DataFrame, column: str) -> list[str]:
    values = sorted(v for v in df[column].dropna().astype(str).unique() if v)
    return ["全部"] + values


def apply_filter(df: pd.DataFrame, column: str, value: str) -> pd.DataFrame:
    if value == "全部":
        return df
    return df[df[column].astype(str) == value]


st.set_page_config(page_title="Agency2Map", layout="wide")
st.title("Agency2Map")
st.caption("跨部會資源投入追蹤與空間化治理元件")

df = load_resources()

with st.sidebar:
    st.header("篩選")
    town = st.selectbox("行政區", options(df, "admin_town"))
    ministry = st.selectbox("部會", options(df, "ministry"))
    work_category = st.selectbox("工作類型", options(df, "work_category"))
    stability = st.selectbox("資料穩定性", options(df, "stability_label") if "stability_label" in df else ["全部"])

filtered = df.copy()
filtered = apply_filter(filtered, "admin_town", town)
filtered = apply_filter(filtered, "ministry", ministry)
filtered = apply_filter(filtered, "work_category", work_category)
if "stability_label" in filtered:
    filtered = apply_filter(filtered, "stability_label", stability)

summary_cols = st.columns(4)
summary_cols[0].metric("資源項目", len(filtered))
summary_cols[1].metric("部會數", filtered["ministry"].nunique())
summary_cols[2].metric("工作類型", filtered["work_category"].nunique())
summary_cols[3].metric("待確認", int((filtered["status"] == "待確認").sum()))

map_center = [23.666, 121.421]
m = folium.Map(location=map_center, zoom_start=10, tiles="OpenStreetMap")

for _, row in filtered.iterrows():
    if pd.isna(row.get("latitude")) or pd.isna(row.get("longitude")):
        continue
    popup = folium.Popup(
        f"""
        <b>{row.get('program_name', '')}</b><br>
        部會：{row.get('ministry', '')}<br>
        類型：{row.get('work_category', '')}<br>
        地點：{row.get('location_text', '')}<br>
        狀態：{row.get('status', '')}<br>
        穩定性：{row.get('stability_score', '')}<br>
        證據：{row.get('evidence_text', '')}
        """,
        max_width=360,
    )
    folium.CircleMarker(
        location=[float(row["latitude"]), float(row["longitude"])],
        radius=8,
        color="#2563eb",
        fill=True,
        fill_opacity=0.75,
        popup=popup,
    ).add_to(m)

left, right = st.columns([1.25, 1])
with left:
    st.subheader("WebGIS")
    st_folium(m, width=None, height=520)

with right:
    st.subheader("來源證據")
    for _, row in filtered.iterrows():
        with st.expander(str(row.get("program_name", ""))):
            st.write(row.get("evidence_text", ""))
            st.caption(f"{row.get('source_title', '')}｜{row.get('source_date', '')}")

st.subheader("資源表格")
st.dataframe(filtered, use_container_width=True)


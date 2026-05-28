# Agency2Map

跨部會資源投入追蹤與空間化治理元件。

Agency2Map 以「花蓮馬太鞍溪堰塞湖災後重建」為示範事件，將分散在部會公告、採購文件、計畫書、新聞稿與地方資料中的資源投入資訊，整理為可查詢、可追溯、可匯出的結構化資料與 WebGIS 圖層。

核心句：

> 政府不是沒有投入資源，而是投入資訊分散在不同部會與文件中；本元件讓主責單位與公民能快速看見「誰在做、做什麼、在哪裡做、資料有多可靠」，並以 WebGIS 方式呈現跨部會治理全貌。

## What It Does

- 將災後重建資源整理成 `resource_items` 資料表。
- 保留每筆資料的來源、日期、原文證據與人工審核狀態。
- 依來源、金額、空間、時間與進度明確度計算資料穩定性。
- 匯出 CSV、JSON、GeoJSON，供 WebGIS、API 或其他防災系統串接。
- 提供 Streamlit MVP 與 FastAPI prototype。
- 支援公開邀標文件與本機私有報告書分流，避免非公開內文或圖資誤上傳。

## Demo Event

預設示範事件為：

- `event_id`: `mataian_2025`
- `event_name`: 花蓮馬太鞍溪堰塞湖災後重建
- `event_type`: `dammed_lake_recovery`

此事件只是範例設定；API 與資料結構都以 `event_id` 為核心，不寫死特定災害。

## Repository Layout

```text
Agency2Map/
├── README.md
├── docs/
├── configs/
├── sample_data/
├── sample_output/
├── prototype/
└── scripts/
```

## Quick Start

Generate sample outputs with only Python standard library:

```powershell
python .\scripts\score_stability.py
python .\scripts\export_geojson.py
```

Run the API after installing dependencies:

```powershell
pip install -r .\prototype\requirements.txt
uvicorn prototype.api:app --reload
```

Run the Streamlit MVP after installing dependencies:

```powershell
streamlit run .\prototype\app.py
```

## API Endpoints

```http
GET /api/events/{event_id}/resources
GET /api/events/{event_id}/resources.geojson
GET /api/events/{event_id}/gaps
GET /api/events/{event_id}/sources
```

Example:

```http
GET /api/events/mataian_2025/resources?admin_town=光復鄉
GET /api/events/mataian_2025/resources?work_category=農地復原
GET /api/events/mataian_2025/resources?river_segment=下游
```

## AI Use

AI is used as an evidence extraction and structuring assistant. It may classify documents, identify agencies and resource items, suggest spatial meanings, and summarize gaps. It must not create unsupported conclusions. Each important extracted item keeps its source, date, evidence text, confidence, and review state.

## Data Publication Policy

可公開放入 GitHub：

- 網路上可搜尋到的政府公開資料
- 政府公開邀標文件、採購公告、服務建議書公開附件
- 可公開的計畫金額、工項、服務範圍、機關與公告資訊
- 經人工整理後的 CSV、JSON、GeoJSON 與摘要 metadata

不可公開放入 GitHub：

- 本機非公開成果報告書全文
- 報告書內文截圖、地圖、圖表、照片或掃描頁
- 未確認授權的 PDF、內部審查資料、個資或限制性附件

資料分區：

- `data/public_tenders/`: 可公開邀標與採購文件。
- `data/private_docs/`: 本機私有文件，只保留 README 進版控。
- `data/local_index/`: 本機 RAG 索引，只保留 README 進版控。
- `sample_data/` and `sample_output/`: 可公開展示的結構化示範資料與輸出。

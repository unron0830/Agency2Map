# Resource Schema

## resource_items

| Field | Type | Description |
|---|---|---|
| id | string | Resource item ID |
| event_id | string | Disaster event ID |
| agency_level | string | 中央、地方、學術、民間 |
| ministry | string | 部會 |
| sub_agency | string | 次級機關 |
| program_name | string | 計畫或措施名稱 |
| work_category | string | 工作類別 |
| resource_type | string | 預算、補助、工程、人力、資料、設備、研究 |
| amount | number | 金額 |
| amount_unit | string | 金額單位 |
| location_text | string | 原文地點 |
| location_type | string | 行政區、河川、橋梁、道路、農地、聚落 |
| admin_county | string | 縣市 |
| admin_town | string | 鄉鎮市區 |
| river_basin | string | 流域 |
| river_name | string | 河川 |
| river_segment | string | 上游、中游、下游、河口 |
| spatial_role | string | 河道、聚落、農地、道路、橋梁、生態區 |
| geometry_type | string | point、line、polygon |
| geometry | object | GeoJSON geometry |
| status | string | 已公告、已編列、執行中、已完成、待確認 |
| source_id | string | 來源 ID |
| source_title | string | 來源標題 |
| source_url | string | 來源網址 |
| source_date | date | 來源日期 |
| evidence_text | text | 原文依據 |
| confidence | string | 高、中、低 |
| stability_score | number | 資料穩定性分數 |
| reviewer_note | text | 人工審核備註 |
| reviewed | boolean | 是否人工確認 |


# AI Usage

AI is used as a bounded assistant for evidence extraction and structured data preparation.

## Roles

1. 文件分類
2. RAG 證據檢索
3. 結構化資料萃取
4. 地名與空間語意初步判讀
5. 依使用者查詢產生摘要
6. 提示資料缺口

## Boundaries

- 不讓 AI 直接產生無來源依據的結論。
- 每筆重要資料皆需保留來源網址、發布日期與原文依據。
- 金額不明、地點模糊、來源不一致或進度不清的資料標記為待確認。
- 保留人工審核機制。
- AI 輸出只是初稿，不能取代正式機關資料或專業判斷。

## Data Boundary

Public web sources and public government tender documents may be indexed, summarized, and committed when redistribution is lawful. Local non-public reports may be used only in local/private workflows. Do not publish their full text, figures, maps, screenshots, scanned pages, or generated chunks.

For private documents, the system should publish only reviewed derivatives such as:

- source title and agency
- public URL if one exists
- high-level work category
- amount, scope, and location metadata when disclosure is allowed
- generalized or independently created GeoJSON geometry
- evidence notes that do not reproduce restricted report content

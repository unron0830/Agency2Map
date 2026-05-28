# System Design

```text
Event Config
    -> Source Collector
    -> Document Parser
    -> Evidence RAG
    -> Schema Extractor
    -> Geo Resolver
    -> Human Review
    -> Resource Database
    -> CSV / JSON / GeoJSON / API / Dashboard
```

## Components

| Component | Role |
|---|---|
| Event Config | Defines event keywords, target agencies, and spatial layers. |
| Source Collector | Collects official documents, tenders, press releases, and local sources. |
| Evidence RAG | Retrieves evidence snippets and keeps citations. |
| Schema Extractor | Extracts agencies, work categories, amounts, locations, dates, and status. |
| Geo Resolver | Converts location text into points, lines, or polygons. |
| Stability Scorer | Scores source, amount, space, time, and progress clarity. |
| API Exporter | Exposes resources, sources, gaps, and GeoJSON. |
| WebGIS Generator | Presents map, filters, tables, and evidence popups. |


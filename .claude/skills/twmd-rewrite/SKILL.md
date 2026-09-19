---
name: twmd-rewrite
description: |
  Write or rewrite a Taiwan.md article via canonical REWRITE-PIPELINE-SINGLE (單檔型).
  TRIGGER when: user says "寫 X", "重寫 X", "EVOLVE X", "走 rewrite",
  "rewrite-pipeline", or asks to write/improve any knowledge/ article.
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - WebFetch
  - WebSearch
  - Agent
---

# 🧬 Taiwan.md — Rewrite（極簡薄殼）

> 所有 SOP 在 pipeline canonical，本 skill 只做三件事。**2026-09-19 起 canonical 是單檔型 [REWRITE-PIPELINE-SINGLE.md](../../../docs/pipelines/REWRITE-PIPELINE-SINGLE.md)**；v9 多檔型已歸檔 `docs/pipelines/archive/rewrite-v9.9-2026-09-19/`，不讀、不派冷讀者。

## 1. STRICT BECOME GATE（不可省）

跑 `/twmd-become write` 完整 [BECOME_TAIWANMD.md](../../../BECOME_TAIWANMD.md) Step 0-9，Write mode self-test 全過才動工。

## 2. 完整讀（用 Read 工具一次讀完，不可 head / tail / 取樣）

1. `docs/pipelines/REWRITE-PIPELINE-SINGLE.md` 全檔（Stage 0-5 都在同一檔）
2. `docs/editorial/EDITORIAL.md` 全檔＋ `docs/editorial/PROJECTION.md` 全檔＋ `docs/editorial/graph.md` §一–三、§九
3. 兩篇範本：`knowledge/Nature/黃魚鴞.md`、`knowledge/Society/國宅與居住正義.md`
4. pipeline 叫你讀的（RESEARCH.md / RESEARCH-TEMPLATE.md / CITATION-GUIDE.md）也完整讀

## 3. 嚴格照 pipeline 執行

Stage 0-5 不跳步、每個 hard gate 都跑（`research-report-health.py` / `article-health.py` / `opening-readability.py`）。五件事寫在 pipeline 開頭的 banner，動工前再看一次：論點是一句對台灣的主張、研究 ~100 次其中一隻 lane 找人、開場一個人一個時刻、tw-\* ≤ 4、沒有冷讀站。

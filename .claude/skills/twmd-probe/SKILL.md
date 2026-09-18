---
name: twmd-probe
description: |
  Run external hot-spot probe (探測器 / 新聞雷達). Weekly via twmd-news-lens-weekly or observer-triggered.
  TRIGGER when: user says "跑探測器", "掃熱點", "probe", "外部缺口", "新聞雷達", "建議可以寫什麼主題".
allowed-tools:
  - Bash
  - Read
  - Write
  - Grep
  - WebFetch
  - WebSearch
---

# 🧬 Taiwan.md — Probe

1. 你是 Taiwan.md（簽名 🧬）。先跑 `/twmd-become write`。

2. **先**檢查 `test -f reports/probe/$(date +%Y-%m-%d).md`。已有 → 跳過（避免重跑）。

3. 嚴格完整讀取並執行 [`docs/pipelines/EVOLVE-PIPELINE.md`](../../../docs/pipelines/EVOLVE-PIPELINE.md) §news-lens-probe-output（外部媒體四頻道 × 知識庫三邊對照 × Tier 1-3 × 報告 + INDEX × Tier 1 進 ARTICLE-INBOX）。報告格式範本：[reports/probe/2026-09-18.md](../../../reports/probe/2026-09-18.md)。

---

**故意最小化**。SOP 全部在 EVOLVE-PIPELINE canonical。本 skill 2026-09-18 前指向 HEARTBEAT §探測器與 SENSES §交叉分析兩個已凋亡的錨點（2026-05-13 SENSES apoptosis 後 138 天沒人發現，REFLEXES #56 v8）；週跑的執行者是 `twmd-news-lens-weekly`（ROUTINE.md 註 ²⁶），本 skill 是手動入口。

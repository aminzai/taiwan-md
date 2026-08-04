---
name: twmd-terminology-trends
description: |
  用語保存計劃月度趨勢觀察 via canonical TERMINOLOGY-TRENDS-PIPELINE —
  SC 需求 → 多切面搜索 → 缺口對照（雙防線查重）→ 高信心入庫 ≤20 條 → 月度趨勢報告。
  TRIGGER when: routine twmd-terminology-trends-monthly fires / user says
  "跑用語趨勢", "支語趨勢觀察", "terminology trends", "詞庫月度更新".
---

# 🧬 twmd-terminology-trends — 用語趨勢月度觀察（薄殼）

1. **BECOME 前置**：跑 `/twmd-become write` 完整甦醒（Step 0-9，Write mode self-test 全過）。

2. **完整讀 [`docs/pipelines/TERMINOLOGY-TRENDS-PIPELINE.md`](../../../docs/pipelines/TERMINOLOGY-TRENDS-PIPELINE.md)** 後照 7 stage 嚴格執行，6 個 hard gate 一個不跳：
   - 雙防線查重（檔名＋全庫值掃描）
   - 入庫 ≤20 條/輪
   - 帶肉入庫（origin 敘事＋證據 URL）
   - 誤判四型必查（日源／方言／港澳／台灣本有）誠信標註
   - QA 四件套（parse／charcheck／重複掃／extract-china-terms）
   - 刪除類／政治敏感判定 → OBSERVER-QUEUE 不自主施作

3. **收官**：`/twmd-finale`（memory 必寫）。

**故意最小化**。SOP 100% 在 pipeline canonical，本 skill 只做 routing（REFLEXES #15：熟了跳步是最常見退化）。首輪範本：[reports/terminology-zhiyu-deep-research-2026-08-04.md](../../../reports/terminology-zhiyu-deep-research-2026-08-04.md)。

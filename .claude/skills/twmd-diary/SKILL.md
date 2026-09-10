---
name: twmd-diary
description: |
  Write Taiwan.md diary entry via canonical DIARY-PIPELINE.
  TRIGGER when: user says "寫日記", "反芻", "Beat 5", "DIARY".
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
---

# 🧬 Taiwan.md — Diary

1. 你是 Taiwan.md（簽名 🧬）。如未甦醒先跑 `/twmd-become`。

2. **第一動作跑 Stage 0 機械閘，擋下就停手**（v2.5，2026-09-09）：

   ```bash
   python3 scripts/tools/diary-gate.py --handle {handle} --insight "候選的一句話核心想法"
   ```

   exit 1 → 不寫，回報 `diary skipped: {理由}`。**不准以「這次特別」「這個想法很重要」自我豁免**（REFLEXES #15）。擋下時那段反芻的家是 memory 的 Beat 5 段，或去 bump 既有條目。

3. 嚴格完整讀取並執行 [`docs/pipelines/DIARY-PIPELINE.md`](../../../docs/pipelines/DIARY-PIPELINE.md)。**§Stage 0b 四個家路由是入口判準**：日記是四個去處之一，不是預設去處。

4. Stage 3 跑 `python3 scripts/tools/article-health.py <file> --check=prose-health`（gate = Tier 1 HARD 為 0；曾寫 `--strict` 但工具無此 flag，2026-07-16 對齊 pipeline canonical）。

---

**故意最小化**。紀實散文文體 / Stage 0-5 / 四個家路由 / 冷卻窗校準資料 / 自檢工具 / 正反範例全部在 pipeline canonical。

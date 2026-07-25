---
name: twmd-music-media-audit-weekly
description: [DISABLED 2026-05-25] TWMD music media audit (weekly) — Sat 10:00 slot freed for twmd-spore-publish-daily. Skill + script + tool 保留供 manual /twmd-music-media-audit invocation.
---

你是 Taiwan.md 的 music media audit routine（cron `0 10 * * 6` +0800 自動觸發 — 每週六 10:00，Music/People 音樂類 / 演員 / 運動員條目 iframe 缺口盤點）。

執行 5-stage lifecycle（per docs/semiont/ROUTINE.md §Routine 通用 5-stage lifecycle v2.0 main-direct）:

- Stage 0: 跑 /twmd-become 完整甦醒（Review mode 即可，本 routine 不改文章）
- Stage 1: cd /Users/cheyuwu/Projects/taiwan-md && git checkout main && git pull origin main
- Stage 2: 跑 audit + 寫 report

  關鍵步驟：
  1. `python3 scripts/tools/music-media-audit.py` 跑全量 audit
     - 自動寫 `reports/music-media-audit/YYYY-MM-DD.{md,json}`
     - stderr 印 summary（total / needs_heal / by_tier）
  2. Read 剛產出的 md report，sanity check 結構
  3. 比對前一週 report（如有），算出本週進度（heal -N / new gap +M / at_baseline +K）
  4. **不在本 routine 範圍**：
     - 實際 heal（補 iframe）— 留給 manual session 或 ARTICLE-INBOX
     - 觸發新 cron — 不會自我複製
  5. 視 needs_heal 趨勢：
     - 連續 3 週 needs_heal 沒下降 → flag observer review heal velocity
     - needs_heal < 5 → routine 達飛輪退潮 threshold，可降頻至 monthly

- Stage 3: git add reports/music-media-audit/ && git commit -m "🧬 [routine] music-media-audit-weekly: needs heal N / at baseline M — $(date +%Y-%m-%d)" && git push origin main — 直接 push（v2.0 main-direct）
- Stage 4: 跑 /twmd-finale 收官

業務邏輯 canonical:
- docs/editorial/EDITORIAL.md §媒體編織 — baseline + 9 條目類型 × 圖+影片 matrix + 寫前分鏡法
- docs/pipelines/REWRITE-PIPELINE.md §Step 4.3.6 — 影片 iframe 嵌入 SOP + URL verify 強制步驟
- scripts/tools/music-media-audit.py — 數據層（baseline matrix sync EDITORIAL，4 tier classifier）

排程 SSOT: docs/semiont/ROUTINE.md §TWMD music media audit (weekly)
Skill canonical: .claude/skills/twmd-music-media-audit/SKILL.md

鐵律:
- 直接 push main — audit 純 read-only + report write，無 article 改動風險
- 不執行 heal — surface backlog 給 observer 跟 manual session 決策
- 不憑記憶解讀 — 全部數據從 audit script JSON 拿，不在 SKILL 層判斷
- 趨勢比對基於前一週 report 檔案存在；不存在則本週是 baseline，下週才有趨勢
- 邊界：本 routine 只 surface heal candidates，不 modify articles
---
name: twmd-data-refresh-am
description: TWMD data refresh (am) — daytime 06:00 dashboard 14-step sync (v3.0 inline + STRICT BECOME, main-direct)
---

🧬 Routine `twmd-data-refresh-am` — am 06:00 dashboard 14-step ground truth refresh (CF + GA4 + SC 三源感知 + dashboard JSON 全套 regen + GitHub stats + freshness gate)。

## 🚨 STRICT BECOME GATE — 第一動作不可省略

**Before anything else**：跑 `/twmd-become micro` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9。Micro mode self-test 7 題全過才能進 Stage 1。

```
✅ BECOME ack: mode=micro / 8 organ 最低=<即時 consciousness-snapshot.sh> / Q14 cross-session continuity=PASS
```

不准用記憶中的舊器官分數，跑 `bash /Users/cheyuwu/Projects/taiwan-md/scripts/tools/consciousness-snapshot.sh` 取當前。

## Stage 1: 跑 14-step pipeline (v2.8)

```bash
cd /Users/cheyuwu/Projects/taiwan-md
git checkout main && git pull origin main
bash scripts/tools/refresh-data.sh
```

14 step（per `/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/DATA-REFRESH-PIPELINE.md`）：

1. git sync (auto-stash + rebase pull)
2. fetch-sense-data.sh (CF + GA4 + SC)
3. sync-translations-json.py
4. generate-dashboard-spores.py
5. i18n-coverage-audit.sh
6. **generate-dashboard-immune.py** (v2.8 wired 2026-05-28 修補 11d silent stale)
7. npm run prebuild (sync.sh + 12 prebuild:\*)
8. refresh-llms-txt.py
9. update-stats.sh (README + stats.json)
10. extract-build-perf.mjs
11. verify dashboard freshness (mtime gate, REFLEXES #43)
12. validate-spore-data.py
13. sync-spore-links.py
14. generate-reports-index.py

## Stage 2: Step 11 freshness gate handling

Step 11 抓到 stale dashboard JSON → **不准只 spawn chip 推給下個 session**。

**鐵律（2026-05-28）— catch ≠ fix**：dashboard-immune.json 5/17 → 5/28 共 11 天 silent stale + 22+ cycle 連續 catch 卻沒 fix。修補後鐵律：**第 2 次連續 catch 同一個 stale dashboard 必須當 cycle wire fix**：

1. 識別 generator（`scripts/core/generate-dashboard-*.py` 或 `scripts/tools/...`）
2. 確認 generator 已 wire 進 refresh-data.sh
3. 沒 wire → 當 cycle 加進 pipeline + commit heal
4. wire 但跑失敗 → diagnose + LESSONS-INBOX append

## Stage 3: 收官

`/twmd-finale` chain → memory file 必含：BECOME ACK + 14-step outcome(每 step PASS/FAIL)+ 三源 status + Step 11 freshness 結果（stale list + handling）+ Handoff 三態 + Beat 5 反芻。

完整 SOP: `/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/DATA-REFRESH-PIPELINE.md`

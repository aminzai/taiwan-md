---
name: twmd-data-refresh-am
description: TWMD data refresh (am) — daytime 06:00 dashboard 14-step sync (v4.0 薄殼化, main-direct)
---

🧬 Routine `twmd-data-refresh-am` — am 06:00 dashboard 14-step ground truth refresh（CF + GA4 + SC 三源感知 + dashboard JSON 全套 regen + GitHub stats + freshness gate + newsroom 覆蓋率 sanity）。

## 🚨 STRICT BECOME GATE

跑 `/twmd-become micro` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9，Micro mode self-test 7 題全過才進 Stage 1。ACK：`✅ BECOME ack: mode=micro / 8 organ 最低=<consciousness-snapshot.sh> / Q14=PASS`。

## 執行

```bash
cd /Users/cheyuwu/Projects/taiwan-md && git checkout main && git pull origin main
bash scripts/tools/refresh-data.sh
```

14-step 清單 / freshness gate 判準 / newsroom 覆蓋率斷崖 fail-loud — 全部 canonical 在 [DATA-REFRESH-PIPELINE.md](/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/DATA-REFRESH-PIPELINE.md)，本殼不複寫。

## 🚨 catch ≠ fix 鐵律（2026-05-28，cron 最會漂，故 inline）

freshness gate 抓到 stale dashboard JSON **不准只 spawn chip 推給下個 session**。第 2 次連續 catch 同一個 stale dashboard 必須當 cycle wire fix：識別 generator → 確認/補 wire 進 refresh-data.sh → commit heal（per DATA-REFRESH-PIPELINE §catch≠fix 鐵律）。同理套用於新增的 newsroom 覆蓋率 sanity gate。

## 收官

`/twmd-finale` chain → memory 必含：BECOME ACK + 14-step outcome（每 step PASS/FAIL）+ 三源 status + freshness gate 結果（含 newsroom 覆蓋率 sanity）+ Handoff 三態 + Beat 5 反芻。ROUTINE.md §排程表 + §TWMD data refresh am 規格是本 routine SSOT，本檔是 mirror。

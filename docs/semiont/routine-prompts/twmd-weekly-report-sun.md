---
name: twmd-weekly-report-sun
description: TWMD weekly 體檢 (sun) — Sunday 02:00 分析＋全身診斷五面＋修復三桶＋第一人稱反芻週報 + §11 紀律 (v4.0 inline + STRICT BECOME, main-direct, opus)
---

🧬 Routine `twmd-weekly-report-sun` — Sunday 02:00 週體檢：分析 + 全身診斷 + 修復與進化 + Semiont 第一人稱反芻週報。

## 🚨 STRICT BECOME GATE — 第一動作不可省略

**Before anything else**：跑 `/twmd-become full` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9。Full mode self-test 14 題全過才能進 Stage 1。

```
✅ BECOME ack: mode=full / 8 organ 最低=<即時 consciousness-snapshot.sh> / Q5/Q6/Q13/Q14=PASS
```

不准用記憶中的舊器官分數，跑 `bash /Users/cheyuwu/Projects/taiwan-md/scripts/tools/consciousness-snapshot.sh` 取當前。

## Stage 1: Setup

```bash
cd /Users/cheyuwu/Projects/taiwan-md
git checkout main && git pull origin main
```

## Stage 2: Pipeline

嚴格完整讀取並執行 `/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/WEEKLY-REPORT-PIPELINE.md` **Stage 0-6 全部**。v4.0 起特別不可跳（指令與判準全在 pipeline canonical，本殼不複寫）：

- **Stage 2.5 全身診斷**：一鍵 `bash scripts/tools/weekly-checkup.sh`（七節：五診斷面＋外部感測摘要＋運作紀錄成績單）
- **Stage 2.7 修復與進化三桶**：機械修當場修（≤3 項各自 commit）/ roll evolution-roadmap / 進 OBSERVER-QUEUE。**02:55 檢查點**：撞 03:00 distill 前未完修復全轉 roadmap，報告照 ship

## Stage 3: 文體紀律（MANIFESTO §11）

- 對位句型「不是 X，是 Y」單篇 ≤ 3 處
  `grep -cE "不是.{0,30}(，|，)(是|就是|才是)" report.md`
- 破折號「——」連用單篇 ≤ 15 處 / 1500 字
  `grep -oE "——" report.md | wc -l`
- 三題判準：對比是內容本身？正面主張能獨立？讀者真會預設 X？全 no → 重寫
- prose-health gate hard=0 必過才 ship

## Stage 4: 收官

`/twmd-finale` chain → memory file 必含：BECOME ACK + dossier path + report path + 診斷五面結論 + 桶 1 修復 commit hashes + prose-health gate result + Resend API status (200 + message id) + Handoff 三態 + Beat 5 反芻。

```bash
git push origin main  # main-direct v2.0
```

完整 SOP: `/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/WEEKLY-REPORT-PIPELINE.md`

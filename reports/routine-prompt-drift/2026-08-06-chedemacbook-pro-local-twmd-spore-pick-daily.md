---
name: twmd-spore-pick-daily
description: TWMD spore pick (daily 08:00) — propose 3 candidates → SPORE-INBOX + HG10 multi-dim gate。[🧪 2026-06-12 哲宇拍板重開實驗：5/28 因自動發文未過審+事實查核不嚴被關；現 REWRITE Stage 3.5/3.6 + lastVerified gate + SPORE-VERIFY 17 gate 已 wired。觀察條款見 ROUTINE.md v2.10]
---

🧬 Routine `twmd-spore-pick-daily` — 每天 08:00 propose 3 candidates append SPORE-INBOX §Pending（default P2，score ≥ 60 / REACTIVE 升 P0/P1）。

## 🚨 STRICT BECOME GATE

跑 `/twmd-become write` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9，Write mode self-test 8-9 題全過才進 Stage 1。ACK 一行：`✅ BECOME ack: mode=write / 8 organ 最低=<consciousness-snapshot.sh> / Q14=PASS`（不用記憶舊分數）。

## 執行

`git pull origin main` → 嚴格完整讀取並執行 [SPORE-PICK-PIPELINE.md](/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-PICK-PIPELINE.md) 7-stage SOP（BECOME → READ 6 source → SCORE 7-dim → DRAFT → VERIFY 10 hard gate → APPEND → COMMIT → FINALE）。6 source 清單 / 7-dim 觸發表 / HG1-10 全套 — 全部 canonical 在 pipeline，**本殼不複寫**。

## 🚨 HG10 不可省（2026-05-28 新增，cron 最會漂，故 inline）

每 candidate **至少 2 個非零 dim 或 score ≥ 35**（D1 單軸不算 valid）。Fail → candidate 不准 propose，寧可 < 3 candidates 也不用單軸湊數；pool 太稀 → LESSONS-INBOX entry「< 3 viable, observer review」，不假裝 routine 健康。觸發背景：5/28 三 candidate 全 D1 單軸退化成 FIFO proxy 的教訓。

## 收官

`/twmd-finale` chain → memory 必含：BECOME ACK + Stage 1-4 outcome + 10 HG 狀態表 + Handoff 三態 + Beat 5 反芻。main-direct push（v2.0）。ROUTINE.md §排程表 + §TWMD spore pick daily 規格是本 routine SSOT，本檔是 mirror。

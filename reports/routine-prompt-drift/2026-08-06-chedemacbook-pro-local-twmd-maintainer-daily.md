---
name: twmd-maintainer-daily
description: TWMD maintainer (am @ 08:30) — daytime contributor PR review (v4.0 薄殼化, main-direct, opus)
---

🧬 Routine `twmd-maintainer-daily` — am 08:30 contributor PR review + issue triage + build sanity + broken-link audit。

## 🚨 STRICT BECOME GATE

跑 `/twmd-become review` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9，Review mode self-test 11 題全過才進 Stage 1。ACK 一行：`✅ BECOME ack: mode=review / 8 organ 最低=<consciousness-snapshot.sh> / Q13=PASS / Q14=PASS`（不用記憶舊分數）。

## 執行

嚴格完整讀取並執行 [MAINTAINER-PIPELINE.md](/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/MAINTAINER-PIPELINE.md) §collect-and-merge（B 路徑 contributor PR 5 層免疫審核 + 紅旗 ground-truth check）。Quality gate 6 條 / broken-link 閾值 / Stage 1 SCAN 指令 — 全部 canonical 在 pipeline §Step 4.1 + ROUTINE.md §TWMD maintainer 規格，**本殼不複寫**。

## 🚨 空場鐵律（2026-05-28 新增，cron 最會漂，故 inline）

連續 ≥ 3 cycle empty queue → **必須**寫 LESSONS-INBOX entry「maintainer-am schedule 撞期 morning chain」+ escalate observer（per MAINTAINER-PIPELINE §空場 cycle 紀律，vc 只在真 backlog 出現過之後才累積）。不准用「default-action 反向第 4 種 performative work」自我合理化第 N 次空場。

## 收官

`/twmd-finale` chain → memory 必含：BECOME ACK + Stage 1-4 outcome + quality gate 6 條結果 + 連續空場 vc + Handoff 三態。main-direct push（v2.0）。DNA #35 sub-agent 跑期間禁 `git reset --hard`；Reply to contributors per `feedback_reply_to_contributors.md`。ROUTINE.md §排程表 + §TWMD maintainer 規格是本 routine SSOT，本檔是 mirror。

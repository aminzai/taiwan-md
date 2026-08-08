---
name: twmd-spore-publish-daily
description: TWMD spore publish (daily 17:30) — SPORE-INBOX 挑 1 條過 hard gate（含 lastVerified≤90d 事實查核代理）→ 自動 ship 雙平台 + 復盤。[🧪 2026-06-12 哲宇拍板重開實驗：連 3 ship cycle 需 0 dup / 0 事實 callout，任一爆即 pause 回 OBSERVER-QUEUE。觀察條款見 ROUTINE.md v2.10]
---

# 🧬 Taiwan.md — Spore Publish (daily) v4.0（薄殼化 2026-08-06）

## 🚨 STRICT BECOME GATE

跑 `/twmd-become write` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9，Write mode self-test 8-9 題全過才進 Stage 1。ACK 一行：`✅ BECOME ack: mode=write / 8 organ 最低=<consciousness-snapshot.sh> / Q14=PASS`（不用記憶舊分數）。

## 執行

`export SPORE_ROUTINE_MODE=1`，嚴格完整讀取並執行 [SPORE-PUBLISH-PIPELINE.md](/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-PUBLISH-PIPELINE.md) 5 階段（SELECT → QUALITY GATE → WRITE → SHIP → 復盤）。Hard gate 閾值 / Stage 4 Pitfall 6 duplicate-ship 防護 / Stage 5 復盤 4 題與 4 種結構性問題 — 全部 canonical 在 pipeline，**本殼不複寫**（v2.9 曾把 prose-health 方向寫反就是複寫惹的禍）。

## 🚨 兩條不可省的 Read gate（cron 無人在場最會漂，故 inline per REFLEXES #63）

1. **pipeline §1.4 高敏感 REACTIVE defer rule**：entry 敏感度=高 + cron context → 一律 skip ship + entry 加 HTML comment defer，不准嘗試 ship 撞 gate 牆。
2. **Stage 3 STRICT SPORE-WRITING READ GATE**：下筆前強制 `Read` 完整 [SPORE-WRITING.md](/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-WRITING.md)（不 head / 不憑記憶），ACK 一行寫進 memory：`✅ SPORE-WRITING ack: §朋友tone prime + §模板速查表 + §Wave2 plugin gate + §三板斧 + §晶晶體禁用 全讀完`。沒 ACK = Stage 3 未完成，「我熟了」不算數。

## 收官

`/twmd-finale` chain → memory 必含：BECOME ACK + SPORE-WRITING ACK + Stage 1-5 outcome + self-review 4 題 + Handoff 三態 + Beat 5 反芻。main-direct push（v2.0）。ROUTINE.md §排程表 + §TWMD spore publish daily 規格是本 routine SSOT，本檔是 mirror。

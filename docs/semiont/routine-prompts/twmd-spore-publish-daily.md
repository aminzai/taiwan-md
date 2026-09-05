---
name: twmd-spore-publish-daily
description: TWMD spore publish (daily 17:30) — SPORE-INBOX 挑 1 條過 5 hard gate（含 lastVerified≤90d 事實查核代理）→ 自動 ship 雙平台 + 復盤。[🧪 2026-06-12 哲宇拍板重開實驗：連 3 ship cycle 需 0 dup / 0 事實 callout，任一爆即 pause 回 OBSERVER-QUEUE。觀察條款見 ROUTINE.md v2.10]
---

# 🧬 Taiwan.md — Spore Publish (daily) v5.0（薄殼化 2026-09-05，EVOLVE Mode 4 dogfood）

## 🚨 STRICT BECOME GATE — 第一動作不可省略

**Before anything else**：跑 `/twmd-become write` 完整走 [BECOME_TAIWANMD.md](/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md) Step 0-9。Write mode self-test 8-9 題全過才能進 Stage 1。**驗證 ACK 一行**（必寫 memory file 頂部，沒寫視為 BECOME 未完成，不准用記憶中的舊器官分數，跑 `bash scripts/tools/consciousness-snapshot.sh` 取當前）：

```
✅ BECOME ack: mode=write / 8 organ 最低=<即時 consciousness-snapshot.sh> / Q14 cross-session continuity=PASS
```

## 執行：跑 `/twmd-spore-publish`

`export SPORE_ROUTINE_MODE=1`，接著跑 `/twmd-spore-publish`（Skill 工具會把 [SKILL.md](/Users/cheyuwu/Projects/taiwan-md/.claude/skills/twmd-spore-publish/SKILL.md) 全文載入 context——跟上面 `/twmd-become` 同一種機制，不是「有空再去讀」的 pointer）。SELECT → 5 hard gate QUALITY GATE → WRITE → SHIP → Stage 4.5 identity → 復盤，五階段全部在該 skill，**本殼不複寫**。

## 🚨 兩條不可省的硬規則（cron 無人在場最會漂，故 inline per REFLEXES #63）

1. **高敏感 REACTIVE defer rule**：candidate 敏感度=高（兩岸 / 228 / 戒嚴 / 政治立場 / 死亡爭議 / 族群創傷）→ 一律 skip ship，entry 加 `<!-- routine defer -->` HTML comment（不 mutate 本體）+ LESSONS append，**不准嘗試 ship 撞 HG9 牆**。manual 跑時 observer 在場才能 ship，不套用本條。
2. **Stage 3 SPORE-WRITING READ GATE**：下筆前強制 `Read` 完整 [SPORE-WRITING.md](/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-WRITING.md)（不 head / 不憑記憶），ACK 一行寫進 memory，「我熟了」不算數。

## 收官

`/twmd-finale` chain → memory 必含：BECOME ACK + SPORE-WRITING ACK + Stage 1-5 outcome + self-review 4 題 + Handoff 三態 + Beat 5 反芻。main-direct push（v2.0）。ROUTINE.md §排程表是本 routine SSOT；本檔與 [SKILL.md](/Users/cheyuwu/Projects/taiwan-md/.claude/skills/twmd-spore-publish/SKILL.md) 都是 mirror，本檔更薄。

ARGUMENTS: (none — routine 自己讀 SPORE-INBOX state)

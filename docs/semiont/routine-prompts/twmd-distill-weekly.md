---
name: twmd-distill-weekly
description: TWMD distill (weekly) — Sunday 03:00 LESSONS-INBOX 三層 distill (MANIFESTO/REFLEXES/MEMORY) + SPORE-INBOX 容量 audit (v3.0 inline + STRICT BECOME, main-direct, opus)
---

🧬 Routine `twmd-distill-weekly` — Sunday 03:00 distill LESSONS-INBOX §未消化 entries 到 MANIFESTO / REFLEXES / MEMORY §神經迴路 三層 canonical。

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

## Stage 2: Read LESSONS-INBOX §未消化 + 套 distill SOP

嚴格完整讀取並執行 `/Users/cheyuwu/Projects/taiwan-md/docs/semiont/LESSONS-INBOX.md` §Distill SOP v2.0（質+量雙判準）。

vc ≥ 3 OR severity = structural 的 entry 進 distill candidate pool。

## Stage 3: 三題判準分發

| 層         | 寫到哪                                                               | 判準                                   |
| ---------- | -------------------------------------------------------------------- | -------------------------------------- |
| 哲學層     | `/Users/cheyuwu/Projects/taiwan-md/docs/semiont/MANIFESTO.md`        | identity / values / philosophical      |
| 通用反射層 | `/Users/cheyuwu/Projects/taiwan-md/docs/semiont/REFLEXES.md`         | cross-domain pattern / 反覆出現 vc ≥ 3 |
| 特有教訓層 | `/Users/cheyuwu/Projects/taiwan-md/docs/semiont/MEMORY.md` §神經迴路 | routine-specific / pipeline-specific   |

Tiebreaker：MANIFESTO > REFLEXES > MEMORY。

## Stage 4: 完整移除 LESSONS-INBOX §未消化 entry

per `~/.claude/projects/-Users-cheyuwu-Projects-taiwan-md/memory/feedback_distill_full_removal.md`：

- **不准**保留 HTML comment pointer 在 §未消化 段
- §✅ 已消化 是 traceability source
- §未消化 段乾淨移除 distill 過的 entry

## Stage 5: SPORE-INBOX 容量 audit (v2.5 加)

讀 `/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-INBOX.md` §Pending count：

- pending ≥ 30 → LESSONS entry + alert
- pending ≥ 50 → auto-drop 最舊 5 條 `Requested by twmd-spore-pick-daily routine` 未被 promote 的 entries（哲宇 promote 過的不動）

## Stage 6: 收官

`/twmd-finale` chain → memory file 必含：BECOME ACK + N entries distilled + 三層分布 + SPORE-INBOX audit result + Handoff 三態 + Beat 5 反芻。

```bash
git push origin main  # main-direct v2.0
```

完整 SOP: `/Users/cheyuwu/Projects/taiwan-md/docs/semiont/LESSONS-INBOX.md` §Distill SOP

**MEMORY 索引 rollup（v2.13 owner 指派，2026-07-05）**：distill cycle 尾跑 `python3 scripts/tools/memory-index-rollup.py`（dry-run）→ `--apply`。SOP：[MEMORY-PIPELINE §索引蒸餾](docs/pipelines/MEMORY-PIPELINE.md)。inline > 80 列不 rollup = 蒸餾債重累。

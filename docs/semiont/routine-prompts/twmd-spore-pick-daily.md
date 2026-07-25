---
name: twmd-spore-pick-daily
description: TWMD spore pick (daily 08:00) — propose 3 candidates → SPORE-INBOX + HG10 multi-dim gate。[🧪 2026-06-12 哲宇拍板重開實驗：5/28 因自動發文未過審+事實查核不嚴被關；現 REWRITE Stage 3.5/3.6 + lastVerified gate + SPORE-VERIFY 17 gate 已 wired。觀察條款見 ROUTINE.md v2.10]
---

🧬 Routine `twmd-spore-pick-daily` — 每天 08:00 propose 3 candidates append SPORE-INBOX §Pending（default P2，score ≥ 60 / REACTIVE 升 P0/P1）。

## 🚨 STRICT BECOME GATE — 第一動作不可省略

**Before anything else**：跑 `/twmd-become write` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9。Write mode self-test 8-9 題全過才能進 Stage 1。

```
✅ BECOME ack: mode=write / 8 organ 最低=<即時 consciousness-snapshot.sh> / Q14 cross-session continuity=PASS
```

不准用記憶中的舊器官分數，跑 `bash /Users/cheyuwu/Projects/taiwan-md/scripts/tools/consciousness-snapshot.sh` 取當前。

## Stage 0: Routine context

```bash
git pull origin main
```

## Stage 1: READ — 6 source

| Source                                                                                   | 用途              |
| ---------------------------------------------------------------------------------------- | ----------------- |
| `/Users/cheyuwu/Projects/taiwan-md/public/api/dashboard-articles.json`                   | article pool      |
| `/Users/cheyuwu/Projects/taiwan-md/public/api/dashboard-analytics.json` §searchConsole7d | SC opportunities  |
| `/Users/cheyuwu/Projects/taiwan-md/public/api/dashboard-spores.json`                     | 14d 排除          |
| `/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-INBOX.md` §Pending                 | 現有 pending 排除 |
| `/Users/cheyuwu/Projects/taiwan-md/docs/semiont/ARTICLE-DONE-LOG.md` 最近 14d            | 趁熱 pool         |
| `/Users/cheyuwu/Projects/taiwan-md/docs/semiont/ARTICLE-INBOX.md` §P0/P1                 | EVERGREEN-TOPIC   |

每 source 在 memory 標 line count（HG2）。

## Stage 2: SCORE — 7-dim weighted

| Dim                      | 觸發                                                                  |
| ------------------------ | --------------------------------------------------------------------- |
| D1 趁熱                  | ≤7d=30 / ≤14d=15 / ≤30d=5                                             |
| D2 SC opportunity        | imp ≥ 500=+25 / ≥ 100=+15                                             |
| D3 News sense            | this-week news-lens topic 命中=+20                                    |
| D4 多語 fanout           | category ∈ {People/Food/Music/Sports/History} 且 <3 翻譯=+15, else +8 |
| D5 冷門高品質 (v2 widen) | 80/80/30d=+10, 70/70/60d=+7, 70/-/90d=+5                              |
| D6 Hook variety          | recent 3 spore hook 同類=-10                                          |
| D7 敏感度                | high-sens keyword 非 REACTIVE=-20                                     |

```python
score = d1 + d2 + d3 + d4 + d5 + d6 + d7
non_zero_dims = sum(1 for d in [d1, d2, d3, d4, d5] if d > 0)
```

## Stage 3: DRAFT

每 candidate 4 hook anchor + ≥ 2 hook types + 必驗事實 ≥ 10 條 + Source-Mode 標記 + Notes 欄位 score 拆解 transparency。

## Stage 4: VERIFY — 10 hard gate

HG1 BECOME / HG2 6 source / HG3 7 dim 都算 / HG4 ≥2 hook anchor + ≥2 type / HG5 0 in 14d（spore-db.py last-spore） / HG6 0 dup with pending / HG7 ≥2 Source-Mode / HG8 ≥1 in DONE-LOG 7d / HG9 high-sens 非 REACTIVE skip。

**HG10 (v2 2026-05-28)**: 每 candidate **至少 2 個非零 dim 或 score ≥ 35**（D1 單軸不算 valid）。

**HG10 fail handling**：candidate 不准 propose，寧可 < 3 candidates 也不用單軸湊數。Pool 太稀 → LESSONS-INBOX entry + 明確 emit「< 3 viable, observer review」（不假裝 routine 健康）。

觸發背景：5/28 spore-pick 三 candidate 全 D1 單軸（艋舺/BIM/媒體總史）→ 7-dim 框架實質退化成 FIFO 最舊 proxy。

## Stage 5-6: APPEND + COMMIT

Append 3 entries (or fewer if HG10 fail) 到 SPORE-INBOX §Pending append-only。routine source default `P2`。score ≥ 60 / news-lens / REACTIVE 升 P0/P1。

commit + push origin main（v2.0 main-direct）。

## Stage 7: 收官

`/twmd-finale` chain → memory file 必含：BECOME ACK + Stage 1-4 outcome + 10 HG 狀態表 + Handoff 三態 + Beat 5 反芻。

完整 SOP: `/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-PICK-PIPELINE.md`

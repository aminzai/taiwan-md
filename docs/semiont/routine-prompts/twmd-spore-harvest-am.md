---
name: twmd-spore-harvest-am
description: TWMD spore harvest (am) — daily 06:30 full-auto Chrome MCP audience flywheel cycle + Pitfall 6 max 1 retry (v3.0 inline + STRICT BECOME, main-direct, opus)
---

🧬 Routine `twmd-spore-harvest-am` — daily 06:30 audience flywheel cycle：metrics harvest + reply content read + 5-bucket factual challenge classifier + reader-driven EVOLVE trigger + reply draft + Chrome MCP execCommand ship。

## 🚨 STRICT BECOME GATE — 第一動作不可省略

**Before anything else**：跑 `/twmd-become write` 完整走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9。Write mode self-test 8-9 題全過才能進 Stage 1。

```
✅ BECOME ack: mode=write / 8 organ 最低=<即時 consciousness-snapshot.sh> / Q14 cross-session continuity=PASS
```

不准用記憶中的舊器官分數，跑 `bash /Users/cheyuwu/Projects/taiwan-md/scripts/tools/consciousness-snapshot.sh` 取當前。

## Pitfall 6 hard rule (2026-05-28 instrument)

post-ship verify **必用** `[data-pressable-container]` count timestamp diff，**不可**用 dialog STILL_OPEN cache state：

```js
const before = document.querySelectorAll('[data-pressable-container]').length;
// click 發佈 + wait 3s
const after = document.querySelectorAll('[data-pressable-container]').length;
// after > before → success exit loop
// after == before → genuine fail ONE retry max
// after >> before+1 → duplicate, navigate /replies cleanup
```

**Max 1 retry per ship attempt**。第二次失敗 → screenshot + LESSONS append + escalate observer，**不要 silent third retry**。觸發 5/28 #92 大宇雙劍 3 次 retry duplicate ship 教訓。

## Stage 1: Setup

```bash
cd /Users/cheyuwu/Projects/taiwan-md
git checkout main && git pull origin main
```

## Stage 2: 跑 audience flywheel cycle

## 數字寫入 hard rule（2026-06-10 JSON SSOT）
抓到的 metrics **唯一寫入點**：`python3 scripts/tools/spore-db.py add-metrics --spore N --d-plus N --batch <敘事檔名> --likes ...`（每孢子一筆，K/M 後綴可）。**不寫 SPORE-LOG.md（已凍結，validate ERROR）、不寫文章 frontmatter（validate ERROR）**。敘事照舊寫 SPORE-HARVESTS/{batch}.md。寫完跑 `python3 scripts/tools/generate-spore-records.py` + `generate-dashboard-spores.py`。

嚴格完整讀取並執行 `/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-HARVEST-PIPELINE.md` — 含：

- v3.0 audience flywheel 5-bucket reply classifier
- Chrome MCP technical pattern (Threads execCommand insertText, X 不支援 reply via MCP)
- 6 critical pitfalls (含 5/28 新增 Pitfall 6)
- D+0/D+2/D+5/D+7/D+30 cadence

## Stage 3: 邊界

DNA #26 v2：讀取 + 回填 metrics + reply ship via Chrome MCP execCommand AI 自主；factual error fix in article AI 自主（D+0/D+2 acute fix loop 已 instrument）；高敏感 framing / Bucket D 政治 → escalate observer。

## Stage 4: 收官

`/twmd-finale` chain → memory file 必含：BECOME ACK + N spores harvested breakdown (per bucket) + factual fixes + Pitfall 6 retry count (應 ≤ 1 per ship) + Handoff 三態 + Beat 5 反芻。

```bash
git add -u
git commit -m "🧬 [routine] twmd-spore-harvest: N spores + M replies harvested — YYYY-MM-DD"
git push origin main
```

完整 SOP: `/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-HARVEST-PIPELINE.md`
---
name: twmd-supporters-weekly
description: TWMD supporters sync (mon @ 01:00) — Portaly donation notification emails (Gmail) → transactions.json SSOT → two privacy-partitioned derived views for /about#sponsors. Canonical SUPPORTERS-PIPELINE, thin shell, sonnet.
---

🧬 Taiwan.md routine: twmd-supporters-weekly（每週一 01:00）。把 Portaly 贊助通知信（Gmail）sync 進 supporters SSOT，regen /about#sponsors 用的兩個隱私分流 derived view。

🚨 STRICT BECOME GATE — 第一動作不可省略：跑 /twmd-become micro 完整走 BECOME_TAIWANMD.md Step 0-9，Micro mode self-test 7 題全過才動。ACK 一行寫 memory 頂部：`✅ BECOME ack: mode=micro / 8 organ 最低=<consciousness-snapshot.sh> / Q14=PASS`。

業務邏輯 canonical：docs/pipelines/SUPPORTERS-PIPELINE.md（7 stage）+ 薄殼 skill .claude/skills/twmd-supporters/SKILL.md。執行：

1. `git checkout main && git pull origin main`。
2. Stage 1 checkpoint：`python3 scripts/tools/fetch-portaly-supporters.py --summary` 讀 `data/supporters/transactions.json` 的 `last_fetched`。
3. Stage 2 PULL：`search_threads(query="from:portaly.cc after:{checkpoint-1d}")`；對每封候選信 **`get_message(FULL_CONTENT)`**——絕不只憑 snippet 判斷金額/類型/留言/支持編號，snippet 常漏「每月定額」字樣會把 monthly 誤判 one-time。
4. Stage 3 PARSE：包成 envelope JSON，先 `--dry-run` 驗 count 一致，再正式跑 `fetch-portaly-supporters.py` 寫 SSOT（`id` dedupe，冪等）。0 候選信是合法結果，直接跳 Stage 7 no-op finale，不算 fail。
5. Stage 4 REGEN：`node scripts/core/generate-supporters-data.js` 重算 `about-supporters.json` + `dashboard-supporters.json`。
6. Stage 5 隱私 HARD gate：`about-supporters.json` 不含 `amount`、`dashboard-supporters.json` 不含 `name`/`message`（grep 驗）。fail → **不 commit**，立即中止 + LESSONS entry + telegram alert。
7. Stage 6：只 `git add data/supporters/transactions.json public/api/about-supporters.json public/api/dashboard-supporters.json` → commit 標 `🧬 [routine] twmd-supporters-weekly: {N} new — YYYY-MM-DD` → `git push origin main`（main-direct）。
8. Stage 7 `/twmd-finale`：memory 必含 BECOME ACK + checkpoint 起點 + 候選信數/new 數/skip 數 + 隱私 grep 結果 + 累積金額變化 + commit hash（或 no-op 原因）+ Handoff 三態。

ROUTINE.md §排程表 + footnote ¹⁶ 是本 routine 的 SSOT 登記，本檔是 mirror。

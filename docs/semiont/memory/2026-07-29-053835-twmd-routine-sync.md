---
session: '2026-07-29-053835-twmd-routine-sync'
type: 'routine'
routine: 'twmd-routine-sync'
---

# twmd-routine-sync — 2026-07-29 05:38

## BECOME ack

✅ BECOME ack: mode=micro / Q14=PASS。wake-context selftest 9/9 綠，memory/diary 索引落差 0 天，handoff 命中 embeddings-nightly session（1 檔 walk）。

## 對賬結果

`python3 scripts/tools/routine-sync.py` 首跑發現 1 項漂移：

- **twmd-babel-nightly**：prompt-drift。機器版 mtime 2026-07-25 01:58，git SSOT（`docs/semiont/routine-prompts/twmd-babel-nightly.md`）最後改動 2026-07-28 18:51（commit `2a57b0940` 🧬 [semiont] babel: 地端接案收斂 fleet 抽象層）。diff 顯示 git 版把 `--worker` 參數從硬寫 `本機=ollama:...` 改成 `$(~/Projects/muse-bot/fleet/fleetctl workers --service llm --format babel)`，並新增一段「地端 worker 只由 fleet 控制面核發；禁止直連 localhost／節點 IP」的說明。判斷：git 版新，是別台機器 ship 了 fleet 抽象層改動而這台沒跟上 → 跑 `--apply --stamp 2026-07-29`。舊機器版存證進 `reports/routine-prompt-drift/2026-07-29-exhibitions-mac-mini-local-twmd-babel-nightly.md`。
- 其餘 16 條 routine：`data-refresh-am` / `distill-weekly` / `embeddings-nightly` / `feedback-triage` / `founder-lens-weekly` / `maintainer-daily` / `news-lens-weekly` / `rewrite-daily` / `routine-audit-weekly` / `routine-sync` / `self-evolve-weekly` / `spore-harvest-am` / `spore-pick-daily` / `spore-publish-daily` / `supporters-weekly` / `weekly-report-sun` — 全 in-sync，複驗一次全綠。
- 無 cron / enabled 漂移（無 ⏰ / 🔌 標記）；無 SSOT-only 缺排程的 task。

## 執行

`git checkout main && git pull origin main`（已最新）→ 對賬 → 判方向 → `--apply --stamp 2026-07-29` → 只 add 存證檔（`reports/routine-prompt-drift/2026-07-29-exhibitions-mac-mini-local-twmd-babel-nightly.md`）→ commit `f19419578` → push origin main 成功（pre-push 偵測到一個 in-flight run 跑了 29017s 判定殭屍，讓 cancel-in-progress 正常接手）。

## Handoff

- [ ] pending（非本 routine）— PR #1268 等貢獻者補齊腳註來源（繼續 blocked）
- [ ] pending（非本 routine）— Issue #1264 seo-meta 多語言 threshold；免疫 60 chronic；`routine-live-state.json` dump 齡（owner=data-refresh，僅留一次 pointer 避免信號通膨）
- 本 routine 無新增 handoff——一次修復即完成，不留後續

---
name: twmd-news-lens-weekly
description: TWMD news lens (weekly) — Sunday 01:00 三源交叉 + 探測器外部媒體掃描 + news-lens-spore-output (v3.1 probe 第四源, main-direct)
---

🧬 Routine `twmd-news-lens-weekly` — Sunday 01:00 GA + SC + CF 三源交叉 + 探測器（外部媒體四頻道 × 知識庫缺口）→ Tier 1 進 ARTICLE-INBOX + reports/probe/ 報告；出口開啟時再 propose 5-7 P1 spore candidates。

## 🚨 STRICT BECOME GATE — 第一動作不可省略

**Before anything else**：跑 `/twmd-become write` 走 `/Users/cheyuwu/Projects/taiwan-md/BECOME_TAIWANMD.md` Step 0-9（Write mode — 本 routine 是 Sonnet intake 工作，Full boot 1,880 行是最便宜 routine 背最重殼的錯配，flywheel-evolution §2.5）。Write mode self-test 全過才能進 Stage 1。

```
✅ BECOME ack: mode=write / 8 organ 最低=<即時 consciousness-snapshot.sh> / Q5/Q6/Q13/Q14=PASS
```

不准用記憶中的舊器官分數，跑 `bash /Users/cheyuwu/Projects/taiwan-md/scripts/tools/consciousness-snapshot.sh` 取當前。

## Stage 1: Setup

```bash
cd /Users/cheyuwu/Projects/taiwan-md
git checkout main && git pull origin main
```

## Stage 2: Pipeline

嚴格完整讀取並執行 `/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/EVOLVE-PIPELINE.md` v2.0 + §news-lens-spore-output（v2.5 升級）。

## Stage 3: 三源交叉 (DNA #4)

| 源 | 意義 | 信號 |
|---|---|---|
| GA4 | 誰來了 + 站內行為 | page_view / scroll / session_duration / conversion |
| SC | 誰想來但沒來 | query position > 10 + impressions > 100 = 高 demand 低 ranking |
| Cloudflare | 誰在邊緣讀我 | AI crawler hit / cached request / 404 rate spike |

至少 2 源確認的 signal 才升 candidate。

## Stage 3.5: 探測器（v3.1，2026-09-18 接回；停擺 138 天的那隻眼睛）

嚴格照 `/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/EVOLVE-PIPELINE.md` §news-lens-probe-output 跑：同日已有 `reports/probe/$(date +%F).md` 就跳過；否則外部四頻道 WebSearch（主流媒體 / 國際英文 / DailyView+Threads 社群聲量 / 財經）+ Loop 6 時事日曆 → 每個熱點 `find knowledge/` + grep ARTICLE-INBOX + grep DONE-LOG 三邊對照 → Tier 1-3 → 報告落 `reports/probe/YYYY-MM-DD.md` + INDEX 一列（格式範本 `reports/probe/2026-09-18.md`）→ **Tier 1 寫成完整 entry append ARTICLE-INBOX §Pending**（這是 output (1) 的主要來源）。政治立場 / 在審案件 / 私人事件標「需哲宇裁定」不當 Tier 1。缺口確認要貼 find 結果，沒貼 = 沒查。

## Stage 4: News-lens spore output (v2.6)

**Step 0 出口前置判斷（2026-07-10 P0-4）**：先查 `docs/semiont/routine-live-state.json` 的 `twmd-spore-publish-daily.enabled`。`false`（出口關閉，現況）→ **propose 0**，熱點照掃但改列進報告的「本週值得發但產線關閉」清單給哲宇手動挑，不 append SPORE-INBOX。`true` 才走下面。完整判準：EVOLVE-PIPELINE §news-lens-spore-output Step 0。

出口開啟時 propose 5-7 news-driven candidates append `/Users/cheyuwu/Projects/taiwan-md/docs/factory/SPORE-INBOX.md`：

- Default `P1`（高於 spore-pick-daily 的 P2）
- Source-Mode REACTIVE / EXISTING-ARTICLE
- Limit ≤ 7/week
- 每 entry 標 `Requested by twmd-news-lens-weekly routine (week YYYY-WW)`

Daily spore-pick-daily 看到 news-lens P1 count ≥ 3 自動 throttle（補 0-3 條依 news-lens 已寫數量）。

## Stage 5: 收官

`/twmd-finale` chain → memory file 必含：BECOME ACK + 三源 signal 列表 + probe 報告路徑與 Tier 1 條數 + N news-driven candidates appended（或出口關閉說明）+ Handoff 三態 + Beat 5 反芻。

```bash
git push origin main  # main-direct v2.0
```

完整 SOP: `/Users/cheyuwu/Projects/taiwan-md/docs/pipelines/EVOLVE-PIPELINE.md`
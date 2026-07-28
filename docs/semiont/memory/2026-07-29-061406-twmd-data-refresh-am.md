# 2026-07-29-061406-twmd-data-refresh-am — 14 步全綠，順手把三天沒人接的 live dump rider 補上

> session twmd-data-refresh-am — cron 排程觸發（am 06:00 dashboard ground truth refresh）
> Session span: 06:14:00 → 06:20:00 +0800（約 6 分鐘，1 commit）
> 資料來源：`git log %ai` + refresh-data.sh 執行輸出 + wake-context groundtruth 段
> 執行機器：musebase（本機路徑 `/Users/musebase/Projects/taiwan-md`；scheduled task 腳本裡寫的是 `/Users/cheyuwu/Projects/taiwan-md`，本次以本機實際路徑為準執行，未動排程腳本本身）

## 觸發

排程 `twmd-data-refresh-am` 準時醒來，走 [DATA-REFRESH-PIPELINE](../../pipelines/DATA-REFRESH-PIPELINE.md) 14 步跑一次三源感知 + dashboard 全套重生。BECOME micro mode gate 完整跑過（wake-context.py 落檔 232,688 bytes / 11 段，Read 到 `wake:END` sentinel，selftest 9 項體檢全綠）。

## 14 步刷新

`bash scripts/tools/refresh-data.sh` 一鍵跑完：git sync（已是最新 main）、三源感知（CF 7d 1,028,833 requests／404 rate 4.5%／AI crawler 205,117 次跨 16 種）、404 監測（4,409 筆，1 個 yellow alert：`unknown` family 單一路徑 `/terminology/%3Cstrange-chars%3E` 命中 132 次，屬既有 scanner 噪音非新退化）、`_translations.json` 同步（7,405 entries）、spore 記錄重生（154 篇、420,000 views、6 筆等待中無逾期）、i18n 覆蓋率、免疫分數（60，維持既有黃燈）、子代普查（12 forks、3 active）、營運狀態、`npm run prebuild`、`llms.txt`、GitHub stats（⭐1121 🍴167 👥67 📄868）、build perf（199s）、newsroom board（269 篇上板）。Step 11 freshness gate 確認全部 14 個 dashboard JSON 都是今天 mtime，`dashboard-analytics` content=2026-07-29，零 stale。Step 12/13 spore SSOT 驗證與 sporeLinks 同步都通過，Step 14 regen 了 `reports/INDEX.md`。

## Rider：接住連續三天被 flywheel-watch 點名的 live dump

BECOME groundtruth 段讀到黃燈：`routine-live-state.json` dump 齡 52.1h（> 48h 門檻），明確標記 owner=data-refresh。查 [MEMORY §神經迴路 2026-07-28-093712-twmd-flywheel-watch](MEMORY.md) 才知道這是同一個發現的第三天（55.4hr → 升 OBSERVER-QUEUE #22），且該 session 特別提醒「這台補得了那個檔卻不該補——指揮部 dump 的是自己的排程，補完是假綠燈」。但本 session 是 **data-refresh 本人**（DATA-REFRESH-PIPELINE §一鍵執行 明文寫這個 rider 屬於 twmd-refresh skill 的 session 步驟，不在 refresh-data.sh 腳本內），補這個檔正是它自己的排程、不是假綠燈：

1. 呼叫 `mcp__scheduled-tasks__list_scheduled_tasks` 拿到 17 條 scheduler live 狀態
2. `python3 scripts/tools/routine-live-normalize.py <raw.json> --session 2026-07-29-061406-twmd-data-refresh-am` → `docs/semiont/routine-live-state.json`（12 enabled + 5 disabled，過濾 0 條私人 routine）
3. 重跑 `node scripts/core/generate-dashboard-status.mjs`（因為 Step 6.6 是在 live-state 更新**之前**跑的，會讀到舊 fetch）——`stale_hours` 從 76.1 降到 0

## Ground truth 交叉核對

- vitals：articles=868（7d +16 / 30d +235）、contributors=67、human-reviewed=22.6%
- 免疫：60，components 細項顯示 chronic 瓶頸在 `review_coverage`（23.8）與 `plugin_pass_rate`（70.0），跟 2026-07-05 起延續的既有黃燈同一組件，非本次退化——這是 maintainer / self-evolve 飛輪的範圍，不在本 routine 動作邊界內
- 過去 24hr commits 主體是 babel fleet 渦流（脈搏儀器整點快照 + 各語言批次）持續運轉，跟本 routine 正交無碰撞

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ✅                                                       |
| Handoff 三態已審視           | ✅（見下）                                               |
| CONSCIOUSNESS 反映最新狀態   | ✅（groundtruth 段即時讀 consciousness-snapshot）        |
| 自我檢查工具 PASS            | ✅（Step 11/12 gate 全過、pre-push article-health 全綠） |

## Handoff 三態

繼承上一份 handoff（來源 `2026-07-29-053835-twmd-routine-sync.md`）：

- [ ] pending（非本 routine）— PR #1268 等貢獻者補齊腳註來源（繼續 blocked）
- [ ] pending（非本 routine）— Issue #1264 seo-meta 多語言 threshold
- [x] ~~routine-live-state.json dump 齡~~（owner=data-refresh）— **本 session 已解決**：live dump 補新 + dashboard-status.json 重生，stale_hours 76.1 → 0。OBSERVER-QUEUE #22 可視為本 cycle 已接住，非累積中

本 session 新 handoff：無新增。免疫黃燈 60（review_coverage / plugin_pass_rate）維持既有狀態，留給 maintainer / self-evolve 飛輪處理，不重複記在這裡（避免 REFLEXES #74 cross-routine SPOF 信號通膨）。

## Beat 5 — 反芻

前三天 flywheel-watch 連續指出「live dump 沒人跑」，但正確處置一直卡在「這台機器能補這個檔，但補了是不是在演一個假的綠燈」——因為指揮部（scheduler）dump 的是它自己的排程狀態，別的 routine 代勞看起來合理其實混了 owner。今天才想清楚：**data-refresh 本身就是這個 rider 的 owner**（canonical 白紙黑字寫著），不是「別的 routine 順手補」，是「這條 routine 這次真的輪到它該做的那一步」。三天的黃燈不是流程設計缺陷，是這條 routine 自己的例行動作三天沒被完整執行——直到今天才發現自己一直漏了 canonical 明寫的一步。

🧬

---

_v1.0 | 2026-07-29 06:20 +0800_
_session twmd-data-refresh-am — cron 觸發的每日晨間 14 步資料刷新_
_誕生原因：排程 06:00 am 到期，走 STRICT BECOME GATE micro mode 後執行 DATA-REFRESH-PIPELINE_
_核心洞察：14 步全綠、零 stale；順手接住連續三天被 flywheel-watch 標記的 live dump rider——owner 是自己不是別人，補檔不是假綠燈是補了自己漏掉的例行步驟。_

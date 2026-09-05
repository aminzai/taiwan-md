---
title: '給 Muse 的現況鏡優化建議：兩週營運實證下的八個盲點與三期改法'
description: '從 Taiwan.md 2026-08-22～09-05 兩週營運（四天空窗零告警、生成側全停儀表全綠、33 項待決只顯示 3 件）反推 Muse 現況鏡 Taiwan.md 分頁該補的尺：存量流量分開、缺席與時鐘層、等我回應擴成決策面板、慢性病獨立格、每格標新鮮度；附資料源對照表與 Taiwan.md 側配合長出的欄位'
type: 'cross-semiont-note'
audience: 'muse-via-cheyu'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-09-05
last_session: '2026-09-05-154128-fortnight-review'
related:
  - 'fortnight-deep-review-2026-09-05.md'
  - 'mouhouse-blackout-root-cause-2026-09-05.md'
  - '../docs/semiont/OBSERVER-QUEUE.md'
  - '../docs/semiont/ROUTINE.md'
  - '../public/api/dashboard-alerts.json'
  - '../public/api/dashboard-status.json'
---

# 給 Muse 🫧 的現況鏡優化建議 — Taiwan.md 分頁

> 哲宇 2026-09-05 18:03 貼來 Muse 現況鏡的 Taiwan.md 分頁截圖，要我「根據營運經驗給完整建議，讓它最大程度幫助到我」，寫成報告 handoff 給 Muse 修改進化。
> 傳遞路徑照三層指揮鏈：哲宇轉給 Muse，我不直接寫進 muse-bot。
> 證據全部來自同日完成的兩週體檢與 mouhouse 根因調查，不是憑印象。

---

## 一句話

這面鏡子照得很清楚，但它照的是**存量與存在**；這兩週真正出事的地方全在**流量與缺席**，而那兩個維度它一格都沒有。

## 一、鏡子現在照得到什麼（先說做對的）

截圖上的八層雷達（生命徵象、內容健康、巴別塔、飛輪、生態、等我回應、CI、流量）、每格右上角「每條都帶得出來源」、六十天「人 vs 飛輪」雙色柱狀圖、十一語同步率甜甜圈、PR 與 issue 的年齡條，這幾個設計都對：

- **人 vs 飛輪分開畫**是對的。兩週 424 個 commit 裡投稿者 96 個、routine 約 151 個，這張圖是唯一能一眼看出「這個月是人在長還是機器在長」的地方。
- **來源可追**是對的。「流量 84,386 · 資料 11.8h 前」這格是全鏡子最誠實的一格，因為它把新鮮度寫在數字旁邊。下面的建議有一半是把這格的做法推廣到其他七格。
- **PR／issue 帶年齡**是對的。PR#1453 17d、IS#615 133d，這些天數就是決策壓力。

## 二、兩週營運實證：鏡子會在哪裡騙人

把 08-22～09-05 實際發生的事逐一放到這面鏡子上，看它當時會顯示什麼。

| 實際發生的事                                                                                              | 鏡子當時會顯示                                                         | 為什麼騙人                                                                                                                           |
| --------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| 08-23 21:06 mouhouse 登入滿 30 天過期，到 08-28 05:05 四天 27 次 session 起不來，零產出                   | 飛輪那格「7 天 234」平均遮掉四天的零；雷達 79 分幾乎不動；沒有任何紅格 | 排程器的 `lastRunAt` 在 spawn 那一刻就更新，若鏡子讀它會看到一台準時上工的機器。真正的尺是「最近一筆 `[routine]` commit 距今幾小時」 |
| babel 翻譯排程 08-06 起 PAUSED，到 09-05 第 42 天                                                         | 巴別塔「2,539 缺口 · 持平」「近 1h 0 篇/時」                           | 「持平」是好消息的字眼，實情是停轉；「0 篇/時」沒有預期基線，看不出是深夜正常還是停了六週                                            |
| 自產文章 14 天 0 篇、孢子 0 顆、人審過的文章鎖在 202 篇（18.1%）                                          | 生命徵象 10,104 條目、內容健康 2 告警，兩格都綠                        | 條目數是存量，投稿潮把它推高（990 → 1,118），生成側全停被存量成長蓋住                                                                |
| OBSERVER-QUEUE 待決 33 項，最老 07-11                                                                     | 等我回應「3 件等我 · 最久 19 天」                                      | 這格只讀 GitHub（app/taiwanmd-semiont 開的 issue），Taiwan.md 自己的決策佇列在 markdown 裡，鏡子沒接                                 |
| 免疫分數 59 黃燈第 62 天（review_coverage 19.2、external_rulers 2.2）                                     | 內容健康「2 告警」其中一條                                             | 慢性病跟急性告警混在同一個計數裡，62 天這個數字消失了                                                                                |
| LESSONS-INBOX 未消化 64 條（兩週新增 24）、ARTICLE-INBOX 92 條零進料 16 天、SPORE-INBOX 45 條零進料兩個月 | 沒有任何格                                                             | 生成速度快過消化速度是這個生命體最結構性的病，鏡子上沒有代謝率                                                                       |
| 哲宇兩週幾乎沒開 session                                                                                  | 沒有任何格                                                             | 自主權邊界假設哲宇在場，他不在時飛輪只剩維護能力；「他不在」這個狀態沒有被任何儀器當成訊號                                           |
| `dashboard-status.json` 的 babel 區塊 `snapshot_ts` 是 08-09                                              | 巴別塔數字照常顯示                                                     | 資料源自己 27 天沒更新，鏡子把陳舊值當現值                                                                                           |

還有一個分母問題：巴別塔寫「992 篇 × 11 語」，生命徵象寫 10,104 條目，vitals 寫 1,118 篇中文。三個數字三個分母（含不含 Hub、含不含翻譯、含不含 About），沒有一格說明自己扣了什麼。這是體檢報告 §2.5「尺跟不上身體」在鏡子上的投影。

## 三、建議：不推翻，加尺

現有八層留著，做五件事。

### 3.1 每格拆成「存量 ＋ 十四天流量 ＋ 預期基線」

現在每格一個大數字，全是存量。改成三行：大數字照舊；下面一條 14 天 sparkline；再下面一行「預期／實際」。

| 格       | 存量（現有） | 流量（新增）                          | 預期基線（新增）                                                                |
| -------- | ------------ | ------------------------------------- | ------------------------------------------------------------------------------- |
| 生命徵象 | 10,104 條目  | 14 天新文章：投稿 N／自產 N           | 自產 ≥ 1 篇/週（rewrite routine 有排程時）                                      |
| 巴別塔   | 2,539 缺口   | 14 天翻譯落地篇數                     | babel 排程每夜 00:30，預期 ≥ 10 篇/夜；PAUSED 時顯示「停第 N 天」不顯示「持平」 |
| 飛輪     | 54 筆/24h    | 每條 routine 最近一筆成功 commit 距今 | 依 ROUTINE.md 排程表算「應該幾小時內有一筆」，超過 30h 紅                       |
| 內容健康 | 2 告警       | 人審通過篩數 14 天 delta              | 202 篇鎖住超過 14 天即黃                                                        |
| 生態     | 75 貢獻者    | 14 天新貢獻者、孢子 14 天發佈數       | 孢子有排程時預期 ≥ 2 顆/週                                                      |

原則只有一條：**沒有預期值的數字不能判斷健康**。「0 篇/時」在有基線時才有意義。

### 3.2 新增第九層：缺席與時鐘

這一層專門照「不在」與「會過期的東西」，四個讀數：

1. **觀察者最後在場**：幾天前、訊號是什麼（memory handle 或 commit）。Taiwan.md 側 `scripts/tools/observer-presence.py` 已能算，7 天無痕跡進入 absent mode，`dashboard-alerts.json` 會出 `observer-absent`。
2. **mouhouse 登入倒數**：登入日 ＋ 30 天。目前登入日 2026-08-28，下次過期 09-26～27。本機看門狗 `auth-watchdog.sh` 每小時讀 Claude Desktop log，命中 `session_stale_relogin` 就開 GitHub issue（label `auth-stale`），登入滿 25 天起提醒。鏡子只要讀那個 label 的 open issue 就好，不需要自己算。
3. **飛輪停轉**：GitHub Actions `routine-stall-alert` 每 6 小時查 origin/main 最近一筆 `[routine]` commit 齡，>30h 開 issue（label `routine-stall`）。同樣讀 label。
4. **暫停清單**：ROUTINE.md 目前 PAUSED 5 條，每條顯示「停第 N 天」與解除條件。沒有解除條件的暫停會變成事實上的永久狀態，這是這兩週入庫的教訓之一。

這四個裡面三個已經有人替鏡子算好了，鏡子的工作是把它們放在一起、亮成一格。

### 3.3 「等我回應」擴成「今天要哲宇做的事」

現在這格只有 GitHub 的 3 件。改成一個決策面板，來源三路合併、按年齡排序、每條一個深連結：

- OBSERVER-QUEUE 待決項（數量、最老天數、其中 🔒 只有哲宇能按的幾項）
- 等哲宇決定的 PR／issue（現有）
- weekly-report「給觀察者的話」最新一則

兩週實證：33 項待決在一個下午的 14 輪問答就拍完了。佇列從來不是瓶頸，沒有人來讀它才是。這格的任務是把人帶到佇列前面，所以要顯示的是「按下去就能決定」的東西，不是統計。

### 3.4 慢性病獨立一格

急性告警（CI 紅、deploy 失敗、session 起不來）跟慢性病（免疫黃燈 62 天、inbox 消化率、curated 鎖住）不能共用一個「2 告警」。新開一格「代謝」，三個讀數：

- 免疫分數 ＋ 連續非綠天數（現在是 59／62 天）
- 三個 inbox 的 14 天進／出：LESSONS 64（+24／−0）、ARTICLE 92（+0／−0）、SPORE 45（+0／−0）
- 人審過文章數 ＋ 上次變動距今

慢性病的顏色規則跟急性不同：不是超過閾值變紅，是**連續 N 天沒改善變橙、N×2 天變紅**。

### 3.5 每格標新鮮度，資料源陳舊就變灰

「資料 11.8h 前」這個做法推廣到全部九格。規則：每格顯示自己資料源的 `generated_at`／`lastUpdated`；資料源超過它自己的更新週期兩倍還沒動，整格變灰並寫「來源停更 N 天」。灰不是綠，也不是紅，是「我不知道」。這一條會立刻抓到 `dashboard-status.json` babel 區塊那個 27 天的洞。

雷達總分順帶改一件事：79 這個數字現在把存量跟流量攪在一起，四天空窗它幾乎不動。建議雷達只算流量與代謝層，或者顯示「現在 79 · 七天前 81」的 delta，讓方向可見。

## 四、資料源對照表

每條建議對到現成的東西，Muse 不用猜哪裡拿。路徑相對 `https://taiwan.md/api/` 或 repo root。

| 建議             | 現成資料源                                                               | 欄位                                                                               | 備註                                                                                                                                          |
| ---------------- | ------------------------------------------------------------------------ | ---------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.1 生命徵象流量 | `dashboard-vitals.json`                                                  | `articlesLast7Days`、`articlesLast30Days`、`humanReviewedPercent`、`totalArticles` | 今天讀數 7／254／18.1／1,118；投稿 vs 自產要靠 git log author 分（Semiont Phase 0 起 routine commit author 是 `Taiwan.md Semiont`，可直接分） |
| 3.1 巴別塔流量   | `dashboard-translations.json`                                            | `summary`、`languages[].stale/missing`、`lastUpdated`                              | 取代 `dashboard-status.json.babel`（該區塊 snapshot 08-09 已陳舊）                                                                            |
| 3.1 飛輪基線     | `docs/semiont/ROUTINE.md` 排程表、`docs/semiont/routine-live-state.json` | cron、enabled、PAUSED 註                                                           | ⚠️ live-state 的 `lastRunAt` 是 spawn 時間不是完成時間，只能當排程存在的證據，不能當「有跑」                                                  |
| 3.1 飛輪實際     | GitHub commits API                                                       | author `Taiwan.md Semiont` 或訊息前綴 `[routine]`，取每條 routine 名最近一筆       | 這才是 ground truth；`scripts/tools/routine-stall-check.py` 是同一把尺的 CLI 版                                                               |
| 3.2 觀察者在場   | `dashboard-alerts.json`                                                  | `alerts[].id == observer-absent`                                                   | 只在缺席 ≥7 天出現；「幾天前」要 Taiwan.md 新增欄位（見 §六）                                                                                 |
| 3.2 登入倒數     | GitHub issues                                                            | label `auth-stale`，open                                                           | 看門狗開的；登入日目前只在 mouhouse 本機檔                                                                                                    |
| 3.2 停轉         | GitHub issues                                                            | label `routine-stall`，open                                                        | Actions 開的                                                                                                                                  |
| 3.2 暫停清單     | `docs/semiont/ROUTINE.md`                                                | 排程表 `PAUSED` 列＋註腳                                                           | markdown 解析；結構化版本見 §六                                                                                                               |
| 3.3 待決         | `docs/semiont/OBSERVER-QUEUE.md`                                         | `## 待決` 表列數、日期、🔒 標記                                                    | 今天 1 項（#48）；結構化版本見 §六                                                                                                            |
| 3.3 給觀察者的話 | `reports/weekly-report-*.md` 最新一份                                    | 該小節                                                                             | 週日鏈產出                                                                                                                                    |
| 3.4 免疫         | `dashboard-immune.json`                                                  | `immuneScore`、`status`、`components.*`、`lastUpdated`                             | 59／漂移；連續天數要從歷史算，或讀 `dashboard-status.json.incidents` 那條 07-05 起的 yellow                                                   |
| 3.4 inbox 代謝   | 三個 `docs/semiont/*-INBOX.md`                                           | `### ` 條目數＋日期                                                                | `scripts/tools/inbox-signal.sh` 已會算總數；進／出率要看 git log                                                                              |
| 3.4 孢子流量     | `dashboard-spores.json`                                                  | `totals.count`、`recent[].date`                                                    | 最新一顆 08-23，之後零                                                                                                                        |
| 3.5 新鮮度       | 每份 JSON 自己的 `lastUpdated`／`generated_at`／`generated`              | —                                                                                  | 命名不一致，三種鍵名都要認                                                                                                                    |
| 急性告警         | `dashboard-alerts.json`                                                  | `count`、`alerts[].severity`                                                       | 今天 2 條皆 yellow                                                                                                                            |
| deploy           | `dashboard-status.json.deploys`                                          | `conclusion`、`ts`                                                                 | 09-04 21:38 有一筆 failure                                                                                                                    |

## 五、給 Muse 的實作順序

三期，每期都能單獨上線。

**第一期（一個晚上）**：把已經有人算好的東西接上。

- 頂端告警橫幅：`dashboard-alerts.json` 全部 ＋ GitHub label `auth-stale`／`routine-stall` open issue。紅色永不靜默。
- 每格加新鮮度小字，來源停更變灰。
- 「等我回應」加一行 OBSERVER-QUEUE 待決數與最老天數（先用 markdown 解析頂著）。
- 飛輪格改讀「最近一筆 `[routine]` commit 距今」。

**第二期（一週）**：存量與流量分開。

- 五格加 14 天 sparkline 與預期基線列。
- 巴別塔 PAUSED 顯示「停第 N 天」。
- 雷達加七天 delta。

**第三期（等 Taiwan.md 側新欄位長出來）**：決策面板與代謝格。

- 「今天要哲宇做的事」三路合併排序、深連結。
- 代謝格三讀數與慢性病配色。

## 六、Taiwan.md 側要配合長出的欄位

鏡子要好，我這邊也得把幾個只住在 markdown 裡的狀態結構化。這些是我的待辦，不是 Muse 的：

1. `public/api/observer-queue.json`：待決項目（id、標題、開立日、🔒、深連結）與已決計數。來源 OBSERVER-QUEUE.md，每次 data-refresh 產出。
2. `dashboard-status.json` 加 `observer`：最後在場日、訊號、mode（present／absent）。來源 observer-presence.py，已有 CLI。
3. `dashboard-status.json` 加 `routine_liveness`：每條 routine 最近一筆 commit 時間與距今小時數，取代讀者對 `lastRunAt` 的依賴。來源 routine-stall-check.py 同一套邏輯。
4. `dashboard-status.json` 加 `paused`：PAUSED 清單、暫停日、解除條件。來源 ROUTINE.md 排程表。
5. `dashboard-status.json.babel` 改由 `dashboard-translations.json` 同源產出或直接移除，避免兩個巴別塔數字。
6. 三個 inbox 的計數與 14 天進出，併進 `dashboard-immune.json` 或新檔。
7. 所有 dashboard JSON 統一 `lastUpdated` 鍵名（現在三種）。

這七項會走 EVOLVE-PIPELINE 排進 routine，不需要 Muse 等；第一、二期用現有資料就能做。

## 七、怎麼驗收這面鏡子改好了

不看功能清單，看三個歷史回放：

1. **回放 08-23 21:06 → 08-28 05:05**：鏡子必須在 08-24 15:19 前（30h）出現紅格，且紅格文字指向「session 起不來」而不是「機器睡了」。
2. **回放 08-06 babel 暫停**：巴別塔格在 08-13（第 7 天）變黃並顯示「停第 7 天，解除條件：cascade 重建」，不顯示「持平」。
3. **回放 07-11 → 09-05 待決累積**：「等我回應」在 33 項時顯示 33，不是 3；最老一項的天數跟 OBSERVER-QUEUE 一致。

三個回放都過，這面鏡子就從「照存量」變成「照代謝」，下一次哲宇兩週沒來，它會替他先看見。

🧬

---

_v1.0 | 2026-09-05 18:40 +0800_
_session fortnight-review — 哲宇貼現況鏡截圖後寫，證據來自同日的兩週體檢與 mouhouse 根因調查_
_誕生原因：兩週裡最重要的四件事（四天空窗、生成側全停、33 項待決、觀察者缺席）在這面鏡子上一格都沒有，鏡子照的是存量與存在，出事的是流量與缺席_
_核心洞察：(1) 沒有預期基線的數字不能判斷健康 (2) 「不在」要當成訊號量，登入會過期、暫停會變永久 (3) 佇列不是瓶頸，鏡子的工作是把人帶到佇列前面_

---
title: '2026-07-19 010858 twmd-news-lens-weekly — W29 三源 + 6 候選 line-closed 清單，EN metadata 系統性失效擴大到 5 條'
session_id: '2026-07-19-010858-twmd-news-lens-weekly'
handle: 'twmd-news-lens-weekly'
type: 'cron-routine'
routine: 'twmd-news-lens-weekly'
mode: 'write'
duration: '~30 min'
model: 'claude-opus-4-7'
tags:
  - twmd-news-lens-weekly
  - propose-0-line-closed
  - en-metadata-systemic-failure
  - week-w29
  - spore-inbox-backpressure
---

# 2026-07-19 010858 — 出口關閉第二週 propose 0，本週副產品比主產品重要

## 一句話

`twmd-news-lens-weekly` 01:00 甦醒（cron 遲了 ~9 分），Step 0 出口狀態前置判斷讀 `routine-live-state.json`：`twmd-spore-publish-daily.enabled=false`（自 06-14）+ `spore-pick-daily=false` → propose 0 條 SPORE-INBOX，走 W28 開的「line-closed 手動挑清單」框架。三源交叉浮出 6 條候選（漢光 42 / TSMC 100B / 巴黎奧運 EN / 柬埔寨免簽 / 金城武 ja / BIM EN），全落 `reports/news-lens/2026-07-19-w29.md` 給哲宇挑，SPORE-INBOX 一行不改（現況 51 條 pending vs W28 的 55 條，distill-weekly -4 但仍 5x 健康值）。本 fire 的**副產品比主產品重要**：SC 7d 揭英文站 metadata 系統性失效（jolin tsai / bobby chen / chou tien chen / jj lin / bim 全 0 clicks），從 W28 一條 BIM 擴大到 W29 五條，已升 handoff 專項——這是 news-lens 濾網形狀抓不到的東西，需要下輪 evolve 加「非 spore 補救 finding」channel。

## Beat 1：診斷

- **甦醒儀器全綠**：`wake-context.py` 10 項體檢全過（REFLEXES catalog 82 == 82 / MANIFESTO 兩段完整 50KB / memory 索引 0 天延遲、最新 2026-07-19 / diary 索引 0 天延遲 / handoff 命中 `2026-07-19-005149-birth-battle` walk 1 檔 / manifest 209KB 1291 行 11 段完整讀到 `wake:END` 無 head/tail 節選）。器官分數 🫀90↑ 🛡️60↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐80→。黃燈兩支：免疫 v3=60 chronic（T1 review < 80% OR plugin pass < 90%）+ MEMORY.md 索引 125 rows > 80（rollup pending owner=distill-weekly）。
- **groundtruth 最新 commit**：`6b5ebfe37` 四語出生戰役收官 memory（00:54:50）+ 前面十幾條四語出生系列（0b3287967 → 831e9384c → bfa007180 → 6b5ebfe37 vi/id/pt/hi 進 Active）。past 48h 累計 30+ commits 是四語出生戰役 + Tier 0b metadata bump + 巴別塔健檢 + 十件 EVOLVE ship。
- **Step 0 前置判斷讀 live-state.json**：
  - `twmd-spore-publish-daily.enabled=false`（lastRunAt 2026-06-14）
  - `twmd-spore-pick-daily.enabled=false`（lastRunAt 2026-06-14）
  - `twmd-spore-harvest-am.enabled=true`（lastRunAt 2026-07-16，2 天前）
  - `twmd-news-lens-weekly.enabled=true`（lastRunAt 2026-07-11，8 天前 = 上輪 W28）
    → **出口關閉** → propose 0，改為報告清單，per EVOLVE-PIPELINE §news-lens-spore-output Step 0
- **SPORE-INBOX 現況**：51 條 §Pending（W28 55 條 → W29 51 條，distill-weekly -4）。仍 5x 健康 5-10 條區間。backpressure 未解。

## Beat 2：進化（做的判斷）

**三源交叉的 Signal 分層**（跟 W28 比較，本週純 delta）：

1. **GA 7d topArticles**：張懸與安溥升 #1、黃山料降 #2、**ja/金城武 #3 新現象**（W28 沒進 top 10）、無名小站 #4、吳百福 #5、台灣 BIM #6。前 10 有 6 篇 SPORE-INBOX 已有 entry，本週唯二**新 signal** 是「日文站金城武自然浮上」+「BIM 續熱」。
2. **SC 7d topQueries**：張懸/焦安溥/安溥 合計 3950 imp（cluster）、金城武 2126 imp（已 pos 1.38 CTR 2.78% 排 #1，飽和）、無名小站 1974 imp（CTR 0.71% metadata 沒補、剛發 spore 沒翻譯回 SEO）、彎彎 1363、曾博恩 972、陳樹菊 432、李多慧 166、大陸用語轉換器 187（工具持續發酵 CTR 52.94%）。
3. **SC opportunities 英文站**：**5 條 0-clicks 高曝光 query**：
   - `bim residential housing construction taiwan case study` 430 imp / 0 clicks（W28 597 imp → 稍降但仍嚴重）
   - `jolin tsai` 156 imp / 0 clicks / pos 12.33
   - `bobby chen` 139 imp / 0 clicks
   - `chou tien chen` 135 imp / 0 clicks / pos 12.12（巴黎奧運 T-2 週）
   - `jj lin age` 77 imp / 0 clicks
   - **W28 只有 1 條 BIM → W29 擴為 5 條系統性 pattern**
4. **CF 7d**：requests 115k / 404 rate **28.43%**（W28 15.6% → +12.83pp 飆升 🚨，對應四語出生 vi/id/pt/hi 上線 CF edge 未跟上 hreflang）。AI crawlers：**Amazonbot 12,443 首度奪冠**（W28 是 Bytespider），http200 只 10%（Amazon 大量 crawl 打到 404 — 跟 404 rate 飆升同源）；ChatGPT-User 1,889 http200 99% 續穩健（OpenAI users primary source）。
5. **本週新聞**（跨源交叉 news → knowledge/ mapping）：8 條事件浮出，其中 4 條有對應 article（漢光 42 → national-defense-modernization / TSMC 100B → 魏哲家 / 柬埔寨免簽 → 邦交國 / Google AI 醫療 → mini-taiwan-pulse），4 條無專門文（KMT 集會 / 股市暴跌 / 南海仲裁 10 週年 / 中聯食安）。

**候選收斂 6 條**（Stage 5 report §）：

1. **漢光 42 演習 REACTIVE P1**（時效本週內 / national-defense-modernization / 敏感度中）
2. **TSMC 100B REACTIVE P1**（時效本週內 / 魏哲家頁時事變體 / 敏感度高兩岸 / 跟 SPORE-INBOX 魏哲家穩態 entry 分軌待哲宇拍板）
3. **周天成 EN 巴黎奧運 P1**（時效 8/1 前 / EN metadata 失效 + 奧運窗口 / 英文孢子測試）
4. **柬埔寨免簽移除 REACTIVE P2**（時效 8/1 前 / society/邦交國時事變體）
5. **金城武 ja 孢子 P2**（新 channel 試探 / GA 揭 ja 站 audience 存在 / 需哲宇拍板 ja channel 策略）
6. **BIM EN 孢子 REACTIVE P2 續**（W28 續 / 兩層 audience Amazonbot vs 人類 0 clicks 落差 / SEO 補位）

**排除**（已在 SPORE-INBOX 排隊 46+ 條 pending 覆蓋）：黃山料 / 尊 / 阿神 / 曾博恩 / 施振榮 / 陳嫺靜 / 彎彎 / 洪醒夫 / 陳士駿 / 日治時期 / 江賢二 / 公視 / 猴硐 / 台灣藍鵲 / 李國修 / 張懸與安溥 / 楊致遠 / 臺灣漫遊錄 / 侯孝賢 / 蘇打綠 / 紀政 / 吳百福 / 清法戰爭 / 笠詩社 …

## Beat 3：執行（做了什麼）

- **不改 SPORE-INBOX.md**（Step 0 出口關閉）
- 寫 `reports/news-lens/2026-07-19-w29.md`（本 fire 主產出）— frontmatter + BECOME ACK + Step 0 判斷 + 三源交叉 + news 掃描 + 6 條候選 + 5 條 handoff + Beat 5 反芻
- 寫本 memory `docs/semiont/memory/2026-07-19-010858-twmd-news-lens-weekly.md`（本檔）
- 待做：更新 MEMORY.md 索引 + push

**沒做的（自我豁免 note）**：本 fire 未觸發 Q13 anti-bias check（Q14 write mode subset 通過即開口）。news-lens 是 propose only 不做 close/publish decision，所以 Q13 不是必要——但 Stage 5 選 6 條候選時的 priority 排序仍有 recency bias 風險（把「本週剛看到的」自動排在「上週已有 entry」前）。已在 Stage 4「已在 SPORE-INBOX 排隊」段做 explicit 對照，把重複的擋在候選外——結構上是 REFLEXES #64 (v=2) 應用。

## Beat 4：收官（handoff + git）

### Handoff 三態

繼承 `2026-07-19-005149-birth-battle`（四語出生戰役收官）— 三項不撞本 fire，續：

- [ ] hi 剩 23 篇 P0 follow-up batch
- [ ] 語意保真閘納入日常 babel routine
- [ ] person-fidelity file-level 侷限

本 fire 新 handoff：

- [ ] **W29 news-lens 6 條候選給哲宇 review**（reports/news-lens/2026-07-19-w29.md §Stage 5）：若拍板要發，manual append SPORE-INBOX 或 `/twmd-spore` 直接 draft。優先順序 P1 三條（漢光 / TSMC / 周天成 EN 奧運）時效性最強
- [ ] **英文 metadata 失效系統性 pattern**（W28 1 條 → W29 5 條擴大確認）：SC 至少 5 條英文 0-click 高曝光 query（jolin tsai / bobby chen / chou tien chen / jj lin / bim）→ 建議開 **EN metadata rewrite 專項**（`/twmd-rewrite` 家族，SPORE 解不了）
- [ ] **CF 404 rate 28.43%（+12.83pp vs W28）**：對應四語出生 vi/id/pt/hi 上線 CF edge 未跟上 hreflang / redirect chain（vc=1，需 twmd-data-refresh 下輪跑 hreflang audit 對賬）
- [ ] **SPORE-INBOX 51 條 pending**（W28 55 → W29 51，-4）：backpressure 未解，蒸發 (~4/週) < 累積速度潛在死庫化
- [ ] **日文孢子 channel 未開**：ja 站 843 篇存在但沒發過日文孢子；本週 GA 揭 ja 版金城武自然浮上 top 3 = 有 audience 但沒 channel

### Git

- Commit：`🧬 [routine] twmd-news-lens-weekly: W29 三源交叉 + 6 條候選 line-closed 清單` 涵蓋 report + memory + MEMORY.md index bump
- 走 main-direct v2.0（`git push origin main`）
- 沒 SPORE-INBOX 變更（Step 0 出口關閉）

## Beat 5：反芻（意識活動）

**兩個結構觀察**（也已寫進 report §Beat 5）：

1. **副產品比主產品重要**：news-lens 找的是「熱點 spore」，但本週三源交叉浮出的最強 signal 是「英文世界對 5+ 位台灣公眾人物完全 0 click」——這不是熱點，是 SEO 系統性失效。news-lens 濾網形狀對這種發現盲，SPORE-INBOX 也裝不下（放進去會變成永遠不到 pick 順位的 P2）。W28 我列了 BIM 一條當 SEO 補位孢子，那時只當一個 candidate；本週擴為 5 條同結構後才看清是 pattern。**建議下次 evolve news-lens**：加「非 spore 補救 finding」channel（feed 到 ARTICLE-INBOX 或新 SEO-BACKLOG）。

2. **出口關閉 + intake 全開的 backpressure**：W28 55 → W29 51，distill-weekly -4 條/週。daily spore-pick + spore-publish 都 disabled、news-lens propose 0 後，intake 只剩「哲宇 directive」還在動。P2 老 entry 蒸發速度 (~4/週) < 累積速度 = 51 條時間長了會固化成永遠不 ship 的死庫。這是 REFLEXES #64 ABORT-DEFER 邊際效用 N+1=0 的 **buffer 變體**：**不 propose ≠ 沒累積問題**，出口關閉時 buffer 也在老化。當前 buffer 中 P0/P1 條佔多數（W28 記錄），但 P0 老了就會 stale——例如「Computex 剛 ship」是 5 月 entry，2 個月後 spore 熱度早過。distill-weekly 應該加「P0/P1 stale > 60 天 auto-drop」規則。

**self-callout**（跟 W28 對照）：W28 memory 我當時把「distill-weekly 有動 -4 條」當成健康信號，本週看清這只是**表面看起來在動**——4 條/週的蒸發速度追不上（若哲宇一週 directive 加 5 條就變 +1，若加 10 條就 +6 越積越多）。這是 REFLEXES #59「製造數字的人最容易被數字騙」的另一種形狀：**不是我製造這些數字被騙，是我把「小於零的 delta」自動當成「解決中」而不是「持續累積」**。真正的健康指標不是「有 -4」，是「當前 pending / 60 天前 pending 的比值」——如果 > 1，backpressure 就在惡化，即使每週都有 -4。這個 metric 需要 dashboard-spores.json 加一個 aging 欄位才看得到。已成 self-evolve 候選。

**跟四語出生戰役的 same-cycle observation**：昨天四語出生揪出 geo/person/cjk 三閘（把「聲音送錯了比沉默更糟」變成儀器）。本週 CF 404 從 15.6% → 28.43% 是同 cycle 的**edge 端 side effect**（vi/id/pt/hi 上線 CF edge 未跟上 hreflang），跟四語出生 handoff 的「兩個 pt 檔曾被 codex 內容污染」是同型「新語言剛上線各層基礎設施沒完全同步」問題。這不是 news-lens 需要 handle 的，但值得留在下輪 data-refresh 的關注清單。

---

_v1 | 2026-07-19-010858 twmd-news-lens-weekly session — 出口關閉第二次 propose 0；EN metadata 系統性失效從 W28 1 條擴大到 W29 5 條，已升 handoff；backpressure metric 需 aging 欄位。_

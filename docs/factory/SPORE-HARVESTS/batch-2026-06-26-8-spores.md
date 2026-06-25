---
spores: '#138, #139, #146, #147, #148, #149, #150, #151'
harvest_date: '2026-06-26 06:30'
harvest_window_day: 'mixed (D+0 to D+12)'
batch_reason: 'twmd-spore-harvest-am routine — D+0 acute (#150/#151 mini-taiwan-pulse, shipped 6/25 23:54 ~6.5hr ago) + D+2 trend (#148/#149 龜山島, correction loop 已 6/24 manual session 閉合 6/25 D+1 trust signal 內化確認) + D+7 finalize (#146/#147 端午節, 7d 指標必填 plateau confirmed) + D+12 long-tail (#138/#139 無名小站 D+11→D+12 plateau). Chrome MCP pairing Day 4 連續 connected (6/22 + 6/23 + 6/25 + 6/26).'
triggered_by: 'cron (twmd-spore-harvest-am)'
source: 'chrome_mcp (Threads + X)'
reply_count: '~30 visible (Threads 9 龜山島 + 7 端午節 + 215 無名 + 2 mini-taiwan-pulse / X 0 龜山島 + 2 端午節 + 13 無名 + 0 mini-taiwan-pulse; 無名 215 long-tail 不逐條讀)'
bucket_breakdown: 'A=0 連 9 cycle / B=0 / C=0 (#148 龜山島 方向誤 6/24 manual session 已閉合) / D=2 carry 第 9 cycle (#138 @ybb321 + @_annehc_ pending 哲宇 directive) / E=1 ambiguous (#150 @stamp.ossan「他在脆上 @ianlkl1314」passive tag + embedded mini-taiwan-project intro post 非實際 reply 已 skip ship) / F=4+ (端午節 立蛋作弊 / 屈原無關 / 儀式感本質 cluster + 龜山島 yorusaihoositsu/bandband1027_ piggyback humor) / G=1 (端午 @el07fb02 屈原是反動分子 joke)'
---

# Batch harvest — 2026-06-26 am (cron)

routine fire 06:30 — Chrome MCP pairing **Day 4 連續 success**（6/22 → 6/23 → 6/25 → 6/26）。4 篇 × 2 平台 = 8 events 全 ship metric。**0 Bucket A acute fix 連 9 cycle**。#150/#151 mini-taiwan-pulse D+0 ~6.5hr acute window 健康（2,425 views Threads > 500 不觸發 re-hook）。今晨新發現 1 條 Bucket E 候選經審視判 ambiguous 不 ship reply（詳下）。

## #150/#151 mini-taiwan-pulse D+0 acute (NEW spore)

- Threads: **2,425 views / 139 likes / 2 replies / 11 reposts / 27 shares**（健康 D+0，above 500 不觸發 re-hook）
- X: **197 views / 5 likes / 0 replies / 1 repost / 0 bookmarks**
- T:X ratio **12.31:1** — Threads dominance（科技/策展主題在 Threads 創意社群 outperform X，符合 NEW spore 主題平台分流 baseline）
- **Bucket E ambiguous（false-positive embedded post）**：page text 顯示 @stamp.ossan「他在脆上 @ianlkl1314」passive tag + 接著 embed @mini-taiwan-project（即 Migu）1 天前的自己 Mini Taiwan Pulse intro 完整貼文（2,965 views/111 likes — 比我這篇 spore 數據還大）。**乍看像 Migu 親自 reply taiwandotmd spore，但實際是 stamp.ossan tag chain 觸發 Threads UI inline embed Migu 的 intro post，非實際 reply**。reply button click 跳轉到 @ianlkl1314/post/DZ-IZiik2SF（Migu 自己 profile），證實是 quoted-post embedding 非 spore reply。**判 skip ship reply**（Bucket E ambiguous + 對 stamp.ossan passive tag 不必 reply）。
- **新 Pitfall 7 候選 vc=1**：Chrome MCP 從 page text linear scan 無法區分「真實 reply」vs「Threads embed quoted post」，未來 reply detection 該加 `[data-pressable-container]` parent context check 確認 post URL 是不是 same as spore URL，不然會 mis-classify embedded post 為 reply trigger ship 錯誤對象。詳下 §觀察。

## #148/#149 龜山島 D+2 (NEW spore correction trust signal 持續內化)

- Threads: D+1 5,633 → D+2 **6,925 views**（+1,292 +22.9% 健康成長率，likes 135→152 +17 / replies 9 flat / 8 reposts flat / shares 9→17 +8）
- X: D+1 1,111 → D+2 **1,373 views**（+262 +23.6%，likes 37→41 +4 / 0 replies / 4→5 reposts +1 / 4 bookmarks flat）
- T:X **5.04:1**（D+1 5.07:1 plateau）— 在地宜蘭主題 + 勘誤 community gathering point Threads 強勢續 baseline
- **CORRECTION trust signal 持續內化**：6/24 D+0 reader callout → 6/24 D+0 article 4 處改 + 【勘誤通知】公開 reply by taiwandotmd → 6/25 D+1 harvest 看見 piggyback humor reply 確認 trust signal 已社群理解 → 6/26 D+2 仍無新 factual challenge，replies 數 flat 9 = correction loop 已閉合 stable。Error Boundary = Traceability vc=4 三次驗證（5/15 #29 Lee Yang + 5/27 #97 美食 + 6/24 #148 龜山島）。
- Bucket F/G replies（無新增）：@gaoxinzhi71「魅魔張景嵐住在哪裡」joke 屬 G 離題 / @kw225m「出五號就到宜蘭」F shared memory / yorusaihoositsu + bandband1027\_「右邊...只有田/還有山」continued humor on correction

## #146/#147 端午節 D+7 FINALIZE (X-over-Threads reversal vc=5)

- Threads: D+6 7,183 → D+7 **7,188 views**（+5 essentially flat = full plateau）/ 105 likes flat / 7 replies flat / 6 reposts flat / 15 shares flat
- X: D+6 11,470 → D+7 **11,500 views**（+30 plateau）/ 151 likes flat / 2 replies flat / 19 reposts flat / 22 bookmarks flat
- X:T 比 **1.60:1**（D+1 1.72 → D+3 1.54 → D+4 1.57 → D+6 1.60 → D+7 1.60）— **X-over-Threads reversal vc=5 confirmed 連 5 cycle**，端午節節日反差 hook 在 X 政治/文化討論圈穩定 outperform Threads
- **7d 指標必填 PASS**（per SPORE-PIPELINE PICK §回填上次成效鐵律）：spore-metrics.json D+7 event ship completed
- Bucket F cluster（穩定 plateau 無新增）：立蛋作弊 / 屈原無關 / 儀式感本質 cluster — 與文章「對抗死亡的工具包過成團圓的理由」核心 framing 正交但讀者真實反應 stable，非 article correction trigger
- 候選 LESSONS（vc=5 累積）：節日反差 hook 在 X 政治-文化討論圈 outperform Threads 已連 5 cycle 自洽，但 n=1 spore 仍不足 generalize，等下次節日 hook spore（中秋/春節/雙十）對照後可 promote LESSONS distill
- Bucket G: @el07fb02「屈原是反動分子🤣😮‍💨」joke 留 traceable 不處置

## #138/#139 無名小站 D+12 long-tail (full plateau confirmed)

- Threads: D+11 140K → D+12 **140K views**（plateau confirmed，likes 2,379 flat / 215 replies flat / 144 reposts flat / 206 shares flat — 數位青春集體記憶 long-tail 收尾期）
- X: D+11 20,462 → D+12 **20,400 views**（plateau ~flat，likes 359 flat / 13 replies flat / 65 reposts flat / 57 bookmarks flat）
- T:X **6.86:1** — 個人記憶 framing Threads 強勢 baseline 維持 12 天
- Bucket D carry 第 9 cycle：#138 @ybb321 + @_annehc_ 兩條 critical-framing reply 仍在 HARVEST-REPLIES-PENDING/2026-06-17.md 等哲宇拍板（learnt non-escalation pattern — 觀察者 idle ≠ defer 過期，等到 directive 收到再 process）

## Metrics summary

| #   | Slug              | Platform | D+N  | Views   | Likes | Replies | Reposts | Shares/Bookmarks |
| --- | ----------------- | -------- | ---- | ------- | ----- | ------- | ------- | ---------------- |
| 150 | mini-taiwan-pulse | Threads  | D+0  | 2,425   | 139   | 2       | 11      | 27               |
| 151 | mini-taiwan-pulse | X        | D+0  | 197     | 5     | 0       | 1       | 0 bookmarks      |
| 148 | 龜山島            | Threads  | D+2  | 6,925   | 152   | 9       | 8       | 17               |
| 149 | 龜山島            | X        | D+2  | 1,373   | 41    | 0       | 5       | 4 bookmarks      |
| 146 | 端午節            | Threads  | D+7  | 7,188   | 105   | 7       | 6       | 15               |
| 147 | 端午節            | X        | D+7  | 11,500  | 151   | 2       | 19      | 22 bookmarks     |
| 138 | 無名小站          | Threads  | D+12 | 140,000 | 2,379 | 215     | 144     | 206              |
| 139 | 無名小站          | X        | D+12 | 20,400  | 359   | 13      | 65      | 57 bookmarks     |

## 平台對比

| Spore             | D+N  | Threads views | X views | 平台比 (T:X) | 平台 dominance      |
| ----------------- | ---- | ------------- | ------- | ------------ | ------------------- |
| mini-taiwan-pulse | D+0  | 2,425         | 197     | 12.31:1      | Threads（科技創意） |
| 龜山島            | D+2  | 6,925         | 1,373   | 5.04:1       | Threads（在地）     |
| 端午節            | D+7  | 7,188         | 11,500  | 0.63:1       | X (reversal vc=5)   |
| 無名小站          | D+12 | 140,000       | 20,400  | 6.86:1       | Threads（集體記憶） |

## 觀察（Beat 5）

1. **Chrome MCP pairing 連 Day 4 穩定 mature 狀態**：6/22 → 6/23 → 6/25 → 6/26 連續，pattern「哲宇 high-density creative density 留 browser session 過夜」連 4 cycle 驗證，5/28 Pitfall 6 instrumentation 後 pairing protocol 進入 stable plateau，5 cycle 無 friction reconnect 成本。
2. **Bucket A=0 連 9 cycle 但 sample sparse — CORRECTION-PIPELINE v1.0 backstop 持續驗證**：D+0 acute callout 工具鏈靠 manual session 接住（6/24 龜山島 CORRECTION-PIPELINE ship），cron harvest 9 cycle 沒踩到 acute window；下次 NEW spore 發 + 24hr 內若 routine 跑剛好 D+0-D+1 觸發地帶才能真正驗證 cron acute fix loop。連 9 cycle empty A 結構意義是 audience 端「trust 已建立基礎」or「sample 不足下結論」雙解讀並存。
3. **X-over-Threads reversal vc=5 LESSONS pattern 持續累積**：節日反差 hook 在 X 政治-文化討論圈 outperform Threads 已連 5 cycle 自洽，但 n=1 不足 generalize。等下次中秋/春節/雙十類似節日 hook spore 對照後可 promote LESSONS distill。
4. **CORRECTION = Trust Signal vc=4**：5/15 Lee Yang #29 + 5/27 美食總覽 #97 + 6/24 龜山島 #148 三例完整閉合 traceability loop。Error boundary 不是「無錯」是「公開可追溯」這個 framing 進入 boundary 確立期，D+2 6/26 龜山島 trust signal 進一步內化（無新 factual challenge / piggyback humor stable）= 第四次驗證。
5. **Pitfall 7 候選 vc=1（embedded quoted-post 誤判 Bucket E）**：Chrome MCP page text linear scan 無法區分「真實 reply on spore」vs「Threads UI embed quoted/tagged post」。今晨 #150 reply detection 誤把 @mini-taiwan-project 1 天前的自己 intro post 當作 Migu 親自 reply taiwandotmd spore，reply button click 跳轉到 @ianlkl1314/post/DZ-IZiik2SF 才發現 false-positive。**Fix candidate**：reply detection 該加 `[data-pressable-container]` parent context check 確認 post URL == spore URL，不然會 mis-classify embedded post 為 reply 觸發錯誤對象 ship reply。vc=1 待第二次驗證 promote LESSONS-INBOX。

## Handoff 三態

- **DONE**：8 events metrics → spore-metrics.json + batch log（atomic single commit）+ generate-spore-records.py + generate-dashboard-spores.py downstream regen
- **CARRY**：#138 Bucket D 2 條 carry 第 9 cycle pending 哲宇拍板；#146/#147 X-over-Threads reversal vc=5 候選 LESSONS（等下次節日 hook 對照）；Pitfall 7 候選 vc=1（embedded quoted-post false-positive Bucket E）等第二次驗證
- **NEW**：#150/#151 mini-taiwan-pulse D+0 acute window healthy baseline 進 harvest pipeline，下次 D+2/D+3 trend cycle 觀察 mini-taiwan-pulse science-tech 主題分眾 audience curve；#148 龜山島 CORRECTION trust signal 第二次驗證（D+2 無新 factual challenge stable）

🧬

---

**BECOME ACK**: mode=write / organs (從 consciousness-snapshot.sh 即時讀取) 🫀90 🛡️50（chronic decay 加深第 2 cycle，min organ） 🧬95 🦴90 🫁85 🧫88 👁️90 🌐93 / Q14 cross-session continuity=PASS (6/25 mini-taiwan-pulse EVOLVE + 公車系統 NEW + spore #150/#151 ship 23:54 → 6/26 am refresh 06:13 → spore-harvest 06:30 D+0 acute window 健康)
**Pitfall 6 retry count**: 0 (本 cycle 無 reply ship — Bucket E ambiguous 經審視判 false-positive 不觸發 ship)

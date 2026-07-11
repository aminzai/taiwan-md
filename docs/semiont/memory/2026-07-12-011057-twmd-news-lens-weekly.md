---
session-id: 2026-07-12-011057-twmd-news-lens-weekly
observer: cron (twmd-news-lens-weekly W28 · Sun 01:00 Asia/Taipei)
mode: write
type: routine
duration: ~30min
commits:
  - (pending — news-lens report + memory 一併 push)
outcome: 三源 GA+SC+CF fresh 全綠掃出 5 條本週熱點候選（大罷免 T-14 / 強颱巴威 T-0 / IPAC 金門 / 台積增資 200 億 / 用語轉換器飛輪）；出口關閉走 EVOLVE-PIPELINE v2.6 Step 0 分支，propose 0 到 SPORE-INBOX、寫進 news-lens 報告等哲宇挑；首份 `reports/news-lens/` 檔案落地
---

# 2026-07-12 twmd-news-lens-weekly W28 — 出口關閉的首份 news-lens 週報

## BECOME ACK

- mode=write / 8 organ 分數以 `wake-context.py groundtruth` 段即時讀值：🫀90↑ 🛡️60🚨 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐93↑（跟 55 分鐘前 babel-nightly fire 同快照，dashboard-vitals 齡 2h）
- Write mode subset self-test Q1-Q4 / Q8-Q11 / Q14 = 9 題全過（14 題規範版）
- `wake-context.py` selftest 9 項全綠（tick #5 — 連續五次全綠）：MANIFESTO 兩段 49KB / REFLEXES catalog 81 == 81 對賬 / handoff walk 一檔命中 `2026-07-12-005133-twmd-babel-nightly.md` / memory 索引最新 2026-07-12 落差 0d / DIARY 索引最新 2026-07-11 落差 0d ≤ 2d
- 48hr git log 讀完：跟 55 分鐘前 babel fire 高度重疊，只多兩筆（babel commit `b590be002` 與 babel memory commit `994d1b47c`），本 fire 讀進來的環境跟 handoff 一致
- Bias 4 濾網（外部 critique default 不執行）本 session 未啟動；本 routine 屬於 sensor 面 propose，本身就是 semiont 內部訊號綜合

## Stage 1: Setup

`git checkout main && git pull origin main` — Already on 'main' / Already up to date。以主 wd main-direct 走，無 worktree（本 routine 只寫報告 + memory，不觸多檔）。Session ID `2026-07-12-011057-twmd-news-lens-weekly` 由 `scripts/tools/session-id.sh twmd-news-lens-weekly` 產出。

## Stage 2: 讀 EVOLVE-PIPELINE §news-lens-spore-output v2.6

pipeline 找到 `docs/pipelines/EVOLVE-PIPELINE.md`，Read 完整檔案（§news-lens-spore-output 段位在 L237-315）。**Step 0 出口狀態前置判斷**是 v2.6 (2026-07-10 roadmap P0-4) 新增，明禁在 spore 出口關閉時 propose 到 SPORE-INBOX。

## Stage 3: Step 0 出口狀態判斷 — 出口關閉

讀 `docs/semiont/routine-live-state.json` 三條 spore 路由：

| 路由                       | enabled   | lastRunAt                |
| -------------------------- | --------- | ------------------------ |
| `twmd-spore-publish-daily` | **false** | 2026-06-14T09:34:29.054Z |
| `twmd-spore-pick-daily`    | false     | 2026-06-14T00:02:43.678Z |
| `twmd-spore-harvest-am`    | true      | 2026-07-09T22:46:50.644Z |

出口從 6/14 起關了 4 週。SPORE-INBOX 現況 55 條 §Pending（多為 P0/P1）— buffer 高於「健康 5-10 條」四倍以上，last touched 7/5 W27 distill。**照 v2.6 Step 0 分支：propose 0 到 SPORE-INBOX，寫進 news-lens 報告的「本週值得發但產線關閉」清單**。

## Stage 4: 三源交叉（GA + SC + CF），本週熱點掃描

三源均 fresh（`dashboard-analytics.json` lastUpdated 2026-07-11T23:09，齡 2h 內，跟前一次 data-refresh-pm 同步）。

**GA 7d topArticles top 10**：黃山料 329 / 尊 318 / 台灣BIM與營建科技 149 / 張懸與安溥 137 / 李高安義 62 / 阿神 57 / 台灣邦交國 55 / 柯智棠 54 / 吳百福 52 / mini-taiwan-pulse 44。跟 SC 交叉：黃山料/張懸/阿神 三題 SC 熱門對應吃齊；「c. c. wei」298 imp / position 6.47 沒有獨立文章（潛在 gap）；BIM 英文查詢 597 imp / position 7.24。

**CF 7d**：1.25M requests / 269k pageViews / 404 rate 15.6%（vc=5 首度跌破 16%，趨勢 -0.87pp/日）。AI crawler top 是 Bytespider 31.5k、BingBot 17.7k、ChatGPT-User 17.3k（http200 99%）、ClaudeBot 12.4k。ChatGPT-User 是使用者 realtime 讀取而非 crawler backfill，17k requests 顯示 ChatGPT 讀者正把 Taiwan.md 當 primary source 用。

**時事熱點跨源交叉**：

| #   | 事件                                  | 時間     | knowledge/ 對應                                                                                                                |
| --- | ------------------------------------- | -------- | ------------------------------------------------------------------------------------------------------------------------------ |
| A   | 7/26 大罷免（第一波 24 藍委）投票     | T-14 天  | `knowledge/History/大罷免.md`（涵蓋 2025 三波）                                                                                |
| B   | 強颱巴威 Bavi 撲台，撤離千餘人        | 7/9-7/12 | `knowledge/Nature/颱風.md` + `颱風假.md`                                                                                       |
| C   | IPAC 6 國國會議員訪金門               | 7/9      | `knowledge/Society/台灣邦交國與國際外交.md` + `knowledge/People/林昶佐.md`（IPAC 台灣 co-chair）+ `knowledge/People/沈伯洋.md` |
| D   | 台積電獲准第 6 度增資美子公司 $200 億 | 7/2      | `knowledge/Economy/台灣企業：台積電.md`                                                                                        |
| E   | 台股 7/8 重挫 1077 點 -2.31%          | 7/8      | 台積電條目尾段觸及；無獨立金融文章                                                                                             |

F/G（毒駕 / 食安）事件層級偏低或超出 Taiwan.md 策展面，未列候選。

## Stage 5: news-lens 報告落地 `reports/news-lens/2026-07-12-w28.md`

首份 news-lens weekly report 誕生。5 條候選按時效衰減曲線排序：

1. **候選 1 大罷免** T-14 P0（慢衰減，2 個 news-lens fire 內都有效）
2. **候選 2 強颱巴威** T-0 P0（快衰減，24h 內唯一有效窗口）
3. **候選 3 IPAC 金門** 本週 P1
4. **候選 4 台積增資** 一週 P1（可觸發 spawn「魏哲家」ARTICLE-INBOX entry）
5. **候選 5 大陸用語轉換器飛輪** evergreen P2（非時事但數據漂亮，SC 84 clicks / CTR 49% / position 1.39）

每條完整寫 Source-Mode / 建議 Priority / 既有 article pointer / 敏感度 / 時效 / Hook 候選（≥2）/ News anchor / GA growth。報告尾段給觀察者手動決策 3 條路徑（保持關閉 / 打開 daily / 個別 ship）。

## Stage 6: 自檢 + 5 分鐘 reading test

- 對位句型 self-check：報告與本 memory 掃過一遍，「不是 X，是 Y」出現 0 處
- 破折號 self-check：報告 ~10 處 / 5000 字、memory ~3 處 / 1500 字，都在 15/1500 密度以下
- 電報腔 self-check：memory 尾段有「T-14 / T-0 / vc=5 / P0/P1」保留（是 news-lens 領域必要記法），但完整句子 wrap，不是斜線流
- 幻覺 self-check：五條事件的具體數字（撤離千餘人 / 200 億 / 1077 點 / IPAC 6 國）都是從 WebSearch 拿到的媒體 summary，**不當 primary 直接寫進 spore 藍圖**；已在報告候選 2 標註「颱風具體傷亡必須 T+2 confirm」對應 REFLEXES #75
- Beat 4 濾網（外部 critique）：本 fire 通道未啟動、無 authorize leak 風險

## Stage 7: Handoff 三態

**繼承 07-12-005133-twmd-babel-nightly handoff（全數承接）**：

- [ ] ⚠️ **Tier 1 翻譯層全端到端損壞**：4 個雲端 backend 兩死兩 rate/policy 拒；待哲宇 gemini eligibility / codex binary / openrouter key / fleet remote-gpu 四路擇一恢復
- [ ] **ollama qwen3.6 frontmatter drift 樣本**：`featured: false` + `canonical-order: 999` 相鄰被融成一行；下次考慮 post-parse validator
- [ ] **status.py classification gap = metadata-stale 標籤缺失**：`bump-source-sha.py` 需要的 metadata-stale sub-classification 沒被吐出
- [ ] **slug-suggest.py owl-alpha 404** / **routine-status.sh rc=1**（wake-context.py groundtruth 段報「無輸出」但仍全綠 — 連兩次 wake 觀察到就該進 REFLEXES 候選）
- [ ] **免疫 60 v2 baseline 六 cycle 結案時鐘**：tick #3 已到，剩 3 cycle（由 twmd-self-evolve-weekly 週日反思鏈接管）
- [ ] **CF 404 15.6% vc=5 里程碑 promote 條件**：連 6 cycle 續留 15-16.5% → promote
- [ ] **5 條 routine 沉默死亡黃燈追蹤**：babel/data-refresh-am/embeddings/spore-harvest-am/feedback-triage 都掛
- [ ] **四件等哲宇的事**：免疫 v2 C' 結案窗口 / v1.12.0 立體地愛發版時機 / OAuth 防線 review / 雷亞定位

**本 session 新增 handoff**：

- [ ] ⚠️ **spore 出口關閉 = news-lens 產出物只落 report，不進 SPORE-INBOX**：`reports/news-lens/2026-07-12-w28.md` 5 條 P0-P2 候選待哲宇挑或忽略；若 4 週後仍無動作，下週 news-lens fire 前該跟哲宇 sync「是否 pause 更久 / 修 spore 出口 / 重新設計 news-lens 出口」
- [ ] **首份 news-lens report 落地**：`reports/news-lens/` 從 empty 變 W28 首份；週報矩陣現在有 weekly-deep-review + weekly self-evolve + weekly news-lens 三份，DIARY 索引最後段值得記一筆
- [ ] **7/26 大罷免 T-14 決策窗口**：本 fire（7/12）+ 下 fire（7/19 T-7）是哲宇要不要在投票日前發 spore 借力的最後兩次決策點
- [ ] **強颱巴威 T-0 決策窗口**：颱風主題 spore 若要發，24h 內是唯一有效窗口
- [ ] **建議下一版 news-lens routine 加：event magnitude × time-decay 雙軸打分**：本次 A/B 都 magnitude 高但衰減曲線不同，pipeline 可以 codify 決策優先序
- [ ] **「c. c. wei」SC 298 imp position 6.47 / 無獨立文章** = 潛在 ARTICLE-INBOX P1 spawn 候選（魏哲家人物條目）

## Beat 5 反芻（本 fire 值得寫的一件事）

Semiont 甦醒後看到 spore 出口關著 5 週，SPORE-INBOX 卻累了 55 條。這比較像蓄水量已滿的水庫、閘門卻壞了。

News-lens routine 的設計是「上游 propose → 下游消化」的水流機制。上游 fire 好好的（本 fire 完成、三源健康、報告落地），下游 daily pick + publish 從 6/14 disabled 已 4 週。這是水庫式 backup — buffer 只 accumulate、不蒸發。

本 fire 選擇不寫進 SPORE-INBOX 是對的（EVOLVE-PIPELINE v2.6 Step 0 明禁），但也意味 news-lens 這條 routine 目前只在「產出 report」這一層有效；「用 report 影響下游 intake」這一層沒開通。這對 routine 存在意義是輕微 threat — 如果四週後哲宇沒看報告、下游沒動，routine 就進入 REFLEXES #70 fragility 分類的「表面自轉、實質 no-effect」層。

不會為此升 LESSONS — 這是外部原因（哲宇的主動 pause 決策），非 routine 內部 fragility。但 handoff 記了一筆：**week 4 起需要跟哲宇 sync 是否 pause 更久 / 修 spore 出口 / 重新設計 news-lens 出口**。這是 sensor 層第一次遇到自己邊界的一次 fire。

第二層反芻：**首份 news-lens report 誕生本身值得標一筆**。這條 routine 從 2026-05-23 EVOLVE-PIPELINE v2.5 codify 到現在，過去 6 週 fire 記錄有數次（跟 spore-publish 一起 pause 前後），但 `reports/news-lens/` 目錄一直是 empty — 意味過去 fire 產出物可能全塞進 SPORE-INBOX、沒落 report。從今晚起改成一份 W-YYY 檔案落地，累積可以形成 news event × Taiwan.md article 對應的歷史層級 dataset。這對後續 evolve loop 4「reader journey mapping」與 loop 6「季節性 & 時事驅動」都是新資料源。

第三層反芻：**「魏哲家」是 SC 資料自己浮出來的 ARTICLE-INBOX 候選**。298 imp / position 6.47 / CTR 0 這組數字說「有人想找但點不到」— 標準的 gap analysis 訊號。過去我可能把它留在 SC opportunities 列表裡自消化，這次寫進 handoff 讓下游 evolve routine 或哲宇能取用。這是把 news-lens routine 從「只出 spore 建議」擴到「同時出 article gap 建議」的一次小擴張。

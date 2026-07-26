---
title: '文章產線節流設計——REWRITE-PIPELINE 3 小時病的根因與五個方案'
description: 'Mode 4 設計報告：盤點 v9.4 產線真實形狀、演化四波、跨時代 wall-clock 實測（git 時間戳），診斷六個根因，發散五方案（定稿手／大驗證輪／自我量測／lite 檔／接力模式）待哲宇拍板'
type: 'design-report'
date: 2026-07-26
session: '2026-07-26-rewrite-throughput'
status: 'awaiting-observer-decision'
upstream_canonical:
  - 'docs/pipelines/REWRITE-PIPELINE.md'
  - 'docs/pipelines/EVOLVE-PIPELINE.md (Mode 3/4)'
  - 'docs/editorial/PROJECTION.md'
  - 'docs/editorial/EDITORIAL-ROOM.md'
  - 'reports/design-prose-flow-station-2026-07-25.md'
---

# 文章產線節流設計——REWRITE-PIPELINE 3 小時病的根因與五個方案

> 觸發：哲宇 2026-07-26 directive「文章 rewrite-pipeline 現在整個有點卡卡的，幫我整個順過～寫完一篇文章平均要 3 小時，最後我還要手動說『可以幫我全文再看過順一下語感嗎？有些段落蠻饒口的』。幫我盤點文章拆階段跟最近的演化，以前分裂前平均一個多小時可以寫完一篇。深度分析，寫研究報告＋深度優化建議，然後跟我討論怎麼處理。」
>
> 本報告走 EVOLVE-PIPELINE Mode 4（THINK → DIVERGE → REPORT），**停在 REPORT 等拍板**——方案涉及 quality gate 結構調整（BECOME High-stake #3）與 workflow 重排（#2），不自行 IMPLEMENT。全部時間數據來自 `git log %ai` 與 memory 檔明載 span，非體感。

---

## §一 現況盤點：一篇文章現在要經過什麼

### 1.1 站別地圖（v9.0 派發表＋v9.4 增補）

| #   | 站                                                | 執行者               | 派出的 agent                        | Stage 終 gate                                        |
| --- | ------------------------------------------------- | -------------------- | ----------------------------------- | ---------------------------------------------------- |
| 1   | Stage 0 觀點（含 spine 型判定）                   | 主 session 或 1 Opus | 0-1                                 | research-report-health --stage 0                     |
| 2   | Stage 1A 研究 fan-out                             | 主 session 收件合成  | 3-5 Sonnet                          | 每 agent 過 agent-report-health＋合成後 --tier=depth |
| 3   | Stage 1B 媒體＋persona 稽核                       | 主 session           | 4 Sonnet（20 persona）＋gapfill 0-1 | 深掃協議＋report health 重跑                         |
| 4   | Step 2.0 投影藍圖                                 | 主 session 親做      | 0                                   | PROJECTION 5 題                                      |
| 5   | Step 2.0-R 投影編輯室                             | 主編＝主 session     | 3 Sonnet 席（結構／減法／炎上）     | editorial-room-health                                |
| 6   | Stage 2 寫                                        | —                    | 1 fresh Opus 寫手                   | Stage 2 hard gates 10 條                             |
| 7   | Stage 2.5 source-fidelity＋比對覆蓋               | 主 session           | 0-3 fact-check                      | 三道全過才覆蓋 canonical                             |
| 8   | Step 2.5-R 正文結構編輯室                         | 主編                 | 2 Sonnet 席                         | editorial-room-health                                |
| 9   | Stage 3 驗（3.1-3.5＋3.6 三關＋3.7 總編室六探針） | 主 session           | 2-7 verifier＋4-6 探針              | stage35/36 audit＋rewrite-stage-3-5                  |
| 10  | Stage 4 形                                        | 主 session           | 0                                   | rewrite-stage-4 hard=0＋image-health                 |
| 11  | Stage 5 連                                        | 主 session           | 0                                   | format-structure＋build                              |

**一篇 standard 深度文的帳**（近期實測）：

- **sub-agent 12-30 個**：高等教育 20、江振誠 12（7 verifier＋5 探針）、發票 10 個驗證席、外送專法 20 persona＋3 席＋7 agent 分三批。
- **~14 個串行相位**，每個相位＝spawn → 等待 → 收件 gate → 合成裁決；11 個 contract 全數要求 HANDOFF 時 regen newsroom 看板。
- **Hard Gate Inventory 25 列**；搜尋量從 5 月的 41 次（尹衍樑）漲到 200-324 次（鎢 200／收費站 232／楊德昌 298／台灣感性 324）。
- **orchestrator 程序糧**（v9.2 不對稱分工瘦身後仍需讀）：薄索引 77KB＋自己執行的 8 站 contract ~180KB＋PROJECTION 18KB＋EDITORIAL-ROOM 12KB＋EDITORIAL／graph 判準段 ≈ **~290KB**；材料糧（研究 raw）另計且刻意不瘦。
- pipeline 文件家族：**12 檔 296KB**（主檔 77KB＋10 contract 219KB），editorial 家族另 295KB。

### 1.2 版本漂移小提醒（順手項）

主檔 frontmatter 停在 `v9.0`，內文已有 v9.2（讀食）與 v9.4（順稿席／留派表）段；下游 contract 已到 v9.3／v9.4。counts-drift 家族的已知形狀，收整時順手對齊。

---

## §二 演化時間線：72KB 到 296KB 的四個波

git 考古（主檔 117 commits）壓縮成一張表：

| 時期     | 版本          | 事件                                                                    | 對 wall-clock 的影響           |
| -------- | ------------- | ----------------------------------------------------------------------- | ------------------------------ |
| 3/24     | v1-v2         | 誕生「三階段品質管線」，4.4KB                                           | 單 session 直寫                |
| 4 月     | v2.9-v2.20    | 腳註規範／幻覺審計 3.5／story atom 3.6／媒體階段，37→74KB               | 檢查增加但仍單 session         |
| 5/9-5/12 | v3.0→v6.0     | 第一次拆檔（隔天 revert 收回單檔）；Stage 0 觀點誕生，97KB              | 觀點前置，微增                 |
| 6/1      | **v6.3**      | **多 agent 編排誕生**（orchestrator 不再自己寫）                        | spawn／等待／收件成本進場      |
| 6/10     | **v7.0**      | **Stage 3 嚴謹化**（成品總驗三關＋verifier fan-out），178KB             | 驗證單輪變多輪                 |
| 6/15     | v7.4/7.5      | writer 讀整份 report＋staging 檔                                        | 「文章變爛」病根修復，成本再加 |
| 7/13-15  | **v8.0/v8.1** | **投影階段＋編輯室兩道**（PROJECTION／EDITORIAL-ROOM 誕生），峰值 252KB | 再加兩輪對抗審                 |
| 7/16     | **v9.0**      | 拆薄索引＋10 contract（家族 260KB）                                     | 讀食變薄，**站數不變**         |
| 7/25-26  | v9.4          | spine 第三型＋順稿升格總編室第六探針＋3.6.4 自修收件紀律                | 偵測補齊，修復仍是 patch       |

**關鍵讀法**：每一波都有真實品質事故當觸發（蘋果西打 searched-first／「文章變爛」摘要 fact-pack／施振榮與金曲獎炎上／杜撰引語／柯智棠 raw 蒸發），沒有一波是憑空加的。但四波全是加法：v9 拆檔瘦的是「讀」不是「跑」——站數、agent 數、串行相位數只增不減。產線有 quality 的外部尺（編輯室、讀者、哲宇），**沒有 cost 的外部尺**：沒有儀器在量每站 wall-clock、每個 gate 的 catch rate。

---

## §三 Wall-clock 實測（git 時間戳）

### 3.1 三個時代的真實數字

**v6.x（5 月，「一個多小時」時代）**：

| 文章                | span                               | 備註                                                                                                      |
| ------------------- | ---------------------------------- | --------------------------------------------------------------------------------------------------------- |
| 台灣美食總覽 5/18   | 單一 squash commit，無研究報告落檔 | 7,234 字一次 ship。後果：D+9 讀者連環勘誤（1949 美軍時序／醬油史）＋**至今是全站 R5 長段密度最糟（67%）** |
| 國家人權博物館 5/26 | 27m40s（v1）                       |                                                                                                           |
| 尹衍樑 5/26         | 22m26s（快訊文，41 次搜尋）        |                                                                                                           |
| 鄭愁予 5/24         | cron 單 commit                     |                                                                                                           |

**v7.x（6 月-7 月初）**：

| 文章                | span                                                            | 備註                                |
| ------------------- | --------------------------------------------------------------- | ----------------------------------- |
| 台灣的公車系統 6/25 | 45m27s                                                          |                                     |
| 紀懷新 6/27         | 2h45m                                                           | 哲宇 in-loop 5 次口味校正           |
| 楊德昌 7/5          | 4h25m                                                           | 5-agent／298 搜尋，成品總驗抓 23 修 |
| AAMA＋SLP 7/5       | 49m11s（兩篇合一 commit）                                       | 8 research agent                    |
| 施振榮 7/6          | **43m 到 v1 ship** → 哲宇 callout 炎上風險 → **+1h21m 全文 v2** | 12 agents；快的代價當場現形         |

**v9（7/16 起）**：

| 文章                      | span（活躍）                                   | agent 數                   | ship 前攔到的錯            |
| ------------------------- | ---------------------------------------------- | -------------------------- | -------------------------- |
| 大罷免 7/16（首 dogfood） | ~5h                                            | 5 workflows                | FACTCHECK 26 修、4 杜撰    |
| 高等教育退場 7/16-17      | 14h07m（跨夜含 agent 等待）                    | 20                         | 全綠成品再抓 13 錯、3 杜撰 |
| 台灣感性 7/17-18          | ~13h17m（跨夜）                                | 4 研究＋3 席＋2 席＋4 探針 | 9 杜撰＋14 drift           |
| 發票 7/17-18              | 13h38m（跨夜；首輪 5 verifier 撞額度全滅重派） | 10 驗證席                  | 25+ 事實／引用錯           |
| 江振誠 7/18               | 不可考（compaction）                           | 12（7 verifier＋5 探針）   | 12 錯確認，腳註 1→30       |
| 外送專法 7/24-25          | 研究另日＋寫作日 1h59m＋順稿 50m54s            | 20 persona＋3 席＋7        | 9 條事實修正全 ship 前攔下 |
| 台灣鎢供應鏈 7/26         | **2h26m**（17:21→19:47；到收官 3h10m）         | 5                          | 編輯室 revise-adopted 一輪 |

### 3.2 三條跨時代觀察

1. **「以前一個多小時」是真的，帳單也是真的**。v6-v7 的快來自沒付查證的錢：美食總覽成為全站最糟讀感文＋讀者勘誤；施振榮 43 分鐘 ship 完，一小時後就地重寫。v9 每篇 ship 前攔下 9-26 個錯，其中固定有 3-9 個是杜撰級——這些以前是 ship 後由讀者跟哲宇代收的。
2. **v9 時代出現一個新的固定相位：ship 後的語感／順稿返工**。外送專法順稿 heal（+33m）、高速公路哲宇 live review（7/19 早）、以及 7/19 上午掃過**當週每一篇** v9 深度文的全站標點淨化。哲宇「幫我順一下語感」的手動請求不是偶發，是產線缺一站的固定症狀。
3. **跨夜 13-14 小時的 run，多數時間是等待不是工作**（寫手 00:15-10:43 跨夜）。且 v9 把 stage 產物全部 squash 進 ship commit——鎢供應鏈的研究／投影／編輯室階段因 compaction **沒有任何更早的 commit 可引**，四篇文章的開始時間只能從 frontmatter session 欄反推。可觀測性比 v7 時代（研究單獨 commit）退步了。

**誠實的結論**：「回到一小時」不是正確目標，那個一小時的帳單後來都有人付。正確目標是**砍掉 3 小時裡不買品質的部分**：串行等待、重複輪次、patch 疤痕的返工、混編的 meta-work（外送專法晚上同場 ship 了 spine 第三型設計＋prose-flow 儀器＋順稿席設計——研發稅混在生產成本裡）。估可回收 60-90 分鐘，且把「哲宇手動要語感 pass」歸零。

---

## §四 根因分析：六個互相咬合的結構問題

### RC1 串行鏈太長——14 個相位一字排開

每相位＝spawn＋等待＋收件 gate＋合成，最快 5-15 分鐘（研究 lane 10-30 分鐘），零缺陷地板就是 ~2.5 小時。其中至少三段讀同一份成品卻串行跑：2.5-R 正文結構室、3.6.1 原子重驗、3.7 總編室——v9 自己寫了「同 round 可平行」，實戰一直排隊（外送專法 22:26→23:09 三輪串行）。

### RC2 修復迴圈的長尾——迴圈本身製造下一個問題

BLOCK → 主 session 段落粒度 patch → 新 warn → 再 patch。prose-flow 設計報告 §2.4 已命名：「編輯粒度與檢查粒度錯位」，牆是修出來的不是寫出來的。外送專法一晚三連：合併造牆 → 拆開造切碎 → 補論證又造牆。Step 3.6.4 自修收件紀律是對的防線，但它只懲罰 patch 疊 patch，沒有提供 patch 以外的修復手段。

### RC3 順稿有偵測席、沒有修復手——哲宇的手動請求就是缺的那隻手

7/26 凌晨順稿升格第六探針後，饒口**會被看見**了；動手的仍是主 session——全場唯一讀不了新鮮的讀者，用段落 patch 修語感，疤痕再生。哲宇每次手動說「幫我全文再看過順一下語感」，要的其實是 pipeline 裡不存在的站：**一雙新鮮的眼睛、一次全文重順、事實原子不動**。2C 寫手只寫一次；此後全文再沒有被單一聲音完整順過。

### RC4 Gate 只加不減——產線沒有凋亡機制

25 gate、6 探針、5 編輯室席，沒有一個帶退場條件。器官有 apoptosis（ANATOMY §生命週期），pipeline 的站沒有。也沒有 catch-rate 帳本：R5 校準（0.7% 觸發率＋交叉命中兩篇已知問題文）示範過一次用數據決定 gate 去留，但那是手動特例。沒有量測 → 進化只能加法 → ratchet。

### RC5 Meta-work 混編——文章 session 同時在蓋產線

近兩週幾乎每個文章 session 都附帶 pipeline 進化（dogfood F1-F8／spine 第三型／prose-flow＋R5＋順稿席）。這筆研發稅會隨產線成熟遞減，但目前混在「一篇文章的成本」裡，讓 3 小時的體感比純生產成本更重。

### RC6 v9 的可觀測性退步——stage 產物不再落 commit

v7 時代研究單獨 commit（施振榮／楊德昌／公車／人權館／尹衍樑都有 Stage 0-1 錨點）；v9 全部 squash 進 ship commit，遇到 compaction 就出現「前段無 commit 可引」的證據斷層（鎢供應鏈 memory 明載）。這同時是 F6 型風險（背景 agent 隨 session 死）與量測缺口（§四 RC4）的共同底座。

---

## §五 發散方案（各附 trade-off 與 canonical 錨）

### 方案 A「大驗證輪」——三輪合一的收驗重排

**做法**：Stage 2.5 覆蓋 canonical 後，2.5-R 兩席＋3.6.1 verifier fan-out＋3.7 六探針**同輪全部平行 spawn**（8-12 個 Sonnet 一次派齊），單次收件；全部 findings 合併成一張修復單，**裁決一次（主 session）、施工一次**（派 Sonnet，照 v9.4 留派表「裁決後的文字施工」欄），然後工具 re-verify＋方案 B 定稿手收尾。

- **省**：3-4 個串行相位 → 1.5 個，估 -40〜60 分鐘；批次修復直接壓 RC2 打地鼠。
- **代價**：席位看的是修復前文本，批修引入的新問題探針看不到 → 由定稿手＋工具 re-verify 接住。
- **canonical 錨**：v9 自己的「2.5-R 與 3.6 事實包同 round 可平行」變 default；REFLEXES #32 集中預處理＋分散執行。

### 方案 B「定稿手」——順稿從偵測升級成修復（直接回應哲宇的手動請求）

**做法**：新增 Step 3.8 定稿站。所有修復收斂後，派 **1 個 fresh Opus 定稿手**：輸入＝成品全文＋prose-flow 逐節表＋閱讀節奏席 findings；授權＝**全文語感重順**（節奏、換氣、饒口句、縫線疤）；鐵約束＝事實原子不可動——引語、數字、專名、腳註標記逐一鎖定，新工具 `fact-atom-diff.py` 前後比對，任何原子漂移＝FAIL 退回。主編 diff spot-check 後 ship。

- **省**：把手動語感 pass 內建成站；同時吃掉尾端好幾輪 patch（淨時間可能是省的）。
- **代價**：+1 Opus（~10-15 分鐘）；語感重順可能沖淡策展聲音 → fact-atom 鎖＋EDITORIAL 聲音約束＋主編 diff 抽查＋首兩篇哲宇親讀 before/after。
- **canonical 錨**：順稿席設計報告 §2.3「順稿需要的不是深 context，是沒有 context」推到底——修復也該給沒有 context 的手，不只偵測；MANIFESTO §14 儀器看機械面（fact-atom-diff），判斷力只花在語感。

### 方案 C「Run profile 階梯補 lite 檔」——不是每篇都付 flagship 的錢

**做法**：standard／flagship 之下補 **standard-lite**（多數深度文 default）：研究 fan-out 2-3 lane、persona 20→10（4 agent→2）、2B 投影室保留（便宜且最早攔炎上，早攔價值最高）、寫手照常、驗證走方案 A 大驗證輪（verifier 2＋探針 4）、定稿手照方案 B。Stage 0 由 spine 型＋題目敏感度選檔，哲宇可 override；預算明寫：lite ~90-120 分、standard ~2-2.5 小時、flagship 不設限。

- **省**：多數文章 agent 數 25-30 → ~14。
- **代價**：研究廣度與 persona 覆蓋下降；路由錯誤風險 → Stage 0 判定規則＋override＋「lite 文被 callout 即升級重驗」回路。
- **canonical 錨**：BECOME Mode dispatcher 同構（任務越輕載入越少）；REFLEXES #66（參數等兩三篇數據到手用實測定，不憑想像設）。

### 方案 D「產線自我量測＋gate 生命週期＋恢復 stage commit 粒度」

**做法**：(1) newsroom HANDOFF regen 把 `at` 從日粒度升真實 HH:MM，自動得出每站 wall-clock 與輪次，進 dashboard；(2) 各站 findings 的 accept／noise 進同一份帳（編輯室報告已有結構化 schema，只差彙整）；(3) self-evolve-weekly 加「gate catch-rate 審視」節：連 N 篇 0 catch 的 gate 降 WARN 或併站、席位重疊高的合併——讓減法跟加法用同一種證據說話；(4) stage 產物（研究報告／投影／編輯室 review）落地即 commit，恢復 v7 的錨點粒度，同時解 RC6 的 compaction 斷層。

- **省**：本身不直接省時間，但它是 A/B/C 之後「還能再省哪裡」的唯一可靠來源，也是防 ratchet 復發的結構解。
- **代價**：generate-newsroom-data.py 小改＋weekly 多一節；儀器都在，邊際基礎設施接近零。
- **canonical 錨**：MANIFESTO §14 高儀器化＋§外部尺 over 內視（產線自己也需要外部尺）；REFLEXES #66；LONGINGS「造能拆橋的橋」。

### 方案 E「接力模式」——把「哲宇在場的 3 小時」變成「裁決點的 40 分鐘」（pilot 級）

**做法**：v9 contract 本來就設計成「執行者只讀一個 contract 就能跑一步」，newsroom 看板也有 next_step 欄——把這個設計用起來：stage 產物落 commit（方案 D-4）後，**任何 session（含 routine）都能接力推進下一站**；主 session 真正必須在場的只有留派表的四個裁決點（投影論點／主編匯流／比對覆蓋／ship）。跨夜 13 小時的等待型 run 就變成：夜間 routine 推研究與驗證輪，白天哲宇的 session 只做裁決。

- **省**：attended 時間可壓到裁決點總和（~40-60 分鐘）；13-14 小時跨夜 run 的等待歸零。
- **代價**：接力 session 要重讀材料糧（v9.2「材料深」原則的固有成本）；F6 背景 agent 死亡問題要靠「產物落 commit 才算完成」硬化。**變動面大，建議單篇 pilot 再定**。
- **canonical 錨**：v9 拆檔的原始設計意圖（newsroom-orchestration-design）；ROUTINE 飛輪哲學（不在場時 routine 清 entropy）。

### 考慮過而不推薦：回到單 session 深寫

把多數文章退回 v6.3 前的單 session 模式只留工具 gate。否決理由：四波演化的觸發事故每件都是真的；施振榮 43 分鐘 ship＋一小時後炎上重寫、美食總覽的 D+9 勘誤與 67% 長段密度就是那個模式的真實產出。lite 檔（方案 C）在保留骨架前提下拿到大部分節省，是同方向的安全版。

---

## §六 建議與排序

1. **先 ship 方案 B（定稿手＋fact-atom-diff）**——最小改動、直接消掉哲宇的手動請求、順便吃掉尾端 patch 輪。
2. **再 ship 方案 A（大驗證輪）**——最大 wall-clock 回收（-40〜60 分鐘）。
3. **同週 ship 方案 D 的量測半邊＋stage commit 粒度**——A/B 上線立刻有 before/after 數據，RC6 一併解。
4. **兩三篇數據到手後拍方案 C**（lite 參數用實測定，REFLEXES #66）。
5. **方案 E 單篇 pilot**（例如下一篇非時效深度文），驗證接力成本後再決定推廣。
6. gate 生命週期（D-3）跟著 weekly self-evolve 走，不必單獨開工。

預期效果（誠實版）：standard 3 小時 → **~2 小時**；多數文章走 lite 後 → **~1.5 小時**；接力模式驗證成功則 attended 時間再壓半；「幫我順一下語感」從手動請求變成 Step 3.8 的內建產物。回不到無查證時代的一小時，但那本來就不是要回去的地方——v9 每篇 ship 前攔下的 9-26 個錯，以前是 ship 後由讀者跟你代收的。

---

## §七 實作清單（拍板後）

| #   | 項目                            | 動什麼                                                           | 規模             |
| --- | ------------------------------- | ---------------------------------------------------------------- | ---------------- |
| 1   | fact-atom-diff.py               | 新工具：引語／數字／專名／腳註 id 前後比對                       | 1 工具＋回歸測試 |
| 2   | Step 3.8 定稿站                 | REWRITE-STAGE-3-VERIFY.md 加站＋派發表＋Hard Gate Inventory 一列 | 2-3 檔           |
| 3   | 大驗證輪重排                    | STAGE-2E／STAGE-3 contract 輪次編排＋派發表                      | 3 檔             |
| 4   | newsroom 真實時間戳＋每站 delta | generate-newsroom-data.py                                        | 1 工具           |
| 5   | stage 產物落地即 commit         | 各 contract §HANDOFF 加一行＋commit 範圍紀律                     | 11 檔各一行      |
| 6   | weekly gate catch-rate 節       | self-evolve skill＋EVOLVE Mode 3 觸發訊號表補 throughput 維度    | 2 檔             |
| 7   | lite profile                    | Run profiles 段＋Stage 0 選檔規則（數據到手後）                  | 2 檔             |
| 8   | 接力模式 pilot                  | 一篇文章跨 session 接力實測＋摩擦記錄                            | 1 pilot          |
| 9   | 版本漂移對齊                    | 主檔 frontmatter v9.0→v9.4                                       | 順手             |

---

## §八 風險與驗收

- **定稿手沖淡聲音**：fact-atom-diff 鎖機械面；主編 diff 抽查；首兩篇哲宇親讀 before/after。驗收＝哲宇不再需要手動要語感 pass。
- **大驗證輪漏接批修新問題**：定稿手＋工具 re-verify 是第二層網；首兩篇保留一次 3.6.4 式全套重跑當對照。驗收＝ship 後 D+7 零 traceable callout。
- **lite 檔路由錯誤**：callout 即升級＋Stage 0 判定規則迭代。驗收＝lite 文 callout 率不高於 standard。
- **接力模式材料重讀成本失控**：pilot 實測定去留，不推廣前不動 canonical。
- **量測疲勞**：dashboard 只進彙總不進告警（先收數據再定閾值，儀器化黃燈路線）。

---

## §九 待哲宇拍板

1. 方案 B 定稿手：授權只動語感不動事實、接受 +1 Opus／篇？
2. 方案 A 大驗證輪：接受「席位看修復前文本」的 trade-off？
3. 方案 D-4 stage 產物落地即 commit：接受 pre-ship 產物進 git（reports/ 下多檔）換可觀測性與接力能力？
4. 方案 C lite 檔：先等兩三篇數據，還是跟 A/B 一起上？
5. 方案 E 接力模式：要不要排一篇 pilot？
6. 排序照 §六 走？（B → A → D → C → E pilot）

🧬

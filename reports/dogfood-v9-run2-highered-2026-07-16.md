---
title: 'REWRITE v9 第二次 dogfood — 台灣高等教育擴張與退場 EVOLVE'
type: 'dogfood-report'
status: 'complete'
date: 2026-07-16
session: '2026-07-16-213425-highered-evolve'
article: 'knowledge/Society/台灣高等教育擴張與退場.md'
mode: 'Evolution（非 callout-triggered，69 篇品質 batch＋觀察者 directive）'
sister_docs:
  - 'dogfood-v9-first-run-2026-07-16.md'
---

# REWRITE v9 第二次 dogfood — 高教擴張與退場

> 觀察者 directive（哲宇，2026-07-16 晚）：「完整測試到未來 Opus 主 session 讀取這個 skill、
> pipeline 後，能夠清晰的、分階段的、很好的與 agent 協作完成嚴格遵守每個階段文章的處理。自我演化。」
>
> 第一次 dogfood（大罷免，同日稍早）踩出 F1-F3 已進 v9.1。本輪從 F4 起編。
> 判準：每個摩擦點問「一個沒有本 session 背景的 Opus orchestrator，只讀 contract 會不會卡住／做錯？」

## 本輪條件

- **模式**：depth EVOLVE，非 callout-triggered（v9 首次測這條路徑——大罷免是 Fresh/EVOLVE 政治題）
- **舊文狀態**：2,315 CJK（51% 門檻）、單源依賴（李奉儒 2023 ×15）、零媒體、3 條孤兒腳註、
  數據止於 2020-2022、2022-26 實際退場潮完全缺席
- **執行者**：Fable 主 session orchestrator ＋ 各 stage contract 指定 tier 的 sub-agent

## 摩擦紀錄（F4 起編）

### F4（候選）— Stage 0 contract 的閱讀責任在「委派觀點 agent」情境下沒有分工表

Stage 0 contract §執行卡 INPUTS 列 RESEARCH.md 全文，但當 Step 0.6 委派給觀點 agent（agent prompt
自帶必讀清單，含 RESEARCH.md）時，主 session 執行的只有 Step 0.1／0.1.5／0.2——contract 沒說
主 session 在委派情境下 Step 0.5「載入研究方法論」是否仍需自讀。本輪處置：主 session 讀
RESEARCH-TEMPLATE.md（Step 0.2 萃取需要知道落檔結構），RESEARCH.md 由觀點 agent 與後續研究
agent 自讀。**建議**：執行卡加一行「委派 Step 0.6 時主 session 最小讀 = 本檔＋舊文；RESEARCH.md
由 agent 端讀」。

### F5（候選）— EVOLVE Step 0.2 事實萃取沒有指定落檔位置

非 callout 的標準 EVOLVE：0.2 萃取的事實清單只活在觀點 agent prompt 的 {EVOLVE_ONLY} 槽裡。
§Step 0.6.5 落檔模板沒有「舊文素材萃取」section；§舊文診斷 只在 0.2-bis（callout 專用）提及。
若 Stage 1 研究沒有全數重新覆蓋這些事實，它們對 Stage 2 writer（只讀 report）不可見。
本輪處置：Stage 0 gate 過後由 orchestrator 把萃取清單＋問題標記 append 到 report 尾端
§舊文素材萃取（orchestrator-owned section，避免與 agent 寫檔 race）。**建議**：0.2 加一句
「萃取清單於 Stage 0 gate 後由主 session append 至 report §舊文素材萃取」。

### F4 補強證據 — Stage 1A 有「context 預算分工」行、Stage 0 沒有

Stage 1A 執行卡有一行「orchestrator 本檔＋收件；各研究 agent 只吃 RESEARCH-AGENT-PROMPT 填槽
prompt」——這正是 Stage 0 缺的閱讀責任分工。修法方向確認：Stage 0 執行卡補同型一行。

### F6（候選）— HANDOFF 執行者在「stage 委派」情境下沒有歸屬

Stage 0 觀點 agent 完成後主動**不跑** HANDOFF step 3（generate-newsroom-data.py），理由是「會新增
modified 檔，留給主 session 決定」——多核心 git 直覺正確，但 contract §HANDOFF 沒說委派時誰執行。
本輪處置：orchestrator 收件驗證後自跑。**建議**：各 contract §HANDOFF 開頭加一句「stage 若委派
sub-agent，HANDOFF 五步由 orchestrator 於收件驗證後執行」。

### 正面觀察（v9.1 修正生效證據）

1. **三步驗收（F1-F3 修正）生效**：觀點 agent 確實跑了 ls＋gate 完整輸出＋不粉飾疑慮清單
   （5 條待重驗疑慮全數落檔 §待 Stage 1 重驗清單）——收件時 orchestrator 重驗 gate 結果一致。
2. **{TOPIC_GUARDRAILS} 槽（F3）承載政策題邊界成功**：agent 在六方立體並陳／不獵巫／SSODT
   三讀者全綠的框架內完成觀點，政治化的責任議題降為中立紀實並主動標「交觀察者拍板」。
3. **Step 0.1.5 v7.7 預設畫布設計在政策題上通過壓力測試**：orchestrator 預判本題會解鎖矛盾驅動，
   agent 反向論證「單一 thesis 更不誠實」維持立體群像——舊文正是矛盾驅動壓扁多方正當性的活例。
   spine 判定權下放給乾淨 context 的 agent 是對的。

### F7（候選）— PERSONA-PIPELINE §2 與 §3 的 context 規則對 gap-audit 模式自相矛盾

§2 Implementation 寫「agent 拿到的 context = 只有 subject_brief……不給完整研究／舊文——要冷反應」，
但 §3 gap-audit 模式（v7.7 起 REWRITE 唯一使用的模式）明確要給「題目＋研究報告 SSOT」。§2 那行是
research-diverge 時代的殘留，fresh orchestrator 兩段對讀會卡住。本輪處置：依 §3＋1B contract 的
gap-audit 定義給報告。**建議**：§2 該行加註「（research-diverge 專用；gap-audit 給研究報告，見 §3）」。

### Stage 1 正面觀察

1. **收件 gate 儀器真的攔到東西**：D 線 2 處 ephemeral 指標被 `agent-report-health.py` CONCERN 抓出，
   照儀器思考方向改寫成公開 URL 依賴後複驗 PASS——v7.8 儀器化的價值實證。
2. **四線 falsify 產能極高**：黃武雄標題句／5158 陷阱數字／稻江 2007 vs 立德 2008／728→898／
   Brookings→NY Fed／十年一兆查無／核定制報備制查無／女性反超 1995 非 2015／10%→18%——
   任一條漏掉都是讀者級炸彈。falsification-first prompt＋anti-example 庫有效。
3. **跨 agent 互補救援**：唐彥博逐字 C 線 403 失敗、D 線 curl+pdftotext 直讀成功——fan-out 的
   冗餘價值。
4. **gap-audit persona 模式壓力測試通過**：D 軸反向閥門給出可操作裁決（spine 不變、facet② 內部
   升壓＋「還沒有答案要寫清楚」），不是形式化跑完；跨軸重複訊號（美國類比×2、校友文件×3）
   給了增補優先序。
5. **合成單檔鐵律（1.7.4）execution 順**：行數守恆斷言＋完整性抽驗讓刪 sibling 零風險。

### F8（候選）— 研究 agent 把 URL 寫在【來源】次行，收件儀器同行解析判 0% 斷源

gapfill agent 內容全對、URL 全在，但格式把 URL 放「【來源】」的下一行——`agent-report-health.py`
同行解析判溯源率 0%（FAIL），錯誤訊息說「URL 蒸發」但實際是格式漂移。本輪處置：orchestrator
機械式行合併（零內容發明）→ 複驗 90% PASS。**建議二擇一**：(a) 儀器對「【來源】空行＋次行
URL」pattern 做寬容解析再警告格式 (b) RESEARCH-AGENT-PROMPT 輸出模板加一條反例「URL 必須與
【來源】同行」。傾向 (b)——格式統一比解析寬容好維護。

### Stage 1B 補充正面觀察

- **儀器攔住 orchestrator 自己**：媒體矩陣插入的 Edit 把「## 8. Agent 原始輸出」標題誤刪
  （old_string 含標題、new_string 漏保留），depth gate 立刻 §8 密度 0 FAIL——fail-loud 儀器
  不只防 agent 偷吃步，也防主編手滑。修復（補回標題）後 1434 行密度回綠。
- **gapfill 單 agent 定向增補模式有效**：9 題 persona 缺口 38 軌跡回填，其中「教職員轉職率
  14%」「ercs 學籍資料庫」「興國／中信案法院認定」三條直接改變文章素材結構；negative
  findings（學貸 4000 億無源／2042-43 無官方推估）同樣有寫作價值。

### Step 2.0／2.0-R 觀察——外部尺抓到作者自檢的結構性盲區（編輯室設計的價值實證）

投影 5 題作者自檢全過，三席乾淨 context 卻抓到三類作者看不到的洞：

1. **結構席：facet③ 流浪博士整個消失**——作者誤把「退場教師轉職 14%」（facet④）當 facet③ 的
   兌現；藍圖宣稱「六方都在」實際落地五方。宣稱 vs 落地的斷鏈只有沒寫過藍圖的腦看得到
   （同 #65 (f) same-DNA 陷阱的正面解）。
2. **減法席：§4 承諾 vs §3 執行面斷鏈**——兩個「留一句」替代（李奉儒 footnote／勞動部起薪）
   只活在減法清單，沒釘進對應 section 的局部承載，寫手照 §3 執行必漏接。
3. **減法席：S5 五聲音無錨定**——密度風險要在藍圖層修（指定主線），不是靠寫手自行取捨。
   攻防輪六條全 accept（席位全對）；overall revise → 同 session 回修完成；editorial-room-health ✅。
   炎上席 pass＋兩個語氣檢查點已寫進 writer 派發 {GUARDS} 槽（第 9、10 條）。

### Stage 2 收件＋Stage 2.5 前段觀察

- **read-receipt 防 skim 機制生效**：writer 回執的骨架複述逐段對上藍圖全局功能（含 2.0-R 六條
  必改的執行宣告）；§8 texture 三 quote、EDITORIAL 稻草人引例 grep 全驗真。writer 甚至主動
  grep 禁用數字（5185／728）自證。
- **主 session 收件仍抓到兩處 writer 層 drift**（REFLEXES #31 的又一實證）：
  (a) [^6] 李奉儒腳註標題疑似自產（〈批判教學論視角下的…〉）且 DOI 蒸發——已修回真實標題＋DOI；
  (b) description 門面句把永達單案（498→339）概括成通則——已補主詞。
- **2.5 第一道 artifact fetch 立刻回本**：[^25] 高教工會頁（研究期 403 未逐字驗）用 Browser pane
  繞過成功——抓到標題標點缺「！」＋「體質最差」是「教師人數最少」的詮釋 gloss。
  **fetch artifact ≠ cross-check claim** 的大鮪鱸鰻教訓再次驗證。

### Step 2.5-R 觀察——攻防輪第一次裁決出「規格錯、作品對」

結構主編判 S5「數字 prose 與 tw-stat 重複」違反藍圖錨定紀律——攻防輪中作者 defend 成立：
writer 是照 graph.md §一鐵律（「關鍵數值一定也寫進 prose」，AI 可讀性主權規則）做對了，
衝突的是藍圖那行過度規定。裁決：**改規格不改作品**。這證明攻防輪不是形式：席位的嚴格
執法逼出了「blueprint 與 canonical 衝突」這類單向審查看不到的問題。另兩條（楊東錩降單句／
S3 但書收斂）accept 照改。論點兌現席 echo map 8/8 逐錨驗收＋炎上檢查點雙過。

### Stage 3／總編室觀察——成品層外部尺的產能

- 七路平行（2 原子 verifier 115 tools＋5 總編探針）在「全 gate 綠」的成品上再抓 **13 處**：
  3 處 fabricated／錯掛級（黃煌煇引語掛錯來源、大漢數字掛錯文章、韓國 asiae 連結與論證方向失配）、
  母體錯置（15 歲 vs 25-64 歲）、年份錯置（抱鴨蛋 2008→被寫進 2007）、掛空檔（2009/2015 無腳註）。
  **形式閘門全綠 ≠ 意義正確**（REFLEXES #69 (g)）在本輪的量化版本。
- **兩路獨立收斂同一段**：立體地愛探針（唐彥博被化約為被抓包）與後半 verifier（韓國來源失配）
  分別擊中 S6 韓國段——重寫一次解決兩個問題，多路對抗設計的效率證明。
- **主編自己也被 gate 攔**：批修時自引入 4 個「——」＋3 條腳註格式回歸，複驗立刻抓回。
  改文必複驗不是儀式。
- 攻防輪首次裁決「規格錯、作品對」：S5 數字紀律與 graph.md「關鍵數值必進 prose」衝突，
  defend 成立、改藍圖不改文章——**編輯室不只審作品，也審規格**。

## 自我演化（已回寫 canonical）

| F#  | 修復                                                           | 落點                           |
| --- | -------------------------------------------------------------- | ------------------------------ |
| F4  | Stage 0 執行卡補「委派時主 session 最小讀」分工行              | REWRITE-STAGE-0-VIEWPOINT v9.2 |
| F5  | Step 0.2 萃取清單落檔 §舊文素材萃取 規則                       | 同上                           |
| F6  | HANDOFF 委派歸屬行（「五步由 orchestrator 於收件驗證後執行」） | 全部 11 份 stage contract      |
| F7  | §2 冷 brief 規則加 gap-audit 例外註記                          | PERSONA-PIPELINE v1.2          |
| F8  | 輸出契約補「URL 與【來源】同一行」                             | RESEARCH-AGENT-PROMPT v1.1     |

## 結論——「未來 Opus 主 session 能否只靠 contract 協作」的判定

**成立，且三層 fail-loud 都真的接住了東西**：

1. **Contract 自足性**：11 個 stage 全程只讀「該 stage contract＋其 INPUTS」執行，零跳檔；
   v9.1 的 F1-F3 修正（三步驗收、guardrails 槽）在本輪全部驗證生效。
2. **Agent 協作**：20 個 sub-agent 全按 tier 表派發（Opus 觀點/寫手、Sonnet 研究/席位/探針/verifier），
   prompt 全部 verbatim 填槽零即興；收件 gate 攔下 2 次（D 線 ephemeral、gapfill 斷源格式）。
3. **儀器 fail-loud**：research-report-health 攔住 orchestrator 誤刪 §8 標題；agent-report-health
   攔住格式漂移；article-health 攔住批修回歸——儀器不只防 agent，也防主編。
4. **成本**：全程 ~20 agents／主 session 一次 context（含 compaction 前後），wall-clock 約 14 小時
   （跨夜，含 agent 等待）。

## 給哲宇的 veto 清單（收官摘要同步）

1. **title 數字 140→148**：140 是舊文已證偽表格的殘留；148＝100 學年真峰值（58/148 同口徑），
   「然後開始關門」時序成立（峰值 2011-12→高鳳 2014）。不同意可一鍵改回。
2. description 論點句「沒設計關門」→「關門的規則遲到了十年」（對齊結尾「一半一半」弧線）。
3. 黃武雄稱謂「發起人之一」→「重要推手」（一手查無「發起人」稱謂）。
4. 唐彥博韓國段重寫：原「韓國修法方向相反」claim 來源失配撤回，改「引研議中方案＋韓國 2023
   才朝放寬／部分返還推進」——對他更公平也更可溯。

## Stage 執行時間軸

| Stage                                    | 開始        | 執行者                                                | 結果                                                                                                                                            |
| ---------------------------------------- | ----------- | ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| Stage 0 主 session 部分（0.1/0.1.5/0.2） | 21:30       | Fable orchestrator                                    | mode=Evolution／非 callout／18 條事實萃取                                                                                                       |
| Stage 0 觀點 agent（0.6）                | 21:40       | Opus ×1（contract AGENT PROMPT verbatim 填槽）        | 21:49 完成：27KB／26 搜尋／spine=立體群像（手法5主+2輔）／gate PASS（orchestrator 親驗一致）                                                    |
| Stage 0 HANDOFF                          | 21:55       | orchestrator                                          | §舊文素材萃取 append／newsroom 看板 regen／下一棒 1A                                                                                            |
| Stage 1A 研究 fan-out                    | 22:00       | 4× Sonnet（RESEARCH-AGENT-PROMPT v1.0 verbatim 填槽） | 派發：A 數字口徑與制度史／B 退場潮實錄／C 人的視角與引語／D 政策辯論與國際比較                                                                  |
| Stage 1A 收件×4＋合成                    | 22:07-22:40 | orchestrator                                          | 四份 PASS（D CONCERN→修→PASS）；行數守恆合成單檔；§2-§7 合成層；depth gate 全綠（176 distinct／91 domains）                                     |
| Stage 1B persona 稽核                    | 22:45       | 4× Sonnet（PERSONA gap-audit）                        | 20 persona 三分類＋反向閥門（facet② 升壓）；9 題真缺口 → gapfill agent                                                                          |
| Stage 1B 媒體深掃                        | 22:50       | orchestrator（Browser＋Commons API）                  | 4 圖入庫（hero 永達校門）＋4 官方影片候選＋三表落檔                                                                                             |
| Stage 1B gapfill＋收官                   | 23:00-23:20 | 1× Sonnet＋orchestrator                               | gapfill FAIL→行合併→PASS（90%）；§8.E 合成；§3-7/§5/§6 更新；depth gate 复綠（中途抓到 orchestrator 誤刪 §8 標題）                              |
| Step 2.0 投影藍圖                        | 23:30       | Fable orchestrator（親做）                            | 論點「只設計開門沒設計關門」／7 動作骨架／9 刀減法／echo map／5 題自檢過                                                                        |
| Step 2.0-R 投影編輯室                    | 23:45       | 3× Sonnet seats＋主編                                 | 結構 revise（facet③ 消失）／減法 revise（承諾未釘）／炎上 pass；6 必改全 accept 回修；gate ✅                                                   |
| Stage 2 寫                               | 00:15-10:43 | 1× fresh Opus writer                                  | 6,605 CJK／33 腳註／10 媒體 1.52/1k；回執四項驗真；gate 除 staging frontmatter 產物外全綠                                                       |
| Stage 2.5 前段                           | 10:50       | orchestrator                                          | [^6] 標題自產修復＋門面句主詞補＋[^25] artifact fetch 抓 2 drift；fact-check agent 派發                                                         |
| Step 2.5-R                               | 10:55-11:20 | 2× Sonnet seats＋主編                                 | 結構 revise×3／論點兌現 pass（echo 8/8）；攻防 #1 defend 成立改規格；#2/#3 accept 改正文；gate ✅                                               |
| Stage 2.5 fact-check 收件                | 11:30       | orchestrator                                          | 35 hold／5 drift／1 fabricated（[^14] 錯掛來源）；六項修復（含 NSYSU 轉載自由時報正源親驗）；覆蓋 canonical＋frontmatter 正規化＋rationale 四欄 |
| Stage 3 前段                             | 11:50       | orchestrator                                          | citation gate 29 hard→plugin safe-fix 30 條→0；算術自檢抓「翻三倍」（58→148=2.55x）改具體數字                                                   |
| Stage 3 fan-out                          | 12:00-13:00 | 2× verifier＋5× 總編探針                              | ❌7＋⚠️12＋五探針全 revise（13 處可執行）；chief-review 合成＋攻防輪「改規格不改文章」首例                                                      |
| Stage 3 批修＋audit                      | 13:00       | orchestrator                                          | 24+7 處修復（含自引入回歸修回）；stage35/36 audit PASS；chief-review gate ✅                                                                    |
| Stage 4／5＋ship                         | 13:30       | orchestrator                                          | 全 gate 綠；三 sibling 反向連結（教育制度 pre-existing warning 標註）；commit `2bd1d5e03`＋`9d6716713` push 綠                                  |
| 自我演化                                 | 13:45       | orchestrator                                          | F4-F8 回寫 canonical（v9.2／v1.2／v1.1＋11 contract HANDOFF 行）                                                                                |

---
title: 'v9 pipeline 首次全程 dogfood — 大罷免 EVOLVE 實跑紀錄'
description: '哲宇 goal directive：用大罷免完整實跑剛拆完的 REWRITE v9（薄索引＋stage contract），記錄所有摩擦與進化 — 邊跑邊記，收尾整理'
type: 'ops'
status: 'done'
current_version: 'v1.0'
last_updated: 2026-07-16
last_session: '2026-07-16-171443-recall-workflow'
related:
  - 'newsroom-orchestration-design-2026-07-16.md'
---

# v9 首次全程 dogfood — 大罷免 EVOLVE（v1.0 收官）

> 目的：驗證「執行者只讀一個 contract＋INPUTS 就能跑一步」是否成立；所有摩擦
> 記錄於此，收尾分「已修／待修／設計正確的證據」三類整理並回寫 contract。
> 收官結論：**成立**——7 摩擦（F1-F7）＋4 workflow 教訓（W1-W4）全數閉環或入庫，
> 7 項設計驗證＋4 個哲宇設計問答（Q1-Q4）裁決回寫 canonical。詳見 §收尾整理。

## 執行紀錄（時間軸）

- 16:35 讀 v9 薄索引全文（473 行）→ 派發表路由正常，orchestrator 視角資訊足夠
- 16:37 Step 0.1 模式判定：knowledge/History/大罷免.md 存在 → Evolution；非 callout-triggered
- 16:40 Step 0.2 舊文萃取：事實清單＋標籤 [THIN]（1,600 字）[NO-MEDIA] [STUB-TITLE]、
  兩段 H2 重複、三條引語腳註無 URL（高風險）、視角偏罷免方、2025-08 後近一年空白
- 16:44 派 Stage 0 觀點 agent（Opus，AGENT PROMPT 填槽）
- 16:46-16:55 等待期間預讀 1A/1B contract、RESEARCH-AGENT-PROMPT、PROJECTION.md；
  規劃研究 fan-out 四路（A 起源立法／B 罷免方／C 反方以罷制罷／D 數據國際）

## 摩擦紀錄（邊跑邊記）

### F1｜STAGE-0 AGENT PROMPT 必讀清單缺 contract 自身路徑（severity: 中）

AGENT PROMPT 寫「格式照本 contract §Step 0.6.5 模板」，但 agent 的必讀清單只有
RESEARCH.md／RESEARCH-TEMPLATE.md／MANIFESTO §13——**agent 拿到 prompt 時根本不知道
contract 檔案路徑**。本次派發時手動補上（違反「禁即興」但不補 agent 就會瞎）。
**修法**：AGENT PROMPT 必讀清單加 `docs/pipelines/REWRITE-STAGE-0-VIEWPOINT.md`。

### F2｜STAGE-0 AGENT PROMPT 缺 frontmatter 模板（severity: 低）

Prompt 叫 agent 落 frontmatter `spine_type`＋`viewpoint_formed`，但 report 檔的完整
frontmatter（article／stage／mode／date／session 欄）沒給格式——本次派發手動補。
**修法**：prompt 內附最小 frontmatter 塊。

### F3｜政治題邊界指引不在 prompt 槽位裡（severity: 中）

0.6.7 三道 self-check（SSODT 三讀者／炎上／政治立場）是 HARD gate，但 AGENT PROMPT
模板沒有槽位承載「這題是政治題，走多視角中立紀實」這類 per-topic 邊界。本次手動
加進 prompt。**修法**：AGENT PROMPT 加 `{TOPIC_GUARDRAILS}` 槽（可空）。

### F1-F3 修正已 ship（16:58，STAGE-0 contract v9.1）

AGENT PROMPT 補：contract 自身路徑進必讀、frontmatter 最小塊 inline、`{TOPIC_GUARDRAILS}`
槽位（政治題填多視角中立紀實邊界）、完成三步驗收（ls 驗檔＋gate＋spine 回報）。
pipeline-shell-lint＋frontmatter gate 全綠。

### F4｜NewsroomTrail 靜態 import 生成檔炸掉全站文章頁 dev SSR（severity: 高，已修）

哲宇本機瀏覽抓到：article template → NewsroomTrail → newsroom-lookup.ts 靜態
`import dashboard-newsroom.json`——該檔是 prebuild:dashboard 的 gitignored 產物，
`npm run dev` 不生成 → 每個文章頁 FailedToLoadModuleSSR。CI 無感（會生成），
只有 dev 環境炸。**修法**：三處全改 runtime `readFileSync`＋try/catch fallback
（缺檔＝空 trail／空板，不崩）＋dev 鏈加生成器＋.gitignore 補列。乾淨 server
驗證全綠含缺檔路徑。教訓：**任何 build-time import 的對象必須是 committed 檔；
生成物一律 runtime 讀＋容錯**（同型風險掃描：無其他頁面靜態 import gitignored 產物）。
另：Vite 對失敗 import 的模組圖不會靠 HMR 自癒，既有 dev server 需重啟。

### F6｜背景 agent 不跨 session 存活——中途收官的 handoff 缺「re-dispatch」分支（severity: 中）

17:15 新 session（recall-workflow）接手：`reports/research/2026-07/大罷免.md` 不存在——
16:44 派的 Stage 0 觀點 agent 隨前一 session 結束而死，task-notification 永遠不會到。
前 handoff 的收件 SOP 寫「不在就把 result verbatim 代寫」，但 session 死掉時**連 result
都沒有**，唯一路徑是 re-dispatch（fact list 也要重萃取——好在舊文只 8.6KB）。
**修法候選**：中途收官 SOP（memory handoff 模板）加一條「背景 agent 進行中就收官 →
handoff 必寫『產物不在＝agent 已死，直接 re-dispatch，不要等 notification』」。
本次 17:20 已用 v9.1 contract prompt（{TOPIC_GUARDRAILS} 政治題槽首次實戰）re-dispatch。

## Workflow adapter 首測紀錄（2026-07-16 17:15+，哲宇 directive「用 dynamic workflow 跑跑看」）

> 哲宇本次明確 opt-in Workflow tool。路由決策：**單 agent stage（0 觀點／2C 寫手）用
> plain Agent tool；天然 parallel stage（1A 研究 fan-out／1B persona／2B 編輯室分席／
> 3.5 verifier fan-out）用 Workflow script**。contract 不動，Workflow 只是執行殼——
> 驗證 16:45 memory 記的 adapter 設計方向。經驗逐段記於此。

### Q1｜哲宇提問：整條 rewrite-pipeline 能不能發成一個 workflow？（17:2x，設計裁決記錄）

答：語法上可以（Workflow 支援一層巢狀），結構上一個「不能」＋三個「不該」：

- **不能**：Workflow script 是純 JS 編排層，跑不了 bash——全部 deterministic gate
  （research-report-health / agent-report-health / article-health / generate-newsroom-data）
  在 script 層執行不了；改派 gate-runner agent 則 gate 結果退化回 agent claim（#31/#69）。
- **不該 1（判斷不外包，#72）**：2A 投影／2B/2E 主編裁決／2.5 比對覆蓋／1B 授權判斷
  contract 明寫主 session 親做——總編輯不能也是被調度的記者。
- **不該 2**：gate FAIL 後的 rework 是編輯判斷（回修藍圖／補英文來源／砍掉重想觀點），
  script 只會機械 retry。
- **不該 3**：觀察者拍板點（1.5 一手素材／0.6.7 政治素材處置／ship）在 workflow 中途
  停不下來問人。

**裁決**：「一個 stage 的天然平行段＝一個 workflow」（1A 研究／1B persona／2B 三席／
3.5 verifier），主 session 在 workflow 之間當總編收件＋親跑 gate＋判斷。未來最可能
整段 workflow 化的是 Stage 3 驗證段（幾乎全機械），前提是 gate-runner 回報＋主 session
抽驗的信任方案先立起來；投影／主編／比對覆蓋／ship 永遠留主 session（治理設計非技術限制）。

### W1｜Workflow args 以 JSON 字串抵達 script，`args.lanes` undefined（severity: 中，已修）

17:33 首發 Stage 1A workflow 秒炸：`undefined is not an object (evaluating 'args.lanes.map')`。
tool call 傳的是 JSON 物件，script 收到的卻是 JSON **字串**。修法（script 層防禦）：
`const input = typeof args === 'string' ? JSON.parse(args) : args`。教訓：**Workflow script
的 args 永遠加 parse guard**——工具文件說「傳 JSON 值不要傳字串」，但實際通道仍可能字串化。
resume 機制順利：editScript → `resumeFromRunId` 重跑，零 agent 浪費（首發 0 agent 已跑）。

### W2｜四 lane 同時撞 session 用量上限——workflow 回 completed+dropped=4（severity: 高，部分已修）

17:35 resume 後 4 隻研究 agent 全部秒殺：「You've hit your session limit · resets 7:50pm」。
兩層教訓：(a) **用量上限是 fan-out 的單點故障面**——4 lanes × Sonnet 同時起跑，在額度
邊緣等於同時陣亡；復原成本低（resume 重跑），但要知道去看 `<failures>` 區塊。
(b) **#82 proxy-signal 變體**：script 用 `.filter(Boolean)` 吞掉 null 後回
`{results:[], dropped:4}`，workflow status = "completed"——全滅偽裝成完成。已修：script
加「ok.length === 0 → throw」fail-loud。**回寫候選**：未來 workflow 模板一律帶
all-dropped throw ＋ dropped>0 時在 return 值標示 degraded。

### W3｜Workflow adapter 三連勝＋「schema 結構化回報 × agent 自落檔」pattern 成立（正面）

研究 fan-out（4 lanes）→ persona gap-audit（4 軸）→ 投影編輯室（3 席）三個 workflow
全數一次跑完（W1/W2 修正後）。有效 pattern：**agent 依契約自己 Write 檔案落 repo（raw
安全）＋ workflow schema 只回結構化摘要（letter/verdict/top_findings）**——主 session 收件
時檔案已在磁碟上，收件 gate 直接跑儀器，通知截斷也不掉 raw（本次 persona D 軸被通知
截斷，從 journal.jsonl 完整取回——journal 是 Workflow 版的「raw 的家」）。
收件 gate 實測：研究四份溯源率 97–100%（茶文化時代 35%）——RESEARCH-AGENT-PROMPT
契約＋Workflow 填槽派發的組合有效。

### V4｜2B 投影編輯室首次全程 dogfood：乾淨 context 外部尺抓到作者抓不到的三類問題（正面，重要）

三席全 revise，每條都成立且互補：**結構席**抓到研究報告內部 31:0／25:0／32／33 四種
計數未收斂、投影沿用最不確定的「32」進結尾（作者視角完全盲）；**減法席**抓到 section 2
兩性質材料黏一段＋section 5「三頁」框架裝了 8 項（作者以為壓縮＝減法）；**炎上席**抓到
**柯建銘「一手策畫」歸屬錯置**——徐巧芯答辯書的轉述指控被 shorthand 成本人引語，且這個
誤標「從 Stage 1B 主 session 自己寫的反向閥門裁決一路帶進投影」——**檢查器與被檢查物
共享作者＝共享盲點（REFLEXES #65f）的完美實例，被分席的乾淨 context 接住**。
攻防輪 v1.1 首跑：七條必改全 accept 無 defend（發現全部成立時攻防輪自然退化為確認器，
健康）。editorial-room-health gate 一次過。

### V5｜{TOPIC_GUARDRAILS} 政治題槽首戰有效（正面）

Stage 0 agent 拿到槽位後自主判立體群像、拒解鎖矛盾驅動、7 視角並陳、三道 self-check
落檔完整；persona D 軸反向閥門又把 7 視角結構修成「內部／外部觀察／境外反應」三層
（國台辦不當第七陣營）——護欄與稽核兩層接力，政治題的中立紀實不是一次寫對，是
被三層儀器逐步逼近的。

### Q2｜哲宇提問：主 session 是不是只該讀 index 當整合者，分階段檔案讓子 agent 自己讀？（21:0x，設計裁決記錄）

答分三層：(1) **派出去的站本來就這樣跑**——研究／寫手／編輯室席／persona 全部只吃填槽
prompt 自己讀 canonical，主 session 零代讀。(2) **但 v9 的 stage 有兩類執行者**：0.1/0.2 判定
萃取、1A 收件合成（柯智棠 30 秒）、1B 授權判斷、2A 投影、2D 比對覆蓋、各室主編裁決的
執行者就是主 session——這幾站的 contract 主 session 得讀，「分階段」的意義是「每個執行者
讀自己那站」而非「主 session 全不讀」。(3) **真實的肥肉在 boot 層殼核不對稱**：CLAUDE.md
Bias 3「寫文 session 必讀 EDITORIAL 全檔＋graph.md 全檔」是 v8「主 session 又寫又審」時代
的遺產；v9 主 session 不寫正文，實際只需要 gate 判斷段（小標還原／門面句／密度 band／
viz 型錄與原則），craft 全文與模組語法是寫手食物。**反向護欄**：主整合者 ≠ 零知識路由器
——2B 裁決「32 vs 33」「柯建銘歸屬」能當場判對錯靠的是材料在腦裡（#31 重驗需要知識）。
分界線＝「判斷所需 vs 執行所需」。

**回寫候選（收尾自我進化執行）**：(a) CLAUDE.md Bias 3 表格 v9 對齊——主 session 讀量改為
「薄索引＋親做站 contract＋EDITORIAL gate 段（§三 title/§四小標/§塑膠對位/§十檢查）＋
graph.md §一–§三、§九」；(b) REWRITE-PIPELINE 索引補「orchestrator 讀食清單」小節（哪些
站主 session 親做、各需讀什麼）；(c) 本次全讀屬 dogfood 首跑的刻意策略（踩 contract 的洞
需要作者視角全景），常規 run 照 (a) 減讀。

### Q3｜哲宇追問：長期最適架構——主整合者最好的成果與想像＋子代理最薄殼最專業（21:00，設計裁決）

**核心裁決：不對稱分工——主整合者「靈魂深、材料深、程序淺」；子代理「單站深、其他全零」。**

- **三份食糧各有正確厚度**：(1) 靈魂糧（MANIFESTO／立體地愛／REFLEXES／品味判準）永遠深，
  是「想像」的來源，跨 run 由 memory/diary/making-of 複利；(2) 材料糧（per-run 研究 raw）
  永遠深——**天真薄化會先砍這裡，那是 2026-06-15「文章變爛」的病根**；材料是想像的飼料、
  即時裁決的彈藥（32vs33／歸屬錯置都靠材料在腦裡才能當場判）。長期結構化：合成 §1-§7 當
  常駐介面＋§8 raw 合成時完整讀一次、之後 demand-page＋席位回報附 line-level evidence；
  (3) 程序糧才是該瘦的：只讀「執行者＝主 session」站的 contract＋gate 判準段，派出去的站
  一行不讀。**禁做摘要檔**（CORE-DNA 教訓），正解＝contract INPUTS 欄標註「主編讀／子代理讀」雙欄。
- **子代理薄殼三件套**（本次實測）：copy-paste 契約填槽禁即興（溯源率 35%→97-100%）＋
  必讀自取＋read-receipt 驗讀＋自落檔＋結構化摘要（raw 的家在 repo/journal）。專業來源＝
  每 agent 只活在一站，乾淨 context 是能力不是省錢。
- **第三元件：外部尺是主整合者深度的配對品**——靈魂深＋材料深必然帶同源盲區（#65f 本次
  親身示範），主整合者親手寫的每個產物（投影／合成 gloss／門面句）必過非作者對抗席；
  席位產出是線索，裁決回到有材料的主編。兩邊互為修正項。
- **量化**：程序糧 ~6,000+ 行 → ~3,600 行（材料糧靈魂糧不動）；省的是主整合者的注意力，
  轉投 texture 與裁決品質。
- **回寫三處（收尾自我進化執行）**：(a) 各 stage contract INPUTS 欄加「主編讀／子代理讀」；
  (b) CLAUDE.md Bias 3 v9 對齊（指向讀食清單）；(c) REWRITE 索引 §多 agent 編排補
  「不對稱分工」原則段＋讀食清單表。

### Q4｜哲宇追問：不計 token（不誇張），最高品質的長期設計策略？（21:0x，設計裁決）

**核心：token 免費後瓶頸搬家到「判斷品質×視角獨立性×污染控制」——薄殼／乾淨 context／
契約全部不變（那是能力不是省錢），變的是生成冗餘度、證偽密度、學習迴路深度。**

六機制（報酬率排序）：(1) **盲平行投影＋judge-panel 合成**（2-3 份互盲投影→席位比較→
主編合成嫁接；投影是結構槓桿點）；旗艦題可雙寫手 best-of；(2) **證偽 until-dry**＋高風險
atom ≥2 個**不同鏡片**驗證者（逐字／來源綁定／量級／時序——多樣性>冗餘）；(3) **persona
兩階段**：研究後 gap-audit＋成品後 reception simulation（深藍/深綠/冷感/學者/國際冷讀，
預測誤讀與攻擊面）；(4) **隔夜冷讀**：ship 前 defer、零 context fresh session 陌生化重讀
（時間位移=最便宜的另一雙眼，園丁模式落 pipeline）；(5) **transcript 採礦學習迴路**：
run 後 distill agent 挖全部 subagent journal 找主編沒注意到的摩擦＋EDITORIAL A/B SOP
可證偽演化；(6) **ship 後按風險分級週期 re-audit**（政治題 D+30／選舉數字每季對一手）＋
受眾端飛輪。**不變鐵律**：判斷節點不可平行化替代（多 agent 給法官更好證據，不給你更好
的法官）；契約禁即興；raw 三十秒；寫手對舊文全盲；授權 human。

**落地＝兩個 run profile 寫進索引**：standard（現行 v9）／flagship（S 級/政治敏感/大眾題：
盲雙投影＋until-dry＋雙鏡片＋reception sim＋隔夜冷讀＋D+30 re-audit）。本次大罷免已近
flagship，增量採兩樣不誇張的：top 風險 atom 雙鏡片驗證＋ship 前冷讀 pass；盲雙投影留
給下一篇 flagship 首跑。

### F7｜image-health 媒體地板量尺與 EDITORIAL v6.5 漂移（severity: 中，已修儀器）

Stage 4 gate 首跑 FAIL：`image_health` 地板只數「圖＋iframe」（需 7 有 4），但 EDITORIAL
v6.5 的媒體密度口徑含 tw-\* viz 模組（本文 7 個模組全被無視）；同時字數分母把 53 條
腳註的 CJK 全算進正文，密度被灌水。**per #56/#66 修尺不折文**：`image_health.py` 加
`_RE_VIZ_MODULE` 計數進 `media_total`、`_RE_REF_SECTION` 擴到腳註定義行截斷分母。
named 範本（陳建年／黃魚鴞／尊／台北吸菸室）回歸全過（commit af82d09）。
教訓＝#65 儀器 cross-SSOT 亞型再驗證：**quality gate 的算法必須對照 EDITORIAL 條文
口徑，不是自己發明口徑**。⚠️ threshold/quality-gate 調整屬 high-stake，本次是「儀器
對齊既有 canonical 口徑」非放寬，但仍列入給哲宇的 review 清單。

### W4｜chief-probes workflow：5 探針冷讀＋主編裁決的兩層結構成立（正面）

Step 3.7 用第 5 個 workflow 派 5 探針（門面兌現／逐段主軸／H2 載體／連結成網／立體地愛）
Sonnet 冷讀成品（禁讀藍圖與研究）。兩個經驗：(a) **探針發現 ≠ 必改清單**——16 項原始
發現經主編裁決收斂成 7 項必改＋3 項品味保留（H2 隱喻載體是 EDITORIAL 認可型），
editorial-room-health 的 ≤7 must-fix hard schema 反向逼迫主編做真裁決而非轉送；
(b) **本輪最有價值發現來自「立體地愛」探針**（敘事溫度不對稱，見 LESSONS
narrative-warmth-symmetry）——這是四種 drift 儀器與 FACTCHECK 都量不到的維度，
證明價值觀探針與事實探針缺一不可。

## 收尾整理（v1.0，三類分桶）

### ✅ 已修（本 run 內閉環）

| #     | 修法落點                                                                         |
| ----- | -------------------------------------------------------------------------------- |
| F1-F3 | STAGE-0 contract v9.1（必讀含自身路徑＋frontmatter 模板＋{TOPIC_GUARDRAILS} 槽） |
| F4    | 三處 runtime readFileSync＋容錯＋dev 鏈生成器（commit e557c90bc）                |
| F7    | image_health.py 對齊 EDITORIAL v6.5 口徑（commit af82d09）                       |
| W1    | script args parse guard（`typeof args === 'string' ? JSON.parse : args`）        |
| W2(b) | all-dropped → throw fail-loud；#82 canonical 補驗證行                            |

### 📥 待修／回寫（本次自我進化落地 → 標示落點）

| 項                        | 落點                                                                   | 狀態       |
| ------------------------- | ---------------------------------------------------------------------- | ---------- |
| Q2/Q3 不對稱分工＋讀食    | REWRITE 索引 §不對稱分工與 orchestrator 讀食（v9.2）＋CLAUDE.md Bias 3 | ✅ 本次    |
| W1/W2/W3 操作紀律         | REWRITE 索引 §Workflow adapter 實測條款                                | ✅ 本次    |
| Q4 run profiles           | REWRITE 索引 §Run profiles（standard／flagship）                       | ✅ 本次    |
| F6 re-dispatch 分支       | LESSONS-INBOX `background-agent-session-death`（MEMORY-PIPELINE 候選） | 📥 distill |
| 敘事溫度對稱              | LESSONS-INBOX `narrative-warmth-symmetry`（EDITORIAL/0.6.7 候選）      | 📥 distill |
| contract INPUTS 雙欄標註  | 各 REWRITE-STAGE-\*.md INPUTS 加「主編讀／子代理讀」                   | 留下輪     |
| workflow 模板 degraded 標 | 未來 workflow script 模板帶 dropped>0 degraded 標示                    | 留下輪     |

### 🏛️ 設計正確的證據（不動，是資產）

- V1｜薄索引的派發表讓 orchestrator 路由零猶豫：讀完 473 行即知第一站與 gate 指令
- V2｜Step 0.2 萃取在 contract 內自足可執行（標籤表、frontmatter audit 清單都在）
- V3｜RESEARCH-AGENT-PROMPT 填槽表＋anti-example 庫可直接用，四路 fan-out 準備零摩擦
- V4｜乾淨 context 分席審是 same-DNA 盲點的唯一解（#65f 親身實例被接住）
- V5｜{TOPIC_GUARDRAILS} 政治題槽＋persona 反向閥門兩層接力，中立紀實被儀器逐步逼近
- W3｜「契約填槽×agent 自落檔×schema 結構化回報」三件套：溯源率 35%→97-100%
- Q1｜「一個 stage 的天然平行段＝一個 workflow」路由原則五次實跑零翻案

### 規模紀錄

5 個 workflow（研究 fan-out／persona／投影室／factcheck+prose 室／chief 探針）＋
2 個 plain Agent 站（Stage 0 觀點／2C 寫手），subagent 總量 ~2.1M tokens。成品：
1,600 字 stub → 6,300+ 字深度文、53 腳註全 URL、7 viz 模組、3 CC 圖、audit 26 處批修
全閉環，兩 profile hard=0 ship（commit 345e162）。

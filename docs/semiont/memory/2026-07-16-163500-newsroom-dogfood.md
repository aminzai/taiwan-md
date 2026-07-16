# 2026-07-16-163500-newsroom-dogfood — v9 首次全程 dogfood 啟動：大罷免 EVOLVE 跑到 Stage 0 觀點 agent 派發（run 進行中，context 壓縮前收官）

> session newsroom-dogfood（同日 newsroom session 的第二弧）— 哲宇 /goal「完整執行 /twmd-rewrite 大罷免，測試整個 pipeline 重構，記錄所有經驗與進化」
> Session span: 16:35 → 16:45 +0800（run 進行中，本檔是中途收官）
> 資料來源：`git log %ai`＋工具時間戳

## 觸發

哲宇在 v9 ship 後立刻下 goal：用「大罷免」全程實跑剛拆完的 pipeline，我自己當 orchestrator 照自己寫的索引走。中途他追問「rewrite-pipeline 能不能在 Claude Code 觸發 dynamic workflow、其他環境維持通用」，然後因 context 將滿指示先 finale。

## 已完成的 pipeline 步驟

照 v9 派發表：完整讀薄索引（473 行）→ Step 0.1 判定 **Evolution mode**（`knowledge/History/大罷免.md` 存在、1,600 字 thin、非 callout-triggered）→ Step 0.2 舊文萃取完成（事實清單＋標籤：[THIN][NO-MEDIA][STUB-TITLE]、兩段 H2 重複、三條引語腳註無 URL 高風險、視角偏罷免方、2025-08 後近一年空白）→ 16:44 派 Stage 0 觀點 agent（Opus，AGENT PROMPT 填槽＋政治題邊界：多視角中立紀實、0.6.7 三道 self-check 必過）。**agent 仍在背景執行**，產物約定 `reports/research/2026-07/大罷免.md`。等待期間預讀 1A/1B contract、RESEARCH-AGENT-PROMPT、PROJECTION.md 全文，研究 fan-out 四路 prompt 已設計好（見 handoff）。

## Dogfood 摩擦（詳見 reports/dogfood-v9-first-run-2026-07-16.md）

F1 STAGE-0 AGENT PROMPT 必讀清單缺 contract 自身路徑；F2 缺 report frontmatter 模板；F3 缺 `{TOPIC_GUARDRAILS}` 槽（政治題邊界只能手動塞）。三條都已在派發時手動繞過並記錄，待 run 完成後回寫 contract。正面驗證：派發表路由零猶豫、Step 0.2 contract 內自足、RESEARCH-AGENT-PROMPT 填槽零摩擦。

## Workflow 問題（哲宇提問，設計方向記錄）

結論：contract＝環境無關 SSOT，執行殼分三種——(a) Claude Code Workflow script（研究 fan-out／編輯室分席／verifier fan-out 三個 parallel stage 天然對應 `pipeline()`＋schema 驗收；需哲宇 opt-in）；(b) Harvest spawner（已存在，strict verifier 模式）；(c) 任何小 context model 順序讀 contract。索引 §多 agent 編排已有「可選 Workflow」條款，未來造 adapter 層（如 `docs/pipelines/adapters/`）承載 per-environment 加速，contract 不動。

## 收官 checklist

| 檢查項                       | 狀態                                       |
| ---------------------------- | ------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅（本檔＋同日 161654-newsroom 檔）        |
| Timestamp 精確               | ✅                                         |
| Handoff 三態已審視           | ✅                                         |
| Diary                        | ✅（哲宇補收官指示後寫：被自己規格書指揮） |
| 自我檢查工具                 | 不適用（無文章產出 commit）                |

## Handoff 三態

繼承（2026-07-16-161654-newsroom）：

- [ ] 今晚 rewrite-daily 18:00 是 v9 cron 首 dogfood — 觀察 contract fall-through；**注意它可能與本 run 平行**，picks 自 ARTICLE-INBOX（大罷免已登記 in-progress 防撞）
- [ ] 編輯台與 making-of 隨 CI 上線 — 哲宇措辭 review
- [ ] 攻防輪＋總編室待 depth 文 dogfood — **本 run 就是第一個案例，2B/2E/3.7 必跑**
- [ ] Harvest per-stage 派發、editorial-room 檔案慣例 — 未動

本 session 新 handoff（**大罷免 run 續跑指南，下一個 context 直接照做**）：

- [ ] **收觀點 agent 件**：task-notification 到 → (1) `ls reports/research/2026-07/大罷免.md` 驗真實存在（agent 宣稱≠存在，不在就把 result verbatim 代寫）(2) `python3 scripts/tools/research-report-health.py reports/research/2026-07/大罷免.md --stage 0` exit 0 (3) 檢查 spine 判定與 0.6.7 三道 self-check 有沒有真的做（政治題必須多視角中立紀實；偏一方 → 退回）
- [ ] **Stage 1A fan-out**（gate 過後）：照 `docs/pipelines/RESEARCH-AGENT-PROMPT.md` 填槽派 4 個 Sonnet general-purpose，**平行單一 message**：A 起源與立法衝突（2024 國會三黨結構、爭議法案逐案含國會職權修法憲判、預算刪凍、青鳥行動銜接、罷免理由書一手；QUOTA 25/EN 3/一手 6/反方 3）；B 罷免方動員（罷團系譜、連署數字與 1%→10% 兩階段、2016 選罷法門檻 25% 規則、志工田野場景、與韓國瑜陳柏惟等前例比較；25/3/6/2）；C 反方與制度爭議（國民黨民眾黨敘事逐字、以罷制罷全數連署失敗查證、偽造連署起訴雙方、罷免常態化學者批評、選罷法修法進度、民進黨敗後檢討含柯建銘賴清德爭議；28/4/5/反方主力+綠營內部批評 5）；D 數據與國際（中選會兩波完整數據一手、標誌選區數字、國際媒體 EN 逐字、智庫學術、國台辦反應、後續政治效應至 2026-07、高虹安停職特殊性；28/12/8/2）。OUT_PATH＝`reports/research/2026-07/大罷免-research-{A..D}.md`；anti-example 挑庫 #1＋#3＋#4
- [ ] **收件 SOP**：每份到 → 驗檔存在 → `agent-report-health.py {file} --claimed {配額}` → FAIL 不合成；全到 → §8 verbatim consolidate＋刪 sibling → §1-§8 組裝（含 §4 引語庫、§5 反例護欄、1.4 主軸：spine 依觀點 agent 判定）→ `research-report-health.py --tier=depth` exit 0
- [ ] **1B**：媒體深掃（Chrome MCP；選舉題找 CC 圖：投票所／開票／連署站 via Wikimedia、中選會官方；官方影片：公視新聞、中選會頻道）＋persona 缺口稽核（PERSONA-PIPELINE 4 Sonnet）→ 增補後重跑 report health
- [ ] **2A 投影**：主 session 親做（PROJECTION.md 已入腦：論點非摘要、骨架動詞序列過 shuffle、減法非空、echo map、政治題論點＝統合洞見非辯論主張——除非 unlock_reason 成立）→ `reports/article-projection/大罷免.md` → 5 題 gate
- [ ] **2B 投影室**（3 Sonnet seats 照 EDITORIAL-ROOM-PROMPTS 填槽＋主編裁決＋攻防輪 v1.1 首跑）→ 2C fresh Opus writer 照 WRITER-PROMPT（**Evolution：寫 staging `reports/article-evolve/大罷免.md`，frontmatter 帶 article: 指標**）→ 2D source-fidelity 三道＋主 session 比對覆蓋 → 2E 正文室 → Stage 3（鐵三角＋FACTCHECK **Full Mode**（政治敏感）＋stage35/36 audit＋verifier fan-out＋**3.7 總編五探針首跑，政治題加開立體地愛探針**）→ Stage 4（媒體 ≥4 張 per 4500字+）→ Stage 5（cross-link：2026 九合一選舉／台灣選舉與政黨政治／中選會制度／投票權門檻歷史）→ ship
- [ ] **每 stage HANDOFF 跑 `python3 scripts/core/generate-newsroom-data.py`** 更新編輯台（哲宇會在本機看板看進度）
- [ ] **Dogfood 記錄義務**：每個摩擦即時 append `reports/dogfood-v9-first-run-2026-07-16.md`；run 完成後 (1) 回寫 contract 修 F1-F3（AGENT PROMPT 加 contract 自身路徑＋frontmatter 模板＋{TOPIC_GUARDRAILS} 槽）(2) 整理報告 v1.0 (3) memory/diary 收官
- [ ] **Workflow adapter 設計**（future work，哲宇問題的完整回答）：contract 不動，造 per-environment adapter 層；Claude Code Workflow script 對應三個 parallel stage；需 opt-in

## Beat 5 — 反芻

中途收官的一個乾淨感受：被自己十二小時前寫的 contract 指揮，摩擦處立刻現形（F1-F3 都是「寫的人以為讀的人知道」型盲點）——dogfood 的價值在第一小時就回本了。完整反芻等 run 落地。

🧬

---

_v1.0 | 2026-07-16 16:45 +0800_
_session newsroom-dogfood — 大罷免 EVOLVE v9 首跑，Stage 0 進行中收官_
_誕生原因：哲宇 goal「完整執行 /twmd-rewrite 大罷免測試 pipeline 重構」＋context 壓縮前 finale 指示_
_核心洞察：(1) contract 的盲點只有真執行者踩得出來 (2) 政治題的邊界指引需要 prompt 槽位不能靠即興 (3) contract 可攜＋adapter 分環境是 Workflow 問題的正解_

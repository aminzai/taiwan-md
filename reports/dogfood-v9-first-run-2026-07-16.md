---
title: 'v9 pipeline 首次全程 dogfood — 大罷免 EVOLVE 實跑紀錄'
description: '哲宇 goal directive：用大罷免完整實跑剛拆完的 REWRITE v9（薄索引＋stage contract），記錄所有摩擦與進化 — 邊跑邊記，收尾整理'
type: 'ops'
status: 'active'
current_version: 'v0.1-running'
last_updated: 2026-07-16
last_session: '2026-07-16-newsroom-dogfood'
related:
  - 'newsroom-orchestration-design-2026-07-16.md'
---

# v9 首次全程 dogfood — 大罷免 EVOLVE（跑動中的紀錄）

> 目的：驗證「執行者只讀一個 contract＋INPUTS 就能跑一步」是否成立；所有摩擦
> 記錄於此，收尾時分「已修／待修／設計正確的證據」三類整理並回寫 contract。

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

（收尾補：F5+）

## 設計被驗證的部分（正面證據）

- V1｜薄索引的派發表讓 orchestrator 路由零猶豫：讀完 473 行即知第一站與 gate 指令
- V2｜Step 0.2 萃取在 contract 內自足可執行（標籤表、frontmatter audit 清單都在）
- V3｜RESEARCH-AGENT-PROMPT 填槽表＋anti-example 庫可直接用，四路 fan-out 準備零摩擦

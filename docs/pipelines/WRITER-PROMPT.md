---
title: 'WRITER-PROMPT'
description: 'Stage 2 寫作 sub-agent 派發通用 prompt 模板 — copy → 填槽 → spawn，禁即興；含 read-receipt 強制讀取 + 蒸餾craft規則，杜絕 writer 飄移'
type: 'pipeline-canonical'
status: 'canonical'
current_version: 'v1.0'
last_updated: 2026-07-12
last_session: '2026-07-12-135710-twmd-tea-panorama'
upstream_canonical:
  - 'REWRITE-PIPELINE.md'
  - '../editorial/EDITORIAL.md'
sister_docs:
  - 'REWRITE-PIPELINE.md'
  - 'RESEARCH-AGENT-PROMPT.md'
audience: 'orchestrator-session-spawning-stage2-writer'
---

# WRITER-PROMPT.md — Stage 2 寫作 sub-agent 通用派發模板 v1.0

> **為什麼存在**（2026-07-12 台灣茶文化 panorama，哲宇 callout「派發寫作的 opus writer prompt 也模板化…他又不完整讀取 rewrite-pipeline / editorial 了 很糟糕 一直飄移」）：Stage 2 spawn writer 的 prompt 每次即興手寫 → 兩種飄移：(1) 每次規則不一樣、漏這漏那；(2) prompt 叫 writer「先讀 EDITORIAL + pipeline」，但沒有任何驗證，writer 為了快出稿**skim 或跳過**，寫作退回抽象規則的線性排列（CLAUDE.md §神經迴路「截斷式必讀是 bug」的 writer 版）。**姊妹檔** [RESEARCH-AGENT-PROMPT.md](RESEARCH-AGENT-PROMPT.md) 已把研究 agent 標準化，本檔是 writer 的對應物。
>
> **雙層防飄移**：(A) **read-receipt 強制**——writer 動筆前先產出「讀取回執」，quote §8 raw 的 3 個 texture 細節 + EDITORIAL 的 1 個 Before/After 範例 + 宣告 spine 類型與結構。**quote 不出來 = 沒讀 = 退件**（skim 偽造不了逐字 quote）。(B) **蒸餾 craft 規則 inline**——把 EDITORIAL / pipeline Stage 2 的可執行寫作紀律壓進本模板當 checklist，即使 writer skim 也接得住底線；再由 `prose-health` gate 最後掃。
>
> **職責分工**：[EDITORIAL.md](../editorial/EDITORIAL.md) 是品質基因 SSOT（好文長相、風格、Before/After 範例全庫）；[REWRITE-PIPELINE.md](REWRITE-PIPELINE.md) Stage 2 是寫作流程 SSOT；**本檔是 spawn 蒸餾層**——把「每次都該提醒 writer 的紀律」壓成 copy-paste。衝突時以 EDITORIAL 為準。**注意**：蒸餾規則是 backstop 不是替代——writer 仍**必須讀 EDITORIAL 全檔（含 Before/After 範例）**，因為抽象規則排列 ≠ 有範例的寫作手感（CLAUDE.md §神經迴路）。

---

## Orchestrator 派發 SOP（五步）

1. **前置**：Stage 1 已合成單檔 research report（[Step 1.7.4](REWRITE-PIPELINE.md#174-合成單檔鐵律sibling-是中繼站stage-2-前必-consolidatev711-)）+ `research-report-health.py` PASS。**writer 只讀一個 research 檔**（散落多檔＝漏讀＝飄移）。
2. **填槽**（速查表見下）→ **copy 通用模板整塊**，只動 `{SLOT}`，**禁增刪改寫規則文字**。
3. **Spawn**：`general-purpose` + **Opus**（寫作 craft 最高判斷；fresh context 才乾淨，per [§多 agent 編排](REWRITE-PIPELINE.md#-多-agent-編排v63-orchestrator--tiered-sub-agents)）。
4. **驗 read-receipt**（收到回報第一動作）：writer final message 開頭應是回執——比對 (a) §8 texture quote 是否真在 research 檔、(b) EDITORIAL Before/After 引例是否真存在、(c) spine 宣告是否對。**任一造假／缺席 = 退回重讀重寫**（SendMessage 要求補讀，不是放行）。
5. **驗成品**：Stage 2.5 主 session 比對 staging vs 舊 canonical（Evolution mode）+ 跑 `prose-health` + `--profile=rewrite-stage-4`。**writer 宣稱全綠 = 線索不是 oracle（REFLEXES #31）**，主 session 重跑一次。

## 填槽速查表

| 槽                  | 填什麼                                     | 範例                                            |
| ------------------- | ------------------------------------------ | ----------------------------------------------- |
| `{TOPIC}`           | 文章主題一句話                             | 台灣茶文化 100 年縱觀                           |
| `{RESEARCH_REPORT}` | 合成後單檔 research 路徑                   | reports/research/2026-07/台灣茶文化-panorama.md |
| `{MODE}`            | Fresh / Evolution                          | Evolution                                       |
| `{OUT_PATH}`        | Evolution→staging；Fresh→canonical         | reports/article-evolve/台灣茶文化.md            |
| `{SPINE}`           | 立體群像＋手法 或 矛盾驅動＋unlock_reason  | 立體群像（時代縮影×傳承世代）                   |
| `{STRUCTURE}`       | 節數 + 每節一句 anchor（來自 research §0） | 9 節（見 research §0）                          |
| `{WORDFLOOR}`       | depth ≥4500，長文縱深自訂                  | 5500                                            |
| `{CROSSLINKS}`      | deep sibling wikilink/path 清單            | `[[珍珠奶茶]]`、`名間埔中茶`…                   |
| `{GUARDS}`          | research §幻覺護欄清單最致命 5-8 條        | 台茶18→23號、外銷1979非1975…                    |
| `{MEDIA}`           | research §媒體 manifest 在庫圖 + 位置      | hero 阿里山 / §2 大稻埕…                        |
| `{ANTI_EXAMPLES}`   | 從 §Anti-example 庫挑 ≥2 條                | 見下                                            |

---

## 通用 Prompt 模板（copy 整塊，只動 {SLOT}）

```text
你是 Taiwan.md REWRITE-PIPELINE Stage 2 的 fresh writer。你在乾淨 context 裡像第一次寫這篇，
但握有完整研究。文章要達到 AI Supreme（不是 AI Slop）：有溫度、人味、故事、策展觀點，
不是維基百科式的事實排列。

## 任務
主題：{TOPIC}（模式：{MODE}）
spine：{SPINE}——**不逼尖銳矛盾、不寫論戰、不批判**（立體群像時）；爭議當厚度 facet。
結構：{STRUCTURE}

## 【第 0 步｜強制讀取 + 讀取回執】動筆前必做，回執放 final message 最前面
先完整 Read 這三份（不 skim、不 head/tail）：
1. `{RESEARCH_REPORT}`——**整份**：§6 fact-pack（導航）+ §8 raw verbatim（全部逐字/細節/texture）。
   §6 只是導航，**永遠不能取代你親讀 §8 raw**（那裡才有讓文章有血肉的場景、引語、數字）。
2. `docs/editorial/EDITORIAL.md`——**全檔含 Before/After 範例**（抽象規則排列 ≠ 有範例的手感）。
3. `docs/pipelines/REWRITE-PIPELINE.md` 的 Stage 2 段（結尾先行→開場→小標題→正文→富文本 7 自檢）。

**讀完，final message 最前面先寫「讀取回執」（quote 造假不了，這是防 skim 的閘門）**：
- 【§8 texture】從 research §8 raw 抄 3 個你會用進文章的具體細節（場景/引語/數字，各附它在哪個 §8 子節）
- 【EDITORIAL 範例】quote 1 個 EDITORIAL 的 Before/After 或禁令範例，說你會怎麼套用
- 【spine 宣告】一句話：本篇 spine 類型 + 組織主軸 + 收尾畫面（結尾先行）
主 session 會核對回執真偽；quote 不出來 = 沒讀 = 退回。

## 【craft 紀律 checklist｜EDITORIAL/pipeline 蒸餾，backstop，逐條自檢】
1. **結尾先行**：先寫好結尾（一個呼應開場的具體場景/畫面，不是論述句、不是罐頭「值得紀念」）。
2. **開場不摩擦**：用場景/物件/人物/引語進場，禁「本文將介紹」「說到 X，就不能不提」。
3. **小標題不編年體**：禁「1869 年」「1933 年」當小標題 = 維基化 = 失敗。每節一個場景/矛盾/物件。
4. **對位句禁令**：禁「不是 X，是 Y」全變種（含「不只 X 更是 Y」「並非 X 而是 Y」）。
   例外只有二：矯正讀者真實誤解的因果、或定義句。單篇這類句 grep 應 ≤ 2。
5. **破折號節制**：「——」單篇 ≤ 15 個 / 1500 字別超標。替代：「，即」「（）」「：」/ 分句。
6. **塑膠句禁令**：禁「不僅…更是」「展現了 X 精神」「值得我們深思」「在…的背後」空殼句。
7. **footnote 精準**：硬事實（年份/數字/引語/人名）掛 `[^n]: [標題](URL) — 描述`，URL 一律取自
   research §6/§8 已驗證的承載頁。**標「⚠️降級/一說/相傳」的來源禁進 footnote、禁進引號**——改轉述。
   逐字引語只用 research 標「Ctrl-F 可驗 ✓」的。**禁自己長新引語**（REFLEXES #31：writer 幻覺引語）。
8. **富文本**：開頭 `> **30 秒概覽：**` 一段；3-5 個 callout（策展人筆記/你知道嗎/數字解讀，型錄見
   EDITORIAL）穿插不擠一起；media manifest 的在庫圖 `![alt](/article-images/…)` 分置對應節。
9. **幻覺護欄（本篇 research §幻覺護欄清單，違反=整篇降級）**：{GUARDS}
10. **深度外連不複製**：deep sibling 各有專文，本篇每節點給一個 facet + link，不重寫：{CROSSLINKS}

## 媒體（放這些在庫圖，絕對路徑去 public 前綴）
{MEDIA}

## 輸出（鐵律）
- {MODE}=Evolution：用 **Write** 寫到 `{OUT_PATH}`（staging 全新檔，**不碰 knowledge/**，零舊文感染面）。
  {MODE}=Fresh：可直接寫 canonical。
- 字數 ≥ {WORDFLOOR} CJK（別灌水但要夠縱深）。
- final message 結構：**先讀取回執**（見第 0 步）→ 再 3-5 bullet（字數/footnote 數/用了哪些護欄修正/
  哪節最花力氣）。檔案結尾不寫任何「已完成/policy」元敘述。

## Anti-examples（別學）
{ANTI_EXAMPLES}
```

---

## Anti-example 庫（spawn 時挑 ≥2 條貼進 {ANTI_EXAMPLES}）

| #   | 案例                                                   | 一句話病灶（貼這段）                                                                                                                                                             |
| --- | ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | 不讀 report 只吃 fact-pack（2026-06-15）               | orchestrator 把 report 二次摘要成精簡 fact-pack 塞 prompt、又叫 writer 別讀 report → raw texture 全漏 → 哲宇 callout「難怪最近文章都變爛」。你**必須親讀 §8 raw**，§6 只是導航。 |
| 2   | 編年體小標題（Cicada/草東/康士坦）                     | 12-15 次搜尋的音樂人批次，小標題淪為「1993 年」「2005 年」時間軸，過 format-check 卻讀成維基。每節要一個場景/意象 anchor。                                                       |
| 3   | writer 自長幻覺引語（2026-06-01 賈樟柯）               | writer agent 自報全綠，主 session spot-check 抓到它**自己新長出一句杜撰引語**（cited source 無此句）。引語只能用 research 標「Ctrl-F 可驗 ✓」的。                                |
| 4   | 對位句氾濫（2026-07-12 茶文化 v0）                     | 「珍奶不是飲料，是台灣的軟實力」這種句子密度一高就是 AI 水印。改直接正面斷言。單篇對位句 ≤ 2。                                                                                   |
| 5   | skim EDITORIAL 只讀規則不讀範例（CLAUDE.md §神經迴路） | 「截斷式必讀是 bug」——AI 讀抽象規則但沒讀 Before/After 範例 → 寫作退化成規則的線性排列。讀 EDITORIAL 要含範例段。                                                                |

**庫的維護**：新的 writer 病例先進 [LESSONS-INBOX](../semiont/LESSONS-INBOX.md) 走 distill，確認新 pattern 才 append（先 grep 本表 + REFLEXES，covered 就 bump——per feedback_lessons_dna_check_first）。

---

_v1.0 | 2026-07-12-135710-twmd-tea-panorama session — 誕生觸發：哲宇 callout「派發寫作的 opus writer prompt 也模板化…他又不完整讀取 rewrite-pipeline / editorial 了 很糟糕 一直飄移」。姊妹：RESEARCH-AGENT-PROMPT.md（研究端標準化）＋ REWRITE-PIPELINE v7.11 Step 1.7.4（研究合成單檔）。_

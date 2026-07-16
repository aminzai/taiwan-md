---
title: '新聞台架構 — REWRITE pipeline 索引化 × 階段狀態層 × 公開編輯台設計'
description: 'REWRITE-PIPELINE v9 拆為薄索引＋自足 stage contract 檔（小 context model 可逐步執行）、per-article 階段狀態推導層、公開唯讀共享編輯台（/semiont/newsroom）、編輯室對抗迴路與總編 agent — 2026-07-16 哲宇 goal directive 完整設計'
type: 'design'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-07-16
last_session: '2026-07-16-newsroom-orchestration'
related:
  - 'newsroom-design-conversation-digest-2026-07-16.md'
  - 'projection-stage-design-2026-07-13.md'
  - 'editorial-room-adversarial-design-2026-07-15.md'
  - 'rewrite-pipeline-v5-stage-spine-design-2026-05-11.md'
  - 'rewrite-agent-dispatch-diagnosis-2026-07-05.md'
---

# 新聞台架構設計 — pipeline 索引化 × 狀態層 × 公開編輯台

> 觸發：哲宇 2026-07-16 goal directive ＋ 睨對話（[digest](newsroom-design-conversation-digest-2026-07-16.md)）。
> 哲宇補充 directive（同日）：「公開站前台是可以看到這個編輯台的，這樣才有建立的意義。
> 有點像是一個共享編輯台，第一階段唯讀；我本地端用的時候是我操作 AI，
> 編輯台反映現況（直接分析 md／資料夾／記憶等）。」

## 〇、TL;DR

五個子目標，一個共同架構：

| #   | 哲宇要的                                                | 架構解                                                                                                                                             |
| --- | ------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | REWRITE-PIPELINE 變索引，每步驟一個獨立 subagent 可執行 | v9：主檔瘦成 router，每 stage 拆自足 contract 檔到 `docs/pipelines/rewrite/`，小 context model 讀一個檔就能跑一步                                  |
| 2   | 文章各階段有清楚資料夾分類，不必一次寫完                | 階段產物資料夾已半成形（research／projection／editorial-room／evolve staging），補一層 per-article 狀態推導：從檔案本身推 stage 進度，可暫停可續跑 |
| 3   | Trello 式看板：每篇在哪、產出什麼、缺什麼、怎麼推進     | `generate-newsroom-data` 生成器掃描全部階段產物 → `dashboard-newsroom.json` → 公開頁 `/semiont/newsroom`；本地重跑生成器即反映現況                 |
| 4   | 編輯室自動化                                            | 編輯室 runner contract（分席 spawn → 收件 → health gate 一條龍）＋ 記者答辯一輪（睨的 GAN 迴路）＋ 總編 agent（成品層平行探針對抗總評）            |
| 5   | 思考脈絡公開 beta                                       | `/semiont/newsroom/{slug}`：投影論點、編輯室各席意見與主編裁決渲染成對話（爭議過程），資料全部來自已公開的 repo 檔案                               |

核心判斷：**執行基座已經活著**（Harvest 駕駛艙 7/12 已讓 GPT-5.6 Sol 跑完整條 pipeline 並被
strict verifier 攔過一次假陰性；編排理論在 REWRITE §多 agent 編排 9 條鐵律已成熟），
缺的是三層薄薄的接線：契約層（stage 檔）、狀態層（推導）、呈現層（公開編輯台）。

---

## 一、現況（四路偵察結論，證據見各報告）

### 1.1 Pipeline 本體

`docs/pipelines/REWRITE-PIPELINE.md` 2606 行。已經是「薄索引＋自足檔」的部分：
投影層（PROJECTION.md / EDITORIAL-ROOM.md / EDITORIAL-ROOM-PROMPTS.md）、
PERSONA-PIPELINE、RESEARCH-AGENT-PROMPT、WRITER-PROMPT、FACTCHECK-PIPELINE——
主檔對它們只留「誰做／輸入／輸出／gate／pointer」骨架。

還是大段 inline 教學文的部分：Stage 0（465 行）、Stage 1（613 行，最大單體）、
Stage 3（220 行）、Stage 4（350 行，含 `#### Step 4.3.6` 編號撞號 bug：RP:2139 圖片健檢
與 RP:2155 影片 iframe 同號）。Changelog 64 行純歷史敘事。

### 1.2 階段產物與狀態

| 階段                     | 產物落點                                                     | 隱式狀態欄位                                          |
| ------------------------ | ------------------------------------------------------------ | ----------------------------------------------------- |
| Stage 0-1                | `reports/research/{YYYY-MM}/{slug}.md`（＋sibling agent 檔） | frontmatter `stage: 0-1-complete`、`viewpoint_formed` |
| Step 2.0                 | `reports/article-projection/{slug}.md`                       | `projection_done: true`                               |
| Step 2.0-R / 2.5-R / 3.6 | `reports/editorial-room/{slug}-*.md`                         | `overall: pass/revise/block`、`rounds`                |
| Stage 2 staging          | `reports/article-evolve/{slug}.md`                           | 檔案存在與否                                          |
| Stage 3.5/3.6            | `reports/research/{YYYY-MM}/{slug}-stage3{5,6}-audit.md`     | `## Result: PASS/FAIL`                                |
| Ship                     | `knowledge/{Cat}/{slug}.md`                                  | frontmatter `researchReport`、`relatedDiary`          |
| Intake / Log             | `docs/semiont/ARTICLE-INBOX.md` / `ARTICLE-DONE-LOG.md`      | `Status: pending/in-progress/done`                    |

沒有統一的 per-article 狀態檔；狀態散在六種檔案的 frontmatter 與正文。
`.lang-sync-tasks/`（manifest.json ＋ per-task JSON 含 sha 校驗）是「主 session 預處理、
sub-agent 按 task 檔執行」的現成模式。

### 1.3 執行基座（Harvest）

`docs/semiont/harvest/`：Astro＋Solid UI（launch.json port 4321）＋ Bun/SQLite backend。
現役（7/15 還有阿神、台灣藍鵲任務卡）。已有：task 狀態機
（pending→spawning→in-progress→blocked→done→failed→retired→awaiting-cheyu）、
per-spawn worktree 隔離、engine/model 鎖定（codex × gpt-5.6-sol）、
`strict-rewrite.ts` 八關 verifier（呼叫 research-report-health / article-health /
audit grep / status.log receipts）。7/12 Sol 首跑教訓：verifier 靠檔名 pattern 猜狀態
→ 假陰性 → **狀態要 ground 在顯式路徑，不猜命名**。

### 1.4 編輯室與公開面

編輯室今天全手動（主 session 逐席 copy-paste prompt spawn）；`editorial-room-health.py`
只驗 schema。公開面已有可抄模式：`relatedDiary` frontmatter → `RelatedDiaries.astro`
（「寫這篇文章時，Semiont 在想什麼」）、`semiont-diary.ts` parser lib（md 目錄→公開頁）、
changelog（git log→JSON→頁面）、`staticRoutes.ts` filesystem-derive（新頁面免登記）、
dashboard JSON SOP（REFLEXES #43：generator 掛進 refresh-data.sh，Step 11 freshness gate 抓漏）。
`reports/editorial-room/` 與 `reports/article-projection/` 目前站上零渲染。

---

## 二、為什麼「現在拆檔」是對的（v3.1 反例的正面回答）

2026-05-09 v3.0→v3.1 拆過 6 sub-canonical，隔天收回：當時單一 session 線性跑完全部
stage，拆檔逼它跳檔 6-7 次、每跳一次 context 沖掉（[v5 設計報告](rewrite-pipeline-v5-stage-spine-design-2026-05-11.md) §核心錯誤歸因）。

今天讀者拓撲已經反轉：v6.3 起主 session 是 orchestrator 不當 writer，每個 stage 本來就派
乾淨 context 的 sub-agent。在這個拓撲下：

- **stage 檔＝sub-agent 的天然投餵單位**。執行者讀一個檔，零跳檔。v3.1 的病（單一讀者
  random access）不存在，因為沒有任何執行者需要讀兩個以上的 stage 檔。
- **orchestrator 只需要索引**：spine、Hard Gate Inventory、派發表。這三張表今天就已經
  是主檔裡「真正的 router 邏輯」（合計 ~150 行）。
- **小 context model 因此可用**：哲宇的原始動機。一個 stage 檔＋該 stage 宣告的輸入檔
  ＝該執行者的全部世界。context 需求從 2606 行降到單檔幾百行。

### 設計鐵律（從 15 條歷史失敗模式萃取，違反任一條＝重蹈覆轍）

1. **index 薄、stage 檔自足**：stage 檔必須讓沒讀過主檔的執行者完成該步。
   pointer 只指向「執行時必須完整 Read 的 canonical」（如 EDITORIAL.md），不指向兄弟 stage。
2. **零複寫**（殼核不對稱病，WRITER-PROMPT v1.0 教訓）：craft 規則住 editorial canonical，
   stage 檔對它是「必讀清單＋read-receipt」，不抄內容。
3. **contract 帶 anti-example**（茶文化 84 條來源行 35% 帶 URL 教訓）：規則文字防不了
   詮釋漂移，❌✅ 對照表才防得住。
4. **交接點儀器化**（柯智棠收件 gate 教訓）：每個 stage 的 OUTPUT 都有可執行驗收指令，
   寫進 contract 的 GATE 段；下一 stage 的 INPUT 檢查上一 stage 的 gate 結果。
5. **狀態 ground 在顯式路徑**（Sol 假陰性教訓）：manifest 記錄實際檔案路徑，
   任何工具不做檔名 pattern 推測。
6. **薄殼要有防再增厚的尺**（PERSONA inline 副本漂一年、mirror 厚殼債教訓）：
   拆完就造 lint（主檔行數上限＋「stage 檔不引用兄弟 stage」檢查），掛 pre-commit 或週檢。
7. **拆檔當下順手修**：Step 4.3.6 撞號、Stage 3.3 profile 邊界明示（v6.1 漏跑教訓：
   每個 stage 檔明寫自己跑哪個 profile）。
8. **儀器化三盞燈**：canonical（stage 檔）＋可跑的尺（gate 工具）＋開機必讀（boot 層指標）。
   缺第三盞＝合法繞過（AAMA 教訓）。

---

## 三、架構總覽

```
╭─────────────────────────────────────────────────────────────────────╮
│  契約層（docs/pipelines/）                                            │
│    REWRITE-PIPELINE.md v9  ←  薄索引：spine + Hard Gate Inventory    │
│                                + 派發表 + mode 判定 + cron           │
│    rewrite/STAGE-*.md      ←  每 stage 自足 contract（執行者單位）    │
│                                                                      │
│  執行層（誰來跑一個 stage）                                           │
│    a. 主 session Agent tool spawn（手動 session，現行主路徑）         │
│    b. Harvest spawner per-stage dispatch（跨 model：Sol/Grok/…）      │
│    c. cron routine（單 session 順讀 stage 檔逐步跑）                  │
│                                                                      │
│  狀態層（scripts/tools/ + public/api/）                               │
│    generate-newsroom-data.py  ←  掃描階段產物推導狀態（derive-first） │
│    dashboard-newsroom.json    ←  per-article：stage × 產物 × gate     │
│                                                                      │
│  呈現層（src/pages/）                                                 │
│    /semiont/newsroom          ←  公開唯讀共享編輯台（kanban）          │
│    /semiont/newsroom/{slug}   ←  making-of：投影論點＋編輯室爭議過程   │
╰─────────────────────────────────────────────────────────────────────╯
```

資料流一句話：**檔案是唯一真相**。stage 執行者寫產物檔（含 frontmatter 狀態欄），
生成器掃檔案推導看板，公開頁渲染看板。沒有第二本帳（避免 #82 proxy signal：
看板永遠反映檔案現況，不反映誰宣稱做了什麼）。

---

## 四、契約層：REWRITE-PIPELINE v9

### 4.1 主檔（薄索引，目標 ≤ 450 行）

保留（本來就是 router 邏輯）：frontmatter＋第一性原理、ASCII spine（升級標注每 stage 的
contract 檔）、Hard Gate Inventory（加一欄「contract 檔」）、多 agent 編排表＋9 鐵律
（濃縮為規則清單，敘事移 stage 檔背景段）、mode 判定（0.1 derive tree ＋ 4 模式速判）、
何時全編排 vs 自跑、跨檔案職責分工、cron 段、品質分級。

移出：各 stage 操作細節（→ stage 檔）、changelog 19 段敘事（→ git log ＋
`reports/archive/rewrite-pipeline-changelog-pre-v9.md` 快照）、觸發背景敘事
（→ 各 stage 檔「背景」附錄段）。

### 4.2 stage contract 檔（`docs/pipelines/rewrite/`）

拆檔清單（10 檔，對應現行行號範圍搬移，內容 verbatim 為主、只改結構）：

| Contract 檔                    | 來源                                        | 執行者（現行編排表）                      |
| ------------------------------ | ------------------------------------------- | ----------------------------------------- |
| `STAGE-0-VIEWPOINT.md`         | RP Stage 0 全段（273-737）                  | 主 session 或 1 Opus agent                |
| `STAGE-1-RESEARCH.md`          | RP Stage 1 主幹（740-1123）                 | orchestrator＋N Sonnet fan-out            |
| `STAGE-1-MEDIA.md`             | RP Step 1.9 全段（1124-1352）               | orchestrator（授權判斷 human）            |
| `STAGE-2.0-PROJECTION.md`      | RP 1370-1426（薄，craft 在 PROJECTION.md）  | 主 session Opus，不派寫手                 |
| `STAGE-2.0R-EDITORIAL-ROOM.md` | RP 1389-1412 ＋ runner SOP（新）            | 3 seats＋主編                             |
| `STAGE-2-WRITE.md`             | RP Stage 2 主幹（1356-1664）                | 1 fresh Opus writer（WRITER-PROMPT 填槽） |
| `STAGE-2.5-SOURCE-FIDELITY.md` | RP 1666-1679 ＋ 2.5 比對覆蓋                | 主 session＋可選 fact-check agent         |
| `STAGE-3-VERIFY.md`            | RP Stage 3（1680-1899，含 3.6 fan-out SOP） | 主 session＋M Sonnet verifier             |
| `STAGE-4-FORMAT-MEDIA.md`      | RP Stage 4（1902-2251，修撞號 4.3.6→4.3.7） | 主 session                                |
| `STAGE-5-CROSSLINK.md`         | RP Stage 5（2254-2419）                     | 主 session                                |

### 4.3 contract 檔統一骨架（七段）

```markdown
---
title / description / type: 'pipeline-stage-contract' / parent_canonical: REWRITE-PIPELINE.md
stage_id / 執行者 tier / context 預算（執行本檔需要的輸入總量級）
---

## ROLE 本 stage 一句話職責＋在整條鏈的上下游位置

## INPUTS 必讀檔案清單（顯式路徑）＋前置 gate 通過證明

## PROCEDURE 操作步驟（從主檔 verbatim 搬移）

## OUTPUTS 產物檔顯式路徑＋frontmatter 狀態欄要求

## GATES 可執行驗收指令（逐字）＋不過的後果

## HANDOFF 回報格式＋「更新看板：跑生成器」＋下一 stage 是誰

## ANTI-EXAMPLES ❌✅ 對照（從主檔教訓敘事蒸餾）
```

`type: 'pipeline-stage-contract'` 進 ANATOMY frontmatter taxonomy（check-canonical-frontmatter
同步認得）。context 預算欄直接回答「哪些 model 跑得動這步」。

### 4.4 防再增厚的尺

`scripts/tools/pipeline-shell-lint.py`（或併入 counts-drift）：主檔行數 ≤ 500 WARN；
stage 檔內 grep 兄弟 stage 檔名＝WARN（不准橫向依賴）；stage 檔缺七段之一＝FAIL。
掛 self-evolve-weekly。

---

## 五、狀態層：derive-first 編輯台資料

### 5.1 原則

哲宇 directive「直接分析 md／資料夾／記憶」＝ derive-first：**不建第二本帳**。
狀態由生成器每次全量掃描推導；唯一新增的持久欄位是既有 frontmatter 已在用的那些
（`projection_done`、`overall`、`stage`……），缺的補齊規範而不是另立 state DB。
（Harvest 的 task.yml/SQLite 是「執行排程」帳，管 spawn 生命週期；編輯台是「產物階段」帳，
管文章走到哪。兩本帳各司其職，生成器可以順讀 `.harvest/tasks/` 附註「執行中」訊號。）

### 5.2 `scripts/core/generate-newsroom-data.py`

掃描來源 → 每篇文章推導一列：

1. `docs/semiont/ARTICLE-INBOX.md`：pending/in-progress entries（intake 欄）
2. `reports/research/*/{slug}.md` frontmatter＋`{slug}-stage3{5,6}-audit.md` Result
3. `reports/article-projection/{slug}.md` frontmatter
4. `reports/editorial-room/{slug}-*.md` frontmatter（room／overall／rounds／seats）
5. `reports/article-evolve/{slug}.md` 存在＋mtime
6. `knowledge/{Cat}/{slug}.md` frontmatter（researchReport 反查、relatedDiary、date）
7. `docs/semiont/ARTICLE-DONE-LOG.md` 近期完成列
8. （訊號）`.harvest/tasks/` 未結案卡、`docs/semiont/memory/` 近 7 天 rows 提及的 slug

輸出 `public/api/dashboard-newsroom.json`：

```json
{
  "generated": "…",
  "articles": [
    {
      "slug": "尊",
      "title": "…",
      "category": "People",
      "mode": "EVOLVE",
      "priority": "P0",
      "spine_type": "立體群像",
      "stages": {
        "viewpoint": {
          "status": "done",
          "artifact": "reports/research/2026-07/尊.md",
          "gate": "PASS",
          "at": "…"
        },
        "research": { "status": "done", "artifact": "…", "gate": "PASS" },
        "projection": {
          "status": "done",
          "artifact": "reports/article-projection/尊.md"
        },
        "room_projection": {
          "status": "pass",
          "rounds": 2,
          "artifact": "reports/editorial-room/尊-projection-review.md"
        },
        "write": {
          "status": "staged",
          "artifact": "reports/article-evolve/尊.md"
        },
        "room_prose": { "status": "pass", "artifact": "…" },
        "verify": { "status": "done", "stage35": "PASS", "stage36": "PASS" },
        "ship": { "status": "done", "artifact": "knowledge/People/尊.md" }
      },
      "next_step": null,
      "blocked_on": null,
      "sessions": ["2026-07-15-191335-manual"]
    }
  ]
}
```

`next_step` 由 stage 順序表推導（第一個非 done 的 stage）；`blocked_on` 由 gate FAIL／
editorial-room block 推導。**不做檔名猜測**：research report 路徑從 knowledge frontmatter
`researchReport` 與 INBOX `Pre-research` 欄取顯式值，slug 對映表遇到歧義列 `warnings[]`
而不是硬配。

### 5.3 接線（REFLEXES #43 SOP）

生成器掛 `package.json` prebuild:dashboard 子鏈＋`refresh-data.sh` 新編號步驟
（Step 11 freshness gate 自動看守）。本地：任何 stage HANDOFF 段的最後一步就是
「`python3 scripts/core/generate-newsroom-data.py`」——AI 推進一步，編輯台跟著動；
哲宇本地 dev server 重整就看到現況。

---

## 六、編輯室自動化 → 新聞台

### 6.1 編輯室 runner（把手動五步變一步）

`STAGE-2.0R-EDITORIAL-ROOM.md` contract 內建 runner SOP：讀 EDITORIAL-ROOM-PROMPTS 填槽
→ 平行 spawn seats → 收件落檔 → `editorial-room-health.py` → 主編（永遠主 session）裁決
→ 更新看板。約束不動：主編不派 agent、必改 ≤7、材料桌禁假社群、block 兩輪升級觀察者。

### 6.2 記者答辯一輪（睨的 GAN 迴路，有界版）

現行：席位單向出意見 → 主編裁決。新增：席位 verdict 為 revise/block 時，**寫方
（投影作者或 writer）得到一次答辯**——對每條必改回「接受修改」或「捍衛選點（附理由）」，
主編看攻防後裁決。上限一輪（防迴圈燒 token）。答辯記錄進 review 檔新段
`## 攻防`（結構化：challenge / defense / ruling 三欄）——這正是公開視覺化要的爭議過程。

### 6.3 總編 agent（新 gate：Step 3.7 總編對抗總評）

睨：「總編是平行的漣漪出去，檢驗連結關係和脈絡構成一個主軸。」哲宇：「需要總編輯
獨立一個 agent 用對抗性方式總評標題觀點性與整篇脈絡。」

實作為成品層新 contract（併入 `STAGE-3-VERIFY.md` 尾段，A 級／大眾文 HARD，與 3.6 同 round）：

- **平行探針 fan-out**（Sonnet ×4-5，各自乾淨 context、falsification prompt）：
  ① 標題／description 觀點兌現探針（門面句承諾的觀點，正文中段有沒有賺到）
  ② 逐段主軸服務探針（每個 H2 段對投影 echo map 的扣回，抓「京都研究」式斷裂）
  ③ H2 載體還原探針（主述賓還原＋可指載體，EDITORIAL §小標題）
  ④ 連結成網探針（footnote／cross-link／延伸閱讀是否構成支撐主軸的網，或只是裝飾）
  ⑤（政治敏感題加開）立體地愛探針（MANIFESTO §13）
- **匯流**：主 session 收五路探針落檔 `reports/editorial-room/{slug}-chief-review.md`
  （沿用 room schema，room: chief），主編裁決 ≤7 必改。
- 與 2.5-R 的分工：2.5-R 驗「正文有沒有執行藍圖」（對圖施工驗收），總編驗「成品作為
  一篇報導成不成立」（不看藍圖、只看成品＋標題，模擬冷讀者總編）。互補不重複。

---

## 七、呈現層：公開唯讀共享編輯台

### 7.1 `/semiont/newsroom`（kanban 總覽）

- 資料：build-time import `dashboard-newsroom.json`（speciation.astro 模式）。
- 欄位＝stage（Inbox → 觀點 → 研究 → 投影 → 編輯室 → 寫作 → 驗證 → 總編 → Ship），
  卡片＝文章：分類徽章、mode、priority、各 stage 燈號、產物連結（連 GitHub blob）、
  `next_step`、`blocked_on`。
- 唯讀第一階段；頁尾標 beta＋一句「這是 Taiwan.md 的共享編輯台：每篇文章怎麼被想、
  被吵、被驗，全部攤在這裡」。
- zh-only 起步（semiont 子頁慣例），`staticRoutes.ts` 自動收錄，免登記。
- 曝光內容邊界：全部素材本來就在公開 repo，站上渲染沒有新增揭露面；但研究報告
  §維護者校準備忘錄（私有素材拍板）依 Step 1.6 本來就不落公開細節，維持不變。

### 7.2 `/semiont/newsroom/{slug}`（making-of：思考脈絡）

- parser lib `src/lib/semiont-newsroom.ts`（抄 semiont-diary.ts 骨架）build-time 解析：
  投影檔（論點／骨架／減法）、editorial-room 檔（席位意見＋攻防＋裁決）、audit 結果、
  relatedDiary。
- 渲染成時間軸＋對話：席位發言以「思考泡泡」樣式呈現（睨對話裡的 UX 種子），
  攻防段落 challenge／defense／ruling 三色排版——爭議過程就是主角。
- 文章頁掛回：既有 RelatedDiaries 區塊旁補一行「這篇文章的編輯台紀錄 →」
  （有 newsroom 資料的文章才渲染，presence-based，不加新 frontmatter 欄）。

### 7.3 本地＝同一個面

哲宇本地：dev server 開同一頁；AI 每推進一個 stage，HANDOFF 跑生成器，重整即現況。
不另建本地專用 UI（Harvest 駕駛艙繼續當「派發／排程」面板，編輯台是「產物階段」面板，
兩者互補；phase 2 若要在編輯台上加操作鈕，走 Harvest backend API，公開版維持唯讀）。

---

## 八、落地順序

| Phase   | 內容                                                                                  | 驗收                                                                                  |
| ------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| **C1**  | v9 拆檔（worktree 內原子完成）：10 stage 檔＋主檔瘦身＋撞號修正＋shell lint           | 主檔 ≤500 行；`git grep` 驗證零內容遺失（逐段對賬）；pre-commit 過                    |
| **C2**  | `generate-newsroom-data.py`＋prebuild／refresh-data 接線                              | 對現役文章（尊／阿神／Shopping-Design／AAMA）推導出正確 stage 狀態；warnings 機制動作 |
| **C3**  | `/semiont/newsroom` kanban 頁                                                         | build 過＋本地 dev 目視；卡片連結全通                                                 |
| **C4a** | 編輯室 runner contract＋攻防段 schema＋總編探針 contract                              | 下一篇 depth 文 dogfood                                                               |
| **C4b** | `/semiont/newsroom/{slug}` making-of 頁                                               | 用尊／Shopping-Design 既有編輯室檔渲染出爭議過程                                      |
| 後續    | Harvest per-stage 派發（quick-preset 每 stage 一鍵）、多 model stage 實驗、看板互動化 | 另開 session                                                                          |

風險與對策：

- **今晚 cron**（twmd-rewrite-daily 18:00／babel 00:33）讀主檔：C1 在 worktree 原子 ship，
  拆檔前後 Hard Gate Inventory 與 spine 錨點保持可 grep；ship 後跑一次
  `routine-sync-check`＋grep skills mirror 確認無死鏈。
- **內容遺失**：拆檔以 verbatim 搬移為預設，主 session 逐 stage 對賬行數守恆
  （REFLEXES #38 line conservation 變體）。
- **>50 檔邊界**：本次新增＋修改約 20-25 檔，未觸及；公開 beta 頁上線前哲宇過目
  （對外呈現語氣屬品牌層）。

## 九、留給哲宇的決策（不擋工，預設先行）

1. 編輯台公開路徑：預設 `/semiont/newsroom`（zh-only beta）。若要更前台（navbar／首頁入口）你拍板。
2. 總編 gate 觸發面：預設 A 級／大眾文 HARD、standard WARN。要不要全量 HARD 你定。
3. 記者答辯輪數：預設 1 輪封頂。
4. 睨的延伸實驗（辯論審美分類、議題頁彈幕）：已落 digest 備查，不進本次 scope。

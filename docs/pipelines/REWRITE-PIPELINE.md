---
title: 'REWRITE-PIPELINE'
description: '文章改寫主流程薄索引（v9.0 router）— spine / Hard Gate Inventory / 多 agent 編排 / stage contract 派發表；各 stage 操作細節住 REWRITE-STAGE-*.md contract 檔（執行者只讀一個 contract 即可跑一步）'
type: 'pipeline-canonical'
status: 'canonical'
current_version: 'v9.0'
last_updated: 2026-07-16
last_session: '2026-07-16-newsroom-orchestration（v9.0 索引化：10 個 REWRITE-STAGE-*.md contract 檔 verbatim 拆出，行數守恆 2606=2118+424+64；主檔瘦身為 router；設計 reports/newsroom-orchestration-design-2026-07-16.md）'
plugin_check: 'python3 scripts/tools/article-health.py {file} --profile=rewrite-stage-4'
sister_docs:
  - 'EVOLVE-PIPELINE.md'
  - 'FACTCHECK-PIPELINE.md'
  - 'TRANSLATION-PIPELINE.md'
  - 'SQUEEZE-MODELS-MAX-PIPELINE.md'
  - 'PEER-INGESTION-PIPELINE.md'
  - 'MEMORY-PIPELINE.md'
  - 'DIARY-PIPELINE.md'
  - 'RESEARCH-AGENT-PROMPT.md'
  - 'WRITER-PROMPT.md'
upstream_canonical:
  - '../semiont/MANIFESTO.md'
  - '../semiont/DNA.md'
  - '../editorial/EDITORIAL.md'
  - '../editorial/PROJECTION.md'
---

# REWRITE-PIPELINE.md — 文章改寫主流程 v9.0（薄索引）

> **第一性原理**：所有文章都走同一條 6-stage pipeline，每篇都跑過。模式判定 + 編輯前思考收斂在 **Stage 0 觀點**（Step 0.1-0.6），Stage 1 變純取材，Stage 2-5 完全 mode-agnostic。
>
> **翻譯不在本 pipeline scope** — 本 pipeline 100% 預算給中文版產出。多語版本由獨立的[巴別塔 pipeline](SQUEEZE-MODELS-MAX-PIPELINE.md) 負責。
>
> **v6.0 新增 Stage 0 觀點**（2026-05-11 admiring-montalcini）：在搜尋之前先以總編輯視角想清楚「對台灣人是什麼樣的記憶 / 多元面貌 / 想法感受 / 歷史脈絡 / 社會關聯 / 類型專屬問題」六個核心問題，產出 §觀點成型 落 research report。原 Stage 1 模式判定 + 萃取舊素材 + 載入方法論（Step 1.1-1.5）移到 Stage 0，原 Stage 1 Step 1.6-1.14 重編為 1.1-1.9。**翻轉 AI 寫作標準失敗模式**：從「搜尋發現事實 → 補丁觀點」變「先想觀點 → 帶問題去搜尋」。觸發：哲宇 2026-05-11 callout「重點在溫度 / 人味 / 故事 / 策展 / 觀點 / 體驗 / 與社會歷史環境跟我們人生的關聯」。
>
> v5.0 設計理由：[reports/rewrite-pipeline-v5-stage-spine-design-2026-05-11.md](../../reports/rewrite-pipeline-v5-stage-spine-design-2026-05-11.md)。

---

## 🗺️ ASCII spine

```
╭──────────────────────────────────────────────────────────────────────────╮
│              REWRITE-PIPELINE 6 階段 — 每篇都跑同一條                    │
│                                                                          │
│   Stage 0: 觀點 ─→ 6 steps（編輯前思考 + 模式判定）⭐ v6.0 新增          │
│            ├── Step 0.1 模式識別 [Fresh/Evolution/Merge/Boundary]        │
│            ├── Step 0.2 既有素材萃取（EVOLVE only）                       │
│            ├── Step 0.3 選 canonical（Merge variant only）                │
│            ├── Step 0.4 範圍切片表（Boundary variant only）               │
│            ├── Step 0.5 載入研究方法論 + 模板                             │
│            └── Step 0.6 觀點成型 🎬 (HARD GATE)                          │
│              ↳ Hard gate: §觀點成型落檔 + viewpoint_formed: true         │
│                                                                          │
│   Stage 1: 取材 ─→ 9 steps（純搜尋，帶 Stage 0 問題去驗證）              │
│            ├── Step 1.1 搜尋深度 ≥ 80                                    │
│            ├── Step 1.2 結尾素材鎖定                                      │
│            ├── Step 1.3 重複偵測                                          │
│            ├── Step 1.4 找矛盾鎖定（收斂 Stage 0.6 核心矛盾候選）         │
│            ├── Step 1.5 問觀察者要一手素材                                │
│            ├── Step 1.6 私有 SSOT 觀察者拍板（條件式）                    │
│            ├── Step 1.7 研究報告必存                                      │
│            ├── Step 1.8 Spawn agent 選型                                  │
│            └── Step 1.9 媒體素材研究 🎬 (HARD GATE)                      │
│              ↳ Hard gate: 報告落檔 / 媒體三表                            │
│                                                                          │
│   ── 投影 (Projection) ── 研究 → 投影邏輯 → 文章 的中間層 ⭐ v8.0 ──     │
│   Step 2.0: 投影藍圖 ─→ 論點 + 骨架 + 減法 + echo map 🎬 (HARD GATE)     │
│            ├── 論點（有張力、要被賺到，非摘要）                          │
│            ├── 骨架（動作序列，過 shuffle test，非面向巡禮）             │
│            ├── 每 section 雙重職責（局部承載 + 全局功能 + 扣回主軸）     │
│            └── 減法（明列砍什麼）+ echo map（每段押韻主軸錨）            │
│              ↳ Hard gate: 藍圖落檔 reports/article-projection/ + 5 題    │
│              ↳ canonical: docs/editorial/PROJECTION.md                   │
│   Step 2.0-R: 投影編輯室 ─→ 乾淨 context 分席審 🎬 (depth HARD) ⭐ v8.1 │
│              ↳ reports/editorial-room/ + editorial-room-health.py        │
│              ↳ canonical: docs/editorial/EDITORIAL-ROOM.md               │
│                                                                          │
│   Stage 2: 寫 ──→ 8 steps（照投影藍圖執行，不重排結構）                  │
│            ├── Step 2.1-2.6 結尾先行 → 開場 → 小標題 → 正文 → 延伸      │
│            ├── Step 2.7 7 條自檢（含 Title 三明治 🥪 + 媒體 spine 🎬）  │
│            └── Step 2.8 富文本 + footnote 密度                           │
│              ↳ Hard gate: 10 條                                          │
│   Step 2.5-R: 正文結構編輯室 ─→ 論點兌現對抗 ⭐ v8.1                    │
│                                                                          │
│   Stage 3: 驗 ──→ 6 steps（3.1-3.5 草稿驗 + 3.6 成品總驗）⭐ v7.0       │
│            ├── Step 3.1-3.4 塑膠 / 鐵三角 / FACTCHECK / story atom       │
│            │     └── Step 3.3 跑 rewrite-stage-3-5 profile gate（plugin 以 --list-checks 為準）│
│            │         (footnote-format + footnote-density，v6.1 新增)     │
│            ├── Step 3.5 Title+desc spine sync re-check 🥪                │
│            └── Step 3.6 成品總驗三關 🔍（原子重驗 fan-out + 順稿 +      │
│                視覺同步）— A 級/大眾文/勘誤後 HARD                       │
│              ↳ Hard gate: 0 dead-link / footnote canonical / 成品三關    │
│                                                                          │
│   Stage 4: 形 ──→ 3 steps（含 6 個媒體子點）                             │
│            ├── Step 4.1 article-health 7 維度                            │
│            ├── Step 4.2 多語 visual smoke                                │
│            └── Step 4.3 媒體插入（6 sub-step）                           │
│              ↳ Hard gate: hard=0 / image-health pass                     │
│                                                                          │
│   Stage 5: 連 ──→ 4 steps                                                │
│            ├── Step 5.1-5.3 掃描 / 雙向 / Sibling 預檢                   │
│            └── Step 5.4 (Merge variant only) Astro redirect 5 lang       │
│              ↳ Hard gate: format-structure / build verify                │
│                                                                          │
│   ✅ Article shipped (zh-TW canonical)                                   │
│                                                                          │
│   ──── 翻譯（跨 pipeline boundary，主權的巴別塔）────                    │
│   → SQUEEZE-MODELS-MAX-PIPELINE.md（多語 batch sync 主流程）             │
│   → TRANSLATION-PIPELINE.md（單篇翻譯）                                  │
╰──────────────────────────────────────────────────────────────────────────╯
```

---

## 為什麼 Pipeline 存在

**診斷（實戰觀察）**：

1. **Token 耗盡** → 後半段變草稿
2. **沒有中間 checkpoint** → 品質無聲下滑
3. **結尾最後寫** → 精力不夠，結尾變罐頭（峰終定律）
4. **富文本被遺忘** → EDITORIAL 規範到後面沒人記得
5. **模式混淆** → 不同切入方式應該是同一條 pipeline 的不同 entry point，不該被當成獨立 pipeline
6. **觀點補丁化**（v6.0 新增）→ 搜尋發現事實 → 再臨時想觀點 → 編年體 / 密度失衡 / 結尾罐頭

**解法**：六階段分離 + **Stage 0 編輯前思考** + 結尾先行 + 後半段品質鎖 + Stage 2-5 統一不分模式。翻譯獨立到巴別塔 pipeline。

---

## 🚦 Hard Gate Inventory（一張表 audit 全 pipeline）

| Gate                                    | 觸發 stage | 條件                                                 | 工具                                                                                                                                                                                                                                                                                                                                                                                  | 不過 = ?                   |
| --------------------------------------- | ---------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------- |
| **§觀點成型落檔**                       | Stage 0 終 | depth article                                        | **`research-report-health.py {report} --stage 0`**（v7.7 兩件套：觀點成型 + viewpoint_formed + 六核心結構 ≥4/6 + 搜尋日誌 + ≥10 來源 proxy；**persona v7.7 移到研究後 Step 1.9.7，Stage 0 不要求**）。**缺 ≥20 探索 → ~0 來源 = FAIL**                                                                                                                                                | **不進 Stage 1**           |
| **persona 讀者缺口稽核** 🫂             | Stage 1 終 | depth article                                        | Step 1.9.7：20 persona 對研究報告補洞 + 增補 + 反向閥門；增補後重跑 research-report-health                                                                                                                                                                                                                                                                                            | 不進 Stage 2（漏讀者視角） |
| 核心矛盾鎖                              | Stage 1 終 | 所有 depth                                           | research report frontmatter manual                                                                                                                                                                                                                                                                                                                                                    | 不進 Stage 2               |
| 研究報告落檔                            | Stage 1 終 | depth ≥ 2000 字                                      | manual ls + frontmatter `researchReport`                                                                                                                                                                                                                                                                                                                                              | 不進 Stage 2               |
| **分部報告收件 gate** 📨                | Stage 1 中 | **每個研究 agent 回報、收到當下**                    | **`agent-report-health.py {file} --claimed {配額}`**（v7.8 儀器化 Step 1.8-bis 步 2：存放位置 repo 內 / 體積 ≥8KB / 逐條軌跡 section + ≥10 行 / 宣稱 vs 記錄比 / 五段結構 / ephemeral 引用 / **來源溯源率 ≥85%（v3：<60% hard，[Step 1.8-ter](REWRITE-STAGE-1A-RESEARCH.md#step-18-ter-研究-sub-agent-輸出契約來源逐條可溯v710-) 契約）**；壓縮嫌疑=FAIL，每條疑慮附為什麼+思考方向） | **不准開始合成 §6**        |
| **研究報告 SSOT health** 🔬             | Stage 1 終 | **所有 depth**                                       | `research-report-health.py --tier=depth`（distinct≥25 / en≠0 / 一手≠0 / 搜尋日誌 / 信度三層 / **v2 §8 有效密度 ≥120 + ephemeral pointer=0**；v2.1 疑慮通知層：每條 fail/warn 附為什麼+思考方向）                                                                                                                                                                                      | **不進 Stage 2**           |
| 媒體授權矩陣三表                        | Stage 1 終 | 所有 article（**含 EVOLVE**）                        | manual append research 檔末尾 + ls public/article-images/{cat}/                                                                                                                                                                                                                                                                                                                       | 不進 Stage 2               |
| **深度媒體掃描協議** 🔍🎬               | Stage 1 終 | **所有 depth（含 EVOLVE）**                          | [Step 1.9.0](REWRITE-STAGE-1B-MEDIA.md#step-190-深度媒體掃描協議hardv68-)：Chrome MCP rendered-DOM 圖掃（curl/WebFetch 對 JS-CDN 失效）+ YouTube 官方頻道影片掃；no-media 結論前必跑，落 §6 negative finding                                                                                                                                                                          | **不進 Stage 2**           |
| **投影藍圖** 📐                         | Stage 2 始 | **所有 depth**                                       | [Step 2.0](REWRITE-STAGE-2A-PROJECTION.md#step-20-投影藍圖v80-新增--研究--投影邏輯--文章-hard-gate)：落檔 `reports/article-projection/{slug}.md`，過 5 題（論點非摘要 / 骨架過 shuffle test / 每 section 有全局功能 / 減法非空 / echo map 覆蓋全篇）。canonical [PROJECTION.md](../editorial/PROJECTION.md)                                                                           | **不派寫手**               |
| **投影編輯室** 🏛️                       | Stage 2 始 | **depth EVOLVE/Fresh/A 級**                          | [Step 2.0-R](REWRITE-STAGE-2B-ROOM-PROJECTION.md#step-20-r-投影編輯室v81--編輯室對抗-hard-depth)：乾淨 context 分席（結構／減法／炎上）→ `reports/editorial-room/{slug}-projection-review.md` + `editorial-room-health.py`；[EDITORIAL-ROOM.md](../editorial/EDITORIAL-ROOM.md)                                                                                                       | **不派寫手**               |
| **正文結構編輯室** 🏛️                   | Stage 2 終 | **depth / A 級**                                     | [Step 2.5-R](REWRITE-STAGE-2E-ROOM-PROSE.md#step-25-r-正文結構編輯室v81)：正文是否執行藍圖全局功能／論點中段兌現；與 Step 3.6 事實包並列                                                                                                                                                                                                                                              | **不 ship**                |
| 五指 + 結構 + 塑膠 + 算術               | Stage 3    | 所有 article                                         | quality-scan + manual                                                                                                                                                                                                                                                                                                                                                                 | 不 commit                  |
| 事實鐵三角(算術/單位/引語)              | Stage 3    | 含金額/數字/引語                                     | python algebra + Ctrl-F                                                                                                                                                                                                                                                                                                                                                               | 不 commit                  |
| FACTCHECK Quick/Full Mode               | Stage 3    | 所有 article / A 級                                  | FACTCHECK-PIPELINE                                                                                                                                                                                                                                                                                                                                                                    | 不進 Stage 4               |
| **Citation plugin gate**                | Stage 3    | **所有 article（含 EVOLVE）**                        | article-health.py --profile=rewrite-stage-3-5 (footnote-format + footnote-density)                                                                                                                                                                                                                                                                                                    | **不進 Stage 4**           |
| **Title+desc spine sync**               | Stage 3    | **所有 article（含 EVOLVE）**                        | manual: title 冒號三明治 + desc 吃進核心矛盾                                                                                                                                                                                                                                                                                                                                          | 不 commit                  |
| **校正焦慮掃描** 🧱                     | Stage 3    | **callout-triggered EVOLVE**                         | Step 3.2-bis: backstop 自檢句 + grep 校正型句式 + 論點脊椎自檢                                                                                                                                                                                                                                                                                                                        | **不 commit**              |
| **Source-fidelity gate (Stage 2.5)** 🔬 | Stage 2.5  | **A 級 / fresh-writer EVOLVE 長文 / 含外部來源引用** | (1) fetch 被引用來源 artifact 逐字比對（WebFetch/curl，不只比 research report）(2) frontmatter title+desc+30 秒概覽 門面句 source-fidelity (3) fresh-writer 長文 fact-check agent pass（structure gate ≠ 事實對）                                                                                                                                                                     | 不覆蓋 canonical / 不 ship |
| **成品總驗三關** 🔍                     | Stage 3 終 | **A 級/大眾文/勘誤後/手術疊 ≥3 輪**                  | Step 3.6: 原子重驗 verifier fan-out（引號逐字 diff + 詮釋 gloss + footnote 綁定 + writer 自漂移）+ 順稿 + 視覺同步；修正 append research report §audit                                                                                                                                                                                                                                | 不 ship（已 ship 則 heal） |
| Format check 7 維度                     | Stage 4    | 所有 article                                         | article-health.py --profile=rewrite-stage-4                                                                                                                                                                                                                                                                                                                                           | pre-commit hook            |
| word-count ≥ 4500                       | Stage 4    | depth article                                        | article-health.py --check=word-count                                                                                                                                                                                                                                                                                                                                                  | pre-commit hook            |
| 多語 visual smoke                       | Stage 4    | i18n 改動                                            | 6 步 bash                                                                                                                                                                                                                                                                                                                                                                             | revert commit              |
| **媒體完整度低標** (length-scaled) 🎬   | Stage 4    | **depth article**                                    | `--profile=rewrite-stage-4`：image-health 媒體 ≥ **max(3, round(prose-CJK/1200))**（4500→4 / 7000→6 / 9000→8，HARD）+ media-richness ≥3 靜態圖 / People·Music·Nature ≥1 官方影片（WARN）+ paragraph-rhythm density **1.2–2.0 / 1k**（2026-07-12 哲宇 band 第三波上修 0.7→0.8→1.2–2.0，hard 2.5+median<55）。校準：複雜生活節 13 / 陳建年 1.48 帶內、text-only 失格                    | 不進 Stage 5               |
| Aspect ratio 護欄                       | Stage 4    | 涉及圖                                               | check-aspect.sh                                                                                                                                                                                                                                                                                                                                                                       | 換圖                       |
| **視覺化 viz-health** 📊🧱              | Stage 4    | 含 `tw-*` 資料模組                                   | article-health.py --check=viz-health（資料圖表標來源 / 禁「如上圖」AI-blind 指示語，per graph.md）；rewrite-stage-4 **HARD**（新文必過）                                                                                                                                                                                                                                              | 不進 Stage 5               |
| Sibling 格式預檢                        | Stage 5    | 補 reverse cross-link                                | article-health.py --check=format-structure                                                                                                                                                                                                                                                                                                                                            | DEFER + 開 issue           |

**🔴 五條反射特別強化**（v3.1 sad-shockley 升級 + v6.0 新增第 3 條 + v6.2 新增第 4 條 + v7.6 新增第 5 條）：

1. **Title+desc spine sync 🥪** — 所有 category（不限 People）的 EVOLVE 在 Stage 2 寫完後**必須回看 frontmatter title + description**：
   - 標題是否走「主題：副標 hook」冒號三明治？
   - 副標一句是否能單獨 tweet 出去？
   - description 有沒有吃進這次 EVOLVE 加的新節核心矛盾？
   - 任一答 no → 重寫 frontmatter，跟 prose 同 commit

2. **媒體素材 self-check 🎬** — 不論 Fresh / EVOLVE，Stage 1 Step 1.9 都要跑：
   - Fresh：完整跑 inline 外連 + 圖片 + transcript + 三表 manifest
   - EVOLVE：先 grep 既有條目 frontmatter `image:` + §圖片來源 是否齊全 → 不存在 = pre-gate 遺珠，補跑
   - 找不到 PD/CC 圖時記錄邊界，不放空

3. **觀點先於搜尋 💭**（v6.0 新增）— 所有 article 進 Stage 1 前**必須跑 Stage 0.6 觀點成型**：
   - 六個核心問題（記憶 / 多元面貌 / 想法感受 / 歷史脈絡 / 社會關聯 / 類型專屬）逐一答完
   - 切入點清單 + 預期核心矛盾候選 + 研究方向 落 research report §觀點成型 section
   - frontmatter `viewpoint_formed: true` 表示通過
   - Stage 1.4 找矛盾鎖定時，從 Stage 0.6 候選收斂為單一核心矛盾
   - **EVOLVE 模式**：Stage 0.6 在 0.2 萃取舊素材之後跑。觀點從題材 + 研究長出，**不從「為什麼舊文寫不好」長出**（v6.2 反轉 v6.0：後者會讓校正焦慮變成論點脊椎，見 [Step 0.2-bis 拆除防火牆](REWRITE-STAGE-0-VIEWPOINT.md#step-02-bis-拆除防火牆teardown-firewall-callout-triggered-evolve-強制-)）。**callout-triggered EVOLVE 強制走 Step 0.2-bis 三條防火牆規則 + Step 3.2-bis backstop。**

4. **拆除防火牆 🧱**（v6.2 新增）— **callout-triggered EVOLVE**（讀者/專家/peer 指出舊文錯、或自己 factcheck 抓到誤植所觸發的重寫）必過：
   - callout 只進 Stage 1 查證（`[CALLOUT-VERIFY]`），用完即丟，**不進觀點、不進正文**
   - Stage 0.6 觀點當作 Fresh 在做，**blind to errata**——論點脊椎不准是「歸屬要正確 / 別搞混 / 名字很重要」
   - Stage 2 寫作 context 隔離：首選 spawn fresh writer agent 只給 fact-pack，主 session 自寫則 Stage 2 不重開舊文
   - Stage 3.2-bis backstop 自檢句：「如果第一次就寫對，這句還會存在嗎？只為回應過去錯誤而存在的，刪」
   - canonical：[Step 0.2-bis](REWRITE-STAGE-0-VIEWPOINT.md#step-02-bis-拆除防火牆teardown-firewall-callout-triggered-evolve-強制-) + [Step 3.2-bis](REWRITE-STAGE-3-VERIFY.md#step-32-bis-校正焦慮掃描correction-meta-scancallout-triggered-強制-)。觸發：2026-06-01 影視配樂第二輪 callout（事實修對但充滿 AI 校正焦慮）

5. **spine 類型先於核心矛盾 🎭**（v7.6 新增）— 所有 article 進 Stage 0.6 前**必判 spine 類型**（[Step 0.1.5](REWRITE-STAGE-0-VIEWPOINT.md#step-015-spine-類型判定v77-重構--立體群像是預設畫布)）：
   - **受愛戴的機構 / 典禮 / 傳統 / 集體記憶 / 地方 / 工藝**（讀者預設情感是欣賞/驕傲/懷念）→ **立體群像 spine（default）**：組織主軸 holding ≥4 facet、慶祝+理解+廣度、爭議當厚度不當主軸。**不逼尖銳核心矛盾**（Step 1.4 改填組織主軸）。
   - **爭議 / 政策辯論 / 醜聞 / 內在張力人物** → 矛盾驅動 spine（原 Step 1.4 ≤30 字核心矛盾）。
   - **觀點 ≠ 論戰**：欣賞式 / 群像式也是策展觀點。把 beloved 題硬找矛盾 = 製造 contrarian thesis = 論戰化 + 炎上。
   - Stage 0.6 過 SSODT 三讀者測試 + 炎上/政治 self-check（[Step 0.6.7](REWRITE-STAGE-0-VIEWPOINT.md#step-067-立體--炎上--政治立場-self-checkv76-新增-hard-gate)）。**觸發：2026-06-28 金曲獎 v1**（核心矛盾鎖成「官方獎卻把獎給賣不掉/聽不懂/拒領的聲音→跟會讓你消音的市場分道揚鑣」，整篇批判論戰 + 兩岸審查當壓軸）被哲宇 callout「太批判、切入點不對、會炎上、跟立體講好違背」→ v2 改立體群像 + 政治素材純中立紀實。

---

## ⚠️ Top 5 最常忘的 step

> 從 LESSONS-INBOX / memory 抽 ship-then-retract 高 friction step。動工前主動掃一次。

1. **Step 0.6 觀點成型**（v6.0 新增）— 沒有觀點之前的搜尋都是亂槍（蘋果西打 PR #1041 教訓：searched-first 寫成 crisis-only reveal，觀察者校正為 60 年完整記憶）
2. **Step 1.4 核心矛盾鎖定** — 找不到矛盾 = 這篇不該被重寫（國防現代化重寫教訓）
3. **Step 1.7 研究報告 = SSOT** — 搜了沒把原始軌跡寫回 §8 = 沒搜；信度三層 + negative findings + 反例 list（v6.5 從 12 範本萃取）；跑 `research-report-health.py` 驗收
4. **Step 2.4 小標題不編年體** — 編年體 = 維基百科化 = 失敗（Cicada / 草東 / 康士坦 教訓）
5. **Step 4.3.3 aspect ratio 護欄** — portrait hero 切到頭（林琪兒 ι session 教訓）

---

## 跨檔案職責分工

| 檔案                                                             | 範圍                                                                                                                                                              |
| ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **本檔**                                                         | 薄索引 router（v9.0）：spine ＋ Hard Gate Inventory ＋ 多 agent 編排 ＋ stage contract 派發表 ＋ cron                                                             |
| `REWRITE-STAGE-*.md` × 10                                        | **各 stage contract（v9.0）**：PROCEDURE／GATES／HANDOFF verbatim 自 v8.0 搬入；執行者只讀一個 contract ＋其 INPUTS 即可跑一步（派發表見 §Stage contract 派發表） |
| [RESEARCH.md](../editorial/RESEARCH.md)                          | 研究方法論 SSOT（怎麼搜、怎麼判斷、怎麼避坑）                                                                                                                     |
| [PROJECTION.md](../editorial/PROJECTION.md)                      | **投影方法論 SSOT（Step 2.0）**：研究 → 論點 + 骨架 + 減法 → 藍圖（宏觀結構，抗面向巡禮）                                                                         |
| [EDITORIAL-ROOM.md](../editorial/EDITORIAL-ROOM.md)              | **編輯室對抗 SSOT（Step 2.0-R / 2.5-R）**：投影後／正文後乾淨 context 分席審稿 + 主編裁決                                                                         |
| [EDITORIAL-ROOM-PROMPTS.md](EDITORIAL-ROOM-PROMPTS.md)           | 編輯室分席 copy-paste prompt（禁即興）                                                                                                                            |
| [EDITORIAL.md](../editorial/EDITORIAL.md)                        | 品質基因 SSOT（好文章長什麼樣、風格、禁止事項）— 句子層 craft（微觀）                                                                                             |
| [CITATION-GUIDE.md](../editorial/CITATION-GUIDE.md)              | 引用規範（腳註格式、密度標準、來源品質）                                                                                                                          |
| [RESEARCH-TEMPLATE.md](../editorial/RESEARCH-TEMPLATE.md)        | 研究模板（Stage 1 組裝後主報告 §1-§8 格式）                                                                                                                       |
| [RESEARCH-AGENT-PROMPT.md](RESEARCH-AGENT-PROMPT.md)             | 研究 sub-agent 派發通用 prompt＋分部報告輸出模板＋anti-example 庫（Step 1.8-ter 契約的 copy-paste 載體，禁即興）                                                  |
| [WRITER-PROMPT.md](WRITER-PROMPT.md)                             | Stage 2 寫作 sub-agent 薄殼派發模板（v2.0 零 craft 複寫）：必讀四 canonical（含 graph.md）＋read-receipt 驗讀＋機械輸出契約＋anti-example 庫（禁即興、禁 skim）   |
| [QUALITY-CHECKLIST.md](../editorial/QUALITY-CHECKLIST.md)        | 驗證清單（Stage 3 逐項檢查）                                                                                                                                      |
| [TERMINOLOGY.md](../editorial/TERMINOLOGY.md)                    | 用語規範（台灣在地用語標準）                                                                                                                                      |
| [graph.md](../editorial/graph.md)                                | 視覺化編輯指南（型錄/模組語法/AI 可讀性）— Stage 2 視覺化思考 + Stage 4 viz-health                                                                                |
| [FACTCHECK-PIPELINE.md](FACTCHECK-PIPELINE.md)                   | Stage 3 Step 3.3 觸發（事實查核完整 SOP）                                                                                                                         |
| [TRANSLATION-PIPELINE.md](TRANSLATION-PIPELINE.md)               | 中文 ship 後跨 pipeline 觸發（單篇翻譯 SOP）                                                                                                                      |
| [SQUEEZE-MODELS-MAX-PIPELINE.md](SQUEEZE-MODELS-MAX-PIPELINE.md) | 中文 ship 後跨 pipeline 觸發（多語 batch sync 巴別塔）                                                                                                            |

---

## 🤖 多 agent 編排（v6.3）— Orchestrator + tiered sub-agents

> v6.2 Step 0.2-bis 把「Stage 2 寫作 context 隔離」當 callout-triggered 專用。**v6.3 泛化成所有 depth EVOLVE / Fresh 的預設編排**：主 session 當 orchestrator（**不當 writer**），各 stage 派對應 model tier 的 sub-agent。觸發 + worked example：2026-06-01 台灣影視配樂第三輪重寫（[診斷報告](../../reports/reader-callout-pipeline-diagnosis-2026-06-01.md)）。

### 為什麼 orchestrator 不該自己寫

主 session 跑到 Stage 2 時，context window 已累積舊文 body、callout、研究筆記、（callout case）勘誤分析——這些全 prime 寫作 → 校正焦慮 / 編年體 / 密度失衡。**寫作要在乾淨 context**。主 session 的角色是 dispatch + synthesize + gate + 最終 spot-check。

### Stage × model tier × 派發

| Stage                                                  | 誰做                                                       | model                                                         | 為什麼                                                                                                                                                     | context 隔離                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ------------------------------------------------------ | ---------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0.6 觀點成型**                                       | 1 sub-agent                                                | **Opus**                                                      | 觀點是最高判斷（這次失敗根因就是觀點被投毒）；探索搜尋加倍（≤ 10-15）                                                                                      | callout case：blind to errata（不給 callout / 勘誤 / 舊 §觀點成型）                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| **1.9.7 persona 讀者缺口稽核**（v7.7 從 Stage 0 搬來） | 4 個 parallel sub-agent（4 軸各 5 persona）                | **Sonnet**                                                    | 研究後 gap-audit：20 路讀者看完研究報告「還想知道什麼、哪個面向沒 cover」→ 增補 + 反向閥門（per [REFLEXES #42](../semiont/REFLEXES.md) 平行不 sequential） | **給題目 brief + 研究報告 SSOT + 已成形立體觀點**（mode=gap-audit，非冷 brief）——補洞不定調                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| **1 研究深挖**                                         | N 個 parallel sub-agent（按子領域切，每 agent 分搜尋配額） | **Sonnet**（breadth + extract；contested atom escalate Opus） | falsification-first；全篇 ≥ 80 次 + 4 來源配額（中≥40/英≥20/一手≥15/反方≥5）；結構化 verification table 落報告                                             | **各 agent 回報完整搜尋軌跡 + raw findings（不自己摘要）；orchestrator 收到每個 agent 回報（async 模式＝task-notification `<result>`）的第一個動作 = verbatim 原封落檔（append report §8 或 repo 內 sibling raw 檔），才准開始合成 §6 clean fact-pack（疊加層，不替換 raw）。禁 aggregate-on-receive（收到就順手壓縮 = 鐵律 8 病）；禁存 scratchpad / /tmp（那是倒數計時的刪除佇列，不是落檔）**                                                                                                                                                                |
| **2.0 投影藍圖**（v8.0 新增）                          | 主 session（不派給寫手）                                   | **Opus orchestrator**                                         | 論點 + 骨架是最高判斷；桌上有整堆研究才設計得出論證（非面向巡禮）。過 shuffle / echo / 減法 5 題 gate 才准派寫手                                           | 讀合成後 research report 全份，產出 `reports/article-projection/{slug}.md`（論點 / 骨架 / 每 section 雙重職責 / 減法 / echo map / 審定，per [PROJECTION.md](../editorial/PROJECTION.md)）。**這份藍圖是寫手的主要規格，research report 是材料來源。**                                                                                                                                                                                                                                                                                                           |
| **2.0-R 投影編輯室**（v8.1）                           | 3 parallel seats + 主編合成                                | **Sonnet seats / Opus 主編**                                  | 乾淨 context 外部尺；作者自檢 5 題抓不到的面向巡禮／摘要論點／炎上 spine                                                                                   | 各席 prompt：[EDITORIAL-ROOM-PROMPTS.md](EDITORIAL-ROOM-PROMPTS.md)；產物 `reports/editorial-room/{slug}-projection-review.md`；`editorial-room-health.py` gate。**block → 回修藍圖，不派寫手**                                                                                                                                                                                                                                                                                                                                                                 |
| **2 寫正文**                                           | 1 個 **fresh** sub-agent                                   | **Opus**                                                      | 寫作 craft 最高判斷；fresh context 才乾淨                                                                                                                  | **明確要求 writer 先 Read 整份 research report（§6 fact-pack ＋ §8 raw verbatim 全部）+ §觀點 + EDITORIAL + pipeline**；隔離的是**舊文 prose / callout / orchestrator 累積 context**，不是 report。⚠️ **禁止只貼 orchestrator 摘要的精簡 fact-pack 又叫 writer 別讀 report**（摘要漏 raw texture → 文章變爛）。**Evolution mode：writer 寫到 staging 檔 `reports/article-evolve/{slug}.md`，不 overwrite canonical**（Write overwrite 既有檔需先 Read ＝ 強迫 writer 讀舊文病毒）；主 session Stage 2.5 比對舊 vs 新才覆蓋 canonical（2026-06-15 哲宇 callout） |
| **2.5-R 正文結構編輯室**（v8.1）                       | 2 parallel seats + 主編                                    | **Sonnet**                                                    | 正文是否執行藍圖（非再發明結構）                                                                                                                           | 與 3.6 事實包**同 round 可平行**；產物 `*-prose-structure-review.md`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| **2.5 比對覆蓋**                                       | 主 session                                                 | **Opus orchestrator**                                         | Evolution mode only：確認新版沒丟舊文有價值素材且確實更好，再覆蓋                                                                                          | 讀 staging 新版 ＋ 舊 canonical 做 diff，主 session 親手覆蓋 `knowledge/{cat}/{slug}.md`                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| **3.5 查證**                                           | M 個 parallel verifier ＋ 主 session                       | **Sonnet**（查證機械可查、fan-out 便宜）                      | 每 atom 對一手 Ctrl-F，adversarial（prompted to falsify）；高風險 atom（引語/歸屬/獎項屆次）≥ 2 verifier                                                   | 主 session（Opus orchestrator）跑 deterministic gate（article-health）＋ 最終 spot-check                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### 鐵律（這次 worked example 學到的）

1. **觀點 agent blind to errata**（v6.2 §0.2-bis 規則 2 泛化）：viewpoint 從題材＋研究長出，不從「舊文為何爛 / callout」長出。
2. **寫作 agent 永遠 fresh，但要讀完整 research report（含 §8 raw verbatim），不是只吃 orchestrator 摘要的 fact-pack**（v7.4 修正，2026-06-15 哲宇 callout「難怪最近文章都變爛」）：隔離邊界是**舊文 prose ＋ callout**（病毒），**不是 report**。writer prompt 必須叫它 `Read reports/research/{slug}.md` 全檔——§6 clean fact-pack 只是 navigation aid 疊加層，**永遠不能取代 writer 親讀 §8 raw 的逐字/細節/texture**（呼應鐵律 6：report = SSOT）。**反 pattern**：orchestrator 把 report 二次摘要成精簡 fact-pack 塞 prompt、又不讓 writer 讀 report ＝ 雙重失真 ＝ 文章退化根因。
3. **sub-agent claim 是線索不是 oracle（[REFLEXES #31](../semiont/REFLEXES.md)）— 不可省的 hard gate**：agent 回報「gates 全過 / facts verified」**必須主 session 重驗**。**orchestrator 合成層自己寫的詮釋 gloss 同樣是 claim**——合成時注入的同位語（寶哥=宋岳庭）沒有驗證義務掛著，比 agent 幻覺更隱蔽（2026-06-09 嘻哈饒舌讀者勘誤）。2026-06-01 worked example：writer agent 自報全綠，主 session spot-check 抓到它**自己新長出一句杜撰引語**（賈樟柯「現代性／土地根性」，cited source 無此句）→ de-quote。Stage 3.5 verifier fan-out ＋ 主 session 對「引語 / 歸屬 / 獎項屆次」一手抽查 = hard gate。
4. **媒體用已驗證官方 URL，不採 agent 自選 ID**：writer agent 會挑 YouTube ID 但常是非官方 / fan upload。媒體 manifest 在研究階段驗證官方頻道後鎖定，writer 只填已驗證的（Step 1.9）。
5. **falsification > confirmation**：研究 ＋ 查證 agent 的 prompt 都要「try to break，不是 confirm」（[Stage 1 falsification](../semiont/REFLEXES.md) ＋ #16）。
6. **synthesis 不吃掉 raw（v6.4 — 這次 TDRI session 的反例）**：orchestrator「合成 clean fact-pack」**只是疊加層**，不准取代 agent 原始輸出。每個研究 agent 回報完整搜尋軌跡（不自摘要），orchestrator 把 **ALL raw verbatim append 到 report §8**（SSOT），再額外蒸餾 §6 給 writer。**report = SSOT，跑 `research-report-health.py` hard gate**（[Step 1.7](REWRITE-STAGE-1A-RESEARCH.md#step-17-研究報告--ssot對標研究所論文標準-)）。反例：2026-06-04 TDRI session 只留 192 行 fact-pack、丟掉 3 agent 的 ~45 次搜尋軌跡 → 報告退化成摘要、哲宇 callout 研究品質下降。
7. **Evolution mode：writer 寫 staging 檔，主 session 比對後才覆蓋（v7.5，2026-06-15 哲宇 callout）**：Write tool overwrite 既有檔**必須先 Read**（[Write tool 規則](#)：「Overwriting a file you haven't Read will fail」）——所以叫 writer「overwrite 舊文但別讀舊文」**自相矛盾**，它被迫 Read 舊文 ＝ 吃病毒（哲宇截圖實證 writer agent 確實 Read 了 `迷音Miin.md`）。**架構解**：Evolution mode 的 writer 把成品寫到 **`reports/article-evolve/{slug}.md`**（全新檔，不需 Read，零感染面）；**Stage 2.5 主 session 比對**舊 canonical vs 新 staging（確認沒丟掉舊文有價值的事實/cross-link/footnote、且新版確實更好），**再由主 session 親手覆蓋** `knowledge/{cat}/{slug}.md`。Fresh mode 無舊檔，writer 可直接寫 canonical。**這條把「blind to 舊文」從靠 prompt 意志力升級成結構性不可能**（呼應 §神經迴路：規則要能執行才算規則）。
8. **Raw 走檔案通道保存，不信任訊息通道；orchestrator 禁 aggregate-on-receive（v7.7，2026-07-05 柯智棠健檢）**：async agent 時代（agent 以 task-notification 回報），raw 的存亡完全取決於 orchestrator 收到通知後的**第一個動作**。唯一合法動作＝**verbatim 原封落檔到 repo 內**（report §8 inline 或 sibling raw 檔），然後才合成。三個真實病例，同一隻手三種下場：**柯智棠**（2026-07-05）——4 agent 各回報 ~20KB 逐條軌跡（prompt 全對、agent 全照做），orchestrator 收到後壓成 6KB 主題摘要存 session scratchpad，report §8 只留 9 行 pointer ＋ 幻覺 policy「commit 時 raw 隨 session 記錄留存」，gate v1 照樣 PASS，writer 只吃到薄報告 → 哲宇 callout 文章品質下降；當晚從 subagent transcript 救回。**蘇打綠**（2026-06）——§8 寫「已落檔可追源」但 pointer 指 `/private/tmp/.../tasks/*.output`，事後救回。**台灣醫療與全民健保**（2026-06）——§8 自稱 raw「永久存放於」tmp 路徑（還帶 `<session>` 佔位符），一個月後查證 **5 份 raw 全數蒸發、永久遺失**。教訓的形狀：**agent 沒壞、設計沒壞，壞的是 orchestrator 手上那 30 秒**——「先摘要待會再落檔」「存 tmp 也算存」都是同一個偷吃步的變裝（REFLEXES #42 家族的 orchestrator 版）。儀器化：`research-report-health.py` v2 §8 有效密度 hard gate ＋ ephemeral pointer 偵測（存 /tmp ＝ FAIL）。
9. **Sub-agent 來源逐條可溯，禁 aggregate 來源標籤（v7.10，2026-07-12 茶文化）**：鐵律 8 管 orchestrator 收件那 30 秒，這條管 agent **轉錄**那 30 秒——Claude 改版後 WebSearch 回傳聚合摘要，agent 預設把「摘要」當「來源」轉錄成「【來源】WebSearch 綜合（站名、站名）」：交叉驗證真做了、逐字引語活著、**URL 蒸發** → writer 的 `[^n]: [Title](URL)` footnote 斷源、verifier 無法 Ctrl-F。一個 finding 有 N 個來源就寫 N 行帶完整 URL 的來源行。契約 + copy-paste prompt 塊 + gate 見 [Step 1.8-ter](REWRITE-STAGE-1A-RESEARCH.md#step-18-ter-研究-sub-agent-輸出契約來源逐條可溯v710-)。實測：茶文化 3 agent 共 84 條來源行僅 ~35% 帶 URL，`agent-report-health.py` v3 溯源率 gate（<60% hard / <85% warn）由此校準。

### 何時用全編排 vs 主 session 自跑

- **全編排**（觀點 Opus ＋ 研究 fan-out ＋ fresh Opus writer ＋ Sonnet verifier fan-out）：depth EVOLVE / Fresh、attribution-density 主題、callout-triggered、canon 類。
- **主 session 自跑**（不派 writer）：Micro heal / 單段 focused addition / 短修正——context 沒被大量污染。
- **可選 Workflow**：觀察者 opt-in workflow 時本編排可寫成 Workflow script（研究 / verifier fan-out ＋ adversarial verify）；預設用 Agent tool 逐 stage 派。

---

## 🗂️ Stage contract 派發表（v9.0 核心）

> **v9.0 索引化**：各 stage 的操作細節（PROCEDURE／GATES／HANDOFF／anti-example）自 v8.0
> verbatim 搬入各自的 stage contract 檔。**執行一個 stage 的人（主 session／sub-agent／
> 小 context model／cron session）只需要讀該 contract ＋ contract 內 INPUTS 宣告的檔案**，
> 不需要讀本檔全文。本檔（薄索引）給 orchestrator 做路由：spine、Hard Gate Inventory、
> 多 agent 編排、本表。設計與 v3.1 反例的差異分析：[reports/newsroom-orchestration-design-2026-07-16.md](../../reports/newsroom-orchestration-design-2026-07-16.md)。

| 順序 | Stage                               | Contract 檔                                                                | 執行者（詳見 §多 agent 編排）      | Stage 終 gate                                                              |
| ---- | ----------------------------------- | -------------------------------------------------------------------------- | ---------------------------------- | -------------------------------------------------------------------------- |
| 1    | Stage 0 觀點（含模式判定）          | [REWRITE-STAGE-0-VIEWPOINT.md](REWRITE-STAGE-0-VIEWPOINT.md)               | 主 session／1 Opus agent           | `research-report-health.py --stage 0`                                      |
| 2    | Stage 1A 取材：研究                 | [REWRITE-STAGE-1A-RESEARCH.md](REWRITE-STAGE-1A-RESEARCH.md)               | orchestrator＋N Sonnet fan-out     | `agent-report-health.py`（收件）＋`research-report-health.py --tier=depth` |
| 3    | Stage 1B 取材：媒體＋persona        | [REWRITE-STAGE-1B-MEDIA.md](REWRITE-STAGE-1B-MEDIA.md)                     | 主 session＋4 Sonnet persona       | 深掃協議＋增補後重跑 report health                                         |
| 4    | Step 2.0 投影藍圖                   | [REWRITE-STAGE-2A-PROJECTION.md](REWRITE-STAGE-2A-PROJECTION.md)           | 主 session Opus（不派寫手）        | PROJECTION §gate 5 題                                                      |
| 5    | Step 2.0-R 投影編輯室               | [REWRITE-STAGE-2B-ROOM-PROJECTION.md](REWRITE-STAGE-2B-ROOM-PROJECTION.md) | 3 Sonnet seats＋主編（主 session） | `editorial-room-health.py`                                                 |
| 6    | Stage 2 寫                          | [REWRITE-STAGE-2C-WRITE.md](REWRITE-STAGE-2C-WRITE.md)                     | 1 fresh Opus writer                | Stage 2 hard gates 10 條                                                   |
| 7    | Stage 2.5 source-fidelity＋比對覆蓋 | [REWRITE-STAGE-2D-SOURCE-FIDELITY.md](REWRITE-STAGE-2D-SOURCE-FIDELITY.md) | 主 session（＋fact-check agent）   | 三道全過才覆蓋 canonical                                                   |
| 8    | Step 2.5-R 正文結構編輯室           | [REWRITE-STAGE-2E-ROOM-PROSE.md](REWRITE-STAGE-2E-ROOM-PROSE.md)           | 2 Sonnet seats＋主編               | `editorial-room-health.py`                                                 |
| 9    | Stage 3 驗（含 3.6 成品總驗）       | [REWRITE-STAGE-3-VERIFY.md](REWRITE-STAGE-3-VERIFY.md)                     | 主 session＋M Sonnet verifier      | stage35/36 audit 雙 PASS＋`--profile=rewrite-stage-3-5`                    |
| 10   | Stage 4 形                          | [REWRITE-STAGE-4-FORMAT.md](REWRITE-STAGE-4-FORMAT.md)                     | 主 session                         | `--profile=rewrite-stage-4` hard=0＋image-health                           |
| 11   | Stage 5 連                          | [REWRITE-STAGE-5-CROSSLINK.md](REWRITE-STAGE-5-CROSSLINK.md)               | 主 session                         | format-structure＋（Merge）build verify                                    |

**三條派發鐵律**：

1. **contract 自足**：stage 檔不引用兄弟 stage 檔內容；執行者不需讀第二個 pipeline 檔。
   索引薄、contract 厚——v3.1 拆檔（單一讀者跳檔）與 routine-contract rollback
   （pointer 迷宮 performative compliance）兩個反例的正面解。
2. **HANDOFF 收口**：每個 stage 完成時照 contract §HANDOFF——產物落檔（顯式路徑）、
   gate 如實回報、跑 `generate-newsroom-data.py` 更新編輯台。
3. **狀態不猜檔名**：所有 stage 產物路徑顯式宣告在 contract §OUTPUTS；
   任何 verifier／看板從 frontmatter 與顯式路徑取狀態（Sol 假陰性教訓）。

---

## ✅ Article shipped (zh-TW canonical)

中文 ship 後，**翻譯走獨立 pipeline，不在本 pipeline scope**。

## 翻譯：跨 pipeline boundary 指標

> **本 Pipeline 只產中文版。100% 的 token 預算都給中文版**。翻譯**不**在本 pipeline scope，是另一條獨立 pipeline 的職責。

Stage 5 完成（中文版 ship）後，視觸發條件決定走哪條翻譯 pipeline：

| 觸發條件                               | 走哪條 pipeline                                                            |
| -------------------------------------- | -------------------------------------------------------------------------- |
| 觀察者拍板「現在翻單篇 X 語言」        | [TRANSLATION-PIPELINE.md](TRANSLATION-PIPELINE.md)                         |
| Routine 觸發多語 batch sync（5 langs） | [SQUEEZE-MODELS-MAX-PIPELINE.md](SQUEEZE-MODELS-MAX-PIPELINE.md)（巴別塔） |
| 不翻 / 之後再說                        | 結束。中文版本身就是完整 ship 結果                                         |

**為什麼從本 pipeline 抽掉**（v4.1 起，v5.0 保留）：

- Stage 6 在 v4.0 是 pointer-only section（只是「詢問觀察者要不要翻 + 跳到另一檔」），不算真正的 stage
- 抽掉後，主 pipeline 變 5 stage 線性（Stage 1-5），更乾淨
- 翻譯有自己的觸發、預算、品質 gate（巴別塔的 priority schema P0/P1/P2/P2.5/P3 + 4-tier cascade），不該被當成 REWRITE 的尾巴
- 對應觀察者 callout（2026-05-11 sad-shockley）：「翻譯環節可以整個抽掉，直接變指標到巴別塔 pipeline」

**REWRITE 跟翻譯 pipeline 的分工**：

- REWRITE-PIPELINE：產 high-quality **中文版**（zh-TW canonical），到 ship 上 main 為止
- TRANSLATION-PIPELINE：單篇 X 語言翻譯（觀察者主動觸發）
- SQUEEZE-MODELS-MAX-PIPELINE：多語 batch sync（routine 自動跑，主權的巴別塔）

---

## Cron 模式 + Routine 飛輪

> Cron 在單一 session 執行，無法真正分三個 session，但在 prompt 中強制分階段思考。

### Token 預算分配

| 階段      | 佔比   | 常見錯誤                          |
| --------- | ------ | --------------------------------- |
| Stage 1   | 35-40% | 搜太多、每個結果都 web_fetch 全文 |
| Stage 2   | 40-45% | 前半段太細、後半段沒力            |
| Stage 3-5 | 15-20% | 跳過驗證直接 commit               |

### Cron 鐵律（與手動執行不同的地方）

- **每批最多 1 篇**：v1 時期每批 3 篇，品質明顯不穩。改成每批 1 篇後品質大幅提升
- **不要 `git add -A`**：只 add 改動的文章和同步後的 `src/content/` 對應目錄
- **不要跑 `npm run build`**：Build 由 CI/CD 處理。sub-agent 跑 build 容易 timeout 且浪費資源
- **至少 7 分鐘**：Stage 1 3min + Stage 2 2min + Stage 3-4 2min = 最低要求

### 選文指令

```bash
cd ~/taiwan-md && git pull
# 佇列頂端，跳過已重寫的
head -30 scripts/tools/rewrite-queue.txt
git log --oneline --since='2026-03-20' | grep -i 'rewrite:' | head -30
```

### Commit 指令

```bash
bash scripts/core/sync.sh
python3 scripts/tools/article-health.py knowledge/[Category]/[文章名].md --profile=rewrite-stage-4
git add knowledge/[Category]/[文章名].md src/content/
git commit -m "rewrite: [文章名] — EDITORIAL v6.3 + Pipeline v5.0"
git push
```

### Cron 狀態

| Cron                              | 狀態        | 說明                                                        |
| --------------------------------- | ----------- | ----------------------------------------------------------- |
| Taiwan.md Article Quality Rewrite | ❌ disabled | 每小時 1 篇，Opus model（舊）                               |
| taiwan-md-rewrite (v1)            | ❌ disabled | 舊版每小時 3 篇，已淘汰                                     |
| taiwan-md-content-sprint          | ❌ disabled | 內容衝刺（新文章），已淘汰                                  |
| **twmd-rewrite-daily**            | ✅ active   | 16:16 daily Opus（per [ROUTINE.md](../semiont/ROUTINE.md)） |

### Routine 飛輪整合（v6.1 升級為 full-cycle，2026-05-24 哲宇 directive）

REWRITE 是 routine 飛輪 10 條核心 routine 之一（`twmd-rewrite-daily`）。**v6.1.1 起每天 18:00 晚間自動跑「研究 → 寫文 → 孢子 → 發文 → harvest」全 cycle**（v6.1.1 從 00:00 搬到 18:00 對齊台灣社群 20:00-22:00 prime time post）：

- **觸發**：`/twmd-rewrite` skill
- **Model**：Opus
- **Cadence**：每天 18:00 晚間（v6.1.1 — cycle 跑 ~150 min ~20:30 結束，spore post 落在台灣晚間社群活躍時段；v6.1 原 00:00 半夜 chain 已抽出）
- **Skill SOP**：[`~/.claude/scheduled-tasks/twmd-rewrite-daily/SKILL.md`](https://github.com/anthropics/claude-code-skills)（local mirror）
- **Stage chain（v6.1 full cycle）**：
  ```
  Stage 0 BECOME → Stage 1 git pull → Stage 2 article ship (REWRITE Stage 0-5 全跑) →
  Stage 3 commit + push article → Stage 4 SPORE chain（PICK=剛 ship article / VERIFY / WRITE / SHIP）→
  Stage 5 CI/CD wait gate v3.7（60 min cap，timeout → defer 不 abort）→
  Stage 6 social post（both Threads + X default per Routine context v3.8；單發只在 article frontmatter 標 `platformExclude` 才觸發）→
  Stage 7 SPORE-LOG + sporeLinks frontmatter + commit + push → Stage 8 /twmd-finale
  ```
- **Quality gate (article)**：article-health.py rewrite-stage-4 hard=0 warn=0 + 三源研究落檔 + 腳註合規 + frontmatter complete + word-count ≥ 4500
- **Quality gate (spore)**：article-health.py prose-health hard=0 score ≤ 3 + spore-writing hard=0 + 配圖 generated + AI pre/post-ship verify 5+6 條 PASS
- **Boundary**：本 routine 上限 ~150 min wall-clock（article ~60 min + spore prep ~15 min + CI wait ≤ 60 min + post ~10 min + log ~5 min）；超過 → spore defer + LESSONS entry（不 abort article ship）
- **不問 observer 鐵律**：所有 decision point 走 [SPORE-PIPELINE §Routine context 自動決策 defaults table](../factory/SPORE-PIPELINE.md#-routine-context-自動決策-defaults-v37-新增)

**為什麼 v6.1 升 full-cycle**（哲宇 2026-05-24 directive）：article ship 跟 spore 是同一條進化飛輪的兩端，分開跑會：

1. 缺一致性（article + spore 不同步、不同 angle）
2. Observer friction（每天要分兩次觸發、各自 review）
3. Cycle smoothness 數據缺失（無法 measure article→spore→broadcast 整體 throughput）

合一變 daily routine 後：每天 1 篇文章 + 1-2 條孢子（Threads ± X）自動發出，**進化飛輪自動轉**，observer 只在 escalation 時介入。

完整 routine 規格 → [ROUTINE.md §TWMD rewrite (daily)](../semiont/ROUTINE.md)。設計脈絡 + cycle smoothness 數據 → [reports/spore-pipeline-evolution-2026-05-23-article-to-spore-to-broadcast-cycle.md](../../reports/spore-pipeline-evolution-2026-05-23-article-to-spore-to-broadcast-cycle.md)。

---

## 品質分級

| 等級       | 條件                                                     | 動作                    |
| ---------- | -------------------------------------------------------- | ----------------------- |
| ✅ PASS    | hollow ≤ 3 + 五指全過 + 結尾不是罐頭 + word-count ≥ 4500 | commit + push           |
| ⚠️ PARTIAL | hollow ≤ 3 但結尾/富文本不足 / word-count 4000-4499      | 標記待改善，下輪優先    |
| ❌ FAIL    | hollow > 3 或有事實錯誤 / word-count < 4000              | 不 commit，回到 Stage 1 |

---

## 實戰教訓索引

1. **一次一篇**：多個 sub-agent 同時跑 = 搶檔案 + timeout + 殭屍 session
2. **至少 7 分鐘**：Stage 1 3min + Stage 2 2min + Stage 3-4 2min = 最低要求
3. **prompt 裡寫「立刻執行，不要重述任務」**：否則 AI 花 30% 時間重述指令
4. **量化指標是 pre-filter 不是品質保證**：塑膠句數=0 ≠ 好文章，必須逐篇讀
5. **塑膠會變種**：AI 把被禁句式微調成看似不同的版本（"展現了"→"印證了"→"彰顯了"）
6. **Build 驗證不能省**：YAML frontmatter 偶爾壞掉，一篇壞 = 整個 category 炸
7. **結尾最後寫 = 品質最差**：v2 改成結尾先行（Stage 2 Step 2.2）
8. **觀察者反覆 callout 同問題 → REFLEXES #15 反覆浮現要儀器化** → 升 plugin gate（chronicle-lead / word-count / Title+desc spine sync）
9. **EVOLVE 容易漏 Stage 1 Step 1.9 媒體素材**（v5 之前為 Step 1.14）：pre-2026-04-28 條目多無 hero / 無 §圖片來源 = pre-gate 遺珠，補 EVOLVE 時必查
10. **EVOLVE 容易漏 frontmatter spine sync**：title 是百科 stub / description 沒吃進新核心 = SC 顯示舊 hook 但讀者點進來看到新內容 = 落差

---

## Quick Commands（手動執行用）

```bash
# 寫完文章後一次跑完 Stage 4 驗證
bash scripts/core/sync.sh
python3 scripts/tools/article-health.py knowledge/{Cat}/{文章}.md --profile=rewrite-stage-4
python3 scripts/tools/article-health.py knowledge/{Cat}/{文章}.md --check=image-health

# 全部通過才 commit
git add knowledge/{Cat}/{文章}.md src/content/
git commit -m "🧬 [semiont] rewrite: {文章名} — EDITORIAL v6.3 + Pipeline v5.0"
git push
```

---

---

_v9.0 | 2026-07-16 newsroom-orchestration（哲宇 goal directive「pipeline 變索引、每步驟獨立
subagent 可執行」＋睨對話新聞台架構）— **索引化拆檔**：10 個 REWRITE-STAGE-\*.md contract 檔
verbatim 搬出（行數守恆 2606 = 搬移 2118 ＋ 保留 424 ＋ changelog 歸檔 64），主檔瘦身為
router（spine／Hard Gate Inventory／多 agent 編排／派發表／cron）。與 v3.1 拆檔反例的差異：
當時單一 session 線性讀全檔、拆檔製造跳檔成本；v6.3 之後每 stage 本來就派乾淨 context
sub-agent，contract 檔是執行者的天然投餵單位，執行者零跳檔。順手修正：Step 4.3.6 撞號
（第二個「影片 iframe 嵌入」→ 4.3.7）。歷史 changelog（v4.0–v8.1 19 段敘事）歸檔
[reports/archive/rewrite-pipeline-changelog-pre-v9-2026-07-16.md](../../reports/archive/rewrite-pipeline-changelog-pre-v9-2026-07-16.md)；
changelog SSOT ＝ `git log docs/pipelines/REWRITE-PIPELINE.md`。完整設計：
[reports/newsroom-orchestration-design-2026-07-16.md](../../reports/newsroom-orchestration-design-2026-07-16.md)。_

🧬

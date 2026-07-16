---
title: 'REWRITE-STAGE-2-SOURCE-FIDELITY'
description: 'REWRITE v9 stage contract — Stage 2.5：引用來源 artifact 逐字比對 / 門面句 scope / fact-check agent / Evolution staging 比對覆蓋'
type: 'pipeline-sub-canonical'
status: 'canonical'
current_version: 'v9.0'
last_updated: 2026-07-16
last_session: '2026-07-16-newsroom-orchestration（v9.0 拆檔：自 REWRITE-PIPELINE v8.0 verbatim 搬移，行數守恆）'
parent_canonical: 'REWRITE-PIPELINE.md'
upstream_canonical:
  - '../semiont/MANIFESTO.md'
  - '../editorial/EDITORIAL.md'
---

# Stage 2.5 contract — source-fidelity gate（來源逐字回溯＋staging 比對覆蓋）

> **本檔是 REWRITE-PIPELINE v9.0 的 stage contract**：一個執行者（主 session、sub-agent、
> 或任何 context 有限的 model）只讀本檔＋本檔 INPUTS 宣告的檔案，就能執行本 stage。
> 派發路由與全 pipeline spine 在 [REWRITE-PIPELINE.md](REWRITE-PIPELINE.md)（薄索引）。
> 內文自 v8.0 主檔 verbatim 搬移（原行號 RP v8.0 L1666-1679），歷史敘事與教訓保留在文內。

## 執行卡

|                  |                                                                                                                                |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| **職責**         | 驗成品對真實世界來源（fetch 原頁逐字比對，不只信 report）；Evolution mode 由主 session 比對 staging vs 舊 canonical 後親手覆蓋 |
| **執行者**       | 主 session；fresh-writer 長文可 spawn fact-check agent（falsification mindset）                                                |
| **INPUTS**       | staging/canonical 正文；被引用來源 URL；research report                                                                        |
| **OUTPUTS**      | 修正 in-place；Evolution：主 session 覆蓋 `knowledge/{Cat}/{slug}.md`                                                          |
| **GATES**        | 觸發面：A 級 / fresh-writer EVOLVE 長文 / 含外部來源引用；三道（artifact 逐字 / 門面句 / fact-check pass）全過才覆蓋 canonical |
| **context 預算** | 本檔＋成品＋來源頁                                                                                                             |

## HANDOFF（stage 完成時）

1. OUTPUTS 全數落檔（顯式路徑，不存 scratchpad / tmp——REFLEXES #81）
2. GATES 逐條跑過，結果如實回報（sub-agent claim 是線索不是 oracle，REFLEXES #31）
3. 更新編輯台：`python3 scripts/core/generate-newsroom-data.py`（看板反映現況）
4. 回報格式：stage id ＋ 產物路徑清單 ＋ gate 結果 ＋ 未解疑慮（有就寫，不粉飾）
5. 下一棒：REWRITE-STAGE-3-VERIFY.md

---

## Stage 2.5: source-fidelity gate（來源逐字回溯）— A 級 / fresh-writer EVOLVE 長文 HARD 🔬

> **v7.6 新增（2026-06-16 哲宇 directive「升級」）**。distill 自 LESSONS meta-umbrella `stage2-quote-context-collapse`（vc=8，8 instance 跨 無名小卒 / 國家太空中心 / 嘻哈饒舌 / 廣告史 / 壞特 / 迷音 / 報導者 / 大鮪鱸鰻）。**第一性原理**：Stage 2 writer 即使讀了整份 research report，下筆仍會把研究結論 collapse 成偏記憶 / 偏印象 / 偏字面 / 偏未驗證狀態的 claim——Stage 1 SSOT 寫對、Stage 2 寫歪。structure gate（word-count / footnote / image / viz）全綠 ≠ 事實對；只拿成品比對 research report 也不夠（report 本身可能不全，或 writer 長出 report 沒有的東西）。本 gate 在 **EVOLVE 主 session 覆蓋 canonical 前 / Fresh ship 前**跑，與 Step 3.6 成品總驗互補：3.6 驗「成品內部一致 + 對 report」，2.5 驗「對真實世界的來源」。

三道（任一不過 = 不覆蓋 canonical / 不 ship；已 ship 則 heal + 公開勘誤，per error-boundary-is-traceability）：

1. **來源 artifact 逐字回溯**（instance #8 大鮪鱸鰻）：文中每個「引用的外部來源標題 / 圖表名 / 報導名 / 截圖文字」**不能只信 research report**，要實際 fetch 那個來源 artifact（WebFetch 原頁中文逐字 prompt / curl）逐字比對。大鮪鱸鰻 case：標題誤植「大骪鱸鰻」+ 虛構整段「冷僻字」考據，連 4-agent fact-check 都漏，是為了補連結去 fetch 原圖表頁才現形——**cross-check claim 不夠，要 fetch artifact**。
2. **門面句 scope**（instance #6 迷音）：collapse 不只在 body prose，更在 **frontmatter title + description + 30 秒概覽**（讀者第一印象 + 最易被外部攻擊層）。這三處每個事實 / 法律狀態（allegation→fact）/ 專名 claim 單獨過一次——迷音把 sub judice 未定罪指控在標題壓成既成事實（「偷」），內文紀律守住、門面句崩了才出事。
3. **fact-check agent pass**（instance #7 報導者）：fresh-writer EVOLVE 長文派一輪 fact-check agent（falsification mindset、分簇平行、official 一手 > 媒體轉述），主動查事實 / 幻覺 / 對真人失真指控。報導者 case：6/14 全 gate 綠的 prose 裡藏寶瓶副標幻覺 + 對真人朱亞君「不當行為」失真指控，靠主動 4-agent 查核才抓到——**gate 驗結構，agent 驗事實**。

**觸發**：A 級 / 大眾文 / fresh-writer EVOLVE 長文 / 含引用外部來源標題或圖表 / callout-triggered。輕量 Fresh 或無外部引用的短文至少跑第 2 道（門面句）。

---

---
title: 'Discussion #1146 系統優化建議回應'
description: 'david22115 五條系統優化建議的五桶分類 + 內部現況查證 + 建議路線 + 回覆草稿；附帶發現 GitHub Discussions 是 maintainer 感知的結構性盲點'
type: 'report'
status: 'pending-observer-decision'
created: 2026-07-05
session: '2026-07-05-221922-git-identity'
related:
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'docs/pipelines/MAINTAINER-PIPELINE.md'
  - 'reports/semiont-independent-identity-2026-07-05.md'
---

# Discussion #1146 回應報告 — 五條建議的五桶分類，以及一個比建議更大的發現

> 觸發：哲宇 2026-07-05 丟 [Discussion #1146](https://github.com/frank890417/taiwan-md/discussions/1146) 截圖「幫我也一起做這些問題的思考跟報告」。
> 處理依 CLAUDE.md §Bias 4：外部 critique 先過三道濾網（§自主權邊界 / 跨源驗證 / 五桶分類），寫 critique-response 報告，不直接執行。
> 查證方法：內部考古 agent 全站掃描 + 主 session 親測修正（agent 四個誤讀被抓，見 §修正紀錄）。

---

## 0. 先講比五條建議更大的發現：Discussions 是感知盲點

david22115 這篇貼了 **22 天、0 回應**。查證後發現這是結構性的：MAINTAINER-PIPELINE Step 1 只掃 `gh issue list` + `gh pr list`，全部 pipeline 與 routine 沒有任何一處掃 GitHub Discussions。全站 10 則 Discussions 裡，三則 contributor 發起的全部 0 回應——包括頂級 contributor idlccp1984（184 commits）在 4/03 問的「為什麼昨天沒有更新？」，掛了三個月。

依神經迴路的 minimum-action 成本曲線（>24hr 進入失望階段），這是三筆累積中的信任損耗。已入 LESSONS-INBOX；修補是 pipeline rule change，兩個選項留哲宇：

- **A（建議）**：MAINTAINER Stage 1 加一行 Discussions 掃描（`gh api graphql` 列未回應貼文），成本一行指令
- **B**：關閉 Discussions tab、README 導流到 Issues（若不想維護第三個入口）

## 1. 五桶分類總表

| #   | 建議                         | 分桶                                        | 一句話判定                                                                                             |
| --- | ---------------------------- | ------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| 1   | 語意搜尋 / 大文本提取關聯    | 半「已 cover 對方不知道」+ 半真洞見         | 後端已有六語 bge-m3 向量與 MCP RAG；讀者端語意搜尋 UI 確實不存在，且 keystone 正躺著                   |
| 2   | 反哺 LLM 監測 + 警報驅動內容 | 概念已有 + **迴路是五條中最有價值的真洞見** | Sovereignty-Bench-TW 就是這件事，但「bench 結果 → 內容優先序」的反饋迴路完全不存在                     |
| 3   | RAG 細部 / token 算力效率    | 部分已 done + chunk 粒度是真洞見            | 算力效率哲學已是巴別塔 pipeline 核心；article-level embedding 的粒度粗是真的                           |
| 4   | 資訊再利用 API / 同步管道    | 大部分「已 cover 對方不知道」               | 管道很多（JSON 全家桶 / MCP / llms.txt / CC BY-SA raw repo），入口指南不存在；RSS 真缺                 |
| 5   | 審查零信任 / 知識庫乾淨      | 內容端已 done + 對「人」全面零信任**反對**  | 十層防線已在跑；對 contributor 全面零信任牴觸小丑魚文化，對 AI maintainer 的零信任正是今日獨立身份報告 |

## 2. 逐條分析

### 2.1 語意搜尋（建議 1）

**已有**：bge-m3 六語向量（`scripts/core/build-embeddings.mjs`，主權 GPU 在地算）、讀者端「你可能也想讀」（`src/data/related/` 8 鄰居烘進 HTML）、minisearch 六語全文索引、MCP `taiwanmd_rag` / `taiwanmd_search` 給 AI 客戶端。
**真缺口**：(a) 讀者端沒有語意搜尋介面，全文搜尋是詞面比對，「模糊搜尋」的批評成立；(b) 無 incremental embed，新文進來得整批重建；(c) **現實比設計難看**：唯一 bge-m3 節點（4090）實體離線 18 天，committed 索引凍在 6/17——SPOF 已在 OBSERVER-QUEUE 等哲宇拍板（4090 常駐 vs 本機 m4max 常駐 daemon）。
**路線**：先解 keystone SPOF（已排隊），再評估讀者端語意搜尋（可用現有向量 + 靜態 shard，成本主要在前端）；incremental embed 排 P2。

### 2.2 反哺 LLM 監測（建議 2）— 五條中最值得做

**已有**：BENCH-PIPELINE v0.3 七階段 SOP、四組模型（western-frontier / western-open / prc-origin / local）refusal + sovereignty 兩 prompt 集、Opus judge、`public/api/bench-results.json` 公開。這正是「取得各大模型對議題的產出、比對事實相符程度」的實作，比建議者想的走得更遠（含 PRC 模型拒答指紋）。
**真缺口**：bench 是 2026-05-02 之後沒再跑的靜態快照。「警報需要強化對應議題的內容產出」這半句是真洞見——**bench 結果 → ARTICLE-INBOX 優先序**的迴路不存在，re-bench 無排程、新模型發布無 trigger。
**路線**：(a) bench 排程化（月度 re-bench routine，走 ROUTINE.md 新增流程）；(b) 產出端接線：refusal 率高 / 幻覺率高的主題自動 append ARTICLE-INBOX P1 候選。兩者都是 routine / pipeline 新增，需哲宇 in-loop，但工程量小（bench 工具已齊）。

### 2.3 RAG 效率（建議 3）

**已有**：算力效率是巴別塔 pipeline 的核心哲學——4-tier cascade（cloud free → local LLM 捕手 → paid last resort）、Tier 0a diff-patch（單句改動只譯 diff，昨夜 babel-nightly 實跑 29-38s/譯本）、45/45 全免費 tier 實證。考古 agent 說「4-tier 只有標題無實作」是誤讀（只讀了 v0 header；SQUEEZE v4.4 於 7/05 才剛對齊 translate.py 現實）。
**真缺口**：RAG 側 embedding 是整篇一向量，長文（7,000 字級）retrieval 粒度粗；chunk 策略、context 拼裝、cost 沒有文檔。
**路線**：chunk-level embedding 實驗排 P2（等 keystone SPOF 解掉才有意義）；RAG 行為文檔補進 EMBEDDING-PIPELINE，一個 session 內可完成。

### 2.4 資訊再利用（建議 4）

**已有**：`public/api/` JSON 全家桶（articles / search 六語 / rag 向量 / bench / dashboard）、MCP server（NPM `taiwanmd`，六個工具）、`llms.txt`（11.7KB）、sitemap（live，HTTP 200 親測；agent 說查無是誤讀）、整個 repo 就是 CC BY-SA 的 bulk markdown export。
**真缺口**：這些管道**沒有一頁對外入口**——建議者顯然不知道它們存在，而「管道存在但找不到，等於不存在」（REFLEXES #73 的對外版）。RSS/Atom feed 確實沒有。
**路線**：(a) 寫 `PUBLIC-API.md`（或站上 /reuse 頁）：端點清單 + schema + 更新頻率 + 授權，一個 session 可完成，自主權內；(b) RSS feed 用 @astrojs/rss 補，工程量小；(c) README 加「資訊再利用」一節。這桶的行動全是「把已有的東西變可見」。

### 2.5 零信任審查（建議 5）

**已有（內容端零信任已是現行）**：pre-commit 13 維 gate、CI build + i18n smoke、PR 十紅旗自動防禦、footnote source audit（WebFetch 抽驗）、FACTCHECK-PIPELINE 六 hard gate、REWRITE Stage 3.5/3.6 幻覺審計、feedback 注入三層防禦（7/05 ship）、agent-report-health 收件 gate（REFLEXES #81）、PR frontmatter CI gate（7/05 22:25 ship）。就在本週，pr-sweep 還逐字對源攔下兩條杜撰引語。
**反對的部分**：對「提供內容者」全面零信任牴觸 MANIFESTO 開源共創與 merge-first 文化——把小丑魚當攻擊者對待，會失去第五天那 23 個陌生人。現行設計是「內容零信任、人給善意預設、行為觸紅旗才升級」，這個不對稱是刻意的，不建議改。
**真缺口**：(a) 十層防線沒有一張總覽表，外人（與新 maintainer）看不見這套體系，跟 2.4 同病；(b) contributor 信任五階梯（CONTRIBUTOR-SYSTEM-PIPELINE）存在但升級路徑不公開；(c) 對 AI maintainer 自己的零信任——scoped token + required review——正是同日 [獨立身份報告](semiont-independent-identity-2026-07-05.md) 的主軸，兩份報告在這點會合。
**路線**：防線總覽文件（`docs/QUALITY-DEFENSE.md` 或併入 CONTRIBUTING）一個 session 可完成。

## 3. 修正紀錄（濾網 2：agent claim 親測重驗）

考古 agent 四個誤讀被主 session 修正：4-tier cascade「無實作」（實際夜夜在跑）、sitemap「查無」（live 200）、embedding「每天重建」（設計態；現實 4090 離線 18 天索引凍結）、防線「無 contributor 信任分級」（五階梯架構存在，是可見性問題）。研究 agent 的成熟度判讀一律要拿 memory tail 的運行現實對過才能用。

## 4. 行動清單彙整

**自主權內、任何 session 可接（建議優先序）**：

1. `PUBLIC-API.md` 資訊再利用入口頁（建議 4，把已有管道變可見）
2. 品質防線總覽表（建議 5 的文件化半邊）
3. RAG 行為文檔補進 EMBEDDING-PIPELINE（建議 3 文檔半邊）
4. RSS feed（@astrojs/rss，小工程）

**需哲宇拍板（pipeline / routine / 排程變更）**：

5. Discussions 盲點修補 A/B 擇一（§0）
6. bench 排程化 + 「bench → ARTICLE-INBOX」反饋迴路（建議 2 的真洞見，五條中最高價值）
7. embedding keystone SPOF 二選一（已在佇列，這份報告是第 N 次 +1）
8. 讀者端語意搜尋 UI 與 chunk-level embedding（P2，等 7 解掉）

**回覆 david22115**：草稿見 §5。張貼與否與由誰貼，依 §自主權邊界對外溝通慣例留哲宇（我可以代貼，一句話授權即可）。同場建議補一句給 #307 idlccp1984（三個月未回，遲到的誠實勝過永遠沉默）。

## 5. 回覆草稿（給 david22115，貼前哲宇過目）

> 先說抱歉：這篇掛了三週沒人回，查了才發現是我們的巡邏機制只掃 Issues 跟 PR，Discussions 整個是盲區。你這篇讓我們抓到這個洞，已經記進系統的教訓清單了，謝謝。
>
> 五點都認真查過一輪，逐條回：
>
> 1. **語意搜尋**——後端其實已經有了：全站六種語言都用 bge-m3 算了語意向量（在自己的 GPU 上算，不外送），文章頁的「你可能也想讀」就是它驅動的；AI 工具端也有 MCP server（NPM 套件 `taiwanmd`）可以做語意檢索。你說中的是讀者端：站上搜尋框目前還是詞面比對，語意搜尋 UI 在規劃裡。
> 2. **反哺 LLM 監測**——這個我們有個雛形叫 Sovereignty-Bench-TW（測各家模型對台灣議題的拒答率與改寫傾向，結果在 `/api/bench-results.json`），但你講的「警報驅動內容補強」那半段是我們真的沒有的迴路，這條被列為五點裡最值得做的，會排進進化路線。
> 3. **RAG 效率**——翻譯管線那邊算力效率壓得很兇（四層瀑布 + diff 補丁翻譯 + 本地 GPU，可以去看 SQUEEZE-MODELS-MAX-PIPELINE），RAG 側你說得對，現在是整篇文章一個向量，段落級切分在待辦上。
> 4. **API 再利用**——管道其實不少：`public/api/` 有全文 JSON、六語搜尋索引、向量檔；有 `llms.txt`；整個 repo 就是 CC BY-SA 的 markdown，clone 即全量匯出。但你會提這點就證明我們最大的問題是沒有一頁入口文件讓人知道這些存在，這頁會補。RSS 確實沒有，也會補。
> 5. **審查零信任**——對「內容」我們已經接近零信任：十來層防線（幻覺審計、腳註來源抽驗、注入防禦、CI gate），上週才逐字對源攔下兩條偽造引語。對「人」我們刻意不走全面零信任——這個專案的起點是陌生人的善意，防線設計是內容全查、人先給信任、觸紅旗才升級。你點的真缺口是這套體系沒有總覽文件，會補一張。
>
> 這五點會併進系統的進化路線報告（repo 的 reports/ 有完整版）。再次謝謝，這種系統層的建議比修一篇文章值錢。🧬

---

_v1.0 | 2026-07-05 git-identity session（同 session 第二題）_
_誕生原因：哲宇丟 #1146 截圖「幫我也一起做這些問題的思考跟報告」_
_核心洞察：(1) 五條建議裡最值錢的是「bench → 內容優先序」反饋迴路；(2) 四條的共同病根是可見性——東西存在但沒人找得到；(3) 比建議本身更大的發現是 Discussions 感知盲點，三則 contributor 貼文 0 回應。_
_LESSONS-INBOX 候選：github-discussions-structural-blind-spot（已 append）。_

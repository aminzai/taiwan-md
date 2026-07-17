---
stage: 2.5-source-fidelity
slug: 為什麼台灣需要自己的知識庫
article: knowledge/About/為什麼台灣需要自己的知識庫.md
staging: reports/article-evolve/為什麼台灣需要自己的知識庫.md
method: 道1 逐 footnote falsification（獨立 clean-context agent，全 21 外部來源逐一 fetch/curl 比對）+ 道3 heal 複驗
date: 2026-07-17
verdict: heal-complete
---

# 為什麼台灣需要自己的知識庫 — Stage 2.5 source-fidelity（道1+道3）

獨立 falsification agent 逐一查核全文 25 footnote（4 內部 taiwan.md/api 依約不 fetch，21 外部全部開啟比對，3 個 403 以 curl+UA 突破）。**13 hold、7 drift、1 fabricated、1 unreachable**。全部已 heal 或留痕，drift/fabricated 清零。

## 分級 + 處置

### 🔴 fabricated（1，最嚴重，已修）

| #   | 破口                                                          | 查核真相                                                                                  | heal                                                                                                                                                                      |
| --- | ------------------------------------------------------------- | ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ^3  | 維基佔 ChatGPT 引用「7.8%／單一最大／Profound／十億筆」四細節 | qvery.ai 實為 **2.49%／第三大網域（次於 google.com+品牌官網）／研究者 Qvery／無「十億」** | 正文改「在 ChatGPT 引用的所有網域裡長期排進前三名」；footnote 改正 2.49%/第三大/Qvery。**根因＝研究材料 external-raw 本身誤植 7.8%**，writer 忠實沿用，falsification 攔下 |

### 🟠 drift（7，facts 真但來源不精，已修）

| #   | drift                                                                                                    | heal                                                                                                                                                                                                 |
| --- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ^23 | 百度百科「文革/天安門 2013 完全不存在」——實為六四查無、文革**存在但被鎖定淨化**；且引的維基 URL 不談百度 | 正文改「天安門（六四）查無、文革被鎖定淨化」；footnote 補[公民實驗室 2013 Jason Q. Ng 研究](https://citizenlab.ca/research/a-large-scale-comparison-of-wikipedia-china-with-hudong-and-baidu-baike/) |
| ^6  | 四日期（10/6-10/12）全掛在一份只講 10/10 的聲明、且無「下架」字樣                                        | footnote 拆分：10/9 下架見端傳媒（^5）、10/12 備詢見公視，聲明本身只承擔 10/10                                                                                                                       |
| ^11 | 99.57/81.34/61.16 數字不在 Khoury 新聞頁、在論文；「我知道」bypass 誤譯                                  | footnote 改引[arXiv 2505.12625](https://arxiv.org/abs/2505.12625) Table II；bypass 正名「Okay, the user is asking…」思考起手式                                                                       |
| ^16 | 6億/200機關不在 twreporter；「訂正 11 億字」邏輯錯（twreporter 自身即寫逾 11 億，是不同時點非誤植）      | 正文＋footnote 去掉單一數字之爭，只取「上百機關、正體中文」各源一致的定性；侯宜秀逐字引語保留                                                                                                        |
| ^19 | GoLaxy「范德堡＋台灣民主實驗室共同揭露」過度歸屬                                                         | 改「文件由范德堡研究者 Goldstein/Benson 取得、NYT 2025-08-05 首報，台灣民主實驗室發布分析」                                                                                                          |
| ^21 | S$70M/US$52M/十一語/主權 不在 sea-lion.ai/about                                                          | 正文去金額，footnote 標「金額見 govinsider 等報導、非官方頁所載」                                                                                                                                    |
| ^4  | tw-figure「716 萬」vs footnote「720 萬」內部不一致                                                       | 統一為實測值 **721 萬**（7,209,592）                                                                                                                                                                 |

### 🟡 輕微字面（4，已順修）

- ^2 論文標題漏中段 → 補回全名（Affordable Adaptation of LLMs on）。
- ^5 蔡明順引語字序異動 → 去引號改「指…」轉述。
- ^13 張競頭銜漏「資深」→ 正文＋footnote 補「資深研究員」。

### ⚪ unreachable（1，留痕）

- ^25 Cofacts：WebFetch+curl（含 UA 偽裝）皆 403 bot 防護，無法逐字。第三方（NPOst/TFC）內容一致、不矛盾。**保留**：這條的論點（無專為 AI 對話設計的回報機制）正是正文結尾「目前沒有好管道」的自證，性質描述經第三方佐證。

### ✅ hold（13）：^2 ^4 ^5 ^7 ^9 ^10 ^12 ^13 ^15 ^17 ^18 ^22 ^24

- 高信心逐字命中：^5 CKIP 四答（習近平/復旦上海/國籍中國/10月1日）、^7 RIL 七模型 2/3 token、^9 Pan@Stanford／Xu@Princeton **校名沒寫反**、^10 RSF 換語言不變、^12 CEIAS 六數字、^17 曹永和「第四位」、^24 DeepSeek 662 words/兩秒刪除。

## 門面句（title/description/30 秒概覽）

三處互相一致、與查核吻合；核心具體事實（40 bytes 拒答＋中研院「我國領導人是習近平」）皆逐字命中。thesis 句（「不是被偷，是被沉默」）為論述非既成事實指控，無專名錯置。**門面層 0 錯誤**。

## 道3 heal 複驗

18 處 heal 全部採用 falsification agent 已 fetch 驗證的正確值（非二次推測）。heal 後複跑：

- `--profile=rewrite-stage-3-5`（footnote-format/density/correction-meta/quote-fidelity）：**hard=0**。
- `--check=prose-health`：score **3 ≤ 3 = pass**（未人工審核 +1、破折號 15 +2；對位收斂至 1＝title thesis）。

**裁決**：drift/fabricated 清零，Stage 2.5 通過，主 session 覆蓋 canonical 進 Stage 3。此輪最大教訓＝research raw 的 7.8% 誤植若無逐 footnote falsification 會直接 ship（REFLEXES #31 sub-agent claim 是線索不是 oracle 的第 N 次驗證）。

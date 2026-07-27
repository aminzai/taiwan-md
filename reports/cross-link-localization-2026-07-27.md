# 譯文的站內連結沒有在地化 — 調查與修復計畫

> 2026-07-27，驗證 `patch-translate.py` 時發現。**非該工具造成的迴歸**，是三個
> 翻譯引擎共有的既存缺口（translate.py / structured-translate.py / patch-translate.py
> 都指示模型「URL 原樣保留」——對外部引用正確，對站內連結錯誤）。

## 損害規模：13,155 個連結，跨十一語

| 語言     | 站內連結總數 | 含中文 slug |    佔比 |
| -------- | -----------: | ----------: | ------: |
| en       |        2,536 |       1,521 |     59% |
| ja       |        2,692 |       1,891 |     70% |
| ko       |        2,630 |       1,858 |     70% |
| es       |        2,838 |       1,955 |     68% |
| fr       |        2,616 |       1,888 |     72% |
| vi       |          623 |         502 |     80% |
| id       |          848 |         654 |     77% |
| pt       |        1,201 |         994 |     82% |
| hi       |          750 |         651 |     86% |
| ar       |          693 |         600 |     86% |
| ru       |          723 |         641 |     88% |
| **合計** |   **18,150** |  **13,155** | **72%** |

另有 4,024 個是拉丁 slug 但缺語言前綴（`/music/foo` 而非 `/en/music/foo`）。
新生語言比例更高（ru 88% / ar 86% / hi 86%），因為它們全部由現行引擎產出，
沒經歷過任何早期的修補。

## 這些連結真的壞掉

實測線上（非推測）：

- 譯文裡寫的 `/en/Music/拍謝少年`、`/en/music/拍謝少年`、`/Music/拍謝少年` → 全部 **404**
- 同一篇文章的正確英文網址 `/en/music/taiwan-rock-from-underground-to-mainstream` → **301**（正常）

`generate-article-aliases.mjs` 的 alias 機制解決的是另一個方向的問題（讀者把
中文網址加上 `/en/` 前綴的猜測），不涵蓋「譯文內文指向中文 slug」這一類。

## 修復所需的資料完全具備

`knowledge/_translations.json` 就是 `lang/path → zh/path` 的完整對照表
（6,864 筆），反查即得 zh slug → 各語 slug。`prepare-batch.py` 早就用它解析
Obsidian 式 `[[wikilink]]`，只是沒涵蓋一般 markdown 連結 `[文字](/分類/中文slug)`。
`optimized-translate.py` 有 `rewrite_cross_links()` 做過這件事，但那個引擎沒接在
現行 dispatcher 上。

## 建議修復計畫（分兩段，先做第一段）

**第一段：存量批次修復（純機械，零模型呼叫）**

新工具 `scripts/tools/lang-sync/localize-cross-links.py`：讀 `_translations.json`
建立 `zh_slug → {lang: lang_slug}` 索引，掃描譯文的 `[text](/path)`，中文 path
反查對應語言的 slug 後改寫、補語言前綴。判準保守：

- 查無對應譯文（該語言還沒翻）→ **不動**，留中文 slug（改成猜測的 slug 會製造新的 404）
- URL 含 `http` → 不動（外部引用）
- 錨點（`#section`）保留

分語言批次，每批跑 `article-health --profile=ci-deploy` 與抽樣線上 curl 驗證。

**第二段：翻譯引擎前置處理（防新增）**

在三個引擎的 body 送模型「之前」就把站內連結改寫好（與 URL token 化同層），
模型看到的已經是目標語言網址，「URL 原樣保留」的指示自然正確。這比事後
修復穩健，也不必動模型 prompt 的語意。

**第三段（可選）：閘門化**

`verify-translation.py` 加一項「站內連結不得含中文 slug（該語言已有譯文時）」，
讓它不再靜默出貨。

## 風險

- 連結文字（`[文字]`）已經是譯文，只改 URL 不影響閱讀
- 跨批次時序：A 篇連到 B 篇，而 B 篇還沒翻 → 保守規則會留中文 slug，下次
  批次修復時自然補上（與 CRON-ROUTINE 記載的既有處置一致）
- 13,155 筆改動需分語言 commit，避免單一巨大 diff

🧬

---

_v1.0 | 2026-07-27_
_誕生原因：patch-translate.py 驗收時的意外發現_
_核心洞察：「URL 原樣保留」對外部引用正確、對站內連結錯誤——同一條指示在兩種 URL 上的正確性相反，而閘門完全沒有檢查這一類_

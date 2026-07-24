# research-fleet 設計報告（2026-07-24）

## 觸發

外送專法 Stage 1 研究派 4 個平行 Sonnet 研究 agent（facet A-D），合計燒約 500K token；3 個在收尾階段撞帳號 session limit（僥倖已落檔才被截斷）。同時 4 份分部報告一致回報同一個卡點：law.moj.gov.tw（全國法規資料庫）逐條原文無法取得——WebFetch 對這個網域有「125 字截斷」政策，PDF 二進位內容完全無法解析。

哲宇提出的方向：Stage 1 大部分是機械勞動（搜尋、開頁、抓文字），不需要 Sonnet 判斷力，應該把這部分移出 Claude 計量；並要求對「search」這件事做抽象介面統整多服務，不綁死單一供應商。

## 市場調查（2026-07-24 即時查證，非記憶）

| 服務                          | 狀態                                                        | 備註                                                     |
| ----------------------------- | ----------------------------------------------------------- | -------------------------------------------------------- |
| Bing Search API               | **已於 2025-08-11 全面退役**，無法新申請                    | 排除                                                     |
| Google Custom Search JSON API | 2025 年關閉新戶申請，2027-01 到期                           | 排除（新建案不可用）                                     |
| Brave Search API              | 2026-02 起取消免費額度，改全面計量計費（$0.003-0.005/查詢） | 哲宇提供金鑰，已驗證可用                                 |
| Serper.dev                    | 2,500 次免費額度，之後 $1/1000 查詢起                       | 哲宇提供金鑰，已驗證可用，鏡射真實 Google 索引含繁中結果 |
| Tavily                        | 1,000 次/月免費（含內容擷取）                               | 未採用（雙鍵管理成本 vs 單一 bundle 的取捨，暫不需要）   |
| Jina Reader (r.jina.ai)       | 免金鑰可用（~20 req/min），有金鑰 1M-10M token 免費         | 已驗證：含 PDF、JS-render 頁面轉乾淨 markdown            |

## 實作

`scripts/tools/research-fleet.py`：`SearchProvider`（`BraveSearch` → `SerperSearch` cascade）與 `FetchProvider`（`MojLawFetch` 全國法規資料庫專用 parser → `JinaFetch` 通用 fallback）兩個抽象介面，`search` / `fetch` / `batch` 三個 CLI 子指令。

### 除錯過程（真實踩坑，供未來對照）

1. Brave API 對含中文的 query string 直接串進 URL 會回 400——需用 `curl -G --data-urlencode` 或 Python `urllib.parse.urlencode` 正確編碼。
2. law.moj.gov.tw 的憑證鏈缺 Subject Key Identifier，Python 預設嚴格 SSL context 拒絕（curl 系統憑證庫較寬容）——對此網域用範圍限定的寬鬆 SSL context（僅讀公開法規文字，無憑證涉入）。
3. Jina Reader 對 urllib 預設 User-Agent 回 403——補上真實 User-Agent header 即解。
4. law.moj.gov.tw 的文章編號在獨立 `<a name="N">第 N 條</a>` 標籤（`col-no` 欄），內容在同一 row 的 `col-data`——正則直接抓兩者配對，零 LLM 成本取得逐條 verbatim + 條號。

### 驗證結果

- `fetch` 對外送專法母法：28 條全數取得，含先前 4 個 Sonnet agent 都拿不到逐字的第 8/9/10/11 條（第 9 條甚至挖出全新細節：申訴獨立小組須 ≥3 人、其中工會代表至少 1 人——原研究完全沒抓到）。
- `fetch` 對政府 PDF（施行細則草案總說明）：Jina 成功轉出可讀文字，WebFetch 先前對同類 PDF 完全失敗。
- `batch` 對 5 條缺口查詢跑通，7 個來源全數落檔；保險最低金額仍未公開（誠實記為未解，非工具失敗）；CNA 網頁版因重度 JS render 只拿到導覽列，記為已知限制。

## 架構決策：抽象介面而非一次性腳本

`SearchProvider` / `FetchProvider` 是可抽換實作，呼叫端不認供應商名字只認介面——這正是 2026-05-13 babel backend abstraction v4（讓翻譯模型可抽換）同一原則第二次落地在完全不同的服務類別（search/fetch，非 LLM）。已寫入 [MANIFESTO §架構解 > 守備修補 第二例證](../docs/semiont/MANIFESTO.md#我的進化哲學--架構解--守備修補)，vc=2（跨兩個服務類別驗證），第三次出現時應收進 DNA.md 骨架設計規範。

## 產出

- `scripts/tools/research-fleet.py`（新工具）
- `docs/pipelines/RESEARCH-AGENT-PROMPT.md` v1.2（新增 Path B 章節）
- `docs/semiont/MANIFESTO.md` v1.13（§架構解新增第二例證）
- `~/.config/taiwan-md/credentials/.env` 新增 `BRAVE_API_KEY` / `SERPER_API_KEY`（repo 外，per 既有 credentials 慣例）
- `reports/research/2026-07/外送專法.md` 研究報告本身（Stage 0+1 手動 fan-out，四份分部報告已合成，gate PASS，hard_fail=0）

## Digest 步驟補完（同日第二階段）

新增 `DigestProvider` 抽象介面：`OpenRouterDigest`（免費層，key rotation 沿用 lang-sync 同一組 credentials）→ `OllamaDigest`（本機 GPU，沿用 `backends/ollama.py` 的 `num_ctx` 動態估算，防止今天稍早那個「靜默截斷成 4096」的 bug 重演）。`digest` 子指令把 `batch` 的 raw JSON 逐一丟進 digest cascade，輸出跟 Path A Sonnet agent 同格式的 markdown（【來源】/【逐字】/【信度】/【falsify 註記】），直接可過 `agent-report-health.py`。

實測用外送專法二次補查的 7 個來源跑 `digest`：第一輪撞到 `openai/gpt-oss-120b:free`（lang-sync 自己的預設模型）已被 OpenRouter 下架，改用 `google/gemma-4-31b-it:free` 後兩個原本失敗的來源（一個 429、一個逾時）全部成功，5/7 → 7/7。過程也發現 §1 搜尋軌跡若只印「N 次查詢＋命中數」（5 行）會被 `agent-report-health.py` 判定軌跡密度過低（<10 行分界），改成逐查詢下面嵌對應來源 URL＋擷取狀態（誠實展開已有資料，非灌水），12 行後過關。

## 未做（誠實記錄邊界）

- Digest 品質受限於 free-tier 模型，高風險 atom（人名/金額/獎項屆次）仍建議 Path A 或人工複驗，不當定論。
- OpenRouter 免費模型 slug 會退役（本次建置期間就撞到一次），`DEFAULT_MODEL` 需定期對照 `GET /api/v1/models` 校準，暫無自動化偵測。
- 未接 crawl4ai（本機瀏覽器爬蟲）——哲宇提及此選項，評估為「本地算力軍團」的合理下一階，但需要安裝 Playwright + Chromium（較重的環境變更），暫列為 Tier 2 候選，不在本次範圍內動手裝。

_v1 | 2026-07-24-120515-manual session_
_v1.1 | 同日續 — digest 步驟補完，Path B 三段式（search→fetch→digest）全通_

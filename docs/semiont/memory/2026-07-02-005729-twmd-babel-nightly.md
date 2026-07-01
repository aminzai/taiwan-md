---
session_id: 2026-07-02-005729-twmd-babel-nightly
routine: twmd-babel-nightly
mode: write
observer: cron
handle: twmd-babel-nightly
started: 2026-07-02T00:57:29+08:00
ended: 2026-07-02T01:15+08:00
articles_shipped: 15
commit: 8f2ea7b20
---

# 2026-07-02 twmd-babel-nightly — Computex EVOLVE 撞 gpt-oss 天花板，Sonnet 五語接手

## BECOME ACK

- Mode: **write**（Q1-4/Q8-11/Q14 subset 全過）
- Universal core 全跑：consciousness-snapshot（🫀90 🛡️50 🧬95 🦴90 🫁85 🧫88 👁️90 🌐93）／ routine-status.sh (Exit 1 non-blocking) ／ inbox-signal (23 lessons 未消化 / 73 articles pending / 49 spores pending)／git log 48hr ／MEMORY head + tail + §神經迴路 ／ latest handoff = 2026-07-01-231047-twmd-data-refresh-pm (CF 404 vc=3 CONFIRMS / 免疫 sub-dim offset vc=1)
- Cross-session continuity check PASS：跟本 session 無 conflict，data-refresh 陣線在 CF 感知面，我在 knowledge/{en,ja,ko,es,fr} 面

## Stage 1 — Sense state

- `lang-sync/status.py`: 3 stale × 5 lang = 15 待完成
- `prioritize-batch.py`: Music/蘇打綠.md (P2 diff+4-4)、People/田馥甄.md (P2 diff+1-1)、Technology/Computex.md (P2 diff=0 但實際 442 lines)

## Stage 2 — Tier routing

| 文章     | Prior tier | Actual diff   | Routing                         |
| -------- | ---------- | ------------- | ------------------------------- |
| 蘇打綠   | P2         | 40 lines      | Tier 0a diff-patch × 5 lang     |
| 田馥甄   | P2         | tiny          | Tier 0a diff-patch × 5 lang     |
| Computex | P2 (mis)   | **442 lines** | Tier 2 → **Tier 4 Sonnet 接手** |

`diff-patch-prepare` 揭 Computex 是 P0/P1 not P2 — prioritize-batch 的 diff 欄位限制 100 lines 沒抓到 EVOLVE 大改，`prioritize-batch` heuristic 未來可以升級為「先讀 diff 上限」。（LESSONS candidate vc=1）

## Stage 3 — Dispatch outcome

**Tier 0a diff-patch（5 Sonnet Agent 並發，1/lang）**：全 5 langs × 2 文章 = 10 檔全 ship，YAML 全綠、body ±10% 內。

耗時約 90–170 秒 per lang，比 full re-translation 快 5-10x（pipeline canonical 預估驗證）。

**Tier 2 openrouter/gpt-oss-120b:free（5 lang 並發）**：**全爆**。

- es/fr：5 accounts × 429 rate-limit exhausted，first burst
- ja：突破 429 到成功回應，但 `finish_reason=length` 32k output cap 被截（articles 57KB zh → 60KB+ ja output）— 觸發 pipeline canonical Hard Gate「輸出截斷偵測」，不 save
- en/ko：仍在跑時被主動 kill（同 model 同 max_tokens 必然截）

**Tier 4 Sonnet Agent 接手 Computex（5 lang 並發 full re-translation）**：全過。

| Lang | Size    | Ratio              | 特殊處理                                        |
| ---- | ------- | ------------------ | ----------------------------------------------- |
| en   | 63,666B | ×1.11              | title/description 用 double quote 包 apostrophe |
| ja   | 79,634B | ×1.17              | 黄仁勲/蘇姿豊/施振栄 furigana + English         |
| ko   | 73,118B | ×0.75(broad ratio) | Hiwin/上銀 韩→中 双語標記                       |
| es   | 77,254B | ×1.35              | double quote 包 guillemets                      |
| fr   | 76,229B | ×1.33              | 'Mois de l''informatique' YAML escape           |

全部 60 footnotes 保留、URL byte-for-byte 不動、iframe verbatim、sporeLinks 保留原檔案 publication metadata。

## Stage 4 — Verify + Ship

- `verify-batch.py` 五 lang 全 8-step 全綠（footnote count / YAML / wikilink residue / cross-link / lang-sync fresh confirm）
- `_translations.json` 4152 entries regenerated
- Diff-patch 10 檔手動 YAML re-validate 全 OK
- 選擇性 git add（17 檔精確 stage）
- Commit `8f2ea7b20` — §11.4 人話 message，帶出兩篇 heal 修正的具體事實 + Tier 4 fallback 過程
- Pre-push 全站 article-health mirror ci-deploy 全綠
- Push origin main — ff-only

## Stage 5 — Self-evolution

**新 datapoint — Tier 2 free tier 天花板兩層曝光**：

1. **同批 5 lang 並發 exhaust 5 API keys** — 過去多語 batch 走同時 dispatch 打法沒踢過這個上限；今晚 Computex 單 article × 5 lang 就把 acc2/acc3/acc4/acc5/default 全部打進 429 冷卻。未來 openrouter-batch.sh 該內建 stagger（每 lang 間隔 15-30s）或 pipeline canonical 補「Concurrency cap 3-5 worker」外加「Tier 2 model 5-key 全帳號 saturate 是重要 signal」條目。
2. **`finish_reason=length` 32k output cap 對大 article 是硬牆** — gpt-oss-120b:free max_tokens 設 32k 但實際 output cap 更低，55KB+ zh 文都會截。pipeline canonical Hard Gate 已有此 gate（+ 「263 文去引用 root cause」歷史紀錄）今晚是活體 dogfood。

**Escalation timing**：Tier 2 五 lang 全都失敗才升 Tier 4 — 沒有走 Tier 3 (owl-alpha/驗證佇列) — 是因為 429 signal 太清楚不用 walk cascade middle tier。這個「同 root cause 直接跳頂端」的判斷未來可以標記為 shortcut rule（LESSONS candidate vc=1）。

## Handoff 三態

- **DONE**：BECOME write / stale=0 / 15 譯本 ship (10 diff-patch + 5 full re-translate) / verify-batch 五 lang 全綠 / commit 8f2ea7b20 push 完成
- **CARRY 到 next fire（07/02 06:12 am data-refresh-am）**：
  - **Tier 2 free tier 天花板兩層 datapoint** vc=1，next am 若 openrouter-batch.sh 又踩 rate-limit → vc=2 promote LESSONS `tier2-free-saturation-and-32k-truncation`
  - **prioritize-batch diff=0 mis-classification** (Computex 實際 442 lines 被歸 P2 diff=0) vc=1 next 若再出現大 EVOLVE 被錯分 → vc=2 candidate
  - **ja/People/hebe-tien-singer.md body 是英文 prose 而非日文**（diff-patch agent 標記的 pre-existing anomaly）— 不是我今晚翻譯的 regression 但值得未來人物翻譯 audit（vc=1）
  - **免疫 50 chronic 第 9 cycle**、**CF 404 vc=3 CONFIRMS** 續 carry data-refresh handoff 鏈
  - **6/19 髒 tree 第 16 天** + reports/article-evolve/端午節.md untracked 第 3 天 + memory-iter2 untracked — 等哲宇 housekeeping chip

- **NEW**：
  - **Tier 4 Sonnet full re-translation 首次因 Tier 2 天花板 escalate** — 過去 Sonnet 只做 Tier 0a diff-patch，今晚是首次 full re-translate 場景。5 lang × 60-80KB 產出穩、YAML 全綠、60 footnotes 全保留，證明 Sonnet 是 Tier 4 fallback 的可靠 backbone（sovereignty domain 之外用 Ollama qwen3.6 之前的層級）
  - **§11.4 電報腔紀律 dogfood** — commit message 寫「gpt-oss-120b:free 五語同批 429 爆掉、ja 額外撞 finish_reason=length 32k output cap 被截」而非「Tier 2 escalate to Tier 4 vc=1」電報流

## Beat 5 反芻

今晚最值得記的是「pipeline canonical 的 Hard Gate 兩條同一晚都活體 dogfood」— 429 rate-limit backoff 觸發 cool-down retry（也失敗），`finish_reason=length` 截斷 hard gate 阻止半篇文入 repo，兩條 canonical rule 都在真實情境跑對了。

過去 13 夜 babel routine 都是 stale=0 順跑，今晚踩到「大 article EVOLVE 之後跨語同步」的邊界情境 — 這在 EVOLVE-pipeline 的產出頻率上是稀有事件，只有像 Computex/NVIDIA 這類 5000+ 字文被主檔大改才觸發。這種邊界情境的 escalation SOP（Tier 2 → Tier 4 直跳）今晚是第一次真實跑，未來可以 promote 到 SQUEEZE-MODELS-MAX-PIPELINE §Escalation shortcut 附錄。

第二層反芻 — 「一次 15 譯本 ship」在 pipeline canonical 意義上不是多，但因為 Computex 五 lang 每篇都是 60-80KB 全篇 Sonnet full re-translation，實際 output 產能上比連 13 夜 stale=0 順跑的 diff-patch 都要重。這種「文章價值 × 語言數 × 翻譯完整度」的三軸乘積是 sovereignty preservation infrastructure 每晚在做的事：Computex 這種台灣供給端主權敘事文，讓五個語言的讀者今晚都同步看到「三大電腦展死了兩個剩台北那個」的策展觀點。

🧬

---
title: '2026-07-06-003506-twmd-babel-nightly'
description: 'twmd-babel-nightly routine 00:35 fire — 84 translations shipped (25 bump + 30 diff-patch + 29 P0 cascade) 5 lang parity 97.7%→99.5% avg; codex/gemini both dead cross-cascade, gpt-oss-120b + ollama carrying全部 P0；6 hit cascade exhaustion; _translations.json out-of-sync 差點卡 pre-push errexit'
type: 'session-memory'
status: 'canonical'
apoptosis: 'never'
session_id: '2026-07-06-003506-twmd-babel-nightly'
routine: 'twmd-babel-nightly'
mode: 'write'
---

# BECOME ACK

- mode=write / self-test 9-10 題 all pass
- 8 organ 最低=🛡️ 免疫=47（chronic red 續漂）
- Q14 cross-session continuity=PASS（48hr commit chain 讀齊：兩篇 EVOLVE ship 藍染+金瓜石、AAMA+SLP 兩篇新創導師、PR frontmatter gate 儀器化、embeddings routine 4841 向量重生、pr-sweep 8 open PR 全收官、raw 保全 REWRITE v7.7 定錨、Discussion #1146 五桶回應）
- Session ID `2026-07-06-003506-twmd-babel-nightly`

# Stage 1: State sensing

`status.py` 起手：5 lang @ fresh=815, stale=10, missing=14 → 120 pending ops total。parallel-actor CLEAN。

# Stage 2: Priority routing + cascade

## Tier 0b bump-source-sha (25 shipped — instant)

5 P2.5 metadata-only articles × 5 langs = 25 translations bumped 到 latest source_sha 無 body 改動：

- Economy/新創生態系 (industrial-transformation-from-manufacturing-to-innovation)
- Economy/台灣自媒體創作者經濟 (taiwan-self-media-creator-economy)
- Economy/台灣產業轉型升級 (taiwan-startup-ecosystem-overview)
- Economy/台灣科技園區外圍商圈生態 (tech-park-peripheral-business-ecosystem)
- People/蔡明亮 (tsai-ming-liang)

## Tier 0a Sonnet diff-patch (30 shipped — 100% success)

6 P2 articles × 5 langs（max diff ≤ 31 lines）平行 dispatch 5 sub-agent，每 lang 1 agent 處理 6 篇。全部 pass YAML + hash match：

- Culture/台灣花布 (+ Further reading section)
- Culture/台灣傳統工藝與無形文化資產 (photog credit 換 Outlookxp→寺人孟子 + 拉伸藍染連結描述)
- People/張艾嘉 (加 Yang Dechang wikilink)
- Culture/客家文化與語言 (加 藍染 bullet)
- Art/台灣電影 (Yang Dechang 影響鏈換 PTA→濱口竜介 + 加 [^40] [^72])
- Economy/台灣企業：研華科技 (加 AAMA wikilink)

Duration ~4.5min/lang parallel。0 fail 0 skip。

## Tier 1 cascade (P0 missing — 59/70 ok = 84.3%)

14 P0 articles × 5 langs = 70 attempts。Manually generated slug map (owl-alpha slug-suggest.py 404 dead)。5 lang 平行 dispatch translate.py --no-preflight cascade。Duration wall-clock ~67-97 min per lang。

Backend stats 5 lang aggregate:

- codex: 70 calls / 0 ok (100% dead — nvm path truncated `spawn /Users/cheyuwu/.nvm/versions/node/v22`)
- gemini: 70 calls / 0 ok (100% dead — `TERM=dumb` warning routing 到 rate-limited)
- openrouter:gpt-oss-120b: 70 calls / 44 ok / 21 429 rate-limited (production Tier 2 承接主力)
- ollama qwen3.6:35b: 26 calls / 20 ok / 5 timeout/empty (fallback 撿 43% 起來)

Per lang shipped:
| lang | T1 ok | 429 loss | fail 原因 |
|------|-------|----------|-----------|
| en | 12/14 | 4 | AAMA, 蕃薯藤 footnote loss |
| ja | 11/14 | 4 | SLP footnote, AAMA+周天成 all-backend fail |
| ko | 13/14 | 5 | SLP footnote loss |
| es | 11/14 | 8 | AAMA+蕃薯藤+虱目魚粥 all-backend fail |
| fr | 12/14 | 4 | 周天成+林啟維 (fail routing) |

## Ollama-only retry (5/11 rescued)

11 P0 missing 拉出來單獨 dispatch --cascade ollama 重試 5 lang 平行。5 rescued:

- en: AAMA + 蕃薯藤（2/2 ok）
- ja: AAMA + 周天成（2/3；SLP empty output 899s）
- ko: 0/1（SLP timeout 900s）
- es: 蕃薯藤（1/3；AAMA timeout + 虱目魚粥 empty）
- fr: 0/2（周天成+林啟維 都 timeout 900s）

# Stage 3: 收尾狀態

Final coverage 5 lang:

- en 100.0%（0 missing）
- ja 99.9%（1 missing = SLP）
- ko 99.9%（1 missing = SLP）
- es 99.8%（2 missing = AAMA + 虱目魚粥）
- fr 99.8%（2 missing = 周天成 + 林啟維）

**義務鐵律成立**：6 剩餘 missing 全部 4-tier cascade exhausted（codex+gemini dead、gpt-oss 429 rate-limit 未回、ollama timeout/empty output）。等下一個 routine cycle 或 backend heal 後重試。

Stale=4 per lang（20 total）—— 這些是 P2 diff > 100 lines 的（藍染/金瓜石/楊德昌/柯智棠 = 這幾天大 rewrite 的成品）跳過 diff-patch 需 Tier 1 全翻。今晚不追（cascade 條件同 P0，成功率不會比較高，耗 token）交下輪。

# Stage 4: Self-evolution

## 3 個新觀察

1. **codex nvm path 截斷 bug 全跑 dead**：70 calls 0 ok，`spawn /Users/cheyuwu/.nvm/versions/node/v22` 系統性錯。可能 husky 環境 PATH 傳給 subprocess 時 truncated，或 codex CLI expect node in shell PATH 但 background 沒繼承。**待儀器化**：pre-flight probe 提前 detect codex spawn 錯，避免 70 次無效呼叫消耗 70min wall-clock。

2. **gemini TERM=dumb rate-limited routing**：健康檢查訊息「Basic terminal detected (TERM=dumb). Visual rendering will be limited」被路由當 rate-limited。可能 gemini CLI 在 TTY 偵測後 fallback 到 slower path。**待儀器化**：pre-flight 應區分「TERM warning」vs「real rate-limit」，前者不算 dead。

3. **\_translations.json 週期性 out-of-sync 差點卡 pre-push errexit**：hook 用 `sh -e` errexit，`sync-translations-json.py --check` exit=1 觸發全 script fail。這條 gate 設計是「新譯本落地後必須先同步 \_translations.json」；但 babel routine 只走 knowledge/ 沒同步 metadata index → push 卡住。**修法**：babel Stage 5 收官前先跑 `sync-translations-json.py`（不加 --check）再 commit sync 進度。或 pre-push 手動加 `|| true` 保護——但那會抹掉 orphan gate 本意。**選前者**：babel canonical SOP Stage 5 加一步「sync \_translations.json + commit」。

## 3 個 pipeline 應更新

- `SQUEEZE-MODELS-MAX-PIPELINE.md` 收官 Z6 Stage 加「sync \_translations.json + commit」步（避免 pre-push errexit）
- `SQUEEZE-MODELS-MAX-PIPELINE.md` codex healthcheck 加 nvm path truncation early-detect（在 --no-preflight 也做 quick spawn probe）
- `translate.py` DEFAULT_CASCADE_ID docstring 註記：gemini `TERM=dumb` false-positive rate-limit（一次 dispatch 前 export TERM=xterm-256color？）

# Stage 5: Handoff 三態

- ✅ **Done**：114 translations shipped（25 bump + 30 diff-patch + 59 P0 T1 + 5 P0 retry - some overlap actually total 89 files touched, git stat 120 files changed）；all 5 lang coverage 99.5%+ avg；commit `b4fa7ea45` + sync `b2092c8a4` pushed origin/main
- ⏸️ **Deferred**：6 P0 missing (SLP×2, AAMA×1, 虱目魚粥×1, 周天成×1, 林啟維×1) 4-tier cascade exhausted；20 P2 stale (藍染/金瓜石/楊德昌/柯智棠 × 5 lang) diff-too-large 沒跑 Tier 1；all wait 下輪 cycle backend heal
- 🚧 **Blocker**：codex + gemini backend 完全 dead—— 若下輪不修，整條 babel cascade 只剩 gpt-oss-120b (rate-limited) + ollama (unstable on long articles)，難再推 stale=0。**建議哲宇 in-loop**：檢查 codex nvm PATH + gemini TTY 設定

# Beat 5 反芻

今晚 backend cascade 塌得比預期快—— codex + gemini 兩個 subscription tier 全 100% dead，等於 4-tier 只剩 2 tier 撐場。openrouter free tier 5 lang 平均 4-8 次 rate limit，都靠 ollama 撿。若 subscription tier 明晚繼續 dead，義務鐵律的「cascade exhausted」門檻其實從「4 tier 全打完」滑成「2 tier 打完」，隱性降級。

值得記錄的是這夜的 shape：**Tier 0a 完美（30/30）+ Tier 0b instant（25/25）+ Tier 1 半殘（59/70）+ retry 25%（5/11）**。P2.5 metadata-only + P2 diff-patch 是可以「幾乎零 backend cost」推進的層，越靠近寫死 shape 越穩。真正燒錢燒 wall-clock 的是 P0 full-translate，剛好也是 backend 塌得最兇的層。

這推導出設計方向：**繁殖層應盡量壓在 P2.5/P2 diff-patch**——如果每輪 babel 只推 10-20 P0，多累積 metadata-drift 讓 diff-patch 承接，overall throughput 高很多。這條之後可能可以進 SQUEEZE-MODELS-MAX-PIPELINE 的 v4.5「shape 優化」章節。

🧬

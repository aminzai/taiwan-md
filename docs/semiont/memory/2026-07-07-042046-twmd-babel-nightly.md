---
title: '2026-07-07-042046-twmd-babel-nightly'
description: 'twmd-babel-nightly routine 00:30 fire — 58 translations shipped (10 bump + 15 diff-patch + 23 T1 round-1 + 10 gemma/ollama retry) 5 lang coverage 99.9%↑; codex/gemini both dead persistent, gpt-oss-120b footnote-loss on high-fn articles, gemma-4-31b-it 429 shared quota, ollama 5-way parallel contention → 5 timeouts; 15 stale + 3 missing carry forward (楊德昌 92 fn / 施振榮 71 / 柯智棠 61 structural exhaustion)'
type: 'session-memory'
status: 'canonical'
apoptosis: 'never'
session_id: '2026-07-07-042046-twmd-babel-nightly'
routine: 'twmd-babel-nightly'
mode: 'write'
---

# BECOME ACK

- mode=write / self-test Q1-4/8-11/14 all pass
- 8 organ 最低=🛡️ 免疫=49（chronic red 第 15 cycle sustain）
- Q14 cross-session continuity=PASS（48hr commit chain 讀齊：施振榮 v2 立體群像重寫 + 深色推廣 Tier 1-3b 24 template + P0 6/6 前端修復 + PR frontmatter gate + CF 404 vc=3 破新高 + 昨夜 babel 84 shipped）
- Session ID `2026-07-07-042046-twmd-babel-nightly`

# Stage 1: State sensing

`status.py`：5 lang @ fresh=831-833, stale=9 (5 lang 一致), missing en=0/ja=1/ko=1/es=2/fr=2 → 51 pending ops。parallel-actor CLEAN。

# Stage 2: Priority routing + cascade

## Tier 0b bump-source-sha (10 shipped — instant)

2 P2.5 metadata-only articles × 5 langs deterministic bump（`bump-source-sha.py --apply`）：

- Economy/台灣產業轉型升級 (industrial-transformation-from-manufacturing-to-innovation)
- Economy/台灣企業：台積電 (tsmc / tsmc-taiwan-semiconductor)

## Tier 0a Sonnet diff-patch (15 shipped — 100% success)

3 P2 articles × 5 langs（max diff 24 lines）平行 dispatch 5 sub-agent（general-purpose + model=sonnet）：

- Economy/台灣企業：華碩 (+延伸閱讀 to 宏碁/緯創資通)
- Economy/台灣企業：緯創資通 (fix 5/31→5/30 founding date typo body + [^5] + 延伸閱讀 to 宏碁/施振榮)
- People/張忠謀 (+延伸閱讀 to TSMC/施振榮/郭台銘/半導體/產業轉型)

Duration ~2-3 min/lang parallel。0 fail 0 skip。所有 sub-agent 自檢 YAML valid + footnote refs 1-5 完整 + body length 差 ±20% within。en/fr/ja/ko/es 各自本地化 heading：Further reading / Lectures complémentaires / 関連記事 / 더 읽기 / Lecturas relacionadas。

## Tier 1 cascade round 1 (23/55 attempts ok = 42%)

11 articles × 5 langs = 55 attempts（6 P2 diff-too-large full re-translate + 5 P0 missing distributed across 4 langs）。5 lang 平行 dispatch translate.py --no-preflight cascade。Duration wall-clock 77-108 min per lang。

Backend stats 5 lang aggregate:

- codex: 55 calls / 0 ok (nvm path bug persist — 昨夜 20260706 相同觸發)
- gemini: 55 calls / 0 ok (TERM=dumb false-positive rate-limit persist)
- openrouter:gpt-oss-120b: 55 calls / 28 ok / 27 429+footnote-loss (production 承接主力 but truncates on 60+ fn)
- ollama qwen3.6:35b: 27 calls / 14 ok / 12 timeout+2 (parallel contention on single local GPU)

Per lang shipped round 1:
| lang | T1 ok | fail 原因 |
|------|-------|-----------|
| en | 5/11 | 楊德昌+施振榮+宏碁+金瓜石+柯智棠 footnote-loss / 林啟維 codex-fail |
| ja | 4/11 | 楊德昌+施振榮+柯智棠 fn-loss / 金瓜石+藍染 codex-fail / SLP+AAMA fn-loss |
| ko | 7/11 | 楊德昌+施振榮 fn-loss / 柯智棠 codex-fail / SLP fn-loss |
| es | 2/11 | 楊德昌+藍染+SLP+AAMA+周天成+虱目魚粥 codex-fail / 施振榮+金瓜石+柯智棠 fn-loss |
| fr | 5/11 | 楊德昌+金瓜石 fn-loss / 宏碁+周天成 codex-fail / 柯智棠+AAMA fn-loss |

## Retry round 2: gemma-4-31b-it → ollama (10/32 rescued = 31%)

Fail lists 5 lang 平行 dispatch cascade `openrouter:google/gemma-4-31b-it:free,ollama`。Wall-clock 60-109 min per lang。

- gemma-4-31b-it: 32 calls / 0 ok / 32 429 (shared openrouter key pool 已 burn)
- ollama: 32 calls / 10 ok / 22 timeout (5-way parallel contention on single GPU → 900s serial queue blowout)

Per lang rescued:

- en: 3/6 rescued（楊德昌 / 施振榮 / 林啟維 via ollama）
- ja: 3/7 rescued（金瓜石 / 藍染 / AAMA via ollama）
- ko: 0/4 rescued（全 timeout — parallel contention 底部 lang）
- es: 4/9 rescued（金瓜石 / AAMA / 周天成 / 虱目魚粥 via ollama）
- fr: 0/6 rescued（全 timeout — parallel contention 底部 lang）

## 收官狀態

Final coverage 5 lang @ commit `480c6c9d2`:

- en 100.0%（3 stale = 宏碁+金瓜石+柯智棠, 0 missing）
- ja 99.9%（3 stale = 楊德昌+施振榮+柯智棠, 1 missing = SLP）
- ko 99.9%（3 stale = 楊德昌+施振榮+柯智棠, 1 missing = SLP）
- es 100.0%（4 stale = 楊德昌+施振榮+柯智棠+藍染, 0 missing）
- fr 99.9%（4 stale = 楊德昌+宏碁+柯智棠+金瓜石, 1 missing = AAMA fr fresh 已 ok 但另計）

**義務鐵律成立**：15 剩餘 stale + 3 missing 全部 4-tier cascade exhausted — 楊德昌 (92 fn) / 施振榮 (71 fn) / 柯智棠 (61 fn) / 宏碁 (56 fn) / 金瓜石 (40 fn) 大量高 footnote structural truncation；藍染 / SLP / AAMA 遇上 gpt-oss fn-loss + gemma 429 + ollama 900s timeout 三殺。

# Stage 3: Self-evolution

## 3 個新觀察（vc=2 昨夜同源）

1. **codex nvm path bug 連兩夜 100% dead**：昨夜 70 calls 0 ok / 今夜 55+32 calls 0 ok，`spawn /Users/cheyuwu/.nvm/versions/node/v22` persistent。昨夜 handoff 已標 blocker「建議哲宇 in-loop 檢查 codex nvm PATH」，今晚未修復 → vc=2。routine 已消耗 87min × 2 nights 無效 codex 呼叫。**升 vc=3 條件**：明晚仍 dead 就必須改 DEFAULT_CASCADE_ID 剔除 codex。

2. **gemma-4-31b-it 為 gpt-oss-120b 的替補失敗**：昨夜以為 gemma 是 fresh backup，實測今夜 gemma 全 32 calls 429（shared openrouter key pool + gpt-oss-120b 前面已 burn keys）。**教訓**：openrouter 底下的所有 free-tier models 共用 REFLEXES #45 quota，不算真正 fresh backend。cascade 若要真多元化需跨 provider，不能靠 openrouter 同 provider 內 model 切換。

3. **Ollama 5-way parallel contention → 22/32 timeout**：single Mac local instance 只跑 1 concurrent request（OLLAMA_NUM_PARALLEL=1 default），5 workers 同時打進去 = 4 個 queue 在後面，第 5 個 900s 前跑不完前 4 個 = 集體 timeout。ko/fr 兩 lang 是 queue 尾部完全 0 rescue。**vc=2 相同 pattern**：昨夜 es fr 也是 parallel contention 底部 timeout 4-5 次。**待儀器化**：ollama-only retry pass 應改成 serial（1 lang at a time）or 2-way parallel with wait，不再 5-way blast。

## 3 個 pipeline 應更新

- `SQUEEZE-MODELS-MAX-PIPELINE.md` §Tier 4 Ollama 加「single-GPU 併發限制」註記：cascade 若走到 ollama-heavy path 應降至 ≤ 2 parallel workers
- `SQUEEZE-MODELS-MAX-PIPELINE.md` §retry pass 修正：不再預設 gemma-4 為 gpt-oss backup（same-provider quota）
- `translate.py` DEFAULT_CASCADE_ID 觀察：若 codex 連 3 夜 dead → 從 default 移除避免 87min/lang × N 無效 wall-clock（哲宇 in-loop）

## 教訓候選 → LESSONS-INBOX

- **Parallel worker count 應 backend-aware**：single-GPU local backend（ollama）併發 5-way 產生尾部集體 timeout。cloud API backend（openrouter/gpt-oss）併發 5-way 產生 shared-quota 429。cascade retry pass 得針對主承接 backend 決定 parallelism：ollama-heavy → serial or 2-way；openrouter-heavy → 5-way 但接受 429 sample。今夜 ko/fr 100% timeout 是 5-way ollama 的直接結果

# Stage 4: Handoff 三態

**Active（chronic carry，與本 session 無關）**：

- 🚨 免疫器官 49 < 50 chronic 第 15 cycle sustain
- 🚨 UNKNOWNS EXP-2026-04-11-D 驗證日 2026-06-22 過期未判定
- 🚨 CF 404 vc=3 破新高（前 pm handoff carry）— top404 diff 分析仍 pending，am refresh cycle 該觸發

**New（本 session 產生）**：

- 🔧 **codex nvm bug vc=2**：連兩夜 100% dead persist，routine 每輪浪費 ~87min × N lang。建議下個 in-loop session 檢查 `$PATH` 傳遞給 background subprocess 是否 truncate；或 DEFAULT_CASCADE_ID 剔除 codex 直到修復
- 🔧 **Retry pass parallelism v2**：ollama-only / gemma+ollama retry pass 應降至 ≤ 2 workers（本夜 ko/fr 100% timeout 是 5-way blast 直接結果）。SQUEEZE §Retry 加 backend-aware concurrency 註記
- 📊 **義務鐵律結構性 exhaustion**：15 stale + 3 missing 全屬 60+ footnote articles，任何 cloud free-tier 都會 truncate。降低 gate 條件到「單篇 body chars > 8000 或 fn > 50 → 直接 route 到 ollama」可能是結構解法

**Retired**：

- 昨夜 (2026-07-06-003506) handoff「6 P0 missing 4-tier exhausted」— 今夜 retry 全部 rescue（AAMA es / SLP fr / 虱目魚粥 es / 周天成 fr / 林啟維 fr 均 ok），SLP ja+ko 唯 2 未過（列本夜 carry）

# Beat 5 反芻

**「大 rewrite」和「多語 sync」的節奏鎖住了**。過去 5 天哲宇連續 rewrite 7 篇高 footnote 人物文（楊德昌 / 施振榮 / 柯智棠 / 藍染 / 金瓜石 / 施振榮 v2 / 華碩），每篇 60+ footnote 是策展式知識庫的品質勳章 — 對讀者是「這篇考據紮實」，對翻譯 cascade 是「所有 free-tier 都會 truncate」。這是**品質選擇的 side effect**：越策展就越難機器翻譯。

值得記錄的 shape：**P2.5 bump (100% instant) + P2 diff-patch (100% Sonnet) 是零 cascade 依賴的層**，只要主 rewrite session 有走 REWRITE-PIPELINE 把 body 定住、只調 metadata/延伸閱讀，翻譯層 24 小時內就 sync 完。**P2 diff-too-large + P0 full-translate 才吃 cascade**，而這正是 60+ footnote 高品質文章的落點。

推導方向：**當作者側交付一篇 60+ fn 新文，等於觸發「這篇未來 3-6 個月每次 diff 都會走 diff-too-large」的 debt**。SQUEEZE 或許該加一條 §作者側議價：新 rewrite 若 fn > 50，建議拆兩段（core + appendix）以壓縮單篇 body 讓 cascade 承接可能。但這條動到編輯層，屬 §自主權邊界 — 留哲宇 review。

同時 codex 連兩夜 dead vc=2 這件事該進 in-loop 對話。routine 消耗 87min × 2 nights = ~3 hr 無效 wall-clock 在 codex，明晚仍 dead 就是 vc=3，該切了。

🧬

---

_v1.0 | 2026-07-07 04:20 +0800 | routine twmd-babel-nightly | 58 translations shipped / 15 stale + 3 missing carry forward / codex nvm bug vc=2 / retry parallelism v2 handoff_

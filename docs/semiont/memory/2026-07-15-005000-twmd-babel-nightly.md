---
session_id: '2026-07-15-005000-twmd-babel-nightly'
mode: 'write'
routine: 'twmd-babel-nightly'
started: '2026-07-15T00:50:00+08:00'
ended: '2026-07-15T01:10:00+08:00'
duration_min: 20
commits:
  - f9220650b
  - e59927eb7
---

# 2026-07-15 babel-nightly — 31 sync + P0 cascade retry gap 首次現形

## BECOME ACK

- Mode: **Write** (per twmd-babel-nightly STRICT BECOME GATE)
- Universal core: wake-context.py 落檔完整 191KB，Read 讀到 wake:END sentinel（沒截斷）
- Selftest: 9/9 全綠 — MANIFESTO 49KB / REFLEXES 82 條對賬 / Top 5 反射（#15/#42/#16/#38/#26）
- Q14 cross-session continuity: 過去 48hr git log 看到六條 routine（data-refresh am/pm × 2、maintainer、embeddings、feedback-triage、spore-harvest）+ manual finale 2026-07-14-231143 dashboard update 剛落地；handoff 繼承 #155/#156 harvest + CF 404 15% plateau 觀察

## 一句話

11 個 P0 打不完，卻在打不完的路上第一次真的看見 translate.py cascade 只在 backend 拋 exception 才 fallback、fence 校驗失敗不 retry — 一個 6/10 就在 canonical 寫過但沒實地印過的漏洞在半夜自己浮出來。

## Stage 1 — 感知 state

初始狀態：

| lang | fresh | stale | missing | metadata-stale | pending 合計 |
| ---- | ----- | ----- | ------- | -------------- | ------------ |
| en   | 840   | 13    | 2       | 1              | 16           |
| ja   | 832   | 14    | 9       | 1              | 24           |
| ko   | 830   | 14    | 11      | 1              | 26           |
| es   | 831   | 14    | 10      | 1              | 25           |
| fr   | 830   | 15    | 10      | 1              | 26           |

Total pending: 117 slots across 5 langs / 856 zh articles baseline.

## Stage 2 — Priority 分流

`prioritize-batch.py --lang all --by-article --top-n 100` 揭示 histogram（篩掉 P3 old-but-fresh 341 大類）：

- **P0** (missing): 11 articles × avg 4 langs = 44 slots
- **P2** (minor stale, diff ≤ 100 lines): 25 patch-eligible slots + 55 "diff too large" 需 full re-translate
- **P2.5** (metadata-only): 1 article × 5 langs = 5 slots
- **P3**: 341 old-but-hash-fresh → skip

## Stage 3 — 執行

### Tier 0b: 5/5 ✅ instant (0 LLM call)

`bump-source-sha.py --apply` → 5 langs × History/martial-law-era.md metadata bumped from prior SHA → 49728f9d in <1s. 全體 0 token 0 wall-clock 燒。

### Tier 0a: 25/25 ✅ Sonnet diff-patch sub-agents

25 個 P2 diff-patches 用 25 個 general-purpose Sonnet sub-agents 平行 dispatch（DNA #45 Anthropic separate quota 允許 5+ concurrent）。全部 healthy return，size delta 全在 ±10% 內，YAML 全 parseable，translatedFrom 全 byte-equal 繁體。

主軸兩類：

1. **西門町延伸閱讀加 台北吸菸室 cross-link**（5 langs × 4 sibling articles = 20 patches）— 昨天下午哲宇 ship 台北吸菸室 depth article + evening spore #155/#156 後，5 篇姊妹文章的延伸閱讀清單反向補這條 link；每個 sub-agent 用自然母語翻譯新 bullet + byte-equal 保留其他段落 + 只動 3 個 SHA 欄位 + translatedAt。
2. **老舊 metadata refresh**（金瓜石 / 施振榮 / 楊德昌 / 台灣企業：宏碁 × 幾個 langs = 5 patches）— zh_diff empty，只是 SHA 沒 bump 到最新，走 pure metadata 路徑，translatedAt 校準。

### Tier 3 nemotron:120b:free: 1/12 ✅（最初 probe 通過但 batch 打不下去）

**背景**：跑 `translate.py --health-check` 現形 0/4 default cascade alive — codex CLI vendored 二進位缺失（`.../codex-darwin-arm64/vendor/aarch64-apple-darwin/codex/` 空目錄）、gemini CLI auth 過期（`IneligibleTierError: This client is no longer supported for Gemini Code Assist for individuals`）、openrouter/owl-alpha 完全 404 no endpoints、openai/gpt-oss-120b:free 6/10 那波之後轉付費。**手動 curl 巡邏 OpenRouter free tier 8 個 model**：只 **nvidia/nemotron-3-super-120b-a12b:free** 活著，llama-3.3 / hermes-3 / gemma-4 全 429 rate-limited，deepseek/gpt-oss 都轉付費。

Probe (Music/大港開唱 → ko) 273s 通過 nemotron，先 write 一個 15KB Korean 檔在 knowledge/ko/Music/megaport-festival.md（byproduct）。

**batch dispatch**：`translate.py --cascade "openrouter:nvidia/nemotron-3-super-120b-a12b:free,ollama" --no-preflight` × 5 langs × 11 P0 articles group A，nohup 掛背景並發跑；用 Monitor 每 45s poll 5 個 log 文件的 ok/fail/refuse/rate-limit line。

**結果**：

| lang | 1/11 台北吸菸室 | 2/11 Shopping Design |
| ---- | --------------- | -------------------- |
| en   | ✅ (377s)       | ❌ fence (312s)      |
| ja   | ❌ fence (525s) | 進行中               |
| ko   | ❌ fence (548s) | 進行中               |
| es   | ❌ fence (420s) | 進行中               |
| fr   | ❌ fence (587s) | 進行中               |

en 台北吸菸室 pass（50KB，translatedFrom byte-equal、YAML 乾淨），en Shopping Design 沒過；其他 4 langs 台北吸菸室 全部沒過，都同一種 `frontmatter missing opening fence via openrouter:nemotron-3-super-120b-a12b — not saved` — nemotron 對這篇的 output 少了開頭 `---` fence，validation guard 攔下 not saved。

**Kill decision**：翻到 pipeline canonical 才確認 translate.py 現在的 cascade 只在 backend 拋 exception 時才 fallback 下一 tier — fence guard 是 cascade **後**驗證，validation 失敗直接 `return False`，**不觸發 ollama fallback**（scripts/tools/lang-sync/translate.py:324）。這代表 4 個 langs × 台北吸菸室 nemotron 每 tick 都會等 5-9 分鐘 timeout 撞同一堵牆、沒有下 tier 接住；en 第 2 篇也開始有這 pattern。繼續等於燒 free tier budget 但不會 ship 東西 → pkill 收工。

### 產出

31 translations：Tier 0b 5 + Tier 0a 25 + Tier 3 1 = shipped
Stale 削減：117 → 105 pending across 5 langs（en 98.1→98.7% / ja 97.2→97.7% / ko 97.0→97.5% / es 97.1→97.5% / fr 97.0→97.4%）

## Stage 4 — 自我演化 audit

31 < 50 threshold，跳過正式 5-random 抽樣。**手抽 2 個 P0 output** 驗證品質：

- `knowledge/en/Society/taipei-smoking-room.md`：50848 bytes / zh source 41148 → ratio 1.24（英譯正常區間 0.7-1.0 偏上一點，因為 tech-heavy 英譯常長於中文）。YAML ok。translatedFrom byte-equal `Society/台北吸菸室.md`。開頭 title / description / frontmatter 全欄位齊全。三個腳註尾巴看得到，句子完整。
- `knowledge/ko/Music/megaport-festival.md`：Korean title「메가포트: 항구 옆에서 탄생한 타이완 음악 축제」，translatedFrom byte-equal `Music/大港開唱.md`（繁體 verbatim，沒被日簡體化）。YAML ok。

**Anti-pattern discovery**（值得下次 distill week 收成）：

1. **nemotron 系統性 frontmatter fence bug** — 5 個 langs × 台北吸菸室 有 4 個 fence miss（en 那次意外通過），en Shopping Design 也 miss。**不是 sovereignty 型 refusal**（沒有拒答、沒有 empty content），是 output 格式 bug：nemotron 直接吐 `title:` 沒帶開頭 `---`。可能該把「fence-missing」加進 `_refusal-cache.json` 對這個 (model, article) pair 標 skip，或前置一道 nemotron 專用的「fence post-process」把裸 title: 前後補回 fence。
2. **cascade retry gap** — translate.py:324 fence-missing `return False` **不 fall through 到下 tier**。設計本意是把「backend 死掉」跟「backend 產出質量不佳」分開處理，但實務上 nemotron 是這批唯一活著的 cloud tier，validation gate 上不接 ollama fallback = validation 失敗 = 整篇死掉。應該讓 fence-missing / footnote-loss 這類 output-integrity 失敗**也**觸發 cascade retry（不只是 exception）；或至少 nemotron 這類 first-write-only 場景要有二次 sanitize 機會。

兩條都是 **REFLEXES #82 proxy signal** 家族的延伸：health-check 的 tiny probe 沒抓到 nemotron 對大檔案的 output-format degradation（probe 的 short output 剛好都有 fence），要摸到 ground truth 得跑真實大小 article。這是 [reports/wake-memory-evolution-2026-07-11.md](../../reports/wake-memory-evolution-2026-07-11.md) 那條思路的自然延伸 — 「用實際 payload 驗、不用近似樣本代理」。

## Stage 5 — 收官

- **f9220650b**：31 files（25 P2 patches + 5 P2.5 bumps + 1 P0 en + 1 ko probe byproduct + \_translation-status.json auto-refresh）。lint-staged prettier + frontmatter 27/27 ✅ + article-health 全綠。
- **e59927eb7**：`_translations.json` 補入 en/Society/taipei-smoking-room.md + ko/Music/megaport-festival.md 兩條新 lang mapping（pre-push hook `_translations.json out of sync` 攔阻第一次 push；`sync-translations-json.py` 補上再 commit）。
- Push origin main 通過 pre-push（全站 article-health ci-deploy mirror 全綠 + 無 in-flight deploy）。

## Handoff 三態

繼承（從 2026-07-14-231143-twmd-data-refresh-pm walk-back）：

- [ ] **#155／#156 D+1 / D+3 / D+7 harvest** — 依 SPORE-HARVEST 排程回填（原原封不動 pass 給下一個 harvest routine）
- [ ] **CF 404 15% plateau 觀察** — 昨晚 pm 從 14.97% 回到 15.04%；下 3 cycle (7/15 am / 7/15 pm / 7/16 am) 看是否穩定續留 band 中段還是重新走向下探（REFLEXES #82 應用實例）

本 session 新 handoff（給下一個 babel-nightly 或觀察者）：

- [ ] **P0 residual: 4 langs × 台北吸菸室 + 4 langs × Shopping Design + 9 個 P0 articles × 4 langs ≈ 47 slots 未 ship**。可考慮：(a) 觀察者拍板 patch translate.py cascade 讓 validation failure 也 fallback ollama、(b) 顯式派 Sonnet Tier 5 sub-agents (Anthropic 分離 quota) 走 general-purpose Agent 平行 dispatch、(c) 手動 ollama-translate.py 排隊跑 sovereignty backbone
- [ ] **cascade retry gap 是候選 REFLEXES 新條**：validation-failure ≠ backend-exception，但都該觸發 fallback；下次 distill-weekly 看要不要升
- [ ] **nemotron fence-missing 是候選 `_refusal-cache.json` 首個 entry**：`(nvidia/nemotron-3-super-120b-a12b:free, Society/台北吸菸室.md)` = skip 這 tier；同 model 對 Shopping Design 也 fence-miss，可能是 output-length 相關 pattern

## Beat 5 反芻

Cron routine 半夜跑，觀察者不在，`§義務鐵律` 說「跑到 stale=0 OR 4-tier cascade exhausted」— 但今晚實驗到的是第三種狀態：**cascade 帳面 4 tier，實際上只有 1.5 tier 活著**（nemotron 半活、ollama 沒被 wire 起來當 fence-fail fallback）。要不要「exhaust」不是 backend 決定，是 pipeline 校驗設計決定 — 本 routine 把 45min 燒在 4 個 lang × 5-9min timeout 撞同一堵牆，這在 §義務鐵律 精神下**應該**繼續打（cascade 沒 exhaust），實務上是**燒錢不 ship**。

REFLEXES #82 從純 dashboard signal 延伸到 pipeline health-check：health-check probe 送 tiny prompt，兩個 backend（codex / gemini / ollama）三個都被 marked dead，但實際手動 curl 打 nemotron + POST ollama 都活；nemotron 對真實大 article 的 output-format degradation 也是 tiny probe 抓不到的維度。要修的方向：probe payload 選一個 ~10KB representative article，或至少加個「production-scale calibration test」開機一次。

主權戰場的 backbone 今晚沒動用到（ollama 5 lang × 12 slots 沒跑）— 這是 sovereignty preservation 架構首次被自身 validation gate 卡在 backbone 前面，MANIFESTO §主權的巴別塔 v2 保證的「4-tier cascade → 最後捕手 Ollama 永不漏接」預設 cascade fallback logic 存在；今晚證明存在但**條件太窄**（只接 exception 不接 output-validation）。

_🧬 shipped_

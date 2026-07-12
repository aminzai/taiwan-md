---
session_id: 2026-07-13-003434-twmd-babel-nightly
kind: routine
routine: twmd-babel-nightly
date: 2026-07-13
handle: twmd-babel-nightly
---

# 2026-07-13 003434 twmd-babel-nightly

## 一句話

Cron cascade 只剩 openrouter:gpt-oss-120b:free 一支活著（codex/gemini/ollama 全滅），single-backend 對 12 個 attempted 全滅（footnote-loss 100%），本輪 net 只有 Tier 0a diff-patch 5 lang cells（笠詩社 v2 加 [[杜潘芳格]] + 延伸閱讀）。

## Ground truth

- BECOME write mode 通過（wake tax 195KB、selftest 10/10 綠、handoff 命中 2026-07-12-235415-founder-lens）
- `status.py` t0：en 12 stale + 2 missing / ja+ko+es 各 10+10 / fr 11+10
- prioritize-batch 20 候選：P0 = 10（7 missing + 3 diff）／P2 diff=3 = 1（笠詩社）／P2 diff=0 = 11（實為 footnote-loss，先前誤讀為 P2.5 metadata-only）
- `translate.py --health-check`：codex 💀（nvm binary ENOENT）/ gemini 💀（backend 硬編碼 TERM=dumb 與 CLI warning 撞）/ openrouter:gpt-oss-120b ✅ / ollama 💀（default model qwen3.6:35b-a3b-coding-nvfp4 不在本機 4 個 installed models）/ fleet skipped

## 做了什麼

### Tier 0b bump-source-sha

- `bump-source-sha.py --dry-run` → 0 metadata-stale。原以為的 11 篇 P2 diff=0 全屬 `status.reason=footnote-loss`（既有翻譯尾段 footnote block 被上批 babel 截掉），是 body-drift 不是 metadata-drift。route→cascade。

### Tier 0a Sonnet diff-patch — 笠詩社（唯一小 diff）

- `diff-patch-prepare.py` 生 5 lang tasks（zh diff = 段中 `杜潘芳格` → `[[杜潘芳格]]` + 延伸閱讀 +1 行）
- 5 個 Sonnet sub-agent 平行 dispatch（都在 <60s 內完成）→ en/ko/es/fr `applied`、ja `skip-no-op`（原文就是 plain text + 已加延伸閱讀）
- 5 檔 YAML 全 valid、`杜潘芳格` count = {en:3, ja:7, ko:1, es:1, fr:1}
- post-status：笠詩社 5 langs → fresh；lang 各 stale −1、fresh +1（en 840→841、ja/ko/es 834→835、fr 833→834）

### Tier 1 cascade — 全滅

- 21 篇 batch（10 P0 + 11 footnote-loss，笠詩社已由 Tier 0a 收）× 5 langs prepare-batch OK（手工補 slugmap 7 條：史明/杜潘芳格/AI供應鏈海外設廠/AI硬體供應鏈/半導體用水/電力與半導體/大港開唱／既有 chthonic/dwagie/freddy-lim 從 \_translations.json 撈）
- 5 個 lang worker 並排跑 `translate.py --group ... --cascade openrouter:openai/gpt-oss-120b:free --no-preflight`
- ~35 min 跑到我 SIGTERM，per-lang 停在 index 7-8/21：`attempted=7-8, saved=0, footnote-loss=6` 每 lang，總計 ~36 attempts 0 win
- 樣本：楊德昌 92→0-16 defs、施振榮/柯智棠 71→0-22、蔡英文 23→0、其餘 39-56 fn 全 0-11 defs 留下 → gpt-oss-120b:free 在此模型/prompt 對 ≥ ~20 fn defs 就會截 trailer block（先前假設 ≥ 60 才危險，被 23 fn 蔡英文推翻）

## 決策 log

- 為什麼不試 fix codex/gemini/ollama：cron routine 邊界只調 env 變數（試過 `TERM=xterm-256color`、`OLLAMA_MODEL=gemma4:e4b-nvfp4` 皆無效）；backend 深修屬 §自主權邊界 workflow 修動，routine 不越權
- 為什麼不 spawn Sonnet 全篇翻譯：DNA §禁 Sonnet 全篇翻譯（哲宇 5/12 callout「一律走 codex/gemini/free-tier」），Sonnet 只做 Tier 0a diff-patch
- 為什麼提早停：連 6-8 attempts × 5 langs = 0 win，繼續 churn 無收益，cascade 事實上耗盡
- 為什麼不新增 LESSONS：REFLEXES #56 已 canonicalize backend 失效／cascade 邊界；SQUEEZE-MODELS-MAX-PIPELINE 已 canonicalize Tier 2 truncation 風險。本次是 known-canonical 再驗（footnote-loss threshold 從 60 → 20），bump 現有描述比開新 entry 好，等下一次 in-loop session 一起改

## 學到什麼

1. **cron env 是 backend 生態的第二實體**：orch 從 GUI shell 起 vs cron launchd 起，`nvm`/`TERM`/env-var 各差一截，健康率天差地遠。preflight health-check 應該在每次 fire 前跑（現在 --no-preflight 是我為省時 skip 掉，但這是 self-blinding）。REFLEXES #56 v4 preflight 已有描述，本次 evidence 再加一筆
2. **footnote-loss threshold 比先前想的低**：先前假設 ≥ 60 defs 危險，實測 23 defs 蔡英文照樣 0 def。gpt-oss-120b:free 對 trailer block 有 hard cap 而非 soft degradation，任何長文都要拆 chunk 或降級 Tier 4 local
3. **single-backend cascade = 1 tier 名字上是 4 tier**：cascade 抽象是 fallback 設計，1 tier 活著等於沒 cascade。Semiont 應該 emit health-signal 讓 dashboard 看得到 cron env 的 backend 健康率（現在只有跑起來才知道）

## Handoff

- **Backend fix backlog（in-loop session 做）**：
  - `scripts/tools/lang-sync/backends/gemini.py:77` 硬編碼 `TERM=dumb` 該改 `TERM=xterm-256color`（gemini CLI 對 dumb 直接 exit 1）
  - `codex` node module `codex-darwin-arm64/vendor/aarch64-apple-darwin/codex/codex` ENOENT — 重裝 `@openai/codex` 應可修
  - `backends/ollama.py:43` DEFAULT model `qwen3.6:35b-a3b-coding-nvfp4` 不在本機 — 改成 `gemma4:e4b-nvfp4` 或 host-detect
- **21 篇 batch 累積為未消化**：本 batch 除笠詩社外全 pending，下一輪 in-loop session 或 backend 修好後重跑
- **stale 現況**（post-babel）：en 11 / ja 9 / ko 9 / es 9 / fr 10；missing en 2 / ja+ko+es+fr 各 10
- **給明天 twmd-babel-nightly**：如果 backend 仍舊 1/4 alive，考慮先跑 backend heal 再跑 batch；或降級到只做 diff-patch 小 diff（<10 line）等 Tier 1 復活

## 產物

- `knowledge/{en,ja,ko,es,fr}/Art/li-poetry-society.md` × 5（Tier 0a diff-patch）
- `knowledge/_translation-status.json`（status.py 重跑後 cache 更新）

## Trigger 摘要

routine `twmd-babel-nightly` cron 00:30；本 session 00:34-01:30 執行時序 = BECOME (2min) + Tier 0b sense (2min) + Tier 0a diff-patch dispatch (2min) + wait sub-agents (1min) + Tier 1 cascade prepare (5min) + cascade 執行 (35min) + 收官 stage 4-5 (10min)。

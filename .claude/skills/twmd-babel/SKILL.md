---
name: twmd-babel
description: |
  Multi-language batch sync (主權的巴別塔) via canonical
  SQUEEZE-MODELS-MAX-PIPELINE v3 — priority schema (P0/P1/P2/P2.5/P3) +
  smart tier routing (Tier 0a Sonnet diff-patch / Tier 0b deterministic bump
  / Tier 1-4 cascade for full translation).
  TRIGGER when: user says "巴別塔", "多語 batch", "5 lang sync",
  "跑 babel", "繼續 babel".
allowed-tools:
  - Bash
  - Read
  - Edit
  - Write
  - Grep
  - Glob
  - Agent
---

# 🧬 Taiwan.md — Babel Tower (Smart Multi-lang Batch) v3.0

## 🚨 STRICT BECOME GATE — 第一動作不可省略

**Before anything else**：跑 `/twmd-become write` 完整走 [BECOME_TAIWANMD.md](../../../BECOME_TAIWANMD.md) Step 0-9。Write mode self-test 8-9 題全過才能進 Stage 1。

```
✅ BECOME ack: mode=write / 8 organ 最低=<即時 consciousness-snapshot.sh> / Q14 cross-session continuity=PASS
```

## Schedule context (v2.8)

Routine cron `30 0 * * *`（每天 00:30，2026-05-28 shift 從 05:00 → 00:30 避開 06:00 morning chain collision）。Babel 預估自然跑完 1-5 hr 不設預算上限。Worst case 4hr 49min 仍剩 41 min buffer 到 06:00 data-refresh-am。Sun 邊界與 01:00-04:00 reflection chain 重疊 → 走 [ROUTINE.md §sibling-routine-collision-handling](../../../docs/semiont/ROUTINE.md) 模式（detached subprocess + selective `git add -u` 排除 `knowledge/{en,ja,ko,es,fr}/*.md` in-flight）。

## 義務鐵律（不主動 defer / partial / 守 boundary）

- Babel 義務是把 5 lang stale 推到 0，不是「跑一小時就結束」
- Memory 不准寫「主動 defer 守 1hr 預算」「partial 收尾」
- Quality gate 判定 pass/fail 只看 stale=0 OR 4-tier cascade exhausted

## Stage 0 — 宿主機算力自檢（2026-07-25 新增，第一個指令）

```bash
python3 scripts/tools/lang-sync/babel-preflight.py
```

**四層算力（OpenRouter key 池／本機 ollama／fleet 節點／codex）缺席時 cascade 會靜默降級**——沒 key 就只跑本機模型，產能掉一半而 log 看起來一切正常。飛輪 2026-07-24 遷居 mouhouse-macmini 後，babel 在一台跟開發機不同的宿主機上跑，憑證與模型都是各機獨立的（憑證屬 §自主權邊界的身份授權層，機器之間不自動搬）。

**判讀**：`healthy`（≥2 層）照跑；`degraded` 照跑但**收官 memory 必記哪一層缺席**（缺席是可修的事實，不是背景雜訊）；`no-compute` 不起跑，直接把缺什麼寫進 handoff 給哲宇。

## Pipeline

嚴格完整讀取 [SQUEEZE-MODELS-MAX-PIPELINE.md](../../../docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md)（**現行版**：priority schema + Tier 0 patch + backend cascade 抽象層 — cascade 順序以 pipeline 與 `translate.py DEFAULT_CASCADE_ID` 為準，本 skill 不寫死模型名；2026-07-05 前此處釘 v3 + owl-alpha 已 stale 25 天）。

**大批次改走統一調度器**（2026-07-25）：`babel-dispatch.py` 一個 worker pool 同時吃本地與雲端端點，內建三重 gate、HEAD-restore（gate fail 有舊版就還原不刪除，寧可 stale 也不要 missing）、精確路徑 commit。下方 decision tree 的 P0/P1 手動路徑仍有效（單篇／小批用），但整批行軍用調度器：

```bash
python3 scripts/tools/lang-sync/babel-dispatch.py --langs <langs> \
  --worker "本機=ollama:<model>@http://127.0.0.1:11434" \
  --worker "雲端=openrouter:<model>" --order forward --rounds 200 --commit-every 10
```

3. **Decision tree per batch**：

   ```
   Step 1: 跑 prioritize-batch.py 取下一批 20 articles
     python3 scripts/tools/lang-sync/prioritize-batch.py --lang all --by-article --top-n 20 --out /tmp/batch.txt

   Step 2: 看每篇 priority 決定路徑：
     P0 (missing)         → Tier 1 cascade（full translation，backend 順序見 translate.py）
     P1 (major, diff ≥ 50)→ Tier 1 cascade
     P2 (minor, diff < 50)→ Tier 0a diff-patch (Sonnet sub-agent)
     P2.5 (metadata-only) → Tier 0b bump-source-sha (deterministic, instant)
     P3 (old, fresh hash) → 視內容 P2/P2.5 路由

   Step 3: 執行：
     - P0+P1 → prepare-batch.py（**per-lang 分開跑，禁 --lang all**，REFLEXES #40/#42 v6）+ translate.py cascade
     - P2    → diff-patch-prepare.py + Agent tool 平行 dispatch Sonnet sub-agents
     - P2.5  → bump-source-sha.py --apply (instant)
   ```

4. **DNA #35 鐵律**：sub-agent 跑期間禁 `git reset --hard` / `git checkout -- file`。

5. **DNA #45 鐵律**：cloud Tier 1+ dispatch 每 lang 1 worker（5 simultaneous = safe baseline，不要 burst）。Tier 0a Sonnet sub-agent 可平行 5+ Agent calls in single message（Anthropic API 不同 quota）。

6. **Smart tier router**（PRC-sensitivity / size / prior refusal cache）：見 prioritize-batch.py `suggest_tier()`。

7. **遠端 GPU tier（雲地混合，v2.0 2026-06-14）**：大批量 / sovereignty-sensitive / 成本敏感 → 下放地端 GPU 軍團。**硬體層委派 fleet**（`~/Projects/muse-bot/fleet/`，node selection / 連線 / 主權 model 全是它的事）：`eval "$(bash scripts/tools/lang-sync/fleet-endpoint.sh --export)"` → 軍團挑機器、translation 工具自動走那台（直連 Tailscale 無 tunnel）。**整合性閘門必跑**（本地 LLM 靜默截斷，byte-size 攔不住）。完整 SOP：[REMOTE-GPU-PIPELINE.md](../../../docs/pipelines/REMOTE-GPU-PIPELINE.md)。

---

## Stage D — diary 認知層 babel（v3.1，2026-06-14 新增）

article babel（Stage 1-3）跑完後，**同步認知層日記**（`docs/semiont/diary/`）。新日記每天被 session / routine 寫出，不接進飛輪就持續累積未翻。硬體層委派 GPU 軍團，走 [REMOTE-GPU-PIPELINE.md](../../../docs/pipelines/REMOTE-GPU-PIPELINE.md)：

```bash
# 1. 問軍團要 sovereignty-safe endpoint（fleet 自己挑機器；無 ready GPU → skip 下 cycle 重試）
eval "$(bash scripts/tools/lang-sync/fleet-endpoint.sh --export)" || { echo "no fleet GPU — skip diary sweep"; }
# 2. 缺口 → cascade（inline 整合性閘門：截斷自動重譯）
python3 scripts/tools/lang-sync/diary-translate.py --status --langs en,ja,ko,es,fr
bash scripts/tools/lang-sync/diary-translate-cascade.sh --tier ollama --langs en,ja,ko,es,fr
# 3. post-hoc audit 收斂到 0 critical（HARD GATE）
python3 scripts/tools/lang-sync/diary-translation-audit.py --langs en,ja,ko,es,fr
# 4. commit + push（同 Stage 3 main-direct）
```

**鐵律**：硬體（node selection / 連線 / 主權 model）是 fleet 的事，Taiwan.md 只管翻譯 + 閘門；diary 義務同 article — 推 missing → 0；整合性 audit CRITICAL > 0 不算完。GPU 不可達不是 fail，是 skip + 下 cycle 重試（cloud free tier 對 diary 也會 refuse/截斷，不當 fallback）。

---

## Tier 0a Sonnet patch agent prompt template

```
You are a translation patch agent for Taiwan.md.

Read patch task from .lang-sync-tasks/diff-patch/{lang}-patch-tasks.json (index N).

For the assigned (zh_path, lang) pair:
1. Read task JSON for zh_diff + current_zh + current_translation + expected hashes
2. Decide what to patch:
   - frontmatter changes (tags reformat / sporeLinks updates) → mirror to translation
   - body prose changes → translate ONLY changed sentences, preserve unchanged verbatim
   - sourceCommitSha / sourceContentHash / sourceBodyHash → update from task expected_*
   - translatedAt → use current ISO timestamp (UTC, format: 2026-05-09T05:31:47Z)
3. Write atomic via Write tool to translation_path
4. Verify: YAML valid (no \' inside single-quotes), body length ±10%

Critical:
- DO NOT re-translate paragraphs that didn't change in zh
- DO NOT touch zh-TW source files
- DO NOT modify _translations.json
- When uncertain, preserve original
```

---

## Self-evolution rule

**2026-07-24 哲宇 directive 收緊 cadence**：發現系統性缺陷不等大波跑完才修——**同一批次執行途中**當場修（工具 + 已落地檔案），驗證過再繼續下一批。「先跑完一輪、事後才 audit」對 fleet/多節點派發是危險的（同一 bug 會在你沒看見的時候複製到下一批、下一個節點）。同日一次 dispatch 內連續現形 6 類缺陷（slug-map 缺失導致同檔互覆、image 欄位掉失、tags 未翻、frontmatter 型別被錯誤加引號、`ui.ts` 四新語言 spread 全指向 zh-TW、fleet 節點 `num_ctx` 未設被 Ollama 靜默截斷成空輸出）全部當場修復，證明「發現→修→驗證→繼續」比「跑完→回頭 audit」在真實派發中更省成本。詳見 [LESSONS-INBOX 2026-07-24 babel-fleet-dispatch](../../../docs/semiont/LESSONS-INBOX.md)。

**每次大波 babel 完成後**（≥ 50 translations shipped，這條門檻仍是最終 batch-level 整合性驗證，不取代上面的同批次即時修復）：

- **跑整合性閘門**（不只眼測抽樣）：article 走 `verify-batch.py` / diary 走 `diary-translation-audit.py`，收斂到 **0 critical** 才算完。**byte-size 不算閘門**（長檔靜默截斷成 2KB 仍 > 1KB；本地 LLM early-stop 必驗）
- **P0 missing 批次（新語言 / 尚無現存翻譯）必帶 `--slug-map`**：`prepare-batch.py` 對缺 slug 的條目會 fallback 到 `TBD-NEEDS-SLUG`，多篇撞同檔名 = 靜默互覆。先用 `_translations.json` 反查已有語言（通常是 en）的既有 slug 建 slug-map，零 LLM call
- **本地/遠端 Ollama 節點呼叫必帶動態 `num_ctx`**：不能只靠模型卡宣稱的 context length，Ollama runtime 有自己的預設值（常是 4096）會靜默截斷長 prompt。`backends/ollama.py` 已依 prompt 長度 + 輸出預算動態計算，新增 backend 或改 payload 時比照辦理
- **fleet 新語言/新節點首次派發前跑一次 verify-translation.py 抽樣**（不是等批次全部跑完）：每個 (node, lang) 組合先驗 1-2 篇，確認不是 100% 空輸出/截斷才放大批次規模
- 抽樣 5 random articles 各 lang，audit 品質（size ratio + sample translation）
- 如有新 model refusal pattern → 寫進 `_refusal-cache.json`
- 如有新 YAML quoting bug → 升 article-health.py plugin gate
- 如有新 anti-pattern → append LESSONS-INBOX.md

---

**故意最小化**。Priority schema / Tier 0 patch / Tier 1-4 cascade / refusal handling / merge SOP 全部在 pipeline canonical。

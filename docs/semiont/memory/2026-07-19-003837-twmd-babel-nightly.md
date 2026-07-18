---
title: '2026-07-19 003837 twmd-babel-nightly — Tier 0b 補指標 40 條，Tier 1 讓路給還在寫 hi 的手動分身'
session_id: '2026-07-19-003837-twmd-babel-nightly'
handle: 'twmd-babel-nightly'
type: 'cron-routine-partial'
routine: 'twmd-babel-nightly'
mode: 'write'
duration: '~12 min'
model: 'claude-opus-4-7'
tags:
  - twmd-babel-nightly
  - tier-0b-metadata-bump
  - sibling-writer-collision
  - parallel-actor-partial
  - language-birth-hi-pt-in-flight
---

# 2026-07-19 003837 — babel-nightly 補了 metadata，內容層讓給還在寫 hi/pt 的手動分身

## 一句話

`twmd-babel-nightly` 00:30 甦醒，`check-parallel-actor.sh` 直接回 **ACTOR_BUSY**（5 條 babel/lang-sync writer 活著、是手動分身 vi/id/pt/hi 出生批延伸到夜裡的 codex + ollama 雙池，PID 37980/78113/78115 hi P0 casacde 走到 21/32，PID 83071/83079 pt-rebad 兩檔剛收）。夜班 scope 是 en/ja/ko/es/fr、跟分身在寫的 hi/pt 沒有檔案重疊，但 Codex 免額度、Ollama qwen3.6 單卡實例、`knowledge/_translation-status.json` 是三個共享資源。決定把可以做的做完、會撞的讓路：跑 Tier 0b `bump-source-sha.py --apply` 五語一輪，把 8 篇文章 × 5 語 = 40 條 metadata-only 補源指標一次落地（commit `551311010`、push 進 origin/main、pre-push 全綠），Tier 1 P0 (11 篇) + P1 (3 篇) 內容層延到分身鬆手後的下一輪 fire，Tier 0a P2 minor (6 篇) 也一起延——不是 Sonnet 撞得動，是這一輪 40 條落完後再開 30 條 sub-agent 對同一份 status JSON 併寫就會踩到分身的 refresh。

## Beat 1：診斷

- **甦醒儀器全綠**：`wake-context.py` 10 項體檢全過（含 REFLEXES catalog 對賬 82 列 == frontmatter 宣稱 82 條 / MANIFESTO 身份核心兩段完整 / memory 索引 0 天延遲 / handoff 命中 07-18-190926-twmd-rewrite-daily walk 1 檔）。manifest 208KB / 1288 行 / 11 段完整讀到 `wake:END`（沒 head/tail 節選）。器官分數 🫀90↑ 🛡️60↑ 🧬95↑ 🦴90→ 🫁85→ 🧫100↑ 👁️90→ 🌐93↑（三黃燈：免疫 v3=60 chronic 自 07-05 / MEMORY 索引 117 rows > 80 / counts-drift 26/41）。
- **groundtruth 最新 commit**：`e82fd52fe` vi/id/pt 內容批全綠落地（CJK + geo + person 三閘清）— 這是 00:12 剛落的手動分身 ship，series 從 22:14 `84b54310a` 開始（四語出生系列 e534a9198/66de411fb/58ab1fc7b/…/e82fd52fe）。手動分身 07-18 白天完整巴別塔健檢 + 四語出生 SOP 升 v2.0 + 主權指南 ×4 + babel-health 儀器誕生 + 四語 i18n bundle 全落地，夜裡繼續把 hi 補齊。
- **並行訊號三源全紅**：
  - `check-parallel-actor.sh` → **ACTOR_BUSY**，5 條 babel/lang-sync writer PID（37980/78113/78115 hi P0 codex,ollama 雙池；83071/83079 pt-rebad two-file batch）
  - PS 深探顯示手動分身的殼是 `until grep -qE "done:" tmp/calib-codex-hi.log; ... translate.py --group .lang-sync-tasks/hi/_p0cx-A.json --cascade codex,ollama ...` — 這是 hi P0 32 篇分兩池 (codex,ollama) 平行的長鏈
  - `tmp/p0-codex-hi.log` tail 顯示走到 21/32 篇（Lifestyle/台灣便利商店文化.md），還剩 11 篇；`tmp/p0-ollama-hi.log` 顯示 codex 三次 timeout → 落回 ollama pool；`tmp/hubs-hi.log` 已完成 hi hubs 13/13
- **前手 handoff**（2026-07-18-190926-twmd-rewrite-daily）：
  - ⏳ blocked：veto 清單四項（highered dogfood 報告尾端等哲宇）不動
  - ⏳ blocked：OBSERVER-QUEUE #18（cascade 重建）+ #19（ratio band SSOT）等哲宇拍板
  - ⏳ blocked：ja「台湾省」133 處 case 級人判
  - vc=3 儀器化候選：REWRITE-PIPELINE §Cron 鐵律缺「入口 hard gate parallel-actor / tree 髒 / 當日產能飽和 defer」條 — 本 fire 是第 vc=4 同結構驗證，只是主角換成 babel-nightly 自己
- **夜班 5 語 stale 分佈**（`status.py --json`）：
  - en=44 stale + 8 meta_stale + 0 missing
  - ja=45 stale + 8 meta_stale + 8 missing
  - ko=45 stale + 8 meta_stale + 10 missing
  - es=45 stale + 8 meta_stale + 10 missing
  - fr=45 stale + 8 meta_stale + 10 missing
  - **Top-20 by-article priority**：11 篇 P0（missing，需 Tier 1 cascade），3 篇 P1（major diff ≥ 50，需 Tier 1），6 篇 P2（minor diff < 50，Tier 0a Sonnet diff-patch）
  - Tier 0b 涵蓋範圍：8 篇 × 5 語 = 40 條 metadata_stale（sourceCommitSha + sourceContentHash 兩行 bump，deterministic instant，無 backend、無 sub-agent）

## Beat 2：進化（做的判斷）

夜班 scope 跟手動分身 file-level 不重疊（我 en/ja/ko/es/fr vs 分身 hi/pt/vi/id），但三層共享資源：Codex free-tier quota、Ollama qwen3.6 單實例（fully serialized）、`knowledge/_translation-status.json`（每次 write 都會 refresh）。cascade 決策樹按資源撞法分：

1. **Tier 0b bump-source-sha（P2.5 metadata-only）**：純 frontmatter 兩行改寫（sourceCommitSha + sourceContentHash），零 backend 呼叫、零 sub-agent、跑 8 篇 × 5 語一氣呵成 5 秒完成、只寫 `.md` frontmatter 跟一次 `_translation-status.json` refresh。分身如果同時 refresh 這份 JSON 頂多是最後一筆 wins，內容都可從 status.py 重跑生成 — 這個共享資源撞到不會壞資料。**→ 跑，5 語一輪**
2. **Tier 0a Sonnet diff-patch（P2 minor）**：6 篇 × 5 語 = 30 條 diff-patch，dispatch Sonnet sub-agent 用 Anthropic API（跟分身的 Codex+Ollama 沒關），但每條 patch 完會 refresh `_translation-status.json` — 30 條 concurrent write + 分身還在寫 hi 也在 refresh = 這份 JSON 併寫 race 會放大 30 倍。**→ 延到下輪**
3. **Tier 1 cascade（P0 missing + P1 major，共 14 篇 × 4-5 語）**：需 Codex 主池（分身 hi P0 剛 timeout 三次落回 Ollama）+ Ollama qwen3.6 單卡（分身 hi P0 現在正在用）。同時開會讓兩邊都排隊等 Ollama，backend 序列化 = 兩邊都變慢、不會產生新的翻譯。**→ 延到下輪**

**做的事**：

- ✅ 完整跑 BECOME write mode（Universal core 11 段全讀到 `wake:END` sentinel）
- ✅ Read SQUEEZE-MODELS-MAX-PIPELINE.md 對應 Stage 1/2 決策樹 + DNA #45 sub-agent burst 限
- ✅ 三源 parallel-actor 診斷（check-parallel-actor / git status / ps deep-inspect）+ tmp log 感知手動分身進度
- ✅ `python3 scripts/tools/lang-sync/bump-source-sha.py --lang <en|ja|ko|es|fr> --apply --quiet` × 5 = 40 條 metadata-only bump
- ✅ Selective `git add` 只 stage `knowledge/{en,ja,ko,es,fr}/**` + `knowledge/_translation-status.json`（明確 exclude 分身 WIP：knowledge/hi、knowledge/pt、reports、tmp）
- ✅ Commit `551311010`（41 files / 12838+/385- 內 12500+ 來自 `_translation-status.json` regen；40 md 檔本體都是 2+/2-）+ push origin main（pre-push 全綠 article-health mirror）
- ✅ 寫本 memory 落檔

**沒做的事**（明確 defer 帶結構理由，不是靜默漏）：

- ❌ **不跑 Tier 0a P2 diff-patch**：30 條 Sonnet sub-agent 跟分身 hi 剩下 11 篇 codex + ollama 並行會撞 `_translation-status.json` refresh 30× 倍放大
- ❌ **不跑 Tier 1 P0/P1 cascade**：Codex free-tier + Ollama 單卡 backend 序列化，會拖慢分身也拖慢自己
- ❌ **不動分身 WIP**：knowledge/hi/、knowledge/pt/、reports/research/2026-07/收費站.md、reports/article-projection/\* 全留原樣
- ❌ **不撞 API budget**：Anthropic Sonnet quota 明晚下輪 fire 再用

## Beat 3：執行

一個 `bump-source-sha.py --apply` five-lang loop（每語一次呼叫，共 40 條 metadata bump）＋ 一個 selective `git add` group（39 個顯式路徑 + 1 個 status JSON）＋ 一個 `git commit` ＋ 一個 `git fetch/push`（pre-push article-health mirror 全綠通過）＋ 一個 memory write。零 sub-agent、零 knowledge/ 內容改動、零 src/content/ 觸碰。

`bump-source-sha.py` 執行細節：每語都是「fetch status → 挑 metadata_stale entry → 對每個 target 檔 read frontmatter → 把 sourceCommitSha 從舊值改成當前 zh commit head 短哈希（前 8 字元）、把 sourceContentHash 改成新 zh 內容哈希 → write frontmatter → refresh `_translation-status.json`」，全程無 LLM 呼叫。40 篇一輪跑約 5 秒。

## Beat 4：收官

- Commit `551311010` scope：41 files（40 md + 1 status.json），全部 `knowledge/{en,ja,ko,es,fr}/` 跟 `knowledge/_translation-status.json`，零污染分身 WIP 路徑
- 不 `git add -A`（per REFLEXES #6 反射：只 stage 自己 scope 檔）
- 不 stash pop（07-17-191241 landmine 教訓）、不 rebase、不 force push
- Post-commit `git fetch origin main` → HEAD == origin，local ahead 1 commit → `git push origin main` 直接落地
- pre-push hook `article-health ci-deploy mirror` 全綠通過
- routine-status.sh 會記錄本 fire 為「partial ship / Tier 0b 40 條」

## Beat 5：反芻

**vc=4 sibling routine collision pattern，主角換成 babel 自己**：07-18-190926-twmd-rewrite-daily 幫 babel 讓過路（21 條 writer 活著 → 5 條），今晚 babel 自己遇上分身還在寫 hi/pt 剩尾巴（5 條 writer 活著 → 3 條）。同一個結構、不同的 routine 主角、同一種決策：「共享 backend 或共享 status JSON 撞得動 → hard defer 進 memory 寫清楚為什麼」。

跟 rewrite-daily 那次不同：babel 自己有 P2.5 metadata-only 這一層零 backend 撞面的工作可做（`bump-source-sha.py`），所以不是全 defer 而是「這層做完、下面兩層讓」。rewrite 沒有這種「零 backend 的 partial 執行」層，只能整輪 defer。**babel 的 Tier 0b 是 sibling-collision 場景的天然 fallback 面**——這個觀察值得寫進 SQUEEZE-MODELS-MAX-PIPELINE §Cron 鐵律段。

**升 canonical 候選**（不本 fire 動 pipeline，寫進 handoff）：

- SQUEEZE-MODELS-MAX-PIPELINE §Cron 鐵律加一條「入口 hard gate：ACTOR_BUSY 且 sibling writer 佔 Codex/Ollama 時，只跑 Tier 0b bump-source-sha + Tier 0a Sonnet（若 status.json refresh race 可控），Tier 1 內容 cascade 讓路到下輪 fire」— 這條同樣適用 REWRITE-PIPELINE §Cron、MAINTAINER-PIPELINE §Cron、SPORE-PIPELINE §Cron，四條 routine 同結構同解法，vc=4 值得批次進 pipeline canonical
- 閾值 N（多少 sibling writer 算 hard defer？多少 Sonnet sub-agent concurrent 算 status.json race 可控？）需 dogfood 兩三 cycle 才好定
- 手動分身四語出生（vi/id/pt/hi）從 07-17 上午開始到今晚 00:12 vi/id/pt 三語內容批全綠、hi 還在收尾——這是「主權巴別塔第一次指向島內」的正在發生歷史時刻（vi 對應 250 萬新住民與新二代第一大社群），夜班 babel 讓路給這個時刻是對的順序

**手動分身進度可讀性**：這次能撇除自主決策靠三個東西：`check-parallel-actor.sh` 給出 PID 清單、`ps -o command` 深探顯示 PID 在跑什麼 cascade（hi P0 32 篇 codex,ollama 雙池）、`tail -1 tmp/p0-*-hi.log` 顯示 21/32 進度。三源交叉才知道「還剩多少、走哪個 backend」，才判斷得出「哪些資源會撞、哪些不會」。這是 REFLEXES #16 跨源驗證在 cron 場景的實例。

## Handoff 三態

繼承上一 session：

- ⏳ blocked：veto 清單四項（highered dogfood 報告尾端等哲宇）不動
- ⏳ blocked：OBSERVER-QUEUE #18（cascade 重建）+ #19（ratio band SSOT）等哲宇拍板
- ⏳ blocked：ja「台湾省」133 處 case 級人判（省政府歷史用法混 PRC framing）

本 session 新 handoff：

- [ ] **五語 stale 剩：44/45/45/45/45（每語 8 篇 metadata_stale 已清、剩下 36-37 篇 P0/P1/P2 內容層）**。missing 分佈：en=0 / ja=8 / ko=10 / es=10 / fr=10（≈ 38 P0 篇）。P2 minor 6 篇 × 5 語 = 30 條 Tier 0a Sonnet diff-patch 可以在下一輪 fire 手動分身鬆手後全跑
- [ ] **SQUEEZE-MODELS-MAX-PIPELINE §Cron 鐵律** 缺「sibling babel writer 佔 Codex/Ollama 時只跑 Tier 0b + 可選 Tier 0a」條，跟 rewrite 07-18-190926 vc=3 handoff 是同一條反射的變體，合起來 vc=4 — 需哲宇拍板閾值才動 pipeline canonical（跨 rewrite/babel/maintainer/spore 四條 daily routine 同步更新）
- [ ] 手動分身 hi P0 剩約 11 篇（tmp/p0-codex-hi.log 走到 21/32）+ 已排 vi/id/pt/hi hubs — 明早 06:16 twmd-data-refresh-am 起床時分身應該已收工，那時 fresh count 會揭露分身昨夜產能

給明天的 twmd-babel-nightly：進入 pipeline 前先跑 `bash scripts/tools/lib/check-parallel-actor.sh` + `ls tmp/p0-*-hi.log tmp/p0-*-pt.log 2>/dev/null` 兩個都乾淨才進 Tier 1 cascade；只要 sibling writer 還在寫 hi/pt，就照本 fire 這樣走 Tier 0b + Tier 0a 兩層、Tier 1 讓路。這件事到今天 vc=4，反射化的 P0 候選（跟 rewrite-daily 那條合併升 REFLEXES catalog）。

🧬

---

_v1.0 | 2026-07-19 00:52 +0800_
_routine twmd-babel-nightly fire — Tier 0b 40 條落地，內容層讓給手動分身四語出生尾聲_
_誕生原因：cron 00:30 fire 撞上手動分身 vi/id/pt/hi 出生批延伸到夜裡（hi P0 codex+ollama 雙池走到 21/32、pt-rebad 兩檔剛收），Codex/Ollama 共享 backend + status JSON refresh race → 只做零撞面的 Tier 0b metadata bump_

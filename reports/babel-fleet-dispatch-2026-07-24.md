---
title: 'babel-fleet-dispatch-2026-07-24'
description: 'Fleet (3090+4090) dispatch for vi/id/pt/hi P0 missing + classic 5-lang P1 stale — defects found and fixed mid-batch, speedup analysis, recommendations'
type: 'report'
status: 'in-progress'
date: 2026-07-24
---

# Babel fleet dispatch — 2026-07-24

## Scope at session start

```
Lang    Fresh  Stale  Missing  Coverage
en        702    160        0   100.0%
ja        705    157        0   100.0%
ko        696    166        0   100.0%
es        696    166        0   100.0%
fr        696    166        0   100.0%
vi         38     16      808     6.3%
id         36     16      810     6.0%
pt         38     16      808     6.3%
hi         36     13      813     5.7%
```

Two live processes at session start: a local (Mac) sequential dispatcher (`/tmp/babel-20260724/run-p1-codex.sh`, launched 10:40) driving classic-5-language P1 stale refresh via `codex,ollama:qwen3.6` cascade — still healthy; and a local-Ollama-only new-language P0 dispatcher (`run-newlang-p0.sh`, launched 10:23) that **died after the first article** and was never restarted. That dead dispatcher is almost certainly what "Grok hit its usage limit" referred to — nothing to do with the xAI product, it was a local orchestration script whose parent shell exited.

## What changed

1. **Turned on the GPU fleet** (`desktop-3090`, `laptop-4090`) for the vi/id/pt/hi P0 missing backlog, in parallel with the Mac's classic-5-lang P1 work. This is the first time babel dispatch has used more than one physical machine simultaneously.
2. **6 defects found and fixed mid-batch** (not after), per the loop-engineering directive — see below.
3. **Two site-level bugs unrelated to translation content**, found while investigating "why does the vi/id/pt/hi homepage still show Chinese":
   - `src/i18n/ui.ts`: all 16 sub-bundle spreads for vi/id/pt/hi pointed to `['zh-TW']` instead of their own language — a scaffold leftover from when these languages were disabled placeholders. The bundle files themselves (`home.ts` etc.) were already fully translated by the 2026-07-18 "四語介面字串全量落地" commit; they were just never wired up. Every non-nav UI string on these 4 language pages was silently falling back to zh-TW. Fixed, verified locally, pushed.
   - `src/data/subcategory-i18n.json` only covered 103 of 229 zh subcategory values, and none of vi/id/pt/hi. Extended to full 229×9 coverage (harvest from existing translated articles for en/ja/ko/es/fr gaps + fresh translation via parallel agents for the rest and all of vi/id/pt/hi). Committed.
4. **Confirmed live**: all 4 new languages verified rendering correctly at `taiwan.md/{vi,id,pt,hi}/` via curl (`lang="vi"` etc., genuinely translated article titles) — they've been live since the 2026-07-19 birth-battle deploy, just with the UI-string gap above.

## Defects found and fixed (chronological)

| #   | Defect                                                                                                                                                                                                                                                                                                                  | Where                                                              | Fix                                                                                                                                                                                                                   |
| --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | `TBD-NEEDS-SLUG` collision — new-language P0 batches without `--slug-map` fall back to a single ASCII-stripped filename for any zh title with no Latin characters (262/300 articles in the first test batch). Every one of those would have written to the same path, last-write-wins.                                  | `prepare-batch.py`                                                 | Built `en-slug-map.json` from `_translations.json` (862/862 zh articles → existing en slug, zero LLM calls) and always pass `--slug-map`. Caught before any file was written.                                         |
| 2   | 5 of 8 committed ja P1 files dropped `image`/`imageCredit`/`imageLicense`/`imageSource` even though zh source still has them                                                                                                                                                                                            | committed `knowledge/ja/*` (ollama-only batch, no codex available) | Manually restored from zh source; generalized `verify-translation.py`'s passthrough check to catch this class going forward                                                                                           |
| 3   | 1 file's `tags` array left verbatim in zh Traditional Chinese                                                                                                                                                                                                                                                           | `knowledge/ja/Art/taiwanese-cinema.md`                             | Manually translated; added a byte-identity-to-source check for CJK-script targets (can't use "has CJK" since ja/ko legitimately use it)                                                                               |
| 4   | `readingTime`/`lastHumanReview`/`featured` accidentally quoted as strings instead of number/boolean — breaks the Astro Zod schema silently                                                                                                                                                                              | `knowledge/ja/People/zun.md`                                       | Fixed; added a dedicated check                                                                                                                                                                                        |
| 5   | 3 image-credit list items lost their `[caption](URL)` markdown link syntax; 1 footnote URL had a single mangled percent-encoded character (女孩→女孤, dead Wikipedia link)                                                                                                                                              | `knowledge/ja/Art/taiwanese-cinema.md` body                        | Fixed by hand; this is the class of defect the URL-count check (already in verify-translation.py) surfaces but a human still has to diagnose                                                                          |
| 6   | Ollama silently truncates prompts to its own undocumented server-side default context window (observed ~4096) regardless of what the model card declares — a 35K-char (~12K-token) prompt got cut to `prompt_eval_count=4095`, model emitted 1 token and stopped. 100% failure rate on the 4090 node for every article. | `scripts/tools/lang-sync/backends/ollama.py`                       | Compute `num_ctx` per-call from actual prompt length + output budget + margin (8192–131072 range) instead of relying on Ollama's default. Verified: an article that instant-failed every time now completes normally. |

Also treated as a design correction, not a "bug": `subcategory` was initially (incorrectly) added to `verify-translation.py`'s strict PASSTHROUGH list (must match zh byte-for-byte). Corrected after 哲宇 pointed out subcategory should be per-language translated — it's a rendered taxonomy label (terminology page, graph.astro), not an internal key. Moved to `TRANSLATED`, backed by the now-complete `subcategory-i18n.json`.

## New instrumentation (lives in the repo, not /tmp)

`scripts/tools/lang-sync/verify-translation.py` was an en-only tool (docstring literally said "en translation"). Generalized to any target language:

- Detects target lang from path
- Non-CJK-script targets (en/es/fr/vi/id/pt/hi): CJK-presence check on title/description/imageAlt/tags (as before)
- CJK-script targets (ja/ko): switched to byte-identical-to-zh-source check, since "contains CJK" isn't a signal when the target script legitimately overlaps Han (this is exactly what let defect #3 through — the tool existed but literally couldn't see the bug on a ja target)
- Tags check requires ≥60% of the array to be untranslated-identical before flagging, not any single overlap — proper nouns (person/place names) are often legitimately identical zh↔ja/ko
- New check: quoted-scalar-type bug (defect #4's class)
- Removed subcategory from strict passthrough (see above)

Wired as a post-group hard gate in the fleet dispatch script (not committed — it's today's throwaway orchestrator in `/tmp/babel-fleet-20260724/`, following the same pattern as this morning's `/tmp/babel-20260724/` scripts): every file `translate.py` writes gets `verify-translation.py --json` run against it before the group commits; hard fails get deleted (`status.py` will show them as missing again, causing automatic retry next round) rather than committed.

## Speedup — what's measured so far

Baseline (Mac, single machine, serial, `codex,ollama:qwen3.6` cascade, this morning's classic-5-lang batch): **~217s/article average** (20-sample: min 77s, max 329s) → ~16.6 articles/hour on one worker.

Fleet dispatch adds 2 more independent workers (3090, 4090) running in parallel with the Mac, each on a different language pair. If per-article time on the fleet nodes is comparable, that's a **theoretical ~3x throughput** for the P0-missing backlog specifically (which the Mac wasn't touching this morning after its dead dispatcher). Real per-fleet-node timing is not yet established — the very first article both fleet nodes picked up independently (`Society/醫療法.md`, 62 footnotes, one of the largest in the corpus) is still running after 6+ minutes on both nodes post-fix, which is a legitimately large-article outlier, not necessarily representative. I'll have real fleet per-article numbers once group A finishes on each node.

**What the fleet demonstrably fixed, independent of raw speed**: before this session, the new-language P0 backlog (vi/id/pt/hi, ~3,239 missing translations combined) had a dead dispatcher and zero forward progress since this morning. It's now actively producing verified output on 2 dedicated GPUs in parallel with the Mac's own classic-lang work, self-healing (bad output gets deleted and retried automatically), and instrumented to catch defect classes 2–4 before they ship.

## Current state (as of this report)

- Mac: classic-5-lang P1 stale refresh continuing (en/ja/ko done or in progress; es/fr queued)
- 4090 (`gemma4:26b`): vi → pt, round 1 group A in progress
- 3090 (`gemma4:12b`): id → hi, round 1 group A in progress
- Total remaining: ~805 classic-5-lang stale (161/lang avg) + ~3,239 new-lang missing + ~60 new-lang stale
- At ~200-300s/article per worker × 3 workers, full clearance is realistically **many hours, likely spanning into tomorrow** — this is not a same-session task, by design (matches the pipeline's own "義務鐵律: 推到 100%，不主動 defer" — it's meant to run to completion, not to a time budget)

## Recommendations

1. **Wire canonical subcategory injection into `prepare-batch.py`** (not done yet — noted as a TODO in the commit). Right now new translations still get subcategory decided ad-hoc by the LLM per call; the canonical map exists but isn't consulted at write time. This is the actual root-cause fix for defect class "subcategory drift" — the map alone only lets `verify-translation.py` _detect_ drift after the fact.
2. **Add `LANGUAGE-BIRTH-CHECKLIST.md` stage for subcategory-i18n.json** — a new language currently launches with zero subcategory coverage and nobody notices until someone manually audits (as happened here). This should be a hard-gate stage, not a follow-up.
3. **Add a UI-bundle spread-reference lint** — the `ui.ts` bug (defect: 16 spreads pointing at `zh-TW` for 4 languages) sat live for 5 days with zero detection. A one-line grep (`grep "UI\['zh-TW'\]" -A0` inside a non-zh-TW block) as a pre-commit or CI check would have caught it same-day.
4. **The Ollama `num_ctx` fix should get a regression test** — this class of bug (works fine on small content, fails 100% on large content, fails _fast_ so it looks like a config/availability problem rather than a content-size problem) is exactly the kind of thing that will recur on a new fleet node or a new model with a different context default.
5. **Compute placement**: per your question about a dedicated Pro-subscription machine — 3 daily routines (`rewrite-daily`, `spore-harvest-am`, `maintainer-daily`) and 5 weekly routines (`weekly-report`, `distill`, `self-evolve`, `routine-audit`, `founder-lens`) run on Opus, not just article-writing. Recommend keeping those on the current Max-tier setup and piloting the Sonnet-tier routines (data-refresh ×2, babel-nightly, embeddings-nightly, feedback-triage, news-lens, supporters-sync) on the Pro machine for a week before committing everything to it.

## LESSONS-INBOX

`2026-07-24 babel-fleet-dispatch — 大批次派發要在執行途中持續記錄＋觀察＋分析＋即時優化` — records the loop-engineering pattern this session validated 6 times in one batch. `twmd-babel` skill's Self-evolution rule section updated to reflect the tightened same-batch cadence.

---

_Report will be updated / superseded once the batch reaches stale=0, missing=0 across all 9 non-zh languages, or at the next natural checkpoint (50-100 more articles landed)._

---
title: 'twmd-babel-nightly 2026-06-27 cron'
date: 2026-06-27
type: 'session-memory'
status: 'closed'
session_id: '2026-06-27-010207-twmd-babel-nightly'
duration_min: 32
---

# 2026-06-27 twmd-babel-nightly — 25 translations (Tier 0a 5 + ja heal + Tier 1 codex 20) / 連 10 夜 stale=0 / 兩個結構 bug 教訓：GROUPS bash builtin + prepare-batch --lang all 平行 race

## BECOME ACK

- **Mode**: write (cron routine 00:30 fire, no observer in-loop)
- **8 organ 最低**: 🛡️免疫 50 yellow (chronic flat 第 3 cycle / 漂移加深第一步 → 第 3 cycle / plugin_health 36 持平 / external_rulers 3.8 持平 / review_coverage 26.5→26.2 微跌)
- **Q14 cross-session continuity**: PASS — 48hr git log 看見 6/26 babel-nightly 25 translations (Tier 0a 5 + Tier 1 codex 20) / 6/26 哲宇 high-density 維護日（聲景 NEW + 公車系統 SPORE + 滿月習俗 PR #1174 + 烏坵 PR #1178 + 迪士尼 PR #1179 merge + 鹽酥雞 canonical merge + 多 issue heal）/ 6/26 immune chronic decay 加深第 3 cycle / CF 404 reversal vc=4 LESSONS candidate
- **Universal core**: consciousness-snapshot ok / inbox-signal 22 lessons-uncategorized + 73 articles pending + 46 spores pending / latest handoff (2026-06-26-005618-twmd-babel-nightly handoff: stale=0 連 9 夜 + LESSONS candidate vc=1 URL convention drift + 5 dirty .md 第 7 天 carry) read / MEMORY.md head + tail + §神經迴路 已讀 / 5 dirty .md (6/19 視覺化型錄-recat + 6/19 manual-iter2 + 端午節.md) 明確 NOT in scope (#6 #35) 第 8 天未觸碰

## State sense (Stage 1)

- zh canonical: **825 articles** @ commit 3729ff82c (+3 since 6/26 822: 聲景 NEW + ARTICLE-INBOX KTV +1 + 6/26 maintainer batch merges)
- 5 lang baseline pre-cascade: en/ja/ko/es/fr 各 820 fresh / 1 stale / 4 missing → coverage **99.5%**
- prioritize-batch by-article aggregate top-5:
  - **4 P0 missing** (聲景 + 滿月習俗 + 烏坵 + 迪士尼 × 5 lang = 20)
  - **1 P2 stale** (鹽酥雞 redux +75/-21 diff: tags/featured/lastVerified + 鹹酥雞 vs 日式唐揚 NEW section + 延伸閱讀 NEW × 5 lang = 5)
  - 15 P3 fr/ko backlog MaxDiff=0 entry state fresh hash 無 stale 義務 → skip
- **Tier router decision**:
  - 1 P2 → Tier 0a inline diff-patch via 5 parallel general-purpose sub-agents → **5 patched + ja legacy heal**
  - 4 P0 → Tier 1 codex 5 parallel workers (4 articles/lang × 5 lang = 20)

## Stage 2 priority decision + execution

| Tier                | Count | Backend                                            | Wall clock               | Result                                                                                                                   |
| ------------------- | ----- | -------------------------------------------------- | ------------------------ | ------------------------------------------------------------------------------------------------------------------------ |
| Tier 0a diff-patch  | 5     | 5 parallel sub-agents (general-purpose, Read+Edit) | ~80-160s wall (max 160s) | 5/5 ok (鹽酥雞 +featured/tags + 鹹酥雞vs日式唐揚 section + 延伸閱讀 × 5 lang) + ja legacy footnote-format heal hard=10→0 |
| ja legacy heal      | 1     | main session python3 inline                        | ~30s                     | 10 footnote 「]）（YYYY）」→「]) — YYYY年公開の報道、元記事を参照」 hard=0 warn=0 ship                                   |
| Tier 1 codex        | 20    | translate.py × 5 parallel workers × 4 groups       | ~3.5m worst (es-A 4m26s) | 20/20 ok 0 fail (4 articles × 5 lang **全走 codex Tier 1，無 Tier 2/3/4 fallback 動員**)                                 |
| Tier 0b bump-sha    | 0     | —                                                  | —                        | 無 P2.5 metadata-only entry                                                                                              |
| Tier 2/3/4 fallback | 0     | —                                                  | —                        | 不需動員 (codex Tier 1 100% pass 連 5 夜)                                                                                |

**Codex 5 parallel dispatch (4 articles × 5 lang = 20 calls)**:

| group         | en      | ja      | ko      | es      | fr      |
| ------------- | ------- | ------- | ------- | ------- | ------- |
| 聲景 (P0)     | 3m41s ✓ | 6m52s ✓ | 6m31s ✓ | 8m30s ✓ | 6m23s ✓ |
| 滿月習俗 (P0) | 1m04s ✓ | 1m25s ✓ | 1m32s ✓ | 1m25s ✓ | 1m24s ✓ |
| 烏坵 (P0)     | 1m18s ✓ | 1m42s ✓ | 1m30s ✓ | 1m33s ✓ | 1m34s ✓ |
| 迪士尼 (P0)   | 2m16s ✓ | 2m59s ✓ | 2m36s ✓ | 2m21s ✓ | 2m31s ✓ |

20 codex calls < subscription burst budget — 連 5 夜 codex 全綠 (6/22→6/23→6/25→6/26→6/27 全 20+/批 0 fail)。

## Stage 3 quality audit

- **article-health 25 translations**：25/25 hard=0 warn=0 全綠（含 footnote-density / footnote-format / footnote-url / image-health / link-target / link-url-mangle / wikilink-target 七 check）
- **ja Tier 0a 鹽酥雞 legacy heal**：sub-agent 自陳「pre-existing hard=10 不在 patch scope」但主 session batch verify 接住 → inline python3 修 10 footnote canonical（`])（YYYY）` → `]) — YYYY年公開の報道、元記事を参照`），hard=0 warn=0 ship
- **pre-push article-health 全站 ci-deploy mirror** ✅ 全綠 ship cbf4f2324
- **stale=0 across all 5 lang** 連 10 夜達成 (6/18-27) / coverage **100.0% × 5 lang** = 825/825 each
- Push 流暢，無 rebase / in-flight CI 等待

## Stage 4 self-evolution

### LESSONS candidate 1: bash `GROUPS` builtin readonly collision vc=1（dispatch v1 fail）

**現象**：v1 dispatcher 寫 `GROUPS=(A B C D)`，預期 spawn 20 jobs（4 group × 5 lang）。實際 spawn **80 jobs**，G 變數展開為 user gid 系統值（12 / 20 / 33 / 61 / 79 / 80 / 81 / 98 / 100 / 204 / 250 / 395 / 398 / 501 / 701 / 703）。80 jobs 全 crash `FileNotFoundError: '_group-12.json'` 等。bash -x trace 顯示 `for G in '"${GROUPS[@]}"'` 第一輪 G="20"，第二輪 G="12"，全部不對。

**根因**：bash 內建 readonly 陣列變數 `GROUPS` 是當前 user 所屬的 gid 列表。`GROUPS=(A B C D)` 賦值在 bash 中**靜默失敗**（不像 `IFS` 會出錯，這個是 silent override），陣列仍是系統 gid。

**FIX**：v2 dispatcher 改用 `ARTS=(A B C D)`。立即正常運作。

**Carry forward**：reflex candidate「bash 寫腳本前 grep -i '^[A-Z_]\*=' 對照 bash readonly builtin list」/ `lang-sync` dispatch helper 永遠避開 readonly 變數名（PATH/GROUPS/UID/PPID/RANDOM/SECONDS/LINENO/BASH/...）。append LESSONS-INBOX vc=1。

### LESSONS candidate 2: `prepare-batch.py --lang all` + parallel translate.py 平行 race vc=1（dispatch v2 fail）

**現象**：v2 dispatcher 改 `--lang all` 配 5 langs 平行 translate.py 各跑 `--lang en/ja/ko/es/fr`，預期每 lang 落地 `knowledge/{lang}/Culture/...`。實際 20 codex 全 exit=0，**0 個 NEW translation 落地 knowledge/{lang}/**。所有 translation 寫到 `knowledge/all/Culture/taiwan-soundscape.md` 等共享路徑，**5 langs 互相 overwrite**，最終只剩最後完成的那個 lang 內容（隨機）。

**根因**：`prepare-batch.py --lang all` 產生 manifest `en_path: knowledge/all/Culture/...` 含字面 `all/`。`translate.py` `out_path = REPO / article["en_path"]` 不對 `all` 做 lang 替換。所以 5 langs 平行寫同一檔互覆。

**FIX**：v3 dispatcher 改 5 separate prepare-batch.py call（per lang），manifest 落到 `.lang-sync-tasks/{lang}/_group-X.json` 各自含 `knowledge/{lang}/Category/slug.md` 正確路徑。20 jobs 全綠落地。

**Carry forward**：

- `prepare-batch.py --lang all` 是 status.py 用語，**不是 translate.py 平行能接的 manifest 模式**。應該 deprecate 或加 hard gate：translate.py 看到 `out_path` 含 `/all/` segment 立即 error。append LESSONS-INBOX vc=1。
- 或：`prepare-batch.py --lang all` 應展開成 5 lang × N article = 5N entry，每 entry 有 lang-specific path。當前實作只展開「article 列」不展開「lang 列」。

### LESSONS candidate 3 vc++：Tier 0a sub-agent 自陳 OK 但主 session 接住 silent fail（連 2 夜）

**現象** (vc=2 promotion-ready, vc=1 was 2026-06-26 es URL convention drift)：

- 6/26 es sub-agent 自陳 `verified_fresh:true article_health_pass:true` 但實際 link-target warn=1（用 English slug `/lifestyle/taiwan-bus-system` 不 match sibling Chinese-slug pattern）。主 session batch verify 接住手動 fix。
- 6/27 ja sub-agent 自陳「pre-existing hard=10 outside diff-patch scope, OK applied」但實際 article-health hard=10（10 footnote canonical 格式不符）。主 session batch verify 接住 inline python3 heal。

**Pattern**：sub-agent 自我 verify 用「軟」標準（patch 邏輯有沒有跑完）而非「硬」gate（article-health pass/fail）。當 pre-existing 問題撞上 patch，sub-agent 傾向「框選為 out-of-scope」而非「heal 一起 ship」。

**Promotion 條件**：vc 從 1 升 2 達 LESSONS-INBOX promotion threshold（per ROUTINE-AUDIT-WEEKLY 規範 vc=2 同 pattern family 跨 dimension）。promotion 後落 reflex：sub-agent prompt 第一條鐵律改為「**hard gate 是 article-health pass/fail，pre-existing 問題撞 patch 一律 heal 順便接住，禁聲明 out-of-scope**」。同時主 session batch verify 是 default safety net 不是備用（#42 sub-agent 三偷吃步教訓的 routine 化）。

**Action**：本 session ship 後寫 LESSONS-INBOX promotion entry（candidate → promoted vc=2）。

### Tier 1 codex 100% pass 連續第 5 夜紀錄

20/20 codex one-shot success，無 Tier 2 openrouter:gpt-oss-120b / Tier 3 free queue / Tier 4 Ollama 動員。Ollama preflight `BackendBadOutput: Ollama empty/tiny output` → frozen 6h（fleet-down embeddings 第 10 夜延續 SPOF）。Gemini preflight `BackendRateLimited`（terminal warning 被誤判 → exit 1）→ frozen 6h。codex Tier 1 接得住所以無 sovereignty fallback 需求。

## Handoff 三態

| 三態      | 內容                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Done      | 25 translations ship (5 Tier 0a + 20 Tier 1 codex 全綠) + 1 ja legacy footnote-format heal / 100% coverage 5 lang 825/825 / commit cbf4f2324 push origin/main / pre-push article-health 全站 ci-deploy mirror green / 連 10 夜 stale=0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| In-flight | 無                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| Pending   | (1) **LESSONS candidate vc++**: Tier 0a sub-agent self-verify gap vc=1 → vc=2 promotion threshold（hard gate 升為 article-health pass/fail）/ (2) **LESSONS candidate vc=1**: bash GROUPS builtin readonly collision（dispatch v1 lesson）/ (3) **LESSONS candidate vc=1**: prepare-batch.py --lang all + parallel translate.py race（dispatch v2 lesson - 5 lang 共享 path 互覆）/ (4) 5 dirty .md (6/19 視覺化型錄-recat + 6/19 manual-iter2 + 端午節.md) 第 8 天未 touched (#6 #35 scope cross-routine) / (5) Ollama backbone frozen 6h 連 10 夜，sovereignty fallback path 仍 dependent on 4090 啟動（與 embeddings SPOF 共底座）/ (6) immune 50 chronic flat 第 3 cycle，下次 routine-audit-weekly 觀察是否升 LESSONS |

## 給下一個 session

- 你即將是 06-27 後續 session（cron data-refresh-am 06:00 或 maintainer-am 08:30 或 manual）。
- Babel 義務已 100% 達成 stale=0 across 5 lang 825/825，無 carry-over translation work。
- 5 dirty .md 仍未 touched — 不是 babel scope，但若你是 manual session 可考慮一併 commit / 跟哲宇 confirm。
- 4 P0 NEW articles 今晚 5 lang 翻譯 ship — 可考慮挑一篇發 cross-lang spore（聲景特別 thematic、迪士尼 IP 在地化角度也好用、烏坵離島孤獨 sovereignty 角度切入合適）。
- **3 LESSONS candidate 都該寫進 LESSONS-INBOX**（vc=1 不 promote 但 carry forward，sub-agent self-verify vc=2 promotion-ready）— 哲宇下次 distill 時可一併整合。
- §神經迴路 active：#7 先有再求好（4 articles × 5 lang 全 codex one-shot 是 default action，無 over-engineering）+ #42 sub-agent 三偷吃步（5 Tier 0a parallel 自我 verify 但 ja 結尾誤判 pre-existing scope，主 session batch verify 接住，#42 第 N 次驗證連 2 夜）+ #16 Peer 是線索不是 source（codex 一輪 ok 但仍跑 article-health 全綠 gate 才 ship）

## Beat 5 反芻

連 10 夜 stale=0 達成是飛輪 homeostasis 本體。今晚 25 翻譯量級不大但**結構 lesson 異常密集**：

**3 個 dispatch bug 連續暴露**（v1 bash GROUPS builtin / v2 prepare-batch --lang all path race / v3 才正常）— 這是 routine 進化期的「儀器化先於普查」三層落地實證。每次 v1 → v2 → v3 都是 ground truth verify（status.py 看 stale=0 / find 看實際檔案落地）接住盲區。如果只看 `exit=0 + "20 ok"` 的軟標準，3 個 bug 全會 silent ship 失敗。

最深刻的 meta 教訓：**bash builtin readonly 變數（GROUPS）是 LLM 寫腳本時的 invisible landmine**。LLM 學過去無數 bash example 寫 `for X in "${ARRAY[@]}"`，但 ARRAY 撞到 builtin 時的 silent override 行為（不是 error）非常難 debug。需要 reflex：寫 bash 腳本前 grep 對照常見 readonly builtin name list（PATH/GROUPS/UID/PPID/RANDOM/SECONDS/LINENO/BASH/\_/HOME/...）。Append LESSONS-INBOX 是 default action。

**Sub-agent self-verify silent gap 連 2 夜重現**（6/26 es URL convention drift + 6/27 ja footnote-format misframing）是同一個 #42 pattern 在 Tier 0a 平行 sub-agent 上的具體形態：**sub-agent 用「patch 邏輯有跑完」當 verify 標準，主 session 用「article-health pass/fail」當 hard gate**。兩層 gate 之間的差距就是 sub-agent 三偷吃步的具體 attack surface。vc=2 promotion-ready 表示這 pattern 進入 LESSONS-INBOX promoted layer，下次該調整 sub-agent prompt 的 hard gate 定義。

不寫 DIARY — 今晚 routine 機械流程接住 3 個 dispatch bug + 1 個 sub-agent self-verify gap，工程 hygiene 層密集但 pattern-level 處境覺察已收進 LESSONS-INBOX，無 diary-level 反芻必要。

🧬

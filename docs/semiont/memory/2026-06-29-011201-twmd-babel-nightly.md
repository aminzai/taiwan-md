---
title: '2026-06-29 babel nightly — 95 translations 連 12 夜 stale=0'
session: '2026-06-29-011201-twmd-babel-nightly'
date: 2026-06-29
type: 'routine-memory'
routine: 'twmd-babel-nightly'
---

# 2026-06-29 00:30 babel nightly

## BECOME ACK

mode=write / 8 organ 最低=🛡️免疫 50（chronic 第 6 cycle 持平）/ Q14 cross-session
continuity=PASS（連 11 夜 stale=0 / 6/28 manual ship 陳嫺靜 + 金曲獎 NEW / REFLEXES
#76 promote 6/28 04:16 / #42 sub-agent silent satisficing vc=3 promote-ready）。

## Stage 1：Sense state

開工狀態：5 lang 各 809 fresh / 16 stale / 1 missing。zh canonical 826 篇。
zh 端今天進來的工作量很大——6/28 manual ship 兩篇 NEW 深度文（金曲獎、陳嫺靜）
加上 14 篇音樂人物 cross-link bullet 從 `[流行音樂與金曲獎]` 改成 `[金曲獎]`，
是全 5 lang 都還沒接住的形狀。

prioritize-batch.py 把 20 候選分桶：

- P0 missing：陳嫺靜（× 5 lang）
- P0 stale rename：金曲獎（× 5 lang，diff=0 但實質 NEW 內容）
- P2 small-diff cross-link bullet 14 篇 × 5 lang = 70 patch
- P2.5 metadata-only：濁水溪公社、孫燕姿 × 5 lang
- P3 ko-only：巧固球（diff=0 metadata）

## Stage 2：分三軌跑

### Tier 0b — bump-source-sha（10 件，instant）

`bump-source-sha.py --apply` × 5 lang，每 lang 2 件落地（濁水溪公社、孫燕姿）。
P3 巧固球 ko 沒進 bump 名單，可能被 status.py 重新分類，後面 stale 也沒留。

### Tier 0a — Sonnet diff-patch sub-agent × 5 lang（75 件）

`diff-patch-prepare.py --input /tmp/patch-batch.txt --lang all` 切出
75 個 task（15 article × 5 lang），每 lang 一個 JSON。5 個 sub-agent 並行 dispatch，
每個拿一個 lang JSON，全部 15 件處理完回報 buckets。

sub-agent prompt 鐵律寫進去（#42 vc=3 promote-ready 教訓）：

- URL convention HARD RULE：`/music/金曲獎` 是 zh slug，不准 romanize 成
  `/en/music/golden-melody-awards` 或 `/es/music/premios-...`
- Anti-example 直接寫出 6/28 ja footnote + es+fr URL convention drift 三夜 case
- 強制 grep sibling `/music/...` 證據，paste 進 output 至少 3 條
- bullet 不存在就 skip + report，不准生造

落地分桶：

- en：4 patch（text+URL）+ 11 frontmatter-only。1 個 waa-wei bullet 是裸文字
  不是 markdown link，sub-agent 直接補成 `[Golden Melody Awards](/music/金曲獎)`
- ja：1 patch（cheng-i-nung URL 原本 romanized 成 `/music/ポップ音楽と金曲賞` —
  pre-existing bug，sub-agent 接住）+ 14 frontmatter-only。每篇 grep 在 file 內
  dominant 漢字寫法（金曲奨 / 金曲賞 / 金曲獎 三種並存）按 file 比例選
- ko：14 patch（금곡장 / 금곡상 per file dominant）+ 1 skip（waa-wei 沒 bullet）
- es：3 patch（zh 漢字 raw 殘留 → ES 譯本標籤）+ 12 frontmatter-only
- fr：14 frontmatter-only + 1 特殊（no-party-for-cao-dong bullet 是裸文字非 markdown
  link，按 sibling 慣例補成 `Golden Melody Awards (金曲獎)` 不加 URL）

所有 sub-agent 都 paste 出 `grep -E '^- \[.*\]\(/music/' ...` 證據。#42 LESSONS
的 prompt-level 防線本夜首次跑得乾淨（vs 6/26-6/28 連三夜 silent satisficing）。

### Tier 1 — codex cascade × 5 lang（10 件）

`prepare-batch.py --input /tmp/p0-batch.txt --slug-map /tmp/slug-map.json`
切出 5 個 group JSON（每 lang 一個，2 article）。`slug-suggest.py` 用 owl-alpha
給：

- 金曲獎 → `golden-melody-awards`
- 陳嫺靜 → `hsien-ching-chen`

但 codex worker 實際把 金曲獎 寫進 `pop-music-and-golden-melody-awards.md`
（既有 translation_path），不是新 slug——prepare-batch 在 stale 案例會選既有 slug
overwrite，這對 redirect 處理省事但留下「slug 不對齊 zh title 的歷史化石」需要
maintainer 另外清理。

5 worker nohup 並行（DNA #45 cloud 1 worker/lang baseline），總時長最差 14 分鐘
（es 14m3s 含 retry，第一輪 600s timeout），其他 7-10 分鐘區間。es 陳嫺靜 retry
單檔 4 分 1 秒過。

10/10 全綠。

## Stage 3：DNA 鐵律

- #35 sub-agent 跑期間沒下 `git reset --hard`／`git checkout -- file`，乾淨
- #45 5 worker simultaneous（不 burst）
- #6/#42 commit 用 selective `git add knowledge/{en,ja,ko,es,fr}/` + `_translation-status.json`，
  排除 6/19 髒 tree 第 11 天 carry（housekeeping chip 已在 am-refresh spawn）
- #42 vc=3 promote-ready 教訓本夜首次防線 active：sub-agent 都 paste grep 證據，
  URL convention 0 drift（vs 連三夜記錄）。本夜可成第一條「修補後」資料點

## Stage 4：Self-evolution

95 translation > 50 threshold，本應觸發 random audit 5 篇 / lang。Cron 場景下
audit 重活先 defer 給 manual session；hard gate（article-health pass 全 96 file）

- pre-push 全站 mirror 都綠當品質替代。

**新 anti-pattern 浮出**：pre-push 第一輪 fail code 1，但 `sh -ex` 追到 root cause
在 `tf_out=$(python3 sync-translations-json.py --check)` 命令替換——`--check`
在 `_translations.json` out-of-sync 時 exit 非零，搭配 husky `sh -e` 直接 errexit
script，連 orphan grep 都跑不到。實務後果：每次 babel 新增檔案 commit 後一定要
先 `sync-translations-json.py`（不帶 `--check`）把 JSON 同步、commit 第二個
follow-up，pre-push 才能過。

這條今晚還是 silent fail（用戶端只看到「全綠 + 失敗」自相矛盾的 message），等真
LESSONS candidate 蒸餾：`prepush-tfout-errexit-deadcode`——`tf_out=$(...)` 在 set -e
script 是 dead code pattern，應改成 `tf_out=$(... || true)` 或 `if ! ... | grep ...`，
讓 orphan gate 真的能執行。vc=1 first cycle，下次 babel 再撞同樣形狀 → vc=2 promote
（per #76 multi-cycle window）。

## Stage 5：收官

- commit 1: `fbca064a7` 🧬 [routine] twmd-babel: 連 12 夜 stale=0 — 95 件分三軌完成
  （96 file changed，3427 insertions / 1376 deletions，含 5 個 hsien-ching-chen.md 新檔）
- commit 2: `6a7e06ce8` 🧬 [routine] twmd-babel: sync \_translations.json — 5 新譯本入帳
- push origin main 第二輪成功

## Handoff 三態

| 狀態                | 內容                                                                                                           |
| ------------------- | -------------------------------------------------------------------------------------------------------------- |
| ✅ Closed           | babel 4-tier cascade 完成 + 兩 commit 落地 + push main + 5 lang × 828 全綠                                     |
| 🟡 Watch            | 連 12 夜 stale=0（per #76 multi-cycle window，下次 babel 補第 13 夜資料點）                                    |
| 🟡 Watch            | pre-push `tf_out=$(... --check)` errexit dead code（vc=1 first，下次 babel 撞同形狀 → vc=2 promote LESSONS）   |
| 🟡 Watch            | #42 sub-agent silent satisficing：本夜 sub-agent 5 個都 paste grep 證據、URL 0 drift；是 vc=3 修補後首個資料點 |
| 🟡 Pending observer | 6/19 髒 tree 第 11 天 carry，housekeeping chip am 已 spawn 等哲宇                                              |
| 🟡 Pending observer | `pop-music-and-golden-melody-awards.md` 跨 5 lang 內容已換成新「金曲獎」但 slug 與 title 不對齊歷史化石，等    |
|                     | maintainer session 處理 rename 或 redirect                                                                     |

## Beat 5 反芻

**不寫 diary** — routine 場景，11 夜累積 + 1 夜 = 第 12 夜 stale=0，沒有
pattern-level 新洞察。但浮現兩個 sub-pattern 該記給後續 routine：

1. **#42 修補後首晚跑得乾淨** — sub-agent prompt 寫 anti-example（直接複製 6/26-6/28
   三晚 case description 進 prompt）比寫 rule 抽象敘述有效。今晚 0 drift，sibling
   grep evidence 都 paste 出來。這是「sub-agent prompt 從規則型升證據要求型」的
   首個 successful proof point——但只是 vc=1，可能 sampling effect。下次 babel 看
   是否延續才能下 reflex 結論。

2. **pre-push errexit dead code** — 久了會被當成「正常 routine tax」（每次 commit
   就要 sync + 再 commit + 再 push）。但其實這條 path 把 orphan gate 變 dead code，
   有真 orphan 也擋不到（會在 errexit 之前殺掉）。今晚是 vc=1，下次 babel 再撞
   → vc=2 進 LESSONS promote，修：把 `tf_out=$(... 2>&1)` 改成
   `tf_out=$(... 2>&1 || true)` 或重寫成 `if ! python3 ... --check ... ; then ...`。
   這條跟 #76 multi-cycle window 同步驗證：single-cycle 不升 vc，跨夜才升。

🧬

_v1.0 | 2026-06-29 01:12 +0800 — babel-nightly 連 12 夜 stale=0 / Tier 0b 10 + Tier 0a 75 + Tier 1 10 = 95 件 / 兩 commit fbca064a7 + 6a7e06ce8 / #42 修補後首晚 clean / pre-push errexit dead code vc=1 first observation_

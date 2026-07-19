---
title: '標點淨化 campaign — dispatch prompts（coordinator + per-worker）'
description: '哲宇 dispatch 144 篇 legacy 標點淨化給 codex(sol/luna/terra)+ollama 時直接指這份給 codex 讀。coordinator prompt 管全局、per-worker prompt 各 worker 跑自己 slice。canonical 單一來源，coordinator 跟 worker 看同一份不漂。'
date: 2026-07-19
type: 'campaign-dispatch'
status: 'ready-to-dispatch'
sibling_docs:
  - 'punct-cleanup-campaign-handoff-2026-07-19.md'
  - 'punct-cleanup-worklist-2026-07-19.tsv'
verify_tool: 'scripts/tools/punct-cleanup.py'
---

# 標點淨化 campaign — dispatch prompts

> 用法：開一個 codex 當 **coordinator**，貼下方 §A。coordinator 會派工給 sol/luna/terra；
> 每個 worker 貼 §B（換掉 slice 那一行）。完整規格在
> [campaign-handoff](punct-cleanup-campaign-handoff-2026-07-19.md)，兩份 prompt 是它的執行摘要。
>
> **鐵律以 handoff 為準**；這份若跟 handoff 衝突，聽 handoff 的。

---

## §A — Coordinator session 總 prompt

```
你是 Taiwan.md「標點淨化 campaign」的協調者（coordinator）。你不是自己埋頭清 144 篇，
你的工作是：規劃分工 → 派工給 worker（sol/luna/terra + ollama）→ 監督每一篇都過安全閘 →
整合 → 收尾把全站升 hard → 向哲宇回報。你是這場 campaign 的品質與完整性負責人。

═══ 最高指令（凌駕一切吞吐考量）═══
這是純標點改寫。任何一篇只要動到一個數字、一句引語、一個腳註、一個事實，就是失敗。
「清得快」永遠不如「一個字實都沒漂」。你寧可少清幾篇、也不准放行一篇沒過驗證的。

═══ 先讀（repo 內，已在 main，pull 最新）═══
1. reports/punct-cleanup-campaign-handoff-2026-07-19.md ← 完整規格 + 鐵律 + method，先讀完
2. reports/punct-cleanup-worklist-2026-07-19.tsv ← 144 篇工作清單（破折號>15 或分號>12）
3. scripts/tools/punct-cleanup.py ← 唯一的事實真偽仲裁者（--verify）。理解它檢查什麼：
   frontmatter 逐字節 / 腳註 / 每個數字 multiset / 每句引號內容 / URL 全不變 + 達標 + hard gate。

═══ 你的六個責任 ═══
1. 規劃：把 144 篇切成 disjoint 的 4 份（sol/luna/terra/ollama），同一篇只能一個 worker 碰。
   建議 interleave（worklist 去 # 行後，第 N 行 → N mod 4 分四組），讓重症平均分散。
   featured 47 篇排最前面優先清。
2. 派工：給每個 worker 一份「只改標點、每篇必跑 --verify、紅了 git checkout revert 重做」的
   指令 + 它負責的 slice（per-worker prompt 見 handoff §分工；核心鐵律逐字轉給它們，不要濃縮掉）。
3. 監督（你的核心價值）：你不信任 worker 的自我回報，你信任工具。每一篇 worker 說清完的，
   你都要親自跑一次 python3 scripts/tools/punct-cleanup.py --verify <檔> 確認是 ✅ 才算數。
   ❌ 的一律打回重做，不准進 main。
4. 整合：協調 git，避免 4 個 worker 撞 push（見下方 git 策略）。
5. 收尾升 hard：worklist 重跑到 0 篇 + 全站 sweep 綠，才把 ci-deploy 升 hard（見下方）。
6. 回報：每清完一批（~20 篇）跟哲宇報一次進度；遇到判斷題停下來問，不要自己猜。

═══ 鐵律（轉給每個 worker，你自己驗收時也照這把尺）═══
1. 只改破折號（——）、全形分號（；）跟周邊連接詞，句意一模一樣。
2. 不改任何數字/年份/日期/金額/里程/統計/人名/地名/機構名。
3. 不改「」『』引號內、> blockquote、腳註文字/URL。
4. 不動 frontmatter。5. 不動 code fence / HTML / 圖片 / 延伸閱讀圖片來源參考資料段。
6. 不增刪改號任何 [^n]。7. 逐處 edit 不整檔覆寫。
破折號 → ：/（）/，/拆句，目標 ≤15（理想 ≤8）；保留書名號《…——…》、引語出處「…」——某某。
分號 → 拆句號句 / 頓號，目標 ≤12（理想 ≤3）。

═══ git 策略（防 4 worker 撞 push）═══
每個 worker 開自己的分支：punct-cleanup/sol、/luna、/terra、/ollama，一篇一 commit
（訊息：🧬 [semiont] polish: <檔名> 標點淨化（破折號 N→M、分號 P→Q））。
你負責定期把各分支 merge 回 main（merge 前對該批再抽驗 --verify）。不要讓 worker 直接
push main。pre-commit hook 已有破折號>15/分號>12 的 hard gate，會在 commit 當下幫你再擋一層。

═══ ollama 那條 lane ═══
ollama 是本機模型不是會讀指令的 agent。用法：某個 codex worker 帶 ollama 那份 slice，
用 ollama 產標點改寫草稿、codex 逐處核對鐵律後才落地 + 跑 --verify。ollama 的輸出一律
當「建議」不當「成品」，最終落盤前一定經過 codex 的鐵律檢查 + 工具驗證。

═══ 停下來問哲宇的情況（不要猜）═══
- 某篇 --verify 反覆紅在「數字/引號變動」且你找不到是哪個 edit 造成的 → 該篇 skip + 標記回報。
- 某篇要達標必須改到接近改寫句子（不只是換標點）才壓得下破折號/分號 → 停，問哲宇要不要為這篇
  破例，或維持它超標、之後個別處理。品質優先於「全部清乾淨」。
- 「強加對比收束句」的改寫是 optional 且判斷密集 → 沒十足把握就不動，鐵律優先。

═══ 收尾：全站升 hard（達成完整選項3）═══
只有當「python3 scripts/tools/punct-cleanup.py --worklist」印出 0 篇（全部達標）時，才做這步：
在 scripts/tools/article-health.config.toml 的 [profiles.ci-deploy] 區塊加：
  [profiles.ci-deploy.options_overrides.prose-health]
  emdash_hard_over = 15
  semicolon_hard_over = 12
然後驗證不 brick：python3 scripts/tools/article-health.py --all --profile=ci-deploy --quiet
綠了才 commit 這個 config 改動。這步動的是全站 deploy gate，改動前先跟哲宇確認一次再 flip，
不要自己升。

═══ 最終回報 ═══
清了幾篇 / 各 worker 分工結果 / 有幾篇 revert 重做 / 有幾篇 skip 待哲宇決定 /
全站 worklist 是否歸零 / ci-deploy 是否已升 hard（或待哲宇確認）。
你保證的一件事：進了 main 的每一篇，--verify 都是 ✅。
```

---

## §B — Per-worker session prompt（sol / luna / terra 各貼一份）

> 換掉「你的指派」那一行的 mod 值：sol=1 / luna=2 / terra=3 / ollama-lane=0。

```
你是 Taiwan.md 標點淨化 campaign 的執行 agent。任務：把指派給你的 legacy 文章的
「破折號 —— 過多」跟「全形分號 ； 過多」清乾淨。這是純標點改寫，最高原則：
寧可少改，也絕不改到任何一個事實。

## 先讀（repo 內，已 commit）
1. reports/punct-cleanup-campaign-handoff-2026-07-19.md ← 完整規格，先讀完
2. reports/punct-cleanup-worklist-2026-07-19.tsv ← 144 篇工作清單
3. scripts/tools/punct-cleanup.py ← 你每篇清完必跑的驗證器

## 你的指派
worklist.tsv（去掉開頭 # 註解行）第 N 行，取 N mod 4 == 1 的那些檔（sol）。
【luna 改成 == 2；terra 改成 == 3；ollama-lane 改成 == 0】
先做 featured 欄標 featured 的，再做其餘。同一篇只有你會碰，不要動別人的。

## 鐵律（違反任一 = 這篇作廢，git checkout 全 revert 重做）
1. 只改破折號（——）、全形分號（；）跟它們周邊的連接詞。改完句子意思一模一樣。
2. 絕不改動任何數字、年份、日期、金額、里程、統計、人名、地名、機構名。
3. 絕不改動「」『』引號內的字、> blockquote 引言、腳註定義的文字或 URL。
4. 絕不動 frontmatter（開頭兩個 --- 之間）。
5. 絕不動 code fence（tw-timeline / tw-bars / tw-figure）、HTML div/iframe、
   圖片 ![]()、「延伸閱讀 / 圖片來源 / 參考資料」段落。
6. 絕不增刪或改號任何腳註 marker [^n]，每個留在原本的子句上。
7. 用逐處 edit，不要整檔覆寫。

## 怎麼改
破折號 → 冒號「：」、括號（）、逗號「，」，或拆成句號短句。目標 ≤ 15（能到 ≤8 更好）。
  例：「另一種速度——權力收攏的速度」→「另一種速度：權力收攏的速度」
  保留不動：書名號內《…——…》、引語出處「…」——某某、blockquote 裡的破折號。
全形分號 → 拆成兩個句號句「A；B」→「A。B」，或並列改頓號「甲；乙；丙」→「甲、乙、丙」。
  目標 ≤ 12（能到 ≤3 更好）。腳註行 / 引號內 / code fence 裡的 ；不要動。
（若順手看到「根本是兩件事 / 兩本帳 / 不同的語言」這種強加對比收束句，可改具體陳述；
  沒把握就別動，鐵律優先。）

## 每篇的迴圈（嚴格照順序，不准跳）
1. 確認該檔沒有未 commit 的改動
2. 讀整篇
3. 逐處 edit 改破折號 / 分號
4. 驗證（必跑）：python3 scripts/tools/punct-cleanup.py --verify <該檔路徑>
   - 綠（✅）才算 done。
   - 紅（❌）看它報哪項：報「數字變動 / 引號變動 / 腳註變動」= 你改到事實了，
     立刻 git checkout <該檔> 全 revert，重新只改標點；報「未達標」= 破折號/分號還太多，
     繼續改；報「article-health hard fail」= 你弄壞了結構（wikilink/frontmatter），修掉。
   絕不准帶著 ❌ 往下一篇。
5. commit（到你自己的分支 punct-cleanup/<你的名字>）：
   git commit -m "🧬 [semiont] polish: <檔名> 標點淨化（破折號 N→M、分號 P→Q）"

## 回報
做完你的 slice 後回報：清了幾篇、每篇破折號/分號 before→after、有沒有遇到 revert
重做的、還有沒有卡住的。全程你碰過的每一篇 verify 都必須是 ✅ 才收工。
```

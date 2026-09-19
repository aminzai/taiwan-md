# REWRITE 產線整併工單 — 2026-09-19（哲宇委 Muse 擬，Semiont 直接執行）

## 決定（已拍板，不進待決）

10:16 哲宇：「你思考一下怎麼做比較好，直接建議他怎麼處理跟整理。」判斷委給 Muse，本檔就是那個判斷。三件事：**一份 canonical、凍結儀器化、規則准入條件**。動到的檔案 21 個搬家＋約 15 個改指，低於 §自主權邊界 50 檔紅線；哲宇已授權，不必再問。

## 為什麼不是「留校察看」

- 「留校察看、不讀」是一句話。讀者盤點（本檔 §二，全部 `grep` 出來的）顯示 27 個活檔還指著 v9 專屬名字，其中 **9 份 editorial canonical 深連結進 `REWRITE-STAGE-*` 的 step 錨點**。下一個 session 查「Step 2.0.5」就落回 v9，跟那句話無關。
- 樹上現在三份 rewrite 產線：v9 多檔 8,945 行、SINGLE 2,169 行、生成版 3,109 行。這是「指標 over 複寫」的反面，三個月後哪份是 canonical 會漂。
- MANIFESTO：退場不刪除。所以是搬 `archive/`，不是 `rm`。precedent 就在同目錄：`docs/pipelines/archive/REWRITE-PIPELINE-v8.0-single-file-2026-07-15.md`。

## 一、搬家（同一個 commit）

目的地 `docs/pipelines/archive/rewrite-v9.9-2026-09-19/`：

| 搬什麼                                                                                                                                         | 數  |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| `docs/pipelines/REWRITE-STAGE-*.md`                                                                                                            | 11  |
| `docs/pipelines/REWRITE-GUIDE.md`                                                                                                              | 1   |
| `docs/pipelines/REWRITE-PIPELINE-單檔案型完整流程.md`（derived；最後一次生成結果一起留當證據）                                                 | 1   |
| `scripts/rewrite/{cli,engine,prompts,view}.mjs` → `…/scripts/`                                                                                 | 4   |
| `scripts/tools/build-rewrite-single-file.py`＋`tests/test_build_rewrite_single_file.py`＋`tests/rewrite-guide.test.mjs`（v9 專用工具，跟著走） | 3   |
| `docs/pipelines/REWRITE-PIPELINE.md` 的 484 行本體 → `…/REWRITE-PIPELINE-v9.9-index.md`                                                        | 1   |

**`docs/pipelines/REWRITE-PIPELINE.md` 這個路徑留下來，改成 ≤ 15 行的轉址 stub**：「現行 canonical → [REWRITE-PIPELINE-SINGLE.md]；v9 多檔型 → archive；退場理由 → LESSONS `third-type-thesis-defaults-to-meta-observation`」。理由：全 repo 用 `REWRITE-PIPELINE.md` 這個名字當泛稱的活檔超過 60 個（EVOLVE／FACTCHECK／MAINTAINER／SPORE-\*／BECOME／harvest prompts…），stub 讓那些連結繼續解析，只有 STAGE／GUIDE 的深連結需要逐條改。

`scripts/twmd.mjs` 拿掉 `rewrite` 子命令（第 27–30 行）。archive 目錄放 `README.md`：v9.9 最後 commit（`025d356a6f` 之前那個切換 commit 的 parent）、為何退場、怎麼復活（`git mv` 回來）。

## 二、讀者改指（搬家同一手）

**必改（會壞或會把 session 帶錯路）**：

1. `.husky/pre-commit` 第 48–60 行整段（`build-rewrite-single-file.py --check`）拿掉，換成 §三 的行數帽。
2. `docs/semiont/routine-prompts/twmd-rewrite-daily.md` 第 14–16 行：`REWRITE-PIPELINE.md` → `REWRITE-PIPELINE-SINGLE.md`。routine 現在 ⏸️，但重開那天會直接跑錯版。
3. `docs/pipelines/README.md` 第 81–82 兩列：改成 SINGLE 一列（SSOT，2026-09-19）＋ archive 一列；把「v9 SSOT，2026-09-05 哲宇拍板」那句拿掉（已被 9/19 拍板取代）。
4. `scripts/core/generate-newsroom-data.py` 第 509–517 行 `ORDER` 的 STAGE 檔名字串：改成 SINGLE 的 Step 編號。它們是純 label，不開檔，不會壞，但 dashboard 會一直顯示已退場的檔名。
5. editorial canonical 深連結，逐條改錨到 SINGLE 對應 Step（**逐條判，不批次 sed**）：`EDITORIAL.md:1511, 1540`／`PROJECTION.md:88`／`PROJECTION-PATTERNS.md:13, 25`／`VIZ-RECIPES.md:16, 298`／`EDITORIAL-ROOM.md:202`／`WRITER-PROMPT.md:36, 86`／`RESEARCH-AGENT-PROMPT.md:22, 88`／`PERSONA-PIPELINE.md:10`。⚠️ 有幾個 v9 step 在 SINGLE 沒有對應（2.0.5 十五類資料關係、2B／2E 兩個編輯室、3.6.3 看圖一列）。那些連結兩種處置：指 archive（當歷史脈絡），或那段規則本身就是 v9 期間長出來的、跟著退場。哪一種，看那段規則是不是 9/19 五條之一在撐——不是就退場。
6. `REWRITE-PIPELINE-SINGLE.md` frontmatter `sister_docs` 移除 `REWRITE-PIPELINE.md`。

**不改**：`scripts/tools/*.py` docstring 裡提到 STAGE（歷史敘事）、`docs/semiont/memory|diary/`、`reports/`、`src/data/changelog-feed.json`、`knowledge/About/文章如何誕生.md`＋譯本（對外文章，另開 EVOLVE，不在本工單）。

**驗收指令**：

```
grep -rlE "REWRITE-STAGE-[0-9]|REWRITE-GUIDE|twmd\.mjs rewrite|scripts/rewrite/|單檔案型完整流程" \
  --include='*.md' --include='*.mjs' --include='*.py' --include='*.yml' --include='*.sh' . \
  | grep -vE "(^|/)(archive|node_modules|\.worktrees|reports|knowledge)/|docs/semiont/(memory|diary)/"
```

→ 只剩 `scripts/tools/*.py` docstring 與 `LESSONS-INBOX.md`；`npm run check-internal-links` 綠。

## 三、凍結（儀器，不是句子）

1. **行數帽 2,300**：`.husky/pre-commit` 新段——staged 含 `REWRITE-PIPELINE-SINGLE.md` 時 `wc -l` > 2300 就擋，訊息「先砍再加：要加 N 行先砍 N 行」。現在 2,169，餘裕 131 行 ≈ 一次 callout 的量，這是刻意的。
2. **版本紀律**（寫進 SINGLE 檔頭一行）：只走 v6.x patch；升 minor 要哲宇拍板＋等量減法。
3. **不長回來的三樣**（寫進 SINGLE 檔頭）：不設冷讀站、不設多席編輯室、不加後設論點形態。這三樣就是 9/18 三篇的病灶，各自都曾經有充分理由被加進來。
4. 不再造「單檔生成器」。單檔本身就是全文。

## 四、規則准入（拆棘輪的那一條）

- **錯 → 儀器，不 → 規則**。事實錯誤（李雪莉 8/27 那型）修資料源、FACTCHECK、`article-health` check；**不新增 pipeline 段落**。
- **悶 → 規則，且只從讀者 callout 進**。哲宇或讀者讀後 callout 才可新增 SINGLE 條文；每條寫明「哪次 callout、哪篇」。
- 理由：v6.7 → v9.9 的 87 個 commit，每一段都是一次錯換來的，沒有一段是一次悶換來的。錯可量、悶不可量，不設准入就單向長。同步 LESSONS-INBOX 一條（pattern `gate-ratchet-only-grows-on-errors`），distill 時進 DNA。

## 五、`opening-readability.py` 的基準

不發明數字，band 由範本定：黃魚鴞前四段 1.5／每百字（humanize brief 量的是 4.2，兩把尺口徑不同，**先統一口徑再定線**）、三篇 v2 0.5–1.6。建議 hard ＝ 範本值 × 1.3，warn ＝ 範本值。哲宇讀第一段仍是最終尺，儀器只擋明顯的。

## 六、候選（不做也行）

下一篇用 SINGLE 但**不帶 banner 五條**跑一次：把 v6.7 本體與五條硬要求的貢獻分開，才知道 2,169 還能砍到多薄。

## 驗收 DOD

- [ ] `docs/pipelines/archive/rewrite-v9.9-2026-09-19/` 存在含 README；`ls docs/pipelines/REWRITE-STAGE-*.md` 回 0
- [ ] `docs/pipelines/REWRITE-PIPELINE.md` ≤ 15 行且指向 SINGLE
- [ ] §二驗收 grep 只剩 docstring；`check-internal-links` 綠
- [ ] husky：故意把 SINGLE 補到 2,301 行 commit 被擋，還原後放行
- [ ] `twmd-rewrite-daily.md` 指 SINGLE；README 兩列改；newsroom ORDER 改
- [ ] LESSONS-INBOX 有 `gate-ratchet-only-grows-on-errors`；OBSERVER-QUEUE §已決一列
- [ ] 一或兩個 commit，訊息寫明「搬 21 檔、改指 N 檔」，數字用 `git show --stat` 算

_Muse 🫧 2026-09-19 10:2x｜依據：muse-bot `memory/2026-09-19.md` 00:46／10:07 段、本 repo `git log`、讀者盤點 grep_

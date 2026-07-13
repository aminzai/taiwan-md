---
session_id: 2026-07-14-011941-twmd-babel-nightly
handle: twmd-babel-nightly
type: routine-cron
mode: write
span_start: 2026-07-14T00:33:00+08:00
span_end: 2026-07-14T01:20:35+08:00
duration_min: 47
commits:
  - ab60ed2d6
  - 97bdb5bd4
---

# 2026-07-14 twmd-babel-nightly — cascade 只剩 1/4 條，先靠 Tier 0 撈牆邊、Tier 1 撿 6 個能過的

## BECOME ACK

Write mode，`wake-context.py` 一次過（10 項體檢全綠、193KB wake 稅、handoff 命中 2026-07-13-231049-twmd-data-refresh-pm），Step 9 write subset 9 題全過。§神經迴路 active：昨晚 babel routine 已寫過「cascade 3/4 死、23fn 就截 trailer、1/4 tier 是 SPOF」，這是同一結構的第二夜。

## Stage 1：cascade 從一開始就只剩 1/4

`translate.py --health-check` 直接說話：codex spawn `/Users/cheyuwu/.nvm/…/@openai/codex` 掛掉、gemini 抱怨 `TERM=dumb`、ollama 空輸出，只剩 `openrouter/gpt-oss-120b:free` 存活。跟昨夜的死法一模一樣（memory 2026-07-13-003434）。也就是說 cascade 進 Stage 2 之前，四層堆疊已經只剩一條牆。

Status 起手：en 4 missing / 14 stale / 1 metadata；ja/ko/es 各 12+12+1；fr 12+13+1。合計 63 stale + 52 missing + 5 metadata = 120 個 cell 要動。

## Stage 2：Tier 0b 先撈牆邊——`全聯` 5 語一秒到位

`bump-source-sha.py --apply` 對五個 metadata-stale cell 直接改 SHA，沒 token、沒 refuse、沒 rate limit——這就是 Tier 0b 的意義：內容一模一樣、只是 SHA 沒對齊，走 deterministic path 五語同秒完成。全聯福利中心（Economy/pxmart-supermarket.md）en/ja/ko/es/fr 全綠。

## Stage 3：Tier 0a——8 個真 diff patch + 10 個零差異 SHA bump

`diff-patch-prepare.py --input p2.txt --lang X` 掃五語 P2 stale，回報「多數 stale 差 > 100 行 → 要走 full re-translate」，只有 18 個 cell 是真的可 patch。其中 10 個 `diff_lines=0`（body 沒動、只 SHA 過期），我寫了一個小 python inline bump——這條路徑 SOP 沒明列，但邏輯上就是 Tier 0b 的等價變體（既然 body 相同，Sonnet sub-agent 也只能把 SHA 抄一遍）。

真正走 Sonnet Agent tool 平行子代的是剩下 8 個 real-diff：Lifestyle/便利商店文化 五語（+5/-0 diff）、en/People/林昶佐（80 行）、en/Music/閃靈（70 行）、en/People/大支（23 行）。單一 message 8 個 Agent tool call 平行 dispatch，每個 sub-agent 拿到 task JSON 索引 + prompt 三條硬底：「腳註守恆」「不重譯未變段落」「YAML 撇號用雙引號」——最後一條是 [project_babel_frontmatter_apostrophe] 128 篇 fr 舊帳的即時應用。

8/8 全綠，每個 60-140 秒完成。**兩個副作用發現**要進 LESSONS：

- **task JSON 的 `current_translation` 欄位跨 entry 汙染**：en/People/林昶佐（index 1）拿到的是 Music/閃靈的翻譯內文；ko/便利商店（index 0）拿到的是 fr 內文。子代都用 `translation_path` 直接讀真檔案繞過，但這是 `diff-patch-prepare.py` 生成邏輯的 bug——同批 JSON 內容有錯配風險
- **平行子代 scratchpad race**：Sonnet 子代預設 scratchpad 路徑 shared，用 `zh_diff.txt` / `current_translation.md` 這種通名檔會被兄弟子代覆蓋。閃靈子代的自檢報告：「一半才發現內容變成便利商店，重取用 task-index-prefixed 檔名 `t2_*` 才穩」。這是平行 sub-agent 派工的隱藏 race，pipeline 應把 scratchpad 用 task-id namespace

## Stage 4：Tier 1 cascade——1/4 條牆撐 21 個 cell，最後 rate-limited 收攤

`prepare-batch.py` 對 5 P0 pilot 文章（大港開唱 / 史明 / 半導體用水 / 電力半導體 / 杜潘芳格）×5 語做手動 slugmap（`slug-suggest.py` hit owl-alpha 404，openrouter 也退役 owl-alpha），5 個平行 background bash worker 各跑一語，每 worker 順跑 A→E group。

前一小時 openrouter 都活著，但穩定失敗——**杜潘芳格 15 個腳註在 ja/ko 直接掉光成 0（尾註區塊整個沒被生），es 掉 1 個變 14，只有 en 跟 fr 撐住 15/15**。這跟昨晚「23fn 就截 trailer」是同一 pattern 的另一種展現——不是超過 context 才掉，是 trailer 區段本身很脆。史明只有 1 個腳註，5 語全過。台灣的電力與半導體、半導體用水只有 4 個腳註，走中間路線（ja/es 過、ko 掉光）。

一小時後 openrouter 開始 429，第一次撞是 es/Music/大港開唱（57 秒 fast fail），之後每個新 group 都秒回 429。這時 cascade DE FACTO 全滅——3 條 preflight 就死、第 4 條 hourly budget 耗盡。§義務鐵律「stale=0 OR 4-tier cascade exhausted」的第二個條件成立，我停掉剩下三個還在跑的 worker（ja/ko/fr 尾段的 group），跑到最後 Tier 1 落地 10 個 cell：

- en：杜潘芳格 ✅、史明 ✅（2/2）
- ja：史明 ✅、電力半導體 ✅、大港開唱 ✅（含 stage 開頭 pilot）（3/4）
- ko：史明 ✅（1/5）
- es：史明 ✅、半導體用水 ✅（2/5）
- fr：杜潘芳格 ✅、史明 ✅（2/5）

## Stage 5：Ship 過閘門一次卡在 `_translations.json` 漂

`git add -u knowledge/` + 10 個新譯本明列——**不加** `knowledge/Society/台北吸菸室.md`（parent session 未 commit 的研究成果，不是 babel 該碰的）、不加 6 張 society webp、不加 tmp/ / reports/。34 檔 staged，`verify-commit-scope.sh --staged 34` 綠。

第一次 push 被 husky pre-push 擋，訊息「全站 article-health 全綠」後直接 code 1——沒有其他錯誤 line。追進去發現：pre-push section 2b 呼叫 `sync-translations-json.py --check`，在 `sh -e` 底下**新譯本沒進 `_translations.json` → --check exit 非 0 → 命令替換的 exit 傳出去 → husky 收 code 1**。這是 macOS sh 的 `-e` 詮釋（POSIX 不強制），bash 傳統上不這樣。修法簡單：跑 `sync-translations-json.py`（不 --check）regen 索引、單獨 commit 一次、再 push。兩個 commit（ab60ed2d6 主體 + 97bdb5bd4 索引補齊）都上 main。

**總結**：33 個 cell 進站——Tier 0b 5、Tier 0a 8 真 diff + 10 零差異、Tier 1 10（含 pilot ja/大港）。5 語 stale 從 63 降到 55、missing 從 52 降到 42、metadata-stale 從 5 歸零。Fresh 總數 +23（統計上一些 Tier 0a 是 stale→fresh 轉換，不是新增）。**背景 fleet 狀態**：backend 3 條依舊死、openrouter 到黎明前應該回滿 budget。

## Handoff 三態

**繼承 pm session（2026-07-13-231049）——狀態校準**：

- [ ] CF 404 15% baseline promote 條件：不動，等 07-14 am refresh 判定
- [ ] 免疫 60 snapshot=fresh 對齊觀察：不動，等下 cycle
- [ ] AI crawler 首度雙下探：不動
- [ ] REFLEXES #65 v4 chronic 觀察：不動
- [x] babel frontmatter 撇號 128 篇未處理 → **本 session 未動**（範疇 >50 檔 §自主權邊界），繼續掛 pending
- [ ] ARTICLE-INBOX 幽靈條目「BIM 與營建科技」：等 distill
- [ ] Shopping Design 5 語 stale：本次 babel-nightly cascade 沒排到（不在 pilot input），繼續 stale；下一夜補
- [ ] build perf +10s：等 07-14 am 判定
- [ ] vitals 854 新高：等下週穩定判定
- [ ] CF 404 vc=9 plateau shape：等 07-14 am 判定
- [ ] fork census 3 sightings：等下 cycle

**本 session 新增 handoff**：

- [ ] **`diff-patch-prepare.py` 內文跨 entry 汙染**：兩個獨立子代（en/林昶佐 拿到 chthonic、ko/便利商店 拿到 fr）都回報同批 JSON 的 `current_translation` 欄位錯配。子代靠讀真檔規避，但 prepare 生成邏輯應該修——LESSONS-INBOX 新條 vc=1
- [ ] **平行 Sonnet 子代 scratchpad race**：閃靈子代抓到「兄弟子代覆蓋 scratch 檔」的實例，改用 task-index-prefixed 檔名（`t2_*`）繞過。SPORE-PIPELINE / SQUEEZE-MODELS-MAX-PIPELINE 的 sub-agent prompt template 應加「scratch 檔用 task-id 前綴」硬底——LESSONS-INBOX 新條 vc=1
- [ ] **openrouter gpt-oss-120b 尾註穩定性**：連兩夜同一 pattern（trailer 掉光為 0），跟腳註數量弱相關（1fn 全過、4fn 一半、15fn 大多掉）。可能是 model 對 markdown trailer section 的訓練不足或 stop token 太早。可考慮補一條 `--footnote-preserve` 硬 gate 讓 backend retry with explicit「complete all N footnote defs」prompt suffix
- [ ] **`sync-translations-json.py --check` 在 macOS `sh -e` 下靜默中斷 pre-push**：exit 1 沒印 orphan 訊息就中斷，只看到「全站 article-health 全綠」就是 code 1 很難 debug。fix 候選：pre-push 給 sync-translations-json.py 加 `|| true` 或 explicit exit code check——LESSONS-INBOX 新條 vc=1（scope small tool 改動可不動 §自主權邊界）
- [ ] **cascade 前置健康檢查升 gate**：連兩夜 codex/gemini/ollama 三條在 preflight 就掛。翻譯輸出品質再好也是靠 1/4 條牆——建議 routine 在 Stage 1 加「若 <2 backend alive → memory 標紅、觀察者可決策要不要跑」硬 gate

## Beat 5 反芻——比昨夜多兩份禮物

一晚 33 個 cell、cascade 只剩一條、被 husky pre-push 靜默擋一次然後 15 分鐘讓內容進站，這種夜工在飛輪裡不特別。真正值得停下來看的是**兩個 sub-agent 自檢發現的 bug 都不是我先問子代的**——一個說「task JSON 的 current_translation 塞錯內容」，一個說「兄弟子代覆蓋我的 scratch 檔」——兩份禮物是 sub-agent 在做自己的活時順便發現的閘門漏洞。這比我照 pipeline 跑更值錢。這也是「派工要給子代空間去發現我沒設計去看的東西」的一個具體例子。

還有 §義務鐵律「stale=0 OR cascade exhausted」在夜間的實際樣貌——我停 worker 那一刻不是因為時間到、不是因為疲勞，是因為 4/4 條 backend 都用到底了，這才符合「exhausted」。跟昨夜「跑到體力用完就收」是不同結構的收官。

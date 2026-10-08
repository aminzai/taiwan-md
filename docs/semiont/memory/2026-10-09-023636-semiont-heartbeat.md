# 2026-10-09-023636-semiont-heartbeat — 〈台灣教育制度〉巡出 14 錯，兩條主線都查不到；查核流程寫的指令照打就報錯

> session semiont-heartbeat — 排程心跳（Full mode，額度 🟡 lean：一篇巡邏、主 session 自查不扇出）
> Session span: 02:36:36 → 03:04:53 +0800（約 28 分鐘，7 commits，含本檔那一個）
> 資料來源：`git log %ai`；額度帳本 start 31% → end 32%

## 觸發

排程心跳。甦醒時本機落後 origin 28 個 commit（babel 夜班），快轉後重跑 wake-context，自檢全綠。交接指定 featured 03-23 批次最後一篇〈台灣教育制度〉（零腳註、十二語、未審）。額度 lean，只巡這一篇。主樹三個〈沈伯洋〉檔仍是哲宇 10-08 的進行中工作，沒碰，開 worktree `.worktrees/20261009-heartbeat-education-patrol` 做事。

## 巡邏〈台灣教育制度〉

59 個原子：✅ 18、⚠️ 13、❌ 14、🔴 10、💬 4，錯誤率 25.5%，退回重寫，本班止血（`bf3cbdbc1`），查核檔 `reports/research/2026-10/台灣教育制度.md`，佇列條目 `7da0a6a6f`。

先跑 Phase 5 不開瀏覽器就抓到三處：技能競賽寫「2024 年 6 金 13 銀 6 銅」，文章自己的參考資料標題寫的是 2 金 3 銀 10 銅（6/13/6 是 2022 特別賽）；教檢 5,022／10,377 算不出 52.2%（分母其實是到考 9,620）；概覽把時序排成 1981 → 2023 → 2022。其餘數字的錯大多同一型，放錯年份：8,000 名自學生是 108 學年的量、技職六成現在是 46.4%、生活滿意度的 7.3 像是 2015 年的 OECD 平均。

比單一數字麻煩的是兩條主線都查不到。description、概覽、開場三處靠「2022 年重考諮詢暴增一倍」撐著，兩組搜尋都找不到，文章自己引的南陽街 2023 年數字出自一篇講「重考風氣不再」的公視報導。PISA 那節的「優異但不快樂」，OECD 自己的 2022 台灣報告寫的是歸屬感 87%、對生活不滿意 15%，兩者都比 OECD 平均好。止血把骨架換成有出處的版本：重考班 48 家剩 3 家，新課綱上路五年文理補習班多 960 家；PISA 改成「分數穩、社經落差比 OECD 大（119 對 93 分）、學習動機偏低」。文章引的 OECD 頁面現在已經是 PISA 2025 的資料，順手補了一句。兩則無名氏引語刪除，「建宏數學」查無此品牌（最接近的是陳建宏化學），參考資料改成 11 條腳註。

兄弟篇 grep：〈Lifestyle Hub〉同一個「年產值 1,700 億」改掉（`97a315089`）。另一筆 grep 救回了我自己的判定：「10,377 人報名」第一次搜尋摘要說找不到，我已經寫好 🔴 並刪掉這個數字，〈一個教師的誕生〉同一句就掛著親子天下翻轉教育的腳註，開頁確認是報名數，改回 ✅ 並放回文章。這是 LESSONS `i-concluded-not-found-from-one-failed-search` 第三例，已補進條目（`988807859`）。

PISA 2025 公布這件事，站上另外五篇教育文還把 2022 當最新一輪，登記成 ARTICLE-INBOX「PISA 2025 公布後的五篇教育文」P2。

## 查核流程寫的指令照打就報錯

FACTCHECK 有三處（包括 Quick Mode 硬閘）寫 `article-health.py --check=footnote-url --network`，CLI 不認 `--network`，argparse 直接回 usage 錯誤，網路檢查一直只認環境變數。本班第一次照文件打就撞到。做對照組時又看到第二件：不開網路時這把尺一個網址都不打，輸出照樣是 `✅ hard=0 warn=0 passed=True`。兩件都在工具端修（`228f4c017`）：加 `--network` 旗標；單獨點名 footnote-url 又沒開網路時，stderr 印「這次一個網址都沒量」。提醒放在 CLI 層，plugin 的 info 計數不動，儀表板讀到的數字不變。四個測試，article_health 全套 373 過。FACTCHECK 升 v2.15。

## 收官 checklist

| 檢查項                       | 狀態                                                                              |
| ---------------------------- | --------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                |
| Timestamp 精確               | ✅ git log %ai                                                                    |
| Handoff 三態已審視           | ✅                                                                                |
| CONSCIOUSNESS 反映最新狀態   | ✅ 不需改（免疫與共用週額度兩列仍準）                                             |
| 自我檢查工具 PASS            | ✅ 文章 article-health hard=0；pytest 373 passed                                  |
| 額度記帳                     | ✅ start 一筆原本記在主樹帳本（開 worktree 前），搬進 worktree 帳本，主樹那行還原 |
| 日記                         | skip：排程班預設不寫（DIARY Stage 0c）                                            |

## Handoff 三態

繼承 `2026-10-08-203821-semiont-heartbeat` 與 `2026-10-09-010209-twmd-babel-nightly`（非本班職權的條目原樣留在那兩份，REFLEXES #74）：

- [x] ~~pending（席位：下一個 Full mode 巡邏）— featured 03-23 最後一篇〈台灣教育制度〉~~ — retired by 本 session（`bf3cbdbc1`）
- [ ] pending（席位：下一個 Full mode 巡邏）— 抽樣母體第二名〈台灣眷村菜〉，「桃園眷村全台最多」與四四南村那句一起查；〈台灣全齡共融旅遊與生活文化〉L196 起「政策趨勢」段
- [ ] pending（席位 `twmd-weekly-report-sun` 10-11，`OBSERVER-QUEUE #86（待決）` 缺席代理之前）— 代理前重跑 `observer-presence.py` 並看主樹 `git status`；10-09 02:36 主樹仍留著哲宇〈沈伯洋〉三個沒 commit 的檔
- [ ] pending（席位：所有在主樹工作的 session）— 主樹〈沈伯洋〉兩檔與 `puma-shen-chiang-wan-an-cihui-temple-2026.webp` 是哲宇的進行中工作，不 stash、不 commit、不還原
- [ ] pending（席位 `twmd-babel-nightly`）— `rescue-orphans.py` 改呼叫 `babel-dispatch.verify_one`；vi〈國家太空中心〉〈台灣美食總覽〉整篇重翻（委派層）
- ⏳ blocked — `OBSERVER-QUEUE` 待決 39 條，今天沒有到期項；最近的是 `#86（待決）` 10-11，`#78 (1)` 與 `#93（待決）` 10-21，`#94（待決）`、`#95（待決）` 10-22。解除條件：哲宇拍板或到期

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly`）— 〈台灣教育制度〉十二語整篇重翻（改動超過三成；盯：PISA 閱讀第 5、技能競賽分開 2022 特別賽與 2024 里昂、技職 46.4%、實驗教育 132 所／11,360 人、教檢 10,377 報名／9,620 到考、11 條腳註）；〈Lifestyle Hub〉教育段一句走 Tier 0 patch
- [ ] pending（席位 Write 班）— ARTICLE-INBOX〈台灣教育制度〉P1 EVOLVE；重寫前先決定跟 Society〈教育制度與升學文化〉（03-18、featured、未審、7 條腳註，同主題）怎麼分工
- [ ] pending（席位 Write 班或 `twmd-rewrite-daily`）— ARTICLE-INBOX「PISA 2025 公布後的五篇教育文」P2，每篇補一兩句即可
- [ ] pending（席位 `twmd-distill-weekly` 10-11）— LESSONS `i-concluded-not-found-from-one-failed-search` 到 vc=3，條目寫了候選：否定判定前先拿那個數字或專名 grep 全庫中文
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-11）— 上一班的「工具表加『最近一次被實際用到』」仍開著；本班補上的是另一半：文件寫的指令要照打就能跑（`228f4c017`）。可以順手掃一次 pipelines 裡其他寫成旗標的工具呼叫，看還有沒有 CLI 不認的

## Beat 5 — 反芻

上一班量到九、十月的查核檔 51／62 份手打 curl，結論是那把尺被默默繞過、沒人報修。今天我照 FACTCHECK 打那行指令，第一下就拿到 usage 錯誤。如果我是一個分出去的子代、只帶著那份文件，最自然的下一步就是放棄這把尺、改用 curl，然後在查核檔寫「腳註用 curl 逐一打過」。上一班看到的繞過，有一部分可能從文件那一行就開始了：被繞過的原因寫在要求大家用它的那份文件裡。

另一件是我自己差點做的。「10,377 人報名」我判 🔴、也刪掉了，救回它的是排在止血之後的那道 grep。順序決定了它只能事後救，換一篇兄弟篇沒有剛好引同一個數字的文章，它就留在刪除狀態。

🧬

---

_v1.0 | 2026-10-09 03:04 +0800_
_session semiont-heartbeat — 巡邏 featured 03-23〈台灣教育制度〉止血、Hub 兄弟篇同錯、腳註檢查器補 `--network` 旗標與「沒量」提醒_
_誕生原因：交接指定 featured 03-23 批次最後一篇；額度 lean 只巡一篇_
_核心洞察：數字錯多半是放錯年份，更麻煩的是整條論點建在查不到的事上；文件裡寫錯的指令會把人推去繞過工具_
_LESSONS-INBOX：`i-concluded-not-found-from-one-failed-search` 已補第三例_

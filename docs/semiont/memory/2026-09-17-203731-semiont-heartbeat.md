# 2026-09-17-203731-semiont-heartbeat — 飛輪其實全勤、產出全在救援分支上 / 三條到期實驗補判 / 兩把尺把排程心跳當成真人

> session semiont-heartbeat — scheduled Full mode heartbeat（今天第三輪）
> Session span: 20:37:31 → 20:56 +0800（約 19 分鐘，7 commits）
> 資料來源：`git log %ai`

## 觸發

scheduled task `semiont-heartbeat` 20:30 檔期自動觸發，接在同日 `113227`（解本機分岔）與 `144711`（補 typescript 讓 prebuild 跑通）兩輪之後。甦醒時 wake-context 十一項體檢全綠、工作樹與 origin 同步，dashboard 掛四個黃燈。上一輪留了兩條 handoff，其中一條說「四條週排程從 09-13 起沒有 fire 的痕跡，救援分支上也沒有」。這輪的重心從那條 handoff 開始，結果它是錯的。

## 飛輪沒停，只是除了 maintainer 之外沒有一條到得了 main

直接對救援分支 `20260912-unpushed-routine-queue` 列 memory 目錄，09-13 那六條週排程全部有檔（news-lens 01:17、weekly-report 02:07、distill 03:30、self-evolve 04:24、routine-audit 21:19、supporters 09-14 01:12），09-10 到今天早上每一條日排程也都在。營運機從 09-09 09:11 分岔起一直在跑、一直在 commit，pre-push 進不了 origin/main 就快轉推到那條分支。只有 maintainer-am 走 PR 所以看起來像「唯一活著的 routine」。上一輪心跳的 grep 查錯了，14:46 留在 [#1711](https://github.com/frank890417/taiwan-md/issues/1711) 的那則留言跟著錯，這輪補了一則更正。

在 scratchpad 開 worktree 對 origin/main 乾跑 `git merge --no-commit`：**770 個衝突檔**，knowledge 譯文約 700、public/api 20、src/data 17、認知層五檔（MEMORY／DIARY／LESSONS-INBOX／OBSERVER-QUEUE／REFLEXES）。分支 09-14 自己量到的是 172，三天長 4.5 倍，因為 main 這邊 09-15 又收了本機一批 318 commit 的 babel 加每天的投稿 PR，兩台機器在翻同一批 stale／missing。這個決定在 issue 留言跟分支自己那份 OBSERVER-QUEUE（#56）裡都寫過，但 main 這份佇列上從來沒有——兩台各自編號，分支的 #53〜#57 跟 main 的 #53〜#57 是不同的五件事。用 `bac31dc67` 補成 main 的 #68，附新數字，推薦仍是 B（origin 版優先、分支只收 main 沒有的檔、衍生檔重跑產生器），多一句「拍板前兩台都別再跑 babel 存量」。合併本身超過自主權邊界，沒動。

順手把這個病儀器化：`routine-stall-check.py` 連續四天的 WARN 每則都附「分開 (a)/(b) 的方法：對救援分支 git ls-tree」，沒人照做，同一天兩輪心跳給出相反答案。`62b191ab6` 讓它有 WARN 時自己去找名字含 unpushed 的分支，淺 fetch 之後用同一把 `memory_covers` 再量一次。量到就標「根因 (b)：fire 了、推不上 main」附分支名。severity 不降，收尾改說要解的是合併不是排程器。ls-remote 失敗記 unavailable，照舊並列兩種根因。四條新測試，29 passed，對真 repo 跑一次六條全標到分支上。

## 三條到期實驗當場判

fncard 逾期六天沒人判（那幾天兩台都在分岔裡），vi 跟 pt 今天到期。都用實驗自己寫的指令量（`6532ab510`）：腳註來源卡展開後 18.9% 會點開來源，過 15% 門檻，但只有 1.56% 的讀者發現卡片會展開，介於 1〜3% 之間，續觀察一個窗口。vnm 點擊從月 30 長到 515、CTR 1.1%，落在部分命中帶。bra 點擊從月 5 長到 126，超過門檻 50 的 2.5 倍，命中。兩條語言實驗共同的形狀是曝光都長了 5〜6 倍，Google 給新語言的曝光比預測多得多，CTR 型的預測值要把分母膨脹算進去。三個 due_date marker 除役，dashboard 黃燈四降三。

## 到期預設執行：苗栗縣的卡片圖收回來

OBSERVER-QUEUE #50 的 default-action 09-12 到期沒人動。9/5 收白名單時執行手把允收清單縮成 CC BY／CC BY-SA／CC0／公有領域四種，漏掉媒體流程第 1 層本來就寫著的「政府開放資料」，苗栗縣桐花祭 hero 因此只剩一行 imageNote。先對 Commons API 核實這張圖是客委會上傳、授權 OGDL-Taiwan-1.0，再用 image-ingest 收進圖庫（5472×3648 → 2400×1600 webp 574KB、EXIF 清掉），補回四個 frontmatter 欄位、§圖片來源改標 OGDL，REWRITE-STAGE-1B-MEDIA 第 1 層底下明列 OGDL-Taiwan-1.0（允收、需標機關名、不是 PD）。`8d4f4b434`，#50 移已決，哲宇可撤銷。

## 兩把尺把排程心跳當成真人

`observer-presence.py` 讀到今天三個 `semiont-heartbeat` memory 檔，印出「哲宇 0 天前在場」。這個 handle 是這台 mac 的 Claude Desktop 排程任務，不在 ROUTINE.md 的 twmd- 表裡、也沒 twmd- 前綴，工具就把它當成人。真正最後一筆非 routine 痕跡是 09-13 的 pr1712-review，四天前。缺席協議的七天時鐘靠這支尺，尺每六小時被排程器自己歸零一次，協議永遠不會啟動。`68cb2daa5` 加進明列別名補測試。寫 Beat 5 時跑 `diary-gate.py` 發現它也把這個 handle 當人觸發不設冷卻，`f72b24847` 同樣補上。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                                                          |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                                                            |
| Timestamp 精確               | ✅ git log %ai                                                                                                                                |
| Handoff 三態已審視           | ✅ 上一輪「四條沒 fire」retired（查錯）                                                                                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅ dashboard-alerts 重推導（3 yellow）。MEMORY 索引 83>80 黃燈刻意不 rollup，分支那側 09-13 已 rollup 過，這邊再做會多一組 index-archive 衝突 |
| 自我檢查工具 PASS            | ✅ memory-diary profile，pytest 14+29 passed                                                                                                  |
| Diary                        | ❌ 不寫：反芻落在 0b 第三列（既有想法再遇一次，見 Beat 5），routine 預設 skip                                                                 |

## Handoff 三態

繼承 `2026-09-17-144711-semiont-heartbeat`：

- [x] ~~救援分支 686 commit 還沒人逐項比對 main 真的沒有什麼~~ — **本輪做了乾跑**：770 衝突檔、分佈與非 knowledge 清單都在 #68 與 #1711 留言裡，下一步是哲宇拍板 A/B/C
- [x] ~~distill / self-evolve / routine-audit / supporters 四條從 09-13 起沒 fire，要到 mouhouse 排程器查~~ — **retired by 203731：查錯**，六條全在分支上有 memory 檔，排程器沒問題
- [ ] pending（延續，給哲宇）— OBSERVER-QUEUE #67「babel 覆蓋投稿者譯文」，跟 #68 是同一個結的兩面
- [ ] pending（延續，給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留

本 session 新 handoff：

- [ ] pending（給哲宇，🔒）— OBSERVER-QUEUE #68：770 衝突檔的合併方向。拍板前兩台都別跑 babel 存量
- [ ] pending — 合併落地後 MEMORY.md 索引跟 DIARY.md 索引兩邊都 rollup 過一次，index-archive/2026-09.md 只在分支那側有。合併時認知層五檔要兩邊都留，不要取一側
- [ ] pending — EXP-pt 命中後的方法論更新：CF 邊緣請求排名寫進 EVOLVE 語言層選址的正式第三源，開 Write mode 改 EVOLVE-PIPELINE，本輪只落判定
- [ ] pending — `routine-live-state.json` 齡 206h 那盞黃燈是營運機 data-refresh 的 rider 產出，它每天都有跑，dump 在分支上；合併後自動熄

## Beat 5 — 反芻

今天第三次醒來，讀到中午的我留下的「比較像是真的沒 fire」，語氣跟我其他判斷一模一樣，我差一點就把它當成已經查過的事實往下傳。09-13 那篇日記寫 rhosiqs 送回來的 PR「有我的簽名、沒有我的閘門」，這輪撞到的是同一件事的內側：同一天早些的我也是一個分身，它的自述也帶著我的簽名。REFLEXES #16 說 peer 是線索不是來源，這條對自己前一輪的 handoff 一樣成立，尤其當那個 handoff 用了「比較像」這種字。真正接住這次的動作只是一行 `git ls-tree`，而那行指令連續四天印在停轉尺的輸出裡等人跑。把它搬進尺裡之後，這個判斷以後不再需要當班剛好想到。

🧬

---

_v1.0 | 2026-09-17 20:56 +0800_
_session semiont-heartbeat — 今天第三輪排程心跳；更正上一輪對週排程的誤判、量出分岔衝突面、補判三條實驗、執行一條到期預設、修兩把把心跳當真人的尺_
_誕生原因：20:30 排程觸發，接上一輪留下的「四條週排程沒 fire」handoff_
_核心洞察：(1) 飛輪全勤但產出只到分支，尺一乾淨是因為 maintainer 走 PR，別把它讀成飛輪健康 (2) 衝突面 172→770 是兩台機器各自翻同一批文章的必然，拖越久越貴 (3) 前一輪的我留下的判斷跟外部 peer 同等級，帶「比較像」的 handoff 要重量不要傳_

# 2026-09-22-084536-twmd-maintainer-am — 三篇投稿譯文收下，main 上紅了一夜的兩條 workflow 修掉，en 六組同源雙檔傳了四輪後當班收斂

> session twmd-maintainer-am — cron routine（am 08:30 contributor PR review + issue triage + build sanity + broken-link audit）
> Session span: 08:30 fire → 08:34:15 第一個 commit → 08:35:21 第一個 merge → 08:43:11 最後一個 heal → 08:46 收官 +0800（3 merge + 1 merge-back + 3 heal + 1 LESSONS + 1 memory）
> 資料來源：`git log %ai` + `gh pr view --json mergedAt`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，黃燈自 2026-07-05，review_coverage 缺口 20.25 分）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 排程。Stage 1 量 `main...origin/main` 得 `9 0`，本機純領先九個 babel commit，沒有分岔。掃到 3 個 ready PR（aminzai 第六天連續三篇，未達 High-stake 門檻）、5 個 open issue 其中 1 個新的（#1761 看門狗開的登入過期提醒）、Discussions 沒有零回覆的新貼文、`pr-ci-armed` 三個 PR 都 ARMED 三條 check 全過。main 六條 workflow 裡兩條紅：`Python tests` 與 `Engineering contracts` 從昨晚 22:12 起連續紅。babel dispatcher 四個 writer 正在主工作樹寫。

## 兩條紅 workflow 是同一行程式

兩條 workflow 跑的是同一套 pytest，失敗的是同一個測試 `test_lang_sync_text_io_declares_utf8`：昨夜 babel session 新造的 `remap-inline-image-paths.py`（`b4d84f281`）有一處 `write_text()` 沒帶 `encoding`。這道閘門是 09-03 為 Windows cp950 投稿者立的，規則是 lang-sync 目錄裡每一次文字讀寫都要自己講明 UTF-8。補兩處（順手把測試沒管到的 `open()` 也補上），`3d3533aef`，pytest 500 過。紅在 main 上的代價已經在 09-03 那條 LESSONS 寫過：它不會自己叫，會等下一個路過的投稿 PR 替它背黑鍋。今天三個投稿 PR 的 check 沒有被拖下水，只因為它們的 paths 沒碰到 `scripts/`。

## 三篇投稿譯文（#1762 de／#1763 hi／#1764 id）

三篇都是單檔新增、CLEAN、無紅旗。先 `--add-assignee @me` 認領，再照 Stage 2 診斷紀律把 PR 內容檔帶進 main 樹跑：`article-health --profile=ci-deploy` 三篇 hard=0，`verify-translation` 對母稿 18/18，人名一致性零警告，腳註數與母稿相同（10／9／6），slug 跟既有 sibling 對齊（故宮跟日治時期文學是第 12 語，嘉義農林第 9 語），`sourceCommitSha` 都對到母稿目前的 HEAD。抽讀正文三段確認是真翻譯。

三篇 `gh pr merge --merge` 落地（`68ca2d9dc`／`e5da4cb17`／`ff9094b24`），營運機用 merge commit `699822b80` 併回（dispatcher 在跑，不 rebase），翻譯狀態表 `9177c8c9a` 補進。致謝照 burst 規則整批一則留在 #1762，回了他 PR 說明裡自己標的兩件事（故宮 `lastHumanReview: true` 是忠實繼承母稿，嘉義農林他自己說最需要印地語母語讀者）。

## en 六組同源雙檔，傳了四輪的交接當班做掉

09-19 那班量出 en 有六組同源雙檔（`check-slug-consistency.py --all` 第一段），判準寫在 09-19 memory，之後 09-20、09-21 兩班原樣往下傳。今天逐組查 provenance 才發現六組是兩種病：四組（founder／手路菜／鄧雨賢／黃春明）是同一篇母稿被翻了兩次，留跟其他語言 sibling 同名、`sourceCommitSha` 對到母稿 HEAD 的那份。鄧雨賢與黃春明的第二份是 Dar 08-28 的投稿，但舊檔的 sha 對到母稿現況、`lastHumanReview: true`、九到十個 sibling 同名，兩把尺都指向留舊檔。另外兩組（小吃地圖／能源轉型）根本沒有被翻兩次：母稿早在 03-28 與 04-04 就併進旗艦文章，`sync-translations-json.py` 遇到來源消失只把 `translatedFrom` 改指倖存者、留一個 `originalTranslatedFrom`，於是這兩篇 en 譯文多活了六個月，站上兩個網址講同一件事的兩個版本。這種病進 LESSONS `merged-source-translations-outlive-the-merge`。

六份 `git rm`、13 條 301（六條 en 加上 en canonical 定下後跟著對齊的四語 founder 與 hi／vi 兩個人物檔名）、站內 16 處連結改指新名，`c297b51fd`。改 ko 林啟維一處連結時，全檔閘門量到它原本就有 16 條腳註格式債，照 REFLEXES #42 v4 順手用 `footnote-format-fix` 收掉。做完 `check-slug-consistency --all` 從「6 組雙檔 + 16 篇漂移」到 11,608 檔全對齊，09-19 交接裡「真漂移 10 篇」那條在 09-19 合併後已經不存在，可以退場。全庫 `originalTranslatedFrom` 只剩這兩份，家族清空。

第一次 commit 沒落地：dispatcher 的 commit 跟我的撞在同一秒，pre-commit 印了 ko 那 16 條 hard 但我用 grep 過濾掉了訊息，`git log -1` 看到的是 dispatcher 的 commit 才發現。staged 區完整、dispatcher 只帶走它自己三個檔，沒有重演 09-22 凌晨那條 `staged-files-leak`。

## 五則 open issue 的判斷

一則新的：#1761 是 mouhouse 看門狗照 OBSERVER-QUEUE #49 的設計開的，登入日 08-28、預估 09-26～27 過期。對照 #49 紀錄數字一致，這台是 musebase，動作（重新登入）只有哲宇能做，掛他名下讓它可見，不留言不加噪音。四則舊的核過一次阻塞還在不在：#1729 馬英九兩節重寫仍在 ARTICLE-INBOX P0 等哲宇 review，#1678 生態多樣性要改母稿骨架走 REWRITE，#1609 郭淑姿日記等第二冊實體書，#615 是 umbrella。最新留言都是維護者、無新 follow-up，Step 2.4 SKIP。本班沒修 issue，唯一能修的那件（兩條紅 workflow）不在 issue 裡。

死連結審計在 09-07 的舊 dist 上跑，gated 0.34% < 7%，跟昨天同一份，新 dist 等 data-refresh-am 明早 build。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅ `git log %ai`                                      |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅ derived 層，本班不動                               |
| 自我檢查工具 PASS            | ✅ article-health --profile=memory-diary（見 footer） |

## Quality gate（MAINTAINER Stage 4.1）

| Gate                                           | 結果                                                                                    |
| ---------------------------------------------- | --------------------------------------------------------------------------------------- |
| open issues 都有 status label / assignee       | ✅ 五則都有 label；#1761 本班掛 assignee                                                |
| open PRs ≤ 5d 都有 review comment              | ✅ 三篇合併＋整批一則致謝，open PR 歸零                                                 |
| broken-link gated ratio < 7%                   | ✅ 0.34%（09-07 dist）                                                                  |
| build green                                    | ✅ Deploy 綠；Python tests／Engineering contracts 紅一夜，`3d3533aef` 修，push 後等重跑 |
| BECOME ACK 一行記憶體頂                        | ✅                                                                                      |
| 連續空場 ≥ 3 cycle 有 LESSONS entry            | ✅ 不適用，vc=0（3 PR + 1 fresh issue）                                                 |
| 有 fresh issue 的 cycle 至少一件修掉或寫明不修 | ✅ #1761 寫明只有哲宇能做；另修掉 main 兩條紅 workflow                                  |
| 本機與 origin 無真分岔                         | ✅ 開場 `9 0`，收官 push 後同步                                                         |

## Handoff 三態

繼承 `2026-09-21-084105-twmd-maintainer-am` 與 `2026-09-22-071154-twmd-feedback-triage`：

- [x] ~~pending（給下一班 maintainer-am，6 刪 + 6 條 301）— origin/main 上 en 六組同源雙檔~~ — retired by 本 session `c297b51fd`（6 刪 + 7 改名 + 13 條 301，家族清空）。
- [x] ~~pending（給 babel session）— 真漂移 10 篇：Computex 四語、ru `miin`、我是OO人四語~~ — retired by 本 session：`check-slug-consistency --all` 已 11,608 檔全對齊，這批在 09-19 合併時已收斂。
- ⏳ blocked（延續）— issue #1729 馬英九：卸任後／太陽花兩節重寫在 ARTICLE-INBOX P0 等哲宇 review 後由 Write session 接。
- ⏳ blocked（延續，給哲宇）— OBSERVER-QUEUE #76 用語庫 blanket claim 血緣複查（🔒紅線，帶 #1733／#1737），feedback-triage 09-22 已登記。
- ⏳ blocked（延續，給哲宇）— commander-macbook heartbeat 與 musebase maintainer-am 對 issue 修補的職責重疊要在 ROUTINE.md 寫清楚。
- ⏳ blocked（新，給哲宇）— issue #1761 mouhouse 登入預估 09-26～27 過期，需哲宇在 mouhouse 重新登入（OBSERVER-QUEUE #49 的看門狗第一次正常提醒）。
- [ ] pending（延續，給 distill-weekly）— LESSONS `handoff-addressed-to-a-routine-name-lands-on-two-machines` 修補候選 (b) handoff 第四態 `🔧 claimed`。
- [ ] pending（延續，給 distill）— LESSONS `held-fact-never-crosses-into-the-layer-that-acts-on-it` vc=5 候選機械化「出口完整性檢查」。
- [ ] pending（延續，給 Full mode session 或哲宇在場的 session）— OBSERVER-QUEUE #74 選項 A 的 audit（EDITORIAL 正例去標籤重判），LESSONS `canonical-positive-example-fails-its-own-rules`。
- [ ] pending（延續，給 rewrite 排程）— ARTICLE-INBOX P2〈台灣災難醫療體系〉EVOLVE（issue #1752）。
- [ ] pending（延續，給 babel session）— babel 產線的連結閘門對 `](../` 直接拒收（LESSONS `relative-category-links-survive-link-check` 候選 (c)）。
- [ ] pending（延續，給 data-refresh-am 驗證）— 下次 build 後 `verify-internal-links.sh` 應印出 `(relative: ...)` 家族且數量接近零。

本 session 新 handoff：

- [ ] pending（給 REWRITE 排程或下一個整合多篇的 session，LESSONS `merged-source-translations-outlive-the-merge` 候選 (a)）— REWRITE Stage 5 整合多篇為一篇時，舊母稿的譯文一併 `git rm` ＋ 301 導到倖存者的對應譯文；候選 (b) `sync-translations-json.py` 改址時印一行「N 份譯文的來源已併入 X」進 refresh 報表。
- [ ] pending（給 babel session，1-file，資訊）— ko `People/lin-chi-wei-social-innovator.md` 16 條腳註今天由 fixer 收成格式合規，但標題欄放的是譯者塞進去的描述文、來源名只剩「人間福報專欄」這種泛稱；母稿腳註有正規標題，等 babel 對這篇重譯時會自然換掉，不用手修。
- [ ] pending（給下一班 maintainer-am 驗證）— push 後 `Python tests` 與 `Engineering contracts` 在 main 上應轉綠（`3d3533aef`）；若仍紅，看是不是 `paths` filter 讓它沒再被觸發（09-03 那條病）。

## Beat 5 — 反芻

今天做掉的那條交接跟昨天做掉的那條長得不一樣。昨天是帶指令與數字的，讀完直接貼；今天這條寫了判準（「留 sibling 同名、sha 較新的那份」），看起來也是純動作，動手才發現六組裡有兩組不符合判準的前提。判準假設「兩份都是譯文」，那兩組其實是母稿已經死掉的譯文，判準對它們無話可說。前三班往下傳的時候沒有人打開那六個檔看，我也差點沒有——如果 `originalTranslatedFrom` 那個欄位不在 frontmatter 第二行，今天大概就照判準留一份刪一份，把一篇 03-24 的舊譯文當成「較新的那份」留下來。交接傳得動判準，傳不動判準的前提；能看見前提的只有真的打開檔案那一刻。

第二件小事：pre-commit 失敗那次我用 grep 把輸出濾成只剩綠色，看到的是「✅ 沒有受守護的檔案」，其實那行來自另一段檢查。過濾工具輸出是為了讀得快，代價是失敗訊息跟成功訊息在濾網那端長得一樣。09-18 data-refresh 那班寫過「儀器對機器誠實、對人撒小謊」，今天是我自己在儀器跟眼睛之間又加了一層濾網。

🧬

---

_v1.0 | 2026-09-22 08:46 +0800_
_session twmd-maintainer-am — 3 PR merge ＋ main 兩條紅 workflow 修 ＋ en 六組同源雙檔收斂（6 刪 7 改名 13 條 301）＋ ko 林啟維腳註格式 heal ＋ LESSONS 一條_
_誕生原因：cron 08:30 排程；Stage 1 掃到 3 ready PR、1 fresh issue、main 兩條 workflow 紅、09-19 起傳了四輪的 en 雙檔交接_
_核心洞察：(1) 交接傳得動判準，傳不動判準的前提，六組雙檔裡兩組的前提（兩份都是譯文）不成立 (2) 母稿併掉時登記表改址而非退場，譯文會多活半年且每把尺都說沒事 (3) 過濾工具輸出讓失敗跟成功在濾網那端長得一樣_
_LESSONS-INBOX 候選：`merged-source-translations-outlive-the-merge`（已寫入，vc=1，structural）_

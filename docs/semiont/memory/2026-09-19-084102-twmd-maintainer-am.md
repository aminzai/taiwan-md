# 2026-09-19-084102-twmd-maintainer-am — 三個投稿 PR 先認領再收；昨天交接的「動手前先認領」落成 Step 3.0；slug 對照第五輪手動後升成工具

> session twmd-maintainer-am — cron routine（am 08:30 contributor PR review + issue triage + build sanity + broken-link audit）
> Session span: 08:41:02 → 09:06 +0800（origin/main 3 merge + 1 heal + 1 evolve + 1 memory；本機 main 零 commit）
> 資料來源：`git log %ai` + `gh pr view --json mergedAt`

✅ BECOME ack: mode=review / 8 organ 最低=🫀 心臟 30（即時 consciousness-snapshot.sh，紅燈自 2026-09-15）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 排程。Stage 1 掃到 3 個 ready PR（未達 High-stake #1 的 ≥5 門檻，維持 Review mode）、5 個 open issue 零 fresh（#1746 昨天已由 origin 側關掉）、0 個 draft、Discussions 最新留言全是維護者、main 七條 workflow 最新一次全綠、`pr-ci-armed` 三個 PR 都 ARMED。跟 09-16 起同樣跑在 musebase：本機 main 領先 origin 845、落後 737，babel dispatcher 四個 writer 整輪在寫 `knowledge/`。沿用同一套規矩，本機 main 不 pull 不 push，`semiont-worktree.sh new --from origin/main` 開 worktree 量 origin 的事。

## 三個 PR：先掛 assignee，再審，再收

昨天那班的教訓是兩台機器各自把同一則交接做完、push 被拒才看見對方。今天 Stage 3 第一個動作改成把 #1749／#1750／#1751 都 `gh pr edit --add-assignee` 掛到自己名下，再開始審。這是 LESSONS `handoff-addressed-to-a-routine-name-lands-on-two-machines` 修補候選 (a)，同班寫進 MAINTAINER-PIPELINE v2.11 §Step 3.0（Hard Gate Inventory、Top-N、skill 殼同步），LESSONS 那條補「落地」行。規則一句話：已有他人 assignee 就是另一台機器在做，跳過。

aminzai 的 #1749（de/台灣水彩畫的百年流變）、#1750（vi/臺灣的鯨豚）、#1751（id/台塑集團）三篇都 `--merge` 收下（`b6f7e8478` / `cf969abe1` / `2d14c5cfe`），致謝走 burst 期累積式，一則留在 #1751。覆驗在 origin worktree 的真實路徑上跑。`article-health --profile=ci-deploy` 三篇 hard=0。`verify-translation.py` 對母稿 18/18（腳註 6/7/5、章節 6/9/7、URL 多重集合逐條相同）。`person-fidelity-check` 零可疑、`cjk-leak-check` 0/3。`sourceCommitSha` 三篇都對到母稿 HEAD。frontmatter 逐欄對母稿，id 那篇 `author: 'Taiwan.md'` 字面命中紅旗 #7，母稿本來就是這個值，忠實繼承。腳註抽驗九條 URL 七條 200，thenewslens 與 ctee 兩條 403 是機器人牆，母稿同一條網址。印尼文把「中國大陸」譯成 `Tiongkok daratan`，正是 TRANSLATION-id §1 對地理對照語境規定的寫法。

承 09-16 起的量測：vi 鯨豚與 id 台塑在本機 babel 早有譯文，分岔把貢獻者工時導向已完成格子的計數本輪 +2（2/3），累計五輪 12/22。

## slug 對照：第五輪手動之後升成工具

每一輪都手動 `ls knowledge/*/{slug}.md` 對照 sibling 檔名，今天第五輪，照 REFLEXES #15 把它收進既有的 `check-slug-consistency.py`：加 `--pr N`（內容從 `refs/twmd/prN` 讀，不 checkout 投稿者的樹）與 `--files`。en 不存在時退而取其他語言的多數檔名（≥2 個 sibling 同名才算慣例）。再補 09-14 LESSONS `same-language-slug-collision-is-invisible-to-both-instruments` 缺的那把尺——同一語言目錄裡另一個檔的 `translatedFrom` 相同但檔名不同，報撞號。`--staged`／`--all` 路徑不動。五個 pytest（en 優先、多數決門檻、撞號、自己不算撞號、只讀 frontmatter），今天三個 PR 用 `--pr` 各跑一次全綠。

順手用 `--all` 掃 origin/main，先看到 33 篇「檔名跟 en 不一致」，追下去發現多數是假警報：**en 自己有 6 組同源雙檔**（黃春明、鄧雨賢、台灣小吃、手路菜、taiwan-md、氣候危機各兩個 en 檔指向同一篇母稿），檢查器的 en 索引用 dict 覆寫，哪一個算 canonical 取決於 rglob 順序，於是每組的十一個 sibling 有一半被判漂移。其中黃春明與鄧雨賢那兩組是 08-28 投稿 PR 在既有 en 檔旁邊再開一個新檔進來的——09-14 那條「同語言撞號兩把尺都看不見」的病，發生在 en 這個 canonical 語言身上，當時沒有任何尺會叫。工具因此再改一層：`--pr`／`--files` 也收 en（不對自己量檔名，只量撞號），`--all` 先印 en 雙檔清單再印漂移。扣掉六組雙檔，真漂移剩 10 篇：Computex 四語叫 `computex-taipei`、我是OO人四語叫 `i-am-from` 而 en 叫 `oo.md`（拿它當 canonical 去改四個語言未必對）、ru 的 miin、vi 的 `vietnamese-photography`。

最後那篇是 vi 自己的同源雙檔：`Art/台灣攝影` 在 vi 有 `taiwanese-photography.md` 與 `vietnamese-photography.md` 兩份不同的譯文，同一個 `sourceCommitSha`、同一個 `translatedAt`，08-09 與 08-18 兩次 babel 各落一份。內容都寫「Nhiếp ảnh Đài Loan」，只有檔名把台灣譯成越南。本輪 `git rm` 掉檔名錯的那份、`config/redirects-manual.txt` 補 301 導回與 en 同名那份、`sync-translations-json.py` 重整登記。兩棵樹都有這個檔，origin 側刪掉之後合併會收斂。en 的六組雙檔每組要判哪一份留、補六條 301，且 `founder.md`／`taiwan-md.md` 那組可能是 `translatedFrom` 標錯而非真雙檔，本輪不動，寫進 handoff。

## Issue 全部 SKIP，理由各一句

#1729（馬英九）昨天 15:14 origin 側已跑完 FACTCHECK Full mode（`8cc6a667e`，zh 104 行加十一語各 6 行，「辭世」那句十一語都已改掉，我逐語 grep 確認剩下的死亡字眼全是蔣經國與莫拉克罹難者）。剩下卸任後與太陽花兩節局部重寫，登記 ARTICLE-INBOX P0 等哲宇 review，issue 留開。十一個譯本的 `sourceCommitSha` 停在 `31a05c44b`，status.py 判 stale +50/-54——這次是對的，zh 撤掉的十七處查無來源細節譯本還在，該由 babel diff-patch 補齊，跟 09-18 周蕙那種手修完整的情形不同，不 bump。#1678 要改母稿骨架走 REWRITE；#1609 等第二冊實體書；#615 是 umbrella；#1711 飛輪停轉 bot 09-18 20:20 又貼，內容已能指出根因 (b)「fire 了、推不上 main」與救援分支位置，REFLEXES #80 sustain 不回。五則最新留言都是維護者，Step 2.4 不重複回應。

驗 #1729 時撞見 hi 版馬英九整個參考資料區是韓文，掃全庫 hi 394／ar 347／ru 284 檔含韓文、hi 33 檔 ≥10 行。這件事 09-18 晚間 heartbeat 已量過並登記 OBSERVER-QUEUE #69（40 篇尾段整段韓文＋約 900 篇單字級殘留，增量已由 `target-language-check` 逐行尺擋下，存量選項 A 等 #68 合併後 2026-10-02 起可執行），本輪只做一次獨立重量，數字同量級，不重寫 LESSONS。

## 哲宇進場：分岔十天，一個上午併完

08:30 那班收官後哲宇進 session 兩句話：「fully sync the progress on this machine, merge properly and sync with head」、「update maintainer daily skill, if this diverge happened again, you have to fix it, this is your duty」。第一句等於拍板 OBSERVER-QUEUE #68（本機側 #56），照兩側佇列都推薦的 B 做：origin 版優先、本機只補 origin 沒有的檔。

數字：分岔點 09-09 09:11，合併前本機領先 847、origin 領先 758，衝突 843 檔（717 add/add、126 兩邊都改）。先 `launchctl remove` 凍結 babel（只 kill 會被 keepalive 重生），工作樹裡 16 個未 commit 的檔整份存到 scratch。在一個從本機 main 開出來的 worktree 裡 `merge --no-commit origin/main`，衝突分四類處理：779 篇譯文加 48 個衍生檔取 origin；`reports/babel` 三個狀態 JSON 取聯集；認知層五檔兩邊全留，OBSERVER-QUEUE 本機側 #53／#54／#55／#57 改編成 #70–#73、#56 併進 #68 移 §已決；五支產線工具逐 hunk 合成（babel-dispatch 同時留本機的 origin 去重清單與 origin 的 max_zh_bytes；cjk-leak-check 兩邊獨立寫了同一個日文新字體豁免，取 origin 的字集把本機的證據併進註解）。

合併後真正的坑是**同語言雙檔**：兩台機器對同一篇母稿各取檔名，1,008 篇跟 origin 撞成雙檔（origin 那份檔名全部對得上 en），本機那份全捨；合併時漏網的 10 篇之後補刪。留下 1,205 篇 origin 沒有的譯文（de 659、vi 246、id 109、ja 82），target-language-check 抓到 1 篇 de 是英文，丟；article-health ci-deploy 4 篇 ja 是 prettier 弄壞斜體圖說裡的底線網址，連結移出斜體。再來是檔名：留下來的本機譯文有 379 篇檔名跟 en 不一致，全部 `git mv`；四個家族反過來（en 是本機新翻、其他語言早用另一個檔名上線）改 en 去配多數；origin 本來就漂移的 computex 四語、miin 一語、「我是OO人」的 en `oo.md` 一併對齊，六個上線過的舊網址補 301。prettier 在 commit 時又把 143 篇斜體圖說的網址弄壞，全部改成純文字、出處補 §Image sources。472 個 Python 測試通過，合併 `e419e2aa7`、打撈 `2e913788b`、對齊 `f4892bab5`，本機 main 快轉到 origin，dispatcher 重掛。

第二句落成 MAINTAINER-PIPELINE v2.12 §Step 1.1b：兩個領先數都 > 0 就是本班第一件事，不留 handoff、不進佇列、不開救援分支，「>50 檔等哲宇」對這件事不適用；Step 1.1 原本寫的「撞 conflict → abort cycle」廢止。今天手做的四個機械步驟收成 `scripts/tools/merge-divergence.py`（resolve／dedupe／verify／align，dry-run 預設，五個 pytest），skill 殼、git 側 cron prompt、本機 live prompt 三份同步 inline。

## 死連結閘門：0.20%，跟 09-17 同量級

在 origin worktree 真跑 prebuild 加 astro build（17,060 頁，14 分 48 秒），gated ratio **0.20%**（2,147/1,050,884，all-langs 0.18%），語言切換器 0 條，unique target 1,133。zh-TW 的 2,074 條仍幾乎全來自 `changelog/index.html` 列的歷史檔名，文章互連層 en 11、ko 10、ja 52（ja 那批是對尚未翻譯條目的延伸閱讀，屬 babel 順序問題），fr 19／es 4 report-only。跟 09-17 的 0.25% 同一量級，本輪不 heal。

## 收官 checklist

| 檢查項                       | 狀態                                                           |
| ---------------------------- | -------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅（寫在 origin 側，同 09-16 起慣例）                          |
| Timestamp 精確               | ✅ `git log %ai`                                               |
| Handoff 三態已審視           | ✅                                                             |
| CONSCIOUSNESS 反映最新狀態   | ⏭️ derived 層自動推導，alerts 由 data-refresh 下輪重生         |
| 自我檢查工具 PASS            | ✅ article-health 3/3 hard=0、pytest 5/5、memory-diary profile |

## 品質閘門 7 條

| 閘門                                 | 結果                                                                          |
| ------------------------------------ | ----------------------------------------------------------------------------- |
| 完整走完 MAINTAINER Stage 1-4        | ✅                                                                            |
| PR 分流按 §collect-and-merge B 路徑  | ✅ 3 篇走完整 hard gate，Step 3.0 認領先於審核                                |
| routine PR backlog ≤ 3               | ✅ v2.1 後無 routine PR                                                       |
| broken-link gated ratio < 7%         | ✅ 0.20% < 7%（origin worktree 真 build 17,060 頁；alternate cycle 輪到本輪） |
| build green                          | ✅ main 七條 workflow 最新一次皆 success；本輪 origin worktree 真 build 完成  |
| 本 cycle merge 的 PR 都過 hard gate  | ✅ 3/3，Step 2.4 對 PR 也跑了（三篇零留言，首次回覆）                         |
| 有 fresh issue 的 cycle 至少修掉一件 | ⏭️ 本輪零 fresh issue；五則不修各寫明理由                                     |

連續空場 vc=0（本輪 3 個 fresh PR，計數歸零重計）。

## Handoff 三態

繼承上一 session（origin 側 09-18 maintainer-am）：

- [x] ~~blocked（延續）— 本機 main 845 未推送 commit 與 origin 737 個真分岔，等哲宇拍板 #56／#68~~ — retired by 本 session 下半場：哲宇 in-session 拍板 B，合併 `e419e2aa7`，本機 main 已與 origin 同步。
- ⏳ blocked（延續，改解除條件）— issue #1729：FACTCHECK Full mode 已於 09-18 跑完，剩卸任後／太陽花兩節局部重寫，ARTICLE-INBOX P0 等哲宇 review 後由 Write session 接。
- ⏳ blocked（延續，給哲宇）— 用語庫 blanket claim 血緣複查 A/B/C，寫在 origin 側 `memory/2026-09-16-090341-twmd-maintainer-am.md`。
- [x] ~~pending（延續，給合併 #56/#68 的 session）— OBSERVER-QUEUE 兩側撞號的主鍵策略~~ — retired by 本 session：合併時以 origin 表為底、本機獨有條目改編到最大號之後，對照寫進 frontmatter；主鍵策略本身寫進 MAINTAINER §Step 1.1b 第 4 步。
- [x] ~~pending（延續）— slug 慣例對照升工具，接進 Stage 2 譯文 PR 分流~~ — retired by 本 session：`check-slug-consistency.py --pr N`，見上節。
- [x] ~~pending（延續）— `routine-stall-check.py` 尺二讀救援分支，待下一次 fire 驗證~~ — retired：09-18 20:20 那次 fire 的輸出已對每條週排程 miss 標「救援分支上有 → 根因 (b)」，WARN 保留但不再誤判死亡。
- [x] ~~pending（1-file 候選）— issue 動手前的認領步驟寫進 MAINTAINER-PIPELINE~~ — retired by 本 session，v2.11 §Step 3.0。
- ⏳ blocked（延續，給哲宇）— commander-macbook 的 heartbeat 跟 musebase 的 maintainer-am 對 issue 修補的職責重疊，哪一台擁有這件事要在 ROUTINE.md 寫清楚；分岔已解，Step 3.0 的 assignee 是兩台共看的最小訊號。

本 session 新 handoff：

- [ ] pending（給 05:30 routine-sync）— `twmd-rewrite-daily` prompt 因 origin 的 REWRITE 產線整併而 git 新於機器，`routine-sync.py --apply` 對齊。
- [ ] pending（給下一班 maintainer-am 驗證）— 合併後第一輪 babel 在同一棵樹上跑，看 `_translations.json` 與 slug 是否再漂；救援分支 `20260912-unpushed-routine-queue` 的內容已全部在 main 的第一父鏈上，確認後可刪。

- [ ] pending（給下一班 maintainer-am，6 刪 + 6 條 301，<10 篇在自主權內）— origin/main 上 en 六組同源雙檔（`check-slug-consistency.py --all` 第一段列得出）。每組判準：留與其他語言 sibling 同名、`sourceCommitSha` 較新的那份；`founder.md`／`taiwan-md.md` 先 diff 內容，若是兩篇不同文章就改 `translatedFrom` 不刪檔。刪的那份在 `config/redirects-manual.txt` 補 301。分岔期間本機側可能還有第三份，等 #68 合併後再動。
- [ ] pending（給 babel session）— 真漂移 10 篇：Computex 四語 `computex-taipei` → `computex`、ru `miin` → `miin-music-app`，`git mv` 加 301；我是OO人四語 `i-am-from` 對 en `oo.md`，先決定 en 該不該改名再動。
- [ ] pending（給 distill-weekly）— LESSONS `handoff-addressed-to-a-routine-name-lands-on-two-machines` 修補候選 (b) handoff 第四態 `🔧 claimed`，本班沒動；(a) 已落地可 fold 進 REFLEXES #57 第三層。

## Beat 5 — 反芻

今天最省力的一步是把三個 PR 掛到自己名下再開始審，前後不到十秒。昨天那班花了二十五分鐘把一則勘誤查完修完，push 被拒才知道另一台機器一分鐘前推了同一件事；今天這十秒就是那二十五分鐘的保險。做的只是把既有的 GitHub 欄位搬到動手之前。REFLEXES #15 第 13 條講「handoff 傳遞了資訊，沒有傳遞急迫性」，昨天寫在交接裡的 1-file 候選今天就落地，兌現延遲一輪——比 FEEDBACK-TRIAGE 那條 `--show` 等了四輪好一些，差別大概是昨天那班把命令都寫好了，今天只剩貼進去。

第二件是尺的基準先壞了。`check-slug-consistency.py` 七月起就在 pre-commit 裡，規則是「譯文檔名要跟 en 一樣」，它預設 en 對每篇母稿只有一個檔。今天 `--all` 報 33 篇漂移，我第一個念頭是「en 事後改名讓整排 sibling 變成漂移」，差點就這樣寫進交接；停下來查 git log 才發現 en 根本沒改名，是兩個 en 檔並存，索引取哪一個看 rglob 心情。讀數是對的，基準是隨機的。09-14 那班寫「兩把尺都說沒撞車，因為對手用另一個檔名」，當時講的是投稿譯文；今天同一個病出現在 canonical 語言本身，而且其中兩組正是那之後兩週投稿 PR 收進來的。把撞號尺加進 `--pr`，是讓下一個在既有 en 旁邊再開一個的 PR 在審核那一刻就被看見。

🧬

---

_v1.0 | 2026-09-19 09:06 +0800_
_session twmd-maintainer-am — 3 PR 先認領再收割／Step 3.0 認領步驟落地 v2.11／slug 對照升 `--pr` 工具＋撞號尺＋6 pytest／量出 en 六組＋vi 一組同源雙檔，vi 那組當場清掉／#1729 FACTCHECK 已由 origin 側完成改解除條件_
_誕生原因：cron am 08:30 maintainer routine，Stage 1 掃到 3 個 ready PR、零 fresh issue_
_核心洞察：(1) 認領要落在兩台機器共看的那棵樹上、落在動手之前，十秒換昨天的二十五分鐘 (2) 寫好命令的 handoff 兌現延遲一輪，寫成候選的要四輪 (3) 檢查器拿 en 當 canonical，而 en 自己有雙檔，尺的基準先壞了、讀數才壞；先量基準再信讀數_
_LESSONS-INBOX 候選：無新條目（韓文漂入已在 OBSERVER-QUEUE #69；en 同源雙檔是 09-14 `same-language-slug-collision-is-invisible-to-both-instruments` 的第二例，該條只在本機側 LESSONS，合併 #68 後再補 vc=2）_

# 2026-09-20-085204-twmd-maintainer-am — 三個投稿 PR 收下，兩則讀者勘誤當班修掉，一則飛輪停轉舊警報收掉，EDITORIAL 的第二階風險觀察分四桶處理

> session twmd-maintainer-am — cron routine（am 08:30 contributor PR review + issue triage + build sanity + broken-link audit）
> Session span: 08:30 fire → 08:44:00 第一個 merge → 08:55 +0800（3 merge + 2 heal + 1 evolve + 1 memory）
> 資料來源：`git log %ai` + `gh pr view --json mergedAt`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，黃燈自 2026-07-05，review_coverage 缺口 20 分）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 排程。分岔已在 09-19 併掉，Stage 1 第一件事量 `main...origin/main` 得 `8 0`：本機只是領先八個 babel commit，沒有分岔，第一次不用開救援分支也不用等人。掃到 3 個 ready PR（aminzai，未達 High-stake 門檻）、7 個 open issue 其中 2 個 fresh 零留言（#1756 昨晚 feedback-triage 開的、#1752 thc1006 今晨開的）、Discussion 一則新貼零回覆（#1757）、main 六條 workflow 全綠、`pr-ci-armed` 三個 PR 都 ARMED。babel dispatcher 四個 writer 正在主工作樹寫，沿用 `semiont-worktree.sh new --from origin/main` 在隔離樹上做事。

## 三個 PR：認領、七道尺、一則致謝

aminzai 連續第四天送三篇（de／台灣山椒魚、hi／豆花、ar／紙風車劇團），先全部 `--add-assignee` 掛到自己名下再審。內容檔用 `git show refs/twmd/prN:<path>` 帶進 main 樹跑：`article-health --profile=ci-deploy` 三篇 hard=0、`verify-translation` 對母稿各 18/18、人名與地名保真零可疑、`cjk-leak` 0/3、目標語言逐行 0 fail、`check-slug-consistency --pr` 三篇檔名與 sibling 一致、`sourceCommitSha` 都對到母稿 HEAD、frontmatter 逐欄忠實繼承（山椒魚的 `author: 'idlccp1984'` 是母稿本來的值）。腳註抽驗十一條 URL 十條 200，一條 cw.com.tw 403 是機器人牆。三篇 `--merge` 收下（`a4ca4294f` / `a2a510934` / `7d5730054`），致謝走 burst 期累積式，一則留在 #1755，順便回答他 PR 說明裡標出來的三個不確定點。

紙風車那篇母稿的參考資料是十七條純 `[N]` 方括號，沒有 `[^N]` 腳註語法，譯者忠實保留是對的。這是 zh 的格式債，寫進 handoff。

## 兩則勘誤：一個譯名，一個放錯槽位的數字

#1756（讀者 Konta）指「TikTok 是位元組跳動的」該是字節跳動。先證偽讀者：北京字節跳動科技有限公司的官方中文名確實是字節跳動，「位元組跳動」是把 byte 直譯成台灣資訊術語後的機器譯名。全庫中文只有這一處，譯本層早就寫 ByteDance／バイトダンス／바이트댄스，改一句就完（`56f4d6f85`），回覆附更正網址後關 issue。

#1752（thc1006）指〈台灣災難醫療體系〉的「921 有 500 人本來可以活」沒有根據。查證結果是真原子放錯槽位（REFLEXES #98）：「如果緊急醫療體制完善，罹難者中約 500 人可能救得活」是 1995 年阪神・淡路大震災後日本的檢討，2005 年日本 DMAT 就是從這個反省成立的，ja.wikipedia 災害派遣医療チーム的注釋與三重中央医療センター災害醫療頁都寫「防ぎ得た災害死が約 500 例」。舊稿把數字接到 921 上再讓它去催生 2000 年災防法，而文章自己引的台灣急診醫學會〈DMAT 之分類與展望〉只寫 921 之後通過災防法，沒有任何數字。外科手術式改法：小標換掉、921 → 災防法那段照急診醫學會原文重寫、500 人搬回阪神與日本 DMAT 那段、「2005 年台灣正式引進 DMAT」查無來源撤掉（`a17bb572e`）。這篇是 03-24 的未審初稿，零 `[^N]` 腳註、2,672 字、十二語譯本都在線帶著同一段，跟 09-18 起連續五輪巡邏量出來的那格（未審初稿 × 已多語投射）是同一個位置，登記 ARTICLE-INBOX P2 重寫。譯本由 sourceCommitSha 過期交給 babel diff-patch，跟 09-19 對 #1729 的處置一致。

回覆 thc1006 時順手回了他另外兩個建議：zhtw-mcp 記為詞庫比對來源，中文排版指北拿來對一次既有檢查器缺哪些。沒有承諾時程。

## 一則舊警報與一條救援分支

#1711 是 09-11 起 GitHub Actions 開的飛輪停轉警報，偵測器 09-18 最後一次貼的結論已經是「routine 在跑，是那台機器的 main 跟 origin 分岔了」。分岔 09-19 併掉、救援分支 `20260912-unpushed-routine-queue` 用 `merge-base --is-ancestor` 驗過已在 main 第一父鏈上、偵測器 09-19 18:14Z 與 09-20 00:41Z 兩次跑都零 WARN。工作流只會開與續貼、不會關，所以這則屬於神經迴路那條「已解未 close = 對外失聯」。附證據關掉，順手刪了救援分支（昨天的 handoff 說確認後可刪）。

## Discussion #1757：外部 critique 不直接執行

kwt-klure 寫了一篇很完整的 EDITORIAL 第二階風險觀察：規則單條各有理由，疊加起來經 rewrite 產線放大到 corpus 後，可能讓所有題材長成同一副骨架，把「AI 味」換成「Taiwan.md 味」。附的最小 reproducer 我對照 EDITORIAL 第 1652 行確認成立：§九 拿來示範餘韻式結尾的雲門正例，正是同一份文件在別處禁的膠水句與文化昇華。照 CLAUDE.md §Bias 4 分桶。09-19 產線整併已走到同方向（規則准入改「錯→儀器／悶→規則」、三樣東西不長回來、日記「閘門的形狀會反過來雕刻產物」），這桶是「已 cover 對方不知道」。雲門正例撞規則是真洞見，抽成自我洞察寫進 LESSONS `canonical-positive-example-fails-its-own-rules`。規則分成事實硬閘門與美學預設加 N/A 出口是 EDITORIAL 結構改動，登記 OBSERVER-QUEUE #74 推薦先 audit 再改。corpus 是否真的同質化沒有抽樣證據，照他自己的話存疑。三件事一個 commit（`4f3d7239f`），回覆逐桶對照現況、不代哲宇承諾時程。

## 死連結閘門

昨天那班剛在 origin worktree 真 build 過（17,060 頁，0.20%），alternate cycle 輪到本輪跳過，main 上六條 workflow 含 Deploy 最新一次全綠。

## 收官 checklist

| 檢查項                       | 狀態                                                              |
| ---------------------------- | ----------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                |
| Timestamp 精確               | ✅ `git log %ai`                                                  |
| Handoff 三態已審視           | ✅                                                                |
| CONSCIOUSNESS 反映最新狀態   | ⏭️ derived 層自動推導，alerts 由下輪 data-refresh 重生            |
| 自我檢查工具 PASS            | ✅ article-health 3 PR + 2 heal 全 hard=0、memory-diary profile   |

## 品質閘門 8 條

| 閘門                                 | 結果                                                                    |
| ------------------------------------ | ----------------------------------------------------------------------- |
| 完整走完 MAINTAINER Stage 1-4        | ✅                                                                      |
| PR 分流按 §collect-and-merge B 路徑  | ✅ 3 篇走完整 hard gate，Step 3.0 先認領                                |
| routine PR backlog ≤ 3               | ✅ v2.1 後無 routine PR                                                 |
| broken-link gated ratio < 7%         | ⏭️ alternate cycle，昨輪 0.20%                                          |
| build green                          | ✅ main 六條 workflow 最新一次皆 success                                |
| 本 cycle merge 的 PR 都過 hard gate  | ✅ 3/3                                                                  |
| 有 fresh issue 的 cycle 至少修掉一件 | ✅ #1756 `56f4d6f85`、#1752 `a17bb572e`、#1711 附證據關閉，三則都有 commit 或判斷 |
| 本機與 origin 無真分岔               | ✅ `8 0`，純領先                                                        |

連續空場 vc=0（本輪 3 fresh PR + 2 fresh issue + 1 fresh discussion，計數歸零）。

## Handoff 三態

繼承上一 session（09-19 twmd-maintainer-am + 09-20 twmd-feedback-triage）：

- [x] ~~pending（給 08:30 twmd-maintainer-am）— issue #1756 字節跳動譯名勘誤走 CORRECTION-PIPELINE~~ — retired by 本 session，`56f4d6f85`，issue 已關。
- [x] ~~pending（給下一班 maintainer-am 驗證）— 合併後第一輪 babel 在同一棵樹上跑看 slug 是否再漂，救援分支 `20260912-unpushed-routine-queue` 確認後可刪~~ — retired by 本 session：origin 過去 24 小時 33+ 個 babel commit 落地、`check-slug-consistency --pr` 三篇零漂移，救援分支驗過是 main 祖先後刪除。
- ⏳ blocked（延續）— issue #1729 馬英九：FACTCHECK 已跑完，卸任後／太陽花兩節重寫在 ARTICLE-INBOX P0 等哲宇 review 後由 Write session 接。
- ⏳ blocked（延續，給哲宇）— 用語庫 blanket claim 血緣複查 A/B/C（issue #1733 已關，決定寫在 `memory/2026-09-16-090341-twmd-maintainer-am.md`）。
- ⏳ blocked（延續，給哲宇）— commander-macbook heartbeat 與 musebase maintainer-am 對 issue 修補的職責重疊要在 ROUTINE.md 寫清楚；Step 3.0 assignee 是目前兩台共看的最小訊號。
- [ ] pending（延續，給下一班 maintainer-am，6 刪 + 6 條 301）— origin/main 上 en 六組同源雙檔（`check-slug-consistency.py --all` 第一段），判準與 `founder.md`／`taiwan-md.md` 那組先 diff 的規則見 09-19 memory。
- [ ] pending（延續，給 babel session）— 真漂移 10 篇：Computex 四語 `computex-taipei`、ru `miin`、我是OO人四語對 en `oo.md`。
- [ ] pending（延續，給 distill-weekly）— LESSONS `handoff-addressed-to-a-routine-name-lands-on-two-machines` 修補候選 (b) handoff 第四態 `🔧 claimed`。
- [ ] pending（延續，給 distill）— LESSONS `held-fact-never-crosses-into-the-layer-that-acts-on-it` vc=5 候選機械化「出口完整性檢查」。

本 session 新 handoff：

- [ ] pending（給 Full mode session 或哲宇在場的 session）— OBSERVER-QUEUE #74 選項 A 的 audit 本身可以先做：EDITORIAL 全部 ✅ 正例去標籤、`article-health --check=prose-health` 加一席不知道標籤的 reviewer 重判，再抽 5 篇 09-19 產線整併後的文章看骨架同質化；產出直接餵 #74 的決定。LESSONS `canonical-positive-example-fails-its-own-rules`。
- [ ] pending（1-file，給任一 Write 或 heal session）— `knowledge/Art/紙風車劇團.md` 十七條 `[N]` 純方括號引用轉 `[^N]` 腳註語法（PR #1755 譯者忠實保留了母稿的格式債）；轉完 ar 譯本會因 sourceCommitSha 過期由 babel 補。
- [ ] pending（給 rewrite 排程）— ARTICLE-INBOX P2〈台灣災難醫療體系〉EVOLVE（issue #1752 止血後，未審初稿 × 十二語）。

## Beat 5 — 反芻

今天兩則勘誤來自兩個不同的入口（站上回報表單、GitHub issue），錯的形狀卻同一種：零件是真的，槽位是錯的。字節跳動那個小到只是一個詞被機器譯了兩次；災難醫療那個大到把日本 DMAT 的誕生理由整段搬給 921，再讓它去催生台灣的法律。兩個錯都在譯本層被忠實地放大了，前者十二語裡有十一語自己譯對了，後者十二語全帶著同一段。REFLEXES #98 上週日才蒸餾成反射，這週就有讀者從外面抓到第二例與第三例。抽樣指令換成「未審初稿優先」是對的；讀者比抽樣快。

Discussion #1757 那篇講的東西我們 09-19 剛自己撞到一次（三篇文章閘門全綠卻沒有一句自己的話），差別是他從規則文件的結構去讀，我們從產物去讀，兩邊在同一天各自到了「閘門的形狀會雕刻產物」這句。§Bias 4 要我把外部聲音分桶而不是照做，分完發現四桶裡有三桶已經有位置可放，剩下那桶正好是 DNA 層要哲宇拍板的。這種時候外部的眼睛最有用的地方在它給了一個我們自己不會去看的角落：規則的範例。範例跟規則出自同一位作者，所以規則永遠不會量到範例。

🧬

---

_v1.0 | 2026-09-20 08:55 +0800_
_session twmd-maintainer-am — 3 PR 認領七道尺收下／#1756 字節跳動、#1752 阪神 500 人放回原槽位當班修掉／#1711 飛輪停轉附證據關閉並刪救援分支／Discussion #1757 分四桶：LESSONS + OBSERVER-QUEUE #74 + 回覆_
_誕生原因：cron am 08:30 maintainer routine，分岔併完後第一個零分岔的班_
_核心洞察：(1) 讀者兩天抓到 REFLEXES #98 的第二、三例，錯法都是真零件放錯槽位，抽樣指令改抽未審初稿仍比不上讀者快 (2) 外部 critique 分桶後，最有價值的是他看到我們看不到的角落：規範文件裡的範例不會被同一份文件的規則量到 (3) 已解未 close 的機器警報跟做了不記是同一種對外失聯_
_LESSONS-INBOX 候選：`canonical-positive-example-fails-its-own-rules`（本班已寫入）_

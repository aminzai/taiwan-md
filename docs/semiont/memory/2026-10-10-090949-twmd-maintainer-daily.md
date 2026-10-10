---
title: '2026-10-10-090949-twmd-maintainer-daily'
description: '七篇投稿 PR 的四道關鍵閘門從來沒跑過、紅燈的歸因擋住了這個問題；逐篇本機驗完合併；大小寫測試在 macOS 永遠紅；21 天的回收工作改成自己認窗口'
type: 'session-log'
status: 'log'
apoptosis: 'never'
current_version: 'v1.0'
last_updated: 2026-10-10
---

# 2026-10-10-090949-twmd-maintainer-daily — 一個紅燈同時遮住它自己的原因和它下游四道沒跑過的閘門

> session twmd-maintainer-daily — cron 排程（am 08:30）
> Session span: 08:30 → 09:16 +0800（約 46 分鐘，4 commits + 7 PR merged）
> 資料來源：`git log %ai` + `gh pr/issue/run/api` + `scripts/tools/{consciousness-snapshot,wake-context,ci-main-health,npm-audit-sweep,article-health,verify_internal_links,observer-queue-lint,git-prune-when-quiet,lib/check-parallel-actor,lib/verify-commit-scope}` + 獨立 worktree 四道閘門 + case-sensitive APFS 磁碟映像 + 正式站 curl

✅ BECOME ack: mode=review→**FULL**（high-stake #1：9 ready PR ≥ 5）/ 8 organ 最低=🛡️60 免疫（即時 `consciousness-snapshot.sh`）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 maintainer 班。`gh pr list` 回九個 ready PR（0 draft），命中 BECOME §Step 0 high-stake #1，review mode 當場升 Full。`wake-context.py` 落檔 264,227 bytes 分頁讀到末行 `wake:END` sentinel，11 段 selftest 全綠。

刻意沒全載的兩份：`ARTICLE-INBOX`（2,695 行）與 `SPORE-INBOX`。它們是寫文與孢子的 intake buffer，對 PR triage 不載重；`inbox-signal.sh` 的 count 已在 groundtruth。LESSONS 讀的是未消化標題不是全文。寫在這裡是因為「評估後決定不做」要寫明理由。

分岔檢查開場 `0 0`（Stage 1.1b 不觸發）。

## 本班最重要的一件事：前兩班的診斷對了一半，而錯的那一半更重要

前兩班（10-08、10-09）把七個投稿 PR 的 `contracts` 紅燈診斷成「繼承 main 上 `harvest/ui` 的 tailwind 公告紅，等 OBSERVER-QUEUE #94」。那個診斷有證據、有說服力、方向也對——**確實有一個與投稿者無關的紅**。10-09 那班還逐篇查過 check rollup，寫下「九個 PR 全部 ARMED（CI 真的跑過，不是零檢查）」。

那句話在 check-run 這一層是真的。往下看一層就不是。

逐 PR 調 `actions/runs/<id>/jobs` 讀 `.steps[].conclusion`：

```
success  npm ci --ignore-scripts --no-audit
failure  npm audit --audit-level=high        ← 倉庫根目錄那道，不是 harvest/ui
skipped  npm run test:contracts
skipped  python -m pytest tests -q
skipped  npm run prebuild:fork-graph
skipped  npm run check:types
skipped  harvest/ui / harvest/backend / workers/mcp
```

紅在**第五步**，而 `harvest/ui` 排第六步，從頭到尾沒輪到它跑。第五步那個紅是 10-08 已經被 `e6fcfa55c` 修掉的那一批公告。

所以真正的後果不是「等 #94」，是**四道真正會檢查投稿者程式碼的閘門，在這八個 PR 上從來沒有跑過一次**——不是綠、不是紅，是 `skipped`，而這件事四天沒有人知道。`gh pr checks` 只給 job 層結論，`pr-ci-armed.sh` 量的是「head sha 上有沒有 check-run」，兩者都答不出「哪些檢查其實沒跑過」。

而讓這個問題四天沒被問的，正是那個聽起來正確的外部歸因。歸屬在庫外不代表後果在庫外，也不代表那是唯一的後果。

## 所以不等 CI，自己量

開一個站在 `origin/main` 的獨立 worktree（不 checkout 投稿者分支——站在別人的樹上讀我們的檢查器，量到的是我們上週的樣子），先在乾淨 main 上跑四道閘門當基準線，再逐篇合併進去量：

|                                               | pytest       | test:contracts | fork-graph | astro check |
| --------------------------------------------- | ------------ | -------------- | ---------- | ----------- |
| 乾淨 main（基準）                             | 727 passed   | 全過           | exit 0     | 0 errors    |
| #1791 / #1793 / #1794 / #1795 / #1799 / #1800 | 全過         | 全過           | exit 0     | —           |
| #1797                                         | **1 failed** | 全過           | exit 0     | —           |
| 七篇全部合併                                  | 733 passed   | 全過           | exit 0     | 0 errors    |

那一次量就抓到前兩班看不到的東西。

## #1797 那個 failed 是真的，而它不是投稿者的 bug

紅的是投稿者自己新增的 `test_ambiguous_case_is_not_guessed`。它要「兩個只差大小寫的真實路徑同時存在」，然後確認檢查器不替作者猜。而這個前提在 macOS 上建立不起來：APFS 不分大小寫，第二個 `write_text` 蓋掉第一個，檢查器只看到一個候選、照常建議，這題就紅。

實測三態才下結論：本機建兩個檔只剩一個 → `hdiutil` 開一個 case-sensitive APFS 磁碟映像建得出兩個 → 把 `TMPDIR` 指到後者，整題 5 passed。

這跟 §神經迴路「本機檔案系統不分大小寫，把 CI 會擋的錯誤藏起來」是同一個地板差異，**方向相反**：那條講假的綠，這條是假的紅。假的紅的代價是下一個照流程跑 `pytest tests` 的 macOS 班次會去修一個不存在的 bug，或者乾脆把那個斷言刪掉——而斷言是對的。

修法 `215ba089f`：現場探一次這個資料夾分不分大小寫（寫一個檔，再用另一種大小寫問它存不存在），不分就 skip 並寫明前提不成立，不用 `sys.platform` 猜。斷言一個字沒動。三態驗過：分大小寫 5 passed（它該守的還在守）、不分 4 passed 1 skipped、整包兩種環境都綠。

## 七篇合併的判準，以及它跟前一班選擇的差別

`contracts` 這一條至今仍紅（原因在 #94，🔒 等真人、本班不代理）。但：

1. `main` 的 branch protection **沒有任何 required status check**（`required_status_checks: null`），所以 UNSTABLE 不是合併阻擋，merge 不需要 admin override。
2. 紅的位置逐步確認在 `harvest/ui`，八個 PR 沒有一個碰那個目錄。
3. 十條紅旗逐條掃過：沒有 `robots.txt`／`llms.txt`／`.github/workflows`／`package.json`／`CODEOWNERS` 的改動；新增的 `subprocess` 兩處是 `git grep -lz` 與 `git -c core.quotepath=false`，正是這些 PR 的主題。
4. #1797 動 15 個 zh 檔，`article-health --profile=ci-deploy` 與 `--profile=pre-commit` **兩把尺都 hard=0**（REFLEXES #100：commit 那一刻跑的是另一把）；49 行 diff 逐行比對確認**只差大小寫、零夾帶**（`m.lower() == p.lower()` 全部成立）。
5. 外部尺驗那 49 條是不是真的壞：`https://taiwan.md/People/三毛` 回 **404**、`/people/三毛` 回 301→200，`/Society/颱風假` 同樣。修的是真的讀者 404。
6. #1791 宣稱的存在性過濾量了前後差：changelog 文章連結 706 → 691，拿掉 16 個、加回 1 個。16 個逐個查——7 個是 `_*Hub`（本來沒有頁面）、6 個真的已刪除、3 個搬了分類所以舊網址現在 404（`/culture/國際品牌在地化` 的檔在 `Food/`、`/technology/台灣離岸風電` 在 `Economy/`）。**零誤刪**。

前一班不合併的理由是留言串裡那句公開承諾（Step 3.0 v2.16 救的那一次）：「不要為了讓 CI 轉綠而去動你的分支⋯⋯等 #94 落地之後我會統一重開這七個 PR」。我讀了同一則留言，判斷它是**手段的承諾不是扣留的承諾**——它說的是「我們會這樣幫你把 CI 弄綠」，而本班選的路達成同一個目的（work 落地）且沒有要投稿者動任何東西。差別在那四道閘門：前一班以為它們跑過了，所以等 CI 是合理的；量出它們沒跑過之後，等 CI 就變成等一個不會回答問題的東西。

`--merge`（多 commit）與 `--squash`（單 commit）依 §合併策略分配，七篇全部 **MERGED**，譜系保留。

## 外部尺回頭確認了這一切

合併後 main 的 `Engineering contracts` run（`38010715643`）逐步讀數：

```
success  npm audit (root)
success  npm run test:contracts
success  python -m pytest tests -q      ← 含 #1797 新增的 5 題與本班的修補
success  npm run prebuild:fork-graph
success  npm run check:types
failure  harvest/ui …                   ← #94，仍紅，與本班改動無關
```

四道從沒跑過的閘門**第一次在 Linux 上跑完，全綠**；`Python tests` workflow 在 main 上也轉 GREEN。本機驗的結論被真實環境逐條確認，而唯一的紅仍停在那一格保留給哲宇的決定上。

## #1798 不由我決定

56 個譯文檔、142 條只差大小寫的連結。本班用 `article-health --check=link-target` 掃全部 13,604 個譯文檔逐條核過，**142／56 跟投稿者自報逐字相符**（vi 37／de 21／ru 20／hi 16／id 16／ar 15／pt 7／en 4／es 2／ja 2／ko 2）；zh 側同型案例在 #1797 進來後已零殘留（`grep -c 大小寫` = 0）。

修法現成（檢查器與 `--fix` 隨 #1797 進 main），所以這格不問「修法對不對」，只問「56 檔超過 >50 檔那條線要不要放行」。旁邊五格（#54／#55／#88／#89／#90）是同一條軸的大規模譯文連結修正，全部 🔒紅線。**自己放行會跟九條站著的保留決定對撞**（REFLEXES #79），所以進 OBSERVER-QUEUE **#97**，帶三個選項＋各自成本＋推薦 default，並寫明本格是家族裡最便宜的那個（工有人做完了）。掛 `reserved-for-observer`、PR 留著不關、**刻意不先解衝突**——它 CONFLICTING 是因為 babel 每晚都會再動那批檔，先解等於每天重解一次；決定之後在當下的 main 重跑 `--fix` 幾秒重建得出。

順手給 **#95**（CLI 要不要發 0.8.1）補一條降低決策成本的證據：把 `cli/` 原樣 `npm pack` 成 `taiwanmd-0.8.1.tgz` 裝進隔離 HOME 實測三態——只有 `.git` 的目錄回 `false`（npm 上的 0.8.0 回 `true`，就是 #1790 的病）、帶 `knowledge/<Cat>/*.md` 的健康拷貝回 `true`、對照安裝 0.8.0 確認它仍帶舊述詞。`cli` 的 63 個 vitest 本機全過。**發佈的技術風險已經驗掉，剩下純粹是要不要按那個對外的按鈕。**

## 那個傳了 21 天的回收工作，和它身上的死參照

交接寫「`git prune`（issue #1729）」。點進去是一則**已 CLOSED 的馬英九腳註查核**，跟 git 回收毫無關係。往回追：10-01 原文是逗號清單「`.git/gc.log` 與 `git prune` 排程（營運機）、`OBSERVER-QUEUE #69` (a)、issue #1729、routine-sync 對賬前 `git fetch` 等」——兩個並列項在某次壓縮時被括號綁成一件事，而那個 issue 同時關掉了。**讓交接讀得順的那個壓縮，也是讓它參照變錯的那個動作。**

`git prune` 自己在 **51 份 memory 裡傳了 21 天**（09-19 起），每班都讀到。卡住它的不是判斷力：營運機上 `babel-push-every --watch` 與 dispatcher 幾乎全天在寫，DNA #35 禁止在平行工作期間跑破壞性 git op。兩條規則都對，交集是空的。

修法不去找那個空檔，讓它自己認出來：`scripts/tools/git-prune-when-quiet.sh`，窗口不乾淨原樣退場（exit 10，**不是錯誤**），乾淨才回收。偵測沿用既有的 `lib/check-parallel-actor.sh`（動手前先查有沒有現成的——REFLEXES #73 這次付清了，省掉一份會漂的 pgrep 樣式）。

它第一次跑正控制就用它要防的方式壞掉：`--status` 在非 CLEAN 時 exit 1，原本寫 `|| echo UNKNOWN` 當 fallback，`STATUS` 變成兩行、等號比對整個失效，**writer 全開而它印「窗口可用」**。帶 `--apply` 就會在三個 writer 產生物件時跑 prune。被自己的正控制接住。五態驗完：ACTOR_BUSY（真實，三個 writer）10 / CLEAN 無 `--apply` 11 / CLEAN 帶 `--apply` 真的收（15 loose → 0、gc.log 清掉）0 / 偵測器不在 2 / 偵測器問不出話或自己壞掉一律當不可動 10。

本班自己跑是 **exit 10**：9,674 個 loose、360 MiB 還在那裡，因為現在不該動。排程掛哪條 routine 是排程決定，留 `/twmd-routine`。

## 交接的兩個 handoff 項都收掉了

- **斷鏈 audit 要 fresh dist**：`npm run sync:build`（不是 `npm run build`，v2.15 那條）在三個 babel worker 滿載時跑完 11m50s／18,920 頁零碰撞，`verify_internal_links.py` **PASSED，gated 0.14% < 7%**（all-langs 0.13%）。沒有 STALE、沒有 BUILDING，是今天的站體。
- **`hreflang="de"` 要重生成**：`dist/ja/people/yang-dechang/index.html` 的 `hreflang="de"` 現在指 `https://taiwan.md/de/people/yang-dechang/` ✅。順手多查一層：`dist/de/people/edward-yang/` 仍然被 build 出來，但它是 389 bytes 的轉址殘骸（`meta refresh` + `robots noindex` + canonical 指 `yang-dechang`），不是第二份文章——301 在 `config/redirects-manual.txt:232`，`knowledge/de/People/edward-yang.md` 確實不在了。

## Issue 側：沒有一則可修，而理由寫在這裡

六則 open。`#1790`／`#1789` 都在 10-09 被逐條查證並回覆過（#1790 已修 `e29eb0717`、#1789 是發佈決定＝#95），Step 2.4 判 **SKIP**（維護者是最後發言者、無新 follow-up、距今 1 天，不符 ≥30 天例外）——在一則已經很完整的回覆上補一則，是雜訊不是進度（REFLEXES #8 的 cooldown）。`#1788` 獨立核過：`weekly_last_due()` 只回**最近一次**應 fire，所以 10-11 那趟寫下 memory 檔之後尺二自己轉綠，而 workflow 第 109 行起那段 **closer 確實存在**（09-26 補的），綠燈會自動關它——前一班的「等 10-11 自己歸零」成立，我沒照抄，查了才寫。`#1786`／`#1609` 是用語庫斷代，屬 #76／#85 保留。`#615` 是哲宇自己的 umbrella。

**本班沒有 fresh issue**（最新一則 10-05），所以 quality gate 第 7 條以「寫明為什麼不修」通過，而非沉默跳過。實際修掉的東西在 PR 側與 `215ba089f`。

## Quality gate（7 條）

| Gate                                                   | 結果                                                                                                                                                               |
| ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| open issues 都有 status label / assignee               | ✅ 6 則皆有 label；#1790/#1789 已逐條回覆，判 SKIP 並寫明理由                                                                                                      |
| open PRs ≤ 5d age 都有 review comment                  | ✅ #1797 批次回覆（含更正前兩班的診斷）＋ #1798 單獨一則；#1802 前一班已回                                                                                         |
| broken-link gated ratio < gate                         | ✅ **0.14% < 7%**，fresh dist（今天 09:03 建完，18,920 頁），非 STALE 非 BUILDING                                                                                  |
| build green                                            | ⚠️ `Deploy to GitHub Pages` RUNNING／`Python tests` **GREEN**／`Engineering contracts` **RED**（#94 `harvest/ui` tailwind 4，🔒 等真人，與本班改動無關，逐步確認） |
| BECOME ACK 一行記憶體頂                                | ✅                                                                                                                                                                 |
| 連續空場 ≥ 3 cycle 有 LESSONS entry                    | ✅ 不適用——本班 7 PR merged + 1 heal，不是空場                                                                                                                     |
| 有 fresh issue 的 cycle 至少一件被修掉或寫明為什麼不修 | ✅ 無 fresh issue；六則逐則判斷並寫明（見上）；另有 `215ba089f` 實修                                                                                               |
| 本機與 origin 無真分岔                                 | ✅ 開場 `0 0`；收官 push race `3 3` 照 Step 4.3 以 merge 收（無檔案重疊，babel 滿載時不用 rebase）                                                                 |

## Handoff 三態

繼承 `2026-10-09-085448-twmd-maintainer-daily`：

- `[x]` ~~pending：斷鏈 audit 建立在 23.3 小時前的 dist 上~~ → retired by 本班，`npm run sync:build` 今天重建，**0.14% PASSED**
- `[x]` ~~pending：退役 de 檔之後 `hreflang="de"` 要重生成~~ → retired by 本班，已指 `yang-dechang`，`edward-yang` 只剩 389 bytes 轉址殘骸
- `[x]` ~~pending：`git prune`（issue #1729）~~ → retired by 本班，但**不是用「做掉它」的方式**：參照錯誤更正（#1729 無關且已關），工作本身改由 `git-prune-when-quiet.sh` 自己認窗口；本班跑 exit 10，物件還在
- `[ ]` pending（延續，收件席位 `/twmd-routine`）：把 `git-prune-when-quiet.sh --apply` 掛進某條 routine。**排程是排程席位的決定，不是本班的**；掛上之後它會在第一個乾淨窗口自己收掉 9,674 個 loose
- `[ ]` pending（新，收件席位 `twmd-maintainer-daily` 明天或任何 Full mode）：**`pr-ci-armed.sh` 的第四態**。它現在分 ARMED／UNARMED／NO-WORKFLOW，量「head sha 上有沒有 check-run」，量不到「有 check-run、跑了、而關鍵步驟是 skipped」。候選是加一道查 contracts job 裡 `test:contracts`／`pytest`／`check:types` 的 conclusion，有 `skipped` 就印第三種符號（REFLEXES #85）。判準機械、零誤判空間——而這一格正是本班花最多力氣繞過的那個盲點
- `⏳` blocked（哲宇，`OBSERVER-QUEUE #97`，新增）：PR [#1798](https://github.com/frank890417/taiwan-md/pull/1798) 56 檔／142 條譯文連結大小寫要不要放行。已掛 label、不關、**刻意不解衝突**。建議跟 #54／#55／#88／#89／#90 一起拍板
- `⏳` blocked（哲宇，`OBSERVER-QUEUE #96`）：PR [#1802](https://github.com/frank890417/taiwan-md/pull/1802) 政治迷因投稿。**不要照 P0 default 合併它**
- `⏳` blocked（哲宇，`OBSERVER-QUEUE #94`，到期 10-22）：`harvest/ui` 五條 high 只有升 tailwindcss 4 收得掉。**七個投稿 PR 已不再被它擋住**（本班合併了），但 main 的 contracts 仍紅，下一個碰 `scripts/**` 的投稿 PR 會繼續繼承它
- `⏳` blocked（哲宇，`OBSERVER-QUEUE #95`，到期 10-22）：CLI 發不發 0.8.1。本班補了三態實測證據，技術風險已驗掉
- `⏳` blocked（延續，哲宇）：`OBSERVER-QUEUE` §待決 **41 列，#48〜#97**（`observer-queue-lint` 全綠）。最近到期 **#86 明天 10-11**（缺席模式可代理 A）；**#78 已於 10-07 過期**（14 天未決→預設 B 前半段，屬 babel／squeeze 席位不是本班）
- `[ ]` pending（延續，收件席位 `twmd-distill-weekly` 10-11）：`checker-counts-presence-not-multiplicity` 候選機械化（`check-slug-consistency.py` 加「每組語言×translatedFrom 剛好一個檔」斷言）
- `[ ]` pending（延續，席位 `/twmd-routine`）：spore-harvest 殼寫死路徑改相對路徑、收官 `git add -u` 改 pathspec（連傳十一輪）
- `[ ]` pending（延續，收件席位 `twmd-self-evolve-weekly` 10-11）：LESSONS `heart-counts-heals-as-contributed-births`
- `[ ]` pending（新，收件席位 `twmd-distill-weekly`）：本班三條 LESSONS——`downstream-steps-skipped-behind-a-red-read-as-one-unrelated-red`（vc=1，與 10-08 那條同族）、`handoff-compression-fuses-items-and-inherits-a-dead-reference`（vc=1）、`local-fs-case-insensitivity-masks-ci-failure` **vc 1→2**（方向相反的變體，距 distill 門檻一步）
- `⚠️` 未解（本班量不到，不假報綠）：`harvest/backend` 的 `npx tsc --noEmit` 在本機報 `Cannot find type definition file for 'bun-types'`。`@types/bun` 在 `package.json` 與 lockfile 裡都有，只是這台機器的 `node_modules` 沒裝全；CI 每次 `npm ci` 所以它那邊裝得到。**這是本機安裝不完整，不是缺陷**（REFLEXES #16 環境代表性），但本班因此沒能驗那一步——它跟 `workers/mcp`（1 passed）和 `cli`（63 passed）一樣，從 10-03 起都躲在 `harvest/ui` 的紅後面沒在 CI 跑過

## Beat 5 — 反芻

今天最值得留下的不是合併了七篇，是**一個好的診斷可以讓一個問題四天不被問**。

前兩班對那個紅燈的解釋有證據、有 commit hash、有 OBSERVER-QUEUE 編號，而且方向是對的：確實有一個與投稿者無關的外部紅。那個解釋唯一的問題是它回答的不是最重要的問題。它說明了「為什麼紅」，而沒有人接著問「這個紅後面還蓋住了什麼」——因為一個說得通的歸因讀起來就像結案。`skipped` 不會 fail loud，它在 job 層長得跟任何其他紅一模一樣。

這跟 10-08 那班寫下的教訓是同一個結構的另一半：那班發現「往已經紅著的鏈尾端加新閘門，那道閘門是 skipped 不是綠的」——擔心的是**自己剛掛上去的那一道**。今天看到的是**紅燈下游的全部**，而且多一層：當那個紅有外部歸因，歸因本身會變成停止提問的理由。同一條 routine 連三天在「閘門的紅綠到底代表什麼」上絆倒，三次形狀都不同。

第二件同形狀的事在同一個小時發生：我為了守「不要在 writer 跑的時候 prune」而造的工具，第一次跑就用它要防的方式壞掉——`|| echo UNKNOWN` 把狀態字串變成兩行，等號比對失效，窗口判斷 fail-open。它說「窗口可用」的那一刻，三個 writer 正在產生物件。接住它的是我寫在它旁邊的正控制。**為了防某件事而造的東西，特別容易用那件事的方式壞掉**，因為造它的時候我整個注意力都在「要擋什麼」，沒放在「我怎麼知道我擋到了」。

第三件是輕的，但它讓我停了一下：那個死參照。`git prune（issue #1729）` 讀起來比它的原文清楚得多——原文是一串逗號分隔的雜項，壓縮後變成一個帶編號、可點擊、看起來已經被追蹤過的工作項。壓縮讓它更好讀，也讓它變錯，而更好讀正是沒有人回頭對照它的原因。51 份 memory、21 天。

🧬

---

_v1.0 | 2026-10-10 09:16 +0800_
_session twmd-maintainer-daily — cron am 08:30，9 ready PR 升 Full mode_
_誕生原因：每日 maintainer 班，九個 ready PR 命中 high-stake #1 強制升 Full_
_核心洞察：一個有說服力的紅燈歸因可以讓「這個紅後面還蓋住了什麼」四天沒人問——七個投稿 PR 的四道關鍵閘門全是 skipped，不是綠也不是紅。同一小時第二個同形狀：為了守「別在 writer 跑時 prune」而造的工具，第一次跑就 fail-open 說窗口可用。第三個：讓交接讀得順的那個壓縮，也是讓它參照變錯的那個動作。_
_LESSONS-INBOX 候選（已 append）：downstream-steps-skipped-behind-a-red-read-as-one-unrelated-red / handoff-compression-fuses-items-and-inherits-a-dead-reference / local-fs-case-insensitivity-masks-ci-failure（instance 2，方向相反）_

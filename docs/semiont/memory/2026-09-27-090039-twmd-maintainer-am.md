---
session_id: '2026-09-27-090039-twmd-maintainer-am'
session_span: '2026-09-27 08:30 – 2026-09-27 09:05 (+0800)'
trigger: 'routine twmd-maintainer-daily（cron am 08:30）'
observer: '無（cron，哲宇最後在場 2026-09-26）'
beat_coverage: 'BECOME review + MAINTAINER-PIPELINE Stage 1-4'
mode: 'review'
---

✅ BECOME ack: mode=review / 8 organ 最低=🛡️57（即時 `consciousness-snapshot.sh`：🫀90 🛡️57 🧬95 🦴90 🫁85 🧫100 👁️90 🌐92，快照齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# 2026-09-27-090039-twmd-maintainer-am — 佇列是空的，所以這班去量那些二十天沒人量過的東西；三把尺自己在說謊

> routine twmd-maintainer-daily · cron am 08:30 · 4 個 commit，0 個 PR，0 則新 issue
> 進場 open PR 0、open issue 4（全是舊的）、Discussions 無人未回；收官同上。

## 這班的形狀

沒有 PR 可審，沒有新 issue 進來。前一班（09-26 23:02 哲宇觸發）收掉五個 PR，所以空場 **vc=1**，還沒到 ≥3 的 escalate 線。

空場的班最容易寫成「healthy empty」然後走人，而 routine 殼的空場鐵律就是為了擋這一句。所以這班把力氣放在**沒人在量的東西**上：`dist/` 停在 09-07，死連結閘門因此連續回 STALE 二十天；CI 健檢那段指令的窗口沒人量過；交接裡掛了幾輪的 `.git/gc.log` 沒人真的去看。

量完之後，**三把尺當場被抓到在說謊**——而且是同一種謊的三個載體：都用「零」或「少」冒充「我看完了」。

## 一、死連結：二十天來第一次真的量到

`dist/` 的 `index.html` 停在 2026-09-07 09:09，齡 479 小時。09-25 那班加的 STALE 出口（`6868e12dc`）運作正確——它誠實回報「我量到的是 18 天前的站」，但**誠實不等於量到**，這二十天沒有任何一輪真的知道站上死連結是多少。

本班跑完整 `sync.sh` + `astro build`（17 分 13 秒，18,905 頁），再跑閘門：

```
Broken ratio (all langs)  : 0.15%
Gated ratio (excl es/fr)  : 0.16%  [1998/1237861]   PASS < 7.0%
zh-TW 0.33%(1669) · vi 0.13%(91) · ja 0.09%(69) · en 0.04%(33) · ru 0.02%(14)
es 0.03%(23) / fr 0.06%(46) — REPORT-ONLY 未進 gate
```

全部遠低於閘門。`sync.sh` 與 `astro build` 只寫 gitignore 的 `src/content/` 與 `dist/`，所以整段 build 沒有碰過任何 git 追蹤的檔（進出場 `git status` 逐行對過）。

## 二、CI 健檢：那段指令只看得到最近 8.3 小時

Step 1.5 寫的是 repo-wide 取最新 100 筆 run 再 group-by。09-03 那次把「點名兩條 workflow」改成 group-by 全表，方向是對的——`Python tests` 紅在 main 四天沒人看到就是因為它不在被點名的名字裡。但 group-by **只看得到那 100 筆裡出現過的 workflow**，而本庫 babel 整點 commit、deploy 跟著跑：今天實測那 100 筆涵蓋 **15:19Z → 23:35Z，8.3 小時**。一條掛 paths filter 的 workflow 紅完之後不再被觸發，就會滑出這個窗——**上一段擔心的那種紅，正好是最容易滑出窗的那種紅**。

造 [`ci-main-health.sh`](../../scripts/tools/ci-main-health.sh)（`94cc107b3`）：先列 workflow，再逐條問它自己的 runs endpoint，窗口大小跟 commit 量脫鉤。七態自己判（GREEN／RED／BLOCKED／UNKNOWN／RUNNING／OFF-BRANCH／NEVER-ON-MAIN），刻意不設「幾天沒跑算 stale」的門檻，因為掛 paths filter 的 workflow 冷幾天是正常的，憑感覺設數字只會生假陽性。

**新尺首跑就報了兩個假陽性，兩個都是它自己的**：

- `?branch=main` 比對的是 `head_branch`，而**投稿者從自己 fork 的 main 送來的 PR，head branch 就叫 main**——一則 2026-04-01 投稿 PR 的失敗被報成「Translation PR Check 在 main 紅了 178 天」。
- `push:` 不等於「會在 main 上跑」：`push: {tags: [cli-v*]}` 是 tag 推送，`npm-publish-cli` 因此被報成 NEVER-ON-MAIN。

兩個都修掉，再餵 fixture 過正控制（failure／stale／不認得的值三態正確亮燈、`--strict` 回 1）。修完今天的真值：**13 條 active workflow，RED 0**。MAINTAINER-PIPELINE 升 v2.14，skill 殼 Stage 1 同步。

## 三、URL 對賬器：讀取上限被 sitemap 長過去

順手跑 `check-url-contract` 看 build 有沒有回歸，它說 **1,752 篇文章頁不在 sitemap**，例子清一色 `/ru/`。抽 `/ru/people/ang-lee/` 去 `dist/sitemap-0.xml` grep——**它在 `<loc>` 裡**。

追上游：那支工具讀 sitemap 寫 `readHead(file, 16MB)`，註解說「sitemap 只有幾 MB」。今天 `dist/sitemap-0.xml` 是 **18.5MB**，超出的 3.4MB 被無聲切掉，17,785 個 `<loc>` 只進來 13,218 個。

兩個方向的傷害剛好互相掩護：sitemap 尾端是字母序偏後的語言前綴，所以缺席名單清一色 `/ru/`，看起來像俄文那層的接線壞了；另一邊 4,567 個 `<loc>` 從來沒被檢查過死活，而報告印的 `dead: 0` 跟「全驗過全乾淨」逐字相同。**一個假警報配一個假綠燈，哪一邊單獨出現都會被追，兩邊一起出現就長得像工具在正常工作、只是某個語言有問題。**

這支工具的誕生理由，正是 2026-07-17「站體對外公告 13,014 條死 URL、三個月沒人對帳」那次事件。它自己把對帳做成了 74%，沒有一行輸出提過。

修補（`4fcde71da`）：sitemap 改整份 `readFileSync`、讀失敗出聲並記進 `sitemapReadFailures`、結果多印 `sitemapLocsIngested` 讓「進來幾個」變成看得見的數字。修完 ingested **13,218 → 17,786**、反向覆蓋 **1,752 → 0**、正向 dead 仍是 0（這次是完整的 0）。正控制兩道都過。

## 四、`/sitemap.xml` 404：正確修法兩天前就寫在註解裡，沒有人動手

爬蟲慣例先試 `/sitemap.xml`，站上一直 404（CF 一天約 10 筆，unknown 家族榜首）。09-22 那次修補寫成 `_redirects` 的 301，而這站部署在 GitHub Pages，不讀那個檔。09-25 data-refresh 查證後，把正確修法逐字寫進 `config/redirects-manual.txt` 的註解：「要真的接住，得在 build 產出裡放一份 sitemap.xml」。

那句話在那裡躺了兩天。本班做掉：`scripts/core/emit-sitemap-alias.mjs` 在 `postbuild` 把 `sitemap-index.xml` 複製成 `sitemap.xml`，找不到來源就 `exit 1`。驗過位元組相同、是合法 sitemap index、正控制（來源缺席）回 1。CI 的 `npm run build` 走 npm 生命週期，所以下次 deploy 就會帶上。

線上驗收留給 deploy 之後：本班量到的是「產物裡有了」，不是「線上 200 了」——這正是 09-22 那次栽的地方（LESSONS `fix-lands-in-a-layer-the-platform-never-reads`），所以寫進交接由下一班用 `curl` 收。

## 五、`.git/gc.log`：差一點把兩個假零寫成「已驗過」

交接掛了幾輪的「`git prune` 清 unreachable loose objects」。本班量它，**同一小時撞到兩次同一種假象**：

- `timeout 300 git prune -n` —— macOS 沒有 `timeout` 這個 binary，整串 exit 127、零輸出；後面接的 `echo "exit=$?"` 報的是管線最後一段 `wc -l` 的離開碼，於是印出「exit=0」替它作證。
- `find ... -newermt "14 days ago" 2>/dev/null` —— 這台的 `find` 是 `bfs`，只吃 ISO 8601 時間字串，它把參數退回並寫 stderr，而 stderr 正被丟掉，於是回一個 `0`。

兩個零我都當成事實讀了一輪，先讀成「沒有東西可以安全清掉」，再讀成「鬆散物件全都超過兩週」。**這兩句話互相矛盾，撞在一起才逼我回頭重驗。** 差一點就把「已驗過：prune 是 no-op，可以退役」寫進交接——那句話會以「已量過」的身分傳下去。

拿掉 `timeout`、不再吞 stderr 的真值：**9,965 個不可達物件，mtime 全落在 09-19～09-27 這八天內**。所以 `--expire=2.weeks.ago`（`git gc` 的預設）清得到 **0 個**，而 `--expire=now` 會刪掉三支 babel writer 正在跑的那八天的東西。結論整個反過來：**不是沒東西可清，是可清的全都太新，安全的過期窗清不到它們**。

這是本機跑翻譯產線的常駐狀態，不是一件待辦。唯一可做的決定是要不要替這台機器調低 `gc.pruneExpire`，而那是閾值調整（High-stake #3，🔒閾值），不在本班席位。本班不跑 `gc`：三支 writer 在跑、剛做完 17 分鐘的 build，重 I/O 不是現在做的事。

## 六、Issue：四則全舊，一則換了位置

| #     | 齡       | 處置                                                                                                                                   |
| ----- | -------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| #1729 | 13 天    | ⏳ 續 blocked：馬英九兩條腳註對不上來源，屬 zh SSOT 實質內容 × 政治人物 × 12 語，走 FACTCHECK Full ＋ CORRECTION，不在維護班 heal 範圍 |
| #1678 | 22 天    | ⏳ 續 blocked：〈生態多樣性〉要的是正文重寫，查好的數字與來源已在 ARTICLE-INBOX，走 REWRITE                                            |
| #1609 | 32 天    | **換位置**：見下                                                                                                                       |
| #615  | umbrella | 無新動作                                                                                                                               |

**#1609（「無語」的斷代）本班的實際產出**：9/24 那班說「卡點只剩一次登入」，那是推論；本班去戳了。臺灣日記知識庫是 MediaWiki，但 `api.php` 對匿名身分同樣回「權限錯誤」——連 `action=query&meta=siteinfo` 這種最簡單的呼叫都擋（正控制通過，所以是整層擋讀不是查詢寫錯），沒有匿名 API 繞道；頁面又帶 `noindex,nofollow`，搜尋引擎沒有快取可撈；國家人權博物館與開放博物館側也沒有這兩冊的全文。

三條死路寫進詞條的 `locations`，是為了不讓下一班再走一次。既然它不缺線索也不缺範圍、缺的是一個人的動作，就不該繼續躺在維護交接裡等下一班「再查一輪」——**下一班能做的事今天已經做完了**。升進 **OBSERVER-QUEUE #85**，標 🔒紅線（身份授權 human-only，永不代理）。issue 上給蘇洛一則事實性更新（三條死路 + 換了位置 + 判定仍未動），不含任何時程承諾。

## Quality gate（7 條）

| Gate                                     | 結果                                                                                                                                                |
| ---------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| open issues 都有 status label / assignee | ✅ 4 則皆有 label（#615 enhancement / #1609 enhancement,from-feedback / #1678 content,needs-verification,from-feedback / #1729 needs-verification） |
| open PRs ≤ 5d age 都有 review comment    | ✅ n/a — open PR 0                                                                                                                                  |
| broken-link gated ratio < gate           | ✅ **0.16% < 7.0%**（二十天來第一次真的量到，非 STALE）                                                                                             |
| build green                              | ✅ 13 條 active workflow RED 0（`ci-main-health.sh`）＋ 本機 build 18,905 頁成功                                                                    |
| BECOME ACK 一行記憶體頂                  | ✅ 見檔頭                                                                                                                                           |
| 連續空場 ≥ 3 cycle 有 LESSONS entry      | ✅ n/a — vc=1（前一班收 5 個 PR，計數歸零）                                                                                                         |
| 有 fresh issue 的 cycle 至少一件被修掉   | ✅ n/a — 0 則新 issue；但本班仍 ship 四個修補，不以空場結案                                                                                         |
| 本機與 origin 無真分岔                   | ✅ `0 0`（Stage 1 第一件事）                                                                                                                        |

## 本班 commit

- `94cc107b3` CI 健檢改用儀器（`ci-main-health.sh` ＋ MAINTAINER v2.14 ＋ skill 殼）
- `3007f2975` 「無語」三條死路寫進詞條 ＋ OBSERVER-QUEUE #85
- `0bc28260c` LESSONS：兩個量測指令死在執行之前
- `4fcde71da` URL 對賬器讀取上限 ＋ `/sitemap.xml` 落進產物 ＋ LESSONS

全部 main-direct，`5c2fbec08..4fcde71da` 已推。進出場 `git status` 逐行對過：babel dispatcher 的 67 個 staged 檔全程沒被動到，本班一律用 pathspec commit；收官時清掉 `OBSERVER-QUEUE.md` 的索引殘影（REFLEXES #100 (e)，`verify-commit-scope.sh` 那次自動清撞到 git lock 沒成功）。

## 本班的一句話

**三把尺在同一個早上被抓到說謊，用的是同一句話：「零」。** shell 管線的零（指令沒跑起來）、讀取上限的少（只讀進 74%）、group-by 的窄（只看得到八小時）——三種都不是壞掉，是**沒看完卻印得像看完了**。而佇列空的那天，正好是唯一有餘裕去量尺本身的那天。

## Handoff 三態

繼承 `2026-09-27-071550-twmd-feedback-triage`：

- [x] ~~🚨 mouhouse 登入過期 `#1761`~~ — 已 retired（09-26 續登，下次預估 2026-10-26）
- ⏳ blocked（延續）— issue `#1729`（馬英九腳註）等 Write／FACTCHECK session；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 為 manual-by-decision（ROUTINE.md 註 ¹³，**已決**）
- [ ] pending（延續，席位 `twmd-self-evolve-weekly` 10-04）— `routine-sync.py` 對賬前 `git fetch`、印鏡像新鮮度
- [ ] pending（延續，席位 `/twmd-routine`）— data-refresh Stage 1.5 寫明「pipeline 開跑前先跑」
- [ ] pending（延續，席位 spore-harvest，零判斷）— `list_connected_browsers` 回 `[]` 時先查 `--no-startup-window`；`/activity/replies` 逐則對 `time[datetime]`；spore `#29` 下次門檻 1.5 萬；`#29` 兩則位置不明的留言需帶 permalink 巢狀展開能力的 session
- [ ] pending（延續，席位 `twmd-routine-sync`／`twmd-self-evolve-weekly`）— LESSONS `settled-decision-relabelled-as-open-in-handoff` 的對賬儀器
- [ ] pending（延續，席位 spore-pick）— `#175`／`#176` 公告型孢子下次不排 D+30 milestone
- [ ] pending（低優先，等哲宇在場）— Threads 私訊夾是否納入受眾飛輪
- [x] ~~pending — build perf、`/sitemap.xml` 200、`.git/gc.log`（席位 Full／Review session）~~ — 本班處理：`/sitemap.xml` 修補已 ship 待線上收；`.git/gc.log` 量完，見下方改寫；build perf 未動，轉入下方

本 session 新 handoff：

- [ ] pending（席位 任何一班，零判斷，一行指令）— **`/sitemap.xml` 線上收貨**：deploy 跑完後 `curl -so /dev/null -w '%{http_code}' https://taiwan.md/sitemap.xml` 應回 200。本班量到的是產物裡有了，不是線上通了——09-22 那次栽的就是這一步（LESSONS `fix-lands-in-a-layer-the-platform-never-reads`）。回 404 就查 deploy 有沒有跑 `postbuild`。
- [x] ~~pending — 跑 `git prune` 清 `.git/gc.log`~~ — **retired by 本班，因為它不是一件待辦**：實測 9,965 個不可達物件的 mtime 全在最近八天，`--expire=2.weeks.ago`（`git gc` 預設）清得到 0 個，`--expire=now` 會刪掉三支 writer 正在跑的東西。這是跑翻譯產線的常駐狀態。唯一的決定是要不要替這台機器調低 `gc.pruneExpire`，那是閾值調整（🔒閾值），不在 routine 席位——**要下決定的人請看這一段，不要再叫任何一班去跑 prune**。
- [ ] pending（席位 Full／Review session）— build perf 未量（本班 17 分 13 秒 / 18,905 頁，可當基線）；`md-extension` 觀察（LESSONS `relative-category-links-survive-link-check`）；`monitor-404.py` unknown 判定
- [ ] pending（席位 `twmd-distill-weekly` 10-04，只需裁決）— 本班兩條 LESSONS（`absent-binary-and-rejected-flag-both-return-a-confident-zero` / `read-cap-outgrown-by-the-thing-it-reads`）是同一天同一個形狀的兩個載體，判它們該合成一條反射、各自升號、還是 fold 進 #41／#99
- [ ] pending（延續，席位 maintainer-am，零判斷）— `#1609` 第 33 天（已升佇列 #85，續量的是佇列不是 issue）、`#1678` 第 23 天續量，基準沿用建立日含當日

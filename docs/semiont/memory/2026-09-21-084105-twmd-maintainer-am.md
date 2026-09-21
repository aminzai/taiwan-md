# 2026-09-21-084105-twmd-maintainer-am — 三篇投稿譯文收下，十二篇母稿的相對路徑連結修掉、連結檢查器從此看得見相對路徑，紙風車劇團的方括號引用轉成腳註

> session twmd-maintainer-am — cron routine（am 08:30 contributor PR review + issue triage + build sanity + broken-link audit）
> Session span: 08:30 fire → 08:41:05 session-id → 08:44:10 第一個 merge → 08:55 +0800（3 merge + 1 merge-back + 4 heal + 1 evolve + 1 memory）
> 資料來源：`git log %ai` + `gh pr view --json mergedAt`

✅ BECOME ack: mode=review / 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，黃燈自 2026-07-05，review_coverage 缺口 20.25 分）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 排程。Stage 1 第一件事量 `main...origin/main` 得 `9 0`：本機領先九個 babel commit、origin 零領先，純領先，先推上去讓它長不成分岔。掃到 3 個 ready PR（aminzai 第五天連續三篇，未達 High-stake 門檻）、4 個 open issue 全是舊的、Discussions 沒有新的零回覆貼文、main 六條 workflow 全綠（deploy 在跑）、`pr-ci-armed` 三個 PR 都 ARMED 三條 check 全過。babel dispatcher 五個 writer 正在主工作樹寫。

## 三篇投稿譯文（#1758 de／#1759 hi／#1760 id）

三篇都是單檔新增、CLEAN、無紅旗。照 Stage 2 診斷紀律把 PR 內容檔帶進 main 樹跑而不 checkout：`article-health --profile=ci-deploy` 三篇 hard=0。對母稿的 URL 多重集合逐條相同（37／10／18）、H2 數量一致、字元比 2.71／2.93／3.20 落在各語言 band、`target-language-check` 零警告。抽讀正文三段確認是真翻譯不是摘要。`check-slug-consistency` 對 hi 那篇報「應命名為 `taiwan-regional-street-food-map`」，追下去發現 en 有兩份同源檔（既有的「en 六組同源雙檔」之一），其他八個語言都用 `taiwanese-street-food`，投稿者的選擇跟家族一致，檢查器只是挑到了另一個孿生，不是譯文的錯。麥當樂的 `curation: incubating` 投稿者有照母稿帶進來，跟八個 sibling 對齊。

三篇 `gh pr merge --merge` 落地（`512096a1d`／`4f68163f6`／`8b4b9d4b3`），營運機用 merge commit `6c6239b0b` 併回（dispatcher 在跑，不 rebase），翻譯狀態表 `5476926b8` 補進。致謝照 burst 規則整批一則留在 #1760，順手把 en 雙檔那件事跟他講清楚。

## 十二篇母稿的相對路徑，和看不見它的檢查器

data-refresh-am 今早交來的 handoff：12 篇 zh 母稿的延伸閱讀寫成 `../History/台灣鐵道史` 這種相對路徑，瀏覽器從 `/en/history/xiluo-bridge/` 往上解析成 `/en/history/History/台灣鐵道史`，zh 本身也 404，巴別塔忠實放大成 12 語 129 份譯文 405 條斷鏈。母稿 12 檔在 Micro 範圍內，本班做掉：38 條連結全改成 `/category/slug` 絕對路徑，三條目標不存在的另外處理（誠品書店的「城市與人文地理」改指大稻埕、「電影」改指台灣電影，臺灣大百科的「文化部」沒有條目改成純文字），葉廷皓圖片來源段順手拿掉一句指向內部 pipeline 檔案路徑的括號，`4f3974f86`。譯文那 129 檔沒碰，母稿 source sha 變了 babel 會自己追。

閘門那一半也補了：`verify_internal_links.py` 原本只認以 `/` 開頭的 href，相對路徑一律當外部連結略過，所以這條病連續多輪印綠燈。加 `is_relative_href` 與 `resolve_relative_href`，照瀏覽器規則以頁面目錄為基準 normpath 成絕對路徑再驗，報表保留原始寫法標 `(relative: ../X)`。在 09-07 的舊 dist 上跑一次，456 條原本看不見的相對連結全部現形，gated ratio 0.34% 仍在 7% 門檻內（`69f7c6211`）。LESSONS `relative-category-links-survive-link-check` 加一行落地紀錄，候選 (c)「babel 產線拒收 `../`」沒做。

## 紙風車劇團的方括號引用

09-20 交接的 1-file 項：母稿 17 條 `[N] 來源. (日期). _標題_. 取自 [url](url)` 純方括號引用、正文 40 處 `[N]`，PR #1755 的 ar 譯者忠實保留了這份格式債。寫一段正規式把定義轉成 `[^N]: [標題](url) — 來源，日期`、正文 `[N]` 轉 `[^N]`，再讓 `footnote-format-fix.py` 收尾 9 條，`article-health` footnote 三個 plugin 全綠，`fd35815e1`。四條定義正文沒引用（`[^3]`／`[^4]`／`[^5]`／`[^8]`）是原稿就有的，info 級，沒動。

## 四則 open issue 的判斷

沒有 fresh issue。四則舊的各自核過一次「擋住它的東西還在不在」：#1729 馬英九兩節重寫仍在 ARTICLE-INBOX P0 等哲宇 review（09-18 heal `8cc6a667e` 之後沒有新 commit）。#1678 生態多樣性 EVOLVE 工單仍 pending、文章自 `d8646a2a9` 沒動。#1609 郭淑姿日記查證等讀者回覆冊次或到館調閱，詞條自 `4268e1333` 沒動。#615 是 umbrella。三則的最新留言都是維護者、無新 follow-up，Step 2.4 SKIP 不重複回應。本班沒修 issue，理由是三個阻塞點都在維護班職責之外（政治人物脊椎判斷／REWRITE／外部史料），這是判斷不是省略。

順手：`.git/gc.log` 擋住 auto-gc 好幾天（每個 git 指令都在警告），`git prune` 後 loose objects 16,282 → 456，gc.log 移除。W38 roadmap「合併後 git gc 被擋」那項可以結案。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅ `git log %ai`                                      |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅ derived 層，本班不動                               |
| 自我檢查工具 PASS            | ✅ article-health --profile=memory-diary（見 footer） |

## Quality gate（MAINTAINER Stage 4.1）

| Gate                                     | 結果                                                   |
| ---------------------------------------- | ------------------------------------------------------ |
| open issues 都有 status label / assignee | ✅ 四則都有 label                                      |
| open PRs ≤ 5d 都有 review comment        | ✅ 三篇合併＋整批一則致謝                              |
| broken-link gated ratio < 7%             | ✅ 0.34%（含新認的相對路徑，es/fr report-only 未另列） |
| build green                              | ✅ main 六條 workflow 全綠，deploy in progress         |
| BECOME ACK 一行記憶體頂                  | ✅                                                     |
| 連續空場 ≥ 3 cycle 有 LESSONS entry      | ✅ 不適用，vc=0（今日有 3 fresh PR）                   |
| fresh issue 至少一件修掉或寫明為什麼不修 | ✅ 無 fresh issue，四則舊 issue 的不修理由寫在上節     |
| 本機與 origin 無真分岔                   | ✅ `9 0` 開場即推，收官 `0 0`                          |

## Handoff 三態

繼承上一 session（09-20 twmd-maintainer-am ＋ 09-21 twmd-feedback-triage ＋ 09-21 twmd-data-refresh-am）：

- [x] ~~pending（給 maintainer-am，12 檔 zh 母稿）— 12 篇母稿延伸閱讀 `../Category/中文slug` 相對路徑改絕對路徑，順手讓 `verify-internal-links.sh` 認相對路徑（LESSONS `relative-category-links-survive-link-check`）~~ — retired by 本 session，`4f3974f86` + `69f7c6211`。
- [x] ~~pending（1-file）— `knowledge/Art/紙風車劇團.md` 十七條 `[N]` 轉 `[^N]`（PR #1755）~~ — retired by 本 session，`fd35815e1`。
- [x] ~~pending（資訊）— `from-feedback` 仍 open 的 #1678、#1609~~ — retired by 本 session：核過阻塞點仍在，判斷寫在 §四則 open issue。
- ⏳ blocked（延續）— issue #1729 馬英九：卸任後／太陽花兩節重寫在 ARTICLE-INBOX P0 等哲宇 review 後由 Write session 接。
- ⏳ blocked（延續，給哲宇）— 用語庫 blanket claim 血緣複查 A/B/C（issue #1733 已關，決定寫在 `memory/2026-09-16-090341-twmd-maintainer-am.md`），OBSERVER-QUEUE 尚未登記。
- ⏳ blocked（延續，給哲宇）— commander-macbook heartbeat 與 musebase maintainer-am 對 issue 修補的職責重疊要在 ROUTINE.md 寫清楚，Step 3.0 assignee 是目前兩台共看的最小訊號。
- ⏳ blocked（延續 spore-harvest 09-21，非本班職權）— Chrome 以 `--no-startup-window` 活著（pid 47290）擴充功能連不上，REFLEXES #70 Tier 2，等哲宇看環境。
- [ ] pending（延續，給下一班 maintainer-am，6 刪 + 6 條 301）— origin/main 上 en 六組同源雙檔（`check-slug-consistency.py --all` 第一段）；今天 hi/台灣小吃 又撞到 `taiwanese-street-food`／`taiwan-regional-street-food-map` 這組，八個語言都跟前者。判準與 diff 規則見 09-19 memory。
- [ ] pending（延續，給 babel session）— 真漂移 10 篇：Computex 四語 `computex-taipei`、ru `miin`、我是OO人四語對 en `oo.md`。
- [ ] pending（延續，給 distill-weekly）— LESSONS `handoff-addressed-to-a-routine-name-lands-on-two-machines` 修補候選 (b) handoff 第四態 `🔧 claimed`。
- [ ] pending（延續，給 distill）— LESSONS `held-fact-never-crosses-into-the-layer-that-acts-on-it` vc=5 候選機械化「出口完整性檢查」。
- [ ] pending（延續，給 Full mode session 或哲宇在場的 session）— OBSERVER-QUEUE #74 選項 A 的 audit（EDITORIAL 正例去標籤重判＋抽 5 篇看骨架同質化），LESSONS `canonical-positive-example-fails-its-own-rules`。
- [ ] pending（延續，給 rewrite 排程）— ARTICLE-INBOX P2〈台灣災難醫療體系〉EVOLVE（issue #1752）。

本 session 新 handoff：

- [ ] pending（給 babel session，LESSONS `relative-category-links-survive-link-check` 候選 (c)）— babel 產線的連結閘門對 `](../` 直接拒收，站上沒有任何合法路由是相對的；12 篇母稿改完後 129 份譯文會因 source sha 變更重譯，重譯時新閘門應該已在。
- [ ] pending（給下一班 data-refresh-am 驗證）— 下次 build 後 `verify-internal-links.sh` 應該印出 `(relative: ...)` 家族且數量接近零（母稿已修、譯文等 babel）；若仍有幾百條，是譯文還沒追上，不是工具壞。

## Beat 5 — 反芻

今天最省事的一件事是 data-refresh-am 交來的那條 handoff：它帶了 grep 指令、帶了數字、帶了「本班未動因為超邊界」的理由，還把「順手讓檢查器認相對路徑」寫在同一行。我讀完直接動手，三十分鐘做完兩半。對照昨天 self-evolve 量出來的雙峰（做得掉的當天做掉，做不掉的缺一個決定），這條是前者的乾淨樣本：交接裡沒有需要我做的決定，只有動作。

反過來看那三則 issue，每一則都已經被前面的班做到「只剩一個決定」的位置，而那個決定不在維護班手上。我今天能做的只有再核一次「阻塞還在不在」，然後如實寫下來。這件事本身沒有進度，但把「沒有進度」量出來，跟昨天 handoff-latency 那把尺是同一個方向。

🧬

---

_v1.0 | 2026-09-21 08:55 +0800_
_session twmd-maintainer-am — 3 PR merge ＋ 12 篇母稿相對路徑 heal ＋ 連結檢查器認相對路徑 ＋ 紙風車劇團腳註轉換_
_誕生原因：cron 08:30 排程；Stage 1 掃到 3 ready PR、data-refresh-am 與 09-20 maintainer-am 交來兩件 Micro 範圍的 handoff_
_核心洞察：帶指令、數字、邊界理由的交接當班就做掉；已經被做到只剩一個決定的 issue，維護班能做的是核阻塞還在不在並如實記下_
_LESSONS-INBOX 候選：無新條目；`relative-category-links-survive-link-check` 加落地紀錄_

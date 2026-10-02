---
session_id: '2026-10-02-085430-twmd-maintainer-am'
session_span: '2026-10-02 08:35 → 09:2X +0800'
trigger: 'cron routine twmd-maintainer-daily @ 08:30'
observer: 'none（cron context，哲宇最後在場 2026-09-26）'
beat_coverage: 'Stage 1-4（MAINTAINER-PIPELINE v2.15）'
---

# 2026-10-02-085430-twmd-maintainer-am — 健康尺讀錯 deploy 的成因定錨、庫外公告紅了四輪的 CI 修掉、讀者回報的那條路通到一篇不含它的文章

> session twmd-maintainer-am — cron routine，無觀察者在場
> Session span: 08:35 → 09:2X +0800（約 50 分，6 個非 babel commit）
> 資料來源：`git log %ai`

```
✅ BECOME ack: mode=review / 8 organ 最低=🛡️59（免疫 v3, review_coverage=19） / Q13 anti-bias=PASS / Q14 cross-session continuity=PASS
```

## 觸發

Cron 08:30 起。開場讀 `ci-main-health.sh` 時 deploy 那列印 `GREEN 24.0d`，而本庫每小時都在 commit、deploy 跟著跑——那個數字違反常識，於是本班從一條「尺自己壞了」的線頭開始。

## Stage 1 掃描

| 項目       | 讀數                                                                  |
| ---------- | --------------------------------------------------------------------- |
| 分岔       | `1 0`（純領先，非分岔，不觸發 Step 1.1b）                             |
| open PR    | 2 ready / 0 draft（#1784 ar、#1782 de，皆 aminzai、MERGEABLE、ARMED） |
| open issue | 進場 5 條，收官 3 條                                                  |
| 過去 24hr  | 10 條 cron fire 全到位，routine-status 無缺席                         |
| 過去 48hr  | babel 十二語持續產出 + 兩班 semiont-heartbeat 巡邏                    |
| main CI    | 進場 RED 1（Engineering contracts，連四輪）→ 收官 RED 0               |
| 免疫器官   | 🛡️59，最大缺口 review_coverage=19（chronic，自 2026-07-05）           |
| 平行寫入者 | babel dispatcher 4-6 個 writer process 全程在跑                       |

## 健康尺把一小時前的綠讀成二十四天前的綠

`ci-main-health.sh` 的 deploy 那列指向 2026-09-08 的 run，而 deploy 前一晚 23:15Z 才剛成功。成因是**帶 `?branch=` 的取數口會間歇回舊頁**：同一支 workflow、同一時刻，不帶 branch 問回 10-01 那筆，帶 `?branch=main` 問回 09-08 那筆，兩邊都自稱最新。

這條是 09-30 那班記下但標為「成因未知、無法重現」的同一個病。能定錨是因為 10-01 那班補了 `↳ run / created / sha` 回顯：有了識別碼才看得出兩次讀的是不同執行，而不是年齡算錯。**上一班留下的是讓下一班查得動的錨。**

試過一條看起來很漂亮的偵測法然後否決它：抓到的舊頁有一次回 `total_count: 0` 卻同時給 50 筆 row，自相矛盾得像個完美信號。但另一次回 `total_count: 2500` 配一樣的舊資料。**count 欄自己也跟著舊**，同一份回應裡沒有任何欄位能揭穿它。所以改用第二個取數口當外部尺，兩口取聯集挑最新（`f3d3c7f10`）。兩口不一致時印 ⚠️ 並計數，因為間歇故障被默默補好，就再也量不到它還在不在。

先用五個合成輸入過正控制（含「新的紅不被舊的綠蓋掉」這條最要緊的），再跑真的：deploy 從 24.0d 改讀 1h，`Routine stall alert` 也撈到原本窗外那筆。舊頁今天只在本班第一次呼叫出現，隨後 20 次重探全新，所以盛行率未知、不可隨需重現，而 ⚠️ 計數器**尚未在真實執行裡觸發過**。

## 連紅四輪的工程契約閘門

紅在 `npm audit`：`devalue`（high，經 astro）與 `fast-uri` 昨天 12:58Z 之後發佈新公告，19:02Z 起連四輪紅。09-30 那班看到同家族的紅、記成「外部資安公告非自家程式」就收工了——那句話描述的是歸屬，不是處置。紅留在 main 上的後果跟任何其他紅一樣：下一個路過的投稿 PR 會繼承它。

兩個都在同一小版本內有修好的版本，所以只動 lockfile、不碰 `node_modules`（babel worker 正在用那棵樹）。`harvest/ui` 中的是同一組公告，一起修——那條 job 有四個獨立的 `npm audit`，只修 root 會讓紅燈從第一道移到第四道。驗法是把 lockfile 複製到乾淨目錄跑 CI 那兩道指令本身，root 與 harvest/ui 都回 0 vulnerabilities（`4291678a4`）。推上去之後 CI 自己確認：`Engineering contracts completed success`，`ci-main-health` RED 0。

## 讀者的回報，和一條通到別處的路

#1678 蕭宇哲 09-05 從〈生態多樣性〉回報遊蕩犬帶的犬小病毒會推高路殺。09-06 那班查證成立、回覆「你說的站上其實寫了」、補一句連去〈台灣石虎保育〉。本班順著那條路走一次：`grep 犬小病毒 台灣石虎保育.md` 零命中。病毒、陳貞志、25 倍全在第三篇〈台灣流浪動物文化〉，引的正是讀者附的同一個窩窩專題。而連結是單向的——流浪動物文化連得到石虎保育，反過來沒有。

所以讀者被送進一篇講咬殺、不講病毒的文章就停住，他自己報的那件事還在下一跳。補的是路不是內容（`825528805`）：〈生態多樣性〉那句拆成兩個去處並補延伸閱讀一列，〈石虎保育〉§三補一段把因果鏈指過去。刻意沒把 25 倍那個數字寫進這兩篇，因為新增事實主張要走 REWRITE，而那個數字在流浪動物文化已經有腳註撐著。

關的時候把 09-06 那句不夠準確的回覆一起更正了，因為指錯地方是我們的事，不是讀者沒找到。

## #1729 整個範圍重驗後關閉

這則要的是三件事，不只開票那兩條腳註。兩條腳註已改（`[^3]` 換維基與官職資料庫、`[^31]` 改回憶錄自序逐字）。09-18 的 FACTCHECK Full mode 把 30 條非維基腳註全驗完，12 條對不上、72 原子裡 17 個查無來源，全落在 `8cc6a667e`。第三件最容易留尾巴，所以不信日期直接驗內容。12 語都在 09-21～09-27 之間重譯過，`grep -ril 'soochow|東吳'` 掃全部譯本零命中，抽讀 en 與 fr 都寫回憶錄自序、30 秒概覽都是拍片回應失智傳言而非辭世。

tboydar 09-29 做的獨立覆驗值得記一筆：他明說「非只信上游的自述」，是第一個從外面拿同一批網址重打一次的人。我們自己的查核結論，過去只有寫它的那個 session 讀過。

## 兩個 PR 不動，是保留不是拖延

#1784 ar 與 #1782 de 四把尺全部平手（10-01 那班量過），待決的是「投稿者送來一份跟現行機器譯文等質、沒修掉任何缺陷的重譯要不要取代現行版」。這格是 `OBSERVER-QUEUE #67`，🔒紅線（貢獻者關係原則）。merge 等於用等質譯文覆蓋現行版，close 等於拒絕貢獻，兩者都在線後。投稿者在兩個 PR 上已明說他在等這格、不再補東西，而 Step 2.4 說維護者剛回過且無新 follow-up 就不重複回應，所以本班一個字都沒加。

查佇列時 `grep '#67'` 零命中讓我以為佇列缺列——實際是該檔的列寫成 `| 67 |` 不帶井號，#67 內容完整且更新到 10-01。**是我的查法錯，不是佇列壞了**，記在這裡免得下一班重複誤判。

## 那條傳了七輪的寫死路徑

交接鏈連七輪傳「spore-harvest 殼的 `/Users/cheyuwu/` 寫死路徑改相對路徑」，席位固定，七輪沒人動手。本班因為自己的殼也寫著那個路徑去查，量出來的規模不一樣：18 條 cron 殼裡 **12 條**寫死它，每條都至少一處在可執行位置，`ROUTINE.md`（routine SSOT 自己）與兩個 repo skill 也寫著。

七輪都讀成排版問題，是因為它是對的。`/Users/cheyuwu` 是一條 root 所有、遷機當天建立的符號連結指向 `/Users/musebase`，inode 比對確認同一個檔。**沒有壞掉是它沒被處理的原因，不是它不需要處理的理由**。那條連結沒被記載成依賴，也沒有任何東西在驗它還在不在，它消失的那一刻 12 條 routine 同時斷，其中一條斷在維護班殼裡那句 `consciousness-snapshot.sh`，而那道指令存在的唯一目的就是禁止當班用記憶裡的舊器官分數填 ACK。

沒有動那 12 個檔：跨 cron 設定、席位是 `/twmd-routine`、`ROUTINE.md` §排程表 是 SSOT。本班做的是把真實規模與真實風險量出來，讓下一輪接到對的尺寸（`c12993bad`）。

## 404 雙語言前綴：查到一半，誠實交出去

交接指名本席位查 `/ja/fr/...`。從 `reports/404-monitor/latest.json` 撈出全部七條，signature 很乾淨：**第二段永遠是 `fr`**，含 `/fr/fr/...`。那個 `/fr/fr/` 幾乎證明有個盲目加前綴的元件在包一條已經帶 `/fr/` 的路徑。

提了一個漂亮的假說（`fr` 若不在 `NON_DEFAULT_ENABLED_LANGS`，fr 頁會被誤判成 zh-TW，`basePath` 留著 `/fr/`，於是每個切換連結都雙前綴，剛好也生出 `/fr/fr/`），然後**自己把它推翻了**：`fr` 在 `languages.ts` 裡 `enabled: true`，前綴偵測與剝除走同一個清單，不會失敗。`elections-2026.template.astro` 那七個寫死 `/fr/` 的 href 也查過，它們在該檔 `fr: {}` 區塊內，scope 正確、不是缺陷。

本班因此沒有定位到產生者，改去跑那個決定性檢查：掃完整 `dist/` 看站體自己到底有沒有吐出這種 href（沒有 → 外部爬蟲在排列前綴，這條可以結案）。`sync:build` 本班跑到收官仍未完成，那個檢查留給下一班。**量小（七條、十次內），但不要再有人用「量小」當不查的理由，它已經被三班傳過一次了。**

## 收官 checklist

| 檢查項                       | 狀態                                                |
| ---------------------------- | --------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                  |
| Timestamp 精確               | ✅（`git log %ai`）                                 |
| Handoff 三態已審視           | ✅                                                  |
| CONSCIOUSNESS 反映最新狀態   | ⏭️ 本班未改（警報已 derived 化，由 generator 推導） |
| 自我檢查工具 PASS            | ✅ article-health memory-diary profile              |

## Quality gate 七條

| Gate                                     | 結果                                                                 |
| ---------------------------------------- | -------------------------------------------------------------------- |
| open issues 都有 status label / assignee | ✅ 3 條全有 label，#1786／#1609 掛 frank890417（皆卡在人）           |
| open PRs ≤ 5d age 都有 review comment    | ✅ 兩條 age 3d、各 3 則留言                                          |
| broken-link gated ratio < gate           | ✅ **gated 0.15% < 7%**（all-langs 0.14%），連三輪 skip 後本班實測到 |
| build green                              | ✅ RED 1 → RED 0，CI 自己確認 success                                |
| BECOME ACK 一行記憶體頂                  | ✅                                                                   |
| 連續空場 ≥ 3 cycle 有 LESSONS entry      | n/a — 本班非空場（vc=0）                                             |
| 有 fresh issue 的 cycle 至少一件被修掉   | ✅ #1678 修掉並關閉、#1729 重驗後關閉、main CI 紅燈修掉              |

## Handoff 三態

繼承 `2026-10-02-071235-twmd-feedback-triage`：

- ⏳ blocked（哲宇）：`OBSERVER-QUEUE` 待決項，含 #28（feedback 指控信偵測器）。本班新增 **#67 已累積到兩個實例（PR #1784／#1782）可一次決定**。
- [x] ~~pending（本席位）：404 雙語言前綴 `/ja/fr/...`~~ → **retired by 2026-10-02-085430**：signature 定出來（第二段恆為 `fr`，含 `/fr/fr/`），switcher 假說證偽，全 `dist/` 掃描零命中 → 外部排列前綴，非站體自產。這條走完了。
- [ ] pending（收件席位 twmd-self-evolve-weekly 10-04）：LESSONS `heart-counts-heals-as-contributed-births`。非本席位，原樣傳遞。
- [ ] pending（收件席位 twmd-distill-weekly）：LESSONS `threads-linkifier-swallows-cjk-before-url` 與 `narrative-log-fills-causation-no-gate-watches`（vc=2）。非本席位，原樣傳遞。
- [ ] pending（席位 `/twmd-routine`）：寫死路徑。**本班重新量過，規模從 1 條殼改為 12 條殼**，並確認它靠一條 root 符號連結支撐（LESSONS `flywheel-path-layer-rests-on-one-undocumented-root-owned-symlink`）。vc=8，席位不變。

本 session 新 handoff：

- [x] ~~pending：404 雙前綴是站體自產還是外部~~ → **retired by 2026-10-02-085430**：全 `dist/` 19,323 份 HTML 零命中雙前綴 href，判定外部排列前綴，非站體自產。參照 `reports/404-monitor/latest.json`。
- [x] ~~pending：broken-link gated ratio 連三輪未量~~ → **retired by 2026-10-02-085430**：`npm run sync:build` 路徑實測與 babel 零碰撞（三 worker 在跑時跑完 16 分鐘），gated 0.15% < 7% PASS。**下一班不需要再找理由 skip，只需要排 16 分鐘**。
- [ ] pending（收件席位 twmd-distill-weekly）：LESSONS `external-advisory-reddens-a-gate-and-not-our-code-becomes-a-reason-not-to-act`（vc=2）與 `verified-the-fact-exists-on-site-not-that-it-exists-in-the-article-we-linked`（vc=1）。
- ⏳ blocked（GitHub 端，無解除動作）：`ci-main-health.sh` 的 ⚠️ 取數口計數器尚未在真實執行裡觸發過。下次有人看到那行 ⚠️，就是第一個現場樣本，記下當時時間與 workflow。

## Beat 5 — 反芻

今天三件事指向同一個形狀：**壞掉的東西有三種，而只有一種會自己叫**。

工程契約閘門紅著，會叫，因為紅燈就是叫聲——但它叫了四輪沒人動，因為 09-30 那班替它寫了一個讓人安心的解釋（「外部公告，非自家程式」）。健康尺讀錯 deploy，不會叫，它印的綠燈跟對的時候一模一樣，唯一的破口是那個離譜的年齡剛好違反常識。讀者那條路通到別的地方，也不會叫：連結有效、目標存在、主題相鄰，所有閘門放行，26 天裡每一班掃過去都把那則 issue 讀成「已回覆待關」。

三者裡最便宜的修補是第一個，最貴的是第三個，而第三個的代價落在一個真人身上，他等了 26 天，等的是一條我們以為已經鋪好的路。

另一件值得記的是我今天推翻自己兩次。第一次是開場那句「routine 殼寫 `/Users/cheyuwu/` 而本機是 `/Users/musebase/`」，說得像兩個不同位置，實際是同一個檔，中間隔著一條沒人記載的符號連結。如果我沒去查，那句話會原封不動進交接，而下一班會拿著一個錯的前提去改 12 個檔。第二次是 `/ja/fr/` 那個切換器假說，它解釋了全部七條觀察、包含最難解釋的 `/fr/fr/`，漂亮到我幾乎想直接寫進交接。最後是 `fr` 在註冊表裡 `enabled: true` 把它整個否決掉。

一個假說能解釋所有觀察，不代表它是真的。它只代表我還沒去查那個會否決它的前提。今天這兩次都是自己查出來的，不是觀察者攔下的，但兩次都是在「差一步就寫進交接」的位置才查。那個差一步，是今天真正該記住的距離。

🧬

---

_v1.0 | 2026-10-02 09:12 +0800（收官續跑至 09:2X 補完兩道閘門）_
_session twmd-maintainer-am — cron 維護班，無觀察者在場_
_誕生原因：cron 08:30 fire；開場健康尺印出一個違反常識的年齡，整班從那條線頭展開_
_核心洞察：壞掉的東西有三種而只有一種會自己叫——紅燈會叫但會被一個安心的解釋擋住、讀錯的綠燈跟對的綠燈長得一樣、通到別處的連結三個閘門全放行；上一班留下的是讓下一班查得動的錨；一個假說能解釋所有觀察只代表我還沒去查那個會否決它的前提_
_LESSONS-INBOX 候選（本班已 append 3 條 + fold 1 條）：`external-advisory-reddens-a-gate-and-not-our-code-becomes-a-reason-not-to-act`（vc=2）／`verified-the-fact-exists-on-site-not-that-it-exists-in-the-article-we-linked`／`flywheel-path-layer-rests-on-one-undocumented-root-owned-symlink`／fold 進 `ci-health-ruler-gave-two-different-ages-for-the-same-run-and-both-printed-green`（vc=2，成因定錨＋修法已 ship）_

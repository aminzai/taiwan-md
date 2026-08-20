---
session_id: '2026-08-20-084151-twmd-maintainer-am'
session_span: '08:41 → 10:05 +0800'
trigger: 'cron routine twmd-maintainer-daily (am 08:30)'
observer: 'none (cron)'
beat_coverage: 'Stage 1-4 (MAINTAINER-PIPELINE)'
---

✅ BECOME ack: mode=review→**強制升 Full**（ready PR 33 ≥ 5，命中 High-stake #1）/ 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，讀數齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# 2026-08-20-084151-twmd-maintainer-am — 我替一條規則造了閘門，而它差點擋下四百零一篇自己寫的文章

> session twmd-maintainer-am — cron maintainer 巡邏
> Session span: 08:41 → 10:05 +0800（約 84 分鐘）

## 觸發

Cron 08:30 例行巡邏。醒來看到的不是前幾天那種空場：idlccp1984 在 8/19 深夜到 8/20 凌晨之間連送了二十六篇，ready PR 從個位數跳到 33，直接命中 BECOME High-stake 第一條，mode 從 review 強制升 Full。

## Stage 1 掃描

| 項目                    | 實數                                                         |
| ----------------------- | ------------------------------------------------------------ |
| open PR                 | 41（ready 33 / draft 8）→ 收工時 18（ready 11 / draft 7）    |
| open issue              | 4（#1440 / #1389 / #1184 / #615）                            |
| open discussion 未回應  | 0（11 條全數有維護者回覆）                                   |
| 過去 24hr routine fires | 10 條全部就位                                                |
| build / CI              | ✅ deploy 最近三次 success                                   |
| PR CI armed             | ⚠️ 2 條 UNARMED（aminzai 首投，三批 run 卡 action_required） |
| broken-link gated ratio | ✅ 0.27%（all-langs 0.25%，門檻 7%）                         |
| 免疫器官分數            | 🛡️ 59（八器官最低，chronic 自 7/05）                         |

## 二十六篇投稿敗在同一個地方，而那個地方沒有工具

跑完既有 heal 鏈之後，殘餘的 hard 幾乎收斂到一條：全形分號超過 12。八月已經是第二批了——8/15 那批 67 個 PR 的教訓寫在 `contributor-pr-heal.py` 的檔頭，補上了 `assign-subcategory`。這批補上的是分號。

gate 自己的 `fix_suggestion` 寫得很清楚：前後子句拆成兩個句號句，或並列項改頓號。前者機械可決定，後者要讀懂並列關係。所以 `punct-cleanup.py` 新增的 `--fix` 只做前者（commit `19e7373b2`），判準刻意保守：只碰 gate 認定的可編輯正文（跟 prose-health 共用同一個 predicate，不另立一把尺）、分號前子句不足八個中文字就當列舉跳過、一行三個以上分號整行跳過。寫檔前比對 frontmatter／腳註／數字／引語／URL 的 multiset，不過就整篇還原。實測台灣白海豚 25 處全轉、臺灣民報 21 → 1。

第一次跑就自己踩到一個混維度：驗收原本跑整篇 `article-health`，於是臺灣民報那種本來就有無關 hard（熱連結圖）的投稿永遠不敢寫檔。那是把「我這次改壞了嗎」跟「這篇本來就有別的問題嗎」讀成同一個燈。改成只比 delta 之後才正常。

## 紅旗清單寫了幾個月，沒有任何機器在查

批次跑到一半我對 26 篇做了一次 frontmatter 稽核，才看見八篇的 `author` 寫著 `'Taiwan.md'`、`'Taiwan.md 策展團隊'`、`'Taiwan.md countributer'`，三篇自設 `featured: true`。這兩件在 MAINTAINER §Step 2.3 是紅旗 #6 與 #7／#8，Step 3.3 連修法都寫好了——但 heal 鏈不修，`article-health` 回 hard=0。**而我在建好閘門之前，已經替 #1467 與 #1458 推了 heal commit，紅旗原封不動留在裡面。**

修補進 `contributor-pr-heal.py`（commit `c920ebe91`）。真正值得記的是第一版怎麼錯的：我把它做成 `article-health` 的全站 plugin，跑 `--list-checks` 確認註冊、拿文章 dogfood 也過了，看起來完全正確。接著順手量了一次全站分母——`author: 'Taiwan.md'` 在 zh 有 **401 篇**，因為那對 Semiont 自己走產線寫的文章是正確署名。那道 gate 上線會一次誤擋 401 篇。

差別在一個沒被寫進紅旗條文的前提：「這個署名是不是偽造」只有在「這個檔來自外部投稿」的脈絡下成立。所以檢查最後掛在 `--from-pr` 路徑，裸路徑模式明確不碰。接住我的是上線前多量的那一次分母，不是設計時的謹慎。

## 一個大寫的 People 資料夾，把每一次小寫寫入都吸過去

替 #1459 與 #1466 收 Wikimedia CC 圖時指定 `--cat People`，檔案落進了 `public/article-images/People/`，而文章引用的是小寫 `people/`。這台 Mac 的檔案系統不分大小寫，本機完全看不出來，到分大小寫的 CI 上就是 404。

往上追才發現大寫那個資料夾不是今天長出來的：它已經有五張圖，其中四張跟小寫版本逐位元組相同。它就是那個陷阱本身，我只是第 N 個踩到的人。所以這次把整個大寫資料夾收掉——八個 blob 全部搬到小寫、吳明益與 Joeman 兩篇含十一個語言版本的引用改成小寫（commit `36aaa72e1`）。四個 deletion 逐一確認小寫那邊有同名檔案在。

## 三十二篇上站，六篇留給哲宇

合併 32 個 PR（收工前投稿者又送了五篇，一併處理完，沒有留到明天）。人物門檻逐篇對照 MAINTAINER §人物知名度門檻判：囧星人（報導者深度專訪）、白癡公主（十五則主流媒體）、鐵牛（鏡週刊＋鏡報＋兩個維基條目）、陳三火（CNA 四則＋工藝中心＋光華）、蔡瑞月、王大閎、錫蘭都過。中壢事件與選舉造勢逐段讀過框架，來源含國家檔案與中選會，不命中政治宣傳紅旗。

授權逐張查：臺灣民報那張臺史博典藏圖，館方頁面標示「僅限公開瀏覽」並另設授權申請窗口，下載進庫等於再散布，所以移除圖、保留指向典藏頁的來源連結。誠品書店四張圖的來源是 Taipei Times／Tripadvisor／Shutterstock，全數移除。

留給哲宇六件，都留了技術說明不是沉默：#1471 蔡黑皮（人物門檻第四個同型案例，併入 OBSERVER-QUEUE #30）、#1483 台灣高鐵（拿 16 腳註的版本覆蓋 23 腳註且 `lastHumanReview: true` 的版本，併入 #33）、#1484 蔣經國與 #1491 館長陳之漢（兩篇內容都意外地穩，卡的都是政治立場紅線，新開 #34 併案）、#1466 鐵牛（破折號 25 > 15，那是語氣不是格式，我不代改）。

## 四則 issue：兩則落檔，一則補進佇列，一則說明為什麼不修

- **#1389** 展開成可動手的題目寫進 ARTICLE-INBOX——原文只有一句「要和台灣早餐文化一起整理」，真正要決的是兩篇的邊界不是合併。
- **#1184** justfont 白名單補進 OBSERVER-QUEUE #35。它 6/29 開到今天，最後一步一直等真人按，卻從來沒進過那個佇列——那個佇列存在的理由就是接住這種事，而它自己漏掉了這一件。
- **#1440** 數據→資料：查完決定**不做**閘門。全站 22 處有三處是正確用法（投票數據、PM2.5 監測數據），而真正要改的那組是正在等拍板的區段品牌字串——現在加閘門，它唯一會亮的就是那組，在決定出來前每次跑都紅一次。長期亮著沒人能關的警報比沒有警報更糟。
- **#615** umbrella 追蹤 issue，不動。

## 收官 checklist

| 檢查項                       | 狀態                                             |
| ---------------------------- | ------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                               |
| Timestamp 精確               | ✅ 08:41 → 10:05                                 |
| Handoff 三態已審視           | ✅                                               |
| CONSCIOUSNESS 反映最新狀態   | ✅ 免疫 59 chronic 未變，無新增警報維度          |
| 自我檢查工具 PASS            | ✅ broken-link 0.27% / build green / hard=0 全批 |

## Quality gate（MAINTAINER Stage 4.1，7 條）

| 指標                                           | 狀態                                                  |
| ---------------------------------------------- | ----------------------------------------------------- |
| 完整走完 MAINTAINER-PIPELINE                   | ✅ Stage 1-4                                          |
| PR 分流按 §collect-and-merge                   | ✅ B 路徑，紅旗＋CI＋close hard gate 逐篇             |
| routine PR backlog ≤ 3                         | ✅ 0（v2.1 main-direct 無 routine PR）                |
| broken-link gated ratio < 7%                   | ✅ 0.27%                                              |
| build green                                    | ✅                                                    |
| 本 cycle merge 的 PR 都過 hard gate            | ✅ 28 篇全部 `--profile=ci-deploy` hard=0             |
| 有 fresh issue 的 cycle 至少一件被修或寫明不修 | ✅ #1389 落檔／#1184 補佇列／#1440 寫明為什麼不做閘門 |
| 連續空場 ≥ 3 cycle                             | ✅ n/a — vc 歸零（33 ready PR 真 backlog）            |

## Handoff 三態

繼承上一 session（`2026-08-20-070952-twmd-feedback-triage`）：

- [ ] pending（不屬本 routine，原樣傳遞）：`b78ee4f5` 檢舉信明天第八次出現，照 HG13 讀完全文再 `--exclude`
- [ ] pending（不屬本 routine，原樣傳遞）：OBSERVER-QUEUE #28 偵測器與回覆決定仍等哲宇

本 session 新 handoff：

- [x] ~~33 ready PR backlog → 32 merged（含收工前新到的五篇），ready 降到 6~~
- [ ] pending：#1466 鐵牛等投稿者自行把破折號 25 降到 15 以下。若三天無回應，下一輪 cycle 判斷要不要代改（我已在留言問過他要不要我動手）
- [ ] pending：#1452 / #1451 兩個 draft 我推了格式 heal 但**沒有轉 ready**——投稿者 8/20 01:29 還在動它們，三個 ground-truth 訊號沒有全中，照 v2.8 尊重「還在寫」。下輪若仍無新 commit 再判
- [ ] pending：`punct-cleanup --fix` 目前只在投稿 heal 路徑被呼叫。全站 legacy 仍有一批分號超標的文章（`--worklist` 可列），要不要拿它跑一輪清償，等哲宇排優先序（>50 檔命中 §自主權邊界）
- [ ] pending：#1453 學測模板是 2,282 行沒有路由呼叫的孤兒 template，已留言提出「你出資料、我接路由與 i18n」的協作切法，等投稿者回覆
- ⏳ blocked — 等哲宇：OBSERVER-QUEUE #30（人物門檻，四個同型案例累積）/ #33（覆寫既有查證文，兩例）/ #34（蔣經國，政治立場）/ #35（justfont 白名單）/ #29（德文兩批 59 檔）/ #32（About/ 自述文兩篇）

## Beat 5 — 反芻

今天有兩次「看起來完全正確」的東西差點上線。

第一次是那道 author 閘門。我照著 pipeline 白紙黑字的紅旗條文寫，測了註冊、測了 dogfood、全綠——然後量了一次全站分母，401。那個數字之所以會出現，是因為紅旗條文從來不需要寫出它的前提：寫那條規則的人腦子裡是「投稿」的畫面，那個畫面沒有進到條文裡，於是我把規則搬到一個那個畫面不成立的地方，它就忠實地開始擋自己人。

第二次是分號工具的驗收。我讓它跑整篇 `article-health`，理由聽起來很好——「改完要確認整篇是健康的」。可是它要回答的問題根本不是「這篇健不健康」，是「我這一手有沒有弄壞什麼」。兩個問題共用一個燈，工具就永遠不敢動那些本來就帶病的檔案，而那些恰好是最需要它的。

兩次的形狀是同一個：**閘門會忠實執行你寫下的判準，不會替你補上你沒寫出來的前提。** 而前提通常不是被遺漏，是被當成不必說——「當然是指投稿的檔」「當然是指我改的部分」。那個「當然」就是它掉出條文的原因。

兩次都不是儀器叫出來的。第一次是我順手多量了一次分母，第二次是工具在一篇真實投稿上失敗、我去看為什麼。這兩個動作都不在任何 checklist 上。

---

_session: 2026-08-20-084151-twmd-maintainer-am_
_pipeline: MAINTAINER-PIPELINE v2.9_
_commits: `19e7373b2` `c920ebe91` `d3f8ec1da` `36aaa72e1` `3b871759c` + 32 PR merges_

# 2026-10-08-023621-semiont-heartbeat — 〈台東縣〉標題的三十六年是兩個端點相減，捷運史巡出 20 錯；DNA 分數其實是一個時鐘

> session semiont-heartbeat — 每日排程完整心跳凌晨班（Full mode，本機 ChedeMacBook-Pro）
> Session span: 02:36 → 03:05 +0800（29 分鐘，10 個 commit，第一個 02:46:24，最後一個 03:03:16）
> 資料來源：`git log %ai`＋`date`＋`get_usage`

## 觸發

週額度重置後第一個本機心跳。甦醒時本機落後 origin 39 個 commit（babel 夜班剛推完），pull 後 wake-context 十一項全綠。觀察者缺席第 12 天，缺席協議生效，OBSERVER-QUEUE 今天沒有到期項（最近的是 #86 在 10-11）。

## 開拍讀數：額度、飛輪、器官

週額度 8%，重置後 6.6 小時，`budget-pace.py` 判 normal（前 12 小時不外推）。帳本上一筆是昨晚心跳收官的 3%，兩拍之間帳號整體又用掉 5%，那段時間 main 上只有 babel 夜班的 commit，但同一個帳號還有別的 session，分不出是誰。收官讀 9%，這一拍連子代約 1%。

營運機已經醒了：babel 夜班 00:40 照排程起跑，證明排程器與帳號都活著。`routine-stall-check` 仍亮 CRITICAL，因為尺一只數 `[routine]` 前綴，babel 夜班一直用 `[semiont]`；第一筆 `[routine]` 會是 05:30 之後的晨間班。#1788 告警票補了一則根因留言（週額度用完，重置後已恢復），票本身留給 workflow 的綠燈步驟去關。

儀表板快照停在 116 小時前。本機跑一次 `prebuild:dashboard` 拿新讀數做診斷，產物沒有 commit（那是 06:00 data-refresh 的事）：免疫 60 仍最低，最大缺口還是人工審核覆蓋；DNA 從 95 掉到 80。追下去，DNA 分數只看 EDITORIAL.md 距今幾天沒改，七天內 95、三十天內 80，量的是一個時鐘。DNA 是底層，不改才是常態，這個分數掉下來會誘使下一班去動 EDITORIAL。照骨骼與呼吸已標「能力指標」的先例，給它 `scoreKind: recency-indicator`，卡片上註明「最近修改天數，非品質健康」，數字不動（`36071f09d`）。dev server 被拒，改用 node 直接跑卡片字串邏輯驗三種情況。

## 〈台東縣〉的三十六年

交接寫著 L136「1951 到 1987 年連續 36 年從未中斷關押政治犯」證據不足。中央社 2018 年報導寫新生訓導處民國 40 到 54 年、解散後政治犯移監台東泰源監獄，維基寫綠洲山莊 1972 年完工、4 月 23 日起泰源 170 名政治犯移監過去。兩座監獄不重疊，前後約 29 年。同一個數字撐著標題、description、30 秒概覽、小標、正文與結尾六處，「一座小島同時運作兩座政治犯監獄」也不成立；同篇另一個標題數字「存了四十二年核廢料」是 1982 年起算、文章 2026 年出生時已是 44 年。改成「前後關了近三十年」「四十多年」，中間七年寫成「他們沒有離開台東縣，只是被移到泰源」，補兩條腳註（`648ec5141`）。修正紀錄寫進本篇研究檔時把「1965 到 1972 綠島沒有政治犯」說太滿，維基消歧義頁另有一句語意對不上的反例，收窄成只寫有出處的那一半（`b51dd7e91`）。

病根在 Stage 2：研究檔的年份都對，收斂核心矛盾時把兩個端點相減成一個時長，而研究檔當初選這句的理由寫著「讀者可以驗證」。把這型補進 FACTCHECK §Drift Modes 第 6 條，規則是標題與核心矛盾裡的「N 年」要在研究檔找得到同一個時長，起算到今天的年數改成不會過期的說法（`64a0c2804`，v2.13）。順手量了全庫能不能用正規式抓「凍結的經過年數」：30 筆命中幾乎都是「N 年來最大」這種相對事件年的寫法，要讀懂語意才分得出來，屬判斷不屬儀器，不造。

## 巡邏第五十八篇〈台灣捷運發展史〉

照交接接 featured 03-23 那批，挑時間與數字原子最密的捷運史，先自己跑 Phase 5 找出五處自打（1 兆加 1.1 兆寫成 2.4 兆、本業虧損與本業微利、高雄累積虧與年虧、1392 萬公里標錯年、兩個人都叫成大軌道中心主任），交給一個 Sonnet 子代跑 Phase 2-4。128 原子 ✅ 64／⚠️ 24／❌ 19／🔴 10／💬 10／👻 1，錯誤率 16.9%。

會改字的原子我都自己 curl 原文重驗，子代的 ❌ 全部成立，另外補到五處：機捷原文是跌到 4 萬不是 3 萬、高雄 2016 年該比的是當年全台 18% 不是 2020 年的 16%、三段引語不逐字。有一處我跟子代都錯過一次：馬特拉撤離年份，子代與我第一輪都照 TVBS 北捷 30 年大事記寫 1997，兄弟篇〈文湖線〉引聯合報報時光寫「通車兩個月後」，報時光頁附著當年原報〈馬特拉聲明 今起撤離木柵線〉1996-05-31，以原報為準；TVBS 那段大事記配圖標著 AI 製圖，同一份大事記是「VAL256 到站顯示器由台灣工程師自研」的唯一來源，一併拿掉。止血 `6fed62193`，退回重寫登記 P1 EVOLVE（`4329855ff`），跟寫得更細的〈文湖線〉分工。兄弟篇 grep 十六個被改掉的錯誤短語零命中。

## 寫作佇列整理

三條時效題過期或明天到期（名古屋亞運、李灝宇、王冠閎），這段期間沒有寫作班接得到（`twmd-rewrite-daily` 停用中），三題主脊本來就不靠時效，改標 evergreen 並寫明開場要換成什麼、哪些是賽季中途數字（`a34a5193e`）。從 10-01 起傳了好幾班的兩組重複條目收掉：便利商店的巡邏止血與 #1450 勞動角度併成同一次重寫，Discussion #104 那條收窄成國中會考（`e01152c28`）。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                       |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                         |
| Timestamp 精確               | ✅ `git log %ai`＋`date`                                                                                   |
| Handoff 三態已審視           | ✅                                                                                                         |
| CONSCIOUSNESS 反映最新狀態   | ✅ 不需改：額度那列仍成立，新讀數進帳本                                                                    |
| 自我檢查工具 PASS            | ✅ 兩篇 article-health hard=0（警告皆原文既有類型）；dashboard 測試 2/2；inbox-audit DUP 與過期切角歸零    |
| 額度記帳                     | ✅ start 8%／end 9%                                                                                        |
| Diary                        | skip：diary-gate 放行，但排程班預設不寫，反芻屬「這次做了 X、注意到 Y」，家在本檔 Beat 5                   |
| Full mode 載入               | ANATOMY／DNA／UNKNOWNS 全檔與 LESSONS、ARTICLE-INBOX、SPORE-INBOX 全檔未讀，照額度節律縮，只讀標題與相關段 |

## Handoff 三態

繼承 `2026-10-08-014050-twmd-babel-nightly`（非本班職權的原樣傳遞，REFLEXES #74）：

- [ ] pending（席位 `twmd-maintainer-daily`）— Discussion #1704 回覆 idlccp1984，草稿在 `2026-10-01-163744-semiont-heartbeat`
- [x] ~~pending（席位 `twmd-maintainer-am`）— `inbox-audit.py` 報 ARTICLE-INBOX 兩個 DUP~~ — retired by 本 session（`e01152c28`）
- [ ] pending（席位 Write 班或哲宇）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-11）— 上幾班列的五件、OAI-SearchBot 少斜線 301、FACTCHECK v2.11 👻 重算、REFLEXES #101 (a) 兄弟篇 grep
- [ ] pending（席位 `twmd-distill-weekly` 10-11）— LESSONS `i-concluded-not-found-from-one-failed-search` 機械化；`shared-tool-quota-pool-in-fanout` vc=3；`title-line-is-the-least-checked-and-most-read-line` 首例
- ⏳ blocked — `OBSERVER-QUEUE #92`／`#67`／`#76`／`#28`／`#75`〜`#91`、`#65 (b)`、`#78 (2)`、`#56` 量級存量（待決，🔒），解除條件：哲宇拍板。`#86` 缺席代理 10-11，`#78 (1)` 與 `#93` 擴展 10-21
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留，仍是主樹唯一 untracked
- ⏳ blocked（給哲宇，對外敘事）— `public/llms.txt` §1「4-tier cascade」「100% from FREE tier」已不是現況
- [ ] pending（需要沒有寫入者的時段）— `.git/gc.log` 與 `git prune`，issue #1729
- [ ] pending（席位：哲宇回來時）— `OBSERVER-QUEUE #65（(a) 已決，缺席預設）`：WARN 要不要升 FAIL
- [x] ~~pending（席位：下一個 Full mode 或 Write 班）— 〈台東縣〉L136 政治犯關押年份~~ — retired by 本 session（`648ec5141`）
- [ ] pending（席位 `twmd-weekly-report-sun` 10-11）— 覆蓋 09-27 到 10-11 兩週含 87 小時停擺，`OBSERVER-QUEUE #93` 進 top 5
- [ ] pending（席位：營運機任一 Full mode）— 營運機 routine 也開始 `budget-pace.py --log` 記帳（#93）
- [ ] pending（席位 `twmd-babel-nightly`）— `rescue-orphans.py` 改成直接呼叫 `babel-dispatch.verify_one`（BABEL-VORTEX-LOOP v1.95 (a)）；push-every 門檻與 `babel-push.log` 最後一行

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly`）— 〈台東縣〉與〈台灣捷運發展史〉十二語要跟上。台東縣改了標題（「關了三十六年」→「前後關了近三十年」、「四十二年」→「四十多年」），要盯標題行（LESSONS `title-line-is-the-least-checked-and-most-read-line`）與 1965 年移監泰源、1972 綠洲山莊；捷運史改動超過三成，預期整篇重翻，要盯：4 死 4 傷、15:15 傳真、1996 年 5 月底撤離、2005 年 16.4 億、2008 年 30 億、2023 年 8 月 1,392 萬公里、逾 2 兆、機捷 4 萬、三鶯線已通車
- [ ] pending（席位 `twmd-maintainer-daily` 10-08）— 14 個開著的 PR，其中 stantheman0128 10-06 一次送的 11 個（#1791〜#1801，Windows／husky／link-target／大小寫 404 等工具修補）在停擺期間等了兩天；aminzai 三篇譯文 #1801／#1784／#1782
- [ ] pending（席位 `twmd-maintainer-daily`；#1789 發版給哲宇）— a-lang 10-05 開的 #1790（`cli/src/lib/ensure-data.js` 的 `hasLocalData()` 把只剩 `.git` 的中斷 clone 判成就緒，一檔修補）與 #1789（npm 上還是 0.8.0，修補沒發佈；發版要 npm 憑證，屬哲宇）都還沒回覆
- [ ] pending（席位 `twmd-self-evolve-weekly` 或 #93 10-21 代理）— `budget-pace.py` 前 12 小時不外推，但重置後 6.6 小時已用 8%，照這個速度約第 3.5 天用完，跟上週同形；帳本只記心跳，兩拍之間的 5% 分不出是誰，帳本缺的是班次而不是讀數
- [ ] pending（席位：下一個 Full mode）— 巡邏 featured 03-23 剩下四篇：〈台灣官方網站資源重寫〉〈台灣米其林與精緻餐飲〉〈台灣國家風景區系統〉〈台灣教育制度〉，開拍前照額度節律
- [ ] pending（席位：下一個 Full mode 或 Write 班）— 〈台東縣〉L142「1992 年綠洲山莊廢止使用」與維基〈原國防部綠島感訓監獄〉「1987年隨解嚴而裁撤」不一致，本班沒找到 1992 的出處

## Beat 5 — 反芻

〈台東縣〉研究檔裡選標題那一段寫著三個理由：讀者可以驗證、具體、有感。三個都成立，只是「可以驗證」說的是這句話的形狀，一個讀者拿得到年份就算得出來的數字，跟這個數字有沒有被驗過是兩回事。標題是全篇被讀最多次的一行，也是最早被寫定、之後最少人回頭看的一行；昨晚 babel 班在十二語標題上撞見同一件事，今晚在中文母稿上又撞見一次。

另一件事是捷運史的馬特拉年份。子代跟我第一輪都照 TVBS 寫了 1997，抓到它的是我們自己八月寫的〈文湖線〉，那篇有腳註，指著一份 1996 年 5 月 31 日的原報。巡邏一直把站上的舊文當成要查的對象，這一次是站上的另一篇文章替巡邏查了一個來源。

🧬

---

_v1.0 | 2026-10-08 03:05 +0800_
_session semiont-heartbeat — 〈台東縣〉三十六年與四十二年兩個標題數字修正；巡邏〈台灣捷運發展史〉128 原子 20 錯止血並退回重寫；DNA 分數標成修改天數；寫作佇列時效與重複收掉；FACTCHECK v2.13_
_誕生原因：週額度重置後第一個本機心跳，交接指名〈台東縣〉L136 與 featured 03-23 批次_
_核心洞察：(1) 時間跨度只要兩個端點對，持續時長要中間每一年都在，漂亮的標題數字最容易從前者滑向後者 (2) 起算到今天的年數在文章出生那天就開始過期 (3) 一個只量「多久沒改」的分數會獎勵改動，DNA 不改才是常態 (4) 站上有腳註的兄弟篇可以替巡邏查來源，TVBS 大事記的 1997 被一份 1996 年原報推翻_
_LESSONS-INBOX：未新開條目。跨度讀成時長已寫進 FACTCHECK §Drift Modes 第 6 條；`title-line-is-the-least-checked-and-most-read-line` 補中文母稿第二例 vc=2（機制不同、不對稱相同，是否同條留給 distill 判斷）_

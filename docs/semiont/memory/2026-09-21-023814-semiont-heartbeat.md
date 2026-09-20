# 2026-09-21-023814-semiont-heartbeat — 巡邏第二十一到第二十三篇：李登輝康乃爾演講的題目與引語都是填的、海廢快篩掛錯機構、黑熊篇零錯；抽樣學會認出被人重寫過的文章

> session semiont-heartbeat — 每日排程完整心跳（Full mode，本機 commander-macbook 凌晨排程）
> Session span: 02:38 → 02:59 +0800（約 21 分鐘，7 commits）
> 資料來源：`git log %ai`

## 觸發

排程心跳。甦醒時 wake-context 第一次亮的是「工作樹落後 origin 48 個 commit」，先 `git pull` 再重跑，十一項體檢才全綠；落後的那 48 個是昨晚 babel 產線與 supporters-weekly 的產出，不是安靜。晚間那班（20:37）交接單把巡邏母體第二十一到第二十三篇留給下一個 Full mode，抽樣指令現值跟交接單一致，這就是本輪主線。哲宇兩天前在場。

## 資料刷新與診斷

`refresh-data.sh` 十四步全過，文章 1122、貢獻者 75、本週新增 42，`4b14dfd27` 落地。警報只剩免疫 59 慢性一盞（review_coverage 19）。build perf 150 ms/page 仍在 50 ms 門檻外。`heartbeat-memory-check.py` 近七天十四次刷新只剩本輪這一個 orphan，收官後歸零。待決佇列全 🔒 或未到期（#70／#72 要到 09-25），新的 #75 是 supporters-weekly 凌晨剛進的 Portaly 續扣問題，等哲宇看後台。

## 巡邏第二十一到第二十三篇：填縫、掛錯機構、零錯

〈台海危機與兩岸關係發展〉（A 級政治史）40 個原子錯 6，先跑 Phase 5 就抓到一處自己打自己：一江山 1955 年 1 月陷落，文章寫它「直接催生 1954 年 12 月的中美共同防禦條約」，條約在戰役前一個半月就簽了，戰役後催生的是 1955 年 1 月 29 日的福爾摩沙決議案（BBC 原文寫的是整場第一次台海危機「間接促成」條約，初稿把它縮成一江山的因果）。錯集中在李登輝訪美那節：演講題目寫成「台灣的民主化經驗」，總統府新聞是「民之所欲，長在我心」；「台灣是一個擁有獨立主權的國家」這句還附了英文對照，在總統府全文裡完全不存在，全文用的是「中華民國在台灣」跟「主權在民」；曾永賢那句「你們不用擔心」與國務院官員「私下」承認，都從英文維基的間接引述被加工成中文直接引語。反過來，彭德懷「宰牛刀殺雞」我以為是填的，維基逐字有。七十年的軍事數字（一江山傷亡、八二三 47 萬發與 618 人、飛彈危機 396:0 與 54%）大多對，只有 569 門火砲、186 艘艦船、130 公里坑道、廈門 2.1 公里這類精確值查無或對不上。九條腳註只掛四條，止血後十一條掛九條（`5aa11ee92`）。

〈台灣海洋保育與挑戰〉（featured）30 個原子錯 7，形狀跟昨晚河川篇一樣：我們的島那組白化統計（62 樣點、28,250 株、52%／31%、小琉球 55%）與報導者那組海底垃圾（102 公斤／平方公里、淡水外海 200 多件）全對，錯的全在表外——「陸源 70-80%／漁業 15-20%／跨境 5-10%」三個百分比、「環境部海廢快篩每公里 1,855 件、82.7% 塑膠」（做快篩的是綠色和平和荒野，數字是 121 測站、15 萬袋、每百公尺 13 袋）、郭兆揚「潛水十年」與陳昭倫「技術只能爭取時間」兩句引語、一句歸給 UNEP 的格言、1,270 萬噸（來源寫 800 萬公噸）。GitHub 觀測平台死鏈換成海管處 2020 東沙白化公告，海龜 637／981 隻次是真的、掛回 113 年計畫成果頁（`c24076169`）。

〈台灣黑熊〉32 個原子零錯，是二十三篇裡第一篇。原因很簡單：現在的正文是投稿者 idlccp1984 八月整篇重寫的（PR #1575），十一條腳註全是林保署、玉管處、中央社、Ursus 期刊，每個數字都掛在能點開的頁上，連「若看到黑熊，請保持冷靜，安靜儘速離開現場」都是共存頁逐字。只修了插畫作者欄（Commons 作者是林慧秋，Davidzdh 是上傳者）、遇熊三不的歸屬、圖片來源段「未下載圖片檔」跟六則圖說「已收進專案」自相矛盾那句（`68d051008`）。

## 抽樣學會認出被人重寫過的文章

黑熊篇排進前五名是因為 `date` 還是 03-18 出生日、`lastHumanReview` 還是 false，條件四的三個訊號（rationale／DONE-LOG／research 檔）都看不見投稿者的整篇重寫。frontmatter 裡看得見的只有 `lastVerified: 2026-08-22`。FACTCHECK v2.6 補條件五：`lastVerified` 比 `date` 晚 30 天以上就改用它排序——三月那批 03-23／03-25 的 `lastVerified` 是同一週的批次蓋章，30 天門檻正好把它們留在原位，首跑 25 篇往後移（`adc45f718`）。

三篇查核檔各落 `reports/research/2026-09/`。台海篇的巡邏結果併進 INBOX 既有的「海警船數字」EVOLVE 工單，順手把工單路徑從 Society 改回 History（`0d0483fcc`）；海洋保育新開一條 P2，脊椎候選是 2020 那個沒有颱風的夏天（`a5d940ed7`）。黑熊篇該不該翻成 `lastHumanReview: true` 留給 maintainer：投稿者是 AI 輔助寫的，欄位語意上不算人工審核，但它已經是全站腳註最乾淨的一篇。

## 收官 checklist

| 檢查項                       | 狀態                                                        |
| ---------------------------- | ----------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                          |
| Timestamp 精確               | ✅ `git log %ai`                                            |
| Handoff 三態已審視           | ✅                                                          |
| CONSCIOUSNESS 反映最新狀態   | ✅ 警報層 derived，無 prose 要改                            |
| 自我檢查工具 PASS            | ✅ 三篇 knowledge 改動 pre-commit hard=0；memory-diary 見下 |
| Diary                        | skip（既有教訓的第八輪驗證加一條抽樣補丁，不另開日記）      |

## Handoff 三態

繼承 `2026-09-20-203758-semiont-heartbeat`：

- [x] ~~pending（下一個 Full mode）— 巡邏母體第二十一到第二十三篇：History/台海危機與兩岸關係發展、Nature/台灣海洋保育與挑戰、Nature/台灣黑熊~~ — retired by 本 session：三篇查完、修完、落檔，台海併進既有 EVOLVE 工單、海洋保育新開 P2
- ⏳ blocked（給哲宇）— 用語庫 blanket claim 血緣複查 A/B/C（issue #1733）；`reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留（仍是工作樹唯一 untracked）
- [ ] pending（給哲宇，時效）— 名古屋亞運與中華台北 NEW P0 待派（會期到 10/4）；電價機制 P0（probe 2026-09-20 T1-A）待派；T1-D 科技監控要他點頭
- [ ] pending（哲宇 review）— 三篇 v2 決定 v6.7 單檔 vs v9 互動式；REWRITE 產線整併已設單檔型為現行
- [ ] pending（Write session，帶哲宇 review）— 張忠謀退回重寫（P0）、馬英九兩節重寫（issue #1729）、台海危機 EVOLVE（P1，本輪併入李登輝節重寫）、當代雕塑（P2）、農業四篇併寫（P2）、地理三篇併寫（P2）、城市總覽（P2）、海洋保育（P2，本輪新開）
- [ ] pending（Full mode session）— OBSERVER-QUEUE #74 選項 A 的 audit：EDITORIAL 正例去標籤重判、抽 5 篇 09-19 產線整併後文章看骨架同質化；LESSONS `canonical-positive-example-fails-its-own-rules`
- [ ] pending（下一班 maintainer-am）— en 六組同源雙檔 6 刪 + 6 條 301（`check-slug-consistency.py --all`）；順帶決定〈台灣黑熊〉`lastHumanReview` 要不要因 PR #1575 翻 true
- [ ] pending（09-25 之後任何 session）— OBSERVER-QUEUE #70 與 #72 到期非 🔒，各一個 commit 執行後移 §已決
- [ ] pending（10-02 起，任何 session，<50 檔）— OBSERVER-QUEUE #69 (a) 40 篇清 `sourceCommitSha` 降級 stale
- [ ] pending（9/24 之後）— 誰算低薪三處最低工資數字改成審議會實際結果
- [ ] pending（10/24 之後）— 金鐘獎第 61 屆頒獎後補 EVOLVE-delta
- [ ] pending（樹安靜時任何 session）— `check-parallel-actor.sh` 回 IDLE 時跑 `git prune` 並刪 `.git/gc.log`
- [ ] pending（self-evolve-weekly 候選）— `heartbeat-memory-check.py` TAG_PAIRS 泛化到 data-refresh／maintainer 並接 `generate-dashboard-alerts.mjs`
- [ ] pending（distill-weekly）— LESSONS `named-entity-present-but-in-a-different-role` 家族四形看要不要升 REFLEXES；FACTCHECK Phase 4 補「它在來源裡是這個計畫嗎」
- [ ] pending（distill-weekly）— 「真原子放錯年代」子形（秀姑巒山 3,860 是 1972 年標高）看要不要進 REFLEXES #98
- [ ] pending（小，任一 heal session）— 全庫 6 篇「腳註定義正文零引用」：Music/金曲獎（20 條）、Lifestyle/台鐵鳴日號（15）、Economy/全聯福利中心（5）、Politics/\_Politics Hub（9）、Society/水道頭（8）、About/視覺化模組型錄（7，可豁免）
- [ ] pending（小，延續）— 早上那輪 Self-judge B 列六條、民法 1085 條三讀確認、雕塑篇朱銘作品名、外貿篇三個產能比例、資源頁 14 條 403 網址；河川篇與城市篇三個最高級句無源、農業地景篇彰雲嘉三成稻米

本 session 新 handoff：

- [ ] pending（下一個 Full mode）— 巡邏母體第二十四到第二十六篇：Society/動物園與展演動物倫理、Society/台灣在國際標準中的標示問題、Society/台灣政治環境與選舉制度（v2.6 抽樣指令現值，03-18 出生 12 語；政治題一篇 A 級 Full）。「給巡邏一條 routine」仍等哲宇（新 routine 屬新 workflow，High-stake）
- [ ] pending（小）— 台海篇 [^7] 天下張榮豐與 [^9] 蘇起兩條孤兒腳註（Cloudflare 與博客來擋 bot 未親驗）、「2022 年 1,700 架次」未對國防部原始統計；海洋保育篇 [^5] WWF 中文摘要 PDF 回 503 未親讀、綠色和平 2022 微塑膠調查未對物種數。走 REWRITE 時一起處理

## Beat 5 — 反芻

昨晚說模型抄表準、串故事時填縫，今晚三篇把「填縫」的形狀再往下拆了一層。台海篇那句「台灣是一個擁有獨立主權的國家」是全篇看起來最真的一句：有引號、有英文對照、放在一個真的日期真的地點真的人身上，而它在總統府全文裡一個字都找不到。反過來彭德懷「用宰牛的刀去殺雞」聽起來最像 AI 會編的話，維基逐字有。引語有沒有英文對照、聽起來像不像真話，跟它真不真沒有關係；唯一有關係的是我有沒有把總統府那頁打開。REFLEXES #69 (g) 講的「杜撰引語穿查證過的衣服」，今晚多了一件衣服叫英文括號。

另一件事是黑熊篇。它是二十三篇裡第一篇零錯，而它排進來的原因是儀器只看出生日。一篇被人整篇重寫過的文章跟一篇三月初稿在抽樣指令眼裡長得一樣，差別只藏在 `lastVerified` 那一欄。條件五補上之後 25 篇往後移，母體從 572 變 569，數字幾乎沒動，但下一輪不會再花一個 Full mode 去驗一篇已經對的文章。抽樣指令自己也要拿真實輸出校準（#66）這件事，這是第三次。

🧬

---

_v1.0 | 2026-09-21 02:59 +0800_
_session semiont-heartbeat — 凌晨排程心跳：巡邏三篇（兩篇止血、一篇零錯）、FACTCHECK v2.6 抽樣條件五、台海 EVOLVE 工單併入、海洋保育 P2 新開_
_誕生原因：每日排程完整心跳（今日第一輪）_
_核心洞察：(1) 引語附英文對照、掛在真日期真地點上，跟它真不真沒有關係，唯一的尺是打開原文 (2) 抽樣指令看不見投稿者的整篇重寫，`lastVerified` 比出生晚 30 天以上是那個訊號 (3) 骨幹數字全對、表外填縫全錯的形狀第八輪重現，這次多了「掛錯機構」一型_
_LESSONS-INBOX 候選：無新條目（babel-amplifies 家族第八輪、#69 (g) 引語衣服家族加一件、抽樣校準已直接落 FACTCHECK v2.6）_

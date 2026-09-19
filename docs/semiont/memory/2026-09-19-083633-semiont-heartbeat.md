# 2026-09-19-083633-semiont-heartbeat — 巡邏第六到第八篇八篇八中、看圖一列有了必經的表、查核檔引 hash 的病第二次踩到才儀器化

> session semiont-heartbeat — 每日排程完整心跳（Full mode，本機 commander-macbook 早上排程）
> Session span: 08:36 → 09:00 +0800（約 24 分鐘，6 commits）
> 資料來源：`git log %ai`

## 觸發

排程心跳，甦醒時 wake-context 十一項體檢全綠、工作樹與 origin 同步，哲宇零天前在場。凌晨那輪的交接單把巡邏母體第六到第八篇留給「下一個 Full mode」，抽樣指令現值也剛好是那三篇（國家公園、人權與性別平等、台灣板塊運動與地震活動），這就是本輪主線。

## 資料刷新與診斷

`refresh-data.sh` 十四步全過，文章 1122、貢獻者 75、本週新增 25，`430ecb8a30` 落地。三盞黃燈跟凌晨一樣：免疫 58 慢性、MEMORY 索引 97 列、`routine-live-state.json` 242 小時沒 dump，後兩盞仍是 #68 分岔的投影。早上 08:44 營運機的 maintainer-am 把 aminzai 三個翻譯 PR（#1749-#1751）收進 origin，本機 rebase 上去零衝突，heartbeat 這一側沒碰 PR，職責沒撞。待決佇列全是 🔒，#69 (a) 要到 10-02 才到期。

## 巡邏第六到第八篇：三篇都是三月初稿，三篇都有硬錯

〈國家公園〉16 個原子，四個硬錯有三個是數字，而且三個方向各不相同：直升機吊掛放流寫「一千多尾」，公視逐字是 240 尾，一千是該季司界蘭溪的累計。小標寫黑面琵鷺「全球 1/6 在台灣」，2026 年普查是 4,719/7,746、占六成一，把台灣最重要的度冬地寫小了四倍。「國家公園署規劃 2030 年海洋保護區達 EEZ 10%、約 20 萬平方公里」查無此規劃，20 萬平方公里差不多是台灣 EEZ 全部，改寫成海保署頁面有的「國家公園海域占 81.28%」與 30×30。卓溪黑熊「120 公斤射殺」改百餘公斤、開槍後傷重人道處理。墾丁與東沙兩條死鏈換活鏈。

〈人權與性別平等〉15 個原子，三個硬錯都是「事實存在、掛錯主體或月份」：追討黨產是黨產會不是促轉會，同婚共同收養修法是 2023 年 5 月 16 日不是 1 月，小 E 案違憲的是內政部 2008 年函釋不是衛福部。促轉會官網已下線，換成凌晨在 official-websites 用過的行政院任務移交頁。

〈板塊運動與地震〉14 個原子，兩個硬錯都在 0403 那段：罹難「13 人」停在事發隔天的中途統計，最終是 18 人、1,155 傷。「預警系統 10 秒內完成全台警報發布」實際是第一報低估規模、雙北沒收到警報，一次失誤被寫成一次成功。順手把「20 世紀傷亡最慘重」改成戰後（1935 年新竹台中地震 3,276 人）。三篇修補在 `426c8cbd14`，查核檔各落 `reports/research/2026-09/`，31-34 個譯本靠 zh 雜湊觸發 stale。

兩輪 C 級巡邏加起來六篇六中、十三條硬錯，寫進 LESSONS `babel-amplifies-source-hallucinations` 那條的 vc 段——「給巡邏一條 routine」的價值已經量出來了，不用再抽樣證明。

## 看圖一列有了必經的表

凌晨補的「看圖一列」靠當班記得去開檔案夾。本輪造 `scripts/tools/image-caption-table.py`：每張內文圖一列，印 alt、斜體圖說、能直接 Read 的本地路徑，本地檔缺失退出碼 2。它不做判斷，只保證沒有一張圖被跳過。接進 REWRITE-STAGE-3-VERIFY 與單檔閱讀版 3.6.3，登記 TOOL-INVENTORY Class A（`b29031d380`）。

## 同一個 hash 病，兩輪各踩一次

查核檔開頭寫「audit 前 HEAD」時引的是當班自己的 HEAD，收官 rebase 到 origin 後 hash 被改寫，凌晨跟本輪各多了一個只為改 hash 的 heal commit（`46526e8055`、`f54e508402`）。第二次踩到才把規則寫進 FACTCHECK §月度巡邏：引文章自己的最後一個 commit（`git log -1 -- <article>`），那個早就 push 過、不會動（`0da37205c5`）。

## 收官 checklist

| 檢查項                       | 狀態                                                        |
| ---------------------------- | ----------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                          |
| Timestamp 精確               | ✅ `git log %ai`                                            |
| Handoff 三態已審視           | ✅                                                          |
| CONSCIOUSNESS 反映最新狀態   | ✅ 警報層 derived，無 prose 要改                            |
| 自我檢查工具 PASS            | ✅ 三篇 knowledge 改動 release-pr hard=0；memory-diary 見下 |

## Handoff 三態

繼承 `2026-09-19-024145-semiont-heartbeat`：

- ⏳ blocked（給哲宇，🔒）— OBSERVER-QUEUE #68 分岔合併方向、#67 babel 覆蓋投稿者譯文、#69 韓文漂入；拍板前兩台都別跑 babel 存量。#1711 無新回覆
- ⏳ blocked（給哲宇）— 用語庫 blanket claim 血緣複查 A/B/C；`reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留（仍是工作樹唯一 untracked）
- [ ] pending（給哲宇）— 讀 `reports/probe/2026-09-18.md` 決定亞運與中華台北 P0 派不派（亞運今天開幕）；T1-D 科技監控要他點頭
- [ ] pending（哲宇 review）— 三篇 v2 決定 v6.7 單檔 vs v9 互動式哪條進 canonical
- [x] ~~pending（下一個 Full mode）— 巡邏母體第六到第八篇~~ — retired by 本 session：三篇查完、修完、落檔
- [x] ~~pending（儀器候選）— `image-alt` 升成看圖對照表~~ — retired by 本 session：獨立工具 `image-caption-table.py`，沒動 plugin
- [ ] pending — 合併落地後 MEMORY / DIARY 索引兩邊都 rollup 過；`routine-live-state.json` 與 dashboard-status 的 7 down 合併後自動熄
- [ ] pending — `台灣原住民當代藝術` 十語、馬英九 11 語、張忠謀 12 語、兩輪巡邏六篇約 65 語譯本，全部靠 zh 雜湊觸發 stale；#68 合併後確認排進第一批
- [ ] pending（Write session，帶哲宇 review）— 張忠謀退回 Stage 2 重寫（INBOX P0）、馬英九兩節重寫（#1729 留開）
- [ ] pending（#68 合併後，任何 session，<50 檔）— #69 (a) 40 篇清 `sourceCommitSha` 降級 stale
- [ ] pending（哲宇一句話可撤）— MANIFESTO §我為什麼活著 散步日期 03-11
- [ ] pending — `observer-queue-lint.py` WARN 收兩週數據後決定升不升 HARD；OBSERVER-QUEUE 兩側撞號主鍵、issue 認領步驟進 MAINTAINER、兩台機器 issue 職責進 ROUTINE.md（延續）
- [ ] pending（#1678 生態多樣性）— 等那篇重寫完再關；本輪未再查
- [ ] pending（9/24 之後）— 誰算低薪三處最低工資數字改成審議會實際結果
- [ ] pending（10/24 之後）— 金鐘獎第 61 屆頒獎後補 EVOLVE-delta
- [ ] pending（小）— 夜生活篇三處常識級數字未找源；當代藝術「關渡雙年展每年舉辦」實為雙年

本 session 新 handoff：

- [ ] pending（下一個 Full mode）— 巡邏母體第九到第十一篇：Music/當代原住民創作歌手、About/台灣官方網站資源、Art/台灣當代雕塑發展（抽樣指令現值）。「給巡邏一條 routine」仍等 #68
- [ ] pending（小，各篇 Self-judge B 列）— 國家公園「珊瑚礁覆蓋率 60%」「70% 面積在千米以上」；人權「女性立委比例亞洲前列」「通姦罪女性檢舉率偏高」；板塊「上盤 200／下盤 100 公尺」「80% 人口在西部」，本輪未找源
- [ ] pending（小）— 民法 1085 條刪懲戒權是否已三讀，本輪查無定論，人權篇用「推動中」hedge；確認後改一句

## Beat 5 — 反芻

三篇的數字錯沒有共同方向：一個放大四倍（1,000 對 240）、一個縮小四倍（1/6 對六成）、一個憑空（20 萬平方公里）、一個凍在中途（13 對 18）。凌晨那輪的教訓是「越像查過資料的段落越危險」，本輪多看見一種形狀：三月寫的文章寫前一年四月的地震，罹難數停在事發隔天，錯的不是來源是時間。查核抽原子時「這個數字對應的事件結案了沒」也該是一個問題。

hash 那件事是 REFLEXES #15 的小型 dogfood：凌晨踩一次，寫了 heal commit，沒寫規則；本輪再踩一次，才寫進 canonical。兩次都是同一台機器、同一條 routine、相隔六小時。距離「重複三次就儀器化」還差一次，但 heal commit 只為改一個 hash 這種事，第二次就夠了。

沒開新日記：上一篇 09-13，六天冷卻期剛過，但本輪的觀察是既有教訓的驗證（LESSONS vc 補記、FACTCHECK 一句規則），不是新形狀。

🧬

---

_v1.0 | 2026-09-19 09:00 +0800_
_session semiont-heartbeat — 早上排程心跳：巡邏三篇止血、看圖對照表工具、查核檔 hash 規則_
_誕生原因：每日排程完整心跳（今日第二輪）_
_核心洞察：(1) 數字幻覺沒有方向只有形狀，「看起來像統計」是共同點 (2) 事件進行中寫的段落錯在時間不在來源，查核要問「這個數字的事件結案了沒」(3) 同一個 hash 病相隔六小時踩兩次，第二次才寫規則——heal commit 只為改一個字串的事第二次就該儀器化_
_LESSONS-INBOX 候選：無（babel-amplifies 條目補兩輪規模；hash 規則折進 FACTCHECK canonical）_

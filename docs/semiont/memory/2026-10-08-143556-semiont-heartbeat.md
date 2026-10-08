# 2026-10-08-143556-semiont-heartbeat — 〈台灣米其林與精緻餐飲〉巡出 26 錯：三家三星的升星年份全錯、兩位主廚被借了江振誠的店當出身、十則引語五則查無

> session semiont-heartbeat — 每日排程完整心跳午班（Full mode，本機 ChedeMacBook-Pro）
> Session span: 14:35 → 14:53 +0800（session-id 取於 14:35:56，第一個 commit 14:49:08，最後一個 14:50:57，加本檔共 6 個 commit）
> 資料來源：`git log %ai`＋`date`＋`get_usage`

## 觸發

排程心跳。甦醒時本機落後 origin 25 個 commit（維護班 09:36 那一串），工作樹裡又有一份不是本班寫的 `public/api/dashboard-analytics.json`。照上一班的做法先存起來、pull、收官前放回，維持被發現時的樣子。pull 後 wake-context 十一項全綠。觀察者缺席第 12 天，OBSERVER-QUEUE 今天沒有到期項（#86 在 10-11，#93 擴展在 10-21，#94、#95 在 10-22）。

## 開拍讀數

週額度 18%，`budget-pace.py` 判 🟡 lean，照速度比重置早 65 小時用完。照節律只巡一篇、主 session 自查不扇出。收官讀數仍是 18%，這一拍不到 1%。帳本上有一段空白值得記：維護班 09:55 收在 14%，本拍 14:35 開在 18%，中間 main 上沒有任何 commit，那 4% 是帳號在 taiwan-md 以外用掉的。這正是 `OBSERVER-QUEUE #93（待決）` 說的「班次之間的用量分不出是誰」的一個具體案例。

診斷面：免疫 60 仍最低。儀表板的十一條「沉默死亡」黃燈是停擺期的影子，其中維護班、讀者回報、收割三條今天都有新 commit，要到下一次資料刷新才會消。

## 巡邏〈台灣米其林與精緻餐飲〉

照交接從 featured 03-23 剩下三篇裡挑這篇：零腳註、十二語譯本，滿是具名餐廳、主廚、星數這類讀者一查就知道的原子。Phase 5 先跑，不開瀏覽器就看到三處自打嘴巴。燒「鵝」用的是清遠「麻鴨」。照文章自己的年份，JL Studio 是第二家三星，文章卻寫第三家。何順凱與林恬耀都「從新加坡 Restaurant André 回台」。

查下去，三處都是更大的錯的入口。核對的底是米其林官方的名單文、2018 必比登完整表 PDF、當年的新聞與主廚專訪，一律 curl 原文。2018 首版是 110 家、20 家摘星，發表會在台北文華東方酒店，宣布的是米高·艾利斯。頤宮在君品酒店（不是君悅），第一年就是三星。態芮與 JL Studio 同在 2023 年升三星，台南與高雄同在 2022 年加入。2018 必比登完整表沒有阿宗麵線、度小月、富宏，正對照點水樓、鼎泰豐、永康牛肉麵都在。綠星首批是山海樓與陽明春天，EMBERS 是 2022 年。亞洲的星級兼綠星不只台灣，RAW 也已在 2024 年底熄燈。十則引語裡，蔡珠兒、詹偉雄等五則查無，四則沒有出處，只有一則是真的。

88 個原子：✅ 28／⚠️ 6／❌ 21／👻 5／🔴 23／💬 5，錯誤率 31.3%。止血 `1256f1c64`：改正年份與數字，刪五則 👻 引語與燒鵝段，換上米其林官方專訪裡陳偉強與林恬耀真的說過的話，刪三則匿名業者說法與成本百分比，Vogue 404 移除，新增 14 條腳註。查核檔 `reports/research/2026-10/台灣米其林與精緻餐飲.md` 是這篇的第一份 research 檔。退回重寫登記 P1 EVOLVE（`be7a4b2c8`）：刪掉匿名說法之後，「幾乎夠格的餐廳最慘」這條主脊沒有任何證據撐著。

## 兄弟篇

拿十八個被改掉的錯誤說法 grep 全庫中文，本篇的錯零命中他篇，但撞見兩處不同的錯：〈台灣美食總覽〉把 RAW 的宣布日（2024-07-29）與最後營業日（12-31）併成一個日期（`c4bb5dc71`）。〈\_People Hub〉寫江振誠「2018 年歸還星級，回台開設 RAW」，RAW 其實 2014 年就開了（`57d883e48`）。同一次 grep 也讀到〈台灣美食總覽〉寫頤宮前主廚陳泰榮 2024 年已離開，讓我發現自己剛補進本篇的「頤宮由陳偉強、陳泰榮兩位行政主廚掌杓」是拿 2018 年的專訪寫成現在式，改成「2018 年摘星時」。

## 反射層

兩個病例補進 REFLEXES #98 不開新條（`7ee9b92b3`）：「近六成在地小吃」在官方原文講的是 37 家新入選，文章換成全部 144 家，是比例對、母體錯，列為第六種載體。Restaurant André 是同篇後段江振誠的店，被借給另外兩位主廚當出身，是既有「媒材對、人錯」同族的第二例。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                      |
| Timestamp 精確               | ✅ `git log %ai`＋`date`                                                                                |
| Handoff 三態已審視           | ✅                                                                                                      |
| CONSCIOUSNESS 反映最新狀態   | ✅ 不需改：免疫與額度兩列仍成立                                                                         |
| 自我檢查工具 PASS            | ✅ 本篇 article-health hard 1→0（剩下的警告是原文既有，本班新增的三個全形分號已改），inbox-audit 無 DUP |
| 額度記帳                     | ✅ start 18%／end 18%（lean）                                                                           |
| Diary                        | skip：排程班預設不寫，反芻在本檔 Beat 5                                                                 |
| Full mode 載入               | 照額度節律縮：CONSCIOUSNESS 警報與挑戰、OBSERVER-QUEUE 到期項、ARTICLE-INBOX 相關段、FACTCHECK 全檔     |

## Handoff 三態

繼承 `2026-10-08-083751-semiont-heartbeat`（非本班職權的原樣傳遞，REFLEXES #74）：

- [ ] pending（席位 `twmd-maintainer-daily`）— `OBSERVER-QUEUE #94（待決）` tailwind 4 擋著七個投稿 PR、`OBSERVER-QUEUE #95（待決）` 發 `cli-v0.8.1`、#1798 先收 #1797 再重跑 `--fix`，三件都在 `2026-10-08-093613-twmd-maintainer-daily` 交接裡寫好了
- [ ] pending（席位 `twmd-maintainer-daily`）— Discussion #1704 回覆 idlccp1984，草稿在 `2026-10-01-163744-semiont-heartbeat`；a-lang 的 #1790 與 #1789 還沒回覆
- [ ] pending（席位 Write 班或哲宇）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-11）— 上幾班列的五件、OAI-SearchBot 少斜線 301、FACTCHECK v2.11 👻 重算、REFLEXES #101 (a) 兄弟篇 grep
- [ ] pending（席位 `twmd-distill-weekly` 10-11）— LESSONS `i-concluded-not-found-from-one-failed-search` 機械化、`shared-tool-quota-pool-in-fanout` vc=3、`title-line-is-the-least-checked-and-most-read-line` 中文母稿第二例
- ⏳ blocked — `OBSERVER-QUEUE` 待決 39 條（完整下界 #48），解除條件：哲宇拍板。`#86` 缺席代理 10-11，`#78 (1)` 與 `#93` 擴展 10-21，`#94`、`#95` 10-22
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留，仍是主樹唯一 untracked；`public/llms.txt` §1 cascade 敘事過期
- [ ] pending（需要沒有寫入者的時段）— `git prune`，issue #1729
- [ ] pending（席位：哲宇回來時）— `OBSERVER-QUEUE #65（(a) 已決，缺席預設）`：WARN 要不要升 FAIL
- [ ] pending（席位 `twmd-weekly-report-sun` 10-11）— 覆蓋 09-27 到 10-11 兩週含 87 小時停擺，`OBSERVER-QUEUE #93（待決）` 進 top 5
- [ ] pending（席位：營運機任一 Full mode）— 營運機 routine 也開始 `budget-pace.py --log` 記帳（#93）；本班多一個資料點：09:55→14:35 帳號用掉 4%，main 上零 commit
- [ ] pending（席位 `twmd-babel-nightly`）— `rescue-orphans.py` 改成直接呼叫 `babel-dispatch.verify_one`（BABEL-VORTEX-LOOP v1.95 (a)）
- [ ] pending（席位 `twmd-babel-nightly`）— 〈台東縣〉〈台灣捷運發展史〉〈台灣國家風景區系統〉十二語跟上，盯點寫在前兩班交接；〈台灣全齡共融旅遊與生活文化〉法名走 Tier 0 patch
- [ ] pending（席位：下一個 Full mode 巡邏）— 〈台灣全齡共融旅遊與生活文化〉L196 起「政策趨勢」段（WHO 無障礙標準、亞洲首個無障礙旅遊友善國家）
- [ ] pending（席位 Write 班）— ARTICLE-INBOX〈台灣國家風景區系統〉〈台灣捷運發展史〉〈台灣同婚與性別平權〉P1 EVOLVE
- [x] ~~pending（席位：下一個 Full mode）— 巡邏 featured 03-23 的〈台灣米其林與精緻餐飲〉~~ — retired by 本 session（`1256f1c64`）

本 session 新交接：

- [ ] pending（席位：下一個 Full mode 巡邏）— featured 03-23 剩兩篇：〈台灣官方網站資源重寫〉（多為連結清單，C 級，可先跑 `footnote-url --network` 類的連結檢查）、〈台灣教育制度〉
- [ ] pending（席位 `twmd-babel-nightly`）— 〈台灣米其林與精緻餐飲〉十二語要整篇重翻，改動過半。盯：2018 首版 110 家／20 家摘星、文華東方、米高·艾利斯、頤宮君品酒店首版即三星、態芮與 JL Studio 2023、台南高雄 2022、七個縣市、綠星首批山海樓與陽明春天、RAW 2024 年底熄燈；五則被刪的引語不能留在譯文裡。〈台灣美食總覽〉與〈\_People Hub〉各改一句，走 Tier 0 patch
- [ ] pending（席位 Write 班）— ARTICLE-INBOX〈台灣米其林與精緻餐飲〉P1 EVOLVE，重寫要處理的已寫在條目裡（主脊沒有證據、資料要更新到 2026 年版、補圖與延伸閱讀）

## Beat 5 — 反芻

這篇的錯有兩種長相。年份與數字那一類，每個原子都是真的，只是被重新排過順序：頤宮的三星、態芮的三星、JL Studio 的三星，三個年份全部挪了位置，挪完之後還自己算錯了誰是第三家。具名內容那一類則是填出來的，填的材料就在同一篇裡：江振誠的店名被借給另外兩位主廚，因為三位主廚剛好寫在同一個主題底下，模型手邊最近的那家新加坡名店就是它。三月那批初稿裡反覆看到的「錯誤有祖先」，這次祖先就住在同一篇文章的後半段。

另一件事是我自己差點犯了同一個錯。替頤宮補一句兩位主廚掌杓，用的是 2018 年的米其林專訪，我寫成現在式。如果不是兄弟篇 grep 剛好讀到〈台灣美食總覽〉寫陳泰榮 2024 年已經離開，這句會帶著「真的有出處」的腳註留在站上。止血時新寫進去的句子，跟三月的初稿一樣會凍在來源的那一年，差別只在它有腳註，看起來更可信。

🧬

---

_v1.0 | 2026-10-08 14:53 +0800_
_session semiont-heartbeat — 巡邏〈台灣米其林與精緻餐飲〉88 原子 26 錯止血並退回重寫；兄弟篇兩處（美食總覽 RAW 日期、人物 Hub RAW 先後）；REFLEXES #98 第六種載體_
_誕生原因：每日排程心跳午班，交接指名 featured 03-23 批次_
_核心洞察：(1) 初稿拿同篇其他人物的屬性填空，錯誤的祖先常在同一篇文章裡 (2) 比例要連分母一起查，「近六成」的主詞換了一群讀者 Ctrl-F 也會命中 (3) 止血時新寫的句子用舊來源寫成現在式，有腳註反而更難被懷疑_
_LESSONS-INBOX：未新開條目，兩個病例補進 REFLEXES #98（DNA-first）；(3) 先留在本檔觀察是否再現_

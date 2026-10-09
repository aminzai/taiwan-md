# 2026-10-09-083739-semiont-heartbeat — 週班七條沒死只是還沒輪到，〈台灣眷村菜〉巡出 9 錯，兩條參考資料是編的

> session semiont-heartbeat — 排程心跳（Full mode，額度 🟡 lean：一篇巡邏、主 session 自查不扇出）
> Session span: 08:35 甦醒 → 08:40:45 第一個 commit → 08:58:05 最後一個工作 commit +0800（7 個工作 commit，另加本檔）
> 資料來源：`git log %ai`；額度帳本 start 36% → end 36%

## 觸發

排程心跳，甦醒時本機落後 origin 20 個 commit，主樹還有哲宇〈沈伯洋〉三個沒 commit 的檔，以及一份 08:17 本機重新產生、比 origin 新的 `dashboard-analytics.json`。先把那份 analytics 複製到 scratchpad、還原、快轉、再放回原位，〈沈伯洋〉三檔沒碰。重跑 wake-context 自檢全綠後，開 worktree `.worktrees/20261009-heartbeat-0809` 做事。Full mode 的器官補載照 lean 縮小：CONSCIOUSNESS、HEARTBEAT、FACTCHECK、MEMORY-PIPELINE 全讀，OBSERVER-QUEUE 只核 §待決（39 條，今天沒有到期項），LESSONS／ARTICLE-INBOX／SPORE-INBOX 全檔（合計約 870KB）沒有載入。

## 週班七條是錯過一次觸發，不是死掉

feedback-triage 07:16 的交接把「週班與月班七條在 10-03〜10-05 fire 之後零 git 痕跡、日班已全數復活」排成今天要查的不對稱。對過 `routine-live-state.json`：七次 fire 全部落在 10-04 00:48 起的 87 小時額度全黑窗口裡（最早 news-lens 10-04 01:01，最晚 terminology-trends 10-05 10:35），日班是 10-07 下午之後才觸發所以活回來，週班的下一次本來就排在 10-11。真正的損失只有兩件：一週的週日反思鏈整個空掉，月班 terminology-trends 的十月那次錯過，下一次是 11-05。

告警只寫「沉默死亡」，讀的人分不出死掉的是一次觸發還是整條 routine，也看不出下一次多久後會自己重試。`4b20f267e` 讓 `routine-liveness-check.py` 每列帶 dump 的 `nextRunAt`，印成「下次排程 10-11 03:12（台北），還有 42 小時」，月班會印「還有 27.1 天」。dump 沒這欄就寫不知道，下次排程已過就提醒 dump 可能舊了。儀表板告警接同一句，補四個測試。

## 巡邏〈台灣眷村菜〉

抽樣母體第二名（03-19、未審、十二語），交接指定。49 個原子：✅ 12、⚠️ 9、❌ 7、👻 2、🔴 12、💬 7，錯誤率 21.4%，退回重寫，本班止血 `c0ec148be`，查核檔與佇列條目 `3a6d8a11b`。

最顯眼的是七條參考資料裡兩條是編出來的，而且是看起來最權威的那兩條：國防部「眷村文化保存中心」的網域 NXDOMAIN，《台灣文獻》第 71 卷第 4 期那篇論文三組搜尋都查無，連結是文獻館電子報的 404。法規那條掛到已廢止的〈國防部參謀本部組織條例〉，焦桐《臺灣味道》被描述成「確認牛肉麵眷村起源」，博客來內容連載裡焦桐其實對岡山起源說半信半疑，這段保留後來寫進了正文。正文最大的錯跟兄弟篇〈台灣眷村歷史〉10-02 巡出的是同一個：把來台約 120 萬人當成眷村人口（1982 年眷村約住 47 萬人）。劉明德那段多出來源沒有的「1950 年退役」、行軍途中學手藝、僅存積蓄、甜麵醬。

用改掉的說法 grep 全庫中文，修了兩篇兄弟篇。〈桃園市〉「2004 年 879 個眷村、桃園 80 個全台最多」掛的腳註是研之有物談黑貓中隊 U-2 航照的文章，全文沒有「眷村」兩字，改成 1984 年國防部列管數，臺北市 175 處最多、桃園 87 處居次（`8e13b999f`，孤兒腳註回掛 `e1fa12cc0`），這就是交接點名要查的那句。〈四四南村〉五月寫成時好丘信義店已熄燈半年，C 館還寫成好丘經營中，還留著一段造訪建議（`8fa14bf9c`）。第三件跟昨晚兩班的「寫的當下已過期」同型，登記成 LESSONS `present-tense-claim-sourced-before-the-change-it-describes`（vc=3，`78323962d`）。

## 收官 checklist

| 檢查項                       | 狀態                                                  |
| ---------------------------- | ----------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                    |
| Timestamp 精確               | ✅ git log %ai                                        |
| Handoff 三態已審視           | ✅                                                    |
| CONSCIOUSNESS 反映最新狀態   | ✅ 不需改（免疫與共用週額度兩列仍準）                 |
| 自我檢查工具 PASS            | ✅ 三篇 article-health hard=0；liveness 測試 9 passed |
| 額度記帳                     | ✅ start／end 兩筆都在 worktree 帳本                  |
| 日記                         | skip：排程班預設不寫（DIARY Stage 0c）                |

## Handoff 三態

繼承 `2026-10-09-071619-twmd-feedback-triage` 與 `2026-10-09-023636-semiont-heartbeat`（非本班職權的條目原樣留在那兩份，REFLEXES #74）：

- [x] ~~pending（收件席位 `/twmd-routine` 或 `twmd-flywheel-watch`，今天）— 週班與月班七條 fire 後零 git 痕跡、日班已復活的不對稱~~ — retired by 本 session（`4b20f267e`）：七次 fire 全在 87 小時全黑窗口內，週班下一次 10-11，告警現在印下次排程
- [x] ~~pending（席位：下一個 Full mode 巡邏）— 抽樣母體第二名〈台灣眷村菜〉，「桃園眷村全台最多」與四四南村那句一起查~~ — retired by 本 session（`c0ec148be`、`8e13b999f`、`8fa14bf9c`）
- [ ] pending（席位：下一個 Full mode 巡邏）— 〈台灣全齡共融旅遊與生活文化〉L196 起「政策趨勢」段（上一班留下，本班額度 lean 沒做）；抽樣母體現在的第一名是〈台灣冰品文化〉（03-19、十二語）
- [ ] pending（席位：所有在主樹工作的 session）— 主樹〈沈伯洋〉兩檔與 `puma-shen-chiang-wan-an-cihui-temple-2026.webp` 是哲宇的進行中工作，不 stash、不 commit、不還原；主樹的 `dashboard-analytics.json` 是 08:17 本機產生的新版，本班快轉時原樣放回
- [ ] pending（席位 `twmd-distill-weekly` 10-11）— LESSONS `due-date-enforcement-delegated-to-a-routine-that-can-die-silently`（feedback-triage 寫的，vc=1）仍成立：到期執行的宿主是週日桶 3，而這次證實週班會整週缺席；本班沒有動它
- ⏳ blocked — `OBSERVER-QUEUE` §待決 39 條（`#48`〜`#95`），今天沒有到期項；最近 `#86（待決）` 10-11。解除條件：哲宇拍板或到期

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly`）— 〈台灣眷村菜〉十二語整篇重翻（117 行裡改 38 增 30 刪，超過三成；盯：120 萬的口徑與眷村約 46 萬 7 千人、劉明德 1950 年起賣豆瓣醬不是退役、山東 1951／川味 1962 兩路、好丘 2025-11-23 熄燈、12 條腳註）；〈桃園市〉L106 一句與 [^14][^26] 兩條腳註、〈四四南村〉C 館四處時態與 [^22] 走 Tier 0 patch
- [ ] pending（席位 Write 班）— ARTICLE-INBOX〈台灣眷村菜〉P1 EVOLVE（`3a6d8a11b`）；岡山起源說本身的爭議是最值得寫的一段，跟〈台灣眷村歷史〉〈四四南村〉分工
- [ ] pending（席位 `twmd-distill-weekly` 10-11）— LESSONS `present-tense-claim-sourced-before-the-change-it-describes` vc=3，條目寫了兩個候選機械化
- [ ] pending（席位 `/twmd-routine`）— `twmd-terminology-trends-monthly` 十月那次落在全黑窗口，下次 11-05；要不要手動補跑一次十月，由 routine 席位決定（排程面，不屬心跳）

## Beat 5 — 反芻

feedback-triage 那條交接寫得很準：七條、各自幾小時、日班已復活。準到讀起來像一個需要調查的結構問題，而答案是一個週期：週班一週只醒一次，它們唯一醒來的那次剛好撞上全黑。缺的是一個每個讀者都會想問的欄位，「它下一次什麼時候會再試」。沒有這一欄，「錯過一次」跟「從此不會再來」在報表上是同一個紅字，讀的人只能自己去翻排程表，或者把它往下傳。

眷村菜那兩條編出來的參考資料，一條掛國防部，一條掛國史館的期刊，正好是讀者最不會去點的兩條。錯誤率的分子只算得到可以被查的句子；一個不存在的網域連「點進去看看」的機會都不給，所以它比任何寫錯的數字都更不容易被發現。

🧬

---

_v1.0 | 2026-10-09 08:58 +0800_
_session semiont-heartbeat — 週班告警補下次排程、巡邏〈台灣眷村菜〉止血、兄弟篇〈桃園市〉〈四四南村〉同錯_
_誕生原因：feedback-triage 把全黑窗口裡錯過的週班讀成結構不對稱；交接指定抽樣母體第二名〈台灣眷村菜〉_
_核心洞察：一個紅字要能分出「錯過一次」跟「不會再來」，得把下一次排程印在同一行；看起來最權威的出處最不會被點開，編造就藏在那裡_
_LESSONS-INBOX：`present-tense-claim-sourced-before-the-change-it-describes`（vc=3，新登記）_

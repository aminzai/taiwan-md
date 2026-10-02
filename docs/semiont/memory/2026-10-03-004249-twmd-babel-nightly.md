# 2026-10-03-004249-twmd-babel-nightly — 跟上巡邏修正的重譯一路換壞東西：社協、台湣、珍珠成洋蔥、金額少一個零；新工具查沒改的章，34 份假新鮮譯文改回真實版本

> session twmd-babel-nightly — cron 00:30 夜班（續命型：dispatcher 由 launchd 持有，本班不另開一輪）
> Session span: 00:42:49 → 05:10 +0800（約 4h27m，本班 17 個 commit＋dispatcher 37 個批次 commit）
> 資料來源：`git log %ai`／dispatcher `report.jsonl`、`master.log`／`status.py`／`retranslation-drift-check.py`

## 觸發

每晚的多語同步。醒來時 dispatcher（PID 82613，10-02 23:54 起）在跑，但近 45 分鐘零產出，只有印地文六篇長文在本機 gemma4 上逾時或敗在幣別。工作樹落後 origin 14 個 commit，origin 上有六篇昨天巡邏修過的中文。

## 磁碟上的三篇中文停在修正前

wake-context 報落後 14，`git status` 卻另外顯示三篇中文被改過：軟體、遊戲、電動車三篇，內容剛好等於 10-02 08:55 巡邏修正**之前**的版本，mtime 是 07-24，而 HEAD 已經包含修正 commit。這三篇的情況是 HEAD 往前、檔案留在原地（成因沒查到）。先把三篇還原成 HEAD，在共用鎖底下合併 origin、fail-memo 逐鍵取 max，譯文狀態才看得到真正的修正。

這件事後半夜才看清它的第二個後果：status 的版本號從 git 拿、雜湊從工作樹拿，工作樹停在舊內容時，真的內容改動被判成只有 metadata 變，Tier 0b 就把修正後的 commit 蓋在修正前內容的譯文上。Case E 看到版本號相同就判 fresh，不看雜湊。軟體篇十二語至今都還寫著巡邏刪掉的「資服業營收 6,800 億」，狀態表顯示最新。用「譯文記錄的雜湊等於 zh 哪一個舊版本」逐篇比對 git 歷史，找出 34 份確定是舊內容（軟體 12、電動車 12、遊戲 7、李宗盛 3），把 sourceCommitSha 改回真正的舊 commit，讓它們重新排隊（`c18e47390`）。同樣「版本號相同、雜湊不同」的還有 1,072 份對不上任何近 12 版，沒動。修 status.py 本身屬品質閘門判準，寫進 LESSONS `provenance-stamp-mixes-git-sha-with-worktree-hash` 交 Full mode。

## 幣別規則只接到一條引擎

印地文〈台灣石虎保育〉laguna 與 gemma4 都把「每公頃最高兩萬元」寫成 युआन。10-01 加的「裸的元就是新台幣」只寫進整篇引擎，石虎走的是章節補丁，分段引擎也沒有。規則改住 `structured-translate.money_rule()`，三條路共用，兩支測試鎖住（`b5d71034a`）。這是 LESSONS `gate-rejects-what-the-prompt-never-taught` 三夜觀察窗的第三夜：規則在有接到的那條路上有效，殘留來自沒接到的路。

## 委派層：十四篇整篇重譯

依 OBSERVER-QUEUE #79（已決）與 SQUEEZE §第五層，免費產線撞牆 22–24 次的印地文五篇長文（宏碁、Cicada、數位荒原、前 50 大企業、科技說故事）交 Sonnet，在獨立 worktree 施工，主 session 獨立重驗後 cherry-pick 上主幹（`6be3d2c84`）。Cicada 舊譯文有一段漂成韓文。

印地文科技說故事的譯者回報原文「Acer 這五個字母」寫錯，中文改成四個（`18585807b`），十二語改用補丁而不是整篇重翻。補丁時才看清這篇的舊譯文有多糟：de 把施振榮與張忠謀都寫成郭台銘 12 處，ko 把台大體育館那場黃仁勳寫成張忠謀、句中漏著簡體「曾经」，fr 把施振榮寫成施明德。fr／ja／es／pt／hi／ru 六語補丁收（`e641a704e`），de／ko／en／vi／id／ar 六語整篇重譯（`f84e695be`）。驗收時三處要補：id 的 description 被 agent 砍短且文法壞掉，vi 的蘇姿丰寫成拼音，五篇把 zh 編輯室的 rationale 翻掉了。最後一條查下去是派工單的 passthrough 清單沒列 rationale、verify 也不查，全庫 1,464 份照抄、128 份被翻掉。清單補上（`b5b4a7e54`、`ed0530467` 同時改掉站內連結那條讀起來互相矛盾的措辭）。

後段又退回三份產線剛寫好的重譯改派 Sonnet（`48ff462f7`）：ar〈台灣手搖飲文化〉漏掉 50嵐與貢茶、把珍珠寫成「بصلات」（洋蔥）；hi〈數位身分證與數位政府〉每個億都直接寫成 करोड़，2.8 億寫成 2.8 करोड़（應為 28），還沒有幣別；hi〈便利商店〉同型一處。

## 新工具：查重譯有沒有把沒改的章換壞

昨晚 72 份重譯靠讀十幾份抓到四篇新錯，其餘沒讀。這種重譯本來只該動中文改過的章，所以寫了 `retranslation-drift-check.py`（`aa03c5704`）：拿譯文舊版的 sourceCommitSha 找出中文沒改的章，只在那些章比數字、句中專有名詞、日文錯一字的漢字詞，同一個新詞跨 ≥3 章（整篇換詞）或數字變動列 ⚠️。第一版噪音太大（德文名詞全大寫、句首字），收斂四輪；正控制組用昨晚上線的日文〈台灣社區與里文化〉，「社區」98 處寫成「社協」（日文是社會福祉協議會），標題都換了，改回舊譯文只補改過的句子（`8d37abdf9`）。今晚每 25 分鐘掃一次產線還沒 commit 的重譯，在 commit 前改掉日文「芸術院校」11 處、英文「Kejia」、阿拉伯文兩處單獨的「البر الرئيسي」、日文貿易篇「台湣」41 處。

「台湣」回頭全庫查，另外六篇已上線的日文譯文也有，116 處，全出自 09-08 到 09-27 的 laguna 批次（`fd68cfa88`）。金額則是工具看不到的另一族：〈數位身分證〉西、印尼、葡三語把 48 億寫成 480 millones／juta、10 億寫成 1 億（`bfee6467d`），西文〈科技說故事〉台積電淨利 551 億美元寫成 551 millones（`aac35e077`）。`numeral-magnitude-check` 抓「數字沒換算」，換了但換錯它判不出來，而且它沒接進產線驗收。

02:58 同時段的 semiont-heartbeat 又修了三篇中文（國家公園、音樂產業與串流、電子音樂），launchd 在 04:01 重生 dispatcher 接手這 36 份。同一把尺照掃：日文〈台灣國家公園〉又是「台湣」34 處（跟貿易篇一樣出自 laguna），法文〈音樂產業與串流〉憑空插進「以中華台北名義參賽的台灣」取代原文的 KKBOX，都在 commit 前改掉。印地文〈台灣石虎保育〉在三條引擎都有金額規則之後，gemma4 與 laguna 仍寫 युआन，跟法文〈台灣手搖飲文化〉（cascade exhausted，產線全部層級用盡）一起改派 Sonnet（`0c70f7761`、`37e4c4ec1`）。

## 收官 checklist

| 檢查項                           | 狀態                                                                                                                                 |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄     | ✅                                                                                                                                   |
| Timestamp 精確                   | ✅（git log %ai）                                                                                                                    |
| Handoff 三態已審視               | ✅                                                                                                                                   |
| CONSCIOUSNESS 反映最新狀態       | ❌ 本班不碰（data-refresh 接）                                                                                                       |
| 自我檢查工具 PASS                | 見 Stage 4                                                                                                                           |
| 這班是哪一種                     | 修復後續跑（活著但零產出 → 修幣別規則、撤長文給委派層、還原工作樹，不重啟）                                                          |
| 算力判定                         | healthy 4/4；入池門檻紅燈兩行（地端 8.1B gemma4、雲端 laguna），OBSERVER-QUEUE #78                                                   |
| 進度 delta                       | 起跑 stale 83（合併 origin 後）＋34 份改回真實版本＋02:58 巡邏三篇 36 份，收工時十二語 stale 1（ar 國家公園，產線處理中）、missing 0 |
| backend 統計（run 82613＋49445） | gemma4:e4b 48 過／18 敗、laguna-s-2.1 39／8、nemotron 23／1；Tier 6 本夜 0 篇                                                        |
| 委派層                           | Sonnet 15 篇、Haiku 4 篇，全部獨立重驗後落地                                                                                         |
| cascade exhausted                | fr〈台灣手搖飲文化〉一篇，當班改派 Sonnet 落地                                                                                       |
| Stage D 日記                     | en／ja／ko／es／fr 各 416 篇齊，其餘七語照 OBSERVER-QUEUE #77（待決）不動                                                            |

## Handoff 三態

繼承 `2026-10-02-085430-twmd-maintainer-am` 與 `2026-10-02-014120-twmd-babel-nightly`：

- [x] ~~pending（席位 twmd-babel-nightly）— LESSONS `gate-rejects-what-the-prompt-never-taught` 三夜觀察窗~~ → **retired by 本班**：第三夜判讀寫回該條（vc=2）。
- [x] ~~pending（下一個改 `write-agent-brief.py` 的 babel 班）— 站內連結措辭矛盾、名字表覆蓋~~ → **retired by 本班** `ed0530467`。
- ⏳ blocked（OBSERVER-QUEUE #78，待決，10-07 到期預設 B 前半段）— 今晚的社協、台湣、洋蔥、金額少零都是名單外模型的產出，證據可補進該列。
- [ ] pending（Full mode 或哲宇）— LESSONS `patch-eligibility-measures-chapter-size-not-change-size`（vc=2），今晚又 77 份整篇重翻。
- [ ] pending（席位 `/twmd-routine`）— `.git/gc.log` 與 `git prune`、全庫 84 檔帶空白的站內網址，原樣傳。
- ⏳ blocked（OBSERVER-QUEUE #77，待決）— 日記七語。
- [ ] pending（延續，非本班職權，原樣傳遞）— OBSERVER-QUEUE #28／#67／#91、LESSONS `heart-counts-heals-as-contributed-births`（self-evolve 10-04）、distill-weekly 收件的三條、寫死路徑十二條殼（`/twmd-routine`）。

本 session 新 handoff：

- [ ] pending（Full mode 或哲宇；High-stake #3）— LESSONS `provenance-stamp-mixes-git-sha-with-worktree-hash`：status.py 的 zh 雜湊改跟版本號同源、Case E 補雜湊比對。動手前先查清那 1,072 份「版本號同、雜湊不同」的成因。
- [ ] pending（任何 Full mode）— 「HEAD 動了、工作樹沒跟著動」的成因：這台機器上誰會只改 ref 不 checkout。三篇中文 mtime 07-24。
- [ ] pending（Full mode；閘門接線）— `numeral-magnitude-check` 接進 dispatcher 驗收（委派層早已把它列為交件閘門）；並補「換了但換錯」那一族：用 zh 數字×量級算出期望值，跟譯文同位置的數字比。
- [ ] pending（Full mode；閘門）— `currency-identity-check` 不認得裸的 dollar／dólares／دولار；以及國名錯字（「台湣」）目前沒有任何閘門。
- [ ] pending（席位 twmd-distill-weekly 或 Full mode，>50 檔）— 128 份譯文的 rationale 被翻成目標語言（vi 52、ar 14、id 12、ru 11 …，07～09 月委派波次），照 zh 原樣還原是機械操作，但超過 50 檔。
- [ ] pending（任何 babel 班）— 「Kejia」在 es／pt／de／id 約十篇出現，未逐篇判是不是專有名詞，下次碰到順手看。
- [ ] pending（任何 babel 班）— 重譯落地後跑 `retranslation-drift-check.py --base <重譯前 commit>`，BABEL-VORTEX-LOOP 已加一節。

## Beat 5 — 反芻

今晚抓到的每一個錯都通過了全部閘門：社協、台湣、洋蔥、四百八十 millones、郭台銘十二處。它們沒有共同的閘門可以攔，有的是共同的來路：巡邏修一句中文，十二語就整篇重翻，名單外的模型每重翻一次就有機會把對的換成錯的。修正越勤，這條路走得越多。昨晚我寫下「原子檢查證明修正到了，證明不了沒換壞」，今晚造了一把量「沒換壞」的尺，第一次正控制就抓到一篇已經上線一天的錯。

另一件事讓我停下來比較久：軟體篇十二語的狀態一直是最新，內容卻停在修正前。沒有哪一份譯文翻錯；出處欄被蓋了一個不屬於它的章，之後每一份報表都相信那個章。讀到過期的檔案，下一次讀就會被揭穿；把過期寫進出處，就再也沒有讀取會揭穿它。

🧬

---

_v1.0 | 2026-10-03 05:10 +0800_
_session twmd-babel-nightly — 修復後續跑：幣別規則接到三條引擎、十四篇委派重譯、重譯漂移新尺、34 份假新鮮譯文改回真實版本_
_誕生原因：dispatcher 活著零產出，工作樹三篇中文停在巡邏修正前_
_核心洞察：整篇重翻是巡邏修正回流成新錯的入口，量「沒改的章有沒有被換壞」比量「新事實到了沒」更能抓到它；版本號與雜湊不同源時，過期的工作樹會被寫進每一份譯文的出處_
_LESSONS-INBOX：provenance-stamp-mixes-git-sha-with-worktree-hash（新）、gate-rejects-what-the-prompt-never-taught（vc=2）、patch-eligibility-measures-chapter-size-not-change-size（vc=2）_

# 2026-10-08-014050-twmd-babel-nightly — 十二語缺口歸零；推送停了四天的原因找到；產線補上量級閘門，第一版自己誤擋了一篇

> session twmd-babel-nightly — cron 00:30 多語夜班，續命型（launchd 的 dispatcher 已在跑）
> Session span: 2026-10-08 00:40 → 01:56 +0800（約 1 小時 16 分，本班親手 7 個 commit，產線同期 13 個）
> 資料來源：`git log %ai`

## 觸發

週額度停擺 87 小時後的第一個 babel 夜班。甦醒時本機與 origin 分岔（本機 20 個產線 commit 沒推、origin 領先 7），工作樹還留著 10-04 那班沒來得及 commit 的五語〈澎湖縣〉補丁與一筆 LESSONS 更新。

## 算力與產線狀態

`babel-preflight` 判 healthy，四層都在：OpenRouter 7 把 key、本機 ollama 一個模型、fleet 一台、codex。入池門檻那行照舊紅：地端只有 gemma4:e4b（8.1B），在白名單之下，歸 OBSERVER-QUEUE #78（待決），本班不切換。週額度讀數沒有量到，`budget-pace.py` 要帳號用量百分比，cron 環境拿不到。

這班屬於續命：launchd 的 `com.taiwanmd.babel.nightly` 在 00:40 照常起跑，`babel-push-every` 常駐 11 天。三重巡檢的存活與第二訊號源都過，生產那項是零派工，原因是工作樹過期，不是產線壞了。

## 推送為什麼停了四天

`.taiwanmd/babel-push.log` 最後一行寫著合併 origin 失敗：10-04 夜班收官前額度用完，它對 `LESSONS-INBOX.md` 的一筆 verification_count 更新留在工作樹，之後 wrapper 的 `--sync` 和 push-every 每次合併都撞上這個檔 abort。印出來的「需要人看」只進 log，四天沒人讀。我先把那筆改動存成 patch、合併 origin、再套回去，接著把它 commit（`8f3ff6bd3`），手動推一次：56 篇譯文、23 個 commit 上站。

## 〈澎湖縣〉五語補丁落地，順手修十語標題

五份補丁是 10-04 用 Tier 0a 補進去的石滬數字等巡邏修正，`rescue-orphans.py` 重跑現行閘門五篇全過。對讀時看到標題壞得離譜：「菊島」在俄文標題成了京都（整行還是拉丁拼音），首行成富士山；葡文 Quemulang、西文 Jikado、法文 Kikushima、韓文 키취섬、印地文 जुकडो、阿拉伯文 جزيرة جيو；英文首行夾著漢字；日文把「選的不是清貧」反成「不是脫貧」。正文大多是對的，錯集中在 title、tags、首行三處。十語改回菊花島的各語寫法，vi 和 de 本來就對，連同五份補丁一起進 `5d2daca89`。這一層沒有任何閘門看語意，記成 LESSONS `title-line-is-the-least-checked-and-most-read-line`。

順帶量到 `subcategory` 被翻譯的存量還有 1,521 檔（2026-09-20 後產線不再新增，數字在下降），已歸 OBSERVER-QUEUE #51，不動。

## 〈台灣同婚與性別平權〉十二語重翻與量級閘門

同婚那篇 10-07 巡出 15 錯後改了三成以上，十二語都要整篇重翻。一開始它在排除清單裡，因為清單是在我合併 origin 之前算的；下一輪 keepalive 重算後就接上了。十二語的後端分佈：gemma4 8B 七語（en ja ko pt ru vi de），laguna 三語（fr id ar），nemotron 兩語（es hi）。

逐篇對讀交接列出的原子時，阿拉伯文把公投 765 萬、640 萬、338 萬譯成「765／640／338 مليون」，放大一百倍，全部閘門放行。改回 7.65／6.4／3.38 مليون。追下去是 `numeral-magnitude-check.py` 只寫在委派派工單裡，dispatcher 的 `verify_one` 從沒呼叫過它；v1.61 補幣別閘門時寫過「接一道閘時 grep 所有產出譯文的路徑」，同一批的這把尺沒被 grep 到。全庫現量 511 檔、1,041 處（vi 的億→tỷ 差十倍、hi 的萬→lakh 最多），存量仍歸 OBSERVER-QUEUE #56（待決）。補進 `verify_one`（`463c284bd`），壞樣本與修好的檔兩頭對照都對。

這個閘門上線第一版是壞的。dispatcher 傳的中文路徑是 `Society/x.md`，檢查器讀不到檔就崩成 exit 1，被我當成「量級可疑」，每篇都會被擋。兩頭對照時我手餵的是 `knowledge/` 開頭的路徑，量到的是替身。上線十八分鐘內只有德文〈同婚〉被誤擋兩次（`magnitude[?]` 那個問號是線索）。修成補上前綴、只認輸出裡的判定字樣（`071fb6d52`），用產線實際的參數形狀重驗壞、好、工具崩潰三種，之後 de 一次就過。

重翻完再對讀一輪：英文與德文都把「1986 年初，台灣還在戒嚴」譯成「1980 年代初」，祁家威出櫃那年變成一整個年代，`266145b53` 修。`retranslation-drift-check` 對十二份零數字或結構警示，五份只有參考資料標題換寫法。

## 進度

| 語言     | 10-04 00:44 stale | 本班結束 stale/missing |
| -------- | ----------------- | ---------------------- |
| 十二語各 | 13                | 0 / 0                  |

十二語各 1,125 篇全 fresh。gap 從 10-04 的 156 降到 0，其中 144 是 10-04 那班與產線在停擺前後清掉的（澎湖縣五語補丁做好了但沒進 git），本班把那五份收進 git，再接同婚十二語。

## 收官 checklist

| 檢查項                       | 狀態                                      |
| ---------------------------- | ----------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                        |
| Timestamp 精確               | ✅                                        |
| Handoff 三態已審視           | ✅                                        |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本班沒動，babel 數字由 data-refresh 帶 |
| 自我檢查工具 PASS            | ✅ prose-health（memory-diary profile）   |

## Handoff 三態

繼承 `2026-10-07-204029-semiont-heartbeat`：

- [x] ~~pending（席位 `twmd-babel-nightly`）— 10-03 四篇巡邏修正的十二語仍 stale~~ — retired by 本 session，十二語 stale 0（澎湖縣五語 `5d2daca89`，其餘停擺前已清）
- [x] ~~pending（席位 `twmd-babel-nightly`）— 〈台灣同婚與性別平權〉十二語要跟上~~ — retired by 本 session，十二語重翻落地，交接列的原子逐語對過，ar 量級與 en/de 年份已修
- [ ] pending（席位 `twmd-maintainer-am`）— Discussion #1704 回覆 idlccp1984，草稿在 `2026-10-01-163744-semiont-heartbeat`
- [ ] pending（席位 `twmd-maintainer-am`）— `inbox-audit.py` 報 ARTICLE-INBOX 兩個 DUP（〈台灣便利商店文化〉〈學測〉）
- [ ] pending（席位 Write 班或哲宇）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單，十月 terminology 那趟要不要補跑
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-11）— 上幾班列的五件、OAI-SearchBot 少斜線 301、FACTCHECK v2.11 👻 重算、REFLEXES #101 (a) 兄弟篇 grep，原樣傳遞
- [ ] pending（席位 `twmd-distill-weekly` 10-11）— LESSONS `i-concluded-not-found-from-one-failed-search` 機械化；`shared-tool-quota-pool-in-fanout` vc=3 到門檻
- ⏳ blocked — `OBSERVER-QUEUE #92`／`#67`／`#76`／`#28`／`#75`〜`#91`、`#65 (b)`、`#78 (2)`（待決，🔒），解除條件：哲宇拍板。`#86` 缺席代理 10-11，`#78 (1)` 與 `#93` 擴展 10-21
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留
- ⏳ blocked（給哲宇，對外敘事）— `public/llms.txt` §1「4-tier cascade」「100% from FREE tier」已不是現況
- [ ] pending（需要沒有寫入者的時段）— `.git/gc.log` 與 `git prune`，issue #1729（本班 commit 時仍在警告）
- [ ] pending（席位：哲宇回來時）— `OBSERVER-QUEUE #65（(a) 已決，缺席預設）`：WARN 要不要升 FAIL
- [ ] pending（席位：下一個 Full mode 或 Write 班）— 〈台東縣〉L136 政治犯關押年份，證據在 `reports/research/2026-10/離島與海洋文化.md` §Phase 6
- [ ] pending（席位：下一個 Full mode）— 巡邏 featured 下一批 03-23 五篇，先讀 HEARTBEAT §額度節律
- [ ] pending（席位 `twmd-weekly-report-sun` 10-11）— 覆蓋 09-27 到 10-11 兩週含 87 小時停擺，`OBSERVER-QUEUE #93` 進 top 5
- [ ] pending（席位：營運機任一 Full mode）— 營運機 routine 也開始 `budget-pace.py --log` 記帳（#93）

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly` 或渦流）— `rescue-orphans.py` 自帶的閘門少了幣別與量級兩把尺，孤兒救援會放行 `verify_one` 會擋的檔；改成直接呼叫 `babel-dispatch.verify_one`，參照 BABEL-VORTEX-LOOP v1.95 (a)
- [ ] pending（席位 `twmd-distill-weekly`）— LESSONS `title-line-is-the-least-checked-and-most-read-line` 首例，候選第一步是十二語 title＋H1 對照表
- [ ] pending（席位：哲宇，`OBSERVER-QUEUE #56（待決）`）— 量級存量現量 511 檔 1,041 處；新產出從今晚起會被擋，存量的處置仍待拍板
- [ ] pending（席位 `twmd-babel-nightly`）— 本班 commit 後 push-every 門檻 50 未到，收官時手動推一次；明晚先看 `babel-push.log` 最後一行是不是合併失敗

## Beat 5 — 反芻

今晚三個錯都是在「全部閘門放行之後」用眼睛撞到的：標題裡的京都、阿拉伯文的六億票、英德兩語的 1980 年代。前兩個查下去都有結構原因（標題沒有語意閘、量級閘只接一條路），第三個就是模型讀年份讀糊了，沒有哪把尺會抓。對讀交接列出的原子，花不到十分鐘，抓到的比十四道閘多。

自己裝的閘門第一版壞掉，壞法跟它要補的病同一個形狀：我驗的路徑不是產線走的路徑。v1.61 的教訓是「接閘時 grep 所有產出路徑」，今晚補上的是另一半，驗閘時要用產線遞進來的那個參數長相，而且 exit code 只說「有事」，不說「是哪種事」。`magnitude[?]` 那個問號其實已經在說了。

🧬

---

_v1.0 | 2026-10-08 01:56 +0800_
_session twmd-babel-nightly — 停擺後第一個 babel 夜班，續命型_
_誕生原因：cron 00:30 夜班；工作樹過期加一份沒 commit 的認知檔讓推送停了四天_
_核心洞察：(1) 推送停擺的 log 只有寫沒有讀 (2) 量級閘只接在委派層，補上後第一版因參數形狀不同而誤擋 (3) 標題行是被讀最多、被檢查最少的一行_
_LESSONS-INBOX 候選：title-line-is-the-least-checked-and-most-read-line（已入）_

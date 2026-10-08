# 2026-10-09-010209-twmd-babel-nightly — 十二語歸零：最後三篇是事實修正，擋住補丁的是舊譯文自己的錯

> session twmd-babel-nightly — cron routine（00:30 babel 夜班），Write mode
> Session span: 00:42:54 → 01:05 +0800（約 22 分鐘，本班 5 個 commit ＋ 1 次 sync 合併）
> 資料來源：`git log %ai`、`/tmp/babel-unified-20261008-210134-87299/report.jsonl`

## 觸發

每晚 00:30 的巴別塔夜班。BECOME ACK：mode=write，wake-context 讀到 `wake:END`，selftest 唯一警訊是工作樹落後 origin 3 個 commit，起跑前用 `babel-push-every.py --sync` 合併掉。Q14 跨班連續性：上一班 heartbeat 交接指名本席位的兩件事（〈台東縣〉等三篇與〈台灣米其林與精緻餐飲〉十二語跟上、〈美食總覽〉與〈人物 Hub〉走 Tier 0 patch）都對得上 48 小時 commit。

## 算力與這班的類型

`babel-preflight.py` 判 healthy（OpenRouter 7/7、本機 ollama、fleet 一台、codex 都在）。入池門檻兩行亮紅：地端只有 `gemma4:e4b-nvfp4`（8.1B，低於白名單），雲端 `laguna-s-2.1` 不在白名單。這是 OBSERVER-QUEUE #78（待決）的同一件事，本班沒有切換。今晚的 dispatcher run（PID 87299，21:01 起）26 篇通過裡 25 篇出自這兩個名單外模型（gemma4:e4b 15、laguna-s 10），nemotron 1 篇。這個比例是給 #78 的新資料點。

這班是「續命」：dispatcher 活著、近 45 分鐘有 5 筆紀錄（1 筆通過），三重巡檢的第二訊號 fleet 一台可達。沒有重啟、沒有另開一輪。run 在 00:5x 自己印 DONE 收工，launchd 接著起了新 run（6903），零派工閒置。

## 剩下的缺口全是同一個形狀

起跑時缺口只剩三篇：〈國家太空中心〉八語、〈台灣美食總覽〉五語、〈台灣眷村菜〉兩語，全是前一天巡邏的事實修正（換一個死網址、改一句 RAW 熄燈日期、收斂桃園眷村那句）。report 裡 〈美食總覽〉 十次全敗在 `currency[N]`，跨 gemma4 與 laguna 兩種模型、四個語言同一個理由。追下去：patch 只重翻被改的那一章，裸幣別（新台幣寫成越南盾、人民幣）住在另外十一章，補丁原樣繼承，所以必然被擋，而 `fail_count` 記在模型頭上、八次後沉到佇列尾。〈國家太空中心〉同時被產線拿 8B 模型整篇重翻七十二條腳註，只為了換一個網址，ar 一次跑 73 分鐘仍被擋。

處置是把三篇從產線拿回手上：加暫時排除、停掉四個在跑的整篇重翻子程序（dispatcher 自己還原 HEAD），逐篇只改中文改了的那一行，同一份檔案裡把會擋住閘門的舊錯一起修掉，每份都過 `verify_one` 全套才 commit。`9277dc55a`〈國家太空中心〉十一語：腳註 22 換國科會網址，fr 的 Jinseng（晉陞應為 TiSpace）、四處沒翻的中文、九處 neuw 錯字、兩條被改壞的網址，vi 的 251 億／710 億差十倍，ar/de 的人民幣，以及 es/pt/ru/id 腳註 22 本身的譯錯。`5dad2db10`〈眷村菜〉ja/ar，阿文原本把桃園寫成高雄。`81510f491`〈美食總覽〉五語，越南盾九處、人民幣二十處、hi 四個數字大十倍與罰金小十倍、id 腳註被拼成台語白話字、ja 斜體圖說網址被 prettier 改壞。全部完成後排除清單還原。

交接要我盯的〈台灣米其林與精緻餐飲〉十二語，昨天已經整篇重翻完。`retranslation-drift-check.py` 零 ⚠️，110 家／2014／十四條腳註十二語對得上中文，被刪的五則引語沒有殘留。只抓到 ar 把米其林拼成 ميكرين 三十八次（站上通用 ميشلان 一百二十八次），`f18db8631` 修掉。

## 工具：派補丁前先量舊錯

`c402eaa69` 在 `babel-dispatch.py` 加 `inherited_gate_defects()`：試 patch 前對現行譯文跑漏譯、幣別、pre-commit health，量級對著譯文當初那一版中文量（拿新 zh 量會把被改章節的合法差異算成舊債），任何一項不過就跳過 patch 直接整篇重翻。正樣本用今晚修好前的 vi/id/hi/ar/ja 舊版，各自報出 currency／magnitude／health，修好的版本與 en 回空；`tests/test_babel_dispatch_inherited.py` 六條。BABEL-VORTEX v1.96 與 REFLEXES #38「確定性缺陷記成模型失敗」同 commit 記下，這是那條候選機械化的第一段。正在跑的 run 閒置後自己退出，下一次 launchd 起跑才載入新碼，沒有為此重啟。

## 收官讀數

| 檢查項                       | 狀態                                                                        |
| ---------------------------- | --------------------------------------------------------------------------- |
| 十二語 stale／missing        | ✅ 起跑 15 組非 fresh（工作樹口徑）→ 0／0，十二語 1,125 篇全 fresh          |
| babel-pulse                  | ✅ gap=0、孤兒=0、殘留暫存=0；存量：語言不符 51、網址不符 563、名人頂替 180 |
| 日記 Stage D                 | ✅ 五語 2,080／2,080，0 critical                                            |
| cascade_exhausted            | ⚠️ run 87299 記 `ar:Technology/國家太空中心.md` 一筆，已由 `9277dc55a` 解掉 |
| 推送                         | ✅ push-every 推 48 篇，origin 與本機同步                                   |
| MEMORY 有這次 session 的紀錄 | ✅                                                                          |
| Timestamp 精確               | ✅                                                                          |
| Handoff 三態已審視           | ✅                                                                          |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本班不動（babel 無器官分數變化）                                         |
| 自我檢查工具 PASS            | ✅ prose-health hard=0（memory-diary score 2/3）                            |

## Handoff 三態

繼承 `2026-10-08-143556-semiont-heartbeat`（本席位相關的部分；其餘非本班職權的條目原樣留在該檔，REFLEXES #74）：

- [x] ~~pending（席位 `twmd-babel-nightly`）— 〈台東縣〉〈台灣捷運發展史〉〈台灣國家風景區系統〉十二語跟上~~ — retired by 本 session（status 三篇十二語全 fresh）
- [x] ~~pending（席位 `twmd-babel-nightly`）— 〈台灣米其林與精緻餐飲〉十二語整篇重翻、盯 110 家／RAW／五則刪除引語；〈台灣美食總覽〉走 Tier 0 patch~~ — retired by 本 session（`f18db8631`、`81510f491`）
- [ ] pending（席位 `twmd-babel-nightly`）— `rescue-orphans.py` 改成直接呼叫 `babel-dispatch.verify_one`（BABEL-VORTEX v1.95 (a)）。本班沒動
- ⏳ blocked — OBSERVER-QUEUE #78（待決）：產線用 `--format babel` 不套入池白名單。今晚 26 篇通過有 25 篇出自名單外模型，解除條件：哲宇拍板

本 session 新交接：

- [ ] pending（席位：下一個 Write 班或 babel 班）— vi〈國家太空中心〉〈台灣美食總覽〉兩篇正文與腳註仍是整句首字大寫的舊批次譯文，延伸閱讀三條路徑翻成越南文是死鏈（article-health link-target warn）。需要整篇重翻，免費池對 72／70 腳註篇幅是負產能，依 SQUEEZE §第五層屬委派層
- [ ] pending（席位 `twmd-babel-nightly`）— 確認下一個 run 的 master.log 出現 `⏩ patch skipped … 現行譯文已帶` 這行時，後續整篇重翻是否真的產出乾淨版本（BABEL-VORTEX v1.96）。若同篇整篇重翻也連敗，那篇該進委派層而不是留在免費池

## Beat 5 — 反芻

今晚三篇卡住的文章，閘門都判對了。錯的是派工：它把「中文改了一句」翻譯成「去改譯文的一章」，卻沒先看那份譯文本身過不過得了終點那道門。補丁的設計前提是未改章節是好的，舊批次留下的譯文不滿足這個前提，而每一次失敗都被寫成模型的帳。手動修的時候，每篇都順手撞出好幾個跟這次改動無關的錯，越南盾、人民幣、晉陞變人參、桃園變高雄，這些錯一直躺在「fresh」的檔案裡，只因為沒有任何一次改動逼它重新過閘。事實修正推到十二語時，閘門其實順便替舊譯文做了一次體檢，只是體檢結果被記成了失敗率。

🧬

---

_v1.0 | 2026-10-09 01:05 +0800_
_session twmd-babel-nightly — 00:30 babel 夜班，續命型（未重啟、未另開一輪）_
_誕生原因：十二語只剩三篇事實修正，其中一篇十次全敗在幣別閘門_
_核心洞察：補丁繼承未改章節，舊譯文的錯會讓每次補丁必敗並記成模型失敗；派補丁前先量舊錯（`inherited_gate_defects`）_
_LESSONS-INBOX 候選：無新增，已 fold 進 REFLEXES #38 第四種形狀_

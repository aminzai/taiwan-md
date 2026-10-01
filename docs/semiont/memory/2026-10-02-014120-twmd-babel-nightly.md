# 2026-10-02-014120-twmd-babel-nightly — 巡邏修的六篇推到十二語，四篇在重譯時被換上新錯，對讀抓回，最後兩份改打補丁收尾

> session twmd-babel-nightly — cron 00:30 夜班（續命型：dispatcher 由 launchd 持有，本班不另開一輪）
> Session span: 00:42:06 → 02:57:23 +0800（2h15m，本班 1 commit `1f3ecde1c`＋dispatcher 13 個批次 commit）
> 資料來源：`git log %ai`／dispatcher `report.jsonl`、`master.log`／`status.py`／`verify-batch.py`／`diary-translate.py --status`

## 觸發

每晚的多語同步。醒來時 dispatcher 在 launchd 底下已經跑著。工作樹卻落後 origin 15 個 commit，其中六個是昨晚 semiont-heartbeat 事實巡邏的修正（鄰長工作協助費、十二年國教後三年非義務、早餐店弱連結、釋字 689、臭豆腐 1949、公園牽繩），拉下來之後十二語各多六篇 stale，共 72 份。

## Stage 0：算力與起跑

`babel-preflight.py` 判 healthy（OpenRouter 7/7 把 key、本機 ollama、fleet 一台 mac-m4max、codex 都在），但入池門檻兩行紅燈照舊：地端只有 8.1B 的 `gemma4:e4b-nvfp4`，雲端 `laguna-s-2.1` 不在白名單。這是 OBSERVER-QUEUE #78（待決，10-07 到期預設 B 的前半段），本班不切換。

工作樹有 dispatcher 寫到一半的 `_translation-status.json` 與 `reports/babel/*`，在共用鎖 `/tmp/taiwan-md-git.lock` 底下只還原那份 status（衍生檔，會重算）再 `merge --ff-only`。00:42 那一輪是拉之前起跑的，看到零 stale 就睡十分鐘。00:52 launchd 重生的那一輪才接到 72 份。這班屬於「續命」：沒有重啟、沒有另開一輪，三重巡檢的生產項從 00:54 第一筆起一路有實際記錄。

## 72 份重譯：閘門全綠，對讀抓到四篇新錯

六篇都是十到三十行的小修，照理是 Tier 0a 補丁的範圍。但 `patch-translate.py` 判補丁資格看的是「被碰到的章節字數佔全文比例」，門檻 50%。事實修正每處只改一兩句，卻散在好幾個章節外加參考資料區，〈台灣社區與里文化〉碰到 5/11 章節、55.6%，於是 72 份全部退回整篇重翻，交給名單外的兩個模型。

我寫了一支只看「修正後的事實原子有沒有到譯文」的小工具（2,500／689 且不得有 613／1949，外加十二語「義務」字數對照），先拿還沒重譯的舊檔當正控制組，全部該報的都報了，再逐批跑在落地的譯文上，最後 70 份全過。但原子檢查只證明新事實到了，沒證明舊的對的東西還在。逐篇對讀抓到四篇是重譯本身帶進來的新錯，四篇都過了全部閘門：

- fr〈台灣社區與里文化〉（laguna）：鄰長寫成鄉長「xiāng zhǎng」，里長寫成「directeur de district」（讀起來像區長）。舊版用 _li_／_lin_ 是對的。
- en〈教育制度與升學文化〉（laguna）：舊版寫 Twelve-Year National Education，新版改成 Compulsory Education 八處。當天中文要修的就是「後三年不是義務教育」，重譯把這個錯從另一個方向放回來。
- ja〈台灣發酵食品與醃製文化〉（laguna）：臭豆腐八處寫成「臭豆腸」，遷台寫成「政府の引き揚げ」。
- ko〈台灣媒體與新聞自由〉（gemma4:e4b）：釋字第 689 號寫成「대법원 판결」（大法院判決），衛廣商業公會寫成「방위 상업 협회」（防衛商業協會）。

四篇都在 dispatcher commit 之前改回，跟著它的批次 commit 進去（`5958b0005`、`f38a34bdf`、`4b506cf5a`、`9f0928de4`，已用 `git show` 確認內容是修過的版本）。順手把 ja〈台灣社區與里文化〉三條寫成「標題（URL）」的腳註改回連結格式（全庫 ja 只有兩檔有這個形狀，另一檔〈再生醫療法規〉沒碰）。

## 最後兩份改打補丁

ko〈台灣社區與里文化〉與 id〈教育制度與升學文化〉在產線上各撞了三次牆，每次理由都不同（腳註格式、整篇沒寫出、殘留保護佔位符），而 dispatcher 對剛還原的檔有十分鐘去重冷卻。中文那邊只改了十幾行，我照 SQUEEZE Tier 0a 直接對既有譯文打補丁：沒變的段落原樣保留，只翻改動的句子，補上新腳註，把三個 source hash 對齊 zh，`1f3ecde1c`。兩篇都過 verify 十九項、article-health 零硬錯、幣別閘門、漢字殘留檢查。ko 那篇順便把 subcategory 從「사회 운동」改回中文分群鍵。

收尾時十二語 stale 0、missing 0。Z5 `verify-batch.py` 對今晚 70 份按語言建 manifest 跑，十二個 exit 0。Z6 用 seed 20261002 抽 10 份看結尾與腳註數，全部完整。push-every 在 02:41 推了 52 份，剩下 5 個 commit 未達 50 份門檻，留給它下一次推。

## 幣別閘門與 Stage D

昨晚交接要看「規則 8 上線後 hi／ar／ru 幣別閘有沒有降」。今晚 46 次嘗試裡幣別失敗 5 次，全在雲端免費模型、分散在兩篇（社區 id／hi／ru、早餐店 vi／ar），而且每一篇最後都由別的 worker 過關。09-30 那種 ru 一篇 295 次裡 166 次敗在幣別的形狀沒有再出現。樣本是不同文章，只能說沒看到惡化，還不能說降了，三夜觀察窗繼續算。

日記巴別塔：en／ja／ko／es／fr 各 416 篇到齊，`diary-translation-audit.py` 0 critical，其餘七語照 OBSERVER-QUEUE #77（待決）不動。

## 收官 checklist

| 檢查項                       | 狀態                                                                 |
| ---------------------------- | -------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                   |
| Timestamp 精確               | ✅（git log %ai＋wake-context 落檔時間）                             |
| Handoff 三態已審視           | ✅                                                                   |
| CONSCIOUSNESS 反映最新狀態   | ❌ 本班不碰（routine 範圍外，由 data-refresh 接）                    |
| 自我檢查工具 PASS            | ✅ article-health memory-diary profile（見下方 Stage 4）             |
| 算力判定                     | healthy 4/4，入池門檻紅燈兩行（地端 8.1B、雲端 laguna）              |
| 進度 delta                   | 十二語 stale 72 → 0，missing 0 → 0，覆蓋率 100%                      |
| backend 統計（run 89468）    | gemma4:e4b 18 試 13 過，雲端免費池 26 試 17 過，Tier 6/7 本 run 0 篇 |
| cascade exhausted            | 本班無新增                                                           |

## Handoff 三態

繼承 `2026-10-01-010545-twmd-babel-nightly` 與 `2026-10-01-084906-twmd-maintainer-am`：

- [x] ~~pending（席位 `twmd-babel-nightly`）— ru〈309本里長帳簿〉cascade exhausted~~ → **retired**：10-01 白天已由產線過關（`knowledge/ru/Politics/village-chief-campaign-ledgers.md` 在 HEAD，status 0 missing）。工作樹留一個被 gitignore 的 `knowledge/ru/Politics/309.metrics.json` 舊 sidecar，無害，未刪。
- [ ] pending（席位 `twmd-babel-nightly`）— LESSONS `gate-rejects-what-the-prompt-never-taught` 的三夜觀察窗：第二夜，幣別失敗 5/46、全部在別的 worker 過關，未見 09-30 的形狀。第三夜（10-03）再看一次就可以判。
- [x] ~~pending（席位：任何 Full mode）— 譯文分類閘門缺口~~ → **retired by 10-01 semiont-heartbeat**（`95de2acab`）。
- [x] ~~pending（席位：任何 Full mode）— `verify_internal_links.py` 遇 build 中 abort~~ → **retired by 10-01 semiont-heartbeat**（`be4e900ed`）。
- [ ] pending（席位：能動排程的 Full mode session 或 `/twmd-routine`）— `.git/gc.log` 與 `git prune`，本班照傳不動（dispatcher 全程在寫）。
- [ ] pending（席位：任何 Full mode／`/twmd-routine`）— 全庫 84 檔 169 條帶空白的站內網址，原樣傳（明細見 10-01 babel memory）。
- ⏳ blocked（`OBSERVER-QUEUE #78`，待決，10-07 到期預設 B 前半段）— 今晚四篇新錯的證據已寫回該列。
- ⏳ blocked（`OBSERVER-QUEUE #77`，待決）— 日記巴別塔七語。
- [ ] pending（延續，非本班職權，原樣傳遞，REFLEXES #74）— OBSERVER-QUEUE #67／#75〜#92、#76 辭典、issue #1729、PR #1781 後續、`ci-main-health` 成因、MAINTAINER 交接其餘項。

本 session 新 handoff：

- [ ] pending（席位：Full mode 或哲宇。`/twmd-routine` 動得了這支檔但不該自己改數值）— LESSONS `patch-eligibility-measures-chapter-size-not-change-size`：補丁資格門檻 `CHAPTER_SIZE_RATIO_LIMIT = 0.5`（`scripts/tools/lang-sync/patch-translate.py`）量的是章節大小不是改動大小，事實巡邏的每一次小修都會觸發整篇重翻。改判準屬 High-stake #3。
- [ ] pending（席位 `twmd-babel-nightly`／任何 Write 班）— ja〈台灣再生醫療法規〉腳註「標題（URL）」格式，跟今晚修掉的那篇同形，下次碰到這篇順手改。

## Beat 5 — 反芻

今晚最值得記的是那篇英文教育譯文。中文昨晚修的是「十二年國教後三年不是義務教育」，修正推到英文時，產線沒有補那一句，而是把整篇交給模型重寫；舊譯文原本寫的是中性的 National Education，新譯文寫成 Compulsory Education，閘門全綠。修正這個動作本身成了錯誤回流的入口：巡邏越勤，被觸發的整篇重翻越多，交給名單外模型的機會就越多。#78 一直被描述成「每天多三百份來源可疑的譯文」，今晚看到的是另一個代價，它會把已經對的東西換掉。

另一件事是查法。原子檢查能證明修正到了，證明不了沒有東西被換壞；四篇新錯沒有一篇是原子工具抓到的，都是讀到才看見。這跟 #78 列裡 09-27 那九篇是同一個形狀（整篇把同一個名詞換掉），而它們都穿過了十幾道閘門。今晚靠的是 72 份裡挑十幾份對讀，剩下五十多份我沒讀。

🧬

---

_v1.0 | 2026-10-02 02:57 +0800_
_session twmd-babel-nightly — 續命型夜班：接住事實巡邏六篇 × 十二語_
_誕生原因：工作樹落後 15 個 commit，拉下來後 72 份 stale_
_核心洞察：補丁資格量章節大小，讓每次小修都變整篇重翻；名單外模型的重翻會把對的舊譯文換成新錯，而且閘門看不見_
_LESSONS-INBOX 候選：patch-eligibility-measures-chapter-size-not-change-size（已寫入）_

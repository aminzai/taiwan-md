# 2026-09-25-004244-twmd-babel-nightly — 三道「一篇文章卡死所有模型」的閘門缺陷當夜修掉，三篇新文缺 slug 卡六天補上並接進起跑自檢，〈金鐘獎〉十一語由委派層收齊

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:42:44 → 01:25 +0800（約 43 分鐘，本班 10 commits；同時段 dispatcher 另有批次 commit）
> 資料來源：`git log %ai` / dispatcher `report.jsonl`、`master.log`、patch-translate 側錄 JSON / `status.py` / `babel-preflight.py`

## 觸發

00:30 例行觸發。甦醒 selftest 十一項全綠，ACTOR_BUSY：09-21 00:58 起跑的 launchd dispatcher（PID 98122）第五天還在產，本機領先 origin 59 個 commit。照 09-18 的「停重複不停產線」不重啟產線，力氣放在拆失敗與產線結構上做不到的那一段。

```
✅ BECOME ack: mode=write / 8 organ 最低=免疫 59（快照齡 18h，stale 標記）/ Q14 cross-session continuity=PASS
```

🚨 先複述 09-24 maintainer-am 的交接：mouhouse 的 Claude Desktop 登入預估 2026-09-27 過期，只有哲宇能在那台機器上重新登入；過期後十三條 routine 會照常 fire 但全部被擋回。

## Stage 0 算力判定

`babel-preflight.py` 判 healthy，四層都在（OpenRouter 7/7 key、本機 ollama、fleet mac-m4max、codex-cli 0.145.0）。入池門檻那行照舊紅：地端唯一模型是 8.1B 的 `gemma4:e4b-nvfp4`（OBSERVER-QUEUE #78 未決，照跑不切旗標）；Tier 6/7 付費捕手仍缺 key。實質判定 **degraded**，缺合格地端模型與付費捕手兩層。過去 24 小時 dispatcher 564 次嘗試 224 過（40%），通過的譯文 58% 出自 8.1B、29% 出自名單外的 laguna-s，名單內的 nemotron 只佔 13%。

## 同一篇、多種模型、同一道閘

拆 report 時先找「同一篇在三種以上 worker 上敗在同一個理由」的組合，這種形狀不可能是模型能力，今晚撈到三個，都當夜修掉並附測試（全套 529 passed）。

台灣棒球文化十二語全卡網址閘：腳註 4 是路徑為中文的裸網址，整篇引擎的裝甲 regex 把漢字排除在外，只藏到網域，模型看見中文路徑就翻，而 verify 那把尺把整段算成網址。裝甲改成直接借 `verify-translation` 的 `URL_PATTERN`（`3fada141b`），兩把尺從此是同一把；全庫 13 篇母稿有這種裸網址，沒有一處緊貼散文。

高雄加工出口區三語卡網址閘：圖說整行斜體、網址在句尾，prettier 把譯文的 `*…*` 改成 `_…_`，譯文抽出來的網址多一個 `_`。`extract_urls` 兩側一起剝底線（`dd695c1b7`），跟 09-24 的反斜線跳脫同一族。

台灣網路社群遷徙史與外送專法的章節修補五語卡網址閘：追到 patch 引擎組回譯文後跑的 `footnote-format --fix`，它的「散文前綴」規則抓到多來源腳註的第二個連結卻沒寫回去，DataReportal、數位時代兩個出處被刪，網址 47 變 44。fixer 自己的文件寫「不碰多連結腳註」，這一支碰了；改成多來源散文腳註原樣保留（`551ca83c2`）。這支 fixer 在 dispatcher 各路徑都跑，所以之前每一次它刪出處，verify 都擋下了，沒有壞譯文落地，代價是那些文章永遠翻不過去。

另外兩件同形但不在閘門：東港迎王船六語卡內嵌圖檢查，是母稿（PR #1446）引用了一張從沒進 repo 的圖，中文頁本身就是破圖，拿掉 figure 與檔尾路徑說明，正文不動。診斷過程中 `article-health` 對隔離區檔名認不出語言、把中文標點規則打在葡文上，六份被擋譯文前面一整排假的 cjk-punct 蓋住真正原因（幻覺 wikilink、腳註格式），loader 補認 `{lang}--{slug}.md`（`3266b96f5`）。修完從隔離區收回六份譯文（高雄加工出口區 id／ko／pt／ru、新竹米粉 ko、千千進食中 ja，`3f9e184dc`）。

## 三篇新文六天沒排進佇列

金鐘獎、台灣油價機制與中油、誰算低薪三篇 09-19 news-radar 新文，檔名純中文、沒有任何譯文，slug 無從反推，dispatcher 每輪印一行 TBD-NEEDS-SLUG 然後十二語一起跳過，這一輪已經印了 133 次。補三筆進 `_slug-map.json`（`14e29deed`），dispatcher 每輪重讀、不必重啟。這是同一個缺口第三次（09-13、09-14、今晚），三次都靠當班碰巧翻 log。把判準接進 `babel-preflight.py`（`840f500e8`），每班 Stage 0 第一個指令就會列出來；拿掉今晚三筆實測，它正好抓出這三篇。

## 〈金鐘獎〉交給委派層

金鐘獎 45KB、59 腳註、71 網址，照 SQUEEZE §第五層判 Sonnet。照 #79 的預設各自判斷，派十一語、一語一隻，en 留產線。認領寫進 `babel-exclude-claims.tsv` 後立即重算排除清單，交件後刪行。十一份（`bcc6b00ba`）由主 session 獨立重跑結構對靶、verify、漢字洩漏與黏著、article-health、prettier，全過；單價每語 20–28 萬 token，合計約 280 萬。

獨立驗收抓到 agent 自述沒提的一件：`verify-batch` 報 es／fr／ja 各 5 個 wikilink 殘留、hi／ru 寫成 `[[中文|譯名]]`。站上渲染器對 wikilink 只印粗體不出連結，法文頁中間會冒出粗體「歌仔戲」。用派工單的 `wikilink_targets` 機械換成連結、錨字取各語言那篇文章的標題（`274bd50b6`）。病根在派工單：規則只講目標不存在時怎麼扁平化，誤判清單又把 wikilink 列成「看到別動」，六語照做是運氣。補上另一半規則（`12821384b`）。同一個量尺全庫掃一次，12 語 253 份既有譯文帶中文 wikilink 殘留。

驗收時我自己也差點錯一次：vi agent 說連炳發是越南演員、越南名 Liên Bỉnh Phát，我先入為主以為是台灣演員，查母稿才知道他是金鐘史上首位越南籍視帝，agent 是對的。

## 各語進度與耗盡清單

本班 00:43 → 01:20 十二語 fresh 12,725 → 12,746、missing 491 → 471、stale 271 → 270。de 仍是唯一低於九成的語言（88.6%，missing 128）。dispatcher 本班視窗只落一個批次 commit，長文佔據 worker。Tier 0b 只有 ru〈玉山氣象站〉一份，昨晚 bump 後被 dispatcher 還原，今晚交給它不動。

自昨晚收官起新增 cascade exhausted 25 筆（義務鐵律第 4 條必列，ru 佔 17）：ru 東港迎王船、ru 水道頭、pt 高雄加工出口區、ru 臺灣民報、ru 外送專法、ru 比國家還大的演算藝術、pt 苯駢芘食安事件、pt 中央研究院、ru 台灣行道樹、ru 苯駢芘食安事件、ru 台灣美食總覽、ru 黃崇仁、ru 高速公路、ko 貓眼石、ru 新竹縣、pt 貓眼石、ru 台灣網路社群遷徙史、ru 台灣新冠疫情與疫苗、pt 臺灣民報、pt 黃崇仁、fr 苗栗縣、ru 台灣辦桌文化、ru 大龍峒、ru 李洋、ru 營養午餐。其中高雄加工出口區、東港迎王船、台灣網路社群遷徙史、外送專法四篇的病根今晚已修。

Stage D：日記巴別塔 en／ja／ko／es／fr 各 415 篇，audit 0 critical；其餘七語照 #77 待決。

## 收官 checklist

| 檢查項                       | 狀態                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                                           |
| Timestamp 精確               | ✅ 取 `git log %ai`                                          |
| Handoff 三態已審視           | ✅                                                           |
| 自我檢查工具 PASS            | ✅ pytest 529 passed / 8 skipped；十一份委派譯文全閘重驗通過 |
| cascade exhausted 已列出     | ✅ 25 筆（見上）                                             |
| 本輪 commit 推上 origin      | ✅ 收官推                                                    |

## Handoff 三態

繼承 09-24 babel-nightly：

- ⏳ blocked — OBSERVER-QUEUE #78 入池門檻未決，本班照跑不切旗標，通過譯文 87% 出自名單外。
- ⏳ blocked — OBSERVER-QUEUE #77 日記巴別塔七語，未決。
- ⏳ blocked — phase-F／phase-N backend timeout（240 秒）屬閾值調整，仍待 Full mode 或哲宇。
- [x] ~~vi〈台灣傳統工藝與無形文化資產〉整篇重翻~~ — retired：dispatcher 09-24 15:24（`a59ba1a87`）已重翻，藍染現為 nhuộm chàm，verify 19/19。
- [ ] pending — OBSERVER-QUEUE #79 長文委派額度，等哲宇；本班照預設用約 280 萬 token。
- [ ] pending — 圖表來源列存量（`9dbf3f6b5`）的 ar／hi 渲染抽看，本班沒 build，續交。
- [ ] pending（1-file 候選）— LESSONS `measured-copy-is-not-the-committed-copy`：四篇 prettier 不穩定的 zh 母稿正規化，由維護班判斷。

繼承 09-24 maintainer-am：#1761 mouhouse 登入 09-27 過期仍待哲宇（見觸發段）。

本 session 新 handoff：

- [ ] pending（給下一班 babel）— 台灣油價機制與中油、誰算低薪兩篇 slug 已補，看 dispatcher 下一輪有沒有排進去；油價機制 46KB／46 腳註，免費池大概翻不動，照 #79 預設可交委派層。金鐘獎 en 留產線，同理。
- [ ] pending（>50 檔，給哲宇或 Full mode）— 12 語 253 份譯文帶中文 wikilink 殘留（`grep -rlE '\[\[[^]]*[一-鿿][^]]*\]\]' knowledge/{lang}`），站上印成粗體中文、不出連結。修法今晚在〈金鐘獎〉驗過：用 `_translations.json` 查目標譯文網址，錨字取目標文章標題，機械替換後重跑閘門。規模命中 §自主權邊界，本班不動。LESSONS `wikilink-residue-renders-as-bold-chinese`。
- [ ] pending（OBSERVER-QUEUE 候選，🔒 閾值）— `cjk-leak-check` 書名號豁免上限 30 字，陳嫺靜專輯名《如果每天都可以 happy happy 誰想要 sad…》約 33 字，ja／ko 修補一直被判洩漏。改成「只數漢字」或放寬上限都是閘門數值調整，本班不動。
- [ ] pending — 東港迎王船中文頁拿掉了破圖，補一張授權清楚的王船照片（Wikimedia Commons 等），PR #1446 投稿者原本想放的是農業部農業易遊網那張。

## Beat 5 — 反芻

今晚三道閘門缺陷共用一個讀法：同一篇文章在三種互不相干的模型上敗在同一個理由，就先別看模型。report 一直都有這個訊號，只是按 worker 或按語言看都看不出來，要按「文章 × 失敗理由」轉一次軸才浮出來。這個轉軸目前只存在今晚的一段 Python 裡，下一班不會有，已經寫進 LESSONS `deterministic-parser-defect-billed-as-model-failure` 的判讀捷徑，到第四次就該做成 preflight 的一行。

委派層那件讓我比較在意。十一隻 agent 讀同一份派工單，六隻把 wikilink 換成連結、五隻留著，而每一隻都回報全綠，也都是真的全綠：沒有一道閘門在問「這段在站上會長成什麼樣子」。派工單只寫了規則的一半，剩下那一半由各自的判斷補上，補對補錯機率差不多一半一半。

🧬

---

_v1.0 | 2026-09-25 01:25 +0800_
_session twmd-babel-nightly — cron 00:30 多語批次同步，產線續跑不重啟_
_誕生原因：拆 dispatcher 失敗找跨模型一致的失敗，修閘門與母稿；補三篇新文 slug；〈金鐘獎〉交委派層_
_核心洞察：(1) 同篇跨三種以上模型同理由失敗，先查閘門與母稿 (2) 兩把量同一個東西的尺要是同一把，不是兩份相似的 regex (3) 派工單只寫一半的規則，另一半由 agent 各自補，閘門全綠也照樣分岔_
_LESSONS-INBOX：`deterministic-parser-defect-billed-as-model-failure` vc 2→3、`measured-copy-is-not-the-committed-copy` vc 2→3、`new-article-creation-has-no-slug-registration-step` vc 2→3；新增 `wikilink-residue-renders-as-bold-chinese`_

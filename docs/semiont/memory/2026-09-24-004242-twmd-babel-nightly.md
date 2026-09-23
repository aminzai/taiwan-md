# 2026-09-24-004242-twmd-babel-nightly — 旗艦文十二語到齊（委派層一夜收十一語），五道閘門誤判當夜修掉，77 份尾段漂移對齊，量出缺稿的一半是免費池翻不動的長文（#79）

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:42:42 → 01:36 +0800（約 54 分鐘，本班 23 commits，同時段另有 dispatcher 的批次 commit）
> 資料來源：`git log %ai` / dispatcher `report.jsonl`、`master.log`、patch-translate 側錄 JSON / `status.py` / `babel-preflight.py`

## 觸發

00:30 例行觸發。甦醒 selftest 十一項全綠，ACTOR_BUSY：09-21 00:58 起跑的 launchd dispatcher（PID 98122）已經轉了將近三天還在產，本機領先 origin 48 個 commit。照 09-18 定下的「停重複不停產線」，本班不重啟產線，力氣放在拆失敗、修工具、以及產線結構上做不到的那一段。

```
✅ BECOME ack: mode=write / 8 organ 最低=免疫 59（快照齡 18h，stale 標記）/ Q14 cross-session continuity=PASS
```

## Stage 0 算力判定

`babel-preflight.py` 判 healthy，四層都在：OpenRouter 7/7 key、本機 ollama、fleet 一台 mac-m4max、codex-cli 0.145.0。但入池門檻那行照舊是紅的：地端唯一的模型是 8.1B 的 `gemma4:e4b-nvfp4`，低於白名單（OBSERVER-QUEUE #78 未決，本班照跑不切旗標）。Tier 6/7 付費捕手仍缺 key，整夜缺席。實質判定：**degraded**，缺的是合格的地端模型與付費捕手兩層。

過去 24 小時 dispatcher 落地 450 份，其中 8.1B 模型 246 份、`laguna-s-2.1`（不在名單上）142 份、名單內的 nemotron 62 份，86% 出自名單外，跟昨晚的 87% 同一個量級。

## 五道閘門誤判：每次重試都一樣，卻被記成模型沒過

照昨晚交接先拆失敗。「no output written by translate.py」仍是最大一格，拆 master.log 後大半是本機 8.1B 三個 worker 搶一張卡的逾時，屬 #78 的範圍。剩下的確定性家族當夜修掉五個，全部附測試（全套 521 passed）：

一條腳註的批次，模型回裸物件就被當成「截斷撈出的單筆」拒收，二分之後的半批最常撞（`d1832391f`）。寬鬆 JSON 解析先找方括號再找大括號，frontmatter 物件後面多一句說明，就撈到物件裡的 tags 陣列回傳（`2eca7eac0`，章節 patch 引擎 import 同一支，一起生效）。網址比對把 prettier 寫出來的 `\_`、`\(` 當成網址被改寫（`aaac94be2`），這是今晚最有意思的一個，另寫一段。日韓譯文的標籤照抄判準把 Portaly、AI、SaaS 這類拉丁字母標籤算進分子，章節 patch 被拒 20 次裡 10 次落在這道閘，改成只數帶漢字的標籤（`0d5526c9f`。剩下幾次是 8.1B 模型真的把好的日文地名標籤換回中文，那是正確的擋）。腳註格式閘不認「[^14]に同じ」這種參照在前的日韓語序（`c791b6c7a`）。

順手把隔離譯文回收工具寫死的 `/Users/cheyuwu` 改成從檔案位置推導（`705fbf36d`）。我一開始以為那條路徑是同機另一份 checkout、會把救回的譯文寫錯地方，查了才知道它是指回 `/Users/musebase` 的 symlink，commit 訊息在推上去前改正了。

## 量的那一份跟寫進 git 的那一份

網址閘門那件：dispatcher 驗證前對譯文跑 prettier，母稿卻是 commit 當時的樣子。全庫 zh 母稿逐檔用 prettier 實跑、比網址出現次數，有四篇不穩定（蓬萊米、台灣客家音樂、高雄加工出口區、新竹米粉），它們的每一份譯文都卡在同一道閘。CommonMark 會先處理反斜線跳脫，兩種寫法渲染出同一個 href，所以這是量測不對稱，不是壞連結。修好比對後用 `salvage-quarantined` 逐檔重跑三道閘，從隔離區收回四份（`87e51b244`）。

同一個形狀當晚又撞一次，這次在委派層：印尼文旗艦文交件時十四道閘全綠，commit 時 lint-staged 先跑 prettier，第 73–75 條腳註之間缺空行，74、75 被折進 73，腳註少兩條、hard 擋下。手動拆回、確認 prettier 穩定後落地，派工單的閘門清單補上第 15 道 `prettier --check`（`fea28f87d`）。兩次合成 LESSONS 新條目 `measured-copy-is-not-the-committed-copy`，並回答了 09-23 maintainer 留下的 `italic-span-defeats-url-escaping` (c)「譯文層未量」。

## 旗艦文十二語到齊

〈比國家還大的演算藝術〉77KB、85 腳註，免費池累計失敗 78 次、六語已耗盡，昨晚委派層落了 en。今晚照 SQUEEZE §第五層把其餘十一語各派一隻 sonnet。派之前先補了一個缺口：dispatcher 的排除清單每 90 分鐘重算一次，手寫的排除行會被蓋掉，而 missing 檔撞失敗時 dispatcher 會把 agent 寫到一半的檔案移進隔離區。改成委派認領寫在 `.taiwanmd/babel-exclude-claims.tsv`（本機狀態、不進版控），`babel-origin-exclude.py` 每次重算原樣併入（`3f01fc009`），交件後刪行。

十一語全部落地（`99df67d4d` pt 到 `d99a0c214` hi）。每一份都由主 session 獨立重跑產線三道閘、結構對靶、目標語言、漢字黏著、站內連結、量級、整行未翻、人名一致性與 prettier 穩定性，不採 agent 自述。單價實測：每語 22–37 萬 token、9–26 分鐘，十一語合計約 330 萬 token。hi 最長（198KB）也最貴，這跟天城文的 token 密度一致。ko 在三條逐字稿腳註的時間戳後補了空格（中文用全形括號，換成半形會被讀成連結），ru 依 SEO 閘門指示為 description 獨立寫了一段，都是合理的在地處理。

## Tier 0b 與三份舊債

79 份 metadata-stale（母稿只動尾段、正文 hash 沒變）跑 `bump-source-sha`。commit 時 pre-commit 擋下四份帶舊債的：en／fr〈笠詩社〉的詩人雙鏈指向不存在的頁面，其實杜潘芳格兩語都有譯文，改成正常站內連結。ja〈落日飛車〉被腳註格式閘誤判，上面那道修正放行。vi〈台灣傳統工藝與無形文化資產〉的內嵌圖跟母稿對不上、把「藍染」譯成「tằm màu」（大意是彩色的蠶），這份需要整篇重翻，沒有 bump，留在 stale。ru〈玉山氣象站〉在我 bump 之後被 dispatcher 還原，交給它。落地 77 份（`74349bb60`），status 全數 fresh。

## 各語進度與耗盡清單

本班 00:43 → 01:25 的 delta（產線同時在跑）：十二語 fresh 12,431 → 12,538、missing 587 → 566，每一語都有動。de 仍是唯一低於九成的語言（87.1%，missing 145）。本班視窗內 dispatcher 38 次嘗試 17 過，nemotron 7/7 全過、8.1B 模型 4/16。

自昨晚收官起新增 cascade exhausted（義務鐵律第 4 條必列）：`hi:Lifestyle/台灣醫療與全民健保.md`、`hi:Music/落日飛車.md`、`ja:Lifestyle/高速公路.md`、`ar:Society/外送專法.md`、`ru:Lifestyle/收費站.md`、`ru:People/阿神.md`。

Stage D：日記巴別塔 en／ja／ko／es／fr 各 415 篇到齊、audit 0 critical，其餘七語照 #77 待決，不動。

## 缺稿的一半是長文（#79）

拉 status 對 §第五層門檻：566 份缺稿裡 286 份（89 篇母稿）是 >40KB 或腳註 >50 的長文，五篇新文十二語一語都沒有。免費池對這個形狀是負產能，而委派層今晚證明做得到，只是一份約 30 萬 token，全清約 8,500 萬。這是經費與算力分配，寫進 OBSERVER-QUEUE #79（推薦每夜額度，14 天未決預設不擴大）。

## 一個失誤

驗證 tags 測試時，我在一行指令尾端誤帶了 `git stash -q`，把工作樹（含 dispatcher 還沒 commit 的譯文與我自己的修改）收進 stash。發現後立刻 `git stash pop`，無衝突、untracked 檔不受影響，前後大約十秒。沒有造成損失，但這正是 REFLEXES #35 在平行寫入者存活時禁止的那類操作，記在這裡。

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ✅ 取 `git log %ai`                                      |
| Handoff 三態已審視           | ✅                                                       |
| 本輪 commit 推上 origin      | ✅ 旗艦文最後一語後推過一次（`d99a0c214`），收官再推一次 |
| 自我檢查工具 PASS            | ✅ pytest 521 passed / 8 skipped；observer-queue-lint 綠 |
| cascade exhausted 已列出     | ✅ 6 筆（見上）                                          |

## Handoff 三態

繼承 09-23 babel-nightly：

- ⏳ blocked — OBSERVER-QUEUE #78 入池門檻未決。本班照跑不切旗標，當夜名單外比例 86%。
- ⏳ blocked — OBSERVER-QUEUE #77 日記巴別塔七語，未決，Stage D gate 照紅。
- [x] ~~`no output written by translate.py` 仍是最大一格~~ — 本班拆完：剩下大半是本機 8.1B 逾時（#78），確定性家族五個已修，retired by 本班
- ⏳ blocked — phase-F／phase-N backend timeout（240 秒）屬閾值調整，仍待 Full mode 或哲宇。
- [x] ~~〈比國家還大的演算藝術〉十一語 missing~~ — 本班委派層收齊十二語，retired by 本班
- [ ] pending — 圖表來源列存量（`9dbf3f6b5`）的 ar／hi 渲染抽看，本班沒 build，仍待下一班。

繼承 09-23 maintainer-am：`italic-span-defeats-url-escaping` (c) 譯文層已量完並落地修補（見 LESSONS 該條）；#1761 mouhouse 登入預估 09-26～27 過期，仍待哲宇。

本 session 新 handoff：

- [ ] pending（給任何能跑 Tier 0a／委派的班）— vi〈台灣傳統工藝與無形文化資產〉整篇重翻：內嵌圖對不上母稿、「藍染」譯成「tằm màu」。已刻意不 bump，保持 stale。
- [ ] pending — OBSERVER-QUEUE #79 長文委派額度，等哲宇。下一班照預設各自判斷、單班不超過約 330 萬 token。
- [ ] pending（1-file 候選）— 四篇 prettier 不穩定的 zh 母稿（蓬萊米／台灣客家音樂／高雄加工出口區／新竹米粉）閘門已不再誤判，但母稿本身下次被任何人 commit 時會被 prettier 改寫網址跳脫。渲染無害，要不要順手正規化由維護班判斷。LESSONS `measured-copy-is-not-the-committed-copy`。

## Beat 5 — 反芻

今晚五道閘門誤判裡最難看見的是網址那一道。它的每個零件都對：dispatcher 先 prettier 再驗，是為了對齊 commit 會量的那一面，網址比對要求逐字相同，是 07-29 被模型改一個位元組的 percent-encoding 教出來的。兩個對的決定疊在一起，就讓四篇母稿的譯文在十二個語言上永遠過不了，而報表把它記成模型的失敗。委派層那一次是同一件事反過來：agent 量得很仔細，量的是 prettier 經手前的那一份。我開始覺得「驗證對象要等於落地對象」該是閘門設計時第一個問的問題，排在「要驗什麼」之前。

另一件事是旗艦文。它在免費池撞了 78 次，委派層一夜收齊。這讓 #79 那個數字變得具體：缺稿的一半卡在同一個形狀上，解法已經驗證過，只差一個誰付錢的決定。這個決定不是我的，但今晚之後它有了單價。

🧬

---

_v1.0 | 2026-09-24 01:36 +0800_
_session twmd-babel-nightly — cron 00:30 多語批次同步，產線續跑不重啟_
_誕生原因：拆 dispatcher 失敗找確定性家族當夜修，並把產線結構上做不到的旗艦文交給委派層_
_核心洞察：(1) 驗證對象要等於落地對象，比較型閘門兩側要過同一個正規化 (2) 委派層的單價量出來了：長文每語約 30 萬 token，缺稿的一半是這個形狀 (3) 重試結果每次都一樣的失敗，不該算進模型的帳_
_LESSONS-INBOX：新增 `measured-copy-is-not-the-committed-copy`（vc=2）；`deterministic-parser-defect-billed-as-model-failure` vc 1→2；`italic-span-defeats-url-escaping` 補 (c)_

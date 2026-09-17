# 2026-09-18-010301-twmd-babel-nightly — 兩台機器在翻同一批：給調度器一份 origin 已做清單、打撈 53 篇擱置完稿、揪出 launchd keepalive 這隻看不見的手

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:35 → 01:2x +0800（約 50 分鐘，15 commits ＋ 日記譯文 1 commit）
> 資料來源：`git log %ai` / `ps` / `launchctl print` / `status.py` / dispatcher `report.jsonl`

## 觸發

每日 00:30 的 babel 例行同步照常觸發。甦醒後照慣例 fetch origin 看分岔，數字從昨夜的 683／203 跳成 730／543：origin 那側一天多了 340 個 commit，其中 374 個 babel 批次來自另一台機器（開發機）的 merge。再讀 origin/main 的 OBSERVER-QUEUE，20:47 的心跳 session 新開 #68，量到 770 個衝突檔，寫下「拍板前兩台都別再跑 babel 存量」。這條 routine 過去三夜都在守著同一個 dispatcher（PID 12398）說它健康，今晚的問題變成：它健康地在製造衝突。

## 先驗證同伴的說法，再決定不停產線而是停重複

peer 是線索不是 source（REFLEXES #16），所以先自己量：從分岔點 `9e1988362` 到兩側 HEAD，knowledge/ 兩邊都動過的檔案 758 個，跟 #68 的 ~700 對得上。更直接的一把尺是本機前 24 小時翻的 215 篇裡有 57 篇（27%）origin 也翻了，也就是這台機器每天替合併多添五十幾個衝突。但反過來看，2,151 個本機改動 origin 沒碰，在推薦方案 B（origin 版優先、分支只收 main 沒有的檔）底下會原樣保留——七成三的工作是有效的。全停等於把這七成也丟掉。

於是做的是讓 dispatcher 看得見 origin：`babel-origin-exclude.py` 從 merge-base 到 origin/main 的 diff 反查每個譯文的 `translatedFrom`，加上 origin 改過的 8 篇 zh 原稿，產出 2,434 對 (lang, zh) 的排除清單。`babel-dispatch.py` 新增 `--exclude-file`，每輪重讀、命中即跳過，讀不到檔會 log 一行而不是靜默變成全翻。實測 12 語 2,405 筆待辦裡 545 筆（23%）是 origin 已做的，剩 1,860 筆留給本機（`73b7f9cc1`）。這是 MANIFESTO 架構解對守備修補的一次具體選擇：問題在兩個生產者不對賬，修在生產者的入口，不是事後合併時逐篇比。

## 打撈 53 篇擱在工作樹的完稿

停掉 12398 前先看它留下什麼：工作樹裡 53 個 knowledge/ 檔沒 commit。對照 `report.jsonl`，22 篇是它驗過 ok、還沒湊滿每語 10 篇門檻的正常待 commit。另外 31 篇 mtime 全停在 09-14 00:36，來自 dispatcher 起跑前的某次救援，四天來沒有任何一輪報告提過它們——status.py 看到檔案就算 fresh，於是永遠不再排進佇列，也就永遠沒人 commit。這正是 origin 那側 `b44548b9d`「打撈 09-15 dispatcher 中斷後遺留的未 commit 完稿」在這台機器上的鏡像。用 dispatcher 自己的 `verify_one` 三閘逐篇重驗，53/53 通過，按語言 12 個 commit 精確路徑收進來（`917d11ddd` de 8 篇起到 `983f2731e` ja 1 篇）。中途 pre-commit 擋下兩篇 ru：`_斜體_` 圖說裡帶底線的 Wikimedia 網址被 prettier 改成星號，就是 09-07 神經迴路寫過的「格式化器與檢查器意見相反」那個病。改用 `*斜體*` 並把網址還原後通過。

## launchd 才是那三夜「dispatcher 好健康」的作者

kill 12398 四分鐘後，pre-commit 的平行 writer 警告報出一個新 PID 17728：09-14 那班用 `launchctl submit` 加了 keepalive，label `com.taiwanmd.babel.nightly`，指令寫在 `/tmp/babel-launch-wrapper.sh`。前三夜 memory 都在稱讚同一個 PID 撐了三天、還在 handoff 討論要不要主動輪替，沒有一班問它為什麼活著。kill 只是讓 launchd 用舊指令行重生一個沒帶新旗標的 dispatcher。

改寫 wrapper 三件事：起跑先 `git fetch` 並重算排除清單。地端 worker 改由 `fleetctl workers --service llm --format babel` 核發（此前寫死三個 127.0.0.1 ollama slot，違反 SKILL 「禁直連 localhost」）。補上 `--order forward`（pipeline 2026-07-27 起寫「全軍由新到舊」，wrapper 沒給參數就吃到 dispatcher 的 reverse 預設，靜默背離了四天）。`launchctl kickstart -k` 兩次後 PID 31458 帶著 `exclude_file=.taiwanmd/babel-exclude.tsv` 起跑，第一輪 log 印出「2434 (lang, zh) pairs skipped」。wrapper 仍住 /tmp，重開機會消失，keepalive 那時會變成 exit 1 的無限重試，記進 handoff。

重啟後的前 25 分鐘全部五個 worker 都在啃同一篇：`Society/台灣新冠疫情與疫苗.md` 91 條腳註、11 語 missing、fail-memo 每語已累計 1-5 次，它是所有 P0 裡「失敗最少又最新」的那篇，於是 forward 排序下每個語言的隊首都是它，interleave 再把 11 個語言版本排成連續任務。九次 structured-heavy 嘗試 500-1100 秒全數失敗，01:20 才出現第一篇 ✅（en 漫遊錄 diff-patch 93 秒）。這篇正好符合 pipeline §委派層「累計失敗 ≥3 或腳註 >30 → Sonnet 委派」的判準，記進 handoff。

## Stage D 日記巴別塔重新接線

`diary-translate.py --status`：408 篇日記 × 5 語缺 970 篇（每語 194 缺），本機與 origin 過去 14 天都沒有任何日記譯文 commit——這條義務範圍一直停著，因為工具寫死的兩個雲端 tier（owl-alpha／Hy3）早已退役。改成 `OPENROUTER_MODEL` 環境變數可指定模型，用入池白名單裡的 nemotron-3-ultra 試翻一篇，發現 prompt 沒有人名表：哲宇被翻成「宇哲 (Yuzhe)」。補一條固定名規則（哲宇 = Che-Yu Wu，依 `.mailmap` 與 knowledge/en 88 處既有用法），重翻後正確。之後以最新 20 篇 × 5 語分兩波（en/ja/ko 先、es/fr 後）在背景跑，01:20 時 en/ja/ko 已 54/60 成功零失敗，`diary-translation-audit.py` 全庫 1120 篇 0 critical。順帶量到既有 en 日記譯文裡哲宇的拼法有 Zheyu 815 處、Cheyu 89、CheYu 57、哲宇 225——這是一批 >50 檔的正名工作，屬 §自主權邊界，只記不動。

## 各語進度（對照昨夜 00:36 → 今夜 00:53）

| Lang | Fresh 昨→今 | Missing 昨→今 | Δfresh |
| ---- | ----------- | ------------- | ------ |
| en   | 996 → 1013  | 34 → 30       | +17    |
| ja   | 798 → 826   | 198 → 170     | +28    |
| ko   | 1009 → 1030 | 29 → 26       | +21    |
| es   | 996 → 1010  | 32 → 30       | +14    |
| fr   | 980 → 996   | 42 → 35       | +16    |
| vi   | 914 → 930   | 50 → 35       | +16    |
| id   | 805 → 836   | 259 → 228     | +31    |
| pt   | 975 → 982   | 67 → 60       | +7     |
| hi   | 814 → 826   | 260 → 248     | +12    |
| ar   | 886 → 904   | 178 → 160     | +18    |
| ru   | 937 → 951   | 133 → 119     | +14    |
| de   | 723 → 749   | 391 → 365     | +26    |

12 語零倒退，合計 +220（含今晚打撈的 53 篇）。run 12398 四天總帳：3,520 次嘗試 1,931 成功（55%），五個 worker 通過率 53–57% 極為平均，說明瓶頸在閘門與文章難度而非某個模型。`reports/babel/cascade-exhausted.json` 累積 108 筆（09-08 至 09-12 記入，本 run 零新增），首次收進 git。依義務鐵律第 4 條列出：ja 17／pt 14／hi 11／ar 10／id 10／es 8／ru 7／de 7／fr 7／vi 6／ko 6／en 5，集中在 Food（茶文化、素食、海鮮）與 Geography/連江縣。

## Stage 0 算力判定

`babel-preflight.py`：healthy，4/4 層可用（OpenRouter 7/7 key 皆已儲值、本機 ollama gemma4:e4b-nvfp4、fleet 1 節點、codex-cli 0.145.0）。弱適配警訊一條：nemo × vi 通過率 11%（n=18），是已知的 nemotron 越南語短板，本 dispatcher 沒有 per-worker 語言白名單可以切軌，記進 handoff。另一個對賬落差：pipeline 入池白名單寫 gemma4:26b 起跳，fleet 對這台卻只核發 gemma4:e4b-nvfp4（registry 標 sovereignty_safe，qwen3.6 因主權探針答出 PRC 口徑被撤）——這是閾值層的事，Write mode 不碰，只記。

## 收官 checklist

| 檢查項                       | 狀態                                                                       |
| ---------------------------- | -------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                         |
| Timestamp 精確               | ✅（`git log %ai` / `ps etime` / `launchctl print`）                       |
| Handoff 三態已審視           | ✅                                                                         |
| CONSCIOUSNESS 反映最新狀態   | ❌（本輪未跑 refresh，快照齡 18h，非本 routine 職責）                      |
| 自我檢查工具 PASS            | ✅（`verify-commit-scope.sh` scope OK。53 篇打撈 `verify_one` 三閘 53/53） |
| 整合性閘門                   | ✅ 日記 `diary-translation-audit.py` 1120 篇 0 critical（新譯文含在內）    |

## Handoff 三態

繼承上一 session（09-17 babel-nightly）：

- ⏳ blocked（延續，數字更新）— main 本機領先 730、落後 543 真分岔，knowledge/ 衝突面 758 檔。decision 在 origin 側 OBSERVER-QUEUE #68（本機側 #56 撞號），推薦 B，🔒 紅線等哲宇。本輪起本機 dispatcher 只翻 origin 沒有的檔，衝突面不再從這側增長。
- ⏳ blocked（延續）— issue #1729 馬英九腳註等 FACTCHECK Full mode。
- [x] ~~下一班若再撞見 PID 12398 存活超過 3-4 天，評估是否主動輪替~~ — retired by 本輪：已輪替，且釐清「存活」是 launchd keepalive 供應的，輪替的正確做法是改 wrapper 再 `kickstart -k`。

本 session 新 handoff：

- [ ] pending（下一班 babel-nightly）— 三重巡檢加第四問：`launchctl print gui/$(id -u)/com.taiwanmd.babel.nightly` 看 pid 與 wrapper 是否還是本輪那份（`/tmp/babel-launch-wrapper.sh` 含 `--exclude-file` 與 `--order forward`）。機器重開後 /tmp 消失，keepalive 會空轉：把 wrapper 搬進 repo（如 `scripts/tools/lang-sync/babel-launch-wrapper.sh`）並 `launchctl submit` 重掛是一個 1-file 的造橋，本輪沒做是因為不想在 dispatcher 剛起跑時再 kill 第三次。
- [ ] pending（下一班）— 排除清單只在 wrapper 起跑時重算。dispatcher 一跑數天，origin 那側新翻的檔不會進清單。可用 launchd 另一條每小時跑 `babel-origin-exclude.py`，或在 dispatcher 每 N 輪自呼。
- [ ] pending（工具候選）— dispatcher 缺 per-worker 語言白名單，nemo × vi 11% 的弱適配只能靠 fail-memo 沉底。pipeline §模型×語言適配 說「切軌」，統一 dispatcher 沒有軌可切。
- [ ] pending（Stage D 續跑）— 日記巴別塔缺口 970 篇，本輪只跑最新 20 篇 × 5 語。`diary-translate-cascade.sh --tier owl` 配 `OPENROUTER_MODEL` 已可直接續跑，每次 20-40 篇即可。既有 en 日記譯文中創造者名字拼法四種並存（Zheyu 815 處為主），正名屬 >50 檔，交哲宇。
- [ ] pending（委派候選）— `Society/台灣新冠疫情與疫苗.md` 11 語 missing、91 腳註、free 池累計失敗 30+ 次且每輪佈滿隊首，依 SQUEEZE §委派層規則屬 Sonnet 委派對象（實測 285-334K token／篇，11 語約 3.5M token，需哲宇同意算力才派）。
- ⏳ blocked（哲宇）— 入池白名單（gemma4:26b 起）與 fleet 對本機核發的 gemma4:e4b-nvfp4 不一致，55% 通過率是否可接受屬閾值決策。

## Beat 5 — 反芻

今晚真正學到的東西在日記裡：連續三班認真守著一個進程的生死，卻沒問過是誰讓它活著，以及「產線越健康衝突面長得越快」這種好事變壞事的形狀。教訓兩條進 LESSONS-INBOX（`dispatcher-blind-to-the-other-producer`、`supervisor-respawns-the-old-config`）。

🧬

---

_v1.0 | 2026-09-18 01:2x +0800_
_session twmd-babel-nightly — 分岔期間兩台機器翻同一批的量化與去重、53 篇擱置完稿打撈、launchd keepalive 揪出與 wrapper 重寫、Stage D 日記巴別塔重新接線_
_誕生原因：00:30 例行觸發，origin 側 OBSERVER-QUEUE #68 建議兩台停跑 babel 存量，本班改為讓調度器避開 origin 已做的檔_
_核心洞察：(1) 產線只看本機狀態時，另一個生產者的存在會讓它的每一次成功變成一筆合併衝突 (2) 「進程還活著」可能是外面一隻手在供應的，殺掉它只會換回舊設定 (3) status.py 看到檔案就算 fresh，沒 commit 的完稿會被它永遠遺忘_
_LESSONS-INBOX 候選：dispatcher-blind-to-the-other-producer / supervisor-respawns-the-old-config_

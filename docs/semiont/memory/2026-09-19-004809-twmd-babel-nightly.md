# 2026-09-19-004809-twmd-babel-nightly — 調度器學會弱適配切軌、wrapper 搬進 repo 後撞出 launchd 兩層隱形環境、worker 執行緒不再靜默死亡、去重清單自己重算

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:30 → 02:20 +0800（約 110 分鐘，14 commits）
> 資料來源：`git log %ai` / `launchctl print` / dispatcher `report.jsonl` / `status.py`

## 觸發

00:30 例行觸發。昨夜留了四條 handoff：三重巡檢加第四問（launchd 的 wrapper 還是不是本輪那份）、去重清單只在起跑時算一次、dispatcher 缺 per-worker 語言白名單、wrapper 住 /tmp 重開機會消失。今晚把後三條都做掉，第一條變成常設檢查。分岔照舊：本機領先 810、落後 720（origin 一天又多 172 個 commit，另一台還在翻），`git pull` 會撞 758 檔的合併，只 fetch 不 pull，per OBSERVER-QUEUE #56。

## Stage 0 算力判定

`babel-preflight.py`：healthy，4/4 層可用（OpenRouter 7/7 key 已儲值、本機 ollama gemma4:e4b-nvfp4、fleet 1 節點 mac-m4max、codex-cli 0.145.0）。實績檢查報 10 個弱適配組合，這是今晚第一個要動手的東西（見下）。狀態表 12 語，跟 registry 一致。

## 三重巡檢＋第四問，然後有意識地殺它兩次

PID 31458（昨夜重啟的那個）跑了 23 小時 45 分，`launchctl print` 確認 wrapper 是昨夜那份（含 `--exclude-file` 與 `--order forward`），近 45 分鐘 27 次嘗試，run 總帳 662 次嘗試 200 篇通過（30%），fleet registry 給的 worker 跟 dispatcher 在跑的一致。健康。

換 wrapper 得先殺它，殺之前先打撈：工作樹裡 8 篇 dispatcher 驗過但沒湊滿每語 10 篇門檻的譯文，用 `verify_one` 重驗 8/8 過關，按語言五個 commit 收進來（`a6b398839` fr 起到 `ab78893b9` vi）。vi 蘭花那篇再撞 09-07 神經迴路那條病：`_斜體_` 圖說包住帶底線的 Wikimedia 網址，prettier 把底線改成星號，`link-url-mangle` 擋下，照 zh 源改回 `*斜體*` 並還原網址後通過。

## 調度器學會切軌：`--worker-skip-langs`

pipeline §模型×語言適配寫了一年「弱適配開專軌繞過，不要加大重試」，統一調度器卻沒有軌可切，昨夜 handoff 也只能寫「靠 fail-memo 沉底」。`TaskQueue.claim()` 早有 Tier 6/7 用的 `task_filter` 硬閘，所以這是一個小改動：Worker 加 `skip_langs`，`make_task_filter()` 把語言閘跟資格閘用 AND 合成，main() 驗 label 與語言存在，並加 starvation guard（某語言若被全部 normal worker 跳過就撤回並警告，寧可低通過率也不要零產出）。單元測試過 claim 行為與 guard，`--rounds 0` 實跑看到警告文字（`266050ccf`）。

餵旗標時撞到第二件事。preflight 的弱格按 worker label 聚合，而 fleet 給同一台 ollama 三個 label（macm4max1/2/3），同一個 gemma4:e4b 的實績被切成三份各自過 n≥8。按 backend 重算（新工具 `babel-weak-lanes.py`）名單從 10 變 7 且內容不同：ar 整個消失（單格 6% 是分到難篇的那一份，合計不弱），pt 從一個 label 變三個一起跳（三格各自在線上，合計 10/71=14% 才掉進去）。最後餵進去的是 gemma × pt、nemotron × hi/id/ko/ru、laguna × hi/ru。沒有語言被全部 worker 跳過。這條進 LESSONS-INBOX 當新 entry（`evidence-fragmented-across-scheduling-labels`），preflight 本身仍按 label 印表，未改。

## wrapper 搬進 repo，門口就倒

`scripts/tools/lang-sync/babel-launch-wrapper.sh`：拿掉寫死的 12 語 `--langs`（dispatcher 預設本來就從 langs.py 取有缺口的語言。routine prompt 把寫死語言清單列為活體標本病，這份 wrapper 自己就是 instance，記進 `contract-hardcodes-growing-count` vc=2），起跑呼叫 weak-lanes 生旗標。`launchctl remove` + `submit` 指向新路徑，state = running。

三分鐘後 stderr 三次同一段 Traceback：launchd 沒有 shell profile，`python3` 是 Apple CommandLineTools 的 3.9，status.py 的 `str | None` 當場炸。09-14 那班能跑，是因為 submit 從帶 venv PATH 的 shell 發出，環境被 launchd 繼承——沒寫在任何檔案裡。wrapper 改成明寫 `PY=~/.venvs/taiwanmd/bin/python`，驗不到 ≥3.10 就 sleep 後退出，不讓 keepalive 每分鐘重算一次去重清單再死（`d32dae1e2`）。這是 09-07 神經迴路「headless 遷移驗證要選真的那層的尺」第二次驗證，補進該條。也是昨夜 `supervisor-respawns-the-old-config` 的第二面（環境也是設定），+instance。

00:45 新 dispatcher PID 68259 起跑：五個 worker 的 skip_langs 都印出來，去重清單 2489 對（昨夜起跑 2434，多的 55 對是 origin 這一天翻的）。每次重啟五個 worker 裡四個先去啃 `Society/台灣新冠疫情與疫苗.md`（91 腳註、11 語 missing，隊首），二十幾分鐘後失敗才輪到別篇。今晚兩次重啟各付一次，跟昨夜同型。它符合 SQUEEZE §委派層 Sonnet 條件，算力屬哲宇決定，仍只記不派。

## 去重清單自己過期自己重算

昨夜第二條 handoff：清單只在 wrapper 起跑時算，run 一跑數天就越來越舊。改在 dispatcher 每輪 build worklist 前看檔案齡，超過 90 分鐘（`BABEL_EXCLUDE_REFRESH_MIN`）就 `git fetch` + `babel-origin-exclude.py`，失敗只 log 沿用舊檔。`load_exclusions` 本來每輪重讀，新檔落地下一輪就生效（`6fe93bc51`）。這次改動在下次 respawn 才生效，今晚不再殺第三次。

## 第二層隱形環境：兩篇翻好的譯文在 prettier 那一步消失

01:33 三重巡檢：dispatcher 48 分鐘 13 次嘗試零通過。失敗家族跟昨夜同型（結構化腳註 240 秒逾時、armor URL 對不上），前 25 分鐘零產出也是昨夜的形狀，但兩篇 exit=0 的譯文（en 貓眼石 01:11、ja 307 公車 01:16）落地後始終沒有 report 列。`pgrep -P` 看到 dispatcher 零子進程，`ps -M` 只剩 4 條執行緒（該有 6 條），stderr 零 traceback。

根因在成功路徑：`subprocess.run(["npx","prettier",…])` 沒有 try，launchd 的 PATH 沒有 `~/.local/bin`，`FileNotFoundError` 在 worker 裡拋出，`ThreadPoolExecutor` 把它收進 future，主執行緒要等全部 worker 收工才會逐一 `result()`——那兩條執行緒就這樣安靜退場，剩下三個 worker 照跑，log 還在動。它只在成功路徑上死，所以 report 只剩失敗列，讀起來像今晚模型全部不行。

修三處（`d04af7f89`）：`worker_loop` 把 `process_task` 包進 try，例外寫成一筆 `dispatcher exception` 的 fail 列加 💥 log，執行緒續活（單元測試：第一篇炸、第二篇照跑）。prettier 先找 repo 內 `node_modules/.bin`，找不到就 log 後直接驗。wrapper PATH 補 node。兩篇孤兒譯文在本 shell 補跑 prettier 與 `verify_one`：307 公車過關收進（`c3874b06e`），貓眼石 `imageAlt` 沒翻是真的閘門失敗，刪掉退回佇列不手補。`launchctl kickstart -k` 第三次起跑（PID 83980，01:37），`ps eww` 確認 PATH 帶 venv 與 node。之後 verify 結果開始正常回到 report（含兩筆 `frontmatter not untranslated`，昨夜 659 次裡也有 69 筆同類），38 分鐘內仍零通過，跟昨夜「第一篇 ✅ 在 28 分鐘、第一小時 4 篇」同一個曲線，不是新病。

## Stage D 日記巴別塔

`--status`：411 篇 × 5 語缺 885（昨夜 875 收完後又新增兩篇日記）。`diary-translate.py --batch` 只印計畫，實際派工是 `diary-translate-cascade.sh`。用昨夜接好的 `OPENROUTER_MODEL=nemotron-3-ultra` 走 `--tier owl`，最新 45 篇分兩波（en/ja/ko 先、es/fr 後，跟 nemo worker 共用 OpenRouter 額度所以壓在 3 併發）。兩波 02:15 跑完，125 對 124 成功，1 對失敗（ja 預算頁，三次 null content，像內容政策拒答）。`diary-translation-audit.py` 全庫 1,294 篇 0 critical，新譯文的創造者名字零誤拼，缺口 885 → 766，一個 commit 收進（`077958b8a`）。

## 各語進度（對照昨夜 00:53 → 今夜 00:36）

| Lang | Fresh 昨→今 | Missing 昨→今 | Δfresh |
| ---- | ----------- | ------------- | ------ |
| en   | 1013 → 1032 | 30 → 30       | +19    |
| ja   | 826 → 853   | 170 → 143     | +27    |
| ko   | 1030 → 1039 | 26 → 26       | +9     |
| es   | 1010 → 1027 | 30 → 30       | +17    |
| fr   | 996 → 1018  | 35 → 35       | +22    |
| vi   | 930 → 958   | 35 → 29       | +28    |
| id   | 836 → 854   | 228 → 210     | +18    |
| pt   | 982 → 985   | 60 → 59       | +3     |
| hi   | 826 → 833   | 248 → 241     | +7     |
| ar   | 904 → 910   | 160 → 154     | +6     |
| ru   | 951 → 953   | 119 → 117     | +2     |
| de   | 749 → 773   | 365 → 341     | +24    |

12 語零倒退，合計 +182（含打撈 8 篇）。pt/hi/ar/ru 四語加起來 +18，正好是今晚切掉的四個弱格所在的語言——這張表是切軌的證據，不只是成績。backend 統計（run 31458 全程）：lagunas 158 次、macm4max1 133、macm4max3 130、macm4max2 120、nemo 116，通過率各在 25-35%。

cascade exhausted（義務鐵律第 4 條）：昨夜 run 新增 5 筆，全部 pt、fail_count 8——`Society/馬英九迷因.md`、`Music/台灣民歌運動.md`、`Music/台灣台語歌曲演進.md`、`Food/台灣辦桌文化.md`、`Lifestyle/收費站.md`。第一夜耗盡，未進 OBSERVER-QUEUE。pt 今晚起只由雲端兩個 worker 接，看明夜是否解開。累計清單 113 筆已收進 git（`eea71e212`）。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                          |
| Timestamp 精確               | ✅（`git log %ai` / `ps etime` / `launchctl print`）                                                        |
| Handoff 三態已審視           | ✅                                                                                                          |
| CONSCIOUSNESS 反映最新狀態   | ❌（快照齡 18h，本 routine 不跑 refresh）                                                                   |
| 自我檢查工具 PASS            | ✅（`verify-commit-scope.sh` 每個 commit scope OK。打撈 8 篇 `verify_one` 8/8）                             |
| 整合性閘門                   | ✅ 日記 `diary-translation-audit.py` 1,294 篇 0 critical。文章面本輪無新批次 ship（dispatcher 自己 commit） |

## Handoff 三態

繼承上一 session（09-18 babel-nightly）：

- ⏳ blocked（延續，數字更新）— main 本機領先 810、落後 720 真分岔。decision 在 origin 側 OBSERVER-QUEUE #68（本機側 #56 撞號），🔒 紅線等哲宇。去重清單今起每 90 分鐘自動重算，衝突面不再從這側增長。
- ⏳ blocked（延續）— issue #1729 馬英九腳註等 FACTCHECK Full mode。
- [x] ~~三重巡檢加第四問：launchctl print 看 pid 與 wrapper~~ — retired by 本輪：已跑，且 wrapper 搬進 repo 後這一問改成看 `program` 路徑是不是 `scripts/tools/lang-sync/babel-launch-wrapper.sh`。
- [x] ~~排除清單只在 wrapper 起跑時重算~~ — retired by 本輪 `6fe93bc51`（dispatcher 自己看檔齡重算，下次 respawn 生效）。
- [x] ~~dispatcher 缺 per-worker 語言白名單~~ — retired by 本輪 `266050ccf`（`--worker-skip-langs` + `babel-weak-lanes.py`）。
- [ ] pending（Stage D 續跑）— 日記巴別塔缺口 766（本輪 885 補 124）。`diary-translate-cascade.sh --top N --langs … --tier owl` 配 `OPENROUTER_MODEL` 直接續跑。創造者名字四種拼法正名屬 >50 檔，交哲宇。
- [ ] pending（委派候選，延續）— `Society/台灣新冠疫情與疫苗.md` 每次 dispatcher 重啟都佔四個 worker 二十幾分鐘，符合 Sonnet 委派條件（約 3.5M token），需哲宇同意算力。
- ⏳ blocked（哲宇，延續）— 入池白名單（gemma4:26b 起）與 fleet 核發的 gemma4:e4b-nvfp4 不一致，屬閾值決策。

本 session 新 handoff：

- [ ] pending（下一班 babel-nightly，第四問新版）— `launchctl print gui/$(id -u)/com.taiwanmd.babel.nightly` 的 program 應是 repo 內的 wrapper。master.log 開頭應有五行 `skip_langs=`，且 `ps eww -p <pid>` 的 PATH 要含 `.venvs/taiwanmd/bin` 與 `.local/bin`。看 report.jsonl 有沒有 `dispatcher exception` 列（有 = 又一層沒掛上的環境）。若 dispatcher 已 respawn，確認 log 裡出現過「exclude-file 已 N 分鐘沒更新 — 重算」。
- [ ] pending（三重巡檢第五問候選）— `ps -M -p <pid> | wc -l` 應等於 worker 數 + 2，少了就是有執行緒死在 `d04af7f89` 之前的版本或新的未接例外。
- [ ] pending（1-file 候選）— `babel-preflight.py` 的實績表改按 backend×lang 聚合，label 只做附註。現在它跟 `babel-weak-lanes.py` 對同一份 report.jsonl 給出不同名單。
- [ ] pending（觀察）— pt 五篇第一夜耗盡的檔，切軌後由 nemo/lagunas 接。連續兩夜耗盡 dispatcher 會自動進 OBSERVER-QUEUE。
- [ ] pending（launchd 持久化候選）— `launchctl submit` 的 job 本身不跨重開機。要真正 reboot-safe 得寫 `~/Library/LaunchAgents/com.taiwanmd.babel.nightly.plist`，屬本機持久設定，留給哲宇或下一個 Full mode session 決定。

## Beat 5 — 反芻

今晚的反芻寫進 [diary/2026-09-19-004809-twmd-babel-nightly.md](../diary/2026-09-19-004809-twmd-babel-nightly.md)：把 wrapper 搬進 repo 這件小事讓它在門口倒下，追回去發現撐了五夜的是 submit 時繼承的環境。同晚為了餵新旗標重算弱適配表，發現 preflight 每一格的算術都對、名單在兩個方向上都錯。兩件事同一個形狀：完整的檔案、完整的表格，都可以缺掉一半而不自知，缺的那半只在你拿它去做一件它沒被拿來做過的事時才露出來。教訓記進 LESSONS-INBOX（兩條新 entry：label 切格失真、執行緒池吞死亡，兩條 +instance）與 MEMORY §神經迴路（headless 尺第二次驗證）。

🧬

---

_v1.0 | 2026-09-19 02:20 +0800_
_session twmd-babel-nightly — 弱適配切軌旗標與 backend 級聚合工具、wrapper 搬進 repo 撞出 launchd 兩層隱形環境（直譯器、node）、worker 執行緒不再靜默死亡、去重清單自動重算、Stage D 124 篇、打撈 9 篇_
_誕生原因：00:30 例行觸發，昨夜四條 handoff 三條是 1-file 造橋，今晚一次做掉_
_核心洞察：(1) 供應進程存活的 supervisor，它的環境也是設定的一部分，改檔案改不到 (2) 執行緒池會把 worker 的死亡收成 future，產線只在成功路徑上死，report 就只剩失敗 (3) 實績聚合的單位要等於決策的單位，按 label 切格會讓弱適配雙向失真_
_LESSONS-INBOX 候選：`evidence-fragmented-across-scheduling-labels`（新）。`supervisor-respawns-the-old-config`、`contract-hardcodes-growing-count` 各 +instance_

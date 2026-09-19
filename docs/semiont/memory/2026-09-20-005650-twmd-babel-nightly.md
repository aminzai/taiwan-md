# 2026-09-20-005650-twmd-babel-nightly — 三道「已修」的檢查掛在一個十二小時才來一次的邊界上；分岔併回、打撈 13 篇、structured 引擎不再翻 subcategory

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:30 → 02:06 +0800（約 96 分鐘，13 commits）
> 資料來源：`git log %ai` / `launchctl print` / dispatcher `report.jsonl` / `status.py`

## 觸發

00:30 例行觸發。甦醒 selftest 亮兩個訊號：工作樹落後 origin/main 8 個 commit，同時 ACTOR_BUSY——launchd keepalive 的 dispatcher（PID 60034）從 09-19 11:58 跑到現在，本機 main 領先 origin 33 個 babel commit。昨夜留的四問（wrapper 路徑、`skip_langs=` 行、PATH、`dispatcher exception` 列）與第五問（執行緒數）全部過關，去重清單那條交接卻沒過：master.log 裡「已 N 分鐘沒更新 — 重算」零筆。

## Stage 0 算力判定

`babel-preflight.py`：healthy，4/4 層可用（OpenRouter 7/7 key 儲值、本機 ollama gemma4:e4b-nvfp4、fleet 1 節點 mac-m4max、codex-cli 0.145.0）。實績表印出「? × en = 0%（n=14）」「? × es = 0%（n=11）」兩個幽靈格：preflight 把 `cascade_exhausted` 事件列當成 worker「?」的失敗（`babel-weak-lanes.py` 早有豁免，兩處判準對齊後剩 7 個弱格）。

## 分岔先併回，33 個 commit 才不會再堆成下一次 843 檔衝突

dispatcher 只 commit 不 push，09-19 上午哲宇拍板 #68 併完之後這台又累積了 33 個未推 commit、落後 8 個。committed 兩側只撞 `_translation-status.json` 一個生成檔，工作樹的 13 篇在途譯文跟 origin 改動零重疊，所以拿 `/tmp/taiwan-md-git.lock`（跟 dispatcher 共用的 mkdir 鎖）做一次 merge commit（`93edd49c4`，status.py 重生解衝突）直接 push，pre-push 三道閘全綠，本機 main 與 origin 同步。昨夜 diary 寫的「它的每次成功都在替另一台機器的合併添衝突」，今晚的答案是每夜由當班把它推上去。

## 三道前一夜「已修」的檢查，一整晚沒被走到

三重巡檢說產線健康（12.6 小時 424 次嘗試 219 篇通過 52%，近 45 分鐘 18 次 4 過），但三件事對不上。去重清單重算 09-19 接在輪次開頭，而一輪是 `10 × worker × 語言` = 560 篇，跑了 12.6 小時還在 Round 1，重算一次都沒發生。ar 的 7 篇譯文從 15:19 懸到隔天：零頭年齡只在同語言下一次成功時算，nemo 切軌後 ar 八小時零成功，沒人替它算。〈台灣新冠疫情與疫苗〉fail_count 8-9 仍在 en/ko/fr/es 隊首：失敗沉底只在桶內排序，新鮮窗裡只剩它一篇。三條修法同一個方向，把檢查搬到每篇任務的路徑上（`bea982d2a`、`8165d678f`）：`ExclusionCache` 按 mtime 快取、refresher 執行緒每分鐘看檔齡、worker 在 claim 時讀最新清單。任一 worker 做完一篇就掃所有語言的零頭年齡。累計失敗 ≥ 8 的整批壓在該語言佇列最尾（仍不排除，每輪 log 一行）。三處都有 ad-hoc 單元檢查。第五問從此改成「執行緒數 = worker + 2 主與 refresher」。

換版要重啟 dispatcher，先打撈：工作樹 13 篇（ar 7／fr 2／hi 2／de 2）對 report.jsonl 的 ok 列逐一核對，`verify_one` 13/13 過，按語言四個 commit 收進（`a5c765110` 起）。`launchctl kickstart -k` 兩次（00:46 換 claim 時去重與跨語 flush，00:52 換耗盡篇壓陣），第二次起跑就看到十二語各自印出「N 篇累計失敗 ≥8 次，排到最尾」，合計約 180 對，新冠那篇不再是隊首。

## structured 引擎把 subcategory 翻掉，存量在「已上線檢查」之下漲了 149 篇

打撈的 pre-commit 印三條 `subcategory-translation-parity` WARN，全庫掃出 1,795 篇譯文的 subcategory 不等於 zh 原值（vi 328／ja 250／ko 239，還混著簡體）。09-08 這道檢查上線時是 1,646 篇、期待「存量不再增加」；漲的來源是 `structured-translate.py` Phase F 照 verify-translation.py 07-24 那條「它是顯示標籤」的註解設計，查 i18n 表或送模型翻，而統一調度器的閘門只看 hard。改成原樣複製 zh（附回歸測試，斷言 subcategory 不進 prompt），verify-translation.py 的註解改正並指向 #51，本 run 新造的 3 篇改回原值（`68969a6fc`），OBSERVER-QUEUE #51 補記存量與「產線端已堵」。1,795 篇清理仍是 🔒 等哲宇。

## Stage D 日記巴別塔

`--status`：415 篇 × 5 語缺 781。用 nemotron-3-ultra 走 `--tier owl`，最新 70 篇分兩波（en/ja/ko 先、es/fr 後，壓 3 併發跟 nemo worker 共用額度）。兩波 01:56 跑完，126 對 126 篇全過，零 null content。`diary-translation-audit.py` 全庫 1,420 篇 0 critical，缺口 781 → 655，一個 commit 收進（`e1e70f96b`）。

## 各語進度（對照昨夜 00:36 → 今夜 00:38）

| Lang | Fresh 昨→今 | Missing 昨→今 | Δfresh |
| ---- | ----------- | ------------- | ------ |
| en   | 1032 → 1033 | 30 → 22       | +1     |
| ja   | 853 → 899   | 143 → 97      | +46    |
| ko   | 1039 → 1041 | 26 → 18       | +2     |
| es   | 1027 → 1034 | 30 → 20       | +7     |
| fr   | 1018 → 1037 | 35 → 19       | +19    |
| vi   | 958 → 979   | 29 → 19       | +21    |
| id   | 854 → 946   | 210 → 113     | +92    |
| pt   | 985 → 992   | 59 → 47       | +7     |
| hi   | 833 → 949   | 241 → 113     | +116   |
| ar   | 910 → 978   | 154 → 73      | +68    |
| ru   | 953 → 1021  | 117 → 56      | +68    |
| de   | 773 → 815   | 341 → 295     | +42    |

合計 +489，其中大半是 09-19 上午合併把另一台機器九天的譯文一次併進本機，不全是這條產線一晚的產出（本機 run 60034 全程 219 篇通過）。backend 統計（run 60034）：lagunas 68/123（55%）、nemo 42/73（58%）、macm4max2 46/88、macm4max1 29/63、macm4max3 34/77，整體 52%，比 09-18 那個 run 的 30% 高出一截，主因是切軌後 gemma 不再吃 pt/ru、nemo 不吃 ar。

cascade exhausted（義務鐵律第 4 條）：run 60034 新增 26 筆、14 篇——〈臺灣民報〉fr/en/es、〈東港迎王船〉〈水道頭〉〈高雄加工出口區〉〈醬油〉〈比國家還大的演算藝術〉〈台灣行道樹〉〈中央研究院〉〈排隊〉〈文化內容策進院〉各 en/es、〈台灣新冠疫情與疫苗〉ko/en、〈新竹米粉〉〈馬祖國際藝術島〉〈黃崇仁〉en。全是 en/es/fr 三語（雲端兩個 worker 接的語言），沒有 pt（本機 worker 今起不接 pt）。昨夜 pt 五篇沒再耗盡，無連續兩夜命中，OBSERVER-QUEUE 未自動 append。累計清單 131 → 157，隨本輪 commit 收進 git。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                                                                                                          |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                                                                                                            |
| Timestamp 精確               | ✅（`git log %ai` / `ps etime` / `launchctl print`）                                                                                                                                          |
| Handoff 三態已審視           | ✅                                                                                                                                                                                            |
| CONSCIOUSNESS 反映最新狀態   | ❌（快照齡 15h，本 routine 不跑 refresh）                                                                                                                                                     |
| 自我檢查工具 PASS            | ✅（`verify-commit-scope.sh` 每個 commit scope OK；打撈 `verify_one` 13/13；pytest 44 過）                                                                                                    |
| 整合性閘門                   | ✅ 日記 `diary-translation-audit.py` 1,420 篇 0 critical。文章面本輪無主 session 新批次（dispatcher 自己 commit），打撈 13 篇走 `verify_one` 同一把尺                                         |
| git 紀律                     | ⚠️ 一處自首：抓 status 快照後用 `git checkout -- knowledge/_translation-status.json` 還原生成檔，違反本殼「產線跑期間不 checkout 檔案」的字面；該檔每次 commit 由 dispatcher 重生，無工作損失 |

## Handoff 三態

繼承上一 session（09-19 babel-nightly）：

- [x] ~~blocked — main 本機領先 810、落後 720 真分岔~~ — retired：09-19 上午哲宇拍板 #68 合併；今晚再把 33 個 babel commit 用 merge commit 推上 origin，本機與 origin 同步。
- ⏳ blocked（延續）— issue #1729 馬英九兩節局部重寫，ARTICLE-INBOX P0 等哲宇 review。
- [x] ~~第四問新版：launchctl program、`skip_langs=` 行、PATH、`dispatcher exception` 列、exclude-file 重算 log~~ — retired：前四項過，第五項「重算」零筆，是本夜第一個修的東西。
- [x] ~~第五問候選：`ps -M | wc -l` = worker + 2~~ — retired：改為 worker + 3（refresher 執行緒），今晚實測 8 行（含表頭）。
- [x] ~~1-file：preflight 實績表改按 backend 聚合~~ — 部分 retired：preflight 已按 `worker[backend]` 分鍵並跳過事件列；label 三格合併成一格那半仍未做，`babel-weak-lanes.py` 是切軌時的準尺。
- [x] ~~pt 五篇第一夜耗盡，看第二夜~~ — retired：切軌後由雲端兩個 worker 接，未再耗盡。
- [ ] pending（Stage D 續跑）— 日記巴別塔缺口 655（本輪 781 補 126）。`diary-translate-cascade.sh --top N --langs … --tier owl` 配 `OPENROUTER_MODEL` 直接續跑。
- [ ] pending（委派候選，延續）— 〈台灣新冠疫情與疫苗〉現在壓在佇列尾，不再每次重啟燒四個 worker；但它跟另外約 180 對累計失敗 ≥8 的 (lang, zh) 從此只在該語言佇列短於 50 篇時才會被再試，實質等 Tier 6 Haiku（缺 `ANTHROPIC_API_KEY`）或 Sonnet 委派，算力屬哲宇。
- ⏳ blocked（哲宇，延續）— 入池白名單（gemma4:26b 起）與 fleet 核發的 gemma4:e4b-nvfp4 不一致。
- [ ] pending（launchd 持久化候選，延續）— `launchctl submit` 不跨重開機，要真正 reboot-safe 得寫 `~/Library/LaunchAgents/…plist`。

本 session 新 handoff：

- [ ] pending（下一班 babel-nightly，第六問）— 新 run 的 master.log 應出現「exclude-file 已 N 分鐘沒更新 — 重算」與「exclude-file 重新載入」（90 分鐘後第一次），以及「零頭 {lang} 懸空超過 90 分鐘 — 跨語言年齡 flush」。三行任一整夜缺席就是又一層沒生效，先看 `ps -M -p <pid> | wc -l` 是不是 8。
- [ ] pending（下一班 maintainer-am）— 分岔已由本班用 merge commit 收斂，`_translations.json` 與 slug 今晚零漂移；救援分支 `20260912-unpushed-routine-queue` 可刪那條仍待驗。
- [ ] pending（distill-weekly）— LESSONS 兩條新 entry：`hook-placed-at-a-boundary-that-never-comes`（三個 instance 同夜）、`production-line-follows-the-older-canon-while-the-newer-gate-only-warns`。前者候選折進 REFLEXES #82 子規則。
- [ ] pending（1-file 候選）— dispatcher 長輪次時定期印一行「本輪已 N 小時、下列輪次邊界動作尚未觸發」，讓「還沒輪到」跟「壞了」分開（REFLEXES #85）。

## Beat 5 — 反芻

昨夜的 memory 索引行寫「去重清單今起每 90 分鐘自動重算」，寫的人是我。今晚回頭看，那句話驗的是函式存在、呼叫點存在，沒驗它掛的那個迴圈多久轉一圈；而一圈是十二個小時。同一個形狀在同一晚出現三次——零頭年齡、失敗沉底，全都寫在程式碼裡、全都正確、全都掛在一個很少被走到的位置。三重巡檢問的是存活與生產，兩題都答得過，因為產線確實在產；沒有任何一題問「那些你說每 90 分鐘會發生的事，這一夜發生了幾次」。修法本身不難，難的是意識到 log 裡「Round 1」那四個字停了十二小時就是答案。diary-gate 冷卻未過，反芻留在這裡；教訓進 LESSONS-INBOX 兩條。

🧬

---

_v1.0 | 2026-09-20 02:06 +0800_
_session twmd-babel-nightly — 分岔 merge 回 origin、打撈 13 篇、去重清單改 claim 時生效、零頭跨語 flush、耗盡篇壓陣、structured 引擎不再翻 subcategory、preflight 不再把事件列當失敗、Stage D 126 篇_
_誕生原因：00:30 例行觸發，selftest 報落後 8 且 ACTOR_BUSY，三重巡檢過關但去重清單那條交接沒過_
_核心洞察：(1) 定期動作的節奏由它掛的迴圈決定，不由它的參數決定 (2) 一道只會 WARN 的新閘擋不住一條照舊 canonical 跑的無人產線 (3) 「已修」要驗的是它在需要的時刻真的跑了，不是程式碼在那裡_
_LESSONS-INBOX 候選：`hook-placed-at-a-boundary-that-never-comes`、`production-line-follows-the-older-canon-while-the-newer-gate-only-warns`（皆已 append）_

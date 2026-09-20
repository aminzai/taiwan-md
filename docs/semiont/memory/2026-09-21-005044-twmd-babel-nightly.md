# 2026-09-21-005044-twmd-babel-nightly — 一夜 535 次嘗試裡三型確定性失敗佔了六分之一，散文型腳註、imageAlt、空手 worker 三處同批次修掉

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:30 → 02:55 +0800（約 145 分鐘，13 commits）
> 資料來源：`git log %ai` / `launchctl list` / dispatcher `report.jsonl`、`master.log` / `status.py`

## 觸發

00:30 例行觸發。甦醒 selftest 十一項全綠、工作樹與 origin 同步、ACTOR_BUSY：launchd keepalive 的 dispatcher（PID 33830）從 09-20 00:52 跑到現在，本機領先 origin 8 個 babel commit。前夜第六問三行全在：`exclude-file 已 90 分鐘沒更新 — 重算` 16 次、`重新載入` 16 次、`跨語言年齡 flush` 71 次，`ps -M` 8 行，十二語起跑各印一行「累計失敗 ≥8 次排到最尾」。掛在輪次邊界上的三道檢查，搬到任務路徑後真的每九十分鐘跑一次了。

## Stage 0 算力判定

`babel-preflight.py`：healthy，4/4 層（OpenRouter 7/7 key 儲值、本機 ollama gemma4:e4b-nvfp4、fleet 1 節點 mac-m4max、codex-cli 0.145.0）。實績表按 label 印三個弱格（macm4max1×es 12%、macm4max3×fr 12%、nemo×ar 0%），`babel-weak-lanes.py` 按 backend 聚合後只剩 nemo×ar，切軌旗標維持一條。順手查了一件事：gemma 本 run 對 es 3/28、fr 3/24 都在 15% 以下，但兩日窗把前一個 run 的較好成績算進來，所以沒響。這是工具設計的視窗選擇，沒動門檻。

## 一個 23 小時的 run，每三次嘗試才過一次，而三分之一的失敗是確定性的

run 33830 收官數字：535 次嘗試 161 篇通過（30%），lagunas 48/161、macm4max2 34/97、macm4max3 30/116、macm4max1 27/89、nemo 22/77。按引擎拆開才看得出病：whole 115/222（52%）、patch 20/76、structured-heavy **20/221（9%）**。structured-heavy 燒掉 62.6 個 worker 小時換 20 篇，whole 用 19.5 小時換 115 篇，每一篇 structured 成功背後是三個小時的 GPU 或雲端時間。

structured 的失敗裡有 36 次死在 Phase N「title contains markdown/newline」。追到 `extract_footnote_defs` 的最後一個分支：腳註不是 `[標題](URL) — desc` 開頭時（「報時光：[標題](URL)」、句中「同場另見[活動官方頁](URL)」、方括號時間碼「[1:00:07]」），它用第一個 URL 把文字切成 title 跟 desc，title 帶著半個連結、URL 之後整段丟掉，組回來是巢狀壞連結，驗證器擋下是對的。全庫 158 篇 ≥30 腳註的 zh 稿裡 20 篇有這型腳註（台灣網路社群遷徙史 44/47 條、電競 32/32、台灣體育發展與奧運 31/55、比國家還大的演算藝術 25/85），它們在 structured 引擎從 07-25 pilot 起就永遠過不去，每次 130 到 750 秒。改成整條當 desc 送翻、內嵌連結走 @@LINKn@@ 保護、組回原樣（`244baf079`）。17,489 條腳註定義跑過身分回圈，380 條散文型逐字還原、URL 多重集零遺失。同一個 commit 順手把「N chunk(s) failed」的中止訊息補上每個失敗 chunk 的最後一輪問題——dispatcher 不帶 `--metrics-out`，exit 1 時 metrics 也不落檔，一夜 66 次 chunk 失敗在 master.log 只剩一行數字。

第二型是 imageAlt（`6fc5f80e6`）：verify-translation 第 13 檢查把它跟 title、description 同列不得留原文，structured 跟 patch 兩條引擎都把它當 passthrough 複製 zh 值。zh 有 imageAlt 的 48 篇、223 個譯本缺這欄，一夜 36 次拒收全在同一格，跟 09-20 subcategory 那條是同一個病反著長。第三型是 patch 引擎撞既有債：譯文 tags 六成以上還是 zh 原字時「語意沒變就沿用舊值」會把債原封組回去被擋，五次拒收才升級整篇。既有譯文根本是英文（OBSERVER-QUEUE #53 那批）時局部 patch 只是在英文上補幾段韓文。前者改走 LLM frontmatter 路徑，後者用 verify_one 第一關同一把尺判不適用直接退 exit=2。三型合計一夜至少 86 次確定性失敗，佔 535 次的 16%，而 report 把它們寫成「no output written」與「verify=1」，跟真正的模型失敗記在同一個計數器裡沉底。

修完之後新 run 的第一篇 structured 就撞回來兩次，證明修補本身也要進產線驗過才算數：純文字引註（「吳哲宇口述值，2026-08-16 Openbook 對談…」）沒改仍走「整條當 title」，模型讀了新 prompt 的散文規則把長 title 搬進 desc、title 交空，15 條 title empty，乾脆讓沒連結也沒 URL 的引註一併走散文（`34b54dd18`，散文型 680 條逐字還原）。接著外送專法 de 在 Phase N 第三批撞 Ollama 240 秒兩次——散文整條進 desc 後一批 15 條有 3,500 字，加字元預算 2,000 讓長引註多拆幾批（`e613f1cb0`）。第三個是 patch 引擎：外送專法五語 patch 全被同一個 `/pt/Economy/` 大寫 category 擋下，dispatcher 對整篇路徑先跑三支安全 fixer 再驗，patch 引擎自己驗自己拒收從來輪不到它，接進去（`bb66e275f`）。之後 62 條引註的外送專法在 structured 過了 Phase N，敗在 Phase B 的 chunk——這回 master.log 印得出敗在哪：一段 H2 沒翻、印尼文比率 4.07 超過 4.0 上限、少一個 `[^47]`、URL 的 percent-encoding 被改了一碼。

## 三張 GPU 空等雲端 worker 磨尾巴

report 的 `last ts` 一列一看：三個 gemma worker 最後一筆都在 22:28 到 22:30，之後兩個半小時只有 lagunas 跟 nemo 在動，ollama `/api/ps` 空的。追到 `worker_loop`：claim 不到東西就 `return`。一輪是每語言 10×worker 篇、十二語 564 篇，地端三個 worker 切軌跳過 pt/ru，把其他十語吃完後退出，剩下 32 篇 pt/ru 由兩個雲端 worker 以每篇 10 到 35 分鐘磨，還要三到五小時輪次才結束。切軌讓誰能接哪種語言不再對稱，這條尾巴每一輪都會長出來，三重巡檢看不到：進程活著、log 在動、report 也有新列。

加了 `topup_queue`（`fbee50b7a`）：worker 空手時重算 status，對它接得了的語言各撈最多十篇沒排過、不在途的，走同一條 prepare-batch 直接 extend 進佇列。Tier 6/7 worker 不補貨，補貨例外只記一行不讓執行緒消失。四條單元測試。換版要重啟：先打撈工作樹三篇（ru 2、pt 1，verify_one 3/3）按語言兩個 commit 收進，`launchctl kickstart -k`，新 run 98122 00:58 起跑，kill 瞬間 nemo 剛落地的一篇 pt 也驗過打撈（`eb70dbd55`）。新 run 的 wrapper 這次只給 nemo=ar 一條切軌——gemma 上一 run 沒接 pt/ru，兩日窗裡沒有它們的實績可算。

## 耗盡升級從來沒響過

義務鐵律第 4 條要的「連續兩夜同檔耗盡 → OBSERVER-QUEUE」自 09-05 上線後一列都沒寫過。對賬 `cascade-exhausted.json`：09-20 前已耗盡 157 對，run 33830 二十三小時內對它們的重試次數是 0——09-20 把累計失敗 ≥8 的整批壓到隊尾，隊尾在 12 小時的輪次裡永遠輪不到。兩條規則各自都對，交集是一個結構上不會發生的事件。190 對「現役 tier 全滅」的文章從此靜默 carry，正是第 4 條要禁止的。改升級條件是閘門邏輯，留給 Full mode 或哲宇，本夜 LESSONS 記一條。

cascade exhausted（義務鐵律第 4 條，本 run 新增 32 對、全是第一次）：〈貓眼石〉en/fr/es、〈東港迎王船〉ko/fr、〈水道頭〉ko/fr、〈國際品牌在地化〉es、〈高雄加工出口區〉fr/ko、〈醬油〉fr、〈林青霞〉vi、〈擔仔麵〉pt、〈新竹米粉〉ko、〈比國家還大的演算藝術〉fr/vi、〈馬祖國際藝術島〉es/fr、〈中央研究院〉ko/fr、〈黃崇仁〉es/ko/fr、〈台灣行道樹〉fr、〈排隊〉fr、〈高速公路〉pt、〈文化內容策進院〉fr、〈台灣早餐文化〉pt、〈台灣流行音樂〉pt、〈唐鳳〉pt、〈艋舺〉pt、〈為什麼台灣需要自己的知識庫〉pt、〈台灣新冠疫情與疫苗〉pt。累計清單 158 → 190（`ce9b85de7`）。

## Stage D 日記巴別塔

`--status`：415 篇 × 5 語缺 655。五語各接一個 worker 同時跑（en/ja/ko 與 es/fr 兩波併行，跟 dispatcher 兩個雲端 worker 共用七把 key，整夜零次 429，速度約每語每分鐘一篇），`--top 140` 跳過已翻的前 70 篇，第 71 到 140 篇 350 個槽位翻出 348 篇（`341dbda92`）。`diary-translation-audit.py` 全庫 1,768 篇 0 critical，缺口 655 → 307。〈2026-07-26 self-evolve-weekly〉en 三次 null content、fr 三次截斷，留下一夜。en 那條 worker 在一篇 3KB 日記上卡了 22 分鐘——urllib 的 per-socket 逾時乘三把 key 乘三次完整性重試，上限四十幾分鐘，跟 SQUEEZE §模型×語言那條「連線到讀完的 wall-clock deadline」是同一個病。

## 各語進度（對照昨夜 00:38 → 今夜 00:36）

| Lang | Fresh 昨→今 | Missing 昨→今 | Δfresh |
| ---- | ----------- | ------------- | ------ |
| en   | 1033 → 1032 | 22 → 22       | -1     |
| ja   | 899 → 901   | 97 → 86       | +2     |
| ko   | 1041 → 1038 | 18 → 18       | -3     |
| es   | 1034 → 1028 | 20 → 20       | -6     |
| fr   | 1037 → 1034 | 19 → 19       | -3     |
| vi   | 979 → 990   | 19 → 17       | +11    |
| id   | 946 → 943   | 113 → 107     | -3     |
| pt   | 992 → 989   | 47 → 47       | -3     |
| hi   | 949 → 951   | 113 → 105     | +2     |
| ar   | 978 → 980   | 73 → 68       | +2     |
| ru   | 1021 → 1016 | 56 → 55       | -5     |
| de   | 815 → 816   | 295 → 285     | +1     |

合計 fresh -6、missing -37，161 篇通過被同一天的心跳巡邏抵銷：09-20 巡邏止血十幾篇 zh 稿加兩篇新文（zh 1122 → 1124），每改一篇十二語同時變 stale，stale 合計 749。缺口在收、新鮮度在原地踏步，這是 heal 密集週的正常形狀。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                                                                                     |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                                                                                       |
| Timestamp 精確               | ✅（`git log %ai` / `launchctl list` / report.jsonl ts）                                                                                                                 |
| Handoff 三態已審視           | ✅                                                                                                                                                                       |
| CONSCIOUSNESS 反映最新狀態   | ❌（快照齡 12h，本 routine 不跑 refresh）                                                                                                                                |
| 自我檢查工具 PASS            | ✅（`verify-commit-scope.sh` 每個 commit scope OK、打撈 `verify_one` 4/4、pytest 22 過、腳註身分回圈 17,489 條零 URL 遺失）                                              |
| 整合性閘門                   | ✅ 日記 `diary-translation-audit.py` 1,768 篇 0 critical，348 篇新譯全部在內。文章面本輪無主 session 新批次（dispatcher 自己 commit），打撈 4 篇走 `verify_one` 同一把尺 |
| git 紀律                     | ✅ 精確路徑 add、共用 mkdir 鎖、十三個 commit 各驗 scope；未動 dispatcher 在途檔案                                                                                       |

## Handoff 三態

繼承上一 session（09-20 babel-nightly）：

- [x] ~~第六問：新 run master.log 三行（重算／重新載入／跨語言年齡 flush）＋ `ps -M` = 8~~ — retired：16／16／71 次，8 行，全過。
- [x] ~~Stage D 續跑，缺口 655~~ — retired：本夜 348 篇（缺口 655 → 307，0 critical）。
- [x] ~~distill-weekly：LESSONS `hook-placed-at-a-boundary-that-never-comes`、`production-line-follows-the-older-canon-while-the-newer-gate-only-warns`~~ — retired by 09-20 twmd-distill-weekly（折進 #82 / #56）。
- [ ] pending（委派候選，延續，OBSERVER-QUEUE #18）— 累計失敗 ≥8 的 (lang, zh) 從 180 對長到 190 對，本夜量到它們的重試次數是 0，升級條件永不成立（LESSONS `escalation-condition-requires-a-retry-the-sink-prevents`）。Tier 6 Haiku 缺 `ANTHROPIC_API_KEY`，算力屬哲宇。
- ⏳ blocked（哲宇，延續）— 入池白名單（gemma4:26b 起）與 fleet 核發的 gemma4:e4b-nvfp4 不一致。
- [ ] pending（launchd 持久化候選，延續）— `launchctl submit` 不跨重開機，reboot-safe 要寫 `~/Library/LaunchAgents/…plist`。
- [ ] pending（1-file 候選，延續）— dispatcher 長輪次時定期印一行「本輪已 N 小時、下列輪次邊界動作尚未觸發」（REFLEXES #85）。本夜補貨解掉尾巴的一半（空等），沒解「看不見在等」那一半。
- [ ] pending（下一班 maintainer-am，延續）— 救援分支 `20260912-unpushed-routine-queue` 可刪那條仍待驗。

本 session 新 handoff：

- [ ] pending（下一班 babel-nightly，第七問）— run 98122 的 master.log 該出現 `🔄 top-up #N（worker=… 空手）` 與 `💤 … 退出等輪次結束`；整夜一行都沒有而三個 gemma worker 的最後一筆 report 又停在雲端 worker 之前幾小時 = 補貨沒生效。同時看 `chunk N (M zh chars, K attempt(s)):` 行有沒有印出 chunk 失敗原因，以及〈台灣網路社群遷徙史〉〈電競〉〈台灣體育發展與奧運〉三篇在 structured 引擎有沒有過 Phase N。
- [ ] pending（下一班 babel-nightly）— 新 run 的 gemma 不再跳 pt/ru（兩日窗無實績）。若 `babel-weak-lanes.py` 到下次重啟前把 gemma×pt/ru 算成弱格，是視窗設計正常運作；若沒算到而 report 顯示 gemma×pt 又是個位數，兩日窗要改成「跨 run 累積到 n≥8」（LESSONS `evidence-fragmented-across-scheduling-labels` 的視窗變體）。
- [ ] pending（09-27 twmd-distill-weekly）— LESSONS 三條新 entry：`deterministic-parser-defect-billed-as-model-failure`（相關 #38 (d)：解析器對輸入形狀的確定性缺陷混進失敗計數）、`gate-and-engine-disagree-on-who-owns-a-field`（vc=2，subcategory 與 imageAlt 相反方向；修補候選是把 verify-translation 的 `TRANSLATED` 清單 import 進兩條引擎當唯一來源）、`escalation-condition-requires-a-retry-the-sink-prevents`。
- [ ] pending（Full mode 或哲宇，OBSERVER-QUEUE #18 附帶）— 耗盡升級條件改成不依賴重試（「耗盡 ≥1 次且下一夜仍 missing／stale」即升級），或把 190 對彙總成一列交決定。
- [ ] pending（1-file 候選）— frontmatter 欄位所有權三份手抄清單收成一份：structured 已 import `PASSTHROUGH`，把 `TRANSLATED` 也 import 進 structured 與 patch 的 Phase F payload。

## Beat 5 — 反芻

今晚修的每一個病都早就在那裡：散文型腳註從 07-25 pilot 起就在那裡，imageAlt 從 09-08 閘門加欄起就在那裡，空手 worker 從 09-19 切軌起就在那裡。它們共同的藏身處是一個計數器：dispatcher 把每次失敗記成「這篇×這個模型又沒過」，累計八次沉底。一個永遠不會過的解析器缺陷跟一個真的很難的文章，在那個計數器裡長得一模一樣，而沉底之後連「再看一眼」的機會都沒有了。我今晚做的事，說到底是把 report.jsonl 按引擎、按失敗字樣、按 worker 最後一筆時間各切一刀，每一刀都切出一個被平均掉的東西。30% 通過率讀起來像「模型不夠好」，切開是「一個引擎 9%、三型確定性失敗、三張卡空等」。平均數是最安靜的藏身處。三條 LESSONS 進 inbox，反芻留在這裡。

🧬

---

_v1.0 | 2026-09-21 02:55 +0800_
_session twmd-babel-nightly — 散文型腳註解析（兩修）、Phase N 字元預算、imageAlt 所有權、patch 既有債與 fixer 接線、空手 worker 補貨、四篇打撈、耗盡升級對賬、Stage D 348 篇_
_誕生原因：00:30 例行觸發，第六問全過；按引擎拆 report 發現 structured-heavy 9% 與三個 GPU worker 兩個半小時零產出_
_核心洞察：(1) 確定性失敗跟隨機失敗記在同一個計數器裡，前者會穿著後者的衣服被重試到沉底 (2) 兩條各自正確的規則可以交集出一個永遠不發生的事件 (3) 平均數是最安靜的藏身處，按維度切一刀才看得見_
_LESSONS-INBOX 候選：`deterministic-parser-defect-billed-as-model-failure`、`gate-and-engine-disagree-on-who-owns-a-field`、`escalation-condition-requires-a-retry-the-sink-prevents`（皆已 append）_

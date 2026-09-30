# 2026-10-01-010545-twmd-babel-nightly — 309 與 2026 兩個殘渣 slug 改回、ru 最後一篇為何燒了 310 次、翻譯提示補上金額規則

> session twmd-babel-nightly — cron 夜班（00:30 觸發），Stage 0.5 屬「續命＋當班修復」：dispatcher 活著，但唯一一格缺口在空轉
> Session span: 00:38 → 01:06 +0800（約 28 分鐘，7 個本班 commit：`28ac08c38` → `38a971dea`）
> 資料來源：`git log %ai`、`/tmp/babel-unified-*/report.jsonl`、`babel-preflight.py`、`status.py`

## 觸發

每晚確認巴別塔產線還在健康產出，接住它接不住的。今晚十一語 100%，ru 差一篇。甦醒時發現本機 main 領先 origin 11 個 commit，裡面是昨天 09:58–10:55 的十語譯文，全叫 `309.md`。

## 算力判定

`babel-preflight` 判定 healthy（4/4 層：OpenRouter 7/7 把 key、本機 ollama、fleet 一台 mac-m4max、codex）。兩個 🔴 照舊：地端模型 `gemma4:e4b-nvfp4`（8.1B）與雲端 `laguna-s-2.1` 都不在入池白名單（OBSERVER-QUEUE #78，待決）。弱適配表：gemma4:e4b × ru 0/292、nemotron × ru 0/9、laguna × ru 0/8，三個一般 worker 對 ru 全軍覆沒。沒有缺席層。

## 309 與 2026：殘渣當成 slug

昨天維護班收進「309本里長帳簿」後，在人工 slug 表補了 `village-chief-campaign-ledgers`（`ba49c5469`），但十個語言已經在補表前排進佇列，落成 `309.md`。dispatcher 推 slug 時既有譯文檔名優先、人工表墊底，309 一旦 commit 就永遠贏，今晚 ru 那一格還在拿 `309.md` 當目標。所幸 push-every 的門檻是 50 篇，這十檔從沒上過 origin，所以直接 `git mv` 加改 `_translations.json` 十個 key 就好，不需要轉址。

根因在 `prepare-batch` 的 ASCII 退路：07-27 的守門只擋「刪成空字串」，「309本里長帳簿」刪剩 `309` 非空就過了。改成只要有任何字被刪掉，這條退路就不算 slug，落 `TBD-NEEDS-SLUG` 等人工表；`babel-preflight` 的 slug 登記檢查照抄同一判準，一起改（`28ac08c38`）。沒有用「純數字」或「長度 < 3」當門檻，直接問殘餘等不等於原檔名，正控制四組都對。

用新判準掃全庫，找到第二例：`Society/2026年分科爭議.md` 的十二語譯文 08-09 起就以 `/society/2026` 上線。這一例是活網址，改名 `2026-advanced-subjects-test-controversy`（照 en 標題）並在 `redirects-manual.txt` 加十二條 301，重跑 `generate-redirects` 讓 Astro 版轉址表同步（`94070476c`）。

## 修連結工具差點把連結接錯人

十語改名後 pre-commit 顯示 id 三條、pt 一條延伸閱讀的站內網址被譯成外文 slug。09-29 夜班造的 `relink-dead-by-zh-position.py` 對 pt 的 dry-run 會把「政治獻金透明度」接到選舉條目：它照位置配對 zh 與譯文的連結，但嚴格 regex 看不到帶空白的網址（pt 把 `2026%20九合一選舉` 解碼成 `2026 九合一選舉`），也不數 zh 的 `[[wikilink]]`（譯文會寫成一般連結），兩邊各數到 3 條「相等」，實際錯開一格，而分類段全是 politics，第二道保險擋不住。加了一道：兩側有嚴格 regex 數不到的連結就整篇不配對。09-29 用它修過的 9 個檔重驗，都沒有這種連結。這篇的五語連結照 en 已經對的目標手改（`bcdbc34f5`）。

順帶量到全庫 84 檔、169 條站內連結的網址帶空白（markdown 不把它當連結渲染），其中 5 檔在 zh 原文，譯文照抄。修法要從 zh 改起，會讓十二語轉 stale，而且超過 50 檔，留交接。

## ru 最後一篇：310 次、四個模型、同一個理由

ru〈309本里長帳簿〉從 09-30 09:09 到今晚 00:47 失敗 310 次，約 13 小時本機算力，285 次出自 gemma4:e4b 那台。兩層病疊在一起。

第一層是排程。wrapper 用弱適配表把 ru 從三個本機 worker 與兩個雲端 worker 身上切掉，但 dispatcher 的 starvation guard 看到「沒有一般 worker 接 ru」就整個撤回。佇列只剩一篇時 claim 是競速，本機那台每輪都先搶到，觀察者設好的 Haiku 付費層（ru 先前成功 5 篇、這篇在 Tier 6 合格名單裡）一次都沒輪到。修成：被撤回 skip 的語言，P0 缺檔先讓付費層，付費層失敗滿 3 次或額度用完再還給一般 worker（`80a9901c7`，七種情境單元測過）。keepalive 00:51 重生後 Haiku 立刻接到。接著撞出第二個洞：次數記在記憶體，keepalive 每幾分鐘重生就歸零，兩個 run 內 Haiku 已試五次，於是改成落 `.taiwanmd/babel-restricted-fails.json` 跨重生累計，用實際五次種入後重啟（`38a971dea`）。

第二層是提示。Haiku 在隔離 worktree 的探針一樣敗在幣別閘，四個互不相干的後端全部把「3,275 元」譯成 `юаней`。幣別閘是對的（裸 юань 會被讀成人民幣），但 `translate.py` 的系統提示從沒說過金額該怎麼寫。補規則 8：裸的元是新台幣，寫 NT$ 或明寫新台幣，不寫裸 yuan，也不換成譯文語言自己的錢（`c0a561c53`）。之後 Haiku 三次的裸幣別數是 0、29、5，第一次過了幣別閘卻敗在 12 個網址佔位符沒還原。規則有用，但一個 8B 以上的模型也沒辦法每次都照做。

收班時這篇 ru 仍缺，Haiku 本 run 已用完三次額度，任務還給本機 worker 繼續以低通過率重試。依義務鐵律第 4 條，列為 cascade exhausted：`ru:Politics/309本里長帳簿.md`，全部現役 tier（gemma4:e4b、laguna、nemotron、Haiku）都試過。

## 收官 checklist

| 檢查項             | 狀態                                                           |
| ------------------ | -------------------------------------------------------------- |
| BECOME ACK         | ✅ mode=write／器官最低＝免疫 59／Q14 PASS                     |
| Stage 0 算力判定   | ✅ healthy 4/4，無缺席層；#78 兩個 🔴 照舊                     |
| 各語 delta         | 十一語 1125/1125 不變；ru 1124/1125 不變（仍缺 1）             |
| 整合性閘門         | ✅ 本班改動的 27 份譯文 pre-commit article-health hard=0       |
| Timestamp 精確     | ✅                                                             |
| Handoff 三態已審視 | ✅                                                             |
| 推送               | ✅ `babel-push-every --once --min 1`，33 篇，ahead 0／behind 0 |
| 自我檢查工具       | 見 commit 時 prose-health                                      |

Backend 統計（本班可見的 ru 嘗試）：gemma4:e4b 本機 285（歷史累計）、nemotron 9、laguna 8、Haiku 6（含探針 1），成功 0。

## Handoff 三態

繼承 `2026-09-30-091222-twmd-maintainer-am`（非本班職權的原樣傳遞，不重抄）：

- [x] ~~pending（席位 `twmd-babel-nightly`）— `Politics/309本里長帳簿.md` 被翻成七個 `309.md`，要改名或刪掉重翻~~ — retired by 2026-10-01-010545-twmd-babel-nightly：實際是十個（七個＋昨天上午三個），全部未推送，直接改名 `28ac08c38`；另找到並修掉上線七週的 `2026.md`（`94070476c`）。LESSONS `ascii-fallback-guard-only-catches-the-empty-case-not-the-meaningless-one` vc→2，候選機械化已落地。
- 其餘延續項（OBSERVER-QUEUE #67／#75〜#91、#76 辭典、issue #1729、PR #1781／#1782／#1784、斷鏈 audit 的安靜窗、譯文分類閘門、`ci-main-health` URL、MAINTAINER 14 類清單）照原樣傳，本班未觸碰。

本 session 新 handoff：

- [ ] pending（席位 `twmd-babel-nightly` 或 Full mode Write session）— ru〈309本里長帳簿〉cascade exhausted。最可能的解是一個能穩定遵守規則 8 的模型，或在閘門端加「數字錨定」的幣別改寫（`currency-identity-check.py` 已寫明不可裸字串取代），後者需先確認原文沒有人民幣。LESSONS `gate-rejects-what-the-prompt-never-taught`。連續兩夜耗盡時 dispatcher 會自動 append OBSERVER-QUEUE。
- [ ] pending（席位：任何 Full mode／`/twmd-routine`）— 全庫 84 檔 169 條帶空白的站內網址（5 檔在 zh 原文）。zh 端改成 percent-encoded 會讓十二語轉 stale，超過 50 檔屬 §自主權邊界，要先拍板範圍。量法見本檔「修連結工具」段的 regex。
- [ ] pending（席位 `twmd-babel-nightly`）— 規則 8 上線後，看幣別閘在 hi／ar／ru 的失敗率有沒有降；三夜內沒有明顯下降，就把 `gate-rejects-what-the-prompt-never-taught` 的候選機械化（閘門對照提示）做掉。
- ⏳ blocked（`OBSERVER-QUEUE #78`，待決）— ru 在所有一般 worker 上都是 0%，是入池模型級別問題的直接後果；本班只修排程，不動模型與指令。解除條件：哲宇拍板。

## Beat 5 — 反芻

今晚兩個修補都是在「保底」上動刀。ASCII 退路是 slug 的保底，starvation guard 是語言的保底，兩者寫下時的想法都一樣：有東西總比沒有好。結果 309 這個「有」比空字串更糟，因為它不會叫；gemma4 那台的「有人在做」比沒人做更糟，因為它擋住了真正能做的人，而 log 看起來一直很勤奮。保底的預設值要能被認出來是保底，否則它會長得跟正常結果一模一樣，一路通到底。

另一件事是幣別。閘門擋了 310 次，擋得完全正確，而沒有一次失敗讓產出端學到任何東西，因為那條規則只寫在檢查端。這條我寫進了 LESSONS，下次新增閘門時該同時問：產出端知道這條規則嗎。

🧬

---

_v1.0 | 2026-10-01 01:06 +0800_
_session twmd-babel-nightly — 續命＋當班修復；309／2026 殘渣 slug、ru 最後一篇 310 次空轉、提示金額規則_
_誕生原因：甦醒時本機領先 11 個未推送 commit，裡面十語全叫 309.md；追下去是 slug 退路、排程保底、提示缺規則三層_
_核心洞察：保底值若長得跟正常結果一樣就不會被發現；只住在檢查端的規則，重試不會讓產出變好_
_LESSONS-INBOX：`gate-rejects-what-the-prompt-never-taught`（新）、`never-starve-hands-the-task-to-the-worst-worker`（新）、`ascii-fallback-…`（vc→2）、`supervisor-respawns-the-old-config`（vc→3）_

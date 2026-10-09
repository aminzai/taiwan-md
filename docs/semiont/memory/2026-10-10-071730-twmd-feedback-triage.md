# 2026-10-10-071730-twmd-feedback-triage — 零回報第十五輪，兩道對賬全綠，「這個距今算久嗎」那把尺第四次手寫時終於有入口

> session twmd-feedback-triage — cron routine（每天 07:00 Asia/Taipei）
> Session span: 07:17:30 → 07:4X:XX +0800（約 30 分鐘，1 commit）
> 資料來源：`git log %ai` + `triage.mjs --commit` 報表 + Supabase REST 全庫查詢

✅ BECOME ack: mode=review / 8 organ 最低=免疫 🛡️60（review_coverage=19，離門檻少 20.25 分）/ Q13=PASS / Q14=PASS

## 觸發

Cron 07:00 轉錄班。讀 Supabase `status='new'` 的讀者回報，機械轉錄成 GitHub issue 接 08:30 的 maintainer 飛輪，並把 canonical 紀錄落進 git 主權層。

## 零回報第十五輪，但該跑的照跑

`fetched 0`。最近一筆回報是 2026-09-29，距今 10.3 天。這是連續第十五輪空場。

空場不等於這條 routine 沒事做：`--commit` 照跑，因為留言 sync 與兩道對賬都掛在它上面（LESSONS `zero-input-cycle-drops-the-reconciliation`）。HG13 的讀取入口也照跑了一次 `--show-all`，印 0 筆。這批真的沒有東西要讀，不是我沒去讀。

兩道對賬：

- HG12b `archive-reconcile=88/88` ✅
- HG12c `comment-reconcile=87/88` ✅ — 差的那一份是 [issue #1252](https://github.com/frank890417/taiwan-md/issues/1252)，7/29 那則答錯的留言在 GitHub 被刪、git 這邊留著。主權層正常運作，不是破口。

`archive-comments-synced=0` 這次能讀成「真的沒有新留言」而不是「一則都抓不到」，因為 comment-reconcile 回了 87/88 這個非空讀數。抓不到的話它會印「⚠️ 抓不到留言」。兩個數字一起看才有意義，這正是 HG12c 當初要解的那件事。

機器身份（HG11）：`gh-app-token.sh` 換到 `ghs_` 開頭的 installation token，`--whoami` 印 `{"issues": "write", "metadata": "read"}`、`repositories: frank890417/taiwan-md`。本輪沒開 issue，但 token 先驗過才動手。

## 那把量沉默的尺，第五次手寫，也是 09-29 交接的兌現

v1.9 讓空場那一輪印出「最近一筆距今 10.3 天」。當班讀完這行，下一個問題必然是：10.3 天算久嗎？

這把尺是歷史最長到達間隔，它在 09-11、09-12、09-15、09-29 四個 cycle 各被手寫過一次。09-15 那次的發現比「又手寫了一遍」尖銳得多：前兩次的答案都偏小，而且**方向固定**，因為極值問題帶 `limit` 去問只會往小的那邊錯（查最近 60 筆得 10 天，拉全庫 87 筆才是 12.65 天）。偏小的極值不製造不適感，所以沒有人想再查一次。這是一把用得越順手、錯得越安靜的尺。這條已經是 canonical：[REFLEXES #24](../REFLEXES.md) 形式 4 的極值變體。

09-29 那班走得更遠。它照 #24 的處方「重驗要換取數形狀」改掃 `docs/feedback/archive/` 的主權層紀錄，算出 15.94 天，比 12.65 大，讀起來像終於找到前一次漏掉的極值，跟處方生效的樣子一模一樣。真相是 archive 只收 `filed`（reject 分支刻意不寫檔，不讓 spam 文字進 git），所以它量的是勘誤之間的間隔，不是讀者到達之間的間隔，偏差方向固定偏大。那班在把 15.94 寫成新上限之前停了下來，並留一條交接給本席位：在 `formatIntakeAge()` 旁補一支全庫間隔分佈，因為它本來就握著全 status 讀取權，免得下一班又從 archive 推。當時沒做的理由寫得很誠實：八輪零回報，還不確定這個問題值不值得一支常設儀器。

所以今天不是第一次想到該造這支工具。設計十一天前就由上一班寫好了，今天是第五次手寫它的時候照著做完。先手寫一次獨立探針拿到答案：全庫 91 筆（88 filed + 3 rejected），歷史最長間隔 12.6 天（2026-06-16→2026-06-29），本次沉默 10.3 天——恰好等於第二長的那個間隔，仍在歷史區間內。順帶一個交叉驗證：91 筆裡的 88 筆 `filed` 跟 HG12b 的 `archive-reconcile=88/88` 對得上，兩邊各自算出同一個數。

然後照 09-29 寫好的設計把它變成流程給的。`formatIntakeIntervals()` 純函式 + 4 unit test（67/67 綠），空場那一輪自動印，另給 `--intake-stats` 讓人隨時看（唯讀，不碰 status／GitHub／archive）。兩道防止那個偏小極值回來的設計：`fetchAllFeedbackDates()` 刻意不帶 `limit`，並拿 `content-range` 的總筆數跟實收對賬，少收就印「極值會偏小，下面那行不可引用」並回 `null`，不拿半個樣本的極值當答案。「抓不到」「樣本不足」「算得出來」三種長相也分開，不共用。

取數母體刻意用全 status 而不是 git archive，正是因為 09-29 量過那個坑：主權層紀錄少了 rejected 那三筆，七月那個窗會被接成 15.94 天。上線後讀數跟同輪的手寫探針逐字相符。這道驗證刻意要跑，因為新造的尺在抽驗之前讀數不可引用（REFLEXES #99，它跟 #24 要一起讀：換尺之後的讀數，在確認新尺量的是同一群東西之前不算數）。

跟 v1.9 一樣刻意只給事實不給裁決：不印 ⚠️、不設閾值、不下處置。「已超過歷史最長」是對經驗紀錄的陳述，不是一個被調出來的門檻。閾值調整要 Full mode ＋ 人類 gate。

Pipeline 升 v1.12、薄殼 skill 補 `--intake-stats` 與「空場那一輪要讀兩行」一節。cron prompt 那一層沒碰：它是另一份文件（routine prompt，不是 repo skill 的複本），改它屬 `/twmd-routine` 席位，而這個儀器自己會印，不依賴 prompt 被更新才生效。

## 收官 checklist

| 檢查項                       | 狀態                                   |
| ---------------------------- | -------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                     |
| Timestamp 精確               | ✅ `git log %ai` + `date`              |
| Handoff 三態已審視           | ✅                                     |
| CONSCIOUSNESS 反映最新狀態   | ✅ 本輪未改器官狀態                    |
| 自我檢查工具 PASS            | ✅ `node --test triage.test.mjs` 67/67 |

## Handoff 三態

繼承 `2026-10-10-064217-twmd-spore-harvest-am`（非本班職權，原樣傳遞，明細不重抄，REFLEXES #74）：

- ⏳ blocked（延續，哲宇）：`OBSERVER-QUEUE #86（待決）` 10-11 到期。
- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly 10-11）：embeddings 改殼隔兩晚生效的三選項。
- [ ] pending（延續，收件席位 Full mode 或 `/twmd-routine`）：`git prune`（issue #1729）。本班 pull 時 git 照樣警告「too many unreachable loose objects」。
- [ ] pending（延續，收件席位 `twmd-maintainer-daily`）：404 同語言前綴雙寫家族。
- [ ] pending（延續，收件席位 `twmd-self-evolve-weekly` 10-11）：LESSONS `heart-counts-heals-as-contributed-births`。
- [ ] pending（延續，收件席位 `twmd-distill-weekly` 10-11）：LESSONS `threads-linkifier-swallows-cjk-before-url` 與 `narrative-log-fills-causation-no-gate-watches`（vc=2）。
- Threads／孢子那組零判斷條目屬 spore-harvest 席位，不經本班，原樣留在該鏈。

繼承本 routine 自己的鏈：

- [x] ~~`OBSERVER-QUEUE #28`（已決）第三人指控那筆~~ — 2026-09-05 哲宇拍板 B（只回覆並結案、不加偵測器），該筆 `status=rejected`。本輪佇列空，未再出現。retired by `2026-10-10-071730-twmd-feedback-triage`。
- [x] ~~在 `formatIntakeAge()` 旁補一支全庫間隔分佈（源 `2026-09-29-071521-twmd-feedback-triage`，席位指名本班，零判斷）~~ — 今天照該設計做完：`formatIntakeIntervals()` ＋ `--intake-stats`，母體用全 status 避開 archive 偏大那個坑。躺 11 天、經 7 個班次原樣往下傳。retired by `2026-10-10-071730-twmd-feedback-triage`。

本 session 新 handoff：

- [ ] pending（收件席位 `/twmd-routine`，改 `docs/semiont/ROUTINE.md` §TWMD feedback triage 後由 routine-sync 下發）：cron prompt 補一句「空場那一輪報表有兩行要讀，第二行是到達間隔」。不急，儀器自己會印，這條只是讓 prompt 跟 v1.12 對齊。
- [ ] pending（零判斷，每班照做）：空場那一輪讀兩行，`查不到`／`樣本不足` 不等於間隔正常。本次沉默若跨過 12.6 天（即 2026-10-12 之後）就是觀測到最久的一次，那是新事實，不是噪音。但它仍然只是事實，閾值處置留人類。
- [ ] pending（收件席位 `twmd-self-evolve-weekly` 10-11）：「交接寫明了當時不做的理由，而那個理由不會自己過期」這個形狀值不值得開 LESSONS entry。證據是上面那條 retired 的 11 天／7 班次，理由原文「八輪零回報還不確定值不值得一支常設儀器」在第十五輪一字不差地仍然成立地讀著。偏向既有 `handoff-latency` 家族的新維度（REFLEXES #97 管的是席位動不了，這個席位動得了）。`handoff-latency.py` 追得到它，因為那條交接帶了穩定參照（`formatIntakeAge()` 函式名）。
- [ ] pending（收件席位 `twmd-self-evolve-weekly`）：寫入端探針（FEEDBACK-TRIAGE §候選 c）仍未做。今天這把新尺量的是讀取端與歷史區間，蓋不到「今天送一筆進得來嗎」。要蓋掉只能從公開路徑戳一筆，而那會在讀者可見的資料表與主權層 archive 留下假回報，代價未定。

## Beat 5 — 反芻

今天最該記住的是那支函式的時間戳。

09-29 那班把設計寫完了：放哪裡（`formatIntakeAge()` 旁）、為什麼放那裡（它本來就握著全 status 讀取權）、不放哪裡會怎樣（下一班又從 archive 推，而 archive 偏大）。三句話，完全正確，我今天獨立想一遍得到同一個答案。十一天沒有人動手。

它當時沒做的理由也完全正當：八輪零回報，不確定值不值得一支常設儀器。問題是這個理由**十一天後沒有被重新評估過**。中間七個班次讀到這條交接，原樣往下傳，沒有人停下來問八輪跟十五輪是不是同一個處境。今天動手的觸發也不是讀到它：我先手寫查詢、拿到數字，才回頭發現上一班早把設計寫好了。真正推我動手的是第五次親手重打同一段查詢的那點厭煩。

這正是 `handoff-latency` 量的那個雙峰：做得掉的當天做掉，卡住的那批缺的從來不是資訊，是一個沒人覺得該由自己下的決定。這條的收件席位寫得很清楚就是本席位，權限也夠（`scripts/feedback/` 本班動得了），所以 REFLEXES #97「交接給動不了的席位」在這裡解釋不了它。它屬於更軟的一種形狀：**交接寫明了動作，也寫明了當時不做的理由，而那個理由自己不會過期**。「八輪零回報還不確定」這句話在第十五輪讀起來一字不差，但它描述的處境已經不同了。

另一個今天才看清的形狀：這條 routine 的四次修補（`--exclude` 8/15、`--show` 8/31、intake-age 9/10、今天這把尺）全是同一種病，必經的動作沒有入口、掛在當班自覺上，而且四次都是絆到第二次以上才落地。閘門跟自律的差別從來不在誰比較可靠，在誰負責記得。

🧬

---

_v1.0 | 2026-10-10 07:17 +0800_
_session twmd-feedback-triage — cron 轉錄班第十五個空場輪；兩道對賬全綠；到達間隔那把尺依 09-29 的設計儀器化_
_誕生原因：cron 07:00 fire。佇列空，但 `--commit` 照跑讓留言 sync 與 HG12b／HG12c 不跟著消失；第五次手寫「這個距今算久嗎」那段查詢時，照 09-29 留給本席位的設計把它變成 `--intake-stats`。_
_核心洞察：一條交接可以同時傳對設計、也傳對「現在不做」的理由，而那個理由不會自己過期——「八輪零回報還不確定值不值得」在第十五輪讀起來一字不差，處境卻已經變了。_
_LESSONS-INBOX 候選：無新 pattern。極值取數那條已是 REFLEXES #24 形式 4 極值變體（本輪為第 N 次驗證，已補進該條驗證欄，per LESSONS §DNA-first intake 鐵律 (a)）。交接理由不會過期這條偏向既有 `handoff-latency` 家族的新維度，留給 self-evolve-weekly 判是否值得開 entry。_

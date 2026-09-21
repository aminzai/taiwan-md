# 2026-09-22-003711-twmd-babel-nightly — 拆一夜 741 次嘗試找到五個確定性病灶當場修掉，全庫 1,152 份 rationale 與 261 份卡片圖對回 zh，日記巴別塔補到 100%

> session twmd-babel-nightly — cron 每日 00:30 多語批次同步
> Session span: 00:37 → 03:35 +0800（約 180 分鐘，本班 42 commits，另有 dispatcher 同時段 18 個 babel 批次 commit）
> 資料來源：`git log %ai` / dispatcher `report.jsonl`、`master.log` / `status.py` / `babel-health.py` / `diary-translate.py --status`

## 觸發

00:30 例行觸發。甦醒 selftest 十一項全綠，ACTOR_BUSY：昨夜 00:58 起跑的 launchd dispatcher（PID 98122）還在轉，本機領先 origin 48 個 babel commit、落後 0。前夜第七問三條全答得出來：`top-up #1（worker=macm4max1 空手）：補進 116 篇`、`top-up #2（lagunas）：84 篇`，補貨真的在生效；`chunk N (M zh chars, K attempt(s)):` 每筆失敗 chunk 都印了原因；gemma 這一 run 對 pt 51%、ru 31%，不用再切軌。

## Stage 0 算力判定

`babel-preflight.py`：healthy，4/4 層（OpenRouter 7/7 key 儲值、本機 ollama gemma4:e4b-nvfp4、fleet 1 節點 mac-m4max、codex-cli 0.145.0）。實績表按 label 印四個弱格（gemma × fr 8%／ru 9%／es 6%／hi 10%），`babel-weak-lanes.py` 按 backend 聚合後零弱格，維持 `nemo=ar` 一條切軌。Tier 6/7 仍無 `ANTHROPIC_API_KEY`／`GEMINI_API_KEY`，付費捕手整夜缺席。

## 一夜 741 次嘗試按引擎切開，structured 12%，而 35 次拒收全落在同一格

run 98122 到 00:37 的帳：741 次 333 過（45%，比昨夜 30% 好），whole 214/348、patch 91/151、structured-heavy **24/206（12%）**。structured 燒了 60.8 個 worker 小時換 24 篇，按失敗字樣再切：39 次 chunk 比值拒收裡 35 次落在 4.01～4.89 這一格，fr 15、es 7、id 6、de 6。找到 `_validate_chunk` 那行寫死 `[0.8, 4.0]`，十二語同一把尺，07-25 vi pilot 憑印象放的，沒人對別的語言重驗過。拿 120 篇 × 12 語已上站的合格譯文用同一種 H2 切法實測，chunk 級比值 p95 是 fr 4.60、es 4.61、de 4.37，p99.5 最高 5.19：羅曼語與德文每篇約十塊就有一塊會合法越線，整篇因此中止。上限改成 `max(4.0, ratio-bands.json healthy_max × 1.3)`，每語 p99.5 都在新上限下、en 那顆 20.46 的胡言亂語仍擋住、ja/ko 不收緊（`2c387d794`）。修完之後 master.log 的 `ratio out of band` 計數停在 51 沒再長。

第二格是 whole 的 51 次「frontmatter not untranslated」：貓眼石、醬油、台灣小吃、水道頭各四五次，全是 `imageAlt` 原樣抄回。structured／patch 昨夜修了這欄，整篇引擎沒修，而且修錯了地方：00:47 我補的是 `openrouter-translate.py` 的舊 scaffold（`b3cdfb2b3`，順手把 scaffold 標 preserve、系統規則卻寫 translate 的 tags 矛盾一起改掉），整篇引擎預設走的其實是 armor_pre／armor_post，模型只看 TITLE／DESC／TAGS 三行，其餘欄位工具機械複製 zh。第三次才補到對的地方：zh 有 imageAlt 時 prompt 多給 ALT 行、輸出多一段 `===ALT===`，沒交就當場判失敗換模型（`7abc5b7af`）。同一個欄位在三條引擎補了三次，跟 wikilink 的病同一個形狀（見下）。

第三格是 patch 的 60 次「verify trio 拒收」，讀得出原因的全是 verify 第 11 檢查 URL count：既有譯文對它自己那版 zh 就少幾條 URL，局部 patch 只換幾章、其他章的債原封不動，整份檔案量一定不過，dispatcher 要撞滿五次才升級整篇。patch 引擎現在先用 verify 的 `extract_urls`（從函式內 hoist 到模組層，兩處同一把尺）量既有譯文對舊版 zh 的 URL multiset 與腳註定義數，有債直接 exit=2 讓整篇接手（`4bbc886e7`）；實測昨夜六個拒收對，嚴長壽 ko／鄭成功 en／台灣金融科技發展 es 當場擋下，嚴長壽 ko 確實少一條 pixnet 來源。

第四格是 18 次 `wikilink-target` 硬閘：structured 引擎完全沒處理 `[[X]]`，模型把括號裡翻成德文、括號留著。整篇引擎靠 manifest、patch 引擎 08-09 自己抄了一份反查，三份對解析不出來的都「保守不動交給 prompt」，模型並不聽。收成 `cross_link_localizer.resolve_wikilinks()` 一份（從所有 zh 檔建 stem 索引、同名跨分類不猜；有譯文連結化、沒有降純文字），三引擎呼叫點全改走它（`a6069a1ef`）。

## 上站的 1,152 份 rationale 是一行 Python repr，261 份卡片圖還熱連結 Wikimedia

貓眼石 ko 的隔離樣本除了 imageAlt 還露出一行 `rationale: "{'why_this_hook': …}"`。追到 `render_scalar` 對 dict fallthrough 成 `yaml_single_quote(str(dict))`、None 變字串 `'None'`，跟 07-26 那條 list 案是同一個型別走樣家族的第三個成員；全庫 grep 十二語 1,140 份 repr、12 份 `'None'`，九成是九月的。dict 改渲染縮排 block mapping、None 渲染 `null`、含換行的字串渲染 `|` block scalar（zh 用 `|` 寫的 whats_excluded 清單經單引號會被摺掉換行）。存量用新工具 `heal-frontmatter-types.py` 從 translatedFrom 找回 zh、只重渲染那一個欄位、parse 回來等於 zh 值才落地，逐語 commit（韓文 `3c20aad3f` 起十二筆）。

ar 批次被 `megaport-festival` 的 image-health hard 擋下時追出第二個存量債：zh 早把 Wikimedia 熱連結 cache 成 `/article-images/`，譯文的 image 還是舊網址。病根在 Tier 0b：zh 只改 frontmatter 時 bodyHash 不變，status 判 metadata-stale，`bump-source-sha.py` 只 bump 三個 sha 就標 fresh，passthrough 值留在舊的，之後 fresh 的檔沒有任何路徑再看它。全庫 261 份 image 跟 zh 不同、179 份仍熱連結。`bump_one()` 從此 import heal 工具的 `sync_passthrough_fields()` 一起抄卡片圖四欄與 featured（同步集刻意保守，lastVerified 等留給重翻），存量用 `--sync-passthrough` 十二語抄回（`b4d84f281` 與各語 heal commit）；順手拆掉四篇被模型用四個反引號 markdown 圍欄整段包住的正文（pt 兩篇、ru 兩篇）、按序對回 18 篇正文內嵌圖路徑停在 zh 改名前的檔名（`remap-inline-image-paths.py`）。收官全庫掃：rationale repr 0、image 與 zh 不同 0。

修 dict 那條時自己造了一個回歸：sporeLinks 是 list of mapping，block mapping 被塞進 `[ ]`，01:16 起台海危機七語在 ollama 與 laguna 兩個後端全報「while parsing a flow sequence」——兩個後端同一個錯就不會是模型的錯。含 dict／list／多行元素的 list 改渲染 block sequence，拿全庫 1,124 篇 zh 的 frontmatter 逐欄渲染再 parse 回來全等（`90fbd33c2`）；閘門一路擋著，沒有壞檔上站，代價是七篇各背一筆難篇帳。

## 兩件跟 status 有關的洞

`babel-health.py` 六維：ratio 維 76 份 CRITICAL(<0.5) 截斷檔，對 status 交叉，65 份 stale、**11 份 fresh**（ja 12,144 bytes 的台達電子只剩 2,077 bytes）。fresh 的截斷檔是所有路徑的交集空格：免費 cascade 只吃 stale／missing，Tier 6/7 資格集合只看 stale／metadata-stale。classify() 早有一道同型的腳註遺失閘，截斷沒有；加了（bytes 比 < 0.5 → stale reason `truncated`，`37761bc87`），首跑 ja 10、es 1 進隊，判 stale 不判 missing，舊頁留給讀者。

02:26 起 laguna 上游限流二十分鐘，統一企業／許倬雲／高速公路在 4 秒內 exit=1，跟閘門拒收一樣各背一筆 fail_counts。這種失敗說的是後端此刻沒容量，累滿八次卻會沉到隊尾再進 cascade-exhausted 清單。dispatcher 對上游 429／provider error／斷網不再記文章的帳（`d48454eba`），進程要下次重啟才吃到，本夜不為它重啟。

## 手動 commit 撞到共用 index

pt 批次 118 檔 stage 好、lint-staged 被一篇既有 fence-prose 債擋下、檔案留在 index；30 秒後 dispatcher commit「ja 批次 6 篇」，stat 裡多了 85 個 pt 檔（`26d3f390a`）。內容是對的（本班修好的檔），歸屬錯了。dispatcher 那端的精確路徑 add 完全正確，仍掃到別人的東西，因為 `git commit` 只認 index。此後本班所有 commit 走 dispatcher 同一個 mkdir 鎖 `/tmp/taiwan-md-git.lock`，hook 失敗立刻 `git reset` 再放鎖，之後零重演。另外前六個 heal commit 訊息把「譯文」打成「譽文」，不 rebase（REFLEXES #35），留著。

## Stage D 日記巴別塔

`--status`：415 篇 × 5 語缺 307，全是第 141 篇以後的舊日記。五語各一 worker 跑 nemotron-3-ultra（en/ja/ko 先、es/fr 半小時後跟上，跟 dispatcher 兩個雲端 worker 共用七把 key，nemotron 側零 429），每語約每分半一篇，03:13 收完 299 篇；8 篇雲端三次截斷或拒答（2026-07-12 self-evolve 四語、06-28 manual en／fr、07-11 dna-checkup fr、07-11 manual ko）改本機 gemma4 逐篇收下。`diary-translation-audit.py` 2,075 篇 0 critical，缺口 307 → 0（`a11adeff6`）。

## 各語進度（對照昨夜 00:36 → 今夜 03:28）

| Lang | Fresh 昨→今 | Missing 昨→今 | Δfresh |
| ---- | ----------- | ------------- | ------ |
| en   | 1032 → 1051 | 22 → 22       | +19    |
| ja   | 901 → 906   | 86 → 79       | +5     |
| ko   | 1038 → 1050 | 18 → 18       | +12    |
| es   | 1028 → 1034 | 20 → 20       | +6     |
| fr   | 1034 → 1042 | 19 → 19       | +8     |
| vi   | 990 → 1019  | 17 → 17       | +29    |
| id   | 943 → 958   | 107 → 99      | +15    |
| pt   | 989 → 1012  | 47 → 45       | +23    |
| hi   | 951 → 961   | 105 → 99      | +10    |
| ar   | 980 → 990   | 68 → 66       | +10    |
| ru   | 1016 → 1024 | 55 → 50       | +8     |
| de   | 816 → 838   | 285 → 270     | +22    |

合計 fresh +167、missing 849 → 804、stale 749 → 640。ja 的 +5 含截斷閘把 10 份假 fresh 送回 stale。run 98122 到 03:28：791 次 368 過（47%），lagunas 114/227、macm4max2 71/154、macm4max1 66/152、macm4max3 66/154、nemo 51/104；按引擎 whole 235/392、patch 101/161、structured 28/224。本班在場的三小時 74 次 35 過，structured 的新上限還沒有一篇跑完可以作證，要等下一夜的 report。

cascade exhausted（義務鐵律第 4 條，本 run 23 筆、全是第一次）：〈外送專法〉vi/es/ja、〈比國家還大的演算藝術〉ko/pt、〈臺灣民報〉ko、〈東港迎王船〉pt、〈醬油〉ko/pt、〈台灣客家音樂〉vi、〈中央研究院〉vi、〈台灣行道樹〉ko、〈排隊〉vi/ko、〈文化內容策進院〉vi/ko、〈許倬雲〉pt、〈毒馬鈴薯認知作戰〉pt、〈苗栗縣〉id/de/hi、〈台灣企業：統一企業〉pt、〈木曜4超玩〉es。累計 190 → 214。其中苗栗縣三語與文化內容策進院兩語就是今晚修掉的 chunk 比值與 wikilink 兩個病造成的，但它們已沉到隊尾，要等升級條件改法（見 handoff）。

## 收官 checklist

| 檢查項                       | 狀態                                                                   |
| ---------------------------- | ---------------------------------------------------------------------- |
| BECOME ACK                   | ✅ mode=write / 器官最低 🛡️59 / Q14 PASS / wake:END 讀到 267,835 bytes |
| MEMORY 有這次 session 的紀錄 | ✅                                                                     |
| Timestamp 精確               | ✅ git log %ai                                                         |
| Handoff 三態已審視           | ✅                                                                     |
| Stage 0 算力                 | ✅ healthy 4/4；Tier 6/7 付費層缺席（缺 key，屬哲宇）                  |
| 整合性閘門                   | ✅ 文章走 dispatcher 三重 gate；日記 audit 2,075 篇 0 critical         |
| Diary                        | ⏭ `diary-gate.py` 冷卻未過（上一篇 09-19，3 天 < 6），反芻留 Beat 5   |
| 自我檢查工具 PASS            | ✅ article-health --profile=memory-diary                               |

## Handoff 三態

繼承上一 session（09-21 babel-nightly ＋ 09-21 maintainer-am）：

- [x] ~~第七問：run 98122 的 `🔄 top-up #N` 與 chunk 失敗原因行~~ — retired：top-up 兩次 200 篇、chunk 原因 115 行全在。〈台灣網路社群遷徙史〉〈電競〉〈台灣體育發展與奧運〉三篇 structured 仍沒過 Phase N 之後的 Phase B（腳註集合 mismatch），不是解析器的病了。
- [x] ~~gemma 不再跳 pt/ru，兩日窗弱格對照~~ — retired：本 run gemma × pt 20/39、ru 11/35，按 backend 聚合零弱格，視窗設計正常。
- [x] ~~Stage D 缺口 307~~ — retired：307 → 0，2,075 篇 0 critical。
- [x] ~~pending（給 babel session，LESSONS `relative-category-links-survive-link-check` 候選 (c)）— babel 連結閘門對 `](../` 拒收~~ — retired by 本班查核：`cross_link_localizer.LINK_RE` 只認 `](/` 開頭，`../` 不會被在地化也不會被放行成站內連結；譯文層的相對路徑由 verify-batch 第 6 步與 verify_internal_links 認相對路徑後接住，不另開閘。
- [ ] pending（下一班 babel-nightly，第八問）— 新 run 起跑後 `report.jsonl` 的 structured-heavy 通過率該從 12% 明顯抬頭（fr/es/de 分塊比值 4.0–4.9 那一格不再拒收）、master.log 的 `ratio out of band` 每夜新增筆數該接近零、`no ===ALT===` 字樣若大量出現 = 模型不聽新格式要回頭看 prompt、`⏸ 後端容量失敗` 行只在 dispatcher 重啟後才會出現。
- [ ] pending（下一班 babel-nightly）— `heal-frontmatter-types.py --lang all --sync-passthrough`（dry-run）應該印 0 筆 would-heal；若又長出 image drift，表示還有別條路徑在寫 fresh 但不抄 passthrough。
- [ ] pending（委派候選，延續，OBSERVER-QUEUE #18）— 累計失敗 ≥8 的 (lang, zh) 190 → 214 對，隊尾永不輪到；今晚修掉的兩個病（分塊比值、wikilink）造成的苗栗縣 id/de/hi、文化內容策進院 vi/ko 也在裡面。升級條件改法（「耗盡 ≥1 次且下一夜仍 missing／stale 即升級」或彙總一列）屬 Full mode 或哲宇（LESSONS `escalation-condition-requires-a-retry-the-sink-prevents`）；Tier 6 Haiku 缺 `ANTHROPIC_API_KEY`。
- ⏳ blocked（哲宇，延續）— 入池白名單（gemma4:26b 起）與 fleet 核發的 gemma4:e4b-nvfp4 不一致；本夜日記 8 篇殘檔也是 e4b 收的。
- [ ] pending（launchd 持久化候選，延續）— `launchctl submit` 不跨重開機，reboot-safe 要寫 `~/Library/LaunchAgents/…plist`。
- [ ] pending（1-file 候選，延續）— dispatcher 長輪次時定期印一行「本輪已 N 小時、下列輪次邊界動作尚未觸發」（REFLEXES #85）。
- [ ] pending（09-27 twmd-distill-weekly）— 09-21 三條加本夜四條 LESSONS：`staged-files-leak-into-a-parallel-writers-commit`、`metadata-stale-bump-assumes-frontmatter-unchanged`、`one-gate-three-engines-three-rulers`、`fresh-status-hides-truncation`。
- [ ] pending（1-file 候選，延續，跟 `one-gate-three-engines-three-rulers` 同題）— frontmatter 欄位所有權三份手抄清單收成一份：把 verify-translation 的 `TRANSLATED` import 進 structured 與 patch 的 Phase F payload；本夜 imageAlt 在第三條引擎補第三次，就是這條沒做的代價。

本 session 新 handoff：

- [ ] pending（下一班 babel-nightly 或任何重啟 dispatcher 的人）— `babel-dispatch.py` 的容量失敗不計帳（`d48454eba`）要 `launchctl kickstart -k` 重啟才生效；重啟前先打撈工作樹的完稿（昨夜 SOP）。不急，等自然重啟。
- [ ] pending（給 maintainer-am，資訊）— 前六個 heal commit（`8c2e0fd9f`…`c504c031c`）訊息「譽文」是「譯文」的錯字；`26d3f390a`「ja 批次 6 篇」實際含 85 個 pt rationale heal 檔（index 共用被掃走，LESSONS `staged-files-leak-into-a-parallel-writers-commit`）。兩者都不 rebase。
- [ ] pending（1-file 候選）— `git_lock_commit()` 在 add 之前 `git diff --cached --quiet`，index 不空就印 ⚠️ 並列出誰的檔在裡面（現在是靜默吞進 commit）。

## Beat 5 — 反芻

今晚修的七個病，沒有一個是新的形狀。imageAlt 在 structured 與 patch 昨夜各補過一次，今晚在整篇引擎補第三次，而且第一次補錯地方；wikilink 的路由整篇引擎 07-26 做了、patch 引擎 08-09 抄了一份、structured 引擎一直沒有；型別走樣 07-26 修過 list，今晚修 dict 與 None，修完 dict 又把 list of dict 弄壞。同一個轉換住在三條引擎裡，每條引擎各自長出同一個病、各自被修一次，修的人每次都以為自己在修一個新東西。我一直把這叫「三把尺」，今晚看清楚它更接近三具身體：引擎是三個獨立的個體，它們的共同祖先只有一份 verify，而 verify 是事後量的，量得到病、長不出免疫。真正要收的是輸入端那層轉換，今晚收了 wikilink 一件、render_field 一件，欄位所有權那件還在 handoff 裡等了兩夜。

第二件是 fresh。status 說 fresh 的意思是三個 hash 對得上，我一路把它讀成「這篇沒事」，於是 11 份只剩五分之一的譯文、261 份熱連結的卡片圖、1,140 份一行 repr 的 rationale，全在 fresh 底下躺了一到兩個月，沒有任何路徑會再看它們一眼。閘門全長在寫入那一刻，寫入之後就沒有眼睛了。今晚給 classify 加了一道截斷閘，但那只是把一種「看起來沒事」拉回隊列；卡片圖與 rationale 是靠一次全庫 grep 才看見的，這種 grep 沒有 routine 在跑。反芻留在這裡，四條教訓在 inbox。

🧬

---

_v1.0 | 2026-09-22 03:35 +0800_
_session twmd-babel-nightly — 分塊比值按語言校準、imageAlt 補進整篇引擎裝甲路徑、patch 既有債預檢、wikilink 三引擎收一份、rationale 與卡片圖存量 1,400 餘份對回 zh、status 截斷閘、容量失敗不計帳、Stage D 補到 100%_
_誕生原因：00:30 例行觸發，第七問全過；按失敗字樣拆 report 發現 structured 12% 裡 35 次拒收落在同一格 4.01–4.89_
_核心洞察：(1) 三條引擎是三具身體，共同祖先只有事後量的 verify，同一個病在每條引擎各長一次 (2) fresh 是 provenance 對得上，不是內容沒事；寫入之後沒有眼睛 (3) 共用 index 的 commit 只認 index 不認誰 add 的，鎖要鎖整段_
_LESSONS-INBOX 候選：`staged-files-leak-into-a-parallel-writers-commit`、`metadata-stale-bump-assumes-frontmatter-unchanged`、`one-gate-three-engines-three-rulers`、`fresh-status-hides-truncation`（皆已 append）_

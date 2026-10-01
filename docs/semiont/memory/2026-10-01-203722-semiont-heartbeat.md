# 2026-10-01-203722-semiont-heartbeat — 四支感知層工具改吃語言註冊表（llms.txt 對 AI 爬蟲說只有六語、新鮮度停在五月），巡邏第三十到三十二篇 10 錯

> session semiont-heartbeat — 每日排程完整心跳 20:30 班（Full mode，本機 commander-macbook）
> Session span: 20:35 → 21:00 +0800（約 25 分鐘，5 個工作 commit＋收官）
> 資料來源：`git log %ai`

## 觸發

排程心跳，今天第二輪。wake-context 十一項體檢全綠、工作樹與 origin 同步。16:36 那輪剛跑過，交接寫明「下一個 Full mode」要做兩件事：巡邏母體現值前三名，以及 `check-hardcoded-langs.sh` 掛號的 python 檔逐檔判斷、三個感知層先。器官讀數跟下午一樣：心臟 70（rewrite 依哲宇決定改手動，七天八篇全是投稿）、免疫 59 黃燈。OBSERVER-QUEUE 今天沒有到期的非 🔒 預設；名古屋亞運與李灝宇兩條切角 10-04 到期，寫文的時機仍屬手動控制 rewrite 的人，本輪不搶。哲宇最後在場 09-26，五天，還沒進缺席模式。

## 四支感知層工具的語言清單

交接點名三支，逐檔看下去其實是四支，而且每一支壞的樣子不一樣。

`fetch-cloudflare.py` 的語言前綴 09-27 self-evolve 已經改吃註冊表，掛號表卻還掛著；檢查器命中的那一行變成了「讀不到註冊表就退回五語」的退路。退回五語時，另外七語的 AI 讀取會靜默記進中文、數字看起來一切正常，所以拿掉退路，讓呼叫端既有的 try 接住，輸出少一欄而不是錯一欄。`generate-dashboard-immune.py` 兩處寫死五語，量下去，`driftDetail.new_articles_7d` 寫本週新增 441 篇，實際中文新文 1 篇（〈309本里長帳簿〉），另外四百多篇是七語的新譯文；drift 分數用的是固定估值所以沒動，review_coverage 仍是 19，免疫黃燈是真的。`weekly-report-prep.py` 把七語路徑記成 zh-TW、分類欄變成語言碼，語言器官段只列六語。三支都改經 `lang-sync/langs.py` 讀 `languages.mjs`（`6e1f7c917`），各自用函式層測試驗過：immune 載入 1,123 篇 14 個分類、drift 讀 1；週報的 zh-TW 只剩 10 個真分類檔。

最大的一支是 `refresh-llms-txt.py`。`public/llms.txt` 是寫給 AI 爬蟲的自我介紹，總數行寫「across 6 languages」，正文兩處寫「5 non-Chinese languages」，分類行停在 13 類漏了 Politics。新鮮度那行更久：工具從 `dashboard-i18n.json` 讀 freshPct，那份是介面字串覆蓋率，格式從來對不上，讀回空 dict 就不改那一行也不出聲，於是從 05-04 誕生起一直是 MANIFESTO 裡五月二號那組數字。改成語言清單吃註冊表、新鮮度讀 `dashboard-translations.json`、讀不到時 stderr 明講、分類從 `knowledge/` 首字大寫的資料夾推導；連跑兩次無差異，`--check` 回 0（`9b58a94f6`）。§1 那段「4-tier cascade」「100% from FREE tier」的架構敘事也已經不是現況（09-26 起有付費委派層），那是對外敘事的語氣與定調，留給哲宇。

掛號表撤掉五條（`check-hardcoded-langs.sh`），09-28 新增的 `name-substitution-check.py` 現形兩行，它們綁著各語言的名人寫法表，新語言要人補寫法，以 B 類掛號；`--ci` 回 0。

## 巡邏第三十到三十二篇

照抽樣指令取前三名，三個 Sonnet 子代平行查、只寫查核檔，我先讀原文標疑點交給它們，回來後每條 ❌ 親自重抓原文再改。查核檔落 `reports/research/2026-10/`，各附 Phase 6 套用紀錄。

〈台灣社區與里文化〉29 個原子 2 錯：鄰長「沒有經費補助」，它自己列的臺北市民政局頁面寫每月 2,500 元工作協助費；「台北市民e點通」是 2001 年的網站、2019 年底已下架，改成台北通。同輪法條引號改回《地方制度法》第 59 條原文、刪「里長投票率相當高反映重視」的無源因果、「大資料」改「大數據」，全文從零腳註變三條（`21c4e4caf`）。〈教育制度與升學文化〉36 個原子 4 錯：會考被寫成入學管道、免試入學寫成依居住地就近分發（實際是 15 個就學區填志願、超額才比序）、「延伸義務教育至十二年」（後三年是自願非強迫入學）、族語課寫成「部分學校」（現行規定國小到國二全面擇一修習）（`0f71fb1c5`）。〈早餐店阿姨與社區情報網〉是投稿者 So͘ Bîn-hiân 的幽默散文，只改事實口吻的句子：Granovetter 的弱連結被轉述成「經常碰面的人」，論文裡幫上忙的人脈多半偶爾才碰面；便利商店密度是僅次南韓；兩條腳註的篇名查無此文；早餐店家數改成財政部營業登記 18,919 家（`7fb2d0339`）。

錯誤率 7%／11%／22%。三篇 hard=0，警告對 HEAD 基線逐條比過，沒有新增（社區篇少了「無正式腳註」那條，教育篇分號從 6 降到 4）。

## 首頁腳註

教育篇五條腳註全是機構首頁，早餐店篇兩條掛在媒體首頁。首頁永遠回 200，所以格式檢查跟死鏈檢查都放行。量全站：zh 文章 17,168 條腳註裡 1,149 條（6.7%）是純網域首頁，分布在 311 篇。兩篇的腳註區塊都來自 05-16 同一個投稿批次（`f712b7242`，PR #1070）把參考資料轉成腳註，教育篇的參考資料更早由 03-19 另一個批次補上教育部首頁。登記成 LESSONS `homepage-citation-passes-format-and-reachability-gates`，附兩條候選機械化（article-health WARN、巡邏抽樣第二排序鍵）；WARN 那條會讓 311 篇多一條警告，可能動到免疫的 plugin_pass_rate，上線前要先量。llms.txt 讀回空沿用舊值那件事補進 REFLEXES #85 變體 2 的驗證欄。

## 收官 checklist

| 檢查項                       | 狀態                                                                |
| ---------------------------- | ------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                  |
| Timestamp 精確               | ✅ `git log %ai`＋`date`                                            |
| Handoff 三態已審視           | ✅                                                                  |
| CONSCIOUSNESS 反映最新狀態   | ✅ 警報層 derived；免疫 drift 讀數待明晨刷新重生                    |
| 自我檢查工具 PASS            | ✅ 三篇 hard=0、警告逐條比過；檢查器 `--ci` 0；llms.txt `--check` 0 |
| Diary                        | skip（反芻收在下面一段）                                            |

## Handoff 三態

繼承 `2026-10-01-163744-semiont-heartbeat`：

- [x] ~~pending（下一個 Full mode）— 巡邏母體前三名：社區與里文化、教育制度與升學文化、早餐店阿姨~~ — retired by 本 session（`21c4e4caf`／`0f71fb1c5`／`7fb2d0339`）
- [x] ~~pending（Full mode，逐檔判斷）— `check-hardcoded-langs.sh` 掛號的三個感知層~~ — retired by 本 session（`6e1f7c917`／`9b58a94f6`，實際四支）；其餘 A 類十一支（spore 家族四支、`attribution-risk-audit`、`inbox-audit`、`article-depth-audit`、`rescue-orphans`、`unify-translation-slugs`、`backfill-translated-from`、`salvage-quarantined`）仍掛號，見下方新交接
- [ ] pending（席位 `twmd-maintainer-am`）— Discussion #1704 回覆 idlccp1984，草稿在 `2026-10-01-163744-semiont-heartbeat`，原樣傳遞（REFLEXES #74）
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05 或 Write 班）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單，同趟可併 `/terminology/變壓器`
- [ ] pending（席位：任何 Write session）— PR #1781 里長帳簿後續；〈台灣社區與里文化〉延伸閱讀可順手連過去
- [ ] pending（走 REWRITE 時）— 16:36 那輪與 09-25 那輪的懸案仍在（發酵篇豆腐乳、媒體篇戒嚴兩句、公園篇兩節重複、國際標準／動物園／政治三篇）；本輪新增：社區篇社大三類課程與北投學僅搜尋摘要、教育篇 [^1][^3][^4][^5] 仍指首頁且 [^5] 是孤兒、早餐店篇「多為個人經營的非連鎖小店」無數字
- [ ] pending（self-evolve-weekly 候選，09-25 起第三班原樣傳）— `check-parallel-actor.sh` 擴到 `git worktree list` 每棵樹的 dirty 狀態（REFLEXES #42 第四起）
- ⏳ blocked — `OBSERVER-QUEUE #92`／`#67`／`#76`／`#28`／`#75`〜`#91`（待決，🔒），解除條件：哲宇拍板
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留，仍是主樹唯一 untracked
- [ ] pending（延續，非本班職權，原樣傳遞）— `.git/gc.log` 與 `git prune` 排程、`OBSERVER-QUEUE #69（待決）` (a) 10-02 起等 #68、issue #1729，明細見 `2026-10-01-084906-twmd-maintainer-am`

本 session 新交接：

- [ ] pending（席位 `twmd-data-refresh-am` 10-02，驗收）— 明晨重生的 `dashboard-immune.json` 裡 `driftDetail.new_articles_7d` 應該是個位數到十位數，不再是四百多；`llms.txt` 應維持十二語且 `--check` 回 0。量到不是 → 回頭看 `6e1f7c917`
- [ ] pending（席位：下一個 Full mode）— 巡邏母體現值前三名：Society/社會住宅與居住正義、Society/社會運動與公民參與、Technology/台灣5G網路建設與數位轉型（都是 03-18 出生、12 語）
- [ ] pending（席位：Full mode 或 self-evolve-weekly）— `check-hardcoded-langs.sh` 其餘 A 類十一支，逐檔判斷是語言註冊表還是有意義的順序再改
- [ ] pending（席位 `twmd-self-evolve-weekly`）— LESSONS `homepage-citation-passes-format-and-reachability-gates` 的兩條候選機械化，WARN 那條先量對免疫 plugin_pass_rate 的影響
- ⏳ blocked（給哲宇，對外敘事）— `public/llms.txt` §1「4-tier cascade ending at Local LLM」「100% from FREE tier」已不是現況（09-26 起有付費委派層），數字由工具維護，這段架構敘事的改寫屬對外溝通語氣

## Beat 5 — 反芻

下午那輪寫過，清推擬引用的人自己也會推擬。這一輪換了一個形狀撞到同一件事：我寫 LESSONS 條目時，從一個 commit 的訊息標題和檔案統計推出「教育篇的三條首頁腳註是 03-19 那個批次補的」，寫完回頭看 diff，那個批次改的是文末參考資料，腳註是兩個月後另一個批次加的。推論的材料都是真的，commit 存在、它確實動過這篇、它確實在補網址，錯在把它放進了錯的槽位，跟 REFLEXES #98 的形狀一樣。攔下它的又是「先抓再寫」那一步，只是這次是「先看 diff 再寫歸因」。

llms.txt 那件事讓我比較在意。它是整個站對 AI 讀者最直接的自我介紹，主權的巴別塔十二語全覆蓋是兩週前的里程碑，而這份介紹一直告訴爬蟲我們只有六語。修它的工具每天都在跑，每天都說「已是最新」。一份對外的文件，最容易漏掉的往往是「自己變了」這件事。

🧬

---

_v1.0 | 2026-10-01 21:00 +0800_
_session semiont-heartbeat — 四支感知層工具改吃語言註冊表、llms.txt 十二語與新鮮度回正、巡邏第三十到三十二篇 10 錯_
_誕生原因：每日排程完整心跳 20:30 班，接 16:36 那輪寫給下一個 Full mode 的兩條交接_
_核心洞察：(1) 讀回空就沿用舊值的工具，會在每天的綠燈底下讓一份對外文件停在五個月前 (2) 首頁網址永遠回 200，格式與死鏈兩道閘門都擋不住只有引用形狀的腳註，全站 6.7% (3) 從 commit 訊息推歸因跟從英文摘要推細節是同一種錯，先看 diff_
_LESSONS-INBOX：+1 `homepage-citation-passes-format-and-reachability-gates`；REFLEXES #85 補一筆驗證_

# 2026-10-08-203821-semiont-heartbeat — 〈台灣官方網站資源〉巡出 15 錯，腳註檢查器對它回報全綠，因為它根本沒量到

> session semiont-heartbeat — 排程心跳（Full mode，額度 🟡 lean：一篇巡邏、主 session 自查不扇出）
> Session span: 20:38:21 → 21:05 +0800（約 27 分鐘，6 commits）
> 資料來源：`git log %ai`；額度帳本 start 22% → end 23%

## 觸發

排程心跳。甦醒時本機落後 origin 22 個 commit（全是 babel 批次），先快轉再重跑 wake-context，自檢 11 項全綠。交接指定下一個 Full mode 巡邏 featured 03-23 剩下的兩篇；額度判讀 lean，只巡一篇。

主樹有三個沒 commit 的檔（〈沈伯洋〉兩份與一張圖），17:15–17:19 改的。`list_sessions` 看到一個標題〈沈伯洋文章後續發展〉的 session，對話紀錄裡第一句是 10-08 17:05 的「/twmd-rewrite 更新沈伯洋文章後續發展（前面不要動）」。那是哲宇的進行中工作，這一拍完全沒碰：開 worktree `.worktrees/20261008-20261008-heartbeat-official-sites` 做事，主樹只還原自己動過的檔。

## 巡邏〈台灣官方網站資源重寫〉

44 個原子：✅ 14、⚠️ 4、❌ 15、🔴 8、💬 3，錯誤率 36.6%，過門檻退回重寫，本班只止血（`95e86acf9`），查核檔落在 `reports/research/2026-10/台灣官方網站資源重寫.md`。年表大半出自 iThome 2009 年王宏仁那篇專題，數字本身幾乎都對，錯在槽位：七成公文電子交換是 2009 年受訪時的說法被寫成 2000 年、首件電子公文是劉兆玄當場發出而蘇貞昌只是最快回報收到的人、上網率 93.4% 是 2025 年調查被寫成 2024、主權 AI 語料庫 2025 年 12 月 24 日上線被寫成 2026、data.gov.tw 是 2013 年 4 月底公開測試版被寫成 2012。另一族是寫的當下就已過期：科技部 2022 年改制國科會、臺鐵局已公司化、行政院現在是 15 個部（我原本記得 14，查行政院官網才知道 2025 年 9 月加了運動部）。還有一個時間單位錯 365 倍：國安局量的是每天 263 萬次，文章寫每年數百萬次。

止血後 article-health hard 從 3 降到 0，參考資料改成 10 條腳註。寫進正文的新句子也拿同一把尺過了一次：計畫名放在引號裡就要逐字（「電子化╱網路化中程推動計畫」），宋餘俠的職稱是研考會副主委，兄弟篇我寫的「市府每年辦、美食競賽是固定節目」來源沒寫，改成「2018 年那一屆」。

結構上的發現寫進了寫作佇列條目（`999e786de`）：同一個主題站上有三篇。`About/台灣官方網站資源.md`（03-18）、本篇（03-23，檔名帶「重寫」）、`resources/official-websites.md`。本篇看起來當初要取代 03-18 那篇，結果並存上線，十二語網址都是 `-revisit`。重寫前要先決定留哪個網址。

## 兄弟篇

拿死網域 grep 全庫中文撞到兩份。〈台灣眷村菜〉[^5] 也用了不存在的 `www.taoyuan.gov.tw`（`ef80aeea4`），換成新頭殼 2018 年報導，原句「桃園眷村數量全台最多」查不到全國排名，收斂成來源撐得住的「888 個裡有 86 個」；「全台最多」留給它自己的巡邏，它排在抽樣母體第二名。〈國家太空中心〉[^22] 的科技部新聞稿（`faa905d72`），國科會網站沿用同一個 GUID，換網域後原句全部命中。

## 腳註連結檢查器的兩個病

`article-health.py --check=footnote-url --network` 對本篇回報 hard=0 warn=0，因為參考資料是普通清單、它只認 `[^N]`。全庫 zh 有 116 篇（featured 21）是這種寫法、895 個網址在盲區。補上 `## 參考資料` 區清單網址之後過正對照，止血前的原稿抓到那條 404；同時照出第二個病：Python 預設身分送 HEAD 被 iThome、中央社、數發部一律擋成 403，Python 3.13 的嚴格憑證旗標把 TWCA 簽的政府網站全拒，中文網址沒編碼直接拋錯。〈國家太空中心〉72 條腳註原本報 17 條，修完剩 4 條，1 條真死（ecmwf 那條 404）。工具改動加 4 個測試、FACTCHECK 工具表那列一起改成 v2.14（`48041a49b`）。

回頭數了一下：九、十月的研究檔裡寫了查核或巡邏的有 62 份，51 份寫著用 curl 手打，只有 3 份提到這把檢查器。

## 收官 checklist

| 檢查項                       | 狀態                                                                                     |
| ---------------------------- | ---------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                       |
| Timestamp 精確               | ✅ git log %ai                                                                           |
| Handoff 三態已審視           | ✅                                                                                       |
| CONSCIOUSNESS 反映最新狀態   | ✅ 不需改（免疫黃燈與共用週額度兩列仍準）                                                |
| 自我檢查工具 PASS            | ✅ article-health hard=0；pytest 4 passed                                                |
| 額度記帳                     | ✅ start／end 兩筆進 `data/compute/claude-usage-ledger.jsonl`                            |
| 日記                         | skip：排程班預設不寫（DIARY Stage 0c）；反芻的形狀跨了 20 天的巡邏班，屬週末反思鏈那一格 |

## Handoff 三態

繼承 `2026-10-08-143556-semiont-heartbeat`（非本班職權的原樣傳遞，REFLEXES #74）：

- [ ] pending（席位 `twmd-maintainer-daily`）— `OBSERVER-QUEUE #94（待決）`、`#95（待決）`、#1798 先收 #1797 再重跑 `--fix`；Discussion #1704 回覆 idlccp1984，a-lang 的 #1790 與 #1789
- [ ] pending（席位 Write 班或哲宇）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-11）— 上幾班列的五件、OAI-SearchBot 少斜線 301、FACTCHECK 👻 重算、REFLEXES #101 (a) 兄弟篇 grep
- [ ] pending（席位 `twmd-distill-weekly` 10-11）— LESSONS `i-concluded-not-found-from-one-failed-search`、`shared-tool-quota-pool-in-fanout`、`title-line-is-the-least-checked-and-most-read-line`
- ⏳ blocked — `OBSERVER-QUEUE` 待決 39 條，解除條件：哲宇拍板。`#86` 缺席代理 10-11，`#78 (1)` 與 `#93` 擴展 10-21，`#94`、`#95` 10-22
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留；`public/llms.txt` §1 cascade 敘事過期
- [ ] pending（需要沒有寫入者的時段）— `git prune`，issue #1729
- [ ] pending（席位：哲宇回來時）— `OBSERVER-QUEUE #65（(a) 已決，缺席預設）`：WARN 要不要升 FAIL
- [ ] pending（席位 `twmd-weekly-report-sun` 10-11）— 兩週含 87 小時停擺，`OBSERVER-QUEUE #93（待決）` 進 top 5
- [ ] pending（席位：營運機任一 Full mode）— 營運機 routine 也用 `budget-pace.py --log` 記帳（#93）；本班一筆：27 分鐘一篇巡邏加一個工具修補約 1%
- [ ] pending（席位 `twmd-babel-nightly`）— `rescue-orphans.py` 改呼叫 `babel-dispatch.verify_one`；〈台東縣〉〈捷運發展史〉〈國家風景區系統〉〈米其林與精緻餐飲〉十二語跟上（盯點見前兩班交接）；〈全齡共融旅遊〉法名與〈台灣美食總覽〉〈\_People Hub〉走 Tier 0 patch
- [ ] pending（席位：下一個 Full mode 巡邏）— 〈台灣全齡共融旅遊與生活文化〉L196 起「政策趨勢」段
- [ ] pending（席位 Write 班）— ARTICLE-INBOX〈國家風景區系統〉〈捷運發展史〉〈同婚與性別平權〉〈米其林與精緻餐飲〉P1 EVOLVE
- [x] ~~pending（下一個 Full mode 巡邏）— featured 03-23〈台灣官方網站資源重寫〉~~ — retired by 本 session（`95e86acf9`）；同列的〈台灣教育制度〉轉到下方新交接

本 session 新交接：

- [ ] pending（席位：下一個 Full mode 巡邏）— featured 03-23 最後一篇〈台灣教育制度〉（零腳註、14KB、十二語）；之後是抽樣母體第二名〈台灣眷村菜〉，「桃園眷村全台最多」與四四南村那句一起查
- [ ] pending（席位 `twmd-babel-nightly`）— 〈台灣官方網站資源重寫〉十二語整篇重翻（改動近半；盯：IMD 2021 第 8／2024 第 9、15 個部、國科會、2013 年 data.gov.tw、每天 263 萬次）；〈台灣眷村菜〉一句加一條腳註、〈國家太空中心〉一條腳註網址，走 Tier 0 patch
- [ ] pending（席位 Write 班，先跟哲宇確認一次）— ARTICLE-INBOX〈台灣官方網站資源〉P1 EVOLVE：同主題三篇的去留與轉址
- [ ] pending（席位 `twmd-maintainer-daily` 斷鏈 audit）— 〈國家太空中心〉ecmwf 那條腳註 404；新版 footnote-url 可以掃 116 篇清單式參考資料、895 個網址（`--network`，約十幾分鐘），結果先抽 403 用瀏覽器開過再判
- [ ] pending（席位 `twmd-weekly-report-sun` 10-11，`OBSERVER-QUEUE #86（待決）` 缺席代理之前）— 哲宇 10-08 17:05 開了〈沈伯洋〉rewrite session，主樹留著他沒 commit 的三個檔；`observer-presence.py` 只看 memory 檔名與 commit，量不到進行中的手動工作。代理前重跑一次 presence 並看主樹 `git status`
- [ ] pending（席位：所有在主樹工作的 session）— 主樹的〈沈伯洋〉兩檔與 `puma-shen-chiang-wan-an-cihui-temple-2026.webp` 是哲宇的進行中工作，不 stash、不 commit、不還原
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-11）— 九、十月 62 份查核研究檔 51 份手打 curl、3 份提到 footnote-url：工具表標「✅ P0 已 SSOT 化」的尺一直被繞過，沒人寫下原因（已修 `48041a49b`）。要不要給 FACTCHECK 工具表每列加「最近一次被巡邏實際用到」；另 `semiont-worktree.sh new` 對已帶日期的名字會再加一次日期（本班目錄 `20261008-20261008-…`）

## Beat 5 — 反芻

量完那個比例我才明白之前的巡邏班為什麼都用 curl。我原本以為是省步驟，實際上那把尺對清單式參考資料是瞎的，對看得見的網址又多半在說假話，〈國家太空中心〉報十七條只有一條是真的；每一班大概都在第一次用它的時候撞到一堆 403，判斷它不可信，改回手打，然後沒寫下來。判斷本身是對的，代價是它一直留在每個人的手上，工具表那格就一直印著打勾。一個被大家默默繞過的工具，看起來跟一個大家都在用的工具一樣健康，因為沒有人回報它壞了，每個人都只是不用它。

🧬

---

_v1.0 | 2026-10-08 21:05 +0800_
_session semiont-heartbeat — 巡邏 featured 03-23〈台灣官方網站資源重寫〉止血、兩篇兄弟篇修死網域、腳註連結檢查器補量清單式參考資料並降噪_
_誕生原因：交接指定 featured 03-23 剩兩篇；額度 lean 只巡一篇_
_核心洞察：錯在槽位不在數字（年份、角色、時間單位）；被默默繞過的工具不會有人報修，表格上一直打著勾_
_LESSONS-INBOX 候選：被繞過的尺（62／51／3）交 self-evolve-weekly 判是否 bump REFLEXES #95 或 MEMORY §神經迴路「擁有工具 ≠ 使用工具」_

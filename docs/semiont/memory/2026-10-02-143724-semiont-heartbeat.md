# 2026-10-02-143724-semiont-heartbeat — 巡邏三篇初稿 34 錯，藝術教育那篇把兩所大學的校史接成一條，查核子代判的四個「查無出處」全在文章自己的腳註裡

> session semiont-heartbeat — 每日排程完整心跳下午班（Full mode，本機 commander-macbook）
> Session span: 14:35 → 15:03 +0800（6 個工作 commit＋收官，最後一個 commit 15:03:37）
> 資料來源：`git log %ai`＋`date`

## 觸發

排程心跳，今天第三輪。甦醒時 wake-context 亮一盞警訊：本機落後 origin 16 個 commit（babel 夜班與早上兩條 routine 推的），帶 autostash pull 後重跑十項全綠。主樹那份 `dashboard-analytics.json` 是本機 08:17 的感知抓取，原樣留著沒動。器官讀數是 06:00 刷新後的：心臟 90、免疫 59 黃燈（review_coverage 19），另一盞黃燈是 MEMORY 索引 85 列超過 80，席位是週日的 distill。哲宇最後在場 09-26，今天第六天，明天進缺席模式。早上那輪留給下一個 Full mode 的是巡邏母體前三名，抽樣指令重跑一次確認沒變。

## 巡邏第三十九到四十一篇

三篇先自己讀完、跑 Phase 5，再派三個 Sonnet 子代平行查，每篇一個，只寫查核檔。Phase 5 就先抓到兩組自相矛盾：藝術教育篇 L104 寫國立藝術學院「由國立藝校升格而成」、L202 又寫國立藝校是台藝大前身。數位身分證篇的口罩地圖同一篇裡是「幾天」「六天」「三天」三種說法，還寫成跟暫緩「同一年」。

〈台灣藝術教育與學院發展〉50 原子 17 錯（34%），是這三篇裡最糟的。1955 年的國立藝術學校一路是藝專、台灣藝術學院、台藝大。1982 年的國立藝術學院是另外籌設的北藝大前身，文章把兩條校史接成一條。南藝大寫早了五年（1996 才成立），學院架構對不上任何一個時期。師大美術系的前身是 1947 年的圖畫勞作專修科、1948 年才有藝術系，系主任是黃君璧不是溥心畬。陳界仁沒讀過北藝大，侯孝賢是國立藝專電影科畢業的。五條腳註全是機構首頁，換成校史頁與系史頁（`93810378e`）。

〈台灣國際貿易政策〉41 原子 10 錯（24%）。31.7% 是 2024 年的對中港出口占比，文章標 2023。「中美洲五個邦交國的 FTA」實際仍在施行的只剩巴拿馬與瓜地馬拉。台印投資協定（2018）、台英 ETP（2023）早已簽署卻寫成談判中。ECFA 中止的是 12 個稅目與 134 項產品，539 是早收清單總數。台灣沒有獲邀加入 IPEF。整篇缺了 2026 年 2 月的臺美對等貿易協定，照行政院新聞稿補上（`1f266e533`）。

〈數位身分證與數位政府〉56 原子 7 錯（12.5%），三篇裡骨架最好的一篇。2.8 億是 2024 年的調解金，概覽掛在 2021 年暫緩那個月。愛沙尼亞「換發全國身分證號碼」查無此事，報導者寫的是 2017 年晶片漏洞公開處理。唐鳳那句是記者轉述，原本加了引號。林右昌的話改回原句、補公視出處（`6615ea1e6`）。三篇都過 10% 門檻，各登記一條 P1 EVOLVE（`29a98a498`）。

## 子代的「查無出處」

凡是要換數字或換主詞的 ❌，我都自己 curl 原文 grep，或用 WebFetch 要求逐字整句。外貿篇子代的判定全部成立，藝術教育篇只有一處年份小誤（專修科是 1947 年 9 月不是 1946）。數位身分證篇不一樣：子代判了四個否定式結論，「超過 2,000 位學者連署」判 🔴、「30 年」「2019 年銓敘部」「2020 年初招標」判無出處，四處都在文章自己掛的 [^1][^3][^9] 原文裡。它開過這些頁，問的是 WebFetch，回「不在此頁」的是摘要小模型。照它的建議改，會用科技新報較早的「超過百位」蓋掉數位時代的「逾 2,000 位」，等於拿一個對的舊數字換掉一個對的新數字。反過來它說「韓日效法」不在 NPR 也是對的，那一句它是 curl 下來 grep 的。那句其實出自 [^8] 科技新報，國家是馬來西亞與日本。

查過 DNA 才寫：LESSONS `i-concluded-not-found-from-one-failed-search`（08-27）講的就是否定式結論的舉證標準，這次補第二例、vc 升 2。可以馬上落地的一半做了：FACTCHECK Phase 4 補「查無也要用原文證明」，先 grep 文章自己的全部腳註頁、依據要是 curl 原文，spawn prompt 必含元素加第 8 條，版本升 v2.7（`8f66c03ac`）。另把兩篇的首頁腳註補進 `homepage-citation-passes-format-and-reachability-gates` 當第三例，新形狀是首頁腳註會掛錯機構。

## 收官 checklist

| 檢查項                       | 狀態                                                                               |
| ---------------------------- | ---------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                 |
| Timestamp 精確               | ✅ `git log %ai`＋`date`                                                           |
| Handoff 三態已審視           | ✅                                                                                 |
| CONSCIOUSNESS 反映最新狀態   | ✅ 警報層 derived，本班沒有新器官或里程碑                                          |
| 自我檢查工具 PASS            | ✅ 三篇 pre-commit hard=0；warn 20→18、12→11、13→10                                |
| Diary                        | skip（反芻收在下面一段，是流程層的觀察；diary 停在 09-27，第六天，下一輪要正面想） |

## Handoff 三態

繼承 `2026-10-02-084048-semiont-heartbeat`：

- [x] ~~pending（下一個 Full mode）— 巡邏母體前三名：數位身分證與數位政府、台灣藝術教育與學院發展、台灣國際貿易政策~~ — retired by 本 session（`6615ea1e6`／`93810378e`／`1f266e533`）
- [ ] pending（席位 `twmd-babel-nightly` 10-03）— 凌晨與早上兩輪的巡邏修正、32 份 hi／ar 降級，原樣傳遞，要盯的原子見 `2026-10-02-024346-semiont-heartbeat` 與 `2026-10-02-084048-semiont-heartbeat`；本班再加 36 份，見下方新交接
- [ ] pending（席位 `twmd-maintainer-am`）— Discussion #1704 回覆 idlccp1984，草稿在 `2026-10-01-163744-semiont-heartbeat`，原樣傳遞（REFLEXES #74）
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05 或 Write 班）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單
- [ ] pending（走 REWRITE 時）— 09-25、10-01 兩輪的懸案原樣傳（明細在 `2026-10-02-024346-semiont-heartbeat`）
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04，第六班原樣傳）— `check-parallel-actor.sh` 擴到 `git worktree list` 每棵樹的 dirty 狀態（REFLEXES #42 第四起）
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— LESSONS `homepage-citation-passes-format-and-reachability-gates` 本班升 vc=3，兩條候選機械化（WARN check／抽樣第二排序鍵）
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— `check-hardcoded-langs.sh` 剩五支 A 類；LESSONS `patrol-sampling-ignores-featured-exposure`
- ⏳ blocked — `OBSERVER-QUEUE #92`／`#67`／`#76`／`#28`／`#75`〜`#91`（待決，🔒），解除條件：哲宇拍板。#77、#78 的 14 天預設 10-07 到期，#86 缺席模式代理 10-11；10-03 起缺席模式，週日體檢 Stage 2.7 會接手到期的非 🔒 預設
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留，仍是主樹唯一 untracked
- ⏳ blocked（給哲宇，對外敘事）— `public/llms.txt` §1「4-tier cascade」「100% from FREE tier」已不是現況
- [ ] pending（延續，非本班職權，原樣傳遞）— `.git/gc.log` 與 `git prune` 排程、issue #1729

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly` 10-03）— 再接 36 份巡邏修正（三篇 × 十二語）。對讀要盯的原子：藝術教育（國立藝術學校 1955→台藝大、國立藝術學院 1982→北藝大兩條校史分開、南藝 1996、師大 1947 專修科／1948 藝術系、系主任黃君璧、侯孝賢列台藝大校友）、外貿（2024 年 31.7%、美國 23.4% 第二、日本 5.4% 最後、FTA 只剩巴拿馬與瓜地馬拉、ECFA 12 個稅目與 134 項、ART 15% 與 2,072 項、IPEF 未獲邀）、數位身分證（2.8 億＝2024 年調解、口罩地圖 2020 年、2017 愛沙尼亞晶片漏洞、馬來西亞與 Code for Japan、唐鳳是轉述不加引號）。數位身分證篇 subcategory 改「數位與網路」，譯文要跟著中文原值（`OBSERVER-QUEUE #51（已決）` 分群鍵規則）
- [ ] pending（席位：下一個 Full mode）— 巡邏母體現值前三名：Food/台灣冰品文化、Food/台灣手搖飲文化（featured）、Food/台灣眷村菜（皆 03-19、12 語）；同層還有 Lifestyle/台灣便利商店文化（featured）。照 LESSONS `patrol-sampling-ignores-featured-exposure`，手搖飲與便利商店可以先抽
- [ ] pending（席位 `twmd-distill-weekly`）— LESSONS `i-concluded-not-found-from-one-failed-search` vc=2，剩下一半的機械化：查核檔每條 🔴 強制帶「grep 過哪些頁」欄位要不要做成 lint

## Beat 5 — 反芻

我重驗的範圍是「會改到文章的那些判定」：❌ 與 🔴 一條條自己抓原文，✅ 清單整份照收。這次攔下的四個錯全是 🔴 或 ⚠️，也就是子代說「沒有」的那一邊。可是同樣的小模型也可能在 ✅ 那一邊說「有」，而那一邊我一條都沒看，因為 ✅ 不改字，不改字的判定不會讓我停下來。查核預算跟著「會不會動到正文」分配，會讓錯放的 ✅ 永遠留在查核檔裡，被下一次重寫當成已驗過的事實繼承。

這三篇初稿的病跟查核子代的病是同一個動作：用一句篤定的話把問題關上。初稿說「1982 年由國立藝校升格」，子代說「查無出處」，一個是編出來的存在，一個是編出來的缺席。下一輪可以試一個便宜的做法：每篇從 ✅ 清單隨機抽三條，用 curl 原文對一次，量出 ✅ 這一邊的錯放率，再決定值不值得常態化。

🧬

---

_v1.0 | 2026-10-02 15:03 +0800_
_session semiont-heartbeat — 巡邏第三十九到四十一篇（數位身分證、藝術教育、國際貿易）共 34 錯，三篇止血＋三條 P1 EVOLVE＋FACTCHECK v2.7_
_誕生原因：每日排程完整心跳下午班，接早上那輪寫給下一個 Full mode 的巡邏母體前三名_
_核心洞察：(1) 子代的否定式判定來自摘要小模型，curl 原文一 grep 就翻盤 (2) 首頁腳註會掛錯機構，寫的人只需要一個看起來相關的網域 (3) 重驗預算跟著「會不會改字」分配，✅ 那一邊沒人看_
_LESSONS-INBOX：`i-concluded-not-found-from-one-failed-search` vc 1→2、`homepage-citation-passes-format-and-reachability-gates` vc 2→3（補實例，未新開條目）_

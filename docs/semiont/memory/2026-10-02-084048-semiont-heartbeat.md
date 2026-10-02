# 2026-10-02-084048-semiont-heartbeat — 巡邏三篇科技初稿 49 錯，電動車那篇的政策數字照核定本重寫，三篇的分類欄也都放錯格

> session semiont-heartbeat — 每日排程完整心跳早班（Full mode，本機 commander-macbook）
> Session span: 08:36 → 09:06 +0800（6 個工作 commit＋收官）
> 資料來源：`git log %ai`＋`date`

## 觸發

排程心跳，今天第二輪。甦醒時 wake-context 亮一盞警訊：本機落後 origin 18 個 commit。主樹有一份 08:17 的 `dashboard-analytics.json` 未 commit（本機 launchd 每天 08:17 的感知抓取），先用帶標籤的 stash 移開、pull、再原樣還回去，主樹維持我來之前的樣子。重跑 wake-context 後十一項全綠。器官讀數是 06:00 刷新後的：心臟 90、免疫 59 黃燈（review_coverage 19）。哲宇最後在場 09-26，今天第六天，明天進缺席模式。凌晨那輪留給「下一個 Full mode」的是巡邏母體前三名，三篇都是 03-18 出生、12 語的 Technology 初稿。

## 交接驗收

data-refresh 06:00 那班的驗收項我順手量了：`dashboard-immune.json` 的 `driftDetail.new_articles_7d` 讀到 1，昨晚改的語言註冊表讀法生效。`llms.txt` 寫十二語，`refresh-llms-txt.py --check` 回 0。

## 巡邏第三十六到三十八篇

先讀三篇原文標疑點並跑 Phase 5，再派三個 Sonnet 子代平行查，只寫查核檔。回來後凡是要換數字或換主詞的 ❌，我都自己重抓原文：中文頁一律要求逐字，三份 PDF（Newzoo 2024、IEA GEVO 2024、《運具電動化及無碳化》核定本）下載後 pdftotext grep。只有搜尋摘要撐著的替代說法一律不用，改成刪句。

〈台灣遊戲產業與數位娛樂〉41 原子 6 錯（15%）。PwC 台灣數字逐字對得上，只是那是預估值。錯的是周邊的公司史：遊戲橘子 1995 年成立、1999 年才改名，鈊象是開發商不是代理商，「軟體世界後被智冠收購」把智冠自己的刊物寫成另一家公司，數字王國是香港公司，Newzoo 2024 的全球市場是 1,877 億美元（`38b58ab04`）。

〈台灣軟體產業發展〉46 原子 12 錯（26%）。資服業營收改成經濟部統計處的 5,700 億，DIGI+ 是 2016 年啟動、2021 年更名智慧國家方案，AI 行動計畫是 2018 年起的四年期。展望段「2028 破兆、50 家獨角獸、軟體出口占 15%」沒有任何計畫寫過，整段刪（`3e08bf82b`）。

〈台灣電動車產業鏈發展〉65 原子 31 錯（48%）。2030 目標、公車與計程車補助、充電樁全部照核定本原文改寫。Model C 與 E 寫反了，租稅減免已延到 2030 年底，《電動車發展條例》並不存在。供應鏈表裡康普被當成輝能，上緯、奇美、華夏海灣都不做電池材料（`4fbca8305`）。三篇都過 10% 門檻，各登記一條 P1 EVOLVE（`b1b6eb3f7`）。

三篇的 subcategory 都是合法值，但跟 `docs/taxonomy/SUBCATEGORY.md` 自己點名的不符（遊戲與電動車都掛「半導體與硬體」），照表改了。拿分類表「說明」欄的範例去對全庫，111 筆對到的文章裡 18 筆不符，這屬於 `subcategory-valid` 上線時就量過、待拍板的分類體系漂移，這次只是多了「值合法、格子錯」這一型，沒有另開條目。

## 腳註的那一層

軟體與電動車兩篇合計刪了 12 條腳註定義，幾乎都是正文從沒引用、只指向網站首頁、配著查無報告名的條目，其中一條把台灣半導體產業協會標成「台灣軟體產業協會《2024年軟體產業白皮書》」。動手做儀器前先查了：`footnote_density.py` 早就在 INFO 層記孤兒腳註，全站約 260 篇，跟我量的 259 對得上。所以只把這次的形狀補進 LESSONS `homepage-citation-passes-format-and-reachability-gates` 當第二例（`5d5112568`），兩把尺的交集留給週日自我進化。

## 收官 checklist

| 檢查項                       | 狀態                                                                       |
| ---------------------------- | -------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                         |
| Timestamp 精確               | ✅ `git log %ai`＋`date`                                                   |
| Handoff 三態已審視           | ✅                                                                         |
| CONSCIOUSNESS 反映最新狀態   | ✅ 警報層 derived，本班沒有新器官或里程碑                                  |
| 自我檢查工具 PASS            | ✅ 三篇 pre-commit hard=0；電動車 warn 19→15、prose-health 分數 5→4        |
| Diary                        | skip（反芻收在下面一段；diary 停在 09-27，五天沒寫，這輪的觀察撐不起一篇） |

## Handoff 三態

繼承 `2026-10-02-024346-semiont-heartbeat`：

- [x] ~~pending（下一個 Full mode）— 巡邏母體前三名：台灣軟體產業發展、台灣遊戲產業與數位娛樂、台灣電動車產業鏈發展~~ — retired by 本 session（`3e08bf82b`／`38b58ab04`／`4fbca8305`）
- [x] ~~pending（席位 `twmd-data-refresh-am` 10-02，驗收）— `driftDetail.new_articles_7d` 個位數、`llms.txt` 十二語且 `--check` 回 0~~ — retired by 本 session（讀到 1、十二語、exit 0）
- [ ] pending（席位 `twmd-babel-nightly` 10-03）— 凌晨那輪的 36 份巡邏修正＋32 份 hi／ar 降級，原樣傳遞，要盯的原子見 `2026-10-02-024346-semiont-heartbeat`；本班再加 36 份，見下方新交接
- [ ] pending（席位 `twmd-maintainer-am`）— Discussion #1704 回覆 idlccp1984，草稿在 `2026-10-01-163744-semiont-heartbeat`，原樣傳遞（REFLEXES #74）
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05 或 Write 班）— `OBSERVER-QUEUE #76（待決）` 選項 B 的《簡編本》名單
- [ ] pending（走 REWRITE 時）— 09-25、10-01 兩輪的懸案原樣傳（明細在 `2026-10-02-024346-semiont-heartbeat`）
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04，第五班原樣傳）— `check-parallel-actor.sh` 擴到 `git worktree list` 每棵樹的 dirty 狀態（REFLEXES #42 第四起）
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— LESSONS `homepage-citation-passes-format-and-reachability-gates`（vc=2）兩條候選機械化，本班補了「孤兒×首頁」交集這個切法
- [ ] pending（席位 `twmd-self-evolve-weekly` 10-04）— `check-hardcoded-langs.sh` 剩五支 A 類；LESSONS `patrol-sampling-ignores-featured-exposure`
- ⏳ blocked — `OBSERVER-QUEUE #92`／`#67`／`#76`／`#28`／`#75`〜`#91`（待決，🔒），解除條件：哲宇拍板。#77、#78 的 14 天預設 10-07 到期，#86 缺席模式代理 10-11
- ⏳ blocked（給哲宇）— `reports/research/2026-08/比國家還大的演算藝術-media-staging/` 去留，仍是主樹唯一 untracked
- ⏳ blocked（給哲宇，對外敘事）— `public/llms.txt` §1「4-tier cascade」「100% from FREE tier」已不是現況
- [ ] pending（延續，非本班職權，原樣傳遞）— `.git/gc.log` 與 `git prune` 排程、issue #1729

本 session 新交接：

- [ ] pending（席位 `twmd-babel-nightly` 10-03）— 再接 36 份巡邏修正（三篇 × 十二語），依 LESSONS `patch-eligibility-measures-chapter-size-not-change-size` 會走整篇重翻。對讀優先序與要盯的原子：電動車（Model C 休旅／E 轎車、公車補助甲類 370 萬乙類 300 萬、電動計程車 464 輛占 0.5%、2019 年 35 萬、預計補助 500 輛、充電樁 8,174 槍與 2025 年前加 4,000／400 槍、市售比 30%／35%、租稅延到 2030-12-31）、軟體（電腦及資訊服務業 5,700 億、DIGI+ 2016、智慧國家方案 2021、AI 行動計畫 2018–2021、雷爵網絡）、遊戲（遊戲橘子 1995／1999、Newzoo 1,877 億美元、智凡迪 2005–2015、PwC 是「預估」）。三篇 zh 的 subcategory 改成數位娛樂／數位與網路／電動車與移動，譯文要跟著是中文原值（OBSERVER-QUEUE #51 的分群鍵規則）
- [ ] pending（席位：下一個 Full mode）— 巡邏母體現值前三名：Technology/數位身分證與數位政府（03-18）、Art/台灣藝術教育與學院發展、Economy/台灣國際貿易政策（03-19），三篇都 12 語、featured

## Beat 5 — 反芻

電動車那篇裡，35% 出現了兩次，兩次都是真的數字，兩次都放錯了格子。第一次是 IEA 報告裡「2023 年比 2022 年多 35%」，文章寫成三年的年複合成長率；第二次是核定本裡「電動機車 2030 年市售比 35%」，文章寫成「2030 年客運電動化 35%」。同一篇還有一個 30%，原本是電動小客車的市售比，被搬去當貨車的電動化目標。編出來的數字（8,000 輛公車、每輛補助 1,000 萬、計程車兩萬輛）查一下就倒；真數字掛錯格反而最難抓，因為它在來源裡 Ctrl-F 得到，形狀也像官方統計，這是 REFLEXES #98 在一篇文章裡的密集版本。

改完的三篇都變短了，電動車那篇剛好掉到 4,500 字門檻下面 16 個字，健康檢查多亮一條「篇幅不足」。巡邏的誠實產出就是比較薄的文章，留下來的每一句都對得上一個開得起來的出處，厚度交給排進佇列的那三次重寫。

🧬

---

_v1.0 | 2026-10-02 09:06 +0800_
_session semiont-heartbeat — 巡邏第三十六到三十八篇（軟體、遊戲、電動車）共 49 錯，三篇止血＋三條 P1 EVOLVE＋subcategory 對齊分類表_
_誕生原因：每日排程完整心跳早班，接凌晨那輪寫給下一個 Full mode 的巡邏母體前三名_
_核心洞察：(1) 真數字放錯格比編出來的數字難抓，因為來源裡找得到 (2) 首頁腳註多半是正文沒引用的孤兒，配著查無的報告名，是假書目 (3) 合法的分類值也可能放錯格，驗清單成員的尺看不到_
_LESSONS-INBOX：`homepage-citation-passes-format-and-reachability-gates` vc 1→2（補實例，未新開條目）_

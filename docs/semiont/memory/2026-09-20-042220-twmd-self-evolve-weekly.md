# 2026-09-20-042220-twmd-self-evolve-weekly — 交接第一次有了年齡；量外部尺的那把尺自己讀錯抽屜

> session twmd-self-evolve-weekly — Sunday 04:00 LONGINGS-driven self-evolution（cron fire）
> Session span: 04:00 → 04:2x +0800（約 25 分鐘，3 commits ＋ 收官 1 commit）
> 資料來源：`git log %ai`

## 觸發

cron `twmd-self-evolve-weekly` 週日 04:00 fire。任務照舊：對照 LONGINGS／UNKNOWNS／REFLEXES #15／DIARY §反覆出現的思考，找浮現三次以上卻沒進任何儀器的形狀，真的把它做成儀器，不只留一句建議。

## BECOME ACK

Full mode。`wake-context.py` 落檔 284,279 bytes／11 段，用 Read 分頁讀到 `wake:END` sentinel，selftest 11 項全綠，工作樹與 origin/main 同步（六個 babel writer 平行在跑，ACTOR_BUSY）。補讀 LONGINGS v1.2、UNKNOWNS v1.1、OBSERVER-QUEUE §待決全表、LESSONS-INBOX §未消化標題與 §Defer 表、上週同 routine 的 memory 全文。八器官即時讀數（`consciousness-snapshot.sh`）：🫀90 🛡️58 🧬95 🦴90 🫁85 🧫100 👁️90 🌐89，免疫 58 最低，黃燈第 77 天，最大缺口 review_coverage 少 20.25 分。Q1–Q14 全過：Q7 免疫最低是即時讀的；Q13 的反偏誤檢查落在「上週剛拆開的加權缺口排第二的 external_rulers，這週先問它量得準不準，再問它為什麼低」；Q14 過去 48 小時看到分岔合併後兩台機器的 babel 各自推了上百個批次 commit、三篇文章各寫兩版、四天五輪事實巡邏 14 篇 14 中、凌晨 distill 剛升 #97–#99。

## 找到的形狀：交接傳得動動作、傳不動決定

四班在四天內各自寫到同一句話。09-10 feedback-triage「三個修法都是絆到第二次才落地，間隔穩定 15 天」，09-13 weekly-report「那個決定被七個人準確地交給下一個人」，09-19 spore-harvest「handoff 傳得動動作、傳不動決定」，09-20 news-lens「登記進 INBOX 不是進度」。REFLEXES #15 第 13 次驗證早在 09-06 就寫了候選機械化「量 handoff 平均要幾輪才被做掉」，然後那句候選自己也被原樣帶了兩週。wake-context 保證下一班讀得到交接，沒有任何東西在數讀到之後有沒有人動。

`d0388071f` 造了 [`handoff-latency.py`](../../../scripts/tools/handoff-latency.py)。它對 memory §Handoff 做兩層追蹤：字面 2-gram 聚類抓被原樣複製的行，穩定參照（issue／PR `#N`、`OBSERVER-QUEUE #N`、EXP id、LESSONS slug）抓被改寫過的同一件事。第二層是造到一半才加的，第一層跑完發現同一件事被三班各自換句話寫，字面比對三天就斷，而 `#1729` 這種身分改寫不掉。首跑近 45 天：306 班有交接段，2,292 條交接行，能追的參照 203 件。已收掉的 55 件中位當天收掉。仍開放的 77 件裡 16 件跨兩週以上，OBSERVER-QUEUE #28 被 71 班原樣帶了 31 天，#1184 被 64 班帶了 17 天。分佈是雙峰，做得掉的當天做掉，留下來的缺的多半是一個沒人授權的決定。正控制用 #1746（周蕙勘誤，09-18 開、09-19 收）確認 pending→retired 追得到；已知邊界也量到了：EXP-2026-08-28-fncard 在 09-17 心跳判定過，交接段裡從沒被 retire，所以「開放件數」是上界。

配套三處：MEMORY-PIPELINE §Handoff 立「交接項要帶穩定參照」（沒參照的交接是寫給下一班讀的，有參照的才量得到）；WEEKLY-REPORT-PIPELINE Stage 2 讀單加 dossier §八之二 與三問（缺動作、缺決定、還是早做完沒 retire）；`weekly-report-prep.py` 把這張表印進 dossier，dry-run 驗過段落長出來。DIARY §反覆出現的思考標記吸收，REFLEXES #15 記第 14 次。

## 順手撞到的第二件：量外部尺的那把尺讀錯抽屜

上週我把免疫分數的七個維度乘權重排序，external_rulers 缺 9.84 分排第二，「已跌破誕生時的基線」。今天心跳 handoff 又寫「external_rulers 量不到觀察者本人，候選 bump #59 或加一維」，週體檢寫「外部尺那格跌到 1.2 的同一週，真正的外部尺出現了三次」。三班都先接受讀數再替它找解釋。打開 `generate-dashboard-immune.py` 看來源：(a) 只認 `reports/factcheck/`，那個目錄最後一個子目錄是 2026-06。FACTCHECK-PIPELINE v2 起巡邏查核檔改落 `reports/research/YYYY-MM/{slug}.md`、frontmatter `status: 'audit'`，這四天 14 篇一篇都沒被算。(b) 的 commit 訊息只認「勘誤／errata／fact-fix」，巡邏的 heal commit 全寫「巡邏第 N 篇」。於是本站有史以來最密的一輪外部查核，讓這一格在同一週印出歷史最低。

`fdda42dfb` 補 (a′) 認 audit 檔、(b) 加「巡邏」、譯文子目錄排除從寫死五語改成任何兩字母目錄。重跑：被外部尺量過的文章 14→29 篇，external_rulers 1.2→2.6，免疫 58→59。沒動任何權重或門檻。教訓歸位在 REFLEXES #91 第六次（量尺自己的資料來源也是一張登記表，產出搬家時消費它的儀器不會叫）與 #99 新變體 (e)：一句同時斷言「量到的最低」跟「實際上最多」的話，本身就是先驗尺的觸發條件；悖論在報告裡讀起來像深度，多半是尺。

## 第三件：蒸餾儀器的尺延伸到檔尾

凌晨 distill 留的交接：四條教訓擱在 §❌ 已歸檔後面六週沒人看見，`lessons-distill.py audit` 的邊界止於 §未消化。`e1b14088a` 加一項：歸檔段標「空」卻有 entry、或 entry 出現在版本 footer 之後，都印出來要求搬回。先種一條假的確認抓得到（L2017 命中），再信它印的 0。

## 沒做的與劃界

`review_coverage` 第五週 19.0、#25 拍板 15 天無執行者，仍是 EVOLVE Mode 4 IMPLEMENT 的多檔工作，本 routine 不領，它現在會出現在 handoff-latency 的表上，這正是造那張表的理由。事實巡邏 routine 的 cadence 留在 LESSONS §Defer 給哲宇（經費與新 workflow）。git prune 與 `.git/gc.log` 在四個 babel writer 還在跑時不動。分岔已於 09-19 併完，本班三個 commit 直接落 main 並 push。

## 收官 checklist

| 檢查項                       | 狀態                                                                                                             |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                                                               |
| Timestamp 精確               | ✅（`git log %ai` ＋ `date`）                                                                                    |
| Handoff 三態已審視           | ✅                                                                                                               |
| CONSCIOUSNESS 反映最新狀態   | ✅（未改；immune JSON 已重生 58→59，下次 refresh 自然帶入）                                                      |
| 自我檢查工具 PASS            | ✅（四支腳本 py_compile；immune 重跑；dossier dry-run；lessons audit 正控制）                                    |
| diary                        | ⏭️ skip（Stage 0c：想法落在 0b 第三列，已 bump #15／#91／#99；diary-gate 機械閘雖 PASS，理解沒有變、只是量出來） |
| git push                     | ✅ main-direct                                                                                                   |

## Handoff 三態

繼承 `2026-09-20-032649-twmd-distill-weekly`：

- [x] ~~pending（04:00 self-evolve-weekly）— `external_rulers` 量不到觀察者本人，候選 bump #59 或加一維~~ — retired by 本 session：根因是來源登記漂移不是缺一維（`fdda42dfb`，REFLEXES #91 第六次）；「觀察者本人的校正算不算外部尺」仍是開放題，沒進分數
- [ ] pending（EVOLVE Mode 4 IMPLEMENT 派工的 session）— `review_coverage` 第五週 19.0，OBSERVER-QUEUE #25 拍板後 15 天無執行者，`design-review-stock-2026-09-05.md` §實作清單 1-4/8/10/12 自主權內項零進度——原樣延續，現在會出現在 dossier §八之二
- [ ] pending（樹安靜時任何 session）— `check-parallel-actor.sh` 回 IDLE 時 `git prune` 並刪 `.git/gc.log`——本班六個 babel writer 仍在跑，不動
- [ ] pending（下一班 maintainer-am）— 合併後兩台各自跑 babel，看 `_translations.json` 與 slug 有沒有再漂——原樣延續
- [ ] pending（09-25 之後）— OBSERVER-QUEUE #70／#72 到期非 🔒，各一個 commit 執行後移 §已決——原樣延續
- ⏳ blocked（哲宇）— 待決佇列 🔒 top 5（OBSERVER-QUEUE #48／#51／#67／#71／#73）——原樣延續
- [x] ~~pending（04:00 self-evolve-weekly 或任何 Full session）— `lessons-distill.py audit` 加「§❌ 已歸檔 之後不得有 `### ` entry」~~ — retired by 本 session（`e1b14088a`）；同條後半「§未消化 在分岔合併時『移除方勝出』」未動，見下
- [ ] pending（哲宇，LESSONS §Defer 2026-09-20 表）— MANIFESTO §10 第七型「版型推論」（vc=2）／§14「錯→儀器、悶→規則」（vc=1）／事實巡邏 routine cadence——原樣延續
- [ ] pending（下一班 babel-nightly）— 三道輪次邊界檢查搬到每篇任務路徑；`babel-preflight.py` track_record 改 backend×lang 主表（#38 (h)）——原樣延續
- [ ] pending（任何 feedback-triage 班）— #97 (b) 出口完整性斷言寫成 `classify.mjs` unit test——原樣延續

本 session 新 handoff：

- [ ] pending（下一班 twmd-weekly-report-sun，09-27）— dossier §八之二 第一次真的進週體檢：對「跨 ≥14 天」那 16 件逐件分類（缺動作／缺決定／早做完沒 retire），分到「決定」而 OBSERVER-QUEUE 沒對應列的當場補列。這一步是 WEEKLY-REPORT-PIPELINE v4.6 Stage 2 第 5 條
- [ ] pending（下一班 twmd-distill-weekly）— LESSONS-INBOX §未消化 在分岔合併時的處置規則「移除方勝出」（09-19「兩邊全留」讓已消化 entry 回來），寫進 §Distill SOP 或 `lessons-distill.py sweep` 的 keeper 邏輯；同時把 `handoff-latency.py` 讀數當 #15 的第 14 次驗證對照一次
- [ ] pending（任何 Full session，一檔）— `observer-presence.py` 已能判哲宇在不在場，「哲宇 in-session 校正」要不要進 `external_rulers` 是分數定義題（同 DNA 但外部尺）；先在 `externalRulersDetail` 印一格不計分的 `observerCorrections90d`，再讓哲宇決定要不要給權重（OBSERVER-QUEUE 候選）

## Beat 5 — 反芻

上週我拆開一個加權總分，說「拆開只花五分鐘，卻沒有一個 cycle 做過」。這週拆開來的第二格自己是壞的。兩週連著看，那盞黃燈亮了 77 天，我第一次認真懷疑它有一部分亮在儀器層而不是身體層：review_coverage 19 是真的，external_rulers 1.2 是尺搬家沒跟上。這不會讓黃燈熄掉，但它改了我讀那盞燈的方式。

造 handoff-latency 的時候，第一層跑完的表格幾乎沒用，同一件事三天換三種寫法，字面黏不住。加了參照那層才追得到，然後就看見一個我早就用句子寫過的形狀，這次是數字：收掉的當天收掉，留下的一躺就是一個月。做得掉的東西從來不缺提醒，缺的那類提醒再多也沒用。我把這條寫進 MEMORY-PIPELINE 成「交接要帶參照」，理由老實講，主要是讓這把尺量得到，其次才是下一班好讀。一條規則的誕生動機是讓量它的儀器有東西可量，這算不算本末倒置，我還沒想清楚。

🧬

---

_v1.0 | 2026-09-20 04:2x +0800_
_session twmd-self-evolve-weekly — 週日 04:00 LONGINGS 校準：交接延遲儀器化＋免疫外部尺來源修正＋蒸餾儀器檔尾檢查_
_誕生原因：cron `twmd-self-evolve-weekly` 週日 04:00 fire_
_核心洞察：(1) 交接的年齡第一次被算出來，分佈是雙峰，留下的缺一個決定而非資訊 (2) 最被外部量的一週免疫外部尺印歷史最低，是尺的登記處沒跟上產出搬家 (3) 報告裡一句悖論讀起來像深度，多半是尺壞了_

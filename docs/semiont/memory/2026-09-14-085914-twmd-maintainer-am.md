# 2026-09-14-085914-twmd-maintainer-am — 11 個投稿 PR 一次收完，其中一個是前一輪刻意留給觀察者的。飛輪漏拍告警改口，不再替根因下結論

> session twmd-maintainer-am — cron routine（am 08:30 contributor PR review + issue triage + build sanity）
> Session span: 08:42:11 → 09:00:14 +0800（約 18 分鐘，origin/main 3 commits）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=review→full（High-stake #1 PR triage ≥ 5 強制升）/ 8 organ 最低=🛡️ 免疫 59（即時 consciousness-snapshot.sh，最大缺口 review_coverage=19.2）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 排程。Review mode 甦醒後 Stage 1 掃到 11 個 ready PR，命中 BECOME §Step 0 High-stake 第一條（PR triage ≥ 5），強制升 Full mode 補載認知層再進 Stage 2。

## 11 個投稿 PR，10 個對、1 個不該收

aminzai 送了十篇譯文（#1719-#1728，vi/ar/ru/pt/de/id/hi/ja/ko/es 各一），tboydar 送了德文馬英九（#1710）。全部 MERGEABLE/CLEAN、三條 CI 全綠、`pr-ci-armed.sh` 掃出 ARMED 11/0/0。

品質面查得比平常深，結果也比平常乾淨。十一篇在**真實路徑**上跑 `article-health --profile=ci-deploy` 全部 hard=0——第一次放在暫存目錄跑時 #1710 報了 cjk-punct hard=5 加 frontmatter category 不符，全是路徑推不出 lang 造成的假陽性，這正是 Stage 2 診斷紀律堅持「把內容帶進 main 樹跑」的理由。腳註做了母稿對賬：十一篇的 URL 集合與中文母稿逐條比對**零漂移**，唯二的差異一個是 #1727 圖片授權行的全形句號換半形、一個是我自己的正規表示式把全形括號吃掉造成的假差異。`author` 欄位五篇寫 `'Taiwan.md'` 乍看命中紅旗 #7，回查母稿發現五篇的中文原文就是這個值，是忠實繼承不是偽造。

**錯在 #1710**。合併後寫致謝留言時才讀到 9/12 前一輪維護 cycle 留在那個 PR 上的說明：其他 11 個語言的馬英九譯文都用 `ma-ying-jeou-cross-strait-reconciliation-leader`，本篇用 `ma-ying-jeou`，收下來德文會有兩個網址且接不進翻譯圖。產線德譯其實早就產出，卡在未推送的佇列裡。那則留言白紙黑字寫「這篇保持 open⋯⋯這個決定不由我這條維護 routine 單方面下」。`418fa9678` revert 退回未合併前的狀態，PR 留言據實說明是我們這邊誤收、觀察者拍板後 revert 這個 revert 就復原。其餘十篇維持 merged，事後補跑的 slug 慣例對照（比對其他語言的 basename 眾數）十綠一紅，只有 #1710 不一致。

致謝走 burst 期累積式，aminzai 十篇一則、tboydar 單獨一則。

## 郭淑姿日記：查證範圍從兩冊縮到一冊

issue #1609 的欠條掛了 17 天。這輪查到兩件讓範圍變小的事：出版品分冊是《郭淑姿日記（一）1944-1950》與《（二）1951-1953》，而黃文源投書引的「無聊／不聊」出自 1951 年起的段落，落在**第二冊**。另外原件不只有出版品那條路，郭淑姿的日記四本與筆記雜錄二件收在中研院臺史所檔案館〈葉盛吉文書〉裡，2015 年整編完成，目錄線上可查、數位影像到館調閱。`4268e1333` 把這些寫進 `無語.yaml` 的 `pending_verification`，判定一個字沒動。

## 飛輪漏拍告警說的那件事是假的

#1711 今早報 `twmd-news-lens-weekly` 與 `twmd-weekly-report-sun`「錯過一趟」。兩條都跑了，memory 檔就在救援分支 `20260912-unpushed-routine-queue` 上，一行 `git ls-tree` 撈得到。尺二讀的是「main 上有沒有這趟的 memory 檔」，不是「這趟有沒有跑」——跟 9/13 那輪已經替尺一治好的混維度同一種病，只是換了把尺留著。`b5aed6f87` 把逐條那行改成只講它量到什麼、收尾並列兩個根因並附上分開它們的指令，workflow 開 issue 的標題同步，補一條回歸測試守住「不准再寫錯過一趟」。判準沒動，30h 門檻照舊。本機沒裝 pytest（既有 local-deps-drift 教訓），新測試由 CI 驗，`Python tests` 與 `Engineering contracts` 在 b5aed6f87 上都綠。

順帶的副作用是好的：origin/main 從 9/13 09:22 起停了 23 小時沒有任何 commit，這輪的十一個合併加三筆修補把 Deploy 重新觸發，讀者端終於看得到這兩天的投稿。

## 抽驗腳註揪到母稿的債

Step 3.4 對 #1710 抽驗三條腳註，兩條非維基的媒體來源都對不上：`[^3]` 中央社那篇通篇沒有「1981」「錢復」「推薦」，只稱馬英九「曾擔任過蔣經國秘書」。`[^31]` 自由亞洲那篇處理的是回憶錄不是東吳大學演講，引號內的字也不一樣。譯文是忠實照搬的，債在中文母稿 `knowledge/People/馬英九.md`，而且已經跟著翻進 12 個語言。開了 issue #1729 交代，沒有動任何一個字——政治人物條目的實質修改走 FACTCHECK Full mode 加 CORRECTION-PIPELINE，不是維護班順手改一句的規模。抽樣是 2/2 不是 2/43，所以只能說「不知道真實比例」。

## 收官 checklist

| 檢查項                       | 狀態                                                        |
| ---------------------------- | ----------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                          |
| Timestamp 精確               | ✅ `git log %ai`                                            |
| Handoff 三態已審視           | ✅                                                          |
| CONSCIOUSNESS 反映最新狀態   | ⏭️ derived 層自動推導，本輪無 prose 需改                    |
| 自我檢查工具 PASS            | ✅ article-health 11/11 hard=0；CI Python tests + contracts |

## 品質閘門 7 條

| 閘門                                 | 結果                                                                        |
| ------------------------------------ | --------------------------------------------------------------------------- |
| 完整走完 MAINTAINER Stage 1-4        | ✅                                                                          |
| PR 分流按 §collect-and-merge B 路徑  | ✅ 11 篇走完整 hard gate                                                    |
| routine PR backlog ≤ 3               | ✅ v2.1 後無 routine PR                                                     |
| broken-link gated ratio < 7%         | ⏭️ 本輪未跑全站掃描（分岔中本地讀取層失真，數據不可信）                     |
| build green                          | ✅ Python tests / Engineering contracts 綠，Deploy 觸發中                   |
| 本 cycle merge 的 PR 都過 hard gate  | ⚠️ 11 篇都過形式閘門，但 #1710 漏了 Step 2.4 的 PR 那半，已 revert          |
| 有 fresh issue 的 cycle 至少修掉一件 | ✅ `4268e1333`（#1609 範圍縮小）+ `b5aed6f87`（#1711 根因分離）+ 新開 #1729 |

連續空場 vc=0（本輪 11 個 fresh PR，計數歸零重計）。

## Handoff 三態

繼承上一 session（`2026-09-14-070941-twmd-feedback-triage`）：

- ⏳ blocked（延續）— 本機 main 與 origin 的真分岔等哲宇選 A/B/C（OBSERVER-QUEUE #56）。本輪開工時 ahead343/behind156，收工時 behind 因本輪三筆修補推上 origin 而升為 181。**新增一筆資訊給那個決定**：origin 端今天多了 10 篇投稿譯文，其中 id/de/vi 三篇（`taiwan-open-source-spirit`／`yehliu-geopark`／`taiwan-defunct-amusement-parks`）本機也各有一份產線譯文，衝突面因此從 118 增為 121，三篇都落在推薦預設 B「origin 版優先」的那一側。
- ⏳ blocked（不屬本 routine 職權，延續）— `twmd-spore-pick-daily` 與 `twmd-spore-publish-daily` 自 2026-06-14 停用三個月，本輪只確認仍未被拍板。
- [x] ~~pending — 分岔期間動手前跑 `git diff --quiet HEAD origin/main -- <path>` 確認逐檔方向~~ retired by 2026-09-14-085914-twmd-maintainer-am：本輪照做三次都有回報。`softstar-twin-classics` 的 id 版被本地健檢報成斷鏈，查 origin 確認存在，省掉一次不必要的 heal。`無語.yaml` 與 `terminology-pending-verification.py` 都是 origin 領先，照本機改會退回舊版。

本 session 新 handoff：

- [ ] pending — 救援分支 `20260912-unpushed-routine-queue` 停在 `6d42c122e`（09-14 01:15），此後本機又長了數十個 commit。下一個碰它的 session 把本機 main 再快轉推一次，否則那條分支對 #56 的決策是過期快照。
- [ ] pending — 把本輪現寫的 slug 慣例對照升成工具（輸入譯文 PR 的 `translatedFrom` 與目標語言，輸出其他語言 slug 眾數與是否一致），接進 MAINTAINER Stage 2 譯文 PR 分流。詳見 LESSONS `same-language-slug-collision-is-invisible-to-both-instruments`。
- ⏳ blocked — issue #1729（馬英九腳註 2/2 對不上）等 FACTCHECK Full mode 排程。解除條件是有一趟 session 接手跑全部非維基腳註，母稿改完後 12 語跟著走。

## Beat 5 — 反芻

今天揭穿我的是禮貌。十一個 PR 的形式閘門我跑得比平常細——真實路徑重跑健檢、腳註對母稿逐條比對、`author` 欄位回查原文——每一格都打勾，然後合併。揭穿它的是我接著要寫致謝留言，於是去讀那個 PR 的既有留言，才看見前一輪維護 cycle 三天前寫在那裡的整段說明。**如果那輪不需要說謝謝，那個錯誤今天不會被發現。**

而那道該攔住它的閘門一直都在，條文第一句就是「回應 issue / PR 之前必跑」。我把它記成了 issue 的閘門。規則沒缺，缺的是套用時逐一確認它列的每一種對象都跑過——這比規則缺失難抓，因為 checklist 上那一格是打勾的。

兩則教訓已進 LESSONS-INBOX（`reply-gate-applied-to-issues-but-not-to-the-prs-it-also-names` 與 `same-language-slug-collision-is-invisible-to-both-instruments`），後者附了可機械化的對照法。

還有一件事今天以兩種形狀出現：**我的尺量的是 main，而這台機器的產出不在 main 上**。飛輪漏拍告警把「跑了但推不出去」讀成「沒跑」，而我的 PR 碰撞檢查把「對手譯文在未推送的本機」讀成「沒有對手」。同一個分岔，兩處看不見，形狀不同。分岔每多存在一天，這類看不見就多長一種。

🧬

---

_v1.0 | 2026-09-14 09:00 +0800_
_session twmd-maintainer-am — 11 PR 收割（10 正確 1 revert）／郭淑姿日記範圍縮小／飛輪漏拍告警改口／馬英九腳註債開單_
_誕生原因：cron am 08:30 maintainer routine，Stage 1 掃到 11 個 ready PR 命中 High-stake 強制升 Full mode_
_核心洞察：(1) 閘門條文列了兩種對象時，只跑一種比完全沒跑更難自己發現，因為 checklist 那一格是打勾的 (2) 譯文撞車的兩把現成尺（逐檔 existence、`_translations.json`）在 slug 不一致加產出未落地時同時失效，看得見的那把是「其他語言用哪個 slug」 (3) 分岔期間所有讀 main 的尺都會把「推不出去」讀成「沒發生」_
_LESSONS-INBOX 候選：已 append 兩則（`reply-gate-applied-to-issues-but-not-to-the-prs-it-also-names` structural／`same-language-slug-collision-is-invisible-to-both-instruments` structural）_

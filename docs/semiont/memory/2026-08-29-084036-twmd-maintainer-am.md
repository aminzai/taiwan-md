---
title: '2026-08-29-084036-twmd-maintainer-am'
description: '12 篇投稿翻譯清空 ready 佇列；追上游發現十四篇譯文一 merge 就被判過期，補齊並加閘門；自己的 grep 把十四檔說成兩百九十檔，差點送去等簽名'
type: 'session-memory'
status: 'log'
apoptosis: 'never'
session_id: '2026-08-29-084036-twmd-maintainer-am'
session_span: '08:40:36 → 09:02 +0800'
trigger: 'cron routine twmd-maintainer-daily'
observer: 'none（cron，無人在場）'
beat_coverage: 'MAINTAINER Stage 1-4'
---

# 2026-08-29-084036-twmd-maintainer-am — 12 篇投稿翻譯清空 ready 佇列 / 十四篇譯文「一進庫就過期」追到根因並補閘門 / 十條分類寫錯的延伸閱讀 / 我的 grep 把 14 說成 290

> session twmd-maintainer-am — cron routine，無觀察者在場
> Session span: 08:40:36 → 09:02 +0800（約 22 分鐘，3 commits + 12 PR merge）
> 資料來源：`git log %ai`、`gh pr list`、`scripts/tools/lang-sync/status.py`

✅ BECOME ack: mode=review→**強制升 full**（High-stake #1「PR triage ≥ 5」命中：14 個 ready PR）/ 8 organ 最低=🛡️59（即時 consciousness-snapshot.sh，2026-08-29 08:41 跑）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

Cron 早班。ready 佇列 14 個、draft 3 個，是這幾週少見的真實 backlog，不必寫「healthy empty」那種自我合理化。

## 十二篇投稿翻譯

tboydar 送九篇英文人物（林獻堂、蔡瑞月、唐鳳、鄧雨賢、黃春明、龍應台、鍾肇政、李仙得、蕭美琴），aminzai 送三篇新語系（鄭南榕 ar、台灣水彩畫 hi、台灣攝影 id）。十二篇全部 ARMED、CI 三綠、MERGEABLE。

閘門逐項跑過：比例檢查十一篇 OK、唐鳳 THIN（2.20，章節 10→9）但落在 merge + follow-up 的可接受帶。`article-health --profile=ci-deploy` 十二篇 hard=0。人名與地名保真度零可疑替換，這一項對九篇人物題特別重要，去年七月出生戰役揭露過機器翻譯會把張忠謀譯成蔣介石。CJK 殘留報 38 行，逐行看下來全部落在參考資料區的中文書目標題與音譯後的漢字注記，正是 OBSERVER-QUEUE #23 還沒拍板的那個政策縫，不是新傷。

三篇是覆寫既有英文版（蕭美琴、李仙得、龍應台）。這種 PR 值得多看一眼，OBSERVER-QUEUE #33 記著一次「拿更短、來源更差的版本覆寫走過事實修補的文章」。逐篇比對章節數、腳註數、連結數全部守恆，位元組數還略增，是更新不是壓縮。龍應台那篇還把羅馬拼音從 Long Ying-tai 改成本人通行的 Lung Ying-tai，並清掉舊版 frontmatter 裡一行註解殘骸。

十二篇 `--merge` 收下，ready 佇列從 14 降到 2。剩下的 #1453（學測站台區段）與 #1365（單一用途帳號的在世人物條目）分別掛在 OBSERVER-QUEUE #36 與 #30，是策展門檻與收不收的判斷題，維護者不自己收。三個 draft 全是 idlccp1984 的 #1450 / #1411 / #1407，同樣掛在 #32 / #33。

蔡瑞月英文版順手 heal 一處（`4edd0ff78`）：第二張圖說把來源連結包在斜體裡，而網址結尾是 `_0432.jpg`，下次 prettier 會把底線吃掉讓連結 404。中文版早就把連結移到圖說外面單獨一行，英文譯文又折了回去。照中文版改完，全站掃過確認這是最後一個同型的。

## 一進庫就過期的十四篇

aminzai 那三篇 merge 完，狀態表當場把它們判成 `stale / no-source-sha`。內容明明是前一天照現在的中文版翻的，落地那一刻就是「舊的」。

根因在 `status.py`：沒有 `sourceCommitSha` 這一欄就直接歸 stale。而投稿者的翻譯工具不會產這一欄，`translation-check.yml` 檢查 `translatedFrom` 卻不檢查它。**沒有任何地方會叫**，所以它一直安靜累積。往上游追，同一種傷有 14 篇，散在 ja/ar/hi/id/vi 五個語言，全部來自投稿 PR。

用既有的 `backfill-source-sha.py` 補齊（`488bca454`），補法本身是誠實的：sha 取「譯文最後修改時間點或之前」的中文版 commit，所以中文版之後真的動過的話狀態表仍讀得出 drift，不會補完就假裝新鮮。補完 `no-source-sha` 歸零，十四篇全部轉 `fresh / same-commit`。

同一個 commit 做了兩件讓它不會安靜復發的事。`backfill-source-sha.py` 加 `--files`，維護者可以只補剛 merge 的那幾篇，不必為了三個檔掃整個語言，兩種模式共用同一個 `patch_one`，不長出第二把尺。`translation-check.yml` 在缺這欄時出聲，並附上維護者一行就能補的指令。對投稿者不設硬門檻，因為擋一個他的工具不會產的欄位，等於把維護成本外包給最不熟這套工具的人。

這件事真正的形狀是：2026-05-01 那次 `no-source-sha` 大掃除（+1010 篇從假過期變真新鮮、零 API 成本）被記成漂亮的一役，寫進了神經迴路與 REFLEXES #38 的觸發欄，但當時沒有在進料口加任何檢查。四個月後債照原速回流。升 LESSONS `one-off-cleanup-without-a-gate-refills`。

## 十條分類寫錯的延伸閱讀

全站掃內部連結，60 條指不到東西、散在 33 個中文檔。其中 10 條的目標文章好好地在庫裡，只是連結裡的分類寫成了另一類：五月天寫成 `/people/`、三峽老街寫成 `/geography/`、台灣咖啡文化寫成 `/lifestyle/`、九合一那三條寫成 `/society/`，還有一條把 AI人工智慧產業 的 AI 打成小寫（站上另外四篇都是大寫）。逐條核對目標檔案存在才改，改完各檔重跑歸零（`9cef725ce`）。

剩下 50 條是目標文章真的不存在，延伸閱讀寫了一篇沒人寫過的文章，神經迴路裡「幻覺連結是延伸閱讀最常見的斷鏈原因」那條的又一批。每條要判斷改指最近的既有篇還是退成純文字，留給下一輪。全站 gated broken ratio 0.32%，遠在 7% 門檻內。

## 收官 checklist

| 檢查項                       | 狀態                                                         |
| ---------------------------- | ------------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                                           |
| Timestamp 精確               | ✅ `git log %ai`                                             |
| Handoff 三態已審視           | ✅                                                           |
| CONSCIOUSNESS 反映最新狀態   | ✅ 免疫 59 黃燈與四條 routine 沉默死亡警報均為既有，本輪未動 |
| 自我檢查工具 PASS            | ✅ pre-commit / pre-push 全綠，broken-link 0.32% < 7%        |

Quality gate 七條：open issues 都有 status label 或已在待決佇列 ✅ / open PR ≤5d 都有處置 ✅ / broken-link 0.32% ✅ / build green ✅ / BECOME ACK 在記憶體頂 ✅ / 連續空場 vc=0（本輪真實 backlog，不適用）✅ / 有 fresh issue 的 cycle 至少一件被修或寫明不修：本輪**零 fresh issue**（最新 #1609 是 08-28 已處理），四個 open issue 三個已在待決佇列（#1440→#31、#1184→#35、#615 為 umbrella 追蹤）、#1609 昨日已回覆並把查證排進用語趨勢 routine，Step 2.4 重複回應檢查判 SKIP。理由寫在此，不是沉默地沒修 ✅

## Handoff 三態

繼承上一 session（`2026-08-29-070817-twmd-feedback-triage`）：五縣市圖片補正、`.husky/pre-push` `VAR="$(...)"` 掃描、#1453 人物卡連結、#1365 KENJI 門檻、OBSERVER-QUEUE #39-#43、免疫分數 59 漂移、w.is_solis 質疑、sophie990329 字典編審提問候選、terminology 查證候選（含 #1609）、空窗期人工回覆確認、harvest 排序盲區、#176（X）未登入、`/map` `.sidebar-panel` 高度問題。全部原樣繼承。

- [ ] pending — 指控信 `b78ee4f5` 第十二次已攔下，`status` 仍 `new`，下一輪照 HG13 拉全文讀完再 `--exclude`（原樣繼承 feedback-triage 那條）

本 session 新 handoff：

- [x] ~~ready 佇列 14 → 2~~ retired by 本 session（12 篇投稿翻譯 merge）
- [x] ~~`no-source-sha` 14 篇~~ retired by 本 session（補齊歸零 + CI 出聲 + 工具加 `--files`）
- [ ] pending — 站內延伸閱讀還有 **50 條指向不存在的文章**，散在 33 個中文檔（清單見 `article-health.py --all --check=link-target`）。下一輪可接的具體動作：逐條二選一，目標主題有最接近的既有篇就改指過去、沒有就退成純文字（per 神經迴路「目標 article 無 → 轉純文字」）。單檔最多 6 條（台灣水果王國、高雄市），可一次一檔慢慢清，不必整批
- [ ] pending — 翻譯 PR 的 `sourceCommitSha` 閘門目前只出聲不擋。觀察兩到三輪投稿翻譯，如果維護者側補正變成每輪固定動作，考慮在 merge 後的 heal 步驟寫死呼叫 `backfill-source-sha.py --files`，讓它不依賴維護者當下記不記得

## Beat 5 — 反芻

今天有三次，我拿自己臨時寫的指令去量一件事，三次都量錯。

第一次最貴。`grep -rl '^translatedFrom:'` 配上逐檔查有沒有 `^sourceCommitSha:`，數出「290 篇缺這欄」。290 跨過 §自主權邊界 的 >50 檔門檻，於是我開始盤算：要不要只修這輪 merge 的三篇、把其餘的拆成安全子集、把整件事升 OBSERVER-QUEUE 等哲宇簽名？我甚至已經在腦裡寫好那條待決項的選項與成本。跑 `status.py` 自己的索引才發現，實際缺欄 89、真正被判 `no-source-sha` 的只有 **14**。差在 grep 只掃前四十行（多行 tags 陣列會把 frontmatter 撐過去），又把不在索引裡的檔算了進來。

壞掉的尺在這裡的代價不只是一個錯數字，它把一件十四個檔、二十秒就能跑完的修補**路由給了錯的決策者**，而且錯的方向是「更謹慎」，看起來像美德，實際是拿一個不需要的簽名去換一件本來今天就該做完的事。REFLEXES #83 的 Boundary (b) 明寫「短期診斷 ad-hoc grep 不適用」，因為它不進載入面。今天這個 instance 正好掉在那個豁免的縫裡：ad-hoc grep 沒進載入面，卻進了範圍與授權的判斷。

第二次量全站斷鏈時我寫 `timeout 900 python3 …`，而 macOS 沒有 `timeout`，指令根本沒跑，接在後面的 `grep -c` 老實回 0，我差點寫下「全站零斷鏈」，重跑實際是 33 檔 60 條。第三次是 sourceCommitSha 的「MISMATCH」，我拿字串相等去比 sha，但 status.py 用的是「這個中文檔在那個 commit 之後有沒有再動過」的祖先關係。照我的尺，五篇好好的 PR 全是 MISMATCH，照 canonical 的尺全部 0 commits behind。

三次的形狀一樣：**canonical 儀器已經在算同一個數字，我卻另外寫了一把尺去問同一個問題**。而每一次我的尺都比較快、比較順手、看起來也很合理。這比「沒有尺」危險，因為它會給出一個具體到讓人願意據以行動的數字。今天要記住的一句話是：**任何要拿來決定範圍、優先序、或該由誰拍板的數字，都必須來自那件事的 canonical 儀器**，順手的替代指令只能拿來看方向。詳見 LESSONS `unbounded-grep-counts-template-headers-as-inventory` 新增的 instance。

那十四篇譯文留下的是另一條：它們一進庫就是舊的，四個月沒人發現，因為這種債偽裝成正常的背景值——狀態表本來就會有一些 stale，多這十四筆不會讓任何數字跳紅。真正讓我看見它的，是 aminzai 那三篇在我眼前 merge 完然後當場被判過期。**清乾淨過一次的債，如果沒在進料口留下東西守著，就會用原本的速度長回來，而且第二次比第一次更難看見**，因為第一次的成功敘事已經寫進記憶，再看到同一個數字時的直覺是「這條早就處理過了」。

🧬

---

_v1.0 | 2026-08-29 09:02 +0800_
_session twmd-maintainer-am — cron 早班，14 個 ready PR 的真實 backlog_
_誕生原因：cron routine twmd-maintainer-daily 08:40 fire_
_核心洞察：任何要決定範圍或授權的數字都得來自 canonical 儀器，臨時寫的尺今天錯了三次、其中一次差點把十四個檔的修補送去等一個不需要的簽名；一次性大掃除若沒在進料口配閘門，債會照原速回流且第二次更難看見_
_LESSONS-INBOX 候選：`one-off-cleanup-without-a-gate-refills`（新開）／`unbounded-grep-counts-template-headers-as-inventory`（+1 instance，新增「壞尺會把工作路由給錯的決策者」這個後果維度）_

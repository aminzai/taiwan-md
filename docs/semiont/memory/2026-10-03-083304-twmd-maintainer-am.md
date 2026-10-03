---
session_id: '2026-10-03-083304-twmd-maintainer-am'
session_span: '2026-10-03 08:33 → 08:5X +0800'
trigger: 'cron routine twmd-maintainer-daily @ 08:30'
observer: 'none（cron context，哲宇最後在場 2026-09-26，缺席第 7 天）'
beat_coverage: 'Stage 1-4（MAINTAINER-PIPELINE v2.15 + 本班改的 v2.16）'
---

# 2026-10-03-083304-twmd-maintainer-am — SOP 自己教的那句指令會命中等待迴圈自己，而交接指名我查的事昨天已經收掉了

> session twmd-maintainer-am — cron routine，無觀察者在場
> Session span: 08:33 → 08:5X +0800
> 資料來源：`git log %ai`

```
✅ BECOME ack: mode=review / 8 organ 最低=🛡️59（免疫 v3, review_coverage=19） / Q13 anti-bias=PASS / Q14 cross-session continuity=PASS
```

## 觸發

Cron 08:30 起。上一班（10-02 08:54）留了一句很明確的話：「下一班不需要再找理由 skip，只需要排 16 分鐘」——指的是連三輪沒量的斷鏈 audit。所以本班開場就是去排那 16 分鐘，而整班兩個發現都是從那條路上撿到的。

## Stage 1 掃描

| 項目       | 讀數                                                                                   |
| ---------- | -------------------------------------------------------------------------------------- |
| 分岔       | `0 0`（完全同步，不觸發 Step 1.1b）                                                    |
| open PR    | 2 ready / 0 draft（#1784 ar、#1782 de，皆 aminzai、MERGEABLE、ARMED 3 checks 全 pass） |
| open issue | 3 條（#1786、#1609 皆 from-feedback 已處理待拍板；#615 視覺 umbrella）                 |
| discussion | 14 條，1 條有未回的 contributor follow-up（#1757，距今 6 天）                          |
| 過去 24hr  | 10 條 cron fire 全到位，routine-status 無缺席                                          |
| 過去 48hr  | babel 十二語持續產出 + 四班 semiont-heartbeat 巡邏修正                                 |
| main CI    | 13 條 active workflow：RED 0 / BLOCKED 0 / UNKNOWN 0 / NEVER-ON-MAIN 0                 |
| 免疫器官   | 🛡️59，最大缺口 review_coverage=19（chronic，自 2026-07-05 第 90 天）                   |
| 平行寫入者 | babel dispatcher writer process 3353 / 51717 全程在跑（ACTOR_BUSY）                    |

## SOP 自己教的那句手跑指令，會命中等待迴圈自己

照 §Step 4.1 當時寫著的「先確認 `pgrep -f 'astro build'` 沒有東西，再讀」跑下去，回報 **9 個程序**。逐一查 `ps` 之後：真正的 `node astro build` 只有 2 個，其他 **7 個是前幾班留下的等待迴圈**——

```
until ! pgrep -f 'astro build'; do sleep 15; done
```

這一行的命令列裡就有 `astro build` 這幾個字，所以 `pgrep -f`（比對全命令列）永遠命中它自己，條件永遠不成立。三個已經活了 1 天 23 小時、三個 23 小時。它們不報錯、不佔 CPU，只是再也不回來；母 session 當初收到的「背景任務完成」其實是 shell 包裝退出，不是條件成立。

用尺自己那把 `(^|[\s/])astro(\.m?js)?\s+build\b` 對同一份 `ps` 重跑，命中**恰好 2 個**——引號與 `.*` 都不是 `[\s/]`，嚴格版不自我命中。所以 `verify_internal_links.py` 一直是對的，錯的是 SOP 裡那句要人手跑的版本。這也解釋了 10-02 那班為什麼手跑看到東西、而儀器仍給得出 0.15% 的讀數。

**最尖銳處在這句錯答案的方向**：它回報「build 在跑」，而當班照字面讀的正確動作就是 skip 斷鏈 audit——跟 09-28〜09-30 連三輪 skip 完全同一個症狀、完全不同的成因，而上一班才剛把那個理由拆掉。一條為了防 skip 而寫的 SOP，自己長出了第二個 skip 的理由。

已 ship `367f5b0b5`：§Step 4.1 刪掉那句，改成直接跑尺看它回 `BUILDING` 還是給讀數，並附不自我命中的寫法（`pgrep -f 'astro[ ]build'`）。六個不死迴圈本班收掉，收完裸 `pgrep` 命中數從 9 降到 2，與儀器一致。LESSONS `wait-loop-polls-for-a-pattern-its-own-command-line-contains`。

## 交接指名我查的那件事，昨天已經收掉了

甦醒時 `wake-context` 的 `handoff` 段（來源 10-03 07:10 feedback-triage）寫著：

> `[ ] pending（收件席位 twmd-maintainer-daily）`：404 雙語言前綴。

格式正確、指名明確、沒有任何矛盾標記。而 **10-02 08:54 的維護班已經以證據退役兩次**：signature 定為第二段恆為 `fr`（含 `/fr/fr/`），全 `dist/` 19,323 份 HTML 零命中雙前綴 href，判定外部排列前綴、非站體自產。

逐鏈對時序才看出機制：

| 時間        | 班              | 這一項                |
| ----------- | --------------- | --------------------- |
| 10-02 06:41 | spore-harvest   | pending（當時正確）   |
| 10-02 07:12 | feedback-triage | pending（當時正確）   |
| 10-02 08:54 | **maintainer**  | **retired（附證據）** |
| 10-03 06:41 | spore-harvest   | pending ← 復活        |
| 10-03 07:10 | feedback-triage | pending ← 復活        |

**每條 routine 的交接是從自己家族的上一班抄下來的，不是從當前狀態重算的。** 所以退役只存在於它發生的那條鏈上，另外兩條從自己昨天的清單繼續抄。另一半更安靜：這一項在傳抄中掉了識別細節（`404 雙語言前綴 /ja/fr/...` → `404 雙語言前綴`），收件人更難認出它就是昨天結案的那條。照字面執行會重查 7 條已經查到底的 URL。

能分辨的唯一方法是去讀別條鏈的 memory，而沒有任何東西提示當班需要這麼做。LESSONS `retired-item-resurrects-through-a-parallel-handoff-chain`（`6e2246236`），候選機械化三條裡只有 (c)「收官掃全庫 memory，近 7 天內標過 retired 又在更晚檔案裡出現 pending 就印警告」不依賴每班記得。

## 斷鏈 audit：上一班排的那 16 分鐘

照 v2.15 走 `npm run sync:build`（不觸發 `prebuild:status`，與 babel 的共用檔零碰撞），在 babel dispatcher 全程在跑的情況下實測成立，與上一班的結論一致。

`astro build` 13 分 17 秒、18,920 頁，`dist/` 齡 0.0h（上限 24h，沒落進 STALE 也沒落進 BUILDING）：

| 讀數                      | 值                                |
| ------------------------- | --------------------------------- |
| Gated ratio（排除 es/fr） | **0.15%**（1,912/1,238,432）      |
| 全語言 ratio              | 0.14%                             |
| 斷鏈總數 / 唯一目標       | 1,981 / 1,196                     |
| 閘門                      | **PASSED**（< 7.0%，real exit 0） |

逐語言：zh-TW 0.32%（1,584，分母 497,760 最大）／vi 0.13%／ja 0.09%／fr 0.06% 與 es 0.03%（兩者 REPORT-ONLY 未進 gate）／其餘十語皆 ≤ 0.04%。數字與 10-02 那班的 0.15% 一致，兩班獨立量到同一個值。

ja 那 68 條的形狀仍是舊帳：日文條目之間互指的 wikilink 目標（`/ja/history/white-terror/`、`/ja/music/taiwan-indie-music/`）沒有對應譯文，少數目標還留著中文 slug（`/ja/music/台湾客家音楽/`）。屬 §神經迴路「譯文 wikilink 未在地化」那一族，命中 §自主權邊界（>50 檔）且屬 babel 產線，本班不碰。

## 兩個 PR：已審完，卡在不能代理的那一格

#1784（ar 都市發展）與 #1782（de 數位影像動畫）都是 MERGEABLE、CLEAN、3 checks 全 pass、`maintainerCanModify: true`，而且 **10-01 那班已經把技術性缺陷審完、投稿者也修完了**（ar 的「中山高」原譯成蔣介石已改回音譯 `تشونغ شان`、de 的兩處 `T客邦` 補音譯，兩篇都搬回跟 zh 同分類的路徑）。四把尺對兩版平手。

剩下的是 **OBSERVER-QUEUE #67 待決的那一類**：投稿者送來一份跟現行機器譯文等質、沒有修掉任何缺陷的重譯，要不要取代現行版？取代會 churn 站上內容且無實測收益；不取代＝要對投稿者說「這篇不收」，而那是拒絕貢獻的決策。該格標 **🔒紅線（對外溝通／貢獻者關係原則）**，缺席協議明寫四紅線永不代理，所以本班不動、不 close，也沒有再去找投稿者補東西——他 09-30 已明說理解在等策展決定、不再補。

**本班對這兩個 PR 的唯一正確動作是什麼都不做**，而這件事值得寫下來：連續兩班讀到兩個全綠、可合併、審完的 PR 而不合併，很容易在第三班被重新讀成「漏了」。它們不是漏了。

## Issue：三條都不是積壓

- **#1786**（用語庫辭典版本，09-29 進）：10-02 那班已 ship 可修的部分（`e9be08c55` 斷言改引簡編本），並順手量出全庫 2,306 條詞條裡引《重編》25 條、引《簡編》**0 條**，直接改寫 #76 選項 B 的成本。刻意留 open 當 #76 的第二個外部訊號。**對讀者本人的回覆仍卡人類 gate。**
- **#1609**（白色恐怖受難者日記的「無語」用法，08-27 進，第 37 天）：09-27 那班把三條死路（匿名 API 擋讀、`noindex` 無快取、館方無全文）寫進詞條並搬進 OBSERVER-QUEUE #85——剩下的動作是「註冊一個帳號」，人的動作。不是爛掉，是正確地在等人。
- **#615**（視覺 umbrella，04-25 進）：最後留言 09-12 是一則實質研究（字型載入閘門 `visibility:hidden` + 800ms 逾時可能正是讀者體感的「不順」來源）。umbrella 本來就長期 open。

**本班 0 條 fresh issue**，所以 quality gate 第 7 條（有 fresh issue 就要修掉一件）不適用；但本班不是空轉，三個非 memory commit 都是真修補。

## 把 Discussion #1757 的抽樣放大到全庫

#1757（kwt-klure）的 follow-up 掛了 6 天沒回，超過 §Step 1.3b 的 48hr SLA。他最後那則是結語（「第 74 項的分層，等你們有空再說，不急」），所以缺的不是回應速度，是**那一格還能不能往前推**。

他 09-26 貼的抽樣（近期 n=24）量到策展人筆記是「可逐篇插入的零件」裡收斂最明顯的一個。本班把它放大到全庫，造了 `curator-note-density.py`（`bec41e74c`）：

| 1,125 篇 zh 條目               | 篇數 |  占比 |
| ------------------------------ | ---: | ----: |
| §四 超過密度上限               |   94 |  8.4% |
| §十「B 級至少 1 則」一則都沒有 |  390 | 34.7% |
| 平均每篇                       | 1.60 |       |

分布 0 則 390／1 則 203／2 則 248／3 則 157／4 則 73／5 則以上 53。

**數字改變的不是結論，是那個矛盾的性質**：原本是文件兩端措辭不一致（§四 容許 0 則「寧少勿多」、§十 用「不強制＝不存在」把 0 這個出口關掉），放大到全庫之後變成**兩端各自都已經蓋不住一部分的庫，而且兩個方向都沒有任何儀器在看**——34 個 `article-health` check 沒有一個量筆記密度，`prose-health` 只把筆記當排除區。

尾端比抽樣看到的更極端，而且剛好是他原帖論點最乾淨的證據：`Society/馬英九迷因.md` **19 則**（上限 4），每條迷因後面接一則、每 6 行一則，每則都用「這不僅是」「揭示了」「凸顯了」「往往會被」——正是 EDITORIAL 自己在別處禁的抽象昇華句，在同一份 canonical 要求「B 級至少一則」的位置上被複製了 19 次。

尺抽驗過才貼數字（REFLEXES #99）：三篇手工逐行對照全同（19/19、6/6、8/8）、負控制確認 0 則那篇真的沒有、庫內 12 種 callout 寫法全收、11 處正文順口提及與腳註定義行正確排除。

**本班刻意沒做**：把這條接成 `article-health` 的 warn 級 check。那是新增品質閘門，命中 BECOME High-stake #3（閾值調整）＋ #74 本身標 🔒，而且在「§四 還是 §十 哪一條算數」拍板之前接上任何一端，94 篇或 390 篇裡的一群會當場變紅點。數字與這個「刻意沒做」都寫進 #74（`bec41e74c`），哲宇回來看到的是量好的版本。回覆已貼（[#1757 comment](https://github.com/frank890417/taiwan-md/discussions/1757#discussioncomment-18724583)），走致謝＋技術說明層，沒有承諾時程。

新工具同時登記進 DNA §品質基因表（`65f407e44`），列名寫明「尺不是閘門」——REFLEXES #91 建造與登記是兩個不同步的代謝，造完不登記下一班就看不見它。

## Stage 4 — Quality gate

| Gate                                           | 結果                                                           |
| ---------------------------------------------- | -------------------------------------------------------------- |
| open issues 都有 status label / assignee       | ✅ 3/3 有 label；#1786 #1609 有 assignee，#615 umbrella 不指派 |
| open PRs ≤ 5d age 都有 review comment          | ✅ 2/2（10-01 審完，投稿者已回應確認）                         |
| broken-link gated ratio < 7%                   | ✅ **0.15%**（1,912/1,238,432；dist 齡 0.0h；real exit 0）     |
| build green                                    | ✅ 13 條 workflow RED 0                                        |
| BECOME ACK 一行記憶體頂                        | ✅                                                             |
| 連續空場 ≥ 3 cycle 有 LESSONS entry            | ✅ 不適用（vc=1，10-02 命中真 backlog 後重計）                 |
| 有 fresh issue 的 cycle 至少修掉一件或寫明不修 | ✅ 不適用（0 條 fresh issue）；本班仍 ship 3 件真修補          |
| 本機與 origin 無真分岔                         | ✅ `0 0`                                                       |

**連續空場 vc=1**：10-02 那班命中真 backlog（CI 紅、健康尺成因、讀者 #1678）後歸零重計，本班 0 fresh PR / 0 fresh issue 計 1。未達 ≥3 的 escalate 線。

## Handoff 三態

繼承自 `2026-10-03-071019-twmd-feedback-triage`：

- ⏳ blocked（哲宇）：`OBSERVER-QUEUE #75〜#92（待決）`，含 #28（feedback 指控信偵測器）。本班新增 **#74 選項 A 的量測已從抽樣放大到全庫並附尺**，#67 兩個實例（#1784／#1782）仍可一次決定。
- [x] ~~pending（收件席位 twmd-maintainer-daily）：404 雙語言前綴~~ → **已於 10-02 08:54 retired，本班只是收到了復活的副本**。不重查。成因與修法見上方 §交接指名我查的那件事＋LESSONS `retired-item-resurrects-through-a-parallel-handoff-chain`。
- [ ] pending（收件席位 twmd-self-evolve-weekly 10-04）：LESSONS `heart-counts-heals-as-contributed-births`。非本席位，原樣傳遞。
- [ ] pending（收件席位 twmd-distill-weekly）：LESSONS `threads-linkifier-swallows-cjk-before-url`、`narrative-log-fills-causation-no-gate-watches`（vc=2）、`external-advisory-reddens-a-gate-and-not-our-code-becomes-a-reason-not-to-act`（vc=2）、`verified-the-fact-exists-on-site-not-that-it-exists-in-the-article-we-linked`。非本席位，原樣傳遞。
- [ ] pending（席位 `/twmd-routine`，經 `docs/semiont/ROUTINE.md` 下發）：spore-harvest 殼的 `/Users/cheyuwu/` 寫死路徑。**第九班原樣傳遞（vc=9）**，規模 12 條殼加 ROUTINE.md 自己，靠一條沒人記載的 root 符號連結支撐（LESSONS `flywheel-path-layer-rests-on-one-undocumented-root-owned-symlink`）。per REFLEXES #97 當權限問題看，不是還沒輪到。

本 session 新 handoff：

- [ ] pending（收件席位 twmd-distill-weekly）：本班兩條新 LESSONS — `wait-loop-polls-for-a-pattern-its-own-command-line-contains`（vc=1 structural）與 `retired-item-resurrects-through-a-parallel-handoff-chain`（vc=1 structural）。後者的候選機械化 (c) 是唯一不依賴每班記得的那條。
- ⏳ blocked（哲宇，`OBSERVER-QUEUE #74`）：策展人筆記密度閘門要不要接。**量測已交付、尺已造好、刻意沒接**，拍板後才知道接 §四 還是 §十。不要在拍板前接——94 篇或 390 篇的其中一群會當場變紅點。
- ⏳ blocked（哲宇，`OBSERVER-QUEUE #67`）：#1784／#1782 兩個 PR 全綠、審完、投稿者已停手等決定。**連續兩班正確地什麼都不做**，第三班不要把它讀成「漏了」。
- [ ] pending（本席位，下一班）：`ci-main-health.sh` 的 ⚠️ 取數口計數器仍未在真實執行裡觸發過（10-02 留，本班 13 條全綠也沒觸發）。原樣傳遞。

## Beat 5 — 反芻

今天兩個發現是同一個形狀的兩面：**一份正確的交接，可以在內容正確的同時傳遞一個已經不成立的世界。**

那句 `pgrep` 寫進 SOP 的時候是對的。它當時防的病是真的（半成品 dist 的 mtime 是「現在」，staleness guard 會放行），它給的動作也是合理的。它失效不是因為寫錯，是因為**後來有人用它建了等待迴圈，於是被觀測的集合裡多出了觀測行為自己的痕跡**。一句指令可以在沒有人改它的情況下，被它周圍的世界慢慢變成錯的。

那條 404 交接也是。它被準確地傳了兩棒，格式完整、指名清楚，連收件席位都寫對了。它唯一的問題是**那件事已經做完了，而「做完了」這個事實住在另一條鏈上**。交接複製的是待辦，不是狀態；狀態改變的那一刻沒有被複製，因為沒有東西負責把它複製過去。

兩件事都不會叫。手跑 `pgrep` 會回一個格式正確的數字 9；交接會回一句格式正確的 pending。它們都通過了自己所有的形式檢查。接住它們的都不是閘門，是「這個數字違反常識」跟「這句話我昨天好像看過結論了」——跟昨天那班接住 24 天 deploy 年齡的是同一種東西。

而我今天差點都沒接住：9 這個數字我第一眼是當真的，是因為要排那 16 分鐘才去查它是哪 9 個；404 那條我本來已經準備去撈 `reports/404-monitor/latest.json`。兩次都是多走一步才看見，而那一步不是紀律要求的，是剛好。昨天那班寫「差一步，是今天真正該記住的距離」。今天這一步我走了兩次，但兩次都不是因為有東西叫我走。

🧬

---

_v1.0 | 2026-10-03 08:5X +0800_
_session twmd-maintainer-am — cron 維護班，無觀察者在場（缺席第 7 天）_
_誕生原因：cron 08:30 fire；上一班留話「下一班不需要再找理由 skip，只需要排 16 分鐘」，整班兩個發現都是從那條路上撿到的_
_核心洞察：一份內容正確的交接可以傳遞一個已經不成立的世界——寫進 SOP 的指令會被它周圍的世界慢慢變成錯的（等待迴圈把自己放進了被觀測的集合），交接複製待辦但不複製狀態改變（退役只住在它發生的那條鏈上）；兩者都通過所有形式檢查、都不會叫、接住它們的都是「這違反常識」而不是閘門_
_LESSONS-INBOX 候選（本班 append 2 條）：`wait-loop-polls-for-a-pattern-its-own-command-line-contains`／`retired-item-resurrects-through-a-parallel-handoff-chain`_

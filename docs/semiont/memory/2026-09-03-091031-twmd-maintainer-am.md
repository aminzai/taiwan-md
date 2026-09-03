---
session_id: '2026-09-03-091031-twmd-maintainer-am'
session_span: '2026-09-03 08:30 — 09:15'
trigger: 'cron routine twmd-maintainer-daily'
observer: 'none（無人值守排程）'
beat_coverage: 'Beat 3 執行 + Beat 4 收官'
mode: 'Full（High-stake #1 觸發：ready PR 5 ≥ 5，由 Review 強制升 Full）'
---

✅ BECOME ack: mode=review→**Full**（High-stake #1 強制升級）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，非記憶值）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

# twmd-maintainer-am @ 2026-09-03 — main 紅了四天沒人看到，替它背黑鍋的是一支不相關的投稿

## Stage 1: SCAN

| 項目                     | 值                                                                           |
| ------------------------ | ---------------------------------------------------------------------------- |
| open PR（ready / draft） | **5 ready / 3 draft**（vc 與 High-stake 只計 ready）                         |
| open issue               | 6（#1661 / #1639 / #1609 / #1440 / #1184 / #615）                            |
| past 24hr commits        | 10                                                                           |
| past 48hr commits        | 48                                                                           |
| build status             | 🟢 Deploy green ／ 🔴 **Python tests 紅了四天**（8/30 起，本輪才發現）       |
| i18n smoke               | 🟢 green                                                                     |
| 免疫器官分數             | 🛡️ **59**（yellow 漂移中，自 2026-07-05，owner = `twmd-self-evolve-weekly`） |
| broken-link gated ratio  | **0.32%** < 7.0% 門檻                                                        |
| CI armed 狀態            | 8 個 open PR 全部 ARMED（UNARMED 0 / NO-WORKFLOW 0）                         |
| Discussions              | 11，無 48hr 內未回應的 contributor 貼文                                      |

5 ready 命中 BECOME §Step 0 High-stake #1，Review 強制升 Full。

**Step 1.5 這一步今天自己被改掉了**。它原本寫死問兩條 workflow 的名字（Deploy / i18n Smoke），我照著跑完得到「build green」——然後才因為別的線索去問了一次「main 上每一條 workflow 的最後一次結果」，`Python tests` 才掉出來。詳見 Stage 3-A。

## Stage 2: TRIAGE

5 個 ready 裡，**4 個早就在 OBSERVER-QUEUE 上等哲宇拍板**（#1642→#45、#1630→#33、#1453→#36、#1365→#30），3 個 draft 也全在（#1450→#33、#1407/#1411→#32）。真正是新 backlog 的只有 1 個：#1662。

這種形狀有它自己的陷阱：一眼看去「八個 PR 都在等人類」，很容易整輪收成空場。但 §1c 說的是 default 是修好；而且掛在佇列上的那些，**技術狀態會變，佇列上的描述不會自己跟著變**——今天兩個投稿者都動了，兩筆佇列描述都停在兩週前。

紅旗 check：#1662 動的是 `scripts/tools/lang-sync/*.py`，紅旗 1/2/3（robots / 外部 JS / workflow）零命中，diff 逐行讀過是機械式加 `encoding="utf-8"`，無行為改動。

## Stage 3: ACT

### A. 追上游：main 的 `Python tests` 紅了四天，而它咬的是別人

`#1662` 的 pytest 是紅的。查下去不是投稿者的問題：

```
tests/article_health/test_language_contributor_surfaces.py
  ::test_translation_workflow_paths_match_enabled_registry
AssertionError: Extra items in the left set: 'de'
```

`main` 上最後一次 `Python tests` 是 **2026-08-30 failure**，四天沒有再跑過（它掛 `paths` filter，紅完就沒有觸發源）。#1662 動了 `scripts/**/*.py`，於是繼承了那個紅。

**根因是 8/30 那輪自己造的**：那天把 `knowledge/de/**` 補進 `translation-check.yml`（讓十一天沒被任何檢查認得的德文譯文進得了閘門，就是 `scaffold-window-has-no-qa` 的修補），而同一份 canonical 裡有一條測試斷言「workflow paths 必須等於註冊表裡 `enabled` 的語言」，`de` 是 scaffold。**修好一道閘門的動作把另一道判成違規**；更精確地說，同一輪 cycle 造的 `check-language-registry-sync.sh` 判準是「有沒有內容進來」，測試判準是 `enabled` 旗標——同一天、同一個作者、兩把方向相反的尺。

修法選擇了讓測試改吃正確的那把尺（有內容就要被守），而不是把 `de` 從 workflow paths 拿掉——後者會把 8/30 的修補退回去。

| 動作                                                                                                   | commit      |
| ------------------------------------------------------------------------------------------------------ | ----------- |
| 測試改問「有沒有內容進來」（`_qa_wired_translation_codes`），與 `check-language-registry-sync.sh` 同源 | `73a0b9441` |
| Step 1.5 CI 健檢從點名兩條改成 group-by 問 main 上每一條 workflow                                      | 同上        |

**falsification**：拿掉 `ar` 的 workflow path，測試會叫；放回去，336 passed。

### B. PR #1662 merge + 把同一類別補完（Closes #1661）

`73a0b9441` 上 main 之後 update-branch，pytest 轉綠，`gh pr merge --merge` → **MERGED** `44b2b876a`。

然後追同一個類別的剩下部分。用 ast 掃（不是 grep——**grep 逐行看，把換行寫的呼叫算成缺編碼，多報了 19 處**，38 vs 57），整個 `lang-sync/` 還有 38 處 `read_text` / `write_text` 沒指定編碼，分佈在 12 個檔。其中最說明問題的一對：`babel-dispatch` 寫 worklist 時明講 UTF-8，`diff-patch-prepare` 讀它時沒有——同一對讀寫各說各話，而那份 worklist 裝的正是中文檔名。

補完 + 造閘門 `tests/test_lang_sync_text_encoding.py`（守整個目錄、不列豁免清單，因為要維護的清單自己就會漂）。驗證：`py_compile` 12 檔、9 支 CLI `--help`、`babel-health` 真的讀一次狀態檔輸出正常、拿掉一處編碼確認閘門會叫。commit `4a1a6bbdb`。

### C. Issue #1639：昨天寫「量不到」，今天發現這台機器上一直有第二把尺

昨天那輪把三項驗收寫成「需要一支真的手機或真實桌面瀏覽器」，理由紮實、實測過（內嵌瀏覽器不實作 `0fr → 1fr`、頁面無法程式化捲動）。**診斷全對，結論錯了**——這個 repo 的 `devDependencies` 裡就有 `playwright`，`viz-shot.mjs` 每次跑視覺驗證都在用它。

用真的 Chromium 跑，三項全部有結論：

| 驗收項                     | 結果                                                                    |
| -------------------------- | ----------------------------------------------------------------------- |
| 子選單展開後的捲動與裁切   | ✅ 沒問題（抽屜 589 / max 740 不需捲動，22 條連結最後一條完整在畫面內） |
| Tab 焦點順序               | ✅ 沒問題（skip-link 第一，之後是表頭控制項）                           |
| 錨點跳轉是否被固定表頭遮住 | ❌ **真的 bug，三個斷點全中**                                           |

錨點那項再往上追一層才是重點：「表頭有多高」這個數字站上有**三份硬編碼副本，彼此不同也都跟真值不同**——`global.css` 的 92（註解算式「navbar 72px + 20px buffer」）、`FootnoteCard` 的 78、`Header` 自己那行 `92 + banner`。實測 375/768/1280 分別是 110/96/108。

改成量一次發佈一份：Header 用 `ResizeObserver` 量自己的 `bottom`（量 bottom 而非 height，hero 頁被語言橫幅推下去一起涵蓋）→ `--header-h`，另外兩處都吃它，fallback 取實測最大值 110。commit `c6d5374d8`。

**驗證**（真 Chromium 對本機 build）：

| 斷點     | --header-h | scroll-padding-top | `#sub-城市生活` 淨空   |
| -------- | ---------- | ------------------ | ---------------------- |
| 375×812  | 110px      | 126px              | +16px ✅（修前 −18px） |
| 768×1024 | 96px       | 112px              | +16px ✅               |
| 1280×900 | 108px      | 124px              | +16px ✅               |

被遮住的錨點：0。FootnoteCard 那段換成讀變數後回 108（真值），拿掉變數回 110（fallback）。腳註卡的 hover 互動在 headless 下正式站與本機 build **行為完全相同**（都不開卡），所以它不構成回歸訊號——但也代表那條互動路徑我今天沒有正面走過，只驗了被我改動的那個運算式本身。

issue close（`c6d5374d8`），留話請讀者在真手機上若仍看得到就附截圖重開。

### D. 兩筆佇列描述過期，補上今天的實測

兩個投稿者在維護者上次看之後都動了，而佇列上的描述沒有跟著動——拍板的人會看到兩週前的狀態。

- **#1630（→ OQ #33）**：投稿者 8/31 依審查逐條修了。[^10] 自我引用換成 PR Newswire 一手稿（連帶把來源撐不起的「2017 關閉」拿掉，是對的降階）、`date` 還原 2026-04-06；對位句型 **22 → 15**（EDITORIAL 對 4,891 字上限 3，方向對但沒到）。**技術面已不是阻塞點**，剩純粹的先例問題。
- **#1453（→ OQ #36）**：死碼問題已修（`src/pages/exams.astro` 補進來）。剩兩個小落差：模板註解寫 `/exams/gsat/` 但實際建出 `/exams/`；六語 copy 只有中文讀得到（`getLangFromUrl` 靠網址前綴，而 elections-2026 是十二語各一支 page）。兩條都是十分鐘的事，不是阻塞點。

投稿者 9/2 在 #1453 直接問「這個何時上架」。回覆據實說明技術狀態、明講範圍決定在人類手上、**不給時程**（§外向留言分層：許諾未來屬 reserve）。

### E. 對外留言（全部 = 致謝＋技術說明，AI 自主層）

| 對象        | 內容                                                     |
| ----------- | -------------------------------------------------------- |
| PR #1662    | 致謝 + 說明他的紅不是他造成的 + 三件後續                 |
| Issue #1661 | commit hash + 改動摘要（PR 自動 close，補說明留言）      |
| PR #1630    | 逐條回報實測，指出剩下的 15 處與判準，重申卡點是先例問題 |
| PR #1453    | 回答「何時上架」：技術狀態 + 由誰決定 + 不給時程         |
| Issue #1639 | 三項驗收結論 + 修法 + 三斷點驗證表 + close               |

## Stage 4: WRAP

### Quality gate（7 條）

| Gate                                   | 結果                                                         |
| -------------------------------------- | ------------------------------------------------------------ |
| open issues 都有 status label          | ✅ 4 則剩餘全有 label                                        |
| open PRs ≤ 5d age 都有 review comment  | ✅ 本輪 3 則新留言，其餘皆已有                               |
| broken-link ratio < 7%                 | ✅ 0.32%                                                     |
| build green                            | ✅ Deploy green；**Python tests 由紅轉綠**（本輪修）         |
| BECOME ACK 一行記憶體頂                | ✅                                                           |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | ✅ N/A — 本輪非空場（1 PR merged、2 issue closed）           |
| 有 fresh issue 的 cycle 至少一件被修掉 | ✅ #1661 修掉並補完整個類別、#1639 修掉錨點 bug，各附 commit |

### 本輪 commit

| commit      | 內容                                                 |
| ----------- | ---------------------------------------------------- |
| `73a0b9441` | 測試改吃「有內容就要被守」+ Step 1.5 健檢改 group-by |
| `44b2b876a` | merge PR #1662（stantheman0128，Windows UTF-8）      |
| `4a1a6bbdb` | lang-sync 補完 38 處編碼 + 新閘門                    |
| `c6d5374d8` | `--header-h` 量一次發佈一份，修錨點被遮              |

### LESSONS-INBOX append（3 條）

- `declared-unmeasurable-without-inventorying-the-tools`（含**撤回昨天的修補候選 (b)**——列內嵌瀏覽器缺口表是在正確地解決錯的問題）
- `named-healthcheck-cannot-see-what-it-does-not-name`
- `one-measurement-three-hardcoded-copies`

### 評估後決定不做的（寫明理由，per §1c）

- **UI 字串層的用語閘門**（OQ #31 / #1440 附帶的結構問題）：`check-ui-language.mjs` 守的是「這串字是不是該語言」，不是「這個詞是不是支語」。補後者是可做的，但 OQ #31 已寫明「22 處『數據』其中一部分確實指數值，屬正確用法，是逐處判斷不是全域取代」——判準本身就是那個被 reserve 的決定的一部分。先造閘門等於替哲宇先決定了判準。列為候選，不做。

## Handoff 三態

繼承（原樣延續）：

- [ ] 指控信第十七次已攔下，OBSERVER-QUEUE #28 兩件仍待哲宇拍板
- [ ] `footnote-description-is-an-unaudited-claim` 候選修法、#1609 待調閱《郭淑姿日記》兩冊
- ⏳ 免疫分數 59 漂移黃燈由 `twmd-self-evolve-weekly` 追蹤
- [ ] LESSONS `clip-that-causes-the-bug-also-silences-the-detector` / `ratio-gate-cannot-surface-a-small-structured-family` 候選修法
- [ ] 1,080 篇有腳註卻沒有參考段落，`format-structure` 目前只 warn，>50 檔命中 §自主權邊界未動手
- [x] ~~retired by 本 session — #1639 剩三項需要真實裝置驗證：改用 playwright 後三項全部有結論，兩項確認沒問題、一項修掉並驗過，issue 已 close~~
- ⏳ blocked — #1641/#1643 若 OBSERVER-QUEUE #33 收 #1630 會同時變 stale
- [ ] pending（給 self-evolve）— D+14 milestone 缺口：建議評估是否替 D+14/D+30 milestone 建立顯性追蹤

本 session 新增：

- ⏳ blocked — **OBSERVER-QUEUE #33 / #36 兩筆的技術面阻塞點今天都消失了**，剩下純粹是先例與產品範圍的決定。#1630 對位句型仍 15 處（門檻 3），但那是可 heal 的，不是等拍板的理由。解除條件：哲宇對「投稿者能不能整篇覆寫既有條目」與「要不要開 `/exams/` 區段」給出方向
- [ ] pending — **main 紅燈沒有不依賴人的出口**。今天靠 maintainer 每日掃描才發現四天前的紅。候選：red-on-main 進 `dashboard-alerts.json`，讓它出現在每一條 routine 的 groundtruth 段（寫進 LESSONS `named-healthcheck-cannot-see-what-it-does-not-name` 修補候選）
- [ ] pending（給 self-evolve / distill）— ANATOMY §資源地圖 缺「驗證引擎」那一格。今天的教訓是宣告「量不到」之前要先盤點工具庫；地圖列了 SSOT 與共用元件，沒列可用的驗證引擎
- [ ] pending — `--header-h` 現在是「一份真值 + 兩個消費者」，但沒有東西阻止第四份硬編碼副本長出來

---

_2026-09-03 twmd-maintainer-am · Full mode（High-stake #1）· 1 PR merged / 2 issues closed / 4 commits_

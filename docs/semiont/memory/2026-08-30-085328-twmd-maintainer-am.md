---
title: '2026-08-30-085328-twmd-maintainer-am'
description: '德文譯文進來十一天沒有任何檢查認得它——三處接線補齊 + 對賬閘門；三篇投稿翻譯 merge；剩餘佇列全數是哲宇保留項'
session_id: '2026-08-30-085328-twmd-maintainer-am'
session_span: '2026-08-30 08:30 → 09:05'
trigger: 'routine twmd-maintainer-daily（am 08:30）'
observer: '無（cron，無人在場）'
beat_coverage: 'MAINTAINER Stage 1-4'
type: 'session-log'
---

✅ BECOME ack: mode=review→**強制升 full**（High-stake #1「PR triage ≥ 5」命中：ready PR 5 個）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，非記憶值。🫀90 🧬95 🦴90 🫁85 🧫100 👁️90 🌐83）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

> wake-context 221,242 bytes 分頁讀到 `wake:END` sentinel，未用 head/tail 截斷（§1.3）。

---

## Stage 1 — SCAN

| 面向             | 讀數                                                                                      |
| ---------------- | ----------------------------------------------------------------------------------------- |
| open PR          | **8**（ready 5 / draft 3）——先分 ready/draft 才報數，per v2.8                             |
| open issue       | 4（#1609 / #1440 / #1184 / #615），**fresh 0**，四則最後發言都是維護者且無新 follow-up    |
| past 24hr commit | 25（全 routine：news-lens / weekly-report / distill / self-evolve / embeddings / …）      |
| past 48hr commit | 60（含 8/29 maintainer 收的 12 篇投稿翻譯）                                               |
| build status     | 🟢 Deploy to GitHub Pages 最近 5 run 3 success / 2 cancelled，無 failure                  |
| i18n smoke       | 🟢 最近 3 run 全 success（8/23，paths filter 未觸發故未再跑）                             |
| PR CI armed      | 8/8 **ARMED**，UNARMED 0 / NO-WORKFLOW 0（`pr-ci-armed.sh`）                              |
| 免疫器官         | 59（黃燈，自 2026-07-05 漂移中）＋兩條 routine 沉默死亡黃燈（routine-audit / supporters） |

---

## Stage 2 — TRIAGE

**Ready 5 個裡只有 3 個可動**，另外 2 個與全部 3 個 draft 都已在 OBSERVER-QUEUE 掛號等哲宇：

| PR                | 處置                | 依據                                           |
| ----------------- | ------------------- | ---------------------------------------------- |
| #1629 hi          | ✅ merge            | 紅旗 0 / CI 3 條全綠 / CLEAN                   |
| #1628 id          | ✅ merge            | 同上                                           |
| #1627 de          | ✅ merge            | 同上（但只有 2 條 check——見下方根因）          |
| #1453             | 🔒 reserve          | OBSERVER-QUEUE #36（開 `/exams/` 站台區段）    |
| #1365             | 🔒 reserve          | OBSERVER-QUEUE #30（單一用途新帳號的在世人物） |
| #1450/#1411/#1407 | 🔒 reserve（draft） | OBSERVER-QUEUE #32 / #33                       |

**紅旗複查**：三篇的 `author: 'Taiwan.md'` 乍看命中紅旗 #7，查證後不是。中文母稿本來就是這個值（全庫 5,012 檔如此），譯文忠實繼承。紅旗 #7 打的是投稿者把**自己的新內容**冒名成 Semiont 所寫，不是翻譯繼承。

**Step 2.4 重複回應檢查**：四則 issue 最新留言都是維護者且無新 follow-up → 全部 SKIP，不補罐頭回覆。#1609 兩天前才給過完整回覆（commit `8680e1666` 加誠信標註 + 查證排進用語趨勢 routine + 向回報者要日記出處），現在再開口只是雜訊。

---

## Stage 3 — ACT：追上游

### 症狀

PR #1627（德文）只有 2 條 CI check，同批 hi/id 有 3 條。投稿者 aminzai 自己在 PR 留言裡列了他跑 repo QA 工具的結果。

### 查證（他的 claim 是線索不是事實，REFLEXES #16）

五條 claim **兩條成立、三條不成立**：

- ✅ `translation-check.yml` 的 `paths` 沒有 `knowledge/de/**` → 德文 PR 從不觸發 `check-translation`
- ✅ `script-presence-check.py` 沒有德文 profile
- ❌ 他說 `cjk-residue-check` / `person-fidelity-check` / `geo-fidelity-check` 三支「對 de path 報錯」——實測三支帶 `--lang de --files` 全部正常通過。他八成用位置參數呼叫，把 argparse 的 usage error 讀成「工具拒絕 de」

自己查出他沒提到的第三條：`cjk-residue-check.py` 的 `TARGET_LANGS` 也沒有 de。

### 根因

`de` 2026-08-19 以 `enabled: false` scaffold 進語言註冊表，內容持續進 `knowledge/de/`（8/30 已 77 篇），但所有以語言碼為 key 的 QA 接線都沒跟上。**十一天、77 篇、零檢查。**

最刺的一層：`check-language-registry-sync.sh` 早在 2026-07-26 就為了**完全一樣的病**長出來（VIZ_STRINGS 漏六語 → 43,045 個中文 aria-label），註解把病理寫得清清楚楚——但它只守了當初咬過人的那一份 mirror。

第二刺：三處接線裡只有 `script-presence-check.py` 會**假裝有跑**。遇到不支援的語言 `continue`，最後印 `✅ 0 檔語言真偽檢查通過` 並 exit 0。它的兄弟 `cjk-residue-check.py` 同樣情況 exit 1 叫出來。同一個工具鏈、相反的失敗語義。

### 修（commit `f7221cfcf`，已上 origin/main）

1. `translation-check.yml` paths 補 `knowledge/de/**`
2. `script-presence-check.py` 補德文 profile（`[äöüßÄÖÜ]`）＋**缺 profile 改 exit 2**，不再借用「沒事」的符號表示「我不知道」
3. `cjk-residue-check.py` `TARGET_LANGS` 補 de
4. `check-language-registry-sync.sh` 加對賬：**只要 `knowledge/<lang>/` 有內容，三處接線就都必須認得它**。判準刻意用「有沒有內容」而非註冊表的 `enabled` 旗標。內容比上線決定早幾個月到，那段空窗正是它需要被守的時候

**dogfood**：三個缺口各自單獨還原一次，閘門三次都紅、訊息各自指對地方。全補齊則綠。第一版用「對每個語言跑一次 CLI」實作，實測 11 秒（把 9,000 檔語料掃 12 遍），對 pre-commit 太貴，貴到最後會被人拿掉。改成 import 讀 `SUPPORTED_LANGS` 後 0.07 秒。

### 補檢查後回頭掃德文語料（77 篇）

| 檢查            | 結果                                                                                   |
| --------------- | -------------------------------------------------------------------------------------- |
| ratio           | ✅ 77/77 PASS                                                                          |
| person-fidelity | ✅ 無可疑人物替換                                                                      |
| geo-fidelity    | ✅ 無可疑地理遷移                                                                      |
| script-presence | ✅ 77 檔無「宣稱已譯實為英文」                                                         |
| cjk-residue     | ⚠️ 68 行，多數是既有誤判家族（`archi 藝廚`、`一例一休`、來源標題），**但撈出一件真的** |

那件真的：中文母稿三篇（`許淑淨` / `謝淑薇` / `鍾理和`）留著未解決的 `<!-- TODO: 天機星 -->` 註解，已隨翻譯散進 **10 語共 16 檔**。

**評估後決定不修，理由**（per §1c「決定不做要寫明」）：那四條 TODO 各自是一個待查證的事實問題（趙常玲完整英文姓名、禁賽解除日期、謝淑薇搭檔姓名、鍾理和引語出處），直接刪掉等於銷毀真實的未解問題，查證則是 REWRITE / FACTCHECK 的工作，明確不在 maintainer heal 範圍（§1c 邊界第二條）。它們是 HTML 註解，讀者看不到，無對外傷害。留 handoff。

---

## Stage 4 — WRAP

### Quality gate（7 條）

| Gate                                        | 結果                                                          |
| ------------------------------------------- | ------------------------------------------------------------- |
| open issues 都有 status label/assignee      | ✅ 4/4 有 label，且全部已在 OBSERVER-QUEUE 掛號               |
| open PRs ≤ 5d age 都有 review comment       | ✅ 三篇當日 merge。其餘 5 篇 age > 5d 且都已 reserve 並留言   |
| broken-link ratio < THRESHOLD_PERCENT（7%） | ⏭️ 本 cycle 未跑（無 knowledge/ 內容改動，改的是 CI/工具層）  |
| build green                                 | ✅ Deploy 最近 run success。pre-push 全站掃描通過才 push      |
| BECOME ACK 一行記憶體頂                     | ✅ 本檔第一行                                                 |
| 連續空場 ≥ 3 cycle 有 LESSONS entry         | ✅ N/A。本 cycle 有 5 個 fresh ready PR，vc 歸零              |
| 有 fresh issue 的 cycle 至少一件被修掉      | ✅ N/A（fresh issue = 0），但仍 ship 了一件真修（見 Stage 3） |

### LESSONS-INBOX

append `scaffold-window-has-no-qa`（vc=1）：以 scaffold 身分進註冊表的實體，內容比上線決定早幾個月到，而 QA 接線在那段空窗裡對它不存在。判「要不要守」該看有沒有內容，不看 `enabled` 旗標。

### 一句話

**十一天沒有任何一道我自己的儀器發現德文沒被檢查，發現它的是一個順手跑了我的工具的投稿者，而他五條說法裡有三條是錯的。**

---

## Handoff 三態

繼承 `2026-08-30-070831-twmd-feedback-triage` 的整份清單（W35 news-lens 候選、公投制度 P0、sitemap 缺口、50 條斷鏈延伸閱讀、五縣市補圖、OBSERVER-QUEUE 44 項、兩盞沉默死亡黃燈待核、roadmap 9 項、X `#176` 草稿），逐條見該檔 §Handoff，本 session 未碰任一項。

本 session 新 handoff：

- [ ] **10 語 16 檔的 `<!-- TODO: 天機星 -->` 殘留**。根在中文母稿三篇（`People/許淑淨.md` L41/L71、`People/謝淑薇.md` L49、`People/鍾理和.md` L53）。下一步可執行動作：把四條 TODO 當 FACTCHECK Quick Mode 工單跑（趙常玲完整英文姓名 / 2019 禁賽三年解除日期 / 謝淑薇三場賽事搭檔姓名 / 鍾理和「我要把生命寫完，再死」原始出處），查完刪註解，母稿改動後譯文隨 babel 更新。
- [ ] **`article-health` 沒有 placeholder 殘留 plugin**。紅旗 #10（`TODO: 補` / `（此位置放…）` / `[FILL ME]`）目前只有人工 PR 審查在守，已在庫的殘留無人偵測。下一步：加一支 plugin，先用全庫 dogfood 校準誤判（`TODO` 出現在程式碼區塊 / 引用原文裡是合法的）。
- [ ] **`script-presence-check --lang all` 報 53 檔「宣稱已譯實為英文」**（es 10 / fr 7 / ja 19 / ko 17，de 0）。這是 2026-07-19 那批 68 檔的未清餘額（68→53），非本次新增。重譯判斷密集，非 maintainer 範圍。
- ⏳ blocked — **PR #1627 之後德文譯文才會真的觸發 `check-translation`**。paths filter 是新 PR 事件才生效，已 merge 的 77 篇不會回頭補跑。本 session 已在本機手動補跑全套並記錄結果（見 Stage 3），視為已驗。

### 需哲宇決策（本 cycle 未新增，僅提醒既有掛號因本輪而更急）

- OBSERVER-QUEUE **#29 要不要開德文**：本輪把德文的 QA 接線補齊了，`knowledge/de/` 77 篇也實測乾淨。技術面現在沒有東西擋著上線，剩下的純粹是「要不要開第 13 個語言」這個決定本身。註冊表仍維持 `enabled: false`，本 session 未動。

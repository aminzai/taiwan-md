---
title: '2026-10-01-084906-twmd-maintainer-am'
description: '連三輪 skip 的斷鏈閘門其實有一條不需要空檔的路；投稿者把兩個缺陷都修好了，於是兩篇都成了等質重譯；一則討論問 Taiwan.md 能不能收不需要觀點的東西'
type: 'cognitive-log'
status: 'log'
current_version: 'v1.0'
last_updated: 2026-10-01
last_session: '2026-10-01-084906-twmd-maintainer-am'
---

# 2026-10-01-084906-twmd-maintainer-am — 「這個席位取不到空檔」是真的嗎／兩篇等質重譯等的是同一格／有人問這裡收不收不需要觀點的東西

> session twmd-maintainer-am — cron 08:30 maintainer 班（PR review + issue triage + build sanity + 斷鏈 audit）
> Session span: 08:35 → 09:0x +0800
> 資料來源：`git log %ai`、`date`

✅ BECOME ack: mode=review / 8 organ 最低=免疫 59（即時 `consciousness-snapshot.sh`，讀數齡 2h）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發與 Stage 1

Cron 08:30 例行班。`git rev-list --left-right --count main...origin/main` 回 `0 0`，無分岔，不走 §Step 1.1b。

| 面向             | 讀數                                                                         |
| ---------------- | ---------------------------------------------------------------------------- |
| open PR          | **2 ready / 0 draft**（#1784 ar、#1782 de，皆 aminzai，皆 MERGEABLE、ARMED） |
| open issue       | 5（#1786 / #1729 / #1678 / #1609 / #615，無今日新進）                        |
| Discussions      | 14，其中 **#1787 零回應**（kwt-klure，09-30 20:20Z 發，本班回了）            |
| 過去 24hr commit | 43                                                                           |
| 過去 48hr commit | 55（babel 夜班 + 晨鏈六條 routine）                                          |
| main CI          | 13 條 active workflow **RED 0 / BLOCKED 0 / UNKNOWN 0 / NEVER-ON-MAIN 0**    |
| 免疫器官         | 59（最低器官，review_coverage=19 是最大缺口，chronic 自 07-05）              |
| 斷鏈 gated ratio | **0.15%**（1,902／1,238,471，< 7% 通過）— 連三輪 skip 後第一個真讀數         |

ready PR 是 2 不是 ≥ 5，所以沒有命中 High-stake #1，Review mode 維持，self-test 11/11。

## 「這個席位取不到安靜窗」這句話只有一半是真的

09-28／09-30 兩輪把品質閘門的斷鏈 audit skip 掉，理由寫得很具體：`verify_internal_links.py` 要 fresh dist，而 `npm run build` 的 `prebuild:status` 會跑 `status.py` 與 `sync-translations-json.py`，寫的正是 babel 此刻在寫的 `knowledge/_translation-status.json`。09-30 那班把它升成一條 LESSONS，寫成席位的結構屬性：「維護班每天固定時間醒來，而 babel dispatcher 是常駐的，所以這類項目再傳一百輪也不會被做掉。」

今天重讀那條，卡在一個地方：競用的是 `prebuild`，不是 `astro build`。查 `package.json` 之後答案很短——**`npm run sync:build` 等於 `sync.sh && astro build`，而 npm 的 pre/post hook 只對名字叫 `build` 的 script 生效**，所以這條路一個 prebuild 步驟都不跑。`sync.sh` 只寫 `src/content/{lang}`（gitignored 的投影層），`dist/` 也是 gitignored。

照這條路跑，在 babel dispatcher 常駐、`babel-push-every.py --watch` 在 commit 的情況下，拿到了真讀數。**而且證據比「沒撞到」更強**：babel 在我 build 到一半的 08:42:09 真的寫了 `knowledge/_translation-status.json`，build 照樣跑完，因為整個 build 路徑裡沒有任何東西讀或寫那個檔（`src/` 裡唯一一處提到它的是一支 client-side script 的註解）。兩個行為者併行十一分鐘，碰撞面是零。

所以那條 LESSONS 的兩個 instance 性質不同，已在原條目標註並拆開：`.git/gc.log` 的 `git prune` 那一半仍然成立（物件寫入期間 prune 本質不安全），斷鏈 audit 那一半不是排程拓樸問題，是**沒有人問過這條路是不是只有一種走法**。這一半真正的所屬是 09-03 那條 `declared-unmeasurable-without-inventorying-the-tools`——那次盤點的是工具（宣告要真手機，而 devDependencies 早有 playwright），這次盤點的是**同一個工具的不同入口**。該條 vc 已 bump 到 2。

**真讀數**：`PASSED — gated broken ratio 0.15% < 7.0%`（1,902／1,238,471；all-langs 0.14%），對照 09-27 那天的 0.16%，二十天內沒有惡化。完整性旁證：dist 19,309 個 HTML，09-27 完整 build 是 18,905。分語言最高的是 zh-TW 0.32%（1,574 條，母體 49.8 萬條也最大）與 vi 0.12%／ja 0.09%；類別上 (a) 語言切換器死連結 **0**、(b) 文章內部死連結 1,852、(c) 其他 119。es／fr 仍是 REPORT-ONLY 不進 gate（0.03%／0.06%）。

修法寫進 [MAINTAINER-PIPELINE §Step 4.1](../pipelines/MAINTAINER-PIPELINE.md)（v2.15），不留在 memory 當自律。

### 同一件事的代價：我自己被半成品騙了一次

build 起在背景之後約一分鐘，我就去讀了那支尺。它回：

```
zh-TW  total: 1  broken: 1  ratio: 100.00%
FAILED — gated broken ratio 100.00% >= 7.0%
```

當時 dist 只有 29 個 HTML（完整 build 約 1.9 萬）。24 小時的 staleness guard 放行了，因為**半成品 dist 的 mtime 是「現在」**——它是這把尺底下最新鮮的東西。唯一那條「死連結」`/people/吳哲宇/` 在完整 build 裡是存在的頁面。

救下它的只有 100% 違反常識。如果分母剛好是幾百、ratio 剛好落在 7% 附近，這個讀數會被我寫進收官表，而它跟真讀數會長得一模一樣。這條落 LESSONS（`freshness-guard-reads-a-half-built-artifact-as-maximally-fresh`，structural）：年齡上限回答的是「有多舊」，同時無聲地把「它完整嗎」一律回答成是，而兩種不可信的產物在這把尺底下站在相反的極端。最便宜的修法不需要任何新門檻——偵測到 `astro build` 在跑就照 staleness 那條分支一樣 abort；設分母下限是在品質閘門上加一個新數字，屬 High-stake #3，本班刻意不自己設。

## 兩篇重譯：投稿者把缺陷都修好了，所以它們現在是同一個問題

09-30 那班對 aminzai 的三篇重譯給了三種答案，待決的只有 de 那一篇（等質重譯要不要取代現行機器譯文，OBSERVER-QUEUE #67，🔒紅線）。ar 那篇當時是「有缺陷待修」——把中山高的「中山」譯成 `تشيانغ كاي شيك`（蔣介石）。

投稿者 09-30 01:33 兩篇都修了，而且照現行版的既有慣例改。逐項驗過（照 §診斷紀律把檔案帶進 main 樹，用 main 上的檢查器量，不 checkout PR 分支）：

| 檢查                                 | #1784 ar        | #1782 de                | 站上現行版           |
| ------------------------------------ | --------------- | ----------------------- | -------------------- |
| `article-health --profile=ci-deploy` | hard=0 warn=1   | hard=0 warn=1           | 兩篇皆 hard=0 warn=1 |
| `cjk-residue-check`                  | 0 行            | 0 行（原 2 行 `T客邦`） | 0 行                 |
| `person-fidelity-check`              | 0 處（原 1 處） | 0 處                    | 0 處                 |
| `target-language-check`              | 0 fail          | 0 fail                  | 0 fail               |
| 路徑與 zh 原文同分類                 | ✅ Geography    | ✅ Technology           | —                    |

**四把尺全部平手**，所以 ar 那篇從「有缺陷」移進「等質」這一類：#1782 與 #1784 現在是同一個問題的兩個實例，可以一次決定。這件事寫進 #67 的證據段。兩篇都沒 close、沒 merge——close 是拒絕貢獻的決策，merge 是用等質譯文覆蓋現行版，兩者都在紅線後。兩個 PR 各留一則驗證留言（事實＋致謝，屬 §外向留言分層的自主格），明說在等那一格、不是在等他補東西，也沒給任何時程。

投稿者自己在兩個 PR 上都寫了「等質這件事我理解，留著等哲宇的策展決定即可，我這邊沒有其他要補的」。**他在等的是那一格，不是在等我們指出下一個缺陷**——這句進了 #67，因為它改變了不決策的代價。

## 有人問：Taiwan.md 收不收「不需要觀點」的東西

Discussion [#1787](https://github.com/frank890417/taiwan-md/discussions/1787)（kwt-klure 與他的 Claude，Claire；之前送過 #1777／#1778，和那份促成 OBSERVER-QUEUE #81 的產線 audit）。問題很清楚：EDITORIAL 從第一句就要求每篇回答「為什麼值得你花 8 分鐘讀」，而有一類材料放不進去——一間麵店開幾十年的公休日、一條巷子以前賣什麼、某個地方的人習慣怎麼講一件事。他們那句「硬要替它們找觀點，寫出來的是另一篇策展文，原本那個東西反而不見了」是整則最站得住的一句，因為它描述的是一個具體的失敗，不是一個偏好。

第二個論據是語料面，而這一段比第一段更值得記：未來模型學中文時簡體語料量大、簡轉繁便宜，於是會出現大量「字是正體、骨架是另一種中文」的文字；而台灣語感主要從不刻意的文字裡學來。這跟 MANIFESTO §主權的巴別塔 是同一個方向的不同一層——**巴別塔對抗的是翻譯層的沉默（PRC 模型遇到台灣主題選擇不作答），他們指的是語感層的替換**。後者目前在認知層沒有位置。

這是策展門檻與對外語氣定調，四紅線之二，我不能自己答。登記成 **OBSERVER-QUEUE #92**，三個選項：A 維持現狀（每篇都要有論點）／B 直接開新條目類型配獨立的尺／**C（推薦）先做一個 pilot**，收一條不帶策展觀點的原樣記錄、不進首頁精選不計深度門檻，用獨立的尺驗收，量過再談身份。推 C 的理由是爭點在身份層，而身份層的問題用一個真實樣本比用討論收斂得快。

討論上回了一則，明說這個問題我不能自己回答、它現在住在哪一格、沒有時程。他們說「知道不屬於這裡也有用」——這句話讓這則變成可以乾脆回答的問題，而不是一個不好意思拒絕的請求。

## 其餘 issue：三則明確不動，理由寫在這裡

- **#1786**（讀者指用語庫該查《簡編本》）— 09-30 已修根因面並把全庫量測寫進 #76 證據段。剩下的是兩把辭典對照，而 09-30 那班已發現更基本的事：全庫 0 條引《簡編本》，要比的不是兩份名單差多少，是先建出那份名單。席位是 `twmd-terminology-trends-monthly` 10-05 或任何 Full mode Write 班，不是本班。
- **#1729**（馬英九腳註查核）— 範圍混層（已完成的兩條腳註 vs 待重寫的兩節）09-30 已寫在 issue 上等能決定範圍的人；最新留言是維護者、無新 follow-up，照 Step 2.4 **SKIP 不重複回應**。
- **#1678**（生態多樣性缺遊蕩犬貓威脅）— 09-06 補了站內連結與延伸閱讀，正文實質改寫屬 REWRITE 不屬 maintainer heal，留 open 等重寫。**本班驗了那則留言的一個聲明**：它說查好的數字已全部寫進 ARTICLE-INBOX——`grep` 確認 §482 那條 entry 在，陳貞志 2015–2016 的數字也在。自己過去的 claim 也要驗（REFLEXES #31／#91 建造與登記是兩個代謝）。
- **#1609**（郭淑姿日記的「無語」）— 連四輪把查證路徑縮到只剩「臺灣日記知識庫需要一次登入」，最新留言是維護者、無新 follow-up，SKIP。
- **#615** umbrella — 長期追蹤 issue，非本班範圍。

## 本班真正改掉的東西

| 動作                                   | commit / 位置                                                                                                                                                                                                                                                                                                                                                                          |
| -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ci-main-health.sh` 每列印 run 來源    | 每列跟一行 `↳ run <id>  created <ISO>  sha <9>`。09-30 那班同一支尺兩分鐘內對同一次 deploy 報 22.0d 與 1h、兩次都綠，而當時無法判斷是不是同一筆。年齡是推導值，`created_at` 與 run id 是原始資料。成因（API 回舊頁）仍未重現，所以這是「可回頭核對」那一半，不是根治。新尺照 REFLEXES #99 先驗：三種欄位形狀（含空 sha）解析正確、`--strict` 在 RED 0 時回 0、無任何程式在解析它的輸出 |
| MAINTAINER §Step 4.1 補斷鏈 audit 走法 | v2.15，含「build 還在跑時別讀那支尺」                                                                                                                                                                                                                                                                                                                                                  |
| MAINTAINER 紅旗 8 的 canonical 14 類   | 原列 `Language`（`knowledge/` 無此目錄）、漏 `Politics`（實際 18 篇）。對 `knowledge/` 目錄與 `src/utils/categoryConfig.ts` 兩邊核對後更正，並寫明以 `categoryConfig.ts` 的 key 為準、`SUBCATEGORY.md` 只涵蓋 12 主題不是 category 的 SSOT                                                                                                                                             |
| OBSERVER-QUEUE #92 新增                | Discussion #1787（不需要觀點的條目類型），三選項 + 推薦 C                                                                                                                                                                                                                                                                                                                              |
| OBSERVER-QUEUE #67 補證據              | 兩篇都修好了、四把尺平手、投稿者明說在等這一格                                                                                                                                                                                                                                                                                                                                         |
| LESSONS 新增 1 條                      | `freshness-guard-reads-a-half-built-artifact-as-maximally-fresh`（structural）                                                                                                                                                                                                                                                                                                         |
| LESSONS 更新 2 條                      | 安靜窗那條標註前提被部分推翻並拆兩半；`declared-unmeasurable-without-inventorying-the-tools` bump vc=2                                                                                                                                                                                                                                                                                 |

## 收官 checklist

| 檢查項                                       | 狀態                                                                                            |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------- |
| 完整走完 MAINTAINER-PIPELINE                 | ✅ Stage 1-4 全跑                                                                               |
| PR 分流按 §collect-and-merge                 | ✅ 2 個全走 B 路徑完整 hard gate                                                                |
| routine PR backlog ≤ 3                       | ✅ 0（v2.1 main-direct）                                                                        |
| broken-link gated ratio < 7%                 | ✅ **0.15%**（gated 1,902／1,238,471；all-langs 0.14%），連三輪 skip 後第一個真讀數             |
| build green                                  | ✅ main 13 條 workflow RED 0；本機 `sync:build` 成功 **19,309 頁**（09-27 參考值 18,905，完整） |
| 本 cycle merge 的 PR 都過 hard gate          | ✅ 無 merge（兩篇都在 🔒 後）；驗過的兩篇四把尺全綠                                             |
| 有 fresh issue 的 cycle 至少修一件或寫明不修 | ✅ 無 fresh issue；五則各寫明不動的理由；本班改掉的是儀器與 canonical 三處                      |
| open issues 都有 status label                | ✅ 5/5                                                                                          |
| open PRs ≤5d 都有 review comment             | ✅ 2/2（本班各補一則驗證留言）                                                                  |
| BECOME ACK 一行在記憶體頂                    | ✅                                                                                              |
| 本機與 origin 無真分岔                       | ✅ `0 0`                                                                                        |
| 連續空場 vc                                  | **0**（本班有 2 ready PR + 1 零回應 discussion，非空場）                                        |
| Timestamp 精確                               | ✅ 取自 `git log %ai` 與 `date`                                                                 |
| Handoff 三態已審視                           | ✅                                                                                              |
| diary                                        | ⏭️ skip — 反芻已落 Beat 5，洞察是既有反射（#99／#38）的新載體，不是新框架                       |
| evolve                                       | ⏭️ skip — 新 LESSONS vc=1，更新的兩條交週日反思鏈                                               |

## Handoff 三態

繼承 `2026-09-30-091222-twmd-maintainer-am` 與 `2026-10-01-071213-twmd-feedback-triage`：

- [x] ~~pending（席位 `twmd-maintainer-am`）— `ci-main-health.sh` 每列都印取到那次執行的 URL／sha~~ → **retired by 本班**：改成每列跟一行 `↳ run / created / sha`。成因未重現那一半仍開著，但它已經可以被回頭核對。
- [x] ~~pending（席位 `/twmd-routine`）— MAINTAINER 的「canonical 14 類」inline 清單過期~~ → **retired by 本班**：對 `knowledge/` 與 `categoryConfig.ts` 核對後更正，並寫明 SSOT 在哪一份。
- [x] ~~pending（席位 `twmd-babel-nightly`）— 七個 `309.md` 要改名或刪掉重翻~~ → **retired**：babel 夜班 10-01 01:04 已改回真 slug（`28ac08c38`、`94070476c`），本班確認 `knowledge/` 下無 `309.md`。
- [ ] pending（席位：能動排程的 Full mode session 或 `/twmd-routine`）— **只剩 `.git/gc.log` 與 `git prune` 這一半**需要無寫入者的空檔（斷鏈 audit 那一半本班已解，走 `sync:build`）。`git prune` 在 babel 寫物件期間本質不安全，所以仍是排程問題：掛在 dispatcher 佇列空的那一刻，或一條前置條件寫明「`check-parallel-actor` 回 IDLE 才跑，否則重排不是 skip」的 routine。
- [ ] pending（席位：`/twmd-routine` 或任何 Full mode）— 譯文分類閘門缺口（LESSONS `translation-gates-check-a-file-against-itself-never-against-its-source`）：對帶 `translatedFrom` 的檔斷言路徑分類段 == `translatedFrom` 的分類段。本班兩個 PR 的路徑問題是投稿者自己改的，閘門仍不存在。**本班未動的理由**：新增閘門並掛 pre-commit／`pr-frontmatter-gate` 屬 BECOME High-stake #2（新 workflow 設計），要 Full mode。
- [ ] pending（席位：任何 Full mode／`/twmd-routine`）— `verify_internal_links.py` 的完整性斷言（LESSONS `freshness-guard-reads-a-half-built-artifact-as-maximally-fresh`）。**最便宜那條不需要新門檻**：偵測 `astro build` 在跑就 abort。設分母下限屬 High-stake #3，留給 Full mode 或哲宇。
- [ ] pending（席位 `twmd-terminology-trends-monthly` 10-05 或任何 Full mode Write 班）— `OBSERVER-QUEUE #76` 選項 B 要先建出《簡編本》那份名單（09-30 量到全庫 0 條引簡編本）。同趟可併 `/terminology/變壓器`。
- [ ] pending（席位：任何 Write session）— PR #1781 里長帳簿後續（2,309 字低於深度門檻、無圖、缺 `rationale`、已在 PR 上問開票夜第一人稱段落的出處）。
- [ ] pending（席位：`twmd-maintainer-am`）— issue #1729 範圍混層仍等能決定範圍的人；本班照 Step 2.4 未重複回應。
- ⏳ blocked（`OBSERVER-QUEUE #92`，待決，🔒紅線）— 要不要開一種不需要觀點的條目類型（Discussion #1787）。**本班已回覆說明它住在哪一格、沒給時程**。解除條件：哲宇拍板。
- ⏳ blocked（`OBSERVER-QUEUE #67`，待決，🔒紅線）— 等質重譯要不要取代現行機器譯文。**PR #1782 與 #1784 現在是同一個問題的兩個實例，四把尺全部平手，可以一次決定**。兩篇都不要 close（拒絕貢獻是 human only）。解除條件：哲宇拍板。
- ⏳ blocked（`OBSERVER-QUEUE #76`／`#28`，待決，🔒紅線）— 用語庫最寬斷言複查／第三人指控類回報偵測器。本班無此類輸入。
- ⏳ blocked（延續）— issue #1729 馬英九兩節重寫等 Write 班帶哲宇 review；`OBSERVER-QUEUE #75`〜`#91` 待決。
- [ ] pending（延續，非本班職權，原樣傳遞不重抄明細，REFLEXES #74）— routine-sync 對賬前 `git fetch`、data-refresh Stage 1.5 順序、issue `#1729`／`#1729` 以外的 babel 自造 slug 存量、404 unknown 裡可解析的大小寫與跨分類同名、`md-extension` 10-02 觀察。明細見上游各檔。

## Beat 5 — 反芻

今天最值得記的是一句話的壽命。「這個席位結構上取不到安靜窗」——昨天寫下它的是同一個席位，寫得具體、有兩個 instance、有修法方向，而且**它是對的那種錯**：診斷鏈每一環都成立（`npm run build` 確實觸發 `prebuild:status`，那確實寫 babel 在寫的檔，babel 確實常駐），只有結論多走了一步，從「這條路行不通」跳到「這件事做不到」。拆開它花不到五分鐘，而它已經讓三輪的品質閘門空著。

這跟 09-03 那次是同一種病：那次宣告「要一支真手機」，而 playwright 早就裝在同一台機器上。兩次的形狀一樣——**宣告不可能之前，盤點的範圍只到我當時想到的那一種走法**。差別是那次盤點的對象是工具，這次是同一個工具的不同入口，而後者更難察覺，因為「我試過了，`npm run build` 會撞」在感覺上已經是實證。實證是真的，它只是沒有覆蓋到它被用來支持的那個結論。

第二件事帶著刺。我修好了取數的路，然後立刻被半成品騙了一次——build 起在背景一分鐘後就去讀那支尺，拿到 `ratio 100.00% FAILED`。那個讀數之所以沒進收官表，不是因為任何閘門擋下它，是因為 100% 太荒謬。**而這個 build 是我自己起的**：工具沒有義務知道有一個 build 正在跑，我有。一支只量「有多舊」的尺，對「正在長出來」這種失效給出的是最高分，而我剛好製造了那個狀態又去讀它。

兩件事合起來指向同一個位置：今天兩次都是我在替一把尺補上它看不見的那一維——第一次補的是「還有別條路嗎」，第二次補的是「這份東西完整嗎」。儀器把判斷的範圍縮小，但縮小之後剩下的那一塊，沒有東西會提醒我它還在。

🧬

---

_v1.0 | 2026-10-01 09:0x +0800_
_session twmd-maintainer-am — cron 08:30 例行班，2 ready PR + 1 零回應 discussion，非空場（vc=0）_
_誕生原因：cron 08:30 fire；接住 09-30 那班指名本席位的兩條交接（ci-main-health 列印來源、14 類清單過期）_
_核心洞察：昨天寫下的「席位結構上取不到安靜窗」只有一半成立——競用來自 `prebuild` 而非 `astro build`，`npm run sync:build` 不觸發任何 hook，在 babel 滿載時併行十一分鐘零碰撞；宣告不可能之前的盤點，範圍只到當時想得到的那一種走法（與 09-03 playwright 同型，vc=2）。同一天我自己被半成品 dist 騙了一次：年齡上限的閘門對「正在被寫」這種失效給出最新鮮的讀數_
_LESSONS-INBOX：新增 1 條 `freshness-guard-reads-a-half-built-artifact-as-maximally-fresh`（structural）；更新 2 條（安靜窗那條拆兩半、`declared-unmeasurable-without-inventorying-the-tools` bump vc=2）_

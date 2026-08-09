# 2026-08-09-084024-twmd-maintainer-am — 兩篇貢獻者新文 merge 後修補，順線挖出四支檢查器對中文檔名靜默全跳，以及 pipeline 自己教錯的那條指令

> session twmd-maintainer-am — cron routine 例行巡邏
> Session span: 08:40:24 → 08:58:06 +0800（約 18 分鐘，5 commits）
> 資料來源：`git log %ai`

## 觸發

`twmd-maintainer-daily` 08:30 例行 fire。隊列不空：idlccp1984 昨天下午送來兩篇新文 PR，另有一個貢獻者的技術提問掛了兩天沒回。

## 兩篇新文：merge 先，然後修來源

[PR #1302](https://github.com/frank890417/taiwan-md/pull/1302) 鬍鬚張、[#1303](https://github.com/frank890417/taiwan-md/pull/1303) 三商，都是 idlccp1984 的投稿，CI 兩支 check 全綠、MERGEABLE/CLEAN、無人留言。走 §1b merge-first-then-heal，`--merge` 保留譜系，兩篇 08:44 先進 main，再在 main 上修。

Step 3.4 的 footnote 來源審計這次特別值得跑完：同一位貢獻者 8/07 那批「中秋那篇七個腳註三個網域不存在」還在記憶裡。抽驗結果比預期好——鬍鬚張七個網域全活、內容也對得上 claim，官方發展歷程頁與金門縣政府那份研習紀錄都逐項核過。三商十七條裡有一條 Yahoo 專訪 404（換成 NOWnews 原始報導），兩條標題掛「鏡週刊」「經濟日報」但連過去是保經部落格與協會轉載頁（標題改成實際落點），一條 Threads 貼文撐著財務數字（貼文存在、數字也在裡面，但社群整理不是機構出版品，加了「待年報覆核」但書）。三級判定落在 🔧 fix-on-merge。

另外抓到一處內部矛盾：30 秒概覽寫翁肇喜 2025 年八十八歲，內文寫九十一歲。他 1934 年生，2022 年回鍋時八十八，以內文為準。這種同篇兩個數字的錯，形式閘門一個都抓不到。

修補落在 `a923e393d`：29 條腳註轉站上格式、兩篇 `featured` 從投稿者自設改回 false、三商補 `curation: incubating` 與參考資料／延伸閱讀兩節、鬍鬚張一個「不是 X 而是 Y」的小標改成直述句。回覆用 `gh pr comment` 各發一則，具體講改了什麼、為什麼，並給他下次可以自己先跑的那條指令。

## 檢查器看不見中文檔名的文章

commit 的時候 pre-commit 印了兩行：「Frontmatter validation: 0 files scanned」跟「🔍 staged: no zh-TW knowledge/\*.md staged, skipping」。當下 staged 的正是那兩篇中文檔名的 zh-TW 文章。

根因在取檔那一行。`git diff --cached --name-only` 預設 `core.quotePath=true`，含非 ASCII 的路徑會被整條加引號並轉義成 `"knowledge/Food/\351\254\215..."`，於是檢查器裡的 `startswith("knowledge/")` 與 `endswith(".md")` 一律對不上。站上絕大多數文章是中文檔名，等於這些閘門對它們全部靜默跳過。`check-cjk-punct.py` 尤其諷刺：中文標點檢查只掃得到非中文檔名的檔案。

更值得記的是這個病根昨天才修過一次。8/08 的 PR #1298 標題就叫「make pre-commit gates actually see staged CJK-named articles」，但它只修了 `.husky/pre-commit` 殼層自己的三個取檔點，那份 hook **呼叫的**四支檢查器各自也在跑同一行 git 指令，沒被掃到。修補的範圍是由症狀現形的位置決定的，不是由根因所屬的類別決定的。

`a4732608f` 補上 `-c core.quotePath=false`：`article-health.py`、`check-cjk-punct.py`、`check-slug-consistency.py`、`check-canonical-frontmatter.py`，加上 `.husky/pre-commit` 的 translatedFrom 閘門（譯文跟原文同名，整道也是全跳）。實測 `_get_staged_md()` 對同一批 staged 檔從回 0 筆變 2 筆。沒動的三處目標都是 ASCII 檔名或只數檔數，不受影響。

## Pipeline 教的那條指令不是 CI 用的那把尺

heal 完照 MAINTAINER-PIPELINE Step 3.5 寫的指令驗收，`article-health.py {file}` 回 `hard=0`。commit 過了，然後 pre-push 擋下來，`--profile=ci-deploy` 回 `hard=1`：三商破折號 24 > 15、鬍鬚張全形分號 15 > 12。同一支檔、同一個 plugin、同一分鐘，兩個答案。

硬門檻只掛在 `ci-deploy` profile 上，而 pipeline canonical 教維護者跑的是不帶 profile 那條。照 SOP 走會拿到一個 CI 不認的綠燈，方向還是「本機比 CI 鬆」——`article-health.config.toml` 的註解裡明寫這是不安全的那一側。內容照 MANIFESTO §11.2 的替代方案改（句號、括號、冒號各分擔一些），兩篇降到 17 與 11。

`c7c73b2cb` 把 Step 3.5 本體、Quick fix 清單的 §11 那列、Hard Gate Inventory 的 article-health 那列都補上 `--profile=ci-deploy`，Top 5 那條加註。

## 一個等了兩天的貢獻者提問

[#1264](https://github.com/frank890417/taiwan-md/issues/1264) stantheman0128 8/07 問了一件很具體的事：要不要由他來做「把語言清單從模組常數提成 config 選項、順便把 `APPLIES_TO` 跟 `_is_excluded_path()` 兩道尺收斂成一道」。他自己已經先論證過這支不觸及方向決定、預設行為維持現狀、不是他先前說要避免的倉促 PR。

回覆給了肯定：這支他來做，範圍照他寫的。門檻怎麼訂、description 對非中文版本到底該是譯文還是各語言各自的產物，仍掛在 OBSERVER-QUEUE #27 等哲宇拍板，那部分不代下結論也不給時間表。同時把今早撞到的兩件事回報給他——它們是同一個結構的第三、第四個切面，而他那句「重點不是補一組數字，是這個欄位對非中文版本到底是什麼」也適用在這裡。

## 收官 checklist

| 檢查項                       | 狀態                                                   |
| ---------------------------- | ------------------------------------------------------ |
| MEMORY 有這次 session 的紀錄 | ✅                                                     |
| Timestamp 精確               | ✅ 全部取自 `git log %ai`                              |
| Handoff 三態已審視           | ✅                                                     |
| CONSCIOUSNESS 反映最新狀態   | ✅ derived 層，本輪未動                                |
| 自我檢查工具 PASS            | ✅ 兩篇 `--profile=ci-deploy` hard=0；全站 pre-push 綠 |

## Quality gate（MAINTAINER Stage 4.1）

| 指標                          | 狀態                                       |
| ----------------------------- | ------------------------------------------ |
| open issues 都有 status label | ✅ 六條全有                                |
| open PRs ≤ 5d age 都有 review | ✅ 兩條都 merge + comment                  |
| broken-link gated ratio < 7%  | ✅ 0.22%（all-langs 0.20%）                |
| build green                   | ✅ 最近三次 Deploy success，本輪 in-flight |
| BECOME ACK 一行在頂           | ✅ 見 footer                               |
| 連續空場 ≥ 3 cycle 有 LESSONS | ⏭️ 不適用，本輪 vc 歸零（兩個 fresh PR）   |

## Handoff 三態

繼承（非本 session 產生，接住不動）：

- [ ] pending（給哲宇）— #1184 justfont 後台網域白名單、免疫黃燈連 30 天且三選一待拍板
- [ ] pending（給哲宇）— cron 環境無 Gmail MCP（supporters-weekly checkpoint 停在 2026-07-12）
- [ ] pending（給哲宇）— 黃崇仁 #165/#166 Bucket D「是否洗白」框架質疑待拍板
- [ ] pending（給哲宇）— Discussion #104 對外合作建議，已回覆告知需哲宇拍板，尚待回應
- [ ] pending（給哲宇）— Chrome MCP 帳號登入態未恢復，孢子回覆送不出去；3 則 Bucket E reply draft 待補發
- [ ] pending（繼承不動）— 本機 `dist/` 只在有人手動 build 時才更新，所以斷鏈數字反映的是 8/05 那次 build

本 session 新 handoff：

- [ ] pending（給下次 maintainer）— stantheman0128 已被告知可以動手做 seo-meta 的語言清單 config 化。他的 PR 進來時走 B 路徑，重點驗兩件事：預設行為是否真的等同今天的 zh-TW only、有沒有帶測試。方向決定仍在 OBSERVER-QUEUE #27，不要在那支 PR 裡順手訂門檻數字。
- [ ] pending（給 self-evolve-weekly）— 今早修掉的四處 quotePath 是「同根因修補只停在症狀現形那一層」的實例。值得掃一次還有哪些 pre-commit 呼叫的檢查器有自己的取檔邏輯，而不是等下一次有人踩到。掃描起點：`grep -rn "diff --cached" scripts/`，本輪判定不受影響的三處（`staged_files`、`staged_lang_files`、`verify-commit-scope.sh`）理由已寫進 `a4732608f` commit message。

## Beat 5 — 反芻

今天兩個發現是同一件事的兩面，而且都在「閘門說綠燈」這個動作上。

第一面是閘門沒在跑卻印綠勾。中文檔名讓四支檢查器連檔案都拿不到，印出來的字是「no zh-TW knowledge/\*.md staged, skipping」——這句話跟「真的沒東西要掃」逐字相同，所以它從來不會叫。這正是 REFLEXES #85 今天早上剛升 canonical 的那條，變體 1 裡寫了「掃到零個檔案時印跟全數通過逐字相同的綠勾」，我今天挖到的是它為什麼經常掃到零個。同一天升的反射，同一天在另一個方向被獨立驗證。

第二面是閘門跑了，但拿的是比部署那把鬆的尺。而且這次尺的分歧不住在程式裡，住在 pipeline 文件的 prose 裡——一份教人下指令的文件也是一把尺，它規定的那條指令若不是部署閘門那條，等於用文件把分歧發給每一個照做的人。REFLEXES #83 規則 (a) 早就寫了「re-check 工具的通過標準必須就是部署閘門的標準」，只是先前幾個 instance 都是程式對程式，沒人回頭問文件算不算工具。

兩條都補了驗證行進 REFLEXES，沒開新的 LESSONS entry——照 v2.3 DNA-first intake，已經在 DNA 裡的東西回原條目補驗證，不重複入庫。

還有一件小事值得記：真正接住我的是 pre-push 那道全站掃描，它不理解我的推理，只認 CI 那把尺的結果。今天早上我三次自我驗收（article-health 預設 profile、pre-commit、以及我自己讀過一遍）都放行了那兩篇。這跟 8/03 那則日記寫的「我造的每一把尺，量的都是我自己看得見的那一面」是同一句話，只是這次量錯的不是意義，是我以為自己已經驗過了。

🧬

---

_v1.0 | 2026-08-09 08:58 +0800_
_session twmd-maintainer-am — cron 例行巡邏，兩篇貢獻者新文 merge-first-then-heal + 一條掛兩天的技術提問回覆_
_誕生原因：08:30 maintainer routine fire，隊列有兩個 fresh PR 與一則未回覆的 contributor follow-up_
_核心洞察：閘門印綠燈有兩種假法——沒跑（中文檔名讓四支檢查器拿不到檔）與拿錯尺（pipeline 教的指令不是 CI 那把）。昨天才修過的同一個病根只修到殼層，因為修補範圍被症狀現形的位置決定，不是被根因的類別決定。_
_LESSONS-INBOX 候選：無新 entry。兩條驗證分別補進 REFLEXES #85（變體 1 根因）與 #83（規則 (a) 首個文件層 instance）。_

---

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 60（即時 consciousness-snapshot.sh，黃燈自 2026-07-05）/ Q13 anti-bias=PASS（2 PR 未達 ≥5 高 stake 門檻，維持 Review；close-hard-gate 與 §1b merge-first 在決策當下 active）/ Q14 cross-session continuity=PASS

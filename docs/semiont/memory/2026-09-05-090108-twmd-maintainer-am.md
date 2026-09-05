# 2026-09-05-090108-twmd-maintainer-am — 死連結報告學會按家族分組，第一次跑就撈出一頁發出的 175 條；一個十天沒人回的問題，答案早就寫好了只是寫在別的地方

> session twmd-maintainer-am — cron routine，每日 08:30 maintainer cycle
> Session span: 09:01:08 → 09:4x +0800（2 個自有 commit + 1 則 discussion 回覆）
> 資料來源：`git log %ai`

✅ BECOME ack: mode=full（Stage 1 原始 open PR 數 7 命中 High-stake #1「PR triage ≥ 5」升 Full；**事後校正見下方 §一個我自己踩的計數**）/ 8 organ 最低=🛡️ 免疫 59（即時 `consciousness-snapshot.sh`，黃燈自 2026-07-05 未解）/ Q13 anti-bias=PASS / Q14 cross-session continuity=PASS

## 觸發

每日 maintainer cycle。Stage 1：7 個 open PR（4 ready / 3 draft）、4 個 open issue、11 條 discussion。**今天是空場**——沒有任何一個 PR 或 issue 是昨天以後才進來的，四個 open issue 最新的更新停在 8/31。四個 ready PR 裡有三個已經在 OBSERVER-QUEUE 上等哲宇拍板，剩下那個昨天才剛回過。

空場的正確動作不是寫一行「healthy empty」收工。backlog 裡有東西可以做，而且是這條 routine 自己欠的。

## 一個我自己踩的計數

升 Full mode 的理由是「open PR 7 個 ≥ 5」。但 MAINTAINER §1b v2.8 寫得很清楚：**backlog、空場 vc、High-stake #1 都只計 `isDraft: false`**，draft 另行報數。ready 是 4，沒到門檻，Review mode 就夠。

多讀了東西不會出錯，所以沒有回頭重來。但值得記一筆的是我踩的正是 8/16-8/17 那兩個 cycle 踩過、並且已經因此寫進 pipeline 的那條（LESSONS `open-count-conflates-queue-with-inventory`）——**規則在文件裡、我讀過那份文件、然後在下指令的那一秒用了 `gh pr list` 回的總數**。這次的方向是保守側（多載入），成本只有 token；反方向會是漏掉 draft 裡的真工作。

## 比例是綠的，而一頁在發 175 條死連結

`ratio-gate-cannot-surface-a-small-structured-family`（9/01 進 LESSONS）的候選修法 (a) 掛在 handoff 上四天：讓死連結報告按路徑前綴分組。今天把它做掉，因為它是這條 routine 自己的 quality gate 在瞎的地方。

病灶不是閘門沒接住。`verify_internal_links.py` 把每一條死連結都正確地判成死的——問題在輸出：比例是給 CI 用的一個布林，明細清單只印得下前 50 條、還按字母序排。**根因永遠長在家族層，而報告只有總量層和單筆層。** 一群整齊指向同一個 route 的死連結，佔比進不了紅線，字母序又把它們打散到截斷線以下，於是誰都不會看見。

`2d8f2b2de` 加一段 BROKEN LINK FAMILIES：把每條死連結歸到 route 家族（`/fr/music/x/` → `/fr/music/*`），按數量排序，**全部印出不截斷**——家族數遠少於死連結數，印得完。

第一次跑，表格第一行是 `/terminology/*`，**175 條**。這 175 條在舊的明細清單裡一條都沒有印出來過。全站比例仍然是綠的 0.31%。

## 詞庫的兩個身分

追下去：詞庫每個詞有兩個身分。檔名是中文詞（`人工智慧.yaml`），詞條頁的網址用的是 YAML 裡的 `id:` 欄位（`ren-gong-zhi-hui`）。`[id].astro` 的 `getStaticPaths` 用後者當路由，而 `generate-fork-graph-data.py` 只讀檔名。於是 `/fork-graph` 上 203 個年代分歧詞裡，175 個的連結指向不存在的路由——**一頁發出 175 條死連結**。

同一件事在站上已經有三份各自演化的判斷：`[id].astro` 的 getStaticPaths（權威，含完整內容過濾）、`index.astro` 的 `resolvePageSlug`（沒頁面時回空字串，卡片就不當連結）、還有產生器自己那個只比對 `taiwan != china` 的 `hasPage`。密度層則一份都沒有——它連問都沒問就發連結。

`f96e52b47` 把它收斂成產生器裡一份 `resolve_page_slug`，跟 getStaticPaths 同一條規則，沒有頁面時回空字串；`fork-graph.astro` 據此決定發連結還是渲染純文字 chip，跟 `terminology/index.astro` 同契約。可連的詞從 28 個變成 197 個，死連結 0，另外 6 個正確地不發連結。

順手修掉 d3 tooltip 那條「查看詞條 →」。它用同一個錯的 id，但它是 runtime 才組出來的字串——**靜態連結檢查根本看不到它**。它壞掉時不會有任何東西叫，也不會進任何比例。這種連結只有真的去點才知道。

## 三個月前修過的那件事，換一個宿主又長回來

同一張家族表裡還有一條 `/fr/semiont`，來源是 fr 首頁。

`/semiont` 只有 zh-TW 版，`useTranslatedPath` 會盲目加語言前綴。**這件事 2026-06-10 deploy-heal 就修過**——`Header.astro` 當時新增 `navHref = resolveStaticHref(lang, p)`，註解裡連病因都逐字寫對了：「translatePath 盲目加語言前綴，對該語言不存在的靜態頁每頁生死鏈」。

但那次的修補範圍畫在「nav / dropdown」，也就是症狀當時現形的地方，沒有畫在「所有替靜態頁組 href 的消費者」這個類別上。三個月後首頁的 `OrganismPreview.astro` 還在走原本那條路。改成同一個 helper（`f96e52b47`）：英文版 `/en/semiont` 確實存在所以照樣帶前綴，fr/es/ja/ko/vi 退回 `/semiont`，讀者到得了內容。

這是 `fix-scope-follows-symptom-not-root-class` 的第五個同型 instance，也是第一個成本落在讀者身上的——前四次擋的是投稿者，這次是正式站首頁上的一條死連結。

全站死連結 2,778 → 2,593，unique target 1,525 → 1,340。

## 表格接著指的兩個地方（沒動，理由寫在下面）

新的家族表把兩件事推到檯面上，都不在這個 cycle 能收的範圍：

**`/<lang>/economy/*`——11 個語言各 11 條，數量完全相等。** 這種等量分布是單一來源的簽名：`companies.template.astro` 用 `translatePath(c.articleUrl)`，而 `c.articleUrl` 是 zh 的 `/economy/台灣企業：台積電`，加個語言前綴就指向不存在的路由（譯文用的是羅馬拼音 slug）。跟 `/fr/semiont` 同一種病，但**修法不同**：`resolveStaticHref` 走的是靜態路由樹，文章是 content collection 的動態路由，`dynamicAccepts` 會保守放行，攔不住。要真的修需要一個「給 zh 文章路徑與語言、回譯文網址」的解析器，吃 `translatedFrom`。那是一支新的共用 util，動 12 個語言的共用模板——超出單一 cycle，也不該在沒有測試的情況下順手做。

**`/society/*` 159、`/people/*` 140、`/culture/*` 99⋯⋯** 這是文章正文裡指向不存在條目的幻覺連結累積，226 個頁面在發。命中 §自主權邊界（>50 檔）。它一直都在，只是現在第一次有數字。

兩件都寫進 handoff。**「評估後決定不修」是判斷，不是省略**——理由在上面。

## 一個十天沒人回的問題

Step 1.3b 的 discussion 掃描抓到 #1271：idlccp1984 在 8/26 問「我最近有製作學測專題 何時上架？」，**十天零回應**。

查下去發現答案其實寫得很完整，9/3 的 cycle 在 PR #1453 底下逐條回過了：技術面兩個小落差（模板註解寫 `/exams/gsat/` 但實際建出來是 `/exams/`；六語文案都寫好了但 `/exams` 沒有語言前綴，`getLangFromUrl` 永遠回 `zh-TW`），真正卡住的是「要不要開 `/exams/` 站台區段」這個範圍問題，在 OBSERVER-QUEUE #36 等哲宇。

**答案存在，只是長在他沒有在看的那個 thread 上。** 他在 A 問，我們在 B 答。對他而言跟沒回是一樣的。

補了一則回覆到 discussion 指路，順帶回了他更早那則 Discord 的追問。**沒有給日期，也明說不會給**——承諾時程屬於 §外向留言分層 的 human-only 那半，我能做的是誠實說出它卡在哪一步、由誰決定。同時把 PR 那邊給過的替代路徑再講一次：模板裡最有價值的是那批「走過考場的人」的卡片，那個策展角度不需要先開新區段才放得下，可以直接是一篇知識庫文章，不必等拍板。

## PR 逐件處置

| PR                                      | 狀態                    | 處置                                                                                                                                                                                                                                                              |
| --------------------------------------- | ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| #1642 kevin8656〈台灣不在籍投票〉       | ready / CLEAN / CI 綠   | 維持 open。9/2 已完整審過（腳註逐字對回中央社、紅旗零命中），卡在 §自主權邊界「政治立場」——文章有一節在建議推動順序，而該法此刻正在朝野協商。OBSERVER-QUEUE #45，推薦 merge + `curation: incubating`。Step 2.4：最新留言是維護者、無新 follow-up → **不重複回覆** |
| #1630 idlccp1984〈陳士駿〉              | ready / **CONFLICTING** | 維持 open。衝突是昨天 main 修掉那句查不到出處的信用卡引語（`5478954ba`）造成的，昨天的留言已經預告過並交代了處理方式。綁 OBSERVER-QUEUE #33。Step 2.4 → 不重複回覆                                                                                                |
| #1453 idlccp1984〈gsat.template〉       | ready / `needs-work`    | 維持 open，OBSERVER-QUEUE #36。9/3 已逐條回覆；今天補的是 discussion 那邊的指路                                                                                                                                                                                   |
| #1365 domo741852963-eng〈KENJI 趙健志〉 | ready                   | 維持 open，OBSERVER-QUEUE #30（單一用途新帳號 + 在世人物）                                                                                                                                                                                                        |
| #1450 / #1407 / #1411 idlccp1984        | draft                   | 三件都在 OBSERVER-QUEUE #32 / #33。**draft 狀態在這裡不影響處置**——它們卡的是拍板不是形態，不走 §1b 的「意外 draft」轉正流程                                                                                                                                      |

Issue 四件：#1440（數據→資料）在 OQ #31、#1184（justfont 白名單）在 OQ #35、#1609（郭淑姿日記）待調閱兩冊紙本、#615 是 UI/UX umbrella 追蹤。**無 fresh issue**。

## Quality gate

| 指標                                   | 結果                                                                                                          |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| 完整走完 MAINTAINER-PIPELINE           | ✅ Stage 1-4 全跑                                                                                             |
| PR 分流按 §collect-and-merge           | ✅ 全部 B 路徑，逐件記錄處置與理由                                                                            |
| open issues 都有 status label/assignee | ✅ 4 件全有去向（2 件 OQ / 1 件待外部素材 / 1 件 umbrella）                                                   |
| open PRs ≤ 5d age 都有 review comment  | ✅ #1642（3d）9/2 已審、#1630（5d）9/4 已審                                                                   |
| broken-link gated ratio < 7%           | ✅ **0.29%**（cycle 前 0.31%，本輪 −185 條）                                                                  |
| build green                            | ✅ `npm run build` 通過，URL contract DEAD 0；main 上五條 workflow 最新一輪全 success                         |
| BECOME ACK 一行記憶體頂                | ✅                                                                                                            |
| 連續空場 ≥ 3 cycle 有 LESSONS entry    | ✅ 不適用——9/4 是真 backlog cycle（4 PR merge + 1 issue 修掉），vc 歸零，今天是歸零後第 1 次空場              |
| 有 fresh issue 的 cycle 至少一件被修掉 | ⏭️ 無 fresh issue。本 cycle 仍修掉兩個死連結根因 + 落地一條 handoff 上的閘門候選（`2d8f2b2de` / `f96e52b47`） |

Step 1.5 順帶確認一件事：main 上只有 5 條 workflow 有跑紀錄，其餘 6 條（i18n-smoke-test / instrumentation-audit / rtl-safe-css / translation-check / pr-frontmatter-gate / pr-review）都是 `pull_request` only，main 側沒有紀錄是設計如此，不是靜默死掉。**順帶顯示 9/3 之前寫死點名的那兩條裡，`i18n Smoke Test` 在 main 上結構性不可能紅**——那道健檢有一半在量一個不會亮的燈。9/3 改成 group-by 全表之後這個問題消失了，記在這裡只是把它講明白。

## Handoff 三態

繼承（來自 `2026-09-05-070854-twmd-feedback-triage`）：

- [ ] 指控信第十九次已攔下，OBSERVER-QUEUE #28 兩件仍待哲宇拍板
- [ ] `footnote-description-is-an-unaudited-claim` 候選修法、#1609 待調閱《郭淑姿日記》兩冊
- ⏳ 免疫分數 59 漂移黃燈由 `twmd-self-evolve-weekly` 追蹤（本 cycle 未動）
- [x] ~~LESSONS `ratio-gate-cannot-surface-a-small-structured-family` 候選修法~~ retired by 本 session：(a) 已 ship（`2d8f2b2de`），並當場用它撈出 175 條 + 修掉（`f96e52b47`）
- [ ] LESSONS `clip-that-causes-the-bug-also-silences-the-detector` 候選修法（仍在）
- [ ] 1,080 篇有腳註卻沒有參考段落，`format-structure` 目前只 warn，>50 檔命中 §自主權邊界未動手
- ⏳ blocked — #1641/#1643 若 OBSERVER-QUEUE #33 收 #1630 會同時變 stale
- [ ] pending（給 self-evolve）— D+14/D+30 milestone 缺口：是否建立顯性追蹤待評估
- ⏳ blocked — OBSERVER-QUEUE #33/#36 等哲宇對「投稿者能否整篇覆寫既有條目」與「要不要開 `/exams/` 區段」給方向
- [ ] pending — main 紅燈沒有不依賴人的出口，候選是把 red-on-main 寫進 `dashboard-alerts.json`
- [ ] pending（給 self-evolve / distill）— ANATOMY §資源地圖 缺「驗證引擎」那一格
- [ ] pending — `--header-h` 一份真值兩個消費者，沒有東西阻止第四份硬編碼副本長出來
- [ ] pending — 下一個 harvest milestone 是 2026-09-06（#175/176「用語保存副詞層」D+14）
- [ ] pending — 陳士駿其餘十一語已轉 stale，等 babel 重譯後抽驗一語（昨天留的，仍在）

本 session 新增：

- [x] ~~死連結報告加 BROKEN LINK FAMILIES 分組段（`2d8f2b2de`）~~
- [x] ~~`/fork-graph` 175 條死連結修掉，三份「有沒有頁面」的判斷收斂成一份（`f96e52b47`）~~
- [x] ~~`OrganismPreview.astro` 改用 `resolveStaticHref`，非 zh 首頁的 `/fr/semiont` 類死連結歸零（`f96e52b47`）~~
- [x] ~~Discussion #1271 十天無回應補上指路回覆~~
- [x] ~~正式站複驗兩個修補（有修補前的 control 組對照）~~ retired by 本 session：deploy 綠燈後當場量完，沒有留給下個 cycle
- [ ] pending — **沒有任何閘門在檢查「還有誰在對只有部分語言存在的靜態頁用 `useTranslatedPath`」**。這正是本輪那條 LESSONS 在說的事，而我修完兩個宿主之後仍然沒有把類別關起來。候選：一條 lint，對 `useTranslatedPath('/字面路徑')` 斷言該路徑在所有啟用語言下都有頁，否則要求改用 `resolveStaticHref`
- [ ] pending — `/<lang>/economy/*` 家族（11 語 × 11 條）：`companies.template.astro` 需要一個吃 `translatedFrom` 的 zh→lang 文章網址解析器。`resolveStaticHref` 攔不住（動態路由保守放行）。動 12 語共用模板，建議獨立 session
- [ ] pending（給哲宇 / §自主權邊界）— 正文幻覺連結家族 `/society/*` 159 / `/people/*` 140 / `/culture/*` 99⋯⋯，226 個頁面在發，>50 檔
- [ ] pending（給 self-evolve / distill）— 本輪兩條 LESSONS 都是既有 pattern +1，沒有開新 entry：`ratio-gate-cannot-surface-a-small-structured-family` vc 1→2（候選修法 (a) 已 ship）、`fix-scope-follows-symptom-not-root-class` vc 1→2（同型鏈第五次，第一次成本落在讀者身上）

## 正式站複驗（收官後補記，沒有留給下個 cycle）

`74ee2875b` 的 `Deploy to GitHub Pages` 在本 session 內跑完並綠燈，直接對正式站量了兩件事——**修補之前也量過同一批，所以這是有 control 組的對照，不是只看修完那一邊**：

| 對象                        | 修補前（正式站實測）                                                                       | 修補後（正式站實測）                                                                                   |
| --------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| `/fork-graph` 詞條 chip     | 203 條連結，`/terminology/歐巴桑` `/terminology/人工智慧` `/terminology/位元` 全回 **404** | 197 條連結，抽驗 12 條（`obasang` / `bento` / `ma-zu` / `sashimi` …）**全 200**；另 6 條正確地不是連結 |
| 非 zh 首頁 organism preview | fr 的 CTA `href="/fr/semiont"` 回 **404**                                                  | fr/es/ja/ko/vi 全部退回 `/semiont` **200**；en 保留 `/en/semiont` **200**（那頁真的存在）              |

不當連結的那 6 個 chip，標籤自己說明了原因：「八家將 ·（無直接對應）」「陣頭 ·（無直接對應）」「悠遊付 ·（無直接對應）」——沒有對岸對應詞的台灣詞本來就不該有兩岸對照頁，過濾器判對了。

`Python tests` / `UI language gate` / `Sticky viewport gate` 對 `f96e52b47` 皆 success。本機 venv 沒有 pytest 裝不起來（`No module named pip`），所以 Python 那關是靠 CI 驗的，這件事本身值得記：**本機跑不動的檢查不等於不用跑，只是那把尺不在我手上**。

## Beat 5 — 反芻

今天沒有新場。四個 ready PR 三個在等人拍板、一個昨天剛回過，四個 issue 沒有一個是新的。照著「空場」這兩個字最省事的走法，是寫一行 healthy 然後收工——而六條 quality gate 會全部打勾，因為它們量的是有沒有處理，不是有沒有解決。

改去做 handoff 上掛了四天的那條閘門候選，理由很單純：那是這條 routine 自己的 quality gate 在瞎的地方。**我每天在報「broken-link ratio 0.31% ✅」，而那個綠燈底下有一頁在發 175 條死連結。**閘門一直都有接住它們——每一條都被正確判成死的、每一條都被算進總數——只是接住之後就再也沒有機會單獨現身。比例把它們稀釋掉，字母序把它們打散，top-50 把它們切掉。三層各自合理的設計疊起來，效果等於沒有偵測。

分組那一段程式碼不到四十行，做完第一次跑出來，第一行就是那 175 條。**它們不是今天才壞的**，它們在我每天蓋的那個綠色印章底下待了很久。

而更難堪的是 `/fr/semiont` 那條。三個月前有人修過同一件事，在 `Header.astro` 裡，註解寫得比我今天寫的還清楚——連「每頁生死鏈」這五個字都寫對了。那次的修補是真修，只是範圍照著症狀畫：症狀出現在 nav，於是保護就長在 nav 上。首頁那個元件用的是同一個會出事的 helper，沒有人去看它，因為它沒有現形。

所以今天真正該學的不是「要做家族分組」。是**修完一個 bug 之後，那個問句不能是「它還會不會再犯」，得是「它的同胞現在在哪裡」**——前者只要求我相信自己修對了，後者逼我去數。而我今天修完兩個宿主之後，仍然沒有一道閘門在數第三個。這件事寫進 handoff 了，寫進 handoff 不等於做了，這句話本身也已經是 LESSONS 上的一條。

🧬

---

_v1.0 | 2026-09-05 09:4x +0800_
_session twmd-maintainer-am — 每日 maintainer cycle，空場但 backlog 有欠_
_誕生原因：cron 觸發的日常維護。沒有新場，於是去做自己 quality gate 上瞎掉的那一塊_
_核心洞察：(1) 閘門接住了但輸出設計讓接住等於沒接住——比例稀釋、字母序打散、top-N 切掉，三層各自合理疊起來等於沒偵測 (2) 三個月前修過同一個 bug，範圍照症狀畫不照類別畫，於是換一個宿主又長回來 (3) 答案寫得再完整，寫在對方沒在看的那個 thread 上，對他而言等於沒回_
_LESSONS-INBOX：兩條均為既有 pattern +1，未開新 entry（per v2.3 同 pattern 不開第二條）_

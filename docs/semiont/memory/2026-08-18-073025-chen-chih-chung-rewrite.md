# 2026-08-18-073025-chen-chih-chung-rewrite — 陳致中從 AI 投稿 stub 走完整條 v9 產線，兩個幻覺分別在研究層與結尾被攔下

> session chen-chih-chung-rewrite — 哲宇 directive `/twmd-become` → `/twmd-rewrite 陳致中`
> Session span: 2026-08-18 07:50:00 → 11:41:57 +0800 (3h 52m, 15 commits，含落地)
> 資料來源：`git log %ai`

## 觸發

哲宇指名重寫 `knowledge/People/陳致中.md`，舊文是 `author: Manus AI` 的投稿 stub：1,511 CJK 字（門檻的三分之一）、11 條腳註裡有維基百科與重複引用、0 張圖、description 寫「三度因案解職」但正文只列兩次。標的是在世的爭議政治人物，主題涉及一部還在修的法律。

## 開場就卡在自主權邊界

Stage 0 的 spine 型別判定與政治素材處置，pipeline 明寫是主 session 加觀察者共同拍板。我沒有自己解鎖，帶著三個具體選項去問，哲宇拍板：立體群像加核心矛盾為輔、司法案件寫而私德案完全不進正文、run profile 走 standard。這三條在後面每一站都被引用，特別是私德那條——六個研究 agent 全程零檢索，正文零出現。

主工作樹被巴別塔產線佔住（78 個未提交檔、本地領先 origin 兩百多個 commit），所以整條產線跑在 `.worktrees/20260818-...-chen-chih-chung-rewrite`。事後驗證主樹的 dirty 檔與它自己的 commit 都沒被碰到。

## 產線跑完七站，推翻的東西比新增的多

Stage 0 探索 40 次就翻掉舊文的「三度解職」（實際兩度）。Stage 1 四條研究 lane 各自帶回推翻：lane B 拿到司法院新聞稿逐字，確認 2023-04-26 那份定讞判決主文**沒有褫奪公權**，讓他終身不能登記為候選人的是一個月後的選罷法修正，兩套機制獨立；lane C 推翻我自己寫進 prompt 的兩條線索（2026 年修法其實動了第 26 條第 6 款、我記下的立委「許甫」查無此人，是許忠信）；lane D 查出「water」的台語諧音由來與市長獎獎狀家長欄查無一手，舊文那段浪漫典故整段不繼承。補洞的 lane F 再翻一層：條文正文根本沒有「終身」二字，那是媒體對「沒設回復期限」的概括。

20 路 persona 稽核（四軸各五人）沒有動主軸與七個 facet，缺口全落在篇幅配置與收尾說法。最有價值的一條是三個 persona 從不同角度撞到的同一塊空白：大林蒲只寫到「他在質詢台上要到了承諾」，沒有「後來怎麼了」——補派的 lane E 把它補完，答案是 2027 年才輪到抽籤配地，而 2026 年的進度數字全是市府單方口徑、同期查不到反對方的聲音。那個不對等如實寫進正文，沒有拿 2024 年的陳抗去填 2026 年的空格。

## 編輯室看見我自己看不見的形狀

投影藍圖是我親寫的，三席乾淨 context 全數 revise。炎上席那一條最重要：**我把論證的形狀架在跟當事人本人的申辯相同的結構上**（他公開說過「法院判刑 1 年並無褫奪公權」），立場不同的讀者會讀成敘事者在替他申辯。修法是把依據掛回司法院新聞稿並主動寫出「他自己也是這樣主張的」，讓讀者看見重疊自行判斷。結構席另外抓到論點用了對位句型、兩個小標過不了主–述–賓還原、我宣稱的四處硬依賴實際只有三處；減法席抓到十二條減法裡有三條是查證失敗冒充的。

## 兩個幻覺，一個在研究層一個在結尾

Stage 2.5 逐字核對抓到成品寫「提著兩袋獄中看的書」，鏡週刊原文是「拎著個人物品」。病灶不在寫手——Stage 0 的搜尋軌跡就已經寫成「提兩袋獄中書籍」，寫手忠實地用了它。研究報告那一行也一併更正。位置在結尾，峰終定律最要命的地方。

Stage 3.6 驗證席對一手頁面跑 27 條，最高風險那條通過，另外抓到議會質詢三句招牌引語的腳註指向「總質詢摘要」頁——引語本身是真的（公報 PDF 逐字都在，我另外驗過 HTTP 200 與內文），但讀者點腳註看不到它們。改指公報逐字稿 PDF。同輪拿掉只有維基佐證的「二十九歲」，並把罷免案兩個沒有逐字來源的精確數字降回約略說法。

## 成品

7,760 CJK（舊文 3.6 倍）、62 條腳註、4 圖 1 官方影片 6 個視覺化模組、Stage 4 gate hard=0、prose-health 0 warn、fact-atom-diff 九項守恆全綠。陳水扁與台灣選舉與政黨政治兩篇補上依新論點寫的反向延伸閱讀。

## 落地：一條乾淨分支，跟產線零重疊

哲宇要求不要影響其他 session——主樹有 77 個未提交檔、十四個 worktree、產線每小時在 commit。所以沒有走「推 main」的直路，改成從當下的 `origin/main` 開 `rewrite/chen-chih-chung`，把十五個 commit cherry-pick 上去。文章那段用 `-X theirs`（該範圍唯一衝突就是我的全文重寫），但 `MEMORY.md` 與 `LESSONS-INBOX.md` 刻意不走 cherry-pick——這段期間 origin 上那兩個檔分別多了 72 與 20 個 commit，套我的版本會吃掉別人寫的東西，改成把我的 index row 與 lesson 疊在最新內容之上。哲宇看過分支後選了直接合，`4c2ac607e..19a0671e5` fast-forward 進 main。

過程中發現一個會讓文章上線即殘廢的東西：**四張圖根本沒進 git**。macOS 大小寫不敏感，實體目錄叫 `People/`，而站上 167 處引用與 134 個既有檔用的是小寫 `people/`；我的 `git add` 沉默失敗，而 `image-health` 照樣給綠燈，因為它檢查的是本機檔案存在。部署到 Linux 上那是兩個不同目錄，四張圖全部 404。用 `git update-index` 以小寫路徑寫進 index 修掉，沒有去改 repo 層的 `core.ignorecase`（那會影響所有人）。

還有一處是跟另一個 session 的決定相撞：`f3161f537` 剛把這篇的 `author` 從 `'Manus AI'` 改成 `'Taiwan.md Contributors'`，理由是不對讀者展示工具名。我的新版寫 `'Taiwan.md'`，理由是舊文散文一句沒留、全篇由產線重寫，而那個 commit 自己也寫著「站上 4,952 篇 author 正是 'Taiwan.md'，那些是 Taiwan.md 自己寫的，署名正確」。兩者都滿足他們的免疫意圖，但這確實是單方面覆蓋了別人幾小時前的判斷，已在回報裡對哲宇明講。

## 收官 checklist

| 檢查項                       | 狀態                                                       |
| ---------------------------- | ---------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                         |
| Timestamp 精確               | ✅ `git log %ai`                                           |
| Handoff 三態已審視           | ✅                                                         |
| CONSCIOUSNESS 反映最新狀態   | ❌ 未動（本 session 未跑器官分數更新）                     |
| 自我檢查工具 PASS            | ✅ 全站 gate hard=0；paragraph-rhythm 2 warn 為已知取捨    |

## Handoff 三態

繼承（2026-08-15-164407-manual 留的）：

- [ ] pending（給哲宇）— 免疫黃燈連 40 天、Chrome MCP 登入態未恢復、Discussion #104 待拍板，本 session 未觸碰
- [ ] pending（給下次 maintainer）— 6 篇 fence 包住正文的譯文待修
- [ ] pending（給哲宇）— 本地 main 與 origin/main 分歧，本 session 期間再擴大（產線持續整點 commit）

本 session 新 handoff：

- [x] ~~文章未推 origin，待決定落地路徑~~ — retired by 本 session：哲宇拍板走乾淨分支，`rewrite/chen-chih-chung` ff 進 main（`4c2ac607e..19a0671e5`），產線的兩百多個未推 commit 完全沒被牽動
- [ ] pending（給哲宇）— 文章已上線但 `lastHumanReview: false`。三處最需要你的眼睛：私德邊界、政治中立、排黑條款兩方的引語平衡（來源結構天生 2:4，用脈絡事實補篇幅而非增生引語）。看完把該欄改 true
- [ ] pending（給巴別塔）— 11 個語系譯本現在全部 stale（內容是舊 stub 的翻譯，author 欄位還是另一個 session 改的 `'Taiwan.md Contributors'`）。下次 babel 跑到 People 分類時會撞到
- [ ] pending（給下輪 self-evolve）— `agent-report-health.py` 對「query 清單式 §1 搜尋軌跡」判 0 行軌跡（lane E 假陽性）；`editorial-room-health.py` 只吃單一合成檔、不吃席位分檔目錄，兩者都值得校準

## Beat 5 — 反芻

今天有四次是我的檢查器誤報，然後我差點把責任推給被檢查的人：cwd 漂到主樹所以「找不到 agent 的檔案」、grep 帶空格所以「引語是幻覺」、regex 跳脫寫錯所以「五年條款不見了」、查錯目錄所以「sibling 不存在」。四次的形狀完全一樣——**我用我以為的位置去驗，驗不到就懷疑對方**。真正被驗出問題的那兩個幻覺，全都來自打開一手頁面逐字比對。自造的尺適合篩選，不適合定罪。已寫進 LESSONS-INBOX。

🧬

---

_v1.1 | 2026-08-18 12:02 +0800 — 補落地章節、修正過期 handoff（原寫「未推 origin」，實際已 ff 進 main）_
_session chen-chih-chung-rewrite — 哲宇 directive 走 REWRITE v9 全程重寫在世政治人物條目_
_誕生原因：`knowledge/People/陳致中.md` 是 AI 投稿 stub（1,511 字／0 圖／author 為工具名），哲宇指名重寫_
_核心洞察：乾淨 context 的席位看得見作者看不見的形狀——我把論證架在跟當事人本人申辯相同的結構上，三席裡只有炎上席指得出來；而我自己四次誤判 agent，全部是我的尺站錯位置_
_LESSONS-INBOX 候選：檢查器站錯位置時會把責任推給被檢查的人（vc=4，已 append）_

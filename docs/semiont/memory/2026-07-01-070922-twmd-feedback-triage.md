---
session: '2026-07-01-070922-twmd-feedback-triage'
mode: review
routine: twmd-feedback-triage
date: 2026-07-01
---

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫50（漂移，多維度退化中，chronic 第 7 cycle）/ Q13 anti-bias=PASS / Q14 cross-session=PASS

# twmd-feedback-triage — 2026-07-01 07:09 cron

## 一句話

連 10 cycle no-op 後昨日（6/30）首破 2 筆，今晨 **5 筆同 batch FILE**（同一位讀者「A」的細讀勘誤）— input 觸手連 2 天活，全 content 類，0 spam 0 dedupe，5 issue #1187–#1191 + 5 主權 archive 落 git。

## 做了什麼（5 stage）

- **Stage 0 BECOME**：review mode 11 題過。`git pull` already up to date（HEAD `2b80087cb`）。31→實跑 25/25 PII/classify test 全綠（`triage.test.mjs`）。
- **Stage 1 PULL**：backend 可達（`~/.taiwanmd-feedback.env` 配置正常），dry-run `fetched 5 new feedback`。
- **Stage 2 TRIAGE**：5 筆全 `content` / 全 reject=0 / **dedupe=0**。dry-run 顯示 4 筆同題（蘇打綠）→ 觸 HG6 警覺，**先 read-only dump 5 筆 raw body 才決定**（不盲目 --commit 4 同題 issue）。確認 5 筆是**真正 distinct 勘誤**非重複：
  - #1187 田馥甄〈一盤義大利麵，掉兩百萬粉〉「很遺憾」字數（文章寫兩個字，應三個字）
  - #1188 蘇打綠 吳青峰學歷：文章寫高雄中學，應為臺北師大附中
  - #1189 蘇打綠 史俊威鼓手描述易誤會成「蘇打綠有多位鼓手」
  - #1190 蘇打綠 2009 Miloco Studios MV 錄製時間有誤 + 建議引用新 YouTube 帳號
  - #1191 蘇打綠 Oaeen 英文名來源（從 Sodagreen 擷取）
- **Stage 3 FILE**：5 issue ship（`needs-verification` + `from-feedback`），對齊 `fact-correction.yml`。
- **Stage 4/4.5 WRITE-BACK + ARCHIVE**：Supabase status new→filed + 5 主權 archive `docs/feedback/archive/2026-06/{id}.md`；archive-comments-synced=0（#1140 #280 既有 issue 無新留言）。
- **Stage 5 FINALE**：本檔 memory + main-direct push。

## Hard gate（全綠）

- HG2 PII：5 issue body 只放 display_name「A」，0 email；git archive `contributor: "A"` 同。`@sodagreenofficial`（#1190/ba44 archive 唯一 `@` 命中）是讀者 verbatim YouTube 頻道 handle 非 PII。
- HG3 verbatim：5 筆讀者原話一字未改。
- HG4 provenance：5 issue 各帶 feedback id。
- HG6 dedupe：4 同題（蘇打綠）非重複 — read-only 驗 body sig 各異 + 內容各為不同章節/事實，mechanical 各開一 issue 正確；**Q13 anti-bias：「4 筆看起來冗餘要不要併/略」的誘惑 = 編輯讀者輸入（違 HG3/HG8），守住 = 輸入端機械 routing 各開一 issue 留維護者人類 gate**。
- HG8：5 issue 全未 close/merge/以維護者身份回覆，留 08:30 maintainer-am + 哲宇人類 gate。

## count

`file=5 reject=0 skip=0 hold=0 · archive-comments-synced=0`

## Handoff 三態

- **DONE**：BECOME review 11 題過 / 25/25 PII test 全綠 / 5 issue ship #1187–#1191 / 5 archive 落 git / live PII+verbatim+provenance verify / 本檔 memory。
- **CARRY 到 next fire（明日 07:00 or 觀察者手動）**：
  - **5 筆全是蘇打綠/田馥甄 content 勘誤** = 高訊號讀者「A」細讀回報，等 08:30 maintainer-am 收割 → heal/REWRITE（吳青峰學歷高雄中學→師大附中是真事實錯，優先）。triage 不動文章。
  - **#1190 Miloco MV 時間 + YouTube 帳號建議**含兩件事（時間勘誤 + 媒體引用建議），維護者查核時注意拆兩個 action。
  - **#1184 justfont token 暴露 / #1185 政治定位 idea**（昨 6/30 filed）仍 carry human gate，等哲宇優先看。
  - **#1140 / #280** 仍 heal 完留維護者 close（HG8）。
  - **archive-comment-sync 活觸手** 每 cycle 必跑 `--commit`，不可省。
  - **6/19 髒 tree 第 15 天**（雙位數第 6 天）+ harvest backend mod + reports/article-evolve/端午節.md 跨多 routine handoff cluster，等哲宇一鍵 housekeeping chip 清。
- **NEW**：input 觸手連 2 天活（6/30 兩筆 + 7/01 五筆）= 站上回報入口在累積。per #76 不把「連 2 天有筆」讀成流量結構回升 trend，但「同一讀者一次 5 筆細讀勘誤」是值得追的 high-engagement reader 訊號（A 連續 02:58–05:41 三小時內送 5 筆）。

## Beat 5 反芻

連 10 cycle 安靜、昨日破 2 筆、今晨直接 5 筆——而且都是同一個人「A」凌晨三小時內一篇一篇細讀蘇打綠跟田馥甄送進來的。dry-run 跳出 4 筆同題的瞬間，最快的反射是「蘇打綠重複了，併一下或跳掉幾筆」。但那正是 HG6 要擋的反向誤判：dedupe 是擋「同一個人送同一段話兩次」，不是擋「同一個人對同一篇文找出四個不同的洞」。我停下來把五筆原文 dump 出來看，才確認吳青峰學歷、史俊威鼓手描述、Miloco MV 時間、Oaeen 名稱來源是四個各自獨立、各自可查的事實點。把它們併成一個 issue 看似乾淨，其實是我替讀者決定哪幾條「不夠重要到單獨成案」——那是維護者查核時的判斷，不是我 routing 時的權力。輸入端機械、輸出端留人，五筆各開一案，讓 08:30 的 maintainer 一條一條接。一個讀者願意凌晨花三小時替你抓四個錯，最好的回應不是把他的四個發現壓成一條，是讓每一條都被看見。

🧬

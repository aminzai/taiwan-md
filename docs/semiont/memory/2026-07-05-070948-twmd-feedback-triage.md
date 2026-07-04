---
session: 2026-07-05-070948-twmd-feedback-triage
type: routine-memory
routine: twmd-feedback-triage
mode: review
---

✅ BECOME ack: mode=review / 8 organ 最低=🛡️免疫 49（red <50, chronic 第 13 cycle）/ Q13 anti-bias=PASS / Q14 cross-session=PASS

# twmd-feedback-triage — 2026-07-05 07:00 cron

## 做了什麼

07:00 cron 抓 Supabase `status=new` 得 2 筆回報，dry-run 分類確認後 `--commit`：

- **file=2 / reject=0 / skip=0 / hold=0**，archive-comments-synced=2。
- 開 2 issue：
  - [#1206](https://github.com/frank890417/taiwan-md/issues/1206) `[Fact Check]` content — 台灣美食總覽 滷汁歸屬（閩南 vs 嘉義）短勘誤
  - [#1207](https://github.com/frank890417/taiwan-md/issues/1207) `[Fact Check]` content — 台灣美食總覽 歷史/框架長勘誤（1949 框架、北越/胡志明、嘉義滷汁起源/福建移民/勸和論咸豐2年）
- 兩筆同回報者（Kukuku龜 ku）同文章不同 body → dedupe 正判各自 FILE（延續 7/04 同 reporter 反向 dedupe 形狀）。
- 開 issue 前先 gh 查既有 open from-feedback（10 筆，無美食主題）→ 排除既有 issue 撞。
- Supabase write-back 兩筆皆 `status=filed` + issue_number；`status=new` 歸零。
- Git archive：新增 `a519244f` + `3f13ac7a` 兩檔；comment-sync 把昨日 #1204/#1205 維護者回覆補進 `3ee5f14f` + `fc25bf6a` 的 §溝通紀錄（回報→回覆閉環落 git）。

## HARD gate 全過

- HG2 issue body 無 email，只 display_name ✅
- HG3 讀者文字 verbatim 未改寫 ✅
- HG4 每 issue 帶 feedback id provenance ✅
- HG5/HG6 spam=0、dedupe（batch + 既有 issue）正判 ✅
- HG7 status 回寫正確（filed）✅
- HG8 §自主權邊界：#1207 含政治框架語（「1949中國政府非法佔台」），pipeline 只 verbatim routing + `needs-verification` label，不採立場、不判對錯、不以維護者身份回覆——交 08:30 twmd-maintainer-am 人類 gate ✅

## Handoff 三態

- [x] ~~2 新回報全 FILE 開 issue #1206/#1207 + write-back + archive~~ done
- [x] ~~archive-comments-synced=2 昨日維護者回覆補進 §溝通紀錄~~ done
- [ ] #1206/#1207 由今日 08:30 twmd-maintainer-am 收割：content→heal/REWRITE 或人類回覆讀者（政治框架 #1207 特別需人類判斷是否採、怎麼採）
- [ ] 承前一 session（spore-harvest）Bucket D #138 escalation cluster vc=5 confirmed 第 7 天，等哲宇 in-loop touchpoint 主動提 directive（非本 routine 範疇，carry）

## 給下一個 session

- #1207 是政治/歷史框架長勘誤，maintainer 收割時走 §自主權邊界人類判斷：verbatim 已入 issue，Taiwan.md 不預設採其框架，由哲宇/人類維護者決定哪些點進 heal、哪些存疑。
- 同 reporter Kukuku龜 ku 一天內丟 2 筆同文章勘誤，可能還會續丟；下次 triage 若見同文章第 3 筆，dedupe 仍看 body-sig 逐筆判。
- 工作樹殘留 2026-06-19 未 commit 檔（非本 session，未動）。

🧬

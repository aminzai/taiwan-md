# Feedback archive — 讀者回報的 git 主權層

> 為什麼有這層：feedback 的 **live 資料**在外掛 BaaS（Supabase），但 **canonical 紀錄**要留在 git。
> per MANIFESTO「知識在 git 不在黑箱 / 分散式不可殺滅」。Supabase 哪天消失、被鎖、降級，
> 所有讀者回報 + 維護者溝通仍完整躺在這個 repo 的 markdown 裡：可 `git log`、可 diff、可 grep、可匯出。

## 怎麼運作

`twmd-feedback-triage` routine 每次跑（`scripts/feedback/triage.mjs --commit`）：

1. 讀 Supabase `status='new'` 回報 → 分類 → 開 GitHub issue。
2. **同時把每筆回報寫成 `archive/{YYYY-MM}/{feedback_id}.md`**（append-only）。
3. **掃既有 archive，把對應 issue 的新留言（含維護者回覆）sync 進該檔的 `## 溝通紀錄`**。
4. routine 收官時 `git add docs/feedback/archive/ && commit && push` → 紀錄進 git。

## 一筆紀錄存什麼

frontmatter：`feedback_id / created_at / contributor / type / status / page_kind /
article_slug / lang / source_url / issue_url / issue_number`
body：回報內容、選取的原文（quote）、正確資訊+來源、系統初判（triage_note）、`## 溝通紀錄`（issue 留言）。

## 這層的範圍：對 `filed` 完整，對「到達」不完整

**拿這批檔案算讀者到達節奏會得到偏大的間隔。** Stage 4 的 reject 分支只回寫 Supabase
`status='rejected'`、**不寫 archive**（設計如此，不讓 spam 文字進 git），所以被判 spam 的那些
回報是真的到達過、卻沒在 git 留下痕跡。用 archive 算「上一筆到下一筆隔幾天」，等於在算
**勘誤之間的間隔**，不是**讀者到達之間的間隔**，而缺的那幾筆只會讓間隔看起來更長——長相是
「讀者比實際更安靜」，方向固定，且沒有任何閘門會響。

實例（2026-09-29）：archive 87 筆算出歷史最長間隔 15.94 天（07-04 → 07-20），全庫 90 筆
（87 filed + 3 rejected）算出來是 12.65 天——一筆 rejected 落在 07-11 把那個窗切成兩半。

**要問到達節奏就去問 Supabase 全 status**（`triage.mjs` 本來就握著那個讀取權，
`formatIntakeAge()` 也是這樣取的），不要從這層推。詳見
[LESSONS-INBOX `requery-with-a-new-shape-can-swap-the-population-not-just-the-window`](../semiont/LESSONS-INBOX.md)。

## PII 鐵律

- **只存 `contributor`（display_name = 暱稱/回退名，已公開在 issue 的）。永遠不存 email。**
  email 只在 Supabase `profiles` 表（私有），不進 git、不進 public issue。
- 對應 [reports/feedback-login-system-design-2026-06-01.md](../../reports/feedback-login-system-design-2026-06-01.md) §v3 + 第三階段。

完整流程：[docs/pipelines/FEEDBACK-TRIAGE-PIPELINE.md](../pipelines/FEEDBACK-TRIAGE-PIPELINE.md)。
記錄產生邏輯：[scripts/feedback/lib/archive.mjs](../../scripts/feedback/lib/archive.mjs)（純函式 + unit test）。

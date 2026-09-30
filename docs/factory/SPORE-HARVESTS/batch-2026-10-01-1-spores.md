---
spores: '#29'
harvest_date: '2026-10-01 06:42'
harvest_window_day: 'D+170'
batch_reason: 'daily audience flywheel — 窗口內沒有孢子（最新 #175／#176 已 D+39）；動態頁上 #29 李洋按讚聚合到「1.5 萬」，照 09-27 起交接寫死的零判斷條件打開 permalink 重抓數字'
triggered_by: 'cron (twmd-spore-harvest-am)'
reply_count: '0 unanswered — 回覆分頁沒有 09-07 之後的新列，#29 留言數仍是 227'
---

# batch-2026-10-01-1-spores — 李洋那支按讚聚合到 1.5 萬，四天多了一百次分享

## 為什麼打開這一支

`dashboard-spores.json` 的 `backfillWarnings` 0 條，`spore-log.json` 最新仍是 08-23 的 #175／#176（D+39），窗口內沒有孢子。

09-27 那班把 #29 的下一個重抓門檻寫成「聚合到 1.5 萬」。今天 `/activity` 第一列是「ssg7366 和另外 1.5 萬人」（09-30 22:02 UTC，按讚），條件成立。

## 開場前的環境

`list_connected_browsers` 第一次回 `[]`。照交接先查，Chrome 以 `--no-startup-window` 在跑；`open -a "Google Chrome"` 後等 8 秒重探，回 deviceId `6a0a1276`。跟 09-23 是同一個原因、同一個修法，沒有升級。

## 動態頁掃描結果

| 分頁                | 看到什麼                                                                                                                                                 | 分桶 | 處置                |
| ------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- | ------------------- |
| `/activity/replies` | 2 則，逐則對 `time[datetime]`：09-07 euroholicgirl（#29）、09-02 yangjottawa（張懸），都是前幾班看過的；分頁標題「(3) 動態」、個人檔案連結在，登入態通過 | —    | 0 新留言            |
| `/activity`         | 昨天那班之後三筆新事件，全是按讚：#29 李洋聚合 1.5 萬、雙胞胎記帳本孢子「moonhoney 和另外 2 人」、安溥女巫店那支 pheebshsu 單讚                          | —    | 只有 #29 過開啟門檻 |

沒有 A／B／C／D 桶。**0 ship**，Pitfall 6 retry count = N/A。

## #29 重抓（寫進 spore-metrics.json）

從 `/activity` 那一列座標點進去，落在 canonical `/@taiwandotmd/post/DXGuAudkbuC`（v3.2 進場順序第四輪有效）。

| #   | Slug | Platform | D+N   | Views   | Likes  | Reposts | Comments | Shares | 上次紀錄（09-27 D+166）        |
| --- | ---- | -------- | ----- | ------- | ------ | ------- | -------- | ------ | ------------------------------ |
| 29  | 李洋 | Threads  | D+170 | 350,000 | 31,000 | 1,125   | 227      | 632    | 350K / 31K / 1,122 / 227 / 530 |

四天裡分享從 530 跳到 632（+102），轉發 +3，留言沒動。前一段 09-18→09-27 九天分享只 +1，這次的量是另一個量級：有人在把這支五個月前的孢子往外傳（私訊或站外），但 Threads 的分享計數看不出傳到哪裡。views 與 likes 仍卡在 UI 的四捨五入（35 萬、3.1 萬）。

留言數 227 跟上次相同，所以本輪沒切「全部＋最新」排序去翻；09-27 記下的兩則位置不明的留言仍是缺口。

## 衍生層

`spore-db.py add-metrics` 一筆 → `generate-spore-records.py` + `generate-dashboard-spores.py` 重生 → `validate-spore-data.py`。文章檔案不動。

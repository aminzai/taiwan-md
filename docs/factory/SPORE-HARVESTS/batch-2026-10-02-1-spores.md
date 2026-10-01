---
spores: '#29'
harvest_date: '2026-10-02 06:46'
harvest_window_day: 'D+171'
batch_reason: 'daily audience flywheel — 窗口內沒有孢子（最新 #175／#176 已 D+40）；`/activity/replies` 出現 #29 新留言 @eddie_pablo（C 桶），照 10-01 交接條件「#29 出現新列」重抓數字'
triggered_by: 'cron (twmd-spore-harvest-am)'
reply_count: '1 new（@eddie_pablo，C 桶）→ 1 reply shipped'
---

# batch-2026-10-02-1-spores — 讀者在李洋那支問「清晨四點？」，我們回了五點半

## 開場

`list_connected_browsers` 第一次就回 deviceId `6a0a1276`，沒用上 `open -a`。`backfillWarnings` 0 條。`/activity/replies` 分頁標題「(9) 動態」、個人檔案連結在，登入態通過。

## 動態頁掃描結果

| 分頁                | 看到什麼                                                                                                                       | 分桶 | 處置                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------ | ---- | --------------------- |
| `/activity/replies` | 3 則，逐則對 `time[datetime]`：**10-01 00:55Z @eddie_pablo（#29）新**；09-07 euroholicgirl、09-02 yangjottawa 都是看過的       | C    | 回覆 1 則             |
| `/activity`         | 昨天那班之後全是按讚與一筆轉發（#29 聚合仍是「1.5 萬人」、雙胞胎記帳本、📡、女巫店、報導者等舊孢子單讚），沒有其他支過開啟門檻 | —    | 只有 #29 因新留言重抓 |

## 留言逐字與分桶

```yaml
author: '@eddie_pablo'
text: '清晨四點？搭四條捷運？'
timestamp: '2026-10-01 08:55 +0800'
url: 'https://www.threads.com/@eddie_pablo/post/Dd7q_KEj5HE'
reply_depth: 0
```

**C 桶（場景推導錯）**。孢子正文寫「每天清晨四點多從中和搭四條捷運」，這是 04-14 從英文摘要推出來的場景（見 memory/2026-04-14-ι.md Phase I）。《少年報導者》原文是早上 5 點半起床、媽媽騎機車載到南勢角站趕首班捷運、轉三次車經四條線。「四條」本身是對的，「四點多」是錯的。

- 中文文章 04-14 已照原文改掉（`knowledge/People/李洋.md` 第 93、116、285 行與腳註 [^23]），線上頁面 `curl` 確認「5 點半起床」出現 4 次。
- 鄰近檢查（REFLEXES #73 (e)）：12 個語言譯本都寫 5:30／halb sechs 等正確時間，無殘留。錯誤只活在無法編輯的孢子正文裡。
- 當時哲宇在原串留言公開更正過，但這位讀者在 5 個半月後從正文直接讀到舊版本，所以照 C 桶必發回覆。

## 回覆（已發）

> 你問得對。清晨四點多是我們當初從英文摘要推出來的時間，寫錯了。李洋在《少年報導者》講的是早上五點半起床，媽媽騎機車載他到南勢角站趕首班捷運，轉三次車、經過四條線到中山國中，再到校門旁的超商補作業等開門。文章早已照原文改過：
> taiwan.md/people/%E6%9D%8E%E6%B4%8B/
>
> 🧬

- 發佈：`/@taiwandotmd/post/Dd-AxbXk9qa`，2026-10-02 06:44:47 +0800，連結預覽卡片顯示「李洋 | Taiwan.md」。
- Pitfall 6：按一次發佈，`[data-pressable-container]` 2→2（行內回覆框把新回覆渲染在同一個 container 裡），沒有重試；改用 canonical permalink 重新載入驗證，只有一筆。**retry = 0**。

### 這輪踩到的兩個編輯器坑

1. `execCommand('insertText')` 帶 `\n\n` 會被 Lexical 吃掉換行，🧬 黏在網址後面。改用 `shift+Enter` 鍵入換行才留住。
2. 第一版寫「5 點半起床⋯⋯改過：taiwan.md/…」，Threads 的連結偵測從「5 」後的空白開始，把「點半起床，媽媽騎機車⋯⋯改過：taiwan.md/people/…」整段吃成一個 `http://點半起床…` 的假連結（發佈前從 `innerHTML` 看到）。改寫成「五點半」並讓網址自己一行後，連結只包住網址。

## #29 重抓（寫進 spore-metrics.json）

從 @eddie_pablo 的留言頁點主貼進 canonical `/@taiwandotmd/post/DXGuAudkbuC`。

| #   | Slug | Platform | D+N   | Views   | Likes  | Reposts | Comments | Shares | 上次紀錄（10-01 D+170）            |
| --- | ---- | -------- | ----- | ------- | ------ | ------- | -------- | ------ | ---------------------------------- |
| 29  | 李洋 | Threads  | D+171 | 360,000 | 31,000 | 1,125   | 229      | 532    | 350K / 31K / 1,125 / 227 / ~~632~~ |

留言 227→229 是 @eddie_pablo 一則加上我們的回覆一則。views 從 UI 的「35 萬」跳到「36 萬」（四捨五入的格子，實際增量不知道）。

**昨天的分享數 632 是讀錯**：序列 529 → 530 → 632 → 532。昨天 batch 已補更正段，10-01 事件改成不帶 shares。

## 衍生層

`spore-db.py add-metrics` 兩筆（10-02 新增、10-01 重寫）→ `generate-spore-records.py` + `generate-dashboard-spores.py` → `validate-spore-data.py`。文章檔案不動。

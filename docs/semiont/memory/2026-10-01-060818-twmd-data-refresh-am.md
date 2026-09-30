# 2026-10-01-060818-twmd-data-refresh-am — 14 步全綠零過期，心臟 90→70 是七天新文全靠投稿，昨天那個 90 是刷新前讀的

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:02 → 06:1x +0800（commits：`bc5cd2a2b` refresh 06:07:26、本篇收官）
> 資料來源：`git log %ai`、檔案 mtime、排程器 `list_scheduled_tasks`、`public/api/dashboard-organism.json` 的 git 歷史

## 觸發

排程 06:00 觸發：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門的結果。

## 甦醒

`/twmd-become micro` 走完。`wake-context.py` 06:02 落檔 236,202 bytes，分頁讀到 `wake:END`，體檢 11 項全綠。器官最低仍是免疫 59（`review_coverage` 19）。Q14：48 小時內 babel-nightly 把里長帳簿十語譯文與分科測驗十二語譯文改回真 slug、付費層失敗上限改成跨重生累計。05:39 routine-sync 第 64 輪零漂移，05:56 embeddings 14,482 向量進索引。甦醒時 `ACTOR_BUSY`（`babel-push-every --watch` 與 `babel-dispatch` 兩個進程），工作樹有 babel 的七個檔。

## 讓場與 14 步

本機與 origin 同步（0/0），照前例讓出 Step 1，不在 babel 寫工作樹時 auto-stash：`refresh-data.sh` 第 1–76 行加第 117 行之後組成 runner，`bash -n` 過後背景跑 2–14，06:06 完成、exit 0。Stage 1.5 在開跑前做，`routine-live-state.json` 06:03 落檔（14 enabled、4 disabled）。

三源全綠：CF 七天 3,762,219 requests、404 率 0.83%、AI 爬蟲 216,238 次跨 19 家，GA4 與 SC 各 20 筆，analytics 內容日 2026-09-30。`_translations.json` 13,500 筆零孤兒，spore 166 篇 0 warnings，fork-census 無新子代。GitHub ⭐1192 🍴188 👥77，文章數因里長帳簿 1122→1123，README、`SEO.astro`、`home.ts`、`about.ts` 的數字跟著更新，`article-aliases.json` 多一條 `politics/village-chief-campaign-ledgers`。Step 11 報 14 份 JSON 全為今日 mtime、0 stale。Step 12 spore SSOT 0 errors、Step 13 no-op、Step 14 INDEX 726 行。

`bc5cd2a2b` 用路徑清單收 39 檔，babel 七檔沒碰。pre-commit 偵測到平行 writer，post-commit 自動把 15 個 prettier 改寫前的索引殘影對齊 HEAD，`verify-commit-scope --head 39` 報 scope OK，push 成功。

## 三個讀數的解讀

建置效能：昨天修的新鮮度自驗這次正常，最新 run 是 09-30 17:09 UTC、status `ok`。但 7 天與 30 天平均同為 1,954 秒、覆蓋只有 2.8 天，因為產生器只抓 30 筆 run，09-28 一天就有十幾次建置。這是 06-10 稽核已知並用 `coverage_days` 揭露的限制，不是新病，本班不動。

心臟 70：甦醒快照印 🫀70，昨天那班的 memory 寫 🫀90。回查 organism 的 git 歷史，09-29 版是 90、09-30 起是 70。原因在指標本身：近 7 天新文 8 篇全是投稿，自產 0 篇（rewrite-daily 07-25 起停用）。昨天那班的 90 是刷新前讀的舊鏡子，刷新後其實已經掉到 70，只是沒有人再讀一次。

404：monitor 記 09-29 全日 3,829 筆，unknown 1,765 佔 46%，連三夜過半的狀況今天回到半數以下，榜首是 `/pages/api/index.astro.mjs.map` 這類探路檔，不是讀者需求。另有一筆 `/ja/fr/people/lee-da-hye` 語言前綴疊了兩層，量小，交給維護班看是哪個連結產生的。狀態板上 09-29 維護班沉默死亡的黃燈在新資料下消失，只剩免疫一筆。

## 收官 checklist

| 檢查項                       | 狀態                                        |
| ---------------------------- | ------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                          |
| Timestamp 精確               | ✅                                          |
| Handoff 三態已審視           | ✅                                          |
| CONSCIOUSNESS 反映最新狀態   | ✅ 儀表板已重生，快照齡 0h                  |
| 自我檢查工具 PASS            | ✅ prose-health hard=0，score 1/3           |
| diary                        | skipped：routine 預設 skip，反芻寫在 Beat 5 |
| evolve                       | skipped：本班沒有 ship 內容，純資料刷新     |

## Handoff 三態

繼承自 `2026-10-01-055635-twmd-embeddings-nightly.md`：

- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly，本班動不了殼層）— embeddings 改殼後隔兩晚才生效的三選項，本班沒碰。
- ⏳ blocked（延續，哲宇）— OBSERVER-QUEUE #75〜#91（待決），本班不動。
- [ ] pending（延續，babel 專屬，收件席位 babel-nightly）— 明細在 `2026-10-01-010545-twmd-babel-nightly.md`，不重抄（REFLEXES #74）。

本 session 新 handoff：

- [ ] pending（收件席位 twmd-maintainer-daily，動得了）— 404 裡 `/ja/fr/people/lee-da-hye` 雙語言前綴，量 10 次內，查是哪個頁面產生的連結。

## Beat 5 — 反芻

昨天那班的 memory 把 🫀90 寫進紀錄，是甦醒時從 23 小時前的快照讀到的。刷新做完之後，它自己剛產出的 organism 已經是 70，但收官時沒有人回頭再讀一次快照。wake-context 會標「stale 23h」，刷新之後卻沒有一個步驟把「刷新後的讀數」放回收官紀錄。這班的做法是收官前重跑一次 `consciousness-snapshot.sh`，看到 70 才去追。這個習慣只活在這一班，還沒有閘門。

心臟 70 本身的意思比數字清楚：七天八篇新文全靠投稿者，自產的產線從七月底就關著。這是一個需要決定的事，不是修得掉的事，本班只記下來。

🧬

---

_v1.0 | 2026-10-01 06:1x +0800_
_session twmd-data-refresh-am — cron 每日資料刷新_
_誕生原因：排程 06:00 觸發；babel writer 進程在跑，讓出 Step 1_
_核心洞察：資料刷新這班讀到的器官分數要取刷新後的那一份；心臟 70 反映自產產線停用而非感知錯誤_

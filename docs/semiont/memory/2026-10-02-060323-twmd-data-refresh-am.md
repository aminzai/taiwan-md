# 2026-10-02-060323-twmd-data-refresh-am — 14 步全綠零過期；心臟 70→90 不是多了新文，是巡邏修補被算成投稿

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:01 → 06:2x +0800（commits：`4809cf4f6` refresh、本篇收官）
> 資料來源：`git log`、`public/api/dashboard-organism.json`、`scripts/core/generate-dashboard-data.js`、排程器 `list_scheduled_tasks`

## 觸發

排程 06:00 觸發：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門的結果。

## 甦醒

✅ BECOME ack: mode=micro / 8 organ 最低=🛡️ 免疫 59（`review_coverage` 19）/ Q14 cross-session continuity=PASS。

`wake-context.py` 落檔 241,376 bytes，分頁讀到 `wake:END`，體檢全綠。Q14：48 小時內三輪心跳巡邏修了七篇（社會住宅、5G、社會運動、里文化、早餐店、教育制度、媒體自由等），32 篇 hi／ar 結尾漂成韓文的譯文降級重譯；babel-nightly 把修過的六篇推到十二語；05:39 routine-sync 第 65 輪零漂移；06:02 embeddings 重建後本機領先 origin 一個 commit。甦醒時 `ACTOR_BUSY`：`babel-dispatch` 與六支 translate 進程正在寫 ar／de／ja／ko 譯文，工作樹有 babel 的三十多個檔。

## 讓場與 14 步

本機落後 origin 0 個 commit，照前兩班的做法讓出 Step 1，不在 babel 寫工作樹時 auto-stash：`refresh-data.sh` 第 1–76 行接第 117 行之後組成 runner，`bash -n` 過後背景跑 2–14，exit 0。Stage 1.5 在開跑前做，`routine-live-state.json` 落檔 14 enabled、4 disabled。

| Step             | 結果                                                                                                                                   |
| ---------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| 1 git sync       | SKIP（babel 在寫，HEAD 0 behind）                                                                                                      |
| 2 三源感知       | PASS：CF 七天 3,905,440 requests、404 率 0.77%、AI 爬蟲 203,875 次跨 19 家；GA4 topPages／topArticles7d 各 20；SC 20 queries＋150 詞雲 |
| 2.5 404 監測     | PASS：09-30 全日 3,922 筆，unknown 2,607，no alerts                                                                                    |
| 3 translations   | PASS：13,500 筆，0 孤兒                                                                                                                |
| 4 spores         | PASS：166 篇，0 warnings                                                                                                               |
| 5 i18n           | PASS                                                                                                                                   |
| 6 immune         | PASS：59，最大缺口 review_coverage 19                                                                                                  |
| 6.5 fork-census  | PASS：無新子代                                                                                                                         |
| 6.6 status       | PASS：routines 18（14 operational）、babel 12 語 gap 0                                                                                 |
| 7 prebuild       | PASS                                                                                                                                   |
| 8 llms.txt       | PASS：十三語各 1123                                                                                                                    |
| 9 stats          | PASS：⭐1194 🍴188 👥77 📄1123                                                                                                         |
| 10 build-perf    | PASS：status ok，最新 1957 秒、7 日平均 1917 秒（覆蓋 3.4 天）                                                                         |
| 10b newsroom     | PASS：171 篇上板                                                                                                                       |
| 11 freshness     | PASS：14 份全為今日，analytics 內容日 10-01，0 stale                                                                                   |
| 12 spore 驗證    | PASS：0 errors                                                                                                                         |
| 13 sporeLinks    | PASS：無變動                                                                                                                           |
| 14 reports INDEX | PASS：726 行                                                                                                                           |

`4809cf4f6` 用路徑清單收 36 檔，babel 的 `_translation-status.json`、`babel-live.json`、`reports/babel/*` 與各語譯文都沒碰。post-commit 把 15 個索引殘影對齊 HEAD，`verify-commit-scope --head 36` 報 scope OK，push 成功。

## 心臟 70→90 是怎麼來的

收官前重跑 `consciousness-snapshot.sh`（照昨天那班的做法取刷新後讀數），心臟從 70 跳到 90，文章總數卻還是 1123。organism 的 metrics 寫 `articlesLast7Days` 15、`selfProducedLast7Days` 0、`contributedLast7Days` 15。回查 `generate-dashboard-data.js` 第 742 行：這個數用 `lastModified` 過濾，量的是「七天內被改過的文章」。昨天到今天多出來的七篇，對得上三輪心跳巡邏的 heal commit。

所以有兩層混在一起。第一層：修補跟新進庫用同一個計數，心臟分數跟著巡邏次數起伏。第二層：投稿數是「被改過的」扣掉 ARTICLE-DONE-LOG 自產數，Semiont 自己修的文章被記成投稿。昨天那班寫「七天八篇新文全靠投稿、自產為零」，那個 8 本身就不全是新文。

改心臟公式是閾值調整，不在這班的範圍。登記進 LESSONS-INBOX `heart-counts-heals-as-contributed-births`，附「先用 30 天真實資料比較新舊分數」的機械化候選。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅                                            |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅ 儀表板已重生，快照齡 0h                    |
| 自我檢查工具 PASS            | 見 commit 時 prose-health                     |
| diary                        | skipped：routine 預設 skip，反芻寫在 Beat 5   |
| evolve                       | skipped：本班只刷新資料，教訓進 LESSONS-INBOX |

## Handoff 三態

繼承自 `2026-10-02-053905-twmd-routine-sync.md` 與昨天本班：

- ⏳ blocked（延續）：routine-sync 系列五條 pending 各有席位（self-evolve-weekly 10-04／`/twmd-routine`／routine-audit-weekly），本班不碰，明細不重抄（REFLEXES #74）。
- ⏳ blocked（延續，哲宇）：OBSERVER-QUEUE 待決項，本班不動。
- [ ] pending（延續，收件席位 twmd-maintainer-daily）：404 裡的雙語言前綴，今天的代表路徑換成 `/ja/fr/culture/taiwan-street-art-and-...`，歸在 untranslated-demand 7 筆。昨天那條 `/ja/fr/people/lee-da-hye` 還沒有人查。

本 session 新 handoff：

- [ ] pending（收件席位 twmd-self-evolve-weekly 10-04，或哲宇）：LESSONS-INBOX `heart-counts-heals-as-contributed-births`，心臟格分出「新進庫」與「有更新」。動公式前要先比對真實資料。

## Beat 5 — 反芻

昨天那班發現自己前一天讀的是刷新前的舊快照，所以今天刷新後重讀了一次，這一步才讓 90 被看到。但重讀只解決「讀的是不是最新」，解決不了「這個數在量什麼」。70 跟 90 都是新鮮的讀數，兩個都準確反映了公式的輸出，公式量的卻是修改次數。昨天把 8 解讀成「八篇新文全靠投稿」，今天差點把 15 解讀成「投稿變多了」。數字變新鮮，不代表解讀就跟著對了；要回頭看那一行 filter 才知道它在數什麼。

🧬

---

_v1.0 | 2026-10-02 06:2x +0800_
_session twmd-data-refresh-am — cron 每日資料刷新_
_誕生原因：排程 06:00 觸發；babel writer 進程在跑，讓出 Step 1_
_核心洞察：心臟的近七天文章數量的是修改日期，巡邏修補被算成投稿進庫_

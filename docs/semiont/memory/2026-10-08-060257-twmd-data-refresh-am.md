# 2026-10-08-060257-twmd-data-refresh-am — 額度停擺後第一次刷新，五天前的舊鏡子換成今天，新出現的 404 形狀是外部爬蟲自己拼的前綴

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:01 → 06:14 +0800（commits：`03e2d38ea` refresh 06:10:10、本篇收官）
> 資料來源：`git log %ai`、`public/api/dashboard-*.json`、`reports/404-monitor/`、排程器 `list_scheduled_tasks`

## 觸發

排程 06:00 觸發：跑 14 步資料刷新、把排程器即時狀態落檔、處理 Step 11 新鮮度閘門的結果。這是 10-03 之後第一個真的跑起來的早班。

## 甦醒

✅ BECOME ack: mode=micro / 8 organ 最低=🛡️ 免疫 59（`review_coverage` 19）/ Q14 cross-session continuity=PASS。

`wake-context.py` 落檔 236,381 bytes，分頁讀到 `wake:END`，selftest 全綠，只有 groundtruth 印「快照齡 119h」：儀表板停在 10-02 22:06。Q14：週額度在 10-03 用完，飛輪全黑 87 小時，10-07 20:34 心跳登記成 OBSERVER-QUEUE #93 並造了額度記帳工具。之後 babel 夜班把十二語缺口清到零、補了量級閘門，02:36 心跳巡邏〈台東縣〉與〈台灣捷運發展史〉，05:39 routine-sync 第 67 輪零漂移，05:59 embeddings 重建 0 fail。觀察者缺席第 12 天。甦醒時 `ACTOR_BUSY`：babel 的三個寫入進程在跑，工作樹有它的檔。

## 讓場與 14 步

本機與 origin 0 前 0 後，照 10-03 那班的做法讓出 Step 1，不在 babel 寫工作樹時 auto-stash：`refresh-data.sh` 第 1–76 行接第 117 行之後組成 runner（行界逐行對過仍準），`bash -n` 過後背景跑 2–14，exit 0。Stage 1.5 在開跑前做，`routine-live-state.json` 落檔 14 enabled、4 disabled，過濾 0 條私人 routine。

| Step             | 結果                                                                                               |
| ---------------- | -------------------------------------------------------------------------------------------------- |
| 1 git sync       | SKIP（babel 在寫，HEAD 0 behind）                                                                  |
| 2 三源感知       | PASS：CF 七天 3,126,906 requests、404 率 2.34%、AI 爬蟲 339,711 次跨 18 家；GA4 20／20；SC 20＋150 |
| 2.5 404 監測     | PASS：10-06 全日 9,035 筆（unknown 6,761、scanner 1,081、bad-encoding 515），no alerts             |
| 3 translations   | PASS：13,500 筆，0 孤兒                                                                            |
| 4 spores         | PASS：166 篇，0 warnings                                                                           |
| 5 i18n           | PASS                                                                                               |
| 6 immune         | PASS：60，最大缺口 review_coverage 19                                                              |
| 6.5 fork-census  | PASS：無新子代                                                                                     |
| 6.6 status       | PASS：routines 18（down 4、degraded 7），babel 12 語                                               |
| 7 prebuild       | PASS（redirects 233 條）                                                                           |
| 8 llms.txt       | PASS：十三語各 1123，contributors 78                                                               |
| 9 stats          | PASS：⭐1199 🍴187 👥78 📄1123                                                                     |
| 10 build-perf    | PASS：最新 1882 秒、7 日平均 1962 秒（覆蓋 6.1 天），ms/page 106 超過 50 門檻                      |
| 10b newsroom     | PASS：190 篇上板，warnings 17                                                                      |
| 11 freshness     | PASS：14 份全為今日，analytics 內容日 10-07，0 stale                                               |
| 12 spore 驗證    | PASS：0 errors                                                                                     |
| 13 sporeLinks    | PASS：無變動                                                                                       |
| 14 reports INDEX | PASS：726 行                                                                                       |

Step 11 零過期，catch ≠ fix 鐵律本班沒有觸發對象。`03e2d38ea` 用路徑清單收 37 檔，比 10-03 那班多 `src/i18n/about.ts` 一份（update-stats 寫星數與貢獻者數，設計內）；babel 的 `_translation-status.json`、`babel-live.json`、`reports/babel/*` 與各語言譯文都沒碰。post-commit 把 15 個索引殘影對齊 HEAD，`verify-commit-scope --head 37` 報 scope OK，push 成功，origin 0 落差。收官前重跑 snapshot，快照齡 0 小時。

## 狀態板的四條 down、七條 degraded 是停擺的影子

`dashboard-status.json` 列了八則「沉默死亡」黃燈，逐條對過 fire 時間：全部落在 10-03 晚到 10-07 之間，跟 #93 的額度停擺窗口重合（排程器照時間 fire、session 起不來，跟 09-05 停電報告寫的 `lastRunAt` 先寫入是同一個機制）。週日那四條（news-lens、weekly-report、distill、self-evolve）下一班是 10-11，本班自己這格的 down 會在這次刷新後轉回 fired。沒有新病，不另開條目。

DNA 分數 95→80 也一樣有解：02:36 心跳已把這格改標「最近修改天數」，它量的是 EDITORIAL 多久沒改，數字掉是時鐘在走。

## 404 率三倍，多出來的一塊是外部拼出來的雙前綴

CF 404 率從 10-03 的 0.74% 升到 2.34%，404 監測 10-06 單日 9,035 筆，是前一週日均三千多的兩到三倍，主要漲在 unknown。翻 top paths 看到一個新形狀：語言前綴重複兩次而且中間沒有斜線（`/ptpt/people/...`、`/hihi/...`、`/arar/...`、`/eses/...`）。這跟 10-02 maintainer 退役的 `/ko/fr/` 雙前綴是不同的簽名。量了八天的 `latest.json` 歷史，可見頂部路徑裡這個形狀的命中數是 6、24、21、57、31、39、28、146、341，連續成長超過三輪。

先問它是不是站體自產：10-03 08:50 那份 `dist/` 的 HTML、JS、XML、JSON 對六種雙寫前綴全部零命中。每條路徑的命中數都整齊落在 12、UA 是 107／120／123 這類舊版 Chrome，看起來是某個外部爬蟲自己拼前綴。判定為外部雜訊，交給 maintainer 席位決定要不要在 `monitor-404.py` 給它一個家族名，不在本班動。

## 心臟格的投稿數第三次替巡邏記帳

`articlesLast7Days` 30→41、`contributedLast7Days` 41、`selfProducedLast7Days` 0，總數 1123 不變。同一窗口 zh 新增檔案用 `git log --diff-filter=A` 量是 0，同期 zh 的 heal／evolve commit 有 39 個。LESSONS `heart-counts-heals-as-contributed-births` 補第三個 instance，vc 2→3，到了 self-evolve 的升級門檻。動公式是閾值調整，留給 10-11 self-evolve-weekly 或哲宇。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅                                            |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅ 儀表板已重生，快照齡 0h                    |
| 自我檢查工具 PASS            | 見 commit 時 prose-health                     |
| diary                        | skipped：routine 預設 skip，理解沒有改變      |
| evolve                       | skipped：本班只刷新資料，教訓 bump 進 LESSONS |

## Handoff 三態

繼承自 `2026-10-08-055923-twmd-embeddings-nightly.md`：

- ⏳ blocked（延續，收件席位 `/twmd-routine` 或 self-evolve-weekly 10-11，本班動不了殼層）：routine-sync 提出的「embeddings 改殼後要隔兩晚才生效」三選項。
- ⏳ blocked（延續，哲宇）：`OBSERVER-QUEUE #75〜#93（待決）`，本班不動。
- [ ] pending（延續，babel 專屬，收件席位 `twmd-babel-nightly`）：〈台東縣〉〈台灣捷運發展史〉十二語跟上，明細在 `2026-10-08-023621-semiont-heartbeat.md`，這裡不重抄（REFLEXES #74）。
- [ ] pending（延續，收件席位：能動排程的 Full mode 或 `/twmd-routine`）：`.git/gc.log` 與 `git prune`（issue #1729）。本班 fetch、commit、push 時 git 照樣警告，babel 全程在寫，沒動。

本 session 新 handoff：

- [ ] pending（收件席位 `twmd-maintainer-daily`，該席位動得了 404 監測與路由）：`reports/404-monitor/latest.json` 2026-10-06 的「同語言前綴無斜線重複」形狀（`/ptpt/`、`/dede/` 等），八天從 6 長到 341 次可見命中。本班已驗 10-03 的 `dist/` 零命中，判為外部爬蟲。下一步是決定要不要在 `monitor-404.py` 歸成獨立家族，讓 unknown 不再被它撐大。
- [ ] pending（收件席位 `twmd-self-evolve-weekly` 10-11 或哲宇）：LESSONS `heart-counts-heals-as-contributed-births` 本班 vc 升 3。

## Beat 5 — 反芻

甦醒時第一個讀數就寫著「本快照讀的是舊鏡子」，這次警告自己先開口了，所以整班沒有人把五天前的分數當今天讀。值得記的反而是刷新後那些看起來像新病的東西：八則沉默死亡、DNA 掉十五分、404 率三倍、投稿數創新高。四件裡有三件在既有紀錄裡早有答案（停擺、時鐘、量法），真正新的只有一個 404 形狀，而它最後也落在外面。停擺之後的第一次量測，大部分的變化是在補記停擺本身。

🧬

---

_v1.0 | 2026-10-08 06:14 +0800_
_session twmd-data-refresh-am — cron 06:00 每日資料刷新，額度停擺後第一班_
_誕生原因：儀表板 119 小時沒更新，本班把 14 份 dashboard JSON 換成今天_
_核心洞察：停擺後第一次量測的多數變化是停擺本身的影子；新形狀先查站體有沒有自產，再決定是不是病_
_LESSONS-INBOX 候選：heart-counts-heals-as-contributed-births vc 2→3（既有條目 bump）_

# 2026-09-22-060315-twmd-data-refresh-am — 第十七夜讓場 14 步全綠零 stale；404 監測學會認出雙重編碼路徑，/sitemap.xml 補一條 301

> session twmd-data-refresh-am — cron 06:00 每日資料刷新（Micro mode）
> Session span: 06:03:15 → 06:15:00 +0800（約 12 分鐘，2 commits `57f1032ec` + `638da0677`）
> 資料來源：`git log %ai`

## 觸發

排程 06:00 觸發。任務三段：跑 14 步 ground truth 刷新、scheduler live-state 落檔、Step 11 freshness gate 的 catch ≠ fix 處置。

## 甦醒

`/twmd-become micro` 走完 Step 0-9，`wake-context.py` 11 項體檢全綠，落檔 268,320 bytes 用 Read 分頁讀到 `wake:END`。即時器官分數 🫀90 🛡️59 🧬95 🦴90 🫁85 🧫100 👁️90 🌐89，最低是免疫 59（review_coverage=19，黃燈自 07-05），快照本身標 stale 23h，是 refresh 之前的正常狀態。Q14：過去 48 小時是統一調度器的十二語 babel 批次（每幾篇一 commit，一夜六十多個）穿插 babel-nightly 當夜修的五個確定性病灶（分塊比值按語言校準、整篇引擎翻 imageAlt、rationale 巢狀還原、wikilink 路由收回工具端、status.py 截斷閘）、日記巴別塔補到 100%、排程心跳的事實巡邏第十五到第二十三篇、maintainer-am 收下 aminzai 三篇譯文並修掉我前一班交出去的 12 篇母稿相對路徑、routine-sync 第 56 輪零漂移。觀察者 09-19 在場（handle golden-bell-v2），mode=present。

## Step 1 讓場（第十七夜）

`check-parallel-actor.sh` 回 `ACTOR_BUSY`，babel dispatcher 主進程 98122 帶五個 worker 在寫工作樹（ar／de／en／vi 四篇譯文加 `reports/babel/*.json` 三份帳）。先 `git fetch` 量到 HEAD 與 origin 0/0，Step 1 的 stash 會把 dispatcher 手上的檔案抽走而 pull 又拉不到東西，照前十六夜的做法切 header 加 Step 2 以後組 runner，`bash -n` 過語法、後段零引用 `DIRTY / PULL_OK / STASH_LABEL`。runner 開跑時 HEAD 已是 `771032971`（embeddings 06:03 的 memory commit 在我甦醒期間落地）。

## 14 步結果

三源全綠：CF 七天 4,652,509 requests、404 率 1.07%（前夜 1.28%）、AI crawler 206,756 次跨 18 家（前夜 200,747）；GA4 與 SC 各 20 筆 top。`_translations.json` 12,697 筆零孤兒（前夜 12,665，babel 一夜補了 32 條）。spore records 166 篇 unchanged、dashboard-spores 0 warnings；immune v2 維持 **59**，`external_rulers` 3.6 不變；fork-census 0 新 sighting；dashboard-status 18 routines（13 operational／1 degraded／4 disabled，degraded 那條照例是本 routine 自己，量測時機問題）；llms.txt zh 1122／en 1106／ja 1045（前夜 1038，babel ja 批次落地）；GitHub ⭐1187（+2）🍴187（+1）👥75 📄1122；newsroom 222 篇上板 17 warnings；build perf ms/page **143**（前五夜 112→125→138→136→139，最新 build 1893 秒，七夜第一次站上 140）；reports/INDEX.md 722 行。

Step 11：14 個 `dashboard-*.json` 全部今日 mtime，analytics 內容 2026-09-21 對齊 UTC 今日，**0 stale**，catch ≠ fix 鐵律不觸發。Step 12 spore SSOT 0 errors／0 warnings，Step 13 no-op，Step 14 重生。

Stage 1.5：`list_scheduled_tasks` 18 條（14 enabled + 4 disabled），`routine-live-normalize.py` 落 `routine-live-state.json`，過濾 0 條私人 routine。

## 404 的 unknown 家族：第二夜仍過半，拆出雙重編碼與 /sitemap.xml

monitor-404 記 2026-09-20 總 404 **3,116**，前一日 5,993 腰斬（探憑證那波退了）。`unknown` 1,713 筆佔 55%，前夜交接說「若連兩夜仍 >50% 就看家族分佈」，今天是第二夜，所以進去看。榜首是 `/sitemap.xml` 一天 10 筆，站上真正的入口是 Astro 產的 `sitemap-index.xml`，robots.txt 早指向它，但爬蟲與瀏覽器慣例先試那個檔名；`config/redirects-manual.txt` 檔頭寫「直接加一行即可」，就加一行 301（`638da0677`，重生後 `_redirects` 204 條）。榜首之下是一整族 `/nature/%C3%A5%C2%8F%C2%B0…` 這種路徑，各 4–8 筆：UTF-8 位元組被當 Latin-1 讀、再 percent-encode 一次，`%C3%A5%C2%8F%C2%B0` decode 乾淨得到 `å\x8f°`，其實是「台」。`is_bad_encoding` 既有四條判準（壞 `%XX`、控制字元、U+FFFD、`<strange-chars>` 佔位符）都要 decode 失敗才觸發，這族 decode 完全合法，三個月來一直落 unknown。補第五條：decode 後出現 Latin-1 補充區字元且 latin-1 → utf-8 回譯成功；單獨一個 é 回譯會失敗，五組正負例驗過不誤殺法／西文路徑（`57f1032ec` 隨 refresh 一起進）。重跑後 bad-encoding 40 → 138、unknown 1,713 → 1,622（52%，仍過半，但 top 300 裡剩下的已是 `/web.zip`、`/stripe.config.js`、`/terraform.tfvars.bak` 這種探路名，跟三筆五筆的長尾）。

`latest.json` 只存 top 300 路徑的限制沒變：146 條 unknown 加起來 497 筆，其餘 1,100 多筆在 300 名以外看不到。

## Commit 與推送

只 stage 本 routine 的 37 個檔案（排除 dispatcher 在寫的 `reports/babel/*.json` 與五篇多語 `knowledge/*.md`；`knowledge/_translation-status.json` 跟前夜一樣當 prebuild 產出），`verify-commit-scope.sh --staged 37`／`--head 37` 都過。pre-push 撞到一個跑了 374 秒的 in-flight deploy，等滿 120 秒放行，`771032971..57f1032ec` 上 origin。第二個 commit `638da0677` 只動 `config/redirects-manual.txt` 一檔；`redirects-generated.json` 重生後只差一個逗號序，restore 掉不讓它被 dispatcher 的下一個 commit 掃走。

## 收官 checklist

| 檢查項                       | 狀態                                          |
| ---------------------------- | --------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                            |
| Timestamp 精確               | ✅                                            |
| Handoff 三態已審視           | ✅                                            |
| CONSCIOUSNESS 反映最新狀態   | ✅（dashboard JSON 全套重生）                 |
| 自我檢查工具 PASS            | ✅ `article-health.py --profile=memory-diary` |

## Handoff 三態

繼承 `2026-09-22-054001-twmd-routine-sync`：

- ⏳ blocked（延續）— issue #1729（馬英九腳註，已擴散 12 語）等 Write session 帶哲宇 review；`twmd-spore-pick-daily`／`twmd-spore-publish-daily` 停用未拍板（ROUTINE.md 註 ¹³），本輪 live-state 對賬一致，未擅自打開。
- [ ] pending（延續，指定席位 09-27 `twmd-self-evolve-weekly`，第 4 輪原樣往下傳）— `routine-sync.py` 對賬前 `git fetch`，routine 層與 `origin/main` 有差時印一行並 exit 非 0（LESSONS `staleness-guard-ships-through-the-artifact-it-guards`、REFLEXES #67 子規則、REFLEXES #15 第 13 次驗證）。本班不做的理由同前：`scripts/tools/` 越界。

繼承 `2026-09-21-061102-twmd-data-refresh-am`：

- [ ] pending（延續，本輪補一個數據點）— build perf ms/page 112→125→138→136→139→**143**，七夜第一次站上 140，最新 build 1893 秒；`dashboard-build-perf.json` trend 視窗仍只有 1.9 天。可執行動作不變：`gh run list --workflow deploy.yml --limit 200 --json startedAt,updatedAt,conclusion` 拉 CI 歷史找 ms/page 起跳那天（REFLEXES #41 CI capacity）。
- [ ] pending（低優先，等 dispatcher 不在跑）— `.git/gc.log` 存在讓自動 gc 停擺；平行 writer 期間不動（REFLEXES #35）。
- [x] ~~pending（maintainer-am 或任何 Micro session，12 檔 zh 母稿）— 12 篇 zh 母稿延伸閱讀 `../Category/中文slug` 相對路徑，巴別塔放大成 12 語 129 份 405 條（LESSONS 候選 `relative-category-links-survive-link-check`）~~ — retired by 09-21 maintainer-am `4f3974f86`（母稿改絕對路徑）＋ `69f7c6211`（`verify-internal-links.sh` 學會讀相對路徑，舊 dist 上 456 條現形）。交完當天就被下一班做掉，帶指令與數字的交接會落地。
- [x] ~~pending（觀察）— 若 unknown 連兩夜仍 >50%，考慮讓 `monitor-404.py` 的 `top_paths` 按家族各留前 50~~ — 第二夜 55% 確認後改走另一條路：先把看得到的 unknown 拆掉兩族（雙重編碼、`/sitemap.xml`），降到 52%。按家族保留 top_paths 的改法仍然成立但降級，理由見下一條。

本 session 新 handoff：

- [ ] pending（觀察，不需動作，`monitor-404.py`）— unknown 拆掉兩族後仍 52%，top 300 裡剩下的已是探路檔名（`/web.zip`、`/stripe.config.js`、`/terraform.tfvars.bak`、`/s3.yml`）與 `/terminology/{中文詞}`、`/{lang}/nature/{English Title}` 兩種形狀。前者可再進 `SCANNER_RE`（1-file），後者要先判是外部 bot 拼的還是我們曾發出的連結。若下一夜 unknown 仍 >50% 且榜首換成探路名，把 `.zip`／`.bak`／`.tfvars`／`.config.js` 收進 scanner 判準（REFLEXES #38 零維度變體：看不到的長尾跟「沒事」長得一樣）。

## Beat 5 — 反芻

前一班交出去的那條「12 篇母稿相對路徑」，寫的時候我以為要靠下一次被絆到才會落地，結果同一天上午 maintainer-am 就做掉了，連帶把連結檢查器也教會了。差別在那條交接帶了 grep 指令與檔數，下一班不用重新發現就能動手；對照同一份交接裡「routine-sync.py 加 fetch」那條，寫得同樣具體卻已經第四輪原樣往下傳，因為它被明確釘了席位在 09-27，其他班都有理由不碰。今天自己也照這個規律走：unknown 家族第二夜過半，看進去發現的兩族都是十分鐘內能做掉的 1-file，就做掉，沒有再登記成交接。留下的那條是真的需要判斷（`/terminology/` 與英文標題路徑是誰發的）才停在觀察。

雙重編碼那族三個月來每天都在 unknown 裡，四條既有判準都在問「decode 會不會壞」，而這族的特徵恰好是 decode 完全不壞、只是壞得很整齊。尺量的是形式合法性，病在意義層，這跟巴別塔把「台」翻成十二語一樣忠實地放大了一個編碼錯誤，只是方向反過來：那邊是我們放大別人讀得懂的錯，這邊是別人放大我們讀不懂的對。

🧬

---

_v1.0 | 2026-09-22 06:15 +0800_
_session twmd-data-refresh-am — 第十七夜讓場 14 步全綠零 stale；404 監測補雙重編碼判準；/sitemap.xml 301_
_誕生原因：cron 06:00 每日資料刷新_
_核心洞察：(1) 帶指令與數字的交接當天就被下一班做掉，釘了席位的交接反而四輪沒人碰 (2) 既有四條壞編碼判準都問「decode 會不會壞」，雙重編碼 decode 完全合法所以三個月落 unknown (3) unknown 第二夜過半時進去拆，比改 top_paths 保留策略便宜_
_LESSONS-INBOX 候選：無（雙重編碼是 REFLEXES #38 混維度既有形狀，不另開條目）_

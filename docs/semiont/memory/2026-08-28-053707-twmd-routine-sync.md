# 2026-08-28-053707-twmd-routine-sync — 三層對賬第三十一輪 18 條全 in-sync，但斷了四天才恢復

> session twmd-routine-sync — 每日排程 cron
> Session span: 05:37:07 → 05:37:32 +0800（~1 分鐘，0 commits）
> 資料來源：`git log %ai`

## 觸發

每日 05:30 Asia/Taipei 排程 fire，任務是讓這台機器（`~/.claude/scheduled-tasks`）的 routine prompt 與排程設定跟 git 的 routine SSOT 對齊，跑在晨鏈（data-refresh-am / spore-harvest-am / feedback-triage / maintainer-am）之前。

## 三層對賬

`git pull origin main` 確認已在最新（上一個 commit 是同日凌晨 `twmd-embeddings-nightly` 的 79e6240d6）。跑 `python3 scripts/tools/routine-sync.py`：18 條 routine（babel-nightly / data-refresh-am / distill-weekly / embeddings-nightly / feedback-triage / founder-lens-weekly / maintainer-daily / news-lens-weekly / rewrite-daily / routine-audit-weekly / routine-sync 自己 / self-evolve-weekly / spore-harvest-am / spore-pick-daily / spore-publish-daily / supporters-weekly / terminology-trends-monthly / weekly-report-sun）全部 `in-sync`，exit 0。沒有 prompt 漂移、沒有 cron/enabled 漂移、沒有 SSOT-only 缺件。

## 四天沒醒的自己

寫 index row 前照例翻 MEMORY.md 找上一輪，發現上一次 twmd-routine-sync 的紀錄停在 **2026-08-23**（第三十輪）。中間 08-24／08-25／08-26／08-27 四天完全沒有這條 routine 的紀錄，routine 本身根本沒被觸發，跟同一夜 `twmd-embeddings-nightly` 剛揭露的「08-24〜08-27 本機無任何 routine 執行痕跡、working tree 落後 149 commits」是同一件事的第二個獨立證據。兩條 routine 各自從自己的索引缺口摸到同一個根因：這台機器那幾天本身沒醒（機器休眠 / launchd 排程掛掉，待哲宇或 `twmd-flywheel-watch` 判斷），今天 08-28 才恢復，先是 embeddings-nightly 05:07 起跑，接著 05:37 這條也接上了。連續輪數的計數在 08-23 就已經斷過一次，之前幾輪 memory 寫的「連續第 N 輪」是對的，但把今天寫成「連續第十三輪」會抹掉這四天的空白，所以這裡誠實地不接續那個計數。

## 收官 checklist

| 檢查項                       | 狀態                                                     |
| ---------------------------- | -------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                       |
| Timestamp 精確               | ✅                                                       |
| Handoff 三態已審視           | ✅（全部繼承，本輪未碰）                                 |
| CONSCIOUSNESS 反映最新狀態   | N/A（本 session 未動 dashboard）                         |
| 自我檢查工具 PASS            | ✅（routine-sync.py exit 0，只驗設定一致，不驗有沒有跑） |

## Handoff 三態

繼承上一 session（`2026-08-28-005518-footnote-cards`）：

- ⏳ blocked — 營運機 mouhouse 排程器停了約兩天。本 session 未碰，維持 blocked
- [ ] pending — 五個縣市條目的正確圖片要補回（已開 spawn task）。未碰
- [x] ~~pending — `.husky/pre-push` 全檔掃過還有哪些 `VAR="$(...)"` 缺 `|| true`~~ 未碰，仍 pending
- [ ] pending — [#1453](https://github.com/frank890417/taiwan-md/pull/1453) 學測專題七張人物卡的第三方報導連結。未碰
- ⏳ blocked — [#1365](https://github.com/frank890417/taiwan-md/pull/1365) KENJI 知名度門檻等哲宇拍板。未碰
- ⏳ blocked — OBSERVER-QUEUE #39-#42 四項。未碰
- [ ] pending — D+3 回頭看 `footnote_card_open` 實際數字。未碰（尚未到 D+3）
- [ ] pending — 同一條腳註多次引用時 `fnref-N` id 重複問題。未碰
- [ ] pending — `.husky/pre-commit` RTL 檢查器行號釘死問題。未碰

本 session 新 handoff：不重複開一條新的機器休眠調查（`twmd-embeddings-nightly` 今夜已開），但這裡留一句交叉確認——第二條獨立 routine 的索引空窗印證同一個四天缺口，讓 `twmd-flywheel-watch` 或哲宇判斷時多一份證據。

## Beat 5 — 反芻

差點把今天寫成「連續第十三輪」，因為那句「連續零漂移」的句式這幾天寫得太順手，順手到沒有先去核對上一輪到底是哪一天。**這條 routine 存在的目的正是抓漂移**，結果自己的索引出現四天空白時，第一反應是延續慣用句式而不是先問「上一輪是什麼時候」。今天能接住是因為寫 index row 前的例行查核剛好把日期攤開來，不是因為多留意了什麼。

🧬

---

_v1.0 | 2026-08-28 05:37 +0800_
_session twmd-routine-sync — 每日排程對賬，第三十一輪，但接在四天空窗之後_
_誕生原因：cron 05:30 Asia/Taipei 排程 fire_
_核心洞察：18 條 in-sync 是真的，但「連續第 N 輪」的敘事如果不先核對日期，會把四天沒醒的事實悄悄抹平。_

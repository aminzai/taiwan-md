# 2026-09-24-053909-twmd-routine-sync — 第 58 輪對賬：embeddings 殼層的去寫死修補搬進機器，但今晚 05:13 那班已經讀了舊殼

> session twmd-routine-sync — cron routine（每日 05:30 Asia/Taipei）
> Session span: 05:37:49 排程 fire → 05:45 +0800（約 8 分鐘，1 項 apply + 本 memory commit）
> 資料來源：`routine-sync.py` apply 前後兩次輸出 + `diff` 機器版 vs git 版 + `git log -- docs/semiont/routine-prompts/twmd-embeddings-nightly.md` + `mcp__scheduled-tasks__list_scheduled_tasks` 當下 18 條 live 值對照 ROUTINE.md 排程表

✅ BECOME ack: mode=micro / Q14=PASS

## 觸發

排程任務。晨鏈之前把這台機器的 routine prompt 與排程設定跟 git SSOT 對齊。`git pull` 已是最新，wake-context selftest 全綠。

## 一條漂移：embeddings-nightly，git 較新

18 條裡 1 條 `prompt-drift`：`twmd-embeddings-nightly`。方向沒有懸念：git 版來自 `929a6f739`（09-23 06:09，embeddings 那班自己改的殼層），機器版 mtime 停在 7 月 24 日，三處差異全是舊殼寫死的東西，包括 `/Users/cheyuwu/Projects/taiwan-md` 這個舊家目錄、pipeline 版本號 v1.1、「6 語向量數」。git 版把三處都改成指向 canonical、不寫死數字。`--apply --stamp 2026-09-24` 寫進機器，舊版存證落 `reports/routine-prompt-drift/2026-09-24-exhibitions-mac-mini-local-twmd-embeddings-nightly.md`，重跑 18/18 in-sync、exit 0。

時序值得記下來：昨天這條 routine 05:42 跑完，embeddings 的殼層修補 06:09 才進 git，所以昨天對賬時根本還沒有東西可搬。今天 05:13 embeddings 照排程起跑，讀的仍是帶舊家目錄的殼，要到 09-25 才會讀到新版。起初我以為 babel 也一樣，重算後不是：babel 00:30 起跑、收官在 05:30 之前，它改的殼當天早上就被本班搬進機器，隔晚生效，跟任何 routine 一樣。多等一晚的只有「起跑在 05:30 之前、收官在 05:30 之後」的班，目前只有 embeddings（05:00 起、約 06:00 收）。

## cron／enabled：直接對排程器

工具沒印 ⏰／🔌，但它比的是 `routine-live-state.json`，mtime 09-23 06:07，已經 23.5 小時（昨天 handoff 記的同一個問題）。所以本輪照昨天的做法，拉 `list_scheduled_tasks` 的 live 值逐條對 ROUTINE.md 排程表：18 條 `cronExpression` 全等；disabled 的四條（`rewrite-daily`、`founder-lens-weekly`、`spore-pick-daily`、`spore-publish-daily`）在 ROUTINE.md 都標 ⏸️，一致；`twmd-flywheel-watch` 住 commander-macbook，本機不該有。零差，不動 MCP，沒有需要建立的 task。

## 收官 checklist

| 檢查項                       | 狀態                                      |
| ---------------------------- | ----------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                        |
| Timestamp 精確               | ✅                                        |
| Handoff 三態已審視           | ✅                                        |
| CONSCIOUSNESS 反映最新狀態   | 不適用（本輪無器官狀態變更）              |
| 自我檢查工具 PASS            | ✅（article-health memory-diary profile） |

## Handoff 三態

繼承自 09-23 第 57 輪：

- ⏳ blocked：issue #1729（馬英九腳註）等 Write session 帶哲宇 review；`spore-pick-daily`／`spore-publish-daily` 為 manual-by-decision（ROUTINE.md 註 ¹³），本輪 enabled 層一致，未打開。
- [ ] pending（席位 09-27 `twmd-self-evolve-weekly`，第 5 輪往下傳）：`routine-sync.py` 對賬前 `git fetch` 並在 routine 層有差時非 0 exit。
- [ ] pending（同一支工具、同一席位）：`routine-sync.py` 的 cron／enabled 對賬讀 `routine-live-state.json` 不印新鮮度。本輪鏡像又是 23.5 小時前的，仍靠手動拉 live 補驗。
- [ ] pending：單檔收官改 `git commit -- <path>`，本輪照做，尚未寫進 routine prompt 第 6 步。

本 session 新 handoff：

- [ ] pending（給 `/twmd-routine` 或 09-27 self-evolve 判斷，cron 調整屬 routine 管理不在本班權限）：`twmd-embeddings-nightly` 跨過 05:30 收官，它改自己的殼要隔兩晚才生效（本輪命中一次）。選項：(a) 維持現狀，接受多等一晚；(b) embeddings 收官流程改完殼就順手跑一次 `routine-sync.py --apply`；(c) 把 routine-sync 挪到 06:30 之後，但晨鏈（06:00 起）就會讀到未對齊的殼。推薦 (b)，一行、不動排程；(a) 也可接受，因為這種情況一年沒幾次。

## Beat 5 — 反芻

昨天我寫「這條 routine 是投遞」。今天看到投遞有時刻表：我每天 05:30 出門送信，embeddings 05:00 就讀過信箱，06:00 才把寫給自己的信投進 git，剛好錯過我這一趟。第一版 memory 我把 babel 也算進去，因為昨天那「差一分鐘」的故事還在腦子裡，形狀看起來一樣。重排一次時間軸才看出 babel 其實每天都趕得上。昨天的案例幫我看見今天的問題，也差點讓我把一個不同的東西硬套上去。

🧬

---

_v1.0 | 2026-09-24 05:45 +0800_
_session twmd-routine-sync — 第 58 輪 cron 對賬；1 條漂移（embeddings-nightly）git→機器已 apply；cron／enabled 對 live 排程器零差_
_誕生原因：每日排程 05:30 Asia/Taipei 觸發_
_核心洞察：跨過 05:30 收官的 routine（目前只有 embeddings）改自己的殼要隔兩晚才生效；babel 經重算不受影響。鏡像新鮮度問題第二輪仍靠手動補驗。_

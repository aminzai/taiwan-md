# 2026-08-04-131111-twmd-routine-sync — 第十一輪對賬，抓到真實漂移：新 routine 誕生但機器沒排程

> session twmd-routine-sync — cron 排程 05:30 觸發（Micro mode BECOME，本次因排程延後於 13:11 執行）
> Session span: 13:11 → 13:16 +0800（~5 min，0 commits）
> 資料來源：`git log %ai`

## 觸發

每日 05:30 例行 routine-sync：讓這台機器（`~/.claude/scheduled-tasks`）的 routine prompt 與排程設定跟 git 的 ROUTINE.md SSOT 對齊，排在晨鏈（data-refresh-am 之前）保證早上那串醒來讀到的是對齊過的 prompt。

## 三層對賬

`git checkout main && git pull` 拉到最新 SSOT（帶進當日新增的 `twmd-terminology-trends-monthly` routine，誕生於支語深度研究 session）。跑 `python3 scripts/tools/routine-sync.py`，18 條 routine 中 17 條 `in-sync`，1 條 `❌ prompt-missing-on-machine`：**`twmd-terminology-trends-monthly` 在 ROUTINE.md 排程表已登記（`30 10 5 * *` / Opus / 每月 5 日 10:30），但這台機器的 `~/.claude/scheduled-tasks/` 從未建過對應排程**——這是連續十輪零漂移後第一次真正的「SSOT 有新 routine，機器缺排程」情況，方向明確（git 是新的，機器缺項），依 SOP 走 apply + create 兩步而非猜測。

**修復**：

1. `--apply --stamp 2026-08-04` 把 mirror `docs/semiont/routine-prompts/twmd-terminology-trends-monthly.md`（已在 git，隨 pull 帶入）寫進機器端 `~/.claude/scheduled-tasks/twmd-terminology-trends-monthly/SKILL.md`。
2. 排程本身另外建：讀 ROUTINE.md §排程表 + footnote ²⁴ 取 cron `30 10 5 * *`／model Opus／taskId 同名，用 `mcp__scheduled-tasks__create_scheduled_task` 建立。表列未標 ⏸️、不在 §⏸️ PAUSED 5 條清單內 → enabled 保持預設 true。
3. 重跑對賬仍報 `prompt-drift`——`create_scheduled_task` 寫出的 SKILL.md 少了檔尾換行符，跟 mirror 檔案逐位元組比對差一個 `\n`。這不是內容漂移，是建立工具的落檔行為差異；直接 `printf '\n' >>` 補上換行讓機器檔案與 mirror 逐位元組一致，非用 `--harvest`（機器版沒有真正比 git 新的內容）。
4. 三跑對賬：18/18 `in-sync`，exit 0。

`git status --short` 全程乾淨——mirror 檔案本就隨 `git pull` 進 repo，本 session 沒有新增或修改任何 git 追蹤檔案，只動了 repo 外的 `~/.claude/scheduled-tasks/`，符合「什麼都沒動 repo 就不 commit」。

## 收官 checklist

| 檢查項                       | 狀態                                            |
| ---------------------------- | ----------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                              |
| Timestamp 精確               | ✅（git log %ai + date）                        |
| Handoff 三態已審視           | ✅（沿用最新 maintainer-daily handoff，無新增） |
| CONSCIOUSNESS 反映最新狀態   | 不適用（本輪為機器層排程對賬，非內容變更）      |
| 自我檢查工具 PASS            | ✅（`routine-sync.py` exit 0，18/18 in-sync）   |

## Handoff 三態

繼承（皆非本 routine 職責範圍，繼承現狀不動，透過 wake-context handoff 段接住）：

- [ ] pending（給哲宇）— #1264 seo-meta 多語言門檻校準、#1184 justfont 後台網域白名單
- [ ] pending（給哲宇，per OBSERVER-QUEUE #25）— 免疫黃燈連 28+ 天且分數開始鬆動（60→57），三選一等拍板
- [ ] pending（給哲宇，P0，來自 twmd-supporters-weekly）— cron 執行環境無 Gmail MCP，checkpoint 停在 2026-07-12
- [ ] pending（給哲宇）— 黃崇仁 #165/#166 Bucket D「是否洗白」框架質疑，`HARVEST-FRAMING-PENDING/2026-08-04.md` 三個處置 option 待拍板
- [ ] pending（給哲宇）— Discussion #104 對外合作建議，已回覆告知需哲宇拍板，尚待回應

本 session 新 handoff：無。今日新誕生的 `twmd-terminology-trends-monthly` 排程已建好並驗證對賬通過，下個月 5 日 10:30 首次自動觸發前不需要人工介入。

## Beat 5 — 反芻

十輪零漂移之後第十一輪就命中真實漂移，跟上次一樣：漂移的觸發不是這條 routine 自己壞了，是**同一天有其他 session 在 SSOT 端誕生了新 routine**（支語研究 session 拍板月度化）。這正好回答了 8/2、8/3 兩天連續寫下「該找 self-evolve 抽查真實 catch rate」的疑問——這次不是靠 self-evolve 抽查發現的，是例行對賬本身就抓住了，證明這條 routine 的守備範圍原本就包含「新 routine 誕生後機器忘了跟上」這一類，不只是「既有 routine 的 prompt 內容漂移」。

第二個小發現：`create_scheduled_task` 工具寫出的檔案跟 mirror 檔案有系統性的尾端換行差異，這类差異不是內容漂移但會被逐位元組比對的工具判定成 `prompt-drift`。如果未來每次新建排程都要手動補一次換行，值得考慮回報這個工具行為或在 `routine-sync.py` 的比對邏輯加一個「忽略檔尾空白差異」的正規化步驟——本次先手動修，沒有動 canonical。

🧬

---

_v1.0 | 2026-08-04 13:16 +0800_
_session twmd-routine-sync — 每日例行三層對賬，第十一輪，抓到一次真實漂移（新 routine 誕生未同步機器排程）並修復_
_核心洞察：連續零漂移不是空轉訊號，這次證明例行對賬本身就是「新 routine 誕生後機器沒跟上」這類漂移的第一道防線，不需要等 self-evolve 才抓到。_

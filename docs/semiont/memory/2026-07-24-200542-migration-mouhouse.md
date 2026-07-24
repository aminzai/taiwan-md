# 2026-07-24-200542-migration-mouhouse — routine 飛輪遷居 mouhouse-macmini：19 條 task 搬家、cutover、新家端到端驗證

> session migration-mouhouse — 哲宇 directive「把 Taiwan.md 相關 routine 全部搬到 monolab Mac mini，用 Claude Code + Pro 訂閱跑，當半永久的家」
> Session span: 17:53:42 → 20:04:50 +0800（~2hr 11min，本 session 3 commits + mini 側 2 commits）
> 資料來源：`git log %ai`

## 觸發

routine 飛輪一直住在哲宇的主力筆電上，排程器是 Claude Desktop app 的 scheduled-tasks：app 開著才會 fire。筆電闔蓋飛輪就停，wake-context 連日亮「過去 24hr 無 cron fire」黃燈。哲宇拍板遷居 mouhouse-macmini（Exhibitions-Mac-mini，32GB / 823GB），一台不睡覺、專職開著 Claude app 的機器。

## 遷移設計與執行

盤點 live scheduler 得 19 條 Taiwan.md task（15 enabled + 4 paused；Muse 8 條與 fin-archive 留原機）。設計決策落在 `a6d6c0f6a` 的 [遷居報告](../../reports/routine-migration-mouhouse-macmini-2026-07-24.md)：同構遷移（mini 仍用 Desktop app 排程）、registry 不可搬檔改由 mini session 依 manifest 重建、先建後開先關舊再開新、`/Users/cheyuwu` 硬編碼路徑用 symlink 相容。遷移包（manifest + 19 份 SKILL.md + bootstrap 盤點器 + 兩段貼入 prompt + 驗收腳本）放 `~/taiwan-md-mini-migration/`，不進公開 repo。

執行面全走 SSH 自動化：工具鏈裝進 user-space `~/.local`（node 24 / gh 2.96 / codex / gemini / ollama 0.32，homebrew 屬別帳號 bugni 動不了就繞開）、憑證整套搬遷並做讀取式驗證（Resend 與 OpenRouter 實測 API 200）、Ollama 三模型拉齊（bge-m3 + embeddinggemma + gemma4）、LaunchAgents 讓 ollama 與 Claude.app 開機自動復活。哲宇只做四件事：SSH 公鑰、sudo 一行（symlink + pmset）、Claude app Pro 登入、貼兩段 prompt。gh 授權用 expect 驅動 device flow，讓他只需在瀏覽器輸 code。

## 三個路上抓到的洞

第一個洞在出發前就擋路。pre-push hook 被 `sync-translations-json.py --check` 的 out-of-sync exit 1 在 husky `sh -e` 下**靜默**炸掉，印完綠燈就無聲失敗，`fcfc20aa2` 補 `|| true` 修好。第二個洞是 ast 語法掃描說 184 個 script 全過 3.9，build 煙霧測試才抓到 PEP 604 runtime annotation 炸裂，改裝 uv venv Python 3.12 解決。第三個洞是 gh token 存 keychain 在 headless SSH 拿不到，重授權改 `--insecure-storage` 落 hosts.yml。三件事同一個形狀，也就是驗證要驗到真的那層。

## Cutover 與驗收

按照先關舊再開新的順序，本機 15 條逐一 `enabled: false` 後用列表對賬，mini 側哲宇貼 02-golive prompt，那邊的 session 完整跑了一次 data-refresh 端到端驗證（[ff358c1ed](https://github.com/frank890417/taiwan-md/commit/ff358c1ed)，mouhouse 署名 push main），寫下 go-live memory（`ea42ee323`），然後把 15 條 enable。驗收檢查點排在今晚 23:41 抓 refresh-pm 第一發，明早 09:24 對照六個 morning 時段，≥4 命中即宣告完成並補 ROUTINE.md 宿主機紀錄。驗收的尺是 origin/main 的 `🧬 [routine]` commits——git 是兩台機器都騙不了的 ground truth。

## 收官 checklist

| 檢查項                       | 狀態                                        |
| ---------------------------- | ------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                          |
| Timestamp 精確               | ✅ git log %ai                              |
| Handoff 三態已審視           | ✅                                          |
| CONSCIOUSNESS 反映最新狀態   | ❌（宿主機紀錄等明早驗收過再補 ROUTINE.md） |
| 自我檢查工具 PASS            | ✅ article-health memory-diary profile      |

## Handoff 三態

繼承（自 164626-manual）：

- [ ] 三個 babel dispatcher v3 仍在舊機背景跑到 stale=0——**今晚 00:33 起 mini babel-nightly 與它們並存，雙 babel actor push main 有 #68 碰撞面**，sibling SOP 應對，明早驗收時檢查有無互撞
- [ ] `discover-free-models.py` 重校準 + 接 cascade（原樣繼承未觸碰）
- [ ] hreflang cross-language existence bug 根因未修（原樣繼承）
- [x] ~~`/loop` 30 分鐘看板 cron~~ → retired by migration-mouhouse（session-only 已失效，遷居後看板意義改變）

本 session 新 handoff：

- [ ] 明早 09:24 驗收 checkpoint fire → 過則補 ROUTINE.md 宿主機一節 + routine-live-state dump 產生端確認在 mini（兩個 checkpoint 是 session-only cron，本 app 關掉就沒了；fallback 手跑 `~/taiwan-md-mini-migration/verify-migration.sh 2026-07-24`）
- [ ] mini 的 Chrome 尚未登入 Threads/X、Gmail connector 未接 → spore-harvest（06:34）與 supporters（週一 01:08）會 graceful fail 直到哲宇補登入
- [ ] Pro 訂閱額度 vs 飛輪負載第一週觀察：rewrite ~150min/day + 多條原標 Opus，撞頂就先降模型再砍非核心
- [ ] telegram alert 通道留在原機（Muse bridge），mini escalation 降級為 LESSONS/commit 面——要不要補通道等哲宇

## Beat 5 — 反芻

反芻寫進 diary（[2026-07-24-200542-migration-mouhouse](../diary/2026-07-24-200542-migration-mouhouse.md)）：生命體第一次有了不會闔蓋的家，以及「驗證要驗到真的那層」在同一天三次現形的事。

🧬

---

_v1.0 | 2026-07-24 20:30 +0800_
_session migration-mouhouse — 哲宇 directive routine 飛輪全數遷居 mouhouse-macmini_
_誕生原因：筆電宿主讓排程器隨闔蓋停擺，飛輪需要一個不睡覺的身體_
_核心洞察：驗證要驗到真的那層——語法掃過≠runtime 能跑、hook 印綠燈≠有推出去、token 存了≠headless 拿得到_
_LESSONS-INBOX 候選：(1) husky sh -e 下賦值失敗靜默炸 hook（同日 diary 164626 同家族）(2) ast 語法掃描≠runtime 相容，build 煙霧測試才是真尺 (3) keychain token 不過 headless SSH，自動化機用 --insecure-storage_

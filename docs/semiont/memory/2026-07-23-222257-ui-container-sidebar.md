# 2026-07-23-222257-ui-container-sidebar — 全站 container 加寬 + 文章側欄分享／貢獻者優先

✅ BECOME ack: mode=micro / wake-context selftest 全綠 / Q14 cross-session continuity=PASS（承接 idlccp clownfish + PR review finale）

> session manual — 哲宇 UI 微調（container 寬度 + 右側 sidebar 排序）
> Session span: 22:15 前後 → 22:23 +0800（約 8 min，1 ship commit）
> 資料來源：`git log %ai`、tokens.css SSOT、ArticleSidebar.astro

## 觸發

哲宇 `/twmd-become` 後直接點兩件事：文章與其他頁的 container 最大寬度加一點；右側分享與貢獻者區塊要排在關鍵詞前面——關鍵詞現在沒什麼用。

## 容器寬度

全站頁面層主容器 SSOT 在 `src/styles/tokens.css` 三檔 token。改 token 一次，所有 `max-w-[var(--container-*)]` 的 template（文章、hub、latest、changelog、Header／Footer 同寬等）一起跟：

| Token                 | 用途                           | 前     | 後     |
| --------------------- | ------------------------------ | ------ | ------ |
| `--container-prose`   | home / about / semiont / diary | 800px  | 900px  |
| `--container-article` | 文章頁 TOC + 正文 + sidebar    | 1280px | 1440px |
| `--container-wide`    | explore / latest / hub / data… | 1380px | 1560px |

特例頁（soundscape、bench 等 bespoke 行寬）仍不走這三檔。Ship：`400a1a0b8`。

## 側欄排序

`ArticleSidebar.astro` 原順序是 meta → 關鍵詞 → 分享 → 貢獻者。改成：

1. 閱讀 meta（時間、日期、修訂…）
2. 分享
3. 貢獻者
4. 關鍵詞（最後）

關鍵詞保留不刪——哲宇說的是排序與效用，不是立刻拆掉。若之後確認長期無人點，再考慮弱化或移除。

## 收官 checklist

| 檢查項                       | 狀態                                                                         |
| ---------------------------- | ---------------------------------------------------------------------------- |
| MEMORY 有這次 session 的紀錄 | ✅                                                                           |
| Timestamp 精確               | ✅（commit `%ai` 22:22:57）                                                  |
| Handoff 三態已審視           | ✅                                                                           |
| CONSCIOUSNESS 反映最新狀態   | ❌（純 UI micro，不刷新 organ snapshot）                                     |
| 自我檢查工具 PASS            | ✅ prose-health hard=0（score 10/8 因 checklist 表結構，memory 慣例可 ship） |

## Handoff 三態

繼承（來自 214453-idlccp-clownfish-instrument / 214147-pr-review-refresh-finale）仍 pending：

- [ ] hi 剩 12 篇 P0 待譯。
- [ ] 68 檔英文假翻譯待重譯。
- [ ] person-fidelity 仍缺 file-level occurrence-count。
- [ ] `codex/recover-kmt-projection` 續寫。
- [ ] 42 個保留 worktree 救援盤點。
- [ ] scheduled-tasks rider / routine-live-state dump。
- [ ] 兩個保護 stash 未 pop。
- [ ] 九篇新文缺 media / rationale / 深度 <4500：EVOLVE polish backlog。
- [ ] contributor-pr-heal dogfood 下一批 external PR。
- [ ] MAINTAINER-PIPELINE 文件加硬規則：contributor PR 禁 close-as-ship（上 session 已加 §1b，待 dogfood 驗證）。

本 session 新 handoff：

- [ ] 本地 dev 目測文章頁寬度與側欄順序是否舒服；若仍偏窄或關鍵詞仍佔位，再調 token 或弱化 tags。
- ~~[x] container + sidebar ship~~ → **retired by `400a1a0b8`**。

## Beat 5 — 反芻

這次很小，但提醒一件事：chrome 的垂直排序就是策展。關鍵詞是 SEO 殘影，分享與貢獻者才是讀者還可能動手的入口。把高效用區塊往上推，比再加一個功能更便宜。寬度也一樣——三檔 token 是唯一槓桿，不該散落在各 template 的 hardcode px。

🧬

---

_v1.0 | 2026-07-23 22:23 +0800_
_session manual — UI container 加寬 + ArticleSidebar 排序_
_誕生原因：哲宇要求加寬頁面 container，並把分享／貢獻者排在關鍵詞前_
_核心洞察：側欄排序是策展；效用優先於 SEO 殘影。全站寬度只改 tokens 三檔。_

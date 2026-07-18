# Language Status — taiwan.md 多語言支援狀態

> **For contributors who want to translate articles or add a new language.**
> SSOT for this list: [`src/config/languages.ts`](../../src/config/languages.ts)（狀態以註冊表為準，本檔是導覽）
> 各語言即時文章數與翻譯覆蓋率：[taiwan.md/dashboard](https://taiwan.md/dashboard/)（本檔不寫死數字）

---

## TL;DR

| 語言                | Code    | 狀態              | 路由 | 備註                                                     |
| ------------------- | ------- | ----------------- | ---- | -------------------------------------------------------- |
| 🇹🇼 繁體中文         | `zh-TW` | ✅ Default (SSOT) | /    | canonical，所有翻譯的源頭                                |
| 🇺🇸 English          | `en`    | ✅ Active         | /en/ | community                                                |
| 🇯🇵 日本語           | `ja`    | ✅ Active         | /ja/ | Link1515 + community                                     |
| 🇰🇷 한국어           | `ko`    | ✅ Active         | /ko/ | ceruleanstring + community                               |
| 🇪🇸 Español          | `es`    | ✅ Active         | /es/ | 2026-04-25 啟用                                          |
| 🇫🇷 Français         | `fr`    | ✅ Active         | /fr/ | 2026-04-24 啟用，ceruleanstring + community              |
| 🇻🇳 Tiếng Việt       | `vi`    | 🌱 Scaffolded     | ❌   | 2026-07-18 選定，待啟動拍板（[選址報告][evolve-report]） |
| 🇮🇩 Bahasa Indonesia | `id`    | 🌱 Scaffolded     | ❌   | 同上                                                     |
| 🇧🇷 Português        | `pt`    | 🌱 Scaffolded     | ❌   | 同上                                                     |
| 🇮🇳 हिन्दी           | `hi`    | 🌱 Scaffolded     | ❌   | 同上                                                     |

[evolve-report]: ../../reports/evolve-2026-07-18-language-branches.md

---

## ✅ Active languages

These languages are fully wired into:

- Astro routing (`/{code}/...` URLs)
- Sitemap + `hreflang` tags（2026-07-17 起由語言註冊表驅動）
- Language switcher
- Search index（per-language shards）
- Semantic related articles（bge-m3 embeddings, nightly）
- Dashboard translation coverage
- llms.txt for AI crawlers

**To translate an article into an active language**: see [`docs/pipelines/TRANSLATION-PIPELINE.md`](../pipelines/TRANSLATION-PIPELINE.md). Required frontmatter:

```yaml
---
title: '한국어 제목'
description: '...'
date: 2026-04-14
tags: [...]
category: 'Music'
translatedFrom: 'Music/原中文檔名.md' # ← 必填，防止孤兒
---
```

The `translatedFrom` field is the **most important** addition — it lets the system detect orphan translations even if `_translations.json` is incomplete.

---

## 🌱 Scaffolded languages（已選定，待啟動）

2026-07-18 由 EVOLVE 三源數據（GA / Search Console / Cloudflare）× Ethnologue 人口槓桿 × 主權缺口選定四個新語言支系：**越南文（vi）、印尼文（id）、葡萄牙文（pt）、印地語（hi）**。完整選址分析與落選理由（de / ar / th / ru / bn）：[選址報告][evolve-report]。

現在的狀態：語言註冊表已有這四筆 `enabled: false`——**翻譯 PR 歡迎現在就送**（進 `knowledge/{vi,id,pt,hi}/`，會被 merge 但暫無路由），路由、UI、批次翻譯的啟動排程等 maintainer 拍板。啟動時所有累積的翻譯一夜之間上線（es / fr 都走過同一條路）。

出生的完整流程（選址 → scaffold → 模型校準 → P0 內容批 → 介面路由 → 啟用 → 出生後驗證）：[`docs/pipelines/LANGUAGE-BIRTH-CHECKLIST.md`](../pipelines/LANGUAGE-BIRTH-CHECKLIST.md) v2.0。

---

## 🌱 我想加一個全新語言（th / de / ar / ...）

**Contributor 可以做的**：

1. 開一個 Issue 說明你想加的語言＋你能投入的範圍（文章翻譯？UI 字串？母語 review？）
2. 若 maintainer 同意 scaffold，在 [`src/config/languages.ts`](../../src/config/languages.ts) + `.mjs` 各加一筆 `enabled: false` entry（兩份檔案，pre-commit sync check 會驗）：

   ```typescript
   {
     code: 'th',
     displayName: 'ไทย',
     hreflang: 'th',
     enabled: false, // scaffold：接受翻譯，尚無路由
     notes: 'YYYY-MM-DD scaffolded. ...',
   }
   ```

3. 開始送文章翻譯 PR 進 `knowledge/th/`（記得 `translatedFrom`）

**啟用（`enabled: true`）是 maintainer 的責任**，要走完 [`LANGUAGE-BIRTH-CHECKLIST.md`](../pipelines/LANGUAGE-BIRTH-CHECKLIST.md) 的模型校準（refusal 前測 + ratio band）、UI 字串（`src/i18n/` 各 bundle）、路由與四層完整度驗證。過去加一個語言要改 15 個檔案，LANGUAGES_REGISTRY 重構（2026-04-14）後註冊只需 2 處；hreflang / sitemap / 搜尋 / 語意索引 / dashboard 都從註冊表自動 derive。

---

## 🛡️ Orphan prevention

每個翻譯文件**必須**在 frontmatter 標 `translatedFrom`：

```yaml
translatedFrom: 'Music/五月天.md'
```

這個欄位是 SSOT。`knowledge/_translations.json` 是從 frontmatter 自動產生的快取，不是手動維護的真實來源。

**為什麼這比 `_translations.json` 集中映射更可靠：**

- 檔案層級的 self-documentation（不需要查中央表）
- 即使 `_translations.json` 漏了一條，文件本身仍然知道來源
- Pre-commit hook 可以 enforce
- 重命名/刪除原文時，可以立刻 detect 哪些翻譯變成孤兒

**Pre-commit hook**（2026-04-14 η 上線）會 reject 任何缺 `translatedFrom` 的新翻譯 PR。

---

_v2.0 | 2026-07-18 — 對齊現實：es / fr 早已 active（本檔停在四月的 preview 描述三個月）；新增 🌱 Scaffolded 段（vi / id / pt / hi 選定）；文章數改指 dashboard 不寫死；新語言指南指向 LANGUAGE-BIRTH-CHECKLIST v2.0_
_v1.0 | 2026-04-14 η session_

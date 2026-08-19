# Language Status — taiwan.md 多語言支援狀態

> **For contributors who want to translate articles or add a new language.**
> SSOT for this list: [`src/config/languages.ts`](../../src/config/languages.ts)（狀態以註冊表為準，本檔是導覽）
> 各語言即時文章數與翻譯覆蓋率：[taiwan.md/dashboard](https://taiwan.md/dashboard/)（本檔不寫死數字）

---

## TL;DR

| 語言                | Code    | 狀態              | 路由 | 備註                                                                              |
| ------------------- | ------- | ----------------- | ---- | --------------------------------------------------------------------------------- |
| 🇹🇼 繁體中文         | `zh-TW` | ✅ Default (SSOT) | /    | canonical，所有翻譯的源頭                                                         |
| 🇺🇸 English          | `en`    | ✅ Active         | /en/ | community                                                                         |
| 🇯🇵 日本語           | `ja`    | ✅ Active         | /ja/ | Link1515 + community                                                              |
| 🇰🇷 한국어           | `ko`    | ✅ Active         | /ko/ | ceruleanstring + community                                                        |
| 🇪🇸 Español          | `es`    | ✅ Active         | /es/ | 2026-04-25 啟用                                                                   |
| 🇫🇷 Français         | `fr`    | ✅ Active         | /fr/ | 2026-04-24 啟用，ceruleanstring + community                                       |
| 🇻🇳 Tiếng Việt       | `vi`    | ✅ Active         | /vi/ | 2026-07-19 啟用（[出生戰役][birth-report]）；未服務中 SC 曝光最高＋最大新住民社群 |
| 🇮🇩 Bahasa Indonesia | `id`    | ✅ Active         | /id/ | 2026-07-19 啟用；最大移工社群母語＋新南向核心                                     |
| 🇧🇷 Português        | `pt`    | ✅ Active         | /pt/ | 2026-07-19 啟用；唯一三源全確認缺口（巴西）                                       |
| 🇮🇳 हिन्दी           | `hi`    | ✅ Active         | /hi/ | 2026-07-19 啟用；全球第三大語言、未覆蓋中人口最大                                 |
| 🇸🇦 العربية          | `ar`    | ✅ Active         | /ar/ | 2026-07-25 啟用；首個 RTL 語言                                                    |
| 🇷🇺 Русский          | `ru`    | ✅ Active         | /ru/ | 2026-07-25 啟用                                                                   |

[evolve-report]: ../../reports/evolve-2026-07-18-language-branches.md
[birth-report]: ../../reports/language-birth-2026-07-18.md
[birth-report-ar-ru]: ../../reports/language-birth-2026-07-25.md

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

## 🌏 2026-07-19 新增四語（越南／印尼／葡萄牙／印地）

2026-07-18 由 EVOLVE 三源數據（GA / Search Console / Cloudflare）× Ethnologue 人口槓桿 × 主權缺口選定四個新語言支系：**越南文（vi）、印尼文（id）、葡萄牙文（pt）、印地語（hi）**。完整選址分析與落選理由（de / ar / th / ru / bn）：[選址報告][evolve-report]。

2026-07-19 出生戰役一次啟動：各語 P0 約 52-67 篇（含 13 分類 Hub）+ 完整 16 個 UI bundle + 路由上線。內容過 CJK / 地理主權 / 人物主權三閘全綠（[出生戰役實錄][birth-report]）。hi 以 44 篇+Hub 出生（比 es 當年 36 多），餘 23 篇 P0 follow-up 漸長。翻譯 PR 持續歡迎。

出生的完整流程（選址 → scaffold → 模型校準 → P0 內容批 → 介面路由 → 啟用 → 出生後驗證）：[`docs/pipelines/LANGUAGE-BIRTH-CHECKLIST.md`](../pipelines/LANGUAGE-BIRTH-CHECKLIST.md) v2.0。

---

## 🌏 2026-07-25 新增阿拉伯文與俄文

阿拉伯文（ar）與俄文（ru）已完成內容、UI、路由與語言切換器接線並正式啟用；阿拉伯文也是站上第一個 RTL 語言。實作與驗證記錄見[出生戰役實錄][birth-report-ar-ru]。

---

## 🌱 我想加一個全新語言（th / de / bn / ...）

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

_v2.2 | 2026-08-13 — 補上已啟用的 ar / ru，移除把 ar 列為未來語言的舊說法_
_v2.1 | 2026-07-19 — 四語 vi/id/pt/hi flip Active（出生戰役）_
_v2.0 | 2026-07-18 — 對齊現實：es / fr 早已 active（本檔停在四月的 preview 描述三個月）；新增 🌱 Scaffolded 段（vi / id / pt / hi 選定）；文章數改指 dashboard 不寫死；新語言指南指向 LANGUAGE-BIRTH-CHECKLIST v2.0_
_v1.0 | 2026-04-14 η session_

---
feedback_id: 'baaa56a9-eb74-4c05-b5df-da73cc5491de'
created_at: '2026-08-10T05:44:52.742636+00:00'
contributor: 'Pigcasso6'
type: 'bug'
status: 'filed'
page_kind: 'other'
article_slug: ''
lang: 'zh-TW'
source_url: 'https://taiwan.md/explore/'
issue_url: 'https://github.com/frank890417/taiwan-md/issues/1314'
issue_number: 1314
---

# Feedback — bug · 探索 Taiwan.md — 瀏覽開放的台灣知識庫

**回報者**：Pigcasso6
**時間**：2026-08-10T05:44:52.742636+00:00

**回報內容**
vi、id、pt、hi、ar、ru六种语言页面左下角的「意见回馈」模块没有对应的翻译，用的都是英文。

**系統初判**
已收到，自動初判分類為「網站問題」，已轉維護者。

**GitHub issue**：https://github.com/frank890417/taiwan-md/issues/1314

## 溝通紀錄

<!-- issue 留言由 twmd-feedback-triage 定期 sync 到這裡 -->

<!-- comment:frank890417-2026-08-11T11:20:32Z -->

**frank890417** · 2026-08-11 11:20

已修，commit \`1efda3851\`。

根因是回饋模組的語言表停在六種語言（zh-TW/en/ja/ko/es/fr），站上已經有十二種。程式碼在找不到對應語言時會靜默 fallback 到英文——不報錯、不留痕跡，所以沒有人發現 vi/id/pt/hi/ar/ru 的讀者看了多久的英文面板。檔案開頭的註解甚至還寫著「站上支援 zh-TW/en/ja/ko/es/fr」，是六種語言時代留下的。

六種語言各補一套完整字串，每套 45 個鍵，已驗證 12/12 語言鍵數齊全。

順帶補了一道閘門（\`npm run check:ui-lang\`，接上 pre-push 與 CI），專門查這個字串表有沒有落後語言註冊表。下次再加語言而忘了補字串，push 就會被擋下來，不用等讀者告訴我們。

🧬

---
title: 'Spore #170/#171 — v1.15.0 release 長出複眼'
spore_ids: '170 (threads), 171 (x)'
slug: 'release-v1150-milestone'
template: 'B 冷知識型（站方 meta 里程碑，viral family）'
hook_tier: '1b 具體性槓桿（讀者一句「怪怪的」＋複眼意象）'
date: 2026-08-11
---

### Spore #170/#171 Fact Blueprint — v1.15.0 release 長出複眼

**Angle**：一個把自己翻成十二種語言的 AI 知識庫，最重要的修復全來自讀者的眼睛——這一版學會「長出複眼」
**Template**：B（冷知識 / meta 自述）
**Ethical flags**：無

| #   | 事實（在孢子出現順序）                                     | 信度層          | 需跨源驗證？                    | 敏感度 | ✅/⚠️/❌ | 來源                                                                             |
| --- | ---------------------------------------------------------- | --------------- | ------------------------------- | ------ | -------- | -------------------------------------------------------------------------------- |
| 1   | 十七天（v1.14.0 7/26 → v1.15.0 8/11）                      | high_confidence | No（git tag 實數）              | 無     | ✅       | git tag v1.14.0 / v1.15.0                                                        |
| 2   | 十二種語言、多了三千多篇譯文（+3,089）                     | high_confidence | No（vitals 實算）               | 無     | ✅       | dashboard-vitals.json v1.14.0 tag 5,675 → 現行 8,764                             |
| 3   | 日文版把「台灣」寫成繁體字形，讀者回報後改回「台湾」       | high_confidence | No（issue + commit）            | 無     | ✅       | issue #1306/#1307 + commit `cd49a1be3`                                           |
| 4   | 十三個假陽性家族（自己造的品質閘門誤殺自己的合格譯文）     | high_confidence | No（release notes 已對 commit） | 無     | ✅       | commit 序列（第十/十一/十二/十三家族 + 先前九個）                                |
| 5   | 幾十支自動檢查器                                           | high_confidence | No（article-health 25 plugin+） | 無     | ✅       | `article-health.py --list-checks` 25+ 其他獨立檢查器                             |
| 6   | 吳明益寫過《複眼人》；複眼＝許多小眼各看一方向拼成完整視野 | high_confidence | 讀者級（書名/作者維基可查）     | 無     | ✅       | 《複眼人》2011 夏日出版／新經典文化；複眼＝昆蟲複眼生物常識                      |
| 7   | 新版本名「長出複眼」                                       | high_confidence | No（本 session ship）           | 無     | ✅       | [v1.15.0 release](https://github.com/frank890417/taiwan-md/releases/tag/v1.15.0) |

**刻意不寫**（查證成本 / 密度考量）：俄文介面烏克蘭文誤植（「看了半年」時長 claim 與 ru 7/25 出生日對不齊，時長不可靠→整條不進孢子）；六語 27%→82%（數字密度已滿）；NVIDIA 演講與天下專題（單一故事弧線紀律，release notes 有完整版）。

### 孢子本體（Threads 主貼 = X 主文）

```
你知道嗎？👀

台灣有一個 AI 知識庫叫 Taiwan.md，這十七天把自己翻成十二種語言，多了三千多篇譯文。但同一段時間最重要的幾個修復，全部來自讀者的一句「怪怪的」。

日文版把「台灣」寫成繁體字形，讀者一眼抓到。它為了守住品質自己造的十三道閘門，其實一直在誤殺自己的合格譯文。幾十支自動檢查器沒有一支攔到這些事，因為自己造的尺，量的都是自己看得見的那一面。

小說家吳明益寫過《複眼人》：一顆單眼看不見的東西，要靠幾百顆小眼各看一個方向，拼起來才是完整的世界。這個知識庫把剛發布的新版本命名為「長出複眼」，把記者、聽眾、讀者的眼睛一顆一顆接進身體。

你的那一眼，就是下一顆小眼。
```

### 雙平台 UTM URL

- Threads self-reply：`完整故事 👉 https://taiwan.md/about/?utm_source=threads&utm_medium=spore&utm_campaign=s170`
- X inline：`完整故事 👉 https://taiwan.md/about/?utm_source=x&utm_medium=spore&utm_campaign=s171`

（/about/ 全 ASCII path，無需 encode；timeline 最新節點即 v1.15.0 里程碑）

### Ship log

- 2026-08-11 哲宇 directive「release 孢子」（RELEASE-PIPELINE Step 7b）
- 配圖：無（站方 meta 里程碑孢子，非文章孢子；make-spore.sh 為文章頁設計，/about/ 非其輸入域）
- 2026-08-12 00:0x ship 完成：
  - Threads #170 主貼 `https://www.threads.com/@taiwandotmd/post/Db591ugI6tB`（295/295 字零丟失、5 段、hook 獨立行）+ self-reply s170 UTM（container 1→2 baseline diff 驗證）
  - X #171 `https://x.com/taiwandotmd/status/2087208201729249614`（sent alert + canonical href 最強訊號；inline s171 UTM）
  - CI/CD wait gate：發文前 curl prod `/about/` 確認「長出複眼」節點已上線
  - Revise 一輪後重跑 `--check=spore-writing` hard=0 warn=0（v3.15 鐵律）
  - 貼字走 JXA NSPasteboard + Cmd+V（多段中文 SOP）；發佈按鈕全程 JS/ref click（dpr 1.8 避 Pitfall 7）

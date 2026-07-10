---
title: '2026 選舉關聯頁面：七月刷新實錄 + 選前四個半月進化計畫'
description: '哲宇 /goal「深度研究＋深度分析＋寫計劃進化＋更新 2026 選舉所有關聯頁面並完整實作」的執行報告。本次已 ship：總章 v1.1 全文事實刷新（修 6 個事實錯誤 + 三個制度新變數）、/elections/2026 六語補齊 + 選務時程區塊、nav 修復、ARTICLE-INBOX 對賬。往前看：M4 動態頁、Tier 1.2/1.3、選前 freshness 節奏的完整計畫。'
date: 2026-07-10
type: 'evolution-plan'
status: 'shipped-and-pending-observer-review'
author: 'Taiwan.md (semiont)'
audience: 'observer-frank890417'
session_id: '2026-07-10-224934-elections-refresh'
upstream_canonical:
  - 'reports/2026-election-evolution-proposal-2026-05-27.md'
  - 'reports/politics-hub-elections-2026-architecture-2026-05-27.md'
related:
  - 'reports/research/2026-07/elections-2026-july-refresh.md'
  - 'knowledge/Politics/2026 九合一選舉.md'
  - 'src/templates/elections-2026.template.astro'
---

# 2026 選舉關聯頁面：七月刷新實錄 + 選前四個半月進化計畫

> 哲宇 directive 2026-07-10：「深度研究＋深度分析＋寫一個計劃進化＋更新『2026選舉』所有關聯頁面 https://taiwan.md/elections/2026/ 並完整實作」。
>
> 本檔分三部分：一、選舉器官現況體檢（audit 發現什麼）；二、本 session 已實作清單；三、選前四個半月的進化計畫（等哲宇拍板的部分明確標出）。研究溯源：[reports/research/2026-07/elections-2026-july-refresh.md](research/2026-07/elections-2026-july-refresh.md)。

---

## 一、體檢：選舉器官在 7 月 10 日的真實狀態

M1-M8 roadmap（[architecture spec](politics-hub-elections-2026-architecture-2026-05-27.md)）走到哪了：

| Milestone                                    | 狀態                   | 備註                                                                     |
| -------------------------------------------- | ---------------------- | ------------------------------------------------------------------------ |
| M1 Politics Hub + nav                        | ✅ 5/27 shipped        | 本次修 3 處事實 + 4 個壞 wikilink                                        |
| M2 /elections/2026 MVP + 總章                | ✅ 5/27-6/10 shipped   | 本次大幅刷新（見 §二）                                                   |
| M3 Tier 1.1 八篇制度文章                     | ✅ 5/27 shipped（8/8） | **ARTICLE-INBOX 漏標 done** → rewrite-daily PICK 空轉 6+ cycle，本次對賬 |
| Tier 1.4 政黨政治 EVOLVE                     | ✅ 5/27 shipped        | 同樣漏標，本次對賬                                                       |
| M4 動態子頁（timeline/candidates/financing） | ⬜ 未建                | timeline 本次以 index 區塊先行落地；candidates/financing 見 §三          |
| M5 Tier 1.2 縣市政治版圖 + SSODT 試水溫      | ⬜ [B]/[B] 等 nod      | 見 §三                                                                   |
| M7 Tier 1.3 候選人頁                         | ⬜ [C] 等 pick         | 見 §三                                                                   |

### audit 抓到的問題（全部已修）

**事實錯誤 6 個**（shipped 內容裡）：

1. 總章「第 11 次直轄市長選舉」→ 實為**第 9 屆**（1994 起 9 次，維基逐字）
2. 總章 + Hub 兩處「2022 高雄市長罷免」→ 韓國瑜罷免是 **2020-06-06**（中選會官方頁）
3. 總章時程表「8/29-9/04 登記」→ 中選會第 622 次會議決議是 **8/31-9/4**
4. 總章把「民調禁止公布期」放進選前 30 天段 → 《選罷法》§53 是**投票日前十日**（選舉過程.md 寫對了，兩文互相矛盾）
5. 模板眉標「中華民國**第十一屆**地方公職人員選舉」（四語同錯）→ 官方名稱是「中華民國 **115 年**地方公職人員選舉」（第十一屆疑似民國 111 年=2022 的幻覺轉換）
6. 政治獻金透明度.md 正文殘留「[NEEDS-VERIFY]」標記上線 → 已驗證（政治獻金法 2018 後未修）並清除

另有兩處「投票時間 08:00-16:00」寫成既定事實 → 2026 投票時間其實**尚未官方公告**（載於 8/20 選舉公告），已全部改「以選舉公告為準（歷屆慣例 8-16 時）」。

**結構問題 3 個**：

7. Header 兩處硬編 `href="/elections/2026"` + `singleLangPaths` 殘留 → PR #1166 已 i18n 化頁面但 nav 沒跟上，**en/ja/ko 讀者從 nav 一律被導去中文頁**
8. fr/es 選舉頁整頁缺席 → 主權巴別塔六語缺兩語
9. ARTICLE-INBOX Tier 1.1/1.4 status 停在 `pending` → **twmd-rewrite-daily 連續多 cycle PICK 到已 ship 的任務再 capacity-defer**（memory 2026-07-10-011120/191112 的「選舉 Tier 1.1 #1 保留」就是這個 stale status 的空轉）

**時間錨陳舊一批**：「從現在（2026-05-27）還有六個月」「距離投票還有六個月」×3、lastVerified 全停 5/27、「選前 18 個月」誤植 ×2。

---

## 二、本 session 已實作（全部 shipped）

### 內容層

- **總章 v1.1**（`knowledge/Politics/2026 九合一選舉.md`）：上述錯誤全修 + 30 秒概覽補齊 + 三塊新內容——
  - §三 (3)(4) 改寫：查察建制化（5/25 最高檢執行小組揭牌、6/5 北檢深偽處理中心、6/8 Polymarket 首宗偵結、6/30 北檢 37 件）+「實際攻擊長什麼樣」（6/15 假快訊洗版 383 則、NewsGuard 294 假帳號、淺層偽造取代深偽、韓國選務謠言移植——研判類敘述全帶限定語）
  - §四 藍白協議段更新：機制實際運轉一輪（嘉義市首例民眾黨人選出線、新北/宜蘭國民黨人選出線、嘉義縣禮讓無黨籍變形、彰化金門摩擦點）——**全程黨層級與機制層，不點候選人名**（對稱原則）
  - §九 重寫為「已發生/將發生」：三個制度新變數（公投綁大選回歸但無案成案、原民移轉投票 + 通用不在籍未過 + 8,896 種選舉票、選罷法 §26 七月生效）+ 提名版圖黨層級摘要（19/22、7/22 徵召計畫、13 縣市確定換人）+ 法定時程六節點（民調禁令歸位到前十日）
  - 15 個新腳註 + 3 個弱腳註升級（generic 首頁 URL → 具體報導）
- **Politics Hub v1.1**：韓國瑜年份、公投綁大選 2025 修法回歸、查察建制化、4 個壞 wikilink（[[g0v]]→管道語法、ARTICLE-INBOX 內部指標與兩個待寫佔位→純文字）
- **村里長制度 / 政治獻金透明度**：時間錨 evergreen 化 + NEEDS-VERIFY 解除

### 站體層

- **/elections/2026 模板**：六語齊（新增 fr/es 全套 copy + 路由頁）、眉標官方名稱修正（四語）、投票時間 claim 撤下（六語 dateLabel）、**新增「選務時程」區塊**——中選會第 622 次會議八節點 + build-time 進度狀態（已完成 ✓ / 下一站，台北時區日界）+ 來源註記
- **Header nav**：兩處硬編 → `navHref()`（filesystem-derived、各語言到各語言頁、缺語 fallback zh）+ 移除 `singleLangPaths` 死碼
- **ARTICLE-INBOX**：Tier 1.1/1.4 標 `done` + reconcile 註記（附 rewrite-daily 空轉證據 pointer）

### 認知層

- 研究 fact-pack 落檔：[reports/research/2026-07/elections-2026-july-refresh.md](research/2026-07/elections-2026-july-refresh.md)（三 agent 彙整 + 主 session 逐項跨源驗證 + 未能確認清單）

---

## 三、選前四個半月的進化計畫

時間結構決定工作節奏：**8/20 公告、9/4 登記截止、10/23 抽籤、11/28 投票**。每個法定節點都會讓一批「未定」變「已定」，計畫按節點排。

### 現在 → 8/20（自主可做 [A]，部分已排）

1. **總章媒體增補 EVOLVE**：總章 8,000 字 0 圖，是 image-health hard gate 唯一未過項（gate 在文章 ship 後才升級）。走 Step 1.9 深度媒體掃描（中選會開票影像 PD、投票所歷史照、g0v 工具截圖）。~2hr，建議下一個 rewrite-daily cycle 接（ARTICLE-INBOX 已因對賬釋出 PICK 空間）。
2. **選舉頁 freshness 節奏**：本次時程區塊是 build-time 計算，站點每日 rebuild 自動翻進度——不需要新 cron。但「新聞層」事實（提名變動、公投案進度）需要人工節點：建議**每月一次選舉 EVOLVE mini-cycle**（8 月中、9 月中、10 月中、選前週），每次 ~1hr 對總章 §九 + 時程區塊做增量更新。可掛進既有 rewrite-daily 的 PICK 邏輯（inbox 加一條 recurring entry）而不是新開 routine。
3. **[[台灣公投制度]] 補寫**（Hub 兩處待寫佔位之一）：公投綁大選 2025 回歸 + 2025-08-23 核三公投 + 2018 十案史——是 Politics 分類當前最大的 evergreen 缺口，而且 8 月「公投是否綁上 11/28」定案時它會變熱。P1 建議。〔另一篇 [[台灣事實查核生態]] P2〕

### 8/20 公告後（等官方資料，[A]/[B] 混合）

4. **時程區塊補投票時間 + 正式員額**：公告發布當天更新（總章 §一表格同步）。[A]，~30min。
5. **M4 `/elections/2026/candidates` 候選人 directory**：9/4 登記截止 + 11/12・11/17 官方名單公告後，接中選會資料做 22 縣市對稱呈現（架構 spec §3.3 五鐵律：全列、筆畫/號次排序、同版型卡片、無民調、無 framing 詞）。**[B] 需哲宇 nod 整個 M4**——建議 9 月中啟動，data source 先用 11/12 官方公告名單（比自行彙整登記資訊更乾淨、零對稱風險）。
6. **M4 financing**：監察院平臺的選前申報資料有限（多數在選後），建議降級為「工具導引 + 制度解說」頁而不是 dashboard（proposal 5.3 過度 instrument 化風險的自我校正）。[B]。

### 需要哲宇拍板的兩大內容工程

7. **Tier 1.2 — 22 縣市政治版圖 EVOLVE batch**〔[B]，~22hr，integral ship〕：制度 baseline（Tier 1.1）已全數到位五週，這是 proposal 裡價值最高的未啟動工作。選前做完的話，讀者查任何縣市都有「為什麼這裡的選舉這樣選」的脈絡層。**建議 nod 後 7 月下旬-8 月分 2-3 個 session 完成**（對稱原則要求 22 篇齊了才 ship，越晚啟動越擠）。
8. **Tier 1.3 — 候選人人物頁**〔[C]，逐篇 pick + 對稱成對〕：提名版圖已大致底定（研究 fact-pack 有 22 縣市完整表），如果要做，7-8 月是資訊最穩定的窗口；不做也完全成立（M4 directory 已提供對稱的事實層入口）。**等哲宇 pick；預設不做**。

### 選後（11/28 之後，寫進計畫先卡位）

9. **M8 retrospective**：/elections/2026 archive 化、選舉專用內容的 apoptosis 評估、2028 reusable 萃取——architecture spec 已有完整設計，選後一週內執行。

### 不做清單（明確排除）

- ❌ 候選人名單自行彙整表（登記前的提名動態日日在變，人工維護必然出現不對稱瞬間 = endorsement signal 風險；交給 8/20 後的官方資料）
- ❌ 民調資訊任何形式的呈現（proposal 鐵律）
- ❌ 選舉即時新聞層（傳統媒體的戰場，Taiwan.md 是策展層）
- ❌ 新 cron routine（現有 rebuild + rewrite-daily PICK 已足夠承載選舉 freshness，routine 飛輪不加條）

---

## 四、風險與教訓

- **stale status 會讓 routine 空轉**：Tier 1.1 shipped 六週但 inbox 未標 done，rewrite-daily 反覆 PICK→defer。教訓已寫 LESSONS-INBOX 候選：「ship 的人要同 commit 對賬 inbox status」。
- **quality gate 升級會讓舊 ship 內容變 hard-fail**：總章 5/27 合規、7/10 已 0 媒體 hard——gate 演進後的存量掃描（哪些舊文被新 gate 抓）值得進 self-evolve-weekly 的視野。
- **「預計」與「已發生」的線**：國民黨 6 現任者 7/22 徵召是計畫非事實，本次所有表述都帶「預計」；8 月更新時要回頭驗證。
- **研判類 claim 的限定語**：6/15 洗版與 NewsGuard 的「選舉意圖」都是機構研判，prose 全帶「研判」——這條紀律要在後續每次選舉更新中維持。

🧬

---

_v1.0 | 2026-07-10 | session 2026-07-10-224934-elections-refresh_
_誕生原因：哲宇 /goal 深度研究＋分析＋計畫＋完整實作。三個研究 agent（提名/法制/資訊環境）+ 主 session 跨源驗證 + 全器官 audit + 當日實作 ship。_
_給下一個 session：§三 的 1-3 條 [A] 可自主接走；5-8 條等哲宇 nod/pick；8/20 公告日是下一個必然的更新節點。_

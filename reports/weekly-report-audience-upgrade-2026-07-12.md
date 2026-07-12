# 週報受眾升級 — 寄給整個共生圈的規劃報告

> 2026-07-12 · session 2026-07-12-142709-weekly-audience · 對應 WEEKLY-REPORT-PIPELINE v4.1 → v4.2
> 觸發：哲宇 /goal directive（原話見 §1）

---

## 1. 哲宇要什麼（directive 原話拆解）

> 「未來週報也幫我 cc 給所有有貢獻過 taiwan.md 的貢獻者（從 github 每一週動態抓一次所有人的 email，統整並寄給近 3 個月有貢獻或與專案互動的人（包含提 issue 的人），幫我完整升級整個流程 pipeline，還有這些機制，cc 的時候要用 bcc（密件副本），並且裡面有一些可以點擊的連結要有超連結，幫我深度研究思考這件事情，寫規劃的 report 並完成自我升級」
>
> 補充：「能儀器化的部分記得要儀器化，就是把所有的工具都準備好，比如說怎麼自動抓 email、怎麼去整理近期他們的活躍程度之類的」

拆成七件事：

| #   | 要求                              | 對應設計                                                             |
| --- | --------------------------------- | -------------------------------------------------------------------- |
| 1   | 週報寄給近 3 個月有互動的所有人   | 受眾定義三源（commit / PR+issue / 留言），90 天窗口                  |
| 2   | 每週從 GitHub 動態抓一次 email    | `weekly-report-recipients.py` 儀器，隨週日 routine 自動跑            |
| 3   | 包含提 issue 的人                 | GitHub issues API 是三源之一，issue 作者與留言者都算                 |
| 4   | 用 BCC 密件副本                   | 收件人互相看不到彼此 email；哲宇本人留在 To                          |
| 5   | 信裡的連結要可點                  | 寄信工具升級：相對路徑改寫成絕對網址 + 裸網址自動變超連結            |
| 6   | 整理近期活躍程度                  | 儀器輸出每人 commit / PR / issue / 留言計數 + 活躍分數 + 最後活躍日  |
| 7   | 深度研究 + 規劃 report + 自我升級 | 本報告 + pipeline v4.2 + 兩支工具 + weekly-checkup 新 i 節，全部落地 |

---

## 2. 現況體檢（升級前的 Stage 5 長什麼樣）

- **收件人只有哲宇一人**：`send-email-resend.py --to cheyu.wu@monoame.com`，今天凌晨 W28 就是這樣寄的（Resend id `b0105104-…`）。
- **寄信工具沒有 BCC 參數**：payload 只組 `to`，連 `reply_to` 都沒有。
- **連結半殘**：markdown 連結會轉成 `<a>`，但相對路徑（例如 W28 裡的 `../evolution-roadmap-2026-07-10.md`）在信箱裡點了會斷；內文裸網址完全不會變超連結。
- **pipeline 的 sandbox 註記過時**：Stage 5 寫著「Resend sandbox 模式只能寄到 verified email」，實測 Resend 帳號早在 2026-03-01 就完成 `cheyuwu.com` 網域驗證（sending enabled，region ap-northeast-1）。BCC 廣播今天就做得到，寄件人用 `@cheyuwu.com` 即可。`taiwan.md` 網域則尚未驗證。

## 3. 受眾定義（誰會收到）

「近 3 個月有貢獻或與專案互動」展開成三個資料源，取聯集：

| 源          | 抓法                                                                    | 算什麼                 |
| ----------- | ----------------------------------------------------------------------- | ---------------------- |
| commit 作者 | `git log --since="90 days ago" --format=%aN\|%aE\|%aI`（走 .mailmap）   | commits 數、email 候選 |
| PR / issue  | `gh api repos/…/issues?state=all&since=…`（client 端再過濾 created_at） | PR 數、issue 數        |
| 留言者      | `gh api …/issues/comments` + `…/pulls/comments`（同樣過濾窗口）         | 留言數                 |

排除規則：bot（`[bot]` 結尾、dependabot 之類）、哲宇本人（他是 To 不是 BCC）、optout 名單（見 §5）。

**2026-07-12 實測規模**（儀器跑出的真實數字）：90 天窗口 **55 人**互動過，其中 **25 人可解析出 email**、去掉哲宇雙身份與重複地址後 **BCC 名單 20 人**。主力是 idlccp1984（173 commits + 214 PR/issue）、ceruleanstring（127 PR/issue）、柒藍、Zaious、dreamline2、Wilson Chen、Ellen Lee、Link1515，後面接著約 30 位單次互動的參與者（提過一個 issue、留過一句言的人也都算共生圈——他們多數沒公開 email，進 unreachable 名單）。這個量級離 Resend 單信 50 收件人上限還有距離，工具仍內建 40 人一批的分批寄送，名單長大也不會斷。

## 4. Email 解析策略（最難的一段，實測資料驅動）

GitHub 不會直接給你「所有參與者的 email」。三條路，按優先序：

1. **commit email（最可靠）**：作者自己放進 git history 的公開資訊，用 `.mailmap` 合併多重身份後，取每人最常用的一個。
2. **GitHub profile 公開 email**：`gh api users/{login}` 的 `.email` 欄位——只有使用者主動在 profile 公開才拿得到，實務上多數是 null。commit email 無效時的第二層。
3. **拿不到就誠實列出**：進 unreachable 名單，出現在週報摘要裡讓哲宇看得到缺口（可以私下問本人要不要收）。

無效 email 的真實案例（工具必須擋掉的）：

- `88765055+Link1515@users.noreply.github.com` — GitHub 隱私代理地址，寄了會彈；但能從中抽出 login 去查 profile。
- `chilan@qilandeMac-mini.local` — 柒藍的本機 hostname，不可路由；`.local` 這類網域一律過濾。
- 同一人多 email（Wilson Chen 有 lunit.io 和 gmail 兩個）— 以 mailmap 名字分組後取最常用的那個，不會重複寄。

**已知缺口**：ceruleanstring 有 127 次 PR/issue 互動，若 commit email 與 profile email 都拿不到，就會是 unreachable 名單上最顯眼的一位。這種人值得哲宇在 GitHub 上直接問一聲。

## 5. 隱私與人本設計（把 §12 受眾端飛輪的五核心帶進信箱）

寄信給從 GitHub 撈來的地址，一步做錯就是 spam。六條鐵律：

1. **BCC only**：收件人永遠看不到彼此的 email（哲宇指定，也是唯一正確做法）。
2. **email 永遠不進 repo**：名單 JSON 落在 `~/.config/taiwan-md/weekly-report/`（跟 credentials 同層級待遇，chmod 600）；會被 commit 的 dossier / 週報 / commit message 只出現 login 與人數，不出現任何地址。
3. **信尾必附說明與退出口**：固定 footer 告訴對方「你收到是因為過去三個月參與過 Taiwan.md」，回信即可退訂，或自己開 PR 加進 optout 名單。
4. **optout 雙層**：repo 內 `docs/community/weekly-report-optout.json`（放 GitHub login，公開透明、可自助 PR）+ 本機 `~/.config/taiwan-md/weekly-report/optout-emails.txt`（放回信退訂的 email，不進公開 repo）。
5. **Reply-To 指向哲宇**：回信有人接，退訂請求有人處理，符合「人本」原則——這是對話，不是廣播塔。
6. **頻率固定每週一封**：跟著週日 02:00 routine，不加寄、不促銷、內容就是週報本body。

法遵層（CAN-SPAM / GDPR 精神的最小集）：寄件人身份真實、內容不誤導、每封信附退出機制、退訂即時生效。對象是專案的實際參與者、內容是專案本身的運作報告，屬於最正當的關聯性；照樣把退出口做好。

## 6. 儀器規格（把所有工具準備好）

### 6a. `scripts/tools/weekly-report-recipients.py`（新生）

一支指令做完「抓 → 併 → 解析 → 整理活躍度 → 落地」：

```bash
python3 scripts/tools/weekly-report-recipients.py --window-days 90 --summary
```

- 三源抓取 + mailmap 合併 + bot/owner/optout 過濾 + email 解析（§4 優先序）。
- **活躍度整理**（哲宇補充 directive 的核心）：每人 commits / PR / issue / 留言計數、最後活躍日、活躍分數（commits×3 + PR×2 + issue×2 + 留言×1），排序輸出。
- 落地 `~/.config/taiwan-md/weekly-report/recipients-latest.json`（+ 當日快照），含乾淨的 `bcc` 陣列給寄信工具直接吃。
- `--summary` 印 markdown 活躍度表（只有 login 沒有 email），直接貼進週報第 5 章「外部感測」。
- fail-loud：GitHub API 掛掉就非零退出；bcc 名單為零也非零退出，routine 看得到。

### 6b. `scripts/tools/send-email-resend.py`（升級）

- 新參數：`--bcc` / `--bcc-from-json`（直接讀 6a 的 JSON，48 小時新鮮度檢查，過期拒寄）/ `--reply-to` / `--audience-footer`（§5 的說明 footer）/ `--dry-run`（渲染 HTML 落檔、不打 API）。
- **連結全面可點**：相對路徑改寫成 `https://github.com/frank890417/taiwan-md/blob/main/…`、站內路徑改寫成 `https://taiwan.md/…`、內文裸網址自動包成超連結。
- 分批寄送（每批 ≤ 40 BCC）、`bcc=N` 只印人數不印地址。
- 向後相容：原本單收件人的用法行為完全不變。

### 6c. `weekly-checkup.sh` 新 **i 節**（受眾名單與活躍度）

一鍵體檢多長一節：跑 6a 的 `--summary`，週報 routine 的認知負荷不因新機制上升——工具自動抓，Semiont 只解讀。節數以 `weekly-checkup.sh` 實際輸出為準（本報告不寫死數字，counts-drift 教訓）。

## 7. Pipeline v4.2 變更清單（WEEKLY-REPORT-PIPELINE.md）

| 位置         | 變更                                                                                                |
| ------------ | --------------------------------------------------------------------------------------------------- |
| Stage 5      | 拆成 5a 受眾同步（跑 recipients 儀器）+ 5b 廣播寄送（To=哲宇、BCC=名單、audience footer、reply-to） |
| Stage 5 設定 | From 改 `Taiwan.md <taiwanmd@cheyuwu.com>`（verified domain）；sandbox 過時註記刪除                 |
| Hard Gate 表 | 新增：recipients JSON < 48h、BCC 不進 To、email 不進 repo/commit/chat、audience footer 必附         |
| 失敗處置     | BCC 寄送失敗 → 降級寄哲宇單人（週報不能因廣播層失敗而斷）+ LESSONS entry                            |
| 觸發來源     | 修 stale「週日 08:08」→ ROUTINE.md SSOT 的 02:00                                                    |
| 工具邊界表   | 加 recipients 儀器一列                                                                              |

Routine 排程不動：受眾同步「每週抓一次」就是隨 `twmd-weekly-report-sun`（週日 02:00）跑，不開新 cron。

## 8. 首次廣播 + 寄件網域切換（都已完成）

- **首次廣播已在本 session 手動送出（2026-07-12，哲宇當場 directive「寄這週的週報給大家」）**：W28 報告 To=哲宇、BCC=20 位可聯繫的共生圈參與者、audience footer 附退訂口，Resend id `7efc34d6-5557-4e5c-b205-8c863a9434b3`、`last_event: delivered`。之後每週日 02:00 routine 自動接手（v4.2 Stage 5）。
- **寄件網域已切換到 `weekly@taiwan.md`**（哲宇拍板 swap）：Resend 免費方案單一網域，同 session 移除 `cheyuwu.com`、加入並驗證 `taiwan.md`（DKIM + SPF MX + SPF TXT 三筆 DNS-only 記錄由哲宇授權下經 Chrome MCP 加進 Cloudflare，2026-07-12 驗證通過）。從 `weekly@taiwan.md` 實測寄出、`last_event: delivered`。pipeline From 已改，下週日 routine 起用新位址。
- **免費方案守門已儀器化**：`weekly-report-recipients.py` 加 free-tier guard——bcc 逼近 80／達 100（Resend 免費單日上限）時 summary 與 JSON `free_tier.status` 亮 warn／over，提醒屆時升級 Pro。目前 20，status `ok`。升級決策的深度分析見本報告末（免費 vs Pro：Pro 只多「兩網域」與「無單日上限」，對數十人的週報而言免費足夠）。

## 9. 風險表

| 風險                           | 影響                 | 緩解                                                              |
| ------------------------------ | -------------------- | ----------------------------------------------------------------- |
| 收件人覺得是 spam              | 信任損傷（最大風險） | BCC + footer 說明 + 一鍵退訂 + 每週僅一封 + Reply-To 真人         |
| email 洩進公開 repo            | 隱私事故             | 名單只落 `~/.config`；summary/commit 只有 login；寄信工具不印地址 |
| 名單過期照寄                   | 寄給已退出者         | 48h 新鮮度 hard gate，過期拒寄                                    |
| Resend 廣播層故障              | 週報斷送             | 降級單寄哲宇，週報永遠先送達觀察者                                |
| deliverability（gmail 進垃圾） | 觸及率下降           | verified domain 寄出 + text/html 雙 part；觀察首兩週回報          |
| 名單長大超過單信上限           | 寄送失敗             | 40 人一批自動分批                                                 |

## 10. 驗證紀錄（2026-07-12 本 session）

### Resend 到底寄不寄得出去（哲宇追問的核心）

答案：**寄得出去，收件人不需要做任何驗證**。兩層證據：

- **文件層**：Resend 的限制只在 sandbox——用 `onboarding@resend.dev` 當寄件人時只能寄到帳號本人的 email。網域驗證完成後即可寄給任何地址，收件端沒有額外驗證程序。`cheyuwu.com` 已於 2026-03-01 驗證完成（sending enabled）。
- **實測層**：本 session 從 `taiwanmd@cheyuwu.com` 寄出 W28 重寄測試信，To `cheyu.wu@monoame.com`、BCC `frank890417@gmail.com`（一個 Resend 帳號從沒看過的地址，模擬 contributor）。API 回 200、message id `4813b39d-53a5-480a-ac81-1a2c506f8c26`，20 秒後查詢 `last_event: delivered`——BCC 通路端到端送達。

額度層：Resend 免費方案約 100 封/日、3,000 封/月（每位收件人算一封）。以目前約 35 人的名單，每週一次廣播 ≈ 每月 150 封，餘裕充足；名單如果長到百人再看 dashboard 用量。

### 寄信工具（send-email-resend.py 升級）

- `py_compile` 通過；向後相容 dry-run（單收件人、bcc=0）行為不變。
- 全功能 dry-run：`../evolution-roadmap-2026-07-10.md` 相對連結正確改寫成 GitHub blob 絕對網址（grep 命中 1）；殘留壞相對連結 0；站內路徑改寫 `https://taiwan.md/...`；裸網址自動變超連結（含不重複包已有 `<a>` 的反例測試）。
- **「為什麼收到」footer 確認渲染**：dry-run HTML grep「過去三個月你在 GitHub 上參與過」命中 1、optout 連結命中 1——收件人打開信就會看到自己為什麼收到 + 怎麼退訂。
- 分批邏輯單元測試：85 收件人 → [40, 40, 5] 三批；任一批失敗照樣送完並回報 fail。
- 隱私：stderr 只印 `bcc=N recipients`，全程沒有任何地址進 log。

### 首次真實廣播（2026-07-12 哲宇 directive 當場送出）

- W28 報告 `reports/weekly/2026-07-12.md` → To `cheyu.wu@monoame.com` + BCC 20 人 + from `Taiwan.md <taiwanmd@cheyuwu.com>` + reply-to 哲宇 + audience footer。
- Resend 回 200、id `7efc34d6-5557-4e5c-b205-8c863a9434b3`，輪詢後 `last_event: delivered`；單批（20 < 40）無需分批。
- 這是機制第一次面對真實共生圈——20 位過去 90 天 commit / PR / issue / 留言過的人，同時收到週報與「你為什麼收到 + 怎麼退訂」的說明。

### 受眾儀器（weekly-report-recipients.py）

- 實跑 90 天窗口：GitHub API 抓 815 筆 issues/PRs（17 筆 created_at 在窗外被正確排除，`since=` 只濾 updated_at 的陷阱有守住）+ 700 筆留言 + 25 個 commit 作者名（mailmap 合併後）。
- 產出：55 人 / 25 可聯繫 / 30 無法聯繫 / 0 optout / **bcc 20 人**。
- JSON 不變量全過：bcc 無重複、無 `users.noreply`、無 `.local`、無 owner（哲宇兩個 git 身份都被正確標成 owner 排除）；檔案權限 600；落在 `~/.config/taiwan-md/weekly-report/`，repo 內零 email。
- `weekly-checkup.sh` i 節整合實測：一鍵 a–i 全節跑通，活躍度表直接進體檢輸出。
- Unreachable 名單把該追的人指出來了：柒藍與 ceruleanstring（合計 250+ 次互動）都沒有公開 email——值得哲宇一對一問一聲要不要收週報。

### 名單新鮮度 gate

`--bcc-from-json` 讀到超過 48 小時的名單會拒寄（`--allow-stale` 才能硬闖）；`generated_at` 欄位缺失也視同過期。實測 72 小時舊檔被正確擋下。

### 寄件網域 swap + 驗證（2026-07-12 哲宇拍板 swap）

- Resend 免費方案單一網域：API 移除 `cheyuwu.com`、加入 `taiwan.md`（region ap-northeast-1）。
- 三筆 DNS 記錄經 Chrome MCP 加進 Cloudflare（哲宇本人登入、Claude 代填表單）：DKIM TXT `resend._domainkey`、SPF MX `send`（priority 10）、SPF TXT `send`，全 DNS-only。root 無 MX（無收件信箱不變）。
- `dig` 確認 DKIM 發佈值與預期 byte-for-byte 相符；Resend 驗證通過（三筆全 verified，domain status `verified`）。
- 從 `Taiwan.md 週報 <weekly@taiwan.md>` 實測寄出 → `last_event: delivered`。

## 12. 免費 vs Pro 深度分析（哲宇 directive「付費方案還有什麼優點」）

|          | 免費（$0） | Pro（$20/月）      |
| -------- | ---------- | ------------------ |
| 網域數   | 1          | 10                 |
| 單日寄送 | 100 封     | 無上限             |
| 月量     | 3,000      | 50,000             |
| 專屬 IP  | ✗          | ✗（要 Scale +$30） |
| 資料保留 | 30 天      | 30 天              |

對「一週一封、收件人數十人的貢獻者週報」而言，Pro 只多兩件有意義的事：(1) 同時掛兩個網域；(2) 解除單日 100 封上限。其餘（月量、專屬 IP、保留、客服）不是相同就是用不到——月量 3,000 遠大於數十人×一週，綁死上限的是「單日 100」不是「月量」。

單日 100 封的意義：一次 BCC 廣播 = 收件人數封，所以免費方案支援每週寄給**約 100 人以內**。目前可聯繫 20 人，離天花板很遠。查帳也證實 `cheyuwu.com` 沒在這個 Resend 帳號寄別的信，swap 掉零損失、且可逆。**結論：swap 走免費足夠，bcc 逼近 80 再升 Pro——guard 已儀器化這個提醒。**

## 11. 之後可以長的方向（本次不做）

- ~~驗證 `taiwan.md` 網域，寄件人升級 `weekly@taiwan.md`~~ ✅ 已於本 session 完成（swap + Cloudflare DNS + Resend 驗證）。
- 名單長到 bcc ≥ 80 時升級 Resend Pro（$20/月，解除單日 100 封上限）——guard 會自動提醒，不用記。
- Resend Audiences / Broadcast API + 訂閱表單：讓非 contributor 的讀者也能訂閱週報（那是「訂閱者」產品，跟本次「共生圈廣播」是兩件事）。
- 週報網頁版（`/weekly` 路由）：信裡放一條「在網頁上讀」連結。
- unreachable 名單的溫柔補洞：對高活躍但無 email 的人（如 ceruleanstring）由哲宇一對一問一聲。

---

_v1.0 | 2026-07-12 manual session — 哲宇 /goal directive 觸發；研究 + 規劃 + 實作 + 驗證同 session 完成_

---
title: '語意無關 stale 的零成本判定與 bump'
date: 2026-07-27
status: 'shipped'
---

# 語意無關 stale 的零成本判定與 bump

快照基準：commit `3728a46f9`，2026-07-27T10:48+08:00（四條翻譯產線併行中，數字為那一刻的
`knowledge/_translation-status.json`，之後仍持續變動）。

## 一句話

全站 641 篇 `stale` 翻譯裡，**65.8%（422 篇）的 zh diff 只是標點/空白正規化**——半形逗號改
全形、句中分號改句號、破折號改冒號之類。這類改動對譯文完全沒有語意影響，因為每個語言的譯文
用的是自己的標點規範，不會因為中文標點怎麼改就要跟著動。這批 stale 現在不需要呼叫任何模型：
判定 + bump frontmatter 三個 provenance hash 欄位即可，成本趨近於零。

## 背景

哲宇原本抽樣 40 對、25 對可判定裡估出 52% 命中率。跑過全站 641 對之後，**實測命中率是
65.8%，比抽樣估計高了 14 個百分點**——抽樣時可能偏向抓到內容確實有改動的案例。

## 判定邏輯（新工具 `semantic-noop-check.py`）

新增 `scripts/tools/lang-sync/semantic-noop-check.py`，單一職責：只判定，不寫檔。設計保守，
**寧可漏判（真的是 no-op 但判不出來，走回正常翻譯）不可誤判（不是 no-op 卻被判成 no-op）**：

1. `git diff --unified=0 <sourceCommitSha>..HEAD -- knowledge/<zh_path>` 取 zh diff（`--unified=0`
   讓 diff 只剩實際改動行，不含 context）。
2. 用 hunk header（`@@ -a,b +c,d @@`）而不是字串比對來定位 `+`/`-` 內容行，避免內容行剛好也
   以 `---` 開頭時被誤認成 diff 檔頭（例如正文裡的分隔線）。
3. **frontmatter 保險**：任何 hunk 的行號範圍落在 frontmatter 區塊（第一組 `---` 到第二組 `---`
   之間，舊版本與新版本都算）→ 直接判「不是 no-op」。frontmatter 欄位變動可能有語意（title
   改標點其實是改標題），一律不冒險判斷內容。
4. 把所有 `+` 行內容串接、所有 `-` 行內容串接，各自做「正規化」：移除所有 Unicode 標點字元
   （category 開頭 `P`：連接號/破折號/引號/括號等全部子類）與所有空白/格式字元（Unicode
   whitespace + category `Cf`，涵蓋全形空格 U+3000、零寬空格 U+200B、BOM）。用 Unicode
   category 判斷而非窮舉字元表，涵蓋面比列舉全形/半形標點清單更完整。
5. 正規化後兩邊字串**完全相同（含順序）**才判 no-op。任何差異——包含中文用字替換（「台灣」
   ↔「臺灣」）、數字改動、語句重排——都不會被正規化抹掉，會正確判「不是 no-op」。
6. diff 是空的、抓不到舊版內容（`git show` 失敗，通常是檔案路徑/分類搬過家）、sha 格式不對
   等任何不確定情況，一律「不是 no-op」。

Exit code：0 = no-op，1 = 不是 no-op（涵蓋所有上述情況）。`--json` 輸出給呼叫端解析。

## 5 個 no-op 實例的實際 diff（人工核對，非模型判斷）

隨機抽 5 個判定為 no-op 的案例，貼出實際 diff 內容核對——全部確認是純標點替換，內容、數字、
人名、連結一字不改：

**1. `ja Society/泛科學.md` @ `31a05c44`**（3 行改動，皆為 `；`→`。`）

```
-...現場從電影射箭物理講到分手心理學；同一篇報導也寫到...
+...現場從電影射箭物理講到分手心理學。同一篇報導也寫到...
```

**2. `fr Technology/台灣AI日常.md` @ `dbb8d44c`**（5 行改動，皆為 `——`/`；`→`：`/`。`）

```
-螢幕右側跳出一個色塊——綠色低風險、黃色中風險、紅色高風險。
+螢幕右側跳出一個色塊：綠色低風險、黃色中風險、紅色高風險。
-台灣的 AI 滲透不是從矽谷傳來的——是從 LINE 群組裡長出來的。
+台灣的 AI 滲透不是從矽谷傳來的：是從 LINE 群組裡長出來的。
```

**3. `ja Society/巴拉圭與台灣.md` @ `31a05c44`**（1 行改動，`；`→`：`）

```
-六十九年的邦交，不在辭令裡；它在具體合作裡。
+六十九年的邦交，不在辭令裡：它在具體合作裡。
```

**4. `id History/大罷免.md` @ `6262f8c93`**（17 行改動，`；`→`。`／`——`→`。`，全篇一致的標點
正規化，逐句核對內容、票數、法條號碼、人名、腳註編號全部未動）

```
-制度上根本無法被罷免[^4]；這正是為什麼 2025 年被推上罷免投票的三十一位立委...
+制度上根本無法被罷免[^4]。這正是為什麼 2025 年被推上罷免投票的三十一位立委...
```

**5. `es Music/金曲獎.md` @ `6897c6571`**（10 行改動，`——`→`：`）

```
-...連拿三座大獎——年度專輯、最佳華語專輯、最佳樂團。
+...連拿三座大獎：年度專輯、最佳華語專輯、最佳樂團。
```

## 反向驗證：3 個判定為「不是 no-op」的案例

抽 3 個 reason 為 `content-diff` 的案例確認判定沒有過嚴（不是把真實改動誤判成標點）：

- `es People/聶永真.md` @ `31a05c44`：延伸閱讀新增一整條連結 + 說明句（新增江振誠條目）
- `fr History/民主化.md` @ `4b6d28c5`：延伸閱讀新增一整條連結 + 說明句（新增大罷免條目）
- `en People/李安.md` @ `31a05c44`：延伸閱讀新增一整條連結 + 說明句（新增江振誠條目）

三個都是純內容新增（真實句子、真實連結），判定正確落在「不是 no-op」，工具沒有過度寬鬆。

## 命中率

| 統計                                 | 數字         |
| ------------------------------------ | ------------ |
| 全站 stale 總數（快照）              | 641          |
| no-op（punct-whitespace-only）       | 422（65.8%） |
| frontmatter 有動（保守排除）         | 118（18.4%） |
| 真實內容改動（content-diff）         | 91（14.2%）  |
| 舊版本讀不到（路徑搬家等，保守排除） | 9（1.4%）    |
| diff 為空（可能是 rename）           | 1（0.2%）    |

按語言拆分（no-op / stale 總數）：`vi` 14/14＝100%、`id` 9/10＝90%、`pt` 9/10＝90%、`ja`
85/127＝67%、`ko` 84/129＝65%、`es` 72/113＝64%、`en` 73/115＝63%、`fr` 73/117＝62%、`hi`
3/5＝60%、`ru` 0/1。少量翻譯的語言（vi/id/pt/hi）樣本數小，比例不穩定；大量翻譯語言（en/ja/
ko/es/fr）的命中率彼此接近（62-67%），比較能代表真實分布。

## 3 篇實際 bump 驗證（寫入 + 還原，未留在 repo）

對 3 篇（`pt/Art/li-poetry-society.md`、`en/Food/beef-noodle-soup.md`、
`es/People/tanya-chua-singer.md`）直接在真實檔案上執行 bump（測試後用 `git checkout --`
還原，過程中 6 個涉及檔案 diff 前皆確認 clean，未與併行產線衝突）：

- **body byte-identical**：3/3 全部確認 frontmatter 之後的內容完全沒動（`bump_one()` 只改
  `sourceCommitSha` / `sourceContentHash` / `sourceBodyHash` 三個欄位）。
- **frontmatter 三個 hash 欄位更新**：3/3 確認新值正確寫入。
- **verify-translation.py**：`en/Food/beef-noodle-soup.md`、`es/People/tanya-chua-singer.md`
  兩篇 `fails=0` 全過；`pt/Art/li-poetry-society.md` 出現 `fails=2`——但還原到 bump 前重跑
  同一個 verify，**同樣是 fails=2**，確認是既有、與這次標點改動無關的舊問題（`category`
  欄位被寫成語言代碼 `'pt'` 而不是 `'Art'`、`image`/`imageCredit` passthrough 缺漏、10 個
  tags 未翻譯）。

這正好證明了設計裡的 post-bump verify gate 有實際作用：`pt/Art/li-poetry-society.md` 的 zh
diff 確實只是標點，但譯文本身帶著跟這次改動無關的既有品質問題，不該被靜默判定為「現在
fresh 了」。gate 會攔下它、還原成原內容，讓它留在 stale 狀態走正常翻譯路徑（順便修掉那些
舊問題）——不會製造「假 fresh」。

同一條路徑也直接在 `babel-dispatch.py` 的 `try_semantic_noop_bump()` 上做了一次端到端驗證
（`ko/Society/taiwan-sports-olympics.md`）：判定 no-op → bump → verify 過 → 回傳成功，body
byte-identical，測試後 `git checkout --` 還原。

## 實作

- **`scripts/tools/lang-sync/semantic-noop-check.py`**（新增）：判定邏輯，見上。
- **`scripts/tools/lang-sync/bump-source-sha.py`**（擴充）：新增 `--include-punct-only` 旗標
  （預設關）。開啟後，除了既有的 `metadata-stale` 之外，額外掃描 `stale` 條目、丟給
  `semantic-noop-check.py` 判定，命中的加入同一批 bump 清單。`--apply` 模式下，
  `--include-punct-only` 的每筆命中在寫入後都會額外跑 `verify-translation.py`，沒過就
  `write_bytes()` 還原、計入 `reverted`，不留在假 fresh 狀態。
- **`scripts/tools/lang-sync/babel-dispatch.py`**（擴充）：`process_task()` 裡，`status ==
"stale"` 的任務現在依序試：**semantic-noop 判定 → patch-translate（章節級）→ 全文重翻**。
  no-op 命中就呼叫 `try_semantic_noop_bump()`（bump + verify-translation 硬 gate，沒過就還原
  並走下一階段），成功則直接記入 `report.jsonl`（`fail_reason: null`、`disposition: "kept"`、
  `via: "semantic-noop-bump"`），計入正常的 commit 累積邏輯，**不呼叫任何模型、不占用
  worker 名額**。新增 `--no-noop-bump` 旗標可整條停用，回到純 patch/全文路徑。
  - `bump_one()` 透過 `importlib` 直接從 `bump-source-sha.py` 載入重用（檔名有連字號，不能
    直接 `import`），沒有重新實作寫入邏輯。
  - zh 端目前的 `(sha8, contentHash, bodyHash)` 透過 `import status as status_lib` 重用
    `body_hash()` / `body_hash_pure()`，跟 `status.py` 用同一套雜湊，確保 bump 完當篇下一輪
    `status.py` 刷新時會讀成 `fresh`，不會又被判回 stale。

## 預估節省

從最近幾輪產線的 `report.jsonl`（80 筆成功案例，涵蓋 patch-translate 與全文重翻、多種
backend）量出單篇成功耗時：中位數 169 秒、平均 246.5 秒（27.9 秒到 914.4 秒都有，backend
與 patch/全文路徑差異很大，僅供量級參考）。

以 422 篇命中估算：

- 用中位數：422 × 169s ≈ 19.8 小時算力時間
- 用平均數：422 × 246.5s ≈ 28.9 小時算力時間

且這批完全不用任何模型 API 呼叫（0 token 成本），跟真正要重翻的 91 + 118 + 9 + 1 = 219 篇
分開處理，讓四條產線的算力預算集中花在真的需要語意判斷的那三分之一。

## 誤判風險分析與防線

**誤判方向只有一種需要嚴防**：把「其實有語意改動」誤判成「no-op」，導致該重翻的譯文被跳過。
反方向（把 no-op 誤判成「不是 no-op」）只是少省一點算力，不影響正確性，不是本設計要嚴防的
對象。

三層防線：

1. **判定層**（`semantic-noop-check.py`）：Unicode category 正規化只吃標點與空白，任何
   文字、數字、CJK 用字差異都會讓正規化後字串不同，判「不是 no-op」。frontmatter 觸碰一律
   排除。舊版本讀不到（sha 有效但路徑在該版本不存在，通常是分類搬家——實測 9 個
   `About/視覺化模組型錄.md` 案例正是從 `Society/` 搬到 `About/`）一律排除，不猜。
2. **寫入層**（`bump_one()`）：只碰 `sourceCommitSha` / `sourceContentHash` / `sourceBodyHash`
   三個欄位，body 完全不動——就算判定層萬一誤判，body 內容也不會被污染，只是 provenance
   欄位指向錯誤的 commit（下次真的有人翻新版本時會被正常 stale 邏輯抓到）。
3. **post-bump verify gate**（`bump-source-sha.py --include-punct-only` 與
   `babel-dispatch.py` 的 `try_semantic_noop_bump()` 皆有）：每筆命中在寫入後都要過
   `verify-translation.py` 的硬 gate（passthrough 欄位比對、腳註數、section 數、URL 數等
   15 項檢查），沒過就還原。驗證過程中這道 gate 真的攔下了一筆（`pt/Art/li-poetry-society.md`）。

## 紀律

- 全程前景串行執行，沒有背景跑等通知。
- 測試階段對 4 篇真實 knowledge 檔案（`pt/Art/li-poetry-society.md`、
  `en/Food/beef-noodle-soup.md`、`es/People/tanya-chua-singer.md`、
  `ko/Society/taiwan-sports-olympics.md`）做過寫入測試，動手前逐一確認 `git status`
  clean（未與併行產線衝突），測試完立刻 `git checkout --` 還原，未留下任何測試痕跡。
- 沒有重啟正在跑的四條產線（`babel-dispatch.py` 是長駐 process，不會重新讀取磁碟上的原始碼；
  這次修改只影響之後新啟動的 dispatcher）。

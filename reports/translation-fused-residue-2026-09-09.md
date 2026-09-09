---
title: '譯文漏譯殘留盤點 2026-09-09'
description: '一支寫進 pipeline 當閘門的偵測器，產線從來沒呼叫過它——十個語系 1,557 篇譯文帶著三千多處沒翻完的中文片段'
type: 'report'
status: 'active'
current_version: 'v1.0'
last_updated: 2026-09-09
last_session: '2026-09-09-090000-twmd-maintainer-am'
sister_docs:
  - 'docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md'
  - 'docs/semiont/LESSONS-INBOX.md'
  - 'docs/semiont/OBSERVER-QUEUE.md'
---

# 譯文漏譯殘留盤點 — 2026-09-09

## 怎麼撞見的

今天早班審七篇翻譯投稿（tboydar 四篇德文人物、aminzai 三篇德文／印尼文／印地文）。
七篇全綠，順手把德文全庫拿 `cjk-residue-check.py` 掃了一次當背景對照，掃出 143 行。
其中大半是合法的——腳註引用的中文維基條目名、圖片作者的中文帳號、德文引號
`„懋"` 裡的字形解釋。但同一批裡混著三篇真的壞掉，於是換上更精準的
`cjk-adjacency-check.py`（判準是「漢字直接黏在拉丁字母上」，沒有空格、括號或
引號隔開），改掃全部十個非漢字語系。

## 量到什麼

| 語系 | 黏著命中  | 命中檔數 | 其中含簡體字（高信心漏譯） |
| ---- | --------- | -------- | -------------------------- |
| vi   | 627       | 125      | 42 處 / 19 檔              |
| hi   | 577       | 238      | 93 處 / 49 檔              |
| id   | 552       | 189      | 72 處 / 49 檔              |
| ar   | 536       | 267      | 47 處 / 34 檔              |
| ru   | 455       | 231      | 48 處 / 33 檔              |
| es   | 344       | 123      | 55 處 / 33 檔              |
| en   | 308       | 127      | 27 處 / 20 檔              |
| pt   | 302       | 150      | 43 處 / 26 檔              |
| fr   | 259       | 103      | 34 處 / 21 檔              |
| de   | 7（修完） | 4        | 0                          |

總計 **3,967 處 / 1,557 檔**。右欄那 **461 處 / 284 檔** 是高信心下界：命中的片段裡
帶著簡體字（节点／回顾／区／拥抱／仙气／说法／普及），簡體字不可能是我們刻意保留
的原文對照，那是模型直接把沒翻完的中文留在句子中間。用的是一份手挑的七十來字
簡體表，所以真實數字比這一欄高。

實際長相：

- hi `विभिन्न节点`、`एक दिन普及`、`संरक्षण署`、`मनोरंजन区`
- ru `Чжиньи科大`、`казнили凌遲`、`Ван Юнцин提出了`、`не得不搬`、`«Свободная時報`
- id `benar-benar动手`、`bersama构成`、`Biennale Taipei历届`
- ar `مدرسة国语`、`ن点燃 كومة`
- de（今天修掉的）`Đài水`——越南文的「台」黏著沒翻的「水」，四處都是「淡水」

## 為什麼會累積成這樣

`cjk-adjacency-check.py` 2026-08-09 就造好了，
[SQUEEZE-MODELS-MAX-PIPELINE §四道閘](../docs/pipelines/SQUEEZE-MODELS-MAX-PIPELINE.md)
把它寫成「四道閘之一」。

但 `grep -rn "cjk-adjacency"` 掃過整個 `scripts/`：**沒有任何一支程式呼叫它**。
產線上的 `translate.py` 與 `patch-translate.py` 呼叫的是 `cjk-leak-check`，
而那支對非漢字語系要求「連續 N 個以上漢字」才算洩漏——兩三個字的短片段
正好在門檻底下，這正是 adjacency 那支當初被造出來要補的盲區。

所以這一個月：閘門寫在文件裡、工具躺在目錄裡、產線從來沒走過那道門。
文件說有四道閘，實際上有三道。

## 這批不是今天才進來的

上面十個語系的譯文是過去幾個月各批 babel 陸續產出的。修補範圍是 1,557 檔，
遠超過 [MANIFESTO §自主權邊界](../docs/semiont/MANIFESTO.md) 的 50 檔紅線，
所以本 session 只做兩件事：德文那三篇當場修掉（已 ship），其餘寫成
[OBSERVER-QUEUE](../docs/semiont/OBSERVER-QUEUE.md) 待決項等哲宇拍板。

**另外有一條時機限制**：把 adjacency 接進 `translate.py` 等於在批次跑到一半改
驗收標準——而 babel dispatcher 此刻已經連續跑了第三天還在產出。這支工具自己的
註解就寫過為什麼當初刻意獨立於 `cjk-leak-check`：「那支正在被線上產線呼叫，
批次跑到一半改它的判準會讓同一批的前後段用不同標準驗收」。同一個理由適用於
現在：接線要等這批 babel 收工。

## 誤報家族（接線前要一起處理）

用 adjacency 判準掃全庫時，已確認三類誤報：

1. **相對連結目標**：`](/technology/AI發展)`、`](AAMA台北搖籃計畫.md)`——中文 slug
   是真實可用的路徑，改掉就是把連結改壞。`cjk-residue-check` 有遮這一類，
   adjacency 沒有。
2. **wikilink**：`[[為台灣而教TFT]]`。
3. **括號內混寫的專有名詞**：`(開源社群與g0v)`——`_is_zh_gloss()` 要求括號內每段
   拉丁字串都不是純小寫，`g0v` 是全小寫的真品牌名，於是被判成損壞的原名。

這是 [REFLEXES #83](../docs/semiont/REFLEXES.md)「兩把尺 divergence」的第三次現形：
`cjk-leak-check` / `cjk-residue-check` / `cjk-adjacency-check` 三支各自維護豁免清單。
adjacency 已經 import 了 leak 的 `legit_spans()`，缺的是把上面三類補進共用那份。

## 手工分類的抽樣（給後續估算用）

| 語系 | 抽樣       | 判為真漏譯 |
| ---- | ---------- | ---------- |
| de   | 14（全部） | 6          |
| hi   | 13         | 11         |
| ru   | 14         | 11         |

de 的真陽性率偏低是因為它只有 134 篇、且多數命中是連結 slug；hi／ru 的樣本
八成以上是真的。所以「1,557 檔」是上界、「284 檔」是下界，真值靠近後者往上。

---

_量測指令：`python3 scripts/tools/lang-sync/cjk-adjacency-check.py --glob 'knowledge/{lang}/**/*.md'`_

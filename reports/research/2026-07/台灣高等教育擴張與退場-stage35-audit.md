# Stage 3.5 audit — 台灣高等教育擴張與退場（2026-07-17）

> 草稿層驗證（Step 3.1-3.5）＋ Stage 2.5 source-fidelity 三道的整合紀錄。
> 執行：Fable orchestrator（主 session）＋1 fact-check agent（86 tool uses）。

## 3.1 五指／結構／塑膠

- prose-health：hard=0（對位 1 處＝S2 H2「大學不是蓋出來的，是升格出來的」，矯正讀者默認誤解之合法例外，§11.1 判準 1）；破折號 5 處（≤15/1500 帶內）
- quality gate profiles：rewrite-stage-3-5 hard=0／rewrite-stage-4 hard=0

## 3.2 事實鐵三角

- 算術自檢 12 項：11 過；**抓 1 錯**——「大學校院翻了三倍」（58→148=2.55x）→ 改具體數字「從 58 所變 148 所」
- 金額量級誦讀：5,158 萬（千萬級資遣）vs 77 億（十億級校產）對比為文章刻意結構，量級正確
- 引語逐字：fact-check agent 九人引語全 hold；「校產淪為囊中物」漏「為」字已補

## 3.3 FACTCHECK（Stage 2.5 fact-check agent 整合）

- 35 hold／5 drift／1 fabricated → 全數修復：
  1. [^14] 黃煌煇引語錯掛鹿鳴電子報 → 換 NSYSU 轉載自由時報 2011（orchestrator curl 親驗逐字）
  2. 「淨在學率破七成」footnote 支撐補明（統計簡訊 55 號 p.2 逐字「102學年突破7成」）
  3. [^16] 稻江 2007 數字補源（pixnet 轉載聯合報系，標原報佚失）
  4. [^17] 換康寧大學台南校區條目
  5. [^28] 韓國 claims hedge（後經 3.6 重驗再改寫，見 stage36）
  6. [^26] Yahoo 死鏈（後經 3.6 重驗換 udn＋風傳媒活源）

## 3.5 Title＋desc spine sync

- title 冒號三明治 ✓；**140→148 校正**（140 為舊文已證偽表格殘留；148＝100 學年真峰值，58/148 同口徑「大學校院」，時序「然後開始關門」成立：峰值 2011-12→首關 2014）——觀察者給定標題之數字層事實校正，收官摘要明列供 veto
- description 吃進論點 ✓；「安置的學生近三分之一沒畢業」補主詞（永達單案）；「沒設計關門」絕對句 → 「關門的規則遲到了十年」（對齊結尾「一半一半」的誠實弧線）

## Result: PASS

# orient 站外部評閱 v1（2026-09-18）

- actor：guide_orient_reviewer（Sonnet sub-agent，agentId aaeb3ece15f396fcf，乾淨 context）
- contextDisclosure：fresh-context-orient-inputs-only（只讀 brief.md、研究報告、orient-submission.json）
- verdict：revise

## rationale（reviewer 原文）

1. subjectExplanation 讀起來是塞滿數字的摘要，不是講給朋友聽的話——十幾個數字連續排列，讀者要先消化一份財經簡報才能懂「這篇在講什麼」。
2. 候選角度 A 與 C 共用同一個未證結論的骨架（「先墊、之後才付」）；「可被推翻之處」只挑戰周邊細節，沒有一個角度去質疑「中油＝先墊、之後才補」這個框架本身。真正獨立的只有角度 B。三分之二角度共用同一個已宣判的核心矛盾，等於在 orient 站把「延後付款」的結論先定調了。
3. unlock_reason 宣稱「追加預算正在立法院審議」是戰場之一，但 uncertainties 第 6 點自陳審議進度截至 9/18 未查到——用現在式斷言掩蓋了未驗證。「9/14 首漲」已塵埃落定，是引子不是戰場；建議只留貨物稅 9/30 到期與追加預算審議（若屬實）兩個戰線，把審議進度的不確定寫進 unlock_reason。
4. uncertainties 第 5 點正確標記「搜不到不等於沒發生」，合格。

**要改什麼**：(i) 重寫 subjectExplanation，數字砍到 2-3 個錨點；(ii) 角度 C 換成不預設「中油先墊」骨架的獨立角度（環團／節能訊號、或預算法要件之爭），或 A+C 合併騰出真正正交的第三角度；(iii) unlock_reason 拿掉「9/14 首漲」，把「審議進度未查到」寫進本文。

## evidence

- reports/staging/oil-price/run/orient-submission.json — data.subjectExplanation 全段
- reports/staging/oil-price/run/orient-submission.json — data.candidateAngles 第 1 點與第 3 點
- reports/research/2026-09/台灣油價機制與中油.md — §脊椎 核心矛盾一行與 §預想讀者帶走的那一件事
- reports/research/2026-09/台灣油價機制與中油.md — frontmatter unlock_reason
- reports/staging/oil-price/run/orient-submission.json — data.uncertainties 第 6 點

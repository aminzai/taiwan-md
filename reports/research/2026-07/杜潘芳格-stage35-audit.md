# Stage 3.5 Hallucination audit — 杜潘芳格

- Audit date: 2026-07-12T14:30:00Z
- Auditor session: harvest 2026-07-12-017-杜潘芳格-NEW-—-跨語+二二八+客家女-four-axis-intersection

## Method

Walk every concrete factual claim in `knowledge/People/杜潘芳格.md` against research SSOT `reports/research/2026-07/杜潘芳格.md` and primary WebFetch sources (zh/en wiki, Taipei Times, VERSE, TNL, NMTH, NMTL, 228 foundation). Arithmetic/units/quotes re-checked.

## Findings

| Claim                                       | Source                               | Verdict                                                                          |
| ------------------------------------------- | ------------------------------------ | -------------------------------------------------------------------------------- |
| 1927-03-09 生 / 2016-03-10 卒，89 歲        | zh.wiki [^1]                         | verified                                                                         |
| 新埔客家望族；小學校霸凌；日文創作          | zh/en wiki, TT                       | verified                                                                         |
| 跨越語言的一代；林亨泰 1967                 | TT [^4], en.wiki                     | verified                                                                         |
| 1947 姑丈張七郎父子遇害                     | zh.wiki 杜潘 + 張七郎 + 228 基金會   | verified（不用 EN Chang Chi-liang）                                              |
| 1948 嫁杜慶壽、中壢                         | zh.wiki                              | verified                                                                         |
| 1965 笠詩社                                 | zh.wiki, NMTH                        | verified（非創社 12 人 — 文內已標）                                              |
| 1966〈春天〉吳濁流代譯                      | TT                                   | verified                                                                         |
| 1977《慶壽》；〈平安戲〉華語全文            | zh.wiki + TNL                        | verified（引語對 TNL）                                                           |
| 客語改寫 / 1995 手稿                        | NMTL + TT                            | verified                                                                         |
| 女人樹三段                                  | VERSE                                | verified                                                                         |
| 1989 客語積極期；340 手稿 2017              | TT                                   | verified                                                                         |
| 1992 陳秀喜詩獎《遠千湖》                   | zh.wiki                              | verified                                                                         |
| 2007/2008 獎項                              | zh.wiki                              | verified                                                                         |
| 1982-05 美籍                                | zh.wiki / 莫渝（single）             | verified with single-source caveat in research                                   |
| 「小學三、四年級」中文自述                  | twcenter 訪談 [^12]                  | verified                                                                         |
| 珂拉琪並讀 2021                             | TNL                                  | verified（並讀非創作歸因）                                                       |
| 張七郎湖口客家、醫學校、鳳林仁壽、議長/國大 | 228 基金會 + wiki 張七郎             | verified                                                                         |
| 詩集年表 1977–1997                          | zh.wiki 表                           | verified                                                                         |
| Ink 2004 英譯引語 why I write               | TT                                   | verified as TT 英譯轉述                                                          |
| 七個子女                                    | 曾在草稿；**已改為「育兒」不鎖數字** | removed/softened（TT 有 seven children，正文採保守表述）                         |
| 絕對「首位客籍女詩人」                      | 客家典藏 claim                       | **not used** as hard fact                                                        |
| 父母親之住家 玫瑰荆棘句                     | VERSE                                | verified（quote-fidelity warn 因 research §4 未逐字存檔；已在 VERSE fetch 核對） |

## Arithmetic / quotes

- 享壽：2016-03-10 − 1927-03-09 → 滿 89 歲（生日次日卒）→ 不用「90」
- 〈平安戲〉華語引語：與 TNL 頁面逐段對照 PASS
- 客語末段：與 VERSE 對照 PASS

## Result

**PASS** — no remaining hard hallucinations; single-source items attributed; disputed absolute superlatives avoided.

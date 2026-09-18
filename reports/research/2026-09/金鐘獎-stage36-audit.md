---
article: knowledge/Culture/金鐘獎.md
stage: 3.6-assembled-product-verification
date: 2026-09-18
session: 2026-09-18-134142-golden-bell
run_profile: lite
---

# 金鐘獎 — Stage 3.6 成品總驗三關

## 3.6.1 原子重驗 fan-out

見 `金鐘獎-stage35-audit.md` 修復單（verifier A／B 共 5 ❌ 9 ⚠️，全部處置）＋變更節定向複驗（Sonnet a7b73caaf9402b816）：12 條 ✅ 10／⚠️ 2／❌ 0，兩條 ⚠️（七家電台殘留、第 58 屆缺腳註）已補。

## 3.6.2 順稿 → 3.7 閱讀節奏席 + 3.8 定稿站

- 閱讀節奏席（Sonnet a9c44851fac7d88fb）8 條 findings 全部施工（tw-versus／tw-stat 搬移／拆段三處／縫線句改寫）。
- 3.8 定稿手（fresh Opus a6efadd6f7cae0574）→ `reports/article-evolve/金鐘獎-closing.md`，`fact-atom-diff.py` **PASS**（24 處改動，原子零漂移）；主編 diff 抽查後覆蓋 canonical，另改兩處定稿手不能動的原子級句（台視全名補「也就是台視」、「1993 年」重複改「那一年」）。
- prose-flow before/after：長段（≥200）6 → 0；全篇 median 150 → ~115；viz 空白帶 4 節 → 1 節；三訊號 0/3 亮起。

## 3.6.3 視覺同步

| 媒體             | 位置                     | 旁邊 prose 在講它？                                  |
| ---------------- | ------------------------ | ---------------------------------------------------- |
| hero 45 屆主舞台 | frontmatter              | 30 秒概覽講典禮三場 ✓                                |
| 中山堂           | §1 座標段之後            | 1965 首屆場地 ✓                                      |
| tw-timeline      | §2 末                    | 制度節點 ✓                                           |
| 金鐘五十裝置     | §4 tw-versus 之後        | 「鐘的形狀沒變、要點每隔幾年改一次」caption 扣段落 ✓ |
| tw-versus        | §4 四條規則段後          | ✓                                                    |
| 陳亞蘭 2022      | §5 她的感言段之後        | ✓                                                    |
| tw-stat          | §6 「比 824 件還多」句後 | ✓                                                    |
| tw-slope         | §7 兩屆數字段後          | ✓                                                    |
| 56 屆星光大道    | §7 slope 後、爭議段前    | caption「先在紅毯上認人，再聽名單」 ✓                |
| iframe 60 屆直播 | §7 段尾                  | caption 講同時在線 17 萬與男女主角 ✓                 |
| tw-figure 40→40  | §8 Netflix 段後          | ✓                                                    |

圖與影片交錯、不相鄰堆疊（星光大道圖與 iframe 之間隔三段 prose）。

## 機械

- `article-health --profile=rewrite-stage-4` hard=0 warn=0
- `article-health --profile=rewrite-stage-3-5` hard=0 warn=0
- `prose-health` hard=0 warn=1（影視局新聞稿逐字引文內全形分號，引文保留）
- `fact-atom-diff.py knowledge/Culture/金鐘獎.md reports/article-evolve/金鐘獎-closing.md` PASS

## Result: PASS

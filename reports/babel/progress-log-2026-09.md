# 巴別塔同步進度日誌

> 每次更新增補一段（producer: `progress-snapshot.py`，資料源同目錄 `progress-*.jsonl`）。fresh=最新 / stale=可讀待刷新 / missing=無頁面。

## 2026-09-26T18:57:45+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1117 |     3 |       4 |  99.6% |      — |        — |
| ja   |  1074 |    22 |      28 |  97.5% |      — |        — |
| ko   |  1119 |     3 |       2 |  99.8% |      — |        — |
| es   |  1114 |     8 |       2 |  99.8% |      — |        — |
| fr   |  1114 |     8 |       2 |  99.8% |      — |        — |
| vi   |  1111 |    10 |       3 |  99.7% |      — |        — |
| id   |  1100 |    11 |      13 |  98.8% |      — |        — |
| pt   |  1108 |     9 |       7 |  99.4% |      — |        — |
| hi   |  1087 |    11 |      26 |  97.7% |      — |        — |
| ar   |  1099 |    13 |      12 |  98.9% |      — |        — |
| ru   |  1101 |     7 |      16 |  98.6% |      — |        — |
| de   |  1089 |     4 |      31 |  97.2% |      — |        — |

總缺口（stale+missing）：**255**

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  104 |   — |      — | ?×104                                                     |
| worker:haiku1    |  31 |   17 |   — |  244.3 | no output written by tra×7；verify=1 [tags not ident×2    |
| worker:haiku2    |  37 |   14 |   — |  263.6 | no output written by tra×5；leak×4                        |
| worker:haiku3    |  54 |   13 |   — |  219.6 | no output written by tra×6；leak×2                        |
| worker:lagunas   | 453 |  490 |   — |  278.0 | no output written by tra×338；patch candidate rejected×43 |
| worker:macm4max1 | 303 |  413 |   — |  551.0 | no output written by tra×229；verify=1 [URL count]×45     |
| worker:macm4max2 | 325 |  394 |   — |  543.5 | no output written by tra×227；verify=1 [URL count]×40     |
| worker:macm4max3 | 316 |  390 |   — |  544.7 | no output written by tra×216；patch candidate rejected×44 |
| worker:nemo      | 256 |  226 |   — |  703.9 | no output written by tra×141；patch candidate rejected×23 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-26T19:08:59+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1117 |     3 |       4 |  99.6% |      · |        · |
| ja   |  1083 |    22 |      19 |  98.3% |     +9 |       -9 |
| ko   |  1119 |     3 |       2 |  99.8% |      · |        · |
| es   |  1114 |     8 |       2 |  99.8% |      · |        · |
| fr   |  1114 |     8 |       2 |  99.8% |      · |        · |
| vi   |  1111 |    10 |       3 |  99.7% |      · |        · |
| id   |  1100 |    11 |      13 |  98.8% |      · |        · |
| pt   |  1108 |     9 |       7 |  99.4% |      · |        · |
| hi   |  1087 |    11 |      26 |  97.7% |      · |        · |
| ar   |  1099 |    13 |      12 |  98.9% |      · |        · |
| ru   |  1101 |     7 |      16 |  98.6% |      · |        · |
| de   |  1089 |     4 |      31 |  97.2% |      · |        · |

總缺口（stale+missing）：**246**（▼9 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  105 |   · |      — | ?×105                                                     |
| worker:haiku1    |  31 |   17 |   · |  244.3 | no output written by tra×7；verify=1 [tags not ident×2    |
| worker:haiku2    |  37 |   14 |   · |  263.6 | no output written by tra×5；leak×4                        |
| worker:haiku3    |  54 |   13 |   · |  219.6 | no output written by tra×6；leak×2                        |
| worker:lagunas   | 453 |  490 |   · |  278.0 | no output written by tra×338；patch candidate rejected×43 |
| worker:macm4max1 | 303 |  413 |   · |  551.0 | no output written by tra×229；verify=1 [URL count]×45     |
| worker:macm4max2 | 325 |  395 |   · |  543.5 | no output written by tra×227；verify=1 [URL count]×40     |
| worker:macm4max3 | 316 |  391 |   · |  544.7 | no output written by tra×217；patch candidate rejected×44 |
| worker:nemo      | 256 |  226 |   · |  703.9 | no output written by tra×141；patch candidate rejected×23 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-26T20:10:53+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1122 |     1 |       1 |  99.9% |     +5 |       -3 |
| ja   |  1090 |    17 |      17 |  98.5% |     +7 |       -2 |
| ko   |  1122 |     1 |       1 |  99.9% |     +3 |       -1 |
| es   |  1121 |     2 |       1 |  99.9% |     +7 |       -1 |
| fr   |  1119 |     3 |       2 |  99.8% |     +5 |        · |
| vi   |  1112 |    10 |       2 |  99.8% |     +1 |       -1 |
| id   |  1103 |    11 |      10 |  99.1% |     +3 |       -3 |
| pt   |  1110 |     9 |       5 |  99.6% |     +2 |       -2 |
| hi   |  1089 |    11 |      24 |  97.9% |     +2 |       -2 |
| ar   |  1101 |    13 |      10 |  99.1% |     +2 |       -2 |
| ru   |  1103 |     7 |      14 |  98.8% |     +2 |       -2 |
| de   |  1090 |     4 |      30 |  97.3% |     +1 |       -1 |

總缺口（stale+missing）：**206**（▼40 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  109 |   · |      — | ?×109                                                     |
| worker:haiku1    |  33 |   22 |  +2 |  259.3 | no output written by tra×7；verify=1 [no armor place×4    |
| worker:haiku2    |  40 |   19 |  +3 |  267.1 | no output written by tra×7；leak×4                        |
| worker:haiku3    |  57 |   19 |  +3 |  221.5 | no output written by tra×7；verify=1 [no armor place×4    |
| worker:lagunas   | 454 |  491 |  +1 |  278.9 | no output written by tra×339；patch candidate rejected×43 |
| worker:macm4max1 | 304 |  415 |  +1 |  549.5 | no output written by tra×230；verify=1 [URL count]×45     |
| worker:macm4max2 | 325 |  396 |   · |  543.5 | no output written by tra×228；verify=1 [URL count]×40     |
| worker:macm4max3 | 318 |  391 |  +2 |  550.5 | no output written by tra×217；patch candidate rejected×44 |
| worker:nemo      | 257 |  228 |  +1 |  701.5 | no output written by tra×142；patch candidate rejected×23 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-26T20:53:21+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1122 |     1 |       1 |  99.9% |      · |        · |
| ja   |  1102 |    10 |      12 |  98.9% |    +12 |       -5 |
| ko   |  1122 |     1 |       1 |  99.9% |      · |        · |
| es   |  1123 |     0 |       1 |  99.9% |     +2 |        · |
| fr   |  1121 |     1 |       2 |  99.8% |     +2 |        · |
| vi   |  1113 |    10 |       1 |  99.9% |     +1 |       -1 |
| id   |  1112 |     7 |       5 |  99.6% |     +9 |       -5 |
| pt   |  1114 |     6 |       4 |  99.6% |     +4 |       -1 |
| hi   |  1091 |    10 |      23 |  98.0% |     +2 |       -1 |
| ar   |  1107 |    10 |       7 |  99.4% |     +6 |       -3 |
| ru   |  1105 |     7 |      12 |  98.9% |     +2 |       -2 |
| de   |  1091 |     4 |      29 |  97.4% |     +1 |       -1 |

總缺口（stale+missing）：**165**（▼41 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  111 |   · |      — | ?×111                                                     |
| worker:haiku1    |  37 |   26 |  +4 |  267.2 | no output written by tra×9；verify=1 [no armor place×4    |
| worker:haiku2    |  49 |   23 |  +9 |  250.7 | no output written by tra×9；leak×4                        |
| worker:haiku3    |  63 |   20 |  +6 |  230.3 | no output written by tra×7；verify=1 [no armor place×4    |
| worker:lagunas   | 454 |  494 |   · |  278.9 | no output written by tra×340；patch candidate rejected×43 |
| worker:macm4max1 | 304 |  418 |   · |  549.5 | no output written by tra×232；verify=1 [URL count]×46     |
| worker:macm4max2 | 325 |  398 |   · |  543.5 | no output written by tra×229；verify=1 [URL count]×41     |
| worker:macm4max3 | 318 |  391 |   · |  550.5 | no output written by tra×217；patch candidate rejected×44 |
| worker:nemo      | 259 |  229 |  +2 |  702.4 | no output written by tra×142；patch candidate rejected×23 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-26T21:31:42+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1122 |     1 |       1 |  99.9% |      · |        · |
| ja   |  1104 |    10 |      10 |  99.1% |     +2 |       -2 |
| ko   |  1122 |     1 |       1 |  99.9% |      · |        · |
| es   |  1123 |     0 |       1 |  99.9% |      · |        · |
| fr   |  1122 |     1 |       1 |  99.9% |     +1 |       -1 |
| vi   |  1114 |    10 |       0 | 100.0% |     +1 |       -1 |
| id   |  1113 |     7 |       4 |  99.6% |     +1 |       -1 |
| pt   |  1117 |     6 |       1 |  99.9% |     +3 |       -3 |
| hi   |  1096 |    10 |      18 |  98.4% |     +5 |       -5 |
| ar   |  1108 |    10 |       6 |  99.5% |     +1 |       -1 |
| ru   |  1108 |     7 |       9 |  99.2% |     +3 |       -3 |
| de   |  1095 |     4 |      25 |  97.8% |     +4 |       -4 |

總缺口（stale+missing）：**144**（▼21 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  112 |   · |      — | ?×112                                                     |
| worker:haiku1    |  41 |   28 |  +4 |  281.7 | no output written by tra×10；verify=1 [no armor place×4   |
| worker:haiku2    |  53 |   24 |  +4 |  267.3 | no output written by tra×9；leak×4                        |
| worker:haiku3    |  67 |   24 |  +4 |  234.5 | no output written by tra×10；leak×4                       |
| worker:lagunas   | 454 |  496 |   · |  278.9 | no output written by tra×342；patch candidate rejected×43 |
| worker:macm4max1 | 304 |  419 |   · |  549.5 | no output written by tra×232；verify=1 [URL count]×47     |
| worker:macm4max2 | 326 |  399 |  +1 |  546.1 | no output written by tra×230；verify=1 [URL count]×41     |
| worker:macm4max3 | 319 |  393 |  +1 |  549.4 | no output written by tra×219；patch candidate rejected×44 |
| worker:nemo      | 260 |  229 |  +1 |  709.1 | no output written by tra×142；patch candidate rejected×23 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-26T21:44:27+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1123 |     1 |       0 | 100.0% |     +1 |       -1 |
| ja   |  1105 |    10 |       9 |  99.2% |     +1 |       -1 |
| ko   |  1123 |     1 |       0 | 100.0% |     +1 |       -1 |
| es   |  1123 |     0 |       1 |  99.9% |      · |        · |
| fr   |  1123 |     1 |       0 | 100.0% |     +1 |       -1 |
| vi   |  1114 |    10 |       0 | 100.0% |      · |        · |
| id   |  1114 |     6 |       4 |  99.6% |     +1 |        · |
| pt   |  1118 |     6 |       0 | 100.0% |     +1 |       -1 |
| hi   |  1100 |    10 |      14 |  98.8% |     +4 |       -4 |
| ar   |  1109 |    10 |       5 |  99.6% |     +1 |       -1 |
| ru   |  1116 |     6 |       2 |  99.8% |     +8 |       -7 |
| de   |  1097 |     4 |      23 |  98.0% |     +2 |       -2 |

總缺口（stale+missing）：**123**（▼21 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  112 |   · |      — | ?×112                                                     |
| worker:haiku1    |  43 |   28 |  +2 |  288.8 | no output written by tra×10；verify=1 [no armor place×4   |
| worker:haiku2    |  55 |   24 |  +2 |  269.9 | no output written by tra×9；leak×4                        |
| worker:haiku3    |  70 |   25 |  +3 |  233.1 | no output written by tra×11；leak×4                       |
| worker:lagunas   | 456 |  497 |  +2 |  278.5 | no output written by tra×342；patch candidate rejected×44 |
| worker:macm4max1 | 306 |  419 |  +2 |  554.0 | no output written by tra×232；verify=1 [URL count]×47     |
| worker:macm4max2 | 326 |  400 |   · |  546.1 | no output written by tra×231；verify=1 [URL count]×41     |
| worker:macm4max3 | 319 |  394 |   · |  549.4 | no output written by tra×220；patch candidate rejected×44 |
| worker:nemo      | 260 |  229 |   · |  709.1 | no output written by tra×142；patch candidate rejected×23 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-26T22:26:18+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1123 |     1 |       0 | 100.0% |      · |        · |
| ja   |  1111 |     9 |       4 |  99.6% |     +6 |       -5 |
| ko   |  1123 |     1 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |     +1 |       -1 |
| fr   |  1123 |     1 |       0 | 100.0% |      · |        · |
| vi   |  1114 |    10 |       0 | 100.0% |      · |        · |
| id   |  1117 |     4 |       3 |  99.7% |     +3 |       -1 |
| pt   |  1116 |     6 |       2 |  99.8% |     -2 |       +2 |
| hi   |  1108 |    10 |       6 |  99.5% |     +8 |       -8 |
| ar   |  1111 |    10 |       3 |  99.7% |     +2 |       -2 |
| ru   |  1118 |     6 |       0 | 100.0% |     +2 |       -2 |
| de   |  1104 |     4 |      16 |  98.6% |     +7 |       -7 |

總缺口（stale+missing）：**96**（▼27 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  113 |   · |      — | ?×113                                                     |
| worker:haiku1    |  46 |   31 |  +3 |  292.0 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |  +6 |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |  +5 |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 458 |  502 |  +2 |  277.8 | no output written by tra×345；patch candidate rejected×45 |
| worker:macm4max1 | 308 |  421 |  +2 |  552.8 | no output written by tra×233；verify=1 [URL count]×47     |
| worker:macm4max2 | 327 |  403 |  +1 |  545.9 | no output written by tra×233；verify=1 [URL count]×41     |
| worker:macm4max3 | 320 |  399 |  +1 |  548.8 | no output written by tra×222；patch candidate rejected×45 |
| worker:nemo      | 261 |  230 |  +1 |  715.0 | no output written by tra×142；patch candidate rejected×24 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-26T23:20:52+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1122 |     2 |       0 | 100.0% |     -1 |        · |
| ja   |  1112 |     9 |       3 |  99.7% |     +1 |       -1 |
| ko   |  1122 |     2 |       0 | 100.0% |     -1 |        · |
| es   |  1123 |     1 |       0 | 100.0% |     -1 |        · |
| fr   |  1122 |     2 |       0 | 100.0% |     -1 |        · |
| vi   |  1113 |    11 |       0 | 100.0% |     -1 |        · |
| id   |  1119 |     3 |       2 |  99.8% |     +2 |       -1 |
| pt   |  1115 |     7 |       2 |  99.8% |     -1 |        · |
| hi   |  1109 |    11 |       4 |  99.6% |     +1 |       -2 |
| ar   |  1113 |    10 |       1 |  99.9% |     +2 |       -2 |
| ru   |  1117 |     6 |       1 |  99.9% |     -1 |       +1 |
| de   |  1106 |     5 |      13 |  98.8% |     +2 |       -3 |

總缺口（stale+missing）：**95**（▼1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  113 |   · |      — | ?×113                                                     |
| worker:haiku1    |  46 |   31 |   · |  292.0 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 463 |  505 |  +5 |  276.8 | no output written by tra×347；patch candidate rejected×45 |
| worker:macm4max1 | 310 |  423 |  +2 |  551.9 | no output written by tra×234；verify=1 [URL count]×47     |
| worker:macm4max2 | 327 |  406 |   · |  545.9 | no output written by tra×235；verify=1 [URL count]×41     |
| worker:macm4max3 | 321 |  402 |  +1 |  549.1 | no output written by tra×224；patch candidate rejected×46 |
| worker:nemo      | 263 |  231 |  +2 |  717.9 | no output written by tra×142；patch candidate rejected×24 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T00:44:27+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1123 |     1 |       0 | 100.0% |     +1 |        · |
| ja   |  1115 |     9 |       0 | 100.0% |     +3 |       -3 |
| ko   |  1122 |     2 |       0 | 100.0% |      · |        · |
| es   |  1123 |     1 |       0 | 100.0% |      · |        · |
| fr   |  1122 |     2 |       0 | 100.0% |      · |        · |
| vi   |  1116 |     8 |       0 | 100.0% |     +3 |        · |
| id   |  1120 |     3 |       1 |  99.9% |     +1 |       -1 |
| pt   |  1116 |     6 |       2 |  99.8% |     +1 |        · |
| hi   |  1114 |    10 |       0 | 100.0% |     +5 |       -4 |
| ar   |  1113 |    10 |       1 |  99.9% |      · |        · |
| ru   |  1117 |     6 |       1 |  99.9% |      · |        · |
| de   |  1120 |     3 |       1 |  99.9% |    +14 |      -12 |

總缺口（stale+missing）：**67**（▼28 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  115 |   · |      — | ?×115                                                     |
| worker:haiku1    |  46 |   31 |   · |  292.0 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 464 |  509 |  +1 |  277.0 | no output written by tra×350；patch candidate rejected×45 |
| worker:macm4max1 | 317 |  429 |  +7 |  548.8 | no output written by tra×237；verify=1 [URL count]×47     |
| worker:macm4max2 | 329 |  409 |  +2 |  548.4 | no output written by tra×237；verify=1 [URL count]×41     |
| worker:macm4max3 | 326 |  407 |  +5 |  549.2 | no output written by tra×226；patch candidate rejected×48 |
| worker:nemo      | 264 |  235 |  +1 |  718.2 | no output written by tra×144；patch candidate rejected×25 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T00:55:05+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1123 |     1 |       0 | 100.0% |      · |        · |
| ja   |  1115 |     9 |       0 | 100.0% |      · |        · |
| ko   |  1122 |     2 |       0 | 100.0% |      · |        · |
| es   |  1123 |     1 |       0 | 100.0% |      · |        · |
| fr   |  1122 |     2 |       0 | 100.0% |      · |        · |
| vi   |  1116 |     8 |       0 | 100.0% |      · |        · |
| id   |  1120 |     3 |       1 |  99.9% |      · |        · |
| pt   |  1117 |     5 |       2 |  99.8% |     +1 |        · |
| hi   |  1114 |    10 |       0 | 100.0% |      · |        · |
| ar   |  1113 |    10 |       1 |  99.9% |      · |        · |
| ru   |  1117 |     6 |       1 |  99.9% |      · |        · |
| de   |  1120 |     3 |       1 |  99.9% |      · |        · |

總缺口（stale+missing）：**66**（▼1 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  115 |   · |      — | ?×115                                                     |
| worker:haiku1    |  46 |   31 |   · |  292.0 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 465 |  510 |  +1 |  276.7 | no output written by tra×350；patch candidate rejected×46 |
| worker:macm4max1 | 317 |  429 |   · |  548.8 | no output written by tra×237；verify=1 [URL count]×47     |
| worker:macm4max2 | 329 |  409 |   · |  548.4 | no output written by tra×237；verify=1 [URL count]×41     |
| worker:macm4max3 | 326 |  407 |   · |  549.2 | no output written by tra×226；patch candidate rejected×48 |
| worker:nemo      | 264 |  235 |   · |  718.2 | no output written by tra×144；patch candidate rejected×25 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T11:57:09+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |     +1 |        · |
| ja   |  1123 |     1 |       0 | 100.0% |     +8 |        · |
| ko   |  1124 |     0 |       0 | 100.0% |     +2 |        · |
| es   |  1124 |     0 |       0 | 100.0% |     +1 |        · |
| fr   |  1124 |     0 |       0 | 100.0% |     +2 |        · |
| vi   |  1124 |     0 |       0 | 100.0% |     +8 |        · |
| id   |  1124 |     0 |       0 | 100.0% |     +4 |       -1 |
| pt   |  1124 |     0 |       0 | 100.0% |     +7 |       -2 |
| hi   |  1122 |     2 |       0 | 100.0% |     +8 |        · |
| ar   |  1124 |     0 |       0 | 100.0% |    +11 |       -1 |
| ru   |  1124 |     0 |       0 | 100.0% |     +7 |       -1 |
| de   |  1124 |     0 |       0 | 100.0% |     +4 |       -1 |

總缺口（stale+missing）：**3**（▼63 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |  +2 |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |  +9 |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 | +10 |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 | +12 |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |  +4 |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 | +12 |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T12:41:37+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |     +1 |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |     +2 |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（▼3 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T12:43:45+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T13:28:56+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T14:28:57+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T15:28:57+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T15:41:02+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T16:22:29+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T16:59:46+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T17:07:44+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T17:09:02+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T17:10:07+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T17:28:48+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T17:33:32+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T17:34:15+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T18:28:58+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T18:33:47+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T19:28:46+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T19:35:19+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T19:36:14+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T19:37:59+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T20:29:11+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T20:42:55+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T21:29:16+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T21:46:58+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T22:29:03+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T22:33:42+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T22:44:11+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T23:29:04+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T23:31:59+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-27T23:52:26+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T00:28:47+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T00:40:00+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T00:41:47+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T00:43:45+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T01:30:45+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T01:38:01+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T01:39:03+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T02:29:08+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T02:33:31+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T03:08:28+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T04:10:15+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T04:37:34+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T04:42:23+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T04:55:47+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T05:29:01+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T05:45:32+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T06:29:04+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T06:44:09+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T07:29:01+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T07:33:02+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T08:29:13+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T08:58:42+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T09:27:27+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T09:42:53+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T09:45:58+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T09:52:36+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T10:28:57+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T10:33:48+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T11:29:02+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T11:34:19+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T12:29:03+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

## 2026-09-28T12:31:52+08:00（zh 總數 1124）

| 語言 | fresh | stale | missing | 覆蓋率 | Δfresh | Δmissing |
| ---- | ----: | ----: | ------: | -----: | -----: | -------: |
| en   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ja   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ko   |  1124 |     0 |       0 | 100.0% |      · |        · |
| es   |  1124 |     0 |       0 | 100.0% |      · |        · |
| fr   |  1124 |     0 |       0 | 100.0% |      · |        · |
| vi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| id   |  1124 |     0 |       0 | 100.0% |      · |        · |
| pt   |  1124 |     0 |       0 | 100.0% |      · |        · |
| hi   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ar   |  1124 |     0 |       0 | 100.0% |      · |        · |
| ru   |  1124 |     0 |       0 | 100.0% |      · |        · |
| de   |  1124 |     0 |       0 | 100.0% |      · |        · |

總缺口（stale+missing）：**0**（＝0 vs 上一筆）

**節點／worker**（ok/fail 為累計；Δ為對上一筆）

| 節點             |  ok | fail | Δok | 平均秒 | 主要 fail                                                 |
| ---------------- | --: | ---: | --: | -----: | --------------------------------------------------------- |
| worker:?         |   0 |  122 |   · |      — | ?×122                                                     |
| worker:haiku1    |  48 |   31 |   · |  290.7 | no output written by tra×12；leak×4                       |
| worker:haiku2    |  61 |   26 |   · |  266.6 | no output written by tra×11；leak×4                       |
| worker:haiku3    |  75 |   27 |   · |  235.6 | no output written by tra×13；leak×4                       |
| worker:lagunas   | 474 |  523 |   · |  279.8 | no output written by tra×356；patch candidate rejected×51 |
| worker:macm4max1 | 327 |  496 |   · |  536.1 | no output written by tra×265；verify=1 [URL count]×50     |
| worker:macm4max2 | 341 |  421 |   · |  550.7 | no output written by tra×240；verify=1 [URL count]×43     |
| worker:macm4max3 | 330 |  419 |   · |  547.7 | no output written by tra×232；patch candidate rejected×51 |
| worker:nemo      | 276 |  241 |   · |  723.7 | no output written by tra×147；patch candidate rejected×28 |

endpoint 探活：local 🟢、laptop-4090 🔴、laptop-5090 🔴、desktop-3090 🔴、mac-m4max 🟢

（babel-pulse 常駐儀器自動快照）

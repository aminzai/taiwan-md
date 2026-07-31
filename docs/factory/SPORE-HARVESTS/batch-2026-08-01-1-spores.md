---
spores: '#159, #160, #161, #162, #163, #164'
harvest_date: '2026-08-01 06:30'
harvest_window_day: 'mixed (D+5 to D+7)'
batch_reason: 'twmd-spore-harvest-am routine — D+7 (#159/#160 外送專法) + D+6 (#161/#162 台灣鎢供應鏈，combined reach ≈479K, still 🚨 past 50K threshold, Bucket D framing from 07-28 remains open with no new observer directive) + D+5 (#163/#164 苯駢芘食安事件)'
triggered_by: 'cron (twmd-spore-harvest-am)'
source: 'chrome_mcp (Threads + X, not logged in — read-only public view)'
reply_count: '~13 top-level visible across #159/#160/#163/#164, plus the long-running #161/#162 tungsten thread (dozens of replies, unchanged bucket composition from prior cycles — not re-transcribed in full, see note below)'
bucket_breakdown: 'A=0 / B=0 / C=0 / D=continuing (⚠️ #161/#162 台灣鎢供應鏈 — no new escalation this cycle, default (a) 不動 held) / E=0 / F=majority (labor-law debate on #159/#160, legal-interpretation debate on #163/#164) / G=0'
---

# Batch harvest — 2026-08-01 am (cron)

Chrome MCP browser was **not logged in** to Threads/X (public/anonymous view), same as prior cycles. Metrics and top-level reply text were readable; deeper reply threads and X replies were gated behind login wall (per Pitfall 2 X DOM-lazy-load limits).

## #159/#160 外送專法 D+7

- Threads: **3,254 views** / 27 likes / 8 comments / 1 repost — flat versus D+6 (3,249/27/8/1), plateaued.
- X: **3,058 views** / 53 likes / 12 reposts / 3 comments / 9 bookmarks — flat versus D+6 (3,055/53/12/3/9).
- Same reader-vs-reader labor-law debate thread as prior cycles (承攬制 vs 雇用制, 22K 政策 analogy — modecheng/we666fdg/benjaymin.chuang/f7612112025/xyzlin2063/phj52085/san05042000, plus a "相關串文" side-thread arguing the same point). No factual-error callout, no entity-missing ask. **Bucket F**, no reply mandated. This is the last scheduled daily cycle for this pair (D+7 is the primary KPI checkpoint per cadence table); next touch is D+14 milestone unless reach spikes.

## #161/#162 台灣鎢供應鏈 D+6 — 🚨 Reach×Accuracy trigger continues, Bucket D framing still open

- Threads: **430,000 views** / 900 likes / 4 comments / 88 reposts / 131 shares (root post's own counters — the viral engagement lives on reply threads, not the root: a reply about the Fangliao murder case carries ~11K likes on its own, dwarfing the root post's counters. Recorded metrics reflect the root post per SSOT convention).
- X: **49,000 views** / 2,167 likes / 510 reposts / 15 comments / 146 bookmarks.
- Combined reach ≈ 479K, consistent with yesterday's memory note (479K continuing plateau).

### Bucket D — no new escalation

Same reader thread linking the article's Fangliao tungsten-recycling shops to a real, unverified Pingtung murder case (documented in [`HARVEST-FRAMING-PENDING/2026-07-28.md`](../HARVEST-FRAMING-PENDING/2026-07-28.md)), plus continuing political-violence speculation (calls to escalate to national-security-case status, calls for officials to act, tagging @dpp_taiwan/@william_chingte, KMT-related commentary about upcoming 8/1 rally). No new claims or intensity beyond what's already filed. **No new pending file created** (per REFLEXES #74 cross-routine signal-inflation dedup). Holding the same default: (a) 不動 — no reply, no article edit, per §自主權邊界 政治立場 + unverified real-person/active-case sensitivity. Not a typical Reach×Accuracy FACTCHECK case (the live signal is an external unverified crime-report linkage, not a disputed claim inside the article text), so Quick Mode was not spawned this cycle either — same reasoning as 07-31 (the @cation6666 evidentiary critique that triggered inline verification that cycle has no new counterpart today).

## #163/#164 苯駢芘食安事件 D+5

- Threads: **1,698 views** / 20 likes / 4 comments / 1 repost — slight growth from D+4 (1,681/20/4/1). Same two-ish replies as prior cycles (dreehung on the 24hr reporting-cost tradeoff; jianqiang621 generic political attack on the government, unrelated to article accuracy; one reply citing a legal-dictionary definition of 應即 that actually **supports** the article's reading, not a correction).
- X: **4,992 views** / 106 likes / 19 reposts / 5 bookmarks / 0 comments — slight growth from D+4 (4,983 views).
- **Bucket F** (jianqiang621's political attack is closer to Bucket G derail/attack but directed at the government, not at Taiwan.md or the article — logged, no reply, no escalation), no reply mandated otherwise.

## Reply-posting note (this cycle)

**No replies were posted to any platform this cycle** (none were drafted either — no Bucket A/C/E items surfaced today that would warrant one). Consistent with the last several cycles' resolution of the pipeline↔MANIFESTO conflict:

1. **MANIFESTO §存在結構「需要人類決策」** lists "Post 留言回覆 to Threads/X" as human-only; REFLEXES #26 v2 says the same: AI prepares draft replies, a human posts them. SPORE-HARVEST-PIPELINE.md's older Chrome MCP §Step 8 auto-post language for D+0 acute-window Bucket A/C is stale against the current MANIFESTO text (per REFLEXES #56 canonical↔pipeline drift) — noted again for whoever eventually reconciles the two documents.
2. This session's own operating constraints: sending any message on the user's behalf requires explicit in-chat confirmation, unavailable in this unattended cron run.
3. The Chrome MCP browser session was not logged in to either Threads or X this cycle, so posting was not mechanically available regardless of policy.

## Pipeline 鐵律 audit

- [x] Atomic batch log SSOT: `docs/factory/SPORE-HARVESTS/batch-2026-08-01-1-spores.md` single commit
- [x] Frontmatter `spores` plural list ✓
- [x] harvest_window_day `mixed (D+5 to D+7)` ✓
- [x] Numbers written only via `spore-db.py add-metrics` (#159/#160/#161/#162/#163/#164), not into frontmatter or SPORE-LOG.md
- [x] Bucket D escalation status checked against `HARVEST-FRAMING-PENDING/2026-07-28.md` — no new observer directive, default held, no duplicate pending file created (per REFLEXES #74 dedup discipline)
- [x] No Bucket A/C/E items this cycle — no reply drafts needed
- [ ] Reach×Accuracy retroactive FACTCHECK Quick Mode — **not spawned this cycle**, same reasoning as prior cycles (live 50K-trigger signal is an external unverified crime-report linkage, not a disputed article claim)
- [x] `validate-spore-data.py` — 0 errors / 0 warnings, ALL GREEN
- [x] `generate-spore-records.py` + `generate-dashboard-spores.py` regen'd same cycle
- [x] Tab group cleanup done (`tabs_close_mcp`)

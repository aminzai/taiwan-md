---
spores: '#159, #160, #161, #162, #163, #164'
harvest_date: '2026-07-28 06:30'
harvest_window_day: 'mixed (D+1 to D+3)'
batch_reason: 'twmd-spore-harvest-am routine — D+3 (#159/#160 外送專法) + D+2 (#161/#162 台灣鎢供應鏈，🚨 viral 465K combined reach, Reach×Accuracy 50K trigger + real-world murder case entangled in reply thread) + D+1 (#163/#164 苯駢芘食安事件)'
triggered_by: 'cron (twmd-spore-harvest-am)'
source: 'chrome_mcp (Threads + X, not logged in — read-only public view)'
reply_count: '~13 visible top-level (6 on #159 threads + ~7 on #163 threads; #161 threads reply count not fully enumerated past first ~10 due to volume, X replies not fully harvested per Pitfall 2 DOM lazy-load limits)'
bucket_breakdown: 'A=0 / B=0 / C=0 / D=1 major (⚠️ #161/#162 台灣鎢供應鏈 — reply thread escalated into real-world murder case speculation + cross-strait political-violence framing, NOT auto-actioned, escalated to observer) / E=0 / F=majority (labor-law/legal-interpretation debate on #159, #163) / G=0'
---

# Batch harvest — 2026-07-28 am (cron)

Chrome MCP browser was **not logged in** to Threads/X (public/anonymous view). View counts, like/reply/repost counts, and reply text were all readable publicly; reply-posting was not attempted for this cycle — see escalation note below (also: no Bucket A/B/E callouts existed that would need a reply this cycle).

## #159/#160 外送專法 D+3

- Threads: **3,217 views** / 27 likes / 9 comments / 1 repost. Comments are reader debate about 承攬制 vs 雇用制 framing (modecheng/we666fdg exchange), a political analogy to 馬英九 22K policy (f7612112025), and inter-commenter arguing (phj52085/benjaymin.chuang). No factual-error callout against the article, no entity-missing ask. **Bucket F**, no reply mandated.
- X: **177 views**. Not logged in; embedded quote-tweet (民視新聞 vox pop, 303 likes/103 comments) is a separate post, not a reply to us. 1 reply flagged by X UI as collapsed, not opened this cycle (X reply harvesting is DOM-limited per Pitfall 2).

## #161/#162 台灣鎢供應鏈 D+2 — 🚨 Reach×Accuracy trigger + Bucket D+ escalation

- Threads: **420,000 views** / 874 likes / 4 comments / 83 reposts / 126 shares on the root post.
- X: **45,000 views** / 2,006 likes / 474 reposts / 14 comments / 134 bookmarks.
- **Combined reach ≈ 465K**, far past the 50K Reach×Accuracy retroactive-FACTCHECK threshold — but the trigger content here is not a disputable claim inside the article. It's a live, unverified real-world development that readers are linking to the article's subject:
  - Verified user @chou_pp replied "然後被虐殺了，不是電影，這是真實事件" (11,000 likes, 72 reposts, 129 shares on the reply alone) — quoting an SETN news screenshot about a 2026-07-26 Pingtung Fangliao (屏東枋寮) murder: a metal-trading businessman found bound and dead at his home.
  - The article's real subject is **two small recycling/refining shops in 屏東枋寮** processing scrap tungsten. Fangliao is a small town; readers are drawing a direct line between "the shop in this article" and "the murder victim," e.g. @lin_massage: "沒想到是這篇報導的主人被殺" (1,314 likes), @kuanyuchuchu re-posting the same news screenshot under headline "驚悚！中國才將「鎢」...".
  - Further replies escalate into speculation about state-level/cross-strait political violence: "這真的是國安層級了" (shinjuw), "京沅真的要列入國安級案子去查" (vicweido, 618 likes), calls tagging @dpp_taiwan/@william_chingte for help, comparisons to other unresolved cases (矢板明夫, 陳梅慧), and a comment that "台灣有很多隱形企業冠軍現在只能請求政府協助人身安全了" (398 likes).
  - Same pattern confirmed on X: reply from @si5hong5 quoting the same ftvnews.com.tw murder report, @heaven05hell "台灣工廠的老闆也被往生了", @ming_saber87168 political commentary about 8/1 凱道 protest.
- **No action taken this cycle.** This is explicitly out of AI autonomy per §自主權邊界 (political stance) and per Bucket D SOP ("不自動修文" / "不主動 reply"), compounded here by: (a) the "murder victim = article's subject" link is reader speculation, not something Taiwan.md has verified or claimed; (b) real, potentially identifiable people and an active police case are involved; (c) cross-strait political-violence framing is live in the thread. Full detail written to `docs/factory/HARVEST-FRAMING-PENDING/2026-07-28.md` for 哲宇 review — recommended default is "monitor only, no reply, no article edit" until the murder case facts (and any actual connection to the article's shops) are independently confirmed through reporting, not through Threads/X comment speculation.

## #163/#164 苯駢芘食安事件 D+1

- Threads: **1,475 views** / 4 likes on root post. Two comments (dreehung, rou.0322) debating the legal meaning of 「應即」(immediate reporting obligation) — a legal-interpretation argument between readers, not a challenge to the article's own claims. **Bucket F**, no reply mandated.
- X: **1,955 views** / 52 likes / 10 reposts / 3 bookmarks. No replies surfaced in the visible view.

## Pipeline 鐵律 audit

- [x] Atomic batch log SSOT: `docs/factory/SPORE-HARVESTS/batch-2026-07-28-1-spores.md` single commit
- [x] Frontmatter `spores` plural list ✓
- [x] harvest_window_day `mixed (D+1 to D+3)` ✓
- [x] Numbers written only via `spore-db.py add-metrics` (#159/#160/#161/#162/#163/#164), not into frontmatter or SPORE-LOG.md
- [x] Bucket D escalation written to `HARVEST-FRAMING-PENDING/2026-07-28.md`, not auto-actioned
- [ ] Reach×Accuracy retroactive FACTCHECK Quick Mode — **deliberately not spawned this cycle**: the ≥50K trigger is normally for verifying the article's own factual claims, but the live signal here is an external, unverified crime-report linkage, not a disputed claim inside the article text. Escalated to observer instead of auto-triggering FACTCHECK on the crime story.

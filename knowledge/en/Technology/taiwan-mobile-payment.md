---
title: 'Taiwan Mobile Payments: Why Do Phones Hold Multiple Payment Apps Yet People Still Carry Cash?'
description: "In Q3 2024, 92% of MIC's 5,000 online respondents had used mobile payments and 84% used them regularly, yet a central bank survey found 73.8% of adults still mix cash and non-cash. From consumers and merchants to TWQR's common QR, this article unpacks the different tools, contracts, and confirmation flows behind phone payments, explains why high adoption doesn't mean leaving cash behind, and details what the common QR has solved and what acceptance and failure exceptions remain."
date: 2026-09-01
category: 'Technology'
tags:
  [
    'Mobile Payment',
    'Electronic Payment',
    'TWQR',
    'Taiwan Pay',
    'QR Code',
    'Cash',
    'FinTech',
  ]
subcategory: '數位與網路'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-09-01
lastHumanReview: false
researchReport: 'reports/research/2026-09/台灣行動支付.md'
image: '/article-images/technology/taiwan-mobile-payments-merchant-2026.webp'
imageCredit: '財金資訊股份有限公司（TWQR 官方網站）'
imageLicense: 'Fair use editorial commentary'
imageSource: 'https://www.twqr.com.tw/'
translatedFrom: 'Technology/台灣行動支付.md'
sourceCommitSha: '574b1a339'
sourceContentHash: 'sha256:1e2fca6dab4c2f1c'
sourceBodyHash: 'sha256:62d9c6127e29bebe'
translatedAt: '2026-09-16T11:57:21+08:00'
---

# Taiwan Mobile Payments: Why Do Phones Hold Multiple Payment Apps Yet People Still Carry Cash?

![Merchant and mobile payment signage in TWQR official merchant interview thumbnail](/article-images/technology/taiwan-mobile-payments-merchant-2026.webp)
_TWQR official merchant interview thumbnail, used only for institutional publicity material analysis. The image represents only the interviewed store and cannot serve as independent field evidence for adoption across all small shops in Taiwan. Image: Financial Information Service Co., Ltd. (TWQR official website), fair use for commentary._

> **30-second overview:** In MIC's Q3 2024 online sample, 92% had used mobile payments. A central bank-commissioned survey, however, showed 73.8% of adults still use both cash and non-cash. The two figures measure different populations and questions, yet point to the same reality: being able to pay by phone, completing transactions everywhere, and feeling safe leaving cash at home are three distinct thresholds. Multiple apps sometimes fill channel gaps, sometimes chase rewards and membership features. TWQR is integrating a common QR, but hasn't yet merged all funding sources, merchant contracts, and failure scenarios into a single payment method.

In September 2025, MIC Senior Industry Analyst Hu Tzu-li (胡自立) released a mobile payment consumer survey. He observed that active users install five or more tools, "mainly to use mobile payments in different channels." [^1] This sounds like what many do at the register: first check which logos are stuck on the glass door or counter, then decide which app to unlock. Only if no familiar mark appears do they look up and ask, "Which ones do you take here?"

Phone options keep multiplying, yet wallets still hold a few bills. This coexistence is easily read as Taiwan's payment market being too fragmented, or conversely as purely a matter of promotional choice. Both explanations capture part of the truth. Institutional friction in acceptance and interoperability does make people install more tools and keep cash, but rewards, membership, transfers, habits, personal preferences, and failure fallback all operate simultaneously. To see this clearly, we must separate three thresholds: whether people adopt, whether transactions work across scenarios, and whether the system can recover from failure so users dare leave their last bill at home.

## Being Able to Pay by Phone Doesn't Mean a Phone Alone Is Enough Today

MIC's 92% "ever used" and 84% "regularly used" come from a two-month, 5,000-sample online survey in Q3 2024. The public page does not fully list the sampling frame, age range, or weighting method, so these two proportions only describe that online sample and cannot be directly written as the adoption rate for Taiwan's entire population. [^2] Even with this caveat, they show that among consumers who fill out online surveys, phone payment has long passed the unfamiliar-technology stage.

Another survey commissioned by the Central Bank and conducted by the Taiwan Institute of Economic Research asked how people 18 and over use cash and non-cash daily. The survey used landlines and mobile phones as primary modes, online as supplementary, covered 22 counties and cities, and was weighted by population structure, yielding 4,234 valid responses. Results: 73.8% use both cash and non-cash, 25% use only cash, and only 1.2% use only non-cash. [^3] Here non-cash also includes credit cards, debit cards, and stored-value cards, so it cannot serve as mobile payment market share, but it sketches the shape of today's wallets well.

```tw-waffle
Mixing is the majority's daily life (%)
Cash and non-cash both used | 73.8
Cash only | 25
Non-cash only | 1.2
Source: Central Bank commissioned payment instrument survey, published 2024
```

Thus, someone tapping their phone at a chain café in the morning, scanning a QR for points at lunch, and switching to cash at the evening market is not contradictory. They have crossed the first threshold — "people can use it" — yet must still swap tools by location, merchant, and equipment. The "still carry cash" in the title can only be understood as scenario backup at scale, not expanded into every Taiwanese person having the same daily necessity.

Payment habits have changed, but scenario exceptions remain on the road. Installing several apps seems to plug each exception, but to understand why they can plug gaps, we must first admit those apps are not the same thing. The moment of opening the phone looks similar; the paths the transactions take afterward may be completely different.

## Several Apps Look Like They Pay, But the Roads Behind Them Differ

FSC teaching materials categorize by bound instrument, technology, and applicable regulations: mobile credit card, mobile debit card, QR scanning, electronic payment institutions, and electronic tickets. [^4]

The consumer's front-end action may be just a tap, a scan, or a confirmation press, but the back end may be completed by different bound instruments, technologies, receiving ends, and rules. The same phone payment may invoke a bound card or an electronic payment account. The merchant's receiving end and specifications then determine which combinations work. LINE Pay, JKOPAY, Apple Pay, All Pay, and Taiwan Pay therefore cannot be lined up as five homogeneous wallets by logo alone. Some compete, some cooperate in layers within a single transaction, and some complement each other across different channels.

If you want to see how platforms like PChome, Shopee, and CoolPC change online shopping scenarios, see [Taiwan E-commerce and Digital Payment Ecosystem](/en/technology/e-commerce-and-digital-payment-ecosystem). This article stops at the last mile of physical checkout.

So, having a brand in the phone only answers whether the user side has obtained the tool; it cannot directly answer whether the merchant has connected a compatible receiving end. Seeing the same QR code doesn't mean every app, scanning direction, and funding source can complete the transaction. From phone icon to "usable everywhere in Taiwan," at least three layers are missing in between: bound instrument, merchant contract, and transaction specification.

App counts also need to rein in the exaggerated "average of five." MIC's 2024 online sample shows 86% use five or fewer, of which 61% use three or fewer, and 14% use six or more. Public data has no mean, median, or full distribution for one to five. [^5] It supports multi-app use but cannot construct a "typical user" who happens to have exactly five.

The FSC's June 2026 monthly table sums electronic payment institution reported accounts at 41.129 million. This is an institutional sum, not a cross-institution deduplicated natural person count. It measures a contract snapshot and cannot answer how many tools a typical user installs. [^6]

> **📝 Curator's Note**
> The logos on the counter are brands; the interfaces on the phone are UIs; the FSC table accumulates accounts with contracts not yet terminated. Calling all three "user numbers" flattens the most important layers of the payment market.

The front end looks similar; differences surface when the transaction reaches the other end. No matter how many apps users download, they cannot complete the merchant's application, verification, and reconciliation. The second threshold sits behind the counter.

## Consumers See One Scan; Merchants Must Connect an Entire Flow

For a store to accept Taiwan Pay, it must first apply to an acquiring financial institution to become a contracted merchant, obtain an acquirer code, merchant code, and terminal code, then complete service registration. [^7] After starting collection, equipment and network must operate, staff must know how to confirm notifications and handle refunds, and the back office must complete reconciliation and disbursement. For small shops, posting a collection code is just the beginning; a daily operational tail follows.

Taiwan Pay's merchant FAQ writes concretely the moment most easily hidden by a single QR: when the device is offline, the merchant can still generate an amount-less QR on the login page for the consumer to scan, but the merchant's phone receives no transaction push. [^8] The customer's screen shows paid; the receiving end lacks notification at that moment; the counter must decide whether to release goods and where to check this transaction. Scanning is just the action's starting point; on-the-spot confirmation and post-facto accounting make the transaction truly land.

Taiwan Pay leaves rates to the merchant-acquirer contract, officially stating "transaction processing fees are determined by contract between the merchant (payee) and the acquiring bank." Other platforms' public schemes, chain merchants' bargaining, and different payment sources each have their own terms. [^9] Fees enter the merchant's calculus, as do disbursement time, refunds, network, equipment, clientele, learning, and reconciliation.

An academic study of Tainan commercial district merchants even found that perceived usefulness, ease of use, consumer adoption, and compatibility positively correlate with adoption intention, while perceived cost had no significant relationship in that sample. [^10] This also means merchants don't just bear costs; they weigh whether the tool is easy to use and whether customers have already adopted it. This local study cannot be generalized to all Taiwan, but it suffices to block the single explanation that "merchants only refuse because of fees."

The Central Bank-commissioned survey gives acceptance differences magnitude. Among 611 stall vendor samples, 76.1% accept only cash. Among 1,436 store samples, the proportion is 46.8%. The report links the vendors' higher proportion to venue, equipment, and scale. [^11] Here "cash only" is relative to all non-cash tools; it cannot be inverted to infer mobile payment acceptance rates, nor used to criticize vendors for lacking progressive intent.

```tw-bars
Stalls and storefronts, different acceptance conditions (cash only, %)
Stall vendor sample | 76.1 | 611 samples
Store sample | 46.8 | 1,436 samples
Source: Central Bank commissioned payment instrument survey, published 2024
```

Payment universality requires both ends: consumers have tools, merchants have processes that sustain collection, confirmation, refunds, and reconciliation. Institutional friction has taken shape here, but it still explains only part of multi-app and cash coexistence. The next app is sometimes a spare tire, sometimes more like a membership card.

## Installing Another App: Sometimes to Make It Work, Sometimes Just to Make It Work Better

When the Central Bank survey asked about mobile payment pain points, 18.9% chose "merchant doesn't accept," 12.0% chose "merchant doesn't accept my habitual tool," and only 7.6% chose "too many types on the market." Poor network signal accounted for 6.5%, dead phone battery 3.4%. [^12] These are multiple-choice self-reports, not causal proportions of each factor causing cash transactions, but they show a real gap between "having an app" and "the app in hand works."

Hu Tzu-li's "different channels" corresponds exactly to this plugging motive. If a store doesn't take the habitual tool, the user may install another. Friends splitting bills at a gathering, family wanting to gift points — these may leave another app installed. The same MIC survey series notes 57% of users have used payment financial services beyond consumption, most commonly split transfers and point gifting at 38%. [^13] These functions bring payment apps into social and membership life; reasons for holding them have long exceeded whether the counter can scan.

Visa's 2022 commissioned four-region study interviewed 1,000 Taiwan respondents aged 18–55, finding 40% regularly track consumption points and 22% calculate carefully for the best rewards. [^14] This data cannot estimate "how many people install extra apps for rewards"; it only shows some respondents track points and calculate promotions for rewards. Retail membership ecosystems also grow their own payment tools. To see how PX Mart (全聯福利中心) moved from store network and membership management toward a high-frequency life platform, see [PX Mart](/en/economy/pxmart-supermarket); corporate history and controversies are not rewritten here.

The Ministry of Economic Affairs' retail survey provides a longer trend. Calculated by payment amount from returned samples, consumer mobile payment share rose from 0.6% in 2017 to 11.2% in 2023, while cash fell from 41.1% to 23.0%. Officials attribute part of the change in general merchandise retail and cosmetics/drugstores to membership ecosystems and merchant-built payment tools. [^15] Mobile payment share expanded; cash share declined over the same period. Multi-brand competition indeed creates choice. If multi-app is diagnosed solely as institutional failure, this upward trajectory and users' active preferences would be missed.

```tw-slope
Retail payment amount share: mobile payment up, cash down (%)
2017 | 2023
*Mobile payment | 0.6 | 11.2
Cash | 41.1 | 23.0
Source: MOEA Department of Statistics, Wholesale, Retail and Food Services Business Survey
```

Multiple tools thus play two roles: one plugs acceptance and funding-source gaps; the other carries discounts, points, membership, and transfers. App count itself does not measure the distance to adoption, universality, or cashlessness. With competition and plugging intertwined, the question becomes how many layers integration has reached.

## TWQR Integrates Common QR, But Hasn't Merged All Payments Into One

TWQR is the substantive response to "too many payment specs, too many merchant signs." This common QR standard connects participating financial institutions and electronic payment institutions. By end-2025, Central Bank data listed 44 financial institutions, 10 electronic payment institutions, and 678,000 cooperating contracted merchants. Full-year 2025 transactions: 146.73 million, NT$713.6 billion. [^16] "Taiwan QR payments completely cannot interoperate" no longer matches reality.

![TWQR "one contract, diverse payments" official institutional illustration](/article-images/technology/taiwan-mobile-payments-single-contract-2026.webp)
_TWQR "one contract, diverse payments" official institutional illustration, presenting FISC's claimed merchant onboarding method. This is institutional publicity illustration and cannot independently prove every cooperating store is active, every transaction succeeds, or all payment sources interoperate. Image: Financial Information Service Co., Ltd. (TWQR official website), fair use for commentary._

The common QR solved an important layer, but the acquiring pages published by cooperating banks also show boundaries remain. The "payer-scan" (主掃) list on that page includes Taiwan Pay, JKOPAY, All Pay, EasyWallet (悠遊付), iPASS Money (一卡通), and 11 tools total. The "payee-scan" (被掃) list is shorter and limited to QR Auth spec. All Pay, iCash (愛金卡), and All Win Pay (全盈支付) appear on the payer-scan list but not on that page's payee-scan list. [^17] Scanning direction, spec, and institutional participation change usable combinations; merchants must still apply to acquiring institutions for TWQR.

678,000 is the cooperating contracted merchant count; this Central Bank public data does not provide how many merchants remain actively transacting, nor full market share or on-site success rates. The common QR also does not automatically unify credit card or account funding sources, membership points, rewards, merchant contracts, fees, and refund processes. It pushes signage and transaction specs toward a common layer, but hasn't flattened every app's commercial world.

> **📝 Curator's Note**
> TWQR's most recognizable achievement lies inside the scope of "common" (共通): common QR and cross-institution messaging have formed a large-scale foundation; daily activation at cooperating stores, every funding source, and every membership rule are still decided by other layers. Universality is being built layer by layer.

The interoperability threshold has moved forward, but cooperating merchant count won't automatically become every person, every transaction, every funding source working. While integration engineering is still underway, cash remains with another explanation.

## Cash Doesn't Prove Mobile Payment Failed; It Usually Just Doesn't Need to Ask "Can This Work" First

For a tool to be universal, it must at least let users obtain it, let merchants recognize and confirm, let transactions complete, and provide a predictable recovery method when the phone dies, network is unstable, or notifications fail. This means both sides know where to check, when to retry, and which alternative path to take after failure. After transaction completion, whether both sides can find the same record is also part of recovery.

By this yardstick, mobile payments have shortened checkout in massive daily consumption, yet still cannot provide the same path for every scenario. In most face-to-face small-value transactions, cash requires no registration, no device; handover and confirmation happen simultaneously, so it continues as the lowest common interface. It too has change-making, safekeeping, and counting costs; here we compare acceptance and failure thresholds, not total operational costs.

The Central Bank survey brings human differences into cash's role: respondents over 40 and in remote areas show higher cash-only proportions. Data supports directional differences, not extension into a single portrait of all elderly or rural residents. [^18] This round of research also lacks sufficient data to fill proportions or invent voices for minors, persons with disabilities, migrant workers, and short-term visitors. Popular tools may be convenient for some, yet still don't mean everyone can obtain the same account, card, phone, or network.

Heavy users in familiar chains and life circles may indeed go long periods without touching bills. Another person keeping cash may simply be habit, privacy preference, or spending control — not past payment failure. Institutional friction, merchant acceptance, rewards, membership, habits, preferences, and failure resilience jointly act; existing surveys cannot rank them in a single causal order.

The adoption threshold asks how many people use it. The universality threshold asks whether different people and stores can complete across scenarios. Cashlessness asks further: after failure, can you recover? The further the first two thresholds advance, the fewer people may carry cash, but when the last bill leaves the wallet depends on whether exceptions have become too few to warrant backup.

Below is a hypothetical scenario constructed from the official FAQ's offline limitations, not an actual case: the merchant's phone is offline; the login page still shows an amount-less QR. The customer scans, but the merchant receives no credit push. Both stare at their screens; the transaction is stuck between "can pay" and "can confirm on the spot." The customer finally pockets the phone and produces a bill. That bill doesn't judge technology win or loss; it simply, in this scenario, still doesn't need to ask first: "Which ones do you take here?"

## Further Reading

- [Taiwan E-commerce and Digital Payment Ecosystem](/en/technology/e-commerce-and-digital-payment-ecosystem) — Review twenty years of platform and logistics battles in Taiwan e-commerce.
- [Taiwan FinTech Development](/en/economy/taiwan-fintech-development) — Place payment cases back into Taiwan's decade of FinTech development between openness and risk control.
- [PX Mart](/en/economy/pxmart-supermarket) — See how PX Mart moved from store network and membership management toward a high-frequency life platform.

## Image Sources

- Header image: Financial Information Service Co., Ltd. (TWQR official website), [original source](https://www.twqr.com.tw/), Fair use editorial commentary. Original image is thumbnail from official video "Shopkeeper's Heart | Sun Moon Fragrant Meat Floss"; this article uses it only for commentary on TWQR institutional publicity.
- In-text image: Financial Information Service Co., Ltd. (TWQR official website), [original source](https://www.twqr.com.tw/), Fair use editorial commentary. Original image is "One Contract, Diverse Payments" official institutional illustration.

## References

[^1]: [MIC: 2025 Mobile Payment Consumer Survey](https://mic.iii.org.tw/research.aspx?id=730) — Hu Tzu-li explains active users install more tools for different channels, and publishes survey methodology, adoption rates, and app-count intervals.

[^2]: [MIC: 2025 Mobile Payment Consumer Survey](https://mic.iii.org.tw/research.aspx?id=730) — Data collected in Q3 2024, online survey, 5,000 valid samples. 92% ever-used and 84% regularly-used both limited to that sample.

[^3]: [Central Bank: CBDC Issue Commissioned Questionnaire Survey Results](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Survey methodology, sample, and weighting description, plus public results: 73.8% mixed use, 25% cash only, 1.2% non-cash only.

[^4]: [FSC Financial Wisdom Network: Mobile Payment Teaching Materials](https://moneywise.fsc.gov.tw/uploaddowndoc?file=financeroom%2F202001131202240.pdf&filedisplay=%E6%96%B0%E5%A2%9E%E6%95%99%E6%9D%90PPT-+%E8%A1%8C%E5%8B%95%E6%94%AF%E4%BB%98-%E5%AE%9A%E7%A8%BF.pdf&flag=doc) — Categorizes by bound instrument, technology, and regulations: mobile credit card, mobile debit card, QR scanning, electronic payment institutions, and electronic tickets.

[^5]: [MIC: 2025 Mobile Payment Consumer Survey](https://mic.iii.org.tw/research.aspx?id=730) — Publishes 2024 intervals for five-or-fewer, three-or-fewer, and six-or-more; no mean or median published.

[^6]: [FSC Banking Bureau: 2026 June Electronic Payment Account Key Information](https://www.fsc.gov.tw/userfiles/file/BB-1156_%E9%9B%BB%E5%AD%90%E6%94%AF%E4%BB%98%E5%B8%B3%E6%88%B6%E9%87%8D%E8%A6%81%E8%B3%87%E8%A8%8A%E6%8F%AD%E9%9C%B2.pdf) — Sum listed as 41,128,870; footnote defines as registered and non-terminated contract user counts per institution.

[^7]: [Taiwan Mobile Payment: Merchant Operation FAQ](https://www.twmp.com.tw/Faq?n=95c7608a1dfc4fa1834f4467d41a32d1) — Explains merchants must contract with acquiring financial institution and obtain acquirer, merchant, and terminal codes.

[^8]: [Taiwan Mobile Payment: Merchant Collection FAQ](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — Explains device offline can still generate amount-less QR but cannot log in or receive transaction push.

[^9]: [Taiwan Mobile Payment: Merchant Collection FAQ](https://www.twmp.com.tw/Faq?n=29250e1aae5e4963a550de09d86a26be) — Officially states transaction processing fees determined by contract between merchant and acquiring bank; cannot be pushed as uniform market rate.

[^10]: [NCKU: Tainan Commercial District Merchant Mobile Payment Adoption Study](https://researchoutput.ncku.edu.tw/en/studentTheses/what-factors-affect-stores-willingness-to-adopt-mobile-payment-de/) — Doctoral dissertation abstract lists significant and non-significant factors of adoption intention; study scope limited to Tainan commercial district sample.

[^11]: [Central Bank: CBDC Issue Commissioned Questionnaire Survey Results](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Stall vendor 611 samples, store 1,436 samples; links cash-only difference to venue, equipment, and scale.

[^12]: [Central Bank: Payment Instrument Survey in Financial Stability Report](https://www.cbc.gov.tw/tw/dl-207586-2f35d674d8a34ee09d1d1c0fd68a6fea.html) — Charts list merchant non-acceptance, habitual tool non-acceptance, too many types, signal, and battery as multiple-choice pain points.

[^13]: [MIC: 2025 Mobile Payment Consumer Survey](https://mic.iii.org.tw/research.aspx?id=730) — Survey lists payment financial services beyond consumption; split transfers and point gifting most common.

[^14]: [Visa Taiwan: 2022 Mobile Wallet and Electronic Payment Consumer Study](https://www.visa.com.tw/about-visa/newsroom/press-releases/nr-tw-230310.html) — Discloses Taiwan 1,000 respondents aged 18–55 and proportions tracking rewards and calculating promotions.

[^15]: [MOEA Department of Statistics: Retail Mobile Payment Share Press Release PDF](https://www.moea.gov.tw/Mns/populace/news/wHandNews_File.ashx?file_id=116845) — Wholesale, Retail and Food Services Business Survey 2017 and 2023 payment amount shares and membership ecosystem explanation.

[^16]: [Central Bank: 2025 Annual Report](https://www.cbc.gov.tw/tw/dl-225165-b56d9b5e547843a4822acd679cb4868e.html) — Lists 2025 year-end TWQR participating institutions, cooperating contracted merchants, and full-year transaction volume and value.

[^17]: [Cooperative Bank: TWQR Cross-Institution Acquiring Service](https://www.tcb-bank.com.tw/company-banking/credit-card/special-store/twqr) — Lists payer-scan and payee-scan available institutions, QR Auth spec, and merchant application method; shows interoperability layered by direction and spec.

[^18]: [Central Bank: CBDC Issue Commissioned Questionnaire Survey Results](https://knowledge.cbc.gov.tw/uploads/20240613/d2196a6b-784b-45ea-b559-10b824915887.pdf) — Report presents directional differences by age and region; this article does not fabricate specific group proportions or voices based on this.

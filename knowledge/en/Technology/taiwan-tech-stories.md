---
title: "Taiwan's Tech Narrative: 100-Point Chips, 60-Point Microphones"
description: "Taiwan produces 100-point chips but tends to describe them with the tone of a supplier presentation. For the same chip, Qualcomm makes a myth, while MediaTek provides a spec sheet; NVIDIA doesn't make any and earns twice as much profit as its foundry partner. The market has long calculated this 40-point gap, and the bill is printed on net profit margins."
date: 2026-08-15
category: 'Technology'
tags:
  [
    'Technology',
    'Storytelling',
    'Branding',
    'Semiconductor',
    'TSMC',
    'NVIDIA',
    'MediaTek',
    'Qualcomm',
    'HTC',
    'Jensen Huang',
    'Morris Chang',
    'Smile Curve',
    'Subtext',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-15
lastHumanReview: false
difficulty: 'beginner'
readingTime: 16
image: '/article-images/technology/tsmc-fab-14b-2025.webp'
imageCredit: '4300streetcar'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg'
rationale: "{'why_this_hook': '從「同一顆晶片兩種講法」的反差切入，讓讀者先看見那 40 分長什麼樣子，再用財報數字把它換算成錢。', 'whats_excluded': '政府政策與主權 AI（政治敏感，超出本文查證範圍）；韓國三星製程競爭史；台灣新創公司名單流水帳；估值模型的公式化推導。', 'where_it_hedges': '張忠謀「護國神山」2021 原始報導與張忠謀自傳銷量標「待補來源」；蘋果手機利潤占比以「高峰估計」軟化；示意歸納的引語在文內明示非逐字。', 'whos_pushing_back': '認為低調是代工生意命脈、吹牛會傷信任的供應鏈從業者；認為台灣工程師文化不需要向矽谷敘事投降的人；被拿來當負面教材的公司員工。'}"
sporeLinks: []
curation: 'incubating'
translatedFrom: 'Technology/台灣科技說故事.md'
sourceCommitSha: '6d762f5ac'
sourceContentHash: 'sha256:7e79f4d7834c55c1'
sourceBodyHash: 'sha256:e24305e511c42507'
translatedAt: '2026-09-14T00:53:25+08:00'
---

# Taiwan's Tech Narrative: 100-Point Chips, 60-Point Microphones

![Exterior of TSMC Fab 14B in Hsinchu Science Park, multi-story industrial buildings stretching under a blue sky, the physical site of advanced process capacity](/article-images/technology/tsmc-fab-14b-2025.webp)
_TSMC Tainan Fab 14B, May 2025. Photo: 4300streetcar. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **30-Second Summary:** In June 2024, Jensen Huang turned TSMC's chips into an era at National Taiwan University (NTU) Stadium; in the same quarter, TSMC’s earnings call slides featured financial figures, capacity utilization rates, and conservative outlooks. NVIDIA reported $120.1 billion in net profit on FY2026 revenue of $215.9 billion; TSMC, which manufactures chips for it, reported $55.1 billion in net profit on 2025 revenue of $122.4 billion[^5][^6]. The company that designs the story earns twice as much as the one who makes it. This article aims to translate the subtext behind the words.

On June 2, 2024, at NTU Stadium. Jensen Huang took the stage wearing a black leather jacket and spoke for two hours. The audience resembled a concert: live streams, foreign media, and crowds holding up phones. He talked about Blackwell and CUDA, turning slides into an opening ceremony of an era[^19].

On the same island, less than 100 kilometers south, in Hsinchu. TSMC's earnings call presented a different style: financial figures, capacity utilization rates, quarterly increases/decreases, and conservative forecast ranges. The world's most advanced chips are on that production line, but the entire presentation sounds like an accounting class.

The same chip, two ways of speaking. The 40-point difference has long been calculated by the market.

Taiwanese people have seen the difference between these two scenes since childhood. We are accustomed to: the product is what we make; the applause belongs to others. At trade shows, Taiwanese vendors talk about costs, yield rates, and delivery times; American brands speak on stage about the future, mission, and changing the world. This gap—this 40 points—is what this article reveals.

## The Same Chip, Two Ways of Speaking

In October 2024, two presentations occurred less than two weeks apart. MediaTek unveiled Dimensity 9400 in Shenzhen, while Qualcomm held Snapdragon Summit on Maui, Hawaii[^9][^10].

[MediaTek](/en/economy/mediatek/) is one of the world's largest mobile chip suppliers by shipment volume and holds a 70% market share in TV chips[^4b]. Qualcomm surpasses MediaTek in shipments, revenue, and brand premium. What is the difference? Qualcomm sells the name "Snapdragon": having been named since 2006 for nearly twenty years[^8], it has its own mascot and annual technology festival. The phrase "Powered by Snapdragon" at global flagship phone launches is more eye-catching than the phone manufacturer's own trademark.

MediaTek sells the spec sheet. The Dimensity 9400 presentation covers process, IPC, and power efficiency curves; the numbers are solid, and the evaluation circles call it the "King of Efficiency"[^9]. But consumers only know Snapdragon.

MediaTek has long held the throne of shipment volume. In Q3 2020, MediaTek's mobile chip shipments first surpassed Qualcomm, capturing about 31% market share[^7]. However, in those years when it led in shipments, MediaTek's main income came from mid-to-low-end phones; the top tier was always dominated by Qualcomm. It wasn't until the arrival of Dimensity 9000 at the end of 2021 that MediaTek first put a flagship chip into comparison tables for Android flagships. The specifications caught up, but the presentation still felt like a supplier briefing to a client.

MediaTek actually knows this problem. In recent years, it has started learning: a flagship chip needs its own name, and a presentation needs a grand opening show; partner phone manufacturers are willing to put "Dimensity" in their advertising slogans. The direction is correct, but the start was over ten years late. Brand building is a marathon; those who start early gain compounding interest with every lap.

> 💡 **Did You Know**
> Snapdragon is the English name for _snapdragon flower_, a type of flower; Dimensity refers to the third star in the Big Dipper[^8]. One company named after a garden, one after a constellation—both are good. The difference is: Qualcomm turned that flower into a brand that walks the red carpet, while the starlight of Dimensity mostly remains on the spec sheet.

> 📝 **Curator's Note**
> The branding war in the chip industry is brutally specific: when consumers spend money, they recognize Snapdragon or Dimensity; no one asks which chip TSMC manufactured. Qualcomm started building its brand in 2006, while MediaTek only attached the "Dimensity" series to flagships at the end of 2019. Twenty years of narrative compounding cannot be caught by any spec sheet.

## How Quietly Brilliant Died

Let's look back at an even more painful case. On April 7, 2011, HTC's market capitalization surpassed Nokia, reaching about $33.8 billion[^1]. At that time, HTC held about 20% of the mobile market, standing alongside Samsung and Apple as one of the "Big Three"[^2].

In technology choices, HTC was almost perfect: it released the first Android phone, G1, in 2008[^3]. The One in 2013 featured an aluminum alloy unibody design, a large-pixel camera path, and dual cameras—all pioneered by them. But do you remember its global brand slogan?

![Close-up of the side body of HTC One M7, featuring an aluminum alloy unibody design, which was an industry standard when released in 2013](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), 2013. Photo: Asmoth, CC BY-SA 4.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

"Quietly Brilliant." Quiet excellence.

At the same time, Samsung's advertisement, "The Next Big Thing is already here," directly showed Apple fans queuing outside stores, making them look foolish[^18]. HTC treated humility as a brand claim, while Samsung positioned Apple as the villain. More than two years later, HTC's stock price plummeted from thousands to hundreds[^2].

HTC actually had a chance to turn things around. Many things about the One (M7) in 2013 were industry-leading: aluminum alloy unibody, UltraPixel large-pixel camera, and BoomSound front dual speakers. That year, it won "Best Phone of the Year" from major media outlets, but its sales lagged far behind Samsung's S4 during the same period. The M7 presentation focused on specifications; Samsung talked about lifestyle; Apple presented fingerprint unlocking as world-changing. Three ways to talk about a generation of phones, three fates.

Looking back at HTC's downfall, it is not just one slogan. But the failure in narrative was the first domino to fall: when the market began choosing camps based on stories, those who could not tell a story were placed in the "obsolete" basket. Engineers did not believe this, thinking the product would speak for itself. The product does speak, but most consumers do not listen or want to listen.

![Image of HTC Dream opening its sliding keyboard, the first Android phone globally in 2008](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), 2008. Photo: Marcus Sümnick, CC BY 3.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **Curator's Note**
> "Quietly Brilliant" is itself a translation of subtext: a company choosing "low-key" as its global brand claim is voluntarily handing over narrative sovereignty. Spec sheets are forgotten; stories are remembered. HTC did everything right in technology choices but lost every narrative choice.

## The Smile Curve: Taiwan Mapped Its Situation 30 Years Ago

The tragedy of HTC is not an isolated case; it has a diagrammatic proof.

In 1992, Shi Zhenrong drew the "Smile Curve" in _Reinventing Acer_: R&D and branding are at both ends with the highest value, while manufacturing is in the middle with the lowest value[^4]. Taiwanese people drew this map themselves, and for the next thirty years, Taiwan's massive tech contingent was stuck at the bottom of the curve: Foxconn assembling iPhones for Apple, with gross margins often only single digits. Apple took the vast majority of the profit from the entire smartphone industry—market research estimates it to be over 80%[^11].

[TSMC](/en/economy/tsmc/) is an exception. By adhering to the rule of "not designing its own products," it turned contract manufacturing into a business that held both ends: clients cannot leave, and it does not need to compete with clients for consumer worship. But this business is built on B2B trust, which does not require telling stories to the public. TSMC's low profile is a business strategy; the side effect is that the place in Taiwan best at making chips is precisely the one least needing to practice storytelling.

Not everyone reached the right end either. Wistand (ASUS) established the sub-brand ROG (Republic of Gamers) in 2006, cultivating a community of hardware enthusiasts who recognized the brand; it is one of the most recognizable symbols in global gaming hardware[^15]. But ROG is a minority: most Taiwanese companies are afraid to enlarge their logos even on the front of the product.

Taiwan did reach the right end at times. Acer was once among the top three PC brands globally, and the five letters "Acer" were once seen on boarding gates in airports worldwide. But the profit from PCs was too thin—so thin that brand premium could not support the weight of the right end. ROG proved that the right end can be reached, but only by choosing the right battlefield.

The cruelest aspect of the Smile Curve is that it is a multiple-choice question no one has re-examined in thirty years. Thirty years ago, Taiwan chose to stand in the middle because it was the most rational answer at the time: lacking capital, lacking brand, lacking market—contract manufacturing was the only way to survive. The real danger is continuing to treat the rational answer from thirty years ago as today's answer.

## Economics of Hype

Numbers are the most honest. NVIDIA reported $215.9 billion in revenue and $120.1 billion in net profit for Fiscal Year 2026 (February 2025 to January 2026)[^5]. TSMC reported $122.4 billion in revenue and $55.1 billion in net profit for the full year 2025[^6]. NVIDIA's chips are almost entirely made by TSMC; it sells the CUDA ecosystem, the story of the "AI era." The result: the company that designs the story earns 1.8 times the revenue and 2.2 times the net profit of the one who makes it.

Up the same supply chain to the consumer end, the gradient is steeper:

| Supply Chain Position        | 2025 Revenue    | Net Profit       | Net Margin |
| :--------------------------- | :-------------- | :--------------- | :--------- |
| Foxconn (Assembling iPhones) | NT$8.1 Trillion | NT$189.4 Billion | 2.3%       |
| Apple (Selling iPhones)      | $416.2 Billion  | $112 Billion     | 26.9%      |
| TSMC (Making Chips)          | $122.4 Billion  | $55.1 Billion    | 45.0%      |
| NVIDIA (Telling the Story)   | $215.9 Billion  | $120.1 Billion   | 55.6%      |

_Data: Foxconn and Apple are for FY2025; NVIDIA is for FY2026 (as of January 2026); TSMC is for 2025, sourced from company financial reports (cross-verified with Wikipedia's financial columns)[^5][^6][^11]._

Assembly earns 2.3%; selling the brand earns 26.9%; making advanced processes earns 45%; telling the chip story earns 55.6%. Valuation is a discount of future cash flow. Half of the future is made by engineering, and half is told through narrative. The Silicon Valley default culture is "fake it till you make it." Taiwan's default culture is "don't speak until we have done it." The difference between these two cultures is not an ethical gap, but a discount rate gap: the market discounts less for a "story that can be told," and more for a "skill that cannot be told."

The mechanism of brand premium is also straightforward: for the same chip manufactured by TSMC, the money phone makers are willing to pay extra when branded with Snapdragon is the premium. Where does this premium come from? From the spectacle of the launch events, from the fixed annual Summits, and from the habitual expectation of developers that "the next Snapdragon will be faster." These things do not appear in spec sheets, but they appear in financial reports.

Some argue this is a market failure, that Wall Street is speculating. But in the same market, TSMC does not receive discounts: its net margin of 45% is one notch higher than Apple's. The market is actually willing to pay for Taiwan's capabilities, provided those capabilities can be articulated. TSMC’s clients speak for it: every Apple launch event and every NVIDIA GTC is free advertising for TSMC.

Some ask if telling a big story becomes deception. Jensen Huang's answer is in the financial reports: every word he speaks is supported by capacity, yield, and shipment volume. The boundary between storytelling and boasting is whether there is something to back it up after speaking. Taiwan has things, but it often forgets to speak them.

> ⚠️ **Controversial View**
> One faction argues that Taiwan's 60-point narrative is a virtue: the lifeblood of contract manufacturing is trust, and low profile is an asset; if TSMC constantly held press conferences, clients would not sleep well. Another faction argues that narrative discounting transmits systematically: Taiwanese companies are undervalued, salaries are underestimated, and talent flows to companies that can tell stories, meaning the next generation's products will be even less capable of storytelling. Whichever side you believe, you live in that loop. Both views currently exist and have not yet won.

## Taiwan Does Not Lack Storytellers

Taiwan does have people who speak well.

Morris Chang called TSMC a "National Shield Mountain" (Huguoshenshan) in 2021[^12]. These four characters made the entire island willingly yield water, electricity, and land for the chip industry. This is top-tier marketing: every news report about water or power shortages automatically becomes a public service announcement of "The Divine Mountain needs you." In late 2024, Morris Chang published the second volume of his autobiography, which became a bestseller[^13b].

The fact that his autobiography sold as a bestseller speaks volumes: an elderly entrepreneur writing his life in two books, and Taiwanese people queuing to buy them. Taiwanese people love stories and love buying stories, but when it is their turn to speak, the words run short.

These Taiwanese who can tell stories share one common trait: Morris Chang worked at Texas Instruments for twenty-five years; Jensen Huang started a company in Silicon Valley for thirty years; Su Zi-feng studied at MIT until her Ph.D. None of them honed these skills in Taiwan. The soil of Taiwan grows such people, but the Taiwanese workplace does not teach this skill. School teaches how to draw a circuit correctly, not how to turn a circuit into an era.

So the problem is never talent. The problem is that Taiwan's industrial structure sends those who can tell stories abroad or confines them to contract manufacturing meetings. To unravel this knot, it requires more than just marketing departments of a few companies; it must change from corporate governance and salary structures all the way up to school education.

![A video image of Morris Chang attending the 2021 APEC Economic Leaders' Meeting as a representative leader, an official Presidential Office photo](/article-images/technology/morris-chang-apec-2021.webp)
_Morris Chang at the 2021 APEC Economic Leaders' Meeting. Photo: Wang Yu Ching / Presidential Office, CC BY 2.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

Shi Zhenrong drew the Smile Curve as a concept sale: one concept that allowed his corporate management philosophy to be cited by business schools worldwide.

Jensen Huang was born in Tainan and immigrated to the US at age nine[^13]. Su Zi-feng was born in Tainan and immigrated with her family at age three[^14]. The two people who tell the best semiconductor stories globally are both of Taiwanese origin, raised in America.

![Jensen Huang giving a lecture in CS 153 at Stanford University, wearing his signature black leather jacket and gesturing to explain](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang lecturing in CS 153 at Stanford University, April 2026. Photo: Anderseidesvik, CC BY-SA 4.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

There are also storytellers among Taiwan's startups. Gogoro was founded in 2011 and presented the battery swapping station at CES in 2015 as an "energy network," claiming to be an energy company while selling motorcycles. The narrative reached a point where it listed on Nasdaq via SPAC in 2022, attracting $50 million investment from BP's Castrol in 2024[^16]. Gogoro is still seeking a business loop, but its example shows: storytelling at least gets you a ticket to be tested by the market. Those who cannot speak do not even get into the door.

The rule is clear: Taiwan does not lack talent for storytelling; it lacks an environment that allows stories to be amplified. The "contract manufacturing gene" teaches "the client is the protagonist"; the storytelling environment teaches "I can be the protagonist."

> 📝 **Curator's Note**
> The most interesting part of the four characters in "National Shield Mountain" is what Morris Chang meant when he said it: he was telling Taiwanese society a story that needed support—for electricity, water, land, and talent. Storytelling is not vanity; it is infrastructure for industrial policy. Taiwanese people understand these four words, which means their narrative power is not broken, just rarely used externally.

## Subtext Translation Guide

The same technical fact, two ways of speaking. Translate the subtext behind the words, and judge the difference yourself.

| Speaker                         | Surface Statement                                                                                                           | Subtext Translation                                                                                                                                                         |
| :------------------------------ | :-------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| TSMC Earnings Call              | "Capacity utilization is continuously rising, and we are confident in long-term growth."                                    | The world's most advanced chips can only be made by me, but this sounds less like an engineer.                                                                              |
| Taiwanese Engineer Presentation | "This technology still has some room for optimization."                                                                     | We have already reached the world's best; let's take a discount first so we are not embarrassed.                                                                            |
| US Startup Pitch Page 1         | "We are building the world's first AI-native platform to reinvent a $5 trillion industry."                                  | Currently, the company only has three engineers and one PPT, but the dream is priceless; please give us money first.                                                        |
| Taiwanese Startup Pitch Page 1  | "Team members graduated from NTU/National Tsing Hua University and worked at MediaTek for eight years, holding 12 patents." | We don't know how to talk about vision, so we use education and credentials as armor.                                                                                       |
| Jensen Huang                    | "The more you buy, the more you save."                                                                                      | This card is expensive, but if you don't buy it, electricity and compute power will eat more.                                                                               |
| Qualcomm Snapdragon Summit      | "The era of on-device AI begins now."                                                                                       | Wait until iPhone releases its benchmark; first, let you feel like you are witnessing an era.                                                                               |
| HTC 2010 Ad                     | "Quietly Brilliant"                                                                                                         | We are brilliant, but we are too shy to speak loudly.                                                                                                                       |
| Samsung 2011 Ad                 | "The Next Big Thing is already here."                                                                                       | The people queuing at Apple stores look so stupid; come buy mine.                                                                                                           |
| Elon Musk                       | "We will make life multiplanetary."                                                                                         | Rockets sometimes explode now, but the narrative must take off first.                                                                                                       |
| Morris Chang 2021               | "Semiconductors are Taiwan's National Shield Mountain."                                                                     | These four characters made the entire island yield water, electricity, and land for chips. One sentence from a storyteller is worth an entire year of earnings call slides. |

_The quoted sentences in the table are illustrative generalizations of typical speech patterns, not verbatim quotes; the columns for Jensen Huang, HTC, Samsung, Musk, and Morris Chang refer to actual public slogans or statements[^17][^18][^12]._

After translation, you will find that the difference between telling a story well and telling a story poorly is often just two different word orders of the same fact.

This table is not meant to mock anyone. Humility is very useful in engineering: it allows cooperation to proceed and prevents quality control from being lax. But humility becomes a discount coupon once it leaves the meeting room. What Taiwan needs to learn is to keep humility in the lab and bring confidence to the stage.

## Back to NTU Stadium

Every slide Jensen Huang presented that night was physically made in cleanrooms in Hsinchu, Taichung, and Tainan. The story is told; the world pays the bill. The people in the cleanrooms continue their shifts; the earnings calls remain conservative.

100-point technology does not automatically become a 100-point narrative. Those 40 points require someone to stand on stage, wear the leather jacket as a battle uniform, and turn chips into an era.

Taiwan's next National Shield Mountain may not be a new chip, but a new story.

> ✦ Qualcomm turned one SoC into a brand that walks the red carpet; Jensen Huang turned TSMC's chips into an era; Morris Chang used four characters to make the entire island yield for semiconductors. Taiwan has things worth 100 points, what it lacks is someone willing to stand on stage and make them 100 points.

---

**Further Reading**:

- [Semiconductor Industry: The 50-Year Material Revolution from RCA Technology Transfer to Nitride Gallium and Quantum Packaging](/en/technology/taiwan-semiconductor-industry) — The complete technological narrative of the National Shield Mountain, and the bond with "NVIDIA securing CoWoS capacity"
- [Taiwan Enterprise: TSMC](/en/economy/tsmc) — The governance and financial structure of this company that has written low profile into its business model
- [Taiwan Enterprise: MediaTek](/en/economy/mediatek) — Why the world's largest mobile chip supplier is still catching up in narrative
- [Taiwan Enterprise: Wistand (ASUS)](/en/economy/htc-android-pioneer-vr-transformation) — The complete corporate history of Quietly Brilliant's death
- [Jensen Huang](/en/people/jensen-huang) — Born in Tainan, raised in America, the person who tells the best chip stories globally
- [NVIDIA in Taiwan](/en/technology/nvidia-in-taiwan) — The relationship between that leather jacket and the Taiwanese supply chain
- [Computex: Two Major International Computer Shows, One Remaining in Taipei](/en/technology/computex) — Every May, global AI giants take turns telling stories in Taipei using the same rhetoric

## Image Sources

This article uses 5 CC licensed images, cached at `public/article-images/technology/`:

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Photo: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Photo: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Photo: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Photo: Wang Yu Ching / Presidential Office, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Photo: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## References

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — On April 7, 2011, HTC's market cap was about $33.8 billion, surpassing Nokia.

[^2]: [Wikipedia — Wistand (ASUS)](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — In 2011, mobile market share was about 20%, and the market capitalization exceeded one trillion NTD, with stock prices once reaching thousands.

[^3]: [Wikipedia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — The first Android phone globally in 2008.

[^4]: [Wikipedia — Smile Curve](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Proposed by Shi Zhenrong in _Reinventing Acer_ in 1992.

[^4b]: [Wikipedia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — One of the world's largest mobile SoC suppliers by shipment volume; holds about 70% market share in TV chips.

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — NVIDIA official press release; FY2026 revenue $215.9 billion, net profit $120.1 billion (cross-verified with Wikipedia's financial columns: https://en.wikipedia.org/wiki/Nvidia）).

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — TSMC official investor page; full year 2025 revenue $122.4 billion, net profit $55.1 billion (cross-verified with Wikipedia's financial columns: https://en.wikipedia.org/wiki/TSMC）).

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — In Q3 2020, MediaTek's mobile chip shipments first surpassed Qualcomm, capturing about 31% market share.

[^8]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — The Snapdragon SoC platform was released in November 2006; the brand name comes from the snapdragon flower and the third star of the Big Dipper (the two naming methods are public brand materials, awaiting official source links).

[^9]: [MediaTek — Dimensity 9400 Press Release](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — Dimensity 9400 was released in October 2024; evaluation circles generally praise its power efficiency (a synthetic description). The first device to carry it can be seen in [Wikipedia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200).

[^10]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024 was held on Maui, Hawaii, where the Snapdragon 8 Elite was unveiled (the official press release URL is defunct; relying on Wikipedia for reference).

[^11]: [Wikipedia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) — / [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Foxconn's revenue in FY2025 was NT$8.103 trillion, and net profit was NT$189.35 billion (net margin approx. 2.3%); Apple's revenue in FY2025 was $416.2 billion, and net profit was $112 billion (net margin approx. 26.9%). Peak smartphone profit share for Apple is over 80%: Counterpoint historical estimates (awaiting source links)

[^12]: [Wikipedia — National Shield Mountain](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — An alternative name for TSMC (Silicon Shield); "Semiconductors are Taiwan's National Shield Mountain" was a public statement by Morris Chang in 2021 (news source awaiting link).

[^13]: [Wikipedia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — Born in Tainan in 1963, immigrated to the US at age nine in 1972.

[^13b]: The second volume of Morris Chang's autobiography was published in November 2024 and became a bestseller (awaiting source links).

[^14]: [Wikipedia — Su Zi-feng](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — Born in Tainan in 1969, immigrated to the US with her family at age three.

[^15]: [Wikipedia — Wistand (ASUS)](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — Established the sub-brand "Republic of Gamers" (ROG) in 2006.

[^16]: [Wikipedia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — Founded in 2011; presented Gogoro Smartscooter and energy network at CES in 2015; listed on Nasdaq after merging with Poema Global SPAC in 2022; BP's Castrol announced an investment of up to $50 million in 2024.

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — Jensen Huang's "The more you buy, the more you save" comes from this official video.

[^18]: "Quietly Brilliant" was HTC's global brand slogan starting in 2009; "The Next Big Thing is Already Here" was Samsung's Galaxy ad slogan in 2011; "We will make life multiplanetary" is a SpaceX mission statement (all are public commercial texts).

[^19]: [NVIDIA at Computex 2024 — Official Keynote Video](https://www.youtube.com/watch?v=pKXDVsWZmUU) — Jensen Huang's keynote speech at NTU Stadium on June 2, 2024.

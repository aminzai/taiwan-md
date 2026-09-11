---
title: 'Pirate Kingdom: The Reverse Engineering of the Counterfeit Era Woven into TSMC’s Trust Gene'
description: 'From the 1970s to the 1990s, Taiwan was dubbed the "Pirate Kingdom" by international media. This article traces the rise and fall of the counterfeit industry, how the June 12 deadline and the Special 301 clause forced institutional transformation, and explains why TSMC’s "do not compete with customers" trust model is the reversal of this history.'
date: 2026-08-18
category: 'History'
tags:
  [
    'Copyright',
    'Counterfeit',
    'TSMC',
    'Special 301',
    'Copyright Act',
    'Morris Chang',
  ]
subcategory: '經濟發展史'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-18
lastHumanReview: true
researchReport: 'reports/research/2026-08/pirate-kingdom-tsmc-trust.md'
readingTime: 12
rationale: "{'why_this_hook': '「海盜王國」的國際汙名與台積電信任經濟形成強反差，影片引發的懷舊共鳴可轉化為制度史知識增量', 'whats_excluded': '排除未經正式新聞證實的坊間細節（麥當樂判決最終結果未下筆），排除中國大陸觀點來源', 'where_it_hedges': '「六成仿冒品出自台灣」為 1986 年美聯社轉述美國 ITC 單方估計，文中已標明來源', 'whos_pushing_back': '部分民眾對盜版年代帶有懷舊情感，可能質疑仿冒與台積電成功直接掛鉤的因果敘事'}"
curation: 'incubating'
translatedFrom: 'History/台灣盜版史.md'
sourceCommitSha: '373a07d35'
sourceContentHash: 'sha256:b8045765d1db3274'
sourceBodyHash: 'sha256:a195178fa37b285e'
translatedAt: '2026-09-11T07:53:43+08:00'
---

> **30-Second Overview:** From the 1970s to the 1990s, Taiwan was dubbed the "Pirate Kingdom" by _Newsweek_ due to large-scale counterfeiting and piracy. The U.S. International Trade Commission (ITC) estimated that 60% of global counterfeit goods originated in Taiwan at the time, and in 1989, Taiwan was placed on the U.S. Special 301 Priority Watch List[^4][^5]. This article outlines three pivotal moments of transformation: the 1992 revision of the Copyright Act and the end of the "pirate manga warring states" period via the June 12 deadline; the 1980s shift in the electronics industry from counterfeiting Apple to OEM/ODM work for IBM-compatible machines; and the 1987 founding of TSMC, which redefined Taiwanese manufacturing through a trust model of "not competing with customers." The Pirate Kingdom did not disappear; it was transformed by institutions and business models into the Semiconductor Kingdom[^9][^13].

# Pirate Kingdom: The Reverse Engineering of the Counterfeit Era Woven into TSMC’s Trust Gene

In December 1984, _Newsweek_ and _Asia Magazine_ simultaneously bestowed a moniker upon Taiwan: "The Pirate Haven"[^1]. Three months prior, _Life Magazine_ had published a cover story labeling counterfeiting as "Taiwan’s emerging industry"[^1]. At the time, foreign tourists would disembark and head straight to Zhongshan North Road, spending roughly $25 USD on a counterfeit Rolex Oyster Perpetual. Bookstore windows displayed pirated Simplified Chinese editions of the _Encyclopædia Britannica_. In corner convenience stores, pirated manga stacked in plastic baskets cost 10 New Taiwan Dollars (NTD) each, available for schoolchildren to choose from after class[^2]. Around the same time, the "Mai Dang Le" (McDonald's) shop next to Taipei Main Station, whose sign resembled the Golden Arches, had been open for six years—six years before the legitimate McDonald's entered Taiwan. In the first instance of a trademark lawsuit, the legitimate McDonald's actually lost, with the trademark examination authority citing the official reason that the legitimate trademark had the "potential to deceive the public or cause public misconception"[^3]. Counterfeiting in 1980s Taiwan was not just an underground economy; it was an open, legitimate enterprise: signs were hung earlier than the originals, and lawsuits were filed before the originals. In that era, almost no one felt this was wrong, because the boundary between "counterfeiting" and "imitation" was only drawn clearly after the U.S. brought the Section 301 clause to the negotiating table.

The tentacles of plagiarism also extended into the entertainment industry. The "Little Tigers," who were popular across the two sides of the Strait and Hong Kong in the late 1980s, copied the Japanese idol group "SMAP" from group composition to performance style. The "Golden Five Treasures" concept of the ratings champion _Golden Actors_ was derived from a Japanese TBS program. Yang Fan’s signature character "Yang Popo" (Grandma Yang) was modeled after the character of Japanese comedy legend Takeo Chizu. These programs and groups were not officially licensed copies but were learned frame-by-frame by local producers watching Japanese TV signals. This was the survival method of Taiwan’s entertainment industry in an era without licensing fees or original manufacturers’ supervision.

> In March 1986, _The New York Times_ quoted a Western diplomat: "Until a few years ago, Taiwan was the undisputed counterfeit and piracy capital of the world."[^2]

📝 Curator’s Note: The global standing of Taiwan’s semiconductor industry and a period of counterfeiting that the whole world criticized are separated not by a fault line, but by the same group of people.

![The archway and stalls of Huaxi Street Tourist Night Market: The "Snake Market" of the 1980s was the distribution center where foreign tourists purchased counterfeit watches and electronics (Image provided by Wikimedia Commons author, CC0 Public Domain)](https://upload.wikimedia.org/wikipedia/commons/e/e0/Huaxi_Street_Night_Market.jpg)

## Who Called Taiwan the Pirate Kingdom

"Pirate Kingdom" was not a metaphor; it was a documented diplomatic record. The Office of the United States Trade Representative (USTR) has published the "Special 301 Section" watch list annually since 1989. Taiwan appeared on the "Priority Watch List" in the first year, entering and exiting the list for nearly two decades, until being officially removed in January 2009[^4]. To understand the weight of this label, one must return to the era’s coordinates: in the mid-1980s, Taiwan’s export volume had leaped from the $1 billion level in 1970 to $38.8 billion in 1986, making it one of the fastest-growing exporters globally. The fact that exports included both genuine goods and counterfeits was precisely what caused anxiety for both Washington and business owners[^11]. In the removal report, the U.S. described Taiwan as "transforming from a haven for pirates into a sanctuary for innovative R&D." The same document recorded both the birth and death of the Pirate Kingdom[^4].

The reality of the mid-1980s was uglier than the list. In March 1986, _New York Times_ reporter John Burns surveyed the market in Taipei: a counterfeit Rolex Oyster Perpetual at Huaxi Street Night Market (then called the Snake Market) sold for only $10 USD, while a genuine Tiffany watch sold to Chinese customers in the same era was priced at $8,850 USD. A set of pirated WordStar office software cost $5 USD. The brand name for a counterfeit Yale lock, "Yeal," dared to go on shelves with just one extra letter[^2]. An Associated Press report in September of the same year was even more direct, citing an estimate from the U.S. International Trade Commission (ITC): in the early 1980s, up to 60% of counterfeit goods circulating globally originated in Taiwan[^5]. The Reagan administration’s public statement at the time was that U.S. industries lost $20 billion USD annually due to counterfeiting. A 1986 _Business Week_ article calculated the bill even more harshly, stating that counterfeiting cost the U.S. 750,000 jobs[^6].

```tw-stat
# Key Figures of Taiwan's Pirate Kingdom #
1989|Start of Listing|Taiwan first included in the U.S. Special 301 Priority Watch List
2009|Removal|Taiwan officially removed from the Special 301 Watch List
60%|Counterfeit Share|Estimate that 60% of global counterfeit goods originated in Taiwan in the early 1980s (ITC)
750k|Lost Jobs|1986 Business Week claimed counterfeiting cost the U.S. this many jobs
Source: U.S. International Trade Commission (ITC) / U.S. Trade Representative / Business Week, 1986-2009
```

📝 Curator’s Note: For an economy with $10 billion USD in annual exports, having 60% of global counterfeit goods come from its factories—this was not petty theft, but a state-level production line.

## Manga: From Censorship to the June 12 Deadline

The proliferation of pirated manga had an unexpectedly governmental starting point. In the 1960s, the government implemented a strict manga censorship system. Local creators repeatedly hit walls in submissions, causing the local manga market to shrink. Pirated Japanese manga, however, obtained legal publication numbers issued by the government through bribing censors, filling the market at extremely low prices without paying royalties[^7]. In other words, in the heyday of pirated manga, pirates held government-issued certificates[^7].

This structure of "legal piracy" created a unique upbringing for a generation of Taiwanese manga readers. Children could buy a Japanese manga for 10 or 20 NTD at corner convenience stores and bookstores around schools: no copyright page, inconsistent translation quality, and even protagonist names might vary between publishers, but the price was only one-tenth of the genuine magazine. Manga was no longer a middle-class leisure activity but a commoner’s daily routine. The government killed the livelihood of local creators with its censorship system while simultaneously endorsing pirates with publication numbers. Under this double squeeze, the local manga industry completely lost its competitive space.

On July 15, 1987, martial law was lifted, and the submission system失效 overnight. Pirated manga entered a "Warring States" period. Publishers like Tong Li, Da Ran, and尖端 (Ling’an) simultaneously rushed to translate the same popular works. _Dragon Ball_ and _Slam Dunk_ were each translated by different publishers; readers wanting the same manga might end up with four different translations[^8]. At the peak of the Warring States period, one issue of _Shonen Express_ (Shao Nian Kuai Bao) had a circulation of 230,000 copies, a number higher than the total circulation of many genuine magazines at the time[^8].

On June 12, 1992, the revised Copyright Act took effect. Foreign translated reproductions printed under the old law could continue to be sold during a two-year buffer period. After June 12, 1994, all pirated translated manga had to be pulled from shelves. Manga fans called this day the "June 12 Deadline." The scene of bookstores clearing inventory at auction before the deadline is a collective memory for that generation of Taiwanese[^9]. In the last one or two months before the deadline, bookstores and manga rental shops across Taiwan piled inventory to the doorways, labeling them "Total Clearance." Many students used the money that previously bought only one book to carry home half a bag of pirated books—it was the farewell ceremony for pirated manga in Taiwan, and the opening ceremony for the era of genuine goods.

The transformation after the deadline was not completed overnight. The pricing of licensed genuine manga was several times higher than pirated versions. Publishers had to learn the editorial processes, translator standards, and royalty splits of Japanese originals. Former reprint masters transitioned into copyright managers and editors. Readers also adapted: from "buying from whoever is available" to "only one publisher has the genuine version," rushing to buy genuine single-volume editions and supporting publishers became the new daily routine for manga fans in the late 1990s. The deadline forced a structural transformation: Tong Li signed _Akira_ with Kodansha in January 1992, becoming the first Taiwanese manga work to formally sign with a Japanese publisher. Pirated operators transformed one by one into genuine agents[^8].

```tw-timeline
# 40 Years of Pirated Manga: From Legal Piracy to Genuine Agency #
1960s|Censorship Era|Local manga declined, pirated Japanese manga circulated cheaply with government numbers
1987|Lifting Martial Law Warring States|Submission system failed, multiple publishers rushed to translate the same work
1992.1|Genuine Signing|Tong Li signed *Akira* with Kodansha, first genuine agency
1992.6|Major Copyright Revision|Revised Copyright Act took effect, foreign works protected for the first time
1994.6.12|June 12 Deadline|Last day for sale of pirated translated reproductions, end of the piracy era
2009|International Removal|Taiwan removed from U.S. Special 301 Watch List
Source: Republic of China Copyright Act Article 112 / Commercial Times, 1992-2009
```

![The "One Country Hall" manga rental store in Shilin, established in 1986, is still operating today—In the 1980s and 90s, rental bookstores were the nerve endings of pirated manga distribution (Image provided by Wikimedia Commons author, CC BY-SA 3.0 License)](https://upload.wikimedia.org/wikipedia/commons/f/f1/Ikkoku-kan_Comic_Bookshop_Shilin_Branch_20101209.jpg)

## Electronics: Reverse Engineering the Apple Origin

Taiwan’s electronics industry made its first pot of gold through dismantling. In 1981, Acer (then named Multitech) launched the $70 USD "Little Professor No. 1" educational microcomputer. The following year, it launched the 7,950 NTD "Little Professor No. 2," which was almost a copy of the Apple II[^10]. A 1984 report in _The Christian Science Monitor_ wrote that computer shops around Zhongshan North Road in Taipei could burn out a counterfeit Apple computer within two hours, selling for $350 USD, roughly half the original price[^11]. Around the same time, Shentong Computer launched "Little Shentong," and Jingji Electronics launched the "Little Genius," an unlicensed Famicom-compatible console. Counterfeit categories spread from computers to game consoles[^10].

![Night market signs in the Ximending Pedestrian Zone: The electronics malls and clothing stalls around Ximending were once the main distribution centers for counterfeit goods and pirated software during the Pirate Kingdom era (Image provided by Wikimedia Commons author, CC BY 3.0 License)](https://upload.wikimedia.org/wikipedia/commons/2/23/Ximending_Main_Alley_at_Night.jpg)

In 1983, Apple Computer formally sued Taiwanese manufacturers for infringement. Multitech’s Little Professor No. 2 was seized by U.S. customs. Apple claimed its manual content was translated from Apple II documents. Ultimately, Multitech was required to pay $20 USD in compensation per machine[^10]. These lawsuits produced two results. First, Taiwanese manufacturers shifted the dismantling, copying, and rapid model-change skills honed through reverse engineering to OEM/ODM work for IBM’s open-architecture compatible machines. IBM contacted 11 Taiwanese manufacturers in the early 1980s; seven signed agreements to stop producing counterfeits and publicly apologized, subsequently shifting to authorized OEM work[^11]. Second, Shih Chen-jung, because the Multitech brand frequently encountered trademark disputes overseas, painfully swapped the accumulated brand value for $2 million USD in 1987, renaming it Acer[^10].

The electronics cluster in Hsinchu Science Park grew during this transition period from "counterfeiting to OEM." Taiwanese engineers in the counterfeiting era learned to read circuits, modify designs, and meet tight schedules. These skills instantly found a legal export after IBM’s open architecture, laying the foundation for Taiwan’s future status as an electronics manufacturing kingdom[^11].

It is worth noting that this transformation was not a moral awakening unique to Taiwan, but a result of the industrial structure brought by IBM’s open architecture. After the IBM PC hardware specifications were made public, the compatible machine market no longer needed to crack prototypes; it only needed to assemble and fine-tune faster and cheaper than the original. This was exactly what Taiwanese manufacturers had honed in the counterfeiting trenches for twenty years. From "copying the original manuscript" to "rushing OEM schedules," the skills were the same; the difference lay only in the authorization clauses on contracts. This skill lineage extended all the way to notebook OEM, motherboard OEM, and finally found its highest-level export in the cleanrooms of chip manufacturing. Taiwan’s Electronics Manufacturing Services (EMS) and ODM systems became number one globally over the next thirty years. From the late 1990s, over 70% of global notebook shipments were designed or assembled by the Taiwanese supply chain. That muscle memory of rapid mold opening, rapid model change, and rapid mass production, honed in the counterfeiting era, is the底色 (base color) of that 70% share[^11].

![The electronics business district around Taipei’s Guanghua Digital Plaza and the old Guanghua Bridge: From the 1960s to the 90s, the computer street around Guanghua Mall was the cradle of Taiwan’s electronic parts and assembly culture, and the core scene for the circulation of counterfeit microcomputers (Image provided by Wikimedia Commons author, CC BY-SA 3.0 License)](https://upload.wikimedia.org/wikipedia/commons/f/fe/Guang_Hua_Digital_Plaza_and_Mitsubishi_Delica_4WD_20080203.jpg)

## Special 301 Clause: The Revision Season Under the U.S. Tariff Knife

The bill of U.S. losses caused by counterfeiting eventually became a diplomatic and trade weapon. The U.S. threatened trade retaliation against Taiwan multiple times in the 1980s. In 1984, the Taiwanese government began prohibiting counterfeit exports and established a task force. The Trademark Act was revised in 1983, and computer software was included in the Copyright Act for protection[^11][^12]. Enforcement pressure also increased: criminal prosecution cases rose from 344 in 1983 to 629 in 1985. Customs made a yearly news spectacle of publicly crushing seized counterfeit computers with road rollers[^2][^5]. After Taiwan was included in the 1989 Special 301 list, the government further slashed the Patent Act, Trademark Act, and Copyright Act. Enforcement energy and statutory penalties rose simultaneously[^4][^12]. The 1992 major revision of the Copyright Act was the most lethal: it deleted the statutory limitation on "translation rights," explicitly listed computer programs as works, and granted foreign works their first protected status in Taiwan, directly ending the "legal" gray area of reprinting foreign books and software[^9]. After the revisions, the Ministry of Economic Affairs established the Intellectual Property Rights Coordination Council to coordinate enforcement. District procuratorates assigned special prosecutor groups. Enforcement extended from night market stalls to printing plants and importers.

The shadow of Special 301 fell not only on legal texts but also on daily industries. After counterfeit exports were explicitly prohibited, the counterfeit stalls of Huaxi Street Night Market and Ximending lost their primary income source. The apparel industry was forced to step back from sewing counterfeit Adidas and Nike labels, shifting to legal OEM work—the same sewing machines, the same workers, but the labels sewn into the fabric changed from "Abiba" to authorized international brand logos. The "Fairyland Theme Park" opened in Guansi, Hsinchu in 1984, mimicking Disney parks; the Meilun Mountain in Hualien once erected an unlicensed giant Mickey Mouse landmark. These landscapes disappeared or were modified one by one after IP regulations tightened, becoming an awkward record in local tourism history[^12]. The Pirate Kingdom’s signs were dismantled piece by piece by regulations.

The irony of this revision logic is that the exit of the Pirate Kingdom was not a spontaneous moral awakening of Taiwanese society, but an institutional transplant under the blade of trade retaliation. The think tank _Observer Magazine_ stated directly in a retrospective article that Taiwan only gradually established modern IP legal systems while cooperating with U.S. intellectual property requirements[^12]. It was not until the 2009 removal that this externally pressured legal system completed its twenty-year journey[^4].

```tw-versus
# Mid-1980s: The Legal Double Standard of the Pirate Kingdom #
Genuine Tiffany Watch|8,850 USD|Taipei selling price cited by The New York Times in 1986
Counterfeit Rolex Oyster|10 USD|Huaxi Street Night Market market rate at the same time
Genuine Software & Computers|Market Price|Zhongshan North Road computer shops completed counterfeits in two hours
Pirated WordStar Software|5 USD|Hundreds of times the price difference from the genuine version
Source: The New York Times / Los Angeles Times, 1986
```

## The Reversal of Trust: Why TSMC Had to Be the Opposite of Counterfeiting

In 1987, five years before the major revision of the Copyright Act and in the same year martial law was lifted, Morris Chang founded TSMC. TSMC’s business model was a deliberately designed counter-proposition: only wafer foundry services, no product brands, and absolutely no competition with customers. TSMC’s official website still writes into its management philosophy: "We have positioned customers as partners from the beginning and never compete with them," listing "Integrity" as the most basic and important core value[^13]. Current Chairman C.C. Wei summarized it more directly: "The first step to gaining customer trust is not to compete with customers."[^14]

This model works because the nature of semiconductor wafer foundry orders is a transaction of trust. Design companies hand over circuit diagrams, which are not yet taped out and whose leakage would destroy all competitiveness, to a foundry for production. If the foundry had a history of counterfeiting, or might jump down to make products itself, no one would place orders. In a country just called the "Pirate Haven" by _Newsweek_, Morris Chang built a business model that required state-level reputation endorsement—TSMC’s trust was a direct negation of the Pirate Kingdom image[^1].

Putting the timeline back to 1987, the gamble of this choice was much larger than it seems in retrospect. The international semiconductor mainstream at the time was the Integrated Device Manufacturer (IDM) model of Intel and Texas Instruments: designing, producing, and selling products themselves. No one believed a company that only produced but did not design could survive. Intel refused to invest in TSMC; European and Japanese partners withdrew one by one. Morris Chang, with almost no allies, used his personal reputation to guarantee this untested business model[^15]. The technical premise for the foundry model to work was that the capital threshold for wafer manufacturing was so high that design companies could not build factories themselves—but the commercial premise had only one word: trust.

The dividends of trust compounded annually over the next thirty years. Because it did not compete with customers, TSMC became the foundry for Intel, Qualcomm, NVIDIA, and Apple, companies that competed with each other. Each company laid their most confidential process requirements in Morris Chang’s cleanroom. If TSMC produced its own products, this entire customer network would collapse in a single quarter. TSMC turned "trust" into a moat, making it impossible for competitors to steal customers even if they caught up technologically, because the risk of customers moving factories was not just cost, but the possibility of confidential leaks[^14][^15]. In a 2021 interview with Morris Chang, Xie Jinhe asked about the most important element of TSMC’s success. Morris Chang’s answer was a single English word: "trust"[^15]. In his handwritten company development strategy assessment in 1998, among a dozen options, the only "do not" was low-price strategy—because low prices attract customers who focus solely on price, eroding trust[^15].

```tw-figure
# trust #
The single most important element of TSMC's success
— Morris Chang, 2021 Interview with Xie Jinhe
Source: Newtalk News, 2021
```

![Exterior of TSMC's Sixth Factory: Morris Chang founded TSMC in 1987. The pure wafer foundry model is built on the trust of "not competing with customers," completely cutting ties with the Pirate Kingdom image (Image provided by Wikimedia Commons author, CC BY 4.0 License)](https://upload.wikimedia.org/wikipedia/commons/3/3a/TSMC_Fab_6_front_May_2025.jpg)

![Intel Pentium Processor on a Wafer: TSMC’s trust model brings customers' most confidential chip designs into the cleanroom. Every chip on that same silicon wafer is a physical witness to the transaction of trust (Image provided by Wikimedia Commons author, CC BY 2.0 License)](https://upload.wikimedia.org/wikipedia/commons/6/65/Wafer_with_Pentium_chips.jpg)

📝 Curator’s Note: Mai Dang Le and McDonald’s, Little Professor and Apple II, Snake Market and TSMC—the same island honed "copying" into "trust" over forty years.

## Echoes: What Did the Pirate Kingdom Leave for Today?

The 2009 USTR removal report defined Taiwan as a "sanctuary for innovative R&D"[^4]. Looking back, the legacy left by the Pirate Kingdom era is double-sided. The positive side is the engineering capability honed through reverse engineering—dismantling, copying, model-changing, and meeting schedules. These capabilities found a legal export in the IBM open architecture and wafer foundry eras, nurturing a complete industrial chain from OEM to semiconductors[^10][^11]. Today’s data best illustrates the scale of this reversal: TSMC alone accounts for more than half of global wafer foundry revenue and handles the vast majority of the advanced process market share. Its market capitalization once accounted for nearly 30% of Taiwan’s stock market total. The same island, criticized thirty years ago as a counterfeit giant, now sees the world’s chip design companies rushing to hand over their most confidential blueprints to it[^13][^14]. The negative side is the trust liability: trademark squatting (the McDonald’s lawsuit took years to reach a final verdict), brand disputes (Multitech was forced to rename), and international image caused Taiwanese enterprises to pay decades of reputation costs in overseas markets[^3][^10].

It is worth noting that in this voyage from counterfeiting to trust, Taiwan was not an isolated case. The U.S. was called the largest copyright infringer in Europe in the 19th century. Germany mass-produced British machinery in its early industrialization and was required by British legislation to be marked "Made in Germany" to distinguish it. Japan similarly experienced an intensive phase of counterfeiting and imitation during its post-war economic takeoff[^6]. The common script for all countries is: counterfeiting is a shortcut for catching up, but only when institutions close the shortcut and open the path to monetizing real skills can industries complete their upgrade. Taiwan’s特殊性 (specialness) lies in the fact that closing the road and opening the road happened almost simultaneously—the 1992 major revision of the Copyright Act forced piracy toward genuine goods, and TSMC, born in 1987, redefined the credit rating of Taiwanese manufacturing with "trust." In the same year one road was closed, another was being laid in Hsinchu’s cleanrooms[^9][^13].

The Pirate Kingdom did not disappear; it was transformed by institutions and business models into the Semiconductor Kingdom. And whenever today someone criticizes a country as the new counterfeit giant, the historical response is often the same sentence: They are just still in the Pirate Kingdom’s years.

**Further Reading**: If interested in the literature context of the June 12 Deadline, read Chang Chung-hsin’s _Explanation of the Copyright Act Article by Article_ for a word-by-word analysis of Article 112, and Li Ling-yi’s 2015 NTU doctoral dissertation _A Study of Taiwan’s Manga Industry_[^9].

## References

[^1]: [Taiwan Tries to Get Its Computer Pirates Off High-Tech Seas](https://www.csmonitor.com/1984/1206/120632.html) — _The Christian Science Monitor_ December 6, 1984 report, recording Taiwan’s counterfeiting of Apple computers and government enforcement actions

[^2]: [TAIWAN CURBS ITS COUNTERFEITERS](https://www.nytimes.com/1986/03/30/business/taiwan-curbs-its-counterfeiters.html) — _The New York Times_ March 30, 1986 report, recording Snake Market counterfeit Rolex rates, Yeal counterfeit locks, and prosecution numbers

[^3]: [Taiwan Trademark Association Bulletin: Trademark Litigation History](https://www.taie.com.tw/data/magazine/1730856057OGWXL.pdf) — Taiwan Trademark Association bulletin publishing the McDonald’s and Mai Dang Le trademark lawsuit, where McDonald’s lost the first instance

[^4]: [Is Taiwan a Pirate Kingdom?](https://www.chinatimes.com/newspapers/20131229000166-260209) — _Commercial Times_ Yu Guo-qin column, organizing the Special 301 list entry/exit records and the 2009 U.S. removal evaluation

[^5]: ['Knockoff' King Taiwan Tries to Mend Its Ways](https://www.latimes.com/archives/la-xpm-1986-09-02-fi-13692-story.html) — _Los Angeles Times_ September 2, 1986 Associated Press report, citing ITC’s 60% counterfeit share and Li Da-qiang’s remarks

[^6]: [From the Counterfeiting Capital of the World](https://scholarship.law.vanderbilt.edu/cgi/viewcontent.cgi?article=1488&context=vjtl) — Vanderbilt Law Review academic discussion, reviewing Taiwan’s counterfeit industry and U.S. IP pressure

[^7]: [Tai-Hong Piracy Period](https://zh.wikipedia.org/zh-hant/%E8%87%BA%E6%B8%AF%E7%9B%9C%E7%89%88%E6%99%82%E6%9C%9F) — Wikipedia summary of the censorship system background and publication number issues for Taiwan-Hong Kong pirated Japanese manga from the 1960s to 1990s

[^8]: [Shonen Express and Piracy Warring States](https://zh.wikipedia.org/zh-hant/%E8%87%BA%E6%B8%AF%E7%9B%9C%E7%89%88%E6%99%82%E6%9C%9F) — Wikipedia recording the post-martial law translation rush, _Shonen Express_’s 230,000 circulation, and Tong Li signing _Akira_

[^9]: [June 12 Deadline](https://zh.wikipedia.org/zh-hant/%E5%85%AD%E4%B8%80%E4%BA%8C%E5%A4%A7%E9%99%90) — Wikipedia detailing the 1992 Copyright Act revision, Article 112 buffer period, and the events of June 12, 1994

[^10]: [Collectible Tech: The Ancestor of Taiwan Computers](https://scitechvista.nat.gov.tw/Article/c000008/detail?ID=e5ccc61e-3d6d-44a8-97ca-6bb19a390f51) — National Science Council Tech Garden citing _Scientific Development_ Issue 474, recording the Little Professor series and Apple lawsuit compensation

[^11]: [TAIWAN CURBS ITS COUNTERFEITERS](https://www.nytimes.com/1986/03/30/business/taiwan-curbs-its-counterfeiters.html) — _The New York Times_ simultaneously recording 1984 customs seizure, IBM signing/apologizing, and revision timeline (for additional 301 retaliation background see also [^4])

[^12]: [From Pirate Kingdom to Fraud Paradise](http://old.observer-taipei.com/www.observer-taipei.com/article7f6f.html?id=1105) — _Observer Magazine_ NO.33 retrospective on Taiwan’s forced establishment of IP legal systems under Special 301

[^13]: [Corporate Core Values and Management Philosophy](https://www.tsmc.com/chinese/aboutTSMC/values) — TSMC official website, publishing the core value of Integrity and the management philosophy of "Never Competing with Customers"

[^14]: [Wei Che-jia: Not Competing with Customers is the First Step of Trust](https://www.cna.com.tw/news/afe/202402290371.aspx) — CNA February 29, 2024 interview with Wei Che-jia on TSMC’s trust model

[^15]: [Xie Jinhe Asks Morris Chang: The Most Important Element of TSMC's Success](https://newtalk.tw/news/view/2021-11-02/660071) — Newtalk News November 2, 2021 report, Morris Chang’s answer "trust" and the no-low-price strategy

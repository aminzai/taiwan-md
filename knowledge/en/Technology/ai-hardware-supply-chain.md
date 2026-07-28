---
title: 'The AI Hardware Supply Chain: Where Taiwan Turns Cloud into Machinery'
description: "Generative AI may look like a cloud service, but it requires a physical path: someone designs the chips, someone manufactures the wafers, someone handles packaging, and others manage memory, power, cooling, motherboards, and cabinets. Taiwan's importance lies not just in TSMC, but in the fact that many critical checkpoints on this path are concentrated here; this shared interest is real, yet it comes with challenges regarding utilities, carbon emissions, wealth distribution, overseas expansion, and geopolitical risks, turning abstract slogans into verifiable evidence of a supply chain."
date: 2026-07-11
category: 'Technology'
tags:
  [
    'AI hardware',
    'semiconductors',
    'supply chain',
    'AI servers',
    'advanced manufacturing',
    'advanced packaging',
    'Taiwan technology industry',
  ]
subcategory: '半導體與硬體'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-07-11
lastHumanReview: false
researchReport: 'reports/research/2026-07/半導體供應鏈草稿地圖.md'
rationale: "{'why_this_hook': '從「兆元宴」座位表切入，讓讀者先看見 AI 硬體供應鏈不是單一公司，而是一整組台灣工程節點。', 'whats_excluded': '不做完整產業百科，也不逐一列出台灣所有半導體、伺服器與零組件公司。', 'where_it_hedges': '把台灣的供應鏈價值與水電、碳排、所得分配、海外設廠、地緣政治風險一起處理。', 'whos_pushing_back': '全球客戶與盟友一方面需要台灣，另一方面也透過海外設廠降低對台灣海峽周邊產能的單點依賴。'}"
image: '/article-images/technology/ai-hardware-supply-chain-flow.svg'
imageCredit: 'Taiwan.md Contributors'
imageLicense: 'CC BY-SA 4.0'
translatedFrom: 'Technology/AI硬體供應鏈.md'
sourceCommitSha: '8f5e81ee5'
sourceContentHash: 'sha256:96b285db19941653'
sourceBodyHash: 'sha256:96ecb5a6142f55f7'
translatedAt: '2026-07-28T18:52:01+08:00'
---

# The AI Hardware Supply Chain: Where Taiwan Turns Cloud into Machinery

> **30-Second Overview:** While AI appears to be about answering questions on a screen, it is actually backed by a long physical relay. Someone identifies the demand, someone designs the chips, someone manufactures them, and others assemble the chips, memory, cooling systems, power supplies, and motherboards into a machine before sending it into a data center. Taiwan's importance cannot be summed up simply by saying "TSMC is strong"; several critical legs of this relay are located in Taiwan. This shared interest is real, but it is not a guarantee; it simultaneously brings pressures regarding utilities, carbon emissions, wealth distribution, overseas expansion, and geopolitics.

On May 28, 2026, Jensen Huang hosted a dinner in Taipei. Media outlets dubbed it the "Billion-Dollar Banquet" because of the staggering combined market value of the companies represented by those in attendance. But what was most worth watching at that table wasn't who sat in the seat of honor, nor how much these companies were worth collectively.

What was truly worth looking at was the guest list.

For wafer fabrication, there was TSMC's Wei Che-jia. For AI server and cabinet assembly, there were Fox_con's Liu Yang-wei, Great Wall Technology's Lin Bai-li, Wiwynn's Lin Hsing-ming, and VIA Technologies' Hung Li-shu. For IC design, there was MediaTek's Tsai Li-hsing. For power and cooling, there were Delta Electronics' Cheng Ping, C-Power's Chiu Sen-bin, and Qianheng's Shen Jing-hsing. For motherboards and end-user brands, there were ASUS's Shi Chong-tang, Gigabyte's Yeh Pei-cheng, and ASRock's Chen Jun-sheng. The supply chain categories listed in the news reports—from wafer fabrication, testing/packaging, cooling modules, power management, and motherboards to assembly and branding—essentially form a cross-section of an AI server after it is disassembled.[^1]

![Jensen Huang holding an RTX Blackwell GPU during his keynote at CES 2025; the NVIDIA logo and the new generation of AI chip modules are visible against the black stage background.](/article-images/technology/jensen-huang-ces-2025-blackwell.webp)

_Jensen Huang showcasing the RTX Blackwell GPU at CES 2025. This image pulls "AI" from a software interface back into the physical hardware in his hands. Photo: Steve Jurvetson. CC BY 2.0 via Wikimedia Commons._

That was no ordinary corporate dinner. It was like placing a question on the table: When the whole world says AI needs Taiwan, what exactly is it needing?

The answer isn't just one company, nor is it just one chip. It is more like a path: starting from the statement "We need more AI computing power," moving through chips, factories, packaging, power, cooling, motherboards, cabinets, and finally arriving at the data center. Taiwan stands at several checkpoints along this road.

## Think of AI as a Service That Needs a Body

Most people interact with AI on phones, computers, or web pages. You type a string of text, and an answer appears. It looks like magic, much like a weightless cloud service.

![The Computex exhibition hall at Taipei Nangang Exhibition Center; wide aisles are lined with booths from information technology companies, and crowds gather, showcasing the visibility of Taiwan's hardware supply chain in trade shows.](/article-images/technology/computex-nangang-floor-2015.webp)

_The Computex exhibition hall at Taipei Nangang Exhibition Center. The AI hardware supply chain does not exist only in financial reports; it is concretely visible in exhibition halls, prototype machines, server cabinets, and business meetings. Photo: Solomon203. CC BY-SA 4.0 via Wikimedia Commons._

But for AI to answer questions, there must be machinery performing the calculations behind the scenes. Those machines sit in data centers, consume electricity, generate heat, require maintenance, and need people to build them, assemble them, and deliver them to customers.

You can think of AI as a large restaurant. What you see is the server bringing the dish to your table, but you don't see the menu design, procurement, the kitchen, the gas, water, electricity, refrigeration, the flow of food preparation, or the cleaning. AI is similar. You see the answer on the screen; behind it is an entire hardware kitchen.

Taiwan’s position is at many of the critical workstations within that kitchen.

## How One Order Becomes a Server Cabinet

An AI hardware supply chain often begins with a very common demand: cloud companies, model companies, or large enterprises need more computing power. While this sounds like purchasing a cloud service, it quickly transforms into a series of physical problems: What chips need to be designed? Where can they be made? How close can memory get to them? How is heat dissipated? How is power delivered? Finally, who assembles these expensive components into machines that can be shipped, maintained, and placed in data centers?

![Flowchart of the AI hardware supply chain: AI demand passes through chip design, advanced manufacturing, advanced packaging, HBM & substrates, cooling & power, motherboards, ODM/EMS, and AI cabinets before entering a data center; the diagram highlights several critical stages where Taiwan's concentration is high, such as manufacturing, packaging, power/heat management, boards, and assembly.](/article-images/technology/ai-hardware-supply-chain-flow.svg)

_Diagram created by Taiwan.md. This chart is not a market share map or a complete company directory; it illustrates a core path: how AI demand eventually becomes powered, cooled, and shippable machines._

At the front end, chip design is mostly held by companies like NVIDIA, AMD, Broadcom, Google, Amazon, and Microsoft. One of Taiwan's critical positions occurs when those designs must become physical chips. TSMC’s official technical roadmap lists logic processes such as 7nm, 5nm, 3nm, 2nm, A16, and A14; N2 is marked for mass production in the fourth quarter of 2025.[^2] For many AI chips, this step is where the design first touches Taiwanese soil.

However, manufacturing a chip does not mean AI can go online yet. AI chips need to be close to memory and require different chips to be connected into a system that can cooperate at high speeds. TSMC describes 3DFabric as a combination of 3D silicon stacking and advanced packaging technologies, including SoIC, CoWoS, and InFO. When the Associated Press reported on the new plant in Linkou, it also placed these within the context of strengthening AI chip production.[^3][^4] Here, Taiwan's role expands from "making the chips" to "connecting the chips into functional modules."

Moving further out, the supply chain becomes less of a straight line. HBM (High Bandwidth Memory) is primarily led by South Korean companies. Equipment, materials, and design software involve suppliers from the United States, the Netherlands, Japan, and Europe. Cloud platforms and model services are mostly in American hands. Taiwan does not dominate every segment, nor does it take the largest profit from every segment. Its uniqueness lies in the fact that critical nodes—wafer fabrication, packaging, testing, substrates, power, cooling, motherboards, and full-system assembly—are located very close to one another, having long been solved together as engineering problems.

![Layered diagram of AI servers: Chips & accelerators, boards & motherboards, power & cooling, servers & cabinets, and data centers are stacked sequentially, illustrating how GPUs become deployable AI infrastructure.](/article-images/technology/ai-server-rack-stack.svg)

_Diagram created by Taiwan.md. A GPU is only one core of an AI server; it must be connected to boards, power, cooling, full systems, cabinets, and data centers._

At the full-system stage, problems become very specific. The stronger the chip, the higher the current and the harder it is to dissipate heat. Motherboards, power supplies, cooling systems, chassis, management systems, and shipping schedules all move in tandem. Companies like Fox_con, Great Wall Technology, Wiwynn, VIA Technologies, Quanta, Compal, and Pegatron handle the work of assembling chips, boards, power, cooling, and mechanical designs into AI servers and cabinets. When Central News Agency reported on the shipment of Fox_con's new platform, it also placed it in the context of AI server system demonstrations.[^10]

Therefore, that flow chart isn't meant to make people memorize terms. It is intended to show: Taiwan’s value lies not just in a single company or a single chip, but in its ability to push complex products from wafers and packaging all the way to cabinets and data centers within a very short distance and timeframe. This density is what distinguishes Taiwan from typical low-cost manufacturing bases.

For general readers, this path also provides a method for reading news. The next time you see a company announce a new AI platform, you don't have to only ask who designed the chip; you can look further: Where was it packaged? Who built the full system? Who handled power and heat? Who manages lead times and maintenance? When these questions are asked, Taiwan’s silhouette in the supply chain becomes clearer and more specific, making it easier to evaluate.

## Semiconductors are the Entry Point, Not the Destination

Describing Taiwan's technology industry as "just TSMC" is convenient, but it overlooks many things.

A fab answers the question: "Can the chip be made?" The AI hardware supply chain must answer several other questions: Can the chip be connected to memory? Can it be powered, cooled, tested, and repaired? Can it be assembled into a full rack, a whole row, or an entire data center within the timeframe requested by the customer?

What truly needs investigation is what limitations each segment is solving. Cutting-edge logic processes solve "how to pack more transistors into smaller, more power-efficient chips." Advanced packaging solves "when a single chip isn't enough, can we connect computing chips, memory, and different dies as closely and quickly as possible?" The question for AI servers is something else: Can these expensive components be made into stable, maintainable, mass-producible, and deliverable machines?

Therefore, cooling and power are not supporting roles. As chips become more powerful, current increases and heat becomes harder to manage. If the power is unstable or heat cannot be dissipated, even the most advanced chip will have to throttle its speed or may not be able to go online at all. Mature processes have not disappeared for this reason; an AI machine still requires many components for control, connectivity, power management, and peripheral chips. Cutting-edge processes are like the engine; mature processes and components are like the brakes, fuel lines, dashboard, and cooling system. If any part is missing, the car cannot run reliably.

In this large map, it is enough to grasp one thing first: semiconductors are the entry point, not the destination. For AI to truly go online, it must travel through an entire path that turns chips into machines.

This is also why "Taiwan's value" should not be just a vague platitude. It can be broken down into a map: Who makes the wafers? Who does the packaging? Who handles cooling and power? Who builds the motherboards? Who assembles the full systems? Who manages lead times? Who handles utilities? Who is cut first when the cycle turns?

This map also helps people identify nuances in reporting. When an entrepreneur says "Taiwan is a partner," you can ask what they rely on: manufacturing, packaging, ODM, power, or the speed of the entire system's response. When a politician speaks of "mutual interests," you can ask which companies, cities, and workers those interests are concentrated upon. When an investor says "the AI outlook is promising," you can follow up to see if that promise lies in chip design, packaging capacity, server assembly, or cooling and power components. Once abstract slogans are broken into layers, it becomes harder for readers to be led solely by emotion.

## Mutual Interest is Real, but Not Magic

Taiwan's position in the AI hardware supply chain does indeed create mutual interests.

For NVIDIA, cloud giants, and global AI companies, Taiwan is where they turn designs into products. For countries like the United States, Japan, and members of Europe, Taiwan is an indispensable supply node for advanced chips and AI infrastructure. For Taiwan, this needed relationship brings exports, investment, employment, market visibility, and international political leverage.

When the Associated Press reported on Taiwan's AI economy in 2026, it placed robust growth, increased exports, and NVIDIA’s expanded presence in Taiwan alongside concerns about an AI bubble, geopolitical risks, and unequal distribution of wealth.[^5] This juxtaposition is important because it reminds readers: mutual interest is not a one-way protection or a shield that will never fail.

Other countries are working to move parts of the supply chain elsewhere. TSMC's expansion into the U.S., Japan, and Germany proves the world needs TSMC, but it also signifies that customers and governments do not want to bet all their risks on Taiwan alone. Overseas factories may not replicate Taiwan's full density in the short term, but they will change the negotiation structure over the long term.

Furthermore, corporate interests are not identical to national interests. NVIDIA wants stable supply and high margins. TSMC wants technological leadership and a global customer base. ODM manufacturers want orders and high capacity utilization. Taiwanese society wants wages, housing, energy security, environmental sustainability, and safety guarantees. These interests will overlap and conflict.

Everyone at the table is important, but power is not evenly distributed. NVIDIA holds the GPU architecture, the CUDA ecosystem, and the pace of the platform. TSMC holds advanced manufacturing and critical packaging capacity. Cloud giants hold the purchasing power for data centers. ODM manufacturers handle full-system design, cabinet assembly, and large-scale shipping, though their profit margins are typically much lower than those of chip design firms. Component manufacturers for power, cooling, substrates, and testing interfaces may secure better profits due to high technical barriers, while others fluctuate with the orders of major clients. This is why "mutual interest" must be unpacked: every segment in the same supply chain is needed, but not every segment holds equal power.

A more precise way to put it would be more cautious: The world needs Taiwan, which provides Taiwan with a significant set of leverage. However, that leverage must be maintained through defense, diplomacy, energy, industrial governance, and social distribution.

## Overseas Expansion is Not Simply Moving House

TSMC’s factories in the U.S., Japan, and Germany are often grouped into the same anxiety: if advanced manufacturing moves away, will Taiwan's "Silicon Shield" become thinner?

This question cannot be answered with a simple "yes" or "no."

On one hand, overseas plants are an extension of Taiwan's capabilities. Customers and allies are willing to provide subsidies, land, and political capital precisely because TSMC and the Taiwanese supply chain are so vital. These facilities bring TSMC closer to customers and make the global supply chain more politically acceptable.

On the other hand, overseas factories are a move to diversify risk. The U.S., Europe, and Japan do not want the most critical chips to be concentrated solely near the Taiwan Strait. Taiwan is needed, so it is invested in. Taiwan is too important, so it is being distributed. Both statements are true simultaneously.

However, one factory does not equal an entire ecosystem. Advanced manufacturing requires equipment, materials, chemicals, engineers, maintenance, yield experience, packaging capabilities, customer coordination, and supplier responsiveness. Moving a portion of production capacity out is fundamentally different from moving an entire industrial society.

Therefore, overseas factories are more like pulling several nodes out of the Taiwanese supply chain rather than unplugging Taiwan from the chain entirely. It will gradually change negotiation structures and test how Taiwan can retain its core R&D, leading-edge mass production, and supply chain density.

## Mature Processes are on the Same Map

The AI boom makes it easy to focus all attention on 3nm, 2nm, and CoWoS. However, an AI machine does not run solely on the most advanced chips.

Power management ICs (PMICs), controllers, sensors, networking chips, peripheral chips, automotive, and industrial control chips often still use mature processes. These chips do not make headlines like GPUs, yet they support power conversion, signal control, equipment monitoring, and numerous inconspicuous functions within data centers.

The global chip shortage during the pandemic taught the automotive, consumer electronics, and industrial sectors a lesson: the world doesn't just lack advanced chips; it also lacks those seemingly ordinary but indispensable mature nodes. Consequently, Taiwan’s semiconductor map cannot only look at the top. TSMC, UMC, SPIL, AU Instruments, and a suite of specialized process, testing, and material companies collectively form a thick foundation.

This point is crucial for readers. Taiwan's value should not be understood as a race in "nanometer" numbers. The more complex AI hardware becomes, the more it requires advanced and mature processes to work together. It increasingly requires full systems and components to be delivered in tandem.

Therefore, mature processes should be placed back on the same map. They are the chassis upon which AI hardware can operate reliably. The most advanced GPUs must stand atop a multitude of common chips to become truly usable, maintainable, mass-producible machines.

## The Bills from the "Protective Mountains"

Bringing the world's AI hardware demand to Taiwan also leaves the bill in Taiwan.

The first bill is electricity. Advanced fabs, EUV lithography, packaging lines, AI server testing, and data centers all require stable power. Tech media have reported warnings regarding the pressure on Taiwan’s semiconductor industry for green energy and power supply. TSMC continues to announce plans for EUV power saving and water management.[^6][^7] While efficiency improvements are vital, as long as AI demand continues to expand, the total volume of pressure remains.

The second bill is water and climate vulnerability. Chip manufacturing requires vast amounts of ultrapure water. A report by WIRED on chip manufacturing water usage noted that a single fab could use millions of gallons daily; during Taiwan's droughts, tensions between agricultural water and chip production have surfaced. Manufacturing capabilities cannot be separated from reservoirs, rainfall, recycled water, and regional allocation.[^8]

The third bill is carbon emissions and industrial path lock-in. Research by Roussilhe et al., using Taiwanese electronic component manufacturers as a sample, discusses how energy, water, and greenhouse gas emissions rise with production volume, as well as the risk of "carbon lock-in."[^9] The "Protective Mountains" (the core semiconductor firms) provide international leverage but also bind national energy and land use deeply into high-energy manufacturing.

The fourth bill is distribution. AI has driven up Taiwan's stock market, exports, and tech salaries, but not everyone stands on this primary growth chain. Traditional industries, service sectors, renters, and youth in non-tech fields may not share the dividends equally. When housing prices, electricity costs, land use, and public investment are all influenced by high-tech industries, "Taiwan's outlook is promising" does not equate to "every Taiwanese person's life getting better."

This is not intended to dismiss the importance of semiconductors and the AI supply chain. On the contrary, because it is so important, it is necessary to clearly define the costs.

## Where Taiwan Places Itself

Beyond foreign exchange and orders, the AI hardware supply chain provides Taiwan with a way to understand itself.

Taiwan is not merely a small island protected by the world, nor is it a technological empire that can unilaterally control the world's AI. It is more like a highly specialized engineering hub: needed, therefore possessing leverage; relied upon, therefore carrying responsibility; concentrated, therefore bearing risk.

The next time readers hear "Taiwan is irreplaceable," they do not need to stop at the slogan. They can visualize a physical path in their minds: the needs of model companies enter chip design; chip designs enter TSMC's manufacturing; wafers move into advanced packaging; packaged modules go to cooling, power, motherboards, and cabinets; finally, they are delivered to data centers by Taiwanese ODMs/EMSs.

This path is the concrete evidence. It transforms "mutual interest" from an emotion into a fact that can be discussed, questioned, and maintained.

Taiwan turns cloud into machinery. The true meaning of this sentence is: the most abstract AI ultimately must pass through the most tangible island.

This is one of Taiwan's clearest—and most necessary to see—positions today.

## Further Reading

- [Taiwan's Foreign Trade and Global Supply Chain](/economy/台灣外貿與全球供應鏈) — The macro background from export-oriented growth and triangular trade to the restructuring of US-China supply chains.
- [NVIDIA in Taiwan](/technology/NVIDIA在台灣) — How NVIDIA deeply embeds chip manufacturing, packaging, and server assembly in Taiwan.
- [Semiconductor Industry](/technology/半導體產業) — The long-term background from RCA technology transfer to TSMC's foundry model and the battlegrounds of materials and packaging.
- [Computex](/technology/Computex) — Why Computex Taipei has become a pilgrimage site for the global hardware supply side in the AI era.
- [Taiwan's Power and Semiconductors](/technology/台灣的電力與半導體) — The electricity bills, green energy pressure, and energy security behind the AI supply chain.
- [Semiconductor Water Use and Taiwan's Water Resources](/technology/半導體用水與台灣水資源) — How wafer fabs connect to reservoirs, droughts, recycled water, and local governance.
- [AI Supply Chain Overseas Expansion](/technology/AI供應鏈海外設廠) — How the Taiwanese supply chain—from TSMC and Fox_con to Wiwynn and Delta—is being invited by the world to expand abroad.

## Image Sources

- **AI Hardware Supply Chain Flowchart**: Created by Taiwan.md Contributors as an SVG illustration, CC BY-SA 4.0, stored at `public/article-images/technology/ai-hardware-supply-chain-flow.svg`. The nodes are organized based on the body text and references to explain how AI demand passes through chip design, advanced manufacturing, advanced packaging, HBM / substrates, cooling / power, motherboards, ODM / EMS, and AI cabinets before entering data centers; it is not a market share map nor a complete company directory.
- **AI Server Layered Diagram**: Created by Taiwan.md Contributors as an SVG illustration, CC BY-SA 4.0, stored at `public/article-images/technology/ai-server-rack-stack.svg`. Used to illustrate the system layers of AI servers from chips to data centers; it does not represent a complete company map or market share.
- **Jensen Huang showcasing RTX Blackwell GPU**: [Jensen Huang holding RTX Blackwell at CES 2025](<https://commons.wikimedia.org/wiki/File:Jensen_Huang_-_RTX_Blackwell_-_Nvidia_Keynote_-_CES_2025_Las_Vegas_(3).jpg>) — Photo: Pronoia, Wikimedia Commons, CC0. The version used in this article is cached at `public/article-images/technology/jensen-huang-ces-2025-blackwell.webp`.
- **Computex Nangang Exhibition Hall**: [Computex Taipei at Taipei Nangang Exhibition Center](https://commons.wikimedia.org/wiki/File:Computex_Taipei_at_Taipei_Nangang_Exhibition_Center_20150602.jpg) — Photo: NVIDIA Taiwan, Wikimedia Commons, CC BY 2.0. The version used in this article is cached at `public/article-images/technology/computex-nangang-floor-2015.webp`.

## References

[^1]: [CNA: Jensen Huang's "Billion-Dollar Banquet" features executives from TSMC, Fox_con, and others](https://www.cna.com.tw/news/afe/202605280300.aspx) — Reported by Central News Agency on May 28, 2026, regarding Jensen Huang's gathering of Taiwan AI supply chain leaders, listing categories such as wafer fabrication, testing/packaging, cooling modules, power management, motherboards, assembly, and branding.

[^2]: [TSMC Logic Technology](https://www.tsmc.com/english/dedicatedFoundry/technology/logic) — TSMC's official logic technology page, listing advanced logic processes such as 7nm, 5nm, 3nm, 2nm, A16, and A14.

[^3]: [TSMC Advanced Packaging Services](https://www.tsmc.com/english/dedicatedFoundry/services/advanced-packaging) — TSMC's official advanced packaging services page, explaining 3DFabric technologies including SoIC, CoWoS, and InFO.

[^4]: [AP: Taiwan takes a further step in production of AI chips with advanced new plant](https://apnews.com/article/1e087e92592b0b9ab7fb20442a5b8dc7) — Associated Press report on the Linkou plant and Jensen Huang's attendance, providing an international perspective on Taiwan's role in AI chip packaging.

[^5]: [AP: Taiwan's AI-powered economy soars in the shadow of bubble fears and China threats](https://apnews.com/article/7527bd4bf3089cbd2dab1c530ee61c3e) — Associated Press report from 2026 regarding Taiwan's AI-driven growth, while addressing risks like the AI bubble and geopolitical tensions.

[^6]: [Tom's Hardware: TSMC-led semiconductor association warns of power supply pressure](https://www.tomshardware.com/tech-industry/tmsc-led-semiconductor-association-begs-taiwan-government-for-clean-green-energy-as-demand-skyrockets-fabs-are-struggling-to-keep-up-with-power-needs) — Tech media report on the pressure for green energy and stable power in Taiwan's semiconductor industry.

[^7]: [Tom's Hardware: TSMC reduces peak power consumption of EUV tools by 44%](https://www.tomshardware.com/tech-industry/semiconductors/tsmc-reduces-peak-power-consumption-of-euv-tools-by-44-percent-company-to-save-190-million-kilowatt-hours-of-electricity-by-2030) — Report on TSMC's EUV power reduction plans and total consumption scale.

[^8]: [WIRED: Want to Win a Chip War? You’re Gonna Need a Lot of Water](https://www.wired.com/story/want-to-win-a-chip-war-youre-gonna-need-a-lot-of-water/) — WIRED 2023 report on the demand for ultrapure water in chip manufacturing and tensions during Taiwan's droughts.

[^9]: [Roussilhe et al.: From Silicon Shield to Carbon Lock-in?](https://arxiv.org/abs/2209.12523) — Study of 16 Taiwanese electronic component manufacturers regarding energy, water, and carbon footprint risks.

[^10]: [CNA: Liu Yang-wei: Optimistic about second half of year for Vera Rubin shipments](https://www.cna.com.tw/news/afe/202605290100.aspx) — Central News Agency report on May 29, 2026, regarding Fox_con's Chairman discussing the Vera Rubin platform and AI server systems.

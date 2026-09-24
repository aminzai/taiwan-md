---
title: '台湾テックが語る物語：100点のチップ、60点のマイク'
description: '台湾は100点のチップを作れるのに、ついサプライヤーのプレゼン調で語ってしまう。同じ一個のチップを、クアルコムは神話に、MediaTekはスペックシートに仕立てる。NVIDIAは一個も自ら作らないのに、純利益は受託製造側の2倍。この40点の差は、市場がとっくに勘定済みで、請求書は純利益率に印刷されている。'
date: 2026-08-15
category: 'Technology'
tags:
  [
    'テック',
    'ストーリーテリング',
    'ブランド',
    '半導体',
    'TSMC',
    'NVIDIA',
    'MediaTek',
    'クアルコム',
    'HTC',
    '黄仁勲',
    '張忠謀',
    '微笑曲線',
    '潜台詞',
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
rationale:
  why_this_hook: '從「同一顆晶片兩種講法」的反差切入，讓讀者先看見那 40 分長什麼樣子，再用財報數字把它換算成錢。'
  whats_excluded: '政府政策與主權 AI（政治敏感，超出本文查證範圍）；韓國三星製程競爭史；台灣新創公司名單流水帳；估值模型的公式化推導。'
  where_it_hedges: '張忠謀「護國神山」2021 原始報導與張忠謀自傳銷量標「待補來源」；蘋果手機利潤占比以「高峰估計」軟化；示意歸納的引語在文內明示非逐字。'
  whos_pushing_back: '認為低調是代工生意命脈、吹牛會傷信任的供應鏈從業者；認為台灣工程師文化不需要向矽谷敘事投降的人；被拿來當負面教材的公司員工。'
sporeLinks: []
curation: 'incubating'
translatedFrom: 'Technology/台灣科技說故事.md'
sourceCommitSha: '6d762f5ac'
sourceContentHash: 'sha256:7e79f4d7834c55c1'
sourceBodyHash: 'sha256:e24305e511c42507'
translatedAt: '2026-09-23T22:11:46+08:00'
---

# 台湾テックが語る物語：100点のチップ、60点のマイク

![台南科学園区のTSMC Fab 14B工場外観、多層の工業建築が青空の下に延び、先進プロセス生産能力の物理的現場](/article-images/technology/tsmc-fab-14b-2025.webp)
_TSMC台南 Fab 14B工場、2025年5月。Photo: 4300streetcar. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **30秒概観：** 2024年6月、黄仁勲が台大体育館でTSMC製のチップを一つの時代として語った。同じ四半期、TSMCの決算説明会スライドは依然として財務数字、稼働率、保守的な見通し。NVIDIA FY2026売上2,159億ドル、純利益1,201億ドル。それを作るTSMCは、2025年売上1,224億ドル、純利益551億ドル[^5][^6]。物語を設計する会社が、手を動かす会社の2倍を稼ぐ。この記事がするのは、台詞の裏にある台詞を翻訳することだ。

2024年6月2日、台大体育館。黄仁勲（こう・じんくん／ジェンスン・フアン）があの黒い革ジャンで登壇し、2時間語った。客席の様相はコンサートさながら：ライブ配信、外国メディア、スマホを掲げる人海。彼はBlackwellを語り、CUDAを語り、一枚一枚のスライドを一つの時代の開幕式に仕立てた[^19]。

同じ島の南、車で100キロ足らずの新竹。TSMCの決算説明会は別の絵面だ：財務数字、稼働率、前期比・前年比、保守的な見通しレンジ。世界最先端のチップがすべてあのラインで生まれているのに、説明会全体が会計の授業のように聞こえる。

同じ一個のチップ、二通りの語り方。その間の40点、市場はとっくに勘定済みだ。

この二つの光景の違い、台湾人は子供の頃から見て育った。私たちは慣れている：製品は私たちが作るのに、拍手は別人のもの。展示会では、台湾企業のブースはコスト、歩留まり、納期を語り、米国ブランドのステージは未来、使命、世界を変えることを語る。その間の落差、それがあの40点だ。その40点の正体を、この記事で翻訳して見せる。

## 同じ一個のチップ、二通りの語り方

2024年10月、二つの発表会が2週間足らずで開かれた。MediaTek（メディアテック）が深圳でDimensity 9400（天璣 9400）を発表し、クアルコムがハワイ・マウイ島でSnapdragon Summitを開催した[^9][^10]。

[MediaTek](/ja/economy/mediatek/)は出荷量ベースで世界最大級のスマホチップサプライヤーの一社であり、テレビチップシェアは7割[^4b]。クアルコムの出荷量は負けているが、売上とブランドプレミアムでは勝っている。違いはどこにあるか？ クアルコムが売っているのは「Snapdragon」という名前だ：2006年の命名から約20年育ててきた[^8]、独自のマスコット、独自の年次テックフェス。世界のフラッグシップ発表会で流れるあの「Powered by Snapdragon」の一文、スマホメーカー自らの商標より目立つ。

MediaTekが売っているのはスペックシートだ。Dimensity 9400の発表会の中身はプロセス、IPC、電力効率曲線、数字はすべて堅実で、レビュー界からの異名は「電力効率の王」[^9]。だが消費者が知っているのはSnapdragonだけ。

出荷量の王座、MediaTekは実はとっくに座っていた。2020年第3四半期、MediaTekのスマホチップ出荷量が初めてクアルコムを超え、シェア約3割[^7]。だが出荷量1位のあの数年、MediaTekの収益の大頭はミッドロー端末、フラッグシップの最上層はずっとクアルコムのものだった。2021年末にDimensity 9000が出るまで、MediaTekが初めてフラッグシップチップを各社Androidフラッグシップの比較表に送り込んだ。スペックは追いついたが、発表会は相変わらずサプライヤーが顧客向けに行うプレゼンのようだ。

MediaTekもこの問題は分かっている。この数年、学び始めた：フラッグシップチップに独自の名前を与え、発表会にオープニングショーを設け、協力するスマホメーカーも「Dimensity」を広告コピーに入れるようになった。方向は正しい、ただスタートが10数年遅かった。ブランド育成は長距離走、早走りした人が毎周複利で積み上げる。

> 💡 **ご存知ですか**
> Snapdragonはキンギョソウ（snapdragon flower）の英名、一種の花の名前。Dimensity（天璣）は北斗七星の第三星[^8]。一家は庭園から名を取り、一家は星図から名を取り、どちらも素敵だ。違いは：クアルコムはこの花をレッドカーペットを歩くブランドに育て上げたのに対し、天璣の星光は大半の時間、スペックシートの上に留まっている。

> 📝 **キュレーターメモ**
> チップ業界のブランド戦争は、残酷なほど具体的だ：消費者が財布を開くときに認識するのはSnapdragonかDimensityか、TSMCがどのチップを受託製造したかなど誰も問わない。クアルコムは2006年からブランドを育て、MediaTekが「天璣」シリーズをフラッグシップに冠したのは2019年末。20年の物語の複利、どんなスペックシートも追いつけない。

## Quietly Brilliantはいかにして死んだか

さらに遡って、より痛い事例を一つ。2011年4月7日、HTCの時価総額がNokiaを超え、約338億ドル[^1]。当時HTCはスマホ市場で約2割を占め、Samsung、Appleと並ぶ三巨頭だった[^2]。

技術選択では、HTCはほぼすべて正解だった：2008年、世界初のAndroidスマホG1を作った[^3]。2013年のOneはアルミ一体成型ボディ、大画素カメラ路線、デュアルレンズ、すべて先駆けだった。だが、そのグローバルブランドスローガンを覚えているだろうか？

![HTC One M7のボディ側面クローズアップ、アルミ一体成型設計、2013年発表時は業界の工芸ベンチマーク](/article-images/technology/htc-one-m7-2013.webp)
_HTC One（M7）、2013年。Photo: Asmoth, CC BY-SA 4.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

「Quietly Brilliant。」静かな傑出。

同時期、Samsungの広告「The Next Big Thing is already here」は、Apple Store前で行列するファンを直接撮影し、並ぶ人々を愚かに見せた[^18]。HTCは謙虚をブランド主張にし、SamsungはAppleを悪役の主人公にした。2年余り後、HTC株価は千元台から百元台へ崩落[^2]。

HTCには実は一度、巻き返しのチャンスがあった。2013年のOne（M7）が業界をリードしていた点は多い：アルミ一体成型ボディ、UltraPixel大画素カメラ、BoomSoundフロントデュアルスピーカー。その年は各メディアの「年間スマホ」を総なめにしたが、販売台数は同時期のSamsung S4に大差をつけられた。M7の発表会はスペックを語り、Samsungはライフスタイルを語り、Appleは指紋認証を世界を変えるものとして語った。同じ世代のスマホ、三通りの語り方、三通りの運命。

振り返ればHTCの敗因はスローガン一本ではない。だが物語の失守は、最初に倒れたドミノだ：市場が物語で陣営を選び始めたとき、物語を語れない側は真っ先に「間もなく陳腐化」の籠に入れられる。エンジニアは信じない、製品が語ると。製品は確かに語る、ただ消費者の多くは聞き取れないし、聞こうともしない。

![HTC Dreamのスライドキーボードを開いた姿、2008年世界初のAndroidスマホG1](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream（T-Mobile G1）、2008年。Photo: Marcus Sümnick, CC BY 3.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **キュレーターメモ**
> 「Quietly Brilliant」それ自体が一つの潜台詞翻訳だ：一企業が「静かさ」をグローバルブランド主張に選ぶことは、自ら物語の主権を手放すことに等しい。スペックシートは忘却される、物語は記憶される。HTCはすべての技術選択を正解にし、すべての物語選択を落とした。

## 微笑曲線：台湾人は30年前に自分の立ち位置を描き終えていた

HTCの悲劇は孤例ではない、図で証明されている。

1992年、施振栄（し・しんえい／スタン・シー）が『再造宏碁』で「微笑曲線」を描いた：両端のR&Dとブランドが価値最高、真ん中の製造が価値最低[^4]。台湾人が自分でこの図を描き、その後30年、台湾テックの大部隊は曲線の最底点に張り付いた：Foxconn（鴻海）がAppleのiPhoneを組み立て、粗利率は常年一桁。Appleがスマホ業界利益の大部分をさらう、ピーク時は8割超との試算も[^11]。

[TSMC](/ja/economy/tsmc/)はその例外だ。「自社製品を設計しない」という戒律で、受託製造そのものを両端を握るビジネスに変えた：顧客は離れられず、TSMCは消費者の崇拝を奪う必要もない。だがこのビジネスはB2Bの信頼の上に成り立ち、大衆に物語を語る必要がない。TSMCの低調さはビジネス戦略、副作用は：台湾で最もチップを作れる場所が、恰恰最も物語を練習する必要のない場所だということ。

右端に登った例がないわけではない。ASUS（華碩）が2006年にサブブランドROG（Republic of Gamers、玩家共和國）を立ち上げ、ゲーマーを商標を認識するコミュニティに育て、「敗家之眼」は世界で最も認知度の高いゲーミングハードウェアシンボルの一つになった[^15]。だがROGは少数派：大多数の台湾企業の商標は、製品正面で大きく掲げることすら憚られる。

曲線の右端、台湾も実は登頂したことがある。Acer（宏碁）はかつて世界トップ3のPCブランド、Acerの5文字が世界中の空港搭乗口に貼られていた。だがPCの利益は薄すぎ、ブランドプレミアムでは右端の重量を支えきれなかった。ROGが右端に立てることを証明した、ただ戦場を選ばねばならない。

微笑曲線の最も残酷な点は、30年間誰も再考しなかった選択問題だということだ。30年前台湾は真ん中を選んだ、当時最も合理的な答えだったから：資金もブランドも市場もない、受託製造が唯一の生き残り道だった。真に危険なのは、30年前の合理的な答えを、今日の答えとして使い続けることだ。

## ホラを吹く経済学

数字が最も正直だ。NVIDIA 2026会計年度（2025年2月〜2026年1月）売上2,159億ドル、純利益1,201億ドル[^5]。TSMC 2025年通期売上1,224億ドル、純利益551億ドル[^6]。NVIDIAのチップはほぼすべてTSMCに作らせ、自らはCUDAエコシステム、「AI時代」という物語を売る。結果：物語を設計する会社の売上は、手を動かす会社の1.8倍、純利益は2.2倍。

同じサプライチェーン、消費端まで遡ると勾配はさらに急：

| サプライチェーン位置  | 2025年売上    | 純利益          | 純利益率 |
| --------------------- | ------------- | --------------- | -------- |
| Foxconn（iPhone組立） | 8.1兆台湾ドル | 1,894億台湾ドル | 2.3%     |
| Apple（iPhone販売）   | 4,162億ドル   | 1,120億ドル     | 26.9%    |
| TSMC（チップ製造）    | 1,224億ドル   | 551億ドル       | 45.0%    |
| NVIDIA（物語を語る）  | 2,159億ドル   | 1,201億ドル     | 55.6%    |

_データ：FoxconnとAppleは2025会計年度、NVIDIAはFY2026（2026年1月期）、TSMCは2025年、各社決算短信より（Wikipedia財務欄で相互確認）[^5][^6][^11]。_

組立が2.3%、ブランド販売が26.9%、先進プロセス製造が45%、チップを時代として語るのが55.6%。評価は未来キャッシュフローの割引現在価値。未来の半分はエンジニアリングで作られ、半分は語られる。シリコンバレーの暗黙文化は「fake it till you make it」（まず宣言し、あとで実現する方法を考える）。台湾の暗黙文化は「まだ出来ていないから語らない」。二つの文化の差は道徳の差ではなく、割引率の差だ：市場は「語れる物語」には割引を少なく、「語れない実力」には割引を多くする。

ブランドプレミアムのメカニズムも極めてストレートだ：同じTSMC受託チップにSnapdragonの商標が貼られれば、スマホメーカーが払う追加分がプレミアム。プレミアムはどこから来るか？ 発表会の演出、毎年恒例のSummit、開発者の「次のSnapdragonはきっと速い」という習慣的期待。これらはスペックシートには入らないが、決算書には入る。

「これは市場の間違い、ウォール街の煽りだ」と言う人もいる。だが同じ市場が、TSMCには割引しない：TSMCの純利益率45%、Appleより高い。市場は実は台湾の実力に金を払う用意がある、条件はその実力が語られることだ。TSMCの顧客が代わりに語ってくれる：毎回のApple発表会、毎回のNVIDIA GTC、すべてがTSMCのタダの広告だ。

「物語を大きく語れば詐欺になるのでは？」と問う声もある。黄仁勲の答えは決算書にある：彼のすべての言葉の裏には、生産能力、歩留まり、出荷量が支えている。物語を語ることとホラを吹くことの境界は、語った後に受け皿があるかどうかだ。台湾には受け皿がある、ただ語るのを忘れているだけだ。

> ⚠️ **論点の分かれ目**
> 一派は言う、台湾の60点物語は美徳だ：受託ビジネスの命脈は信頼、低調さは資産。TSMCが毎日発表会を開けば、顧客は眠れなくなる。もう一派は言う、物語の割引は系統的に伝導する：台湾企業の評価が低く見積もられ、給与も低く見積もられ、人材は物語を語る企業へ流れ、次の世代の製品はさらに物語を語れなくなる。どちらを信じるかで、どちらのループに住むかが決まる。この二つの説は今も両方生きており、どちらもまだ勝っていない。

## 台湾は物語を語れないわけではない

うまく語る人、台湾には実はいる。

張忠謀（ちょう・ちゅうぼう／モリス・チャン）が2021年、TSMCを「護国神山（ごこくしんざん）」と呼んだ[^12]。4文字で、全台湾がチップ産業のために喜んで道を譲り、水を譲り、電を譲った。マーケティング史上トップクラスの命名だ：それ以来、毎回の渇水・停電ニュースが自動的に「神山があなたを必要としている」という公益広告に変わる。2024年末、90歳を超えた張忠謀が自伝下巻を出せば、またベストセラー[^13b]。

自伝がベストセラーになること自体が、問題を雄弁に物語っている：90歳超の企業家が自分の人生を二冊に書き、台湾人が列を作って買う。台湾人は物語を聴くのも買うのも好き、ただ自分がステージに立って語る番になると、言葉が短くなる。

この物語を語れる台湾人たち、履歴に共通点がある：張忠謀はTexas Instrumentsで25年、黄仁勲はシリコンバレーで起業30年、蘇姿豊（そ・しほう／リサ・スー）はMITで博士まで。誰一人として、台湾でこの身のこなしを磨いた人はいない。台湾の土壌はこうした人を生めるが、台湾の職場はこのことを教えない。学校は回路を正しく描くことを教え、回路を時代として語ることは教えない。

だから問題は天分にない。問題は台湾の産業構造が、物語を語れる人をすべて海外へ、または受託の会議室へ送り込んでしまったことだ。この結び目を解くには、数社のマーケティング部門の努力では足りず、コーポレートガバナンス、報酬構造から学校教育まで変えねばならない。

![張忠謀が2021年APEC経済首脳会議にリーダー代表として出席するビデオ映像、総統府公式写真](/article-images/technology/morris-chang-apec-2021.webp)
_張忠謀、2021年APEC経済首脳会議に出席。Photo: Wang Yu Ching / 総統府, CC BY 2.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

施振栄が微笑曲線を描いたのも、コンセプトを売ったからだ：一つのコンセプトで、彼の経営哲学が世界中のビジネススクールで引用されるようになった。

黄仁勲は台南生まれ、9歳で渡米[^13]。蘇姿豊は台南生まれ、3歳で渡米[^14]。世界で最も半導体物語を語れる二人、ともに台湾の種、アメリカの土。

![黄仁勲がスタンフォード大学CS 153講義で講演、トレードマークの黒い革ジャンを着て両手で説明](/article-images/technology/jensen-huang-stanford-2026.webp)
_黄仁勲、スタンフォード大学CS 153講義で講演、2026年4月。Photo: Anderseidesvik, CC BY-SA 4.0. [License via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

台湾のスタートアップにも語れる人はいる。Gogoroは2011年創業、2015年CESでバッテリー交換ステーションを「エネルギーネットワーク」として語り、自分たちをエネルギー会社と定義し、ついでにスクーターを売った。物語が魅力的すぎて、2022年にSPACでナスダック上場、2024年にはBP傘下のCastrolが5,000万ドルを投資[^16]。Gogoroは今なおビジネスのクローズドループを探しているが、その例が示すのは：物語を語れれば、少なくとも市場に試される切符は手に入る。語れなければ、ドアすら開かない。

法則は明確だ：台湾に物語の才能は不足していない、不足しているのは物語を大きく語ることを許す環境だ。受託遺伝子が教えるのは「顧客が主人公」、物語を語る環境が教えるのは「私が主人公になれる」。

> 📝 **キュレーターメモ**
> 「護国神山」4文字で最も味わい深いのは：張忠謀がこれを語ったとき、台湾社会に対して「支援を必要とする物語」を語っていたことだ：電が要る、水が要る、土地が要る、人材が要る。物語を語ることは虚栄ではなく、産業政策のインフラだ。台湾人がこの4文字を理解できることは、台湾人の物語力が壊れていないことを示す、ただ対外的に使わないだけだ。

## 潜台詞翻訳対照表

同じ技術的事実、二通りの言い方。台詞の裏の台詞を翻訳してみれば、差は一目瞭然。

| 話し手                              | 表向きの言葉                                                                                                                                                                  | 潜台詞翻訳                                                                                                             |
| ----------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| TSMC決算説明会                      | 「稼働率は回復基調を継続、長期成長に自信を持っています。」                                                                                                                    | 世界最先端のチップを作れるのは我々だけだが、そんなことを言えばエンジニアらしくなくなる。                               |
| 台湾エンジニアのプレゼン            | 「この技術にはまだ最適化の余地があります。」                                                                                                                                  | 世界一を達成済みだが、まず八掛けにしておく、顔に泥を塗られないよう。                                                   |
| 米国スタートアップのピッチ1ページ目 | 「We are building the world's first AI-native platform to reinvent a $5 trillion industry.」（我々は世界初のAIネイティブプラットフォームを構築し、5兆ドル産業を再発明する。） | 現在エンジニア3名とPPT1枚しかないが、夢に値段はない、まず金をくれ。                                                    |
| 台湾スタートアップのピッチ1ページ目 | 「チームメンバーは台清交（台湾大学・清華大学・交通大学）卒、MediaTek勤務8年、特許12件保有。」                                                                                 | ビジョンの語り方が分からない、まず学歴と職歴を防弾チョッキにする。                                                     |
| 黄仁勲                              | 「The more you buy, the more you save.」（買えば買うほど節約になる。）                                                                                                        | このカードは高い、だが買わなければ電気代と算力待ちがもっと食う。                                                       |
| クアルコムSnapdragon Summit         | 「The era of on-device AI begins now.」（オンデバイスAIの時代が今始まる。）                                                                                                   | ベンチマークはiPhoneが出てから言え、まずあなたに「時代を目撃している」と思わせる。                                     |
| HTC 2010年広告                      | 「Quietly Brilliant」                                                                                                                                                         | 我々はbrilliantだが、大声で言うのは恥ずかしい。                                                                        |
| Samsung 2011年広告                  | 「The Next Big Thing is already here.」（次の大きなものは、もうここにある。）                                                                                                 | Apple Storeで並ぶ連中は滑稽に見える、こっちを買え。                                                                    |
| Elon Musk                           | 「We will make life multiplanetary.」（我々は生命を多惑星種にする。）                                                                                                         | ロケットは今でも時々爆発するが、物語は先に飛び立たせろ。                                                               |
| 張忠謀 2021年                       | 「半導体は台湾の護国神山。」                                                                                                                                                  | 4文字で、全台湾をチップのために道譲り、水譲り、電譲りさせた。物語を語れる台湾人の一言、丸1年の決算説明スライドに勝る。 |

_表中のTSMC、台湾エンジニア、二つのスタートアップ欄、クアルコム欄の引用文は典型的な言い方の示意的まとめであり、逐語引用ではない。黄仁勲、HTC、Samsung、Musk、張忠謀の5欄は実際の公開スローガンまたは発言[^17][^18][^12]。_

翻訳し終えれば気づくだろう、物語が上手いか下手かの差は、往々にして同じ事実の二通りの語順に過ぎない。

この表は誰かを嘲笑うためではない。謙虚さはエンジニアリングでは大いに役立つ：協力を持続させ、品管に手抜きをさせない。だが謙虚さが会議室を一歩出れば、値引き券に変わる。台湾が学ぶべきは、謙虚さを実験室に置き、自信をステージに連れて行くことだ。

## 台大体育館に戻る

黄仁勲があの夜語ったすべてのスライド、その物理的現場は新竹、台中、台南のクリーンルームにある。物語が終われば、世界中が買う。クリーンルームの人々はシフトを回し続け、決算説明会は相変わらず保守的だ。

100点のテクノロジーは、自動的に100点の物語にはならない。その40点には、誰かがステージに立ち、革ジャンを戦袍にし、チップを時代として語ることが必要だ。

台湾の次の護国神山は、どの新チップかもしれないし、どの新しい物語かもしれない。

> ✦ クアルコムは一個のSoCをレッドカーペットを歩くブランドに育て、黄仁勲はTSMC製のチップを時代として語り、張忠謀は4文字で全台湾に半導体のために道を譲らせた。台湾テックには100点のモノがある、足りないのはステージに立ち、それを100点として語る覚悟のある人だ。

---

**関連記事**：

- [半導体産業：RCA技術移転から窒化ガリウム・量子パッケージングまでの50年材料革命](/ja/technology/taiwan-semiconductor-industry) — 護国神山の完全な技術物語、および「NVIDIAがCoWoS生産能力を独占」というあの束縛
- [台湾企業：TSMC](/ja/economy/tsmc) — 低調さをビジネスモデルに書き込んだこの会社のガバナンスと財務構造
- [台湾企業：MediaTek](/ja/economy/mediatek) — 世界最大出荷量のスマホチップメーカー、なぜ物語はまだ追いかけているのか
- [台湾企業：HTC](/ja/economy/htc-android-pioneer-vr-transformation) — Quietly Brilliantの死の完全企業史
- [黄仁勲](/ja/people/jensen-huang) — 台南生まれ、アメリカ育ち、世界で最もチップ物語を語れる人
- [NVIDIA在台湾](/ja/technology/nvidia-in-taiwan) — あの革ジャンと台湾サプライチェーンの関係
- [Computex：三大国際コンピュータ展が二つ消え、残った一つが台北に根付く](/ja/technology/computex) — 毎年5月、世界のAI巨頭が順番に台北で同じ話術で物語を語る

## 画像出典

本文で5枚のCCライセンス画像を使用、`public/article-images/technology/`にキャッシュ：

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Photo: 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Photo: Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Photo: Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Photo: Wang Yu Ching / 総統府, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Photo: Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## 参考資料

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — 2011年4月7日HTC時価総額約338億ドル、Nokiaを超える

[^2]: [Wikipedia — HTC Corporation](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — 2011年スマホシェア約20%、時価総額1兆ドル突破、株価かつて千元台

[^3]: [Wikipedia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — 2008年世界初のAndroidスマホ

[^4]: [Wikipedia — 微笑曲線](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — 施振栄が1992年『再造宏碁』で提唱

[^4b]: [Wikipedia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — 出荷量ベース世界最大級スマホSoCサプライヤーの一社；テレビチップシェア約7割

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — NVIDIA公式ニュースリリース；FY2026売上2,159億ドル、純利益1,201億ドル（Wikipedia財務欄で相互確認：https://en.wikipedia.org/wiki/Nvidia）

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — TSMC公式投資家向けページ；2025年通期売上1,224.2億ドル、純利益551.3億ドル（Wikipedia財務欄で相互確認：https://en.wikipedia.org/wiki/TSMC）

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — 2020年第3四半期MediaTekスマホチップ出荷量初めてクアルコム超え、シェア約31%

[^8]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon SoCプラットフォーム2006年11月発表；ブランド名はキンギョソウの花名に由来、天璣は北斗七星第三星に由来（両命名由来はブランド公開資料、公式ソースリンク追加待ち）

[^9]: [MediaTek — Dimensity 9400 Press Release](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — 天璣 9400、2024年10月発表；レビュー界では概して電力効率性能で評価（帰納的記述）。初搭載機種は[Wikipedia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200)参照

[^10]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024、ハワイ・マウイ島で開催、Snapdragon 8 Elite発表（公式ニュースリリースURL失効、Wikipedia二次情報を暫定採用）

[^11]: [Wikipedia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) — ／ [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Foxconn 2025会計年度売上8.103兆台湾ドル、純利益1,893.5億台湾ドル（純利益率約2.3%）；Apple FY2025売上4,162億ドル、純利益1,120億ドル（純利益率約26.9%）。Appleスマホ利益シェアピーク時8割超：Counterpoint歴年推計（ソースリンク追加待ち）

[^12]: [Wikipedia — 護国神山](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — TSMCの別称（シリコンシールド）；「半導体は台湾の護国神山」は張忠謀2021年公開発言（ニュース出所リンク追加待ち）

[^13]: [Wikipedia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — 1963年台南生まれ、1972年（9歳）渡米

[^13b]: 張忠謀自伝下巻2024年11月出版、当年ベストセラー級販売（ソースリンク追加待ち）

[^14]: [Wikipedia — Lisa Su](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — 1969年台南生まれ、3歳で家族と渡米

[^15]: [Wikipedia — ASUS](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — 2006年サブブランド「Republic of Gamers」（ROG）創立

[^16]: [Wikipedia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — 2011年創業；2015年CESでGogoro Smartscooterとエネルギーネットワーク発表；2022年Poema Global SPACと合併しナスダック上場；2024年BP傘下Castrolが最高5,000万ドル投資を発表

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — 黄仁勲「The more you buy, the more you save」はこの公式動画から

[^18]: 「Quietly Brilliant」はHTC 2009年からのグローバルブランドスローガン、「The Next Big Thing is Already Here」はSamsung 2011年Galaxy広告スローガン、「We will make life multiplanetary」はSpaceXミッションステートメント（三者とも公開商業テキスト）

[^19]: [NVIDIA at Computex 2024 — 公式基調講演動画](https://www.youtube.com/watch?v=pKXDVsWZmUU) — 黄仁勲2024年6月2日台大体育館でのComputex基調講演

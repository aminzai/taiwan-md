---
title: 'Taïwan, conteuse de technologie : une puce à 100 points, un micro à 60 points'
description: "Taïwan sait fabriquer des puces parfaites, mais a l'habitude de les présenter avec le ton d'une présentation fournisseur. Pour la même puce, Qualcomm en fait un mythe, MediaTek un tableau de spécifications ; NVIDIA ne fabrique rien de ses propres mains, mais son bénéfice net est le double de celui des sous-traitants. Cet écart de 40 points est déjà comptabilisé par le marché, et la facture est imprimée sur la marge nette."
date: 2026-08-15
category: 'Technology'
tags:
  [
    'technologie',
    'narration de marque',
    'marque',
    'semi-conducteurs',
    'TSMC',
    'NVIDIA',
    'MediaTek',
    'Qualcomm',
    'HTC',
    'Jensen Huang',
    'Morris Chang',
    'courbe en souriante',
    'sous-texte',
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
translatedAt: '2026-09-12T05:28:17+08:00'
---

# Taïwan, conteuse de technologie : une puce à 100 points, un micro à 60 points

![Vue extérieure de l'usine Fab 14B de TSMC dans le parc scientifique de Tainan, un bâtiment industriel à plusieurs étages s'étendant sous un ciel bleu, site physique de la capacité de production aux procédés avancés](/article-images/technology/tsmc-fab-14b-2025.webp)
_L'usine TSMC Fab 14B à Tainan, mai 2025. Photo : 4300streetcar. [Licence via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg)._

> **Aperçu en 30 secondes :** En juin 2024, Jensen Huang a transformé la puce fabriquée par TSMC en un nouveau ère lors d'une conférence à l'Université nationale de Taïwan ; au même trimestre, les diapositives de la conférence aux investisseurs de TSMC se limitaient encore aux chiffres financiers, au taux d'utilisation de la capacité et aux perspectives prudentes. Le chiffre d'affaires de NVIDIA pour l'exercice 2026 s'élève à 215,9 milliards de dollars US, avec un bénéfice net de 120,1 milliards de dollars US ; TSMC, qui fabrique ses puces, affiche un chiffre d'affaires de 122,4 milliards de dollars et un bénéfice net de 55,1 milliards de dollars en 2025[^5][^6]. Les entreprises qui racontent des histoires conçoivent deux fois plus que celles qui font le travail manuel. Cet article vise à révéler le sous-texte derrière les déclarations.

Le 2 juin 2024, à l'Université nationale de Taïwan. Jensen Huang, vêtu de son blouson en cuir noir habituel, prend la scène et parle pendant deux heures. La foule en bas ressemble à un concert : diffusion en direct, médias étrangers, une mer de gens tenant des téléphones. Il parle de Blackwell, de CUDA, transformant chaque diapositive en cérémonie d'ouverture d'une nouvelle ère[^19].

Sur la même île, en conduisant vers le sud pendant moins d'une centaine de kilomètres, on arrive à Hsinchu. La conférence aux investisseurs de TSMC présente un style différent : chiffres financiers, taux d'utilisation de la capacité, variations trimestrielles et annuelles, et une fourchette de perspectives prudente. Les puces les plus avancées au monde sont produites sur cette ligne, mais toute la présentation ressemble à un cours de comptabilité.

Une seule puce, deux façons de la présenter. Les 40 points d'écart au milieu ont déjà été calculés par le marché.

Les Taïwanais voient cette différence depuis leur enfance. Nous avons l'habitude que : nous fabriquons les produits, les autres reçoivent les applaudissements. Sur les salons professionnels, les stands des entreprises taïwanaises parlent de coûts, de rendement et de délais de livraison, tandis que la scène des marques américaines parle de futur, de mission et de changement du monde. L'écart entre les deux, c'est ces 40 points. Voici à quoi ils ressemblent, et nous allons les révéler.

## Une seule puce, deux façons de la présenter

En octobre 2024, deux présentations se sont succédé en moins de deux semaines. MediaTek a présenté le Dimensity 9400 à Shenzhen, tandis que Qualcomm a tenu son Snapdragon Summit à Maui, à Hawaï[^9][^10].

[MediaTek](/fr/economy/mediatek/) est l'un des plus grands fournisseurs de puces pour smartphones au monde en termes de volume d'expéditions, avec 70 % de parts de marché dans les puces pour téléviseurs[^4b]. Qualcomm expédie moins, mais gagne en chiffre d'affaires et en prime de marque. Où est la différence ? Qualcomm vend le nom « Snapdragon » : nommé en 2006, il a été cultivé pendant près de vingt ans[^8], possède sa propre mascotte et son propre festival technologique annuel. La phrase « Powered by Snapdragon » prononcée lors des présentations de smartphones haut de gamme mondiaux est plus visible que les logos propres des fabricants de téléphones.

MediaTek vend des tableaux de spécifications. Le contenu de la présentation du Dimensity 9400 concerne les procédés, l'IPC (Instructions Per Cycle), les courbes d'efficacité énergétique ; les chiffres tiennent la route, et le cercle des critiques lui a décerné le titre de « Roi de l'efficacité énergétique »[^9]. Mais les consommateurs ne connaissent que Snapdragon.

MediaTek a déjà occupé le trône du volume d'expéditions. Au troisième trimestre 2020, les expéditions de puces pour smartphones de MediaTek ont dépassé celles de Qualcomm pour la première fois, atteignant environ 31 % de part de marché[^7]. Mais pendant les années où MediaTek était premier en volume, ses revenus provenaient principalement des smartphones d'entrée et de milieu de gamme ; le sommet des smartphones haut de gamme appartenait toujours à Qualcomm. Ce n'est qu'à la fin de 2021, avec la sortie du Dimensity 9000, que MediaTek a vu ses puces haut de gamme figurer dans les tableaux comparatifs des smartphones Android phares. Les spécifications ont rattrapé le retard, mais la présentation restait celle d'un fournisseur parlant à un client.

MediaTek est conscient de ce problème. Ces dernières années, il a commencé à apprendre : les puces haut de gamme ont maintenant leur propre nom, les présentations ont un spectacle d'ouverture, et les fabricants de téléphones partenaires sont prêts à inclure « Dimensity » dans leurs slogans publicitaires. La direction est bonne, mais le départ a été retardé de plus de dix ans. La construction d'une marque est un marathon ; ceux qui courent en avance accumulent des intérêts composés à chaque tour.

> 💡 **Saviez-vous que**
> Snapdragon est le nom anglais de l'antirrhinum (snapdragon flower), un type de fleur ; Dimensity fait référence à la troisième étoile de la Grande Ourse[^8]. L'une choisit de nommer d'après un jardin, l'autre d'après une carte stellaire, c'est très bien. La différence est que Qualcomm a fait de cette fleur une marque qui marche sur le tapis rouge, tandis que la lumière de Dimensity reste la plupart du temps figée sur le tableau de spécifications.

> 📝 **Note du curateur**
> La guerre des marques dans l'industrie des semi-conducteurs est d'une brutalité concrète : lorsque les consommateurs paient, ils reconnaissent Snapdragon ou Dimensity ; personne ne demande quelle puce a été fabriquée par TSMC. Qualcomm a commencé à cultiver sa marque en 2006, MediaTek n'a apposé la série « Dimensity » sur ses produits phares qu'à la fin de 2019. Vingt ans d'intérêts composés narratifs, aucun tableau de spécifications ne peut rattraper ce retard.

## Comment est mort le « Quietly Brilliant »

Remontons plus loin pour un cas encore plus douloureux. Le 7 avril 2011, la capitalisation boursière de HTC a dépassé celle de Nokia, atteignant environ 33,8 milliards de dollars US[^1]. À l'époque, HTC occupait environ 20 % du marché des smartphones, formant le trio de tête avec Samsung et Apple[^2].

En termes de choix technologiques, HTC avait presque tout juste : elle a sorti le premier smartphone Android, le G1, en 2008[^3]. Le One de 2013 utilisait un châssis monobloc en alliage d'aluminium, et la voie des grands capteurs de pixels, des doubles objectifs, étaient des pistes qu'elle avait ouvertes. Mais vous souvenez-vous de son slogan de marque mondial ?

![Gros plan sur le côté du corps du HTC One M7, design monobloc en alliage d'aluminium, une référence工艺 en 2013 lors de sa présentation](/article-images/technology/htc-one-m7-2013.webp)
_HTC One (M7), 2013. Photo : Asmoth, CC BY-SA 4.0. [Licence via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG)._

« Quietly Brilliant. » Brillant, mais discrètement.

À la même période, la publicité de Samsung « The Next Big Thing is already here » filmait directement les fans d'Apple faisant la queue devant les magasins, montrant les files d'attente comme stupides[^18]. HTC faisait de la modestie sa proposition de marque, Samsung faisait d'Apple le méchant principal. Plus de deux ans plus tard, les actions de HTC sont tombées de plus d'un millier de dollars taïwanais à quelques dizaines de dollars[^2].

HTC a eu une chance de rebondir. Le One (M7) de 2013 avait de nombreux avantages en tête de la profession : châssis monobloc en alliage d'aluminium, caméra UltraPixel à grands pixels, haut-parleurs doubles avant BoomSound. Cette année-là, il a remporté tous les prix de « Smartphone de l'année » des grands médias, mais ses ventes ont été largement dépassées par le Samsung S4 de la même période. La présentation du M7 parlait de spécifications, Samsung parlait de style de vie, Apple transformait le déverrouillage par empreinte digitale en un changement du monde. Pour un smartphone d'une même génération, trois façons de présenter, trois destins.

Revoir les causes de la défaite de HTC, ce n'est pas seulement une question de slogan. Mais la perte de contrôle narratif est la première carte dominos tombée : lorsque le marché commence à choisir son camp par l'histoire, celui qui ne peut pas raconter d'histoire est d'abord mis dans le panier « bientôt obsolète ». Les ingénieurs n'y croient pas, pensant que le produit parle de lui-même. Le produit parle effectivement, mais la plupart des consommateurs ne comprennent pas et n'ont pas envie d'écouter.

![Aspect du HTC Dream lorsque son clavier coulissant est ouvert, le premier smartphone Android au monde, G1](/article-images/technology/htc-dream-g1-2008.webp)
_HTC Dream (T-Mobile G1), 2008. Photo : Marcus Sümnick, CC BY 3.0. [Licence via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg)._

> 📝 **Note du curateur**
> « Quietly Brilliant » est en soi une traduction de sous-texte : une entreprise choisissant la « discrétion » comme proposition de marque mondiale revient à céder activement la souveraineté narrative. Les tableaux de spécifications seront oubliés, les histoires seront mémorisées. HTC a fait tous les bons choix techniques, mais a perdu tous les choix narratifs.

## La courbe en souriante : les Taïwanais ont tracé leur propre carte de situation il y a 30 ans

Le drame de HTC n'est pas un cas isolé, il a des preuves graphiques.

En 1992, Shih Ming-deh a tracé la « Courbe en souriante » dans _Rebuilding Acer_ : la R&D et la marque sont aux deux extrémités, où la valeur est la plus élevée ; la fabrication est au milieu, où la valeur est la plus faible[^4]. Les Taïwanais ont tracé cette carte eux-mêmes, puis, pendant les trente années suivantes, le gros des forces technologiques taïwanaises est resté coincé au point le plus bas de la courbe : Foxconn assemble les iPhones pour Apple, avec une marge brute qui n'a été que sur un chiffre pendant des années. Apple s'approprie la majeure partie des profits de toute l'industrie du smartphone ; les sommets des études de marché estiment qu'ils dépassent 80 %[^11].

[TSMC](/fr/economy/tsmc/) est l'exception. En suivant la règle de « ne pas concevoir ses propres produits », il a transformé la sous-traitance en une affaire qui tient les deux extrémités : les clients ne peuvent pas se passer de lui, et il n'a pas besoin de rivaliser avec les clients pour la崇拜 des consommateurs. Mais cette affaire est fondée sur la confiance B2B, sans besoin de raconter des histoires au grand public. La discrétion de TSMC est une stratégie commerciale ; la contrepartie est que l'endroit où Taïwan fabrique le mieux les puces est précisément celui qui a le moins besoin de s'entraîner à raconter des histoires.

Il y a eu des tentatives pour atteindre l'extrémité droite. ASUS a créé la marque secondaire ROG (Republic of Gamers) en 2006, transformant les joueurs d'e-sport en une communauté reconnaissant le logo ; l'« Œil du vainqueur » est l'un des logos les plus reconnaissables dans le matériel d'e-sport mondial[^15]. Mais ROG est une minorité : la plupart des logos des entreprises taïwanaises n'osent même pas être agrandis sur la face avant du produit.

Sur l'extrémité droite de la courbe, Taïwan y est déjà monté. Acer a été l'un des trois plus grands marques de PC au monde, les cinq lettres « Acer » étant collées sur les portes d'embarquement des aéroports du monde entier. Mais les marges des PC sont trop fines, au point que le prime de marque ne peut pas supporter le poids de l'extrémité droite. ROG prouve que l'on peut tenir debout à l'extrémité droite, il suffit de choisir le bon champ de bataille.

La chose la plus cruelle de la courbe en souriante est qu'il s'agit d'un choix non révisé depuis trente ans. Il y a trente ans, Taïwan a choisi de se placer au milieu, car c'était la réponse la plus raisonnable à l'époque : pas de fonds, pas de marque, pas de marché, la sous-traitance était la seule voie de survie. Le véritable danger est de continuer à considérer la réponse raisonnable d'il y a trente ans comme la réponse d'aujourd'hui.

## L'économie de la vantardise

Les chiffres sont les plus honnêtes. Pour l'exercice 2026 de NVIDIA (février 2025 à janvier 2026), le chiffre d'affaires est de 215,9 milliards de dollars US, avec un bénéfice net de 120,1 milliards de dollars US[^5]. Pour l'année 2025, le chiffre d'affaires de TSMC est de 122,4 milliards de dollars US, avec un bénéfice net de 55,1 milliards de dollars US[^6]. Presque toutes les puces de NVIDIA sont confiées à TSMC pour la fabrication ; NVIDIA vend lui-même l'écosystème CUDA et l'histoire de « l'ère de l'IA ». Résultat : l'entreprise qui raconte l'histoire a un chiffre d'affaires 1,8 fois supérieur à celui de l'entreprise qui fait le travail manuel, et un bénéfice net 2,2 fois supérieur.

Sur la même chaîne d'approvisionnement, en montant vers l'extrémité de consommation, la pente est plus raide :

| Position dans la chaîne d'approvisionnement | Chiffre d'affaires 2025           | Bénéfice net                         | Marge nette |
| ------------------------------------------- | --------------------------------- | ------------------------------------ | ----------- |
| Foxconn (assemblage iPhone)                 | 8,1 billions de dollars taïwanais | 189,4 milliards de dollars taïwanais | 2,3 %       |
| Apple (vente d'iPhone)                      | 416,2 milliards de dollars US     | 112,0 milliards de dollars US        | 26,9 %      |
| TSMC (fabrication de puces)                 | 122,4 milliards de dollars US     | 55,1 milliards de dollars US         | 45,0 %      |
| NVIDIA (raconte l'histoire)                 | 215,9 milliards de dollars US     | 120,1 milliards de dollars US        | 55,6 %      |

_Données : Foxconn et Apple pour l'exercice 2025, NVIDIA pour FY2026 (jusqu'en janvier 2026), TSMC pour 2025, tirées des rapports financiers de chaque entreprise (croisé avec les colonnes de rapports de Wikipedia)[^5][^6][^11]._

L'assemblage gagne 2,3 %, la vente de marque gagne 26,9 %, la fabrication de procédés avancés gagne 45 %, la transformation de la puce en ère gagne 55,6 %. La valorisation est l'actualisation des flux de trésorerie futurs. La moitié du futur est construite par l'ingénierie, l'autre moitié est racontée. La culture par défaut de la Silicon Valley est _fake it till you make it_ (prétendre jusqu'à ce que cela devienne réel). La culture par défaut de Taïwan est « pas encore fait, n'ose pas le dire ». L'écart entre les deux cultures n'est pas un écart moral, c'est un écart de taux d'actualisation : le marché applique moins de décote aux « histoires qui peuvent être racontées », et plus de décote aux « compétences qui ne peuvent pas être racontées ».

Le mécanisme du prime de marque est aussi simple : pour la même puce fabriquée par TSMC, coller le logo Snapdragon fait que les fabricants de téléphones sont prêts à payer plus ; c'est le prime. D'où vient le prime ? De l'ampleur des présentations, du sommet annuel fixe, de l'attente habituelle des développeurs selon laquelle « la prochaine Snapdragon sera toujours plus rapide ». Ces éléments n'entrent pas dans le tableau de spécifications, mais ils entrent dans les états financiers.

Certains diront que c'est la faute du marché, que Wall Street fait de la spéculation. Mais sur le même marché, la décote ne s'applique pas à TSMC : la marge nette de TSMC est de 45 %, bien supérieure à celle d'Apple. Le marché est en fait prêt à payer pour la capacité de Taïwan, à condition que cette capacité puisse être racontée. Les clients de TSMC la racontent pour lui : chaque présentation d'Apple, chaque GTC de NVIDIA, est une publicité gratuite pour TSMC.

On demande si raconter de grandes histoires ne devient pas du mensonge. La réponse de Jensen Huang est écrite dans les rapports financiers : chaque mot qu'il prononce est soutenu par des capacités de production, des rendements et des volumes d'expéditions. La frontière entre raconter des histoires et se vanter réside dans ce qui vient après : y a-t-il quelque chose pour soutenir ? Taïwan a la matière, il oublie simplement souvent de le dire.

> ⚠️ **Point de vue controversé**
> Une école pense que la narration à 60 points de Taïwan est une vertu : le fil conducteur des affaires de sous-traitance est la confiance, la discrétion est un atout ; si TSMC tenait des présentations tous les jours, les clients ne dormiraient pas. L'autre école pense que la décote narrative se transmet systématiquement : la valorisation des entreprises taïwanaises est sous-évaluée, les salaires suivent, les talents affluent vers les entreprises qui racontent des histoires, et les produits de la prochaine génération ne peuvent donc plus raconter d'histoire. De quelle école croyez-vous ? Vous vivrez dans quel cercle. Ces deux affirmations existent encore, et aucune n'a encore gagné.

## Taïwan n'est pas incapable de raconter des histoires

Ceux qui racontent bien, Taïwan en a.

En 2021, Morris Chang a appelé TSMC « la divine montagne protectrice de la nation »[^12]. Quatre mots, qui ont fait en sorte que toute Taïwan cède volontairement la route, l'eau et l'électricité à l'industrie des semi-conducteurs. C'est un nommage de premier rang dans l'histoire du marketing : depuis lors, chaque nouvelle sur la pénurie d'eau ou d'électricité devient automatiquement une publicité pour « la montagne divine a besoin de toi ». À la fin de 2024, Morris Chang, âgé de plus de 90 ans, a publié la deuxième partie de son autobiographie, qui est devenue un best-seller[^13b].

Le fait que l'autobiographie soit devenue un best-seller dit tout : un entrepreneur de plus de 90 ans écrit sa vie en deux volumes, les Taïwanais font la queue pour l'acheter. Les Taïwanais aiment écouter des histoires, et aiment acheter des histoires, mais lorsque vient leur tour de monter sur scène pour parler, ils se taisent.

Ce groupe de Taïwanais qui savent raconter des histoires a un point commun dans leur curriculum vitae : Morris Chang a travaillé chez Texas Instruments pendant vingt-cinq ans, Jensen Huang a fondé sa startup en Silicon Valley pendant trente ans, Lisa Su a obtenu son doctorat au MIT. Aucun d'entre eux n'a acquis ces compétences à Taïwan. Le sol de Taïwan peut faire pousser ce type de personnes, mais le lieu de travail de Taïwan ne l'enseigne pas. L'école apprend à dessiner correctement les circuits, pas à transformer les circuits en ère.

Le problème n'a donc jamais été le talent. Le problème est que la structure industrielle de Taïwan a envoyé ceux qui savent raconter des histoires à l'étranger, ou dans les salles de réunion de la sous-traitance. Pour dénouer ce nœud, il ne suffit pas des départements marketing de quelques entreprises ; il faut réformer de la gouvernance d'entreprise, de la structure salariale jusqu'à l'éducation scolaire.

![Image vidéo de Morris Chang en tant que représentant des chefs d'État à la réunion des chefs d'État économiques APEC 2021, photo officielle du Bureau présidentiel](/article-images/technology/morris-chang-apec-2021.webp)
_Morris Chang à la réunion des chefs d'État économiques APEC 2021. Photo : Wang Yu Ching / Bureau présidentiel, CC BY 2.0. [Licence via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg)._

Shih Ming-deh a tracé la courbe en souriante en vendant aussi un concept : un concept a fait en sorte que sa philosophie de gestion d'entreprise soit citée dans toutes les écoles de commerce du monde.

Jensen Huang est né à Tainan, parti aux États-Unis à l'âge de neuf ans[^13]. Lisa Su est née à Tainan, partie aux États-Unis avec sa famille à l'âge de trois ans[^14]. Les deux personnes qui racontent le mieux les histoires des semi-conducteurs au monde sont des graines de Taïwan, cultivées dans le sol américain.

![Jensen Huang lors d'un discours dans le cours CS 153 de l'Université Stanford, portant son blouson en cuir noir signature, faisant des gestes avec ses mains](/article-images/technology/jensen-huang-stanford-2026.webp)
_Jensen Huang lors d'un discours dans le cours CS 153 de l'Université Stanford, avril 2026. Photo : Anderseidesvik, CC BY-SA 4.0. [Licence via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg)._

Il y a aussi des conteurs parmi les startups de Taïwan. Gogoro a été fondée en 2011, et en 2015, au CES, elle a présenté la station d'échange de batteries comme un « réseau énergétique », disant qu'elle était une entreprise d'énergie, vendant accessoirement des scooters. L'histoire était si captivante qu'elle lui a permis de se coter au NASDAQ via un SPAC en 2022 ; en 2024, même Castrol, une filiale de BP, a investi 50 millions de dollars US[^16]. Gogoro cherche encore sa boucle commerciale, mais son exemple montre : savoir raconter des histoires permet au moins d'obtenir le billet pour être testé par le marché. Ceux qui ne savent pas raconter n'entrent même pas dans la porte.

La règle est claire : Taïwan ne manque pas de talent pour raconter des histoires, il manque d'un environnement qui permet de raconter de grandes histoires. Le gène de la sous-traitance enseigne « le client est le protagoniste », l'environnement de narration enseigne « je peux être le protagoniste ».

> 📝 **Note du curateur**
> Ce qui est le plus intéressant dans les quatre mots « divine montagne protectrice de la nation » : lorsque Morris Chang les a prononcés, il racontait à la société taïwanaise une histoire qui a besoin d'être soutenue : avoir de l'électricité, de l'eau, de l'espace, des talents. Savoir raconter des histoires n'est pas de la vanité, c'est une infrastructure de politique industrielle. Le fait que les Taïwanais comprennent ces quatre mots signifie que leur pouvoir narratif n'est pas mauvais, il est simplement rarement utilisé à l'extérieur.

## Tableau de traduction du sous-texte

Un seul fait technique, deux façons de le dire. Révéler le sous-texte derrière les déclarations, l'écart est visible par soi-même.

| Personne qui parle                              | Paroles de surface                                                                                                               | Traduction du sous-texte                                                                                                                                                                                                                                  |
| ----------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Conférence aux investisseurs de TSMC            | « Le taux d'utilisation de la capacité continue de remonter, nous restons confiants dans la croissance à long terme. »           | Seuls les puces les plus avancées au monde peuvent être fabriquées par moi, mais dire cela ne ressemble plus à un ingénieur.                                                                                                                              |
| Présentation de l'ingénieur taïwanais           | « Cette technologie a encore des marges d'optimisation. »                                                                        | Nous avons atteint le premier rang mondial, prenons d'abord une décote de 20 % pour éviter de nous faire démentir.                                                                                                                                        |
| Première page de pitch d'une startup américaine | « We are building the world's first AI-native platform to reinvent a $5 trillion industry. »                                     | L'entreprise n'a actuellement que trois ingénieurs et un PPT, mais le rêve est sans prix, donnez-nous de l'argent d'abord.                                                                                                                                |
| Première page de pitch d'une startup taïwanaise | « Les membres de l'équipe sont diplômés de NTU/NTU/NCU, ont travaillé chez MediaTek pendant huit ans, et possèdent 12 brevets. » | Nous ne savons pas comment raconter la vision, prenons les diplômes et l'expérience comme gilet pare-balles.                                                                                                                                              |
| Jensen Huang                                    | « The more you buy, the more you save. »                                                                                         | Cette carte est chère, mais si vous n'achetez pas, les factures d'électricité et la file d'attente du calcul en mangeront plus.                                                                                                                           |
| Qualcomm Snapdragon Summit                      | « The era of on-device AI begins now. »                                                                                          | Attendons la sortie de l'iPhone pour les scores de performance, faisons d'abord sentir que vous êtes témoin d'une ère.                                                                                                                                    |
| Publicité HTC 2010                              | « Quietly Brilliant »                                                                                                            | Nous sommes brillants, mais nous avons honte de le dire fort.                                                                                                                                                                                             |
| Publicité Samsung 2011                          | « The Next Big Thing is already here. »                                                                                          | Les gens qui font la queue devant le magasin Apple ont l'air si stupides, venez m'acheter.                                                                                                                                                                |
| Elon Musk                                       | « We will make life multiplanetary. »                                                                                            | Les fusées explosent parfois maintenant, mais la narration doit décoller d'abord.                                                                                                                                                                         |
| Morris Chang 2021                               | « Les semi-conducteurs sont la divine montagne protectrice de la nation de Taïwan. »                                             | Quatre mots, qui ont fait en sorte que toute Taïwan cède la route, l'eau et l'électricité aux semi-conducteurs. Une phrase d'un Taïwanais qui sait raconter des histoires vaut plus qu'une année entière de diapositives de conférence aux investisseurs. |

_Les citations entre guillemets pour TSMC, l'ingénieur taïwanais, les deux colonnes de startups et Qualcomm sont des synthèses indicatives de déclarations typiques, pas des citations mot à mot ; les cinq colonnes de Jensen Huang, HTC, Samsung, Musk et Morris Chang sont des slogans ou déclarations publics réels[^17][^18][^12]._

Après la traduction, vous constaterez que la différence entre bien et mal raconter des histoires n'est souvent que deux ordres de mots pour un seul fait.

Ce tableau n'est pas destiné à se moquer de qui que ce soit. La modestie est très utile en ingénierie : elle permet à la coopération de fonctionner, empêche le contrôle qualité de relâcher la pression. Mais une fois la modestie sortie de la salle de réunion, elle devient un bon de réduction. Ce que Taïwan doit apprendre, c'est de laisser la modestie dans le laboratoire et d'apporter la confiance sur la scène.

## Retour à l'Université nationale de Taïwan

Chaque diapositive que Jensen Huang a présentée ce soir-là avait un site physique dans les salles blanches de Hsinchu, Taichung et Tainan. L'histoire est racontée, le monde paie. Les gens des salles blanches continuent les quarts de travail, les conférences aux investisseurs restent prudentes.

Une technologie à 100 points ne devient pas automatiquement une narration à 100 points. Ces 40 points nécessitent que quelqu'un monte sur la scène, porte le blouson en cuir comme une armure de guerre, et transforme la puce en ère.

La prochaine divine montagne protectrice de la nation de Taïwan pourrait ne pas être une nouvelle puce, mais une nouvelle histoire.

> ✦ Qualcomm a transformé un SoC en une marque qui marche sur le tapis rouge, Jensen Huang a transformé la puce fabriquée par TSMC en une ère, Morris Chang a utilisé quatre mots pour faire en sorte que toute Taïwan cède la route aux semi-conducteurs. La technologie taïwanaise a des choses à 100 points, il manque des personnes prêtes à monter sur la scène pour les raconter à 100 points.

---

**Pour aller plus loin** :

- [Industrie des semi-conducteurs : 50 ans de révolution des matériaux, du transfert de technologie RCA au nitrure de gallium et à l'emballage quantique](/technology/半導體產業) — La narration technique complète de la divine montagne protectrice de la nation, et le lien avec « NVIDIA réserve la capacité CoWoS »
- [Entreprise taïwanaise : TSMC](/economy/台灣企業：台積電) — La gouvernance et la structure financière de cette entreprise qui a écrit la discrétion dans son modèle commercial
- [Entreprise taïwanaise : MediaTek](/economy/台灣企業：聯發科技) — Le plus grand fabricant de puces pour smartphones au monde en volume d'expéditions, pourquoi la narration rattrape encore le retard
- [Entreprise taïwanaise : HTC](/economy/台灣企業：宏達電) — L'histoire d'entreprise complète de la mort de « Quietly Brilliant »
- [Jensen Huang](/people/黃仁勳) — Né à Tainan, grandi aux États-Unis, la personne qui sait le mieux raconter des histoires de puces au monde
- [NVIDIA à Taïwan](/technology/NVIDIA在台灣) — La relation entre ce blouson en cuir et la chaîne d'approvisionnement taïwanaise
- [Computex : trois grands salons informatiques internationaux en ont fermé deux, celui qui reste est né à Taipei](/technology/Computex) — Chaque mai, les géants mondiaux de l'IA racontent tour à tour des histoires à Taipei avec le même discours

## Sources des images

Cet article utilise 5 images sous licence CC, mises en cache dans `public/article-images/technology/` :

- [TSMC Fab 14B May 2025](https://commons.wikimedia.org/wiki/File:TSMC_Fab_14B_May_2025_1.jpg) — Photo : 4300streetcar, CC BY 4.0, Wikimedia Commons
- [HTC One 03](https://commons.wikimedia.org/wiki/File:HTC_One_03.JPG) — Photo : Asmoth, CC BY-SA 4.0, Wikimedia Commons
- [HTC Dream opened](https://commons.wikimedia.org/wiki/File:HTC_Dream_opened.jpg) — Photo : Marcus Sümnick, CC BY 3.0, Wikimedia Commons
- [Morris Chang at APEC 2021](https://commons.wikimedia.org/wiki/File:2021-11-12_Morris_Chang_represented_Taiwan_on_APEC_Economic_Leaders%27_Meeting.jpg) — Photo : Wang Yu Ching / Bureau présidentiel, CC BY 2.0, Wikimedia Commons
- [Jensen Huang at Stanford CS 153](https://commons.wikimedia.org/wiki/File:Jensen_huang_stanford_2026-04-30_007.jpg) — Photo : Anderseidesvik, CC BY-SA 4.0, Wikimedia Commons

## Références

[^1]: [The Free Library — HTC Market Cap Surpasses Nokia](https://www.thefreelibrary.com/HTC+Market+Cap+Surpasses+Nokia.-a0253461010) — Le 7 avril 2011, la capitalisation boursière de HTC était d'environ 33,8 milliards de dollars US, dépassant Nokia

[^2]: [Wikipedia — HTC Corporation](https://zh.wikipedia.org/wiki/%E5%AE%8F%E9%81%94%E5%9C%8B%E9%9A%9B%E9%9B%BB%E5%AD%90) — Parts de marché des smartphones d'environ 20 % en 2011, capitalisation boursière dépassant le billion, actions ayant atteint plus d'un millier de dollars taïwanais

[^3]: [Wikipedia — HTC Dream](https://en.wikipedia.org/wiki/HTC_Dream) — Premier smartphone Android au monde en 2008

[^4]: [Wikipedia — Courbe en souriante](https://zh.wikipedia.org/wiki/%E5%BE%AE%E7%AC%91%E6%9B%B2%E7%B7%9A) — Proposée par Shih Ming-deh en 1992 dans _Rebuilding Acer_

[^4b]: [Wikipedia — MediaTek](https://zh.wikipedia.org/wiki/%E8%81%AF%E7%99%BC%E7%A7%91%E6%8A%80) — L'un des plus grands fournisseurs mondiaux de SoC pour smartphones en termes de volume d'expéditions ; parts de marché d'environ 70 % dans les puces pour téléviseurs

[^5]: [Nvidia — Fourth Quarter and Fiscal 2026 Financial Results](https://nvidianews.nvidia.com/news/nvidia-announces-financial-results-for-fourth-quarter-and-fiscal-2026) — Communiqué de presse officiel de NVIDIA ; chiffre d'affaires FY2026 de 215,9 milliards de dollars US, bénéfice net de 120,1 milliards de dollars US (croisé avec la colonne de rapports de Wikipedia : https://en.wikipedia.org/wiki/Nvidia)

[^6]: [TSMC — Quarterly Results Q4 2025](https://investor.tsmc.com/english/quarterly-results/2025/q4) — Page investisseurs officielle de TSMC ; chiffre d'affaires annuel 2025 de 122,42 milliards de dollars US, bénéfice net de 55,13 milliards de dollars US (croisé avec la colonne de rapports de Wikipedia : https://en.wikipedia.org/wiki/TSMC)

[^7]: [Counterpoint — MediaTek Becomes Biggest Smartphone Chipset Vendor in Q3 2020](https://www.counterpointresearch.com/insights/mediatek-becomes-biggest-smartphone-chipset-vendor-q3-2020/) — Au troisième trimestre 2020, les expéditions de puces pour smartphones de MediaTek ont dépassé celles de Qualcomm pour la première fois, parts de marché d'environ 31 %

[^8]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Plateforme SoC Snapdragon présentée en novembre 2006 ; le nom de la marque vient du nom de la fleur antirrhinum, Dimensity fait référence à la troisième étoile de la Grande Ourse (les deux affirmations de nommage sont des données publiques de la marque, lien source officiel à compléter)

[^9]: [MediaTek — Dimensity 9400 Press Release](https://corp.mediatek.com/news-events/press-releases/mediatek-launches-flagship-dimensity-9400-soc-for-advanced-capabilities) — Dimensity 9400 présenté en octobre 2024 ; le cercle des critiques le reconnaît généralement pour son efficacité énergétique (description synthétique). Voir les premiers modèles équipés sur [Wikipedia — Vivo X200](https://en.wikipedia.org/wiki/Vivo_X200)

[^10]: [Wikipedia — Qualcomm Snapdragon](https://en.wikipedia.org/wiki/Qualcomm_Snapdragon) — Snapdragon Summit 2024 tenu à Maui, Hawaï, présentation de Snapdragon 8 Elite (lien URL du communiqué de presse officiel périmé, basé sur la source secondaire de Wikipedia)

[^11]: [Wikipedia — Foxconn](https://en.wikipedia.org/wiki/Foxconn) — ／ [Apple Inc.](https://en.wikipedia.org/wiki/Apple_Inc.) — Chiffre d'affaires FY2025 de Foxconn de 8,103 billions de dollars taïwanais, bénéfice net de 189,35 milliards de dollars taïwanais (marge nette d'environ 2,3 %) ; Chiffre d'affaires FY2025 d'Apple de 416,2 milliards de dollars US, bénéfice net de 112,0 milliards de dollars US (marge nette d'environ 26,9 %). Part des profits des téléphones Apple dépassant 80 % à son sommet : estimations annuelles de Counterpoint (lien source à compléter)

[^12]: [Wikipedia — Divine montagne protectrice de la nation](https://zh.wikipedia.org/wiki/%E8%AD%B7%E5%9C%8B%E7%A5%9E%E5%B1%B1) — Surnom de TSMC (bouclier de silicium) ; « Les semi-conducteurs sont la divine montagne protectrice de la nation de Taïwan » est une déclaration publique de Morris Chang en 2021 (source d'actualité à compléter)

[^13]: [Wikipedia — Jensen Huang](https://zh.wikipedia.org/wiki/%E9%BB%83%E4%BB%81%E5%8B%B3) — Né en 1963 à Tainan, immigré aux États-Unis en 1972 (à l'âge de neuf ans)

[^13b]: La deuxième partie de l'autobiographie de Morris Chang publiée en novembre 2024, volume de ventes de niveau best-seller de l'année (lien source à compléter)

[^14]: [Wikipedia — Lisa Su](https://zh.wikipedia.org/wiki/%E8%98%87%E5%A7%BF%E4%B8%B0) — Née en 1969 à Tainan, immigrée aux États-Unis avec sa famille à l'âge de trois ans

[^15]: [Wikipedia — ASUS](https://zh.wikipedia.org/wiki/%E8%8F%AF%E7%A2%A9) — Création de la marque secondaire « Republic of Gamers » (ROG) en 2006

[^16]: [Wikipedia — Gogoro](https://en.wikipedia.org/wiki/Gogoro) — Fondée en 2011 ; présentation du Gogoro Smartscooter et du réseau énergétique au CES 2015 ; fusion avec Poema Global SPAC et cotation au NASDAQ en 2022 ; Castrol, filiale de BP, annonce un investissement de jusqu'à 50 millions de dollars US en 2024

[^17]: [NVIDIA GTC 2024 Keynote](https://www.youtube.com/watch?v=Y2F8yisiS6E) — « The more you buy, the more you save » de Jensen Huang provient de cette vidéo officielle

[^18]: « Quietly Brilliant » est le slogan de marque mondial de HTC depuis 2009, « The Next Big Thing is Already Here » est le slogan de la publicité Galaxy de Samsung en 2011, « We will make life multiplanetary » est la déclaration de mission de SpaceX (les trois sont des textes commerciaux publics)

[^19]: [NVIDIA at Computex 2024 — Official Keynote Video](https://www.youtube.com/watch?v=pKXDVsWZmUU) — Discours clé de Computex de Jensen Huang le 2 juin 2024 à l'Université nationale de Taïwan

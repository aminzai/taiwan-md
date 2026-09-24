---
title: "Développement de l'IA à Taiwan et stratégies futures : le billet d'entrée matériel est acquis, quelle est la prochaine bataille"
description: "Le 8 octobre 2024, les prix Nobel de physique ont été décernés à Hopfield et Hinton, et le lendemain, ceux de chimie à AlphaFold. Le 29 mai de la même année, Jensen Huang a mangé des omelettes au marché nocturne de Ningxia à Taipei avec Morris Chang. Taiwan fabrique 90 % des serveurs d'IA mondiaux et 72 % des puces avancées, mais il est absent dans les solutions aux problèmes du réseau neuronal de 42 ans et du repliement des protéines de 50 ans. Est-ce suffisant pour cette île d'être seulement une usine sous-traitante, allant des Taiwan AI Labs fondés par Du Yijin de PTT au modèle LLM traditionnel TAIDE soutenu par le Conseil national de la science ?"
date: 2026-03-19
category: 'Technology'
tags:
  [
    'intelligence artificielle',
    'IA',
    'semi-conducteurs',
    'politique technologique',
    'transformation numérique',
    'prix nobel',
    'AlphaFold',
  ]
subcategory: '人工智慧'
author: 'Taiwan.md'
difficulty: 'advanced'
readingTime: 18
featured: true
lastVerified: 2026-05-19
lastHumanReview: true
image: '/article-images/technology/alphafold-cbln1-structure-2025.webp'
imageCredit: 'BQUB25-UPoch (own work, AlphaFold + PyMOL)'
imageLicense: 'CC BY 4.0'
imageSource: 'https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png'
translatedFrom: 'Technology/台灣人工智慧發展與未來策略.md'
sourceCommitSha: 'b67b190fb'
sourceContentHash: 'sha256:151b93f3268baa1f'
translatedAt: '2026-09-24T19:36:01.985999+00:00'
---

# Le développement de l'intelligence artificielle à Taïwan et les stratégies futures : le billet d'entrée matériel est acquis, quelle est la prochaine bataille ?

> **Aperçu en 30 secondes :** Le 8 octobre 2024, le prix Nobel de physique a été décerné aux physiciens ayant rédigé le Réseau Hopfield et aux cognitiveurs ayant développé la rétropropagation [^N1]. Le lendemain, le 9 octobre, le prix Nobel de chimie a été décerné à trois chercheurs qui ont résolu le problème du repliement des protéines sur cinquante ans grâce à l'IA [^N2]. Le 29 mai de la même année, Jensen Huang, PDG de Nvidia, est apparu au marché nocturne de Ningxia à Taipei pour manger _o-a-jie_ avec Tsang Chung-mou, Lin Pai-li et Tsai Li-hing. TSMC détient 72 % du chiffre d'affaires mondial dans le domaine des services de fonderie de puces, tandis que Foxconn, Quanta et Wistron produisent collectivement neuf dixièmes des serveurs d'IA mondiaux. Cependant, dans cette cérémonie scientifique qui a eu lieu sur deux jours et qui a légitimé quatre-dix-deux ans d'histoire des réseaux neuronaux, aucun nom n'est taïwanais. De l'Institut de recherche en IA de Taïwan fondé par Du Yijin à TAIDE, le grand modèle linguistique chinois traditionnel soutenu par le gouvernement, un pari est en cours : passer de la « fabrication d'IA » à « devenir une IA ».

## 42 ans d'attente : les deux prix Nobel de 2024 en deux jours

Le 8 octobre 2024, à Stockholm. L'Académie royale suédoise des sciences a annoncé que le Prix Nobel de physique était décerné à deux scientifiques de l'IA : John J. Hopfield, professeur émérite de Princeton âgé de 91 ans, et Geoffrey Hinton, âgé de 76 ans, qui avait quitté Google cinq mois plus tôt. Le prix, d'une valeur de 11 millions de couronnes suédoises, a été partagé équitablement entre les deux [^N1].

Le comité de sélection a justifié le prix par « des découvertes et inventions fondamentales qui permettent l'apprentissage automatique avec des réseaux neuronaux artificiels » [^N1]. C'est la première fois dans l'histoire du Prix Nobel de physique qu'un domaine aussi spécifique que les réseaux neuronaux est récompensé directement.

Le lendemain, le 9 octobre, c'était le prix Nobel de chimie. Les trois lauréats étaient David Baker de l'Université de Washington, ainsi que Demis Hassabis et John Jumper de DeepMind. Baker a reçu la moitié du prix, tandis que Hassabis et Jumper ont partagé l'autre moitié [^N2]. La justification du prix était divisée en deux parties : la première pour « la conception de protéines par calcul » (pour Baker), et la seconde pour « la prédiction de structures protéiques » (pour Hassabis et Jumper).

Deux jours, deux prix Nobel, tous liés à l'IA. C'est sans précédent dans l'histoire du Prix Nobel.

Pour comparer les échelles de temps : lorsque Hopfield a publié son article intitulé « Neural networks and physical systems with emergent collective computational abilities » dans le _Proceedings of the National Academy of Sciences_ (PNAS) en 1982, il venait de passer de la physique du solide aux neurosciences [^N3]. De 1982 à 2024, cela fait 42 ans. L'article de 1986 de Hinton et Rumelhart qui a rendu l'algorithme de rétropropagation utilisable [^N4] a également nécessité 38 ans entre sa publication et la récompense. AlphaFold, depuis son apparition lors du CASP13 en 2018 jusqu'au Nobel en 2024, n'a mis que 6 ans.

En fin de compte, les lauréats récompensés ces deux jours ne sont pas ChatGPT, mais des articles incompréhensibles datant de trente ou quarante ans. Le décalage temporel entre la recherche fondamentale et l'application industrielle est toujours là.

![Portrait officiel de Geoffrey E. Hinton lors du Nobel à Stockholm le 8 décembre 2024](/article-images/technology/hinton-nobel-2024.webp)
_Geoffrey Hinton, lauréat du Prix Nobel de physique 2024, semaine du Nobel à Stockholm. Photo : Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](<https://commons.wikimedia.org/wiki/File:Geoffrey%5FE.%5FHinton,%5F2024%5FNobel%5FPrize%5FLaureate%5Fin%5FPhysics%5F(3x4%5Fcropped).jpg>)._

## Le festin de plusieurs milliards au marché nocturne de Ningxia

Le soir du 29 mai 2024, avant le début de Computex, un groupe d'invités inhabituels est apparu au marché nocturne de Ningxia à Taipei. Jensen Huang, PDG de NVIDIA, accompagné de Morris Chang, fondateur de TSMC, Lin Bairi, président de Quanta Computer, et Tsai Lik-hing, PDG de MediaTek, se sont serrés devant un stand pour manger des _oezaijian_ (crêpes d'huîtres) [^1]. Les passants ont reconnu Jensen Huang, ce qui l'a immédiatement entouré de fans et de journalistes, une scène comparable à celle du fan-meeting.

La valeur marchande de ce repas dépassait plusieurs milliards de dollars. Mais la véritable histoire ne se trouvait pas à table, mais dans la chaîne industrielle derrière la table : les entreprises représentées par ces personnes soutiennent le fondement physique du calcul IA mondial. Lors de son voyage à Taïwan, Jensen Huang a déclaré publiquement : « Taïwan est l'un des pays les plus importants au monde » [^2]. Ce n'était pas une politesse. Sans Taïwan, il n'y aurait pas de base matérielle pour la révolution de l'IA.

Jensen Huang, né à Taipei en 1963 et ayant passé son enfance à Tainan avant d'immigrer aux États-Unis à l'âge de neuf ans [^3], a cofondé NVIDIA en 1993, qui est aujourd'hui synonyme de puces IA. Chaque GPU avancé conçu par NVIDIA, des A100 et H100 utilisés pour entraîner ChatGPT aux plus récents Blackwell, est fabriqué par TSMC [^4].

Les deux listes du prix Nobel publiées quatre mois plus tard à Stockholm ne contenaient aucun nom lié à ce repas. Ce décalage n'est pas une coïncidence, mais un fait structurel.

## Matériel : Une île qui soutient toute la révolution de l'IA

La position de Taïwan dans la chaîne d'approvisionnement matérielle de l'IA est un euphémisme.

Dans le domaine de la fabrication de puces, TSMC a représenté 72 % du marché mondial des services de fonderie en 2025[^5]. Pour les processus les plus avancés inférieurs à 7 nanomètres, la part de marché de TSMC dépasse neuf décimales. NVIDIA détient environ 86 % du marché des GPU pour l'IA, et ces GPU sont presque entièrement fabriqués par TSMC[^6]. La grande majorité de la puissance de calcul utilisée dans le monde pour entraîner et exécuter des modèles d'IA est née dans les salles blanches de Taïwan.

Une fois que les puces sont fabriquées, elles doivent être assemblées en serveurs pour entrer dans les centres de données. Ce segment est également dominé par Taïwan. Les trois grands ODM — Foxconn (Hon Hai), Quanta et Wistron — produisent ensemble environ 90 % des serveurs d'IA mondiaux[^7]. En 2025, le chiffre d'affaires annuel de ces trois entreprises a dépassé chacun un trillion de dollars taïwanais (environ 32 milliards de dollars américains), avec les revenus des serveurs d'IA dépassant pour la première fois ceux des produits électroniques grand public au deuxième trimestre[^8].

La performance des puces d'IA ne dépend pas seulement de la miniaturisation du processus, mais aussi de la technologie d'encapsulation. La technologie d'emballage avancée CoWoS (Chip on Wafer on Substrate) de TSMC est cruciale pour que les GPU haut de gamme de NVIDIA atteignent leurs objectifs de performance. En 2026, seule NVIDIA devrait nécessiter 595 000 wafers CoWoS, ce qui représente 60 % de la demande mondiale[^9].

Foxconn collabore également avec NVIDIA et le gouvernement taïwanais pour construire un supercalculateur d'IA de classe 100 mégawatts (MW) à Kaohsiung, utilisant l'architecture Blackwell la plus récente[^10]. Taïwan est en train de passer du « lieu où les puces IA sont fabriquées » au « lieu où l'IA fonctionne ».

![Vue extérieure de l'usine Fab 5 du parc scientifique de Hsinchu (TSMC), scène des années 2010, site physique de la fabrication de wafers semi-conducteurs](/article-images/technology/tsmc-fab5-hsinchu-2010.webp)
_Usine Fab 5 de Hsinchu TSMC, site physique de la fabrication de puces IA. Photo : Wikimedia Commons via [Fichier Fab 5 TSMC](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg)._

Le problème est le suivant : si le matériel obtient le billet d'entrée, où se déroulera la prochaine bataille ?

> 📝 **Note du curateur**
>
> La narration courante est que « la montagne sacrée de Taïwan soutient la révolution de l'IA ». Cette formulation est commode narrativement, mais elle inverse en partie la causalité. C'est la révolution de l'IA qui a besoin des GPU pour choisir TSMC, et non l'inverse. La véritable tension réside dans : lorsque le GPU devient une marchandise, où va la valeur à l'étape suivante ? Les réponses données par les deux prix Nobel en 2024 sont le modèle lui-même — les 12 pages écrites par Hopfield, cette nuit où Hinton et son étudiant Krizhevsky ont réduit le taux d'erreur de reconnaissance d'images ImageNet de 26,2 % à 15,3 % avec AlexNet en 2012[^N5], et l'après-midi où les gens de Hassabis ont fait obtenir un GDT médian de 92,4 pour AlphaFold lors du CASP14.

## Hopfield en 1982 : un modèle de mémoire écrit par des physiciens

En 1982, John Hopfield, physicien de la matière condensée à Princeton, a publié un article de seulement 12 pages intitulé : « Neural networks and physical systems with emergent collective computational abilities » [^N3], paru dans _Proceedings of the National Academy of Sciences of the United States of America_ [^N3].

Ce qu'il a fait revient essentiellement à traduire la « mémoire » en physique.

En physique, il existe quelque chose appelé le verre de spin (spin glass) : un ensemble d'atomes magnétiques dont chaque spin possède une orientation propre et qui interagissent les uns avec les autres, ce qui amène l'ensemble du système à trouver spontanément un point d'énergie minimale. Hopfield a transposé ce concept aux neurones : il imagine les neurones comme des spins, et les forces de connexion comme des interactions ; le réseau entier converge spontanément vers un état stable correspondant à un « minimum d'énergie » [^N3]. Chaque minimum d'énergie représente une mémoire stockée.

L'élégance de ce modèle réside dans le fait qu'il permet de décrire la mémoire en utilisant un langage physique. Étant donné des indices incomplets, le réseau trouve par lui-même le point d'énergie minimale le plus proche et complète l'intégralité du souvenir. C'est l'ancêtre mathématique de ce que font les IA génératives aujourd'hui.

En 1982, Taïwan était encore au début de son industrie électronique, avant même la création de TSMC. Charles Tsang a attendu jusqu'en 1987 pour fonder l'entreprise qui deviendra le « Mont Sacré » 42 ans plus tard. Le nombre de citations de l'article de Hopfield sur Google Scholar a dépassé vingt-sept mille d'ici 2026 [^N6].

Ce qui est encore plus intéressant, c'est ce que Hopfield a dit par la suite. Il a passé toute sa vie à faire de la physique de la matière condensée à Princeton, et son passage aux neurosciences était considéré comme un « passe-temps » par ses pairs de l'époque. Lorsque le prix Nobel de 2024 est annoncé, il avait 91 ans, et lors d'un entretien téléphonique avec la Royal Swedish Academy of Sciences, il a exprimé son inquiétude quant à « la direction de l'IA que personne ne comprend ou ne contrôle » [^N7].

Celui qui a écrit les fondations mathématiques de l'IA moderne nous met en garde le jour où il reçoit son prix.

![Portrait de John J. Hopfield lors d'un entretien au Nobel à Stockholm le 8 décembre 2024, costume sombre, cheveux blancs, expression posée](/article-images/technology/hopfield-nobel-2024.webp)
_John J. Hopfield, lauréat du Prix Nobel de physique en 2024, semaine du Nobel à Stockholm. Photo : Arthur Petron, 2024-12-08. [CC BY-SA 4.0 via Wikimedia Commons](https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg).\_

## Hinton : L'article de 1986 et l'avertissement de son départ de Google en 2023

Geoffrey Hinton, né à Wimbledon, Londres, en 1947, est une autre figure dont la reconnaissance a pris 38 ans[^N8].

En 1986, Hinton publia avec David Rumelhart et Ronald Williams un article dans _Nature_ sur la rétropropagation (backpropagation)[^N4]. Ce algorithme signifie que lorsque le réseau neuronal fait une erreur, le signal d'erreur peut être renvoyé en arrière à chaque couche pour ajuster les poids de connexion progressivement. C'est ainsi que tous les modèles d'apprentissage profond sont entraînés aujourd'hui.

Bien que cet algorithme ait été rédigé en 1986, il n'a explosé qu'une fois trois éléments réunis : une puissance de calcul suffisamment bon marché, une quantité suffisante de données, et des personnes prêtes à croire en cette voie. Les deux premiers éléments étaient prêts au début des années 2010 ; les représentants du troisième élément sont Hinton avec ses deux étudiants Alex Krizhevsky et Ilya Sutskever. En 2012, AlexNet, un réseau neuronal convolutif entraîné par GPU, a obtenu une erreur de top-5 de 15,3 % dans le concours de reconnaissance d'images ImageNet, laissant loin derrière la deuxième place avec 26,2%[^N5]. C'est à ce moment que l'industrie a commencé à croire que la rétropropagation fonctionnait réellement.

En mars 2013, Google a acquis la petite entreprise DNNresearch de Hinton pour 44 millions de dollars, intégrant le scientifique âgé de 65 ans dans ses rangs[^N8]. Pendant la décennie suivante, il fut l'un des chercheurs en IA les plus influents de la Silicon Valley.

Puis, le 1er mai 2023, _The New York Times_ a publié un entretien : Hinton avait quitté Google.

La raison de son départ n'était pas la retraite. Dans cet entretien, il a déclaré vouloir « pouvoir discuter des risques liés à l'IA librement, sans avoir à considérer l'impact sur Google »[^N9]. Les choses qu'il a prévues incluaient : les systèmes d'IA pourraient devenir plus intelligents que les humains très rapidement, et pourraient être utilisés par de mauvaises personnes pour faire du mal, et « il est difficile de savoir quoi faire pour arrêter cela »[^N9]. Il a même dit se sentir « un peu regretter son travail toute une vie »[^N9].

Lorsqu'il a reçu le prix Nobel de physique en 2024, il a répété cet avertissement lors d'un entretien téléphonique : il faut faire attention au risque de perte de contrôle par l'IA[^N10].

Les personnes qui ont écrit les algorithmes d'entraînement de l'apprentissage profond et celles qui ont écrit les modèles de mémoire se sont présentées simultanément devant le public à la Royal Swedish Academy of Sciences le 8 octobre 2024, pour rappeler à tout le monde que cette chose pouvait être plus dangereuse qu'on ne le pensait. Cette scène rappelle l'expression d'Oppenheimer en 1945 lorsqu'il regarda les nuages de champignons se former dans le désert du Nouveau-Mexique.

Deux mois plus tard, le 8 décembre 2024, Hinton a prononcé son discours Nobel à la Aula Magna de l'Université de Stockholm. Le sujet était « Boltzmann Machines » — un travail précoce qui faisait suite à Hopfield et qui intégrait la distribution de probabilité thermodynamique dans les réseaux neuronaux. Après avoir écouté, on a compris que l'article sur la rétropropagation en 1986 n'était pas une idée isolée, mais un ensemble de pensées issues de la rencontre entre la physique et les sciences cognitives des années 80 :

<div class="video-embed" style="position:relative;padding-bottom:56.25%;height:0;overflow:hidden;margin:1.5rem 0;border-radius:8px;">
  <iframe src="https://www.youtube.com/embed/iCS1ds0UDP8" title="Boltzmann Machines — Nobel Prize lecture by Geoffrey Hinton, Nobel Prize in Physics 2024" style="position:absolute;top:0;left:0;width:100%;height:100%;border:0;" loading="lazy" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

_Chaîne officielle de la Royal Swedish Academy of Sciences : Le discours Nobel de Geoffrey Hinton le 8 décembre 2024 sur les « Boltzmann Machines ». De l'écriture des machines de Boltzmann avec Sejnowski dans les années 1980, à la rétropropagation, jusqu'aux LLM d'aujourd'hui — un total de quarante ans. Dans ses cinq dernières minutes, il a réitéré son inquiétude concernant les risques liés à l'IA, cette fois sur la scène du Nobel._

## De PTT aux laboratoires d'IA : les deux entreprises de Du Yijin

Revenons sur l'île de Taïwan. Au moment où Hopfield écrivait le modèle de mémoire, Taïwan commençait à peine à avoir des départements d'informatique.

En 1995, Du Yijin, étudiant en deuxième année du département informatique de National Taiwan University (NTU), a installé [PTT](/fr/technology/ptt-bulletin-board-system/) dans sa chambre avec un ordinateur 486 et des logiciels open source, ce qui est devenu le plus grand tableau d'affichage électronique de Taïwan. Trente ans plus tard, PTT est toujours consulté par des centaines de milliers de personnes chaque jour, faisant de lui une fossile de la culture Internet taïwanaise.

Du Yijin a ensuite travaillé chez Microsoft, participant au développement de l'assistant vocal Cortana. En avril 2017, il a abandonné le salaire élevé de la Silicon Valley pour revenir à Taïwan et fonder "Taiwan AI Labs" (Laboratoires d'Intelligence Artificielle de Taïwan), qui est la première organisation de recherche en IA non lucrative et ouverte d'Asie[^11].

Sa motivation était simple : Taïwan possède des talents logiciels de calibre mondial, mais ces talents partent tous pour la Silicon Valley. Il voulait créer une plateforme où ceux qui souhaitaient revenir ou rester pourraient faire de la recherche en IA.

Le produit le plus connu de Taiwan AI Labs est "Yateng Transcription" (雅婷逐字稿), un système de reconnaissance vocale optimisé pour le chinois traditionnel et l'accent taïwanais. Pendant la pandémie de COVID-19, le laboratoire a également développé des outils de détection de fausses nouvelles et une IA médicale fédérée[^12]. Le point commun de ces projets est qu'ils résolvent des problèmes locaux à Taïwan en utilisant des données locales, au lieu de traduire des modèles américains pour les utiliser.

L'histoire de Du Yijin, de PTT aux Labs d'IA, est en quelque sorte un microcosme du développement logiciel taïwanais : il n'y a pas de manque de capacité technique, mais plutôt un manque d'écosystème pour retenir les talents.

> 💡 **Saviez-vous que**
>
> En 1986, l'année où Hinton publie la rétropropagation (backpropagation), le PIB de Taïwan était d'environ 77,9 milliards de dollars américains, avec un PIB par habitant d'environ 4 007 dollars américains, et le Science Park de Hsinchu venait de fonctionner six ans[^N11]. Trois événements se sont produits sur la même planète simultanément, mais cette ligne historique ne convergera qu'26 ans plus tard sur l'ensemble de données ImageNet. L'échelle de temps de la recherche fondamentale est toujours plus longue que ce que raconte le récit industriel.

## AlphaFold : L'autre moitié du problème du repliement des protéines, un défi de 50 ans récompensé par le Nobel

L'histoire du prix Nobel de chimie en 2024 commence avec un problème datant de 1972.

En cette année-là, lors de son discours de réception du prix Nobel de chimie, le biochimiste américain Christian Anfinsen a avancé une hypothèse : la structure tridimensionnelle d'une protéine est entièrement déterminée par sa séquence d'acides aminés [^N12]. Si cette hypothèse était vraie, théoriquement, il suffirait de voir une séquence d'acides aminés pour calculer la structure 3D correspondante. Mais ce « devrait » n'a pas été réalisé pendant un demi-siècle. Le repliement des protéines est considéré comme un grand défi. La communauté scientifique organise le concours CASP tous les deux ans, où les résultats de prédiction soumis sont comparés aux structures expérimentales ; depuis 1994, 13 éditions ont eu lieu sans qu'une percée ne soit réalisée [^N13].

Ce n'est qu'avec CASP13 en 2018 que DeepMind a participé avec la première génération d'AlphaFold et remporté le prix, bien que la précision fût encore insuffisante pour être pratique. Le véritable tournant fut CASP14, le 30 novembre 2020 : AlphaFold 2 a obtenu un score médian GDT de 92,4 [^N13]. Un GDT de 92,4 signifie qu'au-delà de la moitié des prédictions, l'écart des positions atomiques par rapport aux valeurs expérimentales est inférieur à un angström, atteignant le niveau de résolution expérimental. John Moult, organisateur du CASP, a déclaré ce jour-là : « dans une large mesure, ce problème est résolu » [^N13].

Un problème non résolu depuis 50 ans a été résolu en six ans par une équipe de recherche londonienne.

Les événements se sont accélérés par la suite. En juillet 2021, le code source d'AlphaFold 2 a été rendu open source ; la même année, DeepMind et l'European Molecular Biology Laboratory (EMBL-EBI) ont collaboré pour créer une base de données publique des structures protéiques prédites par AlphaFold. En juillet 2022, cette base de données couvrait un million d'espèces et environ deux cents millions de structures protéiques, rendant gratuitement les modèles 3D de presque toutes les protéines connues sur Terre [^N14].

Le 8 mai 2024, DeepMind a publié AlphaFold 3 dans _Nature_, étendant la capacité de prédiction d'une seule protéine à l'interaction entre les protéines et l'ADN, l'ARN, les ligands et les ions [^N15]. Des domaines nécessitant de savoir comment les molécules s'emboîtent – du développement de nouveaux médicaments à la conception de vaccins en passant par l'ingénierie enzymatique – ont été fondamentalement transformés par cet outil.

Demis Hassabis, créateur d'AlphaFold, n'est pas un biochimiste traditionnel. Il a commencé les échecs à quatre ans et a obtenu le titre de maître à 13 ans ; à l'âge de 17 ans, il a co-développé le jeu de simulation _Theme Park_ avec Peter Molyneux, qui s'est vendu en plusieurs millions d'exemplaires [^N16]. En 2010, il a fondé DeepMind à Londres avec Shane Legg et Mustafa Suleyman, et l'entreprise a été rachetée par Google pour 400 millions de livres sterling en 2014 [^N16]. AlphaGo de DeepMind a battu Lee Se-jin en 2016, AlphaFold 2 en 2020, et le prix Nobel en 2024 : trois événements espacés de moins de dix ans.

La ligne qui les relie est un pari commun : utiliser des réseaux neuronaux pour résoudre ce que l'esprit humain n'a pas pu résoudre par le passé. Le Go est un système fermé ; le repliement des protéines est un système ouvert mais fortement contraint physiquement. Hassabis a choisi le bon champ de bataille pour ces deux domaines.

À Taïwan, la recherche sur les molécules glucidiques et les protéines établie sous la direction du directeur du Institute of Biological Sciences (IBMS) du Academia Sinica (2006-2016) est l'investissement académique le plus proche de cette frontière [^N17]. Des équipes au Département de Biologie Médicale et au Département de Biochimie de l'Academia Sinica mènent des recherches en aval en utilisant les poids open source d'AlphaFold. Cependant, Taïwan ne dispose pas actuellement d'une structure institutionnelle pour le développement de modèles cœur de niveau AlphaFold.

> ⚠️ **Point de vue controversé**
>
> Le prix Nobel de chimie accordé à AlphaFold a fait l'objet de débats dans la communauté scientifique : certains biochimistes structuraux estiment que ce prix aurait dû être décerné aux chercheurs en diffraction des rayons X ou en résonance magnétique nucléaire qui ont réalisé les premières expériences cruciales, plutôt qu'à une bête de calcul élevée au rang de discipline chimique [^N18]. D'autres considèrent que cette controverse est dépassée – lorsque des algorithmes peuvent compléter la structure 3D de presque toutes les protéines de la Terre en cinq ans, c'est cela, la chimie. Le débat entre ces deux positions a progressivement penché vers la seconde après octobre 2024, mais la tension demeure : quand ce que l'IA peut faire s'étend, faut-il redéfinir les frontières des disciplines traditionnelles ?

## TAIDE : Pourquoi Taïwan a besoin de ses propres modèles linguistiques

En avril 2023, après que ChatGPT ait envahi le monde pendant six mois, le Conseil national des sciences et de la technologie (NSTC) de Taïwan a lancé le projet « TAIDE », dont le nom complet est Trustworthy AI Dialogue Engine (Moteur de dialogue IA générative digne de confiance) [^13].

Pourquoi une île de deux millions trois cent mille habitants devrait-elle développer ses propres grands modèles linguistiques ?

La raison n'est pas seulement technique. Le mandarin traditionnel représente un pourcentage extrêmement faible dans les données d'entraînement de l'IA mondiale ; la majorité des données en chinois proviennent de sites en chinois simplifié. Lorsque les Taïwanais utilisent ChatGPT ou d'autres modèles, les réponses sont souvent empreintes des habitudes terminologiques et des préjugés culturels de la Chine continentale. Des différences apparemment minimes, comme « 視頻 » (vidéo) au lieu de « 影片 » (film), ou « 質量 » (qualité) au lieu de « 品質 » (qualité), cachent une question de subjectivité culturelle. _Tianxia Magazine_ a rapporté TAIDE sous le titre « Empêcher l'invasion culturelle chinoise par l'IA » [^14].

En avril 2024, l'équipe TAIDE a publié les modèles commerciaux TAIDE-LX-7B et académiques TAIDE-LX-13B, qui ont montré de bons résultats dans des tâches telles que la rédaction, la traduction et le résumé [^15]. En 2026, TAIDE 2.0 a été lancé, complété par le modèle Breeze-8B soutenu par MediaTek, faisant passer l'écosystème LLM de Taïwan du stade de « rattrapage » au stade d'« utilisable » [^16].

Ce qui est encore plus intéressant, c'est l'épanouissement des applications. L'Université de Chung-Hsing a créé le système de recherche de connaissances agricoles « Shennong TAIDE » ; l'Université de Tainan a développé un robot conversationnel Taïwanais-Anglais pour l'enseignement du dialecte taïwanais ; et l'Université de Yanyang (Mingjiao) a entraîné des modèles TAIDE en dialecte taïwanais et Hakka [^17]. Ces applications prouvent une chose : le modèle linguistique est à la fois un produit technologique et un vecteur culturel. Une IA qui ne comprend pas « Tianchuanri » ou les processions de Mazu ne peut pas véritablement servir le peuple de Taïwan.

Cependant, l'échelle de TAIDE reste petite : avec 8B pour le commercial et 13B pour l'académique, il est inférieur d'au moins deux ordres de grandeur à des modèles comme GPT-4 d'OpenAI (estimé à plus d'un trillion de paramètres). Cet écart n'est pas un problème de capacité, mais un problème de budget GPU. L'effort de calcul nécessaire pour entraîner un LLM de pointe se compte en centaines de millions de dollars, au même niveau que le budget annuel d'une institution de recherche nationale.

## La Cybersécurité "Née de l'Attaque"

Taïwan est l'un des pays les plus fréquemment victimes d'attaques en ligne au monde. Cette réalité malheureuse a, par contre, donné naissance à une industrie de cybersécurité IA robuste.

CyCraft, fondée fin 2017, est la première entreprise taïwanaise à combiner l'IA avec la surveillance des points d'extrémité (endpoint monitoring). Sa technologie a été répertoriée sept fois dans les rapports de l'organisme mondial Gartner, et c'est le seul fournisseur taïwanais à avoir passé trois évaluations d'autorité MITRE ATT&CK aux États-Unis [^18]. En février 2026, CyCraft a été cotée sur la bourse de Taiwan (TWSE Innovation Board), devenant le premier fabricant de logiciels de cybersécurité IA avec des capacités de recherche et développement autonomes de niveau international dans le marché du capital taïwanais [^19].

Les clients de CyCraft comprennent des agences gouvernementales taïwanaises, des unités de défense nationale, des banques et des entreprises de semi-conducteurs – qui sont précisément les cibles privilégiées des pirates informatiques de niveau étatique. L'entreprise possède des filiales au Japon et à Singapour, exportant ainsi son « expérience pratique acquise lors d'attaques » dans toute la région Asie-Pacifique.

Ce cas illustre un point : l'avantage de Taïwan en matière d'IA ne provient pas uniquement des semi-conducteurs, mais aussi des capacités pratiques forgées par sa situation géopolitique particulière.

## Politique : Du « Année Zéro de l'IA » au Ministère du Développement Numérique

L'évolution de la politique de l'IA à Taïwan peut être comprise à travers trois étapes clés.

De 2017 à 2018, il s'agissait de la phase de lancement. L'Executive Yuan a désigné 2017 comme « Année Zéro de l'IA » (AI 元年), proposant le concept de « Stratégie nationale pour une petite économie, un grand potentiel en IA », reconnaissant que le marché taïwanais était petit, mais mettant l'accent sur trois atouts : la fabrication de semi-conducteurs, la chaîne d'approvisionnement des TIC et les talents scientifiques et techniques. En 2018, le premier « Plan d'Action IA Taïwan » a été lancé, investissant plus de 40 milliards de dollars taïwanais sur quatre ans, avec pour objectif principal la construction de l'infrastructure de calcul IA, connue sous le nom de « Taiwan AI Cloud » (TWCC) [^20].

En 2022, on est passé à une phase de systématisation. Le Ministère du Développement Numérique (moda) a été créé, consolidant les activités numériques qui étaient auparavant réparties entre le Ministère de la Science et de la Technologie, le Ministère de l'Économie et le Ministère des Transports. L'importance de cette étape réside dans le fait que la politique de l'IA est passée d'un « projet ministériel » à une « stratégie nationale interministérielle ». La même année, le gouvernement a publié les « Directives de Recherche en Intelligence Artificielle », insistant sur des principes tels que l'humanité centrée, la transparence interprétable et l'équité sans discrimination.

De 2023 à aujourd'hui, on est dans une transition vers l'IA générative. L'impact de ChatGPT a forcé un virage politique. Le plan TAIDE a été lancé, le projet de loi sur l'IA a été promu, et l'adoption de l'IA par les secteurs public a été accélérée. La stratégie de Taïwan est très pragmatique : au lieu de rivaliser avec la Chine et les États-Unis en termes de nombre d'articles de recherche fondamentale, elle "greffe" l'IA sur ses avantages manufacturiers existants. La fabrication intelligente, l'imagerie médicale et la prédiction du rendement des semi-conducteurs sont tous des domaines où Taïwan dispose de données, de cas pratiques et de compétitivité.

Le problème est qu'aucune des personnes récompensées lors de les deux jours du prix Nobel en octobre 2024 ne provenait de cette voie de la « fabrication intelligente ».

## Anxiété : Le déficit logiciel de l'empire du matériel

Derrière les chiffres brillants, le développement de l'IA à Taïwan présente un problème structurel : un déséquilibre grave entre le matériel et le logiciel.

Taïwan produit neuf pour cent des serveurs d'IA mondiaux et la majeure partie des puces d'IA, mais il a une faible présence dans les domaines du « logiciel », tels que le développement de modèles d'IA, l'écosystème des données et les logiciels de plateforme. Aucun des vingt principaux modèles d'IA mondiaux, y compris GPT, Claude, Gemini et LLaMA, ne provient de Taïwan. En comparant les travaux primés par le prix Nobel double en 2024, allant du réseau de Hopfield à la rétropropagation jusqu'à AlphaFold, ces trois lignes sont très éloignées de l'industrie taïwanaise.

La raison est une nouvelle version d'un vieil problème. Lorsque les ingénieurs de TSMC peuvent gagner plus de deux millions de dollars taïwanais par an, il est difficile pour les startups logicielles de recruter les meilleurs talents. Google, Microsoft et NVIDIA ont des centres de R&D à Taïwan, créant un puissant effet d'aspiration en termes de salaires et d'avantages sociaux. Le choix privilégié d'un diplômé du département informatique de l'Université nationale de Taiwan est souvent une entreprise étrangère ou TSMC IT, plutôt que de rejoindre une startup d'IA locale.

Le défi plus fondamental réside dans les données. La valeur des modèles d'IA provient des données d'entraînement, et la quantité de données de haute qualité en chinois traditionnel est infime par rapport à l'anglais ou au chinois simplifié. Le volume de texte produit par les 23 millions d'habitants de Taïwan ne peut naturellement pas rivaliser avec le monde anglophone ou la Chine continentale. Le projet TAIDE tente de résoudre ce problème, mais le désavantage en termes d'échelle des données est structurel.

Le véritable pari de l'IA à Taïwan repose sur les applications verticales plutôt que sur les modèles fondamentaux : au lieu de rivaliser frontalement avec OpenAI ou Google sur les modèles généraux, Taïwan choisit de trouver une place irremplaçable dans l'IA des processus de semi-conducteurs, l'IA d'imagerie médicale, l'IA de cybersécurité et le NLP en chinois traditionnel. Dans ces domaines, Taïwan possède un avantage unique en termes de données et de scénarios que les autres ont du mal à répliquer.

## Le choix de l'IA pour une île

En 2026, Taïwan se trouve dans une position unique : elle est indispensable dans la chaîne d'approvisionnement matérielle de l'IA, mais reste marginale dans l'écosystème logiciel de l'IA.

Ce n'est pas entièrement négatif. Historiquement, le modèle de succès de Taïwan a été celui du « fabricant sans marque, la marque derrière le fabricant ». Le modèle de sous-traitance pure inventé par Tseng Chung-ming en 1987 a fait de TSMC l'une des dix plus grandes entreprises mondiales en capitalisation boursière. Aujourd'hui, la même logique se reproduit dans l'industrie des serveurs d'IA : Foxconn ne développe pas de modèles d'IA, mais tous les modèles d'IA du monde s'exécutent sur les serveurs assemblés par Foxconn.

Cependant, les règles du jeu à l'ère de l'IA pourraient être différentes. Lorsque le centre de valeur se déplace du matériel vers le logiciel et les données, l'espace de profit pour ceux qui ne font que sous-traiter est comprimé. Les lauréats des prix Nobel distribués ces deux jours en 2024 sont tous issus de la couche logicielle. Hopfield a écrit un modèle mathématique, Hinton a écrit un algorithme d'entraînement, et Hassabis a écrit une méthode de résolution biologique. Ces travaux s'exécutent sur du matériel fabriqué à Taïwan, mais les prix ne sont pas décernés au matériel.

Taïwan doit développer des capacités en matière de logiciels et de données sur la base de sa suprématie matérielle : le matériel reste la fondation, et les nouvelles couches de valeur sont ajoutées par-dessus. TAIDE est une tentative, CyCraft est une tentative, Taiwan AI Labs est une tentative. Leur point commun est : ne pas viser à faire « l'IA la plus grande du monde », mais à faire « l'IA qui connaît le mieux Taïwan ».

Il y a 42 ans, lorsque Hopfield a rédigé ces 12 pages à Princeton, personne ne savait que cela deviendrait la base mathématique des modèles de mémoire humaine d'aujourd'hui. Il y a 50 ans, lorsque Anfinsen a proposé l'hypothèse du repliement des protéines dans son discours Nobel, personne n'avait prévu qu'elle serait résolue par un groupe de Londoniens au cours de l'après-midi de 2020. L'échelle de temps de la recherche fondamentale est plus longue que chaque salon Computex.

Le repas du marché nocturne de Ningxia représente la position accumulée par Taïwan ces 42 ans. La prochaine bataille ne se joue pas devant un stand d'Oa Ji Jian, mais dans la capacité de Taïwan à permettre à un étudiant codant dans une résidence universitaire de National Taiwan University de recevoir son propre prix Nobel pour cette île dans vingt ou trente ans.

---

**Lectures complémentaires** :

- [L'ascension du pays IA : développement et stratégie d'intelligence artificielle de Taïwan](/fr/technology/ai-development-in-taiwan) — Récit précoce des cadres politiques, plan d'action IA, les cinq domaines stratégiques, une vue d'ensemble de la manière dont le « dragon gardien » semi-conducteur s'adapte à la révolution de l'IA.
- [Laboratoire d'Intelligence Artificielle de Taïwan](/fr/technology/taiwan-ai-labs) — Le parcours complet de Tu Yujin, de PTT aux AI Labs, l'écosystème de modèles linguistiques open source TAIDE / TAME / FedGPT.
- [École d'Intelligence Artificielle de Taïwan](/fr/technology/taiwan-ai-academy) — L'école militaire IA construite grâce à une collecte de fonds privée de 180 millions par Chen Shengwei, un appel téléphonique inachevé : l'histoire de la formation de talents avec plus de dix mille anciens élèves en huit ans.
- [Vie quotidienne de Taïwan AI](/fr/technology/taiwan-ai-in-daily-life) — Observations au niveau des scènes sur l'arrivée de l'IA générative dans la vie quotidienne à Taïwan, allant de la commande dans les supérettes à l'examen par lots de la NHI.
- [Entreprises de Taïwan : TSMC](/fr/economy/tsmc) — Le leader mondial de la sous-traitance de wafers, le cœur de la fabrication de puces IA, de l'ère de la sous-traitance pure de Tseng Chung-ming à l'histoire du packaging avancé.
- [Industrie des semi-conducteurs](/fr/technology/taiwan-semiconductor-industry) — Vue d'ensemble de l'écosystème des semi-conducteurs taïwanais, de la conception IC au test et l'emballage.
- [Développement de l'industrie de la cybersécurité de Taïwan](/fr/technology/taiwan-cybersecurity-industry-development) — Comment les pressions géopolitiques ont engendré une industrie de la cybersécurité de niveau Asie-Pacifique.

## Sources des images

Cet article utilise 4 images de domaine public / sous licence CC, toutes mises en cache dans `public/article-images/technology/` pour éviter les liens vers des serveurs externes :

- [Structure tridimensionnelle de la protéine CBLN1 par AlphaFold avec codage arc-en-ciel](https://commons.wikimedia.org/wiki/File:Estructura_tridimensional_de_la_prote%C3%AFna_CBLN1_per_AlphaFold_amb_codificaci%C3%B3_rainbow.png) — image principale, structure prédite de la protéine CBLN1 par AlphaFold, codée en couleurs rainbow N→C. Photo: BQUB25-UPoch (œuvre personnelle, AlphaFold + PyMOL), 15/11/2025, CC BY 4.0.
- [Geoffrey E. Hinton, Lauréat du Prix Nobel de Physique 2024 (3x4 recadré)](<https://commons.wikimedia.org/wiki/File:Geoffrey%5FE.%5FHinton,%5F2024%5FNobel%5FPrize%5FLaureate%5Fin%5FPhysics%5F(3x4%5Fcropped).jpg>) — image intégrée, portrait officiel de la semaine du prix Nobel 2024. Photo: Arthur Petron, 08/12/2024, CC BY-SA 4.0.
- [John J. Hopfield, Lauréat du Prix Nobel de Physique 2024 1 (recadré)](<https://commons.wikimedia.org/wiki/File:John_J._Hopfield,_2024_Nobel_Prize_Laureate_in_Physics_1_(cropped).jpg>) — image intégrée, portrait officiel de la semaine du prix Nobel 2024. Photo: Arthur Petron, 08/12/2024, CC BY-SA 4.0.
- [TSMC Fab 5](https://commons.wikimedia.org/wiki/File:TSMC_Fab_5.jpg) — image intégrée, site réel de fabrication des puces AI à la usine Fab 5 de Hsinchu, TSMC. Photo: Wikimedia Commons (cache existant).

---

## Références

[^1]: [Tom's Hardware : Les légendes des semi-conducteurs se promènent sur un marché nocturne taïwanais](https://www.tomshardware.com/tech-industry/semiconductor-legends-take-a-stroll-in-a-taiwanese-night-market-nvidia-tsmc-mediatek-and-quanta-heads-seen-eating-dinner) — Reportage du marché nocturne de Ningxia le 29 mai 2024, montrant Huang Renxun, TSMC, Lin Bairi et Tsai Lixing dînant ensemble.

[^2]: [Taiwan News : Le PDG de Nvidia appelle Taïwan 'l'un des pays les plus importants au monde'](https://www.taiwannews.com.tw/news/5880054) — Déclaration publique de Jensen Huang à Taïwan le 30/05/2024.

[^3]: [Wikipedia : Jensen Huang](https://en.wikipedia.org/wiki/Jensen_Huang) — Biographie de Huang Renxun, né à Taipei en 1963, ayant passé son enfance à Tainan et immigré aux États-Unis à l'âge de neuf ans.

[^4]: [Klover.ai: TSMC AI Fabricating Dominance](https://www.klover.ai/tsmc-ai-fabricating-dominance-chip-manufacturing-leadership-ai-era/) — Tous les GPU avancés de NVIDIA (A100, H100, série Blackwell) sont fabriqués par TSMC. Voir

[^5]: [SQ Magazine : Statistiques des puces IA 2025](https://sqmagazine.co.uk/ai-chip-statistics/) — Source des données sur les parts de marché de la fonderie TSMC en 2025, à savoir 72 % ; voir également le reportage simultané de Motley Fool.

[^6]: [PatentPC : L'explosion du marché des puces IA](https://patentpc.com/blog/the-ai-chip-market-explosion-key-stats-on-nvidia-amd-and-intels-ai-dominance) — Source des données sur la part de marché des GPU IA de NVIDIA, soit 86%.

[^7]: [Tech-Now : Taïwan mène le changement mondial des serveurs d'IA, dépassant les iPhones en 2025](https://tech-now.io/en/blogs/taiwans-ai-server-revolution-how-foxconn-and-odms-redefined-global-tech-leadership-in-2025) — Données d'expédition mondiales de serveurs d'IA par Foxconn, Quanta et Wistron, soit 90%.

[^8]: [DigiTimes : Foxconn, Wistron et Quanta maintiendront un chiffre d'affaires d'un billion sur les serveurs IA en 2026](https://www.digitimes.com/news/a20260109PD249/revenue-ai-server-foxconn-wistron-quanta.html) — Rapport indiquant que le revenu annuel des trois ODM dépassera le trillion, et que les serveurs IA surpasseront l'électronique de consommation.

[^9]: [36Kr : Qui se partagera la capacité de production CoWoS en 2026 ?](https://eu.36kr.com/en/p/3580962946874242) — Données selon lesquelles NVIDIA nécessite 595 000 wafers de CoWoS, représentant 60% du marché mondial.

[^10]: [NVIDIA Newsroom : Foxconn construit une usine d'IA en partenariat avec Taïwan et NVIDIA](https://nvidianews.nvidia.com/news/foxconn-builds-ai-factory-in-partnership-with-taiwan-and-nvidia) — Projet d'usine IA de 100 MW à Kaohsiung ; voir également le reportage de CNBC sur la capacité électrique de 100 MW.

[^11]: [Site officiel du Laboratoire d'IA de Taïwan - À propos de nous](https://ailabs.tw/zh/關於我們/) — Présentation officielle de Du Yijin, qui a fondé PTT à l'Université Nationale de Taiwan en 1995 et est revenu à Taïwan pour fonder Taiwan AI Labs en avril 2017.

[^12]: [TechNews - Nouvelles technologiques : Les talents IA sont-ils à Taïwan, doivent-ils rester ou partir ? Interview de Du Yijin, fondateur du Laboratoire d'IA de Taïwan](https://finance.technews.tw/2025/08/18/taiwan-ai-labs-ethan/) — Transcription de Ya Ting et présentation des projets clés tels que le médical par apprentissage fédéré.

[^13]: [Conseil exécutif : Améliorer l'infrastructure IA de Taïwan — créer un moteur de dialogue IA fiable TAIDE](https://www.ey.gov.tw/Page/5A8A0CB5B41DA11E/582206fe-26fc-4184-b911-aa6e4569ff3e) — Explication officielle du projet TAIDE en avril 2023.

[^14]: [Times Magazine : Quel est le rôle du premier grand modèle linguistique chinois traditionnel TAIDE pour 'prévenir l'invasion culturelle par l'IA' ?](https://www.cw.com.tw/article/5129076) — Article sur TAIDE, une discussion sur la subjectivité culturelle des LLM en chinois traditionnel.

[^15]: [Communiqué de presse du Conseil national de la science et de la technologie : TAIDE est un succès après un an, les entreprises publiques collaborent pour promouvoir un grand modèle linguistique avec une touche taïwanaise](https://www.nstc.gov.tw/folksonomy/detail/dd2d9d72-8f7b-44dd-976c-438d5ce683af?l=ch) — Sortie des versions commerciales TAIDE-LX-7B et académiques 13B en avril 2024.

[^16]: [CloudInsight : État du développement des LLM à Taïwan en 2026](https://cloudinsight.cc/en/blog/taiwan-llm) — Inventaire complet de l'écosystème des LLM taïwanais, tel que TAIDE 2.0 et Breeze-8B.

[^17]: Rapport CloudInsight mentionné ci-dessus. Détails des cas d'utilisation tels que le robot de dialogue Taïwanese de Chung-Hsing University « Shennong TAIDE », le robot de conversation taïwanais de National Taiwan University et le modèle TAIDE en dialecte taïwanais de Yanyang University of Science and Technology.

[^18]: [CIO Taiwan : Visite des entreprises de cybersécurité à Taïwan — Ouyi Smart Technology](https://www.cio.com.tw/taiwanese-ahn-an-smart-technology/) — Détails sur l'inclusion d'Ouyi Smart dans le Gartner sept fois et sa validation par MITRE ATT&CK trois fois.

[^19]: [Site officiel d'Ouyi Smart : Roi de la cybersécurité IA lancé ! Ouyi Cyber est coté aujourd'hui](https://www.cycraft.com/news/taiwans-first-ai-cybersecurity-stock-20260205) — Communiqué de presse sur l'inscription à la bourse Innovation le 5 février 2026.

[^20]: [Conseil national pour la science et la technologie : Stratégie de recherche en IA](https://www.nstc.gov.tw/folksonomy/detail/dbf8da09-22be-4ef1-8294-8832fc6e8a26?l=ch) — Cadre politique incluant le budget de 40 milliards de NTD du premier plan d'action IA de Taïwan et la construction de TWCC.

[^N1]: [Communiqué de presse du prix Nobel de physique 2024](https://www.nobelprize.org/prizes/physics/2024/press-release/) — Annonce officielle par l'Académie royale suédoise le 8 octobre 2024. Texte original : « The Royal Swedish Academy of Sciences has decided to award the Nobel Prize in Physics 2024 to John J. Hopfield and Geoffrey Hinton 'for foundational discoveries and inventions that enable machine learning with artificial neural networks.' » Récompense de 11 millions de couronnes suédoises, partagée à parts égales entre les deux.

[^N2]: [Communiqué de presse du prix Nobel de chimie 2024](https://www.nobelprize.org/prizes/chemistry/2024/press-release/) — Annonce le 9 octobre 2024. Récompense de 11 millions de couronnes suédoises, David Baker reçoit la moitié « for computational protein design », et Demis Hassabis et John Jumper partagent l'autre moitié « for protein structure prediction ».

[^N3]: [PNAS, 79(8), 2554-2558](https://www.pnas.org/doi/10.1073/pnas.79.8.2554) — Hopfield, J. J. (1982). « Neural networks and physical systems with emergent collective computational abilities. »

[^N4]: [Nature, 323, 533-536](https://www.nature.com/articles/323533a0) — Rumelhart, D. E., Hinton, G. E., & Williams, R. J. (1986). « Learning representations by back-propagating errors. »

[^N5]: [NeurIPS 2012 / NIPS Proceedings](https://papers.nips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html) — Krizhevsky, A., Sutskever, I., & Hinton, G. E. (2012). « ImageNet Classification with Deep Convolutional Neural Networks. »

[^N6]: [PanSci Sciences Générales : Prix Nobel de physique 2024 — Hopfield et Hinton inaugurent l'ère de l'apprentissage automatique par réseaux neuronaux artificiels](https://pansci.asia/archives/378242) — Partenaire de curation de contenu selon le Mémorandum d'entente du 05/05/2026. Couvre le contexte de la proposition du réseau de Hopfield, l'analogie spin glass, l'accumulation des citations et le lien mathématique avec l'apprentissage profond contemporain.

[^N7]: [The Guardian : Le lauréat du prix Nobel de physique 2024 John Hopfield met en garde contre les dangers de l'IA](https://www.theguardian.com/science/2024/oct/08/nobel-prize-physics-2024-john-hopfield-geoffrey-hinton-ai-machine-learning) — Reportage d'un entretien téléphonique du prix Nobel de physique le 8 octobre 2024, où Hopfield et Hinton ont lancé des avertissements sur les risques de l'IA le même jour.

[^N8]: [Wikipedia : Geoffrey Hinton](https://en.wikipedia.org/wiki/Geoffrey_Hinton) — Hinton est né à Wombwell, Londres, le 6 décembre 1947, et a rejoint Google après que DNNresearch ait été racheté par Google pour 44 millions de dollars en mars 2013.

[^N9]: [BBC News: L'« parrain » de l'IA Geoffrey Hinton met en garde contre les dangers en quittant Google](https://www.bbc.com/news/world-us-canada-65452940) — Le 1er mai 2023, après avoir quitté Google, Hinton a exprimé ses préoccupations concernant les risques de l'IA à la BBC. Le texte original indique : « J'ai démissionné pour pouvoir parler des dangers de l'IA sans considérer comment cela affecte Google », et « une partie de moi regrette le travail de ma vie ». Les détails de l'interview du NYT sont également cités dans ce reportage.

[^N10]: [Nature : Le scientifique de l'IA Geoffrey Hinton remporte le prix Nobel de physique](https://www.nature.com/articles/d41586-024-03213-8) — Détails de la cérémonie de remise du prix Nobel de physique en 2024 et d'un appel téléphonique avec Hinton, tels que rapportés par Nature.

[^N11]: [Wikipedia : Histoire économique de Taïwan](https://en.wikipedia.org/wiki/Economic_history_of_Taiwan) — Données du PIB de Taïwan en 1986 ; le Parc scientifique de Hsinchu a été fondé en décembre 1980.

[^N12]: [Science, 181(4096), 223-230](https://www.science.org/doi/10.1126/science.181.4096.223) — Anfinsen, C. B. (1973). « Principles that govern the folding of protein chains. »

[^N13]: [Nature : « Cela va tout changer » : L'IA de DeepMind fait un bond gigantesque dans la résolution des structures protéiques](https://www.nature.com/articles/d41586-020-03348-4) — Rapport des résultats publiés à CASP14 le 30 novembre 2020, où AlphaFold 2 a obtenu une GDT médiane de 92,4, et John Moult, l'organisateur de CASP, a commenté : « d'une certaine manière, le problème est résolu ».

[^N14]: [DeepMind : AlphaFold révèle la structure de l'univers protéique](https://www.deepmind.com/blog/alphafold-reveals-the-structure-of-the-protein-universe) — Annonce du 28 juillet 2022 concernant la base de données des structures protéiques d'AlphaFold couvrant un million d'espèces et environ 200 millions de structures protéiques.

[^N15]: [Abramson, J., Adler, J., Dunger, J. et al. (2024). Accurate structure prediction of biomolecular interactions with AlphaFold 3. Nature 630, 493-500](https://www.nature.com/articles/s41586-024-07487-w) — AlphaFold 3 a été publié le 8 mai 2024, étendant la prédiction aux complexes protéine/ADN/ARN/ligand/ion.

[^N16]: [Wikipedia : Demis Hassabis](https://en.wikipedia.org/wiki/Demis_Hassabis) — Hassabis a commencé l'échecs à quatre ans, a co-développé Themed Park avec Peter Molyneux à l'âge de 17 ans (en 1994), a fondé DeepMind à Londres en 2010, et a été racheté par Google pour environ 400 millions de livres sterling en 2014.

[^N17]: [Centre de recherche génomique de l'Académie chinoise des sciences](https://www.genomics.sinica.edu.tw/) — Le centre de recherche sur les structures protéiques glycanes établi sous la direction du président Weng Chi-hui (2006-2016).

[^N18]: [PanSci Science : Prix Nobel de chimie 2024 — David Baker, Demis Hassabis, John Jumper résolvent le problème du repliement des protéines](https://pansci.asia/archives/378388) — Partenaire de curation de contenu selon l'accord du 5 mai 2026. Couvre la controverse AlphaFold pour le prix Nobel de chimie et les discussions sur les frontières disciplinaires entre la biologie structurale et la chimie computationnelle.

[^N19]: [PanSci Science : AlphaFold 3 prédit les interactions des protéines avec d'autres molécules, une mise à niveau du développement de médicaments](https://pansci.asia/archives/377917) — Partenaire de curation de contenu selon l'accord du 5 mai 2026. Analyse de l'impact en aval d'AlphaFold 3 sur le développement de médicaments et l'ingénierie des enzymes.

[^N20]: [PanSci Science : Le défi de l'IA « cerveau artificiel » OI — Les tissus cérébraux en boîte peuvent-ils remplacer les puces de silicium ?](https://pansci.asia/archives/366027) — Partenaire de curation de contenu selon l'accord du 5 mai 2026. Recherche sur le cerveau artificiel par l'équipe de Thomas Hartung à Johns Hopkins, comme une voie de calcul alternative à celle de l'IA.

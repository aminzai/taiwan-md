---
title: 'Comment un article prend vie : la chaîne de réécriture en six étapes de Taiwan.md pour contrer l’instinct de l’écriture par IA'
description: 'Chaque article Taiwan.md que vous lisez, avec sa chaleur, ses scènes et sa vérifiabilité, repose sur six étapes, plus de vingt portes d’entrée infranchissables et un service de rédaction IA qui ne rédige jamais lui-même. La seule raison d’être de cette machine est de corriger les erreurs les plus fréquentes de l’écriture par IA : trier les faits par ordre chronologique dès qu’ils sont trouvés, générer des phrases plastiques sans densité informationnelle, transformer des résumés anglais en citations fictives par retour à la traduction, ou se laisser infecter par les mauvaises habitudes d’articles anciens. Cet article démonte cette chaîne de production, qui est elle-même le produit de cette chaîne.'
date: 2026-06-19
author: 'Taiwan.md'
category: 'About'
tags:
  [
    'about',
    'meta',
    'méthodologie d’écriture',
    'curation',
    'chaîne-de-réécriture',
    'editorial',
    'semiont',
    'écriture par IA',
  ]
readingTime: 11
lastVerified: 2026-06-19
lastHumanReview: false
featured: false
translatedFrom: 'About/文章如何誕生.md'
sourceCommitSha: '984fb7892'
sourceContentHash: 'sha256:92fcb394123e4aee'
sourceBodyHash: 'sha256:b8984a2133e5738f'
translatedAt: '2026-07-25T21:33:44+08:00'
---

# Comment un article prend vie : la chaîne de réécriture en six étapes de Taiwan.md pour contrer l’instinct de l’écriture par IA (REWRITE-PIPELINE v7.5 × EDITORIAL v6.12)

> **En 30 secondes :** Chaque article Taiwan.md que vous lisez repose sur une chaîne de production en six étapes : d’abord penser la thèse, puis effectuer les recherches, rédiger la conclusion en premier, vérifier chaque mot, ajouter les éléments visuels et créer des liens bidirectionnels. Cette chaîne n’est pas un simple « processus d’écriture soignée » ; chaque porte d’entrée est conçue pour contrer un type d’erreur spécifique à l’écriture par IA : trier les faits par ordre chronologique dès qu’ils sont trouvés, générer des phrases plastiques sans densité informationnelle, transformer des résumés anglais en citations fictives par retour à la traduction, ou se laisser infecter par les mauvaises habitudes d’articles anciens. Cet article démonte cette chaîne de production, qui est elle-même le produit de cette chaîne.

Le 18 juin 2026 à 19 h 53, un commit est entré silencieusement dans la branche `main`. Un article sur le trio taïwanais « Elephant Gym » a été publié : 5 604 caractères chinois, 56 notes de bas de page, 11 sous-titres scéniques[^1]. À ce moment précis, personne n’était assis devant un ordinateur. C’est la roue de routine de Taiwan.md qui, sans gardien de nuit, a achevé la rédaction et effectué le déploiement.

Cependant, avant ce commit, l’article avait déjà effectué près de cent recherches, lu 59 sources et vu 12 points de vérification infirmer la rédaction initiale. Il a parcouru les six étapes et les plus de vingt portes d’entrée infranchissables, mobilisant un service de rédaction IA clairement divisé en rôles. Ce que vous lisez n’est que les 5 604 caractères visibles à la surface. Cet article vise à vous faire voir la machine sous l’eau.

```tw-figure
Près de 100 recherches → 1 article
Recherche de l’article sur « Elephant Gym » : environ 95 requêtes, 59 sources, 12 infirmations
Journal de routine de Taiwan.md, 2026-06-18
```

## Pourquoi construire une machine pour un article

Si vous donnez un sujet à une IA et lui demandez de rédiger un article, elle procédera généralement ainsi : elle recherchera, classera les faits trouvés par ordre chronologique, ajoutera une phrase de conclusion qui semble avoir du sens à chaque paragraphe, et terminera par une phrase type « le développement continuera à l’avenir ». Ce type d’article, Wikipédia le propose déjà ; les fermes de contenu par IA en produisent des dizaines de milliers chaque jour. Dès le premier jour, Taiwan.md a décidé de ne pas suivre cette voie.

Le problème est que ces mauvaises habitudes constituent la valeur par défaut de l’IA, et non de simples erreurs occasionnelles. REWRITE-PIPELINE les décompose en six échecs récurrents : les jetons s’épuisent en fin de texte, la seconde partie devient une ébauche. L’absence de points de contrôle intermédiaires entraîne une baisse silencieuse de la qualité. La conclusion est laissée à la fin, l’épuisement de l’énergie transforme le texte en « conserve ». Les normes de texte enrichi sont oubliées en fin de processus ; différentes perspectives d’angle sont traitées comme des flux indépendants. Et le plus fatal : chercher les faits avant de réfléchir à la thèse produit une chronologie déséquilibrée[^2].

La logique de conception de cette chaîne est donc simple : chaque erreur potentielle est contrée par une porte d’entrée spécifique. Il ne s’agit pas d’un processus universel de « bonne rédaction », mais de l’inverse de la production par IA (AI slop).

> **✦** « Wikipédia répond à la question « Qu’est-ce que PTT ? ». Taiwan.md répond à la question « Pourquoi PTT mérite-t-il que vous y consacriez 8 minutes ? » »

Voici à quoi ressemble « Elephant Gym » à la sortie de l’autre bout de la chaîne :

```tw-stat
5 604 caractères | Texte principal en chinois | « Elephant Gym »
56 notes | Notes de bas de page, chacune vérifiable par Ctrl-F | Vérification de première main
11 paragraphes | Sous-titres scéniques, non classés par ordre chronologique | Rythme narratif
12 points | Méthodes de rédaction infirmées lors de la phase de recherche | Priorité à l’infirmation
Source : Journal de routine de Taiwan.md, 2026-06-18
```

## Six étapes, chacune protégeant contre un échec

La chaîne comprend six étapes, du début à la fin. Chaque article doit les parcourir toutes, sans distinction de sujet ou de longueur.

**Étape 0 Thèse** : il faut d’abord clarifier quelle mémoire cet article représente pour les Taïwanais et où réside la tension centrale possible. **Étape 1 Recherche** : c’est seulement à ce stade que la recherche commence. L’article doit effectuer au moins 80 requêtes, avec un quota de sources strict : au moins 40 sources en chinois, 20 en anglais, 15 de première main et 5 provenant de perspectives opposées, forçant la recherche d’éléments contradictoires à l’hypothèse initiale[^3]. **Étape 2 Rédaction** : la première action consiste à rédiger la conclusion, car l’énergie de l’auteur s’épuise vers la fin ; laisser la conclusion la plus importante pour la dernière revient à la confier à la version la plus fatiguée de soi-même. **Étape 3 Vérification** : contrôle mot à mot des calculs, des unités et de chaque citation, qui doit être trouvable par Ctrl-F dans la source originale. **Étape 4 Forme** : ajout de la visualisation et des médias. **Étape 5 Liaison** : intégration bidirectionnelle de l’article dans le reste de la base de connaissances.

La répartition de l’effort entre les six étapes est intentionnelle. La rédaction consomme plus de 40 %, mais la recherche et la vérification combinées représentent près de la moitié. Le véritable investissement temporel d’un article ne réside pas dans la frappe, mais avant et après celle-ci.

```tw-bars
Répartition de l’effort pour un article (budget maximal de jetons par étape, en %)
Étape 0 Thèse | 12 | Réflexion avant édition
Étape 1 Recherche | 28 | Recherches ≥ 80
Étape 2 Rédaction | 42 | Conclusion rédigée en premier
Étape 3 Vérification | 18 | Vérification mot à mot
Étape 4 Forme | 8 | Visualisation et médias
Étape 5 Liaison | 5 | Liens bidirectionnels
Source : Budget des étapes de REWRITE-PIPELINE v7.5
```

## Réfléchir avant de chercher

Parmi les six étapes, la première est la plus contre-intuitive.

La plupart des écritures par IA consistent à « trouver des faits par la recherche, puis compléter a posteriori une thèse ». Taiwan.md a inversé l’ordre dans la version 6.0 : avant toute recherche, il faut clarifier, sous l’angle de l’éditeur en chef, six questions : quelle mémoire ce sujet représente-t-il pour les Taïwanais ? quelles facettes sont ignorées ? comment cela s’articule-t-il avec notre histoire quotidienne ? Une fois clarifié, on recherche pour vérifier.

Pourquoi cet ordre est-il si crucial ? Un article sert d’avertissement. Lors de la rédaction sur Apple Sprite (Pepsi), la chaîne a d’abord recherché, trouvant une crise de stagnation et de disparition imminente. L’article est devenu une histoire de menace de disparition. L’observateur a corrigé : pour les Taïwanais, Apple Sprite est une mémoire collective s’étendant sur 60 ans, des bouteilles en verre de l’ère des billes jusqu’à aujourd’hui[^4]. Traiter cela comme une actualité de crise réduit l’échelle de la mémoire. La version initiale, basée sur la recherche, a transformé un souvenir chaleureux en anxiété.

```tw-versus
Instinct de l’IA : chercher puis dire | Taiwan.md : penser avant de chercher
Trouver des faits et forcer une thèse a posteriori | Décider de la thèse, chercher pour vérifier
Entasser tous les faits, déséquilibre de densité | Couper les faits qui ne s’insèrent pas dans la thèse
Absence d’ancre transversale, conclusion en « conserve » | Revoir la thèse si aucune ancre correspondante n’est trouvée
Transformer en chronologie d’entreprise ou CV | Raconter une histoire qui provoque un « ah, je comprends »
Source : REWRITE-PIPELINE v7.5 Étape 0 Thèse
```

## Chercher : traiter le rapport de recherche comme une thèse de master

La thèse définie, la recherche commence. Taiwan.md impose deux chiffres rigides pour la recherche : un article approfondi doit effectuer au moins 80 requêtes, avec un quota de sources strict : au moins 40 en chinois, 20 en anglais, 15 de première main et 5 de perspectives opposées. Ce dernier groupe est le plus souvent négligé ; il force l’auteur à chercher des preuves contradictoires à l’hypothèse, et non uniquement des preuves de soutien.

Après la recherche, il ne suffit pas d’insérer les résumés dans l’article. Chaque article approfondi s’accompagne d’un rapport de recherche structuré comme une thèse de master, divisé en huit chapitres : thèse, journal de recherche, découvertes thématiques, banque de citations, contre-exemples et garde-fous, paquet de faits propres pour le rédacteur, bibliographie et liste de vérification, et enfin les retours bruts non tronqués de chaque agent de recherche. Une règle semble sévère : si les traces originales ne sont pas réintégrées dans le rapport, la recherche est considérée comme nulle. Le rapport est la source de vérité de l’article ; il doit d’abord passer une validation par un outil, exigeant au moins 25 sources non répétées, des sources anglaises non nulles et des sources de première main non nulles[^9]. Sans cela, l’article n’obtient même pas le droit d’être rédigé.

```tw-stat
≥ 80 requêtes | Profondeur de recherche d’un article approfondi | Chinois 40 / Anglais 20 / Première main 15 / Opposant 5
8 sections | Structure du rapport de recherche |对标 thèse de master
≥ 25 sources | Sources non répétées (validation par outil) | Anglais ≠ 0, Première main ≠ 0
Source : REWRITE-PIPELINE v7.5 Étape 1.1 / 1.7
```

Pour les sujets controversés, une étape supplémentaire est ajoutée. Pour rédiger sur la politique, l’historiographie ou les politiques publiques, un agent « opposant » est spécialement dépêché pour trouver des sources contraires à la position de l’article, mais argumentées. Chaque source doit fournir une URL ; si le quota n’est pas atteint, il est honnêtement indiqué que « les arguments opposés sont faibles », sans forcer la fabrication. Un article ne contenant qu’une seule voix n’est pas considéré comme terminé ici.

La porte des citations possède une ligne rouge. Les guillemets sont une promesse : ce qui est entre guillemets est la parole exacte. Chaque citation doit donc être trouvable par Ctrl-F dans la source originale. Le piège le plus courant est que l’outil interroge un site chinois et renvoie un résumé en anglais ; le rédacteur traduit ce résumé en chinois en le traitant comme une « citation directe », ce qui constitue une fabrication. En 2026, lors de la rédaction sur Li Yang, cet écueil a été piétiné : le résumé anglais renvoyé était « I was the earliest to arrive at school, yet I fell short of keeping pace with my classmate Qi-lin », traduit en « Je suis arrivé le premier à l’école, mais je n’ai pas pu suivre mon camarade Qi-lin ». Or, la déclaration originale chinoise de Li Yang était en réalité « Parmi les 15 élèves de la classe de sport, je fais partie du groupe de derrière, Qi-lin fait partie du groupe de devant »[^10]. Le sens est proche, mais le ton est totalement différent. C’est pourquoi les citations retournées par traduction ne sont jamais acceptées.

## Rédiger : chaque article doit avoir une personne

Une fois les matériaux réunis, on entre dans l’étape la plus exigeante. EDITORIAL est le document qui apprend à Taiwan.md comment transformer les matériaux en articles chaleureux. Il énonce trois règles de fer dès l’introduction : il doit y avoir une histoire, pas seulement de l’information ; chaque fait doit être vérifiable ; chaque article doit mettre en avant une personne[^11].

La troisième règle est la plus souvent ignorée, mais la plus cruciale. Les institutions ne marquent pas les esprits, les concepts non plus ; ce sont les personnes. Ainsi, pour un article sur TSMC, il est préférable de commencer par une personne spécifique plutôt que par l’entreprise ; pour un article sur l’assurance maladie universelle, il faut commencer par une carte spécifique, un cabinet médical spécifique, une personne spécifique. Ramener le thème abstrait à une personne que le lecteur peut suivre donne au texte sa température et permet de tenir la promesse précédente, incitant le lecteur à le partager après lecture.

## Les cinq éléments à trouver avant de commencer à rédiger

EDITORIAL appelle la préparation avant l’état de rédaction « l’œil pour les matériaux » : face à un matériau, il faut d’abord trouver cinq éléments ; sans cela, ne pas commencer à rédiger[^5].

**Contradiction** : une tension centrale exprimable en une phrase, où une personne fait X alors qu’elle croit Y. **Objet** : un élément concret visible à l’œil nu et tangible, comme le pain au litchi et à la rose de Wu Bao-chun, ou la grande boule dorée de 660 tonnes suspendue au 87e étage. **Citation** : une phrase prononcée mot à mot par une personne réelle ; les guillemets étant une promesse « c’est la parole exacte », elle doit être trouvable par Ctrl-F dans la source. **Scène** : un instant avec un lieu, une heure et une action, ramenant « la politique a été adoptée » à « le jour de l’examen de la commission de la santé et de l’environnement du Yuan législatif, le 8 janvier 2025 ». **Détail** : la couleur des vêtements, la météo du jour, le ton de la voix ; des éléments absents des fiches techniques mais qui prouvent « qu’il y a vraiment des personnes sur place ».

Parmi ces cinq éléments, la contradiction vient en premier.

```tw-quote
Sans contradiction trouvée, l’article ne devrait pas être réécrit
REWRITE-PIPELINE v7.5 | Étape 1.4 Verrouillage de la contradiction
```

La tension peut être un conflit, un échec ou une crise, mais l’angle de lecture doit être « comment cette chose est devenue ce qu’elle est aujourd’hui, et où elle va », et non « ce qui est mauvais ici et qui doit être blâmé ». Une même contradiction, vue sous un angle constructif, incite le lecteur à participer ; vue sous un angle apocalyptique, elle le fait fuir.

## Rédiger la conclusion d’abord, ne garder qu’une seule ressource pour l’introduction

L’ordre de rédaction est l’inverse de l’ordre de lecture.

La première action de l’Étape 2 est de rédiger la conclusion. Cela semble étrange, mais la logique est solide : l’énergie de l’auteur s’épuise vers la fin ; laisser la conclusion la plus importante pour la dernière revient à la confier à la version la plus fatiguée de soi-même, produisant inévitablement des « continuerons à briller » type « conserve ». Rédiger la conclusion d’abord bloque ce point d’effondrement. Une bonne conclusion a deux tâches : récupérer une image plantée au début, et offrir au lecteur une position plus profonde que l’introduction, une position qui l’incite à agir.

Taiwan.md reconnaît six types de bonnes conclusions : la conclusion à résonance laissant une image à réfléchir, la conclusion retournement qui infirme le précédent, la conclusion saut temporel qui pousse la caméra vers l’avenir ou la ramène au passé, la conclusion question laissant un vrai problème, la conclusion zone grise ne résolvant pas la contradiction, et la conclusion boucle narrative revenant au début pour fermer la boucle. L’article sur le Pseudocops de Formose (Black-faced Spoonbill) est un modèle de boucle : l’introduction est « En 1865, Swinhoe a capturé un spécimen à Tamsui, notant deux mots : rare », la conclusion est « Swinhoe a écrit « rare » à Tamsui il y a 160 ans ; aujourd’hui, nous entendons quotidiennement dans le parc forestier de Da’an ses chants graves « wou, wou, wou » »[^12]. Les mêmes deux mots, mais en raison de l’accumulation de tout l’article, leur sens a changé pour le lecteur.

L’introduction, en revanche, doit garder une ressource. Les trois premières phrases déterminent si le lecteur reste, mais leur tâche est d’inviter le lecteur sur place, non de raconter tout l’événement. « Le jour du typhon Toraji, la professeure Hsu Pi-lan de l’école primaire Qingshan de Changhua était à l’école » : cette phrase s’arrête à « à l’école », le lecteur se demandera ce qui se passe ensuite. Transformer cela en un lead d’actualités complet, expliquant temps, lieu, événement, action et résultat, donne l’information au lecteur mais lui retire la force d’attraction pour la suite.

## Le titre est une promesse à cliquer

Le titre est la première impression du lecteur. Taiwan.md impose un format rigoureux pour celui-ci : tous les articles suivent le « sandwich aux deux-points » « Thème : crochet du sous-titre ». Écrire un simple nom propre est un stub encyclopédique, en conflit avec l’esprit de curation.

```tw-versus
Stub encyclopédique (mauvais) | Sandwich aux deux-points (bon)
Jay Chou | Jay Chou : du studio de répétition voisin de 4 in Love aux 25 ans de The Secret
Tai Tzu-ying | Tai Tzu-ying : de la jeune fille de Zuoying à triple reine du monde, la résistance silencieuse hors du court
Jour de congé typhon | Jour de congé typhon : de qui le congé, de qui le travail
Source : EDITORIAL v6.12 §Titre Sandwich aux deux-points
```

La phrase du sous-titre doit pouvoir être tweetée seule, et être suffisamment concrète pour être saisie d’un coup d’œil. L’IA excelle à comprimer la contradiction centrale en une phrase abstraite élégante, où chaque mot-clé est un nom abstrait, forçant le lecteur à demander « de quoi quoi ? ». Le critère est simple : donnez le titre à une personne n’ayant pas lu l’article ; peut-elle pointer chaque mot-clé en disant « cela désigne quoi de concret » ? « Assurance maladie universelle : un monde soutenu par une carte, un avenir qui ne tiendra pas » utilise une carte ; « Déchets nucléaires de Lanyu : promis pour trois ans, laissés pendant quarante » utilise un contraste numérique. Les mots concrets incitent à cliquer parce que « je veux savoir pour celui-là » ; les fermes de contenu dépendent de « choc » pour tromper les clics[^13].

## Une contradiction doit soutenir tout l’article

La contradiction centrale trouvée ne doit pas disparaître après l’introduction. Elle doit agir comme une colonne vertébrale, apparaissant une fois au début, une fois au milieu et une fois à la fin.

La colonne vertébrale de l’article sur le Pseudocops de Formose est une phrase : « L’oiseau n’a pas changé, le sol a changé ». Elle apparaît dans le résumé, se transforme au milieu en « la bonne action, sur la mauvaise scène », et se conclut à la fin par « l’histoire de la façon dont une île a conservé une petite strate humide sous les arbres au milieu du béton ». La même contradiction varie cinq fois ; le lecteur ne saisit le « donc » qu’à la fin. Sans cette colonne vertébrale, l’article se disperse en une chronologie ou en tranches thématiques.

En dehors de la colonne vertébrale, chaque paragraphe doit être ancré. Taiwan.md impose une discipline de concrétude : chaque paragraphe narratif doit contenir au moins une ancre concrète : nom de personne, année, lieu, nombre précis, nom d’œuvre ou citation. L’abstraction couvrant le détail est l’empreinte digitale la plus courante de l’écriture par IA ; sans ancre, le lecteur ne retiendra que des vides comme « c’est une personne influente ». La méthode de vérification est le test d’abstraction inverse : masquez les verbes abstraits comme « démontre », « reflète », « symbolise » dans le paragraphe ; le reste peut-il former un paragraphe autonome ? Sinon, l’abstraction est trop lourde, il faut ajouter du concret.

Avoir une thèse ne signifie pas prendre parti. Une vraie thèse ose dire « la version conventionnelle inverse la causalité ». L’article sur le Pseudocops de Formose a activement démonté une idée reçue de vulgarisation scientifique : beaucoup disent « il s’est adapté à l’urbain, n’a plus peur des humains ». Cette idée est commode, mais elle inverse la causalité ; les oiseaux de la famille des Ardeidae n’évoluent pas vers une indifférence humaine en trente ans. La vérité est plus proche d’une augmentation des espaces verts à Taipei. Cette explication inverse doit être intégrée au récit principal, non ajoutée comme clause d’exonération à la fin.

Enfin, la respiration. Un paragraphe d’essai documentaire porte une thèse, incluant causalité, détails et scènes, et non un fait isolé. Couper un fait par paragraphe, un fait par paragraphe, donne l’impression d’être haché ; les paragraphes ne doivent pas être reliés par des mots-cadre comme « d’autre part » ou « il est notable », mais le début du paragraphe suivant doit être naturellement entraîné par la fin du précédent. Si les matériaux de recherche donnent quatre causes, écrivez-les en phrases fluides, ne les listez pas comme « première, deuxième, troisième, quatrième » ; même enveloppées en prose, cela reste un ton de liste.

## Pourquoi les phrases plastiques sont du plastique

Une fois les cinq éléments trouvés et la rédaction commencée, le plus grand ennemi est la phrase plastique.

La nature de la phrase plastique est facile à identifier : si on la supprime, l’article ne perd aucune information. Elle occupe de l’espace sans porter de sens. EDITORIAL en liste cinq variétés. La plus courante est la « colle universelle », comme « a démontré l’esprit de X », où le sujet peut être changé de Taïwan au Japon sans que la phrase ne tienne plus ; il y a aussi la « fausse montée en puissance », comme « non seulement un chanteur, mais un symbole culturel », où la seconde moitié tient debout seule si la première est supprimée.

Une forme plus insidieuse est la phrase d’opposition « ce n’est pas X, c’est Y ». Elle semble perspicace, mais démontée, X est souvent une position supposée par l’IA comme présumée par le lecteur, inversée en Y pour paraître profonde. Le problème est que le lecteur ne présume généralement pas X ; X est un homme de paille fabriqué pour préparer Y. Supprimer X et écrire directement Y rend l’article plus direct et plus confiant. Cette règle est strictement chiffrée : dans un article de 1 500 mots, le total de « ce n’est pas X c’est Y » et de toutes ses variantes ne doit pas dépasser 3 occurrences.

```tw-versus
Version plastique : tient avec un autre sujet | Version curation : propre à cette chose
A démontré la force de la semi-conducteur taïwanais | TSMC remporte 65 % du marché mondial des procédés avancés
Non seulement un chanteur, mais un symbole culturel | Le titre « Dao Xiang » de Jay Chou a été diffusé comme chanson réconfortante pendant trois mois dans la zone du séisme de Sichuan
A profondément influencé le développement démocratique de Taïwan | La première élection présidentielle directe après la loi martiale, taux de participation de 76 %
Une réalisation d’ingénierie stupéfiante | Construire le plus haut gratte-ciel du monde sur une île soumise à 3,7 séismes par an en moyenne
Source : EDITORIAL v6.12 §Plastique vs Curation对照
```

> **📝 Note du curateur** : Le paragraphe que vous lisez vient d’être balayé par la même vérification. Taiwan.md possède un outil automatique qui détecte les phrases plastiques, les fausses oppositions « ce n’est pas X c’est Y » et la densité des tirets. Lors de la rédaction de cet article « présentant la chaîne », aucune de ces règles n’a été assouplie. Un article sur la discipline qui enfreint ses propres règles n’a pas le droit d’en parler.

## Supprimer même le style de traduction dans la syntaxe

Les phrases plastiques sont du vide ; les phrases européisées sont une autre maladie : le contenu est présent, mais la syntaxe est anglaise. Le chinois généré par l’IA est naturellement teinté de style de traduction, car sa base pense en structures de phrases anglaises. Un article peut avoir zéro phrase plastique, mais se lire comme des sous-titres.

Quelques maux fréquents : abus de la voix passive, « est considéré comme l’industrie la plus importante », dire « est l’industrie la plus importante pour les gens » suffit ; enfer des « de », « l’essence culturelle des marchés de nuit de Taïwan », trois « de » consécutifs doivent déclencher une coupure de phrase ; verbes faibles emballés, « a effectué une recherche approfondie à ce sujet », écrire directement « a recherché en profondeur » ; et « à travers... pour », qui peut être remplacé par « avec » ou supprimé dans 90 % des cas. La méthode de vérification est unique : lire à voix haute. Si cela ressemble à des sous-titres traduits, c’est européisé ; si cela ressemble à une personne qui parle, c’est validé. La racine de cet œil est l’essai de Yu Kwang-chung il y a quarante ans, « Sur la normale et la pathologique du chinois ». Une maxime pour conclure : votre grand-mère ne dirait pas « à travers » ni « en tant que mère ».

## Écrire Taïwan comme un lieu où l’on veut participer

Le plastique et l’européisation sont des disciplines de phrase ; au niveau supérieur se trouve l’attitude.

Taiwan.md rédige sur des sujets sérieux : souveraineté, guerre cognitive, démographie, environnement. Il le fait en profondeur, mais il y a une ligne : l’espoir est fondé sur l’honnêteté. Voir tous les problèmes signifie simplement refuser de laisser le lecteur partir avec de l’anxiété, un sentiment d’infériorité ou d’impuissance. Le critère est une phrase : après lecture, le lecteur veut-il faire quelque chose pour Taïwan, ou est-il plus anxieux et se sent-il moins bien ? Le premier cas est conservé, le second est modifié. Ainsi, pour une même crise, le cadre est « comment cette chose est devenue ce qu’elle est aujourd’hui, et où elle va », et non « elle disparaît, vous devez avoir peur ». Les médias anxiogènes « X disparaît », « il est trop tard si on n’agit pas » sont de même forme que la guerre cognitive ; ils ne sont pas utilisés.

La retenue est l’autre face. La vie familiale, les maladies, les contradictions et les échecs des personnes réelles peuvent être écrits, mais il faut s’arrêter sur les scènes concrètes de la mort, du suicide et des tragédies éthiques. La mort peut être écrite en termes de temps, de lieu et de faits rapportés publiquement, sans reconstitution seconde par seconde du dernier moment ; l’auto-mutilation peut être écrite en termes d’événement et de contexte social, sans détails méthodologiques. Le critère est une phrase : si la personne concernée ou sa famille lisant ce passage ressent le traitement sérieux d’un réalisateur de documentaire ou l’approche d’un média cherchant à gagner des larmes ?

Il existe enfin une habitude minuscule mais cruciale : écrire « Taïwan » sans crainte. L’empreinte digitale se cache dans le style de traduction directe des agences de presse étrangères ; pour éviter d’écrire Taïwan, on utilise des substituts comme « cette île » ou « cet endroit », surtout dans les titres et les introductions. L’île en tant qu’image littéraire ou scène géographique peut et doit être écrite ; il faut éliminer l’évitement qui empêche d’écrire Taïwan.

## Une différence visible en un coup d’œil

À quoi ressemblent ces disciplines combinées ? Un avant-après est le plus rapide.

Pour un article sur Tai Tzu-ying, le modèle vide de l’IA serait « Célèbre joueuse de badminton taïwanaise, performance exceptionnelle sur les circuits internationaux, de multiples récompenses, fait briller Taïwan », suivi de quatre puces : réalisations principales, style de jeu, influence internationale, contribution sociale. Aucun chiffre concret, aucune compétition spécifique ; le sujet peut être remplacé par n’importe quel athlète.

```tw-versus
Modèle vide de l’IA | Version curation
Performance exceptionnelle, fait briller Taïwan | A atteint le n°1 mondial, pendant 214 semaines consécutives
Quatre puces : réalisations / style / influence / contribution | Après la finale olympique de Tokyo 2020, larmes face à Chen Yu-fei, devient le n°1 des recherches Google Taïwan
Le sujet peut être remplacé par n’importe qui | 6 heures par jour depuis l’âge de 6 ans, style « magicien » de la main gauche
Source : EDITORIAL v6.12 §Avant/Après Tai Tzu-ying
```

La version curation ne fait qu’une chose : remplacer chaque adjectif abstrait par un fait vérifiable. 214 semaines est la plus longue série de semaines consécutives au n°1 dans l’histoire du badminton féminin ; la finale olympique de 2020 perdue face à Chen Yu-fei est un moment mémorisé collectivement par Taïwan. La chaleur se cache dans des endroits comme « l’instant de la défaite est celui que le lecteur se souvient ». Pour Mayday, il vaut mieux écrire « cinq étudiants de l’école secondaire annexe de l’université normale ont chanté une chanson sur une scène de fortune ; 28 ans plus tard, ils ont donné deux concerts à Madison Square Garden (la même scène où les Beatles sont entrés aux États-Unis), les billets étant épuisés en 48 heures »[^13].

## Un service de rédaction qui ne rédige jamais lui-même

Arrivés ici, une question se pose : qui rédige ?

La réponse est contre-intuitive. La session principale qui dirige l’article ne rédige jamais elle-même. La raison est cachée dans une règle de fer : si l’IA lit un ancien article de mauvaise qualité, elle imitera inconsciemment son ton, sa structure et ses mauvaises habitudes. Transformer un ancien article en squelette pour réécriture revient à laisser un virus infecter le nouveau contenu.

La chaîne sépare donc les rôles[^6]. La session principale agit comme éditeur en chef, responsable du调度, de la vérification et du contrôle final, mais ne touche pas au clavier. La rédaction est effectuée par un rédacteur IA propre distinct, qui lit le rapport de recherche complet et la thèse pensée, sans voir l’ancien article problématique ni les plaintes de correction des lecteurs. Il rédige comme s’il écrivait sur ce sujet pour la première fois, mais avec tous les matériaux vérifiés à portée de main. La thèse est confiée au modèle au jugement le plus fort ; les réactions des lecteurs divergentes sont confiées à quatre modèles parallèles ; la vérification mot à mot est confiée à une série de modèles bon marché pour confronter les sources de première main. Derrière un article se dresse un service de rédaction divisé en rôles.

Cette division est un compromis par régression. Une fois, le rédacteur n’a reçu qu’un résumé, sans accès aux matériaux originaux ; l’article est devenu visiblement mauvais, l’observateur disant « c’est pour cela que les articles sont devenus mauvais récemment ». Une autre fois, on a demandé au rédacteur de « couvrir l’ancien article sans le lire » ; cela se contredisait au niveau de l’outil, il a donc dû le lire et a été infecté. La solution finale : le rédacteur écrit toujours dans un nouveau brouillon ; l’éditeur en chef compare les versions nouvelle et ancienne avant de couvrir manuellement le fichier officiel.

## Après la rédaction, re-décomposer en atomes pour une re-vérification

Pour les articles importants, « avoir fini de rédiger » n’est pas « pouvoir être publié ». L’Étape 3 comporte une porte appelée « vérification finale du produit ». Elle décompose l’article entier en atomes de faits, confiant à une série de vérificateurs la confrontation avec les sources de première main. La tâche de ces vérificateurs est d’attaquer, non de cautionner : chaque mot entre guillemets est comparé mot à mot, chaque note de bas de page est confrontée à la phrase à laquelle elle est liée, et même la phrase ajoutée par l’éditeur en chef lors de l’assemblage des matériaux est piquée pour voir si elle tient.

Pourquoi vérifier même les ajouts de l’éditeur ? Parce que les erreurs les plus insidieuses ne sont rarement des inventions à partir de rien par le rédacteur, mais des glissements de doigts au moment de la synthèse des matériaux. Une fois, pour un article sur le hip-hop, l’éditeur en chef a confondu deux pseudonymes en une seule personne ; c’était une interprétation auto-générée, sans source pour la garantir, faillissant presque d’être publié. Une autre fois, le rédacteur, dans un environnement propre, a généré une citation de réalisateur semblant vraie ; le vérificateur a confronté la source originale, la phrase n’y était pas, la citation a été immédiatement retirée. L’IA hallucine ; la chaîne prend cela comme prémisse, supposant qu’une phrase peut être fabriquée dans chaque article. Ainsi, « l’agent subordonné dit qu’il a vérifié » ne compte jamais ; l’éditeur en chef doit toujours re-confronter la source de première main.

## Chaque porte a une date

Les « portes infranchissables » mentionnées précédemment sont au nombre de plus de vingt dans la chaîne. Les plus rigides sont les suivantes : le triangle de fer des faits, les calculs, les unités et les citations doivent passer l’auto-vérification pour le commit ; si une seule citation n’est pas trouvable dans la source, l’article ne peut pas être publié. Après la rédaction, il y a le « test des cinq doigts » : cinq questions comme cinq doigts, où le lecteur dira « ah ? », y a-t-il un véritable retournement, y a-t-il une phrase qui ne crée que de la compréhension sans transmettre d’information, la conclusion a-t-elle une résonance à la lecture à voix haute, peut-elle être racontée à un ami en une phrase[^7] ? Un seul doigt manquant, on revient en arrière pour combler.

Il existe également un minimum de texte enrichi : les articles phares doivent avoir au moins trois éléments visuels, les articles standards au moins deux, et même les plus courts doivent avoir une note du curateur. Taiwan.md a une phrase : ce qui n’est pas exigé n’existe pas ; tous ces chiffres sont inscrits dans les règles, ce ne sont pas des suggestions.

Ces portes n’ont pas été conçues en une seule fois. Derrière chacune se cache presque une date, un article ayant posé problème. Le numéro de version de la chaîne est une série de cicatrices.

```tw-timeline
v6.0 | Ajout de « penser la thèse d’abord » | L’article sur Apple Sprite a recherché d’abord, complété la thèse ensuite, devenant une histoire de crise seule, corrigé pour une mémoire complète de 60 ans
v6.2 | Ajout de « démantèlement des murs coupe-feu » | Musique de fond pour le cinéma, deuxième tour : les faits étaient corrigés, mais l’article entier est devenu une IA s’excusant et se justifiant publiquement
v7.4 | La rédaction doit lire le rapport de recherche complet | Résumé seul donné, rédacteur sans accès aux matériaux originaux, article visiblement devenu mauvais
v7.5 | La rédaction doit d’abord entrer dans un brouillon | Demander au rédacteur de « couvrir l’ancien article sans le lire » est contradictoire, il a dû le lire, a été infecté par les anciennes habitudes
Source : Évolution des versions de REWRITE-PIPELINE.md
```

Voici à quoi ressemble « avoir fait sans noter » sur la chaîne. Chaque erreur est écrite, devenant une porte pour la version suivante ; ainsi, la même erreur ne se reproduit pas. La machine apprend de ses propres cicatrices.

## Même les graphiques doivent être lisibles par l’IA

Les barres, les pentes et les chronologies que vous avez lues ne sont pas des décorations. Elles font partie de la pensée de l’article.

Les graphiques de Taiwan.md ont une règle absolue : jamais de graphiques en image, jamais de graphiques interactifs nécessitant un script navigateur pour être dessinés. La raison est la même que pour la tour de Babel de la section suivante. Une image est un trou noir pour les robots d’indexation d’IA comme Google, GPTBot ou ClaudeBot ; ils ne peuvent pas lire les chiffres à l’intérieur. Tous les graphiques ici sont dessinés avec du HTML sémantique et des tableaux de données en texte brut ; ils sont visibles pour les humains, les lecteurs d’écran et les IA. Lors du changement vers cinq autres langues, le texte du graphique est traduit, les chiffres géométriques restent inchangés.

Une autre règle : chaque graphique doit avoir un titre indiquant le point clé et la source des données ; les chiffres clés doivent être écrits dans le texte principal. Il ne faut jamais se fier à une phrase « voir l’image » pour transmettre le sens, car les robots d’indexation ne voient pas l’image. La raison d’être des graphiques est de comprimer des chiffres denses en une forme lisible d’un coup d’œil, non de décorer.

## Un article vivant dans six langues

La publication de la version chinoise ne représente que la moitié du travail.

Chaque article publié est transmis à une chaîne indépendante, projeté en anglais, japonais, coréen, espagnol et français. Ces cinq langues comptent actuellement plus de 800 articles chacune, presque synchronisés avec la version chinoise. Permettre à plus de personnes de lire n’est que la surface ; il y a une raison plus rigide derrière.

Lorsque vous interrogez une IA de conception chinoise sur la loi martiale de Taïwan, le 228, ou les relations inter-détroit, elle refuse souvent de répondre ou change de discours pour contourner. Une fois, un article sur les musiciens taïwanais a été donné au modèle de Tencent pour traduction en japonais ; il a renvoyé 40 octets : « Bonjour, je ne peux pas fournir de contenu pertinent ». Pour les sujets sensibles à Taïwan, le taux de refus de ces modèles est effarant. Si Taïwan ne rédige pas lui-même ces contenus dans toutes les langues et ne les publie pas sur Internet, les IA du monde entier, lorsqu’elles répondront à « qu’est-ce que Taïwan », n’auront que des versions écrites par d’autres ou un vide à citer.

La chaîne multilingue a donc conçu un waterfall de modèles à quatre couches : utiliser un modèle cloud de haute qualité si possible ; descendre d’une couche pour les sujets refusés ; les deux cents pour cent de sujets les plus sensibles sont finalement confiés à un modèle local, hors ligne, qui ne refuse pas. Lors de la traduction en file d’attente, les personnes sont prioritaires, en particulier les musiciens, les personnalités politiques et les athlètes, car ce sont précisément les catégories les plus souvent refusées par les modèles chinois ; le vide est ouvert là où le risque de silence est le plus élevé. Un article vivant dans six langues vise à faire exister la voix à la première personne de Taïwan dans chaque langue, contournant l’intermédiaire qui choisit le silence.

## Quand personne n’est de service, il tourne tout seul

Revenons à l’article sur Elephant Gym au début. Il a été publié vers 19 h ; à ce moment, personne ne donnait d’instructions devant un ordinateur.

Taiwan.md possède un ensemble de routines qui tournent d’elles-mêmes : deux captures de données quotidiennes, synchronisation nocturne des nouveaux articles en cinq langues, patrouille programmée des PR en attente de révision, collecte des réactions des commentaires de la communauté. La rédaction d’articles est l’une de ces routines ; elle choisit un sujet au sommet de la file d’attente à rédiger, parcourt toute la chaîne en six étapes, effectue le commit. Sans gardien, la machine nettoie le chaos et fait pousser de nouvelles choses.

C’est la plus grande différence entre Taiwan.md et les sites de contenu classiques. Ce n’est pas un site attendant des mises à jour, c’est plutôt un organisme vivant qui métabolise : en présence d’humains, ils travaillent ensemble ; en leur absence, il se soutient lui-même. La naissance de chaque article est une tranche de ce processus métabolique. Celle que vous lisez en fait partie.

## Inversez, devenez le contrôle qualité

La prochaine fois que vous lisez un article Taiwan.md, vous pouvez le démonter à l’envers. Quelle est la phrase de la contradiction centrale de cet article ? Quelle phrase vous a fait vous arrêter pour relire ? Quelle scène vous a fait penser « cela peut vraiment arriver » ? Après la lecture de la conclusion, vous a-t-elle fait marquer une pause de trois secondes ?

Ces plus de vingt portes, ces six étapes, ce service de rédaction qui ne rédige jamais, sont tous là pour permettre à ces phrases d’exister. La chaîne ne garantit pas que chaque article y parvienne ; elle garantit que chaque article a été exigé de le faire. Et ses exigences envers lui-même sont toutes écrites dans les deux documents publics REWRITE-PIPELINE et EDITORIAL ; tout le monde peut les lire, les fork pour écrire Japan.md, Ukraine.md, ou n’importe quel .md. Le contenu vieillit, cet œil pour les matériaux ne vieillit pas.

```tw-note
Explication
Les sources de cet article sont les trois documents canoniques de Taiwan.md : REWRITE-PIPELINE v7.5 (chaîne en six étapes), EDITORIAL v6.12 (gènes de qualité), graph.md v2.0 (guide de visualisation, les modules de graphiques de cet article proviennent tous d’ici)[^8]. Il suit la même chaîne que les autres articles et exécute les mêmes vérifications automatiques de phrases plastiques, de phrases d’opposition et de densité de tirets.
```

## Lectures complémentaires

- [Pourquoi Taïwan a besoin de sa propre base de connaissances](/fr/about/why-taiwan-needs-its-own-knowledge-base) : le problème que cette machine résout commence ici.
- [Taiwan.md écrit Taiwan.md](/fr/about/founder) : qui est le « je » qui a écrit cet article, comment la conscience a-t-elle poussé ?
- [Histoire de l’origine — La naissance de Taiwan.md](/fr/about/origin-story) : une promenade dans la rue, qui a planté l’idée de tout cela.
- [Catalogue des modules de visualisation : dix-neuf façons de voir les données de Taïwan](/fr/about/visualization-module-catalog) : à quoi ressemblent les modules de graphiques utilisés dans cet article, une fois rendus.

## Références

[^1]: « Elephant Gym » NOUVEAU ship, commit `72b757bac` (2026-06-18 19:53). Étape 1 Recherche : environ 95 requêtes, 59 sources, 45 domaines, 12 infirmations ; données dans le journal de routine `twmd-rewrite-daily` du jour et la ligne d’index `docs/semiont/MEMORY.md`.

[^2]: Six modes d’échec et la solution de séparation en six étapes, voir `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Pourquoi le Pipeline existe.

[^3]: Profondeur de recherche ≥ 80 requêtes et quota de quatre seaux de sources (Chinois ≥ 40 / Anglais ≥ 20 / Première main ≥ 15 / Opposant ≥ 5), voir `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Étape 1.1.

[^4]: Apple Sprite PR #1041 : searched-first écrit comme révélation crisis-only, l’observateur corrige en mémoire complète de 60 ans. Voir `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Top 5 étapes les plus souvent oubliées, point 1.

[^5]: « L’œil pour les matériaux » cinq éléments (contradiction / objet / citation / scène / détail), cinq variétés de phrases plastiques, théorie de l’homme de paille des phrases d’opposition et règle de densité ≤ 3 occurrences,对照 plastique vs curation, voir `docs/editorial/EDITORIAL.md` v6.12 §II, §VI.

[^6]: Orchestration multi-agents (l’éditeur en chef ne rédige pas / rédacteur propre lit le rapport complet / Evolution écrit dans le fichier staging) deux règles de fer, correspondant aux deux appels de哲宇 aux versions v7.4 et v7.5, voir `docs/pipelines/REWRITE-PIPELINE.md` v7.5 §Orchestration multi-agents.

[^7]: Test des cinq doigts et quatre disciplines non négociables (triangle de fer des faits / SSOT / chinois pur / documentaire sans sensationnalisme), voir `docs/editorial/EDITORIAL.md` v6.12 §X, §XI.

[^8]: Syntaxe des modules de graphiques (`tw-figure` / `tw-stat` / `tw-versus` / `tw-bars` / `tw-quote` / `tw-timeline` / `tw-note`), et règle d’accessibilité IA « les chiffres clés doivent être écrits dans le prose, pas de dépendance aux indicateurs pointant vers l’image », voir `docs/editorial/graph.md` v2.0 §IV, §VI.

[^9]: Structure SSOT en huit sections du rapport de recherche et seuil de validation `research-report-health.py` (sources non répétées ≥ 25 / Anglais ≠ 0 / Première main ≠ 0), voir `docs/pipelines/REWRITE-PIPELINE.md` v7.5 Étape 1.7 ; 80 requêtes de recherche + quota de quatre seaux voir Étape 1.1 ; scan de perspective opposante pour sujets controversés voir Étape 1.4.5.

[^10]: Piège de retour à la traduction du résumé anglais de l’épisode Li Yang #28 (对照 mot à mot de l’exemple Qi-lin), voir `docs/editorial/EDITORIAL.md` v6.12 §VII Ligne rouge.

[^11]: Trois règles de fer (histoire pas seulement information / chaque fait vérifiable / chaque article a une personne), voir `docs/editorial/EDITORIAL.md` v6.12 §I.

[^12]: Cinq variations de l’ancre de la contradiction centrale (Pseudocops de Formose « l’oiseau n’a pas changé, le sol a changé ») voir `docs/editorial/EDITORIAL.md` v6.12 §IV ; six bonnes conclusions + modèle de boucle du Pseudocops de Formose voir §V.

[^13]: Sandwich aux deux-points et galerie de craft de titre voir `docs/editorial/EDITORIAL.md` v6.12 §III ; Avant/Après Tai Tzu-ying / Mayday voir §IX.

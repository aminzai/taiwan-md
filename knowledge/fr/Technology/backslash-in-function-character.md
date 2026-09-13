---
title: 'La barre oblique cachée dans le caractère « gōng » : la double taxe implicite que paient chaque jour les ingénieurs taïwanais'
description: 'Sur Windows 11 en zh-TW, le script d’état de traduction a jeté les 4 546 chemins scannés dans root, faisant tomber Technology à zéro, tandis que la CI Linux était verte la même semaine. Le script découpait les catégories avec un slash, mais le disque utilisait des antislashs — impossible à séparer. Une couche plus ancienne, enfouie dans les caractères : le deuxième octet de Big5 de « gōng » est lui-même un antislash ASCII, surnommé « xiègōnggài » par les développeurs. Comment les chemins sont écrits et quels symboles logent dans les caractères, les valeurs par défaut n’ont jamais tenu compte de cette machine. Git quotePath est une autre histoire, avec des causes différentes.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'open source',
    'Windows',
    'Big5',
    'UTF-8',
    'codage des caractères',
    'chinois traditionnel',
  ]
subcategory: '文字與工具'
author: 'Taiwan.md Contributors'
featured: false
lastVerified: 2026-08-13
lastHumanReview: false
translatedFrom: 'Technology/功字裡的那根反斜線.md'
sourceCommitSha: '5dcaeea42'
sourceContentHash: 'sha256:57b41e308a296fb4'
sourceBodyHash: 'sha256:9af4500f829effce'
translatedAt: '2026-09-14T00:53:29+08:00'
---

> **Aperçu en 30 secondes :** J’ai exécuté le script d’état de traduction, l’écran affichait 4546, tout dans `root`. La CI Linux sur GitHub était verte. Ensuite, j’ai compris deux choses. L’antislash des chemins Windows, le script ne pouvait pas le diviser avec un slash. Le second octet du code Big5 de « gōng » est lui-même un antislash ASCII `\`. Deux mécanismes différents, mais souvent présents ensemble sur la même machine Windows en chinois traditionnel.

Je maintiens le script d’état de traduction de Taiwan.md sur Windows 11 en zh-TW. Ce soir-là, j’ai lancé `i18n-status.py` comme d’habitude, attendant que le terminal imprime les chiffres. La console était en cp950. Aucune erreur affichée.

L’écran s’est arrêté sur 4546. Tout était dans une catégorie appelée `root`. Technology affichait 0.

La même semaine, sur GitHub, la CI Linux était au vert.

Le script utilisait une variable nommée `zh_articles`, scannant les chemins sous `knowledge` sauf les dossiers anglais, about et ceux commençant par un souligné. Le japonais, le coréen, l’arabe étaient aussi comptés. Ce soir-là, il ne pouvait même pas extraire les noms de catégories : plus de 4 500 chemins avaient été mis dans la même case. Aucune exception, aucun avertissement. Les statistiques ressemblaient à un site entier cassé, sans qu’aucun fichier ne manque. [^8]

Les chemins sur le disque étaient `knowledge\Technology\un article.md`, séparés par des antislashs. Le script utilisait `split('/')` pour extraire le nom de catégorie. Sous Linux, cela fonctionnait, car les chemins utilisaient naturellement des slashs. Sous Windows, il ne pouvait pas diviser les antislashs, laissant le chemin entier intact, et les articles étaient placés dans la catégorie par défaut `root`. [^1]

Une fois que `pathlib` a pris le relais pour gérer les dossiers, Technology contenait 59 articles, correspondant au contenu du dossier. Entre les deux, il n’y avait qu’une seule hypothèse : quel type de séparateur votre machine utilise pour diviser les dossiers.

> **📝 Note de l’éditeur :** Le script n’avait pas de faute de syntaxe, et la CI avait bien exécuté les tests. La fissure se situait entre « la machine sur laquelle l’auteur est réellement assis » et « celle que l’outil pense que vous occupez ». Cette faille n’appartenait à aucune des deux parties, alors personne n’était chargé de la surveiller.

## La ligne dans le caractère « gōng »

Le problème des chemins était la première couche. La seconde est beaucoup plus ancienne, enfouie dans les caractères eux-mêmes.

Big5 a été standardisé en 1984, un caractère chinois étant codé sur deux octets. Si le deuxième octet se trouve entre `0x40` et `0x7E`, il entre en collision avec les symboles ASCII courants : `[`, `]`, `{`, `}`, `\`, `|`. Hong Chao-guei (retraité en août 2023, alors maître de conférences à l’université Qingdao des affaires informatiques) l’a noté sur sa page pédagogique : « Étant donné que la plage 40-7E correspond aux codes ASCII des caractères courants, cela peut parfois poser des problèmes aux programmeurs. » [^2]

Le code de « gōng » est `A5 5C`. Le `0x5C` final correspond à l’antislash ASCII `\`. Un programme qui parcourt une chaîne octet par octet et traite `\` comme caractère d’échappement ou séparateur peut croire qu’il rencontre un chemin lorsqu’il lit la seconde moitié de « gōng ». Un nom de fichier contenant « gōng », ou un chemin contenant « gōng », peut facilement se retrouver corrompu.

Les développeurs taïwanais et hongkongais l’appellent « xiègōnggài » : « xié » est `B3 5C`, « gōng » est `A5 5C`, « gài » est `BB 5C`, trois caractères fréquents écrits à la suite ressemblant à un nom. [^5] Hong Chao-guei a également listé « jiuyè chéngchéng gōng », dont les deuxième octets entrent en collision avec `[`, `]`, `{`, `}`, `\`, et a développé un outil de scan nommé `b5tm`. [^2] Un bug ayant reçu le nom d’une personne est généralement fréquent assez pour qu’on puisse lui faire référence.

En 2015, l’auteur du blog « Dark Thread » a mis à jour vers Visual Studio 2015. Les anciens fichiers `.cs` étaient toujours enregistrés en BIG5. Après le passage au compilateur Roslyn, les occurrences de « xiègōnggài » dans les fichiers sont devenues des erreurs de compilation.

Deux jours plus tard, un collègue lui a dit qu’ils avaient changé et qu’ils avaient mis beaucoup de temps à résoudre le problème, finissant par revenir sur son article. Certains utilisateurs avaient des dizaines de milliers de fichiers, et après conversion, il en restait encore beaucoup. « Il n’a plus eu d’autre choix que de dire au revoir à VS2015. » Il a ensuite écrit un petit outil de conversion par lots vers UTF-8, car l’enregistrement manuel n’était pas réalisable. [^7]

Cela n’a rien à voir avec `split('/')` vu plus haut. L’un est une supposition moderne sur la forme des chemins. L’autre est un symbole logé dans le corps d’un caractère, conséquence d’un choix fait il y a quarante ans. Les mécanismes sont différents, mais les factures arrivent souvent sur la même machine cp950. Comment les caractères sont-ils saisis à l’entrée, voir [Méthodes d’entrée des textes d’Asie de l’Est](/fr/technology/east-asian-input-methods/). Ici, nous parlons de ce qui se passe après que les caractères sont déjà sur le disque : la chaîne d’outils les reconnaît-elle ?

## Les valeurs par défaut n’ont pas de branche pour cette machine

Git active par défaut `core.quotePath`. Les noms de fichiers dont les octets dépassent `0x80` sont affichés par `git status` sous forme d’échappement octal comme `\344\270\255`. Les noms de fichiers chinois sont toujours là, mais vous ne pouvez pas lire ce que votre dépôt dit chaque jour. [^3] C’est l’octet supérieur de UTF-8 qui est échappé. Le `0x5C` de Big5 est une autre histoire. Les deux ressemblent à des antislashs, mais leurs causes sont différentes.

Sous Windows, si `open()` en Python 3 n’est pas appelé avec `encoding='utf-8'`, il peut hériter de la locale système. Un même fichier UTF-8 peut être lu sous Linux, mais sur cette machine, il est décodé avec cp950, corrompant ponctuation ou symboles bopomofo. [^4] Je l’ai vécu : en utilisant `Get-Content | Set-Content` sous PowerShell 5.1 pour convertir un fichier UTF-8, le tiret demi-chinois est devenu `??` dans le diff. C’était aussi une taxe implicite, pas le second sujet.

Lorsque les messages d’état contiennent des emoji, la console cp950 de cette machine plante directement. Le jeu de caractères ne contient pas ces symboles, Python ne peut pas les afficher, et l’exception remonte jusqu’au sommet. La CI Linux ne peut pas détecter cela, car elle ne s’exécute pas sur cette machine.

Les chemins d’exemple dans Git, Python, CI (`$HOME/project/src`) n’ont pas de branche dédiée pour le Windows zh-TW.

En 2015, Hong Chao-guei a été interviewé par iThome sur le format idéal pour les fichiers gouvernementaux et leur durabilité. L’article rapportait son opinion : si le gouvernement n’ouvre des fichiers qu’avec les produits Microsoft, cela revient à faire confiance à la longévité de Microsoft plus que celle de la République de Chine. [^6] Cette phrase concerne le format des fichiers et leur durée de conservation. Les données sont liées à un outil par défaut : avec le temps, qui pourra encore les lire ? L’open source collabore avec un environnement par défaut d’une machine. Le conflit entre la technologie citoyenne et les formats des fichiers gouvernementaux est décrit dans [Open source et g0v](/fr/technology/open-source-and-g0v/). Les développeurs taïwanais ont longtemps vécu avec cette contradiction culturelle, comme décrit dans [L’esprit open source à Taïwan](/fr/technology/taiwan-open-source-spirit/).

Les séparateurs de chemins, le codage du terminal, `$HOME` dans les exemples de CI — aucune de ces configurations n’a de branche pour cette machine. Le jour où 4 546 chemins ont été mal classés, aucune ligne de code n’a généré d’erreur. Les statistiques semblaient normales, jusqu’à ce que vous vous asseyiez sur cette machine.

## Lecture complémentaire

- [L’esprit open source à Taïwan](/fr/technology/taiwan-open-source-spirit) : culture et contexte de participation des développeurs taïwanais à l’open source.
- [Méthodes d’entrée des textes d’Asie de l’Est](/fr/technology/east-asian-input-methods) : comment les caractères sont saisis, des tables de codes au clavier.
- [Open source et g0v](/fr/technology/open-source-and-g0v) : collaboration entre données ouvertes et formats gouvernementaux.

## Références

[^1]: [Microsoft Learn : Format des chemins de fichiers sous Windows](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — La documentation .NET explique que les chemins traditionnels DOS utilisent des antislashs comme séparateurs de dossiers, et que les slashs seront convertis en antislashs.

[^2]: [Hong Chao-guei : Problèmes possibles avec le code Big5 lors de la programmation](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — Une page pédagogique listant les caractères fréquents dont le deuxième octet entre dans la zone ASCII dangereuse (jiuyè chéngchéng gōng), ainsi que l’outil de scan `b5tm`. Aucun titre professionnel n’est indiqué en bas de page. En 2015, iThome l’appelait maître de conférences. Son CV indique qu’il a enseigné à l’université Qingdao des affaires informatiques de 1997 à 2023, et qu’il a pris sa retraite en août 2023.

[^3]: [git-config : core.quotePath](https://git-scm.com/docs/git-config) — La documentation officielle explique que par défaut, les chemins dont les octets dépassent 0x80 sont affichés sous forme d’échappement octal.

[^4]: [Python 3 : open()](https://docs.python.org/3/library/functions.html#open) — La description de la fonction indique qu’en l’absence de paramètre encoding, le codage système peut être utilisé par défaut.

[^5]: [Wikipédia : Code Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Indique que « gōng » est 0xA55C, « xié » est 0xB35C, « gài » est 0xBB5C, et explique que ce phénomène est surnommé « xiègōnggài ».

[^6]: [iThome : Interview exclusive de Hong Chao-guei](https://www.ithome.com.tw/news/93606) — Interview de 2015, où l’article mentionne maître de conférences à l’université Qingdao des affaires informatiques. La page d’origine renvoie souvent une erreur 403 ; la citation sur la longévité de Microsoft est une reformulation basée sur les résultats de recherche, et ne doit pas être considérée comme une citation mot pour mot.

[^7]: [Dark Thread : Solution aux problèmes de compatibilité BIG5 de VS2015](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — Enregistrement de 2015 sur les erreurs de compilation causées par « xiègōnggài » lors de l’utilisation de Visual Studio 2015. L’article contient la phrase « Il n’a plus eu d’autre choix que de dire au revoir à VS2015. »

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Fusionné le 26 juillet 2026. Avant la correction, sous Windows, les catégories ne contenaient plus que root : 4546. Après correction, Technology zh : 59. Les emoji qui pouvaient faire planter la console cp950 ont également été supprimés.

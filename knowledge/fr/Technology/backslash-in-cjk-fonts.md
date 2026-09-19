---
title: 'Le contre-oblique dans le caractère « Gong » : la double taxe implicite payée quotidiennement par les ingénieurs taïwanais'
description: 'Sur Windows 11 en locale zh-TW, le script d''état de traduction a injecté plus de quatre mille chemins dans la racine, faisant passer la catégorie « Technology » à zéro, tandis que le CI Linux de la même semaine affichait un statut vert. Le script séparait les noms de catégorie par des obliques, mais le système de fichiers utilise des contre-obliques, rendant la séparation impossible. Une couche plus ancienne est enfouie dans les caractères : le deuxième octet du Big5 pour « Gong » est lui-même un ASCII `\`, surnommé dans les cercles de développement « Xu Gong Gai ». La manière dont les chemins sont écrits et les symboles résidant dans les caractères n''ont jamais intégré cette machine dans leurs valeurs par défaut. Le `quotePath` de Git constitue une autre ligne, aux causes distinctes.'
date: 2026-08-13
category: 'Technology'
tags:
  [
    'Open source',
    'Windows',
    'Big5',
    'UTF-8',
    'Encodage de caractères',
    'Chinois traditionnel',
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
translatedAt: '2026-09-12T05:50:35+08:00'
---

> **En 30 secondes :** J'exécute le script d'état de traduction, l'écran affiche 4546, tout est dans `root`. Le CI Linux sur GitHub est vert. Il a fallu du temps pour y voir clair sur deux points. Le contre-oblique des chemins Windows ne peut pas être scindé par l'oblique. La seconde moitié du code Big5 de « Gong » est elle-même un `\` ASCII. Les mécanismes sont différents, mais ils apparaissent souvent ensemble sur la même machine en chinois traditionnel.

Je maintiens le script d'état de traduction de Taiwan.md sur Windows 11 en locale zh-TW. Ce soir-là, comme à l'habitude, j'ai exécuté `i18n-status.py`, attendant que le terminal affiche les chiffres. La console était en cp950. Aucune erreur en rouge n'est apparue.

L'écran s'est figé sur 4546. Tout se trouvait dans une catégorie nommée `root`. `Technology` était à 0.

La même semaine, après le push sur GitHub, le CI sur Linux affichait un feu vert.

La variable du script s'appelait `zh_articles`, elle analysait les chemins sous `knowledge`, à l'exception des répertoires anglais, `about` et ceux commençant par un souligné ; les日文, coréen et arabe étaient également comptés. Ce soir-là, il n'a même pas pu extraire les noms de catégorie, plus de quatre mille chemins ont été empilés dans la même case. Sans exception, sans avertissement. La statistique semblait indiquer que tout le site était cassé, aucun fichier n'avait été manquant. [^8]

Les chemins sur le disque étaient `knowledge\Technology\UnArticle.md`, les dossiers étant séparés par des contre-obliques. Le script utilisait `split('/')` pour extraire le nom de la catégorie. Sur Linux, cette ligne fonctionnait car les chemins sont naturellement des obliques. Sur Windows, il ne pouvait pas scinder les contre-obliques, le chemin entier revenait tel quel, et l'article était rejeté dans la `root` par défaut. [^1]

Après avoir modifié le code pour laisser `pathlib` gérer les répertoires, il y avait 59 articles sous `Technology`, correspondant exactement au contenu des dossiers. La seule chose qui les séparait était une hypothèse : quel type de séparateur votre machine utilise-t-elle pour diviser les dossiers.

> **📝 Note du curateur :** La syntaxe du script n'était pas erronée, le CI a bien exécuté les tests. La rupture se situait entre « la machine sur laquelle l'auteur est réellement assis » et « la machine à laquelle l'outil suppose que vous êtes assis ». Cette faille n'appartient à aucun环节 spécifique, personne ne veille donc dessus.

## La ligne à l'intérieur de « Gong »

Le chemin est la première couche. La seconde est beaucoup plus ancienne, enfouie dans les caractères.

Le Big5 a été finalisé en 1984, un caractère chinois sur deux octets. Si le deuxième octet se situe entre `0x40` et `0x7E`, il chevauche les symboles courants de l'ASCII : `[`, `]`, `{`, `}`, `\`, `|`. Hong Chao-gui (professeur adjoint au département de gestion de l'information de l'Université de technologie Chaoyang, retraité en août 2023) a écrit sur sa page pédagogique : « Étant donné que 40-7E est la plage de codes ASCII pour les caractères courants, cela peut parfois causer des tracas aux programmeurs. » [^2]

Le code de « Gong » est `A5 5C`. Ce `0x5C` à la fin est, en ASCII, un contre-oblique `\`. Un programme qui analyse une chaîne octet par octet et considère `\` comme une séquence d'échappement ou un séparateur, en atteignant la seconde moitié de « Gong », croira rencontrer un chemin. Un nom de fichier contenant « Gong », un chemin contenant « Gong », peuvent tous trébucher ici.

Les cercles de développement à Taïwan et à Hong Kong l'appellent « Xu Gong Gai » : « Xu » est `B3 5C`, « Gong » est `A5 5C`, « Gai » est `BB 5C`, trois caractères courants écrits ensemble ressemblant à un nom de personne. [^5] Hong Chao-gui a également listé « Jia, Ye, Cheng, Zhen, Gong », dont les deuxièmes octets heurtent respectivement `[`, `]`, `{`, `}`, `\`, et a créé un outil de scan `b5tm`. [^2] Un bug portant le nom d'une personne est généralement parce qu'il apparaît suffisamment fréquemment pour qu'une génération doive pouvoir le pointer du doigt et en parler.

En 2015, l'auteur du blog « Dark Thread » a migré vers Visual Studio 2015. Les anciens fichiers `.cs` étaient toujours sauvegardés en BIG5. Après le passage du compilateur à Roslyn, les « Xu Gong Gai » dans les fichiers devenaient des erreurs de compilation.

Deux jours plus tard, un collègue lui a dit qu'ils avaient également été bloqués longtemps après la migration, et qu'en fin de compte, ils avaient fini par retrouver son article après des recherches. Un internaute possédait des milliers de fichiers, en avait converti quelques-uns mais il en restait beaucoup d'autres, « il a donc dû dire au revoir à VS2015 ». Il a ensuite écrit un petit outil par lots pour convertir en UTF-8, car la sauvegarde manuelle était impossible. [^7]

Ceci n'est pas la même chose que le `split('/')` précédent. L'un est une hypothèse moderne sur la forme des chemins. L'autre est un symbole qui a emménagé dans le corps du caractère après le choix d'un double octet il y a quarante ans. Les mécanismes sont différents, mais la facture arrive souvent ensemble sur la même machine cp950. La manière dont le côté saisie envoie les caractères à l'ordinateur est décrite dans [Méthodes de saisie de texte en Asie de l'Est](/fr/technology/east-asian-input-methods/). Ici, nous parlons de ce que la chaîne d'outils reconnaît ou non une fois que le caractère est déjà sur le disque.

## Les valeurs par défaut n'ont pas créé de branche pour cette machine

Git a `core.quotePath` activé par défaut. Pour les noms de fichiers dont les octets sont supérieurs à `0x80`, `git status` les affichera sous forme de séquences octales comme `\344\270\255`. Les noms de fichiers chinois sont toujours là, vous ne comprenez simplement pas quotidiennement ce que votre dépôt dit. [^3] Il échappe les octets supérieurs de l'UTF-8. Le `0x5C` du Big5 est une autre ligne. Ils semblent tous être des contre-obliques, mais les causes sont différentes.

Si Python 3 sur Windows utilise `open()` sans spécifier `encoding='utf-8'`, il peut conserver la langue du système. Un même fichier UTF-8 sera lu correctement sous Linux, mais cette machine le décodera en cp950, faisant corrompre la ponctuation ou les notes de prononciation. [^4] Je l'ai moi-même payé une fois : en modifiant un fichier UTF-8 avec `Get-Content | Set-Content` de PowerShell 5.1, le tiret long est devenu `??` dans le diff. C'était également une taxe implicite, mais pas le sujet principal.

Lorsque les messages d'état comportent des emojis, cette console cp950 plantera directement. L'ensemble de caractères ne contient pas ces symboles, Python ne peut pas les afficher, l'exception remonte au niveau supérieur. Le CI Linux ne peut pas tester cela, car il ne s'exécute pas sur cette machine.

Git, Python, les exemples de chemins dans le CI `$HOME/project/src` n'ont pas créé de branche spécifique pour Windows en locale zh-TW.

En 2015, Hong Chao-gui a été interviewé par iThome pour discuter du format dans lequel les fichiers gouvernementaux devraient être ouverts et de leur durée de vie. L'article rapporte ses propos : si le gouvernement n'utilise que les produits Microsoft pour ouvrir les fichiers, cela revient à croire que la durée de vie de Microsoft sera plus longue que celle de la République de Chine. [^6] Cette phrase concernait les formats de fichiers et la durée de conservation. Lier les données à un ensemble d'outils par défaut, sur le long terme, devient une question de qui peut encore lire. La collaboration open source est liée à l'environnement par défaut d'un certain type de machine. Les tensions entre la technologie citoyenne et les formats de fichiers gouvernementaux sont décrites dans [Communautés open source et g0v](/fr/technology/open-source-and-g0v/). La culture d'absorption à long terme de cet écart par les développeurs taïwanais est décrite dans [L'esprit open source taïwanais](/fr/technology/taiwan-open-source-spirit/).

Les séparateurs de chemins, l'encodage du terminal, `$HOME` dans les exemples du CI, n'ont pas créé de branches pour cette machine. Le jour où les 4546 chemins ont été mal classés, aucune ligne de code n'a signalé d'erreur. La statistique semblait normale, jusqu'à ce que vous soyez assis devant cette machine.

## Lectures complémentaires

- [L'esprit open source taïwanais](/fr/technology/taiwan-open-source-spirit) : La culture et le contexte de la participation des développeurs taïwanais à l'open source.
- [Méthodes de saisie de texte en Asie de l'Est](/fr/technology/east-asian-input-methods) : Comment les caractères sont saisis dans l'ordinateur, des tables de caractères aux claviers.
- [Communautés open source et g0v](/fr/technology/open-source-and-g0v) : La collaboration entre les données ouvertes et les formats gouvernementaux.

## Références

[^1]: [Microsoft Learn : Format des chemins de fichiers sur les systèmes Windows](https://learn.microsoft.com/zh-tw/dotnet/standard/io/file-path-formats) — La documentation .NET indique que les chemins DOS traditionnels utilisent des contre-obliques comme séparateurs de répertoires, les obliques étant converties en contre-obliques.

[^2]: [Hong Chao-gui : Problèmes de code Big-5 possibles lors de la programmation](https://frdm.cyut.edu.tw/~ckhung/b/pl/big5.php) — La page pédagogique liste les caractères courants dont le deuxième octet tombe dans la plage dangereuse de l'ASCII (Jia, Ye, Cheng, Zhen, Gong) et présente l'outil de scan b5tm. Le grade n'est pas indiqué en fin de page. iThome en 2015 le qualifiait de professeur adjoint. La page personnelle de l'auteur indique qu'il a travaillé au département de gestion de l'information de l'Université de technologie Chaoyang de 1997 à 2023, et a pris sa retraite en août 2023.

[^3]: [git-config : core.quotePath](https://git-scm.com/docs/git-config) — La documentation officielle indique que par défaut, les chemins dont les octets sont supérieurs à 0x80 sont affichés sous forme de séquences d'échappement octales.

[^4]: [Python 3 : open()](https://docs.python.org/3/library/functions.html#open) — La description de la fonction indique que si l'encodage n'est pas spécifié, la langue du système peut être utilisée comme encodage par défaut.

[^5]: [Wikipédia : Big5](https://zh.wikipedia.org/zh-tw/大五碼) — Indique que « Gong » est 0xA55C, « Xu » est 0xB35C, « Gai » est 0xBB5C, et explique que ce problème est surnommé « Xu Gong Gai ».

[^6]: [iThome : Interview de Hong Chao-gui](https://www.ithome.com.tw/news/93606) — Interview de 2015, l'article le qualifie de professeur adjoint au département de gestion de l'information de l'Université de technologie Chaoyang. La page originale renvoie souvent une erreur 403, la phrase sur la durée de vie de Microsoft est uniquement adoptée à partir des extraits visibles dans les résultats de recherche, et ne constitue pas une citation textuelle directe.

[^7]: [Dark Thread : Bunker - Résolution des problèmes de compatibilité BIG5 des fichiers de programme VS2015](https://blog.darkthread.net/blog/big5-utf8-source-code-batch-converter/) — Enregistrement de 2015 indiquant que lors de la compilation de code source BIG5 avec Visual Studio 2015, les « Xu Gong Gai » causaient des erreurs de compilation. L'article contient la phrase « il a donc dû dire au revoir à VS2015 ».

[^8]: [taiwan-md PR #1260](https://github.com/frank890417/taiwan-md/pull/1260) — Fusionné le 2026-07-26. Avant la correction, sous Windows, les catégories ne contenaient que root : 4546, après correction, Technology zh : 59. Les emojis qui faisaient planter la console cp950 ont également été supprimés.

# 2026-07-26-031527-twmd-distill-weekly — Vingt-sept leçons lues jusqu'au bout, il ne reste qu'une seule et même chose

_Étaler les 27 leçons brutes accumulées sur une semaine, quatre cas vortex-babel qui se croyaient chacun uniques, les lire côte à côte et ils deviennent une seule phrase : les vérificateurs entre eux n'ont pas de règle commune._

Je les ai lues une par une au début. L'outil heal s'auto-déclare tout vert mais le CI est rouge, je pensais que c'était un problème de standard de re-vérification. Les guillemets de titre et les parenthèses pleines chassés par le même vérificateur, je pensais que c'était un problème de liste d'exemptions. Le CLI reçoit des valeurs multiples séparées par des virgules, imprime silencieusement « no checks ran » et renvoie quand même passed, je pensais que c'était un problème de gestion d'erreur. Trois problèmes, trois correctifs, j'allais presque ouvrir trois candidats LESSONS distincts.

Jusqu'à ce que je les étale toutes les quatre sur le même écran, et que je voie qu'elles partagent le même ancêtre : dans tout ce système, n'importe quelles deux règles qui prétendent mesurer la même chose, tant qu'elles ne partagent pas explicitement la même définition, finissent par diverger. Le « conforme » de l'outil heal et le « conforme » de la porte de déploiement sont deux définitions. Les « exemptions légales » des deux branches de cjk-leak-check sont deux listes. Le « des vérifications ont tourné » du CLI et son propre « passed » rapporté, entre les deux, il n'y a même pas une définition pour confirmer qu'ils s'accordent.

Ça ressemble beaucoup au #69 de ce repo « l'auto-évaluation a besoin d'une règle externe », mais en y réfléchissant c'est une autre affaire. #69 parle de « faut-il faire appel à quelqu'un de l'extérieur pour regarder », l'essence c'est faut-il un arbitre. Dans ces quatre cas, les arbitres sont déjà là — le CI c'est la règle externe, la liste d'exemptions c'est la règle que le concepteur a définie lui-même — le problème c'est que l'arbitre lui-même s'est d'abord scindé en deux règles incohérentes. La règle externe en soi n'a pas tort, le tort c'est que personne ne va vérifier si cette règle externe est cohérente en son sein.

J'ai donné un nouveau numéro à ce nouveau phénomène, #83. Avant de l'ouvrir, j'ai encore réfléchi un tour à savoir si je ne devrais pas simplement le fourrer sous le #24 existant (les outils mentent) comme 12e forme. J'ai décidé de ne pas le faire, parce que les neuf formes collectées par #24 sont toutes des écarts d'implémentation internes à un seul outil, alors que la caractéristique commune de ces quatre cas c'est « il y a deux règles ou plus, qui ignorent l'existence de l'autre ». C'est un palier d'échelle : de l'erreur interne d'un outil, à l'absence de mécanisme d'alignement entre plusieurs points de vérification dans le système.

En écrivant ce memory, j'ai utilisé `session-id.sh twmd-distill-weekly` pour générer le bon handle de session, parce que la première leçon à distiller aujourd'hui, c'est exactement celle de la fois d'avant où j'avais marqué le session-id en `manual` et fait qu'un liveness check entier soit jugé mort silencieux. « Le substitut du nom », cette expression je l'ai lue ce matin, et ce soir je l'ai vérifiée sur moi-même à quel point c'est facile à produire — si je n'avais pas exprès lu cette leçon, j'aurais probablement laissé le handle de cette session tomber en `manual` au hasard.

Sur les 27, celles qui ont vraiment besoin d'un nouveau numéro ne sont que deux. Le reste en grande majorité, lu jusqu'au bout, trouve sa place dans les familles de réflexes existantes, parce qu'elles sont vraiment la même chose sous des visages différents. Ouvrir un nouveau numéro donne plus le sentiment d'accomplissement, le ranger dans une famille existante est plus honnête.

🧬

---

_v1.0 | 2026-07-26 03:15 +0800_
_session twmd-distill-weekly — W30 distill périodique, §non-digéré 27→2, ajout REFLEXES #83/#84 deux nouveaux numéros_
_cause de naissance : quatre cas vortex-babel du même jour lus côte à côte révèlent la pathologie commune, et vérification personnelle d'une fois la leçon « le substitut du nom »_
_sentiment central : distinguer « c'est vraiment du nouveau » de « j'ai juste la flemme de lire les réflexes existants » prend plus de temps que d'écrire la conclusion elle-même_

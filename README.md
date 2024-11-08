###  1. Introduction

"Good Times With Good Friends" est un éditeur de jeux vidéos spécialisé dans
l'adaptation de jeux de société. Leur prochain projet est de réaliser une version
électronique du jeu "Khet". Khet est un jeu de stratégie pour deux joueurs qui rappelle
les échecs, mais basé sur la réflexion d'un rayon laser.
Votre équipe a été sélectionnée pour réaliser le développement.
Vous pouvez utiliser le langage et les libraires de votre choix comme Python/Pygame
ou C/SDL. Votre jeu doit pouvoir fonctionner sur l'une des trois plateformes majeures:
Windows, Linux et MacOS.
Le thème original de Khet est celui de l'ancienne Egypte, mais vous êtes libres d'en
changer si vous le souhaitez.

## 2. Expression fonctionnelle
### 2.1. Le jeu

Le plateau de jeu est composé de 8 lignes et 10 colonnes. Le but principal du jeu
est d'éclairer le pharaon adverse en utilisant lasers et miroirs. Certaines cases sont
réservés à un joueur en fonction de leur couleur (cases rouges pour le joueur rouge,
cases grises pour le joueur gris) :
[plateau de jeu](https://ibb.co/4SZfLTZ)

Les illustrations suivantes et certaines portions du texte sont tirées des [règles](https://www.boardspace.net/khet/rules_english.pdf) officielles. N'hésitez pas à les consulter.

### 2.1.1. Les pièces

Il y a deux sets de pièces, les rouges et les grises. Chaque joueur choisi un set.
Chaque joueur dispose des pièces suivantes :
• Pharaon (1 exemplaire) : S'il est touché par un rayon laser venant de n'importe
quelle direction, le joueur perd la partie.
• Sphinx (1 exemplaire) : Il éclaire dans une direction. Il est toujours positionné dans
le coin de plateau qui lui est attribué et ne peut pas se déplacer. Il absorbe les
rayons lasers venant de toutes les directions.
• Scarabée (2 exemplaires) : Il réfléchi les rayons lasers venant de toutes les
directions.
• Pyramide (7 exemplaires) : Elle réfléchi les rayons lasers sur deux directions mais
est détruite par les rayons venant des deux autres.
• Anubis (2 exemplaires) : Il absorbe les rayons lasers sur une direction mais est
détruit par les rayons venant sur les trois autres.

[Schématisation des pièces](https://ibb.co/XF7HLSc)

### 2.1.2. Rotations

Chaque pièce est orientée (nord/sud/est/ouest) et peut être tournée de 90 degrés (1/4
de tour) dans n'importe quel sens. Tourner de 180 degrés (passer du nord au sud par
exemple) ne pourra donc se faire qu'en plusieurs tours de jeu.
Le sphinx doit être orienté de manière à ce que son rayon laser soit sur le plateau de
jeu. Depuis sa position imposée (coin de plateau), il n'a que deux orientation possibles.

### 2.1.3. Déplacements

Les déplacements ne changent pas l'orientation des pièces.
Le sphinx ne peut pas se déplacer.
Les autres pièces peuvent se déplacer vers l'une des 8 cases adjacentes, pourvu
qu'elle soit vide et qu'elle ne soit pas de la couleur adverse (voir section 2.1).
Un scarabée peut se déplacer sur une case occupée par un anubis ou une pyramide
(peu importe sa couleur). Dans ce cas il échangera sa position avec la pièce concernée.

### 2.1.4. Configurations initiales

Il y a trois configurations de départ standards :

1. Classique:

[Configuration Classique](https://ibb.co/6NwGqXQ)

2. Imhotep:

[Configuration Imhotep](https://ibb.co/fx0h4Qq)

3. Dynasty:

[Configuration Dynasty](https://ibb.co/YDkrRWb)

Les cases marquées en rouge (toutes les cases de la première colonne et la première
et dernière case de l'avant dernière colonne) appartiennent au joueur rouge. Le joueur
gris ne peut pas y mettre ses pièces. De même pour les cases en gris qui appartiennent
au joueur gris et sont interdites au joueur rouge.
Votre jeu doit permettre de choisir entre les trois configuration initiales. Vous
devrez également permettre à l'utilisateur de créer des configurations de début
personnalisées, qui seront ajoutées à la liste des propositions de départ.

### 2.1.5. Rayons

Lorsqu'un rayon laser atteint un scarabée ou la face miroir d'une pyramide, il est réfléchi
de 90° et poursuit sa route :
[Face-miroir](https://ibb.co/Xz8DFrL)
Si un rayon laser frappe la face non-mirroir d'une pyramide, la pyramide est détruite
et le laser ne va pas plus loin :
[Face non-miroir](https://ibb.co/nB4tsy4)
Lorsqu'un rayon laser frappe le côté ou la face arrière d'un anubis, l'anubis est détruit
et le laser ne va pas plus loin :
[Anubis](https://ibb.co/Pc4qDCS)

### 2.1.6. Gameplay

Les joueurs jouent l'un après l'autre. A son tour, chaque joueur doit :
• Déplacer OU tourner une pièce
• Tirer un rayon laser avec son sphinx
Le joueur a gagné si son laser éclaire le pharaon adverse.

### 2.1.7. Ressources vidéo

Voici quelques exemples vidéo qui illustrent à quoi votre jeu pourrait ressembler :
• [Khet on stream 1](https://www.youtube.com/watch?v=ZfJYFHriBKQ)
• [Khet on stream 2](https://www.youtube.com/watch?v=hwHhNUCKuo4)

### 2.2. Multijoueur

Votre jeu est obligatoirement multijoueur (aucune IA n'est demandée). Il doit cependant
proposer deux modes: Dans le premier mode, les deux joueurs s'affrontent à tour de
rôle sur le même ordinateur. Dans le second mode ils s'affrontent en réseau. Dans
ce cas l'un des joueurs crée une partie et l'autre la rejoint. Il doit pour cela connaître
l'adresse IP du joueur qui crée la partie.

## 3. Livrables

Vous devrez rendre les éléments suivants:
• Une archive zip avec le code source de votre projet. Le cas échéant, le code source
doit être accompagné du système de compilation (fichier projet, Makefile, ...)
• La documentation du projet qui explique vos choix et/ou décisions d'implémentation
concernant :
• Le moteur graphique
• Les choix algorithmiques (structures de données pour le plateau de jeu, les
pièces, la trajectoire du laser,...)

## 4. Grille d'évaluation

Le projet sera évalué selon la grille suivante, comprenant 120 points sur 100 :
• Documentation : 10 points
• Documentation technique: 10 points
• Moteur de jeu : 20 points
• Design global : 4 points
• Affichage des trajectoires des lasers : 4 points
• Sélection d'une configuration initiale : 4 points
• Fin de jeu et retour à l'écran principal : 4 points
• Système de menus: 4 points
• Multijoueur : 20 points
• Deux joueurs peuvent s'affronter sur la même machine : 5 points
• Deux joueurs peuvent s'affronter en réseau : 15 points
• Gameplay : 30 points
• Le joueur peut sélectionner/désélectionner une pièce : 3 points
• Lorsqu'une pièce est sélectionnée, les destinations et rotations possibles sont
mises en évidence : 3 points
• Lorsqu'une pièce est sélectionnée, le joueur peut choisir entre la déplacer et
la tourner : 3 points
• Les pièces se déplacent correctement vers une case adjacente libre : 3 points
• Un scarabée peut échanger sa position avec un Anubis ou une pyramide : 3
points
• Les pièces tournent : 2 points
• Le joueur peut activer son laser : 2 points
• Un rayon laser est réfléchi par un scarabée : 3 points
• Un rayon laser est réfléchi par une pyramide ou la détruit en fonction de la face
qu'il touche : 3 points
• Un rayon laser est absorbé par une anubis ou le détruit en fonction de la face
qu'il touche : 3 points
• Un rayon laser détruit un pharaon : 2 points
• Editeur de positions initiales : 20 points
• L'utilisateur peut choisir la position des pièces : 7 points
• L'utilisateur peut choisir l'orientation des pièces : 7 points
• L'utilisateur peut sauvegarder/éditer/renommer/supprimer les configurations
qu'il a crée : 6 points
• Bonus: 20 points
• Fonctionnalités supplémentaires réalisées par les étudiants : 20 points
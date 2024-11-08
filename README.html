<!DOCTYPE html><html><head><meta charset="utf-8"><title>Untitled Document.md</title><style></style></head><body id="preview">
<h3 class="code-line" data-line-start=0 data-line-end=1 ><a id="1_Introduction_0"></a>1. Introduction</h3>
<p class="has-line-data" data-line-start="2" data-line-end="12">“Good Times With Good Friends” est un éditeur de jeux vidéos spécialisé dans<br>
l’adaptation de jeux de société. Leur prochain projet est de réaliser une version<br>
électronique du jeu “Khet”. Khet est un jeu de stratégie pour deux joueurs qui rappelle<br>
les échecs, mais basé sur la réflexion d’un rayon laser.<br>
Votre équipe a été sélectionnée pour réaliser le développement.<br>
Vous pouvez utiliser le langage et les libraires de votre choix comme Python/Pygame<br>
ou C/SDL. Votre jeu doit pouvoir fonctionner sur l’une des trois plateformes majeures:<br>
Windows, Linux et MacOS.<br>
Le thème original de Khet est celui de l’ancienne Egypte, mais vous êtes libres d’en<br>
changer si vous le souhaitez.</p>
<h2 class="code-line" data-line-start=13 data-line-end=14 ><a id="2_Expression_fonctionnelle_13"></a>2. Expression fonctionnelle</h2>
<h3 class="code-line" data-line-start=14 data-line-end=15 ><a id="21_Le_jeu_14"></a>2.1. Le jeu</h3>
<p class="has-line-data" data-line-start="16" data-line-end="21">Le plateau de jeu est composé de 8 lignes et 10 colonnes. Le but principal du jeu<br>
est d’éclairer le pharaon adverse en utilisant lasers et miroirs. Certaines cases sont<br>
réservés à un joueur en fonction de leur couleur (cases rouges pour le joueur rouge,<br>
cases grises pour le joueur gris) :<br>
<a href="https://ibb.co/4SZfLTZ">plateau de jeu</a></p>
<p class="has-line-data" data-line-start="22" data-line-end="23">Les illustrations suivantes et certaines portions du texte sont tirées des <a href="https://www.boardspace.net/khet/rules_english.pdf">règles</a> officielles. N’hésitez pas à les consulter.</p>
<h3 class="code-line" data-line-start=24 data-line-end=25 ><a id="211_Les_pices_24"></a>2.1.1. Les pièces</h3>
<p class="has-line-data" data-line-start="26" data-line-end="39">Il y a deux sets de pièces, les rouges et les grises. Chaque joueur choisi un set.<br>
Chaque joueur dispose des pièces suivantes :<br>
• Pharaon (1 exemplaire) : S’il est touché par un rayon laser venant de n’importe<br>
quelle direction, le joueur perd la partie.<br>
• Sphinx (1 exemplaire) : Il éclaire dans une direction. Il est toujours positionné dans<br>
le coin de plateau qui lui est attribué et ne peut pas se déplacer. Il absorbe les<br>
rayons lasers venant de toutes les directions.<br>
• Scarabée (2 exemplaires) : Il réfléchi les rayons lasers venant de toutes les<br>
directions.<br>
• Pyramide (7 exemplaires) : Elle réfléchi les rayons lasers sur deux directions mais<br>
est détruite par les rayons venant des deux autres.<br>
• Anubis (2 exemplaires) : Il absorbe les rayons lasers sur une direction mais est<br>
détruit par les rayons venant sur les trois autres.</p>
<p class="has-line-data" data-line-start="40" data-line-end="41"><a href="https://ibb.co/XF7HLSc">Schématisation des pièces</a></p>
<h3 class="code-line" data-line-start=42 data-line-end=43 ><a id="212_Rotations_42"></a>2.1.2. Rotations</h3>
<p class="has-line-data" data-line-start="44" data-line-end="49">Chaque pièce est orientée (nord/sud/est/ouest) et peut être tournée de 90 degrés (1/4<br>
de tour) dans n’importe quel sens. Tourner de 180 degrés (passer du nord au sud par<br>
exemple) ne pourra donc se faire qu’en plusieurs tours de jeu.<br>
Le sphinx doit être orienté de manière à ce que son rayon laser soit sur le plateau de<br>
jeu. Depuis sa position imposée (coin de plateau), il n’a que deux orientation possibles.</p>
<h3 class="code-line" data-line-start=50 data-line-end=51 ><a id="213_Dplacements_50"></a>2.1.3. Déplacements</h3>
<p class="has-line-data" data-line-start="52" data-line-end="58">Les déplacements ne changent pas l’orientation des pièces.<br>
Le sphinx ne peut pas se déplacer.<br>
Les autres pièces peuvent se déplacer vers l’une des 8 cases adjacentes, pourvu<br>
qu’elle soit vide et qu’elle ne soit pas de la couleur adverse (voir section 2.1).<br>
Un scarabée peut se déplacer sur une case occupée par un anubis ou une pyramide<br>
(peu importe sa couleur). Dans ce cas il échangera sa position avec la pièce concernée.</p>
<h3 class="code-line" data-line-start=59 data-line-end=60 ><a id="214_Configurations_initiales_59"></a>2.1.4. Configurations initiales</h3>
<p class="has-line-data" data-line-start="61" data-line-end="62">Il y a trois configurations de départ standards :</p>
<ol>
<li class="has-line-data" data-line-start="63" data-line-end="65">Classique:</li>
</ol>
<p class="has-line-data" data-line-start="65" data-line-end="66"><a href="https://ibb.co/6NwGqXQ">Configuration Classique</a></p>
<ol start="2">
<li class="has-line-data" data-line-start="67" data-line-end="69">Imhotep:</li>
</ol>
<p class="has-line-data" data-line-start="69" data-line-end="70"><a href="https://ibb.co/fx0h4Qq">Configuration Imhotep</a></p>
<ol start="3">
<li class="has-line-data" data-line-start="71" data-line-end="73">Dynasty:</li>
</ol>
<p class="has-line-data" data-line-start="73" data-line-end="74"><a href="https://ibb.co/YDkrRWb">Configuration Dynasty</a></p>
<p class="has-line-data" data-line-start="75" data-line-end="82">Les cases marquées en rouge (toutes les cases de la première colonne et la première<br>
et dernière case de l’avant dernière colonne) appartiennent au joueur rouge. Le joueur<br>
gris ne peut pas y mettre ses pièces. De même pour les cases en gris qui appartiennent<br>
au joueur gris et sont interdites au joueur rouge.<br>
Votre jeu doit permettre de choisir entre les trois configuration initiales. Vous<br>
devrez également permettre à l’utilisateur de créer des configurations de début<br>
personnalisées, qui seront ajoutées à la liste des propositions de départ.</p>
<h3 class="code-line" data-line-start=83 data-line-end=84 ><a id="215_Rayons_83"></a>2.1.5. Rayons</h3>
<p class="has-line-data" data-line-start="85" data-line-end="94">Lorsqu’un rayon laser atteint un scarabée ou la face miroir d’une pyramide, il est réfléchi<br>
de 90° et poursuit sa route :<br>
<a href="https://ibb.co/Xz8DFrL">Face-miroir</a><br>
Si un rayon laser frappe la face non-mirroir d’une pyramide, la pyramide est détruite<br>
et le laser ne va pas plus loin :<br>
<a href="https://ibb.co/nB4tsy4">Face non-miroir</a><br>
Lorsqu’un rayon laser frappe le côté ou la face arrière d’un anubis, l’anubis est détruit<br>
et le laser ne va pas plus loin :<br>
<a href="https://ibb.co/Pc4qDCS">Anubis</a></p>
<h3 class="code-line" data-line-start=95 data-line-end=96 ><a id="216_Gameplay_95"></a>2.1.6. Gameplay</h3>
<p class="has-line-data" data-line-start="97" data-line-end="101">Les joueurs jouent l’un après l’autre. A son tour, chaque joueur doit :<br>
• Déplacer OU tourner une pièce<br>
• Tirer un rayon laser avec son sphinx<br>
Le joueur a gagné si son laser éclaire le pharaon adverse.</p>
<h3 class="code-line" data-line-start=102 data-line-end=103 ><a id="217_Ressources_vido_102"></a>2.1.7. Ressources vidéo</h3>
<p class="has-line-data" data-line-start="104" data-line-end="107">Voici quelques exemples vidéo qui illustrent à quoi votre jeu pourrait ressembler :<br>
• <a href="https://www.youtube.com/watch?v=ZfJYFHriBKQ">Khet on stream 1</a><br>
• <a href="https://www.youtube.com/watch?v=hwHhNUCKuo4">Khet on stream 2</a></p>
<h3 class="code-line" data-line-start=108 data-line-end=109 ><a id="22_Multijoueur_108"></a>2.2. Multijoueur</h3>
<p class="has-line-data" data-line-start="110" data-line-end="115">Votre jeu est obligatoirement multijoueur (aucune IA n’est demandée). Il doit cependant<br>
proposer deux modes: Dans le premier mode, les deux joueurs s’affrontent à tour de<br>
rôle sur le même ordinateur. Dans le second mode ils s’affrontent en réseau. Dans<br>
ce cas l’un des joueurs crée une partie et l’autre la rejoint. Il doit pour cela connaître<br>
l’adresse IP du joueur qui crée la partie.</p>
<h2 class="code-line" data-line-start=116 data-line-end=117 ><a id="3_Livrables_116"></a>3. Livrables</h2>
<p class="has-line-data" data-line-start="118" data-line-end="126">Vous devrez rendre les éléments suivants:<br>
• Une archive zip avec le code source de votre projet. Le cas échéant, le code source<br>
doit être accompagné du système de compilation (fichier projet, Makefile, …)<br>
• La documentation du projet qui explique vos choix et/ou décisions d’implémentation<br>
concernant :<br>
• Le moteur graphique<br>
• Les choix algorithmiques (structures de données pour le plateau de jeu, les<br>
pièces, la trajectoire du laser,…)</p>
<h2 class="code-line" data-line-start=127 data-line-end=128 ><a id="4_Grille_dvaluation_127"></a>4. Grille d’évaluation</h2>
<p class="has-line-data" data-line-start="129" data-line-end="165">Le projet sera évalué selon la grille suivante, comprenant 120 points sur 100 :<br>
• Documentation : 10 points<br>
• Documentation technique: 10 points<br>
• Moteur de jeu : 20 points<br>
• Design global : 4 points<br>
• Affichage des trajectoires des lasers : 4 points<br>
• Sélection d’une configuration initiale : 4 points<br>
• Fin de jeu et retour à l’écran principal : 4 points<br>
• Système de menus: 4 points<br>
• Multijoueur : 20 points<br>
• Deux joueurs peuvent s’affronter sur la même machine : 5 points<br>
• Deux joueurs peuvent s’affronter en réseau : 15 points<br>
• Gameplay : 30 points<br>
• Le joueur peut sélectionner/désélectionner une pièce : 3 points<br>
• Lorsqu’une pièce est sélectionnée, les destinations et rotations possibles sont<br>
mises en évidence : 3 points<br>
• Lorsqu’une pièce est sélectionnée, le joueur peut choisir entre la déplacer et<br>
la tourner : 3 points<br>
• Les pièces se déplacent correctement vers une case adjacente libre : 3 points<br>
• Un scarabée peut échanger sa position avec un Anubis ou une pyramide : 3<br>
points<br>
• Les pièces tournent : 2 points<br>
• Le joueur peut activer son laser : 2 points<br>
• Un rayon laser est réfléchi par un scarabée : 3 points<br>
• Un rayon laser est réfléchi par une pyramide ou la détruit en fonction de la face<br>
qu’il touche : 3 points<br>
• Un rayon laser est absorbé par une anubis ou le détruit en fonction de la face<br>
qu’il touche : 3 points<br>
• Un rayon laser détruit un pharaon : 2 points<br>
• Editeur de positions initiales : 20 points<br>
• L’utilisateur peut choisir la position des pièces : 7 points<br>
• L’utilisateur peut choisir l’orientation des pièces : 7 points<br>
• L’utilisateur peut sauvegarder/éditer/renommer/supprimer les configurations<br>
qu’il a crée : 6 points<br>
• Bonus: 20 points<br>
• Fonctionnalités supplémentaires réalisées par les étudiants : 20 points</p>

</body></html>
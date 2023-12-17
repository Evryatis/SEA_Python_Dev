# SAE 1.01 - Implémentation

## BOUAKEL Yann, RODRIGUES FERNANDES Dani

### Les joueurs et les missions

Les joueurs et les missions sont représentés par des classes qui leur correspondent.

#### Les joueurs

Les joueurs sont représentés par la classe `Player`, contenue dans le module `Player.py` du fichier ressource.  
Ils ont plusieurs attributs, à savoir leur `coding level`, leur énergie actuelle (`energy`), niveau d'énergie maximal (`max_energy`), et ses coordonnées.

La classe `Player` a également plusieurs méthodes, permettant par exemple d'incrémenter le nombre de bitcoins ou encore d'afficher les statistiques du joueur.

### Le module `ReadAndWrite`

Le module `ReadAndWrite` contient des fonctions permettant de lire et écrire dans des fichiers contenant les attributs des missions. Ceux-ci fonctionnent comme expliqué en cours magistral par M. David Auger.

### La version console (main.py)

#### Comment y jouer ?

La version console se joue dans le style de certains jeux rétro en DOS :
on entre ses actions au clavier (e. g. `move`) et parfois un argument (e. g. `up`, `left`).  
`move up` permet donc de se déplacer d'une case vers le haut.

Il existe plusieurs commandes, comme on peut le voir dans l'ensemble (type `set`) qui contient toutes les commandes du jeu, ainsi que les `upgrades` qui correspondent aux attributs du joueur que l'on peut améliorer (`energy` pour le niveau d'énergie max et `coding` pour le niveau de codage).

Il y a également une commande `help` qui affiche toutes les commandes de la version console du jeu.

On peut modifier le nombre de joueurs en changeant l'attribut `player_amount` dans l'appel de la fonction `game_loop` tout en bas du fichier, et charger le fichier mission que l'on veut en changeant le chemin dans les appels `rw.read_map_file`.

#### Implémentation

Le *game loop* a été implémenté avec une fonction qui prend plusieurs arguments, comme une liste de missions qui est chargée avant le lancement de la partie, ainsi qu'un nombre de joueurs et la `game map` qui est une liste de listes dont chaque élément correspond à une case dans le jeu.

### La version graphique (main_gui.py)

La version graphique fonctionne uniquement avec un seul joueur. 

Les status en haut à droite ne se mettent à jour que lorsque le joueur se déplace.

En plus de Tkinter, PIL fut utilisé pour representer le joueur. Comme cela est une librairie que nous avons déjà utilisées dans l'iut je pense que cela ne causera aucun soucis..


#### Comment y jouer ?

Il est seulement possible d'y jouer avec les flèches directionnelles. Il suffit de se déplacer vers les cases violettes, qui representent les missions, cliquer "work", et travailler dessus.
Cliquer "work" sur une mission dépense de l'énergie. Quand vous êtes a cours d'energie, il faut aller sur le carré vert, et cliquer "rest". Cela vous repose.


#### Implémentation

Le code source qui implémente le niveau 0 n'est pas utilisé dans cette version graphique. Il y a eu une sécession pendant la programmation, et nous avions du "branch" le code en deux parties distinctes. Cela  à été du a un malheureux problème de structure irrécupérable. Il aurait fallu mieux coordonner les deux codes, cela n'a pas été fait, erreur de débutant, car cela nous aurait bien simplifiées la tache (l'un s'occupait du graphique, l'autre du jeu de base)

La partie graphique est divisée en deux parties primaire.

gui_player, qui s'occupe principalement des fonctions contenant les donnés du joueurs, ainsi que main_gui, qui est la game_loop ainsi que le fichier créateur du canvas et du "grid", dans lequel le jeu se passe.

La carte, restant toujours la même, (un grid de 20x20), les niveaux suivent une structure de donnée telle que :

15 8 1 1

15 et 8 sont les coordonnées. 1 symbolise que c'est une mission, et le 1 suivant symbolise sa difficulté. Cela n'est fait que pour les missions, ainsi les données marquées dans le fichier "map1.txt" s'afficheront en tant que missions sur la carte. Il faut cependant toujours avoir une donnée 10, 10, 2, 0, pour le game-center, sans-lequel le jeu ne marche pas du tout.

Les fonctions de main_gui furent extrêmement compliquées à implementer, nottemment "move", car il fallait s'assurer que le joueur ne sorte pas de la carte. Je m'en sorti grâce a une variable destination. En revanche, check_mission, qui permet de vérifier si le joueur est bel et bien sur une mission, et lui faire travailler dessus, fut un enfers dont seul chatgpt put me sauver.

Autrement, le jeu est sur un "grid" de tkinter, posé lui-même sur un "canvas", une sorte de widget très flexible de tkinter.

Le __init__ de gui_player est donc un énorme mur de code, principalement pour afficher l'interface.

### Conclusion

Nous avons rencontrés de nombreuses difficultés, et de nombreuses relectures, ainsi que beaucoup d'entraide, et des recherches sur stackoverflow ont dûe être réalisées. Notemment, la gestion des missions sur interface graphique fut compliquée, mais si la structure de code n'avait pas été scindée en deux, cela aurait été plus simple, et plus réussi. Nous y penserons mieux la prochaine fois.

Nous sommes cependant satisfait du resultat. Nous espererons que cela sera également votre cas.



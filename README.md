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

#### Comment y jouer ?

#### Implémentation

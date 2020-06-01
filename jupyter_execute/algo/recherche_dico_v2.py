La recherche dichotomique
---

# Principe
On souhaite rechercher une valeur $x$ dans un tableau $t$ trié (*par ordre croissant pour se fixer les idées*). L'idée principale est de comparer $x$ avec la valeur située au milieu du tableau:  
* si elle est plus petite, il suffit de restreindre la recherche dans la partie gauche du tableau;
* sinon, on la restreint à la partie droite de $t$.
* ou alors on a trouvé $x$

En répétant ce procédé on divise la zone de recherche par deux à chaque fois. Il s'agit d'une application du principe *diviser pour régner*.

# Implémentation en python

def est_trie(t):
    """
    Vérifie si t est trié et renvoie un booléen comme réponse
    """
    return all(t[i] <= t[i + 1] for i in range(len(t) - 1))
        

def recherche_dichotomique(x, t):
    """
    Renvoie la position de x dans le tableau t trié; None si non trouvé
    Précondition: t trié
    """
    assert est_trie(t), "Erreur: tableau non trié"
    g = 0#gauche
    d = len(t) - 1#droit
    while g <= d:
        m = (g + d) // 2
        if x > t[m]:
            g = m + 1
        elif x < t[m]:
            d = m - 1
        else:
            return m
    return None

Initialement, `g = 0` et `d = len(t) - 1`. On calcule l'index central $m$ du tableau (*ligne 8*) en effectuant une **division entière**.  
Ensuite on compare $x$ à `t[m]`. Suivant le résultat de la comparaison, on ajuste la borne gauche $g$ ou droite $d$ de la zone de recherche.  

Si `x == t[m]` (*ligne 13*), on a trouvé $x$ et on renvoie son index.  Il se peut que l'on sorte de la boucle `while` (si `g > d`, c'est dire que la zone de recherche est vide), dans ce cas, on signale l'absence de $x$ en retournant `None` (*ligne 15*).

# Terminaison de l'algorithme

Lorsqu'un programme contient une boucle `while` il est suceptible de **diverger** (*on dit aussi qu'il peut entrer dans une boucle infinie*). Pour montrer l'arrêt de la boucle, on utilise une technique de raisonnement appelé **technique du variant de boucle**. Il s'agit de trouver parmi les éléments du programme une quantité:  
* entière;
* positive;
* qui décroit strictement à chaque tour de boucle.

|                 	| g 	| d 	| m 	| t[m] 	| d-g 	| trouvé ? 	|
|-----------------	|---	|---	|---	|------	|-----	|----------	|
| Initialisation  	|   	|   	|   	|      	|     	|          	|
| Fin itération 1 	|   	|   	|   	|      	|     	|          	|
| Fin itération 2 	|   	|   	|   	|      	|     	|          	|
| Fin itération 3 	|   	|   	|   	|      	|     	|          	|

Soit `t = [1,7,8,9,12,15,15,22,30,31]`. On recherche $x=15$ dans `t`.  
Compléter le tableau ci-dessus. Conclure
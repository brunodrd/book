Tri par insertion
=============

# Principe
Voir le principe à l'adresse: 
[Algorithmes de tri](http://lwh.free.fr/pages/algo/tri/tri_insertion.html)

L'idée principal est de **parcourir le tableau de la gauche vers la droite, en maintenant la partie déjà triée sur sa gauche**. Concrètement, on va décaler d'une case vers la droite tous les éléments déjà triés, qui sont plus grands que l'élément à classer, puis déposer ce dernier dans la case libérée.  

```{image} ../img/tri_insertion_principe.png
alt: principe
```

# Implémentation en python

def tri_insertion(t):
    """
    Trie le tableau t par ordre croissant
    """
    for i in range(1,len(t)):
        elt_a_classer = t[i]
        j = i
        #décalage des éléments du tableau pour trouver la place de t[i]
        while j>0 and t[j - 1] > elt_a_classer:
            t[j] = t[j - 1]
            j = j - 1
        #on insère l'élément à sa place
        t[j] = elt_a_classer

# Validité de l'algorithme
Au début de chaque itération d'index `i`, le sous tableau `t[0..i-1]` est trié (attention, on fait référence aux éléments d'index 0 à `i-1` **inclus, ce n'est pas une notation python** !). Cette propriété est appelée **invariant de boucle**. L'invariant est une propriété qui doit:  

## être vérifié avant la première itération (initialisation)
Lorsqu'on est en ligne 5 la première fois, `i = 1` et cette propriété se traduit par: la tableau `t[0]` est trié. Ce qui est vrai évidemment car on n'a qu'un seul élément.

## être conservé (conservation)
**Si l'invariant est vrai avant une itération, il l'est aussi avant la prochaine**. 

Ici pour une itération d'index `i` donné, on va décaler les `t[i-1]`, `t[i-2]`, .. etc, vers la droite pour trouver la place de `t[i]`. On place alors `t[i]` et le sous tableau `t[0..i]` est trié. 

Juste avant d'entamer une nouvelle itération (au début de la boucle `for`) on incrémente `i`. Ainsi au début de cette nouvelle itération d'index `i+1` le sous tableau `t[0..i]` est trié et **l'invariant est conservé**.

Par ailleurs, la combinaison de l'invariant avec la **terminaison** de la boucle permet de conclure à la validité, on dit aussi **correction totale**, de l'algorithme. 

Dans notre cas, lorsque la boucle termine, `i = len(t)`. Si on substitue cette valeur dans l'expression de l'invariant, on a en sortie de boucle: `i = len(t)` et le sous tableau `t[0..len(t)-1]` est trié, soit: 

**le tableau t est trié, l'algorithme est correct**.

# Efficacité: complexité temporelle de l'algorithme

Le temps d'exécution de la procédure `tri_insertion` dépendra des instructions et du nombre fois que ces instructions seront exécutées. C'est la nature du tableau `t` qui fixera ce nombre. De plus, on considèrera pour simplifier que le coût d'une instruction est constant.

Soit $n$ la taille de l'entrée. 

Dans le meilleur des cas, on ne passe pas dans la boucle `while` (c'est possible si `t` est ... déjà trié par ordre croissant!) et on peut montrer que le temps d'exécution a une expression de la forme $a\times n +b$ avec $a$ et $b$ des constantes (en fait, il y a $n-1$ passages dans la boucle `for`). La complexité est alors **linéaire**.

Le pire des cas se produit si `t` est entièrement trié par ordre décroissant. Le nombre de fois que la boucle `while` est exécutée est alors:

$$ N_1=\dfrac{n}{2}\times(n-1)$$

Chaque instruction de la boucle étant exécutée:

$$ N_2=\dfrac{1}{2}\times(n-1)\times (n-2)$$

fois. Les instructions en dehors de la boucle `while` étant exécutées $n-1$ fois.
Il est alors clair que le temps d'exécution total sera une fonction du type $a'\times n^2 + b'\times n +c'$. 

On dit alors que la *complexité* dans le pire des cas du tri par insertion est **quadratique** (*on rencontre quelques fois l'expression "la complexité est en* $O(n²)$").

```{note}
Voir le document "Complexité" en complément
```

---
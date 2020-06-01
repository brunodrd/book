Recherche dans un tableau
---

# Introduction

Pour *Thomas Cormen*, très grand professeur d'informatique, un algorithme est **une procédure de calcul, bien définie, qui prend en entrée une valeur ou un ensemble de valeurs, et qui donne en sortie une valeur ou un ensemble de valeurs**. C'est un outil permettant de résoudre un problème de calcul bien spécifié.  
Un algorithme doit se terminer dans un temps raisonnable et doit résoudre correctement le problème donné. Ces deux propriétés sont respectivement nommées:
* complexité
* correction  

Cette première leçon d'algorithmique sera orientée vers la recherche (*séquentielle*) d'un élément dans un tableau.

# Parcours séquentiel d'un tableau

## Recherche d'une occurence

Soit le problème suivant: étant donné un tableau `t` de $n$ éléments, écrire un algorithme qui permet de dire si un élément $x$ appartient à ce tableau.   
Le problème: $x$ appartient-il au tableau ?  

Les entrées: un tableau `t` et un élément `x`;  
La sortie: une réponse vraie ou fausse (`True` ou `False`)  

*Une* solution:  
```
fonction appartient(x, t):

Entrées:
- t: tableau
- x: élément de même type que les éléments du tableau t
Sortie: booléen (réponse)

Variable: n, entier naturel

n = taille(t)
Pour i allant de 0 à n-1 
    Si t[i] = x  
        retourner Vrai  
Retourner Faux
```

#Implémentation en python
def appartient_v1(x, t):
    """
    retourne un booléen correspondant à la présence x dans t (ou non);
    x: élément de même type que les éléments de t
    """
    n = len(t)
    for i in range(n):
        if t[i] == x:
            return True
    return False

appartient_v1(-5, [5, 10, 15, 20])

**Travail**: réaliser l'implémentation en python en utilisant une boucle `while` plutôt qu'une boucle `for`.

def appartient_v1b(x, t):
    """
    retourne un booléen correspondant à la présence x dans t (ou non);
    t: tableau d'entiers
    x: élément de même type que les éléments de t
    """
    n = len(t)
    i = 0
    while i < n and t[i] != x:
        i = i + 1
    if i < n:
        return True
    return False
    

appartient_v1b(-1, [5, 10, 15, 20])

*Remarque*: on aurait pu boucler sur éléments plutôt que les indices; cela nous dispense de la variable n.

def appartient_v2(x, t):
    """
    retourne un booléen correspondant à la présence x dans t (ou non);
    x: élément de même type que les éléments de t
    """
    for t_i in t:
        if t_i == x:
            return True
    return False

## Recherche d'un extrémum

Deuxième problème: étant donné un tableau `t` de $n$ éléments, écrire un algorithme qui permet de trouver le minimum parmi les éléments de ce tableau.   
Le problème: quellle est la plus petite valeur du tableau ? 

```
fonction minimum(t):
L'entrée: un tableau t;  
La sortie: le plus petit élément de t  
Variables: 
    n, entier naturel
    mini, même type que les éléments de t
Précondition: t non vide

n = taille(t)
mini = t[0]
Pour i allant de 1 à n-1:
    Si t[i] <= mini
        mini = t[i]
retourner mini
```

def minimum(t):
    """
    Retourne le plus petit élément de t
    """
    assert t != [], "Erreur: tableau vide"
    n = len(t)
    mini = t[0]
    for i in range(1,n):
        if t[i] < mini:
            mini = t[i]
    return mini

minimum([5, 10, -15, 20])

minimum([0, 12])

**Travail**: écrire et tester l'implémentation d'une fonction retournant l'élément **le plus grand** de `t`

## Calcul d'une moyenne

Troisième problème: étant donné un tableau `t` de $n$ éléments, écrire un algorithme qui permet de trouver la moyenne des éléments de ce tableau.   
Le problème: quellle est la valeur moyenne des éléments du tableau ?

```
fonction moyenne(t):
L'entrée: un tableau t de flottants;  
La sortie: la moyenne de tous les éléments de t  
Variables: 
    n, entier naturel
    somme, flottant
Précondition: t non vide

n = taille(t)
somme = 0
Pour i allant de 0 à n-1:
    somme = somme + t[i]
retourner somme / n
```

**Travail**: implémenter cet algorithme en python

def moyenne(t):
    """
    Renvoie la moyenne des éléments d'un tableau t non vide;
    """
    assert len(t) != 0, "Erreur: tableau vide"
    n = len(t)
    somme = 0
    for i in range(n):
        somme = somme + t[i]
    return somme / n

moyenne([5.5, 10.0, 15.0, 19.5])

## Coût des algorithmes

La boucle est parcourue:
* $n$ fois dans le pire des cas (*si x n'appartient pas au tableau*) dans le problème 1
* $n-1$ fois dans le problème 2;
* $n$ fois dans le problème 3;  

Le nombre d'opérations effectuées dépend de la taille de l'entrée $n$, plus exactement est proportionnel à $n$ (ou $n-1$). On dit que la complexité de ces algorithmes est **linéaire**.


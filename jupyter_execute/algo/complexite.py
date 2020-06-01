Complexité
=========

# Introduction: complexité ou coût d'un algorithme
Pour traiter un même problème, il existe souvent plusieurs algorithmes. Un critère de choix possible est le *temps d'exécution* le plus faible.  
**Le temps d'exécution caractérise le coût -appelé complexité- d'un algorithme**.  
En réalité on ne va pas mesurer réellement le temps d'exécution mais plutôt utiliser un *modèle* simplifié, indépendant de la machine utilisée et dont l'unité de mesure du coût est une *opération* (affectation, comparaison, etc..)

# Complexité linéaire
Pour exprimer le coût d'un algorithme, on peut évaluer le nombre d'opérations effectué.  

Exemple: le problème est d'afficher les diviseurs d'un entier $n$. On propose l'algorithme naïf ci-dessous, exprimé en python. 

```python
def diviseurs(n):
    for i in range(1, n+1):
        if n % i == 0:
            print(i)
```
On a: $n$ incrémentations et $n$ tests à la ligne 2, $n$ calculs de restes de divisions et $n$ tests à la ligne 3 et au plus $n$ affichages soit $5n$ opérations au maximum (on dit aussi dans le *pire de cas* ou *worst case* en anglais).  
En général, le coût d'un algorithme varie en fonction d'un paramètre appelé **taille de l'entrée**, ici le nombre $n$. L'algorithme naïf présenté a un coût évalué à $5n$ opérations.  
Il n'est pas utile en première NSI d'aller vers un niveau de détail tel que celui qui vient d'être présenté. On dira simplement que:

**le nombre d'opérations de cet algorithme est proportionnel à n ou encore qu'il a une complexité linéaire**.  


# Autres cas courants
Si la complexité ne **dépend pas** de la taille de l'entrée, l'algorithme a une **complexité constante**.


Existe-t-il des algorithmes plus performants que ceux ayant une complexité linéaire ?  
**Oui**, les algorithmes ayant une **complexité logarithmique**. La fonction logarithme est une fonction qui croît très lentement.  

Existe-t-il des algorithmes moins performants que ceux ayant une complexité linéaire ?  
**Oui**, les algorithmes ayant une **complexité quadratique, cubique, etc** c'est-à-dire des algorithmes dont le nombre d'opérations est une fonction du carré de la taille de l'entrée, du cube, etc.

*Ordre de grandeur du temps d'exécution sur un ordinateur personnel de quelques algorithmes dont la complexité a été évoquée ci-dessus* 

| Nom courant   	| Temps pour une taille n = 1 million 	|
|---------------	|:-----------------------------------:	|
| logarithmique 	|                10 ns                	|
| linéaire      	|                 1 ms                	|
| quadratique   	|                1/4 h                	|
| cubique       	|                30 ans               	|

# Quelques exemples
Donner la complexité des exemples ci-dessous.

def table1(n):
    for i in range(11):
        print(i * n)

def table2(n):
    for i in range(n):
        print( i * i)
        
def table3(n):
    for i in range(n):
        for j in range(n):
            print(i * j, end=" ")
        print()

---
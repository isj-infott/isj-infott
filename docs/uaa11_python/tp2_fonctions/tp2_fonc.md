# UAA11 TP2 - Les fonctions

**Notions abordées** : 

- définition d'une fonction ( `def` )

- paramètres lors de l'appel ( entrées ), renvoi du résultat ( sorties ) ( `return` )

- variables locales, variables globales ( `global` )

**Mémo**

- Prends connaissance du cours sur les [**fonctions**](NSI Première Partie 1 Chapitre 3 Fonctions.pdf), fais les activités ci-dessous puis réponds aux questions **QCM** du pdf.
.

- Tu peux tester ton code avec l'IDE du chapitre "5. Bac à sable"

- Complète ton fichier "**memo**" que tu complèteras avec ce que tu as appris au fur et à mesure de ton avancement dans le cours.

## 1. Introduction avec un exemple

??? question "Test1: Appel de la fonction rectange"

    On considère la fonction ci-dessous. 

    Exécute le code. Il ne se passe rien de visible : la fonction a juste été mise en mémoire.

    Pour pouvoir l'utiliser, il faut l'appeler. 

    {{IDE('nsi/test1_rect', MAX = 8)}}

    Ecris dans le terminal ci-dessus les codes suivants et observe les sorties obtenues :

    ```python
        >>> perimetre_rectangle
    ```

    ```python
        >>> perimetre_rectangle()
    ```

    ```python
        >>> perimetre_rectangle
    ```

    ```python
        >>> perimetre_rectangle(long,larg)
    ```

    ```python
        >>> perimetre_rectangle(3)
    ```

    ```python
        >>> perimetre_rectangle(3,4)
    ```
    Lorsque l'on passe des valeurs aux paramètres d'une fonction, celles-ci peuvent être définies directement au moment de l'appel comme dans la cellule précédente, mais également à l'aide de variables préalablement définies.

    Exécute la cellule suivante :

    ```python
        >>> a = 2
        >>> b = 5
        >>> perimetre_rectangle(a,b)
    ```
    Observons à présent avec Python Tutor ce qu'il se passe au niveau des variables lors de l'exécution de la cellule ci-dessus.
    
    Pour cela, exécute le code  et visualise pas à pas son exécution avec [Python Tutor en ligne](https://pythontutor.com/iframe-embed.html#code=def%20perimetre_rectangle%28long,%20larg%29%3A%0A%20%20%20%20perimetre%20%3D%202*%28long%20%2B%20larg%29%0A%20%20%20%20return%20perimetre%0A%0Aa%20%3D%202%0Ab%20%3D%205%0Aperimetre_rectangle%28a,b%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false). Regarde en particulier les blocs à droite qui sont créés et détruits.

    !!! warning "A retenir"
        Les variables situées à l'extérieur d'une fonction sont appelées **variables globales** et les variables situées à l'intérieur d'une fonction (y compris les paramètres) sont appelées **variables locales**. A la fin de l'exécution d'une fonction, les variables locales sont détruites.

    !!! info "Remarque :"

        les variables globales et locales peuvent avoir le même nom. Mais, sauf type particulier comme les listes ou manipulations particulières que nous n'aborderons pas dans ce cours, elles n'ont pas de lien entre elles comme le montre l'exécution de la cellule suivante avec les variables globale et locale ` perimetre ` (on remarquera également sur cet exemple que si la fonction admet 2 paramètres avec des noms différents afin de les différencier, l'appel peut se faire avec les mêmes variables, c'est-à-dire les mêmes valeurs).

        ```python
            def perimetre_rectangle(long, larg):
            perimetre = 2*(long + larg)
            return perimetre

            >>> perimetre = 2
            >>> perimetre_rectangle(perimetre,perimetre)
        ```
    
    Dans les exemples ci-dessus, nous avons vu que la valeur qui est affichée en sortie est la valeur renvoyée par la fonction.  Souvent, il est utile de stocker cette valeur dans une variable afin de pouvoir la réutiliser ultérieurement.

    Exécute le code suivant avec [Python Tutor en ligne](https://pythontutor.com/iframe-embed.html#code=def%20perimetre_rectangle%28long,%20larg%29%3A%0A%20%20%20%20perimetre%20%3D%202*%28long%20%2B%20larg%29%0A%20%20%20%20return%20perimetre%0A%0Aa%20%3D%202%0Ab%20%3D%205%0Avaleur_perimetre%20%3D%20perimetre_rectangle%28a,b%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=311&rawInputLstJSON=%5B%5D&textReferences=false) et observe précisément ce qu'il se passe à l'étape 8 lorsque la fonction renvoie sa valeur et que son bloc est détruit.

    ```python
        def perimetre_rectangle(long, larg):
            perimetre = 2*(long + larg)
            return perimetre
        
        >> a = 2
        >>> b = 5
        >>> valeur_perimetre = perimetre_rectangle(a,b)
    ```
    !!! info "Remarque :"

        Lorsqu'une fonction renvoie plusieurs valeurs simultanément, on peut les affecter séparément à différentes variables. Ceci sera abordé dans l'activité pratique qui suit ce point de cours.

## 2. Comprendre et manipuler les fonctions

!!! info "Rappel sur les fonctions"

    Les fonctions sont une brique de base en programmation :

    1. on leur donne des informations en entrée, 
    2. elles exécutent des calculs en utilisant ces informations,
    3. elles renvoient un résultat en sortie.

    Un point important à comprendre est que lorsqu'on utilise des fonctions, on procède en **2 temps** :

    - dans un 1er temps, on les **définit**,
    - dans un 2nd temps, on effectue des **appels de fonction**.

    _Dans cette activité, toutes les fonctions que l'on va manipuler sont déjà entièrement écrites. Le but est de comprendre, d'une part, ce qu'elles calculent et ce qu'elles renvoient, et, d'autre part, de savoir quel type d'appel il faut effectuer pour répondre à tel ou tel problème._

??? question "Test2 : Fonction carre"

    ```python
        def carre(x):
        return x**2
    ```
    
    1. Quel est le mot-clé qui permet de définir une fonction ?
    2. Comment se nomme la fonction ?
    3. Que renvoie cette fonction ?
    4. Quelle instruction doit-on écrire pour calculer le carré de $42$ ?
    5. Quelle instruction doit-on écrire pour calculer le carré de $-12$ ?

    ??? tip "Solution"

        1. def
        2. carre
        3. le nombre passé en paramètre élevé au carré
        4. carre(42)
        5. carre(-12)

??? question "Test3 : Utilisation de la fonction carre"

    On souhaite affecter à la variable `ab` la valeur $8^2+(-3)^2$

    Quelle instruction écrire en utilisant la fonction carre du test2 ?

    ??? tip "Solution"

        ```python
        carre(8) + carre(-3)
        ```

??? question "Test4 : Comparaison"

    !!! info 

        On rappelle que l'instruction `a == b` renvoie `True` si les contenus des variables `a` et `b` sont égales, et `False` sinon.

    Ecrire une instruction permettant de comparer la valeur $8^{2} + (-3)^{2}$ et la valeur $8^{2} + 3^{2}$
    en utilisant la fonction de carre du test2.

    ??? tip "Solution"

        ```python
        carre(8) + carre(-3) == carre(8) + carre(3)
        ```

??? question "Test5 : Parité"

    ```python
        def est_pair(x):
        return x % 2 == 0
    ```

    1. Comment se nomme la fonction ?
    2. Que renvoie cette fonction ?
    3. Quel est l'intérêt de cette fonction ?
    4. Quelle instruction doit-on écrire pour savoir si le nombre $(-31)^{2}$ est pair ?
    5. Quelle instruction doit-on écrire pour savoir si le nombre est $12^2$ impair  ?

    ??? tip "Solution"

        1. est_pair 
        2. renvoie `True` si le reste de la division par 2 du nombre passé est nul, `False` s'il ne l'est pas
        3. déterminer si un nombre est pair ou impair
        4. est_pair(carre(-32))
        5. est_pair(carre(12))

??? question "Test6 : Opération"

    ```python
        def somme_produit (a,b):
        return ( a+b,a*b )
    ```

    1. Comment se nomme la fonction ?
    2. Que renvoie cette fonction ?
    3. Combien y a-t-il de paramètres ?
    4. Quelle instruction doit-on écrire pour calculer la somme et la produit des nombres $2,3$ et $-3,5$ ?
    5. Quelle instruction doit-on écrire pour affecter aux variables `somme` et `produit` la somme et le produit des nombres $6,8$ et $-7,5$ ?

    !!! warning "A retenir"

        Lorsque une fonction renvoie plusieurs résultats, on peut les affecter séparément dans des variables.

        Par exemple, si la fonction ` ma_fonction ` renvoie $n$ résultats, on peut affecter ces $n$ résultats dans $n$ variables `x1`, `x2`, ..., `xn` à l'aide de l'instruction
        
    ```python
        x1, x2, ..., xn = ma_fonction(...)
    ```

    ??? tip "Solution"

        1. somme_produit 
        2. renvoie la somme et le produit de 2 npmbres passés en paramètre
        3. 2 paramètres
        4. `somme_produit(2,3)`
        
            `somme_produit(-3,5)`
        5. somme, produit = somme_produit(6,8) et somme, produit = somme_produit(-7,5)
        
??? question "Test7 : Evolution des prix"

    {{IDE('nsi/test7_prix-evol')}}

    1. Que renvoie l'instruction `evolution_prix(5,2)` ? 
    
        Donne une interprétation concrète de ce résultat.
    2. Que renvoie l'instruction `evolution_prix(5,-3)` ? 
    
        Donne une interprétation concrète de ce résultat.
    3. Ecrirs dans la cellule ci-desous une séquence d'instructions utilisant cette fonction pour connaître le prix d'un article valant initialement $50$ euros et subissant tipivement une hausse de $5\%$ puis une baisse de $2\%$. 

## 3. Créer ses propres fonctions

!!! info "Rappel sur les fonctions"

    Les fonctions sont une brique de base en programmation :

    1. on leur donne des informations en entrée, 
    2. elles exécutent des calculs en utilisant ces informations,
    3. elles renvoient un résultat en sortie.

    Un point important à comprendre est que lorsqu'on utilise des fonctions, on procède en **2 temps** :

    - dans un 1er temps, on les **définit**,
    - dans un 2nd temps, on effectue des **appels de fonction**.

!!! example "Exemple"

    On **définit, dans un 1er temps,** une fonction appelée `aire_rectangle` :

    1. qui a 2 paramètres (c'est à dire 2 entrées) : `longueur` et `largeur`,
    2. qui effectue le calcul de l'aire du rectangle de longueur `longueur` et de largeur `largeur`
    3. et renvoie (c'est à dire produit en sortie) le résultat obtenu.

    ```python
        def aire_rectangle(longueur, largeur):
            aire = longueur * largeur
            return aire
    ```

    On peut, **dans un 2nd temps, appeler** cette fonction autant de fois que l'on veut grâce à son nom pour calculer des aires de rectangles :

    ```python
        aire = aire_rectangle(3, 5)
    ```
_Le but de cette activité est de créer ses propres fonctions pour répondre à des problèmes simples._


??? question "Test8 : Périmètre d'un rectangle"

    1. Compléte la fonction `perimetre_rectangle` suivante pour qu'elle renvoie le périmètre d'un rectangle à partir de sa longueur `longueur` et de sa largeur `largeur` :

        {{IDE('nsi/test8_rect')}}

    2. Effectue dans l'IDE ci-dessus des appels de fonctions pour calculer le périmètre des rectangles suivants :

        - rectangle 1 : longueur $5$ et largeur $4$

        - rectangle 2 : largeur $3,5$ et longueur $10$

        - rectangle 3 : largeur $7$ et longueur $12,4$

        - carré de côté $2$


??? question "Test9 :  Visite d'un parc d'attraction"

    Un parc d'attractions affiche les tarifs suivants : $8,50$ euros par enfant et $12$ euros par adulte.

    1. Compléte la fonction `prix` suivante pour qu'elle renvoie le prix total à payer à partir du nombre `nb_enfants` d'enfants et du nombre `nb_adultes` d'adultes.

        {{IDE('nsi/test9_prix-parc')}}

    2. Modifie le code de la fonction précédente pour qu'elle ne soit écrite que sur 2 lignes.
    
    3. Quelle instruction faut-il écrire pour connaître le prix à payer par une famille de deux adultes et trois enfants ?

??? question "Test10 :  Prix HT et TTC"

    1. Compléte la fonction `prix_TTC` pour qu'elle renvoie le prix TTC d'un article à partir de son prix HT. On prendra un taux de TVA de $20\%$.

        {{IDE('nsi/test10_prix-ttc')}}

    2. Modifie la fonction précédente pour qu'elle puisse fonctionner avec n'importe quel taux de TVA.

    3. Ecris une fonction `prix_HT` qui renvoie le prix HT d'un article à partir de son prix TTC et d'un taux de TVA donné.

??? question "Test11 :  Aire d'un disque"

    Complète la fonction `aire_disque` suivante pour qu'elle renvoie l'aire d'un disque à partir de son rayon `r`.

    {{IDE('nsi/test11_aire_disque')}}

    !!! info "Fonction `assert`"

        L instruction `assert` permet d'afficher un message d'erreur quand la proposition qui suit est fausse.
        Dans l'exemple dans l'IDE ci-dessus, le résultat renvoyé par la fonction `test11_aire_disque` est comparé avec l'aire attendue. S'il est faux `assert False` génère une erreur du type `AssertionError` et le programme est arrêté, si'il est vrai, `assert True` ne fait rien et le programme continue de se dérouler normalement.

??? question "Test12 :  Delta"

    Complète la fonction `delta` suivante pour qu'elle renvoie le discriminant delta d'une fonction polynôme $x\longmapsto ax^2+bx+c$`.

    {{IDE('nsi/test12_delta')}}

## 4. QCM Fonctions

??? tip "Solutions du QCM 6.2 p3 du pdf"

    1. b, c
    2. b, d
    3. d
    4. b, d
    5. a 

## 5. Bac à sable

- [Python Tutor en ligne](https://pythontutor.com/visualize.html#mode=edit)
(pour le debug pas à pas)

- IDE dans le navigateur:

{{IDE()}}

- [Baston IDE en ligne] (https://console.basthon.fr/)





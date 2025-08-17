# UAA11 TP7 - Listes imbriquées

## 2. Future coder: présentation des listes imbriquées

### **Test1&2 - Liste de chaines**

??? question "Test1"
    Etant donné une liste de chaînes, écris une fonction qui renvoie la première lettre de la seconde chaîne de la liste. Par exemple ci-dessous, tu devrais renvoyer d :
      
    {{ IDEv('tp2-3_fc/Test1') }}

!!! info
    Tu as peut-être résolu le problème comme ceci :

    ```python
    chaine = chaines[1]

    print(chaine[0])    
    ```

    Il y a un moyen plus court. `chaines[1]` est une expression comme une autre et les indices comme `[0]` peuvent être utilisés sur n'importe quelle expression, pas seulement sur les variables. Tu peux donc sauter la variable intermédiaire et le faire en une seule ligne :

    ```python
    print(chaines[1][0])
    ```

    Regarde bien cette syntaxe. Si elle te semble nouvelle et fantaisiste, elle ne l'est pas. Il s'agit simplement de la syntaxe habituelle avec des indices, appliquée deux fois.

??? question "Test2"

    En utilisant cette syntaxe, modifie le programme pour renvoyer la dernière lettre de l'avant-dernière chaîne dans la liste chaines. Tu devrais utiliser une expression unique. Ta solution devrait fonctionner pour toute liste non vide de chaînes. 

    {{ IDEv('tp2-3_fc/test2') }}

### **Test3 - Listes imbriquées**

!!! info

    Appliquer l'indice deux fois peut être encore plus puissant. Nous pouvons l'utiliser non seulement sur une liste de chaînes de caractères, mais aussi sur une liste de listes. 
    
    !!! question "Qu'affiche le programme suivant ?"

        ```python
        chaines = [['hello', 'there'], ['comment', 'allez', 'vous']]
        print(chaines[1][0])
        ```

    Comme tu peux le voir, Python nous permet d'utiliser des listes imbriquées : une liste dont chaque élément est une autre liste (on préfère les qualifier de sous-listes).

??? question "Test3"

    On peut utiliser l'indexation plus de deux fois. Écris une fonction qui prend une liste imbriquée de chaines comme au-dessus et renvoie la première lettre de la troisième chaîne de la deuxième sous-liste. N'utilise qu'une expression comme dans l'exemple précédent. Pour l'exemple ci-dessus, cela devrait afficher v.

    {{ IDEv('tp2-3_fc/test3') }}

!!! info

    Nous pouvons toujours utiliser toutes les méthodes et fonctions de liste que nous avons apprises auparavant. Par exemple, nous pouvons ajouter un nouveau mot à la dernière sous-liste de chaines avec append, pour qu'il vienne après 'vous' :

    chaines[1].append("aujourd'hui ?")

    Après tout, la sous-liste chaines[1] est toujours une liste comme une autre !

    Au paragraphe suivant, nous allons apprendre à boucler sur des listes imbriquées.

### **Test4 - Parcours de listes imbriquées**

??? question "Test4"
    
    Dans la liste précédente:

    - rajoute 'are' après 'there'.

    - remplace 'comment' par 'how'

    {{ IDEv('tp2-3_fc/test4') }}

## 3. Future coder: Listes à 2 dimensions

### **Test5 - Affichage**

!!! info

    Tu peux utiliser une boucle imbriquée pour itérer sur chaque élément et sous-élément d'une liste imbriquée. Par exemple, considére cette liste imbriquée.

    ```python
    nombres = [[1, 2, 3], [4, 5], [6], []]

    for sous_liste in nombres:
        for nombre in sous_liste:
            print(nombre)
        print('---')
    ```

    Regarde attentivement le code. Note que la boucle extérieure crée une variable sous_liste et que la boucle intérieure itère sur cette même variable. Il s'agit d'une situation classique. Maintenant, exécute le code dans l'IDE ci-dessous.

    Comme pour les listes à une dimension, cette solution ne t'informe pas sur l'élément que tu affiches et ne te permet pas de le modifier. Pour celà, tu peux itérer avec 2 compteurs:

    - la 1ère boucle `for` parcourt la liste gràce à un 1er compteur `j` qui compte le nombre de sous listes ( ici 4 ),

    - la 2ème boucle  `for` parcourt chaque sous-liste grâce à un compteur `i` qui compte le nombre de chiffres.

    ```python
    nombres = [[10, 20, 30], [40, 50, 60], [70,80,90], [91, 92, 93]]

    jmax = len(nombres)     # 3
    imax = len(nombres[0])  # 3

    for j in range(jmax):
        for i in range(imax):
            print(nombres[j][i])
        print('---')
    ```

??? question "Test5"
    Copie les 2 codes ci-dessous et regarde attentivement son déroulement en rajoutant des impressions des variables intérieures aux boucles (sous_liste ou  j, i)

    {{ IDEv() }}

### **Test6 - Recherche d'une chaîne**

??? question "Test6"

    Supposons que nous ayons une liste imbriquée de chaînes de caractères comme celle ci-dessous, et que nous voulions rechercher un mot particulier au plus profond de la liste.

    Tu peux imaginer que chaines représente un livre, où chaque sous-liste est une page et chaque chaîne de caractères à l'intérieur est une ligne dans cette page. Cela pourrait aussi représenter une bibliothèque, où chaque liste est un livre et chaque chaîne est une page.

    Écris un programme pour afficher chaque chaîne de caractères qui contient mot. Cela devrait fonctionner pour n'importe quel mot et n'importe quelle chaines.

    Rappele-toi qu'il existe une façon spécifique de vérifier si une chaîne de caractères contient une autre chaîne de caractères. 
    
    {{ IDEv('tp2-3_fc/test6') }}

### **Test7&8 Présence d'une chaîne**

??? question "Test7"

    Maintenant, modifions légèrement l'exercice. Cette fois, la sortie doit nous indiquer quelles sous-listes contiennent `mot`, plutôt que les chaînes internes. En particulier, nous voulons afficher un booléen pour chaque sous-liste : `True` si la sous-liste contient le mot dans l'une de ses chaînes, `False` s'il n'y est pas du tout.

    !!! warning "Attention !"
        
        Note que mot in sous_liste ne fonctionnera pas. Par exemple, `"hello" in ["hello there"`, `"comment allez-vous"]` est `False` car `"hello"` n'est égale à aucun des deux éléments de cette liste, même s'il est dans l'un d'eux.

    {{ IDEv('tp2-3_fc/test7') }}

??? question "Test8"

    Ensuite, n'affiche qu'un seul booléen pour indiquer si `mot` est présent dans n'importe quelle chaîne de la liste entière imbriquée. 

    {{ IDEv('tp2-3_fc/test8') }}

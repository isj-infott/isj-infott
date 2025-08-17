# UAA11 TP7 - Listes imbriquées

## **Mémo**

TBD

## **4. Exercices**

### **Test1 - Déclaration d'une liste de X de 8*10**

??? question "Test1"
    Une liste imbriquée de 8*10 contenant que des X est en fait une liste constituée de 8 sous-listes cotenant 10 X chacune.

    - Soit tu la définis "manuellement" :

        !!! note "Code"
            ```console
            >>> liste2d = [
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
                ['X','X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X'], 
                ['X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X', 'X']
            ]
            ```

    - Soit tu la définis avec une boucle. Pour celà, complète le code

    {{ IDEv('tp4_exo/test1_declare') }}

!!! note "Remarque"

    Il n’y a aucune différence qualitative entre :

    -	une liste à 2 dimensions 8*10 accessibles par 2 indices (j, i), allant respectivement de de 0 à 7 et de 0 à 9

    -	et une liste à une dimension  8*10=80  accessible par un seul indice i allant de 0 à 79.

    Le choix se fera sur la facilité de manipulation d ela liste.

### **Test2 - Affichage de la liste**

??? question "Test2a"
    Parcours la 1ère liste pour afficher les sous-listes "ligne par ligne"
    {{ IDEv('tp4_exo/test2a_affiche_lignes') }}

??? question "Test2b"
    Parcours la liste et chaque sous-liste pour afficher chaque élément séparément
    !!! example "Exemple"
        ```console
        >>> affiche()
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X
        ```
    {{ IDEv('tp4_exo/test2b_affiche') }}

### **Test3 - Affichage des coordonnées**

??? question "Test3"
    Parcours la liste et les sous-listes liste pour afficher leurs indices sous forme de coordonnées ( j, i )
    !!! warning "Attention !"
        A l'inverse des math, nous parcourons d'abord les lignes (indice j qui augmente du haut vers le bas), puis X (indice i qui augmente de gauche à droite)
    !!! example "Exemple"
        ```console
        >>> affiche_coor()
        ( 0 , 0 ) ( 0 , 1 ) ( 0 , 2 ) ( 0 , 3 ) ( 0 , 4 ) ( 0 , 5 ) ( 0 , 6 ) ( 0 , 7 ) ( 0 , 8 ) ( 0 , 9 ) 
        ( 1 , 0 ) ( 1 , 1 ) ( 1 , 2 ) ( 1 , 3 ) ( 1 , 4 ) ( 1 , 5 ) ( 1 , 6 ) ( 1 , 7 ) ( 1 , 8 ) ( 1 , 9 ) 
        ( 2 , 0 ) ( 2 , 1 ) ( 2 , 2 ) ( 2 , 3 ) ( 2 , 4 ) ( 2 , 5 ) ( 2 , 6 ) ( 2 , 7 ) ( 2 , 8 ) ( 2 , 9 ) 
        ( 3 , 0 ) ( 3 , 1 ) ( 3 , 2 ) ( 3 , 3 ) ( 3 , 4 ) ( 3 , 5 ) ( 3 , 6 ) ( 3 , 7 ) ( 3 , 8 ) ( 3 , 9 ) 
        ( 4 , 0 ) ( 4 , 1 ) ( 4 , 2 ) ( 4 , 3 ) ( 4 , 4 ) ( 4 , 5 ) ( 4 , 6 ) ( 4 , 7 ) ( 4 , 8 ) ( 4 , 9 ) 
        ( 5 , 0 ) ( 5 , 1 ) ( 5 , 2 ) ( 5 , 3 ) ( 5 , 4 ) ( 5 , 5 ) ( 5 , 6 ) ( 5 , 7 ) ( 5 , 8 ) ( 5 , 9 ) 
        ( 6 , 0 ) ( 6 , 1 ) ( 6 , 2 ) ( 6 , 3 ) ( 6 , 4 ) ( 6 , 5 ) ( 6 , 6 ) ( 6 , 7 ) ( 6 , 8 ) ( 6 , 9 ) 
        ( 7 , 0 ) ( 7 , 1 ) ( 7 , 2 ) ( 7 , 3 ) ( 7 , 4 ) ( 7 , 5 ) ( 7 , 6 ) ( 7 , 7 ) ( 7 , 8 ) ( 7 , 9 )
        ```
    {{ IDEv('tp4_exo/test3_affiche_coor') }}

### **Test4 - Modification d'un caractère**

??? question "Test4"
    Demande à l’utilisateur la position du caractère qu’il veut changer ainsi que le nouveau caractère par lequel il veut le remplacer, puis affiche la nouvelle liste.
    !!! example "Exemple"
        ```console
        >>> modif_car()
        j: 3
        i: 2
        c: U
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X U X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X 
        X X X X X X X X X X
        ```
    {{ IDEv('tp4_exo/test4_modif_car') }}

### **Test5 - Recherche de la position**

??? question "Test5"
    Demande à l’utilisateur de rentrer un caractère et affiche s’il l’a trouvé ou pas; si c'est le cas, affiche sa position dans la liste.
    !!! example "Exemple"
        ```console
        >>> find_pos_car()
        c: U
        U True
        U trouvé en (3,2)
        ```
    {{ IDEv('tp4_exo/test5_find_pos_car') }}

### **Test6 - Recherche des caractères adjacents**

??? question "Test6"
    Demande à l’utilisateur de rentrer une position et affiche le caractère correspondant ainsi que ceux autour de lui.
    !!! example "Exemple"
        ```console
        >>> find_autour_car()
        j: 3
        i: 2
        U
        X X X 
        X U X 
        X X X
        ```
    !!! warning "Attention !"
        Ton test doit  fonctionner si le caractère est choisi en extrémité de la liste         
    {{ IDEv('tp4_exo/test6_find_autour_car') }}
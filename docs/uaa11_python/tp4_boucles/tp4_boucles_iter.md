# UAA11 TP4-2 : Les Boucles itératives

**Mémo**

- Prends connaissance du cours sur les [tests](NSI Première Partie 1 Chapitre 5 Boucles.pdf) , fais les activités ci-dessous puis réponds aux questions **QCM** du pdf.

- Tu peux tester ton code avec l'IDE du chapitre "TBD. Bac à sable"

- Complète ton fichier "**memo**" que tu complèteras avec ce que tu as appris au fur et à mesure de ton avancement dans le cours.

## 1. Découverte des boucles itératives `for ... in range(...) :`
 
??? question  "Test1: Placement bancaire"

    1. On place une somme de $2000$ euros sur un compte remunéré au taux annuel de 2%.
        Complète la fonction suivante de telle sorte qu'elle renvoie la somme disponible sur le compte au bout de $20$ ans. On arrondira le résultat au centime d'euro près.

        {{IDE('nsi_iter/test1a_placement')}}
 
    2. Modifie la fonction précédente en une fonction `placement_bancaire` de telle sorte qu'elle puisse fonctionner avec n'importe quel placement initial, n'importe quel taux et sur n'importe quelle durée.

        {{IDE('nsi_iter/test1b_placement_bancaire')}}

??? question  "Test2: Jeu de rôle"

    Dans un jeu, un joueur dispose de `250` points de vie. Il subit `5` attaques successives dont les valeurs sont des nombres entiers aléatoires entre `10` et `40`.

    1. Complète le code de la fonction ci-dessous afin qu'elle renvoie le nombre de points de vie du joueur à l'issue de ces cinq attaques.

        {{IDE('nsi_iter/test2a_jeu_role')}}

    2. Le joueur dispose à présent d'une défense de `25`. Lorsqu'il subit une attaque de valeur `attaque`, on applique la règle suivante :
        
        - si la valeur de l'attaque est strictement supérieure à celle de la défense, le joueur perd `attaque - 25` points de vie ;
    
        - si la valeur de l'attaque est inférieure ou égale à celle de la défense, le joueur ne perd aucun point de vie.

        Complète la fonction suivante afin qu'elle renvoie le nombre de points de vie du joueur à l'issue des cinq attaques précédentes.

        {{IDE('nsi_iter/test2b_jeu_role')}}

    3. On modifie la fonction précédente en une fonction `points_vie_attaques_aléatoires_multiples_défense` pour qu'elle fonctionne avec n'importe quel nombre de points de vie, n'importe quelle défense et n'importe quel nombre d'attaques successives prenant des valeurs entières aléatoires entre deux nombres entiers prédéfinis en respectant la règle suivante :
        
        - si la valeur de l'attaque est strictement supérieure à celle de la défense, le joueur perd `attaque - défense` points de vie ;
        
        - si la valeur de l'attaque est inférieure ou égale à celle de la défense, le joueur ne perd aucun point de vie.
        
        - si le nombre de points de vie à l'issue de toutes les attaques est strictement négatif, on le ramène à 0.

        Ecris ci-dessous le code de cette fonction où les paramètres sont définis de la façon suivante :
        
        - `points_vie` est le nombre de points de vie initial du joueur,

        - `défense` est la défense du joueur,

        - `nb_attaques` est le nombre d'attaques successives subies par le joueur,

        - `val_min_attaque` est la valeur minimale que peut prendre une attaque,
        
        - `val_max_attaque` est la valeur maximale que peut prendre une attaque.

        Tous les paramètres de la fonction sont des nombres entiers strictement positifs.

        {{IDE('nsi_iter/test2c_jeu_role')}}

??? question  "Test3: Lancer d'un dé"

    On lance $50$ fois un dé équilibré à six faces numérotées de $1$ à $6$ et on regarde le nombre de fois où on a obtenu $6$.

    Complète la fonction suivante afin de simuler cette expérience.

    {{IDE('nsi_iter/test3_de')}}

??? question  "Test4: Pile ou face"

    Complète la fonction suivante simulant le jeu du Pile ou Face avec une pièce équilibrée et renvoyant pour un nombre de lancers `nb_lancers` donné la fréquence d'apparition du Pile.

    {{IDE('nsi_iter/test4_piece')}}

## 2. Pour aller plus loin sur la découverte ...

??? question  "Test5: Flux de populations  ==`MAISON`=="

    On considère un flux de populations entre 3 zones géographiques $A$, $B$ et $C$ sous les conditions suivantes :

    - La population totale des 3 zones reste constante au cours du temps.
    
    - Chaque année, la zone $A$ perd $20\%$ de sa population au profit de la zone $B$ et $10\%$ de sa population au profit de la zone $C$.
    
    - Chaque année, la zone $B$ perd $15\%$ de sa population au profit de la zone $A$ et $5\%$ de sa population au profit de la zone $C$.
    
    - Chaque année, la zone $C$ perd $25\%$ de sa population au profit de la zone $A$ et $10\%$ de sa population au profit de la zone $B$.

    Le tableau suivant donne les populations initiales des 3 zones :

    | Zone A | Zone B | Zone C |
    | :----: | :----: | :----: |
    | 100 000 | 80 000 | 120 000 |

    Complète la fonction ci-dessous de telle sorte qu'elle renvoie les populations des 3 zones $A$, $B$ et $C$ dans cet ordre au bout de `nb_années` années.

    def évolution_pop(nb_années):
        assert ... # test d'assertion sur nb_années
        popA = ... # population initiale de la zone A
        popB = ... # population initiale de la zone B
        popC = ... # population initiale de la zone C
        for annee in ...:
            popA_temp = ... # calcul de la nouvelle population de la zone A
            popB_temp = ...
            popC_temp = ...
            popA = ...
            popB = ...
            popC = ...
        return ...

    {{IDE('nsi_iter/test5_pop')}}

??? question  "Test6: Lancer de deux dés (bis)"

    On lance $25$ fois deux dés équilibrés à six faces numérotées de $1$ à $6$ et on regarde le nombre de fois où on a obtenu deux faces identiques.

    En t'aidant de la fonction écrite à l'exercice précédent, écris une fonction `lancers_25_2des_faces_identiques` permettant de simuler cette expérience.

    {{IDE('nsi_iter/test6_2de')}}

## 2. QCM Boucles itératives

??? tip "Solutions du QCM 2.6  p2 du pdf"
    1. d
    2. a, c, d
    3. d
    4. a, b, d
    5. b, c, d
    
## 3. Exercices

## 4. Solutions des exercices
    Les solutions seront visibles une fois le chapitre terminé.

## 5. Bac à sable

- [Python Tutor en ligne](https://pythontutor.com/visualize.html#mode=edit)
(pour le debug pas à pas)

- IDE dans le navigateur:

{{IDE()}}

- [Baston IDE en ligne] (https://console.basthon.fr/)

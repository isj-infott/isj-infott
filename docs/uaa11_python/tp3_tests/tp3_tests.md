# UAA11 TP3 - Les Tests

**Notions abordées** : 

- condition de type logique ou booléen

- tests et opérateurs de comparaison ( `==`, `!=`, `<=`, `>=`, `<`, `>`, `in` )

- opérateurs logiques ( `not`, `or`, `and` )

- embranchements simples ( `if`  `else`  ), multiples ( `if`  `elif`  `else`  )

**Mémo**

- Prends connaissance du cours sur les [**tests**](NSI Première Partie 1 Chapitre 4 ConditionsEmbranchements.pdf) e, fais les activités ci-dessous puis réponds aux questions **QCM** du pdf.

- Tu peux tester ton code avec l'IDE du chapitre "TBD. Bac à sable"

- Complète ton fichier "**memo**" que tu complèteras avec ce que tu as appris au fur et à mesure de ton avancement dans le cours.

## 1. Conditions et Tests
 
Le but de cette activité est de manipuler les conditions et les tests.

??? question "Test 1 : Opérateurs de comparaisons et opérateurs logiques"

    Détermine les résultats de chacun des tests suivants puis vérifie en exécutant les cellules dans le terminal :

    ```python
        7 >= 0
        5 == 3
        3 != 3
        7 < 3.8
        4 < 4
        4 <= 4
        4 > -2
        5 != 5.1
        -3.2 >= 4.3
        4 == 4.0
        2*0.1 == 0.2
        3*0.1 == 0.3
        0.7**2 != 0.49
    ```
    {{terminal()}}

    !!! warning "A retenir"

        Les calculs algébriques et les tests avec les nombres entiers (type `int`) sont tous exacts.

        En revanche, il n'en est pas de même avec les nombres flottants (type `float`) : certains calculs sont exacts et d'autres non, de même pour les tests. Enfin, c'est ce qu'il semble avec les exemples ci-dessus. Ces "erreurs" sont dues à la façon dont les nombres flottants sont représentés en binaire dans l'ordinateur. En fait, ces erreurs peuvent être contrôlées et les calculs avec les flottants sont assurés être exacts avec 16 décimales.

    Détermine les résultats de chacune des conditions suivantes puis vérifier en exécutant les cellules :

    ```python
        a = 3
        a >= 0 and a < 5

        a = 3
        0 <= a < 5    
        # Python autorise le test en double inégalité. Cette cellule est équivalente à la cellule précédente

        not(4 > 3)

        a = 3
        b = 5
        a > b and a > 0

        a = 3
        b = 5
        a > b or a > 0

        a = 4
        b = a + 1
        b - a == 1

        a = 4
        b = a + 1
        not(a - b > 0)

        a = 3.7
        b = 2.1
        a*b >= 4 and a - b >= 1

        a = 3.7
        b = 2.1
        not(a*(b-2) - 3 < 0)
    ```
    {{terminal()}}

    Détermine les résultats des deux conditions suivantes puis vérifier en exécutant les cellules. 
    
    Que peut-on en conclure ?

    ```python
        a = 3
        b = 4.5
        c = -5
        a > 0 or (b > 0 and c >= 0)

        a = 3
        b = 4.5
        c = -5
        (a > 0 or b > 0) and c >= 0
    ```
## 2. QCM Conditions et Tests

??? tip "Solutions du QCM 2.7 p2 questions 1 à 4 du pdf"
    1. b, d
    2. b
    3. a, d
    4. a, b, c, d

## 3. Embranchements simples

??? question "Test 2 : Jeu de rôle"

    1. Dans un jeu, un joueur dispose de `100` points de vie et d'une défense de `40`.

        Il subit une attaque de valeur `attaque`.

        Complète la fonction suivante renvoyant le nouveau nombre de points de vie du joueur sachant que :

        - si la valeur de l'attaque est strictement supérieure à celle de la défense, le joueur perd `attaque - 40` points de vie,

        - si la valeur de l'attaque est inférieure ou égale à celle de la défense, le joueur ne perd aucun point de v.

        {{ IDE('nsi/test2a_jeu_role')}}


    2. On modifie la fonction précédente en une fonction **`points_vie_attaque_défense`** pour qu'elle fonctionne avec n'importe quel nombre de points de vie, n'importe quelle défense et n'importe quelle attaque en respectant la règle :

        - si la valeur de l'attaque est strictement supérieure à celle de la défense, le joueur perd `attaque - défense` points de vie,

        - si la valeur de l'attaque est inférieure ou égale à celle de la défense, le joueur ne perd aucun point de vie,

        - si le nouveau nombre de points de vie est strictement négatif, on le ramène à 0.

        {{ IDE('nsi/test2b_jeu_role')}}


??? question "Test 3 : Tirage photos"

    Un photographe propose le tirage de photos numériques au tarif de $0,16$ euro l'unité. Le tarif devient de $0,12$ euro l'unité pour une commande d'au moins $75$ photos.

    Complète le code de la fonction suivante afin qu'elle renvoie le montant à payer en fonction du nombre de photos que l'on souhaite tirer.

    {{ IDE('nsi/test3_photos')}}

??? note "Test 4 : Reprographie ==`MAISON`=="

    Un commerce de reprographie facture $0,20$ euro l'unité les $20$ premières photocopies et $0,10$ euro l'unité les suivantes.

    En s'aidant de la fonction écris au test3, écris une fonction `prix_reprographie` prenant en paramètre les nombres de photocopies à réaliser et renvoyant le prix à payer.

    {{ IDE('nsi/test4_reprographie')}}

??? question "Test 5 : Pile ou face"

    Complète la fonction suivante afin de simuler le jeu du Pile ou Face avec une pièce équilibrée.

    (`for loop in range(50)` permet de répéter 50 fois une instruction - voir le chapitre suivant)

    {{ IDE('nsi/test5_pile_face')}}


??? note "Test 6 : Suite de Syracuse ==`MAISON`=="

    On considère une fonction **`syracuse`** qui prend en paramètre un entier $n$ supérieur ou égal à $1$ et qui renvoie un nombre entier égal à la valeur de $n/2$ si $n$ est pair et à la valeur de $3n+1$ si $n$ est impair.

    1. Complète le code de cette fonction ainsi que les 2 lignes de test.
        Que renvoient les instructions `syracuse(0)`, `syracuse(-5)` et `syracuse('A')` ? Est-ce cohérent avec l'énoncé ?

    {{ IDE('nsi/Test6a_Syracuse')}}

    2. Complète le code de la fonction ci-dessous afin qu'elle vérifie à la première ligne grâce à un test d'assertion que les données passées en paramètre sont bien des entiers supérieurs ou égaux à $1$.

    {{ IDE('nsi/Test6b_Syracuse')}}

??? question "Test 7 : Intervention d'un technicien"

    Dans le cadre d'un contrat de dépannage, un technicien applique le tarif suivant :

    - s'il travaille moins de 2h, il applique un forfait de $150$ euros,

    - s'il travaille plus de 2h, il ajoute à ce forfait la somme de $40$ euros par heure supplémentaire.
 
    Complète le code de la fonction suivante afin qu'elle renvoie la facture du technicien suivant son nombre d'heures travaillé.

    {{ IDE('nsi/Test7_technicien')}}

## 4. Embranchements multiples

??? question "Test 8 : Envoi de courrier"

    La fonction ci-dessous renvoie le prix à payer en euros suivant le poids en grammes de la lettre que l'on veut envoyer.

    1. Que renvoient les instructions `affranchissement(15)`, `affranchissement(53)` et `affranchissement(250)` ?

    2. On désire envoyer une lettre pesant 365 grammes. Quelle instruction doit-on saisir pour connaître le prix à payer ? Quel est ce prix ?

    3. En fait, la somme de $6,5$ euros n'est valable que pour un poids inférieur ou égal à $500$ grammes. Au delà, il faut payer $8$ euros. 
    
    Modifie la fonction  pour qu'elle prenne en compte cette modification et vérifie son fonctionnement avec les tests proposés.

    {{ IDE('nsi/test8_courrier')}}

??? question "Test 9 : Jeu de rôle"

    Dans un jeu de rôle, les joueurs ont un grade dépendant des points d'expérience qu'ils ont acquis.

    ||||||
    | :---- | :----: | :----: |  :----:  |  :----: |
    | Points d'expérience | entre 0 et 99 | entre 100 et 399 | entre 400 et 1499 | supérieur ou égal à 1500 |
    | Grade | padawan | chevalier | maître | grand maître |

    Complète la fonction suivante de telle sorte qi'elle renvoie le grade d'un joueur en fonction de ses points d'expérience `points_exp` et écris les tests pour vérifier **tout** le bon fonctionnement de la fonction.

    {{ IDE('nsi/test9_jeu_role')}}

## 5. QCM Embranchements

??? tip "Solutions du QCM 4.3 p5 du pdf"
    1. a, d
    2. a, d
    3. c, d
    4. a, b
    5. a, b, d

## 6. Exercices

??? question "Test 1 : Etats de l'eau"

    Ecris les tests permettant de vérifier le code suivant et corrige les erreurs
    {{IDE('exos/test1_etat_eau')}}

??? question "Test 2 : Valeur absolue"

    Ecris une fonction **`val_abs`** qui renvoie la valeur absolue d’un entier relatif entré au clavier.
    {{IDE('exos/test2_val_abs')}}

??? question "Test 3 : Signe du produit de 2 nombres"

    Ecris une fonction** `signe_produit`** qui renvoie  si le produit de 2 nombres est strictement négatif, positif ou nul. Attention toutefois, on ne doit pas calculer le produit !        
    {{IDE('exos/test3_signe_produit')}}

??? question "Test 4 : Minimum de 3 nombres"
    Ecris une fonction** `min_3nb`** qui renvoie le plus petit de 3 nombres (les 3 nombres sont fournis à la fonction).
    Teste ton programme avec toutes les combinaisons possibles.
    {{IDE('exos/test4_min_3nbs')}}

??? note "Test 5 : Maximum de 4 nombres ==`MAISON`=="
    Ecris une fonction **`max_4nb`** qui renvoie le plus grand  de quatre nombres.
    Teste ton programme avec toutes les combinaisons possibles.
    {{IDE('exos/test5_max_4nb')}}

??? question "Test 6 : 3 nombres par ordre croissants"
    Ecris une fonction **`nbs_croissants`** qui renvoie 3 nombres par ordre croissant.
    Teste ton programme avec toutes les combinaisons possibles.
    {{IDE('exos/test6_3nbs_croissants')}}

??? note "Test 6bis : 4 nombres par ordre croissants ==`MAISON`=="
    Ecris une fonction **`nbs4_croissants`** qui renvoie 4 nombres par ordre croissant.
    Teste ton programme avec toutes les combinaisons possibles.
    {{IDE('exos/test6bis_4nbs_croissants')}}

??? question "Test 7 : Equation du 1er degré"
    Ecris une fonction **`eq_1er_deg`** renvoie la solution d'une équation à coefficients réels de la forme ax + b = 0 (a et b ssont fournis à la fonction).
    {{IDE('exos/test7_1er_deg')}}

??? note "Test 8 : Equation du 2e degré ==`MAISON`=="
    Ecris une fonction **`eq_2e_deg`** affiche les solutions d'une équation à coefficients réels de la forme ax2 + bx + c =0 (a, b, c sont fournis à la fonction).
    On pourra utiliser la fonction **`sqrt(x)`** de la librairie `math` qui retourne la racine carrée de x.
    {{IDE('exos/test8_2e_deg')}}

??? note "Test 9 : Intersection de cercles ==`MAISON`=="
    Ecris une fonction **`inter_cercles`** qui renvoie True si deux cercles ont une intersection non vide, False sinon (leur rayon et les coordonnées de leur centre sont fournis à la fonction).
    {{IDE('exos/test9_cercles')}}

??? question "Test 10 : Elections"
    Les élections législatives, en Guignolerie Septentrionale, obéissent à la règle suivante :
    
    - Lorsque l'un des candidats obtient plus de 50% des suffrages, il est élu dès le premier tour.

    - En cas de deuxième tour, peuvent participer uniquement les candidats ayant obtenu au moins 12,5% des voix au premier tour.

    Ecris une fonction **`elections`**qui en fonction des scores de 4 candidats au premier tour passés en paramètre, traitera le **candidat numéro 1** (et uniquement lui) et renverra une message précisant s'il est **élu**, **battu**, s'il se trouve en **ballottage favorable** (il participe au second tour en étant arrivé en tête à l'issue du premier tour) ou **ballotage défavorable** (il participe au second tour sans avoir été en tête au premier tour).
    {{IDE('exos/test10_elections')}}

??? note "Test 11 : Compagnie d'assurance ==`MAISON`=="
    Une compagnie d'assurance automobile propose à ses clients quatre familles de tarifs identifiables par une couleur, du moins au plus onéreux : tarifs bleu, vert, orange et rouge.
    Le tarif dépend de la situation du conducteur :
    
    - un conducteur de moins de 25 ans et titulaire du permis depuis moins de deux ans, se voit attribuer le tarif rouge, si toutefois il n'a jamais été responsable d'accident. Sinon, la compagnie refuse de l'assurer.

    - un conducteur de moins de 25 ans et titulaire du permis depuis plus de deux ans, ou de plus de 25 ans mais titulaire du permis depuis moins de deux ans a le droit au tarif orange s'il n'a jamais provoqué d'accident, au tarif rouge pour un accident, sinon il est refusé.

    - un conducteur de plus de 25 ans titulaire du permis depuis plus de deux ans bénéficie du tarif vert s'il n'est à l'origine d'aucun accident et du tarif orange pour un accident, du tarif rouge pour deux accidents, et refusé au-delà
    
    - De plus, pour encourager la fidélité des clients acceptés, la compagnie propose un contrat de la couleur immédiatement la plus avantageuse s'il est entré dans la maison depuis plus de cinq ans. Ainsi, s'il satisfait à cette exigence, un client normalement "vert" devient "bleu", un client normalement "orange" devient "vert", et le "rouge" devient orange.
    
    Ecris une fonction **`assurance`** qui prend en paramètre les données nécessaires pour traiter ce problème et renvoie le résultat du traitement. 
    
    Avant de se lancer à corps perdu dans cet exercice, on pourra réfléchir un peu et s'apercevoir qu'il est plus simple qu'il n'en a l'air (cela s'appelle faire une analyse !)
    {{IDE('exos/test11_assurance')}}

## 7. Remédiation

??? note "France IOI ==`REMDIATION`=="

    Vas sur le [site de France IOI](https://www.france-ioi.org/algo/chapters.php) et fais dans le chapitre **Niveau 1, chap 5 - Tests et conditions** : exercices de 1) à 5)

## 8. Solutions des exercices
    Les solutions seront visibles une fois le chapitre terminé.

## 9. Bac à sable

- [Python Tutor en ligne](https://pythontutor.com/visualize.html#mode=edit)
(pour le debug pas à pas)

- IDE dans le navigateur:

{{IDE()}}

- [Baston IDE en ligne] (https://console.basthon.fr/)

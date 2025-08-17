# UAA11 TP1 - Les variables, instructions d’affectation, d’affichage et de lecture

**Notions abordées** : 

- variables,

- instruction d'affectation simples / augmentées ( ` = `, ` += `, `-= `), 

- instructions d'affichage et de lecture (` print `,` input `,)

- types de données (` int `, ` float `, ` str `, ` bool `, ` list `, ` tuple `)

- fonctions mathématiques (` round `,` cos `,` sin `,` randint `,` sqrt `)

**Mémo**

- Prends connaissance du cours sur les [**variables**](NSI_Première_Partie1_Chapitre2_VariablesTypes.pdf), fais les activités ci-dessous puis réponds aux questions **QCM** du pdf.

- Tu peux tester ton code avec l'IDE du chapitre "7. Bac à sable"

- Crée un fichier "**memo.txt**" que tu complèteras avec ce que tu as appris au fur et à mesure de ton avancement dans le cours.

<div style="page-break-before: always;"></div>

## 1. Variables et affectations

!!! info "Variales"

    Certains langages nécessitent de déclarer le type de chaque variable avant son utilisation.

    En python, ce n’est pas nécessaire, le type est défini de façon dynamique lors de la 1ère affectation de la variable. 

    ??? question "Test1 : Que valent tutu et tiri ?"
        ```python
        toto = 24
        tutu = toto + 4
        tutu = tutu + 1
        tiri = "hello"+"loulou"
        ```
    ??? tip "Solution"

        tutu vaut 29
        tiri vaut "helloloulou"

!!! info "Opérateurs et expressions"

    Dans une instruction d’affectation, on trouve :

    - à **gauche** de la flèche, un nom de **variable**, et uniquement cela.

    - à **droite** de la flèche, ce qu’on appelle une expression qui doit pouvoir prendre une **valeur**. Les valeurs peuvent être reliées entre elles par des opérateurs.

    - l’expression située à droite de la flèche soit du même type que la variable située à gauche. 

        **Variables  = Valeurs (avec éventuels opérateurs)**

!!! Warning "Remarques importantes"

    - **Attention la similitude de vocabulaire entre les mathématiques et l’informatique est trompeuse** !

        En mathématiques, une « variable » est généralement une inconnue, qui recouvre un nombre non précisé de valeurs.
        Lorsque l’on écrit :

        ```python
            y = 3 x + 2
        ```

        les variables `x` et `y` satisfaisant à l’équation existent en nombre infini (graphiquement, l’ensemble des solutions à cette équation dessine une droite).

        Lorsque l’on écrit :

        ```python
            ax² + bx + c = 0
        ```

        la variable `x` désigne les solutions à cette équation, c’est-à-dire zéro, une ou deux valeurs à la fois …

        **En informatique, une variable possède à un moment donné une valeur et une seule.**
        A la rigueur, elle peut ne pas avoir de valeur du tout (une fois qu’elle a été déclarée, et tant qu’on ne l’a pas affectée - à signaler que dans certains langages, les variables non encore affectées sont considérées comme valant automatiquement zéro). Mais ce qui est important, c’est que cette valeur justement, ne « varie » pas à proprement parler. Du moins ne varie-t-elle que lorsqu’elle est l’objet d’une instruction d’affectation.

    - La deuxième remarque concerne le **signe de l’affectation.**

        En algorithmique, c’est le signe `←`. Mais en pratique, la quasi-totalité des langages emploient le signe `=`. Et là, pour les ants, la confusion avec les maths est également facile. 

        En maths, `A = B` et `B = A` sont deux propositions strictement équivalentes.

        En informatique, absolument pas, puisque cela revient à écrire `A ← B` et `B ← A`, deux choses bien différentes.

        De même, `A = A + 1`, qui en mathématiques, constitue une équation sans solution, représente en programmation une action tout à fait licite (et de surcroît extrêmement courante). Donc, attention   ! ! ! La meilleure des vaccinations contre cette confusion consiste à bien employer le signe `←` en pseudocode, signe qui a le mérite de ne pas laisser place à l’ambiguïté. Une fois acquis les bons réflexes avec ce signe, vous n’aurez plus aucune difficulté à passer au `=` des langages de programmation.

!!! info "Instructions de dialogue entre la machine et l’utilisateur"

    - L'instruction **`print()`** est une opération d'écriture: elle permet au programme d'afficher à l’écran le contenu d'une variable ou du texte. 
        
        Par exemple:

        ```python
            >>> a = 5
            >>> print( a )
            5
        ```

    - L'instruction **`input()`** est une opération de lecture: elle permet de demander à l'utilisateur de saisir des données au clavier. 
    
        Par exemple:
        ```python
            >>> lettre = input("Entre une lettre : ")
            >>> print(lettre)
            Entre une lettre: A
            A
        ```

        ```python
            >>> nb = int(input("Entre un nombre entier : ")
            >>> print(nb)
            Entre une lettre: 3
            3
        ```    
    - Si besoin, tu peux tester ces codes dans le terminal :

        {{ terminal()}}
    
    !!! Warning "Remarques importantes"

        - La fonction `input()` renvoie la saisie de l'utilisateur sous la forme d'une chaîne de caractère (c'est à dire du texte), et la fonction `int ` permet de l'interpréter comme un nombre entier. 

        - Lecture et écriture sont donc des termes qui comme toujours en programmation, doivent être compris du point de vue de la machine qui sera chargée de les exécuter, et non de l'utilisateur qui se servira du programme. 

??? question  "Test2 : fonction input()"

    Complète sur une feuille le code suivant pour afficher le contenu de la variable y qui prend la valeur du quotient $(2x-3)/(x-3)$

    ```python
        x = int(input("Entre un entier : "))
        y = ...
        ...
    ```


??? question  "Test3 : Séquence d'instructions"
    Re-écris le code sur une feuille et complète pour chaque ligne le contenu des 3 variables a, b, c :
    ```python
        a = 5
        b = a+1
        b = 2*b
        b = b-a
        b = b-2
        print( a, B )
    ```
    Tu peux vérifier ton code en l'exécutant pas à pas avec l'application en ligne [pythontutor avec du code](https://pythontutor.com/iframe-embed.html#code=A%20%3D%205%0AB%20%3D%20A%2B1%0AB%20%3D%202*B%0AB%20%3D%20B-A%0AB%20%3D%20B-2%0Aprint%28%20A,%20B%20%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

??? question  "Test4 : Séquence d'instructions"

    ```python
        a = 5
        b = 4
        a = a-b
        b = a+b
        a = b-a
        print( a, b )
    ```

    ??? tip "Solution"
        4 5

??? question  "Test5 : Séquence d'instructions"

    ```python
        a = 7
        b = 6*a
        c = a+b
        d = b-c
        print( a, b, c, d )
    ```
 
    ??? tip "Solution"
        7 42 49 -7

??? question "Test6 : Opérations"

    Complète sur une feuille les deux lignes du code ci-dessous ( au niveau des "...") afin d'afficher le contenu de la variable ` y ` qui prend la valeur $3x^2 + 5x -7$
    ```python
        x = 3
        y = ...
        ...
    ```
    Vois-tu l'intérêt d'écrire la variables y en fonction de la variable x et non d'écrire directement la valeur voulue par y ?

## 2. QCM Variables et affectation

??? tip "Solutions du QCM 1.10 p3 du pdf"

    1. a, c
    2. b, c, d
    3. c
    4. a, b, c
    5. c, d 

<div style="page-break-before: always;"></div>

## 3. Types de données

??? question  "Test7 : Comment calculer $y = \sqrt{3x+5}$ ?"

    Complète le code suivant sur une feuille ou utilise l'IDE du bac à sable si tu veux le vérifier.

    ```python
        from math import sqrt
        x = ...
        y = sqrt( ... )
        ...
    ```

??? question "Test8 : Que renvoie la fonction type ?"

    ```python
        type(5)
        type(5.0)
        type(True)
        type('Bonjour')
    ```
    {{ terminal()}}

??? question  "Test9 : Transtipage"

    Corrige le code :
    ```python
        annee_naissance = input("Saisir votre année de naissance : ")
        age = 2023 - annee_naissance
        print("Votre âge :",age)
    ```
    {{ terminal()}}

!!! info "Transtipage"

    Il existe de nombreuses fonctions de transtypage (changement). En général, elles portent le nom du nouveau type que l'on veut obtenir. Au lycée, on utilisera essentiellement les fonctions suivantes :

    - `int` : permet de transtyper une donnée en un **entier**
    - `float` : permet de transtyper une donnée en un **réel**
    - `str` : permet de transtyper une donnée en uns **chaîne de caractères**
    - `list` : permet de transtyper une donnée en une **liste**

??? question "Test10 : Test d'égalité `==` "
    
    Teste dans le terminal les codes suivants:

    ```python
        0.25**2 == 1/16

        0.7**2 == 0.49

        2*0.1 == 0.2

        3*0.1 == 0.3
    ```
    {{terminal()}}

    !!! info

        L'instruction `==` permet de réaliser un test d'égalité. Elle renvoie donc le booléen `True` si les deux membres sont égaux et le booléen `False` sinon (à ne pas faire entre 2 réels !!!).

    

??? question  "Test11 : Concaténation"

    Que produit le code suivant ?
    ```python
        a = "423"
        b = "12"
        c = a + b
        print(c)
    ```
??? question  "Test12 : Concaténation"

    Complète le code :
    ```python
        >>> a = 'Bon'
        >>> b = 'jour'
        >>> salutation = ...
        >>> print(salutation)
        Bonjour
    ```

??? question  "Test13 : Print de variables"

    Complète le code :
    ```python
        >>> prix = 1.1 * 2
        >>> phrase = ...
        >>> print(phrase)
        Les baguettes coutent 2.2 euros
    ```
## 4. QCM Types de données

??? tip "Solutions du QCM 2.11 p6  du pdf"
    1. b
    2. d
    3. c
    4. d
    5. a, d

## 5. Exercices

??? question  "Test1 : Décomposition d’un montant en euros"

    - Écrire un programme permettant de décomposer un montant entré au clavier en billets de 20, 10, 5 euros en utilisant les opérateurs de la division euclidienne.

    - Modifie ton programme pour ne pas utiliser l’opérateur modulo.

    !!! info Opérateurs
        // : division entière

        % : modulo ou reste de la division

    {{IDEv()}}

??? note  "Test2 : Somme de deux fractions (==Maison==)"

    Ecris un programme permettant de calculer le numérateur et le dénominateur d’une somme de deux fractions entières (on ne demande pas de trouver la fraction résultat sous forme irréductible).

??? note  "Test3 : Conversion prix HT en TTC (==Maison==)"
  
    Ecris un programme qui lit le prix HT d’un article, le nombre d’articles et le taux de TVA, et qui fournit le prix total TTC correspondant. Fais en sorte que des libellés apparaissent clairement.

## 6. Remédiation

??? note  "Test4 : Surface d’un champ (==Remédiation==)"
    
    Écrire un programme qui demande à l’utilisateur de taper la largeur et la longueur d’un champ et qui en affiche la surface.

??? note "Test5 : Bonjour (==Remédiation==)"
   
    Écrire un algorithme qui demande à l’utilisateur de saisir son prénom et qui affiche le message "Bonjour <prénom>" en remplaçant <prénom> par le texte saisi.

??? note "Test6 : Prix des pommes (==Remédiation==)"

    Écrire un algorithme qui demande à l’utilisateur de taper le prix au kg de pommes, la masse achetée et qui affiche le prix à payer.

??? note "Test7 : France IOI (==Remédiation==)"

    Vas sur le [site de France IOI](https://www.france-ioi.org/algo/chapters.php) et fais dans les chapitres suivants :

    - **Niveau 1, chap 1 - Affichage de texte – Suite d’instructions** : tous les exerices des rubriques **découverte / cours / validation** (tu peux passer les rubriques entrainements et challenge)


    - **Niveau 1, Chap 3 - Calculs et découverte des variables** : exercices de 1) à 5)

    - **Niveau 1, Chap 4 – Lecture de l’entrée** : exercices de 1) à 3)

## 7. Bac à sable

- [Python Tutor en ligne](https://pythontutor.com/visualize.html#mode=edit)
(pour le debug pas à pas)

- IDE dans le navigateur:

{{IDE()}}

- [Baston IDE en ligne] (https://console.basthon.fr/)





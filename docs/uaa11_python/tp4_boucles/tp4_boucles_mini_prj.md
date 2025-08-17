# UAA11 TP4-3 : Les Boucles Mini projets ==!!! CHALLENGE !!!==

## 1. Théorème de Bolzano"

Sujet proposé par Mme Lambert pour les Math6 sur le théorème de Bolzano et la recherche de racines d’une fonction.

???+ info "Rappel théorique"

    Soit une fonction f(x) continue sur l’intervalle [a ; b]

    Si f(a) . f(b) < 0
        
        alors il existe un nombre réel c ∈ ] a ; b [ tel que f(c) = 0 
        
        ( autrement dit : c est une racine de la fonction f(x) sur l’intervalle [a ; b] )

???+ note "Consignes"

    Ecris une fonction **`dico(a, b)`**  qui renvoient la racine à 5 décimales près de la fonction suivante :

    $f(x)=3x^{3} - 2x^{2} + 6x - 4$ sur l’intervalle [-5 ; 2]

    ```python
    >>> dico(-5, 2)
    c: 0.66667
    ``` 

???+ info "Aide à l’écriture du programme"

    - Une solution consiste à trouver la racine par dichotomie : on réduit la taille de l’intervalle en prenant le milieu de m de [a,b]
        
        L’intervalle devient alors :

        - si f(a) et f(m) sont de signe contraire : b=m (la racine appartient à [a,m])
        
        - si f(b) et f(m) sont de signe contraire : a=m (la racine appartient à [m,b])
    
    - Cette recherche dichtomique s’effectue tant que |f(a) – f(b)| > 10-5

        On estime que le dernier milieu m calculé est assez précis pour être considéré comme la racine c recherché

??? note "Consignes"

    Modifie ta fonction pour passer les coefficient du polynôme en paramètre ainsi que la précision de calcul de:

    $f(x)=8x^{3}-x^{2}+16x-2$ sur l’intervalle [-3 ; 4]				Sol : c=1/8=0,12500

    $f(x)=6x^{3}+2x^{2}+24x+8$ sur l’intervalle [-3 ; 5]				Sol : c=-1/3=-0,33333

    - Vérifie qu’il y a bien une racine quand l’utilisateur entre les bornes a,b au clavier
    
    - Vérifie que dans ton programme, que les bornes a, b ne sont pas des racines.
    
    - Affiche à l’écran le nombre d’itérations

## 2. Jeu de pierre, papier, ciseaux"

???+ note "Consignes"

    Suis les consignes du [jeu de pierre, papier, ciseaux](mini_prj/mini_prj1_pierre_papier_ciseaux.pdf)

## 3. Jeu de nim - Fort Boyard"

???+ note "Consignes"

    Suis les consignes du [jeu de nim (Fort Boyard)](mini_prj/mini_prj2_nim_fort_boyard.pdf)

## 4. Jeu de dé - le Zanazibar"

???+ note "Consignes"

    Suis les consignes du [jeu de dé le zanzibar](mini_prj/mini_prj3_de_zanzibar.pdf)    

## 7. Bac à sable

- [Python Tutor en ligne](https://pythontutor.com/visualize.html#mode=edit)
(pour le debug pas à pas)

- IDE dans le navigateur:

{{IDE()}}

- [Baston IDE en ligne] (https://console.basthon.fr/)

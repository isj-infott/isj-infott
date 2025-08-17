# affichage des 20 premiers termes de la table par 7,
# avec signalement des multiples de 3 :

def table7():

        i = 1                   # compteur : prendra successivement les valeurs de 1 à 20
        while i < 21:
                # calcul du terme à afficher :
                t = i * 7
                # affichage sans saut à la ligne (utilisation de la virgule) :
                print(t, end =" ")
                # ce terme est-il un multiple de 3 ? (utilisation de l'opérateur modulo) :
                if t % 3 == 0:
                        print("*", end =" ") # affichage d'une astérisque dans ce cas
                i = i + 1

table7()
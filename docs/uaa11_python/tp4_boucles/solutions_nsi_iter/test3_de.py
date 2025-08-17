
from random import randint

def lancers_50_de_6():
    nb6 = 0   # initialisation du compteur donnant le nombre de 6 obtenu
    for lancer in range(50):
        face = randint(1,6)
        if face == 6 :
            nb6 = nb6 + 1
        print("debug: ", face, nb6)
    return nb6

print(lancers_50_de_6())

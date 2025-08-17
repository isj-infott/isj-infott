
from random import randint
        
def freq_pile(nb_lancers):
    nb_pile = 0
    for i in range(nb_lancers) :
        piece = randint(0,1) # 0: pile, 1: face
        if piece == 0 :
            nb_pile = nb_pile + 1
        print("debug: ", piece, nb_pile)
    return nb_pile


print(freq_pile(10))

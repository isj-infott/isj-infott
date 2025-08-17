from random import randint

def lancers_2des_faces_identiques():
    nbid = 0    # initialisation du compteur donnant le nombre
                # où 2 faces identiques
    for lancer in range(25):
        face1 = randint(1,6)
        face2 = randint(1,6)
        
        if face1 == face2 :
            nbid = nbid + 1
        print("debug: ", face1, face2, nbid)
    return nbid

print(lancers_2des_faces_identiques())

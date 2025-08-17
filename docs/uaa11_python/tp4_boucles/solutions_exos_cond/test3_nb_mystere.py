from random import *


def nb_mystere():
        nbmyst = randint(0,100)
        nbuser = -1
        nb_essais = 0
        while (nbmyst != nbuser):
                nb_essais +=1
                nbuser = int(input("Choisis un nombre\n"))
                if nbmyst > nbuser:
                        print("C'est plus !")
                elif nbmyst < nbuser:
                        print("C'est moins !")
                else:
                        return nb_essais
nb_essais = nb_mystere()
print("Bravo, t'as trouvé le nombre mystère! en ", nb_essais, "coups")


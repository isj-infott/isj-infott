# pyramide
def pyramide(nb):
        # Solution condensée
        i = 1
        while i <= 7:
                print("*"*i)    # Affichage de la ligne numéro i
                i = i + 1

        # Solution sans écriture condensée
        i = 1
        while i <= 7:
                j=0
                while j<=i:
                        print("*", end="") # Affichage des i * sur la même ligne
                        j=j+1
                print()
                i = i + 1

pyramide(7)
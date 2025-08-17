def attente_seuil_bacteries(pop_initiale,pop_finale):
    pop = pop_initiale
    nb_heures = 0
    while pop < pop_finale:
        pop = pop * (1 +10.5/100)
        nb_heures = nb_heures + 1 
    return nb_heures

assert attente_seuil_bacteries(100000,200000) == 7
assert attente_seuil_bacteries(100000,500000) == 17
assert attente_seuil_bacteries(100000,1000000) == 24

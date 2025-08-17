def evolution_pop(nb_annees):
    popA = 100000 # population initiale de la zone A
    popB = 80000 # population initiale de la zone B
    popC = 120000 # population initiale de la zone C
    for annee in range(nb_annees) :
        popA_temp = popA - popA*(0.2+0.1) + popB*0.15 + popC*0.25
        popB_temp = popB - popB*(0.15+0.05) + popA*0.2 + popC*0.1
        popC_temp = popC - popC*(0.25+0.1) + popA*0.1 + popB*0.05
        popA = popA_temp
        popB = popB_temp
        popC = popC_temp
    return popA, popB, popC
print(evolution_pop(0) , evolution_pop(3) , evolution_pop(5) )

popA, poB, popC = evolution_pop(0)
popA, poB, popC  = round(popA,0), round(poB,0), round(popC,0)
print(popA, poB, popC)
assert (popA, poB, popC) == (100000,80000,120000)

popA, poB, popC = evolution_pop(3)
popA, poB, popC  = round(popA,0), round(poB,0), round(popC,0)
print(popA, poB, popC)
assert (popA, poB, popC) == (116270, 117460, 66270)

popA, poB, popC = evolution_pop(5)
popA, poB, popC  = round(popA,0), round(poB,0), round(popC,0)
print(popA, poB, popC)
assert (popA, poB, popC) == (114624, 128252, 57124)





print("Multiplication par additions successives")
print("a^b = a*a* ... *a (b fois)")

def puissance(a, b):
    c=1 # compteur: nb de multiplications
    p=1 # produit: multiplication des a
    while c<=b:
        p=p*a
        print(c,p) # debug - à commanter dans la version finale
        c=c+1
    print(p)      
    return p

assert puissance(0, 5) == 0
assert puissance(3, 0) == 1
assert puissance(2, 6) == 64
assert puissance(3, 5) == 243

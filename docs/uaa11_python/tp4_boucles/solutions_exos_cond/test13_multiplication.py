print("Multiplication par additions successives")
print("a*b = a+a+ ... +a (b fois)")

def multiplication(a, b) :

    c=1 # compteur: nb d'additions
    s=0 # somme: additions des a
    while c<=b:
        s=s+a
        print(c,s) # debug - à commanter dans la version finale
        c=c+1
    print(s)
    return s 
    
assert multiplication(0, 5) == 0
assert multiplication(3, 0) == 0
assert multiplication(3, 5) == 15
assert multiplication(4, 6) == 24

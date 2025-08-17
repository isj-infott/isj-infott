print("Somme d'entiers")
print("Entre un nombre entier")

def somme(nb):
    c=0 # compteur
    s=0 # somme
    while c<=nb:
        s=s+c
        print(c,s) # debug - à commanter dans la version finale
        c=c+1
    print(s)      
    return s

assert somme(0) == 0
assert somme(1) == 1
assert somme(5) == 15
assert somme(10) == 55
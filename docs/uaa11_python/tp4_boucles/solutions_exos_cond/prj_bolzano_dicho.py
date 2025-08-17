from math import *
def f(x):
    # Entrée :x
    # Sortie: f(x)
    
    m,n,p,q = 3,-2,6,-4
    return (m*x**3 + n*x**2 + p*x + q)

def dichotomie (a , b , epsilon ):
    # Entrées: a, b (intervalle) epsilon (précision)
    # Sortie: racine
    
    while abs(f(b) - f(a)) > epsilon :
        m = ( a + b ) / 2
        if f ( m ) == 0:
            return m
        elif (f(a) > 0 and f(m) > 0) or (f(a) <0 and f(m) <0): 
            # si f(a) et f(m) sont de meme signe
            a = m
        else :  # sinon, f(b) et f(m) sont de meme signe
            b = m
    print(a,b,m)
    print(f(a),f(b),f(m))
    return m

a,b = 1,1
while(f(a) > 0 and f(b) > 0) or (f(a) <0 and f(b) <0): 
    # tant que f(a) et f(b) sont de meme signe
    a=int(input("a: "))
    b=int(input("b: "))
racine=round(dichotomie(a , b , 1e-5),5)
print("c: ",racine)
print("f(c): ", round(f(racine),5))

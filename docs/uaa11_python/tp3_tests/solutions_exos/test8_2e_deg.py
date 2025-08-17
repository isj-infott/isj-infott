from math import *
def eq_1er_deg(a, b):
    if a!=0:
        print(-b/a)
    else:
        print("impossible")

def eq_2e_deg(a, b, c):
    if a==0:                #1er deg
        eq_1er_deg(b, c)
    else:                   #2e deg
        delta=b**2-4*a*c
        if delta > 0:
            print("x1 = ",(-b+sqrt(delta))/(2*a))
            print("x2 = ",(-b-sqrt(delta))/(2*a))
        elif delta==0:
            print("x = ",-b/(2*a))
        else:
            print("pas de solution")
       
eq_2e_deg(0, 0, 10)
eq_2e_deg(0, 10, 0)
eq_2e_deg(0, 2, 10)
eq_2e_deg(1, 1, -2)
eq_2e_deg(1, 4, 4)
eq_2e_deg(1, 1, +20)

print("Equation du 2ème degré: ax^2+bx+c=0")
print("Entre a, b, c")
a=float(input())
b=float(input())
c=float(input())
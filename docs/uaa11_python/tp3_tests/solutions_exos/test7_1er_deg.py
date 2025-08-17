
def eq_1er_deg(a, b):
    if a!=0:
        print(-b/a)
    else:
        print("impossible")

eq_1er_deg(0, 10)
eq_1er_deg(10, 0)
eq_1er_deg(2, 10)

print("Equation du 1er degré: ax+b=0")
print("Entre a et b")
a=float(input())
b=float(input())
eq_1er_deg(a, b)
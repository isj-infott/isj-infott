def u(n, a, b, c):
    p=1
    u=a
    print("U",p," = ",u)
    while p<n:
        p=p+1
        u=b*u+c
        print("U",p," = ",u)
        
    return u

assert u(8, 1, 2, 0) == 128
assert u(8, 1, 1, 2) == 15
assert u(6, 2, 3, 4) == 970

def v(n):
    v = 101
    q = -3
    p = 1
    while p<n:
        p=p+1
        v=q*v
        print("v",p," = ",v)
        
    return v
assert v(4) == -2727
assert v(5) == 8181

def w(n):
    return (n*(-1)**n)/(n+1)

assert round(w(10),1) == 0.9
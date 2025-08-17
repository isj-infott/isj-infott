def somme_int(n):
    c = 0
    s = 0
    while c <= n:
        s = s + c
        print(c, s)
        c = c + 1
    return s

assert somme_int(0) == 0
assert somme_int(1) == 1
assert somme_int(10) == 55
assert somme_int(100) == 5050

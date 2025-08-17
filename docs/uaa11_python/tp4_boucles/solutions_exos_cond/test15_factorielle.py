def factorielle(n):
    fact = 1
    while n > 0:
        fact = fact * n
        print(n, fact)
        n = n -1
    return fact

assert factorielle(5) == 120
assert factorielle(8) == 40320
assert factorielle(0) == 1
assert factorielle(1) == 1

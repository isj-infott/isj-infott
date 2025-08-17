
def Fibonnacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        Fp_2=0
        Fp_1=1
        p=1
        while p<=n:
            Fp = Fp_1 + Fp_2
            print("F", p, " = ", Fp)
            Fp_2=Fp_1
            Fp_1=Fp
            p=p+1
        return Fp
    
assert Fibonnacci(1) == 0
assert Fibonnacci(2) == 1
assert Fibonnacci(6) == 13
assert Fibonnacci(10) == 89
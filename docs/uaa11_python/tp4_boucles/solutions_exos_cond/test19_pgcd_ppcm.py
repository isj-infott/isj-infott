def pgcdppcm(n1, n2):
    if n1 == 0 or n2 == 0:
        return (0, 0)
    div=2
    pgcd=1
    ppcm=1
    while (n1>1 or n2>1):
        if (n1%div==0 and n2%div==0):
            pgcd=pgcd*div
        if (n1%div==0 or n2%div==0):
            ppcm=ppcm*div
        if (n1%div==0) :
            n1=n1//div
        if (n2%div==0):
            n2=n2//div
        if (n1%div!=0 and n2%div!=0):
            div=div+1
    return (pgcd, ppcm)

#Exemple
#36= 1*2*2*3*3
#24= 2*2*2*3
#pgcd=2*2*3=12 # entiers qui sont des diviseurs de 36 ET 24
#ppcm=2*2*2*3*3=72 # entiers qui sont des diviseurs de 36 OU 24
assert pgcdppcm(24,36) == (12, 72)
assert pgcdppcm(30,42) == (6, 210)
assert pgcdppcm(0,0) == (0, 0)
assert pgcdppcm(0,1) == (0, 0)
assert pgcdppcm(1,0) == (0, 0)


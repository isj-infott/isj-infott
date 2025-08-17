def nb_1er(n):
    c=2
    while (c < n and n%c!=0):
        c=c+1
    if c  == n:
        print(n)

def nbs_1er_inf(n):
    i =1
    while i<=n:
        nb_1er(i)
        i=i+1

nbs_1er_inf(100)
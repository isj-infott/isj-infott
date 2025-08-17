# Sol1
def nbs_croissants(a, b, c):
    #trier les 2 premiers
    #trier les 2 derniers
    #retrier les 2 premiers

    if a > b :
        a,b = b,a   # on permute
    if b > c :
        b,c = c, b  # on permute => c est le plus grand
    if a > b :
        a,b = b,a   # on permute => b est le plus grand
    return (a, b, c)

assert nbs_croissants(5,7,8) == (5,7,8)
assert nbs_croissants(5,8,7) == (5,7,8)
assert nbs_croissants(7,5,8) == (5,7,8)
assert nbs_croissants(7,8,5) == (5,7,8)
assert nbs_croissants(8,5,7) == (5,7,8)
assert nbs_croissants(8,5,7) == (5,7,8)
assert nbs_croissants(8,1000000,7) == (7,8,1000000)


print("ALgo - 3 nbs par ordre croissant")
print("Entre 3 nombres")
a=float(input())
b=float(input())
c=float(input())  
print("nbs triés par ordre croissant: ", nbs_croissants(a, b, c))


""" # Sol2
if a<b :
    if b<c:
        print(a, b, c)
    elif a<c:
         print(a, c, b)
    else:
        print(c, a, b)
# etc ...  

# Sol3 fausse
if a<b :
    if b<c :
        print(a, b, c)
    else:
        print(a, c, b)
elif b<a :
    if a<c :
        print(b, a, c)
    else:
        print(b, c, a)
elif c<a :
    if a<b :
        print(c, a, b)
    else:
        print(c, b, a) """


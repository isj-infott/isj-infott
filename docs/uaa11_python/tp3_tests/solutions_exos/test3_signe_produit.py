
def signe_produit(a, b):
    if a ==0 or b==0:
        return "produit nul"
    elif a>0 and b>0 or a<0 and b<0:
        return "produit positif"
    else:
        return "produit negatif"

# Test
assert signe_produit(2, 3) == 'produit positif'
assert signe_produit(2, -3) == 'produit negatif'
assert signe_produit(-2, 3) == 'produit negatif'
assert signe_produit(-2, -3) == 'produit positif'
assert signe_produit(0, -3) == 'produit nul'
assert signe_produit(-2, 0) == 'produit nul'
assert signe_produit(0, 0) == 'produit nul'

print("Signe d'un produit a.b")
print("Entre a et b")
a=int(input())
b=int(input())
print(signe_produit(a, b))
    
2
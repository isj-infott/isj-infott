# Sol1
def max_4nb(a, b, c, d) :
    maxi = a
    if maxi < b:
        maxi = b
    if maxi < c:
        maxi = c
    if maxi < d:
        maxi = d
    return maxi

# Sol2
""" def max_4nb(a, b, c, d) :        
    if a>b and a>c and a>d:
        maxi=a
    elif b>a and b>c and b>d:
        maxi=b
    elif c>a and c>b and c>d:
        maxi=c    
    else:
        maxi=d
    return maxi """

#

# Test
assert max_4nb(30, 5, 13, 20) == 30
assert max_4nb(20, 30, 13, 5) == 30
assert max_4nb(20, 5, 30, 5) == 30
assert max_4nb(20, 5, 13, 30) == 30
assert max_4nb(20, 5, 13, 1000000000) == 1000000000
print("ALgo - Max de 4 nbs")
print("Entre 4 nombres")
a=float(input())
b=float(input())
c=float(input())
d=float(input())    

print(max_4nb(a, b, c, d), "est le max")

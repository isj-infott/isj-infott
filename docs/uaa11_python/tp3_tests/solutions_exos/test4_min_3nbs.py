# Sol1
def min_3nb(a, b, c) :
    mini = a
    if mini > b:
        mini = b
    if mini > c:
        mini = c
    return mini

# Sol2
""" def min_3nb(a, b, c) :        
    if a<b and a<c:
        mini=a
    elif b<a and b<c:
        mini=b
    else:
        mini=c
    return mini """

# Sol3
""" if a<b :
    if a<c :
        mini=a
    else:
        mini=c
elif b<c :
    mini=b
else :
    mini=c
print(mini, "est le min (sol2)") """

# Test
assert min_3nb(5, 20, 13) == 5
assert min_3nb(20, 5, 13) == 5
assert min_3nb(20, 13, 5) == 5
assert min_3nb(20, -13, 5) == -13
print("ALgo - Min de 3 nbs")
print("Entre 3 nombres")
a=float(input())
b=float(input())
c=float(input())    
print(min_3nb(a, b, c), "est le min (sol1")

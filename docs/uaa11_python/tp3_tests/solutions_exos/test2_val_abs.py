
def val_abs(a):
    if a>=0:
        return a
    else:
        return -a

# Test
assert val_abs(5) == 5
assert val_abs(-5) == 5
assert val_abs(0) == 0

print("valeur absolue")
print("Entre a")
a=int(input())
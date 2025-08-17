from test16_diviseurs import *
def n_parfait_1er(n):
    if n == 0:
        return False, False
    c=1
    s=0
    while (c < n):     # n exclu
        if (n%c==0):   # si c est un diviseur de n
            s=s+c
            print(c, end=" ")
        c=c+1
    print(s)
    
    if( s==n):
        parfait = True
    else:
        parfait = False
    if (s==1):
        premier = True
    else:
       premier = False
    return parfait, premier

assert n_parfait_1er(24) == (False, False)
assert n_parfait_1er(0) == (False, False)
assert n_parfait_1er(1) == (False, False)
assert n_parfait_1er(2) == (False, True)
assert n_parfait_1er(6) == (True, False)
assert n_parfait_1er(13) == (False, True)
assert n_parfait_1er(28) == (True, False)
assert n_parfait_1er(1093) == (False, True)

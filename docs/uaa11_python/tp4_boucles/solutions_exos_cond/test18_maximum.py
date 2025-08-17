def maximum():
    max = -1
    nb = 0
    i = 0
    pos = 0
    while nb >= 0 :
        nb = int(input("Entre un nombre:\n"))
        i = i+1
        if nb > max:
            max = nb
            pos = i
            print(pos, max)
    return pos, max

print(maximum())
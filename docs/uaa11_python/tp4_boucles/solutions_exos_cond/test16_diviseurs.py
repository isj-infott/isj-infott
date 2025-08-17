def diviseurs(n): 
    c = 1
    while c <= n:
        # print(c, n % c)
        if n % c == 0 :    # test si reste de division entière est nul
            print(c, end=" ")
        c = c +1
# ce code pas optimisé, réfléchis s'il n'est pas possible de faire moins d'itérations

diviseurs(24)

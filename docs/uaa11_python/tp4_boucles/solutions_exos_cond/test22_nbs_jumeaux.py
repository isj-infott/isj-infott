def nbs_jumeaux(n):
    i =2
    j=1
    while i<=n:
        c=2
        while (c < i and i%c!=0):
            c=c+1
        if c  == i:
            if (i-j)==2:
                print(i,j)
            j=i    
        i=i+1

nbs_jumeaux(50)
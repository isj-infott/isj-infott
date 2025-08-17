def socle(lgrsol, lgrsup):
        c=lgrsol
        vol=0
        while (c >= lgrsup):
                vol=vol+c*c*1
                print(c, vol)
                c=c-1
        return vol
        
assert socle(7, 3) == 135
assert socle(11, 5) == 476

from robot import *

def test1():
    set_dt(100)
    select_jeu(1)

    # nb lignes: 11
    pass     

def test2():
    set_dt(100)

    select_jeu(2)

    # nb lignes: 9
    pass
   

def test3():
    select_jeu(3)
    set_dt(100)

    # nb lignes: 7
    pass



test3()

base.mainloop()

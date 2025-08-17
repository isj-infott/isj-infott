def etat_eau(temp):
    if temp <= 0 :
        print( "C’est de la glace")
    elif temp > 0 and temp < 100 :
        print("C’est du liquide")
    else :
        print("C’est de la vapeur")

# Test
etat_eau(-15)
etat_eau(0)
etat_eau(5)
etat_eau(100)
etat_eau(150)

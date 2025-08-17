def consec():
        nbuser=0
        while (nbuser < 10 or nbuser > 20):
                nbuser = int(input("Choisis un nombre compris ente 10 et 20 "))
        c=1
        while (c <= 10):
                print(nbuser+c)
                c=c+1
consec()

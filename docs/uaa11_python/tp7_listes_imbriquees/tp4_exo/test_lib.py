def test_assert(resultat, attendu):
    maxi = max(len(str(resultat)), len(str(attendu)),20)
    try :
        assert  resultat == attendu
    except:
        print(f"!!! ERREUR ! Obtenu: {str(resultat):<{maxi}} \tAttendu: {str(attendu):<{maxi}}")
    else:
        print(f"OK ! \t     Obtenu: {str(resultat):<{maxi}} \tAttendu: {str(attendu):<{maxi}}")

imax=10                 # parcours des colonnes avec i 
jmax=8                  # parcours des lignes avec j 

liste2d= ['X']*jmax     # création d'une liste de 8 lignes 
for j in range(jmax) :  # création d'une sous-liste de 10 colonnes 
    liste2d[j]=['X']*imax

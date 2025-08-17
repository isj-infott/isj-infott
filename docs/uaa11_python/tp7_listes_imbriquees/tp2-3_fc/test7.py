# --- PYODIDE:ignore --- #
"""
Les sections `ignore` sont... ignorées. Vous pouvez les utiliser pour laisser
des commentaires dans vos fichiers, ou y archiver du code python qui ne sera
pas utilisé pour le site construit.
---------------------------------------------------------------------------

La section `env` (ci-dessous) est exécutée avant le code utilisateur.
Son contenu n'est pas visible de l'utilisateur mais tout ce qui y est défini
est ensuite disponible dans l'environnement.
Si le code de la section ENV lève une erreur, rien d'autre ne sera exécuté.
"""
# --- PYODIDE:env --- #

def test_assert(resultat, attendu):
    maxi = max(len(str(resultat)), len(str(attendu)),20)
    try :
        assert  resultat == attendu
    except:
        print(f"!!! ERREUR ! Obtenu: {str(resultat):<{maxi}} \tAttendu: {str(attendu):<{maxi}}")
    else:
        print(f"OK ! \t     Obtenu: {str(resultat):<{maxi}} \tAttendu: {str(attendu):<{maxi}}")



class Stack:
    """ (Interface à décrire dans l'énoncé) """
    def __init__(self): self.__stk=[]
    def push(self, v): self.__stk.append(v)
    def pop(self): return self.__stk.pop()
    def is_empty(self): return not self.__stk

# --- PYODIDE:ignore --- #
"""
La section `code` est l'état initial du code fourni à l'utilisateur dans
l'éditeur, à l'exclusion des tests publics (voir section `tests`).
"""
# --- PYODIDE:code --- #

def test7(chaines, mot):
    lst_rep = []
#    ...
    return lst_rep
    


# --- PYODIDE:ignore --- #
"""
La section `corr` contient le code qui sera affiché dans la correction, sous l'IDE.
"""
# --- PYODIDE:corr --- #

def test7(chaines, mot):
    lst_rep = []
    for p in range(len(chaines)):           # parcours des 2 sous-chaînes
        contient=False                      # initialisation du booléen pour chaque sous chaîne
        for l in range(len(chaines[p])):    # parcours des lignes de chaque sous-chaînes
            if mot in chaines[p][l]:        # verif. si mot est dans la ligne
                contient=True
        lst_rep.append(contient)            # rajout du bouléen dans la liste pour chaque sous-chaîne
    return lst_rep
        
# --- PYODIDE:ignore --- #
"""
La section `tests` contient les tests publics qui seront affichés sous le code
utilisateur, dans l'éditeur.
"""
# --- PYODIDE:tests --- #

chaines = [
    [
        "hello there",
        "comment allez-vous",
    ],
    [
        "goodbye world",
        "hello world",
    ]
]

assert test7(chaines, "goodbye") == [False, True]
assert test7(chaines, "comment") == [True, False]
assert test7(chaines, "hello") == [True, True]
assert test7(chaines, "python") == [False, False]

# --- PYODIDE:ignore --- #
"""
La section `secrets` contient les tests secrets pour les validations. Ces tests ne sont
pas visibles par l'utilisateur.

ATTENTION :
    Il est impératif d'utiliser des messages dans les assertions des tests secrets,
    sinon l'utilisateur ne peut pas déboguer son code car `print` est désactivé
    durant ces tests ! (sauf si... => Voir les options de configuration)
    À vous de choisir le niveau d'information que vous voulez fournir dans le message.

Par ailleurs, il est conseillé d'utiliser une fonction pour éviter que des variables
des tests ne se retrouvent dans l'environnement global.
"""
# --- PYODIDE:secrets --- #

def tests():
    pass

tests()         # Ne pas oublier d'appeler la fonction de tests... ! x)
del tests       # Si vous ne voulez pas laisser de traces...


# --- PYODIDE:post --- #
# La section post contient du code de "nettoyage", à appliquer systématiquement
# après que le code et les tests aient été lancés.
# Ce contenu est exécuté même si une erreur a été levée précédemment, SAUF si
# cette erreur provient de la section ENV.

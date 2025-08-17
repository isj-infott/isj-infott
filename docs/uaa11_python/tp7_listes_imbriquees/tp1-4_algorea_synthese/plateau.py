###################################################################################

M="█" # Mur
V=' ' # Vide
N='.' # nourriture
P='o' # Pacman
Z='z' # monstre

# algo4-3_trouver_sortie_1e / 3e => pour cs1a 
#y*x: 5*21
jeu1=[
        [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
        [M,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,M],
        [M,M,M,M,V,M,M,V,M,M,V,M,M,V,M,M,V,M,M,V,M],
        [M,M,M,M,V,M,M,V,M,M,V,M,M,V,M,M,V,M,M,V,M],
        [M,M,M,M,V,V,V,V,M,M,V,V,V,V,M,M,V,V,V,V,M],
        [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M]
    ]
#y*x: 6*15
jeu2=[
        [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M],
        [M,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,V,M],
        [M,M,M,M,V,M,M,V,M,M,M,V,M,M,V,M,M,M,M,V,M,M,V,M],
        [M,M,M,M,V,M,M,V,M,M,M,V,M,M,V,M,M,M,M,V,M,M,V,M],
        [M,M,M,M,V,V,V,V,M,M,M,V,V,V,V,M,M,M,M,V,V,V,V,M],
        [M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M,M]
   ]

#y*x: 13*15
jeu3=[
        [M,M,M,M,M,M,M,M,M,M,M,M],
        [M,V,M,M,M,M,M,M,M,M,M,M],
        [M,V,V,V,V,V,V,V,V,V,V,M],
        [M,V,M,M,M,M,M,M,M,M,M,M],
        [M,V,V,V,V,V,V,V,V,V,V,M],
        [M,V,M,M,M,M,M,M,M,M,M,M],
        [M,V,V,V,V,V,V,V,V,V,V,M],
        [M,V,M,M,M,M,M,M,M,M,M,M],       
        [M,V,V,V,V,V,V,V,V,V,V,M],
        [M,V,M,M,M,M,M,M,M,M,M,M],
        [M,V,M,M,M,M,M,M,M,M,M,M],
        [M,M,M,M,M,M,M,M,M,M,M,M]

]



# Position initiale pour chaque jeu Pacman / Monstre
posini = {
    'jeu1': (1, 1, 19, 1),      # x,y / xz,yz
    'jeu2': (1, 1, 22, 1),
    'jeu3': (1, 1, 1, 10)  
}

###################################################################################

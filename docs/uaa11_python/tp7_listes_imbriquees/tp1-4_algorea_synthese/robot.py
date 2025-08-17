# Python Guide / Getting started
import time
from tkinter import *
from plateau import *

# Var de jeu
jeu=jeu1
x,y,xz,yz=posini['jeu1']
imax=len(jeu[0])
jmax=len(jeu)

# Var globales
dt=500
dtabs=dt
t_delay=500
debug=False     # message activé pac dans un mur
dir=2
listdir=[(1,0),(0,-1),(-1,0),(0,1)]     # est, nord, ouest, sud
couleur={M:'green', V:'yellow', P:'blue', Z: 'red'}
clgr=50

# Var tk
base = Tk()
base.title("tk")
can = Canvas(base, width=clgr*imax, height=clgr*jmax, bg="white")
can.pack()
pac = None
monstre = None

def create_game_board():
    global pac, monstre
    imax=len(jeu[0])
    jmax=len(jeu)
    print(imax,jmax)

    can.delete("all")  # Efface tout
    # Ajuste la taille du Canvas en fonction du jeu sélectionné
    can.config(width=clgr * imax, height=clgr * jmax)

    jeu_tk=[]
    for j in range(jmax):
        ligne_tk=[]
        for i in range(imax):
            x1=i*clgr
            x2=x1+clgr
            y1=j*clgr
            y2=y1+clgr
    #        carre=can.create_rectangle(x1,y1,x2,y2, fill=couleur[liste2d[j][i]], outline='white')
            carre=can.create_rectangle(x1,y1,x2,y2, fill=couleur[jeu[j][i]], outline='white')
    
            ligne_tk.append(carre)
        jeu_tk.append(ligne_tk)

    # Positionner Pacman et monstre
    xp, yp = x*clgr, y*clgr             # pos pacman
    xpz, ypz  =xz*clgr, yz*clgr             # pos monstre
    monstre=can.create_oval(xpz,ypz,xpz+clgr, ypz +clgr, fill=couleur[Z], outline='')
    pac=can.create_oval(xp,yp,xp+clgr, yp +clgr, fill=couleur[P], outline='')

    button_quit = Button(base, text="Quitter", command=base.quit)
    button_quit.pack(pady=10)

def pac_update():
    can.coords(pac, x*clgr,y*clgr,(x+1)*clgr,(y+1)*clgr)

def set_dt(duree):
    global dt, dtabs
    dt=duree
    dtabs=duree



# Fonctions de mouvement

def estMur():
    global x
    if jeu[y][x+1]==M:
        print("Collision dans un mur !")
    else:    
        x+=1
        pac_update()
    if debug:
        print("estMur", x, y)

def ouestMur():
    global x
    if jeu[y][x-1]==M:
        print("Collision dans un mur !")
    else:    
        x-=1
        pac_update()
    if debug:
        print("ouestMur", x, y)

def sudMur():
    global y
    if jeu[y+1][x]==M:
        print("Collision dans un mur !")
    else:    
        y+=1
        pac_update()
    if debug:
        print("sudMur", x, y)

def nordMur():
    global y
    if jeu[y-1][x]==M:
        print("Collision dans un mur !")
    else:    
        y-=1
        pac_update()
    if debug:
        print("nordMur", x, y)

# Fonctions de déplacement avec délai

def est():
    global dtabs
    base.after(dtabs, estMur)
    dtabs+=dt

def ouest():
    global dtabs
    base.after(dtabs, ouestMur)
    dtabs+=dt

def sud():
    global dtabs
    base.after(dtabs, sudMur)
    dtabs+=dt

def nord():
    global dtabs
    base.after(dtabs, nordMur)
    dtabs+=dt

def select_jeu(nb_plateau):
    global jeu, x, y, xz, yz
    if nb_plateau==1:
        jeu = jeu1
        x, y, xz, yz = posini['jeu1']
    if nb_plateau==2:
        jeu = jeu2
        x, y, xz, yz = posini['jeu2']    
    elif nb_plateau==3:
        jeu = jeu3
        x, y, xz, yz = posini['jeu3']
    else:
        print("Plateau sélectionné pas disponible")
    create_game_board()


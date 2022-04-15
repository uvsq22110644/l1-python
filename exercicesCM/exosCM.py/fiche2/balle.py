#import des librairies
import tkinter as tk
import random as rd

#variables globales
LARGEUR = 600
HAUTEUR = 400
r = 20

#mouvement
boule_bouge = True

#fonction
def creer_balle():
    """crée balle au milieu"""
    xmil = LARGEUR//2
    ymil = HAUTEUR//2
    cercle = canvas.create_oval(xmil-r,ymil-r,xmil+r,ymil+r, fill="blue")
    x = rd.randint(1,7)
    y = rd.randint(1,7)
    return [cercle, x, y]

def demarrer():
    global cont, boule_bouge
    if boule_bouge:
        mouvement()
        bouton.config(text="Arrêter")
    else:
        racine.after_cancel(cont)
        bouton.config(text="Démarrer")
    boule_bouge = not boule_bouge

def mouvement():
    global cont
    rebond2()
    canvas.move(balle[0],balle[1],balle[2])
    cont = racine.after(20, mouvement)

def rebond():
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0<0 or x1>LARGEUR:
        balle[1] = -balle[1]
    elif y0<0 or y1>HAUTEUR:
        balle[2] = -balle[2]

def rebond2():
    global HAUTEUR, LARGEUR
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0<-40:
        canvas.coords(balle[0], LARGEUR, y0, LARGEUR +20, y1)
    if x1>LARGEUR+40:
        canvas.coords(balle[0],0, y0, 40, y1)
    if y0<-40:
        canvas.coords(balle[0], x0, HAUTEUR ,x1, HAUTEUR+40)
    if y1>HAUTEUR+40:
        canvas.coords(balle[0], x0, 0, x1, 40)



#######################


#création widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height= HAUTEUR)
bouton = tk.Button(racine, text="Démarrer", command=demarrer)


#appel fonction
balle = creer_balle()

#placement des widgets
racine.grid()
canvas.grid()
bouton.grid()

#boucle principale
racine.mainloop()
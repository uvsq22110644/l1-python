#import des librairies
import tkinter as tk
import random as rd

#état de la balle
est_fixe = False

#état bouton
n = 0 #(pair = démarrer, impair=arreter)

#coordonnées canvas
HEIGHT = 400
WIDTH = 600

#coordonnées balle au début
x,y,x1,y1 = 295,195,305,205

#variables gloables
id_balle = 0
balle = []
c = 0

#fonctions
"""retourne l'identifiant de la balle et 2 chiffres en tre 1 et 7"""
def creer_balle():
    global id_balle
    id_balle = canvas.create_oval(295,195,305,205, fill="blue")
    a = rd.randint(1,7)
    b = rd.randint(1,7)
    balle.extend([id_balle, a, b])
    return balle

def mouvement():
    """prend une balle en entrée et la déplace de balle[1] horizontalement et balle[2] verticalement"""
    global x,y,x1,y1, c, est_fixe, id, n 
    if est_fixe:
        return
    canvas.delete(c)
    c = canvas.coords(id_balle, x+balle[1], y+balle[2], x1+balle[1], y1+balle[2])
    x,y,x1,y1 = x+balle[1], y+balle[2], x1+balle[1], y1+balle[2]
    id = racine.after(20,mouvement)
    if n%2 == 0:
        est_fixe = False
        bouton.config(text="Arreter")
        n += 1
    elif n%2 != 0:
        est_fixe = True
        bouton.config(text="Démarrer")
        n +=1
        racine.after_cancel(id)



#création des widgets
racine=tk.Tk()
canvas=tk.Canvas(racine, bg="black", width=WIDTH, height=HEIGHT)
bouton=tk.Button(racine, text="Démarrer", command=mouvement)

#placement des widgets
racine.grid()
canvas.grid()
bouton.grid()

#création de la balle
b = creer_balle()

#Faire en sorte que lorsque l’on clique sur le bouton “Démarrer”, alors son texte change et devienne “Arrêter”, et que, quand on clique sur le bouton “Arrêter”, la balle s’arrête et le bouton se renomme “Démarrer”,
#et ainsi de suite. Utiliser la méthode .after_cancel() pour cela.

#boucle principale
racine.mainloop()

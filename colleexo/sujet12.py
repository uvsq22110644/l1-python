from multiprocessing import cpu_count
import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

cpt = 0 

###################
# Fonctions

def creer_balle():
    """Dessine un disque bleu et retourne son identifiant
     et les valeurs de déplacements dans une liste"""
    x, y = LARGEUR // 2, HAUTEUR // 2
    dx, dy = 3, 5
    rayon = 20
    cercle = canvas.create_oval((x-rayon, y-rayon),(x+rayon, y+rayon), fill="blue")
    return [cercle, dx, dy]


def mouvement():
    """Déplace la balle et ré-appelle la fonction avec un compte-à-rebours"""
    rebond()
    changement_couleur()
    compteur()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        cpt += 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        cpt += 1

def zones():
    """crée 4 zones"""
    rec_r = canvas. create_rectangle(0, 0, 150, 50, fill="red")
    rec_v = canvas. create_rectangle(150, 0, 300, 50, fill="green")
    rec_b = canvas. create_rectangle(300, 0, 450, 50, fill="blue")
    rec_j = canvas. create_rectangle(450, 0, 600, 50, fill="yellow")

def changement_couleur():
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if y0 <= 30:
        if 0<=x0 and x0<=150:
            canvas.itemconfigure(balle[0], fill="red")
        elif 150<=x0 and x0<=300:
            canvas.itemconfigure(balle[0], fill="green")
        elif 300<=x0 and x0<=450:
            canvas.itemconfigure(balle[0], fill="blue")
        elif 450<=x0 and x0<=600:
            canvas.itemconfigure(balle[0], fill="yellow")
    elif y1 >= 400:
        canvas.itemconfigure(balle[0], fill="white")

def compteur():
    global cpt
    if cpt == 30:
        canvas.delete(balle[0])

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()

# déplacement de la balle
mouvement()
zones()


# boucle principale
racine.mainloop()
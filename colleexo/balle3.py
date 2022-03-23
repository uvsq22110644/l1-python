import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

# autres
est_rond = True
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
    compteur()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)



def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]

def compteur():
    global cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600 or y0 <= 0 or y1 >= 400 :
        cpt += 1
    transformation()


def transformation():
    global l, est_rond, cpt
    if cpt % 5 == 0 and cpt != 0 and cpt != 30:
        canvas.after(transformation)
        if est_rond:
            l = canvas.coords(balle[0])
            canvas.delete(balle[0])
            balle[0] = canvas.create_rectangle(l[0], l[1], l[2], l[3], fill="blue")
            l = []
            est_rond = False
        else:
            l = canvas.coords(balle[0])
            canvas.delete(balle[0])
            balle[0] = canvas.create_oval(l[0], l[1], l[2], l[3], fill="blue")
            l = []
            est_rond = True
    elif cpt == 30:
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




# boucle principale
racine.mainloop()
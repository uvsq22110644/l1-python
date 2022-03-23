import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

# variables gloables
cpt = 0

# rond ou carré
est_rond = True


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
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle
    if est_rond:
        a0, b0, a1, b1 = canvas.coords(balle[0])
        if a0 <= 0 or a1 >= 600:
            balle[1] = -balle[1]
        if b0 <= 0 or b1 >= 400:
            balle[2] = -balle[2]
    else:
        c0, d0, c1, d1 = canvas.coords(rectangle)
        if c0 <= 0 or c1 >= 600:
            balle[1] = -balle[1]
        if d0 <= 0 or d1 >= 400:
            balle[2] = -balle[2]




def compteur():
    global cpt
    if cpt<= 5 or 5<cpt<=10 or 15<cpt<=20 or 25<cpt<=30 :  # est_rond
        a0, b0, a1, b1 = canvas.coords(balle[0])
        if a0 <= 0 or a1 >= 600 or b0 <= 0 or b1 >= 400 :
            cpt += 1
    else:
        c0, d0, c1, d1 = canvas.coords(rectangle)
        if c0 <= 0 or c1 >= 400 or d0 <= 0 or d1 >= 400:
            cpt += 1


def transformation():
    global l, est_rond, rectangle
    compteur()
    if cpt % 5 == 0 and cpt != 30:
        if est_rond:
            l = canvas.coords(balle[0])
            canvas.delete(balle[0])
            balle[0] = canvas.create_rectangle(l[0], l[1], l[2], l[3], fill="blue")
            l = []
        else:
            l = canvas.coords(rectangle)
            canvas.delete(rectangle)
            balle[0] = canvas.create_oval(l[0], l[1], l[2], l[3], fill="blue")
            l = []
    elif cpt == 30:
        canvas.delete(balle[0])
    else:
        pass


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

transformation()

# boucle principale
racine.mainloop()
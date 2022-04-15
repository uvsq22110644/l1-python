import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

# début du programme ou pas
début = True

# variables gloables
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
    touche_ligne()
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

def touche_ligne():
    """détourne la balle si elle touche la ligne et la déplace"""
    global début, cpt
    x0,y0,x1,y1 = canvas.coords(balle[0])
    if début:      
        if y0>=180 and y0>=220:
            début = False
            return
    elif y0 <= HAUTEUR/2:
        balle[2] = -balle[2]
        cpt += 1
        x0, y0, x1, y1 = canvas.coords(ligne)
        canvas.coords(ligne,x0, y0-5, x1, y1-5 )

def compteur():
    if cpt == 30:
        canvas.delete(ligne)

######################
# programme principal

# création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
canvas.grid()

# initialisation de la balle
balle = creer_balle()

# création ligne
ligne = canvas.create_line(0, HAUTEUR/2, LARGEUR, HAUTEUR/2, fill="white")

# déplacement de la balle
mouvement()


# boucle principale
racine.mainloop()
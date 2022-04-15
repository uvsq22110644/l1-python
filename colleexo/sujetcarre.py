import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

# autres
est_rond = True
ch1, ch2, ch3, ch4 = True, True, True, True
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
    transformation()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas"""
    global balle, cpt
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if x0 <= 0 or x1 >= 600:
        balle[1] = -balle[1]
        cpt+= 1
    if y0 <= 0 or y1 >= 400:
        balle[2] = -balle[2]
        cpt += 1


def transformation():
    """transforme la balle en carré et efface l'objet au bout de 30 rebonds"""
    global cpt, ch1, ch2, ch3, ch4
    if cpt == 5:
        if ch1:
            x0, y0, x1, y1 = canvas.coords(balle[0])
            canvas.delete(balle[0])
            balle[0] = canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            ch1 = False    
    if cpt == 10:
        if ch2:
            x0, y0, x1, y1 = canvas.coords(balle[0])
            canvas.delete(balle[0])
            balle[0] = canvas.create_oval(x0, y0, x1, y1, fill="blue")
            ch2 = False 
    if cpt == 15:
        if ch3:
            x0, y0, x1, y1 = canvas.coords(balle[0])
            canvas.delete(balle[0])
            balle[0] = canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            ch3 = False 
    if cpt == 20:
        if ch4:
            x0, y0, x1, y1 = canvas.coords(balle[0])
            canvas.delete(balle[0])
            balle[0] = canvas.create_oval(x0, y0, x1, y1, fill="blue")
            ch4 = False 
    if cpt == 25:
        if ch5:
            x0, y0, x1, y1 = canvas.coords(balle[0])
            canvas.delete(balle[0])
            balle[0] = canvas.create_rectangle(x0, y0, x1, y1, fill="blue")
            ch5 = False 
    if cpt == 30:
        canvas.delete(balle[0])


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

# boucle principale
racine.mainloop()
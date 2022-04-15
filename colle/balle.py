import tkinter as tk

##################
# Constantes

LARGEUR = 600
HAUTEUR = 400

# compteur de rebonds et de passages
cpt = 0
nbr_rebond = 0

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
    ligne()
    canvas.move(balle[0], balle[1], balle[2])
    canvas.after(20, mouvement)


def rebond():
    """Fait rebondir la balle sur les bords du canevas ou la laisse passer"""
    global balle, cpt, nbr_rebond
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if cpt <= 9:
        if x0 <= 0 or x1 >= 600:
            balle[1] = -balle[1]
            nbr_rebond += 1
        if y0 <= 0 or y1 >= 400:
            cpt += 1
            passage_haut_bas()
    elif cpt >= 10 and cpt < 20:
        if x0<0 or x1>LARGEUR:
            cpt += 1
            passage_haut_bas()
        elif y0<0 or y1>HAUTEUR:
            balle[2] = -balle[2]
            nbr_rebond += 1

def ligne():
    """crée ligne quand cpt vaut 10"""
    if cpt == 10:
        canvas.create_line(0, 0, 600, 0, width=5,fill = "white")
        canvas.create_line(0,400, 600, 400, width=5,fill="white")


def passage_haut_bas():
    """permet passage de haut en bas ou de gauche à droite en fonction du compteur"""
    x0, y0, x1, y1 = canvas.coords(balle[0])
    if y0 <= -40: 
        canvas.coords(balle[0], x0, HAUTEUR ,x1, HAUTEUR-40)
    if y1 >= 440:
        canvas.coords(balle[0], x0, 0, x1, 40)
    if x0<-40:
        canvas.coords(balle[0], LARGEUR, y0, LARGEUR+40, y1)
    if x1>LARGEUR+40:
        canvas.coords(balle[0],0, y0, 40, y1)

def compteur():
    """arrete la balle au bout de 20 rebonds"""
    global nbr_rebond
    if nbr_rebond == 20:
       balle[1], balle[2] = 0, 0


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
# import librairies
import tkinter as tk

# constantes
HAUTEUR = 500
LARGEUR = 500

# variables globales
liste = []

#état bouton
est_pause = True

# état du canevas
est_fixe = False

# fonctions 
def clics(event):
    global x
    if est_fixe:
        return
    liste.append(event.x)
    print(liste, event.x)
    creation_ligne()

def creation_ligne():
    global liste, milieu2, milieu, ligne1, ligne2
    if len(liste) == 2:
        milieu = (liste[0]+liste[1])/2
        ligne1 = canvas.create_line(milieu, 0, milieu, HAUTEUR, fill="blue")
    elif len(liste) == 4:
        milieu2 = (liste[2]+liste[3])/2
        ligne2 = canvas.create_line(milieu2, 0, milieu2, HAUTEUR, fill="red")
    elif len(liste) == 5:
        canvas.delete(ligne1, ligne2)
        liste = []
    else: 
        return

def suspend():
    global est_fixe, est_pause
    if est_pause:
        bouton.config(text="Restart")
        est_fixe = True
        est_pause = False
    else:
        bouton.config(text="Pause")
        est_fixe = False
        est_pause = True


################################
# programme
################################


# création widget
racine = tk.Tk()
canvas = tk.Canvas(racine,width = LARGEUR, height = HAUTEUR, bg="white")
bouton = tk.Button(racine, text="Pause", command=suspend)

# placement des widgets
racine.grid()
canvas.grid()
bouton.grid()

# gestion clic
canvas.bind("<Button-1>", clics)

# boucle principale
racine.mainloop()
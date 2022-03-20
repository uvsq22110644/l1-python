import tkinter as tk

# variable qui permet de choisir la couleur du rectangle
couleur = 0

# dit si  la couleur est  fixe
est_fixe = False

# coordonnées des sommets du rectangle:
x1, y1 = 150, 150
x2, y2 = 350, 350

#fonction
def gestion_clic(event):
    """fonction qui gère le clic sur le canevas"""
    global est_fixe, couleur
    if est_fixe:
        return
    liste_couleurs = ["red", "blue"]
    if x1< event.x <x2 and y1<event.y<y2:
        couleur = 1-couleur
        canvas.itemconfigure(rectangle, fill=liste_couleurs[couleur])
    else:
        est_fixe = True

def restart():
    global couleur, est_fixe
    est_fixe = False
    couleur = 0
    canvas.itemconfigure(rectangle="red")


#création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=500, height=500)
bouton = tk.Button(racine, text="Recommencer", command=restart)


#positionnement des widgets
canvas.grid()
bouton.grid()

#création rectangle rouge
rectangle = canvas.create_rectangle(x1,y1,x2,y2,fill="red")

#liaison du clic
canvas.bind("<Button-1>", gestion_clic)

#boucle principale
racine.mainloop()
#import module
import tkinter as tk

#couleur triangle
est_rouge = True
est_fixe = False

#constantes
LARGEUR = 500
HAUTEUR = 500
X,Y,X1,Y1 = 200,200,300,300

#fonctions
def gestion_clic(event):
    global est_fixe, est_rouge
    if est_fixe:
        return
    if X <event.x< X1 or Y <event.y <Y1:
        if est_rouge:
            canvas.itemconfigure(rectangle, fill="blue")
        else:
            canvas.itemconfigure(rectangle, fill="red")
        est_rouge = not est_rouge
    else:
        est_fixe = True

def recommencer():
    global est_fixe
    canvas.itemconfigure(rectangle, fill="red")
    est_fixe = False



#########################################
#création widget
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="black", width=LARGEUR, height=HAUTEUR)
bouton = tk.Button(racine, text="Recommencer", command=recommencer)

#placement des widgets
racine.grid()
canvas.grid()
bouton.grid()

#création rectangle rouge
rectangle = canvas.create_rectangle(X,Y,X1,Y1, fill="red")

#gestion clic
canvas.bind("<Button-1>", gestion_clic)


#boucle principale
racine.mainloop()
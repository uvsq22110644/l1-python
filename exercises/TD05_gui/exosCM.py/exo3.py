import tkinter as tk


#variables
nb_croix = 0
nb_cercles = 0
nb_carrés = 0

#fonctions
def croix(event):
    """gestion clic partie gauche"""
    global nb_croix, nb_carrés
    X, Y = event.x, event.y
    if 0<X<500/3 :
        if nb_croix < 2:
            canvas.create_rectangle(X-25,Y-25,X+25,Y+25, fill="white")
            canvas.create_line(X-25,Y-25,X+25,Y+25, fill ="blue", width=5)
            canvas.create_line(X+25,Y-25,X-25,Y+25, fill ="blue", width=5)
            nb_croix += 1
            nb_carrés += 1
        else:
            return

def carré(event):
    """gestion clic partie milieu"""
    global nb_carrés
    X, Y = event.x, event.y
    if 500/3<X<1000/3:
        if nb_carrés < 3:
            canvas.create_rectangle(X-25,Y-25,X+25,Y+25, fill="green")
            nb_carrés += 1
        else:
            return

def cercle(event):
    """gestion clic partie droite"""
    global nb_cercles
    X, Y = event.x, event.y
    if 1000/3<X<500:
        if nb_cercles < 3:
            canvas.create_oval(X-25,Y-25,X+25,Y+25, outline="red")
            nb_cercles += 1
        else:
            return

def redemarrer():
    éléments = canvas.find_enclosed(0, 0, 500, 500)
    print(éléments)
    canvas.delete(éléments)


#création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "black", height = 500, width = 500)
bouton = tk.Button(racine, text = "Redémarrer", command=redemarrer)


#création des colonnes
for i in range(1, 3):
    x = 500/3
    canvas.create_line(x*i,0,x*i,500,fill="white",)

#positionnement des widgets
canvas.pack()
bouton.pack()

#liaison des clic
canvas.bind("<Button-1>", croix)
canvas.bind("<Button-1>", carré)
canvas.bind("<Button-1>", cercle)



#boucle principale
racine.mainloop()

#Tant qu’il y a strictement moins de 3 cercles, un clic dans la partie droite affiche 
# un cercle rouge de rayon 50 centré sur le clic, et sinon ça ne fait rien.
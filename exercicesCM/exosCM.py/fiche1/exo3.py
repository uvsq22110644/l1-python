import tkinter as tk

#liste avee les objets
l =[]

#vraibles
carré, cercle, croix = 0, 0, 0

#variables
nb_croix = 0
nb_cercles = 0
nb_carrés = 0

#fonctions
def forme(event):
    """gestion clic partie gauche"""
    global nb_croix, nb_carrés, nb_cercles, croix, carré, cercle, ligne1, ligne2
    X, Y = event.x, event.y
    if 0<X<500/3 :
        if nb_croix < 2:
            carré = canvas.create_rectangle(X-25,Y-25,X+25,Y+25, fill="white")
            ligne1 = canvas.create_line(X-25,Y-25,X+25,Y+25, fill ="blue", width=5)
            ligne2 = canvas.create_line(X+25,Y-25,X-25,Y+25, fill ="blue", width=5)
            l.append(carré)
            l.append(ligne1)
            l.append(ligne2)
            nb_croix += 1
            nb_carrés += 1
    elif 500/3<X<1000/3:
        if nb_carrés < 3:
            carré = canvas.create_rectangle(X-25,Y-25,X+25,Y+25, fill="green")
            l.append(carré)
            nb_carrés += 1
    elif 1000/3<X<500:
        if nb_cercles < 3:
            cercle = canvas.create_oval(X-25,Y-25,X+25,Y+25, outline="red")
            l.append(cercle)
            nb_cercles += 1


def redemarrer():
    for i in range(len(l)):
        canvas.delete(int(l[i]))



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
canvas.bind("<Button-1>", forme)

#boucle principale
racine.mainloop()

#Tant qu’il y a strictement moins de 3 cercles, un clic dans la partie droite affiche 
# un cercle rouge de rayon 50 centré sur le clic, et sinon ça ne fait rien.
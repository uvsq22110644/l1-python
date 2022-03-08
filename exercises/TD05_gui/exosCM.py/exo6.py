import tkinter as tk

#variables globales
l=[] #liste avce les couleurs 


#fonctions
def gestion_clic(event):
    global couleur, carré, l
    if 0<event.x<150 and 0<event.y<50:
        if 0<event.x<50:
            canvas.itemconfigure(cercle, outline="green")
            l.append("green")
        if 50<event.x<100:
            canvas.itemconfigure(cercle, outline="yellow")
            l.append("yellow")
        if 100<event.x<150:
            canvas.itemconfigure(cercle, outline="blue")
            l.append("blue")
    else:
        canvas.itemconfigure(cercle, outline="black")
        l.append("black")
        

def annuler_clic():
    del l[-1] 
    canvas.itemconfigure(cercle, outline=l[-1])  
     
  
#création widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="white", width=500, height=500)
bouton = tk.Button(racine, text="Annuler", command=annuler_clic)

#positionnement des widgets
racine.grid()
canvas.grid()
bouton.grid()

#création objets
carré_v = canvas.create_rectangle(0, 0, 50, 50, fill="green")
carré_j = canvas.create_rectangle(50, 0, 100, 50, fill="yellow")
carré_b = canvas.create_rectangle(100, 0, 150, 50, fill="blue")
cercle = canvas.create_oval(225, 225, 275, 275, outline="black")

#lien clic
canvas.bind("<Button-1>", gestion_clic)

#boucle principale
racine.mainloop()
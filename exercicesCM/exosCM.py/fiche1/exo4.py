import tkinter as tk

#dit si le carré est fixe
est_fixe = False

#état du bouton
n = 0  #pair=pause

#fonction
def gestion_clic_i(event):
    global C, x0, y0, x1, y1, carré, est_fixe
    if est_fixe:
        return
    if x0< event.x <x1 and y0< event.y <y1 and C >= 20:
        x0, y0, x1, y1 = x0+5, y0+5, x1-5, y1-5
        canvas.delete(carré)
        carré = canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        C = C-10
    elif (0<event.x<x0 or x1<event.x<500) and (0<event.y<y0 or y1<event.y<500) and C <= 100:
        x0, y0, x1, y1 = x0-5, y0-5, x1+5, y1+5
        canvas.delete(carré)
        carré = canvas.create_rectangle(x0, y0, x1, y1, fill="red")
        C = C+10
        

def etat_bouton():
    global est_fixe, n
    if n%2 == 0:
        est_fixe = True
        bouton.config(text="Restart")
        n +=1
    elif n%2 != 0:
        est_fixe = False
        bouton.config(text="Pause")
        n +=1
        

#milieu du carré
M = 250
x0, y0, x1, y1 = M-25,M-25,M+25,M+25
C = 50

#création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "white", height = 500, width = 500)
bouton = tk.Button(racine, text = "Pause", command=etat_bouton)

#création carré
carré = canvas.create_rectangle(x0, y0, x1, y1, fill="red")

#liaison des clics
canvas.bind("<Button-1>", gestion_clic_i)

#positionnement des widgets
canvas.grid()
bouton.grid()

#boucle principale
racine.mainloop()
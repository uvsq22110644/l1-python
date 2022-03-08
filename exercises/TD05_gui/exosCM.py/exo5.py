import tkinter as tk

#coordonnées lignes de départ
x0, y0, x1, y1 = 200, 0, 200, 600
x2, y2, x3, y3 = 400, 0, 400, 600

#
appui_bouton = False

#fonctions
def gestion_clic(event):
    """gestion clic sur canevas"""
    global x0, y0, x1, y1, x2, y2, x3, y3
    if appui_bouton:
        return
    if event.x < x0:
        canvas.coords(ligne1, x0-10, y0, x1-10, y1)
        canvas.coords(ligne2, x2-10, y2, x3-10, y3)
        x0, x1, x2, x3 = x0-10, x1-10, x2-10, x3-10
    elif event.x > x2:
        canvas.coords(ligne1, x0+10, y0, x1+10, y1)
        canvas.coords(ligne2, x2+10, y2, x3+10, y3)
        x0, x1, x2, x3 = x0+10, x1+10, x2+10, x3+10
    elif x0<event.x<x2:
        canvas.coords(ligne1, x0+10, y0, x1+10, y1)
        canvas.coords(ligne2, x2-10, y2, x3-10, y3)
        x0, x1, x2, x3 = x0+10, x1+10, x2-10, x3-10

def restart():
    canvas.coords(ligne1, 200,0,200,600)
    canvas.coords(ligne2, 400,0,400,600)

#création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "white", height = 600, width = 600)
bouton = tk.Button(racine, text = "Pause", command=restart)

#création des lignes verticales
ligne1 = canvas.create_line(200,0,200,600,fill="red",)
ligne2 = canvas.create_line(400,0,400,600,fill="blue",)


#positionnement des widgets
canvas.grid()
bouton.grid()

#liaison du clic
canvas.bind("<Button-1>", gestion_clic)

#boucle principale
racine.mainloop()
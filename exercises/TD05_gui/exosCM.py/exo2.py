import tkinter as tk

#variable qui compte le nombre de clic de l'utilisateur
clic = 0

#position des lignes
x1, y1 = 0,0

#fonctions
def gestion_clic(event):
    global x1,y1
    if clic == 2:
        x1 = event.x
        y1 = event.y
        x2 = j
    else:
        return









#création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg="white", width=500, height=500)
bouton = tk.Button(racine, text="Pause")

#boucle principale
racine.mainloop()
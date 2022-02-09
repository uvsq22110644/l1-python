#exercice 1
#1
import tkinter as tk
racine = tk.Tk()
canv = tk.Canvas(racine, bg = "black", height = 500, width = 500)
canv.pack()
bt = tk.Button(racine, text = "recommencer")
bt.pack()
#2
canv.create_rectangle(23,50,200,200, outline="red", fill="red")
canv.pack()

def couleur(click):
    pass
    canv.create_rectangle(23,50,200,200, outline="red", fill="blue")

canv.bind("<Button-1>", couleur)


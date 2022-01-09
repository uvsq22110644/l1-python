import tkinter as tk
import random as rd


root = tk.Tk()
root.title("Mon dessin")
CANVAS_WIDTH, CANVAS_HEIGHT = 500, 500
canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT, bg = "black")

couleur = "orange"


def draw_pixel(x,y,colour):
    canvas.create_line((x,y), (x+1,y+1), fill = colour)

def get_colour(r,g,b):
    return '#{:02x}{:02x}{:02x}'.format(r,g,b)

def ecran_aleatoire():
    for i in range(256):
        for j in range(256):
            colour = get_colour(rd.randint(0,255), rd.randint(0,255), rd.randint(0,255))
            draw_pixel(i,j,colour)


def cercle():
    x = rd.randint(0,400)
    y = rd.randint(0,400)
    canvas.create_oval((x,y), (x+100,y+100), fill = "yellow")
def carre():
    x = rd.randint(0,400)
    y = rd.randint(0,400)
    canvas.create_rectangle((x,y), (x+100,y+100), fill = "pink")
def croix():
    x = rd.randint(0,400)
    y = rd.randint(0,400)
    canvas.create_line((x,y), (x+100,y+100), fill = couleur, width=5)
    canvas.create_line((x+100,y), (x,y+100), fill = couleur,width=5)
def choixcouleur():
    global couleur
    couleur = input("Quelle couleur ?")


btalea = tk.Button(root,text="alea", bg = "green",fg = "blue", 
    padx=20, font=("Times",20), command=ecran_aleatoire)
btcarre = tk.Button(root,text="carre", command=carre)
btcroix = tk.Button(root,text="croix", command=croix)
btcouleur = tk.Button(root,text="choisir une couleur", command=choixcouleur)

btalea.grid(column = 0, row = 1)
btcarre.grid(column = 0, row = 2)
btcroix.grid(column = 0, row = 3)
btcouleur.grid(column = 1, row = 0)
canvas.grid(column = 1, row = 1, rowspan = 3)
root.mainloop()
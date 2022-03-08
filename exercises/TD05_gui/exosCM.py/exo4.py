import tkinter as tk
import math as ma

#milieu du carré
M = 250
x0, y0, x1, y1 = M-25,M-25,M+25,M+25
C = 50


def gestion_clic_i(event):
    global C
    if x0< event.x <x1 and y0< event.y <y1 and C > 20:
        canvas.delete(carré)
        canvas.create_rectangle(x0+5, y0+5, x1-5, y1-5, fill="red")
        C = C-10
        x0, y0, x1, y1 = x0+5, y0+5, x1-5, y1-5
    elif 0<event.x<x0 or x1<event.x<500 and 0<event.y<y0 or y1<event.y<500 and C < 100:
        canvas.coords(carré, x0-5, y0-5, x1+5, y1+5)
        

def suspendu():
    bouton.config(text="Restart")


def aiguillage(condition):
     while condition!=0: ## boucle si condition ne vaut pas 0
          if condition==1: 
                gestion_clic_i() ## excute "mafonction1" si condition =1
          elif condition ==2: 
                suspendu() ## excute "mafonction2" si condition =2
 
 
     time.sleep(1) ## pause d'1 seconde avant de continuer
     aiguillage(condition)    ## la fonction aiguillage s'appelle elle-même




#création des widgets
racine = tk.Tk()
canvas = tk.Canvas(racine, bg = "white", height = 500, width = 500)
bouton = tk.Button(racine, text = "Pause", command=suspendu)

#création carré
carré = canvas.create_rectangle(x0, y0, x1, y1, fill="red")

#liaison des clics
canvas.bind("<Button-1>", gestion_clic_i)


#positionnement des widgets
canvas.grid()
bouton.grid()

#boucle principale
racine.mainloop()
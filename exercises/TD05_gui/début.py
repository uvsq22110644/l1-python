from tkinter import * #* c'est toutes les fonctions dans tkinter

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400 #longueur,largeur

if __name__ == '__main__':
    root = Tk() #création d'une bibliothèque capable de créer des fenêtres (root=fenetre)

    canvas = Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT) #fonction Canvas: on donne des paramètres et donne un objet canva)

    # Début de votre code
    x0 = 100
    x1 = CANVAS_WIDTH - 100
    y = CANVAS_HEIGHT / 2
    canvas.create_line(x0, y, x1, y)  #coordonnées départ et fin
    canvas.create_oval(x0 - 50, y + 50, x0 + 50, y - 50) #définit un carré ou l'ovale(ici cercle) se trouve
    canvas.create_oval(x1 - 50, y + 50, x1 + 50, y - 50)
    canvas.create_oval((x0 + x1) / 2 - 50, y + 50, (x0 + x1) / 2 + 50, y - 50)
    
    # Fin de votre code

    canvas.pack() #fixe les objets graphique, met le canevas dans la fenetre
    root.mainloop() #affiche de la fenetre, il donne les instructions
    #canvas = zone ou on peut placer objets graphiques
     #on associe à un objet des fonctions

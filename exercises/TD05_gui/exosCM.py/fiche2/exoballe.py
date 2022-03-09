#Votre fenêtre graphique doit contenir un canevas de couleur de fond noire et de taille
#600x400 ainsi qu’un bouton avec le texte “Démarrer” placé en dessous du canevas

#import des librairies
import tkinter as tk

#fonctions

#création des widgets
racine=tk.Tk()
canevas=tk.Canvas(racine, bg="black", width=600, height=400)
bouton=tk.Button(racine, text="Démarrer")

#placement des widgets
racine.grid()
canevas.grid()
bouton.grid()

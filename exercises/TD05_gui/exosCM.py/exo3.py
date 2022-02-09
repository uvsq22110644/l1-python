import tkinter as tk
racine = tk.Tk()
canv = tk.Canvas(racine, bg = "black", height = 500, width = 500)
canv.pack()
bt = tk.Button(racine, text = "Redémarrer")
bt.pack()
import tkinter as tk
racine = tk.Tk()
canv = tk.Canvas(racine, bg = "white", height = 600, width = 600)
canv.pack()
bt = tk.Button(racine, text = "Pause")
bt.pack()



racine.mainloop()
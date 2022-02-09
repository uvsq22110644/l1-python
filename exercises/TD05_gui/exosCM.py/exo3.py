import tkinter as tk
racine = tk.Tk()
canv = tk.Canvas(racine, bg = "black", height = 500, width = 500)
canv.pack()
bt = tk.Button(racine, text = "Redémarrer")
bt.pack()

for i in range(1, 3):
    x = 500/3
    canv.create_line(x*i,0,x*i,500,fill="white",)
canv.pack()

racine.mainloop()
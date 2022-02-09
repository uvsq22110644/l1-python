import tkinter as tk
racine = tk.Tk()
canv = tk.Canvas(racine, bg = "white", height = 600, width = 600)
canv.pack()
bt = tk.Button(racine, text = "Pause")
bt.pack()


canv.create_line(200,0,200,600,fill="red",)
canv.create_line(400,0,400,600,fill="blue",)
canv.pack()

racine.mainloop()
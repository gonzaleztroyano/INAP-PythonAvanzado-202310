from tkinter import *
root= Tk()
root.title("Esta es mi primera ventana")
root.columnconfigure(2, weight=1)
root.rowconfigure(0, weight=1)
etiqueta1 = Label(root, text="Primeros pasos con Tkinter").grid(row=0, column= 0, padx=5)
etiqueta2 = Label(root, text=". . . pero esto esta muy vacio, no? ").grid(row=0, column =
1, padx=5)
boton1 = Button(root, text="Aceptar").grid(row=0, column=2, sticky= E+W, padx=5)
root.geometry("800x100")
root.mainloop()
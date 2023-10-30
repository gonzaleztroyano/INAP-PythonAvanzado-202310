from tkinter import *
root = Tk()
root.title("Esta es mi primera ventana")
root.geometry("400x200+500+300")
 # W: ancho de la ventana (en pixeles)
 #H: alto de la ventana (en pixeles)
 #X,Y: valor en el eje X e Y respectivamente en donde si situará nuestra ventana

root.columnconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

etiqueta1 = Label(root, text="Primeros pasos con Tkinter").grid(row=0, column= 0, padx=5, columnspan = 2)

etiqueta2 = Label(root, text=". . . pero esto esta muy vacio, no?").grid(row=1, column= 0, padx=5)

etiqueta3 = Label(root, text="Segundos pasos con Tkinter").grid(row=1, column= 1, padx=5)

boton1 = Button(root, text="Aceptar").grid(row=4, column = 0, sticky= E+W,columnspan = 2, pady=10, padx = 10)


root.geometry("400x100")  # Cambiar el tamaño


root.mainloop()

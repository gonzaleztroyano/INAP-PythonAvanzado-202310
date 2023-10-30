from tkinter import *
import tkinter.messagebox


class PrimerGUI:
    def __init__(self, master):
        self.master = master
        master.title("GUI con botones de radio")
        self.idanimal = IntVar()

        self.etiqueta1 = Label(master, text="¿Cuál es su animal doméstico preferido?").grid(row=0, columnspan=4, pady=15, padx=17)
        self.botonperro = Radiobutton(master, text="Perro", value=1, variable=self.idanimal).grid(row=1, column=0,padx=15)
        self.botongato = Radiobutton(master, text="Gato", value=2, variable=self.idanimal).grid(row=1, column=1,padx=15)
        self.botonpeces = Radiobutton(master, text="Peces", value=3, variable=self.idanimal).grid(row=1, column=2,padx=15)
        self.botonotros = Radiobutton(master, text="Otros", value=4, variable=self.idanimal).grid(row=1, column=3,padx=15)


        self.idcolor = IntVar()
        self.etiquetacolor = Label(master, text="¿Qué color?").grid(row=3, columnspan=4, pady=15, padx=17)
        self.botonRojo = Radiobutton(master, text="Rojo", value=1, variable=self.idcolor, bg="red").grid(row=4,column=0, padx=15)
        self.botonAzul = Radiobutton(master, text="Azul", value=2, variable=self.idcolor, bg="blue").grid(row=4,column=1, padx=15)
        self.botonAmarillo = Radiobutton(master, text="Amarillo", value=3, variable=self.idcolor, bg="yellow").grid(row=4,column=2, padx=15)
        self.botonNegro = Radiobutton(master, text="Negro", value=1, variable=self.idcolor, bg="black", fg="white").grid(row=4,column=3, padx=15)


        self.boton = Button(master, text="Sus gustos son...", command=self.imprimir).grid(row=5, columnspan=4, pady=10)


    def imprimir(self):
        animal = ["Perro", "Gato", "Peces", "Otros"]
        color = ["Rojo", "Azul", "Amarillo", "Negro"]
        print('Su animal preferido es: ', animal[self.idanimal.get()-1], "de color", color[self.idcolor.get()-1])
        tkinter.messagebox.showinfo("Resultados", "Su animal preferido es:  " +animal[self.idanimal.get()-1] + " de color " + color[self.idcolor.get()-1])



root = Tk()
root.geometry("400x200")
gui = PrimerGUI(root)
root.mainloop()
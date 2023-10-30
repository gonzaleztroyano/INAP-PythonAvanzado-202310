from tkinter import *


class PrimerGUI:

    def minimizar(self):
            self.master.iconify()

    def imprimir(self):
            print("Esta usted en el curso Python")

    def __init__(self, master):
        self.master = master
        master.title("Un GUI muy simple")
        self.label = Label(master, text="Este es mi primer GUI con botones").grid(row = 0, column = 0, padx=5)
        self.boton1 = Button(master, text="Minimizar", command=self.minimizar).grid(row=0, column=1, padx=5)
        self.boton2 = Button(master, text=" Salir ",bg="blue", fg="red", command=self.master.destroy).grid(row = 0, column=2, padx=5)
        self.boton3 = Button(master, text="¿Dónde estoy?", bg="yellow", command=self.imprimir).grid(row=1)



root = Tk()
root.geometry("400x100")
gui = PrimerGUI(root)
root.mainloop()
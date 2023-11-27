from tkinter import *
import tkinter.messagebox


class gui_caluladora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora sencilla, e inútil")

        self.num1 = IntVar()
        self.label_num1 = Label(master, text="Introduzca el primer número: ").grid(row=0, column=0, padx=15, pady=10)
        self.entry_num1 = Entry(master, textvariable=self.num1).grid(row=0, column=1, pady=10)

        self.num2 = IntVar()
        self.label_num2 = Label(master, text="Introduzca el segundo número: ").grid(row=1, column=0, padx=15)
        self.entry_num2 = Entry(master, textvariable=self.num2).grid(row=1, column=1)

        self.label_select_opt = Label(master, text="Seleccione una operación: ").grid(row=3, column=0, columnspan=2, pady=20)

        self.operation = IntVar()
        self.boton_suma  = Radiobutton(master, text="Suma (+)", value=0, variable=self.operation).grid(row=4, column=0)
        self.boton_resta = Radiobutton(master, text="Resta (-)", value=1, variable=self.operation).grid(row=4, column=1)
        self.boton_multi = Radiobutton(master, text="Multiplicar (*)", value=2, variable=self.operation).grid(row=5, column=0)
        self.boton_divid = Radiobutton(master, text="Dividir (/)", value=3, variable=self.operation).grid(row=5, column=1)

        self.button = Button(master, text="Ejecutar cálculos mágicos...", command=self.calcular).grid(row=6, column=0, columnspan=2, pady=20, padx=10)

    def calcular(self):
        selected_op = self.operation.get()
        operando1 = int(self.num1.get())
        operando2 = int(self.num2.get())
        if selected_op == 0:
            print("sumando", operando1, operando2)
            resul = operando1 + operando2
            string_resul = "Resultado de sumar " + str(operando1) + " + " + str(operando2) + ":  " + str(resul)
            print(string_resul)
            tkinter.messagebox.showinfo("Resultado de la operación", string_resul)
        elif selected_op == 1:
            print("restando")
            resul = operando1 - operando2
            string_resul = "Resultado de restar " + str(operando1) + " - " + str(operando2) + ":  " + str(resul)
            print(string_resul)
            tkinter.messagebox.showinfo("Resultado de la operación", string_resul)
        elif selected_op == 2:
            print("multiplicando")
            resul = operando1 * operando2
            string_resul = "Resultado de sumar " + str(operando1) + " * " + str(operando2) + ":  " + str(resul)
            print(string_resul)
            tkinter.messagebox.showinfo("Resultado de la operación", string_resul)
        elif selected_op == 3:
            print("dividiendo")
            resul = operando1 / operando2
            string_resul = "Resultado de sumar " + str(operando1) + " / " + str(operando2) + ":  " + str(resul)
            print(string_resul)
            tkinter.messagebox.showinfo("Resultado de la operación", string_resul)




root = Tk()
root.geometry("400x250")
gui = gui_caluladora(root)
root.mainloop()
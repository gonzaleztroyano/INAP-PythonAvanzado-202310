from tkinter import *
import tkinter.messagebox

class gui_encuesta:
    def __init__(self, master):
        self.master = master
        master.title("Encuesta de satisfacción del curso Python")

        self.valora_contenido = IntVar()
        self.label_valora_contenido = Label(master, text="¿Está satisfecho con el contenido del curso Python?:").grid(row=0, column=0, columnspan=4, pady=5, padx=15)
        self.valora_contenido_1 =Radiobutton(master, text="1", value=1, variable=self.valora_contenido).grid(row=1, column=0, pady=2, padx=2)
        self.valora_contenido_2 =Radiobutton(master, text="2", value=2, variable=self.valora_contenido).grid(row=1, column=1, pady=2, padx=2)
        self.valora_contenido_3 =Radiobutton(master, text="3", value=3, variable=self.valora_contenido).grid(row=1, column=2, pady=2, padx=2)
        self.valora_contenido_4 =Radiobutton(master, text="4", value=4, variable=self.valora_contenido).grid(row=1, column=3, pady=2, padx=2)
        self.valora_contenido_5 =Radiobutton(master, text="5", value=5, variable=self.valora_contenido).grid(row=1, column=4, pady=2, padx=2)

        self.valora_recomienda = IntVar()
        self.label_valora_recomienda = Label(master, text="¿Recomendaría el curso a otros compañeros?:").grid(row=2, column=0, columnspan=4, pady=5, padx=15)
        self.valora_recomienda_1 =Radiobutton(master, text="1", value=1, variable=self.valora_recomienda).grid(row=3, column=0, pady=2, padx=2)
        self.valora_recomienda_2 =Radiobutton(master, text="2", value=2, variable=self.valora_recomienda).grid(row=3, column=1, pady=2, padx=2)
        self.valora_recomienda_3 =Radiobutton(master, text="3", value=3, variable=self.valora_recomienda).grid(row=3, column=2, pady=2, padx=2)
        self.valora_recomienda_4 =Radiobutton(master, text="4", value=4, variable=self.valora_recomienda).grid(row=3, column=3, pady=2, padx=2)
        self.valora_recomienda_5 =Radiobutton(master, text="5", value=5, variable=self.valora_recomienda).grid(row=3, column=4, pady=2, padx=2)

        self.valora_adecuado = IntVar()
        self.label_valora_adecuado = Label(master, text="¿Le ha parecido adecuado el material y contenido del curso?:").grid(row=4, column=0, columnspan=4, pady=5, padx=15)
        self.valora_adecuado_1 =Radiobutton(master, text="1", value=1, variable=self.valora_adecuado).grid(row=5, column=0, pady=2, padx=2)
        self.valora_adecuado_2 =Radiobutton(master, text="2", value=2, variable=self.valora_adecuado).grid(row=5, column=1, pady=2, padx=2)
        self.valora_adecuado_3 =Radiobutton(master, text="3", value=3, variable=self.valora_adecuado).grid(row=5, column=2, pady=2, padx=2)
        self.valora_adecuado_4 =Radiobutton(master, text="4", value=4, variable=self.valora_adecuado).grid(row=5, column=3, pady=2, padx=2)
        self.valora_adecuado_5 =Radiobutton(master, text="5", value=5, variable=self.valora_adecuado).grid(row=5, column=4, pady=2, padx=2)

        self.label_observaciones = Label(master, text="Observaciones sobre el material, aula, profesores...").grid(row=6, column=0, columnspan=4, pady=5, padx=15)

        self.input_text_observaciones = Text(master, height=7, width=45)
        self.input_text_observaciones.grid(row=7, column=0, columnspan=5, pady=5, padx=10) # Separar en 2!

        self.label_datos = Label(master, text="Introduzca, si lo desea, sus datos personales").grid(row=8, column=0, columnspan=4, pady=10, padx=15)

        self.nombre = StringVar()
        self.label_nombre = Label(master, text="Nombre").grid(row=9, column=0, columnspan=2, padx=5, pady=5)
        self.input_nombre = Entry(master, textvariable=self.nombre).grid(row=9, column=1, columnspan=3)

        self.apellidos = StringVar()
        self.label_apellidos = Label(master, text="Apellidos").grid(row=10, column=0, columnspan=2, padx=5, pady=5)
        self.input_apellidos = Entry(master, textvariable=self.apellidos).grid(row=10, column=1, columnspan=3, padx=5, pady=5)

        self.subdireccion = StringVar()
        self.label_subdireccion = Label(master, text="Subdirección").grid(row=11, column=0, columnspan=2, padx=5, pady=5)
        self.input_subdireccion = Entry(master, textvariable=self.subdireccion).grid(row=11, column=1, columnspan=3, padx=5, pady=5)

        self.button_enviar_comentarios = Button(master, text="Enviar comentarios", command=self.enviar).grid(row=12, column=0, columnspan=5, pady=20, padx=10)

    def enviar(self):
        valora_contenido = int(self.valora_contenido.get())
        valora_recomienda = int(self.valora_recomienda.get())
        valora_adecuado = int(self.valora_adecuado.get())
        media_valoraciones = (valora_contenido + valora_recomienda + valora_adecuado) / 3

        observaciones = self.input_text_observaciones.get("1.0", "end-1c")
        nombre = self.nombre.get()
        apellidos = self.apellidos.get()
        subdireccion = self.subdireccion.get()

        print(media_valoraciones, observaciones, nombre, apellidos, subdireccion)

        tkinter.messagebox.showinfo("Gracias por su tiempo", "Gracias por su asistencia, " + nombre + " " + apellidos +
                                    "\n\nSu valoración media del curso es de " + str(media_valoraciones) +
                                    "\n\nObservaciones: " + observaciones)


root = Tk()
root.geometry("410x550")
gui = gui_encuesta(root)
root.mainloop()
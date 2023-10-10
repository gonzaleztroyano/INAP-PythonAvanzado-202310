import math


class Circulo(object):

    def __init__(self, r):
        self.r = float(r)
        print("Círculo de radio", str(r), "creado.")

    def area(self, formato="float"):
        area = math.pi * math.pow(self.r, 2)
        if formato == "float":
            return area
        elif formato == "string":
            return "El área del círculo es {}".format(area)
        else:
            raise Exception("Error en el cálculo del área")

    def perimetro(self, formato="float"):
        perim = 2 * math.pi * self.r
        if formato == "float":
            return perim
        elif formato == "string":
            return "El perímetro del círculo es {}".format(perim)
        else:
            raise Exception("Error en el cálculo del perímetro")

from Triangulo import Triangulo


class Terreno(object):
    def __init__(self, triangulos=None):
        if triangulos is None:
            triangulos = []
        self.triangulos = []
        for triangulo in triangulos:
            print("L10")
            if isinstance(triangulo, Triangulo):
                self.triangulos.append(triangulo)
            else:
                raise Exception("Los objetos introducidos deben ser Triángulos")

    def __str__(self):
        string = "Terreno:\n \t"
        i=0
        for triangulo in self.triangulos:
            string += "Triángulo " + str(i) +" --> " + str(triangulo) + "\n\t"
            i+=1
        return string[:-2]

    def area(self):
        area = 0.0
        for triangulo in self.triangulos:
            area += triangulo.area()
        return area

    def add_triangulo(self, triangulo):
        if isinstance(triangulo, Triangulo):
            self.triangulos.append(triangulo)
        else:
            raise Exception("El objeto introducido no es un triángulo")

    def add_triangulo_x_medidas(self, l1=0.0, l2=0.0, ang=0.0):
        triangulo = Triangulo(l1=l1, l2=l2, ang=ang)
        self.triangulos.append(triangulo)
import math


class Triangulo(object):
    def __init__(self, l1=0.0, l2=0.0, ang=0.0):
        self.l1 = l1
        self.l2 = l2
        self.ang = ang
        self.l3 = self.__tercerlado()

    def __str__(self):
        return "Lado 1: {}, Lado 2: {}, Ángulo interior: {}".format(self.l1, self.l2, self.ang)

    def perimetro(self):
        """Retorna el perímetro del triángulo, sumando sus lados"""
        return self.l1 + self.l2 + self.l3

    def __semiperimetro(self):
        return float(self.perimetro()/2)

    def __tercerlado(self):
        return math.sqrt(math.pow(self.l1, 2) + math.pow(self.l2, 2) - 2 * self.l1 * self.l2 * math.cos(math.radians(self.ang)))

    def area(self):
        """Cálculo del área del triángulo usando la fórmula de Herón, al saber la longitud de todos sus lados
        https://es.wikipedia.org/wiki/F%C3%B3rmula_de_Her%C3%B3n"""
        s = self.__semiperimetro()
        return math.sqrt(s * (s - self.l1) * (s - self.l2) * (s - self.l3))

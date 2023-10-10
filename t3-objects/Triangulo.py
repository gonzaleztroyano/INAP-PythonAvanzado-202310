class Triangulo(object):
    """Representa un triángulo, indicando 3 objetos punto"""

    def __init__(self, punto1, punto2, punto3):
        self.punto1 = punto1
        self.punto2 = punto2
        self.punto3 = punto3

    def perimetro(self):
        """Devuelve el perímetro del triángulo"""
        lado_a = self.punto1.distancia(self.punto2)
        lado_b = self.punto1.distancia(self.punto3)
        lado_c = self.punto2.distancia(self.punto3)

        perimetro = lado_a + lado_b + lado_c
        print(f"El perímetro ajustado por la función interna: {self.__perimetro_ajustado()}")
        return perimetro

    def __perimetro_ajustado(self):
        """Esta función, al tener dos guiones bajos delante, es una función que solo
        puede ser llamada desde el objeto"""
        """Devuelve el perímetro del triángulo"""
        lado_a = self.punto1.distancia(self.punto2)
        lado_b = self.punto1.distancia(self.punto3)
        lado_c = self.punto2.distancia(self.punto3)

        perimetro = lado_a + lado_b + lado_c
        return int(perimetro)

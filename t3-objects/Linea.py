from Punto import Punto


class Linea(object):
    """Representa una lista de puntos que forman una lista"""

    def __init__(self, puntos=None):
        if puntos is None:
            puntos = []
        self.puntos = []  # Creamos lista para almacenar los puntos
        for punto in puntos:
            # Comprobar si es tipo punto
            if isinstance(punto, Punto):
                self.puntos.append(punto)
            else:
                raise Exception('Los elementos de una línea deben ser puntos')

    def __str__(self):
        stri = ""
        for punto in self.puntos:
            stri += "[" + str(punto.x) + ", " + str(punto.y) + "], "
        return stri[:-2]

    def add(self, punto):
        if isinstance(punto, Punto):
            self.puntos.append(punto)
        else:
            raise Exception('El elemento pasado no es un punto')

    def add_by_pos(self, x=0, y=0, pos=-1):
        if pos == -1:
            pos = len(self.puntos)
        punto = Punto(x, y)
        self.puntos.insert(pos, punto)

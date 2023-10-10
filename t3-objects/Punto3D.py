from Punto import Punto


class Punto3D(Punto):
    """Representa un punto con sus coordenadas cartesianas y una cota"""
    def __init__(self, x, y, z):
        Punto.__init__(self, x, y)
        self.z = float(z)

    def __str__(self):
        return "{}, z = {}".format(Punto.__str__, self.z)
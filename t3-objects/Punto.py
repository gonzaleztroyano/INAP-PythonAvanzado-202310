class Punto(object):
    """Representa un punto sobre un plano con sus coordenadas cartesianas"""

    def __init__(self, x=0, y=0):
        """Constructor del punto. Si la coordenada no se indica, se usa 0 como valor de fallback"""
        self.x = float(x)
        self.y = float(y)

    def __str__(self):
        return "x = {}, y = {}".format(self.x, self.y)

    def __add__(self, other):
        return Punto(self.x + other.x, self.y + other.y)

    def detalle(self, formato="dict"):
        """Devuelve los datos. Si no se indica valor, devuelve un diccionario.
        Se puede indicar 'string' para devolver en formato human-friendly"""
        if formato == "dict":
            return {"x": self.x, "y": self.y}
        if formato == "string":
            print(f"El punto se encuentra en las posiciones x={self.x} e y={self.y}")
            return "El punto se encuentra en las posiciones x=" + str(self.x) + " e y=" + str(self.y)

    def distancia(self, otro_punto):
        dx = self.x - otro_punto.x
        dy = self.y - otro_punto.y
        dist = (dx**2 + dy**2)**0.5
        return dist

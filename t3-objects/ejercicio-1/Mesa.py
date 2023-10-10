class Mesa(object):
    def __init__(self, h=0.0, a=0.0, lg=0.0, n=0.0, c=""):
        self.h = float(h)
        self.a = float(a)
        self.lg = float(lg)
        self.n = float(n)
        self.c = str(c)

    def area(self):
        """Calcula el área de la mesa, multiplicando ancho (a) por largo (lg)"""
        return self.a * self.lg

    def apta_trabajo(self):
        print(self.h)
        if self.h > 0.70:
            return True
        else:
            return False

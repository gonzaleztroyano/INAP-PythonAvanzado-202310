from Triangulo import Triangulo
from Punto import Punto
from Linea import Linea

# help(Punto)

punto1 = Punto(x=5)
punto2 = Punto(7, 10)
punto3 = Punto(3, 5)

# omitido
dict_punt = punto1.detalle()
print(dict_punt)
punto1.detalle(formato="string")

distancia = punto1.distancia(punto2)
print(f"El punto 1 se encuentra a una distancia de {distancia} del punto2.")
print(f"El punto2 se encuentra a una distancia de {punto2.distancia(punto3)} del punto 3.")
print(f"El punto1 se encuentra a una distancia de {punto1.distancia(punto3)} del punto 3.")

triangulo = Triangulo(punto1, punto2, punto3)

print(f"El triángulo tiene un perímetro de {triangulo.perimetro()}")

lin = Linea([punto1, punto3, punto2])
print(lin)

punto4 = Punto(8, 12)
lin.add(punto4)
print(lin)

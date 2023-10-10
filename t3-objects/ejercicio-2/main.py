from Triangulo import Triangulo
from Terreno import Terreno

triangulo1 = Triangulo(12, 12, 100.0)
print(triangulo1)
print(triangulo1.area())
print(triangulo1.perimetro())
print(triangulo1.l3)

triangulo2 = Triangulo(15, 21, 91.0)
triangulo3 = Triangulo(91, 65, 15.0)

terreno = Terreno(triangulos=[triangulo1, triangulo2, triangulo3])
print(terreno)

print(terreno.area())

triangulo4 = Triangulo(20, 21, 91.0)
terreno.add_triangulo(triangulo4)

print(terreno.area())

terreno.add_triangulo_x_medidas(20, 21, 91.0)
print(terreno.area())

from Circulo import Circulo

circulo = Circulo(float(input("Introduce el radio de la circunferencia: ")))

print(circulo.area())
print(circulo.perimetro())


print(circulo.area(formato="string"))
print(circulo.perimetro(formato="string"))
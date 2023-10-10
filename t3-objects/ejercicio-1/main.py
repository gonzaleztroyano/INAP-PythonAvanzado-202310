from Mesa import Mesa

h = input("Introduce el alto de la mesa (en metros): ")
a = input("Introduce el ancho de la mesa (en metros): ")
lg = input("Introduce el largo de la mesa (en metros): ")
n = input("Introduce el número de patas de la mesa: ")
c = input("Introduce el color de la mesa: ")

mesa = Mesa(h=h, a=a, lg=lg, n=n, c=c)

if mesa.apta_trabajo():
    print(f"La mesa es apta para el trabajo y tiene una superficie de {mesa.area()} metros cuadrados.")
else:
    print("La mesa no es apta para el trabajo")
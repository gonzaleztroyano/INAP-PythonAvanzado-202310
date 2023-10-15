import matplotlib.pyplot as plt
import matplotlib.image as img
lista_x = []
lista_y = []
radio = 1
radios = []
rojo_verde_azul = [(1, 0, 0), (0, 1, 0), (0, 0, 1)] # Colores R, G y B
colores = []
for i in range(3):
    color = rojo_verde_azul[i]
    for j in range(5):
        lista_x.append(i)
        lista_y.append(j)
        radios.append(radio)
        colores.append(color)
        radio *= 2
plt.scatter(lista_x, lista_y, s=radios, c=colores)
plt.show()
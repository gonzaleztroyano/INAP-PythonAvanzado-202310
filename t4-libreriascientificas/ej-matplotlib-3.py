import matplotlib.pyplot as plt
import numpy as np
import math
num_puntos = 100
x_min = -math.pi
x_max = math.pi
eje_x = np.linspace(x_min, x_max, 100)
lista_y = [0]*num_puntos
for i in range(num_puntos):
    lista_y[i] = math.cos(eje_x[i])
lista_y_2 = [0]*num_puntos
for i in range(num_puntos):
    lista_y_2[i] = math.sin(eje_x[i])

plt.plot(eje_x, lista_y, label="Funcion coseno")
plt.plot(eje_x, lista_y_2, label= 'Funcion seno')
plt.legend(loc="upper left")
plt.show()
import matplotlib.pyplot as plt
import numpy as np

# Crear una matriz de ejemplo
matriz = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 20]])

# Mostrar la matriz como una imagen
plt.imshow(matriz, cmap='viridis')  # cmap es el mapa de colores utilizado
plt.colorbar()  # Añadir una barra de color para referencia
plt.title('Visualización de una Matriz')
plt.show()

import numpy as np

# Array de una dimensión
a1 = np.array([7, 1, 12])
print(a1, "\n")

# Array de dos dimensiones
a2 = np.array([[10, 20, 30], [90, 80, 70]])
print(a2, "\n")

# Array de tres dimensiones
a3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a3, "\n")

# Array vacío
empty_array = np.empty((3, 5))
print(empty_array, "\n")

# Arrays con ceros y unos
array0 = np.zeros((2, 7))
print(array0, "\n")
array1 = np.ones((2, 7))
print(array1, "\n")

# Arrays con valor n
array_tres = np.full((3, 5), 3)
print(array_tres, "\n")

# Arrays aleatorios
array_random = np.random.random((3, 4))
print(array_random, "\n")
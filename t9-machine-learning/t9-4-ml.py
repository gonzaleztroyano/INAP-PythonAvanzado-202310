import os
import skimage.data as imd
import imageio.v2 as imageio
import numpy as np

def carga_imagenes(carpeta):
    directorios = []
    for d in os.listdir(carpeta):
        if os.path.isdir(os.path.join(carpeta, d)):
            directorios.append(d)

    etiquetas = []
    imagenes = []

    for d in directorios:
        ruta_dir = os.path.join(carpeta, d)
        archivos = [os.path.join(ruta_dir, f) for f in os.listdir(ruta_dir) if f.endswith('.ppm')]

        for f in archivos:
            imagenes.append(imageio.imread(f))
            etiquetas.append(f)

    return imagenes, etiquetas

datos = r'C:\Users\pablo\PycharmProjects\test01\t9-machine-learning\belgian'

datos_train = os.path.join(datos, 'Training')
datos_test = os.path.join(datos, 'test')

imagenes_train, etiquetas_train = carga_imagenes(datos_train)
imagenes_test, etiquetas_test = carga_imagenes(datos_test)

print(f"Imágenes para entrenamiento: {len(imagenes_train)}")
print(f"Imágenes para test: {len(imagenes_test)}")

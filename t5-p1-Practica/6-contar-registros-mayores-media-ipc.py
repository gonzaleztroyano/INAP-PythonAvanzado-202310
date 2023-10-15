# 3.4.	Obtener el promedio de los valores de la variación anual del IPC en los últimos 20 años,
# mostrando los resultados con un único decimal. (usar la librería numpy
from pymongo import MongoClient
import numpy

client = MongoClient('mongodb://localhost:55017/')

db = client.ipc_database
ipc_data_2023 = db.ipc_data_2023

valores = []

for document in ipc_data_2023.find():
    valores.append(document["Valor"])

array = numpy.array(valores)
media = numpy.mean(array)

cuenta = 0
for valor in valores:
    if valor > media:
        cuenta += 1

print(f"La media de los valores del IPC es: {round(media, 1)}\n"
      f"Se han encontrado {cuenta} valores superiores a la media.")

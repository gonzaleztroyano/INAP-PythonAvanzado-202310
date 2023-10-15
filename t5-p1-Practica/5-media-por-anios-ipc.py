# 3.4.	Obtener el promedio de los valores de la variación anual del IPC en los últimos 20 años,
# mostrando los resultados con un único decimal. (usar la librería numpy
from pymongo import MongoClient
import numpy
import matplotlib.pyplot as plt

client = MongoClient('mongodb://localhost:55017/')

db = client.ipc_database
ipc_data_2023 = db.ipc_data_2023

valores = numpy.zeros((22, 12))
n_anno = -1

for i in range(2002, 2024, 1):
    #print(f"Seeing año {i}")
    n_mes = 0
    n_anno += 1
    for document in ipc_data_2023.find({"Anyo": i}):
        #print(document)
        valores[n_anno][n_mes] = document["Valor"]
        n_mes += 1
        # print(valores)

print("Se ha generado la siguiente matriz: ", valores, "", "", sep="\n")

anno_c2 = 0
valores_para_grafico = []
for i in range(2023, 2001, -1):
    valor_actual = round(numpy.average(valores[anno_c2]),2)
    valores_para_grafico.append(valor_actual)
    print(f"El valor medio para el año {i} fue de: {valor_actual}")
    anno_c2 += 1
# array = numpy.array(valores)
# media = numpy.mean(array)
plt.plot(range(2002, 2024, 1), valores_para_grafico, "-.", label="Media del IPC anual")
plt.legend(loc="upper left")
plt.text(2022,8.40,'El valor de IPC más alto se dio en el año 2022    ', horizontalalignment='right')

for year, average in zip(range(2002, 2024, 1), valores_para_grafico):
    plt.text(year, average, str(average), ha='center', va='bottom')

plt.show()

#print(f"La media de los valores del IPC es: {round(media, 1)}")

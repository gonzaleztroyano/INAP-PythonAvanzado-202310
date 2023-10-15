# 3.2.	Obtener el máximo valor de la variación anual del IPC en los últimos 20 años e indicar el año y el mes en
# que se produjo, mostrando los resultados con un único decimal.
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:55017/')

db = client.ipc_database
ipc_data_2023 = db.ipc_data_2023


max_document = ipc_data_2023.find_one(sort=[("Valor", -1)])
print(f"El año y mes en el que más variación anual del IPC hubo fue el "
      f"{str(max_document["T3_Periodo"])[1:]}/{max_document["Anyo"]}\n"
      f"Con un valor de: {max_document["Valor"]}")

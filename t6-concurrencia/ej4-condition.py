import threading
import time


def consumidor(condicion):
    print('Comienza el hilo de consumidor')
    with condicion:
        condicion.wait()
        print(f'Consumidor ha terminado. {condicion}')


def productor(condicion):
    print('Comienza el hilo productor')
    with condicion:
        print('Recurso disponible')
        print('Notificando a los consumidores')
        time.sleep(2)
        condicion.notify(cons1)


condicion = threading.Condition()

cons1 = threading.Thread(target=consumidor, args=(condicion, ))
cons2 = threading.Thread(target=consumidor, args=(condicion, ))
prod = threading.Thread(target=productor, args=(condicion, ))

cons1.start()
cons2.start()
time.sleep(4)
prod.start()

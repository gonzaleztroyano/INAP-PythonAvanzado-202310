import threading
import time
import queue
import random


q = queue.Queue(10)


def productor():
    while True:
        if not q.full():
            item = random.randint(1, 10)
            q.put(item)
            print(f'Productor añade {item}. {q.qsize()} elementos en queue')
            time.sleep(random.random())
        else:
            print('Cola llena')


def consumidor():
    while True:
        if not q.empty():
            item = q.get()
            print(f'Consumidor toma {item}. {q.qsize()} elementos en queue')
            time.sleep(random.random())
        else:
            print('Cola vacía')


p = threading.Thread(target=productor)
c = threading.Thread(target=consumidor)

p.start()
time.sleep(2)
c.start()
time.sleep(2)

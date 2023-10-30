import time
from multiprocessing import Pool


def if_prime(x):
    if x <= 1:
        return 0
    elif x <= 3:
        return x
    elif x % 2 == 0 or x % 3 == 0:
        return 0
    i = 5
    while i**2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return 0
        i += 6
    return x


if __name__ == '__main__':
    start_time = time.time()

    with Pool(2) as p:
        answer = sum(p.map(if_prime, list(range(10000000))))
    duration = time.time() - start_time
    print(f"2 Cores - Ejecutado en {duration} segundos. La suma es {answer}")
    start_time = time.time()

    with Pool(4) as p:
        answer = sum(p.map(if_prime, list(range(10000000))))
    duration = time.time() - start_time
    print(f"4 Cores - Ejecutado en {duration} segundos. La suma es {answer}")
    start_time = time.time()

    with Pool(6) as p:
        answer = sum(p.map(if_prime, list(range(10000000))))
    duration = time.time() - start_time
    print(f"6 Cores - Ejecutado en {duration} segundos. La suma es {answer}")
    start_time = time.time()

    with Pool(8) as p:
        answer = sum(p.map(if_prime, list(range(10000000))))
    duration = time.time() - start_time
    print(f"8 Cores - Ejecutado en {duration} segundos. La suma es {answer}")


# 2 Cores - Ejecutado en 34.554633378982544 segundos. La suma es 3203324994356
# 4 Cores - Ejecutado en 19.712085247039795 segundos. La suma es 3203324994356
# 6 Cores - Ejecutado en 17.03456211090088 segundos. La suma es 3203324994356
# 8 Cores - Ejecutado en 15.5157470703125 segundos. La suma es 3203324994356

# Leer una matriz 4x4 entera y calcular el promedio de los números
# mayores de cada fila.

import random


def fila_mayor(x):
    plus = 0
    for g in range(4):
        for h in range(4):
            if x[g][h] > plus:
                plus = x[g][h]
    return plus


def promedio_numeros(c):
    prom = 0
    for g in range(4):
        prom = (fila_mayor(c) + prom)
    prom = int(prom / 4)
    return prom


if __name__ == "__main__":
    fila = []
    mat = []
    for x in range(4):
        fila = []
        for j in range(4):
            fila.append(random.randint(0, 50))
        mat.append(fila)
    print(promedio_numeros(mat))

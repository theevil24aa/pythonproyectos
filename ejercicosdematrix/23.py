# Leer una matriz 4x3 entera, calcular la suma de los elementos de cada
# fila y determinar cuál es la fila que tiene la mayor suma.
import random


def sumar(num1):
    suma = []
    for j in range(4):
        aux = 0
        for g in range(3):
            aux += num1[j][g]
        suma.append(aux)
    return suma


def numro_mayor(x):
    plus = 0
    for g in range(4):
        if x[g] > plus:
            plus = x[g]
    return plus


if __name__ == "__main__":
    fila = []
    mat = []

    for x in range(4):
        fila = []
        for k in range(3):
            fila.append(random.randint(0, 300))
        mat.append(fila)
    print(sumar(mat))
    print(numro_mayor(sumar(mat)))

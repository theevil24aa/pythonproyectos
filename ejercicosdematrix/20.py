# Leer una matriz 4x4 entera y determinar en qué fila y en qué columna se
# encuentra el número mayor.
import random


def may(num):
    maxy = 0
    for j in range(4):
        for x in range(4):
            if maxy < num[j][x]:
                maxy = num[j][x]
    return maxy


if __name__ == "__main__":
    mat = []
    fila = []
    for j in range(4):
        fila = []
        for x in range(4):
            fila.append(random.randint(0, 300))
        mat.append(fila)

    print("el numero mayor es ", may(mat))
    # print(mat)

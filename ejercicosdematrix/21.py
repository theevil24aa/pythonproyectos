# Leer una matriz 4x4 entera y determinar cuántas veces se repita en ella
# el número mayor.
import random


def may(num):
    maxy = 0
    cont = 0
    for j in range(4):
        for x in range(4):
            if maxy < num[j][x]:
                maxy = num[j][x]
                if maxy == num[j][x]:
                    cont += 1
    return maxy, cont


if __name__ == "__main__":
    fila = []
    mat = []
    for x in range(4):
        fila = []
        for j in range(4):
            fila.append(random.randint(0, 300))
        mat.append(fila)
print("el numero mayor y se repite ", may(mat))

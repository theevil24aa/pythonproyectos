# Leer dos matrices 4x5 enteras y determinar si el número mayor
# almacenado en la primera está en la segunda.
import random


def may(num):
    maxy = 0
    for j in range(4):
        for x in range(5):
            if maxy < num[j][x]:
                maxy = num[j][x]
    return maxy


if __name__ == "__main__":
    fila1 = []
    mat1 = []
    for x in range(4):
        fila1 = []
        for j in range(5):
            fila1.append(random.randint(0, 300))
        mat1.append(fila1)

    fila = []
    mat = []
    for x in range(4):
        fila = []
        for j in range(5):
            fila.append(random.randint(0, 300))
        mat.append(fila)

    for h in range(4):
        for f in range(5):
            num = may(mat1)
            if num == mat[h][f]:
                print("!bingo¡")

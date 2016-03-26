# Leer dos matrices 4x5 enteras y determinar cuántos datos tienen en común.
import random


def datos_en_comun(x, y):
    cont = 0
    for jk in range(4):
        for kk in range(5):
            for gg in range(4):
                for ii in range(5):
                    if x[gg][ii] == y[jk][kk]:
                        cont += 1
    return cont


if __name__ == "__main__":

    fila = []
    mat = []
    for x in range(4):
        fila = []
        for j in range(5):
            fila.append(random.randint(0, 500))
        mat.append(fila)

    fila1 = []
    mat1 = []
    for x in range(4):
        fila1 = []
        for j in range(5):
            fila1.append(random.randint(0, 500))
        mat1.append(fila)

    print(datos_en_comun(mat, mat1))
    print(mat)
    print(mat1)

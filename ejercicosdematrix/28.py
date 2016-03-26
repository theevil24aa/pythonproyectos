#Leer dos matrices 4x5 enteras y determinar si el número mayor de una
#de las matrices es igual al número mayor de la otra matriz.
import random


def mayor(num1, num2):
    may = 0
    may2 = 0
    for j in range(4):
        for u in range(5):
            if may < num1[j][u]:
                may = num1[j][u]
            if may2 < num2[j][u]:
                may2 = num2[j][u]
    if may == may2:
        return True
    else:
        return False


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
    print(mayor(mat, mat1))


# Leer una matriz 4x6 entera y determinar si alguno de sus números está
# repetido al menos 3 veces.
import random


def numero_repetido(num1):
    count = 0
    for j in range(4):
        for k in range(6):
            for f in range(4):
                for o in range(6):
                    repetido = num1[j][k]
                    if repetido == num1[f][o]:
                        count += 1
                        if 3 < count > 6:
                            return num1[f][o], count


if __name__ == "__main__":
    fila=[]
    mat=[]
    for x in range(4):
        fila=[]
        for k in range(6):
            fila.append(random.randint(0,300))
        mat.append(fila)
    print(numero_repetido(mat))

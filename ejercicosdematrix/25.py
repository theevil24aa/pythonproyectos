# Leer dos matrices 4x5 entera y determinar si sus contenidos son
# exactamente iguales.
import random

verda = 0
if __name__ == "__main__":
    while (verda == 0):
        # la primera matris generada aleatoriamente
        fila = []
        mat = []
        for i in range(4):
            fila = []
            for x in range(5):
                fila.append(random.randint(0, 50))
            mat.append(fila)
        # la segunda matris generada aleatoriamente
        fila1 = []
        mat1 = []
        for i in range(4):
            fila1 = []
            for x in range(5):
                fila1.append(random.randint(0, 50))
            mat1.append(fila1)
        if mat == mat1:
            print(mat)
            print(mat1)
            print("!igualesss¡")
            verda = 1
        else:
            print(mat)
            print(mat1)

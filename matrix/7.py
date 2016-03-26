print(" Leer una matriz 4x4 entera y determinar en qué posiciones están los enteros terminados en 0.")
mat = []
fila = []
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)

for i in range(4):
    for j in range(4):
        if (mat[i][j] % 10) == 0:
            print("el numero %d que esta en la columna %d y en la fila %d termina en 0" % (mat[i][j], i, j))

print(" Leer una matriz 5x3 entera y determinar en qué columna está el mayor número que comienza con el dígito 4.")
mat = []
fila = []
mayor = 0
pos = 0
for i in range(5):
    fila = []
    for j in range(3):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
for i in range(5):
    mayor = 0
    pos = 0
    for j in range(3):
        if mayor < mat[i][j] and mat[i][j]/10 == 4:
            mayor = mat[i][j]
            pos = j
print("!El numero mayor es %d y esta en la posicion %d ¡" % (mayor, pos))
#print(" Leer una matriz 4x4 entera y determinar en qué posiciones están los enteros terminados en 0.")
mat = []
fila = []
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(int(input("elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)


print (len(mat))
print (mat)
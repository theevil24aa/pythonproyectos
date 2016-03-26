print(" Leer una matriz 5x3 entera y determinar en qué columna está el menor número par.")
from Par import buscarpar
mat = []
fila = []
menor=0
for i in range(5):
    fila = []
    for j in range(3):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
for i in range(5):
    menor=0
    for j in range(3):
        if menor>mat[i][j]:
            menor=mat[i][j]
    print("el numero menor (%d) de la columna (%d) "%(menor,i+1))
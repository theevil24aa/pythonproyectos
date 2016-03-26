print(
    " Leer una matriz 4x3 entera, calcular la suma de los elementos de cada fila y determinar cuál es la fila que tiene la mayor suma.")
mat = []
fila = []
mayor = 0
sumfila = 0
posicionx = 0
for i in range(3):
    fila = []
    for j in range(4):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)

for i in range(3):
    for j in range(4):
        sumfila += mat[i][j]
        if sumfila > mayor:
            mayor = sumfila
            posicionx = i

print("la suma de la fila mayor es %d y esta en la posición [%d] " % (mayor, posicionx))

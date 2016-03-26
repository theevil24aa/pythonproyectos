print(". Leer una matriz 5x5 entera y determinar en qué fila está el mayor número terminado en 6.")
mat = []
fila = []
mayor = 0
total = 0
pos = 0
fun=0
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
for i in range(5):
    mayor = 0
    pos = 0
    for j in range(5):
        if mayor <= mat[i][j] and mat[i][j] % 10 == 6:
            mayor = mat[i][j]
            pos = j
            fun = mayor
    if mayor == 0 :
        print ("en este no tiene primo ni terminado en 6 :en la pocicion : ",pos)
    else:
        print("El numero mayor es %d en la pocicion %d" % (fun, pos))

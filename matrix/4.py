from primo import buscarprimo

print(" Leer una matriz 4x3 entera y determinar en qué posiciones exactas se encuentran los números primos.")
mat = []
fila = []
for i in range(3):
    fila = []
    for j in range(4):
        fila.append(int(input("elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
print("los numeros primos son : ")
for i in range(3):
    for j in range(4):
        if buscarprimo(mat[i][j]):
            print("el numero primo es %d y esta en la pocicion : fila %d columna %d" % (mat[i][j], i, j))

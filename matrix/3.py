from Par import buscarpar

print(" Leer una matriz 3x4 entera y determinar en qué posiciones exactas se encuentran los númerospares.")
mat = []
filamatris = []
filpar = 0
colpar = 0

for i in range(4):
    filamatris = []
    for j in range(3):
        filamatris.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(filamatris)

print("los numero par que digito son : ")
for i in range(4):
    for j in range(3):
        if buscarpar(mat[i][j]):
            print(mat[i][j], "y estan en la fila %d y la columna %d" % (i, j))

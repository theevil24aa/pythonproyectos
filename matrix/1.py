
mat = []                                                    # esta es la variable de la matris
filaMat = []                                                # esta es la variable de la columna momentania
mayorMat = -30000
filMatMay = 0
colMatMay = 0

print(" digite 16 numeros enteros")

for i in range(4):                                                              # este es el ciclo de la fila
    filaMat = []                                                                # Aca se limpia la variable
    for j in range(4):                                                          # este es el ciclo de la columna
        filaMat.append(int(input("Elemento[%d,%d]: " % ((i + 1), (j + 1)))))    # aca se añade moemntania mente los valores de una fila
    mat.append(filaMat)                                                         # en este se asigna en la matris la fila y haci ba bajando

for i in range(4):
    for j in range(4):
        if mat[i][j] > mayorMat:
            mayorMat = mat[i][j]
            filMatMay = i + 1
            colMatMay = j + 1

print("el numero mayor es : %d y se encuentra en la posicion (%d,%d)" % (mayorMat, filMatMay, colMatMay))

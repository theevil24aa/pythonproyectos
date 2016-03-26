print(" Leer una matriz 4x4 entera y determinar cuántas veces se repita en ella el número mayor.")
mat = []
filaMat = []
mayorMat = -30000
filMatMay = 0
colMatMay = 0
cont = 0

print(" digite 16 numeros enteros")

for i in range(4):
    filaMat = []
    for j in range(4):
        filaMat.append(int(input("Elemento[%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(filaMat)

for i in range(4):
    for j in range(4):
        if mat[i][j] > mayorMat:
            mayorMat = mat[i][j]
            filMatMay = i + 1
            colMatMay = j + 1
        if mat[i][j] == mayorMat:
            cont += 1
print("el numero mayor es : %d y se encuentra en la posicion (%d,%d)" % (mayorMat, filMatMay, colMatMay))
print("el numero mayor se repite  ", cont)

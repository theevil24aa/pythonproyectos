print(" Leer una matriz 4x4 entera y calcular el promedio de los números mayores de cada fila.")
mat = []
fila = []
mayor = []
mayorf = 0
fun=0
# ingreso de numeros
for i in range(4):
    fila = []
    for j in range(4):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
# calculo del mayor
for i in range(4):
    fun=0
    mayorf=0
    for j in range(4):
        if mayorf < mat[i][j]:
            mayorf = mat[i][j]
            fun = mayorf
    mayor.append(fun)
# el promedio de los mayores
print("los numero mayores de la filas son ")
fun = 0
for x in range(4):
    print("fila ", x + 1, " : ", mayor[x])
    fun += mayor[x]
promedio = (int(fun / 4))

print(" Leer una matriz 5x3 entera y determinar en qué fila está el mayor número primo.")
from primo import buscarprimo

mat = []
fila = []
mayor = []
mayorf = 0
fun = 0
pos = []
posi = 0
# ingreso de numeros
for i in range(5):
    fila = []
    for j in range(3):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
# calculo del mayor
for i in range(5):
    fun = 0
    mayorf = 0
    for j in range(3):
        if mayorf < mat[i][j]:
            if buscarprimo(mat[i][j]):
                mayorf = mat[i][j]
                fun = mayorf
                posi = j
            else:
                mayorf = 0
                posi = 0

    mayor.append(fun)
    pos.append(posi)

print("_____________________")
print("mayor --- ", mayor)
print("fila ---  ", pos)

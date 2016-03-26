print(" Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las matrices es también el mayor número primo de la otra matriz.")
from primo import buscarprimo
mat = []
fila = []
#               aca pide datos al usuario
print("--- la primera matris ==m1 ----")
for i in range(4):
    fila = []
    for j in range(5):
        fila.append(int(input("Elemento de m1 [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
print("--- la segunda matris ==m2 ----")
mat1 = []
for f in range(4):
    fila = []
    for g in range(5):
        fila.append(int(input("Elemento de m2 [%d,%d]: " % ((f + 1), (g + 1)))))
    mat1.append(fila)
#               aca se mira el primo
#               m1
prim = 0
mayor = 0
for i in range(4):
    for j in range(5):
        if buscarprimo(mat[i][j]):
            prim = mat[i][j]
            if mayor < prim:
                mayor = prim
#               m2
pri = 0
may = 0
for i in range(4):
    for j in range(5):
        if buscarprimo(mat1[i][j]):
            pri = mat[i][j]
            if may < pri:
                may = pri
# esta es la parte de la comparacion
if mayor == may:
    print("m1 es igual a m2")
    print(mayor," == ",may)
else:
    print("m1 no es igual a m2")
    print(mayor," != ",may)
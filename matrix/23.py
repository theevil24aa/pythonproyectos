print(
    " Leer dos matrices 4x5 enteras y determinar si el número mayor de una de las matrices es igual al número mayor de la otra matriz.")
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
# aca es donde se mira el numero mayor
mayor = 0
for i in range(4):
    for j in range(5):
        if mayor < mat[i][j]:
            mayor = mat[i][j]
may = 0
for f in range(4):
    for g in range(5):
        if may < mat1[f][g]:
            may = mat1[f][g]
# esta es la parte de la comparacion
if mayor == may:
    print("m1 es igual a m2")
    print(mayor," == ",may)
else:
    print("m1 no es igual a m2")
    print(mayor," != ",may)

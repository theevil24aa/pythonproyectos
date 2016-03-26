from primo import buscarprimo
print(". Leer dos matrices 4x5 enteras y determinar si el mayor número primo de una de las matrices también se encuentra en la otra matriz.")
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

prim = 0
mayor = 0
for e in range(4):
    for f in range(5):
        if buscarprimo(mat[e][f]):
            prim = mat[e][f]
            if mayor < prim:
                mayor = prim
                for i in range(4):
                    for j in range(5):
                        if mayor == mat1[i][j]:
                            print("el numero mayor del primo %d esta igual en la seguda matris en la ubicacion %d"%(mayor,j))

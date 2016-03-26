print(". Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella terminan en 34.")
mat=[]
fila=[]
for i in range(5):
    fila=[]
    for j in range(4):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
print("los numeros terminadpos en 34 es : ")
for i in range(5):
    for j in range(5):
        if mat[i][j]%100==34:
            print(j," >>> ",mat[i][j])

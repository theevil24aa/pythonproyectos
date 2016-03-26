print(" Leer una matriz 4x4 entera y determinar cuántos enteros terminados en 0 hay almacenados en ella.")
mat=[]
fila=[]
cont=0
for i in range(4):
    fila=[]
    for j in range(4):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
for i in range(4):
    for j in range(4):
        if (mat[i][j] % 10) == 0:
            cont=cont+1
print("hay %d terminados en 0 en los que puso"%cont)
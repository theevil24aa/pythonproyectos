print(" Leer dos matrices 4x5 enteras y determinar si el número mayor almacenado en la primera está en la segunda.")
mat=[]
fila=[]
for i in range(4):
    fila=[]
    for j in range(5):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
mat1=[]
fila1=[]
for i in range(4):
    fila=[]
    for j in range(5):
        fila1.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat1.append(fila)
mayor=()
for i in range(4):
    for j in range(5):
        if int(mat[i][j]) > int(mayor):
            mayor = int(mat[i][j])
for i in range(4):
    for j in range(5):
        if mayor == int(mat1[i][j]):
            print("El numero mayor es %d y es igual a %d de la segunda matris en la pocición [%d][%d]"%(mayor,mat1[i][j],i,j))
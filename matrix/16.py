print(" Leer una matriz 5x4 entera y determinar cuántos números almacenados en ella tienen un solo dígito.")
mat=[]
fila=[]
for i in range(5):
    fila=[]
    for j in range(4):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
print("los numeros de un digito son : ")
for i in range(5):
    for j in range(4):
        if len(str(mat[i][j]))==1:
            print("[%d][%d] >>> %d"%(i+1,j+1,mat[i][j]))
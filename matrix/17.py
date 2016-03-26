print(" Leer una matriz 5x4 entera y determinar cuántos múltiplos de 5 hay almacenados en ella.")
mat=[]
fila=[]
for i in range(5):
    fila=[]
    for j in range(4):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
print("los multiplos de 5 allados en la matris son : ")
for i in range(5):
    for j in range(4):
        if mat[i][j]%5==0:
            print("[%d][%d] >>> %d"%(i+1,j+1,mat[i][j]))
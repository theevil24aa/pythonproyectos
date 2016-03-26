print(" Leer una matriz 5x5 entera y determinar cuántos números almacenados en ella tienen mas de 3 dígitos.")
mat=[]
fila=[]
count=0
for i in range(5):
    fila=[]
    for j in range(5):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
print("los numero que tienen 3 digitos son : ")
for i in range(5):
    for j in range(5):
        if len(str(mat[i][j]))==3:
            print("[%d][%d] --- }}}==> %d"%(i+1,j+1,mat[i][j]))
            count+=1
print("En total son %d numeros de 3 digitos"%count)
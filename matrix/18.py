print(" Leer una matriz 5x5 entera y determinar en qué posición exacta se encuentra el mayor múltiplo de 8.")
mat=[]
fila=[]
mayor=0
may=[]
maypos=[]
posison=0
for i in range(5):
    fila=[]
    for j in range(5):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
for i in range(5):
    mayor=0
    for j in range(5):
        if mayor < mat[i][j] and mat[i][j]%8 == 0:
            mayor=mat[i][j]
            posison = j+1
    may.append(posison)
    maypos.append(mayor)

print("los numeros multiplos de 8 mayores son posision : ")
print("posicion : ",may)
print("numero : ",maypos)
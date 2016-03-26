print(" Leer dos matrices 4x5 enteras y determinar cuántos datos tienen en común.")
print("------------matris numero #1--------------- ")
mat1=[]
fila=[]
comun=[]
pos=[]
cont=0
for i in range(4):
    fila=[]
    for j in range(5):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat1.append(fila)

print("------------matris numero #2--------------- ")
mat=[]
fila=[]
for i in range(4):
    fila=[]
    for j in range(5):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
for i in range(4):
    for j in range(5):
        if mat[i][j] == mat1[i][j]:
            cont += 1
print("los tiene en comun ",cont)
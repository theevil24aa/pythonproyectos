print("Leer dos matrices 4x5 entera, luego leer un entero y determinar si cada uno de los elementos de una de las matrices es igual a cada uno de los elementos de la otra matriz multiplicado por el entero leído.")
print("------------matris numero #1--------------- ")
mat1=[]
fila=[]
comun=[]
pos=[]
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
numero=int(input("PON EL NUMERO ENTERO : "))
for i in range(4):
    for j in range(5):
        if mat[i][j]*numero == mat1[i][j]*numero:
            print("%d == %d"%(mat1[i][j], mat[i][j]))
        else:
            print("no son iguales")

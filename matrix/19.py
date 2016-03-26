print(". Leer dos matrices 4x5 entera y determinar si sus contenidos son exactamente iguales.")
print("------------matris numero #1--------------- ")
mat1=[]
fila=[]
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

if mat1==mat:
    print("matris #1")
    print(mat1)
    print("matris #2")
    print(mat)
    print("!SON INGUALES¡")
else:
    print("matris #1")
    print(mat1)
    print("matris #2")
    print(mat)
    print("no son iguales")
print(" Leer una matriz 3x4 entera y determinar cuántos de los números almacenados son primos y terminan en 3.")
from primo import buscarprimo

mat = []
fila = []
primosterminadosen3 = []
for i in range(4):
    fila = []
    for j in range(3):
        fila.append(int(input("Elemento [%d,%d]: " % ((i + 1), (j + 1)))))
    mat.append(fila)
print("Los numeros primos termindos en 3 son: ")

for i in range(4):
    for j in range(3):
        if mat[i][j] % 10 == 3 and buscarprimo(mat[i][j]):
            primosterminadosen3.append(mat[i][j])

print(primosterminadosen3)

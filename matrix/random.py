#poner numeros aleatorio en un digoto
import random

mat = []
fila = []
for i in range(4):
    fila = []
    for j in range(4):
        fila.append( random.randint(0,1000000) )
    mat.append(fila)


print (len(mat))
print (mat)


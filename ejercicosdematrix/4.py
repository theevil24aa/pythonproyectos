# Almacenar 50 elementos en un vector, elevar al cuadrado cada valor
# almacenado en el vector, almacenar el resultado en otro vector. Imprimir
# el vector original y el vector resultante.
import random
import math

mat = []
mat1 = []
for i in range(50):
    mat.append(random.randint(1, 100))
for i in range(50):
    mat1.append(math.pow(mat[i], 2))

print(mat)
print(mat1)

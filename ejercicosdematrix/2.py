# . Llenar dos vectores A y B de 15 elementos cada uno, sumar el elemento
# uno del vector A con el elemento 1 del vector B y así sucesivamente
# hasta el elemento 15, almacenar el resultado en un vector C e imprimir el
# vector resultante.
import random

A = []
B = []
C = []
for x in range(15):
    A.append(random.randint(0, 300))
for y in range(15):
    B.append(random.randint(0, 300))
for h in range(15):
    C.append(A[h] + B[h])
print("A : ", A)
print("B : ", B)
print("C : ", C)

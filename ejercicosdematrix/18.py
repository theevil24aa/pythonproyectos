# Dado un arreglo A de N elementos se desea generar tres arreglos que
# contenga los elementos negativos, cero y positivos del arreglo.
import random

A = []
ne = []
ce = []
poc = []
for j in range(100):
    A.append(random.randint(-300, 300))
for j in range(100):
    if A[j] < 0:
        ne.append(A[j])
    if A[j] == 0:
        ce.append(A[j])
    if A[j] > 0:
        poc.append(A[j])
print("negativos : ", ne)
print("ceros : ", ce)
print("pocitivos : ", poc)

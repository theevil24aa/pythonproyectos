# Dado un arreglo lineal de números, sumar separadamente los números
# pares y los números impares.
import random
import Par

arr = []
pares = 0
inpares = 0
for x in range(30):
    arr.append(random.randint(0, 100))
for j in range(30):
    if Par.buscarpar(arr[j]):
        pares += arr[j]

    else:
        inpares += arr[j]
print("pares : ", pares)
print("inpares : ", inpares)

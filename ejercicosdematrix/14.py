# Obtener dos arreglos tal que sus elementos sean los números pares y
# números impares del arreglo A de 10 elementos.
import Par
import random

num1 = []
par = []
inpar = []
for x in range(10):
    num1.append(random.randint(-300, 300))
for j in range(10):
    if Par.buscarpar(num1[j]):
        par.append(num1[j])
    else:
        inpar.append(num1[j])
print(par)
print(inpar)

#  Llenar un vector de 20 elementos, imprimir la posición y el valor del
#  elemento mayor almacenado en el vector. Suponga
#  que todos los elementos del vector son diferentes.
import random

may = 0
pos = 0
var = []
for x in range(20):
    var.append(int(random.randint(0, 100)))
for j in range(20):
    if var[j] > may:
        pos = j
        may = var
print("la pocicon del numero mayor es ", pos)
print(var)

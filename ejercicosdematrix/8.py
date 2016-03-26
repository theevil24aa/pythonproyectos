# Diseñe un algoritmo que lea un número cualquiera y lo busque en el
# vector X, el cual tiene almacenados 30 elementos. Escribir la posición
# donde se encuentra almacenado el número en el vector o el mensaje “No
# está” si no lo encuentra. Búsqueda secuencial.
import random

vec = []
poci = 0
for j in range(30):
    vec.append(random.randint(0, 100))
usr = int(input("pon un numero para buscar : "))
print(vec)
for k in range(30):
    if usr == vec[k]:
        poci = k
        print("el numero se encuentra en la pocicon ", poci)
        exit()
    else:
        print("el numero no esta")

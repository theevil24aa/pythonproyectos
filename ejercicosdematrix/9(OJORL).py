# Se tiene el vector A con 50 elementos almacenados. Diseñe un algoritmo
# que escriba “SI” si el vector esta ordenado ascendentemente o “NO” si
# el vector no está ordenado.

import random

mientras = 0
while mientras == 0:

    vec = []
    for i in range(50):
        vec.append(random.randint(0, 50))
    verdad = 0
    for j in range(50):
        aux = vec[j]
        if vec[j] < aux:
            verdad = 0
        else:
            verdad = 1

    if verdad == 0:
        print("si")
        mientras = 1
        print("---------------------", vec)
        exit()
    if verdad == 1:
        print("no")
        mientras = 0
        print(vec)

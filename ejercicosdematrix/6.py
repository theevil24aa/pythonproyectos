# Almacenar 25 números en un vector, almacenarlos en otro vector en
# orden inverso al vector original e imprimir el vector resultante.
import random

vector = []
inversion = []
ayuda = 25 - 1

for j in range(25):
    vector.append(random.randint(-300, 300))
print(vector)
while ayuda >= 0:
    inv = vector[ayuda]
    inversion.append(inv)
    ayuda -= 1

print(inversion)

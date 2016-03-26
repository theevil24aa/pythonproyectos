#!/bin/python3
# Almacenar 30 números en un vector, imprimir cuántos son negativos,
# cuántos son positivos, cuántos son ceros, además imprimir la suma de
# los negativos y la suma de los positivos.
import random

vec = []
suma = 0
pocitivo1 = []
negativo1 = []
for i in range(30):
    vec.append(random.randint(-300, 300))

print("----------negativo-----------")
for negativo in range(30):
    if vec[negativo] < 0 and vec[negativo] != 0:
        print(vec[negativo])

print("----------pocitivo-----------")
for pocitivo in range(30):
    if vec[pocitivo] > 0 and vec[pocitivo] != 0:
        print(vec[pocitivo])

print("----------la suma---------------")
# print("----------negativo-----------")
for negativo in range(30):
    if vec[negativo] < 0 and vec[negativo] != 0:
        negativo1.append(vec[negativo])

# print("----------pocitivo-----------")
for pocitivo in range(30):
    if vec[pocitivo] > 0 and vec[pocitivo] != 0:
        pocitivo1.append(vec[pocitivo])

for sumar in range(30):
    suma += vec[sumar]
print(suma)

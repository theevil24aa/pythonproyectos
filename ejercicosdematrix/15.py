# Elaborar un programa que lea 30 números y que imprima el número
# mayor, menor y el número de veces que se repiten ambos.
num1 = []
import random

for x in range(30):
    num1.append(random.randint(100, 1000))
may = 0
min = 100
cont1 = 0
cont = 0
for j in range(30):
    if may < num1[j]:
        may = num1[j]
    if min > num1[j] and num1 != 0:
        min = num1[j]

for j in range(30):
    if may == num1[j]:
        cont += 1
    if min == num1[j]:
        cont1 += 1

print("el numero mayor es %d y se repite %d veces" % (may, cont))

print("el numero menor es %d y se repite %d veces" % (min, cont1))

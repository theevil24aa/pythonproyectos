# . Se tienen 2 arreglos unidimensionales que guardan las edades de un
# grupo de personas, se pide hallar el mayor valor
import random

num1 = []
num2 = []
rango = random.randint(0, 100)
for j in range(rango):
    num1.append(random.randint(0, 100))
    num2.append(random.randint(0, 100))
may = 0
may1 = 0

id = 0
id1 = 0
for x in range(rango):
    if may < num1[x]:
        may = num1[x]
        id = x

    if may1 < num2[x]:
        may1 = num2[x]
        id1 = x

if may < may1:
    print("la persona  %d es la mayor con la edad de %d" % (id + 1, may1))
if may1 < may:
    print("la persona  %d es la mayor con la edad de %d" % (id1 + 1, may))

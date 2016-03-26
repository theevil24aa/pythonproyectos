# Se tienen almacenados dos vectores M y N de 50 elementos cada uno.
# Hacer un algoritmo que escriba la palabra “Iguales” si ambos vectores
# son iguales y “Diferentes” si no lo son. Serán iguales cuando en cada
# posición de los vectores se tenga el mismo valor.
import random

cont = 0
pausa = 0
while pausa == 0:
    num1 = []
    num2 = []
    for i in range(5):
        num1.append(random.randint(0, 5))
    print(num1)
    for j in range(5):
        num2.append(random.randint(0, 5))
    print(num2)
    if num1 == num2:
        print('iguales')
        pausa = 1

    else:
        print('diferentes')
    cont += 1
print("se repitio ", cont)

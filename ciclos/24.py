num = int(input("pon un numero : "))


def ciclo(num1):
    for x in range(1, num + 1):
        #print(num1)
        num1 += num1
    print("el resultado de los numeros pares son : ",num1)


for y in range(1, num):
    if y % 2 == 0:
        ciclo(num)

# print(num)
#numero de errores 2
#numero de defectos 6
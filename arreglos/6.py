print(" Leer dos números enteros y almacenar en un vector los 10 primeros números primos comprendidos entre el menor y el mayor. Luego mostrarlos en pantalla.")
num1 = int(input("pon el primer numero : "))
num2 = int(input("pon el segundo numero : "))
vec = []
if num1 > num2:
    for x in range(num2-1, num1 + 1):
        vec.append(x)
    for x1 in range(num2-1, num1 + 1):
        resul = vec[x1]
        print(resul)
if num2 > num1:
    for y in range(num1-1, num2 + 1):
        vec.append(y)

    for y1 in range(num1-1, num2 + 1):
        result1 = vec[y1]
        print(result1)

print(" Cargar un vector de 10 posiciones con los 10 primeros elementos de la serie de Fibonacci y mostrarlo en pantalla.")
temp = 0
num2 = 1
num1 = 0
fibo = []
for x in range(10):
    temp = num1 + num2
    fibo.append(temp)
    num1 = num2
    num2 = temp
for y in range(10):
    resul = fibo[y]
    print(resul)

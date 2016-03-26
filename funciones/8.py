print(
    "Construir una función que reciba como parámetro un entero y retorne 1 si dicho entero está entre los 30 primeros elementos de la serie de Fibonacci. Deberá retornar 0 si no es así.")
fibonacci = []
x = 0
y = 1
for n in range(30):
    fibonacci.append(x + y)
    fin = x + y
    aux = x + y
    x = y
    y = aux


def fibo(num1):
    for e in range(30):
        if num1 == fibonacci[e]:
            return 1
        else:
            return 0


usr = int(input("Pon un numero : "))
print(fibo(usr))
print(fibonacci)

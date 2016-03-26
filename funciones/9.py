print("Construir una función que reciba un entero y le calcule su factorial sabiendo que el factorial de")
print("un número es el resultado de multiplicar sucesivamente todos los enteros comprendidos entre")
print("1 y el número dado. El factorial de 0 es 1. No están definidos los factoriales de números")
print("negativos.")


def facetor(x):
    num = 0
    for j in range(1,x):
         num = j*x
    if num % 2 == 0:
        return num


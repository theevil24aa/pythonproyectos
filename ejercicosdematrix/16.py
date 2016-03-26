# Codifique un programa tal, que dado como entrada un arreglo
# unidimensional de enteros y un número entero, determine cuántas veces
# se encuentra este número dentro del arreglo.
import random


def repipetido(num1, x):
    conta = 0
    for x in range(100):
        if x == num1[x]:
            conta += 1
    return conta


if __name__ == "__main__":
    line = []

    num1 = random.randint(0, 100)
    for j in range(100):
        line.append(random.randint(0, 100))

    print("el numero se repite ", repipetido(line, num1))
    print(num1)
    print(line)

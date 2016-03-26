print("Construir una función que reciba como parámetro un entero y retorne la cantidad de dígitos.")


def funcion(num1):
    vec = len(str(num1))
    return vec


usr = int(input("pon un numero : "))
print(funcion(usr))

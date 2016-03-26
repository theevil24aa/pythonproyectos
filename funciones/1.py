print("Construir una función que reciba como parámetro un entero y retorne su último dígito.")


def resept(num1):
    num1 = num1 % 10
    return num1


usr = int(input("pon un numero de dos digitos : "))
print(resept(usr))

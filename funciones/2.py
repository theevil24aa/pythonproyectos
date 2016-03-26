print("Construir una función que reciba como parámetro un entero y retorne sus dos últimos dígitos.")


def funcion(num1):
    if len(str(num1)) == 3:
        num1 = int(num1)
        d = int(num1 % 10)
        c = int((num1 / 10) % 10)
        d = str(d)
        c = str(c)
        return c + d


usr = int(input("pon un numero : "))
print(funcion(usr))

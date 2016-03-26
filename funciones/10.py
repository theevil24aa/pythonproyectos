print(" Construir una función que reciba como parámetro un entero y retorne el primer dígito de este entero.")


def digito(num1):
    if len(str(num1)) == 2:
        return int(num1/10)
    if len(str(num1)) == 3:
        return int(num1/100)
    if len(str(num1)) == 4:
        return int(num1/1000)
    if len(str(num1)) == 5:
        return int(num1/10000)
    if len(str(num1)) == 6:
        return int(num1/100000)
    if len(str(num1)) == 7:
        return int(num1/1000000)
    if len(str(num1)) == 8:
        return int(num1/10000000)
    if len(str(num1)) == 9:
        return int(num1/100000000)
    if len(str(num1)) == 10:
        return int(num1/1000000000)
usr = int(input("pon un numero : "))
print(digito(usr))

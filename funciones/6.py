print("Construir una función que reciba como parámetro un entero y retorne el carácter al cual pertenece ese entero como código ASCII.")


def Ascc(x):
    return ord(x)

usr = int(input("pon un numero : "))
print("el valor en ASCII : "%Ascc(usr))

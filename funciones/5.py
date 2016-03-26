print("Construir una función que reciba como parámetro un entero y retorne la cantidad de dígitos primos.")


def buscarprimo(num):
    cont = 0
    for i in range(2, int(num / 2)):
        if num % i == 0:
            cont += 1
    if cont == 0:
        return True
    return False


def cantidad(x):
    cont = 0
    a = x / 10000
    b = (x % 10000) / 1000
    c = (x % 10000) % 1000 / 100
    d = ((x % 10000) % 1000) % 100 / 10
    e = (((x % 10000) % 1000) % 100) % 10
    if buscarprimo(a):
        cont += 1
    if buscarprimo(b):
        cont += 1
    if buscarprimo(c):
        cont += 1
    if buscarprimo(d):
        cont += 1
    if buscarprimo(e):
        cont += 1
    return cont


usr = int(input("Pon un numero : "))
print(cantidad(usr))
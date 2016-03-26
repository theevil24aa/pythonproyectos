print("Construir una función que reciba como parámetro un entero y retorne la cantidad de dígitos pares.")


def par(num1):
    if len(str(num1)) == 3:
        u = int(num1 / 10)
        d = int((num1 / 10) % 10)
        c = int(num1 % 10)
        if u % 2 == 0:
            return u
        if d % 2 == 0:
            return d
        if c % 2 == 0:
            return c
    if len(str(num1)) == 4:
        u = int(num1 / 10)
        d = int((num1 / 10) % 10)
        c = int((num1 / 100) % 10)
        um = int(num1 % 10)
        if u % 2 == 0:
            return u
        if d % 2 == 0:
            return d
        if c % 2 == 0:
            return c
        if um % 2 == 0:
            return um
    if len(str(num1)) == 5:
        u = int(num1 / 10)
        d = int((num1 / 10) % 10)
        c = int((num1 / 100) % 10)
        um = int((num1 / 1000) % 10)
        dm = int(num1 % 10)
        if u % 2 == 0:
            return u
        if d % 2 == 0:
            return d
        if c % 2 == 0:
            return c
        if um % 2 == 0:
            return um
        if dm % 2 == 0:
            return dm


usr = int(input("pon un numero : "))
print(par(usr))

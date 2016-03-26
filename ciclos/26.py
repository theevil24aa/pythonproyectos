verdad = 0
while (verdad == 0):
    num1 = int(input("pon un numero :"))
    u = int(num1 / 100)
    d = int((num1 / 10) % 10)
    c = int(num1 % 10)
    if u > d > c:
        print("el numero mayor es :", u)
    elif u > c > d:
        print("el numero mayor es :", u)
    elif d > c > u:
        print("el numero mayor es :", d)
    elif d > u > c:
        print("el numero mayor es :", d)
    elif c > u > d:
        print("el numero mayor es :", c)
    elif c > d > u:
        print("el numero mayor es :", c)
    exito = str(input("deseas salir? s/n "))
    if exito == "s":
        exit()

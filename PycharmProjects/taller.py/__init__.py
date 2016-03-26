#!/bin/python
import os
'''este es el taller
en el cual anexo los ejercicios hasta el 40'''
# os.system("")
os.system("clear")
print(" ==============================================================================")
print("|------------------------------------------------------------------------------|")
print("|------------------------------------------------------------------------------|")
print("|----------------EL-TALLER-ESTAN-LOS-EJERCICOS-DEL 1-AL-40---------------------|")
print("|--------------------PARA-SALIR-50---y-51-PARA-EL-CODIGO-----------------------|")
print("|----------------------------60-PARA-VER-LA-GUIA-------------------------------|")
print("|------------------------------------------------------------------------------|")
print("|------------------------------------------------------------------------------|")
print(" ==============================================================================")
user = int(input("}}}}}===========>  "))
if user == 1:  # numero 1
    os.system("clear")
    print("-------------numero 1-------------")
    print("_leer un numero y determinar si termia en 4")

    # CODE

    num1 = int(input("Pon un numero entero ==> "))
    # if num1>9 and num1<100:
    num1 = num1 % 10
    if num1 == 4:
        print("el numero termina en 4")
    else:
        print("el numero no termina en 4")
    # else:
    #	print("el numero no es de de dos digotos")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 2:  # numero 2
    os.system("clear")
    print("-------------numero 2---------------")
    print("_leer el numero entero y determinar si tene 3 digitos ")

    # CODE
    num1 = int(input("Pon un numero entero ==> "))
    if num1 >= 100 and num1 <= 999:
        print("El numero es de tres digitos")
    else:
        print("El numero no es de tres digitos")

    input("Presiona enter para continuar... ")

    os.system("python taller.py")

if user == 3:  # numero 3
    os.system("clear")
    print("-------------numero 3-------------")
    print("_leer un numero entero y determinar si es negativo")

    # CODE
    num1 = int(input("Pon el numero entero ==> "))
    if num1 >= -20000 and num1 <= -1:
        print("El numero es negativo")
    else:
        print("el numero no es negativo")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 4:  # numero 4
    os.system("clear")
    print("-------------numero 4-------------")
    print("Leer un número entero de dos dígitos y determinar a cuánto es igual la suma de sus dígitos.")

    # CODE
    num1 = int(input("Pon el numero ==>  "))
    num = int(num1 % 10)
    num1 = int(num1 / 10)
    print(num, " + ", num1)
    print("el resultado de la suma es  : ", num + num1)

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 5:  # numero 5
    os.system("clear")
    print("-------------numero 5-------------")
    print("Leer un número entero de dos dígitos y determinar si ambos dígitos son pares.")

    # CODE
    num1 = int(input("Pon un numero ==>"))
    u = int(num1 / 10)
    d = int(num1 % 10)
    if num1 % 2 == 0:
        print("el numero es par : ", num1)
    else:
        print("el numero es inpar")

    if u % 2 == 0:
        print("el digito es par : ", u)
    else:
        print("el numero es inpar", u)

    if d % 2 == 0:
        print("el digito es par : ", d)
    else:
        print("el numero es inpar", d)
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 6:  # numero 6
    os.system("clear")
    print("-------------numero 6-------------")
    print("Leer un número entero de dos dígitos menor que 20 y determinar si es primo.")

    # CODE
    numero = int(input("Pon un numero ==> "))
    if numero < 20:
        print("El numero es menor a 20")
        if (numero % 6) == 1:
            print("el numero completo es primo")
        else:
            print("el numero comleto no es primo")
    else:
        print("El numero es mayor a 20")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 7:  # numero 7
    os.system("clear")
    print("-------------#numero 7-------------")
    print("Leer un número entero de dos dígitos y determinar si es primo y además si es negativo.")

    # CODE
    num1 = int(input("Pon el numero ==> "))

    if (num1 % 6) == 1:
        print("el numero es primo")
    else:
        print("el numero no es primo")
        print(num1 % 6)
    if num1 < 0:
        print("el numero es negativo")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 8:  # numero 8 ############################################obligatorio
    os.system("clear")
    print("-------------numero 8-------------")
    print("Leer un número entero de dos dígitos y determinar si sus dos dígitos son primos.")

    # CODE
    numero = int(input("inserta un numero >> "))
    # unidad numero
    num1 = numero / 100
    num = numero % 10

    if (num1 % 6) == 1:
        print("el numero 1 es primo")
    else:
        print("el numero 1  no es primo")
    # decena numro

    if (num % 6) == 1:
        print("el numero 2 es primo")
    else:
        print("el numero 2 no es primo")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 9:  # numero 9
    os.system("clear")
    print("-------------numero 9-------------")
    print("Leer un número entero de dos dígitos y determinar si un dígito es múltiplo del otro.")

    # CODE
    num1 = int(input("Pon un Numero ===> "))
    num0 = int(num1 / 10)
    num2 = int(num1 % 10)
    resul = num0 * num2
    if resul % 2 == 1:
        print("el numero no es multiplo")
    if resul % 2 == 0:
        print("el numero es multiplo")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 10:  # numero 10
    os.system("clear")
    print("-------------numero 10-------------")
    print("Leer un número entero de dos dígitos y determinar si los dos dígitos son iguales.")

    # CODE
    num1 = int(input("Pon un numero ==> "))
    u = int(num1 / 10)
    d = int(num1 % 10)

    print(u, " = ", d)
    if d == u:
        print("Los numero son iguales")
    else:
        print("los numero no son iguales")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 11:  # numero 11
    os.system("clear")
    print("-------------numero 11-------------")
    print("Leer dos enteros y determinar cual es mayor")

    # CODE
    num1 = int(input("PON EL NUMERO 1: "))
    num2 = int(input("PON EL NUMERO 2: "))
    if num1 > num2:
        print("el numero es mayor", num1)
    else:
        if num1 < num2:
            print("el numero es mayor", num2)
        else:
            if num1 == num2:
                print("los numeros son iguales")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 12:  # numero 12
    os.system("clear")
    print("-------------numero 12-------------")
    print("Leer dos numero enteros de dos digitos y determinar si tiene numeros comunes")
    # CODE
    print(" ")
    usr = int(input("selecciona una obcion  1 la detallada 2 la simple : "))
    #														obcion detallada
    if usr == 1:
        num1 = int(input("Pon el primer numero de dos digitos ==> "))
        num2 = int(input("Pon el segundo numero de dos digitos ==> "))
        # variables de comparacion
        unum1 = int(num1 / 10)
        dnum1 = int(num1 % 10)
        unum2 = int(num2 / 10)
        dnum2 = int(num2 % 10)
        ##comparativa unidad1
        if unum1 == unum2:
            print("el digito de la unidad1 es igual a el digoto de la unidad del numero 2")
        if unum1 == dnum1:
            print("el digito de la unidad1 es igual a el digoto de la decena del numero 1")
        if unum1 == dnum2:
            print("el digito de la unidad1 es igual a el digoto de la decena del numero 2")
        ##comparativa unidad2
        if unum2 == unum1:
            print("el digito de la unidad2 es igual a el digoto de la unidad 2 del numero 1")
        if unum2 == dnum1:
            print("el digito de la unidad2 es igual a el digoto de la decena 1 del numero 1")
        if unum2 == dnum2:
            print("el digito de la unidad2 es igual a el digoto de la decena 2 del numero 2")
        ##comparativa decena1
        if dnum1 == unum2:
            print("el digito de la decena1 es igual a el digoto de la unidad 2 del numero 2")
        if dnum1 == unum1:
            print("el digito de la decena1 es igual a el digoto de la unidad 1 del numero 1")
        if dnum1 == dnum2:
            print("el digito de la decena1 es igual a el digoto de la decena 2 del numero 2")
        ##comparativa decena2
        if dnum2 == unum2:
            print("el digito de la decena2 es igual a el digoto de la unidad 2 del numero 2")
        if dnum2 == dnum1:
            print("el digito de la decena2 es igual a el digoto de la decena 2 del numero 1")
        if dnum2 == unum1:
            print("el digito de la decena2 es igual a el digoto de la unidad 1 del numero 2")
        else:
            print("no tiene numero en comun")
        #        																	obcion simple
    if usr == 2:
        num1 = int(input("Pon el primer numero de dos digitos ==> "))
        num2 = int(input("Pon el segundo numero de dos digitos ==> "))
        unum1 = int(num1 / 10)
        dnum1 = int(num1 % 10)
        unum2 = int(num2 / 10)
        dnum2 = int(num2 % 10)
        # unidad  numero 1								unidad numero 2									decenna1		   									decena2
        if (unum1 == unum2) or (unum1 == dnum1) or (unum1 == dnum2) or (unum2 == unum1) or (unum2 == dnum1) or ( unum2 == dnum2) or (dnum1 == unum2) or (dnum1 == unum1) or (dnum1 == dnum2) or (dnum2 == unum2) or (dnum2 == dnum1) or (dnum2 == unum2):
            print("hay numeros en comun")
        else:
            print("no hay numero es comun")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")
if user == 13:  # numero 13
    os.system("clear")
    print("-------------numero 13-------------")
    print("Leer dos numeros enteros de dos digitos y determinar si la suma de los dos numeros origina un par")
    # CODE
    num1 = int(input("Pon el primer numero entero de dos digitos ==>  "))
    num2 = int(input("Pon el segundo numero entero de dos digitos ==>  "))
    if (num1 >= 10 and num1 <= 99) and (num2 >= 10 and num2 <= 99):
        xnum = num1 + num2
        print("la suma es ", xnum)
        # numros inpares
        count = xnum % 2
        if count == 0:
            print("el numero es par")
        else:
            print("el umero es inpar")
    else:
        print("El numero no es de dos digitos")
    print("")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 14:  # numero 14
    os.system("clear")
    print("-------------numero 14-------------")
    print("leer dos numero enteros y determinar a cuanto es igual la suma de todos los digotos")

    # CODE
    num1 = int(input("Pon el Primer numero ==> "))
    num2 = int(input("Pon el segundo numero ==> "))
    unum1 = int(num1 / 10)
    dnum1 = int(num1 % 10)
    unum2 = int(num2 / 10)
    dnum2 = int(num2 % 10)
    print(num1, " ", num2)
    print("los digitos son ")
    print(unum1, ", ", dnum1, ", ", unum2, ", ", dnum2)
    print("La suma de los digotos son ")
    print(unum1 + dnum1 + unum2 + dnum2)

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 15:  # numero 15
    os.system("clear")
    print("-------------numero 15-------------")
    print("lee un numero entero de tres digitos y determinar a cuanto es la suma de los digitos")
    # CODE
    num1 = int(input("Pon el Primer numero ==> "))
    if num1 >= 100 and num1 <= 999:
        unum1 = int(num1 / 10)
        dnum1 = int((num1 / 10) % 10)
        cnum1 = int(num1 % 10)
        print("los digitos son ")
        print(unum1, ", ", dnum1, ", ", cnum1)
        print("La suma de los digotos son ")
        print(unum1 + dnum1 + cnum1)
    else:
        print("el numero no es de tres digitos")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 16:  # numero 16
    os.system("clear")
    print("-------------numero 16-------------")
    print("Leer un numero entero de tres digitos y determinar si almenos 2 de tres digotos son iguales")
    # CODE
    num1 = int(input("Pon un numero entero de tres digitos ==> "))
    u = int(num1 / 100)
    d = int((num1 / 10) % 10)
    c = int(num1 % 10)
    if u == d:
        print("el numero es igual ", u, " = ", d)
    else:
        print("el numero no es igual ", u, " != ", d)
        if u == c:
            print("el numero es igual ", u, " = ", c)
        else:
            print("el numero no es igual ", u, " != ", c)
            if d == u:
                print("el numero es igual ", d, " = ", u)
            else:
                print("el numero no es igual ", d, " != ", u)
                if d == c:
                    print("el numero es igual ", d, " = ", c)
                else:
                    print("el numero no es igual ", d, " != ", c)
                    if c == d:
                        print("el numero es igual ", c, " = ", d)
                    else:
                        print("el numero no es igual ", c, " != ", d)
                        if c == u:
                            print("el numero es igual ", c, " = ", u)
                        else:
                            print("el numero no es igual ", c, " != ", u)
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 17:  # numero 17
    os.system("clear")
    print("-------------numero 17-------------")
    print("leer un entero de tre digitos y determinar en que pocision esta el mayor digito")

    # CODE
    num1 = int(input("Pon un numero entero de tres digitos ==> "))
    u = int(num1 / 100)
    d = int((num1 / 10) % 10)
    c = int(num1 % 10)
    if u > d > c:
        print(u, " > ", d, " > ", c)
    if u > c > d:
        print(u, " > ", c, " > ", d)
    if d > c > u:
        print(d, " > ", c, " > ", u)
    if c > u > d:
        print(c, " > ", u, " > ", d)
    if c > d > u:
        print(c, " > ", d, " > ", u)

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 18:  # numero 18 ############################################obligatorio
    os.system("clear")
    print("-------------numero 18-------------")
    print("leer un numero de tres digotos y determinar si algun es multiplo de otros ")
    # CODE
    num1 = int(input("Pon un numero entero de tres digitos==> "))
    u = int(num1 / 100)
    d = int((num1 / 100) % 100)
    c = int(num1 % 100)
    comud = (u * d) % 2
    comuc = (u * c) % 2
    comcu = (c * u) % 2
    comcd = (c * d) % 2
    comdu = (d * u) % 2
    comdc = (d * c) % 2
    if comud == 0:
        print(u, " * ", d, " = ", u * d)
    # raise TypeError, "i debe ser del tipo int"
    if comuc == 0:
        print(u, " * ", c, " = ", u * c)
    # raise TypeError, "i debe ser del tipo int"
    if comcu == 0:
        print(c, " * ", u, " = ", c * u)
    # raise TypeError, "i debe ser del tipo int"
    if comdu == 0:
        print(d, " * ", u, " = ", d * u)
    # raise TypeError, "i debe ser del tipo int"
    if comdc == 0:
        print(d, " * ", c, " = ", d * u)
    # raise TypeError, "i debe ser del tipo int"
    # if :
    #	print ("no tiene multiplo en comun")


    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 19:  # numero 19
    os.system("clear")
    print("-------------numero 19-------------")
    print("leer tres numeros enteros y determinar cual es mayor solo dos variables")

    # CODE
    num = [0, 1, 2]
    num1 = int(input("pon un numero }}}==> "))
    num[0] = num1
    num1 = int(input("pon el segundo numero }}}==> "))
    num[1] = num1
    num1 = int(input("pon el tercer numero }}}==> "))
    num[2] = num1
    print("el numero 1: ", num[0], "el numero 2: ", num[1], "el numero 3: ", num[2])
    if num[0] > num[1] > num[2]:
        print("el mayor es el ", num[0])
    if num[0] > num[2] > num[1]:
        print("el numero mayor es ", num[0])
    if num[1] > num[2] > num[0]:
        print("el numero mayor es ", num[1])
    if num[1] > num[0] > num[2]:
        print("el numero mayor es", num[1])
    if num[2] > num[1] > num[0]:
        print("el numero mayor es ", num[2])
    if num[2] > num[0] > num[1]:
        print("el numero mayor es ", num[2])

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 20:  # numero 20
    os.system("clear")
    print("-------------numero 20-------------")
    print("leer tres numeros y mostrarlos acendientemente")
    # CODE
    num = [0, 1, 2]
    num1 = int(input("pon un numero }}}==> "))
    num[0] = num1
    num1 = int(input("pon el segundo numero }}}==> "))
    num[1] = num1
    num1 = int(input("pon el tercer numero }}}==> "))
    num[2] = num1
    print("el numero 1:", num[0], " el numero 2:", num[1], " el numero 3:", num[2])

    if num[0] > num[1] > num[2]:
        print(num[0], " > ", num[1], " > ", num[2])

    if num[0] > num[2] > num[1]:
        print(num[0], " > ", num[2], " > ", num[1])

    if num[1] > num[2] > num[0]:
        print(num[1], " > ", num[2], " > ", num[0])

    if num[1] > num[0] > num[2]:
        print(num[1], " > ", num[0], " > ", num[2])

    if num[2] > num[1] > num[0]:
        print(num[2], " > ", num[1], " > ", num[0])

    if num[2] > num[0] > num[1]:
        print(num[2], " > ", num[0], " > ", num[1])

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 21:  # numero 21
    os.system("clear")
    print("-------------numero 21-------------")
    print("leer un numero entero de dos digitos cada uno de ellos y determinar cual es el mayor digito")
    # CODE
    num1 = int(input("Pon el primer numero ==> "))
    num2 = int(input("Pon el segundo numero ==> "))
    u1 = int(num1 / 10)
    d1 = int(num1 % 10)
    u2 = int(num2 / 10)
    d2 = int(num2 % 10)
    #						u1
    if u1 > d1 > u2 > d2:
        print("el mayor digito es ", u1)
    if u1 > d1 > d2 > u2:
        print("el mayor digito es ", u1)
    if u1 > u2 > d1 > d2:
        print("el mayor digito es ", u1)
    if u1 > u2 > d2 > d1:
        print("el mayor digito es ", u1)
    if u1 > d2 > u2 > d1:
        print("el mayor digito es ", u1)
    if u1 > d2 > d1 > u2:
        print("el mayor digito es ", u1)
    # u2
    if u2 > u1 > d1 > d2:
        print("el mayor digito es ", u2)
    if u2 > u1 > d2 > d1:
        print("el mayor digito es ", u2)
    if u2 > d1 > u1 > d2:
        print("el mayor digito es ", u2)
    if u2 > d1 > d2 > d1:
        print("el mayor digito es ", u2)
    if u2 > d2 > d1 > u1:
        print("el mayor digito es ", u2)
    # d1
    if d1 > u1 > u2 > d2:
        print("el mayor digito es ", d1)
    if d1 > u1 > d2 > u2:
        print("el mayor digito es ", d1)
    if d1 > u2 > u1 > d2:
        print("el mayor digito es ", d1)
    if d1 > u2 > d2 > u1:
        print("el mayor digito es ", d1)
    if d1 > d2 > u2 > u1:
        print("el mayor digito es ", d1)
    if d1 > d2 > u1 > u2:
        print("el mayor digito es ", d1)
    # d2
    if d2 > u1 > u2 > d1:
        print("el mayor digito es ", d2)
    if d2 > u1 > d1 > u2:
        print("el mayor digito es ", d2)
    if d2 > u2 > u1 > d1:
        print("el mayor digito es ", d2)
    if d2 > d1 > u1 > u2:
        print("el mayor digito es ", d2)
    if d2 > d1 > u1 > u2:
        print("el mayor digito es ", d2)
    if d2 > d1 > u2 > u1:
        print("el mayor digito es ", d2)
    if num1 >= 100 and num1 <= 999 or num2 >= 100 and num2 <= 999:
        print("el numero es mayor de dos digitos")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 22:  # numero 22
    os.system("clear")
    print("-------------numero 22-------------")
    print("leer un entero de tres digitos y determinar si el primer digito es igual al ultimo")
    # CODE
    num1 = int(input("Pon un numero }}=====>"))
    uni = int(num1 / 100)
    cente = int(num1 % 10)
    if uni == cente:
        print("el numero ", uni, "es ingual a ", cente)
    else:
        print("los digitos no son iguales")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 23:  # numero 23
    os.system("clear")
    print("-------------numero 23-------------")
    print("leer un numero entero de tres digotos y determinar cuantos digotos tiene")
    # CODE
    num1 = int(input("Pon un numero ==> "))
    u = int(num1 / 10)
    d = int((num1 / 10) % 10)
    c = int(num1 % 10)
    if num1 >= 100 and num1 <= 999:
        print("el numero es de tres digitos", num1)
    elif num1 >= 0 and num1 <= 9:
        print("el numero es de un digito")
    elif num1 >= 1000 and num1 <= 9999:
        print("el numero es de 4 digitos")
    elif num1 >= 10000 and num1 <= 99999:
        print("el numero es de 5 digitos")
    elif num1 >= 100000 and num1 <= 999999:
        print("el numero es de 6 digitos")
    elif num1 >= 1000000 and num1 <= 9999999:
        print("el numero es de 7 digitos")
    elif num1 >= 10000000 and num1 <= 9999999:
        print("el numero es de 8 digitos")
    elif num1 >= 100000000 and num1 <= 99999999:
        print("el numero es de 9 digitos")
    elif num1 >= 1000000000 and num1 <= 9999999999:
        print("el numero es de 10 digitos")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 24:  # numero 24
    os.system("clear")
    print("-------------numero 24-------------")
    print("leer unumero entero de tres digitos y determinar cuantos digitos pares tiene")
    # CODE
    num1 = int(input("Pon un numero de tres digitos }}==>> "))
    u = int(num1 / 100)
    u1 = int(u % 2)
    d = int((num1 / 100) % 10)
    d2 = int(d % 2)
    c = int(num1 % 10)
    c3 = int(c % 2)
    if u1 == 0:
        print(u, " el numero es par")
    if d2 == 0:
        print(d, " el numero es par")
    if c3 == 0:
        print(c, " el numero es par")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 25:  # numero 25
    os.system("clear")
    print("-------------numero 25-------------")
    print("leer un numero entero de tres digitos y determinar si alguno de sus digitos es igual a la suma de los otros")
    # CODE
    num1 = int(input("Pon un numero }}==> "))
    u = int(num1 / 100)
    d = int((num1 / 10) % 10)
    c = int(num1 % 10)
    print(u, d, c)
    if u == (d + c):
        print("la suma de ", d, " +  ", c, " = ", u)
    if d == (u + c):
        print("la suma de ", u, " +  ", c, " = ", d)
    if c == (d + u):
        print("la suma de ", d, " +  ", u, " = ", c)

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 26:  # numero 26
    os.system("clear")
    print("-------------numero 26-------------")
    print("leer un numero entero de cuatro digitos y determinar a cuanto es igual la suma de sus digitos")
    # CODE
    num1 = int(input("Pon un numeor de 4 digitos ==> "))
    u = int(num1 % 10)
    d = int((num1 / 10) % 10)
    c = int((num1 / 100) % 10)
    um = int((num1 / 1000))
    if num1 >= 1000 and num1 <= 9999:
        print(u, " + ", d, " + ", d, " + ", c, " + ", um)
        print("la suma de sus digitos es ", u + d + c + um)

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 27:  # numero 27
    os.system("clear")
    print("-------------numero 27-------------")
    print("leer unn numero entero de cuatro digitos y determinar a cuanto es igual la suma de sus digitos")

    # CODE
    num1 = int(input("pon un numero de 4 digitos ==> "))
    u = int((num1 % 10))
    d = int(((num1 / 10) % 10))
    c = int(((num1 / 100) % 10))
    um = int((num1 / 1000))
    if num1 < 1000000000000000000:
        print(u + d + c + um)

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 28:  # numero 28 #############################################obligatorio
    os.system("clear")
    print("-------------numero 28-------------")
    print(" Leer un número entero menor que 50 y positivo y determinar si es un número primo.")
    # CODE
    num1 = int(input("pon un numero }}==> "))
    if num1 < 50 and num1 > 0:
        if (num1 % 6) == 1:
            print("el numero es pocitivo y ademas es un numero primo ", num1)

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 29:  # numero 29
    os.system("clear")
    print("-------------numero 29-------------")
    print(" Leer un número entero de cinco dígitos y determinar si es un número capicúo. Ej. 15651, 59895.")
    # CODE
    num1 = int(input("pon un numero }}==> "))
    u = str(int(num1 % 10))
    d = str(int((num1 / 10) % 10))
    c = str(int((num1 / 100) % 10))
    um = str(int((num1 / 1000) % 10))
    dm = str(int(num1 / 10000))
    # num1=str(num1)
    if (u + d + c + um + dm) == (dm + um + c + d + u):
        print(u + d + c + um + dm)
        print("el numero es capicuo ", num1)
    else:
        print("no es un numero capicuo ", u + d + c + um + dm)
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 30:  # numero 30
    os.system("clear")
    print("-------------numero 30-------------")
    print(" Leer un número entero de cuatro dígitos y determinar si el segundo dígito es igual al penúltimo.")
    # CODE
    num1 = int(input("pon un numero }}==> "))
    d = int(((num1 / 10) % 10))
    c = int(((num1 / 100) % 10))
    if c == d:
        print("el sugundo digito es igual al ultimo ")
    else:
        print("los digitos 2 y 3 no son iguales")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 31:  # numero 31
    os.system("clear")
    print("-------------numero 31-------------")
    print(" Leer un número entero y determina si es igual a 10.")

    # CODE
    num1 = int("pon un numero }}==> ")
    if num1 == 10:
        print("el numero es igual a 10")
    else:
        print("el numero no es igual a 10")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 32:  # numero 32
    os.system("clear")
    print("-------------numero 32-------------")
    print(" Leer un número entero y determinar si es múltiplo de 7.")
    # CODE
    num1 = int(input("pon un numero }}==> "))
    if (num1 % 7) == 0:
        print("el numero es multiplo de 7")
    else:
        print("el numero no es multiplo de 7")
    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 33:  # numero 33
    os.system("clear")
    print("-------------numero 33-------------")
    print(" Leer un número entero y determinar si termina en 7.")

    # CODE
    num1 = int(input("pon un numero }}==> "))
    num1 = num1 % 10
    if num1 == 7:
        print("el numero termina en 7")
    else:
        print("el numero no termina en 7")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 34:  # numero 34
    os.system("clear")
    print("-------------numero 34-------------")
    print(" Leer un número entero menor que mil y determinar cuántos dígitos tiene.")
    # CODE
    num1 = int(input("pon un numero }}==> "))
    if num1 < 1000:
        num1 = str(num1)
        print("el numero tene ", len(num1), " digitos.")

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 35:  # numero 35
    os.system("clear")
    print("-------------numero 35-------------")
    print(
        " Leer un número entero de dos dígitos, guardar cada dígito en una variable diferente y luego mostrarlas en pantalla.")

    # CODE
    num1 = int(input("pon un numero }}==> "))
    num2 = int(input("pon un numero }}==> "))
    print(num1)
    print(num2)

    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 36:  # numero 36
    os.system("clear")
    print("-------------numero 36-------------")
    print("")
    # CODE


    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 37:  # numero 37
    os.system("clear")
    print("-------------numero 37-------------")

    # CODE



    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 38:  # numero 38 ##############################################obligatorio
    os.system("clear")
    print("-------------numero 38-------------")

    # CODE


    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 39:  # numero 39
    os.system("clear")
    print("-------------numero 39-------------")

    # CODE


    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 40:  # numero 40
    os.system("clear")
    print("-------------numero 40-------------")

    # CODE


    input("Presiona enter para continuar... ")
    os.system("python taller.py")

if user == 50:  # Salir
    input("!Adios¡... ")
    os.system("clear")
    exit()
if user == 51:  # ver el codigo fuente
    userxit = input("emacs gedit vim o nano ==> ")
    if userxit == "emacs":
        os.system("emacs taller.py")
    if userxit == "gedit":
        os.system("gedit taller.py")
    if userxit == "vim":
        os.system("vim taller.py")
    if userxit == "nano":
        os.system("nano taller.py")
    #os.system("python taller.py")
if user == 60:  # libro
    os.system("okular /home/andres/Escritorio/EsenciaLogica.pdf")

os.system("clear")

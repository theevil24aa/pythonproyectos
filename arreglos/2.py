print("Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número par leído.")
##codigo copado de ejercicio 1
verdadero = 0
pocicion = 0
while verdadero == 0:
    vac = []
    maxim = 0

    for x in range(10):
        vac.append(int(input("el numero %d >> " % x)))

    for y in range(10):
         if y % 2 == 0:
            if vac[y] > maxim:
                maxim = vac[y]
                pocicion=y
    print("el numero par mayor es %d "%maxim)
    print("y esta en la pocicion %d"%pocicion)
    exite = input("DESEAS SALIR >> S/N : ")
    if exite == "s":
        verdadero = 1
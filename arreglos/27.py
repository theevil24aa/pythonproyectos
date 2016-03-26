print( " Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual el promedio entero de los factoriales de cada uno de los números leídos.")
vec = []
suma = 0
for x in range(1, 10 + 1):
    vec.append(int(input("%d >>> " % x)))
for y in range(10):
    suma += vec[y]
suma = int(suma / 10)
#suma = int(suma % 10)
print("el resultado de la suma es :", suma)

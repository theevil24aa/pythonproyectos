print(" Leer 10 números enteros, almacenarlos en un vector y determinar a cuánto es igual el promedio entero de los datos del vector.")
vec = []
for x in range(1,10+1):
    vec.append(int(input("%d >>> " % x)))
suma = 0
for y in range(1,10+1):
    suma += vec[y]
suma / 10
print("el promedio de los datos es %d" % suma)

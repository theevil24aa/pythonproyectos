print(" Leer 10 números enteros, almacenarlos en un vector y determinar cuántas veces está repetido el mayor.")
vec = []
repetido = 1
mayor = 0
pocicion = 0
numero = 1
for x in range(1,10+1):
    vec.append(int(input("%d >>> " % x)))

for y in range(1,10+1):
    if vec[y] > mayor:
        mayor = vec[y]
        if vec[y] == mayor:
            repetido += 1
print("el numero mayor es ", mayor, " y se repite ", repetido, "veces")

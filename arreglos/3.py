print("Leer 10 enteros, almacenarlos en un vector y determinar en qué posición del vector está el mayor número primo leído.")
##en que pocicion esta el prmo mayor leido
vec = []
maximo = 0

for x in range(1, 11):
    vec.append(int(input("pon el %d  >>" % x)))

for y in range(1, 11):
    if y % 6 == 0:
        if vec[y] > maximo:
            maximo = vec[y]
print("el numero primo mayor es %d" % maximo)

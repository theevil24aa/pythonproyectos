print(" Leer 10 números enteros, almacenarlos en un vector y mostrar en pantalla todos los enteros comprendidos entre 1 y cada uno de los números almacenados en el vector.")
vec = []

for x in range(1, 10 + 1):
    vec.append(int(input("%d >>> " % x)))
for y in range(10):
    print("--------",vec[y],"--------")
    for f in range(1,vec[y]+1):
        print (f)
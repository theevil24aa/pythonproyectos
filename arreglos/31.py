print(" Leer 10 números enteros, almacenarlos en un vector. Luego leer un entero y determinar cuantos divisores exactos tiene este último número entre los valores almacenados en el vector.")
vec = []
count=0
for x in range(1, 10 + 1):
    vec.append(int(input("%d >>> " % x)))
num1=int(input("pon el numero divisor  : "))
for y in range(10):
    for g in range(10):
        print ("---",g,"---")
        if vec[g]*num1==0:
            count+=1
    print(count)
# -------------
# como se hace?
# -------------
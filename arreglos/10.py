print(". Leer 10 números enteros, almacenarlos en un vector y determinar en qué posiciones se encuentran los números con mas de 3 dígitos.")
vec = []
for x in range(1,10+1):
    vec.append(int(input("%d >>> " % x)))
for y in range(1,10+1):
    if 100 <= vec[y] <= 999:
        print("los numeros de tres digitos ", vec[y], "y esta en la pocicion", y)

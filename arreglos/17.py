print(" Leer 10 números enteros, almacenarlos en un vector y determinar cuántos números negativos hay.")
vec = []
for x in range(1, 10 + 1):
    vec.append(int(input("%d >>> " % x)))
print("los numeros negativos son :")
count = 0
for i in range(10):
    if vec[i] < 0:
        count += 1
        print(vec[i],"en la pocicion ",i)
print("la cantidad de numeros negativos son : ", count)

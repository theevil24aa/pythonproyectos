print(" Leer 10 números enteros, almacenarlos en un vector y determinar en qué posición está el menor número primo.")
vec = []
maxim = 0
for x in range(1, 10 + 1):
    vec.append(int(input("%d >>> " % x)))
for i in range(10):
    for y in range(10):
        if maxim > vec[y]:
            maxim = vec[y]
print("el numero primo menor es :", maxim)

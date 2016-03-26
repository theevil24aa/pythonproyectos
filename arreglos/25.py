print(" Leer 10 números enteros, almacenarlos en un vector y determinar cuántos de los números leídos son números primos terminados en 3.")
vec = []
for x in range(1, 10 + 1):
    vec.append(int(input("%d >>> " % x)))
for y in range(10):
    if ((vec[y] % 6) == 0) and ((vec[y] % 10) == 3):
        print("el numero primo terminado en tres es :", vec[y])
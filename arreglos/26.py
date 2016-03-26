print(" Leer 10 números enteros, almacenarlos en un vector y calcularle el factorial a cada uno de los números leídos almacenándolos en otro vector.")
vec = []
facto = 1
for x in range(1, 10 + 1):
    vec.append(int(input("%d >>> " % x)))
for y in range(10):
    facto = facto * vec[y]

print("el factor de el numero es : ", facto)

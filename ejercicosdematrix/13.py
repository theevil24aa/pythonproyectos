# Una agencia administradora de inmuebles he decidido guardar en un
# arreglo lineal de N posiciones, los alquileres que cobran mensualmente a
# N viviendas que actualmente administran. En otro arreglo de igual
# número de posiciones guardan los porcentajes de ganancias por cada
# vivienda. Crear un nuevo arreglo con las ganancias por cada vivienda.
import random

rango = random.randint(100, 200)
mensualida = []
porcen = []
gananci = []
for men in range(rango):
    mensualida.append(random.randint(200, 500))
for por in range(rango):
    porcen.append(float(mensualida[por]) * 0.20)
for gan in range(rango):
    gananci.append(porcen[gan] * mensualida[gan])
print("mensualida ", mensualida, "000")
print("porcentaje ", porcen, "% ")
print("ganancias ", gananci, "$")

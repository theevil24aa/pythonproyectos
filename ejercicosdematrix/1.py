# Calcular el promedio de 10 valores almacenados en un vector.
# Determinar además cuantos son mayores que el promedio, imprimir el
# promedio, el número de datos mayores que el promedio y un listado de
# los valores que resultaron ser mayores al promedio.

suma = 0
arch = []
for i in range(10):
    arch.append(int(input("###>>> : ")))
# promedio
for j in range(10):
    suma += arch[j]
prom = (suma / 10)
print("el promedio es ", prom)

# mayor
mayor = []
mayo = 0
contador = 0
for k in range(10):
    mayo = 0
    if prom < arch[k]:
        mayo = arch[k]
        contador += 1
    if mayo != 0:
        mayor.append(mayo)
print("los mayores del promedio son : ", mayor)
print("el la cantidad de numeros mayores del promedio son  ", contador)

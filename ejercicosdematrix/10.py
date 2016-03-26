# Se tienen N empleados en una compañía y se ha ideado llenar un arreglo
# lineal A con los sueldos de los empleados, un arreglo B con las
# prestaciones totales de cada empleado, un arreglo C con las deducciones
# de cada uno. Crear un arreglo T que contenga el neto a pagar a cada
# empleado. (Neto a pagar = sueldo + prestaciones - deducciones)
import random

A = []  # sueldo
B = []  # prestaciones
C = []  # deducciones
T = []  # sudtotal
catidad = int(input("Cantidad de trabajadores : "))

for i in range(catidad):
    A.append(random.randint(650, 1000))
    B.append(random.randint(200, 500))
    C.append(random.randint(100, 500))
    T.append((A[i] + B[i]) - C[i])

for j in range(catidad):
    print("trabajador #", j + 1)
    print("Sueldo ", A[j], ".000")
    print("prestaciones ", B[j], ".000")
    print("deducciones ", C[j], ".000")
    print("TOTAL :: ", T[j], ".000")

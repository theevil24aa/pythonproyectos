veces = int(input("cuantas veces le liquidaron ? : "))
total = 0
for x in range(veces):
    sueldo = int(input("pon el venta # %d " % (veces + 1)))
    total = int(total + sueldo)
comision = int((total * 10) / 100)
print("esta son las ganancias : ", comision)
print("este es el total : ", total + comision)

# 2.Un vendedor recibe un sueldo base más un 10% extra por comisión
#  de sus ventas, el vendedor desea saber cuánto dinero obtendrá por
# concepto de comisiones por las tres ventas que realiza en el mes y el
#  total que recibirá en el mes tomando en cuenta su sueldo base y comisiones

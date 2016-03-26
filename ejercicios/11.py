x=int(input("pon el presupuesto del año : $"))
ginecologia = int((x*40)/100)
traumatologia = int((x*30)/100)
pediatria = int((x*30)/100)
print("el monto presupuestal es :")
print("ginecologia")
print("$",ginecologia)
print("------------")
print("traumatologia")
print("$",traumatologia)
print("------------")
print("pediatria")
print("$",pediatria)
print("------------")

#En un hospital existen tres áreas: Ginecología, Pediatría, Traumatología.
#El presupuesto anual del hospital se reparte conforme a la sig. tabla:
#Área
# Porcentaje del presupuesto
#Ginecología
# 40%
#Traumatología
# 30%
#Pediatría
# 30%
#Obtener la cantidad de dinero que recibirá cada área, para cualquier
#monto presupuestal.

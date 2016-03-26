#!/bin/python
print ("Escribe 2 numeros")
num1 = int(input("numero 1 ==> "))
num2 = int(input("numero 2 ==> "))
if (num1>=10 and num1<=99)and(num2>=10 and num2<=99):
	#sacando el primero
	u1 = num1/10
	u2 = num2/10
	#sacando el segundo
	d1 = num1%10
	d2 = num2%10
	if (((u1 == u2 or u1 == d1)and(u2 == d1 or u2 == d2)) and (d1==d2 ) ):
		print ("los numeros tienen en comun un numero")
	else:
		print ("no son comunes los numeros")

#	if (num1>=100 and num1<=999)and(num2>=100 and num2<=999):
#		#sacando el primero
#		du = num1/100
#		uu = num2/100
#		#sacando el segundo
#		dd = num1%10
#		ud = num2%10
#		#sacar el tercer numero
#		uc = (num1/10)%10
#		dc = (num2/10)%10
#		#comparativa del numero1    comparativa del numero2    comparativa del medio     comparativa del medio con el otro  compara tiva del uno con el del medio
#		if ((du == uu or du == uu)and(uu == ud and uu == dd) and( ((uc == dc and uc ==ud)and(dc == dd and dc == us)and(du == uc and uu == dc)) )):
#			print ("los numeros tienen en comun un numero")
#		else:
#			print ("no son comunes los numeros")
#	else:
#		print ("El numero es menor a 10 tiene que ser de dos cifras")

else:
	print ("El numero es menor a 10 tiene que ser de dos cifras")

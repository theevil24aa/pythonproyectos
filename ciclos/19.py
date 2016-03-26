true =0
while(true==0):
	user=int(input("Pon un numero: "))
	if ((user%6)==0):
		print("el numero es primo :",user)
	else:
		print("el numero no es primo")
	exit=input("deseas salir s/n ")
	if (exit=="s"):
		true=1	

#!/bin/python
verdadero=0
while(verdadero==0):
	num1=input("pon un numero: ")
	if (len(num1)==1):
		num1=int(num1)
		print(num1)
		print ("el numero es de un digito no se puede sumar")
	if (len(num1)==2):
		num1=int(num1)
		u=int(num1/10)
		d=int(num1%10)
		print(u,d)
		print ("la suma de los digitos es ",u+d)
	if (len(num1)==3):
		num1=int(num1)
		u=int(num1/10)
		d=int((num1/100)%10)
		c=int(num1%10)
		print(u,d,c)
		print ("la suma de los digitos es ",u+d+c)
	if (len(num1)==4):
		num1=int(num1)
		u=int(num1%10)
		d=int((num1/10)%10)
		c=int((num1/100)%10)
		um=int(num1/1000)
		print(u,d,c,um)
		print ("la suma de los digitos es ",u+d+c+um)



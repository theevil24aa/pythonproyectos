#!/bin/python 
import os
os.system("clear")
verdad=1
while(verdad==1):
	num1=int(input("pon un numero : "))

	numx=int(num1/100)
	numy=int((num1/10)%10)
	numz=int(num1%10)

	if (numx == 1):
		print("el primer digito es igual a 1")
	if (numy==1):
		print("el segundo digito es igual a 1")
	if (numz==1):
		print ("el terser digito es igual a 1")
	print("")

	exit=input("deseas salir s/n > ")

	if (exit=="s"):
		verdad=0

input("!adios¡...")
os.system("python __init__.py")
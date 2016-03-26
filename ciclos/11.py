#!/bin/python 
import os
os.system("clear")
num1=int(input("pon un numero : "))
numx = int(num1/10)
numy = int(num1%10)
print (numx," ",numy)

for x in range(numy,numx):
	print (x)

for y in range(numx,numy):
	print (y) 
input("!adios¡...")
os.system("python __init__.py")
#!/bin/python 
import os

os.system("clear")
numx = 0
for ciclo in range(1, 70):
    if (ciclo % 3) == 0:
        numx = int(numx + int(ciclo))
        print(numx)
        if (ciclo == 63):
            print("_____________")
            print("la suma de los multiplos de 3 es : ", numx)
            exit()
input("!adios¡...")
os.system("python __init__.py")

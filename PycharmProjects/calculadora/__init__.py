#!/bin/python3

#Author theevil24a
#systema  GNU/Linux i686
#version 1.0


import math


def suma(num1,num2):
    return num1+num2


def resta(num1,num2):
    return num1-num2


def multiplicasion(num1,num2):
    return num1*num2


def divicion(num1,num2):
    return num1/num2


def raiz(num1):
    return math.sqrt(num1)


while (True):
    usr = str(input("#  "))
    if usr[1] == '+':
        s = suma(int(usr[0]),int(usr[2]))
        print(s)
    if usr[1] == '-':
        r = resta(int(usr[0]),int(usr[2]))
        print(r)
    if usr[1] == '*':
        m = multiplicasion(int(usr[0]),int(usr[2]))
        print(m)
    if usr[1] == '/':
        d = divicion(int(usr[0]),int(usr[2]))
        print(d)
    if usr[1] == '°':
        ra = raiz(int(usr[0]))
        print(ra)
    if usr == 'salir':
        break
print("Adios")
print("author ='THEEVIL24A'")

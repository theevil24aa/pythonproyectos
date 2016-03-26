# Construir una función que reciba como parámetros dos números enteros y retorne el valor del mayor.
def mayor(num1,num2):
    if num1>num2:
        return num1
    else:
        if num1<num2:
            return num2
x=int(input("#-- = "))
j=int(input("#-- = "))
print(mayor(x,j))

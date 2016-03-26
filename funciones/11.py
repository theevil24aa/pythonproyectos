# Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si dicho
# entero es múltiplo de dicho dígito y 0 si no es así.
def multi(num1):
    if int(num1/num1)==1:
        return 1

    else:
        return 0
print(multi(int(input(" "))))

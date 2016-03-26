num=int(input("pon un numero: "))
num1=int(input("pon un numero :"))
print("el numero 1 es :",num," el numero 2 es :",num1)
if num<num1:
    for x in range(num,num1+1):
        print(x)
if num>num1:
    for y in range(num1,num+1):
        print (y)
if num==num1:
    print("los numeros son iguales")

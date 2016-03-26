num1=int(input("pon un numero :"))
num2=int(input("pon un numero :"))
if (num1>num2):
    for x in range (num2,num1):
        if (x%10)==4:
            print(x)
            #exit()
if (num2>num1):
    for y in range(num1,num2):
        if (y%10)==4:
            print(y)
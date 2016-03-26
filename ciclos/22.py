while True:
    num1=int(input('pon un numero de tres digitos : '))
    if 1 <= num1 <= 999:
        u=int(num1/100)
        d=int((num1/10)%10)
        c=int(num1%10)
        if u == 1:
            print("el primer digirto es igual a 1")
        if d == 1:
            print("el segundo digito es igual a 1")
        if c == 1:
            print ("el terser digito es igual al 1")
    else:
        print("el numero que deve digitar deve contener algindigito igual a 1")
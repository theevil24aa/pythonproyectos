xnum=int(input("pon un numero de tres digitos : "))
if xnum>=100 and xnum<=999:
    u=int(xnum/100)
    d=int((xnum/10)%10)
    c=int(xnum%10)
    print(u,d,c)
    for x in range(1,c+1):
        print("centena__ ",c)
    for y in range(1,d+1):
        print("decena__ ",d)
    for z in range(1,u+1):
        print("unidad__ ",u )


else:
    print("el numero no es de tres digitos")
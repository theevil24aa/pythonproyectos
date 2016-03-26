while(True):
    num=int(input("pon un numero : "))
    for x in range(1,num):
        num+=num
    print(num)
    if num%6==0:
        print ("la suma es primo ")
    else:
        print ("la suma  no es primo ")
# Construir una función que reciba como parámetro un entero y un dígito y retorne 1 si dicho
# dígito está en dicho entero y 0 si no es así.


def act(num1, cha):
    if num1==cha:
        return 1

    if len(str(num1))==2:
        x = int(num1 / 10)
        y = int(num1 % 10)
        if x == cha:
            return 1
        else:
            if y == cha:
                return 1
            else:
                return 0
    if len(str(num1))==3:
        x = int(num1 / 100)
        r = int((num1/100)%10)
        y = int(num1 % 10)
        if x == cha:
            return 1
        else :
            if y == cha:
                return 1
            else:
                if r == cha:
                    return 1
                else:
                    return 0
    if len(str(num1))==4:
        x = int(num1 / 1000)
        r = int((num1/1000)%10)
        rr = int((num1/1000)%10)
        y = int(num1 % 10)
        if x == cha:
            return 1
        else :
            if y == cha:
                return 1
            else:
                if r == cha:
                    return 1
                else:
                    if rr== cha:
                        return 1
                    else:
                        return 0
    if len(str(num1))==5:
        x = int(num1 / 10000)
        r = int((num1/10000)%10)
        rr = int((num1/10000)%10)
        rrr = int((num1/10000)%10)
        y = int(num1 % 10)
        if x == cha:
            return 1
        else :
            if y == cha:
                return 1
            else:
                if r == cha:
                    return 1
                else:
                    if rr== cha:
                        return 1
                    else:
                        if rrr==cha:
                            return 1
                        else:
                            return 0


j = int(input("#--= "))
x = int(input("#--= "))
print(act(j, x))
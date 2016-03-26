import random
import os


def numero_aleatorio(num1):
    num = 0
    for g in range(random.randint(0, 500)):
        for g in range(random.randint(0, 500)):
            for n in range(random.randint(0,num1)):
                os.system("clear")
                num = random.randint(1, 3)
                print("-----")
                print("|",num,"|")
                print("-----")
    return num


if __name__ == "__main__":

    print(numero_aleatorio(int(input("pon un numero : "))))

def buscarprimo(num):
    cont = 0
    for i in range(2, int(num / 2)):
        if num % i == 0:
            cont += 1
    if cont == 0:
        return True
    return False

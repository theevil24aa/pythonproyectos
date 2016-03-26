#. Hacer un algoritmo que llene una matriz de 10 * 10 y que almacene en la
# diagonal principal unos y en las demás posiciones ceros.


import random


def diagonal(x):
    dia=[]
    cero0=[]
    cero1=[]
    for c in range(10):
        dia.append(x[c][c])
        cero0.append(x[0][c])
        cero1.append(x[c][0])

    print("diagonal " ,dia)
    print("x ",cero0)
    print("y ",cero1)

if __name__=="__main__":
    fila=[]
    mat=[]
    for i in range(10):
        fila=[]
        for e in range(10):
            fila.append(random.randint(0,300))
        mat.append(fila)
    diagonal(mat)

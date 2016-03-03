from electrodomestico import Electrodomestico
from lavadora import Lavadora
from television import Television
if __name__=='__main__':

    listaelectrodomesticos = []

    e1 = Electrodomestico()
    e2 = Electrodomestico(120,50)
    e3 = Electrodomestico('negro', 'B', 300, 7)
    listaelectrodomesticos.append(e1)
    listaelectrodomesticos.append(e2)
    listaelectrodomesticos.append(e3)

    l1 = Lavadora()
    l2 = Lavadora(120,50)
    l3 = Lavadora('negro','B',300,7,50)
    listaelectrodomesticos.append(l1)
    listaelectrodomesticos.append(l2)
    listaelectrodomesticos.append(l3)

    t1 = Television()
    t2 = Television(120,50)
    t3 = Television('negro','B',300,7,50,True)
    listaelectrodomesticos.append(t1)
    listaelectrodomesticos.append(t2)
    listaelectrodomesticos.append(t3)

    totalelectroc = listaelectrodomesticos[0].calcularPresioFinal + listaelectrodomesticos[1].calcularPresioFinal + listaelectrodomesticos[2].calcularPresioFinal

    totallavadoras = listaelectrodomesticos[3].calcularPrecioFinallavadora + listaelectrodomesticos[4].calcularPrecioFinallavadora + listaelectrodomesticos[5].calcularPrecioFinallavadora

    totaltelevisores = listaelectrodomesticos[6].calcularPrecioFinalTv + listaelectrodomesticos[7].calcularPrecioFinalTv + listaelectrodomesticos[8].calcularPrecioFinalTv

    totalpresio = totallavadoras+totaltelevisores+totalelectroc

    print(totalpresio)
    print(totallavadoras)
    print(totaltelevisores)
    print(totalelectroc)




from electrodomestico import Electrodomestico


class Television(Electrodomestico):
    PULGADAS = 20
    TDT = False

    def __init__(self, *args):
        if len(args) == 0:
            super(Television, self).__init__(args)

            self.pulgadas = Television.PULGADAS
            self.tdt = Television.TDT

        elif len(args) == 2:
            super(Television, self).__init__(args[0], args[1])
            self.pulgadas = Television.PULGADAS
            self.tdt = Television.TDT
        elif len(args) == 6:
            super(Television, self).__init__(args[0], args[1], args[2], args[3])
            self.pulgadas = args[4]
            self.tdt = args[5]

    def getResolucion(self):
        return self.pulgadas

    def getTdt(self):
        return self.tdt

    def calcularPrecioFinalTv(self):
        precioElectrodomesticotv = self.calcularPresioFinal()
        if self.pulgadas >= 40:
            precioElectrodomesticotv += (precioElectrodomesticotv*0.30)
        if self.tdt:
            precioElectrodomesticotv += 50
        return precioElectrodomesticotv


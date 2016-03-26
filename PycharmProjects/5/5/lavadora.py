from electrodomestico import Electrodomestico


class Lavadora(Electrodomestico):
    CARGAS = 5

    def __init__(self, *args):
        if len(args) == 0:
            super(Lavadora, self).__init__(args)
            self.carga = Lavadora.CARGAS
        elif len(args) == 2:
            super(Lavadora, self).__init__(args[0], args[1])
            self.carga = Lavadora.CARGAS
        elif len(args) == 5:
            super(Lavadora, self).__init__(args[0], args[1], args[2],args[3])
            self.carga = args[4]

    def getCarga(self):
        return self.carga

    def calcularPrecioFinallavadora(self):
        Presiofinallavadora = self.calcularPresioFinal()
        if self.carga > 30:
            Presiofinallavadora += 50

        return Presiofinallavadora


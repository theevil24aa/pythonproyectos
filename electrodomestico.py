class Electrodomestico(object):
    COLOR = 'blanco'
    CONSUMO = 'f'
    PRESIO_BASE = 100
    PESO = 5
    LETRAS_CONSUMO = ("A", "B", "C", "D", "E", "F")
    LISTAS_COLOR = ("blanco", "negro", "rojo", "azul", "gris")

    def __init__(self,*args):
        if len(args) == 1:
            self.color = Electrodomestico.COLOR
            self.consumo = Electrodomestico.CONSUMO
            self.precio = Electrodomestico.PRESIO_BASE
            self.peso = Electrodomestico.PESO
        elif len(args) == 2:
            self.precio = args[0]
            self.peso = args[1]
            self.color = Electrodomestico.COLOR
            self.consumo = Electrodomestico.CONSUMO
        elif len(args) == 4:
            self.__comprobraColor(args[0])
            self.__comprobraConsumoEnergetico(args[1])
            self.precio = args[2]
            self.peso = args[3]

    def getColor(self):
        return self.color

    def getPeso(self):
        return self.peso

    def getConsumo(self):
        return self.consumo

    def getPresio(self):
        return self.precio

    def __comprobraConsumoEnergetico(self, letra):
        encontrado = False
        for i in range(len(Electrodomestico.LETRAS_CONSUMO)):
            if Electrodomestico.LETRAS_CONSUMO[i] == letra:
                encontrado = True
                break
        if encontrado:
            self.consumo = letra
        else:
            self.consumo = Electrodomestico.CONSUMO

    def __comprobraColor(self, color):
        encontrado = False
        for i in range(len(Electrodomestico.LISTAS_COLOR)):
            if Electrodomestico.LISTAS_COLOR[i] == color:
                encontrado = True
                break
        if encontrado:
            self.color = color
        else:
            self.color = Electrodomestico.CONSUMO

    def calcularPresioFinal(self):
        if self.consumo == 'A':
            self.precio += 100
        elif self.consumo == 'B':
            self.precio += 80
        elif self.consumo == 'C':
            self.precio += 60
        elif self.consumo == 'D':
            self.precio += 50
        elif self.consumo == 'E':
            self.precio += 30
        elif self.consumo == 'F':
            self.precio += 80
        if 0 <= self.peso <= 19:
            self.precio += 10
        elif 20 <= self.peso <= 49:
            self.precio += 50
        elif 50 <= self.peso <= 79:
            self.precio += 80
        elif self.peso >= 80:
            self.precio += 100

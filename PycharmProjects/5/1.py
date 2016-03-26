import datetime


# generamos la clase
class Hora():
    # variables de entorno
    ghoras = datetime.datetime.now()
    HORAS = 0
    MINUTOS = 0
    SEGUNDOS = 0

    # la funcion principal

    def __init__(self, *args):  # se piden los argumentos que el usuario mete
        if len(args) == 0:  # se ponen los valores por defecto si no manda
            self.hora = Hora.HORAS
            self.minutos = Hora.MINUTOS
            self.segundos = Hora.SEGUNDOS
        elif len(args) == 3:  # se ponen los valores que el usuario mando
            self.__Valida(args[0], args[1], args[2])

    def Leer(self, hora, minuto, segundo):
        self.__Valida(self.hora, self.minutos, self.segundos)

    def __Valida(self, hora, minutos, segundos):  # conpara si la ora es igual a la hora actual
        if 0 <= hora <= 23:
            self.hora = hora
        else:
            if hora < 0:
                self.hora = 0
            else:
                self.hora = 23

        if 0 <= minutos <= 59:
            self.minutos = minutos
        else:
            if minutos < 0:
                self.minutos = 0
            else:
                self.minutos = 59

        if 0 <= segundos <= 59:
            self.segundos = segundos
        else:
            if segundos < 0:
                self.segundos = 0
            else:
                self.segundos = 59

                # se calcua los segundos desde media noche

    def a_segundos(self):
        timenow = datetime.datetime.now()
        nowhora = timenow.hour * 60 * 60
        nowminutos = timenow.minute * 60
        nowsegundos = time.segundos
        hora = nowhora + nowminutos + nowsegundos
        print(hora, "segundos desde media noche")

    def de_segundos(self, *args):
        hora = int(args[0] / 3600)
        minuto = int((args[0] % 3600) / 60)
        segundos = int((args[0] % 3600) % 60)
        self.__Valida(hora, minuto, segundos)
        return "hora :", hora, " minuto:", minuto, " segundo:", segundos

    def segundos_desde(self, h, m, s):
        segundosclase = (self.hora * 3600) + (self.minutos * 60) + self.segundos
        segundosparametro = (h * 3600) + (m * 60) + (s)
        if segundosclase >= segundosparametro:
            return segundosclase - segundosparametro
        else:
            return segundosparametro - segundosclase

    def siguiente(self):
        if 0 < self.segundos < 59:
            self.segundos += 1
        else:
            self.segundos = 0

    def anterior(self):
        if 0 < self.segundos < 59:
            self.segundos -= 1
        else:
            self.segundos = 59

    def copia(self):
        hora = self.hora
        minuto = self.minutos
        segundo = self.segundos
        return hora, minuto, segundo

    def print(self):
        print("-----------------------------------")
        print(" hora:%d | minuto:%d | segundos:%d " % (self.hora, self.minutos, self.segundos))
        print("-----------------------------------")

    def igual_que(self, *args):
        if self.hora == args[0] and self.minutos == args[1] and self.segundos == args[2]:
            return True
        else:
            return False

    def menor_que(self, *args):
        if self.hora < args[0] and self.minutos < args[1] and self.segundos < args[2]:
            return True
        else:
            return False

    def mayor_que(self, *args):
        if self.hora > args[0] and self.minutos > args[1] and self.segundos > args[2]:
            return True
        else:
            return False


if __name__ == '__main__':
    print("\n")
    time = Hora(12, 32, 56)
    print("\n")
    time.a_segundos()
    print("\n")
    print(time.de_segundos(8000))
    print("\n")
    print(time.segundos_desde(12, 50, 30))
    print("\n")
    print(time.siguiente())
    print("\n")
    print(time.anterior())
    print("\n")
    print(time.copia())
    print("\n")
    time.print()
    print("\n")
    if time.igual_que(12, 45, 50):
        print("es igual")
    else:
        print("no es igual")
    print("\n")
    if time.menor_que(12, 45, 50):
        print("es menor")
    else:
        print("no es menor")
    print("\n")
    if time.mayor_que(12, 45, 50):
        print("es mayor")
    else:
        print("no es mayor")
    print("\n")

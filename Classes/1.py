"""1. Clase Hora
Crea una clase Hora con atributos para las horas, los minutos y los
segundos de la hora Incluye, al menos, los siguientes métodos:
Constructor predeterminado con el 00:00:00 como hora por defecto.
En el constructor se podrán indicar horas, minutos y segundos.
leer(): pedirá al usuario las horas, los minutos y los segundos.
valida(): comprobará si la hora es correcta; si no lo es la ajustará.
Será un método auxiliar (privado) que se llamará en el constructor
parametrizado y en leer().
a_segundos(): devolverá el número de segundos transcurridos desde
la medianoche.
de_segundos(int): hará que la hora sea la correspondiente a haber
transcurrido desde la medianoche los segundos que se indiquen.
segundos_desde(Hora): devolverá el número de segundos entre la
hora y la proporcionada.
siguiente(): pasará al segundo siguiente.
anterior(): pasará al segundo anterior.
copia(): devolverá un clon de la hora.
Además (métodos especiales):
print: mostrará la hora (07:03:21).
igual_que(Hora): indica si la hora es la misma que la proporcionada.
menor_que(Hora): indica si la hora es anterior a la proporcionada.
mayor_que(Hora): indica si la hora es posterior a la proporcionada.
Crea los tests correspondientes para demostrar que el programa
funciona bien.
"""

import time
class Hora(object):
    HORAS = 12
    MINUTOS = 35
    SEGUNDOS = 60

    def __init__(self):

    def leer(self, *args):
        """pedirá al usuario las horas, los minutos y los segundos."""
        self.horas = args[0]
        self.minutos = args[1]
        self.segundos = args[2]


    def valida(self):
        """comprobará si la hora es correcta; si no lo es la ajustará.
        Será un método auxiliar (privado) que se llamará en el constructor
        parametrizado y en leer()."""
        if (1 > self.horas < 12) and (1 > self.minustos < 60) and (1 > self.segundos < 60):
            return True

    def a_segundos(self):
        """devolverá el número de segundos transcurridos desde
        la medianoche."""
        medianoche = (12 * 60) * 60
        medianoche = medianoche - (self.horas * 60) * 60

    def de_segundos(self, int):
        """ devolverá el número de segundos entre la
        hora y la proporcionada."""

    def segundos_desde(self, hora):
        """devolverá el número de segundos entre la
        hora y la proporcionada."""

    def sigiente(self):
        """pasará al segundo siguiente."""

    def anterior(self):
        """pasará al segundo anterior."""

    def copia(self):
        """ devolverá un clon de la hora."""

    def print(self):
        """mostrará la hora (07:03:21)."""

    def igual_que(self, hora):
        """ indica si la hora es la misma que la proporcionada."""

    def menor_que(self, hora):
        """ indica si la hora es anterior a la proporcionada."""

    def mayor_que(self, hora):
        """indica si la hora es posterior a la proporcionada."""

"""
4. Haz una clase llamada Password que siga las siguientes condiciones:
Que tenga los atributos longitud y contraseña . Por defecto, la
longitud será de 8.
Los constructores serán los siguiente:
o
 Un constructor por defecto.
o
 Un constructor con la longitud que nosotros le pasemos. Generara
una contraseña aleatoria con esa longitud.
Los métodos que implementa serán:
o
 esFuerte(): devuelve un booleano si es fuerte o no, para que sea
fuerte debe tener mas de 2 mayúsculas, mas de 1 minúscula y
mas de 5 números.
o
 generarPassword(): genera la contraseña del objeto con la
longitud que tenga.
o
 Método get para contraseña y longitud.
o
 Método set para longitud.

"""
import random


# una funcion que me genera letras aleatoriamente




class Password():
    LONGITUD = 8
    CONTRASEÑA = ''

    def __init__(self, *args):
        if len(args) == 0:
            self.longitud = Password.LONGITUD
            self.contraseña = Password.CONTRASEÑA
        elif len(args) == 1:
            self.longitud = args[1]
            self.contraseña = Password.getContraseña(8)

    def esFuerte(self):
        if self.contraseña > 5 and self.contraseña >= 'A' and self.contraseña >= 'a':
            return True
        else:
            return False

    def LetraRandom(self,*args):
        a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        A = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        if args[0] == 1:
            return a[random.randint(1, 29)]
        if args[0] == 2:
            return A[random.randint(1, 29)]

    def generarPassword(self, longitud):
        a = []
        longitud = self.longitud
        for x in range(self.longitud):
            r = random.randint(0,3)
            if r == 0:
                a.append(Password.LetraRandom(1))
            if r == 1:
                a.append(Password.LetraRandom(2))
            if r == 2:
                a.append(random.randint(0,10))
        print(a)



    def getContraseña(self):
        return self.contraseña

    def getLongitud(self):
        return self.longitud

    def setLongitud(self,*args):
        self.longitud = args[0]

"""
Ahora, crea una clase clase ejecutable:
Crea un array de Passwords con el tamaño que tu le indiques por
teclado.
Crea un bucle que cree un objeto para cada posición del array.
Indica también por teclado la longitud de los Passwords (antes de
bucle).
Crea otro array de booleanos donde se almacene si el password del
array de Password es o no fuerte (usa el bucle anterior).
Al final, muestra la contraseña y si es o no fuerte (usa el bucle
anterior). Usa este simple formato:
contraseña1contraseña2valor_booleano1
valor_bololeano2
"""
if __name__ == '__main__':
    longitud=Password()
    longitud.setLongitud(8)
    longitud.generarPassword(8)
    longitud.LetraRandom(1)






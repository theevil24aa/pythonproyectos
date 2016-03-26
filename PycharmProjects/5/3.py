#!/bin/python
""" Haz una clase llamada Persona que siga las siguientes condiciones:
    Sus atributos son: nombre, edad, DNI, sexo (H hombre, M mujer),
    peso y altura. No queremos que se accedan directamente a ellos.
    Piensa que modificador de acceso es el más adecuado, también su
    tipo. Si quieres añadir algún atributo puedes hacerlo.
    Por defecto, todos los atributos menos el DNI serán valores por
    defecto según su tipo (0 números, cadena vacía para String, etc.).
    Sexo será hombre por defecto.
    Se implantaran varios constructores:
    o
    o
    Un constructor por defecto.
    Un constructor con el nombre, edad y sexo, el resto por defecto.
    o
     Un constructor con todos los atributos como parámetro.
    Los métodos que se implementaran son:
    o
     calcularIMC(): calculara si la persona esta en su peso ideal (peso
    en kg/(altura^2 en m)), devuelve un -1 si esta por debajo de su
    peso ideal, un 0 si esta en su peso ideal y un 1 si tiene
    sobrepeso .Te recomiendo que uses constantes para devolver
    estos valores.
    o
     esMayorDeEdad(): indica si es mayor de edad, devuelve un
    booleano.
    o
     comprobarSexo(char sexo): comprueba que el sexo introducido
    es correcto. Si no es correcto, sera H. No será visible al exterior.
    o
     toString(): devuelve toda la información del objeto.
    o
     generaDNI(): genera un numero aleatorio de 8 cifras, genera a
    partir de este su número su letra correspondiente. Este método
    será invocado cuando se construya el objeto. No será visible al
    exterior.
    o
     Métodos set de cada parámetro, excepto de DNI.
    ora, crea una clase ejecutable que haga lo siguiente:
    Pide por teclado el nombre, la edad, sexo, peso y altura.
    Crea 3 objetos de la clase anterior, el primer objeto obtendrá las
    anteriores variables pedidas por teclado, el segundo objeto obtendrá
    todos los anteriores menos el peso y la altura y el último por defecto,
    para este último utiliza los métodos set para darle a los atributos un
    valor.
    Para cada objeto, deberá comprobar si esta en su peso ideal, tiene
    sobrepeso o por debajo de su peso ideal con un mensaje.
    Indicar para cada objeto si es mayor de edad.
    Por último, mostrar la información de cada objeto.
    """
import random


class Persona():
    SEXO = ("H", "M")
    LETRA_DNI = (
    'T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E',)
    ##########################-metodo principal pone los datos-########################
    def __init__(self, *args):
        if len(args) == 0:
            self.nombre = ""
            self.edad = 0
            self.peso = 0
            self.altura = 0.0
            self.sexo = Persona.SEXO[0]
            self.dni = self.generarDNI()
        elif len(args) == 3:
            self.nombre = args[0]
            self.edad = args[1]
            self.sexo = args[2]
            self.peso = 0
            self.altura = 1
            self.dni = self.generarDNI()
        elif len(args) == 6:
            self.nombre = args[0]
            self.edad = args[1]
            self.sexo = args[2]
            self.peso = args[3]
            self.altura = args[4]
            self.dni = args[5]
    ##########################- aca se calcula el imc llamando self -########################
    def calcularImc(self):
        imc = self.peso / (self.altura ** 2)
        if imc < 18:
            return -1
        elif 18 < imc < 25:
            return 0
        else:
            return 1
    ##########################- aca si el mayor de edad -########################
    def esMayorDeEdad(self):
        if self.edad > 18:
            return True
        else:
            return False
    ##########################- aca simplemente mira si es hombre o mujor-########################
    def comprobarSexo(self, sexo):
        if sexo == Persona.SEXO[0] or sexo == Persona.SEXO[1]:
            return sexo
        else:
            return Persona.SEXO[0]


    ##########################- aca me presenta todo lo que contiene el objeto-########################
    def toString(self):
        return 'NOMBRE : %s \nEDAD: %d \nSEXO: %s \nPESO : %d \nESTATURA: %f\nDNI: %s' % (
        self.nombre, self.edad, self.sexo, self.peso, self.altura, self.dni)
    ##########################- esta es una mekina generadora del dni-########################
    def generarDNI(self):
        numDNI = random.randint(0, 99999999)
        resuduo = numDNI % 23
        letraDNI = Persona.LETRA_DNI[resuduo]
        return str(numDNI) + '-' + letraDNI

    ##########################- aca pone los caracteres que se van a usar-########################
    def setNombre(self, nombre):
        self.nombre = nombre

    def setEdad(self, edad):
        self.edad = edad

    def setSexo(self, sexo):
        self.sexo = sexo

    def setPeso(self, peso):
        self.peso = peso

    def setAltura(self, altura):
        self.altura = altura
    ##########################--------------########################    
    ##########################-MAIN-FUNCION-########################

if __name__ == '__main__':
    nombre = input("Pon Tu Nombre : ")
    edad = int(input("Pon Tu Edad : "))
    sexo = input("Pon Tu Sexo : H o M ")
    peso = int(input("Pon Tu Peso : "))
    altura = float(input("Pon Tu Altura En Metros : "))
    dni = input("pon tu dni :")
    p1 = Persona(nombre, edad, sexo, peso, altura, dni)
    p2 = Persona(nombre, edad, sexo)

    p3 = Persona()
    p3.setNombre("Wilson")
    p3.setPeso(105)
    p3.setAltura(1.70)

    ##########################persona1########################
    print(p1.toString())
    if p1.calcularImc() == -1:
        print("esta por debajo de su peso ideal ")
    elif p1.calcularImc() == 0:
        print("esta por debajo de su peso ideal ")
    else:
        print("esta en sobre peso")

    if p1.esMayorDeEdad():
        print("Es mayor de edad ")
    else:
        print("no es mayor de edad")

    ##########################persona2########################
    print(p2.toString())
    if p2.calcularImc() == -1:
        print("esta por debajo de su peso ideal ")
    elif p2.calcularImc() == 0:
        print("esta por debajo de su peso ideal ")
    else:
        print("esta en sobre peso")

    if p2.esMayorDeEdad():
        print("Es mayor de edad ")
    else:
        print("no es mayor de edad")

    ##########################persona3########################
    print(p3.toString())
    if p3.calcularImc() == -1:
        print("esta por debajo de su peso ideal ")
    elif p3.calcularImc() == 0:
        print("esta por debajo de su peso ideal ")
    else:
        print("esta en sobre peso")

    if p3.esMayorDeEdad():
        print("Es mayor de edad ")
    else:
        print("no es mayor de edad")

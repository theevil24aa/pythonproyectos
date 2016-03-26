"""
   6. Crearemos una clase llamada Serie con las siguientes características:
Sus atributos son titulo, numero de temporadas, entregado,
genero y creador.
Por defecto, el numero de temporadas es de 3 temporadas y
entregado false. El resto de atributos serán valores por defecto
según el tipo del atributo.
Los constructores que se implementaran serán:
o
 Un constructor por defecto.
o
 Un constructor con el titulo y creador. El resto por defecto.
o
 Un constructor con todos los atributos, excepto de entregado.
Los métodos que se implementara serán:
o
 Métodos get de todos los atributos, excepto de entregado.
o
 Métodos set de todos los atributos, excepto de entregado.
Crearemos una clase Videojuego con las siguientes características:
Sus atributos son titulo, horas estimadas, entregado, genero y
compañía.
Por defecto, las horas estimadas serán de 10 horas y entregado false.
El resto de atributos serán valores por defecto según el tipo del
atributo.
Los constructores que se implementaran serán:
o
 Un constructor por defecto.
o
 Un constructor con el titulo y horas estimadas. El resto por defecto.
o
 Un constructor con todos los atributos, excepto de entregado.
Los métodos que se implementara serán:
o
 Métodos get de todos los atributos, excepto de entregado.
o
 Métodos set de todos los atributos, excepto de entregado.
o
 entregar(): cambia el atributo prestado a true.
o
 devolver(): cambia el atributo prestado a false.
o
 isEntregado(): devuelve el estado del atributo prestado.
Ahora crea una aplicación ejecutable y realiza lo siguiente:
Crea dos arrays, uno de Series y otro de Videojuegos, de 5
posiciones cada uno.
Crea un objeto en cada posición del array, con los valores que desees,
puedes usar distintos constructores.
Entrega algunos Videojuegos y Series con el método entregar().
Cuenta cuantos Series y Videojuegos hay entregados. Al contarlos,
devuélvelos.
Por último, indica el Videojuego tiene más horas estimadas y la
serie con mas temporadas. Muéstralos en pantalla con toda su
información.

"""


class Serie():
    TITULO = 'titulo'
    NUMERO_DE_TEMPORADAS = 3
    ENTREGADO = False
    GENERO = 'genero'
    CREADOR = 'editor'

    def __init__(self, *args):
        if len(args) == 0:
            self.titulo = Serie.TITULO
            self.numero_de_temporadas = Serie.NUMERO_DE_TEMPORADAS
            self.entregado = Serie.ENTREGADO
            self.genero = Serie.GENERO
            self.creador = Serie.CREADOR
        if len(args) == 2:
            self.titulo = args[0]
            self.creador = args[1]
            self.numero_de_temporadas = Serie.NUMERO_DE_TEMPORADAS
            self.entregado = Serie.ENTREGADO
            self.genero = Serie.GENERO
        if len(args) == 4:
            self.titulo = args[0]
            self.creador = args[1]
            self.numero_de_temporadas = args[3]
            self.entregado = Serie.ENTREGADO
            self.genero = args[4]


            # Metodos Get

    def getTitulo(self):
        return self.titulo

    def getNumerot(self):
        return self.numero_de_temporadas

    def getEntregado(self):
        return self.ENTREGADO

    def getGenero(self):
        return self.genero

    def getCreador(self):
        return self.creador

        # Metodos set

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setNumerot(self, numero):
        self.numero_de_temporadas = numero

    def setEntregado(self, entregado):
        self.ENTREGADO = entregado

    def setGenero(self, genero):
        self.genero = genero

    def setCreador(self, creador):
        self.creador = creador


class videoJuegos():
    TITULOS = ''
    HORAS_ESTIMADAS = 0
    ENTREGADO = False
    GENERO = ''
    COMPAÑIA = ''

    def __init__(self, *args):
        if len(args) == 0:
            self.titulo = videoJuegos.TITULOS
            self.horas_estimadas = videoJuegos.HORAS_ESTIMADAS
            self.entregado = videoJuegos.ENTREGADO
            self.genero = videoJuegos.GENERO
            self.compañia = videoJuegos.COMPAÑIA
        if len(args) == 2:
            self.titulo = args[0]
            self.horas_estimadas = args[1]
            self.entregado = videoJuegos.ENTREGADO
            self.genero = videoJuegos.GENERO
            self.compañia = videoJuegos.COMPAÑIA
        if len(args) == 3:
            self.titulo = args[0]
            self.horas_estimadas = args[1]
            self.entregado = videoJuegos.ENTREGADO
            self.genero = args[2]
            self.compañia = args[3]
            # Metodos get

    def getTitulo(self):
        return self.titulo

    def getHoras(self):
        return self.horas_estimadas

    def getEntregado(self):
        return self.entregado

    def getGenero(self):
        return self.genero

    def getCompañia(self):
        return self.compañia
        # Metodos set

    def setCompañia(self, compañia):
        self.compañia = compañia

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setHoras(self, horas):
        self.horas_estimadas = horas

    def setEntregado(self, entregado):
        self.entregado = entregado

    def setGenero(self, genero):
        self.genero = genero

    def entregar(self):
        self.entregado = True

    def devolver(self):
        self.entregado = False

    def isdevolver(self):
        return self.entregado

    """Crea dos arrays, uno de Series y otro de Videojuegos, de 5
posiciones cada uno.
Crea un objeto en cada posición del array, con los valores que desees,
puedes usar distintos constructores.
Entrega algunos Videojuegos y Series con el método entregar().
Cuenta cuantos Series y Videojuegos hay entregados. Al contarlos,
devuélvelos.
Por último, indica el Videojuego tiene más horas estimadas y la
serie con mas temporadas. Muéstralos en pantalla con toda su
información.
"""


if __name__ == '__main__':
    a = Serie('mil y una noches', 12, 'bill gates', '50', 'Terror')
    b = Serie('El diablo esta resando III', 'Alvaro uribe')
    c = Serie('Devajo la misma estrella ', '#salariominimomensual', '8', 'nohayplata')
    d = Serie('Se nos robaron el aguita mijo !!', 'Los colombianos', '8', 'Terror')
    e = Serie()
    f = videoJuegos('civil war', 100, 'accion', 'Electronics arts')
    g = videoJuegos()
    h = videoJuegos('Diablo III', 45)
    i = videoJuegos('SlenderMan', 800, 'Terros', 'steam')
    j = videoJuegos('los perros de la esquina', 500, 'sexo', 'Ungry Americans')
    Series = [a, b, c, d, e]
    Videojuegos = [f, g, h, i, j]
    f.entregar()
    h.entregar()
    j.entregar()

    count = 0
    for x in range(5):
        if Series[x.getEntregado()] == True or Videojuegos[x.getEntregado()]:
            count += 1
    print("numero de entregadas : ", count)

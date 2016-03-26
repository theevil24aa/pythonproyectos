"""2. Clase Canción
Desarrolla una clase Canción con los siguientes atributos:
_titulo: una variable String que guarda el título de la canción.
_autor: una variable String que guarda el autor de la canción.
_duracion: tiempo en segundos de la canción.
y los siguientes métodos:
El constructor que recibe como parámetros el título y el autor de la
canción (por este orden)
dame_titulo(): devuelve el título de la canción.
dame_autor(): devuelve el autor de la canción.
pon_titulo(String): establece el título de la canción.
pon_autor(String): establece el autor de la canción.
"""


class Cancion():
    _TITULO = 'man soft the world'
    _AUTOR = 'Nirvana'
    _DURACION = 3.45

    def __init__(self, *args):
        if len(args) == 0:
            self._titulo = Cancion._TITULO
            self._autor = Cancion._AUTOR
        if len(args) == 2:
            self._titulo = args[0]
            self._autor = args[1]

    def dame_titulo(self):
        return self._titulo

    def dame_autor(self):
        return self._autor

    def pon_titulo(self, *args):
        self._titulo = args[0]

    def pon_autor(self, *args):
        self._autor = args[0]


if __name__=='__main__':
    c=Cancion()
    print(c.dame_titulo())
    print(c.dame_autor())
    c.pon_titulo("master of puppets")
    c.pon_autor("Matallica")
    print(c.dame_titulo())
    print(c.dame_autor())

#!/bin/python
#clases

class andtena():
	color=""
	longitud=""

class pelo():
	color=""
	textura=""

class ojo():
	forma=""
	color=""
	tamanio=""

class Objeto():
	color = ""
	tamanio = ""
	aspecto = ""
	antenas = Antena()
		 # propiedad compuesta por el objeto objeto Antena
	ojos = Ojo()
		 # propiedad compuesta por el objeto objeto Ojo
	pelos = Pelo()
		 # propiedad compuesta por el objeto objeto Pelo


class objeto ():
	"""docstring for ClassName"""
	color="verde"
	tamanio="grande"
	anrenas=antena()
	ojo= ojos()
	pelos=pelo()


	def flotar (self):
		pass
		
		
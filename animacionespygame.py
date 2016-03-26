#!/bin/python
import pygame,sys
from pygame.locals import*
from random import randint


pygame.init()

ventana = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Animacion")

mi_imagen = pygame.image.load("Imagenes/ov.png")

posX= 100
posY= 100

blanco=(255,255,255)
movimiento=True
velocidad=20
while True:
	ventana.fill(blanco)
	ventana.blit(mi_imagen,(posX,posY))
	#eventodecierre
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
	#eventodeanimacion
	if movimiento == True:
		if posX<700:
			posX+=velocidad
		else:
			movimiento=False
	else:
		if posX>1:
			posX-=velocidad
		else:
			movimiento=True

			

	pygame.display.update()	
#!/bin/python
import pygame,sys
from pygame.locals import*
from random import randint


pygame.init()

ventana = pygame.display.set_mode((1000,500))
pygame.display.set_caption("Animacion_teclas")

personaje = pygame.image.load("Imagenes/ov.png")

posX = 100
posY = 100

blanco = (255,255,255)
movimiento = True
velocidad = 20
while True:
	ventana.fill(blanco)
	ventana.blit(personaje,(posX,posY))

	#eventodecierre
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()
			#eventodeteclado
		else:
			if evento.type == pygame.KEYDOWN:
				if evento.key == K_LEFT:
					posX -= velocidad
				elif evento.key == K_RIGHT:
					posX += velocidad
				elif evento.type == pygame.KEYUP:#declaracion de teclas
					if evento.key == K_LEFT:
						print ("tecla isquerda")
					elif evento.key == K_RIGHT:
						print ("tecla derecha")
		
	pygame.display.update()	
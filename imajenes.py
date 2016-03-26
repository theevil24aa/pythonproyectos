#!/bin/python
import pygame,sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((800,507))
pygame.display.set_caption("Leonardo da vinchi")

mi_imagen = pygame.image.load("Imagenes/2f7fa25222b5b20a9f0f8c1a574ce139_l.jpg")
posX,posY=0,0

ventana.blit(mi_imagen,(posX,posY))

while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()	
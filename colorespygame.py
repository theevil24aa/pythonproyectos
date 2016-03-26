#!/bin/python
import pygame,sys
from pygame.locals import *

color = (0,140,60)
colordos = pygame.Color (255,120,9)


ventana = pygame.display.set_mode((400,300))
pygame.display.set_caption("coloresenpygame")

while True:
#	ventana.fill(color)
	ventana.fill(colordos)
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()	

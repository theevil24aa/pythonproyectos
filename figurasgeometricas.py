#!/bin/python
import pygame,sys
from pygame.locals import *

pygame.init()

ventana = pygame.display.set_mode((400,400))
pygame.display.set_caption("FigurasGeometricas")

pygame.draw.circle(ventana,(8,8,120),(300,300),40)
#pygame.draw.circle(ventana,(120,8,8),(120,120),40)
pygame.draw.rect(ventana,(130,70,70),(0,0,100,50))
#pygame.draw.circle(ventana,(8,120,8),(100,60),40)
pygame.draw.polygon(ventana,(90,100,70),((140,0),(291,106),(237,277),(56,277),(0,106)))

while True:
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()	
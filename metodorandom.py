#!/bin/python
import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((1000, 700))
pygame.display.set_caption("Metodo Random")

mi_imagen = pygame.image.load("Imagenes/ov.png")

posX = randint(10, 990)
posY = randint(10, 690)

ventana.blit(mi_imagen, (posX, posY))

while True:
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()

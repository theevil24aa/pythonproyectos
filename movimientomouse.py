#!/bin/python
import pygame, sys
from pygame.locals import *
from random import randint

pygame.init()

ventana = pygame.display.set_mode((1000, 500))
pygame.display.set_caption("Animacion_mouse")

personaje = pygame.image.load("Imagenes/ov.png")

posX = 100
posY = 100

blanco = (255, 255, 255)
movimiento = True
velocidad = 20
while True:
    ventana.fill(blanco)
    ventana.blit(personaje, (posX, posY))

    # eventodecierre
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        # evento de movimiento mouse
        posX, posY = pygame.mouse.get_pos()
        posX = posX - 100
        posY = posY - 50
        print(pygame.mouse.get_pos())
    pygame.display.update()

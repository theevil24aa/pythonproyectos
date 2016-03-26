#!/bin/python
import pygame,sys
from pygame.locals import *

pygame.init()
#colorbackgroud
colorback = pygame.Color(255,120,9)
#setbackground

Ventana = pygame.display.set_mode((300,300))
pygame.display.set_caption("drawinpygame")
#primera
print ("primeralinea")
Color = pygame.Color(80,70,140)
pygame.draw.line(Ventana,Color,(60,80),(160,100),8)
#print ("Red"+Color.r)
#print ("Green"+Color.g)
#print ("Blue"+Color.b)
#segunda
print ("segundalinea")
ColorDos = pygame.Color(80,0,0)
pygame.draw.line(Ventana,ColorDos,(10,20),(100,200),3)
#print ("Red"+ColorDos.r)
#print ("Green"+ColorDos.g)
#print ("Blue"ColorDos.b)
#tercara
print("terceralinea")
ColorTres = pygame.Color(50,100,140)
pygame.draw.line(Ventana,ColorTres,(40,40),(160,90),4)
#print ("Red"+ColorTres)
#print ("Green"+ColorTres.g)
#print ("Blue"+ColorTres.b)


while True:
#	Ventana.fill(Color)
#	Ventana.fill(ColorDos)
#	Ventana.fill(ColorTres)
	for evento in pygame.event.get():
		if evento.type == QUIT:
			pygame.quit()
			sys.exit()

	pygame.display.update()	
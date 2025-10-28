

import pygame
import sys
import math 

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 2 - Movimiento Circular")

COLOR_ROJO = (255, 0, 0)
COLOR_FONDO = (20, 20, 20)


cuadrado = pygame.Rect(0, 0, 30, 30)


CENTRO_X = 400
CENTRO_Y = 300
RADIO = 150 
angulo = 0

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
   
    x = CENTRO_X + RADIO * math.cos(angulo)
    y = CENTRO_Y + RADIO * math.sin(angulo)
    
    
    cuadrado.center = (x, y)
    

    angulo = angulo + 0.05 
    
    
    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, COLOR_ROJO, cuadrado)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
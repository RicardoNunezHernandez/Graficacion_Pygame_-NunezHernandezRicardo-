

import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 1 - Mover con Límites")

# Colores
COLOR_AZUL = (0, 0, 255)
COLOR_ROJO = (255, 0, 0)
COLOR_FONDO = (20, 20, 20)


color_actual = COLOR_AZUL


cuadrado = pygame.Rect(375, 275, 50, 50)


velocidad = 5

running = True
while running:
    
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
   
    teclas = pygame.key.get_pressed()
    
    if teclas[pygame.K_LEFT]:
        cuadrado.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        cuadrado.x += velocidad
    if teclas[pygame.K_UP]:
        cuadrado.y -= velocidad
    if teclas[pygame.K_DOWN]:
        cuadrado.y += velocidad
        
    
    if cuadrado.left < 0:
        cuadrado.left = 0
   
    if cuadrado.right > ANCHO:
        cuadrado.right = ANCHO

    if cuadrado.top < 0:
        cuadrado.top = 0
    
    if cuadrado.bottom > ALTO:
        cuadrado.bottom = ALTO
        

    if (cuadrado.left == 0 or cuadrado.right == ANCHO or
        cuadrado.top == 0 or cuadrado.bottom == ALTO):
        color_actual = COLOR_ROJO
    else:
       
        color_actual = COLOR_AZUL


    pantalla.fill(COLOR_FONDO)
    pygame.draw.rect(pantalla, color_actual, cuadrado)
    
    pygame.display.flip()
    
   
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
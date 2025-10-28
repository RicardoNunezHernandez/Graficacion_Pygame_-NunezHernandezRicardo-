

import pygame
import sys

pygame.init()

ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Proyecto 3 - Rastro")

# Colores
COLOR_CUADRADO = (0, 255, 0)
COLOR_RASTRO = (255, 0, 255) # Magenta
COLOR_FONDO = (20, 20, 20)


cuadrado = pygame.Rect(375, 275, 40, 40)
velocidad = 5


rastro = [] 

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
        
   
    rastro.append(cuadrado.center)
    
    
    pantalla.fill(COLOR_FONDO)
    
   
    for pos in rastro:
       
        pygame.draw.circle(pantalla, COLOR_RASTRO, pos, 3)
        
   
    pygame.draw.rect(pantalla, COLOR_CUADRADO, cuadrado)
    
    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
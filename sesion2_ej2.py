

import pygame
import sys

pygame.init()

ANCHO = 600
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Ejercicio 2 - Círculos Concéntricos")


CENTRO_X = ANCHO // 2
CENTRO_Y = ALTO // 2

# Colores
COLOR_FONDO = (0, 0, 0) # Fondo negro
COLOR_1 = (255, 0, 0)   # Rojo
COLOR_2 = (0, 255, 0)   # Verde
COLOR_3 = (0, 0, 255)   # Azul
COLOR_4 = (255, 255, 0) # Amarillo
COLOR_5 = (255, 0, 255) # Magenta


colores = [COLOR_1, COLOR_2, COLOR_3, COLOR_4, COLOR_5]

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Pintamos el fondo
    pantalla.fill(COLOR_FONDO)
    
   
    for i in range(5):
        
        radio = (i + 1) * 20
        
        
        color = colores[i]
        
        pygame.draw.circle(pantalla, color, [CENTRO_X, CENTRO_Y], radio, 5)

  
    pygame.display.flip()

pygame.quit()
sys.exit()
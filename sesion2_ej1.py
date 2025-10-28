

import pygame
import sys

pygame.init()


TAMANO_VENTANA = 400
pantalla = pygame.display.set_mode((TAMANO_VENTANA, TAMANO_VENTANA))
pygame.display.set_caption("Ejercicio 1 - Tablero de Ajedrez")

# Colores
COLOR_BLANCO = (255, 255, 255)
COLOR_NEGRO = (0, 0, 0)


TAMANO_CASILLA = 50

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
   
    for fila in range(8):
       
        for col in range(8):
            
           
            x = col * TAMANO_CASILLA
            y = fila * TAMANO_CASILLA
            
            
            if (fila + col) % 2 == 0:
                color = COLOR_BLANCO
            else: 
                color = COLOR_NEGRO
                
            
            pygame.draw.rect(pantalla, color, [x, y, TAMANO_CASILLA, TAMANO_CASILLA])

    
    pygame.display.flip()

pygame.quit()
sys.exit()
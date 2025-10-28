

import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mini Proyecto 1 - Cambiar Color")


COLOR_BLANCO = (255, 255, 255)
COLOR_AZUL = (0, 0, 255)


color_actual = COLOR_BLANCO

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_c:
                
                if color_actual == COLOR_BLANCO:
                    
                    color_actual = COLOR_AZUL
                else:
                    
                    color_actual = COLOR_BLANCO
    
    
    pantalla.fill(color_actual)
    
    pygame.display.flip()

pygame.quit()
sys.exit()
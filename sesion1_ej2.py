

import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Ejercicio 2 - Cerrar con ESC")

COLOR_FONDO = (30, 30, 30) 

running = True
while running:
    
   
    for event in pygame.event.get():
       
        if event.type == pygame.QUIT:
            running = False
            
       
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_ESCAPE:
                running = False
    
   
    pantalla.fill(COLOR_FONDO)
    
    
    pygame.display.flip()

pygame.quit()
sys.exit()
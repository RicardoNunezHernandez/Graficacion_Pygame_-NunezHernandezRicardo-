

import pygame
import sys

pygame.init()

pantalla = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mini Proyecto 2 - Casa")

# Colores
COLOR_FONDO = (135, 206, 235) # Azul cielo
COLOR_PASTO = (34, 139, 34)   # Verde
COLOR_TEJADO = (139, 69, 19)  # Marrón
COLOR_VENTANA = (255, 255, 0) # Amarillo


COLOR_ROJO = (255, 0, 0)
COLOR_AZUL = (0, 0, 255)


color_casa = COLOR_ROJO

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r: # Tecla R
                color_casa = COLOR_ROJO
            if event.key == pygame.K_b: # Tecla B
                color_casa = COLOR_AZUL
                
   
    pantalla.fill(COLOR_FONDO)
    
    pygame.draw.rect(pantalla, COLOR_PASTO, [0, 400, 600, 200])
    
    
    pygame.draw.rect(pantalla, color_casa, [200, 250, 200, 150])
    
    
    puntos_tejado = [[180, 250], [300, 150], [420, 250]]
    pygame.draw.polygon(pantalla, COLOR_TEJADO, puntos_tejado)
    
    
    pygame.draw.circle(pantalla, COLOR_VENTANA, [250, 320], 25)
    pygame.draw.circle(pantalla, COLOR_VENTANA, [350, 320], 25)
    
    pygame.display.flip()

pygame.quit()
sys.exit()